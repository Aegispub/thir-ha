# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-23 |
| **Generated At** | 2026-06-23T18:01:37Z |
| **Shift Time** | 18:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **423** |
| Confirmed Threats | **398** |
| False Positives Filtered | **25** (5.9%) |
| Unique Attacker IPs | **17** |
| Countries of Origin | **6** |
| High Severity Cases | **256** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **167** |
| Malware Samples Analyzed | **4** HIGH · **24** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **258** |
| Unique Credential Pairs | **250** |
| Unique Usernames | **132** |
| Unique Passwords | **199** |
| Successful Auth Pairs | **253** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 92 |
| `admin` | 10 |
| `ubuntu` | 8 |
| `test` | 5 |
| `git` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 17 |
| `1234` | 10 |
| `12345678` | 5 |
| `123` | 5 |
| `password` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 4 |
| `root` | `admin123` | 2 |
| `root` | `P@ssw0rd123` | 2 |
| `root` | `123456` | 2 |
| `root` | `123@@@` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `appuser` | `password` | `176.65.139.92` | 2026-06-23T14:55:06 |
| `test` | `qwerty123` | `176.65.139.92` | 2026-06-23T14:55:14 |
| `tactical` | `tactical` | `176.65.139.92` | 2026-06-23T14:55:20 |
| `solana` | `1234` | `176.65.139.92` | 2026-06-23T14:55:27 |
| `ubuntu` | `admin@123` | `176.65.139.92` | 2026-06-23T14:55:34 |
| `hd` | `123456` | `209.99.185.59` | 2026-06-23T14:55:38 |
| `rock` | `rock` | `176.65.139.92` | 2026-06-23T14:55:40 |
| `potok` | `potok` | `176.65.139.92` | 2026-06-23T14:55:47 |
| `rancher` | `rancher123` | `176.65.139.92` | 2026-06-23T14:55:52 |
| `gitlab` | `git` | `176.65.139.92` | 2026-06-23T14:55:58 |
| `bitrix` | `bitrix` | `176.65.139.92` | 2026-06-23T14:56:04 |
| `root` | `111111` | `176.65.139.92` | 2026-06-23T14:56:10 |
| `bot` | `123456` | `176.65.139.92` | 2026-06-23T14:56:17 |
| `nvidia` | `nvidia` | `176.65.139.92` | 2026-06-23T14:56:23 |
| `nagios` | `nagios` | `176.65.139.92` | 2026-06-23T14:56:29 |
| `git` | `1234` | `176.65.139.92` | 2026-06-23T14:56:36 |
| `sup` | `sup:` | `209.99.185.59` | 2026-06-23T14:56:39 |
| `root` | `admin123` | `176.65.139.92` | 2026-06-23T14:56:43 |
| `root` | `Password1` | `176.65.139.92` | 2026-06-23T14:56:50 |
| `admin1` | `modzmodz` | `176.65.139.92` | 2026-06-23T14:56:57 |
| `jakob` | `jakob` | `176.65.139.92` | 2026-06-23T14:57:04 |
| `sdadmin` | `51nGleD` | `176.65.139.92` | 2026-06-23T14:57:10 |
| `claude` | `password` | `176.65.139.92` | 2026-06-23T14:57:17 |
| `jack` | `1234` | `176.65.139.92` | 2026-06-23T14:57:24 |
| `webuser` | `webuser` | `176.65.139.92` | 2026-06-23T14:57:31 |
| `ranga` | `ranga` | `176.65.139.92` | 2026-06-23T14:57:39 |
| `svnuser` | `svnuser` | `209.99.185.59` | 2026-06-23T14:57:41 |
| `hamed` | `hamed` | `176.65.139.92` | 2026-06-23T14:57:46 |
| `vncuser` | `123456` | `176.65.139.92` | 2026-06-23T14:57:53 |
| `sam` | `1qaz@WSX` | `176.65.139.92` | 2026-06-23T14:57:59 |
| `root` | `test123` | `176.65.139.92` | 2026-06-23T14:58:06 |
| `teamspeak` | `1` | `176.65.139.92` | 2026-06-23T14:58:13 |
| `pi` | `1234` | `176.65.139.92` | 2026-06-23T14:58:19 |
| `ec2-user` | `12345678` | `176.65.139.92` | 2026-06-23T14:58:29 |
| `root` | `Aa112211..` | `176.65.139.92` | 2026-06-23T14:58:38 |
| `yjq` | `123456` | `209.99.185.59` | 2026-06-23T14:58:40 |
| `root` | `Password1234567890` | `45.205.1.42` | 2026-06-23T14:58:41 |
| `admin` | `111` | `176.65.139.92` | 2026-06-23T14:58:46 |
| `root` | `Password` | `176.65.139.92` | 2026-06-23T14:58:53 |
| `xiao` | `xiao` | `176.65.139.92` | 2026-06-23T14:59:00 |
| `wso2` | `wso2` | `176.65.139.92` | 2026-06-23T14:59:07 |
| `root` | `aA123456` | `176.65.139.92` | 2026-06-23T14:59:15 |
| `deployer` | `12345678` | `176.65.139.92` | 2026-06-23T14:59:22 |
| `root` | `Yun@wocloud.szkj` | `176.65.139.92` | 2026-06-23T14:59:30 |
| `centreon` | `centreon` | `176.65.139.92` | 2026-06-23T14:59:37 |
| `root` | `Manager` | `209.99.185.59` | 2026-06-23T14:59:39 |
| `ts` | `ts` | `176.65.139.92` | 2026-06-23T14:59:44 |
| `niaoyun` | `123456` | `176.65.139.92` | 2026-06-23T14:59:52 |
| `lucas` | `lucas` | `176.65.139.92` | 2026-06-23T14:59:59 |
| `server` | `123456` | `176.65.139.92` | 2026-06-23T15:00:06 |
| `openclaw` | `1234` | `176.65.139.92` | 2026-06-23T15:00:14 |
| `jenkins` | `jenkins@123` | `176.65.139.92` | 2026-06-23T15:00:21 |
| `ubuntu` | `Aa123456` | `176.65.139.92` | 2026-06-23T15:00:28 |
| `root` | `abc123456` | `176.65.139.92` | 2026-06-23T15:00:35 |
| `root` | `PASSWORD` | `209.99.185.59` | 2026-06-23T15:00:38 |
| `redhat` | `redhat` | `176.65.139.92` | 2026-06-23T15:00:42 |
| `root` | `a123456A` | `176.65.139.92` | 2026-06-23T15:00:48 |
| `test` | `test123` | `176.65.139.92` | 2026-06-23T15:00:55 |
| `developer` | `dev` | `176.65.139.92` | 2026-06-23T15:01:02 |
| `root` | `null` | `176.65.139.92` | 2026-06-23T15:01:09 |
| `jack` | `jack` | `176.65.139.92` | 2026-06-23T15:01:14 |
| `deployer` | `1234567890` | `176.65.139.92` | 2026-06-23T15:01:22 |
| `angel` | `angel` | `176.65.139.92` | 2026-06-23T15:01:28 |
| `alex` | `alex` | `176.65.139.92` | 2026-06-23T15:01:36 |
| `lighthouse` | `lighthouse` | `176.65.139.92` | 2026-06-23T15:01:43 |
| `uss` | `123456` | `209.99.185.59` | 2026-06-23T15:01:46 |
| `test` | `12345678` | `176.65.139.92` | 2026-06-23T15:01:51 |
| `root` | `Aa123321` | `176.65.139.92` | 2026-06-23T15:01:57 |
| `admin2` | `1234` | `176.65.139.92` | 2026-06-23T15:02:05 |
| `milad` | `milad` | `176.65.139.92` | 2026-06-23T15:02:13 |
| `splunk` | `splunk` | `176.65.139.92` | 2026-06-23T15:02:20 |
| `root1` | `root1` | `176.65.139.92` | 2026-06-23T15:02:28 |
| `arthur` | `arthur` | `176.65.139.92` | 2026-06-23T15:02:36 |
| `kafka` | `kafka` | `176.65.139.92` | 2026-06-23T15:02:43 |
| `wei2` | `panwei12` | `209.99.185.59` | 2026-06-23T15:02:47 |
| `prefect` | `prefect` | `176.65.139.92` | 2026-06-23T15:02:52 |
| `root` | `P@ssw0rd123` | `176.65.139.92` | 2026-06-23T15:02:59 |
| `user4` | `user4` | `176.65.139.92` | 2026-06-23T15:03:07 |
| `sam` | `1234` | `176.65.139.92` | 2026-06-23T15:03:14 |
| `ali` | `ali` | `176.65.139.92` | 2026-06-23T15:03:22 |
| `admin123` | `1234` | `176.65.139.92` | 2026-06-23T15:03:30 |
| `gateway` | `gateway` | `176.65.139.92` | 2026-06-23T15:03:38 |
| `bob` | `root` | `176.65.139.92` | 2026-06-23T15:03:45 |
| `skw` | `kevin2000A` | `209.99.185.59` | 2026-06-23T15:03:49 |
| `root` | `root12345` | `176.65.139.92` | 2026-06-23T15:03:52 |
| `user` | `123` | `176.65.139.92` | 2026-06-23T15:04:01 |
| `guest` | `111111` | `176.65.139.92` | 2026-06-23T15:04:09 |
| `user3` | `1` | `176.65.139.92` | 2026-06-23T15:04:24 |
| `master` | `qwerty` | `176.65.139.92` | 2026-06-23T15:04:31 |
| `root` | `qwertyuiop` | `176.65.139.92` | 2026-06-23T15:04:38 |
| `root` | `samantha` | `209.99.185.59` | 2026-06-23T15:04:50 |
| `root` | `0.123456789` | `209.99.185.59` | 2026-06-23T15:05:50 |
| `root` | `Zxcvbnm` | `209.99.185.59` | 2026-06-23T15:06:55 |
| `root` | `schalke04` | `209.99.185.59` | 2026-06-23T15:08:03 |
| `postgres` | `1q2w3e4r` | `209.99.185.59` | 2026-06-23T15:09:08 |
| `ubuntu` | `!qazXsw2` | `209.99.185.59` | 2026-06-23T15:10:10 |
| `justin` | `justin` | `209.99.185.59` | 2026-06-23T15:11:10 |
| `rudolfxx` | `roxanneluo` | `209.99.185.59` | 2026-06-23T15:12:18 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-06-23T15:12:42 |
| `root` | `123@@@` | `165.1.75.106` | 2026-06-23T15:12:42 |
| `root` | `Root@2019` | `209.99.185.59` | 2026-06-23T15:13:21 |
| `kaz` | `kaz` | `45.205.1.42` | 2026-06-23T15:13:27 |
| `root` | `forever` | `209.99.185.59` | 2026-06-23T15:14:24 |
| `jatin` | `jatin` | `209.99.185.59` | 2026-06-23T15:15:29 |
| `mqm` | `mqm` | `209.99.185.59` | 2026-06-23T15:16:38 |
| `user0` | `user0` | `209.99.185.59` | 2026-06-23T15:17:45 |
| `ftptest` | `123456` | `209.99.185.59` | 2026-06-23T15:18:52 |
| `lzh` | `lzh` | `209.99.185.59` | 2026-06-23T15:19:53 |
| `root` | `1qaz@WSX#EDC` | `209.99.185.59` | 2026-06-23T15:20:58 |
| `root` | `root@8888` | `209.99.185.59` | 2026-06-23T15:22:02 |
| `root` | `"+mDVt{%xnU9K/KG+"` | `209.99.185.59` | 2026-06-23T15:23:03 |
| `password` | `password` | `209.99.185.59` | 2026-06-23T15:24:06 |
| `root` | `a1s2` | `209.99.185.59` | 2026-06-23T15:25:09 |
| `jessica` | `jessica` | `209.99.185.59` | 2026-06-23T15:26:17 |
| `root` | `admin@1111` | `209.99.185.59` | 2026-06-23T15:27:25 |
| `root` | `P@ssw0rd12345` | `45.205.1.42` | 2026-06-23T15:28:25 |
| `root` | `P@ssword!@#` | `209.99.185.59` | 2026-06-23T15:28:28 |
| `intflow` | `intflow3121` | `209.99.185.59` | 2026-06-23T15:29:30 |
| `wxl` | `wxl584593403` | `209.99.185.59` | 2026-06-23T15:30:32 |
| `root` | `testing` | `209.99.185.59` | 2026-06-23T15:31:38 |
| `root` | `1999` | `209.99.185.59` | 2026-06-23T15:32:42 |
| `tangqian` | `tangqian123` | `209.99.185.59` | 2026-06-23T15:33:47 |
| `huawei` | `huawei12#$` | `209.99.185.59` | 2026-06-23T15:34:55 |
| `heinrich` | `heinrich` | `209.99.185.59` | 2026-06-23T15:36:01 |
| `postgres` | `test` | `209.99.185.59` | 2026-06-23T15:37:07 |
| `ubuntu` | `zaq12wsxcde3` | `209.99.185.59` | 2026-06-23T15:38:13 |
| `git` | `Git123` | `209.99.185.59` | 2026-06-23T15:39:19 |
| `operator` | `operator321` | `209.99.185.59` | 2026-06-23T15:40:25 |
| `hecj` | `a123456` | `209.99.185.59` | 2026-06-23T15:41:31 |
| `test` | `changeme` | `209.99.185.59` | 2026-06-23T15:42:37 |
| `root` | `zaq1XSW@` | `45.205.1.42` | 2026-06-23T15:43:01 |
| `user` | `2020` | `209.99.185.59` | 2026-06-23T15:43:40 |
| `root` | `root2007` | `209.99.185.59` | 2026-06-23T15:44:47 |
| `ubuntu` | `1qaz2wsx` | `209.99.185.59` | 2026-06-23T15:45:55 |
| `git` | `gitpassword` | `209.99.185.59` | 2026-06-23T15:47:04 |
| `ftpuser` | `1234567` | `209.99.185.59` | 2026-06-23T15:48:08 |
| `xuw` | `123xuw` | `209.99.185.59` | 2026-06-23T15:49:09 |
| `iexcel001` | `iexcel0011` | `209.99.185.59` | 2026-06-23T15:50:11 |
| `root` | `ubuntu` | `106.63.6.210` | 2026-06-23T15:50:56 |
| `git` | `passpass` | `209.99.185.59` | 2026-06-23T15:51:14 |
| `gpadmin` | `blabla123x!` | `209.99.185.59` | 2026-06-23T15:52:18 |
| `root` | `asd123!@#` | `209.99.185.59` | 2026-06-23T15:53:25 |
| `yanlei` | `yanlei` | `209.99.185.59` | 2026-06-23T15:54:20 |
| `geonho` | `1` | `209.99.185.59` | 2026-06-23T15:55:16 |
| `jxchen` | `123456` | `209.99.185.59` | 2026-06-23T15:56:17 |
| `zqf` | `zqf123` | `209.99.185.59` | 2026-06-23T15:57:13 |
| `test1` | `123456` | `45.205.1.42` | 2026-06-23T15:57:23 |
| `root` | `zxc123456` | `209.99.185.59` | 2026-06-23T15:58:10 |
| `dell` | `dell@6666` | `209.99.185.59` | 2026-06-23T15:59:13 |
| `root` | `q1w1e1a1s1d1z1x1c1` | `209.99.185.59` | 2026-06-23T16:00:12 |
| `ansible` | `1qaz2wsx` | `209.99.185.59` | 2026-06-23T16:00:57 |
| `yli` | `123456` | `209.99.185.59` | 2026-06-23T16:01:40 |
| `root` | `password123` | `209.99.185.59` | 2026-06-23T16:02:23 |
| `projects` | `projects` | `209.99.185.59` | 2026-06-23T16:03:08 |
| `hdoop` | `hdoop` | `209.99.185.59` | 2026-06-23T16:03:52 |
| `test` | `321123` | `209.99.185.59` | 2026-06-23T16:04:41 |
| `root` | `aaaAAA111` | `209.99.185.59` | 2026-06-23T16:05:32 |
| `pengqiwei` | `pengqiwei` | `209.99.185.59` | 2026-06-23T16:06:18 |
| `root` | `QWEasd?123!!` | `209.99.185.59` | 2026-06-23T16:07:06 |
| `root` | `antonio` | `209.99.185.59` | 2026-06-23T16:07:52 |
| `root` | `753951` | `209.99.185.59` | 2026-06-23T16:08:35 |
| `salav2` | `salav2` | `209.99.185.59` | 2026-06-23T16:09:18 |
| `qy` | `qy` | `209.99.185.59` | 2026-06-23T16:10:02 |
| `ubuntu` | `upload12345678` | `209.99.185.59` | 2026-06-23T16:10:50 |
| `root` | `1234rewq` | `45.205.1.42` | 2026-06-23T16:11:27 |
| `wangxiaoliang` | `wxl` | `209.99.185.59` | 2026-06-23T16:11:37 |
| `internet` | `internet` | `209.99.185.59` | 2026-06-23T16:12:29 |
| `root` | `SUGON@HPC123` | `209.99.185.59` | 2026-06-23T16:13:22 |
| `lee` | `123456` | `209.99.185.59` | 2026-06-23T16:14:10 |
| `potok` | `potok111111` | `209.99.185.59` | 2026-06-23T16:14:55 |
| `root` | `ad1d4s` | `209.99.185.59` | 2026-06-23T16:15:40 |
| `comercial` | `comercial` | `209.99.185.59` | 2026-06-23T16:16:28 |
| `root` | `Biaofeng!@998` | `209.99.185.59` | 2026-06-23T16:17:13 |
| `malu2019` | `woaimalu1020` | `209.99.185.59` | 2026-06-23T16:17:59 |
| `bvb` | `123456` | `209.99.185.59` | 2026-06-23T16:18:47 |
| `dell` | `Admin@1111` | `209.99.185.59` | 2026-06-23T16:19:36 |
| `root` | `q!w@e#` | `209.99.185.59` | 2026-06-23T16:20:23 |
| `james` | `12345` | `209.99.185.59` | 2026-06-23T16:21:07 |
| `kthrp` | `kthrp` | `209.99.185.59` | 2026-06-23T16:21:52 |
| `app` | `123qwe!@#` | `209.99.185.59` | 2026-06-23T16:22:39 |
| `root` | `2000` | `209.99.185.59` | 2026-06-23T16:23:26 |
| `shell` | `shell` | `209.99.185.59` | 2026-06-23T16:24:13 |
| `root` | `ssssss` | `209.99.185.59` | 2026-06-23T16:25:01 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-23T16:25:37 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-23T16:25:37 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-23T16:25:40 |
| `root` | `qhdidc@` | `45.205.1.42` | 2026-06-23T16:25:45 |
| `root` | `qwe12345^&` | `209.99.185.59` | 2026-06-23T16:25:52 |
| `root` | `123` | `91.92.40.6` | 2026-06-23T16:26:03 |
| `nginx` | `123` | `209.99.185.59` | 2026-06-23T16:26:41 |
| `root` | `1234` | `91.92.40.6` | 2026-06-23T16:27:15 |
| `root` | `987654` | `209.99.185.59` | 2026-06-23T16:27:27 |
| `co_come` | `co_come` | `209.99.185.59` | 2026-06-23T16:28:13 |
| `root` | `12345` | `91.92.40.6` | 2026-06-23T16:28:25 |
| `jiayuxin` | `JiaYuxin` | `209.99.185.59` | 2026-06-23T16:29:01 |
| `yuyi` | `Rxyz219021` | `209.99.185.59` | 2026-06-23T16:29:48 |
| `ubuntu` | `1a2b3c` | `209.99.185.59` | 2026-06-23T16:30:37 |
| `root` | `1234567` | `91.92.40.6` | 2026-06-23T16:30:47 |
| `root` | `1234QWERasdf` | `209.99.185.59` | 2026-06-23T16:31:26 |
| `root` | `12345678` | `91.92.40.6` | 2026-06-23T16:31:56 |
| `ac` | `123` | `209.99.185.59` | 2026-06-23T16:32:17 |
| `root` | `mnbvcx` | `209.99.185.59` | 2026-06-23T16:33:04 |
| `root` | `123456789` | `91.92.40.6` | 2026-06-23T16:33:15 |
| `user` | `User1234` | `209.99.185.59` | 2026-06-23T16:33:50 |
| `root` | `1234567890` | `91.92.40.6` | 2026-06-23T16:34:22 |
| `root` | `server` | `209.99.185.59` | 2026-06-23T16:34:38 |
| `root` | `123abc` | `91.92.40.6` | 2026-06-23T16:35:22 |
| `soomvi` | `soomvi` | `209.99.185.59` | 2026-06-23T16:35:28 |
| `hsj` | `korea2018` | `209.99.185.59` | 2026-06-23T16:36:16 |
| `root` | `1q2w3e4r` | `91.92.40.6` | 2026-06-23T16:36:21 |
| `user` | `123123` | `209.99.185.59` | 2026-06-23T16:37:03 |
| `root` | `P@ssw0rd123` | `91.92.40.6` | 2026-06-23T16:37:20 |
| `mormegil` | `quanquan` | `209.99.185.59` | 2026-06-23T16:37:52 |
| `root` | `abc123` | `91.92.40.6` | 2026-06-23T16:38:20 |
| `root` | `qaz2wsx` | `209.99.185.59` | 2026-06-23T16:38:41 |
| `root` | `admin123` | `91.92.40.6` | 2026-06-23T16:39:20 |
| `nagios` | `wasd` | `209.99.185.59` | 2026-06-23T16:39:28 |
| `ubuntu` | `ubuntuadmin` | `45.205.1.42` | 2026-06-23T16:39:52 |
| `root` | `Pass@word1!` | `209.99.185.59` | 2026-06-23T16:40:14 |
| `root` | `letmein` | `91.92.40.6` | 2026-06-23T16:40:20 |
| `wyx` | `123456` | `209.99.185.59` | 2026-06-23T16:41:01 |
| `root` | `pass123` | `91.92.40.6` | 2026-06-23T16:41:19 |
| `admin` | `abcd1234` | `209.99.185.59` | 2026-06-23T16:41:48 |
| `root` | `password` | `91.92.40.6` | 2026-06-23T16:42:18 |
| `root` | `admin!123` | `209.99.185.59` | 2026-06-23T16:42:36 |
| `root` | `password1` | `91.92.40.6` | 2026-06-23T16:43:18 |
| `yixuebu` | `yixuebu` | `209.99.185.59` | 2026-06-23T16:43:23 |
| `fanruan` | `fanruan123` | `209.99.185.59` | 2026-06-23T16:44:15 |
| `root` | `qwerty123` | `91.92.40.6` | 2026-06-23T16:44:16 |
| `dev` | `12345` | `209.99.185.59` | 2026-06-23T16:45:04 |
| `root` | `root123` | `91.92.40.6` | 2026-06-23T16:45:15 |
| `git` | `password123` | `209.99.185.59` | 2026-06-23T16:45:50 |
| `root` | `welcome` | `91.92.40.6` | 2026-06-23T16:46:14 |
| `ul` | `ul1` | `209.99.185.59` | 2026-06-23T16:46:36 |
| `admin` | `123` | `91.92.40.6` | 2026-06-23T16:47:16 |
| `ymxia` | `Pt2srkWXvC` | `209.99.185.59` | 2026-06-23T16:47:23 |
| `root` | `qaz!@#` | `209.99.185.59` | 2026-06-23T16:48:11 |
| `admin` | `1234` | `91.92.40.6` | 2026-06-23T16:48:15 |
| `root` | `admin88` | `209.99.185.59` | 2026-06-23T16:49:00 |
| `admin` | `12345` | `91.92.40.6` | 2026-06-23T16:49:14 |
| `easyits` | `easyits123` | `209.99.185.59` | 2026-06-23T16:49:50 |
| `admin` | `123456` | `91.92.40.6` | 2026-06-23T16:50:15 |
| `tomcat7` | `tomcat7` | `209.99.185.59` | 2026-06-23T16:50:44 |
| `admin` | `1234567` | `91.92.40.6` | 2026-06-23T16:51:23 |
| `user` | `Dan12MMA22cra` | `209.99.185.59` | 2026-06-23T16:51:41 |
| `admin` | `12345678` | `91.92.40.6` | 2026-06-23T16:52:27 |
| `bran` | `bran` | `209.99.185.59` | 2026-06-23T16:52:31 |
| `backup` | `backup@123` | `209.99.185.59` | 2026-06-23T16:53:20 |
| `admin` | `123456789` | `91.92.40.6` | 2026-06-23T16:53:24 |
| `webadmin` | `webadmin` | `45.205.1.42` | 2026-06-23T16:53:56 |
| `root` | `ske` | `209.99.185.59` | 2026-06-23T16:54:10 |
| `admin` | `1234567890` | `91.92.40.6` | 2026-06-23T16:54:22 |
| `yfhu` | `yfhu` | `209.99.185.59` | 2026-06-23T16:54:58 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **423** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 251 |
| libssh | 11 |
| Paramiko (Python) | 8 |
| OpenSSH | 5 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 140 | 2 |
| `0a07365cc01f...` | Generic scanner | 81 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 28 | 1 |
| `a2de0f306611...` | Mirai/variant | 8 | 2 |
| `a984ff804585...` | libssh-based | 5 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 140 | 2 | Generic scanner |
| `0a07365cc01f...` | Go SSH scanner | 81 | 1 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 28 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 27 | 1 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `91.92.40.6`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **17** |
| Unique ASNs | **13** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS215925` | VPSVAULT.HOST LTD | 1 | HIGH |
| `AS197170` | TechTies Inc. | 1 | HIGH |
| `AS213790` | Limited Network LTD | 1 | HIGH |
| `AS0` |  | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (256)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8422bf3fc28b

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:55 |
| **Last Seen** | 2026-06-23 14:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:55:06` | `cowrie.session.connect` |
| `2026-06-23 14:55:06` | `cowrie.client.version` |
| `2026-06-23 14:55:06` | `cowrie.client.kex` |
| `2026-06-23 14:55:06` | `cowrie.login.success` |
| `2026-06-23 14:55:08` | `cowrie.session.params` |
| `2026-06-23 14:55:08` | `cowrie.command.input` |
| `2026-06-23 14:55:08` | `cowrie.log.closed` |
| `2026-06-23 14:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f9c55d80941

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:55 |
| **Last Seen** | 2026-06-23 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:55:13` | `cowrie.session.connect` |
| `2026-06-23 14:55:13` | `cowrie.client.version` |
| `2026-06-23 14:55:13` | `cowrie.client.kex` |
| `2026-06-23 14:55:14` | `cowrie.login.success` |
| `2026-06-23 14:55:15` | `cowrie.session.params` |
| `2026-06-23 14:55:15` | `cowrie.command.input` |
| `2026-06-23 14:55:15` | `cowrie.log.closed` |
| `2026-06-23 14:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f4c184de513

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:55 |
| **Last Seen** | 2026-06-23 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:55:20` | `cowrie.session.connect` |
| `2026-06-23 14:55:20` | `cowrie.client.version` |
| `2026-06-23 14:55:20` | `cowrie.client.kex` |
| `2026-06-23 14:55:20` | `cowrie.login.success` |
| `2026-06-23 14:55:21` | `cowrie.session.params` |
| `2026-06-23 14:55:21` | `cowrie.command.input` |
| `2026-06-23 14:55:21` | `cowrie.log.closed` |
| `2026-06-23 14:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c6af67a1b95

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:55 |
| **Last Seen** | 2026-06-23 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:55:26` | `cowrie.session.connect` |
| `2026-06-23 14:55:26` | `cowrie.client.version` |
| `2026-06-23 14:55:26` | `cowrie.client.kex` |
| `2026-06-23 14:55:27` | `cowrie.login.success` |
| `2026-06-23 14:55:28` | `cowrie.session.params` |
| `2026-06-23 14:55:28` | `cowrie.command.input` |
| `2026-06-23 14:55:28` | `cowrie.log.closed` |
| `2026-06-23 14:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97c7df4e9e29

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:55 |
| **Last Seen** | 2026-06-23 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:55:33` | `cowrie.session.connect` |
| `2026-06-23 14:55:33` | `cowrie.client.version` |
| `2026-06-23 14:55:33` | `cowrie.client.kex` |
| `2026-06-23 14:55:34` | `cowrie.login.success` |
| `2026-06-23 14:55:34` | `cowrie.session.params` |
| `2026-06-23 14:55:34` | `cowrie.command.input` |
| `2026-06-23 14:55:35` | `cowrie.log.closed` |
| `2026-06-23 14:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cdcdde8f1e1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 14:55 |
| **Last Seen** | 2026-06-23 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:55:38` | `cowrie.session.connect` |
| `2026-06-23 14:55:38` | `cowrie.client.version` |
| `2026-06-23 14:55:38` | `cowrie.client.kex` |
| `2026-06-23 14:55:38` | `cowrie.login.success` |
| `2026-06-23 14:55:39` | `cowrie.session.params` |
| `2026-06-23 14:55:39` | `cowrie.command.input` |
| `2026-06-23 14:55:39` | `cowrie.log.closed` |
| `2026-06-23 14:55:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bac4d45de071

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:55 |
| **Last Seen** | 2026-06-23 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:55:40` | `cowrie.session.connect` |
| `2026-06-23 14:55:40` | `cowrie.client.version` |
| `2026-06-23 14:55:40` | `cowrie.client.kex` |
| `2026-06-23 14:55:40` | `cowrie.login.success` |
| `2026-06-23 14:55:41` | `cowrie.session.params` |
| `2026-06-23 14:55:41` | `cowrie.command.input` |
| `2026-06-23 14:55:41` | `cowrie.log.closed` |
| `2026-06-23 14:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39852e0d3e92

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:55 |
| **Last Seen** | 2026-06-23 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:55:46` | `cowrie.session.connect` |
| `2026-06-23 14:55:46` | `cowrie.client.version` |
| `2026-06-23 14:55:46` | `cowrie.client.kex` |
| `2026-06-23 14:55:47` | `cowrie.login.success` |
| `2026-06-23 14:55:48` | `cowrie.session.params` |
| `2026-06-23 14:55:48` | `cowrie.command.input` |
| `2026-06-23 14:55:48` | `cowrie.log.closed` |
| `2026-06-23 14:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05c893c5737a

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:55 |
| **Last Seen** | 2026-06-23 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:55:52` | `cowrie.session.connect` |
| `2026-06-23 14:55:52` | `cowrie.client.version` |
| `2026-06-23 14:55:52` | `cowrie.client.kex` |
| `2026-06-23 14:55:52` | `cowrie.login.success` |
| `2026-06-23 14:55:53` | `cowrie.session.params` |
| `2026-06-23 14:55:53` | `cowrie.command.input` |
| `2026-06-23 14:55:53` | `cowrie.log.closed` |
| `2026-06-23 14:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0bdf106589b

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:55 |
| **Last Seen** | 2026-06-23 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:55:58` | `cowrie.session.connect` |
| `2026-06-23 14:55:58` | `cowrie.client.version` |
| `2026-06-23 14:55:58` | `cowrie.client.kex` |
| `2026-06-23 14:55:58` | `cowrie.login.success` |
| `2026-06-23 14:55:59` | `cowrie.session.params` |
| `2026-06-23 14:55:59` | `cowrie.command.input` |
| `2026-06-23 14:55:59` | `cowrie.log.closed` |
| `2026-06-23 14:55:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-476f4ee3cc96

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:56 |
| **Last Seen** | 2026-06-23 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:56:03` | `cowrie.session.connect` |
| `2026-06-23 14:56:03` | `cowrie.client.version` |
| `2026-06-23 14:56:03` | `cowrie.client.kex` |
| `2026-06-23 14:56:04` | `cowrie.login.success` |
| `2026-06-23 14:56:04` | `cowrie.session.params` |
| `2026-06-23 14:56:04` | `cowrie.command.input` |
| `2026-06-23 14:56:05` | `cowrie.log.closed` |
| `2026-06-23 14:56:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59dad5221e52

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:56 |
| **Last Seen** | 2026-06-23 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:56:10` | `cowrie.session.connect` |
| `2026-06-23 14:56:10` | `cowrie.client.version` |
| `2026-06-23 14:56:10` | `cowrie.client.kex` |
| `2026-06-23 14:56:10` | `cowrie.login.success` |
| `2026-06-23 14:56:11` | `cowrie.session.params` |
| `2026-06-23 14:56:11` | `cowrie.command.input` |
| `2026-06-23 14:56:11` | `cowrie.log.closed` |
| `2026-06-23 14:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-263b45e0921e

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:56 |
| **Last Seen** | 2026-06-23 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:56:16` | `cowrie.session.connect` |
| `2026-06-23 14:56:16` | `cowrie.client.version` |
| `2026-06-23 14:56:16` | `cowrie.client.kex` |
| `2026-06-23 14:56:17` | `cowrie.login.success` |
| `2026-06-23 14:56:17` | `cowrie.session.params` |
| `2026-06-23 14:56:17` | `cowrie.command.input` |
| `2026-06-23 14:56:18` | `cowrie.log.closed` |
| `2026-06-23 14:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcd87235f84f

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:56 |
| **Last Seen** | 2026-06-23 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:56:23` | `cowrie.session.connect` |
| `2026-06-23 14:56:23` | `cowrie.client.version` |
| `2026-06-23 14:56:23` | `cowrie.client.kex` |
| `2026-06-23 14:56:23` | `cowrie.login.success` |
| `2026-06-23 14:56:24` | `cowrie.session.params` |
| `2026-06-23 14:56:24` | `cowrie.command.input` |
| `2026-06-23 14:56:24` | `cowrie.log.closed` |
| `2026-06-23 14:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67ff3eed43c6

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:56 |
| **Last Seen** | 2026-06-23 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:56:29` | `cowrie.session.connect` |
| `2026-06-23 14:56:29` | `cowrie.client.version` |
| `2026-06-23 14:56:29` | `cowrie.client.kex` |
| `2026-06-23 14:56:29` | `cowrie.login.success` |
| `2026-06-23 14:56:31` | `cowrie.session.params` |
| `2026-06-23 14:56:31` | `cowrie.command.input` |
| `2026-06-23 14:56:31` | `cowrie.log.closed` |
| `2026-06-23 14:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-197de6acc38b

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:56 |
| **Last Seen** | 2026-06-23 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:56:36` | `cowrie.session.connect` |
| `2026-06-23 14:56:36` | `cowrie.client.version` |
| `2026-06-23 14:56:36` | `cowrie.client.kex` |
| `2026-06-23 14:56:36` | `cowrie.login.success` |
| `2026-06-23 14:56:37` | `cowrie.session.params` |
| `2026-06-23 14:56:37` | `cowrie.command.input` |
| `2026-06-23 14:56:37` | `cowrie.log.closed` |
| `2026-06-23 14:56:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d061819fc576

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 14:56 |
| **Last Seen** | 2026-06-23 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:56:39` | `cowrie.session.connect` |
| `2026-06-23 14:56:39` | `cowrie.client.version` |
| `2026-06-23 14:56:39` | `cowrie.client.kex` |
| `2026-06-23 14:56:39` | `cowrie.login.success` |
| `2026-06-23 14:56:40` | `cowrie.session.params` |
| `2026-06-23 14:56:40` | `cowrie.command.input` |
| `2026-06-23 14:56:40` | `cowrie.log.closed` |
| `2026-06-23 14:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf7a6a325e17

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:56 |
| **Last Seen** | 2026-06-23 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:56:42` | `cowrie.session.connect` |
| `2026-06-23 14:56:42` | `cowrie.client.version` |
| `2026-06-23 14:56:42` | `cowrie.client.kex` |
| `2026-06-23 14:56:43` | `cowrie.login.success` |
| `2026-06-23 14:56:44` | `cowrie.session.params` |
| `2026-06-23 14:56:44` | `cowrie.command.input` |
| `2026-06-23 14:56:44` | `cowrie.log.closed` |
| `2026-06-23 14:56:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ba033ef982f

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:56 |
| **Last Seen** | 2026-06-23 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:56:50` | `cowrie.session.connect` |
| `2026-06-23 14:56:50` | `cowrie.client.version` |
| `2026-06-23 14:56:50` | `cowrie.client.kex` |
| `2026-06-23 14:56:50` | `cowrie.login.success` |
| `2026-06-23 14:56:51` | `cowrie.session.params` |
| `2026-06-23 14:56:51` | `cowrie.command.input` |
| `2026-06-23 14:56:51` | `cowrie.log.closed` |
| `2026-06-23 14:56:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baf38b4a619d

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:56 |
| **Last Seen** | 2026-06-23 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:56:57` | `cowrie.session.connect` |
| `2026-06-23 14:56:57` | `cowrie.client.version` |
| `2026-06-23 14:56:57` | `cowrie.client.kex` |
| `2026-06-23 14:56:57` | `cowrie.login.success` |
| `2026-06-23 14:56:58` | `cowrie.session.params` |
| `2026-06-23 14:56:58` | `cowrie.command.input` |
| `2026-06-23 14:56:58` | `cowrie.log.closed` |
| `2026-06-23 14:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92fb017986f6

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:57 |
| **Last Seen** | 2026-06-23 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:57:03` | `cowrie.session.connect` |
| `2026-06-23 14:57:03` | `cowrie.client.version` |
| `2026-06-23 14:57:03` | `cowrie.client.kex` |
| `2026-06-23 14:57:04` | `cowrie.login.success` |
| `2026-06-23 14:57:05` | `cowrie.session.params` |
| `2026-06-23 14:57:05` | `cowrie.command.input` |
| `2026-06-23 14:57:05` | `cowrie.log.closed` |
| `2026-06-23 14:57:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71b9682fa54e

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:57 |
| **Last Seen** | 2026-06-23 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:57:10` | `cowrie.session.connect` |
| `2026-06-23 14:57:10` | `cowrie.client.version` |
| `2026-06-23 14:57:10` | `cowrie.client.kex` |
| `2026-06-23 14:57:10` | `cowrie.login.success` |
| `2026-06-23 14:57:11` | `cowrie.session.params` |
| `2026-06-23 14:57:11` | `cowrie.command.input` |
| `2026-06-23 14:57:11` | `cowrie.log.closed` |
| `2026-06-23 14:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a884294c1e5

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:57 |
| **Last Seen** | 2026-06-23 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:57:16` | `cowrie.session.connect` |
| `2026-06-23 14:57:16` | `cowrie.client.version` |
| `2026-06-23 14:57:17` | `cowrie.client.kex` |
| `2026-06-23 14:57:17` | `cowrie.login.success` |
| `2026-06-23 14:57:18` | `cowrie.session.params` |
| `2026-06-23 14:57:18` | `cowrie.command.input` |
| `2026-06-23 14:57:18` | `cowrie.log.closed` |
| `2026-06-23 14:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43a29c3500dd

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:57 |
| **Last Seen** | 2026-06-23 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:57:24` | `cowrie.session.connect` |
| `2026-06-23 14:57:24` | `cowrie.client.version` |
| `2026-06-23 14:57:24` | `cowrie.client.kex` |
| `2026-06-23 14:57:24` | `cowrie.login.success` |
| `2026-06-23 14:57:25` | `cowrie.session.params` |
| `2026-06-23 14:57:25` | `cowrie.command.input` |
| `2026-06-23 14:57:25` | `cowrie.log.closed` |
| `2026-06-23 14:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da96292c3716

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:57 |
| **Last Seen** | 2026-06-23 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:57:30` | `cowrie.session.connect` |
| `2026-06-23 14:57:30` | `cowrie.client.version` |
| `2026-06-23 14:57:31` | `cowrie.client.kex` |
| `2026-06-23 14:57:31` | `cowrie.login.success` |
| `2026-06-23 14:57:32` | `cowrie.session.params` |
| `2026-06-23 14:57:32` | `cowrie.command.input` |
| `2026-06-23 14:57:32` | `cowrie.log.closed` |
| `2026-06-23 14:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aac0510acf11

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:57 |
| **Last Seen** | 2026-06-23 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:57:39` | `cowrie.session.connect` |
| `2026-06-23 14:57:39` | `cowrie.client.version` |
| `2026-06-23 14:57:39` | `cowrie.client.kex` |
| `2026-06-23 14:57:39` | `cowrie.login.success` |
| `2026-06-23 14:57:40` | `cowrie.session.params` |
| `2026-06-23 14:57:40` | `cowrie.command.input` |
| `2026-06-23 14:57:40` | `cowrie.log.closed` |
| `2026-06-23 14:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-791bef6e7440

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 14:57 |
| **Last Seen** | 2026-06-23 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:57:40` | `cowrie.session.connect` |
| `2026-06-23 14:57:40` | `cowrie.client.version` |
| `2026-06-23 14:57:40` | `cowrie.client.kex` |
| `2026-06-23 14:57:41` | `cowrie.login.success` |
| `2026-06-23 14:57:41` | `cowrie.session.params` |
| `2026-06-23 14:57:41` | `cowrie.command.input` |
| `2026-06-23 14:57:41` | `cowrie.log.closed` |
| `2026-06-23 14:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a92fe3029435

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:57 |
| **Last Seen** | 2026-06-23 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:57:46` | `cowrie.session.connect` |
| `2026-06-23 14:57:46` | `cowrie.client.version` |
| `2026-06-23 14:57:46` | `cowrie.client.kex` |
| `2026-06-23 14:57:46` | `cowrie.login.success` |
| `2026-06-23 14:57:47` | `cowrie.session.params` |
| `2026-06-23 14:57:47` | `cowrie.command.input` |
| `2026-06-23 14:57:47` | `cowrie.log.closed` |
| `2026-06-23 14:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b9995d3d83e

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:57 |
| **Last Seen** | 2026-06-23 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:57:53` | `cowrie.session.connect` |
| `2026-06-23 14:57:53` | `cowrie.client.version` |
| `2026-06-23 14:57:53` | `cowrie.client.kex` |
| `2026-06-23 14:57:53` | `cowrie.login.success` |
| `2026-06-23 14:57:54` | `cowrie.session.params` |
| `2026-06-23 14:57:54` | `cowrie.command.input` |
| `2026-06-23 14:57:54` | `cowrie.log.closed` |
| `2026-06-23 14:57:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e644d407e66

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:57 |
| **Last Seen** | 2026-06-23 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:57:59` | `cowrie.session.connect` |
| `2026-06-23 14:57:59` | `cowrie.client.version` |
| `2026-06-23 14:57:59` | `cowrie.client.kex` |
| `2026-06-23 14:57:59` | `cowrie.login.success` |
| `2026-06-23 14:58:00` | `cowrie.session.params` |
| `2026-06-23 14:58:00` | `cowrie.command.input` |
| `2026-06-23 14:58:00` | `cowrie.log.closed` |
| `2026-06-23 14:58:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-127fabba9a9d

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:58 |
| **Last Seen** | 2026-06-23 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:58:05` | `cowrie.session.connect` |
| `2026-06-23 14:58:05` | `cowrie.client.version` |
| `2026-06-23 14:58:05` | `cowrie.client.kex` |
| `2026-06-23 14:58:06` | `cowrie.login.success` |
| `2026-06-23 14:58:07` | `cowrie.session.params` |
| `2026-06-23 14:58:07` | `cowrie.command.input` |
| `2026-06-23 14:58:07` | `cowrie.log.closed` |
| `2026-06-23 14:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f10889669c2

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:58 |
| **Last Seen** | 2026-06-23 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:58:13` | `cowrie.session.connect` |
| `2026-06-23 14:58:13` | `cowrie.client.version` |
| `2026-06-23 14:58:13` | `cowrie.client.kex` |
| `2026-06-23 14:58:13` | `cowrie.login.success` |
| `2026-06-23 14:58:14` | `cowrie.session.params` |
| `2026-06-23 14:58:14` | `cowrie.command.input` |
| `2026-06-23 14:58:14` | `cowrie.log.closed` |
| `2026-06-23 14:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02ed8bd0c0bf

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:58 |
| **Last Seen** | 2026-06-23 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:58:19` | `cowrie.session.connect` |
| `2026-06-23 14:58:19` | `cowrie.client.version` |
| `2026-06-23 14:58:19` | `cowrie.client.kex` |
| `2026-06-23 14:58:19` | `cowrie.login.success` |
| `2026-06-23 14:58:20` | `cowrie.session.params` |
| `2026-06-23 14:58:20` | `cowrie.command.input` |
| `2026-06-23 14:58:20` | `cowrie.log.closed` |
| `2026-06-23 14:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77b4002cfd58

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:58 |
| **Last Seen** | 2026-06-23 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:58:28` | `cowrie.session.connect` |
| `2026-06-23 14:58:28` | `cowrie.client.version` |
| `2026-06-23 14:58:28` | `cowrie.client.kex` |
| `2026-06-23 14:58:29` | `cowrie.login.success` |
| `2026-06-23 14:58:30` | `cowrie.session.params` |
| `2026-06-23 14:58:30` | `cowrie.command.input` |
| `2026-06-23 14:58:30` | `cowrie.log.closed` |
| `2026-06-23 14:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34acb74e66c4

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 14:58 |
| **Last Seen** | 2026-06-23 14:58 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:58:32` | `cowrie.session.connect` |
| `2026-06-23 14:58:34` | `cowrie.client.version` |
| `2026-06-23 14:58:34` | `cowrie.client.kex` |
| `2026-06-23 14:58:41` | `cowrie.login.success` |
| `2026-06-23 14:58:45` | `cowrie.session.params` |
| `2026-06-23 14:58:45` | `cowrie.command.input` |
| `2026-06-23 14:58:46` | `cowrie.log.closed` |
| `2026-06-23 14:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd63242db121

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:58 |
| **Last Seen** | 2026-06-23 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:58:37` | `cowrie.session.connect` |
| `2026-06-23 14:58:37` | `cowrie.client.version` |
| `2026-06-23 14:58:37` | `cowrie.client.kex` |
| `2026-06-23 14:58:38` | `cowrie.login.success` |
| `2026-06-23 14:58:38` | `cowrie.session.params` |
| `2026-06-23 14:58:38` | `cowrie.command.input` |
| `2026-06-23 14:58:39` | `cowrie.log.closed` |
| `2026-06-23 14:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3a3a1b4b116

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 14:58 |
| **Last Seen** | 2026-06-23 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:58:39` | `cowrie.session.connect` |
| `2026-06-23 14:58:39` | `cowrie.client.version` |
| `2026-06-23 14:58:40` | `cowrie.client.kex` |
| `2026-06-23 14:58:40` | `cowrie.login.success` |
| `2026-06-23 14:58:41` | `cowrie.session.params` |
| `2026-06-23 14:58:41` | `cowrie.command.input` |
| `2026-06-23 14:58:41` | `cowrie.log.closed` |
| `2026-06-23 14:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5647c3dbafd3

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:58 |
| **Last Seen** | 2026-06-23 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:58:46` | `cowrie.session.connect` |
| `2026-06-23 14:58:46` | `cowrie.client.version` |
| `2026-06-23 14:58:46` | `cowrie.client.kex` |
| `2026-06-23 14:58:46` | `cowrie.login.success` |
| `2026-06-23 14:58:47` | `cowrie.session.params` |
| `2026-06-23 14:58:47` | `cowrie.command.input` |
| `2026-06-23 14:58:47` | `cowrie.log.closed` |
| `2026-06-23 14:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1c3d6440582

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:58 |
| **Last Seen** | 2026-06-23 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:58:53` | `cowrie.session.connect` |
| `2026-06-23 14:58:53` | `cowrie.client.version` |
| `2026-06-23 14:58:53` | `cowrie.client.kex` |
| `2026-06-23 14:58:53` | `cowrie.login.success` |
| `2026-06-23 14:58:54` | `cowrie.session.params` |
| `2026-06-23 14:58:54` | `cowrie.command.input` |
| `2026-06-23 14:58:54` | `cowrie.log.closed` |
| `2026-06-23 14:58:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5ec37f8ced9

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:59 |
| **Last Seen** | 2026-06-23 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:59:00` | `cowrie.session.connect` |
| `2026-06-23 14:59:00` | `cowrie.client.version` |
| `2026-06-23 14:59:00` | `cowrie.client.kex` |
| `2026-06-23 14:59:00` | `cowrie.login.success` |
| `2026-06-23 14:59:01` | `cowrie.session.params` |
| `2026-06-23 14:59:01` | `cowrie.command.input` |
| `2026-06-23 14:59:01` | `cowrie.log.closed` |
| `2026-06-23 14:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cefbba18d9ac

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:59 |
| **Last Seen** | 2026-06-23 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:59:07` | `cowrie.session.connect` |
| `2026-06-23 14:59:07` | `cowrie.client.version` |
| `2026-06-23 14:59:07` | `cowrie.client.kex` |
| `2026-06-23 14:59:07` | `cowrie.login.success` |
| `2026-06-23 14:59:08` | `cowrie.session.params` |
| `2026-06-23 14:59:08` | `cowrie.command.input` |
| `2026-06-23 14:59:08` | `cowrie.log.closed` |
| `2026-06-23 14:59:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3d3255822e7

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:59 |
| **Last Seen** | 2026-06-23 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:59:14` | `cowrie.session.connect` |
| `2026-06-23 14:59:14` | `cowrie.client.version` |
| `2026-06-23 14:59:14` | `cowrie.client.kex` |
| `2026-06-23 14:59:15` | `cowrie.login.success` |
| `2026-06-23 14:59:16` | `cowrie.session.params` |
| `2026-06-23 14:59:16` | `cowrie.command.input` |
| `2026-06-23 14:59:16` | `cowrie.log.closed` |
| `2026-06-23 14:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9710d66ffec

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:59 |
| **Last Seen** | 2026-06-23 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:59:22` | `cowrie.session.connect` |
| `2026-06-23 14:59:22` | `cowrie.client.version` |
| `2026-06-23 14:59:22` | `cowrie.client.kex` |
| `2026-06-23 14:59:22` | `cowrie.login.success` |
| `2026-06-23 14:59:23` | `cowrie.session.params` |
| `2026-06-23 14:59:23` | `cowrie.command.input` |
| `2026-06-23 14:59:23` | `cowrie.log.closed` |
| `2026-06-23 14:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b663c56ff3bf

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:59 |
| **Last Seen** | 2026-06-23 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:59:30` | `cowrie.session.connect` |
| `2026-06-23 14:59:30` | `cowrie.client.version` |
| `2026-06-23 14:59:30` | `cowrie.client.kex` |
| `2026-06-23 14:59:30` | `cowrie.login.success` |
| `2026-06-23 14:59:31` | `cowrie.session.params` |
| `2026-06-23 14:59:31` | `cowrie.command.input` |
| `2026-06-23 14:59:31` | `cowrie.log.closed` |
| `2026-06-23 14:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c03a5712a04a

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:59 |
| **Last Seen** | 2026-06-23 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:59:37` | `cowrie.session.connect` |
| `2026-06-23 14:59:37` | `cowrie.client.version` |
| `2026-06-23 14:59:37` | `cowrie.client.kex` |
| `2026-06-23 14:59:37` | `cowrie.login.success` |
| `2026-06-23 14:59:38` | `cowrie.session.params` |
| `2026-06-23 14:59:38` | `cowrie.command.input` |
| `2026-06-23 14:59:39` | `cowrie.log.closed` |
| `2026-06-23 14:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba71dd51608d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 14:59 |
| **Last Seen** | 2026-06-23 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:59:39` | `cowrie.session.connect` |
| `2026-06-23 14:59:39` | `cowrie.client.version` |
| `2026-06-23 14:59:39` | `cowrie.client.kex` |
| `2026-06-23 14:59:39` | `cowrie.login.success` |
| `2026-06-23 14:59:40` | `cowrie.session.params` |
| `2026-06-23 14:59:40` | `cowrie.command.input` |
| `2026-06-23 14:59:40` | `cowrie.log.closed` |
| `2026-06-23 14:59:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-277ddeb4616b

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:59 |
| **Last Seen** | 2026-06-23 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:59:44` | `cowrie.session.connect` |
| `2026-06-23 14:59:44` | `cowrie.client.version` |
| `2026-06-23 14:59:44` | `cowrie.client.kex` |
| `2026-06-23 14:59:44` | `cowrie.login.success` |
| `2026-06-23 14:59:45` | `cowrie.session.params` |
| `2026-06-23 14:59:45` | `cowrie.command.input` |
| `2026-06-23 14:59:45` | `cowrie.log.closed` |
| `2026-06-23 14:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d1dfcff77f8

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:59 |
| **Last Seen** | 2026-06-23 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:59:52` | `cowrie.session.connect` |
| `2026-06-23 14:59:52` | `cowrie.client.version` |
| `2026-06-23 14:59:52` | `cowrie.client.kex` |
| `2026-06-23 14:59:52` | `cowrie.login.success` |
| `2026-06-23 14:59:53` | `cowrie.session.params` |
| `2026-06-23 14:59:53` | `cowrie.command.input` |
| `2026-06-23 14:59:53` | `cowrie.log.closed` |
| `2026-06-23 14:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc827dd80c2e

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 14:59 |
| **Last Seen** | 2026-06-23 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:59:58` | `cowrie.session.connect` |
| `2026-06-23 14:59:58` | `cowrie.client.version` |
| `2026-06-23 14:59:58` | `cowrie.client.kex` |
| `2026-06-23 14:59:59` | `cowrie.login.success` |
| `2026-06-23 14:59:59` | `cowrie.session.params` |
| `2026-06-23 14:59:59` | `cowrie.command.input` |
| `2026-06-23 14:59:59` | `cowrie.log.closed` |
| `2026-06-23 14:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43877d3720ae

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:00 |
| **Last Seen** | 2026-06-23 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:00:06` | `cowrie.session.connect` |
| `2026-06-23 15:00:06` | `cowrie.client.version` |
| `2026-06-23 15:00:06` | `cowrie.client.kex` |
| `2026-06-23 15:00:06` | `cowrie.login.success` |
| `2026-06-23 15:00:07` | `cowrie.session.params` |
| `2026-06-23 15:00:07` | `cowrie.command.input` |
| `2026-06-23 15:00:07` | `cowrie.log.closed` |
| `2026-06-23 15:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8ba5764aa4d

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:00 |
| **Last Seen** | 2026-06-23 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:00:13` | `cowrie.session.connect` |
| `2026-06-23 15:00:13` | `cowrie.client.version` |
| `2026-06-23 15:00:13` | `cowrie.client.kex` |
| `2026-06-23 15:00:14` | `cowrie.login.success` |
| `2026-06-23 15:00:15` | `cowrie.session.params` |
| `2026-06-23 15:00:15` | `cowrie.command.input` |
| `2026-06-23 15:00:15` | `cowrie.log.closed` |
| `2026-06-23 15:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d7396d0d1cb

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:00 |
| **Last Seen** | 2026-06-23 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:00:20` | `cowrie.session.connect` |
| `2026-06-23 15:00:20` | `cowrie.client.version` |
| `2026-06-23 15:00:20` | `cowrie.client.kex` |
| `2026-06-23 15:00:21` | `cowrie.login.success` |
| `2026-06-23 15:00:21` | `cowrie.session.params` |
| `2026-06-23 15:00:21` | `cowrie.command.input` |
| `2026-06-23 15:00:22` | `cowrie.log.closed` |
| `2026-06-23 15:00:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4da1d70bdffe

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:00 |
| **Last Seen** | 2026-06-23 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:00:28` | `cowrie.session.connect` |
| `2026-06-23 15:00:28` | `cowrie.client.version` |
| `2026-06-23 15:00:28` | `cowrie.client.kex` |
| `2026-06-23 15:00:28` | `cowrie.login.success` |
| `2026-06-23 15:00:29` | `cowrie.session.params` |
| `2026-06-23 15:00:29` | `cowrie.command.input` |
| `2026-06-23 15:00:29` | `cowrie.log.closed` |
| `2026-06-23 15:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab5c1b78fc4b

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:00 |
| **Last Seen** | 2026-06-23 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:00:34` | `cowrie.session.connect` |
| `2026-06-23 15:00:34` | `cowrie.client.version` |
| `2026-06-23 15:00:34` | `cowrie.client.kex` |
| `2026-06-23 15:00:35` | `cowrie.login.success` |
| `2026-06-23 15:00:35` | `cowrie.session.params` |
| `2026-06-23 15:00:35` | `cowrie.command.input` |
| `2026-06-23 15:00:35` | `cowrie.log.closed` |
| `2026-06-23 15:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b13558c9cbba

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:00 |
| **Last Seen** | 2026-06-23 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:00:38` | `cowrie.session.connect` |
| `2026-06-23 15:00:38` | `cowrie.client.version` |
| `2026-06-23 15:00:38` | `cowrie.client.kex` |
| `2026-06-23 15:00:38` | `cowrie.login.success` |
| `2026-06-23 15:00:39` | `cowrie.session.params` |
| `2026-06-23 15:00:39` | `cowrie.command.input` |
| `2026-06-23 15:00:39` | `cowrie.log.closed` |
| `2026-06-23 15:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0dca44ecc46

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:00 |
| **Last Seen** | 2026-06-23 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:00:41` | `cowrie.session.connect` |
| `2026-06-23 15:00:41` | `cowrie.client.version` |
| `2026-06-23 15:00:41` | `cowrie.client.kex` |
| `2026-06-23 15:00:42` | `cowrie.login.success` |
| `2026-06-23 15:00:42` | `cowrie.session.params` |
| `2026-06-23 15:00:42` | `cowrie.command.input` |
| `2026-06-23 15:00:43` | `cowrie.log.closed` |
| `2026-06-23 15:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b39c2276d4a

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:00 |
| **Last Seen** | 2026-06-23 15:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:00:47` | `cowrie.session.connect` |
| `2026-06-23 15:00:47` | `cowrie.client.version` |
| `2026-06-23 15:00:47` | `cowrie.client.kex` |
| `2026-06-23 15:00:48` | `cowrie.login.success` |
| `2026-06-23 15:00:49` | `cowrie.session.params` |
| `2026-06-23 15:00:49` | `cowrie.command.input` |
| `2026-06-23 15:00:49` | `cowrie.log.closed` |
| `2026-06-23 15:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1b71257315c

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:00 |
| **Last Seen** | 2026-06-23 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:00:54` | `cowrie.session.connect` |
| `2026-06-23 15:00:54` | `cowrie.client.version` |
| `2026-06-23 15:00:54` | `cowrie.client.kex` |
| `2026-06-23 15:00:55` | `cowrie.login.success` |
| `2026-06-23 15:00:55` | `cowrie.session.params` |
| `2026-06-23 15:00:55` | `cowrie.command.input` |
| `2026-06-23 15:00:56` | `cowrie.log.closed` |
| `2026-06-23 15:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c63dbe093750

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:01 |
| **Last Seen** | 2026-06-23 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:01:01` | `cowrie.session.connect` |
| `2026-06-23 15:01:01` | `cowrie.client.version` |
| `2026-06-23 15:01:01` | `cowrie.client.kex` |
| `2026-06-23 15:01:02` | `cowrie.login.success` |
| `2026-06-23 15:01:02` | `cowrie.session.params` |
| `2026-06-23 15:01:02` | `cowrie.command.input` |
| `2026-06-23 15:01:03` | `cowrie.log.closed` |
| `2026-06-23 15:01:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e079a2751d17

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:01 |
| **Last Seen** | 2026-06-23 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:01:08` | `cowrie.session.connect` |
| `2026-06-23 15:01:08` | `cowrie.client.version` |
| `2026-06-23 15:01:08` | `cowrie.client.kex` |
| `2026-06-23 15:01:09` | `cowrie.login.success` |
| `2026-06-23 15:01:09` | `cowrie.session.params` |
| `2026-06-23 15:01:09` | `cowrie.command.input` |
| `2026-06-23 15:01:09` | `cowrie.log.closed` |
| `2026-06-23 15:01:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb45b539800c

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:01 |
| **Last Seen** | 2026-06-23 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:01:14` | `cowrie.session.connect` |
| `2026-06-23 15:01:14` | `cowrie.client.version` |
| `2026-06-23 15:01:14` | `cowrie.client.kex` |
| `2026-06-23 15:01:14` | `cowrie.login.success` |
| `2026-06-23 15:01:15` | `cowrie.session.params` |
| `2026-06-23 15:01:15` | `cowrie.command.input` |
| `2026-06-23 15:01:15` | `cowrie.log.closed` |
| `2026-06-23 15:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82bf52b8de1b

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:01 |
| **Last Seen** | 2026-06-23 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:01:22` | `cowrie.session.connect` |
| `2026-06-23 15:01:22` | `cowrie.client.version` |
| `2026-06-23 15:01:22` | `cowrie.client.kex` |
| `2026-06-23 15:01:22` | `cowrie.login.success` |
| `2026-06-23 15:01:23` | `cowrie.session.params` |
| `2026-06-23 15:01:23` | `cowrie.command.input` |
| `2026-06-23 15:01:23` | `cowrie.log.closed` |
| `2026-06-23 15:01:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-480ed6b0a723

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:01 |
| **Last Seen** | 2026-06-23 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:01:28` | `cowrie.session.connect` |
| `2026-06-23 15:01:28` | `cowrie.client.version` |
| `2026-06-23 15:01:28` | `cowrie.client.kex` |
| `2026-06-23 15:01:28` | `cowrie.login.success` |
| `2026-06-23 15:01:29` | `cowrie.session.params` |
| `2026-06-23 15:01:29` | `cowrie.command.input` |
| `2026-06-23 15:01:29` | `cowrie.log.closed` |
| `2026-06-23 15:01:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aa4109c3689

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:01 |
| **Last Seen** | 2026-06-23 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:01:36` | `cowrie.session.connect` |
| `2026-06-23 15:01:36` | `cowrie.client.version` |
| `2026-06-23 15:01:36` | `cowrie.client.kex` |
| `2026-06-23 15:01:36` | `cowrie.login.success` |
| `2026-06-23 15:01:37` | `cowrie.session.params` |
| `2026-06-23 15:01:37` | `cowrie.command.input` |
| `2026-06-23 15:01:37` | `cowrie.log.closed` |
| `2026-06-23 15:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e71e873f1a7b

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:01 |
| **Last Seen** | 2026-06-23 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:01:42` | `cowrie.session.connect` |
| `2026-06-23 15:01:42` | `cowrie.client.version` |
| `2026-06-23 15:01:43` | `cowrie.client.kex` |
| `2026-06-23 15:01:43` | `cowrie.login.success` |
| `2026-06-23 15:01:44` | `cowrie.session.params` |
| `2026-06-23 15:01:44` | `cowrie.command.input` |
| `2026-06-23 15:01:44` | `cowrie.log.closed` |
| `2026-06-23 15:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6880bf38bbeb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:01 |
| **Last Seen** | 2026-06-23 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:01:45` | `cowrie.session.connect` |
| `2026-06-23 15:01:45` | `cowrie.client.version` |
| `2026-06-23 15:01:45` | `cowrie.client.kex` |
| `2026-06-23 15:01:46` | `cowrie.login.success` |
| `2026-06-23 15:01:46` | `cowrie.session.params` |
| `2026-06-23 15:01:46` | `cowrie.command.input` |
| `2026-06-23 15:01:47` | `cowrie.log.closed` |
| `2026-06-23 15:01:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-969484ae6599

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:01 |
| **Last Seen** | 2026-06-23 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:01:50` | `cowrie.session.connect` |
| `2026-06-23 15:01:50` | `cowrie.client.version` |
| `2026-06-23 15:01:50` | `cowrie.client.kex` |
| `2026-06-23 15:01:51` | `cowrie.login.success` |
| `2026-06-23 15:01:51` | `cowrie.session.params` |
| `2026-06-23 15:01:51` | `cowrie.command.input` |
| `2026-06-23 15:01:51` | `cowrie.log.closed` |
| `2026-06-23 15:01:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32949392cef4

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:01 |
| **Last Seen** | 2026-06-23 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:01:57` | `cowrie.session.connect` |
| `2026-06-23 15:01:57` | `cowrie.client.version` |
| `2026-06-23 15:01:57` | `cowrie.client.kex` |
| `2026-06-23 15:01:57` | `cowrie.login.success` |
| `2026-06-23 15:01:58` | `cowrie.session.params` |
| `2026-06-23 15:01:58` | `cowrie.command.input` |
| `2026-06-23 15:01:58` | `cowrie.log.closed` |
| `2026-06-23 15:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-374edec21bda

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:02 |
| **Last Seen** | 2026-06-23 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:02:05` | `cowrie.session.connect` |
| `2026-06-23 15:02:05` | `cowrie.client.version` |
| `2026-06-23 15:02:05` | `cowrie.client.kex` |
| `2026-06-23 15:02:05` | `cowrie.login.success` |
| `2026-06-23 15:02:06` | `cowrie.session.params` |
| `2026-06-23 15:02:06` | `cowrie.command.input` |
| `2026-06-23 15:02:06` | `cowrie.log.closed` |
| `2026-06-23 15:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3e404725266

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:02 |
| **Last Seen** | 2026-06-23 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:02:12` | `cowrie.session.connect` |
| `2026-06-23 15:02:12` | `cowrie.client.version` |
| `2026-06-23 15:02:12` | `cowrie.client.kex` |
| `2026-06-23 15:02:13` | `cowrie.login.success` |
| `2026-06-23 15:02:14` | `cowrie.session.params` |
| `2026-06-23 15:02:14` | `cowrie.command.input` |
| `2026-06-23 15:02:14` | `cowrie.log.closed` |
| `2026-06-23 15:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f99ce49d3a2

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:02 |
| **Last Seen** | 2026-06-23 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:02:19` | `cowrie.session.connect` |
| `2026-06-23 15:02:19` | `cowrie.client.version` |
| `2026-06-23 15:02:19` | `cowrie.client.kex` |
| `2026-06-23 15:02:20` | `cowrie.login.success` |
| `2026-06-23 15:02:21` | `cowrie.session.params` |
| `2026-06-23 15:02:21` | `cowrie.command.input` |
| `2026-06-23 15:02:21` | `cowrie.log.closed` |
| `2026-06-23 15:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f498056de9e

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:02 |
| **Last Seen** | 2026-06-23 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:02:27` | `cowrie.session.connect` |
| `2026-06-23 15:02:27` | `cowrie.client.version` |
| `2026-06-23 15:02:27` | `cowrie.client.kex` |
| `2026-06-23 15:02:28` | `cowrie.login.success` |
| `2026-06-23 15:02:28` | `cowrie.session.params` |
| `2026-06-23 15:02:28` | `cowrie.command.input` |
| `2026-06-23 15:02:29` | `cowrie.log.closed` |
| `2026-06-23 15:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2171ca4cd758

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:02 |
| **Last Seen** | 2026-06-23 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:02:35` | `cowrie.session.connect` |
| `2026-06-23 15:02:35` | `cowrie.client.version` |
| `2026-06-23 15:02:35` | `cowrie.client.kex` |
| `2026-06-23 15:02:36` | `cowrie.login.success` |
| `2026-06-23 15:02:37` | `cowrie.session.params` |
| `2026-06-23 15:02:37` | `cowrie.command.input` |
| `2026-06-23 15:02:37` | `cowrie.log.closed` |
| `2026-06-23 15:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0973b81131e1

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:02 |
| **Last Seen** | 2026-06-23 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:02:42` | `cowrie.session.connect` |
| `2026-06-23 15:02:42` | `cowrie.client.version` |
| `2026-06-23 15:02:42` | `cowrie.client.kex` |
| `2026-06-23 15:02:43` | `cowrie.login.success` |
| `2026-06-23 15:02:43` | `cowrie.session.params` |
| `2026-06-23 15:02:43` | `cowrie.command.input` |
| `2026-06-23 15:02:44` | `cowrie.log.closed` |
| `2026-06-23 15:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37afa8d6d7f1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:02 |
| **Last Seen** | 2026-06-23 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:02:47` | `cowrie.session.connect` |
| `2026-06-23 15:02:47` | `cowrie.client.version` |
| `2026-06-23 15:02:47` | `cowrie.client.kex` |
| `2026-06-23 15:02:47` | `cowrie.login.success` |
| `2026-06-23 15:02:48` | `cowrie.session.params` |
| `2026-06-23 15:02:48` | `cowrie.command.input` |
| `2026-06-23 15:02:48` | `cowrie.log.closed` |
| `2026-06-23 15:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-690aa8383702

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:02 |
| **Last Seen** | 2026-06-23 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:02:51` | `cowrie.session.connect` |
| `2026-06-23 15:02:51` | `cowrie.client.version` |
| `2026-06-23 15:02:51` | `cowrie.client.kex` |
| `2026-06-23 15:02:52` | `cowrie.login.success` |
| `2026-06-23 15:02:52` | `cowrie.session.params` |
| `2026-06-23 15:02:52` | `cowrie.command.input` |
| `2026-06-23 15:02:52` | `cowrie.log.closed` |
| `2026-06-23 15:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42a352c38217

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:02 |
| **Last Seen** | 2026-06-23 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:02:59` | `cowrie.session.connect` |
| `2026-06-23 15:02:59` | `cowrie.client.version` |
| `2026-06-23 15:02:59` | `cowrie.client.kex` |
| `2026-06-23 15:02:59` | `cowrie.login.success` |
| `2026-06-23 15:03:00` | `cowrie.session.params` |
| `2026-06-23 15:03:00` | `cowrie.command.input` |
| `2026-06-23 15:03:00` | `cowrie.log.closed` |
| `2026-06-23 15:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1da31e673afb

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:03 |
| **Last Seen** | 2026-06-23 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:03:07` | `cowrie.session.connect` |
| `2026-06-23 15:03:07` | `cowrie.client.version` |
| `2026-06-23 15:03:07` | `cowrie.client.kex` |
| `2026-06-23 15:03:07` | `cowrie.login.success` |
| `2026-06-23 15:03:08` | `cowrie.session.params` |
| `2026-06-23 15:03:08` | `cowrie.command.input` |
| `2026-06-23 15:03:08` | `cowrie.log.closed` |
| `2026-06-23 15:03:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93779e0196c8

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:03 |
| **Last Seen** | 2026-06-23 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:03:14` | `cowrie.session.connect` |
| `2026-06-23 15:03:14` | `cowrie.client.version` |
| `2026-06-23 15:03:14` | `cowrie.client.kex` |
| `2026-06-23 15:03:14` | `cowrie.login.success` |
| `2026-06-23 15:03:15` | `cowrie.session.params` |
| `2026-06-23 15:03:15` | `cowrie.command.input` |
| `2026-06-23 15:03:15` | `cowrie.log.closed` |
| `2026-06-23 15:03:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-809b5099e119

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:03 |
| **Last Seen** | 2026-06-23 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:03:21` | `cowrie.session.connect` |
| `2026-06-23 15:03:21` | `cowrie.client.version` |
| `2026-06-23 15:03:21` | `cowrie.client.kex` |
| `2026-06-23 15:03:22` | `cowrie.login.success` |
| `2026-06-23 15:03:23` | `cowrie.session.params` |
| `2026-06-23 15:03:23` | `cowrie.command.input` |
| `2026-06-23 15:03:23` | `cowrie.log.closed` |
| `2026-06-23 15:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f600f30c8a48

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:03 |
| **Last Seen** | 2026-06-23 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:03:30` | `cowrie.session.connect` |
| `2026-06-23 15:03:30` | `cowrie.client.version` |
| `2026-06-23 15:03:30` | `cowrie.client.kex` |
| `2026-06-23 15:03:30` | `cowrie.login.success` |
| `2026-06-23 15:03:31` | `cowrie.session.params` |
| `2026-06-23 15:03:31` | `cowrie.command.input` |
| `2026-06-23 15:03:31` | `cowrie.log.closed` |
| `2026-06-23 15:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ea0f4aab5c1

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:03 |
| **Last Seen** | 2026-06-23 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:03:37` | `cowrie.session.connect` |
| `2026-06-23 15:03:37` | `cowrie.client.version` |
| `2026-06-23 15:03:37` | `cowrie.client.kex` |
| `2026-06-23 15:03:38` | `cowrie.login.success` |
| `2026-06-23 15:03:39` | `cowrie.session.params` |
| `2026-06-23 15:03:39` | `cowrie.command.input` |
| `2026-06-23 15:03:39` | `cowrie.log.closed` |
| `2026-06-23 15:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c99035bb577a

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:03 |
| **Last Seen** | 2026-06-23 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:03:45` | `cowrie.session.connect` |
| `2026-06-23 15:03:45` | `cowrie.client.version` |
| `2026-06-23 15:03:45` | `cowrie.client.kex` |
| `2026-06-23 15:03:45` | `cowrie.login.success` |
| `2026-06-23 15:03:46` | `cowrie.session.params` |
| `2026-06-23 15:03:46` | `cowrie.command.input` |
| `2026-06-23 15:03:46` | `cowrie.log.closed` |
| `2026-06-23 15:03:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5520430d5297

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:03 |
| **Last Seen** | 2026-06-23 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:03:48` | `cowrie.session.connect` |
| `2026-06-23 15:03:48` | `cowrie.client.version` |
| `2026-06-23 15:03:48` | `cowrie.client.kex` |
| `2026-06-23 15:03:49` | `cowrie.login.success` |
| `2026-06-23 15:03:49` | `cowrie.session.params` |
| `2026-06-23 15:03:49` | `cowrie.command.input` |
| `2026-06-23 15:03:49` | `cowrie.log.closed` |
| `2026-06-23 15:03:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a960c2133ac1

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:03 |
| **Last Seen** | 2026-06-23 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:03:52` | `cowrie.session.connect` |
| `2026-06-23 15:03:52` | `cowrie.client.version` |
| `2026-06-23 15:03:52` | `cowrie.client.kex` |
| `2026-06-23 15:03:52` | `cowrie.login.success` |
| `2026-06-23 15:03:54` | `cowrie.session.params` |
| `2026-06-23 15:03:54` | `cowrie.command.input` |
| `2026-06-23 15:03:54` | `cowrie.log.closed` |
| `2026-06-23 15:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59ee58beeb74

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:04 |
| **Last Seen** | 2026-06-23 15:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:04:00` | `cowrie.session.connect` |
| `2026-06-23 15:04:00` | `cowrie.client.version` |
| `2026-06-23 15:04:00` | `cowrie.client.kex` |
| `2026-06-23 15:04:01` | `cowrie.login.success` |
| `2026-06-23 15:04:02` | `cowrie.session.params` |
| `2026-06-23 15:04:02` | `cowrie.command.input` |
| `2026-06-23 15:04:02` | `cowrie.log.closed` |
| `2026-06-23 15:04:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa8c98865f1b

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:04 |
| **Last Seen** | 2026-06-23 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:04:08` | `cowrie.session.connect` |
| `2026-06-23 15:04:08` | `cowrie.client.version` |
| `2026-06-23 15:04:08` | `cowrie.client.kex` |
| `2026-06-23 15:04:09` | `cowrie.login.success` |
| `2026-06-23 15:04:09` | `cowrie.session.params` |
| `2026-06-23 15:04:09` | `cowrie.command.input` |
| `2026-06-23 15:04:10` | `cowrie.log.closed` |
| `2026-06-23 15:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2a879ce2c00

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:04 |
| **Last Seen** | 2026-06-23 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:04:24` | `cowrie.session.connect` |
| `2026-06-23 15:04:24` | `cowrie.client.version` |
| `2026-06-23 15:04:24` | `cowrie.client.kex` |
| `2026-06-23 15:04:24` | `cowrie.login.success` |
| `2026-06-23 15:04:25` | `cowrie.session.params` |
| `2026-06-23 15:04:25` | `cowrie.command.input` |
| `2026-06-23 15:04:25` | `cowrie.log.closed` |
| `2026-06-23 15:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ec78ef12854

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:04 |
| **Last Seen** | 2026-06-23 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:04:31` | `cowrie.session.connect` |
| `2026-06-23 15:04:31` | `cowrie.client.version` |
| `2026-06-23 15:04:31` | `cowrie.client.kex` |
| `2026-06-23 15:04:31` | `cowrie.login.success` |
| `2026-06-23 15:04:32` | `cowrie.session.params` |
| `2026-06-23 15:04:32` | `cowrie.command.input` |
| `2026-06-23 15:04:32` | `cowrie.log.closed` |
| `2026-06-23 15:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98c083f7a622

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]92` |
| **First Seen** | 2026-06-23 15:04 |
| **Last Seen** | 2026-06-23 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:04:38` | `cowrie.session.connect` |
| `2026-06-23 15:04:38` | `cowrie.client.version` |
| `2026-06-23 15:04:38` | `cowrie.client.kex` |
| `2026-06-23 15:04:38` | `cowrie.login.success` |
| `2026-06-23 15:04:39` | `cowrie.session.params` |
| `2026-06-23 15:04:39` | `cowrie.command.input` |
| `2026-06-23 15:04:39` | `cowrie.log.closed` |
| `2026-06-23 15:04:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5984be8d7136

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:04 |
| **Last Seen** | 2026-06-23 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:04:49` | `cowrie.session.connect` |
| `2026-06-23 15:04:49` | `cowrie.client.version` |
| `2026-06-23 15:04:49` | `cowrie.client.kex` |
| `2026-06-23 15:04:50` | `cowrie.login.success` |
| `2026-06-23 15:04:50` | `cowrie.session.params` |
| `2026-06-23 15:04:50` | `cowrie.command.input` |
| `2026-06-23 15:04:50` | `cowrie.log.closed` |
| `2026-06-23 15:04:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ace23e5a44f5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:05 |
| **Last Seen** | 2026-06-23 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:05:50` | `cowrie.session.connect` |
| `2026-06-23 15:05:50` | `cowrie.client.version` |
| `2026-06-23 15:05:50` | `cowrie.client.kex` |
| `2026-06-23 15:05:50` | `cowrie.login.success` |
| `2026-06-23 15:05:51` | `cowrie.session.params` |
| `2026-06-23 15:05:51` | `cowrie.command.input` |
| `2026-06-23 15:05:51` | `cowrie.log.closed` |
| `2026-06-23 15:05:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f04029f1eac7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:06 |
| **Last Seen** | 2026-06-23 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:06:55` | `cowrie.session.connect` |
| `2026-06-23 15:06:55` | `cowrie.client.version` |
| `2026-06-23 15:06:55` | `cowrie.client.kex` |
| `2026-06-23 15:06:55` | `cowrie.login.success` |
| `2026-06-23 15:06:56` | `cowrie.session.params` |
| `2026-06-23 15:06:56` | `cowrie.command.input` |
| `2026-06-23 15:06:56` | `cowrie.log.closed` |
| `2026-06-23 15:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0347256158c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:08 |
| **Last Seen** | 2026-06-23 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:08:02` | `cowrie.session.connect` |
| `2026-06-23 15:08:02` | `cowrie.client.version` |
| `2026-06-23 15:08:02` | `cowrie.client.kex` |
| `2026-06-23 15:08:03` | `cowrie.login.success` |
| `2026-06-23 15:08:04` | `cowrie.session.params` |
| `2026-06-23 15:08:04` | `cowrie.command.input` |
| `2026-06-23 15:08:04` | `cowrie.log.closed` |
| `2026-06-23 15:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6320cd57eddd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:09 |
| **Last Seen** | 2026-06-23 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:09:08` | `cowrie.session.connect` |
| `2026-06-23 15:09:08` | `cowrie.client.version` |
| `2026-06-23 15:09:08` | `cowrie.client.kex` |
| `2026-06-23 15:09:08` | `cowrie.login.success` |
| `2026-06-23 15:09:09` | `cowrie.session.params` |
| `2026-06-23 15:09:09` | `cowrie.command.input` |
| `2026-06-23 15:09:09` | `cowrie.log.closed` |
| `2026-06-23 15:09:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d859e5ffeeb5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:10 |
| **Last Seen** | 2026-06-23 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:10:10` | `cowrie.session.connect` |
| `2026-06-23 15:10:10` | `cowrie.client.version` |
| `2026-06-23 15:10:10` | `cowrie.client.kex` |
| `2026-06-23 15:10:10` | `cowrie.login.success` |
| `2026-06-23 15:10:11` | `cowrie.session.params` |
| `2026-06-23 15:10:11` | `cowrie.command.input` |
| `2026-06-23 15:10:11` | `cowrie.log.closed` |
| `2026-06-23 15:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-674bb8ac4d95

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:11 |
| **Last Seen** | 2026-06-23 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:11:09` | `cowrie.session.connect` |
| `2026-06-23 15:11:09` | `cowrie.client.version` |
| `2026-06-23 15:11:09` | `cowrie.client.kex` |
| `2026-06-23 15:11:10` | `cowrie.login.success` |
| `2026-06-23 15:11:10` | `cowrie.session.params` |
| `2026-06-23 15:11:10` | `cowrie.command.input` |
| `2026-06-23 15:11:10` | `cowrie.log.closed` |
| `2026-06-23 15:11:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcec1983b213

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:12 |
| **Last Seen** | 2026-06-23 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:12:17` | `cowrie.session.connect` |
| `2026-06-23 15:12:17` | `cowrie.client.version` |
| `2026-06-23 15:12:17` | `cowrie.client.kex` |
| `2026-06-23 15:12:18` | `cowrie.login.success` |
| `2026-06-23 15:12:18` | `cowrie.session.params` |
| `2026-06-23 15:12:18` | `cowrie.command.input` |
| `2026-06-23 15:12:19` | `cowrie.log.closed` |
| `2026-06-23 15:12:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c97c528eb8f9

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-23 15:12 |
| **Last Seen** | 2026-06-23 15:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:12:41` | `cowrie.session.connect` |
| `2026-06-23 15:12:41` | `cowrie.client.version` |
| `2026-06-23 15:12:41` | `cowrie.client.kex` |
| `2026-06-23 15:12:42` | `cowrie.login.success` |
| `2026-06-23 15:12:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91debb0cd347

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-23 15:12 |
| **Last Seen** | 2026-06-23 15:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:12:42` | `cowrie.session.connect` |
| `2026-06-23 15:12:42` | `cowrie.client.version` |
| `2026-06-23 15:12:42` | `cowrie.client.kex` |
| `2026-06-23 15:12:42` | `cowrie.login.success` |
| `2026-06-23 15:12:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b0b46443883

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-23 15:12 |
| **Last Seen** | 2026-06-23 15:15 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:12:58` | `cowrie.session.connect` |
| `2026-06-23 15:12:58` | `cowrie.client.version` |
| `2026-06-23 15:12:59` | `cowrie.client.kex` |
| `2026-06-23 15:12:59` | `cowrie.login.success` |
| `2026-06-23 15:13:00` | `cowrie.session.file_upload` |
| `2026-06-23 15:13:01` | `cowrie.session.params` |
| `2026-06-23 15:13:01` | `cowrie.command.input` |
| `2026-06-23 15:13:01` | `cowrie.command.input` |
| `2026-06-23 15:13:01` | `cowrie.command.input` |
| `2026-06-23 15:13:01` | `cowrie.command.failed` |
| `2026-06-23 15:13:01` | `cowrie.log.closed` |
| `2026-06-23 15:13:02` | `cowrie.session.params` |
| `2026-06-23 15:13:02` | `cowrie.command.input` |
| `2026-06-23 15:13:02` | `cowrie.log.closed` |
| `2026-06-23 15:13:02` | `cowrie.session.params` |
| `2026-06-23 15:13:02` | `cowrie.command.input` |
| `2026-06-23 15:13:03` | `cowrie.log.closed` |
| `2026-06-23 15:13:03` | `cowrie.session.params` |
| `2026-06-23 15:13:03` | `cowrie.command.input` |
| `2026-06-23 15:13:03` | `cowrie.command.failed` |
| `2026-06-23 15:13:03` | `cowrie.command.failed` |
| `2026-06-23 15:14:04` | `cowrie.session.params` |
| `2026-06-23 15:14:04` | `cowrie.command.input` |
| `2026-06-23 15:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de4769fefb9a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 15:13 |
| **Last Seen** | 2026-06-23 15:13 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:13:19` | `cowrie.session.connect` |
| `2026-06-23 15:13:21` | `cowrie.client.version` |
| `2026-06-23 15:13:21` | `cowrie.client.kex` |
| `2026-06-23 15:13:27` | `cowrie.login.success` |
| `2026-06-23 15:13:30` | `cowrie.session.params` |
| `2026-06-23 15:13:30` | `cowrie.command.input` |
| `2026-06-23 15:13:32` | `cowrie.log.closed` |
| `2026-06-23 15:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9f6a9424395

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:13 |
| **Last Seen** | 2026-06-23 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:13:21` | `cowrie.session.connect` |
| `2026-06-23 15:13:21` | `cowrie.client.version` |
| `2026-06-23 15:13:21` | `cowrie.client.kex` |
| `2026-06-23 15:13:21` | `cowrie.login.success` |
| `2026-06-23 15:13:22` | `cowrie.session.params` |
| `2026-06-23 15:13:22` | `cowrie.command.input` |
| `2026-06-23 15:13:22` | `cowrie.log.closed` |
| `2026-06-23 15:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cf92fa90fcc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:14 |
| **Last Seen** | 2026-06-23 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:14:24` | `cowrie.session.connect` |
| `2026-06-23 15:14:24` | `cowrie.client.version` |
| `2026-06-23 15:14:24` | `cowrie.client.kex` |
| `2026-06-23 15:14:24` | `cowrie.login.success` |
| `2026-06-23 15:14:25` | `cowrie.session.params` |
| `2026-06-23 15:14:25` | `cowrie.command.input` |
| `2026-06-23 15:14:25` | `cowrie.log.closed` |
| `2026-06-23 15:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-943b77b608bd

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-23 15:15 |
| **Last Seen** | 2026-06-23 15:17 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:15:20` | `cowrie.session.connect` |
| `2026-06-23 15:15:20` | `cowrie.client.version` |
| `2026-06-23 15:15:20` | `cowrie.client.kex` |
| `2026-06-23 15:15:20` | `cowrie.login.success` |
| `2026-06-23 15:15:21` | `cowrie.session.file_upload` |
| `2026-06-23 15:15:22` | `cowrie.session.params` |
| `2026-06-23 15:15:22` | `cowrie.command.input` |
| `2026-06-23 15:15:22` | `cowrie.command.input` |
| `2026-06-23 15:15:22` | `cowrie.command.input` |
| `2026-06-23 15:15:22` | `cowrie.command.failed` |
| `2026-06-23 15:15:22` | `cowrie.log.closed` |
| `2026-06-23 15:15:23` | `cowrie.session.params` |
| `2026-06-23 15:15:23` | `cowrie.command.input` |
| `2026-06-23 15:15:23` | `cowrie.log.closed` |
| `2026-06-23 15:15:24` | `cowrie.session.params` |
| `2026-06-23 15:15:24` | `cowrie.command.input` |
| `2026-06-23 15:15:24` | `cowrie.log.closed` |
| `2026-06-23 15:15:25` | `cowrie.session.params` |
| `2026-06-23 15:15:25` | `cowrie.command.input` |
| `2026-06-23 15:15:25` | `cowrie.command.failed` |
| `2026-06-23 15:15:25` | `cowrie.command.failed` |
| `2026-06-23 15:16:25` | `cowrie.session.params` |
| `2026-06-23 15:16:25` | `cowrie.command.input` |
| `2026-06-23 15:17:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c4b5cd530b1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:15 |
| **Last Seen** | 2026-06-23 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:15:28` | `cowrie.session.connect` |
| `2026-06-23 15:15:28` | `cowrie.client.version` |
| `2026-06-23 15:15:28` | `cowrie.client.kex` |
| `2026-06-23 15:15:29` | `cowrie.login.success` |
| `2026-06-23 15:15:29` | `cowrie.session.params` |
| `2026-06-23 15:15:29` | `cowrie.command.input` |
| `2026-06-23 15:15:30` | `cowrie.log.closed` |
| `2026-06-23 15:15:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f709f014f830

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:16 |
| **Last Seen** | 2026-06-23 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:16:37` | `cowrie.session.connect` |
| `2026-06-23 15:16:37` | `cowrie.client.version` |
| `2026-06-23 15:16:37` | `cowrie.client.kex` |
| `2026-06-23 15:16:38` | `cowrie.login.success` |
| `2026-06-23 15:16:39` | `cowrie.session.params` |
| `2026-06-23 15:16:39` | `cowrie.command.input` |
| `2026-06-23 15:16:39` | `cowrie.log.closed` |
| `2026-06-23 15:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe5d33ea2d08

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:17 |
| **Last Seen** | 2026-06-23 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:17:45` | `cowrie.session.connect` |
| `2026-06-23 15:17:45` | `cowrie.client.version` |
| `2026-06-23 15:17:45` | `cowrie.client.kex` |
| `2026-06-23 15:17:45` | `cowrie.login.success` |
| `2026-06-23 15:17:46` | `cowrie.session.params` |
| `2026-06-23 15:17:46` | `cowrie.command.input` |
| `2026-06-23 15:17:46` | `cowrie.log.closed` |
| `2026-06-23 15:17:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c502539cef9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:18 |
| **Last Seen** | 2026-06-23 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:18:51` | `cowrie.session.connect` |
| `2026-06-23 15:18:51` | `cowrie.client.version` |
| `2026-06-23 15:18:52` | `cowrie.client.kex` |
| `2026-06-23 15:18:52` | `cowrie.login.success` |
| `2026-06-23 15:18:53` | `cowrie.session.params` |
| `2026-06-23 15:18:53` | `cowrie.command.input` |
| `2026-06-23 15:18:53` | `cowrie.log.closed` |
| `2026-06-23 15:18:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b00f32960e88

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:19 |
| **Last Seen** | 2026-06-23 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:19:53` | `cowrie.session.connect` |
| `2026-06-23 15:19:53` | `cowrie.client.version` |
| `2026-06-23 15:19:53` | `cowrie.client.kex` |
| `2026-06-23 15:19:53` | `cowrie.login.success` |
| `2026-06-23 15:19:54` | `cowrie.session.params` |
| `2026-06-23 15:19:54` | `cowrie.command.input` |
| `2026-06-23 15:19:54` | `cowrie.log.closed` |
| `2026-06-23 15:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89fe5f72c0a9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:20 |
| **Last Seen** | 2026-06-23 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:20:58` | `cowrie.session.connect` |
| `2026-06-23 15:20:58` | `cowrie.client.version` |
| `2026-06-23 15:20:58` | `cowrie.client.kex` |
| `2026-06-23 15:20:58` | `cowrie.login.success` |
| `2026-06-23 15:20:59` | `cowrie.session.params` |
| `2026-06-23 15:20:59` | `cowrie.command.input` |
| `2026-06-23 15:20:59` | `cowrie.log.closed` |
| `2026-06-23 15:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f7a44623e85

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:22 |
| **Last Seen** | 2026-06-23 15:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:22:02` | `cowrie.session.connect` |
| `2026-06-23 15:22:02` | `cowrie.client.version` |
| `2026-06-23 15:22:02` | `cowrie.client.kex` |
| `2026-06-23 15:22:02` | `cowrie.login.success` |
| `2026-06-23 15:22:03` | `cowrie.session.params` |
| `2026-06-23 15:22:03` | `cowrie.command.input` |
| `2026-06-23 15:22:03` | `cowrie.log.closed` |
| `2026-06-23 15:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d2952d3e885

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:23 |
| **Last Seen** | 2026-06-23 15:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:23:03` | `cowrie.session.connect` |
| `2026-06-23 15:23:03` | `cowrie.client.version` |
| `2026-06-23 15:23:03` | `cowrie.client.kex` |
| `2026-06-23 15:23:03` | `cowrie.login.success` |
| `2026-06-23 15:23:04` | `cowrie.session.params` |
| `2026-06-23 15:23:04` | `cowrie.command.input` |
| `2026-06-23 15:23:04` | `cowrie.log.closed` |
| `2026-06-23 15:23:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9acb01c2df0e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:24 |
| **Last Seen** | 2026-06-23 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:24:05` | `cowrie.session.connect` |
| `2026-06-23 15:24:05` | `cowrie.client.version` |
| `2026-06-23 15:24:05` | `cowrie.client.kex` |
| `2026-06-23 15:24:06` | `cowrie.login.success` |
| `2026-06-23 15:24:06` | `cowrie.session.params` |
| `2026-06-23 15:24:06` | `cowrie.command.input` |
| `2026-06-23 15:24:06` | `cowrie.log.closed` |
| `2026-06-23 15:24:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-385140fc94b3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:25 |
| **Last Seen** | 2026-06-23 15:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:25:09` | `cowrie.session.connect` |
| `2026-06-23 15:25:09` | `cowrie.client.version` |
| `2026-06-23 15:25:09` | `cowrie.client.kex` |
| `2026-06-23 15:25:09` | `cowrie.login.success` |
| `2026-06-23 15:25:10` | `cowrie.session.params` |
| `2026-06-23 15:25:10` | `cowrie.command.input` |
| `2026-06-23 15:25:10` | `cowrie.log.closed` |
| `2026-06-23 15:25:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ce1a106168a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:26 |
| **Last Seen** | 2026-06-23 15:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:26:16` | `cowrie.session.connect` |
| `2026-06-23 15:26:16` | `cowrie.client.version` |
| `2026-06-23 15:26:16` | `cowrie.client.kex` |
| `2026-06-23 15:26:17` | `cowrie.login.success` |
| `2026-06-23 15:26:17` | `cowrie.session.params` |
| `2026-06-23 15:26:17` | `cowrie.command.input` |
| `2026-06-23 15:26:17` | `cowrie.log.closed` |
| `2026-06-23 15:26:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aba42248648

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:27 |
| **Last Seen** | 2026-06-23 15:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:27:24` | `cowrie.session.connect` |
| `2026-06-23 15:27:24` | `cowrie.client.version` |
| `2026-06-23 15:27:25` | `cowrie.client.kex` |
| `2026-06-23 15:27:25` | `cowrie.login.success` |
| `2026-06-23 15:27:27` | `cowrie.session.params` |
| `2026-06-23 15:27:27` | `cowrie.command.input` |
| `2026-06-23 15:27:27` | `cowrie.log.closed` |
| `2026-06-23 15:27:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8542d369f94d

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 15:28 |
| **Last Seen** | 2026-06-23 15:28 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:28:17` | `cowrie.session.connect` |
| `2026-06-23 15:28:18` | `cowrie.client.version` |
| `2026-06-23 15:28:18` | `cowrie.client.kex` |
| `2026-06-23 15:28:25` | `cowrie.login.success` |
| `2026-06-23 15:28:29` | `cowrie.session.params` |
| `2026-06-23 15:28:29` | `cowrie.command.input` |
| `2026-06-23 15:28:31` | `cowrie.log.closed` |
| `2026-06-23 15:28:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c338f654098f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:28 |
| **Last Seen** | 2026-06-23 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:28:27` | `cowrie.session.connect` |
| `2026-06-23 15:28:27` | `cowrie.client.version` |
| `2026-06-23 15:28:27` | `cowrie.client.kex` |
| `2026-06-23 15:28:28` | `cowrie.login.success` |
| `2026-06-23 15:28:29` | `cowrie.session.params` |
| `2026-06-23 15:28:29` | `cowrie.command.input` |
| `2026-06-23 15:28:29` | `cowrie.log.closed` |
| `2026-06-23 15:28:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-808dd23a6ac3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:29 |
| **Last Seen** | 2026-06-23 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:29:29` | `cowrie.session.connect` |
| `2026-06-23 15:29:29` | `cowrie.client.version` |
| `2026-06-23 15:29:29` | `cowrie.client.kex` |
| `2026-06-23 15:29:30` | `cowrie.login.success` |
| `2026-06-23 15:29:30` | `cowrie.session.params` |
| `2026-06-23 15:29:30` | `cowrie.command.input` |
| `2026-06-23 15:29:31` | `cowrie.log.closed` |
| `2026-06-23 15:29:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55fc7e6aee1c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:30 |
| **Last Seen** | 2026-06-23 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:30:32` | `cowrie.session.connect` |
| `2026-06-23 15:30:32` | `cowrie.client.version` |
| `2026-06-23 15:30:32` | `cowrie.client.kex` |
| `2026-06-23 15:30:32` | `cowrie.login.success` |
| `2026-06-23 15:30:33` | `cowrie.session.params` |
| `2026-06-23 15:30:33` | `cowrie.command.input` |
| `2026-06-23 15:30:33` | `cowrie.log.closed` |
| `2026-06-23 15:30:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7f14d04fd7f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:31 |
| **Last Seen** | 2026-06-23 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:31:37` | `cowrie.session.connect` |
| `2026-06-23 15:31:37` | `cowrie.client.version` |
| `2026-06-23 15:31:37` | `cowrie.client.kex` |
| `2026-06-23 15:31:38` | `cowrie.login.success` |
| `2026-06-23 15:31:38` | `cowrie.session.params` |
| `2026-06-23 15:31:38` | `cowrie.command.input` |
| `2026-06-23 15:31:38` | `cowrie.log.closed` |
| `2026-06-23 15:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d3a05496782

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:32 |
| **Last Seen** | 2026-06-23 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:32:41` | `cowrie.session.connect` |
| `2026-06-23 15:32:41` | `cowrie.client.version` |
| `2026-06-23 15:32:41` | `cowrie.client.kex` |
| `2026-06-23 15:32:42` | `cowrie.login.success` |
| `2026-06-23 15:32:42` | `cowrie.session.params` |
| `2026-06-23 15:32:42` | `cowrie.command.input` |
| `2026-06-23 15:32:43` | `cowrie.log.closed` |
| `2026-06-23 15:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f174df41c7e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:33 |
| **Last Seen** | 2026-06-23 15:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:33:47` | `cowrie.session.connect` |
| `2026-06-23 15:33:47` | `cowrie.client.version` |
| `2026-06-23 15:33:47` | `cowrie.client.kex` |
| `2026-06-23 15:33:47` | `cowrie.login.success` |
| `2026-06-23 15:33:48` | `cowrie.session.params` |
| `2026-06-23 15:33:48` | `cowrie.command.input` |
| `2026-06-23 15:33:48` | `cowrie.log.closed` |
| `2026-06-23 15:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfadef3cd296

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:34 |
| **Last Seen** | 2026-06-23 15:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:34:55` | `cowrie.session.connect` |
| `2026-06-23 15:34:55` | `cowrie.client.version` |
| `2026-06-23 15:34:55` | `cowrie.client.kex` |
| `2026-06-23 15:34:55` | `cowrie.login.success` |
| `2026-06-23 15:34:56` | `cowrie.session.params` |
| `2026-06-23 15:34:56` | `cowrie.command.input` |
| `2026-06-23 15:34:56` | `cowrie.log.closed` |
| `2026-06-23 15:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ee26e138769

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:36 |
| **Last Seen** | 2026-06-23 15:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:36:00` | `cowrie.session.connect` |
| `2026-06-23 15:36:00` | `cowrie.client.version` |
| `2026-06-23 15:36:00` | `cowrie.client.kex` |
| `2026-06-23 15:36:01` | `cowrie.login.success` |
| `2026-06-23 15:36:01` | `cowrie.session.params` |
| `2026-06-23 15:36:01` | `cowrie.command.input` |
| `2026-06-23 15:36:02` | `cowrie.log.closed` |
| `2026-06-23 15:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-743258c3cf0b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:37 |
| **Last Seen** | 2026-06-23 15:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:37:06` | `cowrie.session.connect` |
| `2026-06-23 15:37:06` | `cowrie.client.version` |
| `2026-06-23 15:37:07` | `cowrie.client.kex` |
| `2026-06-23 15:37:07` | `cowrie.login.success` |
| `2026-06-23 15:37:08` | `cowrie.session.params` |
| `2026-06-23 15:37:08` | `cowrie.command.input` |
| `2026-06-23 15:37:08` | `cowrie.log.closed` |
| `2026-06-23 15:37:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76f7a5dbdd28

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:38 |
| **Last Seen** | 2026-06-23 15:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:38:12` | `cowrie.session.connect` |
| `2026-06-23 15:38:12` | `cowrie.client.version` |
| `2026-06-23 15:38:12` | `cowrie.client.kex` |
| `2026-06-23 15:38:13` | `cowrie.login.success` |
| `2026-06-23 15:38:14` | `cowrie.session.params` |
| `2026-06-23 15:38:14` | `cowrie.command.input` |
| `2026-06-23 15:38:14` | `cowrie.log.closed` |
| `2026-06-23 15:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9468d4f79c04

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:39 |
| **Last Seen** | 2026-06-23 15:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:39:19` | `cowrie.session.connect` |
| `2026-06-23 15:39:19` | `cowrie.client.version` |
| `2026-06-23 15:39:19` | `cowrie.client.kex` |
| `2026-06-23 15:39:19` | `cowrie.login.success` |
| `2026-06-23 15:39:20` | `cowrie.session.params` |
| `2026-06-23 15:39:20` | `cowrie.command.input` |
| `2026-06-23 15:39:20` | `cowrie.log.closed` |
| `2026-06-23 15:39:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b55cafbcad09

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:40 |
| **Last Seen** | 2026-06-23 15:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:40:25` | `cowrie.session.connect` |
| `2026-06-23 15:40:25` | `cowrie.client.version` |
| `2026-06-23 15:40:25` | `cowrie.client.kex` |
| `2026-06-23 15:40:25` | `cowrie.login.success` |
| `2026-06-23 15:40:26` | `cowrie.session.params` |
| `2026-06-23 15:40:26` | `cowrie.command.input` |
| `2026-06-23 15:40:26` | `cowrie.log.closed` |
| `2026-06-23 15:40:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b19ddd27ba2b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:41 |
| **Last Seen** | 2026-06-23 15:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:41:30` | `cowrie.session.connect` |
| `2026-06-23 15:41:30` | `cowrie.client.version` |
| `2026-06-23 15:41:30` | `cowrie.client.kex` |
| `2026-06-23 15:41:31` | `cowrie.login.success` |
| `2026-06-23 15:41:32` | `cowrie.session.params` |
| `2026-06-23 15:41:32` | `cowrie.command.input` |
| `2026-06-23 15:41:32` | `cowrie.log.closed` |
| `2026-06-23 15:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-608f62b60ad1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:42 |
| **Last Seen** | 2026-06-23 15:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:42:36` | `cowrie.session.connect` |
| `2026-06-23 15:42:36` | `cowrie.client.version` |
| `2026-06-23 15:42:36` | `cowrie.client.kex` |
| `2026-06-23 15:42:37` | `cowrie.login.success` |
| `2026-06-23 15:42:37` | `cowrie.session.params` |
| `2026-06-23 15:42:37` | `cowrie.command.input` |
| `2026-06-23 15:42:38` | `cowrie.log.closed` |
| `2026-06-23 15:42:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f8be4cb70f8

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 15:42 |
| **Last Seen** | 2026-06-23 15:43 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:42:53` | `cowrie.session.connect` |
| `2026-06-23 15:42:54` | `cowrie.client.version` |
| `2026-06-23 15:42:54` | `cowrie.client.kex` |
| `2026-06-23 15:43:01` | `cowrie.login.success` |
| `2026-06-23 15:43:05` | `cowrie.session.params` |
| `2026-06-23 15:43:05` | `cowrie.command.input` |
| `2026-06-23 15:43:07` | `cowrie.log.closed` |
| `2026-06-23 15:43:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be837eb49c93

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:43 |
| **Last Seen** | 2026-06-23 15:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:43:40` | `cowrie.session.connect` |
| `2026-06-23 15:43:40` | `cowrie.client.version` |
| `2026-06-23 15:43:40` | `cowrie.client.kex` |
| `2026-06-23 15:43:40` | `cowrie.login.success` |
| `2026-06-23 15:43:41` | `cowrie.session.params` |
| `2026-06-23 15:43:41` | `cowrie.command.input` |
| `2026-06-23 15:43:41` | `cowrie.log.closed` |
| `2026-06-23 15:43:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-449ef6cf3d84

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:44 |
| **Last Seen** | 2026-06-23 15:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:44:47` | `cowrie.session.connect` |
| `2026-06-23 15:44:47` | `cowrie.client.version` |
| `2026-06-23 15:44:47` | `cowrie.client.kex` |
| `2026-06-23 15:44:47` | `cowrie.login.success` |
| `2026-06-23 15:44:48` | `cowrie.session.params` |
| `2026-06-23 15:44:48` | `cowrie.command.input` |
| `2026-06-23 15:44:48` | `cowrie.log.closed` |
| `2026-06-23 15:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f6a0711062c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:45 |
| **Last Seen** | 2026-06-23 15:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:45:54` | `cowrie.session.connect` |
| `2026-06-23 15:45:54` | `cowrie.client.version` |
| `2026-06-23 15:45:54` | `cowrie.client.kex` |
| `2026-06-23 15:45:55` | `cowrie.login.success` |
| `2026-06-23 15:45:55` | `cowrie.session.params` |
| `2026-06-23 15:45:55` | `cowrie.command.input` |
| `2026-06-23 15:45:56` | `cowrie.log.closed` |
| `2026-06-23 15:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e8120185c04

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:47 |
| **Last Seen** | 2026-06-23 15:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:47:04` | `cowrie.session.connect` |
| `2026-06-23 15:47:04` | `cowrie.client.version` |
| `2026-06-23 15:47:04` | `cowrie.client.kex` |
| `2026-06-23 15:47:04` | `cowrie.login.success` |
| `2026-06-23 15:47:05` | `cowrie.session.params` |
| `2026-06-23 15:47:05` | `cowrie.command.input` |
| `2026-06-23 15:47:05` | `cowrie.log.closed` |
| `2026-06-23 15:47:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1dfe43671bb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:48 |
| **Last Seen** | 2026-06-23 15:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:48:08` | `cowrie.session.connect` |
| `2026-06-23 15:48:08` | `cowrie.client.version` |
| `2026-06-23 15:48:08` | `cowrie.client.kex` |
| `2026-06-23 15:48:08` | `cowrie.login.success` |
| `2026-06-23 15:48:09` | `cowrie.session.params` |
| `2026-06-23 15:48:09` | `cowrie.command.input` |
| `2026-06-23 15:48:09` | `cowrie.log.closed` |
| `2026-06-23 15:48:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-564c18a35593

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:49 |
| **Last Seen** | 2026-06-23 15:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:49:09` | `cowrie.session.connect` |
| `2026-06-23 15:49:09` | `cowrie.client.version` |
| `2026-06-23 15:49:09` | `cowrie.client.kex` |
| `2026-06-23 15:49:09` | `cowrie.login.success` |
| `2026-06-23 15:49:10` | `cowrie.session.params` |
| `2026-06-23 15:49:10` | `cowrie.command.input` |
| `2026-06-23 15:49:10` | `cowrie.log.closed` |
| `2026-06-23 15:49:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ada597ada32

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:50 |
| **Last Seen** | 2026-06-23 15:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:50:11` | `cowrie.session.connect` |
| `2026-06-23 15:50:11` | `cowrie.client.version` |
| `2026-06-23 15:50:11` | `cowrie.client.kex` |
| `2026-06-23 15:50:11` | `cowrie.login.success` |
| `2026-06-23 15:50:12` | `cowrie.session.params` |
| `2026-06-23 15:50:12` | `cowrie.command.input` |
| `2026-06-23 15:50:12` | `cowrie.log.closed` |
| `2026-06-23 15:50:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd512f7618b8

| Field | Detail |
|---|---|
| **Source IP** | `106.63.6[.]210` |
| **First Seen** | 2026-06-23 15:50 |
| **Last Seen** | 2026-06-23 15:55 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:50:54` | `cowrie.session.connect` |
| `2026-06-23 15:50:55` | `cowrie.client.version` |
| `2026-06-23 15:50:55` | `cowrie.client.kex` |
| `2026-06-23 15:50:56` | `cowrie.login.success` |
| `2026-06-23 15:55:56` | `cowrie.session.file_upload` |
| `2026-06-23 15:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.63.6[.]210` to AbuseIPDB if not already reported
- [ ] Block `106.63.6[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b5c64464d49

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:51 |
| **Last Seen** | 2026-06-23 15:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:51:14` | `cowrie.session.connect` |
| `2026-06-23 15:51:14` | `cowrie.client.version` |
| `2026-06-23 15:51:14` | `cowrie.client.kex` |
| `2026-06-23 15:51:14` | `cowrie.login.success` |
| `2026-06-23 15:51:15` | `cowrie.session.params` |
| `2026-06-23 15:51:15` | `cowrie.command.input` |
| `2026-06-23 15:51:15` | `cowrie.log.closed` |
| `2026-06-23 15:51:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e8488036a33

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:52 |
| **Last Seen** | 2026-06-23 15:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:52:18` | `cowrie.session.connect` |
| `2026-06-23 15:52:18` | `cowrie.client.version` |
| `2026-06-23 15:52:18` | `cowrie.client.kex` |
| `2026-06-23 15:52:18` | `cowrie.login.success` |
| `2026-06-23 15:52:19` | `cowrie.session.params` |
| `2026-06-23 15:52:19` | `cowrie.command.input` |
| `2026-06-23 15:52:19` | `cowrie.log.closed` |
| `2026-06-23 15:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-691f7818f13e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:53 |
| **Last Seen** | 2026-06-23 15:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:53:25` | `cowrie.session.connect` |
| `2026-06-23 15:53:25` | `cowrie.client.version` |
| `2026-06-23 15:53:25` | `cowrie.client.kex` |
| `2026-06-23 15:53:25` | `cowrie.login.success` |
| `2026-06-23 15:53:26` | `cowrie.session.params` |
| `2026-06-23 15:53:26` | `cowrie.command.input` |
| `2026-06-23 15:53:26` | `cowrie.log.closed` |
| `2026-06-23 15:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83cc0c2acfc3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:54 |
| **Last Seen** | 2026-06-23 15:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:54:20` | `cowrie.session.connect` |
| `2026-06-23 15:54:20` | `cowrie.client.version` |
| `2026-06-23 15:54:20` | `cowrie.client.kex` |
| `2026-06-23 15:54:20` | `cowrie.login.success` |
| `2026-06-23 15:54:21` | `cowrie.session.params` |
| `2026-06-23 15:54:21` | `cowrie.command.input` |
| `2026-06-23 15:54:21` | `cowrie.log.closed` |
| `2026-06-23 15:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-641e482ce54b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:55 |
| **Last Seen** | 2026-06-23 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:55:16` | `cowrie.session.connect` |
| `2026-06-23 15:55:16` | `cowrie.client.version` |
| `2026-06-23 15:55:16` | `cowrie.client.kex` |
| `2026-06-23 15:55:16` | `cowrie.login.success` |
| `2026-06-23 15:55:17` | `cowrie.session.params` |
| `2026-06-23 15:55:17` | `cowrie.command.input` |
| `2026-06-23 15:55:17` | `cowrie.log.closed` |
| `2026-06-23 15:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4e8a97f8ebc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:56 |
| **Last Seen** | 2026-06-23 15:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:56:17` | `cowrie.session.connect` |
| `2026-06-23 15:56:17` | `cowrie.client.version` |
| `2026-06-23 15:56:17` | `cowrie.client.kex` |
| `2026-06-23 15:56:17` | `cowrie.login.success` |
| `2026-06-23 15:56:18` | `cowrie.session.params` |
| `2026-06-23 15:56:18` | `cowrie.command.input` |
| `2026-06-23 15:56:18` | `cowrie.log.closed` |
| `2026-06-23 15:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3127f05aa844

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:57 |
| **Last Seen** | 2026-06-23 15:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:57:13` | `cowrie.session.connect` |
| `2026-06-23 15:57:13` | `cowrie.client.version` |
| `2026-06-23 15:57:13` | `cowrie.client.kex` |
| `2026-06-23 15:57:13` | `cowrie.login.success` |
| `2026-06-23 15:57:14` | `cowrie.session.params` |
| `2026-06-23 15:57:14` | `cowrie.command.input` |
| `2026-06-23 15:57:14` | `cowrie.log.closed` |
| `2026-06-23 15:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-378a9dd834ed

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 15:57 |
| **Last Seen** | 2026-06-23 15:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:57:15` | `cowrie.session.connect` |
| `2026-06-23 15:57:17` | `cowrie.client.version` |
| `2026-06-23 15:57:17` | `cowrie.client.kex` |
| `2026-06-23 15:57:23` | `cowrie.login.success` |
| `2026-06-23 15:57:27` | `cowrie.session.params` |
| `2026-06-23 15:57:27` | `cowrie.command.input` |
| `2026-06-23 15:57:28` | `cowrie.log.closed` |
| `2026-06-23 15:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eb16b268cfc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:58 |
| **Last Seen** | 2026-06-23 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:58:10` | `cowrie.session.connect` |
| `2026-06-23 15:58:10` | `cowrie.client.version` |
| `2026-06-23 15:58:10` | `cowrie.client.kex` |
| `2026-06-23 15:58:10` | `cowrie.login.success` |
| `2026-06-23 15:58:11` | `cowrie.session.params` |
| `2026-06-23 15:58:11` | `cowrie.command.input` |
| `2026-06-23 15:58:11` | `cowrie.log.closed` |
| `2026-06-23 15:58:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7158cdb18fe3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 15:59 |
| **Last Seen** | 2026-06-23 15:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 15:59:13` | `cowrie.session.connect` |
| `2026-06-23 15:59:13` | `cowrie.client.version` |
| `2026-06-23 15:59:13` | `cowrie.client.kex` |
| `2026-06-23 15:59:13` | `cowrie.login.success` |
| `2026-06-23 15:59:14` | `cowrie.session.params` |
| `2026-06-23 15:59:14` | `cowrie.command.input` |
| `2026-06-23 15:59:14` | `cowrie.log.closed` |
| `2026-06-23 15:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa991dd6c30f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:00 |
| **Last Seen** | 2026-06-23 16:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:00:11` | `cowrie.session.connect` |
| `2026-06-23 16:00:11` | `cowrie.client.version` |
| `2026-06-23 16:00:11` | `cowrie.client.kex` |
| `2026-06-23 16:00:12` | `cowrie.login.success` |
| `2026-06-23 16:00:13` | `cowrie.session.params` |
| `2026-06-23 16:00:13` | `cowrie.command.input` |
| `2026-06-23 16:00:13` | `cowrie.log.closed` |
| `2026-06-23 16:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16e240a5457c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:00 |
| **Last Seen** | 2026-06-23 16:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:00:56` | `cowrie.session.connect` |
| `2026-06-23 16:00:56` | `cowrie.client.version` |
| `2026-06-23 16:00:56` | `cowrie.client.kex` |
| `2026-06-23 16:00:57` | `cowrie.login.success` |
| `2026-06-23 16:00:57` | `cowrie.session.params` |
| `2026-06-23 16:00:57` | `cowrie.command.input` |
| `2026-06-23 16:00:58` | `cowrie.log.closed` |
| `2026-06-23 16:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79ecaae50d81

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:01 |
| **Last Seen** | 2026-06-23 16:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:01:40` | `cowrie.session.connect` |
| `2026-06-23 16:01:40` | `cowrie.client.version` |
| `2026-06-23 16:01:40` | `cowrie.client.kex` |
| `2026-06-23 16:01:40` | `cowrie.login.success` |
| `2026-06-23 16:01:41` | `cowrie.session.params` |
| `2026-06-23 16:01:41` | `cowrie.command.input` |
| `2026-06-23 16:01:41` | `cowrie.log.closed` |
| `2026-06-23 16:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec33bda7482d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:02 |
| **Last Seen** | 2026-06-23 16:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:02:23` | `cowrie.session.connect` |
| `2026-06-23 16:02:23` | `cowrie.client.version` |
| `2026-06-23 16:02:23` | `cowrie.client.kex` |
| `2026-06-23 16:02:23` | `cowrie.login.success` |
| `2026-06-23 16:02:24` | `cowrie.session.params` |
| `2026-06-23 16:02:24` | `cowrie.command.input` |
| `2026-06-23 16:02:24` | `cowrie.log.closed` |
| `2026-06-23 16:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-589a0ef2e9cc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:03 |
| **Last Seen** | 2026-06-23 16:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:03:08` | `cowrie.session.connect` |
| `2026-06-23 16:03:08` | `cowrie.client.version` |
| `2026-06-23 16:03:08` | `cowrie.client.kex` |
| `2026-06-23 16:03:08` | `cowrie.login.success` |
| `2026-06-23 16:03:09` | `cowrie.session.params` |
| `2026-06-23 16:03:09` | `cowrie.command.input` |
| `2026-06-23 16:03:09` | `cowrie.log.closed` |
| `2026-06-23 16:03:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbd957e6dff6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:03 |
| **Last Seen** | 2026-06-23 16:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:03:52` | `cowrie.session.connect` |
| `2026-06-23 16:03:52` | `cowrie.client.version` |
| `2026-06-23 16:03:52` | `cowrie.client.kex` |
| `2026-06-23 16:03:52` | `cowrie.login.success` |
| `2026-06-23 16:03:53` | `cowrie.session.params` |
| `2026-06-23 16:03:53` | `cowrie.command.input` |
| `2026-06-23 16:03:53` | `cowrie.log.closed` |
| `2026-06-23 16:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b36b2973b116

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:04 |
| **Last Seen** | 2026-06-23 16:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:04:41` | `cowrie.session.connect` |
| `2026-06-23 16:04:41` | `cowrie.client.version` |
| `2026-06-23 16:04:41` | `cowrie.client.kex` |
| `2026-06-23 16:04:41` | `cowrie.login.success` |
| `2026-06-23 16:04:42` | `cowrie.session.params` |
| `2026-06-23 16:04:42` | `cowrie.command.input` |
| `2026-06-23 16:04:42` | `cowrie.log.closed` |
| `2026-06-23 16:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71f597ad4263

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:05 |
| **Last Seen** | 2026-06-23 16:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:05:31` | `cowrie.session.connect` |
| `2026-06-23 16:05:31` | `cowrie.client.version` |
| `2026-06-23 16:05:32` | `cowrie.client.kex` |
| `2026-06-23 16:05:32` | `cowrie.login.success` |
| `2026-06-23 16:05:33` | `cowrie.session.params` |
| `2026-06-23 16:05:33` | `cowrie.command.input` |
| `2026-06-23 16:05:33` | `cowrie.log.closed` |
| `2026-06-23 16:05:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c8b85f17749

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:06 |
| **Last Seen** | 2026-06-23 16:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:06:17` | `cowrie.session.connect` |
| `2026-06-23 16:06:17` | `cowrie.client.version` |
| `2026-06-23 16:06:17` | `cowrie.client.kex` |
| `2026-06-23 16:06:18` | `cowrie.login.success` |
| `2026-06-23 16:06:18` | `cowrie.session.params` |
| `2026-06-23 16:06:18` | `cowrie.command.input` |
| `2026-06-23 16:06:19` | `cowrie.log.closed` |
| `2026-06-23 16:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-365bb3c1a21e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:07 |
| **Last Seen** | 2026-06-23 16:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:07:06` | `cowrie.session.connect` |
| `2026-06-23 16:07:06` | `cowrie.client.version` |
| `2026-06-23 16:07:06` | `cowrie.client.kex` |
| `2026-06-23 16:07:06` | `cowrie.login.success` |
| `2026-06-23 16:07:07` | `cowrie.session.params` |
| `2026-06-23 16:07:07` | `cowrie.command.input` |
| `2026-06-23 16:07:07` | `cowrie.log.closed` |
| `2026-06-23 16:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bcce87d5696

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:07 |
| **Last Seen** | 2026-06-23 16:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:07:51` | `cowrie.session.connect` |
| `2026-06-23 16:07:51` | `cowrie.client.version` |
| `2026-06-23 16:07:51` | `cowrie.client.kex` |
| `2026-06-23 16:07:52` | `cowrie.login.success` |
| `2026-06-23 16:07:52` | `cowrie.session.params` |
| `2026-06-23 16:07:52` | `cowrie.command.input` |
| `2026-06-23 16:07:53` | `cowrie.log.closed` |
| `2026-06-23 16:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d597908c99f2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:08 |
| **Last Seen** | 2026-06-23 16:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:08:35` | `cowrie.session.connect` |
| `2026-06-23 16:08:35` | `cowrie.client.version` |
| `2026-06-23 16:08:35` | `cowrie.client.kex` |
| `2026-06-23 16:08:35` | `cowrie.login.success` |
| `2026-06-23 16:08:36` | `cowrie.session.params` |
| `2026-06-23 16:08:36` | `cowrie.command.input` |
| `2026-06-23 16:08:36` | `cowrie.log.closed` |
| `2026-06-23 16:08:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60fa51eff248

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:09 |
| **Last Seen** | 2026-06-23 16:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:09:18` | `cowrie.session.connect` |
| `2026-06-23 16:09:18` | `cowrie.client.version` |
| `2026-06-23 16:09:18` | `cowrie.client.kex` |
| `2026-06-23 16:09:18` | `cowrie.login.success` |
| `2026-06-23 16:09:19` | `cowrie.session.params` |
| `2026-06-23 16:09:19` | `cowrie.command.input` |
| `2026-06-23 16:09:19` | `cowrie.log.closed` |
| `2026-06-23 16:09:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02411885e0aa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:10 |
| **Last Seen** | 2026-06-23 16:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:10:02` | `cowrie.session.connect` |
| `2026-06-23 16:10:02` | `cowrie.client.version` |
| `2026-06-23 16:10:02` | `cowrie.client.kex` |
| `2026-06-23 16:10:02` | `cowrie.login.success` |
| `2026-06-23 16:10:03` | `cowrie.session.params` |
| `2026-06-23 16:10:03` | `cowrie.command.input` |
| `2026-06-23 16:10:03` | `cowrie.log.closed` |
| `2026-06-23 16:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-149697ebdacb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:10 |
| **Last Seen** | 2026-06-23 16:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:10:50` | `cowrie.session.connect` |
| `2026-06-23 16:10:50` | `cowrie.client.version` |
| `2026-06-23 16:10:50` | `cowrie.client.kex` |
| `2026-06-23 16:10:50` | `cowrie.login.success` |
| `2026-06-23 16:10:51` | `cowrie.session.params` |
| `2026-06-23 16:10:51` | `cowrie.command.input` |
| `2026-06-23 16:10:51` | `cowrie.log.closed` |
| `2026-06-23 16:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75e16e857c5e

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 16:11 |
| **Last Seen** | 2026-06-23 16:11 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:11:19` | `cowrie.session.connect` |
| `2026-06-23 16:11:21` | `cowrie.client.version` |
| `2026-06-23 16:11:21` | `cowrie.client.kex` |
| `2026-06-23 16:11:27` | `cowrie.login.success` |
| `2026-06-23 16:11:31` | `cowrie.session.params` |
| `2026-06-23 16:11:31` | `cowrie.command.input` |
| `2026-06-23 16:11:33` | `cowrie.log.closed` |
| `2026-06-23 16:11:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36e194b3281a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:11 |
| **Last Seen** | 2026-06-23 16:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:11:36` | `cowrie.session.connect` |
| `2026-06-23 16:11:36` | `cowrie.client.version` |
| `2026-06-23 16:11:37` | `cowrie.client.kex` |
| `2026-06-23 16:11:37` | `cowrie.login.success` |
| `2026-06-23 16:11:38` | `cowrie.session.params` |
| `2026-06-23 16:11:38` | `cowrie.command.input` |
| `2026-06-23 16:11:38` | `cowrie.log.closed` |
| `2026-06-23 16:11:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-985bd152e3b5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:12 |
| **Last Seen** | 2026-06-23 16:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:12:28` | `cowrie.session.connect` |
| `2026-06-23 16:12:28` | `cowrie.client.version` |
| `2026-06-23 16:12:28` | `cowrie.client.kex` |
| `2026-06-23 16:12:29` | `cowrie.login.success` |
| `2026-06-23 16:12:30` | `cowrie.session.params` |
| `2026-06-23 16:12:30` | `cowrie.command.input` |
| `2026-06-23 16:12:30` | `cowrie.log.closed` |
| `2026-06-23 16:12:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-084df6f389f8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:13 |
| **Last Seen** | 2026-06-23 16:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:13:21` | `cowrie.session.connect` |
| `2026-06-23 16:13:21` | `cowrie.client.version` |
| `2026-06-23 16:13:21` | `cowrie.client.kex` |
| `2026-06-23 16:13:22` | `cowrie.login.success` |
| `2026-06-23 16:13:22` | `cowrie.session.params` |
| `2026-06-23 16:13:22` | `cowrie.command.input` |
| `2026-06-23 16:13:22` | `cowrie.log.closed` |
| `2026-06-23 16:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7be64e69dc7f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:14 |
| **Last Seen** | 2026-06-23 16:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:14:10` | `cowrie.session.connect` |
| `2026-06-23 16:14:10` | `cowrie.client.version` |
| `2026-06-23 16:14:10` | `cowrie.client.kex` |
| `2026-06-23 16:14:10` | `cowrie.login.success` |
| `2026-06-23 16:14:11` | `cowrie.session.params` |
| `2026-06-23 16:14:11` | `cowrie.command.input` |
| `2026-06-23 16:14:11` | `cowrie.log.closed` |
| `2026-06-23 16:14:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d5e6e3ab834

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:14 |
| **Last Seen** | 2026-06-23 16:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:14:55` | `cowrie.session.connect` |
| `2026-06-23 16:14:55` | `cowrie.client.version` |
| `2026-06-23 16:14:55` | `cowrie.client.kex` |
| `2026-06-23 16:14:55` | `cowrie.login.success` |
| `2026-06-23 16:14:56` | `cowrie.session.params` |
| `2026-06-23 16:14:56` | `cowrie.command.input` |
| `2026-06-23 16:14:56` | `cowrie.log.closed` |
| `2026-06-23 16:14:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45c67ec24850

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:15 |
| **Last Seen** | 2026-06-23 16:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:15:39` | `cowrie.session.connect` |
| `2026-06-23 16:15:39` | `cowrie.client.version` |
| `2026-06-23 16:15:39` | `cowrie.client.kex` |
| `2026-06-23 16:15:40` | `cowrie.login.success` |
| `2026-06-23 16:15:40` | `cowrie.session.params` |
| `2026-06-23 16:15:40` | `cowrie.command.input` |
| `2026-06-23 16:15:40` | `cowrie.log.closed` |
| `2026-06-23 16:15:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e19c4a59de4d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:16 |
| **Last Seen** | 2026-06-23 16:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:16:27` | `cowrie.session.connect` |
| `2026-06-23 16:16:27` | `cowrie.client.version` |
| `2026-06-23 16:16:27` | `cowrie.client.kex` |
| `2026-06-23 16:16:28` | `cowrie.login.success` |
| `2026-06-23 16:16:28` | `cowrie.session.params` |
| `2026-06-23 16:16:28` | `cowrie.command.input` |
| `2026-06-23 16:16:29` | `cowrie.log.closed` |
| `2026-06-23 16:16:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dcbd44c9c55

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:17 |
| **Last Seen** | 2026-06-23 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:17:13` | `cowrie.session.connect` |
| `2026-06-23 16:17:13` | `cowrie.client.version` |
| `2026-06-23 16:17:13` | `cowrie.client.kex` |
| `2026-06-23 16:17:13` | `cowrie.login.success` |
| `2026-06-23 16:17:14` | `cowrie.session.params` |
| `2026-06-23 16:17:14` | `cowrie.command.input` |
| `2026-06-23 16:17:14` | `cowrie.log.closed` |
| `2026-06-23 16:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40005981d520

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:17 |
| **Last Seen** | 2026-06-23 16:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:17:59` | `cowrie.session.connect` |
| `2026-06-23 16:17:59` | `cowrie.client.version` |
| `2026-06-23 16:17:59` | `cowrie.client.kex` |
| `2026-06-23 16:17:59` | `cowrie.login.success` |
| `2026-06-23 16:18:00` | `cowrie.session.params` |
| `2026-06-23 16:18:00` | `cowrie.command.input` |
| `2026-06-23 16:18:00` | `cowrie.log.closed` |
| `2026-06-23 16:18:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2270f8e08f88

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:18 |
| **Last Seen** | 2026-06-23 16:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:18:46` | `cowrie.session.connect` |
| `2026-06-23 16:18:46` | `cowrie.client.version` |
| `2026-06-23 16:18:46` | `cowrie.client.kex` |
| `2026-06-23 16:18:47` | `cowrie.login.success` |
| `2026-06-23 16:18:47` | `cowrie.session.params` |
| `2026-06-23 16:18:47` | `cowrie.command.input` |
| `2026-06-23 16:18:48` | `cowrie.log.closed` |
| `2026-06-23 16:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b62d9bc4f6e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:19 |
| **Last Seen** | 2026-06-23 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:19:36` | `cowrie.session.connect` |
| `2026-06-23 16:19:36` | `cowrie.client.version` |
| `2026-06-23 16:19:36` | `cowrie.client.kex` |
| `2026-06-23 16:19:36` | `cowrie.login.success` |
| `2026-06-23 16:19:37` | `cowrie.session.params` |
| `2026-06-23 16:19:37` | `cowrie.command.input` |
| `2026-06-23 16:19:37` | `cowrie.log.closed` |
| `2026-06-23 16:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f5ce4440a2c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:20 |
| **Last Seen** | 2026-06-23 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:20:22` | `cowrie.session.connect` |
| `2026-06-23 16:20:22` | `cowrie.client.version` |
| `2026-06-23 16:20:22` | `cowrie.client.kex` |
| `2026-06-23 16:20:23` | `cowrie.login.success` |
| `2026-06-23 16:20:23` | `cowrie.session.params` |
| `2026-06-23 16:20:23` | `cowrie.command.input` |
| `2026-06-23 16:20:23` | `cowrie.log.closed` |
| `2026-06-23 16:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d198d0e01723

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:21 |
| **Last Seen** | 2026-06-23 16:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:21:07` | `cowrie.session.connect` |
| `2026-06-23 16:21:07` | `cowrie.client.version` |
| `2026-06-23 16:21:07` | `cowrie.client.kex` |
| `2026-06-23 16:21:07` | `cowrie.login.success` |
| `2026-06-23 16:21:08` | `cowrie.session.params` |
| `2026-06-23 16:21:08` | `cowrie.command.input` |
| `2026-06-23 16:21:08` | `cowrie.log.closed` |
| `2026-06-23 16:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb9ca201766c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:21 |
| **Last Seen** | 2026-06-23 16:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:21:51` | `cowrie.session.connect` |
| `2026-06-23 16:21:51` | `cowrie.client.version` |
| `2026-06-23 16:21:51` | `cowrie.client.kex` |
| `2026-06-23 16:21:52` | `cowrie.login.success` |
| `2026-06-23 16:21:52` | `cowrie.session.params` |
| `2026-06-23 16:21:52` | `cowrie.command.input` |
| `2026-06-23 16:21:52` | `cowrie.log.closed` |
| `2026-06-23 16:21:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-139dc2e4e08f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:22 |
| **Last Seen** | 2026-06-23 16:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:22:39` | `cowrie.session.connect` |
| `2026-06-23 16:22:39` | `cowrie.client.version` |
| `2026-06-23 16:22:39` | `cowrie.client.kex` |
| `2026-06-23 16:22:39` | `cowrie.login.success` |
| `2026-06-23 16:22:40` | `cowrie.session.params` |
| `2026-06-23 16:22:40` | `cowrie.command.input` |
| `2026-06-23 16:22:40` | `cowrie.log.closed` |
| `2026-06-23 16:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afc794f82dfd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:23 |
| **Last Seen** | 2026-06-23 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:23:26` | `cowrie.session.connect` |
| `2026-06-23 16:23:26` | `cowrie.client.version` |
| `2026-06-23 16:23:26` | `cowrie.client.kex` |
| `2026-06-23 16:23:26` | `cowrie.login.success` |
| `2026-06-23 16:23:27` | `cowrie.session.params` |
| `2026-06-23 16:23:27` | `cowrie.command.input` |
| `2026-06-23 16:23:27` | `cowrie.log.closed` |
| `2026-06-23 16:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca5e9fc8775f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:24 |
| **Last Seen** | 2026-06-23 16:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:24:12` | `cowrie.session.connect` |
| `2026-06-23 16:24:12` | `cowrie.client.version` |
| `2026-06-23 16:24:12` | `cowrie.client.kex` |
| `2026-06-23 16:24:13` | `cowrie.login.success` |
| `2026-06-23 16:24:13` | `cowrie.session.params` |
| `2026-06-23 16:24:13` | `cowrie.command.input` |
| `2026-06-23 16:24:14` | `cowrie.log.closed` |
| `2026-06-23 16:24:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64e6571adad4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:25 |
| **Last Seen** | 2026-06-23 16:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:25:00` | `cowrie.session.connect` |
| `2026-06-23 16:25:00` | `cowrie.client.version` |
| `2026-06-23 16:25:00` | `cowrie.client.kex` |
| `2026-06-23 16:25:01` | `cowrie.login.success` |
| `2026-06-23 16:25:02` | `cowrie.session.params` |
| `2026-06-23 16:25:02` | `cowrie.command.input` |
| `2026-06-23 16:25:02` | `cowrie.log.closed` |
| `2026-06-23 16:25:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aba03301da92

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-23 16:25 |
| **Last Seen** | 2026-06-23 16:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:25:36` | `cowrie.session.connect` |
| `2026-06-23 16:25:36` | `cowrie.client.version` |
| `2026-06-23 16:25:37` | `cowrie.client.kex` |
| `2026-06-23 16:25:37` | `cowrie.login.success` |
| `2026-06-23 16:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d19e26fa1887

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-23 16:25 |
| **Last Seen** | 2026-06-23 16:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:25:37` | `cowrie.session.connect` |
| `2026-06-23 16:25:37` | `cowrie.client.version` |
| `2026-06-23 16:25:37` | `cowrie.client.kex` |
| `2026-06-23 16:25:37` | `cowrie.login.success` |
| `2026-06-23 16:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa2188b897b2

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 16:25 |
| **Last Seen** | 2026-06-23 16:25 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:25:38` | `cowrie.session.connect` |
| `2026-06-23 16:25:40` | `cowrie.client.version` |
| `2026-06-23 16:25:40` | `cowrie.client.kex` |
| `2026-06-23 16:25:45` | `cowrie.login.success` |
| `2026-06-23 16:25:50` | `cowrie.session.params` |
| `2026-06-23 16:25:50` | `cowrie.command.input` |
| `2026-06-23 16:25:51` | `cowrie.log.closed` |
| `2026-06-23 16:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a10c2ecfec41

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-23 16:25 |
| **Last Seen** | 2026-06-23 16:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:25:39` | `cowrie.session.connect` |
| `2026-06-23 16:25:39` | `cowrie.client.version` |
| `2026-06-23 16:25:39` | `cowrie.client.kex` |
| `2026-06-23 16:25:40` | `cowrie.login.success` |
| `2026-06-23 16:25:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ddcc9e72e58

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-23 16:25 |
| **Last Seen** | 2026-06-23 16:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:25:40` | `cowrie.session.connect` |
| `2026-06-23 16:25:40` | `cowrie.client.version` |
| `2026-06-23 16:25:40` | `cowrie.client.kex` |
| `2026-06-23 16:25:41` | `cowrie.login.success` |
| `2026-06-23 16:25:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28f20f569948

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:25 |
| **Last Seen** | 2026-06-23 16:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:25:52` | `cowrie.session.connect` |
| `2026-06-23 16:25:52` | `cowrie.client.version` |
| `2026-06-23 16:25:52` | `cowrie.client.kex` |
| `2026-06-23 16:25:52` | `cowrie.login.success` |
| `2026-06-23 16:25:53` | `cowrie.session.params` |
| `2026-06-23 16:25:53` | `cowrie.command.input` |
| `2026-06-23 16:25:53` | `cowrie.log.closed` |
| `2026-06-23 16:25:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8858b481b2f0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:26 |
| **Last Seen** | 2026-06-23 16:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:26:02` | `cowrie.session.connect` |
| `2026-06-23 16:26:02` | `cowrie.client.version` |
| `2026-06-23 16:26:02` | `cowrie.client.kex` |
| `2026-06-23 16:26:03` | `cowrie.login.success` |
| `2026-06-23 16:26:05` | `cowrie.session.params` |
| `2026-06-23 16:26:05` | `cowrie.command.input` |
| `2026-06-23 16:26:05` | `cowrie.command.input` |
| `2026-06-23 16:26:05` | `cowrie.command.input` |
| `2026-06-23 16:26:05` | `cowrie.command.input` |
| `2026-06-23 16:26:05` | `cowrie.log.closed` |
| `2026-06-23 16:26:06` | `cowrie.session.params` |
| `2026-06-23 16:26:06` | `cowrie.command.input` |
| `2026-06-23 16:26:06` | `cowrie.command.input` |
| `2026-06-23 16:26:06` | `cowrie.command.failed` |
| `2026-06-23 16:26:06` | `cowrie.command.failed` |
| `2026-06-23 16:26:06` | `cowrie.command.failed` |
| `2026-06-23 16:26:06` | `cowrie.command.failed` |
| `2026-06-23 16:26:07` | `cowrie.log.closed` |
| `2026-06-23 16:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d37c104c122f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:26 |
| **Last Seen** | 2026-06-23 16:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:26:40` | `cowrie.session.connect` |
| `2026-06-23 16:26:40` | `cowrie.client.version` |
| `2026-06-23 16:26:40` | `cowrie.client.kex` |
| `2026-06-23 16:26:41` | `cowrie.login.success` |
| `2026-06-23 16:26:41` | `cowrie.session.params` |
| `2026-06-23 16:26:41` | `cowrie.command.input` |
| `2026-06-23 16:26:41` | `cowrie.log.closed` |
| `2026-06-23 16:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7141280b9dfd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:27 |
| **Last Seen** | 2026-06-23 16:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:27:13` | `cowrie.session.connect` |
| `2026-06-23 16:27:13` | `cowrie.client.version` |
| `2026-06-23 16:27:13` | `cowrie.client.kex` |
| `2026-06-23 16:27:15` | `cowrie.login.success` |
| `2026-06-23 16:27:16` | `cowrie.session.params` |
| `2026-06-23 16:27:16` | `cowrie.command.input` |
| `2026-06-23 16:27:16` | `cowrie.command.input` |
| `2026-06-23 16:27:16` | `cowrie.command.input` |
| `2026-06-23 16:27:16` | `cowrie.command.input` |
| `2026-06-23 16:27:17` | `cowrie.log.closed` |
| `2026-06-23 16:27:18` | `cowrie.session.params` |
| `2026-06-23 16:27:18` | `cowrie.command.input` |
| `2026-06-23 16:27:18` | `cowrie.command.input` |
| `2026-06-23 16:27:18` | `cowrie.command.failed` |
| `2026-06-23 16:27:18` | `cowrie.command.failed` |
| `2026-06-23 16:27:18` | `cowrie.command.failed` |
| `2026-06-23 16:27:18` | `cowrie.command.failed` |
| `2026-06-23 16:27:18` | `cowrie.log.closed` |
| `2026-06-23 16:27:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8062f7763afa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:27 |
| **Last Seen** | 2026-06-23 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:27:27` | `cowrie.session.connect` |
| `2026-06-23 16:27:27` | `cowrie.client.version` |
| `2026-06-23 16:27:27` | `cowrie.client.kex` |
| `2026-06-23 16:27:27` | `cowrie.login.success` |
| `2026-06-23 16:27:28` | `cowrie.session.params` |
| `2026-06-23 16:27:28` | `cowrie.command.input` |
| `2026-06-23 16:27:28` | `cowrie.log.closed` |
| `2026-06-23 16:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fca85a6dd6a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:28 |
| **Last Seen** | 2026-06-23 16:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:28:12` | `cowrie.session.connect` |
| `2026-06-23 16:28:12` | `cowrie.client.version` |
| `2026-06-23 16:28:12` | `cowrie.client.kex` |
| `2026-06-23 16:28:13` | `cowrie.login.success` |
| `2026-06-23 16:28:13` | `cowrie.session.params` |
| `2026-06-23 16:28:13` | `cowrie.command.input` |
| `2026-06-23 16:28:14` | `cowrie.log.closed` |
| `2026-06-23 16:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-344725a01998

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:28 |
| **Last Seen** | 2026-06-23 16:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:28:23` | `cowrie.session.connect` |
| `2026-06-23 16:28:23` | `cowrie.client.version` |
| `2026-06-23 16:28:23` | `cowrie.client.kex` |
| `2026-06-23 16:28:25` | `cowrie.login.success` |
| `2026-06-23 16:28:26` | `cowrie.session.params` |
| `2026-06-23 16:28:26` | `cowrie.command.input` |
| `2026-06-23 16:28:26` | `cowrie.command.input` |
| `2026-06-23 16:28:26` | `cowrie.command.input` |
| `2026-06-23 16:28:26` | `cowrie.command.input` |
| `2026-06-23 16:28:27` | `cowrie.log.closed` |
| `2026-06-23 16:28:28` | `cowrie.session.params` |
| `2026-06-23 16:28:28` | `cowrie.command.input` |
| `2026-06-23 16:28:28` | `cowrie.command.input` |
| `2026-06-23 16:28:28` | `cowrie.command.failed` |
| `2026-06-23 16:28:28` | `cowrie.command.failed` |
| `2026-06-23 16:28:28` | `cowrie.command.failed` |
| `2026-06-23 16:28:28` | `cowrie.command.failed` |
| `2026-06-23 16:28:28` | `cowrie.log.closed` |
| `2026-06-23 16:28:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6af4842ea681

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:29 |
| **Last Seen** | 2026-06-23 16:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:29:01` | `cowrie.session.connect` |
| `2026-06-23 16:29:01` | `cowrie.client.version` |
| `2026-06-23 16:29:01` | `cowrie.client.kex` |
| `2026-06-23 16:29:01` | `cowrie.login.success` |
| `2026-06-23 16:29:02` | `cowrie.session.params` |
| `2026-06-23 16:29:02` | `cowrie.command.input` |
| `2026-06-23 16:29:02` | `cowrie.log.closed` |
| `2026-06-23 16:29:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66c364d042af

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:29 |
| **Last Seen** | 2026-06-23 16:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:29:48` | `cowrie.session.connect` |
| `2026-06-23 16:29:48` | `cowrie.client.version` |
| `2026-06-23 16:29:48` | `cowrie.client.kex` |
| `2026-06-23 16:29:48` | `cowrie.login.success` |
| `2026-06-23 16:29:49` | `cowrie.session.params` |
| `2026-06-23 16:29:49` | `cowrie.command.input` |
| `2026-06-23 16:29:49` | `cowrie.log.closed` |
| `2026-06-23 16:29:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e45f1b5b764

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:30 |
| **Last Seen** | 2026-06-23 16:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:30:36` | `cowrie.session.connect` |
| `2026-06-23 16:30:36` | `cowrie.client.version` |
| `2026-06-23 16:30:37` | `cowrie.client.kex` |
| `2026-06-23 16:30:37` | `cowrie.login.success` |
| `2026-06-23 16:30:38` | `cowrie.session.params` |
| `2026-06-23 16:30:38` | `cowrie.command.input` |
| `2026-06-23 16:30:38` | `cowrie.log.closed` |
| `2026-06-23 16:30:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f68540a6116

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:30 |
| **Last Seen** | 2026-06-23 16:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234567' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:30:45` | `cowrie.session.connect` |
| `2026-06-23 16:30:45` | `cowrie.client.version` |
| `2026-06-23 16:30:45` | `cowrie.client.kex` |
| `2026-06-23 16:30:47` | `cowrie.login.success` |
| `2026-06-23 16:30:48` | `cowrie.session.params` |
| `2026-06-23 16:30:48` | `cowrie.command.input` |
| `2026-06-23 16:30:48` | `cowrie.command.input` |
| `2026-06-23 16:30:48` | `cowrie.command.input` |
| `2026-06-23 16:30:48` | `cowrie.command.input` |
| `2026-06-23 16:30:48` | `cowrie.log.closed` |
| `2026-06-23 16:30:50` | `cowrie.session.params` |
| `2026-06-23 16:30:50` | `cowrie.command.input` |
| `2026-06-23 16:30:50` | `cowrie.command.input` |
| `2026-06-23 16:30:50` | `cowrie.command.failed` |
| `2026-06-23 16:30:50` | `cowrie.command.failed` |
| `2026-06-23 16:30:50` | `cowrie.command.failed` |
| `2026-06-23 16:30:50` | `cowrie.command.failed` |
| `2026-06-23 16:30:50` | `cowrie.log.closed` |
| `2026-06-23 16:30:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7b77f0d0798

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:31 |
| **Last Seen** | 2026-06-23 16:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:31:26` | `cowrie.session.connect` |
| `2026-06-23 16:31:26` | `cowrie.client.version` |
| `2026-06-23 16:31:26` | `cowrie.client.kex` |
| `2026-06-23 16:31:26` | `cowrie.login.success` |
| `2026-06-23 16:31:27` | `cowrie.session.params` |
| `2026-06-23 16:31:27` | `cowrie.command.input` |
| `2026-06-23 16:31:27` | `cowrie.log.closed` |
| `2026-06-23 16:31:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db27229ca827

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:31 |
| **Last Seen** | 2026-06-23 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345678' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:31:54` | `cowrie.session.connect` |
| `2026-06-23 16:31:55` | `cowrie.client.version` |
| `2026-06-23 16:31:55` | `cowrie.client.kex` |
| `2026-06-23 16:31:56` | `cowrie.login.success` |
| `2026-06-23 16:31:58` | `cowrie.session.params` |
| `2026-06-23 16:31:58` | `cowrie.command.input` |
| `2026-06-23 16:31:58` | `cowrie.command.input` |
| `2026-06-23 16:31:58` | `cowrie.command.input` |
| `2026-06-23 16:31:58` | `cowrie.command.input` |
| `2026-06-23 16:31:58` | `cowrie.log.closed` |
| `2026-06-23 16:31:59` | `cowrie.session.params` |
| `2026-06-23 16:31:59` | `cowrie.command.input` |
| `2026-06-23 16:31:59` | `cowrie.command.input` |
| `2026-06-23 16:31:59` | `cowrie.command.failed` |
| `2026-06-23 16:31:59` | `cowrie.command.failed` |
| `2026-06-23 16:31:59` | `cowrie.command.failed` |
| `2026-06-23 16:31:59` | `cowrie.command.failed` |
| `2026-06-23 16:32:00` | `cowrie.log.closed` |
| `2026-06-23 16:32:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca4e0b54b574

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:32 |
| **Last Seen** | 2026-06-23 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:32:17` | `cowrie.session.connect` |
| `2026-06-23 16:32:17` | `cowrie.client.version` |
| `2026-06-23 16:32:17` | `cowrie.client.kex` |
| `2026-06-23 16:32:17` | `cowrie.login.success` |
| `2026-06-23 16:32:18` | `cowrie.session.params` |
| `2026-06-23 16:32:18` | `cowrie.command.input` |
| `2026-06-23 16:32:18` | `cowrie.log.closed` |
| `2026-06-23 16:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58e59e90e204

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:33 |
| **Last Seen** | 2026-06-23 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:33:04` | `cowrie.session.connect` |
| `2026-06-23 16:33:04` | `cowrie.client.version` |
| `2026-06-23 16:33:04` | `cowrie.client.kex` |
| `2026-06-23 16:33:04` | `cowrie.login.success` |
| `2026-06-23 16:33:05` | `cowrie.session.params` |
| `2026-06-23 16:33:05` | `cowrie.command.input` |
| `2026-06-23 16:33:05` | `cowrie.log.closed` |
| `2026-06-23 16:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0580b2eb64a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:33 |
| **Last Seen** | 2026-06-23 16:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123456789' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:33:12` | `cowrie.session.connect` |
| `2026-06-23 16:33:13` | `cowrie.client.version` |
| `2026-06-23 16:33:13` | `cowrie.client.kex` |
| `2026-06-23 16:33:15` | `cowrie.login.success` |
| `2026-06-23 16:33:16` | `cowrie.session.params` |
| `2026-06-23 16:33:16` | `cowrie.command.input` |
| `2026-06-23 16:33:16` | `cowrie.command.input` |
| `2026-06-23 16:33:16` | `cowrie.command.input` |
| `2026-06-23 16:33:16` | `cowrie.command.input` |
| `2026-06-23 16:33:17` | `cowrie.log.closed` |
| `2026-06-23 16:33:18` | `cowrie.session.params` |
| `2026-06-23 16:33:18` | `cowrie.command.input` |
| `2026-06-23 16:33:18` | `cowrie.command.input` |
| `2026-06-23 16:33:18` | `cowrie.command.failed` |
| `2026-06-23 16:33:18` | `cowrie.command.failed` |
| `2026-06-23 16:33:18` | `cowrie.command.failed` |
| `2026-06-23 16:33:18` | `cowrie.command.failed` |
| `2026-06-23 16:33:18` | `cowrie.log.closed` |
| `2026-06-23 16:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd21ab102f78

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:33 |
| **Last Seen** | 2026-06-23 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:33:50` | `cowrie.session.connect` |
| `2026-06-23 16:33:50` | `cowrie.client.version` |
| `2026-06-23 16:33:50` | `cowrie.client.kex` |
| `2026-06-23 16:33:50` | `cowrie.login.success` |
| `2026-06-23 16:33:51` | `cowrie.session.params` |
| `2026-06-23 16:33:51` | `cowrie.command.input` |
| `2026-06-23 16:33:51` | `cowrie.log.closed` |
| `2026-06-23 16:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b42eb2fdd37e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:34 |
| **Last Seen** | 2026-06-23 16:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234567890' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:34:21` | `cowrie.session.connect` |
| `2026-06-23 16:34:21` | `cowrie.client.version` |
| `2026-06-23 16:34:21` | `cowrie.client.kex` |
| `2026-06-23 16:34:22` | `cowrie.login.success` |
| `2026-06-23 16:34:24` | `cowrie.session.params` |
| `2026-06-23 16:34:24` | `cowrie.command.input` |
| `2026-06-23 16:34:24` | `cowrie.command.input` |
| `2026-06-23 16:34:24` | `cowrie.command.input` |
| `2026-06-23 16:34:24` | `cowrie.command.input` |
| `2026-06-23 16:34:24` | `cowrie.log.closed` |
| `2026-06-23 16:34:25` | `cowrie.session.params` |
| `2026-06-23 16:34:25` | `cowrie.command.input` |
| `2026-06-23 16:34:25` | `cowrie.command.input` |
| `2026-06-23 16:34:25` | `cowrie.command.failed` |
| `2026-06-23 16:34:25` | `cowrie.command.failed` |
| `2026-06-23 16:34:25` | `cowrie.command.failed` |
| `2026-06-23 16:34:25` | `cowrie.command.failed` |
| `2026-06-23 16:34:25` | `cowrie.log.closed` |
| `2026-06-23 16:34:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdbc2f6f071c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:34 |
| **Last Seen** | 2026-06-23 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:34:37` | `cowrie.session.connect` |
| `2026-06-23 16:34:37` | `cowrie.client.version` |
| `2026-06-23 16:34:37` | `cowrie.client.kex` |
| `2026-06-23 16:34:38` | `cowrie.login.success` |
| `2026-06-23 16:34:38` | `cowrie.session.params` |
| `2026-06-23 16:34:38` | `cowrie.command.input` |
| `2026-06-23 16:34:38` | `cowrie.log.closed` |
| `2026-06-23 16:34:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69ca33b401ca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:35 |
| **Last Seen** | 2026-06-23 16:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123abc' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:35:21` | `cowrie.session.connect` |
| `2026-06-23 16:35:21` | `cowrie.client.version` |
| `2026-06-23 16:35:21` | `cowrie.client.kex` |
| `2026-06-23 16:35:22` | `cowrie.login.success` |
| `2026-06-23 16:35:23` | `cowrie.session.params` |
| `2026-06-23 16:35:23` | `cowrie.command.input` |
| `2026-06-23 16:35:23` | `cowrie.command.input` |
| `2026-06-23 16:35:23` | `cowrie.command.input` |
| `2026-06-23 16:35:23` | `cowrie.command.input` |
| `2026-06-23 16:35:24` | `cowrie.log.closed` |
| `2026-06-23 16:35:24` | `cowrie.session.params` |
| `2026-06-23 16:35:24` | `cowrie.command.input` |
| `2026-06-23 16:35:24` | `cowrie.command.input` |
| `2026-06-23 16:35:24` | `cowrie.command.failed` |
| `2026-06-23 16:35:24` | `cowrie.command.failed` |
| `2026-06-23 16:35:24` | `cowrie.command.failed` |
| `2026-06-23 16:35:24` | `cowrie.command.failed` |
| `2026-06-23 16:35:25` | `cowrie.log.closed` |
| `2026-06-23 16:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a6a0ba6b4f0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:35 |
| **Last Seen** | 2026-06-23 16:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:35:28` | `cowrie.session.connect` |
| `2026-06-23 16:35:28` | `cowrie.client.version` |
| `2026-06-23 16:35:28` | `cowrie.client.kex` |
| `2026-06-23 16:35:28` | `cowrie.login.success` |
| `2026-06-23 16:35:29` | `cowrie.session.params` |
| `2026-06-23 16:35:29` | `cowrie.command.input` |
| `2026-06-23 16:35:29` | `cowrie.log.closed` |
| `2026-06-23 16:35:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd383fd67e15

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:36 |
| **Last Seen** | 2026-06-23 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:36:15` | `cowrie.session.connect` |
| `2026-06-23 16:36:15` | `cowrie.client.version` |
| `2026-06-23 16:36:15` | `cowrie.client.kex` |
| `2026-06-23 16:36:16` | `cowrie.login.success` |
| `2026-06-23 16:36:16` | `cowrie.session.params` |
| `2026-06-23 16:36:16` | `cowrie.command.input` |
| `2026-06-23 16:36:16` | `cowrie.log.closed` |
| `2026-06-23 16:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e798d3ee78b7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:36 |
| **Last Seen** | 2026-06-23 16:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1q2w3e4r' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:36:19` | `cowrie.session.connect` |
| `2026-06-23 16:36:19` | `cowrie.client.version` |
| `2026-06-23 16:36:19` | `cowrie.client.kex` |
| `2026-06-23 16:36:21` | `cowrie.login.success` |
| `2026-06-23 16:36:22` | `cowrie.session.params` |
| `2026-06-23 16:36:22` | `cowrie.command.input` |
| `2026-06-23 16:36:22` | `cowrie.command.input` |
| `2026-06-23 16:36:22` | `cowrie.command.input` |
| `2026-06-23 16:36:22` | `cowrie.command.input` |
| `2026-06-23 16:36:22` | `cowrie.log.closed` |
| `2026-06-23 16:36:24` | `cowrie.session.params` |
| `2026-06-23 16:36:24` | `cowrie.command.input` |
| `2026-06-23 16:36:24` | `cowrie.command.input` |
| `2026-06-23 16:36:24` | `cowrie.command.failed` |
| `2026-06-23 16:36:24` | `cowrie.command.failed` |
| `2026-06-23 16:36:24` | `cowrie.command.failed` |
| `2026-06-23 16:36:24` | `cowrie.command.failed` |
| `2026-06-23 16:36:24` | `cowrie.log.closed` |
| `2026-06-23 16:36:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b64d0a467d9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:37 |
| **Last Seen** | 2026-06-23 16:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:37:03` | `cowrie.session.connect` |
| `2026-06-23 16:37:03` | `cowrie.client.version` |
| `2026-06-23 16:37:03` | `cowrie.client.kex` |
| `2026-06-23 16:37:03` | `cowrie.login.success` |
| `2026-06-23 16:37:04` | `cowrie.session.params` |
| `2026-06-23 16:37:04` | `cowrie.command.input` |
| `2026-06-23 16:37:04` | `cowrie.log.closed` |
| `2026-06-23 16:37:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1ec16c4c5c4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:37 |
| **Last Seen** | 2026-06-23 16:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'P@ssw0rd123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:37:19` | `cowrie.session.connect` |
| `2026-06-23 16:37:19` | `cowrie.client.version` |
| `2026-06-23 16:37:19` | `cowrie.client.kex` |
| `2026-06-23 16:37:20` | `cowrie.login.success` |
| `2026-06-23 16:37:21` | `cowrie.session.params` |
| `2026-06-23 16:37:21` | `cowrie.command.input` |
| `2026-06-23 16:37:21` | `cowrie.command.input` |
| `2026-06-23 16:37:21` | `cowrie.command.input` |
| `2026-06-23 16:37:21` | `cowrie.command.input` |
| `2026-06-23 16:37:22` | `cowrie.log.closed` |
| `2026-06-23 16:37:23` | `cowrie.session.params` |
| `2026-06-23 16:37:23` | `cowrie.command.input` |
| `2026-06-23 16:37:23` | `cowrie.command.input` |
| `2026-06-23 16:37:23` | `cowrie.command.failed` |
| `2026-06-23 16:37:23` | `cowrie.command.failed` |
| `2026-06-23 16:37:23` | `cowrie.command.failed` |
| `2026-06-23 16:37:23` | `cowrie.command.failed` |
| `2026-06-23 16:37:23` | `cowrie.log.closed` |
| `2026-06-23 16:37:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff3148f1914

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:37 |
| **Last Seen** | 2026-06-23 16:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:37:52` | `cowrie.session.connect` |
| `2026-06-23 16:37:52` | `cowrie.client.version` |
| `2026-06-23 16:37:52` | `cowrie.client.kex` |
| `2026-06-23 16:37:52` | `cowrie.login.success` |
| `2026-06-23 16:37:53` | `cowrie.session.params` |
| `2026-06-23 16:37:53` | `cowrie.command.input` |
| `2026-06-23 16:37:53` | `cowrie.log.closed` |
| `2026-06-23 16:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2d611195abb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:38 |
| **Last Seen** | 2026-06-23 16:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'abc123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:38:19` | `cowrie.session.connect` |
| `2026-06-23 16:38:19` | `cowrie.client.version` |
| `2026-06-23 16:38:19` | `cowrie.client.kex` |
| `2026-06-23 16:38:20` | `cowrie.login.success` |
| `2026-06-23 16:38:22` | `cowrie.session.params` |
| `2026-06-23 16:38:22` | `cowrie.command.input` |
| `2026-06-23 16:38:22` | `cowrie.command.input` |
| `2026-06-23 16:38:22` | `cowrie.command.input` |
| `2026-06-23 16:38:22` | `cowrie.command.input` |
| `2026-06-23 16:38:22` | `cowrie.log.closed` |
| `2026-06-23 16:38:23` | `cowrie.session.params` |
| `2026-06-23 16:38:23` | `cowrie.command.input` |
| `2026-06-23 16:38:23` | `cowrie.command.input` |
| `2026-06-23 16:38:23` | `cowrie.command.failed` |
| `2026-06-23 16:38:23` | `cowrie.command.failed` |
| `2026-06-23 16:38:23` | `cowrie.command.failed` |
| `2026-06-23 16:38:23` | `cowrie.command.failed` |
| `2026-06-23 16:38:23` | `cowrie.log.closed` |
| `2026-06-23 16:38:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e35a9edaa1a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:38 |
| **Last Seen** | 2026-06-23 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:38:41` | `cowrie.session.connect` |
| `2026-06-23 16:38:41` | `cowrie.client.version` |
| `2026-06-23 16:38:41` | `cowrie.client.kex` |
| `2026-06-23 16:38:41` | `cowrie.login.success` |
| `2026-06-23 16:38:42` | `cowrie.session.params` |
| `2026-06-23 16:38:42` | `cowrie.command.input` |
| `2026-06-23 16:38:42` | `cowrie.log.closed` |
| `2026-06-23 16:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5c6f6a62734

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:39 |
| **Last Seen** | 2026-06-23 16:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'admin123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:39:19` | `cowrie.session.connect` |
| `2026-06-23 16:39:19` | `cowrie.client.version` |
| `2026-06-23 16:39:19` | `cowrie.client.kex` |
| `2026-06-23 16:39:20` | `cowrie.login.success` |
| `2026-06-23 16:39:22` | `cowrie.session.params` |
| `2026-06-23 16:39:22` | `cowrie.command.input` |
| `2026-06-23 16:39:22` | `cowrie.command.input` |
| `2026-06-23 16:39:22` | `cowrie.command.input` |
| `2026-06-23 16:39:22` | `cowrie.command.input` |
| `2026-06-23 16:39:22` | `cowrie.log.closed` |
| `2026-06-23 16:39:23` | `cowrie.session.params` |
| `2026-06-23 16:39:23` | `cowrie.command.input` |
| `2026-06-23 16:39:23` | `cowrie.command.input` |
| `2026-06-23 16:39:23` | `cowrie.command.failed` |
| `2026-06-23 16:39:23` | `cowrie.command.failed` |
| `2026-06-23 16:39:23` | `cowrie.command.failed` |
| `2026-06-23 16:39:23` | `cowrie.command.failed` |
| `2026-06-23 16:39:23` | `cowrie.log.closed` |
| `2026-06-23 16:39:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb1c9d04c638

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:39 |
| **Last Seen** | 2026-06-23 16:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:39:28` | `cowrie.session.connect` |
| `2026-06-23 16:39:28` | `cowrie.client.version` |
| `2026-06-23 16:39:28` | `cowrie.client.kex` |
| `2026-06-23 16:39:28` | `cowrie.login.success` |
| `2026-06-23 16:39:29` | `cowrie.session.params` |
| `2026-06-23 16:39:29` | `cowrie.command.input` |
| `2026-06-23 16:39:29` | `cowrie.log.closed` |
| `2026-06-23 16:39:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a45a35568a0

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 16:39 |
| **Last Seen** | 2026-06-23 16:39 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:39:45` | `cowrie.session.connect` |
| `2026-06-23 16:39:46` | `cowrie.client.version` |
| `2026-06-23 16:39:46` | `cowrie.client.kex` |
| `2026-06-23 16:39:52` | `cowrie.login.success` |
| `2026-06-23 16:39:56` | `cowrie.session.params` |
| `2026-06-23 16:39:56` | `cowrie.command.input` |
| `2026-06-23 16:39:57` | `cowrie.log.closed` |
| `2026-06-23 16:39:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96aebc1d2c2d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:40 |
| **Last Seen** | 2026-06-23 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:40:14` | `cowrie.session.connect` |
| `2026-06-23 16:40:14` | `cowrie.client.version` |
| `2026-06-23 16:40:14` | `cowrie.client.kex` |
| `2026-06-23 16:40:14` | `cowrie.login.success` |
| `2026-06-23 16:40:15` | `cowrie.session.params` |
| `2026-06-23 16:40:15` | `cowrie.command.input` |
| `2026-06-23 16:40:15` | `cowrie.log.closed` |
| `2026-06-23 16:40:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64ea4514f34f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:40 |
| **Last Seen** | 2026-06-23 16:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'letmein' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:40:19` | `cowrie.session.connect` |
| `2026-06-23 16:40:19` | `cowrie.client.version` |
| `2026-06-23 16:40:19` | `cowrie.client.kex` |
| `2026-06-23 16:40:20` | `cowrie.login.success` |
| `2026-06-23 16:40:22` | `cowrie.session.params` |
| `2026-06-23 16:40:22` | `cowrie.command.input` |
| `2026-06-23 16:40:22` | `cowrie.command.input` |
| `2026-06-23 16:40:22` | `cowrie.command.input` |
| `2026-06-23 16:40:22` | `cowrie.command.input` |
| `2026-06-23 16:40:22` | `cowrie.log.closed` |
| `2026-06-23 16:40:23` | `cowrie.session.params` |
| `2026-06-23 16:40:23` | `cowrie.command.input` |
| `2026-06-23 16:40:23` | `cowrie.command.input` |
| `2026-06-23 16:40:23` | `cowrie.command.failed` |
| `2026-06-23 16:40:23` | `cowrie.command.failed` |
| `2026-06-23 16:40:23` | `cowrie.command.failed` |
| `2026-06-23 16:40:23` | `cowrie.command.failed` |
| `2026-06-23 16:40:23` | `cowrie.log.closed` |
| `2026-06-23 16:40:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41aa3f815201

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:41 |
| **Last Seen** | 2026-06-23 16:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:41:01` | `cowrie.session.connect` |
| `2026-06-23 16:41:01` | `cowrie.client.version` |
| `2026-06-23 16:41:01` | `cowrie.client.kex` |
| `2026-06-23 16:41:01` | `cowrie.login.success` |
| `2026-06-23 16:41:02` | `cowrie.session.params` |
| `2026-06-23 16:41:02` | `cowrie.command.input` |
| `2026-06-23 16:41:02` | `cowrie.log.closed` |
| `2026-06-23 16:41:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7f23788d3b9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:41 |
| **Last Seen** | 2026-06-23 16:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'pass123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:41:17` | `cowrie.session.connect` |
| `2026-06-23 16:41:18` | `cowrie.client.version` |
| `2026-06-23 16:41:18` | `cowrie.client.kex` |
| `2026-06-23 16:41:19` | `cowrie.login.success` |
| `2026-06-23 16:41:20` | `cowrie.session.params` |
| `2026-06-23 16:41:20` | `cowrie.command.input` |
| `2026-06-23 16:41:20` | `cowrie.command.input` |
| `2026-06-23 16:41:20` | `cowrie.command.input` |
| `2026-06-23 16:41:20` | `cowrie.command.input` |
| `2026-06-23 16:41:20` | `cowrie.log.closed` |
| `2026-06-23 16:41:21` | `cowrie.session.params` |
| `2026-06-23 16:41:21` | `cowrie.command.input` |
| `2026-06-23 16:41:21` | `cowrie.command.input` |
| `2026-06-23 16:41:21` | `cowrie.command.failed` |
| `2026-06-23 16:41:21` | `cowrie.command.failed` |
| `2026-06-23 16:41:21` | `cowrie.command.failed` |
| `2026-06-23 16:41:21` | `cowrie.command.failed` |
| `2026-06-23 16:41:21` | `cowrie.log.closed` |
| `2026-06-23 16:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f99f61982db0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:41 |
| **Last Seen** | 2026-06-23 16:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:41:48` | `cowrie.session.connect` |
| `2026-06-23 16:41:48` | `cowrie.client.version` |
| `2026-06-23 16:41:48` | `cowrie.client.kex` |
| `2026-06-23 16:41:48` | `cowrie.login.success` |
| `2026-06-23 16:41:49` | `cowrie.session.params` |
| `2026-06-23 16:41:49` | `cowrie.command.input` |
| `2026-06-23 16:41:49` | `cowrie.log.closed` |
| `2026-06-23 16:41:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c09d82c3b6c2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:42 |
| **Last Seen** | 2026-06-23 16:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:42:17` | `cowrie.session.connect` |
| `2026-06-23 16:42:17` | `cowrie.client.version` |
| `2026-06-23 16:42:17` | `cowrie.client.kex` |
| `2026-06-23 16:42:18` | `cowrie.login.success` |
| `2026-06-23 16:42:19` | `cowrie.session.params` |
| `2026-06-23 16:42:19` | `cowrie.command.input` |
| `2026-06-23 16:42:19` | `cowrie.command.input` |
| `2026-06-23 16:42:19` | `cowrie.command.input` |
| `2026-06-23 16:42:19` | `cowrie.command.input` |
| `2026-06-23 16:42:20` | `cowrie.log.closed` |
| `2026-06-23 16:42:20` | `cowrie.session.params` |
| `2026-06-23 16:42:20` | `cowrie.command.input` |
| `2026-06-23 16:42:20` | `cowrie.command.input` |
| `2026-06-23 16:42:20` | `cowrie.command.failed` |
| `2026-06-23 16:42:20` | `cowrie.command.failed` |
| `2026-06-23 16:42:20` | `cowrie.command.failed` |
| `2026-06-23 16:42:20` | `cowrie.command.failed` |
| `2026-06-23 16:42:21` | `cowrie.log.closed` |
| `2026-06-23 16:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-998d5f5bb224

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:42 |
| **Last Seen** | 2026-06-23 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:42:35` | `cowrie.session.connect` |
| `2026-06-23 16:42:35` | `cowrie.client.version` |
| `2026-06-23 16:42:35` | `cowrie.client.kex` |
| `2026-06-23 16:42:36` | `cowrie.login.success` |
| `2026-06-23 16:42:36` | `cowrie.session.params` |
| `2026-06-23 16:42:36` | `cowrie.command.input` |
| `2026-06-23 16:42:37` | `cowrie.log.closed` |
| `2026-06-23 16:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c69fe589239d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:43 |
| **Last Seen** | 2026-06-23 16:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password1' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:43:16` | `cowrie.session.connect` |
| `2026-06-23 16:43:17` | `cowrie.client.version` |
| `2026-06-23 16:43:17` | `cowrie.client.kex` |
| `2026-06-23 16:43:18` | `cowrie.login.success` |
| `2026-06-23 16:43:19` | `cowrie.session.params` |
| `2026-06-23 16:43:19` | `cowrie.command.input` |
| `2026-06-23 16:43:19` | `cowrie.command.input` |
| `2026-06-23 16:43:19` | `cowrie.command.input` |
| `2026-06-23 16:43:19` | `cowrie.command.input` |
| `2026-06-23 16:43:19` | `cowrie.log.closed` |
| `2026-06-23 16:43:20` | `cowrie.session.params` |
| `2026-06-23 16:43:20` | `cowrie.command.input` |
| `2026-06-23 16:43:20` | `cowrie.command.input` |
| `2026-06-23 16:43:20` | `cowrie.command.failed` |
| `2026-06-23 16:43:20` | `cowrie.command.failed` |
| `2026-06-23 16:43:20` | `cowrie.command.failed` |
| `2026-06-23 16:43:20` | `cowrie.command.failed` |
| `2026-06-23 16:43:20` | `cowrie.log.closed` |
| `2026-06-23 16:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a1f0eeae755

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:43 |
| **Last Seen** | 2026-06-23 16:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:43:23` | `cowrie.session.connect` |
| `2026-06-23 16:43:23` | `cowrie.client.version` |
| `2026-06-23 16:43:23` | `cowrie.client.kex` |
| `2026-06-23 16:43:23` | `cowrie.login.success` |
| `2026-06-23 16:43:24` | `cowrie.session.params` |
| `2026-06-23 16:43:24` | `cowrie.command.input` |
| `2026-06-23 16:43:24` | `cowrie.log.closed` |
| `2026-06-23 16:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1acf0e72d2e5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:44 |
| **Last Seen** | 2026-06-23 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:44:14` | `cowrie.session.connect` |
| `2026-06-23 16:44:14` | `cowrie.client.version` |
| `2026-06-23 16:44:14` | `cowrie.client.kex` |
| `2026-06-23 16:44:15` | `cowrie.login.success` |
| `2026-06-23 16:44:15` | `cowrie.session.params` |
| `2026-06-23 16:44:15` | `cowrie.command.input` |
| `2026-06-23 16:44:15` | `cowrie.log.closed` |
| `2026-06-23 16:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b806b0aec548

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:44 |
| **Last Seen** | 2026-06-23 16:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'qwerty123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:44:15` | `cowrie.session.connect` |
| `2026-06-23 16:44:15` | `cowrie.client.version` |
| `2026-06-23 16:44:16` | `cowrie.client.kex` |
| `2026-06-23 16:44:16` | `cowrie.login.success` |
| `2026-06-23 16:44:17` | `cowrie.session.params` |
| `2026-06-23 16:44:17` | `cowrie.command.input` |
| `2026-06-23 16:44:17` | `cowrie.command.input` |
| `2026-06-23 16:44:17` | `cowrie.command.input` |
| `2026-06-23 16:44:17` | `cowrie.command.input` |
| `2026-06-23 16:44:18` | `cowrie.log.closed` |
| `2026-06-23 16:44:19` | `cowrie.session.params` |
| `2026-06-23 16:44:19` | `cowrie.command.input` |
| `2026-06-23 16:44:19` | `cowrie.command.input` |
| `2026-06-23 16:44:19` | `cowrie.command.failed` |
| `2026-06-23 16:44:19` | `cowrie.command.failed` |
| `2026-06-23 16:44:19` | `cowrie.command.failed` |
| `2026-06-23 16:44:19` | `cowrie.command.failed` |
| `2026-06-23 16:44:19` | `cowrie.log.closed` |
| `2026-06-23 16:44:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d38b58fbaf92

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:45 |
| **Last Seen** | 2026-06-23 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:45:03` | `cowrie.session.connect` |
| `2026-06-23 16:45:03` | `cowrie.client.version` |
| `2026-06-23 16:45:03` | `cowrie.client.kex` |
| `2026-06-23 16:45:04` | `cowrie.login.success` |
| `2026-06-23 16:45:04` | `cowrie.session.params` |
| `2026-06-23 16:45:04` | `cowrie.command.input` |
| `2026-06-23 16:45:04` | `cowrie.log.closed` |
| `2026-06-23 16:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b17d2dece40b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:45 |
| **Last Seen** | 2026-06-23 16:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'root123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:45:14` | `cowrie.session.connect` |
| `2026-06-23 16:45:14` | `cowrie.client.version` |
| `2026-06-23 16:45:14` | `cowrie.client.kex` |
| `2026-06-23 16:45:15` | `cowrie.login.success` |
| `2026-06-23 16:45:16` | `cowrie.session.params` |
| `2026-06-23 16:45:16` | `cowrie.command.input` |
| `2026-06-23 16:45:16` | `cowrie.command.input` |
| `2026-06-23 16:45:16` | `cowrie.command.input` |
| `2026-06-23 16:45:16` | `cowrie.command.input` |
| `2026-06-23 16:45:17` | `cowrie.log.closed` |
| `2026-06-23 16:45:18` | `cowrie.session.params` |
| `2026-06-23 16:45:18` | `cowrie.command.input` |
| `2026-06-23 16:45:18` | `cowrie.command.input` |
| `2026-06-23 16:45:18` | `cowrie.command.failed` |
| `2026-06-23 16:45:18` | `cowrie.command.failed` |
| `2026-06-23 16:45:18` | `cowrie.command.failed` |
| `2026-06-23 16:45:18` | `cowrie.command.failed` |
| `2026-06-23 16:45:18` | `cowrie.log.closed` |
| `2026-06-23 16:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7723299156ea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:45 |
| **Last Seen** | 2026-06-23 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:45:50` | `cowrie.session.connect` |
| `2026-06-23 16:45:50` | `cowrie.client.version` |
| `2026-06-23 16:45:50` | `cowrie.client.kex` |
| `2026-06-23 16:45:50` | `cowrie.login.success` |
| `2026-06-23 16:45:51` | `cowrie.session.params` |
| `2026-06-23 16:45:51` | `cowrie.command.input` |
| `2026-06-23 16:45:51` | `cowrie.log.closed` |
| `2026-06-23 16:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-369fce1d1086

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:46 |
| **Last Seen** | 2026-06-23 16:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'welcome' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:46:13` | `cowrie.session.connect` |
| `2026-06-23 16:46:13` | `cowrie.client.version` |
| `2026-06-23 16:46:13` | `cowrie.client.kex` |
| `2026-06-23 16:46:14` | `cowrie.login.success` |
| `2026-06-23 16:46:15` | `cowrie.session.params` |
| `2026-06-23 16:46:15` | `cowrie.command.input` |
| `2026-06-23 16:46:15` | `cowrie.command.input` |
| `2026-06-23 16:46:15` | `cowrie.command.input` |
| `2026-06-23 16:46:15` | `cowrie.command.input` |
| `2026-06-23 16:46:16` | `cowrie.log.closed` |
| `2026-06-23 16:46:17` | `cowrie.session.params` |
| `2026-06-23 16:46:17` | `cowrie.command.input` |
| `2026-06-23 16:46:17` | `cowrie.command.input` |
| `2026-06-23 16:46:17` | `cowrie.command.failed` |
| `2026-06-23 16:46:17` | `cowrie.command.failed` |
| `2026-06-23 16:46:17` | `cowrie.command.failed` |
| `2026-06-23 16:46:17` | `cowrie.command.failed` |
| `2026-06-23 16:46:17` | `cowrie.log.closed` |
| `2026-06-23 16:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d651da9a26ed

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:46 |
| **Last Seen** | 2026-06-23 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:46:35` | `cowrie.session.connect` |
| `2026-06-23 16:46:35` | `cowrie.client.version` |
| `2026-06-23 16:46:35` | `cowrie.client.kex` |
| `2026-06-23 16:46:36` | `cowrie.login.success` |
| `2026-06-23 16:46:37` | `cowrie.session.params` |
| `2026-06-23 16:46:37` | `cowrie.command.input` |
| `2026-06-23 16:46:37` | `cowrie.log.closed` |
| `2026-06-23 16:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0522629ab6c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:47 |
| **Last Seen** | 2026-06-23 16:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:47:15` | `cowrie.session.connect` |
| `2026-06-23 16:47:15` | `cowrie.client.version` |
| `2026-06-23 16:47:15` | `cowrie.client.kex` |
| `2026-06-23 16:47:16` | `cowrie.login.success` |
| `2026-06-23 16:47:18` | `cowrie.session.params` |
| `2026-06-23 16:47:18` | `cowrie.command.input` |
| `2026-06-23 16:47:18` | `cowrie.command.input` |
| `2026-06-23 16:47:18` | `cowrie.command.input` |
| `2026-06-23 16:47:18` | `cowrie.command.input` |
| `2026-06-23 16:47:18` | `cowrie.log.closed` |
| `2026-06-23 16:47:19` | `cowrie.session.params` |
| `2026-06-23 16:47:19` | `cowrie.command.input` |
| `2026-06-23 16:47:19` | `cowrie.command.input` |
| `2026-06-23 16:47:19` | `cowrie.command.failed` |
| `2026-06-23 16:47:19` | `cowrie.command.failed` |
| `2026-06-23 16:47:19` | `cowrie.command.failed` |
| `2026-06-23 16:47:19` | `cowrie.command.failed` |
| `2026-06-23 16:47:19` | `cowrie.log.closed` |
| `2026-06-23 16:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07924f0212da

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:47 |
| **Last Seen** | 2026-06-23 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:47:22` | `cowrie.session.connect` |
| `2026-06-23 16:47:22` | `cowrie.client.version` |
| `2026-06-23 16:47:22` | `cowrie.client.kex` |
| `2026-06-23 16:47:23` | `cowrie.login.success` |
| `2026-06-23 16:47:23` | `cowrie.session.params` |
| `2026-06-23 16:47:23` | `cowrie.command.input` |
| `2026-06-23 16:47:24` | `cowrie.log.closed` |
| `2026-06-23 16:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8e2391eed4e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:48 |
| **Last Seen** | 2026-06-23 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:48:11` | `cowrie.session.connect` |
| `2026-06-23 16:48:11` | `cowrie.client.version` |
| `2026-06-23 16:48:11` | `cowrie.client.kex` |
| `2026-06-23 16:48:11` | `cowrie.login.success` |
| `2026-06-23 16:48:12` | `cowrie.session.params` |
| `2026-06-23 16:48:12` | `cowrie.command.input` |
| `2026-06-23 16:48:12` | `cowrie.log.closed` |
| `2026-06-23 16:48:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02d443f9c80a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:48 |
| **Last Seen** | 2026-06-23 16:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:48:14` | `cowrie.session.connect` |
| `2026-06-23 16:48:14` | `cowrie.client.version` |
| `2026-06-23 16:48:14` | `cowrie.client.kex` |
| `2026-06-23 16:48:15` | `cowrie.login.success` |
| `2026-06-23 16:48:16` | `cowrie.session.params` |
| `2026-06-23 16:48:16` | `cowrie.command.input` |
| `2026-06-23 16:48:16` | `cowrie.command.input` |
| `2026-06-23 16:48:16` | `cowrie.command.input` |
| `2026-06-23 16:48:16` | `cowrie.command.input` |
| `2026-06-23 16:48:17` | `cowrie.log.closed` |
| `2026-06-23 16:48:18` | `cowrie.session.params` |
| `2026-06-23 16:48:18` | `cowrie.command.input` |
| `2026-06-23 16:48:18` | `cowrie.command.input` |
| `2026-06-23 16:48:18` | `cowrie.command.failed` |
| `2026-06-23 16:48:18` | `cowrie.command.failed` |
| `2026-06-23 16:48:18` | `cowrie.command.failed` |
| `2026-06-23 16:48:18` | `cowrie.command.failed` |
| `2026-06-23 16:48:18` | `cowrie.log.closed` |
| `2026-06-23 16:48:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56c05490681c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:49 |
| **Last Seen** | 2026-06-23 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:49:00` | `cowrie.session.connect` |
| `2026-06-23 16:49:00` | `cowrie.client.version` |
| `2026-06-23 16:49:00` | `cowrie.client.kex` |
| `2026-06-23 16:49:00` | `cowrie.login.success` |
| `2026-06-23 16:49:01` | `cowrie.session.params` |
| `2026-06-23 16:49:01` | `cowrie.command.input` |
| `2026-06-23 16:49:01` | `cowrie.log.closed` |
| `2026-06-23 16:49:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-042fc71cb852

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:49 |
| **Last Seen** | 2026-06-23 16:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:49:13` | `cowrie.session.connect` |
| `2026-06-23 16:49:13` | `cowrie.client.version` |
| `2026-06-23 16:49:13` | `cowrie.client.kex` |
| `2026-06-23 16:49:14` | `cowrie.login.success` |
| `2026-06-23 16:49:16` | `cowrie.session.params` |
| `2026-06-23 16:49:16` | `cowrie.command.input` |
| `2026-06-23 16:49:16` | `cowrie.command.input` |
| `2026-06-23 16:49:16` | `cowrie.command.input` |
| `2026-06-23 16:49:16` | `cowrie.command.input` |
| `2026-06-23 16:49:16` | `cowrie.log.closed` |
| `2026-06-23 16:49:17` | `cowrie.session.params` |
| `2026-06-23 16:49:17` | `cowrie.command.input` |
| `2026-06-23 16:49:17` | `cowrie.command.input` |
| `2026-06-23 16:49:17` | `cowrie.command.failed` |
| `2026-06-23 16:49:17` | `cowrie.command.failed` |
| `2026-06-23 16:49:17` | `cowrie.command.failed` |
| `2026-06-23 16:49:17` | `cowrie.command.failed` |
| `2026-06-23 16:49:17` | `cowrie.log.closed` |
| `2026-06-23 16:49:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a02fe2c01255

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:49 |
| **Last Seen** | 2026-06-23 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:49:49` | `cowrie.session.connect` |
| `2026-06-23 16:49:49` | `cowrie.client.version` |
| `2026-06-23 16:49:50` | `cowrie.client.kex` |
| `2026-06-23 16:49:50` | `cowrie.login.success` |
| `2026-06-23 16:49:51` | `cowrie.session.params` |
| `2026-06-23 16:49:51` | `cowrie.command.input` |
| `2026-06-23 16:49:51` | `cowrie.log.closed` |
| `2026-06-23 16:49:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-770802fcd9f8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:50 |
| **Last Seen** | 2026-06-23 16:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123456' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:50:13` | `cowrie.session.connect` |
| `2026-06-23 16:50:13` | `cowrie.client.version` |
| `2026-06-23 16:50:13` | `cowrie.client.kex` |
| `2026-06-23 16:50:15` | `cowrie.login.success` |
| `2026-06-23 16:50:17` | `cowrie.session.params` |
| `2026-06-23 16:50:17` | `cowrie.command.input` |
| `2026-06-23 16:50:17` | `cowrie.command.input` |
| `2026-06-23 16:50:17` | `cowrie.command.input` |
| `2026-06-23 16:50:17` | `cowrie.command.input` |
| `2026-06-23 16:50:17` | `cowrie.log.closed` |
| `2026-06-23 16:50:18` | `cowrie.session.params` |
| `2026-06-23 16:50:18` | `cowrie.command.input` |
| `2026-06-23 16:50:18` | `cowrie.command.input` |
| `2026-06-23 16:50:18` | `cowrie.command.failed` |
| `2026-06-23 16:50:18` | `cowrie.command.failed` |
| `2026-06-23 16:50:18` | `cowrie.command.failed` |
| `2026-06-23 16:50:18` | `cowrie.command.failed` |
| `2026-06-23 16:50:18` | `cowrie.log.closed` |
| `2026-06-23 16:50:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-250297c381c0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:50 |
| **Last Seen** | 2026-06-23 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:50:44` | `cowrie.session.connect` |
| `2026-06-23 16:50:44` | `cowrie.client.version` |
| `2026-06-23 16:50:44` | `cowrie.client.kex` |
| `2026-06-23 16:50:44` | `cowrie.login.success` |
| `2026-06-23 16:50:45` | `cowrie.session.params` |
| `2026-06-23 16:50:45` | `cowrie.command.input` |
| `2026-06-23 16:50:45` | `cowrie.log.closed` |
| `2026-06-23 16:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bae6336d3ced

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:51 |
| **Last Seen** | 2026-06-23 16:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234567' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:51:20` | `cowrie.session.connect` |
| `2026-06-23 16:51:20` | `cowrie.client.version` |
| `2026-06-23 16:51:20` | `cowrie.client.kex` |
| `2026-06-23 16:51:23` | `cowrie.login.success` |
| `2026-06-23 16:51:24` | `cowrie.session.params` |
| `2026-06-23 16:51:24` | `cowrie.command.input` |
| `2026-06-23 16:51:24` | `cowrie.command.input` |
| `2026-06-23 16:51:24` | `cowrie.command.input` |
| `2026-06-23 16:51:24` | `cowrie.command.input` |
| `2026-06-23 16:51:24` | `cowrie.log.closed` |
| `2026-06-23 16:51:25` | `cowrie.session.params` |
| `2026-06-23 16:51:25` | `cowrie.command.input` |
| `2026-06-23 16:51:25` | `cowrie.command.input` |
| `2026-06-23 16:51:25` | `cowrie.command.failed` |
| `2026-06-23 16:51:25` | `cowrie.command.failed` |
| `2026-06-23 16:51:25` | `cowrie.command.failed` |
| `2026-06-23 16:51:25` | `cowrie.command.failed` |
| `2026-06-23 16:51:26` | `cowrie.log.closed` |
| `2026-06-23 16:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f54499baf33

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:51 |
| **Last Seen** | 2026-06-23 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:51:41` | `cowrie.session.connect` |
| `2026-06-23 16:51:41` | `cowrie.client.version` |
| `2026-06-23 16:51:41` | `cowrie.client.kex` |
| `2026-06-23 16:51:41` | `cowrie.login.success` |
| `2026-06-23 16:51:42` | `cowrie.session.params` |
| `2026-06-23 16:51:42` | `cowrie.command.input` |
| `2026-06-23 16:51:42` | `cowrie.log.closed` |
| `2026-06-23 16:51:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-605a679323fe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:52 |
| **Last Seen** | 2026-06-23 16:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345678' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:52:26` | `cowrie.session.connect` |
| `2026-06-23 16:52:26` | `cowrie.client.version` |
| `2026-06-23 16:52:26` | `cowrie.client.kex` |
| `2026-06-23 16:52:27` | `cowrie.login.success` |
| `2026-06-23 16:52:29` | `cowrie.session.params` |
| `2026-06-23 16:52:29` | `cowrie.command.input` |
| `2026-06-23 16:52:29` | `cowrie.command.input` |
| `2026-06-23 16:52:29` | `cowrie.command.input` |
| `2026-06-23 16:52:29` | `cowrie.command.input` |
| `2026-06-23 16:52:29` | `cowrie.log.closed` |
| `2026-06-23 16:52:30` | `cowrie.session.params` |
| `2026-06-23 16:52:30` | `cowrie.command.input` |
| `2026-06-23 16:52:30` | `cowrie.command.input` |
| `2026-06-23 16:52:30` | `cowrie.command.failed` |
| `2026-06-23 16:52:30` | `cowrie.command.failed` |
| `2026-06-23 16:52:30` | `cowrie.command.failed` |
| `2026-06-23 16:52:30` | `cowrie.command.failed` |
| `2026-06-23 16:52:30` | `cowrie.log.closed` |
| `2026-06-23 16:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02610f86e323

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:52 |
| **Last Seen** | 2026-06-23 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:52:30` | `cowrie.session.connect` |
| `2026-06-23 16:52:30` | `cowrie.client.version` |
| `2026-06-23 16:52:31` | `cowrie.client.kex` |
| `2026-06-23 16:52:31` | `cowrie.login.success` |
| `2026-06-23 16:52:32` | `cowrie.session.params` |
| `2026-06-23 16:52:32` | `cowrie.command.input` |
| `2026-06-23 16:52:32` | `cowrie.log.closed` |
| `2026-06-23 16:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e18e74cd640

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:53 |
| **Last Seen** | 2026-06-23 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:53:20` | `cowrie.session.connect` |
| `2026-06-23 16:53:20` | `cowrie.client.version` |
| `2026-06-23 16:53:20` | `cowrie.client.kex` |
| `2026-06-23 16:53:20` | `cowrie.login.success` |
| `2026-06-23 16:53:21` | `cowrie.session.params` |
| `2026-06-23 16:53:21` | `cowrie.command.input` |
| `2026-06-23 16:53:21` | `cowrie.log.closed` |
| `2026-06-23 16:53:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-919500eb9251

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:53 |
| **Last Seen** | 2026-06-23 16:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123456789' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:53:22` | `cowrie.session.connect` |
| `2026-06-23 16:53:23` | `cowrie.client.version` |
| `2026-06-23 16:53:23` | `cowrie.client.kex` |
| `2026-06-23 16:53:24` | `cowrie.login.success` |
| `2026-06-23 16:53:25` | `cowrie.session.params` |
| `2026-06-23 16:53:25` | `cowrie.command.input` |
| `2026-06-23 16:53:25` | `cowrie.command.input` |
| `2026-06-23 16:53:25` | `cowrie.command.input` |
| `2026-06-23 16:53:25` | `cowrie.command.input` |
| `2026-06-23 16:53:26` | `cowrie.log.closed` |
| `2026-06-23 16:53:27` | `cowrie.session.params` |
| `2026-06-23 16:53:27` | `cowrie.command.input` |
| `2026-06-23 16:53:27` | `cowrie.command.input` |
| `2026-06-23 16:53:27` | `cowrie.command.failed` |
| `2026-06-23 16:53:27` | `cowrie.command.failed` |
| `2026-06-23 16:53:27` | `cowrie.command.failed` |
| `2026-06-23 16:53:27` | `cowrie.command.failed` |
| `2026-06-23 16:53:27` | `cowrie.log.closed` |
| `2026-06-23 16:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc62ab5fde75

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 16:53 |
| **Last Seen** | 2026-06-23 16:54 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:53:49` | `cowrie.session.connect` |
| `2026-06-23 16:53:50` | `cowrie.client.version` |
| `2026-06-23 16:53:50` | `cowrie.client.kex` |
| `2026-06-23 16:53:56` | `cowrie.login.success` |
| `2026-06-23 16:54:00` | `cowrie.session.params` |
| `2026-06-23 16:54:00` | `cowrie.command.input` |
| `2026-06-23 16:54:01` | `cowrie.log.closed` |
| `2026-06-23 16:54:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cf5616c5529

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:54 |
| **Last Seen** | 2026-06-23 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:54:09` | `cowrie.session.connect` |
| `2026-06-23 16:54:09` | `cowrie.client.version` |
| `2026-06-23 16:54:09` | `cowrie.client.kex` |
| `2026-06-23 16:54:10` | `cowrie.login.success` |
| `2026-06-23 16:54:11` | `cowrie.session.params` |
| `2026-06-23 16:54:11` | `cowrie.command.input` |
| `2026-06-23 16:54:11` | `cowrie.log.closed` |
| `2026-06-23 16:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc475e101e41

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:54 |
| **Last Seen** | 2026-06-23 16:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234567890' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:54:20` | `cowrie.session.connect` |
| `2026-06-23 16:54:20` | `cowrie.client.version` |
| `2026-06-23 16:54:20` | `cowrie.client.kex` |
| `2026-06-23 16:54:22` | `cowrie.login.success` |
| `2026-06-23 16:54:23` | `cowrie.session.params` |
| `2026-06-23 16:54:23` | `cowrie.command.input` |
| `2026-06-23 16:54:23` | `cowrie.command.input` |
| `2026-06-23 16:54:23` | `cowrie.command.input` |
| `2026-06-23 16:54:23` | `cowrie.command.input` |
| `2026-06-23 16:54:24` | `cowrie.log.closed` |
| `2026-06-23 16:54:25` | `cowrie.session.params` |
| `2026-06-23 16:54:25` | `cowrie.command.input` |
| `2026-06-23 16:54:25` | `cowrie.command.input` |
| `2026-06-23 16:54:25` | `cowrie.command.failed` |
| `2026-06-23 16:54:25` | `cowrie.command.failed` |
| `2026-06-23 16:54:25` | `cowrie.command.failed` |
| `2026-06-23 16:54:25` | `cowrie.command.failed` |
| `2026-06-23 16:54:25` | `cowrie.log.closed` |
| `2026-06-23 16:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d05d8733653a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:54 |
| **Last Seen** | 2026-06-23 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:54:58` | `cowrie.session.connect` |
| `2026-06-23 16:54:58` | `cowrie.client.version` |
| `2026-06-23 16:54:58` | `cowrie.client.kex` |
| `2026-06-23 16:54:58` | `cowrie.login.success` |
| `2026-06-23 16:54:59` | `cowrie.session.params` |
| `2026-06-23 16:54:59` | `cowrie.command.input` |
| `2026-06-23 16:54:59` | `cowrie.log.closed` |
| `2026-06-23 16:54:59` | `cowrie.session.closed` |

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
| `209.99.185[.]59` | **131** | 2026-06-23 14:55 | 2026-06-23 16:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `159.65.233[.]253` | **3** | 2026-06-23 15:19 | 2026-06-23 16:10 | 3m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]93` | **3** | 2026-06-23 16:26 | 2026-06-23 16:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]6` | **2** | 2026-06-23 16:22 | 2026-06-23 16:29 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.94.9[.]55` | 1 | 2026-06-23 16:12 | 2026-06-23 16:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]92` | 1 | 2026-06-23 15:04 | 2026-06-23 15:04 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.195[.]59` | 1 | 2026-06-23 16:50 | 2026-06-23 16:50 | 15s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (29 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 61/100 | 🟡 MEDIUM | **3/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/73** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **38/73** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **42/73** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 60/100 | 🟡 MEDIUM | 0/76 ✅ |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **37/73** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318` | Unknown binary | `ea73a088909b5311...` | 55/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `eaf9adb4bb80316a3aafceabc0f2ed2aed7c76cf134b9b7c66226fc4f003aa97` | ELF Binary (Linux executable) (x86-64 64-bit) | `eaf9adb4bb80316a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |
| `209.99.185[.]59` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 22 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `176.65.139[.]92` | NL | Storm Industries LLC | **100** ⚠️ | 6 |
| `91.92.40[.]6` | NL | TechTies Inc. | **100** ⚠️ | 23 |
| `66.132.224[.]93` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `172.94.9[.]55` | NL | Secure Internet LLC (UK) | **100** ⚠️ | 46 |
| `66.132.195[.]59` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 278 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 256 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 29 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 27 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 18 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 423 cases |
| Tool 34  | Credential Extractor        | ✅ 258 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 17 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (5.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 29 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 256 priority case(s) shown individually · 7 recon entry/entries in table (4 group(s) consolidating 139 session(s)).

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
_Report time: 2026-06-23T18:01:37Z_

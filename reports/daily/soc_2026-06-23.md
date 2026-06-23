# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-23 |
| **Generated At** | 2026-06-23T21:45:23Z |
| **Shift Time** | 21:45 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **756** |
| Confirmed Threats | **713** |
| False Positives Filtered | **43** (5.7%) |
| Unique Attacker IPs | **37** |
| Countries of Origin | **11** |
| High Severity Cases | **389** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **367** |
| Malware Samples Analyzed | **4** HIGH · **24** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **390** |
| Unique Credential Pairs | **377** |
| Unique Usernames | **168** |
| Unique Passwords | **285** |
| Successful Auth Pairs | **383** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 129 |
| `ubuntu` | 19 |
| `debian` | 14 |
| `admin` | 13 |
| `developer` | 13 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 27 |
| `123` | 12 |
| `admin123` | 7 |
| `abc123` | 6 |
| `password` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `123@@@` | 4 |
| `root` | `LeitboGi0ro` | 4 |
| `root` | `smo@@kkklss` | 3 |
| `admin` | `admin` | 3 |
| `root` | `` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `1q2w3e4r` | `91.92.40.6` | 2026-06-23T16:55:20 |
| `yskim` | `yskim` | `209.99.185.59` | 2026-06-23T16:55:47 |
| `admin` | `P@ssw0rd123` | `91.92.40.6` | 2026-06-23T16:56:18 |
| `root` | `oracol123` | `209.99.185.59` | 2026-06-23T16:56:42 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-23T16:56:58 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-23T16:56:58 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-23T16:57:01 |
| `admin` | `abc123` | `91.92.40.6` | 2026-06-23T16:57:16 |
| `node` | `zy035346` | `209.99.185.59` | 2026-06-23T16:57:32 |
| `admin` | `admin123` | `91.92.40.6` | 2026-06-23T16:58:14 |
| `api` | `api` | `209.99.185.59` | 2026-06-23T16:58:20 |
| `ue` | `ue` | `209.99.185.59` | 2026-06-23T16:59:08 |
| `admin` | `letmein` | `91.92.40.6` | 2026-06-23T16:59:11 |
| `et22-liy` | `Ly1234` | `209.99.185.59` | 2026-06-23T17:00:00 |
| `admin` | `pass123` | `91.92.40.6` | 2026-06-23T17:00:09 |
| `hyq` | `hyq123` | `209.99.185.59` | 2026-06-23T17:00:51 |
| `admin` | `password` | `91.92.40.6` | 2026-06-23T17:01:07 |
| `vps` | `654321` | `209.99.185.59` | 2026-06-23T17:01:43 |
| `admin` | `password1` | `91.92.40.6` | 2026-06-23T17:02:05 |
| `root` | `3edc4rfv5tgb` | `209.99.185.59` | 2026-06-23T17:02:37 |
| `admin` | `qwerty123` | `91.92.40.6` | 2026-06-23T17:03:02 |
| `root` | `sasha123` | `209.99.185.59` | 2026-06-23T17:03:30 |
| `admin` | `root123` | `91.92.40.6` | 2026-06-23T17:04:00 |
| `weihuang` | `weihuang` | `209.99.185.59` | 2026-06-23T17:04:20 |
| `admin1` | `123` | `91.92.40.6` | 2026-06-23T17:04:59 |
| `root` | `QWERasdf1234` | `209.99.185.59` | 2026-06-23T17:05:09 |
| `admin1` | `1234` | `91.92.40.6` | 2026-06-23T17:05:57 |
| `libuuid` | `libuuid` | `209.99.185.59` | 2026-06-23T17:06:00 |
| `cx` | `123456` | `209.99.185.59` | 2026-06-23T17:06:50 |
| `admin1` | `admin123` | `91.92.40.6` | 2026-06-23T17:06:54 |
| `wangyan` | `wangyan` | `209.99.185.59` | 2026-06-23T17:07:47 |
| `admin1` | `password1` | `91.92.40.6` | 2026-06-23T17:07:51 |
| `root` | `Painter` | `45.205.1.42` | 2026-06-23T17:08:04 |
| `chat` | `123456` | `209.99.185.59` | 2026-06-23T17:08:41 |
| `admin1` | `qwerty123` | `91.92.40.6` | 2026-06-23T17:08:48 |
| `root` | `server2` | `209.99.185.59` | 2026-06-23T17:09:32 |
| `administrator` | `123` | `91.92.40.6` | 2026-06-23T17:09:45 |
| `root` | `RootRoot` | `209.99.185.59` | 2026-06-23T17:10:24 |
| `administrator` | `1234` | `91.92.40.6` | 2026-06-23T17:10:43 |
| `local` | `changeme123` | `209.99.185.59` | 2026-06-23T17:11:14 |
| `administrator` | `123abc` | `91.92.40.6` | 2026-06-23T17:11:38 |
| `root` | `orkancloud` | `209.99.185.59` | 2026-06-23T17:12:05 |
| `administrator` | `1q2w3e4r` | `91.92.40.6` | 2026-06-23T17:12:34 |
| `devuser` | `changeme123` | `209.99.185.59` | 2026-06-23T17:12:55 |
| `administrator` | `admin123` | `91.92.40.6` | 2026-06-23T17:13:30 |
| `root` | `spid2019` | `209.99.185.59` | 2026-06-23T17:13:47 |
| `administrator` | `qwerty123` | `91.92.40.6` | 2026-06-23T17:14:27 |
| `ljd` | `123456` | `209.99.185.59` | 2026-06-23T17:14:39 |
| `apache` | `1234` | `91.92.40.6` | 2026-06-23T17:15:24 |
| `work` | `work` | `209.99.185.59` | 2026-06-23T17:15:32 |
| `backup` | `123` | `91.92.40.6` | 2026-06-23T17:16:21 |
| `userroot` | `userroot` | `209.99.185.59` | 2026-06-23T17:16:25 |
| `tomcat` | `abcd1234` | `209.99.185.59` | 2026-06-23T17:17:17 |
| `backup` | `12345678` | `91.92.40.6` | 2026-06-23T17:17:20 |
| `root` | `dPictImaging-01` | `209.99.185.59` | 2026-06-23T17:18:08 |
| `backup` | `password` | `91.92.40.6` | 2026-06-23T17:18:16 |
| `admin` | `admin` | `34.38.222.164` | 2026-06-23T17:18:41 |
| `root` | `a123456a` | `209.99.185.59` | 2026-06-23T17:18:59 |
| `daemon` | `123456` | `91.92.40.6` | 2026-06-23T17:19:12 |
| `xyf` | `123456` | `209.99.185.59` | 2026-06-23T17:19:49 |
| `daemon` | `abc123` | `91.92.40.6` | 2026-06-23T17:20:10 |
| `root` | `cti` | `209.99.185.59` | 2026-06-23T17:20:41 |
| `debian` | `123` | `91.92.40.6` | 2026-06-23T17:21:08 |
| `mysql` | `changeme` | `209.99.185.59` | 2026-06-23T17:21:35 |
| `ubuntu` | `123qwe` | `45.205.1.42` | 2026-06-23T17:22:02 |
| `debian` | `1234` | `91.92.40.6` | 2026-06-23T17:22:06 |
| `cookie` | `cookie` | `209.99.185.59` | 2026-06-23T17:22:27 |
| `debian` | `12345` | `91.92.40.6` | 2026-06-23T17:23:05 |
| `postgres` | `password1` | `209.99.185.59` | 2026-06-23T17:23:19 |
| `debian` | `123456` | `91.92.40.6` | 2026-06-23T17:24:00 |
| `easyits` | `123456` | `209.99.185.59` | 2026-06-23T17:24:10 |
| `debian` | `12345678` | `91.92.40.6` | 2026-06-23T17:24:57 |
| `rds` | `rds` | `209.99.185.59` | 2026-06-23T17:25:01 |
| `root` | `hallo` | `209.99.185.59` | 2026-06-23T17:25:51 |
| `debian` | `123456789` | `91.92.40.6` | 2026-06-23T17:25:53 |
| `root` | `linux123` | `209.99.185.59` | 2026-06-23T17:26:44 |
| `debian` | `1234567890` | `91.92.40.6` | 2026-06-23T17:26:49 |
| `root` | `scan` | `209.99.185.59` | 2026-06-23T17:27:38 |
| `debian` | `1q2w3e4r` | `91.92.40.6` | 2026-06-23T17:27:46 |
| `root` | `xiaozhang` | `209.99.185.59` | 2026-06-23T17:28:33 |
| `debian` | `abc123` | `91.92.40.6` | 2026-06-23T17:28:42 |
| `prime` | `prime` | `209.99.185.59` | 2026-06-23T17:29:26 |
| `debian` | `admin123` | `91.92.40.6` | 2026-06-23T17:29:38 |
| `sammy` | `sammy` | `209.99.185.59` | 2026-06-23T17:30:19 |
| `debian` | `letmein` | `91.92.40.6` | 2026-06-23T17:30:35 |
| `root` | `z1` | `209.99.185.59` | 2026-06-23T17:31:12 |
| `debian` | `pass123` | `91.92.40.6` | 2026-06-23T17:31:31 |
| `ubuntu` | `asdlkj123` | `209.99.185.59` | 2026-06-23T17:32:05 |
| `debian` | `password` | `91.92.40.6` | 2026-06-23T17:32:26 |
| `zhh` | `zhh` | `209.99.185.59` | 2026-06-23T17:32:59 |
| `debian` | `qwerty123` | `91.92.40.6` | 2026-06-23T17:33:24 |
| `root` | `Passw0rd` | `209.99.185.59` | 2026-06-23T17:33:54 |
| `deploy` | `123` | `91.92.40.6` | 2026-06-23T17:34:21 |
| `ubuntu` | `!@#123` | `209.99.185.59` | 2026-06-23T17:34:50 |
| `deploy` | `1234` | `91.92.40.6` | 2026-06-23T17:35:20 |
| `weixiao` | `123456` | `209.99.185.59` | 2026-06-23T17:35:45 |
| `root` | `Qwer1` | `45.205.1.42` | 2026-06-23T17:36:09 |
| `deploy` | `1234567890` | `91.92.40.6` | 2026-06-23T17:36:17 |
| `root` | `` | `217.60.195.138` | 2026-06-23T17:36:19 |
| `root` | `333` | `209.99.185.59` | 2026-06-23T17:36:38 |
| `deploy` | `1q2w3e4r` | `91.92.40.6` | 2026-06-23T17:37:15 |
| `root` | `Password123$%^` | `209.99.185.59` | 2026-06-23T17:37:30 |
| `deploy` | `admin123` | `91.92.40.6` | 2026-06-23T17:38:12 |
| `dongshuowu` | `dongshuowu` | `209.99.185.59` | 2026-06-23T17:38:21 |
| `deploy` | `pass123` | `91.92.40.6` | 2026-06-23T17:39:08 |
| `zchen` | `999` | `209.99.185.59` | 2026-06-23T17:39:13 |
| `deploy` | `password1` | `91.92.40.6` | 2026-06-23T17:40:04 |
| `root` | `2wsx#EDC4rfv` | `209.99.185.59` | 2026-06-23T17:40:08 |
| `deploy` | `qwerty123` | `91.92.40.6` | 2026-06-23T17:41:01 |
| `dsadm` | `dsadm` | `209.99.185.59` | 2026-06-23T17:41:04 |
| `dev` | `12345` | `91.92.40.6` | 2026-06-23T17:41:57 |
| `root` | `OOOOOO` | `209.99.185.59` | 2026-06-23T17:42:00 |
| `dev` | `123456` | `91.92.40.6` | 2026-06-23T17:42:53 |
| `curelink` | `7582!bumin` | `209.99.185.59` | 2026-06-23T17:42:53 |
| `ftp` | `ftp@123` | `209.99.185.59` | 2026-06-23T17:43:46 |
| `dev` | `1234567` | `91.92.40.6` | 2026-06-23T17:43:48 |
| `damon` | `damon123` | `209.99.185.59` | 2026-06-23T17:44:38 |
| `dev` | `12345678` | `91.92.40.6` | 2026-06-23T17:44:45 |
| `ubuntu` | `davidvlad10` | `209.99.185.59` | 2026-06-23T17:45:33 |
| `dev` | `123456789` | `91.92.40.6` | 2026-06-23T17:45:44 |
| `hpy13` | `major3928` | `209.99.185.59` | 2026-06-23T17:46:29 |
| `dev` | `abc123` | `91.92.40.6` | 2026-06-23T17:46:41 |
| `Soyoun` | `korea2022` | `209.99.185.59` | 2026-06-23T17:47:24 |
| `dev` | `admin123` | `91.92.40.6` | 2026-06-23T17:47:38 |
| `sklep` | `sklep` | `209.99.185.59` | 2026-06-23T17:48:18 |
| `root` | `` | `141.11.88.100` | 2026-06-23T17:48:27 |
| `dev` | `password` | `91.92.40.6` | 2026-06-23T17:48:34 |
| `root` | `user1234` | `209.99.185.59` | 2026-06-23T17:49:11 |
| `developer` | `123` | `91.92.40.6` | 2026-06-23T17:49:30 |
| `root` | `sqlserver2005` | `209.99.185.59` | 2026-06-23T17:50:04 |
| `developer` | `1234` | `91.92.40.6` | 2026-06-23T17:50:27 |
| `root` | `qwe!@#$%^` | `45.205.1.42` | 2026-06-23T17:50:35 |
| `andre` | `andre` | `209.99.185.59` | 2026-06-23T17:50:56 |
| `developer` | `12345` | `91.92.40.6` | 2026-06-23T17:51:26 |
| `www-data` | `123` | `209.99.185.59` | 2026-06-23T17:51:49 |
| `developer` | `123456` | `91.92.40.6` | 2026-06-23T17:52:21 |
| `root` | `pass7` | `209.99.185.59` | 2026-06-23T17:52:46 |
| `developer` | `1234567` | `91.92.40.6` | 2026-06-23T17:53:19 |
| `chenliang` | `123456` | `209.99.185.59` | 2026-06-23T17:53:46 |
| `developer` | `12345678` | `91.92.40.6` | 2026-06-23T17:54:18 |
| `yuanwd` | `pass` | `209.99.185.59` | 2026-06-23T17:54:45 |
| `developer` | `123456789` | `91.92.40.6` | 2026-06-23T17:55:15 |
| `apache` | `pass` | `209.99.185.59` | 2026-06-23T17:55:43 |
| `developer` | `1234567890` | `91.92.40.6` | 2026-06-23T17:56:10 |
| `sport` | `sport` | `209.99.185.59` | 2026-06-23T17:56:40 |
| `developer` | `1q2w3e4r` | `91.92.40.6` | 2026-06-23T17:57:06 |
| `root` | `testpassword` | `209.99.185.59` | 2026-06-23T17:57:36 |
| `developer` | `abc123` | `91.92.40.6` | 2026-06-23T17:58:01 |
| `guest` | `guest123` | `209.99.185.59` | 2026-06-23T17:58:41 |
| `developer` | `admin123` | `91.92.40.6` | 2026-06-23T17:58:57 |
| `user` | `22&%DJO*8Ph@1ZlfyaT^Y8#Iw&Od0B&W` | `209.99.185.59` | 2026-06-23T17:59:41 |
| `developer` | `password` | `91.92.40.6` | 2026-06-23T17:59:54 |
| `guest` | `qwerty123456` | `209.99.185.59` | 2026-06-23T18:00:34 |
| `developer` | `password1` | `91.92.40.6` | 2026-06-23T18:00:49 |
| `nand` | `nandnand` | `209.99.185.59` | 2026-06-23T18:01:17 |
| `ghost` | `ghost1234` | `209.99.185.59` | 2026-06-23T18:02:00 |
| `root` | `qwe1234%^&` | `209.99.185.59` | 2026-06-23T18:02:43 |
| `root` | `Pa55word2009` | `209.99.185.59` | 2026-06-23T18:03:25 |
| `dzfp` | `x` | `209.99.185.59` | 2026-06-23T18:04:08 |
| `root` | `Password#1234567890` | `45.205.1.42` | 2026-06-23T18:04:49 |
| `testing` | `111111` | `209.99.185.59` | 2026-06-23T18:04:53 |
| `gitea` | `gitea` | `209.99.185.59` | 2026-06-23T18:05:40 |
| `srman` | `1eogksalsrnr` | `209.99.185.59` | 2026-06-23T18:06:26 |
| `root` | `1234.com` | `209.99.185.59` | 2026-06-23T18:07:12 |
| `root` | `liuxiang` | `209.99.185.59` | 2026-06-23T18:07:57 |
| `git` | `changeme123` | `209.99.185.59` | 2026-06-23T18:08:41 |
| `root` | `Root@12345` | `209.99.185.59` | 2026-06-23T18:09:25 |
| `root` | `qwe@123456` | `209.99.185.59` | 2026-06-23T18:10:08 |
| `zhangsan` | `222222` | `209.99.185.59` | 2026-06-23T18:10:54 |
| `root` | `starwars` | `209.99.185.59` | 2026-06-23T18:11:39 |
| `root` | `unit` | `209.99.185.59` | 2026-06-23T18:12:24 |
| `lamps` | `lamps` | `209.99.185.59` | 2026-06-23T18:13:10 |
| `root` | `Sugon` | `209.99.185.59` | 2026-06-23T18:13:53 |
| `ubuntu` | `p4ssword` | `209.99.185.59` | 2026-06-23T18:14:36 |
| `root` | `1QAZ2WSX` | `209.99.185.59` | 2026-06-23T18:15:19 |
| `lb` | `123456` | `209.99.185.59` | 2026-06-23T18:16:02 |
| `lga` | `lga` | `209.99.185.59` | 2026-06-23T18:16:45 |
| `root` | `server$3210` | `209.99.185.59` | 2026-06-23T18:17:30 |
| `root` | `qw` | `209.99.185.59` | 2026-06-23T18:18:17 |
| `ta` | `ta` | `209.99.185.59` | 2026-06-23T18:19:03 |
| `root` | `Passw0rd11` | `45.205.1.42` | 2026-06-23T18:19:10 |
| `ubuntu` | `demo12345678` | `209.99.185.59` | 2026-06-23T18:19:51 |
| `jira` | `123` | `209.99.185.59` | 2026-06-23T18:20:37 |
| `ljt22` | `329182ljtL` | `209.99.185.59` | 2026-06-23T18:21:22 |
| `root` | `passcholkin121` | `209.99.185.59` | 2026-06-23T18:22:07 |
| `cuiyijia` | `cuiyijia` | `209.99.185.59` | 2026-06-23T18:22:51 |
| `jialh` | `jlh131415` | `209.99.185.59` | 2026-06-23T18:23:35 |
| `cyrus` | `cyrus1234` | `209.99.185.59` | 2026-06-23T18:24:20 |
| `fa` | `123456` | `209.99.185.59` | 2026-06-23T18:25:07 |
| `root` | `P455word123` | `209.99.185.59` | 2026-06-23T18:25:52 |
| `gwj` | `123456` | `209.99.185.59` | 2026-06-23T18:26:36 |
| `catadmin` | `admin@default` | `209.99.185.59` | 2026-06-23T18:27:20 |
| `root` | `!@#$%^&` | `209.99.185.59` | 2026-06-23T18:28:04 |
| `root` | `testpass` | `209.99.185.59` | 2026-06-23T18:28:50 |
| `peter` | `123456` | `209.99.185.59` | 2026-06-23T18:29:34 |
| `ftpuser` | `123` | `209.99.185.59` | 2026-06-23T18:30:19 |
| `sunmingming` | `simaqie` | `209.99.185.59` | 2026-06-23T18:31:05 |
| `ubuntu` | `11` | `209.99.185.59` | 2026-06-23T18:31:52 |
| `stu01` | `stu01` | `209.99.185.59` | 2026-06-23T18:32:39 |
| `chengkun` | `chufengxiao` | `209.99.185.59` | 2026-06-23T18:33:26 |
| `root` | `qazqaz` | `45.205.1.42` | 2026-06-23T18:33:32 |
| `pnp` | `pnp` | `209.99.185.59` | 2026-06-23T18:34:13 |
| `oracle` | `hunter` | `209.99.185.59` | 2026-06-23T18:34:59 |
| `ansible` | `12345678` | `209.99.185.59` | 2026-06-23T18:35:47 |
| `root` | `Root123456` | `209.99.185.59` | 2026-06-23T18:36:36 |
| `root` | `r00t123` | `209.99.185.59` | 2026-06-23T18:37:25 |
| `root` | `abc@@123` | `209.99.185.59` | 2026-06-23T18:38:14 |
| `scan` | `scan` | `209.99.185.59` | 2026-06-23T18:39:02 |
| `ubuntu` | `password123456789` | `209.99.185.59` | 2026-06-23T18:39:50 |
| `root` | `w3bmast3r` | `209.99.185.59` | 2026-06-23T18:40:38 |
| `root` | `ubuntu12345` | `209.99.185.59` | 2026-06-23T18:41:25 |
| `root` | `k8s@123` | `209.99.185.59` | 2026-06-23T18:42:12 |
| `postgres` | `qwer1234` | `209.99.185.59` | 2026-06-23T18:43:00 |
| `root` | `o9q1w2e3i8u7` | `209.99.185.59` | 2026-06-23T18:43:49 |
| `guochenyang` | `gcy506067668` | `209.99.185.59` | 2026-06-23T18:44:39 |
| `git` | `1qaz!QAZ` | `209.99.185.59` | 2026-06-23T18:45:30 |
| `root` | `4321` | `209.99.185.59` | 2026-06-23T18:46:20 |
| `root` | `abcdpass` | `209.99.185.59` | 2026-06-23T18:47:10 |
| `root` | `qwertasdfg` | `45.205.1.42` | 2026-06-23T18:47:46 |
| `root` | `!a1357911` | `209.99.185.59` | 2026-06-23T18:47:59 |
| `ubuntu` | `pass1234567` | `209.99.185.59` | 2026-06-23T18:48:48 |
| `zhangruida` | `zhangruida2021` | `209.99.185.59` | 2026-06-23T18:49:38 |
| `lzy21` | `123456` | `209.99.185.59` | 2026-06-23T18:50:30 |
| `hd` | `hd@123` | `209.99.185.59` | 2026-06-23T18:51:21 |
| `root` | `debianadmin` | `209.99.185.59` | 2026-06-23T18:52:13 |
| `yanghuan` | `yanghuan` | `209.99.185.59` | 2026-06-23T18:53:03 |
| `uftp` | `pass123` | `209.99.185.59` | 2026-06-23T18:53:53 |
| `es` | `12345` | `209.99.185.59` | 2026-06-23T18:54:44 |
| `bjznk` | `Bjznk@5158` | `209.99.185.59` | 2026-06-23T18:55:40 |
| `root` | `%%codyy@1935!` | `209.99.185.59` | 2026-06-23T18:56:42 |
| `root` | `INeedSugaR321` | `209.99.185.59` | 2026-06-23T18:57:38 |
| `ubuntu` | `q1w2e3r4t5y6u` | `209.99.185.59` | 2026-06-23T18:58:30 |
| `root` | `qwer!234` | `209.99.185.59` | 2026-06-23T18:59:22 |
| `root` | `Pass123$%^` | `209.99.185.59` | 2026-06-23T19:00:13 |
| `root` | `258741` | `209.99.185.59` | 2026-06-23T19:01:04 |
| `root` | `qwe1234%` | `209.99.185.59` | 2026-06-23T19:01:56 |
| `root` | `Pass@word123!@#` | `45.205.1.42` | 2026-06-23T19:02:01 |
| `xieqingxiang` | `xieqingxiang` | `209.99.185.59` | 2026-06-23T19:02:49 |
| `badmin` | `sd.30df.1s,m1` | `209.99.185.59` | 2026-06-23T19:03:42 |
| `marsboard` | `marsboard` | `209.99.185.59` | 2026-06-23T19:04:35 |
| `mks` | `mks123` | `209.99.185.59` | 2026-06-23T19:05:27 |
| `root` | `2402301978` | `209.99.185.59` | 2026-06-23T19:06:19 |
| `liguangqi` | `liguangqi` | `209.99.185.59` | 2026-06-23T19:07:11 |
| `songshuai` | `ss123456` | `209.99.185.59` | 2026-06-23T19:08:03 |
| `student4` | `student4` | `209.99.185.59` | 2026-06-23T19:08:55 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-23T19:09:24 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-23T19:09:24 |
| `linchunli` | `linchunli123` | `209.99.185.59` | 2026-06-23T19:09:48 |
| `device` | `123` | `209.99.185.59` | 2026-06-23T19:10:42 |
| `oracle` | `wasd` | `209.99.185.59` | 2026-06-23T19:11:35 |
| `root` | `inetd` | `209.99.185.59` | 2026-06-23T19:12:28 |
| `mzf` | `123456` | `209.99.185.59` | 2026-06-23T19:13:21 |
| `server` | `abc123` | `209.99.185.59` | 2026-06-23T19:14:15 |
| `root` | `Qa123456` | `209.99.185.59` | 2026-06-23T19:15:09 |
| `hsj` | `korea2013` | `209.99.185.59` | 2026-06-23T19:16:03 |
| `root` | `qsczse` | `45.205.1.42` | 2026-06-23T19:16:21 |
| `jlgao` | `jlgao` | `209.99.185.59` | 2026-06-23T19:16:57 |
| `lizepeng` | `lizepeng` | `209.99.185.59` | 2026-06-23T19:17:50 |
| `zwl` | `123456` | `209.99.185.59` | 2026-06-23T19:18:42 |
| `ubuntu` | `123456` | `209.99.185.59` | 2026-06-23T19:19:34 |
| `root` | `Vtpl@0612` | `209.99.185.59` | 2026-06-23T19:20:27 |
| `log` | `log` | `209.99.185.59` | 2026-06-23T19:21:20 |
| `root` | `adminsa` | `209.99.185.59` | 2026-06-23T19:22:15 |
| `root` | `qazwsxedcrfvtgbyhn` | `209.99.185.59` | 2026-06-23T19:23:10 |
| `test` | `333333` | `209.99.185.59` | 2026-06-23T19:24:05 |
| `informat` | `123456` | `209.99.185.59` | 2026-06-23T19:24:59 |
| `root` | `qazsw2` | `209.99.185.59` | 2026-06-23T19:25:54 |
| `asem00` | `asem00` | `209.99.185.59` | 2026-06-23T19:26:47 |
| `root` | `1234q` | `209.99.185.59` | 2026-06-23T19:27:42 |
| `jbn` | `jbn` | `209.99.185.59` | 2026-06-23T19:28:37 |
| `root` | `---fuck_you----` | `121.29.5.231` | 2026-06-23T19:28:48 |
| `root` | `woaini123` | `209.99.185.59` | 2026-06-23T19:29:33 |
| `weblogic` | `weblogic` | `209.99.185.59` | 2026-06-23T19:30:28 |
| `ubuntu` | `PASSWORD` | `45.205.1.42` | 2026-06-23T19:30:43 |
| `ubuntu` | `321` | `209.99.185.59` | 2026-06-23T19:31:24 |
| `root` | `linode.com` | `209.99.185.59` | 2026-06-23T19:32:19 |
| `site8030` | `site8030` | `209.99.185.59` | 2026-06-23T19:33:14 |
| `cw` | `dslb136cw` | `209.99.185.59` | 2026-06-23T19:34:09 |
| `admin` | `admin` | `118.194.235.105` | 2026-06-23T19:34:57 |
| `sunyq19` | `971219` | `209.99.185.59` | 2026-06-23T19:35:07 |
| `ubuntu` | `qwerty09` | `209.99.185.59` | 2026-06-23T19:36:04 |
| `magic` | `Magic2019` | `209.99.185.59` | 2026-06-23T19:37:02 |
| `iexcel_qingdao` | `iexcel_qingdao123` | `209.99.185.59` | 2026-06-23T19:37:59 |
| `hcm` | `hcm` | `209.99.185.59` | 2026-06-23T19:38:56 |
| `www-data` | `www-data@2021` | `209.99.185.59` | 2026-06-23T19:39:53 |
| `web` | `12345678` | `209.99.185.59` | 2026-06-23T19:40:51 |
| `cxc768` | `QAZwsx768@` | `209.99.185.59` | 2026-06-23T19:41:49 |
| `wzm` | `wzm123` | `209.99.185.59` | 2026-06-23T19:42:47 |
| `root` | `Zaq12wsx!` | `209.99.185.59` | 2026-06-23T19:43:44 |
| `lyh` | `lyj` | `209.99.185.59` | 2026-06-23T19:44:41 |
| `ubuntu` | `1a2s3d` | `45.205.1.42` | 2026-06-23T19:45:06 |
| `amandabackup` | `amandabackup1` | `209.99.185.59` | 2026-06-23T19:45:37 |
| `movies` | `123456` | `209.99.185.59` | 2026-06-23T19:46:35 |
| `trade` | `trade123` | `209.99.185.59` | 2026-06-23T19:47:33 |
| `git` | `test` | `209.99.185.59` | 2026-06-23T19:48:32 |
| `root` | `abc1234%` | `209.99.185.59` | 2026-06-23T19:49:30 |
| `yangliusha5` | `yangliusha5` | `209.99.185.59` | 2026-06-23T19:50:27 |
| `tempuser` | `tempuser` | `209.99.185.59` | 2026-06-23T19:51:23 |
| `root` | `ascend` | `209.99.185.59` | 2026-06-23T19:52:21 |
| `root` | `debian` | `61.240.17.66` | 2026-06-23T19:52:23 |
| `test` | `pgj-heu05HQM=bMvz` | `209.99.185.59` | 2026-06-23T19:53:19 |
| `root` | `admin!@#` | `209.99.185.59` | 2026-06-23T19:54:17 |
| `testuser` | `testuser123` | `209.99.185.59` | 2026-06-23T19:55:16 |
| `wyadmins` | `wyadmins` | `209.99.185.59` | 2026-06-23T19:56:14 |
| `root` | `center` | `209.99.185.59` | 2026-06-23T19:57:11 |
| `rust` | `rust` | `209.99.185.59` | 2026-06-23T19:58:07 |
| `shen` | `123456` | `209.99.185.59` | 2026-06-23T19:59:05 |
| `root` | `qw` | `45.205.1.42` | 2026-06-23T19:59:13 |
| `chris` | `Chris123` | `209.99.185.59` | 2026-06-23T20:00:04 |
| `git` | `git!!@@1` | `209.99.185.59` | 2026-06-23T20:00:53 |
| `root` | `qwerty1234567890` | `209.99.185.59` | 2026-06-23T20:01:39 |
| `root` | `z1a2q3!@#` | `209.99.185.59` | 2026-06-23T20:02:23 |
| `root` | `QAZ2WSX` | `209.99.185.59` | 2026-06-23T20:03:08 |
| `wyy` | `wyy123456` | `209.99.185.59` | 2026-06-23T20:03:52 |
| `ubuntu` | `a1a1a1` | `209.99.185.59` | 2026-06-23T20:04:38 |
| `db2fenc1` | `123` | `209.99.185.59` | 2026-06-23T20:05:24 |
| `root` | `12345qwert` | `209.99.185.59` | 2026-06-23T20:06:12 |
| `inspur` | `123456a!` | `209.99.185.59` | 2026-06-23T20:07:01 |
| `ts3` | `teamspeak` | `209.99.185.59` | 2026-06-23T20:07:50 |
| `root` | `protected` | `209.99.185.59` | 2026-06-23T20:08:38 |
| `root` | `r@@t` | `209.99.185.59` | 2026-06-23T20:09:27 |
| `root` | `r4e3w2q1` | `209.99.185.59` | 2026-06-23T20:10:12 |
| `hxd` | `hxd` | `209.99.185.59` | 2026-06-23T20:10:57 |
| `zhangwei4` | `zhangwei4` | `209.99.185.59` | 2026-06-23T20:11:44 |
| `root` | `giant@123phpadmin` | `209.99.185.59` | 2026-06-23T20:12:33 |
| `root` | `qwerty1` | `209.99.185.59` | 2026-06-23T20:13:22 |
| `root` | `7654321` | `45.205.1.42` | 2026-06-23T20:13:45 |
| `tibero` | `tibero` | `209.99.185.59` | 2026-06-23T20:14:11 |
| `root` | `***` | `209.99.185.59` | 2026-06-23T20:15:00 |
| `sunhr` | `123456` | `209.99.185.59` | 2026-06-23T20:15:47 |
| `hisense` | `hisense` | `209.99.185.59` | 2026-06-23T20:16:35 |
| `ubuntu` | `Pass1` | `209.99.185.59` | 2026-06-23T20:17:24 |
| `root` | `ZAQ!@WSX` | `209.99.185.59` | 2026-06-23T20:18:15 |
| `root` | `P4sswOrd` | `209.99.185.59` | 2026-06-23T20:19:05 |
| `rentai` | `Wednesday0713` | `209.99.185.59` | 2026-06-23T20:19:55 |
| `a` | `guest` | `209.99.185.59` | 2026-06-23T20:20:44 |
| `JiaYuxin` | `JiaYuxion` | `209.99.185.59` | 2026-06-23T20:21:33 |
| `userftp` | `userftp` | `209.99.185.59` | 2026-06-23T20:22:22 |
| `liugt` | `blabla123x!!!` | `209.99.185.59` | 2026-06-23T20:23:11 |
| `root` | `letmein1` | `209.99.185.59` | 2026-06-23T20:23:59 |
| `ubuntu` | `123456a` | `209.99.185.59` | 2026-06-23T20:24:48 |
| `root` | `2020` | `209.99.185.59` | 2026-06-23T20:25:37 |
| `ubuntu` | `q1w2e3r4t5` | `209.99.185.59` | 2026-06-23T20:26:27 |
| `root` | `6z66YC6P4T` | `10.0.0.73` | 2026-06-23T20:27:01 |
| `dodamx` | `1` | `209.99.185.59` | 2026-06-23T20:27:15 |
| `yangliusha6` | `yangliusha6` | `209.99.185.59` | 2026-06-23T20:28:03 |
| `root` | `Test1234` | `45.205.1.42` | 2026-06-23T20:28:06 |
| `` | `op:hadoop` | `209.99.185.59` | 2026-06-23T20:28:52 |
| `root` | `770713` | `209.99.185.59` | 2026-06-23T20:29:40 |
| `price` | `price` | `209.99.185.59` | 2026-06-23T20:30:28 |
| `root` | `sh123456` | `209.99.185.59` | 2026-06-23T20:31:16 |
| `root` | `qwertz12345` | `209.99.185.59` | 2026-06-23T20:32:05 |
| `xj` | `xiangjun-xj` | `209.99.185.59` | 2026-06-23T20:32:54 |
| `student1` | `123456` | `209.99.185.59` | 2026-06-23T20:33:43 |
| `app` | `app123456` | `209.99.185.59` | 2026-06-23T20:34:31 |
| `hlq` | `123456` | `209.99.185.59` | 2026-06-23T20:35:18 |
| `test` | `test2019` | `209.99.185.59` | 2026-06-23T20:36:04 |
| `zhaoliming` | `123456` | `209.99.185.59` | 2026-06-23T20:36:50 |
| `root` | `admin` | `192.42.116.101` | 2026-06-23T20:37:32 |
| `postgres` | `1q2w3e` | `209.99.185.59` | 2026-06-23T20:37:38 |
| `lixuan15` | `linear.com` | `209.99.185.59` | 2026-06-23T20:38:27 |
| `pul` | `password` | `209.99.185.59` | 2026-06-23T20:39:17 |
| `admbackup` | `Cliri$R00tBackup` | `209.99.185.59` | 2026-06-23T20:40:07 |
| `fk` | `123456` | `209.99.185.59` | 2026-06-23T20:40:55 |
| `angel` | `angel111111` | `209.99.185.59` | 2026-06-23T20:41:43 |
| `test01` | `Test@cii` | `209.99.185.59` | 2026-06-23T20:42:30 |
| `root` | `Passwd!@#456` | `45.205.1.42` | 2026-06-23T20:42:32 |
| `root` | `nctu1974` | `209.99.185.59` | 2026-06-23T20:43:19 |
| `nuri` | `nuri` | `209.99.185.59` | 2026-06-23T20:44:08 |
| `root` | `741` | `209.99.185.59` | 2026-06-23T20:44:57 |
| `root` | `root@5555` | `209.99.185.59` | 2026-06-23T20:45:48 |
| `test` | `password123` | `209.99.185.59` | 2026-06-23T20:46:37 |
| `root` | `pxf@123` | `209.99.185.59` | 2026-06-23T20:47:26 |
| `root` | `000000` | `209.99.185.59` | 2026-06-23T20:48:13 |
| `zyli` | `l6fhnl54Km` | `209.99.185.59` | 2026-06-23T20:49:00 |
| `stu02` | `stu02` | `209.99.185.59` | 2026-06-23T20:49:48 |
| `pul` | `123` | `209.99.185.59` | 2026-06-23T20:50:41 |
| `admin` | `admin` | `47.85.8.171` | 2026-06-23T20:51:20 |
| `root` | `Password#123` | `209.99.185.59` | 2026-06-23T20:51:32 |
| `zhaozhenchi` | `YJN539` | `209.99.185.59` | 2026-06-23T20:52:24 |
| `root` | `1234$#@!` | `209.99.185.59` | 2026-06-23T20:53:14 |
| `root` | `Lnlt@2019` | `209.99.185.59` | 2026-06-23T20:54:04 |
| `vbox` | `Vbox` | `209.99.185.59` | 2026-06-23T20:54:52 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **756** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 377 |
| libssh | 25 |
| Paramiko (Python) | 11 |
| Nmap scanner | 7 |
| OpenSSH | 6 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 299 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 70 | 1 |
| `a2de0f306611...` | Mirai/variant | 11 | 2 |
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |
| `98f63c4d9c87...` | Generic scanner | 5 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 299 | 2 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 70 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 24 | 5 | — |
| `a2de0f306611...` | Paramiko (Python) | 11 | 2 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 5 | 4 | Generic scanner |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 70 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |

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
echo '1q2w3e4r' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'
```
Source IPs: `91.92.40.6`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
echo ALIVE_CHECK
```
```
/bin/busybox TEST 2>&1
```
```
cat /proc 2>&1
```
```
./ 2>&1
```
Source IPs: `217.60.195.138`

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
Source IPs: `141.11.88.100`

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
| `AS396982` | Google LLC | 6 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS197170` | TechTies Inc. | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS402253` | SKN Subnet & Telecom Ltd | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (388)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1680698e8e75

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:55 |
| **Last Seen** | 2026-06-23 16:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1q2w3e4r' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:55:18` | `cowrie.session.connect` |
| `2026-06-23 16:55:19` | `cowrie.client.version` |
| `2026-06-23 16:55:19` | `cowrie.client.kex` |
| `2026-06-23 16:55:20` | `cowrie.login.success` |
| `2026-06-23 16:55:21` | `cowrie.session.params` |
| `2026-06-23 16:55:21` | `cowrie.command.input` |
| `2026-06-23 16:55:21` | `cowrie.command.input` |
| `2026-06-23 16:55:21` | `cowrie.command.input` |
| `2026-06-23 16:55:21` | `cowrie.command.input` |
| `2026-06-23 16:55:21` | `cowrie.log.closed` |
| `2026-06-23 16:55:22` | `cowrie.session.params` |
| `2026-06-23 16:55:22` | `cowrie.command.input` |
| `2026-06-23 16:55:22` | `cowrie.command.input` |
| `2026-06-23 16:55:22` | `cowrie.command.failed` |
| `2026-06-23 16:55:22` | `cowrie.command.failed` |
| `2026-06-23 16:55:22` | `cowrie.command.failed` |
| `2026-06-23 16:55:22` | `cowrie.command.failed` |
| `2026-06-23 16:55:23` | `cowrie.log.closed` |
| `2026-06-23 16:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-896152a51fd6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:55 |
| **Last Seen** | 2026-06-23 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:55:47` | `cowrie.session.connect` |
| `2026-06-23 16:55:47` | `cowrie.client.version` |
| `2026-06-23 16:55:47` | `cowrie.client.kex` |
| `2026-06-23 16:55:47` | `cowrie.login.success` |
| `2026-06-23 16:55:48` | `cowrie.session.params` |
| `2026-06-23 16:55:48` | `cowrie.command.input` |
| `2026-06-23 16:55:48` | `cowrie.log.closed` |
| `2026-06-23 16:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55dc09159a7a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:56 |
| **Last Seen** | 2026-06-23 16:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'P@ssw0rd123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:56:16` | `cowrie.session.connect` |
| `2026-06-23 16:56:16` | `cowrie.client.version` |
| `2026-06-23 16:56:16` | `cowrie.client.kex` |
| `2026-06-23 16:56:18` | `cowrie.login.success` |
| `2026-06-23 16:56:19` | `cowrie.session.params` |
| `2026-06-23 16:56:19` | `cowrie.command.input` |
| `2026-06-23 16:56:19` | `cowrie.command.input` |
| `2026-06-23 16:56:19` | `cowrie.command.input` |
| `2026-06-23 16:56:19` | `cowrie.command.input` |
| `2026-06-23 16:56:20` | `cowrie.log.closed` |
| `2026-06-23 16:56:20` | `cowrie.session.params` |
| `2026-06-23 16:56:20` | `cowrie.command.input` |
| `2026-06-23 16:56:20` | `cowrie.command.input` |
| `2026-06-23 16:56:20` | `cowrie.command.failed` |
| `2026-06-23 16:56:20` | `cowrie.command.failed` |
| `2026-06-23 16:56:20` | `cowrie.command.failed` |
| `2026-06-23 16:56:20` | `cowrie.command.failed` |
| `2026-06-23 16:56:21` | `cowrie.log.closed` |
| `2026-06-23 16:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e50c13bf8f70

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:56 |
| **Last Seen** | 2026-06-23 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:56:41` | `cowrie.session.connect` |
| `2026-06-23 16:56:41` | `cowrie.client.version` |
| `2026-06-23 16:56:41` | `cowrie.client.kex` |
| `2026-06-23 16:56:42` | `cowrie.login.success` |
| `2026-06-23 16:56:42` | `cowrie.session.params` |
| `2026-06-23 16:56:42` | `cowrie.command.input` |
| `2026-06-23 16:56:43` | `cowrie.log.closed` |
| `2026-06-23 16:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70509564ce17

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-23 16:56 |
| **Last Seen** | 2026-06-23 16:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:56:58` | `cowrie.session.connect` |
| `2026-06-23 16:56:58` | `cowrie.client.version` |
| `2026-06-23 16:56:58` | `cowrie.client.kex` |
| `2026-06-23 16:56:58` | `cowrie.login.success` |
| `2026-06-23 16:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64867cba5a8b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-23 16:56 |
| **Last Seen** | 2026-06-23 16:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:56:58` | `cowrie.session.connect` |
| `2026-06-23 16:56:58` | `cowrie.client.version` |
| `2026-06-23 16:56:58` | `cowrie.client.kex` |
| `2026-06-23 16:56:58` | `cowrie.login.success` |
| `2026-06-23 16:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db2c386b6c11

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-23 16:57 |
| **Last Seen** | 2026-06-23 16:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:57:00` | `cowrie.session.connect` |
| `2026-06-23 16:57:00` | `cowrie.client.version` |
| `2026-06-23 16:57:00` | `cowrie.client.kex` |
| `2026-06-23 16:57:01` | `cowrie.login.success` |
| `2026-06-23 16:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7718920d6d58

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-23 16:57 |
| **Last Seen** | 2026-06-23 16:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:57:01` | `cowrie.session.connect` |
| `2026-06-23 16:57:01` | `cowrie.client.version` |
| `2026-06-23 16:57:01` | `cowrie.client.kex` |
| `2026-06-23 16:57:01` | `cowrie.login.success` |
| `2026-06-23 16:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a52276b1ef8e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:57 |
| **Last Seen** | 2026-06-23 16:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'abc123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:57:14` | `cowrie.session.connect` |
| `2026-06-23 16:57:15` | `cowrie.client.version` |
| `2026-06-23 16:57:15` | `cowrie.client.kex` |
| `2026-06-23 16:57:16` | `cowrie.login.success` |
| `2026-06-23 16:57:17` | `cowrie.session.params` |
| `2026-06-23 16:57:17` | `cowrie.command.input` |
| `2026-06-23 16:57:17` | `cowrie.command.input` |
| `2026-06-23 16:57:17` | `cowrie.command.input` |
| `2026-06-23 16:57:17` | `cowrie.command.input` |
| `2026-06-23 16:57:18` | `cowrie.log.closed` |
| `2026-06-23 16:57:19` | `cowrie.session.params` |
| `2026-06-23 16:57:19` | `cowrie.command.input` |
| `2026-06-23 16:57:19` | `cowrie.command.input` |
| `2026-06-23 16:57:19` | `cowrie.command.failed` |
| `2026-06-23 16:57:19` | `cowrie.command.failed` |
| `2026-06-23 16:57:19` | `cowrie.command.failed` |
| `2026-06-23 16:57:19` | `cowrie.command.failed` |
| `2026-06-23 16:57:19` | `cowrie.log.closed` |
| `2026-06-23 16:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84f62d66ea54

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:57 |
| **Last Seen** | 2026-06-23 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:57:31` | `cowrie.session.connect` |
| `2026-06-23 16:57:31` | `cowrie.client.version` |
| `2026-06-23 16:57:31` | `cowrie.client.kex` |
| `2026-06-23 16:57:32` | `cowrie.login.success` |
| `2026-06-23 16:57:32` | `cowrie.session.params` |
| `2026-06-23 16:57:32` | `cowrie.command.input` |
| `2026-06-23 16:57:33` | `cowrie.log.closed` |
| `2026-06-23 16:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbae3ba4d62c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:58 |
| **Last Seen** | 2026-06-23 16:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'admin123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:58:12` | `cowrie.session.connect` |
| `2026-06-23 16:58:12` | `cowrie.client.version` |
| `2026-06-23 16:58:12` | `cowrie.client.kex` |
| `2026-06-23 16:58:14` | `cowrie.login.success` |
| `2026-06-23 16:58:15` | `cowrie.session.params` |
| `2026-06-23 16:58:15` | `cowrie.command.input` |
| `2026-06-23 16:58:15` | `cowrie.command.input` |
| `2026-06-23 16:58:15` | `cowrie.command.input` |
| `2026-06-23 16:58:15` | `cowrie.command.input` |
| `2026-06-23 16:58:15` | `cowrie.log.closed` |
| `2026-06-23 16:58:16` | `cowrie.session.params` |
| `2026-06-23 16:58:16` | `cowrie.command.input` |
| `2026-06-23 16:58:16` | `cowrie.command.input` |
| `2026-06-23 16:58:16` | `cowrie.command.failed` |
| `2026-06-23 16:58:16` | `cowrie.command.failed` |
| `2026-06-23 16:58:16` | `cowrie.command.failed` |
| `2026-06-23 16:58:16` | `cowrie.command.failed` |
| `2026-06-23 16:58:16` | `cowrie.log.closed` |
| `2026-06-23 16:58:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dff747834886

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:58 |
| **Last Seen** | 2026-06-23 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:58:19` | `cowrie.session.connect` |
| `2026-06-23 16:58:19` | `cowrie.client.version` |
| `2026-06-23 16:58:20` | `cowrie.client.kex` |
| `2026-06-23 16:58:20` | `cowrie.login.success` |
| `2026-06-23 16:58:21` | `cowrie.session.params` |
| `2026-06-23 16:58:21` | `cowrie.command.input` |
| `2026-06-23 16:58:21` | `cowrie.log.closed` |
| `2026-06-23 16:58:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c99a52fe910

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 16:59 |
| **Last Seen** | 2026-06-23 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:59:08` | `cowrie.session.connect` |
| `2026-06-23 16:59:08` | `cowrie.client.version` |
| `2026-06-23 16:59:08` | `cowrie.client.kex` |
| `2026-06-23 16:59:08` | `cowrie.login.success` |
| `2026-06-23 16:59:09` | `cowrie.session.params` |
| `2026-06-23 16:59:09` | `cowrie.command.input` |
| `2026-06-23 16:59:09` | `cowrie.log.closed` |
| `2026-06-23 16:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18aed5a73537

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 16:59 |
| **Last Seen** | 2026-06-23 16:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'letmein' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 16:59:09` | `cowrie.session.connect` |
| `2026-06-23 16:59:09` | `cowrie.client.version` |
| `2026-06-23 16:59:09` | `cowrie.client.kex` |
| `2026-06-23 16:59:11` | `cowrie.login.success` |
| `2026-06-23 16:59:13` | `cowrie.session.params` |
| `2026-06-23 16:59:13` | `cowrie.command.input` |
| `2026-06-23 16:59:13` | `cowrie.command.input` |
| `2026-06-23 16:59:13` | `cowrie.command.input` |
| `2026-06-23 16:59:13` | `cowrie.command.input` |
| `2026-06-23 16:59:13` | `cowrie.log.closed` |
| `2026-06-23 16:59:14` | `cowrie.session.params` |
| `2026-06-23 16:59:14` | `cowrie.command.input` |
| `2026-06-23 16:59:14` | `cowrie.command.input` |
| `2026-06-23 16:59:14` | `cowrie.command.failed` |
| `2026-06-23 16:59:14` | `cowrie.command.failed` |
| `2026-06-23 16:59:14` | `cowrie.command.failed` |
| `2026-06-23 16:59:14` | `cowrie.command.failed` |
| `2026-06-23 16:59:14` | `cowrie.log.closed` |
| `2026-06-23 16:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e0d26d2fcc8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:00 |
| **Last Seen** | 2026-06-23 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:00:00` | `cowrie.session.connect` |
| `2026-06-23 17:00:00` | `cowrie.client.version` |
| `2026-06-23 17:00:00` | `cowrie.client.kex` |
| `2026-06-23 17:00:00` | `cowrie.login.success` |
| `2026-06-23 17:00:01` | `cowrie.session.params` |
| `2026-06-23 17:00:01` | `cowrie.command.input` |
| `2026-06-23 17:00:01` | `cowrie.log.closed` |
| `2026-06-23 17:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3135c9a964c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:00 |
| **Last Seen** | 2026-06-23 17:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'pass123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:00:08` | `cowrie.session.connect` |
| `2026-06-23 17:00:08` | `cowrie.client.version` |
| `2026-06-23 17:00:08` | `cowrie.client.kex` |
| `2026-06-23 17:00:09` | `cowrie.login.success` |
| `2026-06-23 17:00:10` | `cowrie.session.params` |
| `2026-06-23 17:00:10` | `cowrie.command.input` |
| `2026-06-23 17:00:10` | `cowrie.command.input` |
| `2026-06-23 17:00:10` | `cowrie.command.input` |
| `2026-06-23 17:00:10` | `cowrie.command.input` |
| `2026-06-23 17:00:10` | `cowrie.log.closed` |
| `2026-06-23 17:00:12` | `cowrie.session.params` |
| `2026-06-23 17:00:12` | `cowrie.command.input` |
| `2026-06-23 17:00:12` | `cowrie.command.input` |
| `2026-06-23 17:00:12` | `cowrie.command.failed` |
| `2026-06-23 17:00:12` | `cowrie.command.failed` |
| `2026-06-23 17:00:12` | `cowrie.command.failed` |
| `2026-06-23 17:00:12` | `cowrie.command.failed` |
| `2026-06-23 17:00:12` | `cowrie.log.closed` |
| `2026-06-23 17:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74a4158ecbad

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:00 |
| **Last Seen** | 2026-06-23 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:00:50` | `cowrie.session.connect` |
| `2026-06-23 17:00:50` | `cowrie.client.version` |
| `2026-06-23 17:00:51` | `cowrie.client.kex` |
| `2026-06-23 17:00:51` | `cowrie.login.success` |
| `2026-06-23 17:00:52` | `cowrie.session.params` |
| `2026-06-23 17:00:52` | `cowrie.command.input` |
| `2026-06-23 17:00:52` | `cowrie.log.closed` |
| `2026-06-23 17:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b98fa21e7589

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:01 |
| **Last Seen** | 2026-06-23 17:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:01:05` | `cowrie.session.connect` |
| `2026-06-23 17:01:05` | `cowrie.client.version` |
| `2026-06-23 17:01:05` | `cowrie.client.kex` |
| `2026-06-23 17:01:07` | `cowrie.login.success` |
| `2026-06-23 17:01:08` | `cowrie.session.params` |
| `2026-06-23 17:01:08` | `cowrie.command.input` |
| `2026-06-23 17:01:08` | `cowrie.command.input` |
| `2026-06-23 17:01:08` | `cowrie.command.input` |
| `2026-06-23 17:01:08` | `cowrie.command.input` |
| `2026-06-23 17:01:09` | `cowrie.log.closed` |
| `2026-06-23 17:01:10` | `cowrie.session.params` |
| `2026-06-23 17:01:10` | `cowrie.command.input` |
| `2026-06-23 17:01:10` | `cowrie.command.input` |
| `2026-06-23 17:01:10` | `cowrie.command.failed` |
| `2026-06-23 17:01:10` | `cowrie.command.failed` |
| `2026-06-23 17:01:10` | `cowrie.command.failed` |
| `2026-06-23 17:01:10` | `cowrie.command.failed` |
| `2026-06-23 17:01:10` | `cowrie.log.closed` |
| `2026-06-23 17:01:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-619ded59cee6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:01 |
| **Last Seen** | 2026-06-23 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:01:42` | `cowrie.session.connect` |
| `2026-06-23 17:01:42` | `cowrie.client.version` |
| `2026-06-23 17:01:42` | `cowrie.client.kex` |
| `2026-06-23 17:01:43` | `cowrie.login.success` |
| `2026-06-23 17:01:44` | `cowrie.session.params` |
| `2026-06-23 17:01:44` | `cowrie.command.input` |
| `2026-06-23 17:01:44` | `cowrie.log.closed` |
| `2026-06-23 17:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38c02dad7020

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:02 |
| **Last Seen** | 2026-06-23 17:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password1' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:02:03` | `cowrie.session.connect` |
| `2026-06-23 17:02:03` | `cowrie.client.version` |
| `2026-06-23 17:02:03` | `cowrie.client.kex` |
| `2026-06-23 17:02:05` | `cowrie.login.success` |
| `2026-06-23 17:02:06` | `cowrie.session.params` |
| `2026-06-23 17:02:06` | `cowrie.command.input` |
| `2026-06-23 17:02:06` | `cowrie.command.input` |
| `2026-06-23 17:02:06` | `cowrie.command.input` |
| `2026-06-23 17:02:06` | `cowrie.command.input` |
| `2026-06-23 17:02:06` | `cowrie.log.closed` |
| `2026-06-23 17:02:08` | `cowrie.session.params` |
| `2026-06-23 17:02:08` | `cowrie.command.input` |
| `2026-06-23 17:02:08` | `cowrie.command.input` |
| `2026-06-23 17:02:08` | `cowrie.command.failed` |
| `2026-06-23 17:02:08` | `cowrie.command.failed` |
| `2026-06-23 17:02:08` | `cowrie.command.failed` |
| `2026-06-23 17:02:08` | `cowrie.command.failed` |
| `2026-06-23 17:02:08` | `cowrie.log.closed` |
| `2026-06-23 17:02:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63ffbb878c71

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:02 |
| **Last Seen** | 2026-06-23 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:02:37` | `cowrie.session.connect` |
| `2026-06-23 17:02:37` | `cowrie.client.version` |
| `2026-06-23 17:02:37` | `cowrie.client.kex` |
| `2026-06-23 17:02:37` | `cowrie.login.success` |
| `2026-06-23 17:02:38` | `cowrie.session.params` |
| `2026-06-23 17:02:38` | `cowrie.command.input` |
| `2026-06-23 17:02:38` | `cowrie.log.closed` |
| `2026-06-23 17:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f5f1dc9080f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:03 |
| **Last Seen** | 2026-06-23 17:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'qwerty123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:03:01` | `cowrie.session.connect` |
| `2026-06-23 17:03:01` | `cowrie.client.version` |
| `2026-06-23 17:03:01` | `cowrie.client.kex` |
| `2026-06-23 17:03:02` | `cowrie.login.success` |
| `2026-06-23 17:03:04` | `cowrie.session.params` |
| `2026-06-23 17:03:04` | `cowrie.command.input` |
| `2026-06-23 17:03:04` | `cowrie.command.input` |
| `2026-06-23 17:03:04` | `cowrie.command.input` |
| `2026-06-23 17:03:04` | `cowrie.command.input` |
| `2026-06-23 17:03:04` | `cowrie.log.closed` |
| `2026-06-23 17:03:05` | `cowrie.session.params` |
| `2026-06-23 17:03:05` | `cowrie.command.input` |
| `2026-06-23 17:03:05` | `cowrie.command.input` |
| `2026-06-23 17:03:05` | `cowrie.command.failed` |
| `2026-06-23 17:03:05` | `cowrie.command.failed` |
| `2026-06-23 17:03:05` | `cowrie.command.failed` |
| `2026-06-23 17:03:05` | `cowrie.command.failed` |
| `2026-06-23 17:03:05` | `cowrie.log.closed` |
| `2026-06-23 17:03:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9530434dd9b1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:03 |
| **Last Seen** | 2026-06-23 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:03:30` | `cowrie.session.connect` |
| `2026-06-23 17:03:30` | `cowrie.client.version` |
| `2026-06-23 17:03:30` | `cowrie.client.kex` |
| `2026-06-23 17:03:30` | `cowrie.login.success` |
| `2026-06-23 17:03:31` | `cowrie.session.params` |
| `2026-06-23 17:03:31` | `cowrie.command.input` |
| `2026-06-23 17:03:31` | `cowrie.log.closed` |
| `2026-06-23 17:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edb3e47bc238

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:03 |
| **Last Seen** | 2026-06-23 17:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'root123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:03:58` | `cowrie.session.connect` |
| `2026-06-23 17:03:59` | `cowrie.client.version` |
| `2026-06-23 17:03:59` | `cowrie.client.kex` |
| `2026-06-23 17:04:00` | `cowrie.login.success` |
| `2026-06-23 17:04:01` | `cowrie.session.params` |
| `2026-06-23 17:04:01` | `cowrie.command.input` |
| `2026-06-23 17:04:01` | `cowrie.command.input` |
| `2026-06-23 17:04:01` | `cowrie.command.input` |
| `2026-06-23 17:04:01` | `cowrie.command.input` |
| `2026-06-23 17:04:02` | `cowrie.log.closed` |
| `2026-06-23 17:04:03` | `cowrie.session.params` |
| `2026-06-23 17:04:03` | `cowrie.command.input` |
| `2026-06-23 17:04:03` | `cowrie.command.input` |
| `2026-06-23 17:04:03` | `cowrie.command.failed` |
| `2026-06-23 17:04:03` | `cowrie.command.failed` |
| `2026-06-23 17:04:03` | `cowrie.command.failed` |
| `2026-06-23 17:04:03` | `cowrie.command.failed` |
| `2026-06-23 17:04:03` | `cowrie.log.closed` |
| `2026-06-23 17:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ea0d6d88dd5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:04 |
| **Last Seen** | 2026-06-23 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:04:20` | `cowrie.session.connect` |
| `2026-06-23 17:04:20` | `cowrie.client.version` |
| `2026-06-23 17:04:20` | `cowrie.client.kex` |
| `2026-06-23 17:04:20` | `cowrie.login.success` |
| `2026-06-23 17:04:21` | `cowrie.session.params` |
| `2026-06-23 17:04:21` | `cowrie.command.input` |
| `2026-06-23 17:04:21` | `cowrie.log.closed` |
| `2026-06-23 17:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32b65da5786b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:04 |
| **Last Seen** | 2026-06-23 17:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:04:58` | `cowrie.session.connect` |
| `2026-06-23 17:04:58` | `cowrie.client.version` |
| `2026-06-23 17:04:58` | `cowrie.client.kex` |
| `2026-06-23 17:04:59` | `cowrie.login.success` |
| `2026-06-23 17:05:00` | `cowrie.session.params` |
| `2026-06-23 17:05:00` | `cowrie.command.input` |
| `2026-06-23 17:05:00` | `cowrie.command.input` |
| `2026-06-23 17:05:00` | `cowrie.command.input` |
| `2026-06-23 17:05:00` | `cowrie.command.input` |
| `2026-06-23 17:05:01` | `cowrie.log.closed` |
| `2026-06-23 17:05:02` | `cowrie.session.params` |
| `2026-06-23 17:05:02` | `cowrie.command.input` |
| `2026-06-23 17:05:02` | `cowrie.command.input` |
| `2026-06-23 17:05:02` | `cowrie.command.failed` |
| `2026-06-23 17:05:02` | `cowrie.command.failed` |
| `2026-06-23 17:05:02` | `cowrie.command.failed` |
| `2026-06-23 17:05:02` | `cowrie.command.failed` |
| `2026-06-23 17:05:03` | `cowrie.log.closed` |
| `2026-06-23 17:05:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a83594838c8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:05 |
| **Last Seen** | 2026-06-23 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:05:09` | `cowrie.session.connect` |
| `2026-06-23 17:05:09` | `cowrie.client.version` |
| `2026-06-23 17:05:09` | `cowrie.client.kex` |
| `2026-06-23 17:05:09` | `cowrie.login.success` |
| `2026-06-23 17:05:10` | `cowrie.session.params` |
| `2026-06-23 17:05:10` | `cowrie.command.input` |
| `2026-06-23 17:05:10` | `cowrie.log.closed` |
| `2026-06-23 17:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb6bd79d02b4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:05 |
| **Last Seen** | 2026-06-23 17:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:05:56` | `cowrie.session.connect` |
| `2026-06-23 17:05:56` | `cowrie.client.version` |
| `2026-06-23 17:05:56` | `cowrie.client.kex` |
| `2026-06-23 17:05:57` | `cowrie.login.success` |
| `2026-06-23 17:05:59` | `cowrie.session.params` |
| `2026-06-23 17:05:59` | `cowrie.command.input` |
| `2026-06-23 17:05:59` | `cowrie.command.input` |
| `2026-06-23 17:05:59` | `cowrie.command.input` |
| `2026-06-23 17:05:59` | `cowrie.command.input` |
| `2026-06-23 17:05:59` | `cowrie.log.closed` |
| `2026-06-23 17:06:00` | `cowrie.session.params` |
| `2026-06-23 17:06:00` | `cowrie.command.input` |
| `2026-06-23 17:06:00` | `cowrie.command.input` |
| `2026-06-23 17:06:00` | `cowrie.command.failed` |
| `2026-06-23 17:06:00` | `cowrie.command.failed` |
| `2026-06-23 17:06:00` | `cowrie.command.failed` |
| `2026-06-23 17:06:00` | `cowrie.command.failed` |
| `2026-06-23 17:06:00` | `cowrie.log.closed` |
| `2026-06-23 17:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-164ec54af1a0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:05 |
| **Last Seen** | 2026-06-23 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:05:59` | `cowrie.session.connect` |
| `2026-06-23 17:05:59` | `cowrie.client.version` |
| `2026-06-23 17:05:59` | `cowrie.client.kex` |
| `2026-06-23 17:06:00` | `cowrie.login.success` |
| `2026-06-23 17:06:01` | `cowrie.session.params` |
| `2026-06-23 17:06:01` | `cowrie.command.input` |
| `2026-06-23 17:06:01` | `cowrie.log.closed` |
| `2026-06-23 17:06:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c50ca960cacf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:06 |
| **Last Seen** | 2026-06-23 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:06:50` | `cowrie.session.connect` |
| `2026-06-23 17:06:50` | `cowrie.client.version` |
| `2026-06-23 17:06:50` | `cowrie.client.kex` |
| `2026-06-23 17:06:50` | `cowrie.login.success` |
| `2026-06-23 17:06:51` | `cowrie.session.params` |
| `2026-06-23 17:06:51` | `cowrie.command.input` |
| `2026-06-23 17:06:51` | `cowrie.log.closed` |
| `2026-06-23 17:06:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-065152042307

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:06 |
| **Last Seen** | 2026-06-23 17:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'admin123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:06:53` | `cowrie.session.connect` |
| `2026-06-23 17:06:53` | `cowrie.client.version` |
| `2026-06-23 17:06:53` | `cowrie.client.kex` |
| `2026-06-23 17:06:54` | `cowrie.login.success` |
| `2026-06-23 17:06:56` | `cowrie.session.params` |
| `2026-06-23 17:06:56` | `cowrie.command.input` |
| `2026-06-23 17:06:56` | `cowrie.command.input` |
| `2026-06-23 17:06:56` | `cowrie.command.input` |
| `2026-06-23 17:06:56` | `cowrie.command.input` |
| `2026-06-23 17:06:56` | `cowrie.log.closed` |
| `2026-06-23 17:06:57` | `cowrie.session.params` |
| `2026-06-23 17:06:57` | `cowrie.command.input` |
| `2026-06-23 17:06:57` | `cowrie.command.input` |
| `2026-06-23 17:06:57` | `cowrie.command.failed` |
| `2026-06-23 17:06:57` | `cowrie.command.failed` |
| `2026-06-23 17:06:57` | `cowrie.command.failed` |
| `2026-06-23 17:06:57` | `cowrie.command.failed` |
| `2026-06-23 17:06:57` | `cowrie.log.closed` |
| `2026-06-23 17:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-352589f0fbc3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:07 |
| **Last Seen** | 2026-06-23 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:07:47` | `cowrie.session.connect` |
| `2026-06-23 17:07:47` | `cowrie.client.version` |
| `2026-06-23 17:07:47` | `cowrie.client.kex` |
| `2026-06-23 17:07:47` | `cowrie.login.success` |
| `2026-06-23 17:07:48` | `cowrie.session.params` |
| `2026-06-23 17:07:48` | `cowrie.command.input` |
| `2026-06-23 17:07:48` | `cowrie.log.closed` |
| `2026-06-23 17:07:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5791e2023674

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:07 |
| **Last Seen** | 2026-06-23 17:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password1' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:07:49` | `cowrie.session.connect` |
| `2026-06-23 17:07:50` | `cowrie.client.version` |
| `2026-06-23 17:07:50` | `cowrie.client.kex` |
| `2026-06-23 17:07:51` | `cowrie.login.success` |
| `2026-06-23 17:07:52` | `cowrie.session.params` |
| `2026-06-23 17:07:52` | `cowrie.command.input` |
| `2026-06-23 17:07:52` | `cowrie.command.input` |
| `2026-06-23 17:07:52` | `cowrie.command.input` |
| `2026-06-23 17:07:52` | `cowrie.command.input` |
| `2026-06-23 17:07:52` | `cowrie.log.closed` |
| `2026-06-23 17:07:54` | `cowrie.session.params` |
| `2026-06-23 17:07:54` | `cowrie.command.input` |
| `2026-06-23 17:07:54` | `cowrie.command.input` |
| `2026-06-23 17:07:54` | `cowrie.command.failed` |
| `2026-06-23 17:07:54` | `cowrie.command.failed` |
| `2026-06-23 17:07:54` | `cowrie.command.failed` |
| `2026-06-23 17:07:54` | `cowrie.command.failed` |
| `2026-06-23 17:07:54` | `cowrie.log.closed` |
| `2026-06-23 17:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6f210a5243b

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 17:07 |
| **Last Seen** | 2026-06-23 17:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:07:57` | `cowrie.session.connect` |
| `2026-06-23 17:07:58` | `cowrie.client.version` |
| `2026-06-23 17:07:58` | `cowrie.client.kex` |
| `2026-06-23 17:08:04` | `cowrie.login.success` |
| `2026-06-23 17:08:08` | `cowrie.session.params` |
| `2026-06-23 17:08:08` | `cowrie.command.input` |
| `2026-06-23 17:08:09` | `cowrie.log.closed` |
| `2026-06-23 17:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d8580d0f023

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:08 |
| **Last Seen** | 2026-06-23 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:08:40` | `cowrie.session.connect` |
| `2026-06-23 17:08:40` | `cowrie.client.version` |
| `2026-06-23 17:08:40` | `cowrie.client.kex` |
| `2026-06-23 17:08:41` | `cowrie.login.success` |
| `2026-06-23 17:08:41` | `cowrie.session.params` |
| `2026-06-23 17:08:41` | `cowrie.command.input` |
| `2026-06-23 17:08:41` | `cowrie.log.closed` |
| `2026-06-23 17:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-609dd9f123c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:08 |
| **Last Seen** | 2026-06-23 17:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'qwerty123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:08:46` | `cowrie.session.connect` |
| `2026-06-23 17:08:47` | `cowrie.client.version` |
| `2026-06-23 17:08:47` | `cowrie.client.kex` |
| `2026-06-23 17:08:48` | `cowrie.login.success` |
| `2026-06-23 17:08:49` | `cowrie.session.params` |
| `2026-06-23 17:08:49` | `cowrie.command.input` |
| `2026-06-23 17:08:49` | `cowrie.command.input` |
| `2026-06-23 17:08:49` | `cowrie.command.input` |
| `2026-06-23 17:08:49` | `cowrie.command.input` |
| `2026-06-23 17:08:50` | `cowrie.log.closed` |
| `2026-06-23 17:08:51` | `cowrie.session.params` |
| `2026-06-23 17:08:51` | `cowrie.command.input` |
| `2026-06-23 17:08:51` | `cowrie.command.input` |
| `2026-06-23 17:08:51` | `cowrie.command.failed` |
| `2026-06-23 17:08:51` | `cowrie.command.failed` |
| `2026-06-23 17:08:51` | `cowrie.command.failed` |
| `2026-06-23 17:08:51` | `cowrie.command.failed` |
| `2026-06-23 17:08:51` | `cowrie.log.closed` |
| `2026-06-23 17:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfb4b0f73fb5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:09 |
| **Last Seen** | 2026-06-23 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:09:31` | `cowrie.session.connect` |
| `2026-06-23 17:09:31` | `cowrie.client.version` |
| `2026-06-23 17:09:32` | `cowrie.client.kex` |
| `2026-06-23 17:09:32` | `cowrie.login.success` |
| `2026-06-23 17:09:33` | `cowrie.session.params` |
| `2026-06-23 17:09:33` | `cowrie.command.input` |
| `2026-06-23 17:09:33` | `cowrie.log.closed` |
| `2026-06-23 17:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b3e6ffe1b04

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:09 |
| **Last Seen** | 2026-06-23 17:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:09:43` | `cowrie.session.connect` |
| `2026-06-23 17:09:44` | `cowrie.client.version` |
| `2026-06-23 17:09:44` | `cowrie.client.kex` |
| `2026-06-23 17:09:45` | `cowrie.login.success` |
| `2026-06-23 17:09:46` | `cowrie.session.params` |
| `2026-06-23 17:09:46` | `cowrie.command.input` |
| `2026-06-23 17:09:46` | `cowrie.command.input` |
| `2026-06-23 17:09:46` | `cowrie.command.input` |
| `2026-06-23 17:09:46` | `cowrie.command.input` |
| `2026-06-23 17:09:47` | `cowrie.log.closed` |
| `2026-06-23 17:09:48` | `cowrie.session.params` |
| `2026-06-23 17:09:48` | `cowrie.command.input` |
| `2026-06-23 17:09:48` | `cowrie.command.input` |
| `2026-06-23 17:09:48` | `cowrie.command.failed` |
| `2026-06-23 17:09:48` | `cowrie.command.failed` |
| `2026-06-23 17:09:48` | `cowrie.command.failed` |
| `2026-06-23 17:09:48` | `cowrie.command.failed` |
| `2026-06-23 17:09:48` | `cowrie.log.closed` |
| `2026-06-23 17:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94a78fb4b935

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:10 |
| **Last Seen** | 2026-06-23 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:10:23` | `cowrie.session.connect` |
| `2026-06-23 17:10:23` | `cowrie.client.version` |
| `2026-06-23 17:10:23` | `cowrie.client.kex` |
| `2026-06-23 17:10:24` | `cowrie.login.success` |
| `2026-06-23 17:10:25` | `cowrie.session.params` |
| `2026-06-23 17:10:25` | `cowrie.command.input` |
| `2026-06-23 17:10:25` | `cowrie.log.closed` |
| `2026-06-23 17:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c40c11652bd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:10 |
| **Last Seen** | 2026-06-23 17:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:10:41` | `cowrie.session.connect` |
| `2026-06-23 17:10:41` | `cowrie.client.version` |
| `2026-06-23 17:10:41` | `cowrie.client.kex` |
| `2026-06-23 17:10:43` | `cowrie.login.success` |
| `2026-06-23 17:10:44` | `cowrie.session.params` |
| `2026-06-23 17:10:44` | `cowrie.command.input` |
| `2026-06-23 17:10:44` | `cowrie.command.input` |
| `2026-06-23 17:10:44` | `cowrie.command.input` |
| `2026-06-23 17:10:44` | `cowrie.command.input` |
| `2026-06-23 17:10:45` | `cowrie.log.closed` |
| `2026-06-23 17:10:46` | `cowrie.session.params` |
| `2026-06-23 17:10:46` | `cowrie.command.input` |
| `2026-06-23 17:10:46` | `cowrie.command.input` |
| `2026-06-23 17:10:46` | `cowrie.command.failed` |
| `2026-06-23 17:10:46` | `cowrie.command.failed` |
| `2026-06-23 17:10:46` | `cowrie.command.failed` |
| `2026-06-23 17:10:46` | `cowrie.command.failed` |
| `2026-06-23 17:10:46` | `cowrie.log.closed` |
| `2026-06-23 17:10:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5583466922e0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:11 |
| **Last Seen** | 2026-06-23 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:11:14` | `cowrie.session.connect` |
| `2026-06-23 17:11:14` | `cowrie.client.version` |
| `2026-06-23 17:11:14` | `cowrie.client.kex` |
| `2026-06-23 17:11:14` | `cowrie.login.success` |
| `2026-06-23 17:11:15` | `cowrie.session.params` |
| `2026-06-23 17:11:15` | `cowrie.command.input` |
| `2026-06-23 17:11:15` | `cowrie.log.closed` |
| `2026-06-23 17:11:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69de066f73c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:11 |
| **Last Seen** | 2026-06-23 17:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123abc' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:11:36` | `cowrie.session.connect` |
| `2026-06-23 17:11:36` | `cowrie.client.version` |
| `2026-06-23 17:11:36` | `cowrie.client.kex` |
| `2026-06-23 17:11:38` | `cowrie.login.success` |
| `2026-06-23 17:11:39` | `cowrie.session.params` |
| `2026-06-23 17:11:39` | `cowrie.command.input` |
| `2026-06-23 17:11:39` | `cowrie.command.input` |
| `2026-06-23 17:11:39` | `cowrie.command.input` |
| `2026-06-23 17:11:39` | `cowrie.command.input` |
| `2026-06-23 17:11:39` | `cowrie.log.closed` |
| `2026-06-23 17:11:40` | `cowrie.session.params` |
| `2026-06-23 17:11:40` | `cowrie.command.input` |
| `2026-06-23 17:11:40` | `cowrie.command.input` |
| `2026-06-23 17:11:40` | `cowrie.command.failed` |
| `2026-06-23 17:11:40` | `cowrie.command.failed` |
| `2026-06-23 17:11:40` | `cowrie.command.failed` |
| `2026-06-23 17:11:40` | `cowrie.command.failed` |
| `2026-06-23 17:11:41` | `cowrie.log.closed` |
| `2026-06-23 17:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-005c6d684f64

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:12 |
| **Last Seen** | 2026-06-23 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:12:05` | `cowrie.session.connect` |
| `2026-06-23 17:12:05` | `cowrie.client.version` |
| `2026-06-23 17:12:05` | `cowrie.client.kex` |
| `2026-06-23 17:12:05` | `cowrie.login.success` |
| `2026-06-23 17:12:06` | `cowrie.session.params` |
| `2026-06-23 17:12:06` | `cowrie.command.input` |
| `2026-06-23 17:12:06` | `cowrie.log.closed` |
| `2026-06-23 17:12:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00b8981b6383

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:12 |
| **Last Seen** | 2026-06-23 17:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1q2w3e4r' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:12:32` | `cowrie.session.connect` |
| `2026-06-23 17:12:32` | `cowrie.client.version` |
| `2026-06-23 17:12:32` | `cowrie.client.kex` |
| `2026-06-23 17:12:34` | `cowrie.login.success` |
| `2026-06-23 17:12:35` | `cowrie.session.params` |
| `2026-06-23 17:12:35` | `cowrie.command.input` |
| `2026-06-23 17:12:35` | `cowrie.command.input` |
| `2026-06-23 17:12:35` | `cowrie.command.input` |
| `2026-06-23 17:12:35` | `cowrie.command.input` |
| `2026-06-23 17:12:35` | `cowrie.log.closed` |
| `2026-06-23 17:12:36` | `cowrie.session.params` |
| `2026-06-23 17:12:36` | `cowrie.command.input` |
| `2026-06-23 17:12:36` | `cowrie.command.input` |
| `2026-06-23 17:12:36` | `cowrie.command.failed` |
| `2026-06-23 17:12:36` | `cowrie.command.failed` |
| `2026-06-23 17:12:36` | `cowrie.command.failed` |
| `2026-06-23 17:12:36` | `cowrie.command.failed` |
| `2026-06-23 17:12:37` | `cowrie.log.closed` |
| `2026-06-23 17:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0c76ce2d7bb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:12 |
| **Last Seen** | 2026-06-23 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:12:55` | `cowrie.session.connect` |
| `2026-06-23 17:12:55` | `cowrie.client.version` |
| `2026-06-23 17:12:55` | `cowrie.client.kex` |
| `2026-06-23 17:12:55` | `cowrie.login.success` |
| `2026-06-23 17:12:56` | `cowrie.session.params` |
| `2026-06-23 17:12:56` | `cowrie.command.input` |
| `2026-06-23 17:12:56` | `cowrie.log.closed` |
| `2026-06-23 17:12:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f59c5f6f850b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:13 |
| **Last Seen** | 2026-06-23 17:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'admin123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:13:29` | `cowrie.session.connect` |
| `2026-06-23 17:13:29` | `cowrie.client.version` |
| `2026-06-23 17:13:29` | `cowrie.client.kex` |
| `2026-06-23 17:13:30` | `cowrie.login.success` |
| `2026-06-23 17:13:31` | `cowrie.session.params` |
| `2026-06-23 17:13:31` | `cowrie.command.input` |
| `2026-06-23 17:13:31` | `cowrie.command.input` |
| `2026-06-23 17:13:31` | `cowrie.command.input` |
| `2026-06-23 17:13:31` | `cowrie.command.input` |
| `2026-06-23 17:13:32` | `cowrie.log.closed` |
| `2026-06-23 17:13:33` | `cowrie.session.params` |
| `2026-06-23 17:13:33` | `cowrie.command.input` |
| `2026-06-23 17:13:33` | `cowrie.command.input` |
| `2026-06-23 17:13:33` | `cowrie.command.failed` |
| `2026-06-23 17:13:33` | `cowrie.command.failed` |
| `2026-06-23 17:13:33` | `cowrie.command.failed` |
| `2026-06-23 17:13:33` | `cowrie.command.failed` |
| `2026-06-23 17:13:34` | `cowrie.log.closed` |
| `2026-06-23 17:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9da290d0363

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:13 |
| **Last Seen** | 2026-06-23 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:13:47` | `cowrie.session.connect` |
| `2026-06-23 17:13:47` | `cowrie.client.version` |
| `2026-06-23 17:13:47` | `cowrie.client.kex` |
| `2026-06-23 17:13:47` | `cowrie.login.success` |
| `2026-06-23 17:13:48` | `cowrie.session.params` |
| `2026-06-23 17:13:48` | `cowrie.command.input` |
| `2026-06-23 17:13:48` | `cowrie.log.closed` |
| `2026-06-23 17:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab8970bde6a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:14 |
| **Last Seen** | 2026-06-23 17:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'qwerty123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:14:26` | `cowrie.session.connect` |
| `2026-06-23 17:14:26` | `cowrie.client.version` |
| `2026-06-23 17:14:26` | `cowrie.client.kex` |
| `2026-06-23 17:14:27` | `cowrie.login.success` |
| `2026-06-23 17:14:28` | `cowrie.session.params` |
| `2026-06-23 17:14:28` | `cowrie.command.input` |
| `2026-06-23 17:14:28` | `cowrie.command.input` |
| `2026-06-23 17:14:28` | `cowrie.command.input` |
| `2026-06-23 17:14:28` | `cowrie.command.input` |
| `2026-06-23 17:14:29` | `cowrie.log.closed` |
| `2026-06-23 17:14:30` | `cowrie.session.params` |
| `2026-06-23 17:14:30` | `cowrie.command.input` |
| `2026-06-23 17:14:30` | `cowrie.command.input` |
| `2026-06-23 17:14:30` | `cowrie.command.failed` |
| `2026-06-23 17:14:30` | `cowrie.command.failed` |
| `2026-06-23 17:14:30` | `cowrie.command.failed` |
| `2026-06-23 17:14:30` | `cowrie.command.failed` |
| `2026-06-23 17:14:30` | `cowrie.log.closed` |
| `2026-06-23 17:14:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8199beb00cc5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:14 |
| **Last Seen** | 2026-06-23 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:14:39` | `cowrie.session.connect` |
| `2026-06-23 17:14:39` | `cowrie.client.version` |
| `2026-06-23 17:14:39` | `cowrie.client.kex` |
| `2026-06-23 17:14:39` | `cowrie.login.success` |
| `2026-06-23 17:14:40` | `cowrie.session.params` |
| `2026-06-23 17:14:40` | `cowrie.command.input` |
| `2026-06-23 17:14:40` | `cowrie.log.closed` |
| `2026-06-23 17:14:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca96a687231c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:15 |
| **Last Seen** | 2026-06-23 17:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:15:23` | `cowrie.session.connect` |
| `2026-06-23 17:15:23` | `cowrie.client.version` |
| `2026-06-23 17:15:23` | `cowrie.client.kex` |
| `2026-06-23 17:15:24` | `cowrie.login.success` |
| `2026-06-23 17:15:25` | `cowrie.session.params` |
| `2026-06-23 17:15:25` | `cowrie.command.input` |
| `2026-06-23 17:15:25` | `cowrie.command.input` |
| `2026-06-23 17:15:25` | `cowrie.command.input` |
| `2026-06-23 17:15:25` | `cowrie.command.input` |
| `2026-06-23 17:15:26` | `cowrie.log.closed` |
| `2026-06-23 17:15:27` | `cowrie.session.params` |
| `2026-06-23 17:15:27` | `cowrie.command.input` |
| `2026-06-23 17:15:27` | `cowrie.command.input` |
| `2026-06-23 17:15:27` | `cowrie.command.failed` |
| `2026-06-23 17:15:27` | `cowrie.command.failed` |
| `2026-06-23 17:15:27` | `cowrie.command.failed` |
| `2026-06-23 17:15:27` | `cowrie.command.failed` |
| `2026-06-23 17:15:27` | `cowrie.log.closed` |
| `2026-06-23 17:15:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72e9fde58e68

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:15 |
| **Last Seen** | 2026-06-23 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:15:32` | `cowrie.session.connect` |
| `2026-06-23 17:15:32` | `cowrie.client.version` |
| `2026-06-23 17:15:32` | `cowrie.client.kex` |
| `2026-06-23 17:15:32` | `cowrie.login.success` |
| `2026-06-23 17:15:33` | `cowrie.session.params` |
| `2026-06-23 17:15:33` | `cowrie.command.input` |
| `2026-06-23 17:15:33` | `cowrie.log.closed` |
| `2026-06-23 17:15:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9942a9016362

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:16 |
| **Last Seen** | 2026-06-23 17:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:16:20` | `cowrie.session.connect` |
| `2026-06-23 17:16:20` | `cowrie.client.version` |
| `2026-06-23 17:16:20` | `cowrie.client.kex` |
| `2026-06-23 17:16:21` | `cowrie.login.success` |
| `2026-06-23 17:16:23` | `cowrie.session.params` |
| `2026-06-23 17:16:23` | `cowrie.command.input` |
| `2026-06-23 17:16:23` | `cowrie.command.input` |
| `2026-06-23 17:16:23` | `cowrie.command.input` |
| `2026-06-23 17:16:23` | `cowrie.command.input` |
| `2026-06-23 17:16:23` | `cowrie.log.closed` |
| `2026-06-23 17:16:24` | `cowrie.session.params` |
| `2026-06-23 17:16:24` | `cowrie.command.input` |
| `2026-06-23 17:16:24` | `cowrie.command.input` |
| `2026-06-23 17:16:24` | `cowrie.command.failed` |
| `2026-06-23 17:16:24` | `cowrie.command.failed` |
| `2026-06-23 17:16:24` | `cowrie.command.failed` |
| `2026-06-23 17:16:24` | `cowrie.command.failed` |
| `2026-06-23 17:16:25` | `cowrie.log.closed` |
| `2026-06-23 17:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acb49a55c045

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:16 |
| **Last Seen** | 2026-06-23 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:16:25` | `cowrie.session.connect` |
| `2026-06-23 17:16:25` | `cowrie.client.version` |
| `2026-06-23 17:16:25` | `cowrie.client.kex` |
| `2026-06-23 17:16:25` | `cowrie.login.success` |
| `2026-06-23 17:16:26` | `cowrie.session.params` |
| `2026-06-23 17:16:26` | `cowrie.command.input` |
| `2026-06-23 17:16:26` | `cowrie.log.closed` |
| `2026-06-23 17:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41b55c39da98

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:17 |
| **Last Seen** | 2026-06-23 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:17:16` | `cowrie.session.connect` |
| `2026-06-23 17:17:16` | `cowrie.client.version` |
| `2026-06-23 17:17:16` | `cowrie.client.kex` |
| `2026-06-23 17:17:17` | `cowrie.login.success` |
| `2026-06-23 17:17:18` | `cowrie.session.params` |
| `2026-06-23 17:17:18` | `cowrie.command.input` |
| `2026-06-23 17:17:18` | `cowrie.log.closed` |
| `2026-06-23 17:17:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45ec60beb12a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:17 |
| **Last Seen** | 2026-06-23 17:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345678' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:17:18` | `cowrie.session.connect` |
| `2026-06-23 17:17:18` | `cowrie.client.version` |
| `2026-06-23 17:17:18` | `cowrie.client.kex` |
| `2026-06-23 17:17:20` | `cowrie.login.success` |
| `2026-06-23 17:17:21` | `cowrie.session.params` |
| `2026-06-23 17:17:21` | `cowrie.command.input` |
| `2026-06-23 17:17:21` | `cowrie.command.input` |
| `2026-06-23 17:17:21` | `cowrie.command.input` |
| `2026-06-23 17:17:21` | `cowrie.command.input` |
| `2026-06-23 17:17:21` | `cowrie.log.closed` |
| `2026-06-23 17:17:22` | `cowrie.session.params` |
| `2026-06-23 17:17:22` | `cowrie.command.input` |
| `2026-06-23 17:17:22` | `cowrie.command.input` |
| `2026-06-23 17:17:22` | `cowrie.command.failed` |
| `2026-06-23 17:17:22` | `cowrie.command.failed` |
| `2026-06-23 17:17:22` | `cowrie.command.failed` |
| `2026-06-23 17:17:22` | `cowrie.command.failed` |
| `2026-06-23 17:17:22` | `cowrie.log.closed` |
| `2026-06-23 17:17:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bd2f93fd548

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:18 |
| **Last Seen** | 2026-06-23 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:18:07` | `cowrie.session.connect` |
| `2026-06-23 17:18:07` | `cowrie.client.version` |
| `2026-06-23 17:18:08` | `cowrie.client.kex` |
| `2026-06-23 17:18:08` | `cowrie.login.success` |
| `2026-06-23 17:18:09` | `cowrie.session.params` |
| `2026-06-23 17:18:09` | `cowrie.command.input` |
| `2026-06-23 17:18:09` | `cowrie.log.closed` |
| `2026-06-23 17:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dfa93aadb40

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:18 |
| **Last Seen** | 2026-06-23 17:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:18:14` | `cowrie.session.connect` |
| `2026-06-23 17:18:15` | `cowrie.client.version` |
| `2026-06-23 17:18:15` | `cowrie.client.kex` |
| `2026-06-23 17:18:16` | `cowrie.login.success` |
| `2026-06-23 17:18:17` | `cowrie.session.params` |
| `2026-06-23 17:18:17` | `cowrie.command.input` |
| `2026-06-23 17:18:17` | `cowrie.command.input` |
| `2026-06-23 17:18:17` | `cowrie.command.input` |
| `2026-06-23 17:18:17` | `cowrie.command.input` |
| `2026-06-23 17:18:18` | `cowrie.log.closed` |
| `2026-06-23 17:18:19` | `cowrie.session.params` |
| `2026-06-23 17:18:19` | `cowrie.command.input` |
| `2026-06-23 17:18:19` | `cowrie.command.input` |
| `2026-06-23 17:18:19` | `cowrie.command.failed` |
| `2026-06-23 17:18:19` | `cowrie.command.failed` |
| `2026-06-23 17:18:19` | `cowrie.command.failed` |
| `2026-06-23 17:18:19` | `cowrie.command.failed` |
| `2026-06-23 17:18:19` | `cowrie.log.closed` |
| `2026-06-23 17:18:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-920a39ae34b0

| Field | Detail |
|---|---|
| **Source IP** | `34.38.222[.]164` |
| **First Seen** | 2026-06-23 17:18 |
| **Last Seen** | 2026-06-23 17:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:18:39` | `cowrie.session.connect` |
| `2026-06-23 17:18:39` | `cowrie.client.version` |
| `2026-06-23 17:18:39` | `cowrie.client.kex` |
| `2026-06-23 17:18:41` | `cowrie.login.success` |
| `2026-06-23 17:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.222[.]164` to AbuseIPDB if not already reported
- [ ] Block `34.38.222[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0dbd36c28ef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:18 |
| **Last Seen** | 2026-06-23 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:18:58` | `cowrie.session.connect` |
| `2026-06-23 17:18:58` | `cowrie.client.version` |
| `2026-06-23 17:18:58` | `cowrie.client.kex` |
| `2026-06-23 17:18:59` | `cowrie.login.success` |
| `2026-06-23 17:19:00` | `cowrie.session.params` |
| `2026-06-23 17:19:00` | `cowrie.command.input` |
| `2026-06-23 17:19:00` | `cowrie.log.closed` |
| `2026-06-23 17:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-987c0c4b8b14

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:19 |
| **Last Seen** | 2026-06-23 17:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123456' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:19:11` | `cowrie.session.connect` |
| `2026-06-23 17:19:11` | `cowrie.client.version` |
| `2026-06-23 17:19:11` | `cowrie.client.kex` |
| `2026-06-23 17:19:12` | `cowrie.login.success` |
| `2026-06-23 17:19:14` | `cowrie.session.params` |
| `2026-06-23 17:19:14` | `cowrie.command.input` |
| `2026-06-23 17:19:14` | `cowrie.command.input` |
| `2026-06-23 17:19:14` | `cowrie.command.input` |
| `2026-06-23 17:19:14` | `cowrie.command.input` |
| `2026-06-23 17:19:14` | `cowrie.log.closed` |
| `2026-06-23 17:19:15` | `cowrie.session.params` |
| `2026-06-23 17:19:15` | `cowrie.command.input` |
| `2026-06-23 17:19:15` | `cowrie.command.input` |
| `2026-06-23 17:19:15` | `cowrie.command.failed` |
| `2026-06-23 17:19:15` | `cowrie.command.failed` |
| `2026-06-23 17:19:15` | `cowrie.command.failed` |
| `2026-06-23 17:19:15` | `cowrie.command.failed` |
| `2026-06-23 17:19:16` | `cowrie.log.closed` |
| `2026-06-23 17:19:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-509e82755466

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:19 |
| **Last Seen** | 2026-06-23 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:19:49` | `cowrie.session.connect` |
| `2026-06-23 17:19:49` | `cowrie.client.version` |
| `2026-06-23 17:19:49` | `cowrie.client.kex` |
| `2026-06-23 17:19:49` | `cowrie.login.success` |
| `2026-06-23 17:19:50` | `cowrie.session.params` |
| `2026-06-23 17:19:50` | `cowrie.command.input` |
| `2026-06-23 17:19:50` | `cowrie.log.closed` |
| `2026-06-23 17:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89a04c4a1d00

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:20 |
| **Last Seen** | 2026-06-23 17:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'abc123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:20:09` | `cowrie.session.connect` |
| `2026-06-23 17:20:09` | `cowrie.client.version` |
| `2026-06-23 17:20:09` | `cowrie.client.kex` |
| `2026-06-23 17:20:10` | `cowrie.login.success` |
| `2026-06-23 17:20:12` | `cowrie.session.params` |
| `2026-06-23 17:20:12` | `cowrie.command.input` |
| `2026-06-23 17:20:12` | `cowrie.command.input` |
| `2026-06-23 17:20:12` | `cowrie.command.input` |
| `2026-06-23 17:20:12` | `cowrie.command.input` |
| `2026-06-23 17:20:12` | `cowrie.log.closed` |
| `2026-06-23 17:20:13` | `cowrie.session.params` |
| `2026-06-23 17:20:13` | `cowrie.command.input` |
| `2026-06-23 17:20:13` | `cowrie.command.input` |
| `2026-06-23 17:20:13` | `cowrie.command.failed` |
| `2026-06-23 17:20:13` | `cowrie.command.failed` |
| `2026-06-23 17:20:13` | `cowrie.command.failed` |
| `2026-06-23 17:20:13` | `cowrie.command.failed` |
| `2026-06-23 17:20:13` | `cowrie.log.closed` |
| `2026-06-23 17:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5bc5517f983

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:20 |
| **Last Seen** | 2026-06-23 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:20:41` | `cowrie.session.connect` |
| `2026-06-23 17:20:41` | `cowrie.client.version` |
| `2026-06-23 17:20:41` | `cowrie.client.kex` |
| `2026-06-23 17:20:41` | `cowrie.login.success` |
| `2026-06-23 17:20:42` | `cowrie.session.params` |
| `2026-06-23 17:20:42` | `cowrie.command.input` |
| `2026-06-23 17:20:42` | `cowrie.log.closed` |
| `2026-06-23 17:20:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc5bcdc89fc7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:21 |
| **Last Seen** | 2026-06-23 17:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:21:07` | `cowrie.session.connect` |
| `2026-06-23 17:21:07` | `cowrie.client.version` |
| `2026-06-23 17:21:07` | `cowrie.client.kex` |
| `2026-06-23 17:21:08` | `cowrie.login.success` |
| `2026-06-23 17:21:09` | `cowrie.session.params` |
| `2026-06-23 17:21:09` | `cowrie.command.input` |
| `2026-06-23 17:21:09` | `cowrie.command.input` |
| `2026-06-23 17:21:09` | `cowrie.command.input` |
| `2026-06-23 17:21:09` | `cowrie.command.input` |
| `2026-06-23 17:21:10` | `cowrie.log.closed` |
| `2026-06-23 17:21:11` | `cowrie.session.params` |
| `2026-06-23 17:21:11` | `cowrie.command.input` |
| `2026-06-23 17:21:11` | `cowrie.command.input` |
| `2026-06-23 17:21:11` | `cowrie.command.failed` |
| `2026-06-23 17:21:11` | `cowrie.command.failed` |
| `2026-06-23 17:21:11` | `cowrie.command.failed` |
| `2026-06-23 17:21:11` | `cowrie.command.failed` |
| `2026-06-23 17:21:11` | `cowrie.log.closed` |
| `2026-06-23 17:21:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0e8108ff7c7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:21 |
| **Last Seen** | 2026-06-23 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:21:34` | `cowrie.session.connect` |
| `2026-06-23 17:21:34` | `cowrie.client.version` |
| `2026-06-23 17:21:34` | `cowrie.client.kex` |
| `2026-06-23 17:21:35` | `cowrie.login.success` |
| `2026-06-23 17:21:35` | `cowrie.session.params` |
| `2026-06-23 17:21:35` | `cowrie.command.input` |
| `2026-06-23 17:21:35` | `cowrie.log.closed` |
| `2026-06-23 17:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b95c7f594de

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 17:21 |
| **Last Seen** | 2026-06-23 17:22 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:21:54` | `cowrie.session.connect` |
| `2026-06-23 17:21:56` | `cowrie.client.version` |
| `2026-06-23 17:21:56` | `cowrie.client.kex` |
| `2026-06-23 17:22:02` | `cowrie.login.success` |
| `2026-06-23 17:22:06` | `cowrie.session.params` |
| `2026-06-23 17:22:06` | `cowrie.command.input` |
| `2026-06-23 17:22:08` | `cowrie.log.closed` |
| `2026-06-23 17:22:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3450561f47e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:22 |
| **Last Seen** | 2026-06-23 17:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:22:05` | `cowrie.session.connect` |
| `2026-06-23 17:22:05` | `cowrie.client.version` |
| `2026-06-23 17:22:05` | `cowrie.client.kex` |
| `2026-06-23 17:22:06` | `cowrie.login.success` |
| `2026-06-23 17:22:08` | `cowrie.session.params` |
| `2026-06-23 17:22:08` | `cowrie.command.input` |
| `2026-06-23 17:22:08` | `cowrie.command.input` |
| `2026-06-23 17:22:08` | `cowrie.command.input` |
| `2026-06-23 17:22:08` | `cowrie.command.input` |
| `2026-06-23 17:22:08` | `cowrie.log.closed` |
| `2026-06-23 17:22:09` | `cowrie.session.params` |
| `2026-06-23 17:22:09` | `cowrie.command.input` |
| `2026-06-23 17:22:09` | `cowrie.command.input` |
| `2026-06-23 17:22:09` | `cowrie.command.failed` |
| `2026-06-23 17:22:09` | `cowrie.command.failed` |
| `2026-06-23 17:22:09` | `cowrie.command.failed` |
| `2026-06-23 17:22:09` | `cowrie.command.failed` |
| `2026-06-23 17:22:09` | `cowrie.log.closed` |
| `2026-06-23 17:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89d06a44ef9b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:22 |
| **Last Seen** | 2026-06-23 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:22:27` | `cowrie.session.connect` |
| `2026-06-23 17:22:27` | `cowrie.client.version` |
| `2026-06-23 17:22:27` | `cowrie.client.kex` |
| `2026-06-23 17:22:27` | `cowrie.login.success` |
| `2026-06-23 17:22:28` | `cowrie.session.params` |
| `2026-06-23 17:22:28` | `cowrie.command.input` |
| `2026-06-23 17:22:28` | `cowrie.log.closed` |
| `2026-06-23 17:22:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca5efeb909b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:23 |
| **Last Seen** | 2026-06-23 17:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:23:03` | `cowrie.session.connect` |
| `2026-06-23 17:23:03` | `cowrie.client.version` |
| `2026-06-23 17:23:03` | `cowrie.client.kex` |
| `2026-06-23 17:23:05` | `cowrie.login.success` |
| `2026-06-23 17:23:06` | `cowrie.session.params` |
| `2026-06-23 17:23:06` | `cowrie.command.input` |
| `2026-06-23 17:23:06` | `cowrie.command.input` |
| `2026-06-23 17:23:06` | `cowrie.command.input` |
| `2026-06-23 17:23:06` | `cowrie.command.input` |
| `2026-06-23 17:23:06` | `cowrie.log.closed` |
| `2026-06-23 17:23:07` | `cowrie.session.params` |
| `2026-06-23 17:23:07` | `cowrie.command.input` |
| `2026-06-23 17:23:07` | `cowrie.command.input` |
| `2026-06-23 17:23:07` | `cowrie.command.failed` |
| `2026-06-23 17:23:07` | `cowrie.command.failed` |
| `2026-06-23 17:23:07` | `cowrie.command.failed` |
| `2026-06-23 17:23:07` | `cowrie.command.failed` |
| `2026-06-23 17:23:07` | `cowrie.log.closed` |
| `2026-06-23 17:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ba665fd3bbc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:23 |
| **Last Seen** | 2026-06-23 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:23:19` | `cowrie.session.connect` |
| `2026-06-23 17:23:19` | `cowrie.client.version` |
| `2026-06-23 17:23:19` | `cowrie.client.kex` |
| `2026-06-23 17:23:19` | `cowrie.login.success` |
| `2026-06-23 17:23:20` | `cowrie.session.params` |
| `2026-06-23 17:23:20` | `cowrie.command.input` |
| `2026-06-23 17:23:20` | `cowrie.log.closed` |
| `2026-06-23 17:23:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c57c02be0541

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:23 |
| **Last Seen** | 2026-06-23 17:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123456' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:23:58` | `cowrie.session.connect` |
| `2026-06-23 17:23:59` | `cowrie.client.version` |
| `2026-06-23 17:23:59` | `cowrie.client.kex` |
| `2026-06-23 17:24:00` | `cowrie.login.success` |
| `2026-06-23 17:24:01` | `cowrie.session.params` |
| `2026-06-23 17:24:01` | `cowrie.command.input` |
| `2026-06-23 17:24:01` | `cowrie.command.input` |
| `2026-06-23 17:24:01` | `cowrie.command.input` |
| `2026-06-23 17:24:01` | `cowrie.command.input` |
| `2026-06-23 17:24:01` | `cowrie.log.closed` |
| `2026-06-23 17:24:03` | `cowrie.session.params` |
| `2026-06-23 17:24:03` | `cowrie.command.input` |
| `2026-06-23 17:24:03` | `cowrie.command.input` |
| `2026-06-23 17:24:03` | `cowrie.command.failed` |
| `2026-06-23 17:24:03` | `cowrie.command.failed` |
| `2026-06-23 17:24:03` | `cowrie.command.failed` |
| `2026-06-23 17:24:03` | `cowrie.command.failed` |
| `2026-06-23 17:24:03` | `cowrie.log.closed` |
| `2026-06-23 17:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d6afd8f6fd0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:24 |
| **Last Seen** | 2026-06-23 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:24:10` | `cowrie.session.connect` |
| `2026-06-23 17:24:10` | `cowrie.client.version` |
| `2026-06-23 17:24:10` | `cowrie.client.kex` |
| `2026-06-23 17:24:10` | `cowrie.login.success` |
| `2026-06-23 17:24:11` | `cowrie.session.params` |
| `2026-06-23 17:24:11` | `cowrie.command.input` |
| `2026-06-23 17:24:11` | `cowrie.log.closed` |
| `2026-06-23 17:24:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aa22c23cc06

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:24 |
| **Last Seen** | 2026-06-23 17:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345678' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:24:55` | `cowrie.session.connect` |
| `2026-06-23 17:24:55` | `cowrie.client.version` |
| `2026-06-23 17:24:56` | `cowrie.client.kex` |
| `2026-06-23 17:24:57` | `cowrie.login.success` |
| `2026-06-23 17:24:58` | `cowrie.session.params` |
| `2026-06-23 17:24:58` | `cowrie.command.input` |
| `2026-06-23 17:24:58` | `cowrie.command.input` |
| `2026-06-23 17:24:58` | `cowrie.command.input` |
| `2026-06-23 17:24:58` | `cowrie.command.input` |
| `2026-06-23 17:24:59` | `cowrie.log.closed` |
| `2026-06-23 17:25:00` | `cowrie.session.params` |
| `2026-06-23 17:25:00` | `cowrie.command.input` |
| `2026-06-23 17:25:00` | `cowrie.command.input` |
| `2026-06-23 17:25:00` | `cowrie.command.failed` |
| `2026-06-23 17:25:00` | `cowrie.command.failed` |
| `2026-06-23 17:25:00` | `cowrie.command.failed` |
| `2026-06-23 17:25:00` | `cowrie.command.failed` |
| `2026-06-23 17:25:00` | `cowrie.log.closed` |
| `2026-06-23 17:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc05cde24fa6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:25 |
| **Last Seen** | 2026-06-23 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:25:00` | `cowrie.session.connect` |
| `2026-06-23 17:25:00` | `cowrie.client.version` |
| `2026-06-23 17:25:00` | `cowrie.client.kex` |
| `2026-06-23 17:25:01` | `cowrie.login.success` |
| `2026-06-23 17:25:01` | `cowrie.session.params` |
| `2026-06-23 17:25:01` | `cowrie.command.input` |
| `2026-06-23 17:25:01` | `cowrie.log.closed` |
| `2026-06-23 17:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3522a2c5263

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:25 |
| **Last Seen** | 2026-06-23 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:25:51` | `cowrie.session.connect` |
| `2026-06-23 17:25:51` | `cowrie.client.version` |
| `2026-06-23 17:25:51` | `cowrie.client.kex` |
| `2026-06-23 17:25:51` | `cowrie.login.success` |
| `2026-06-23 17:25:52` | `cowrie.session.params` |
| `2026-06-23 17:25:52` | `cowrie.command.input` |
| `2026-06-23 17:25:52` | `cowrie.log.closed` |
| `2026-06-23 17:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8427e68bb517

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:25 |
| **Last Seen** | 2026-06-23 17:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123456789' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:25:51` | `cowrie.session.connect` |
| `2026-06-23 17:25:51` | `cowrie.client.version` |
| `2026-06-23 17:25:51` | `cowrie.client.kex` |
| `2026-06-23 17:25:53` | `cowrie.login.success` |
| `2026-06-23 17:25:54` | `cowrie.session.params` |
| `2026-06-23 17:25:54` | `cowrie.command.input` |
| `2026-06-23 17:25:54` | `cowrie.command.input` |
| `2026-06-23 17:25:54` | `cowrie.command.input` |
| `2026-06-23 17:25:54` | `cowrie.command.input` |
| `2026-06-23 17:25:55` | `cowrie.log.closed` |
| `2026-06-23 17:25:56` | `cowrie.session.params` |
| `2026-06-23 17:25:56` | `cowrie.command.input` |
| `2026-06-23 17:25:56` | `cowrie.command.input` |
| `2026-06-23 17:25:56` | `cowrie.command.failed` |
| `2026-06-23 17:25:56` | `cowrie.command.failed` |
| `2026-06-23 17:25:56` | `cowrie.command.failed` |
| `2026-06-23 17:25:56` | `cowrie.command.failed` |
| `2026-06-23 17:25:56` | `cowrie.log.closed` |
| `2026-06-23 17:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89e83e662fca

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:26 |
| **Last Seen** | 2026-06-23 17:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:26:44` | `cowrie.session.connect` |
| `2026-06-23 17:26:44` | `cowrie.client.version` |
| `2026-06-23 17:26:44` | `cowrie.client.kex` |
| `2026-06-23 17:26:44` | `cowrie.login.success` |
| `2026-06-23 17:26:45` | `cowrie.session.params` |
| `2026-06-23 17:26:45` | `cowrie.command.input` |
| `2026-06-23 17:26:45` | `cowrie.log.closed` |
| `2026-06-23 17:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cf704a630f1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:26 |
| **Last Seen** | 2026-06-23 17:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234567890' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:26:47` | `cowrie.session.connect` |
| `2026-06-23 17:26:48` | `cowrie.client.version` |
| `2026-06-23 17:26:48` | `cowrie.client.kex` |
| `2026-06-23 17:26:49` | `cowrie.login.success` |
| `2026-06-23 17:26:50` | `cowrie.session.params` |
| `2026-06-23 17:26:50` | `cowrie.command.input` |
| `2026-06-23 17:26:50` | `cowrie.command.input` |
| `2026-06-23 17:26:50` | `cowrie.command.input` |
| `2026-06-23 17:26:50` | `cowrie.command.input` |
| `2026-06-23 17:26:50` | `cowrie.log.closed` |
| `2026-06-23 17:26:52` | `cowrie.session.params` |
| `2026-06-23 17:26:52` | `cowrie.command.input` |
| `2026-06-23 17:26:52` | `cowrie.command.input` |
| `2026-06-23 17:26:52` | `cowrie.command.failed` |
| `2026-06-23 17:26:52` | `cowrie.command.failed` |
| `2026-06-23 17:26:52` | `cowrie.command.failed` |
| `2026-06-23 17:26:52` | `cowrie.command.failed` |
| `2026-06-23 17:26:52` | `cowrie.log.closed` |
| `2026-06-23 17:26:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f134fb09826

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:27 |
| **Last Seen** | 2026-06-23 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:27:38` | `cowrie.session.connect` |
| `2026-06-23 17:27:38` | `cowrie.client.version` |
| `2026-06-23 17:27:38` | `cowrie.client.kex` |
| `2026-06-23 17:27:38` | `cowrie.login.success` |
| `2026-06-23 17:27:39` | `cowrie.session.params` |
| `2026-06-23 17:27:39` | `cowrie.command.input` |
| `2026-06-23 17:27:39` | `cowrie.log.closed` |
| `2026-06-23 17:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28a6d8e31f1d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:27 |
| **Last Seen** | 2026-06-23 17:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1q2w3e4r' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:27:44` | `cowrie.session.connect` |
| `2026-06-23 17:27:44` | `cowrie.client.version` |
| `2026-06-23 17:27:44` | `cowrie.client.kex` |
| `2026-06-23 17:27:46` | `cowrie.login.success` |
| `2026-06-23 17:27:47` | `cowrie.session.params` |
| `2026-06-23 17:27:47` | `cowrie.command.input` |
| `2026-06-23 17:27:47` | `cowrie.command.input` |
| `2026-06-23 17:27:47` | `cowrie.command.input` |
| `2026-06-23 17:27:47` | `cowrie.command.input` |
| `2026-06-23 17:27:47` | `cowrie.log.closed` |
| `2026-06-23 17:27:48` | `cowrie.session.params` |
| `2026-06-23 17:27:48` | `cowrie.command.input` |
| `2026-06-23 17:27:48` | `cowrie.command.input` |
| `2026-06-23 17:27:48` | `cowrie.command.failed` |
| `2026-06-23 17:27:48` | `cowrie.command.failed` |
| `2026-06-23 17:27:48` | `cowrie.command.failed` |
| `2026-06-23 17:27:48` | `cowrie.command.failed` |
| `2026-06-23 17:27:49` | `cowrie.log.closed` |
| `2026-06-23 17:27:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eda2540db4b2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:28 |
| **Last Seen** | 2026-06-23 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:28:32` | `cowrie.session.connect` |
| `2026-06-23 17:28:32` | `cowrie.client.version` |
| `2026-06-23 17:28:33` | `cowrie.client.kex` |
| `2026-06-23 17:28:33` | `cowrie.login.success` |
| `2026-06-23 17:28:34` | `cowrie.session.params` |
| `2026-06-23 17:28:34` | `cowrie.command.input` |
| `2026-06-23 17:28:34` | `cowrie.log.closed` |
| `2026-06-23 17:28:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ea108ceede1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:28 |
| **Last Seen** | 2026-06-23 17:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'abc123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:28:40` | `cowrie.session.connect` |
| `2026-06-23 17:28:41` | `cowrie.client.version` |
| `2026-06-23 17:28:41` | `cowrie.client.kex` |
| `2026-06-23 17:28:42` | `cowrie.login.success` |
| `2026-06-23 17:28:43` | `cowrie.session.params` |
| `2026-06-23 17:28:43` | `cowrie.command.input` |
| `2026-06-23 17:28:43` | `cowrie.command.input` |
| `2026-06-23 17:28:43` | `cowrie.command.input` |
| `2026-06-23 17:28:43` | `cowrie.command.input` |
| `2026-06-23 17:28:43` | `cowrie.log.closed` |
| `2026-06-23 17:28:45` | `cowrie.session.params` |
| `2026-06-23 17:28:45` | `cowrie.command.input` |
| `2026-06-23 17:28:45` | `cowrie.command.input` |
| `2026-06-23 17:28:45` | `cowrie.command.failed` |
| `2026-06-23 17:28:45` | `cowrie.command.failed` |
| `2026-06-23 17:28:45` | `cowrie.command.failed` |
| `2026-06-23 17:28:45` | `cowrie.command.failed` |
| `2026-06-23 17:28:45` | `cowrie.log.closed` |
| `2026-06-23 17:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4531712fc9c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:29 |
| **Last Seen** | 2026-06-23 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:29:26` | `cowrie.session.connect` |
| `2026-06-23 17:29:26` | `cowrie.client.version` |
| `2026-06-23 17:29:26` | `cowrie.client.kex` |
| `2026-06-23 17:29:26` | `cowrie.login.success` |
| `2026-06-23 17:29:27` | `cowrie.session.params` |
| `2026-06-23 17:29:27` | `cowrie.command.input` |
| `2026-06-23 17:29:27` | `cowrie.log.closed` |
| `2026-06-23 17:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e8bd29d0a31

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:29 |
| **Last Seen** | 2026-06-23 17:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'admin123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:29:36` | `cowrie.session.connect` |
| `2026-06-23 17:29:36` | `cowrie.client.version` |
| `2026-06-23 17:29:36` | `cowrie.client.kex` |
| `2026-06-23 17:29:38` | `cowrie.login.success` |
| `2026-06-23 17:29:39` | `cowrie.session.params` |
| `2026-06-23 17:29:39` | `cowrie.command.input` |
| `2026-06-23 17:29:39` | `cowrie.command.input` |
| `2026-06-23 17:29:39` | `cowrie.command.input` |
| `2026-06-23 17:29:39` | `cowrie.command.input` |
| `2026-06-23 17:29:39` | `cowrie.log.closed` |
| `2026-06-23 17:29:40` | `cowrie.session.params` |
| `2026-06-23 17:29:40` | `cowrie.command.input` |
| `2026-06-23 17:29:40` | `cowrie.command.input` |
| `2026-06-23 17:29:40` | `cowrie.command.failed` |
| `2026-06-23 17:29:40` | `cowrie.command.failed` |
| `2026-06-23 17:29:40` | `cowrie.command.failed` |
| `2026-06-23 17:29:40` | `cowrie.command.failed` |
| `2026-06-23 17:29:40` | `cowrie.log.closed` |
| `2026-06-23 17:29:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47f84880eebe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:30 |
| **Last Seen** | 2026-06-23 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:30:19` | `cowrie.session.connect` |
| `2026-06-23 17:30:19` | `cowrie.client.version` |
| `2026-06-23 17:30:19` | `cowrie.client.kex` |
| `2026-06-23 17:30:19` | `cowrie.login.success` |
| `2026-06-23 17:30:20` | `cowrie.session.params` |
| `2026-06-23 17:30:20` | `cowrie.command.input` |
| `2026-06-23 17:30:21` | `cowrie.log.closed` |
| `2026-06-23 17:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dd031e8f1f9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:30 |
| **Last Seen** | 2026-06-23 17:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'letmein' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:30:33` | `cowrie.session.connect` |
| `2026-06-23 17:30:33` | `cowrie.client.version` |
| `2026-06-23 17:30:33` | `cowrie.client.kex` |
| `2026-06-23 17:30:35` | `cowrie.login.success` |
| `2026-06-23 17:30:36` | `cowrie.session.params` |
| `2026-06-23 17:30:36` | `cowrie.command.input` |
| `2026-06-23 17:30:36` | `cowrie.command.input` |
| `2026-06-23 17:30:36` | `cowrie.command.input` |
| `2026-06-23 17:30:36` | `cowrie.command.input` |
| `2026-06-23 17:30:36` | `cowrie.log.closed` |
| `2026-06-23 17:30:37` | `cowrie.session.params` |
| `2026-06-23 17:30:37` | `cowrie.command.input` |
| `2026-06-23 17:30:37` | `cowrie.command.input` |
| `2026-06-23 17:30:37` | `cowrie.command.failed` |
| `2026-06-23 17:30:37` | `cowrie.command.failed` |
| `2026-06-23 17:30:37` | `cowrie.command.failed` |
| `2026-06-23 17:30:37` | `cowrie.command.failed` |
| `2026-06-23 17:30:37` | `cowrie.log.closed` |
| `2026-06-23 17:30:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2a05c2f8be5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:31 |
| **Last Seen** | 2026-06-23 17:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:31:12` | `cowrie.session.connect` |
| `2026-06-23 17:31:12` | `cowrie.client.version` |
| `2026-06-23 17:31:12` | `cowrie.client.kex` |
| `2026-06-23 17:31:12` | `cowrie.login.success` |
| `2026-06-23 17:31:13` | `cowrie.session.params` |
| `2026-06-23 17:31:13` | `cowrie.command.input` |
| `2026-06-23 17:31:13` | `cowrie.log.closed` |
| `2026-06-23 17:31:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccc7884a1749

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:31 |
| **Last Seen** | 2026-06-23 17:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'pass123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:31:29` | `cowrie.session.connect` |
| `2026-06-23 17:31:29` | `cowrie.client.version` |
| `2026-06-23 17:31:29` | `cowrie.client.kex` |
| `2026-06-23 17:31:31` | `cowrie.login.success` |
| `2026-06-23 17:31:32` | `cowrie.session.params` |
| `2026-06-23 17:31:32` | `cowrie.command.input` |
| `2026-06-23 17:31:32` | `cowrie.command.input` |
| `2026-06-23 17:31:32` | `cowrie.command.input` |
| `2026-06-23 17:31:32` | `cowrie.command.input` |
| `2026-06-23 17:31:33` | `cowrie.log.closed` |
| `2026-06-23 17:31:34` | `cowrie.session.params` |
| `2026-06-23 17:31:34` | `cowrie.command.input` |
| `2026-06-23 17:31:34` | `cowrie.command.input` |
| `2026-06-23 17:31:34` | `cowrie.command.failed` |
| `2026-06-23 17:31:34` | `cowrie.command.failed` |
| `2026-06-23 17:31:34` | `cowrie.command.failed` |
| `2026-06-23 17:31:34` | `cowrie.command.failed` |
| `2026-06-23 17:31:34` | `cowrie.log.closed` |
| `2026-06-23 17:31:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c2bc6f51a7a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:32 |
| **Last Seen** | 2026-06-23 17:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:32:04` | `cowrie.session.connect` |
| `2026-06-23 17:32:04` | `cowrie.client.version` |
| `2026-06-23 17:32:05` | `cowrie.client.kex` |
| `2026-06-23 17:32:05` | `cowrie.login.success` |
| `2026-06-23 17:32:05` | `cowrie.session.params` |
| `2026-06-23 17:32:05` | `cowrie.command.input` |
| `2026-06-23 17:32:06` | `cowrie.log.closed` |
| `2026-06-23 17:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aae6f91b5be9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:32 |
| **Last Seen** | 2026-06-23 17:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:32:25` | `cowrie.session.connect` |
| `2026-06-23 17:32:25` | `cowrie.client.version` |
| `2026-06-23 17:32:25` | `cowrie.client.kex` |
| `2026-06-23 17:32:26` | `cowrie.login.success` |
| `2026-06-23 17:32:28` | `cowrie.session.params` |
| `2026-06-23 17:32:28` | `cowrie.command.input` |
| `2026-06-23 17:32:28` | `cowrie.command.input` |
| `2026-06-23 17:32:28` | `cowrie.command.input` |
| `2026-06-23 17:32:28` | `cowrie.command.input` |
| `2026-06-23 17:32:28` | `cowrie.log.closed` |
| `2026-06-23 17:32:30` | `cowrie.session.params` |
| `2026-06-23 17:32:30` | `cowrie.command.input` |
| `2026-06-23 17:32:30` | `cowrie.command.input` |
| `2026-06-23 17:32:30` | `cowrie.command.failed` |
| `2026-06-23 17:32:30` | `cowrie.command.failed` |
| `2026-06-23 17:32:30` | `cowrie.command.failed` |
| `2026-06-23 17:32:30` | `cowrie.command.failed` |
| `2026-06-23 17:32:30` | `cowrie.log.closed` |
| `2026-06-23 17:32:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc5001196b29

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:32 |
| **Last Seen** | 2026-06-23 17:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:32:58` | `cowrie.session.connect` |
| `2026-06-23 17:32:58` | `cowrie.client.version` |
| `2026-06-23 17:32:58` | `cowrie.client.kex` |
| `2026-06-23 17:32:59` | `cowrie.login.success` |
| `2026-06-23 17:32:59` | `cowrie.session.params` |
| `2026-06-23 17:32:59` | `cowrie.command.input` |
| `2026-06-23 17:32:59` | `cowrie.log.closed` |
| `2026-06-23 17:32:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12efcacf190d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:33 |
| **Last Seen** | 2026-06-23 17:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'qwerty123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:33:23` | `cowrie.session.connect` |
| `2026-06-23 17:33:23` | `cowrie.client.version` |
| `2026-06-23 17:33:23` | `cowrie.client.kex` |
| `2026-06-23 17:33:24` | `cowrie.login.success` |
| `2026-06-23 17:33:25` | `cowrie.session.params` |
| `2026-06-23 17:33:25` | `cowrie.command.input` |
| `2026-06-23 17:33:25` | `cowrie.command.input` |
| `2026-06-23 17:33:25` | `cowrie.command.input` |
| `2026-06-23 17:33:25` | `cowrie.command.input` |
| `2026-06-23 17:33:26` | `cowrie.log.closed` |
| `2026-06-23 17:33:27` | `cowrie.session.params` |
| `2026-06-23 17:33:27` | `cowrie.command.input` |
| `2026-06-23 17:33:27` | `cowrie.command.input` |
| `2026-06-23 17:33:27` | `cowrie.command.failed` |
| `2026-06-23 17:33:27` | `cowrie.command.failed` |
| `2026-06-23 17:33:27` | `cowrie.command.failed` |
| `2026-06-23 17:33:27` | `cowrie.command.failed` |
| `2026-06-23 17:33:27` | `cowrie.log.closed` |
| `2026-06-23 17:33:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84b5970020a2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:33 |
| **Last Seen** | 2026-06-23 17:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:33:53` | `cowrie.session.connect` |
| `2026-06-23 17:33:53` | `cowrie.client.version` |
| `2026-06-23 17:33:53` | `cowrie.client.kex` |
| `2026-06-23 17:33:54` | `cowrie.login.success` |
| `2026-06-23 17:33:54` | `cowrie.session.params` |
| `2026-06-23 17:33:54` | `cowrie.command.input` |
| `2026-06-23 17:33:54` | `cowrie.log.closed` |
| `2026-06-23 17:33:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9da5656a80ef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:34 |
| **Last Seen** | 2026-06-23 17:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:34:19` | `cowrie.session.connect` |
| `2026-06-23 17:34:19` | `cowrie.client.version` |
| `2026-06-23 17:34:19` | `cowrie.client.kex` |
| `2026-06-23 17:34:21` | `cowrie.login.success` |
| `2026-06-23 17:34:22` | `cowrie.session.params` |
| `2026-06-23 17:34:22` | `cowrie.command.input` |
| `2026-06-23 17:34:22` | `cowrie.command.input` |
| `2026-06-23 17:34:22` | `cowrie.command.input` |
| `2026-06-23 17:34:22` | `cowrie.command.input` |
| `2026-06-23 17:34:22` | `cowrie.log.closed` |
| `2026-06-23 17:34:23` | `cowrie.session.params` |
| `2026-06-23 17:34:23` | `cowrie.command.input` |
| `2026-06-23 17:34:23` | `cowrie.command.input` |
| `2026-06-23 17:34:23` | `cowrie.command.failed` |
| `2026-06-23 17:34:23` | `cowrie.command.failed` |
| `2026-06-23 17:34:23` | `cowrie.command.failed` |
| `2026-06-23 17:34:23` | `cowrie.command.failed` |
| `2026-06-23 17:34:23` | `cowrie.log.closed` |
| `2026-06-23 17:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a94ee2c7d07

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:34 |
| **Last Seen** | 2026-06-23 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:34:50` | `cowrie.session.connect` |
| `2026-06-23 17:34:50` | `cowrie.client.version` |
| `2026-06-23 17:34:50` | `cowrie.client.kex` |
| `2026-06-23 17:34:50` | `cowrie.login.success` |
| `2026-06-23 17:34:51` | `cowrie.session.params` |
| `2026-06-23 17:34:51` | `cowrie.command.input` |
| `2026-06-23 17:34:51` | `cowrie.log.closed` |
| `2026-06-23 17:34:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee07dcc74260

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:35 |
| **Last Seen** | 2026-06-23 17:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:35:18` | `cowrie.session.connect` |
| `2026-06-23 17:35:18` | `cowrie.client.version` |
| `2026-06-23 17:35:18` | `cowrie.client.kex` |
| `2026-06-23 17:35:20` | `cowrie.login.success` |
| `2026-06-23 17:35:21` | `cowrie.session.params` |
| `2026-06-23 17:35:21` | `cowrie.command.input` |
| `2026-06-23 17:35:21` | `cowrie.command.input` |
| `2026-06-23 17:35:21` | `cowrie.command.input` |
| `2026-06-23 17:35:21` | `cowrie.command.input` |
| `2026-06-23 17:35:21` | `cowrie.log.closed` |
| `2026-06-23 17:35:22` | `cowrie.session.params` |
| `2026-06-23 17:35:22` | `cowrie.command.input` |
| `2026-06-23 17:35:22` | `cowrie.command.input` |
| `2026-06-23 17:35:22` | `cowrie.command.failed` |
| `2026-06-23 17:35:22` | `cowrie.command.failed` |
| `2026-06-23 17:35:22` | `cowrie.command.failed` |
| `2026-06-23 17:35:22` | `cowrie.command.failed` |
| `2026-06-23 17:35:23` | `cowrie.log.closed` |
| `2026-06-23 17:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fcd25d1cc00

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:35 |
| **Last Seen** | 2026-06-23 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:35:44` | `cowrie.session.connect` |
| `2026-06-23 17:35:44` | `cowrie.client.version` |
| `2026-06-23 17:35:45` | `cowrie.client.kex` |
| `2026-06-23 17:35:45` | `cowrie.login.success` |
| `2026-06-23 17:35:46` | `cowrie.session.params` |
| `2026-06-23 17:35:46` | `cowrie.command.input` |
| `2026-06-23 17:35:46` | `cowrie.log.closed` |
| `2026-06-23 17:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0420eb3b51f3

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 17:36 |
| **Last Seen** | 2026-06-23 17:36 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:36:01` | `cowrie.session.connect` |
| `2026-06-23 17:36:02` | `cowrie.client.version` |
| `2026-06-23 17:36:02` | `cowrie.client.kex` |
| `2026-06-23 17:36:09` | `cowrie.login.success` |
| `2026-06-23 17:36:13` | `cowrie.session.params` |
| `2026-06-23 17:36:13` | `cowrie.command.input` |
| `2026-06-23 17:36:15` | `cowrie.log.closed` |
| `2026-06-23 17:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fa4e981c0be

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:36 |
| **Last Seen** | 2026-06-23 17:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234567890' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:36:16` | `cowrie.session.connect` |
| `2026-06-23 17:36:16` | `cowrie.client.version` |
| `2026-06-23 17:36:16` | `cowrie.client.kex` |
| `2026-06-23 17:36:17` | `cowrie.login.success` |
| `2026-06-23 17:36:18` | `cowrie.session.params` |
| `2026-06-23 17:36:18` | `cowrie.command.input` |
| `2026-06-23 17:36:18` | `cowrie.command.input` |
| `2026-06-23 17:36:18` | `cowrie.command.input` |
| `2026-06-23 17:36:18` | `cowrie.command.input` |
| `2026-06-23 17:36:19` | `cowrie.log.closed` |
| `2026-06-23 17:36:21` | `cowrie.session.params` |
| `2026-06-23 17:36:21` | `cowrie.command.input` |
| `2026-06-23 17:36:21` | `cowrie.command.input` |
| `2026-06-23 17:36:21` | `cowrie.command.failed` |
| `2026-06-23 17:36:21` | `cowrie.command.failed` |
| `2026-06-23 17:36:21` | `cowrie.command.failed` |
| `2026-06-23 17:36:21` | `cowrie.command.failed` |
| `2026-06-23 17:36:21` | `cowrie.log.closed` |
| `2026-06-23 17:36:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1989da96aa4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.195[.]138` |
| **First Seen** | 2026-06-23 17:36 |
| **Last Seen** | 2026-06-23 17:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, echo ALIVE_CHECK, /bin/busybox TEST 2>&1, cat /proc 2>&1, ./ 2>&1` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:36:19` | `cowrie.session.connect` |
| `2026-06-23 17:36:19` | `cowrie.login.success` |
| `2026-06-23 17:36:20` | `cowrie.session.params` |
| `2026-06-23 17:36:21` | `cowrie.command.input` |
| `2026-06-23 17:36:22` | `cowrie.command.input` |
| `2026-06-23 17:36:22` | `cowrie.command.input` |
| `2026-06-23 17:36:23` | `cowrie.command.input` |
| `2026-06-23 17:36:24` | `cowrie.command.input` |
| `2026-06-23 17:36:24` | `cowrie.command.failed` |
| `2026-06-23 17:36:24` | `cowrie.log.closed` |
| `2026-06-23 17:36:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.195[.]138` to AbuseIPDB if not already reported
- [ ] Block `217.60.195[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-335c757d95cc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:36 |
| **Last Seen** | 2026-06-23 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:36:37` | `cowrie.session.connect` |
| `2026-06-23 17:36:37` | `cowrie.client.version` |
| `2026-06-23 17:36:37` | `cowrie.client.kex` |
| `2026-06-23 17:36:38` | `cowrie.login.success` |
| `2026-06-23 17:36:39` | `cowrie.session.params` |
| `2026-06-23 17:36:39` | `cowrie.command.input` |
| `2026-06-23 17:36:39` | `cowrie.log.closed` |
| `2026-06-23 17:36:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d47d59607742

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:37 |
| **Last Seen** | 2026-06-23 17:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1q2w3e4r' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:37:13` | `cowrie.session.connect` |
| `2026-06-23 17:37:13` | `cowrie.client.version` |
| `2026-06-23 17:37:13` | `cowrie.client.kex` |
| `2026-06-23 17:37:15` | `cowrie.login.success` |
| `2026-06-23 17:37:16` | `cowrie.session.params` |
| `2026-06-23 17:37:16` | `cowrie.command.input` |
| `2026-06-23 17:37:16` | `cowrie.command.input` |
| `2026-06-23 17:37:16` | `cowrie.command.input` |
| `2026-06-23 17:37:16` | `cowrie.command.input` |
| `2026-06-23 17:37:16` | `cowrie.log.closed` |
| `2026-06-23 17:37:17` | `cowrie.session.params` |
| `2026-06-23 17:37:17` | `cowrie.command.input` |
| `2026-06-23 17:37:17` | `cowrie.command.input` |
| `2026-06-23 17:37:17` | `cowrie.command.failed` |
| `2026-06-23 17:37:17` | `cowrie.command.failed` |
| `2026-06-23 17:37:17` | `cowrie.command.failed` |
| `2026-06-23 17:37:17` | `cowrie.command.failed` |
| `2026-06-23 17:37:17` | `cowrie.log.closed` |
| `2026-06-23 17:37:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32ac94a0c815

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:37 |
| **Last Seen** | 2026-06-23 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:37:29` | `cowrie.session.connect` |
| `2026-06-23 17:37:29` | `cowrie.client.version` |
| `2026-06-23 17:37:29` | `cowrie.client.kex` |
| `2026-06-23 17:37:30` | `cowrie.login.success` |
| `2026-06-23 17:37:31` | `cowrie.session.params` |
| `2026-06-23 17:37:31` | `cowrie.command.input` |
| `2026-06-23 17:37:31` | `cowrie.log.closed` |
| `2026-06-23 17:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-568fc6a75714

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:38 |
| **Last Seen** | 2026-06-23 17:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'admin123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:38:10` | `cowrie.session.connect` |
| `2026-06-23 17:38:10` | `cowrie.client.version` |
| `2026-06-23 17:38:10` | `cowrie.client.kex` |
| `2026-06-23 17:38:12` | `cowrie.login.success` |
| `2026-06-23 17:38:13` | `cowrie.session.params` |
| `2026-06-23 17:38:13` | `cowrie.command.input` |
| `2026-06-23 17:38:13` | `cowrie.command.input` |
| `2026-06-23 17:38:13` | `cowrie.command.input` |
| `2026-06-23 17:38:13` | `cowrie.command.input` |
| `2026-06-23 17:38:13` | `cowrie.log.closed` |
| `2026-06-23 17:38:14` | `cowrie.session.params` |
| `2026-06-23 17:38:14` | `cowrie.command.input` |
| `2026-06-23 17:38:14` | `cowrie.command.input` |
| `2026-06-23 17:38:14` | `cowrie.command.failed` |
| `2026-06-23 17:38:14` | `cowrie.command.failed` |
| `2026-06-23 17:38:14` | `cowrie.command.failed` |
| `2026-06-23 17:38:14` | `cowrie.command.failed` |
| `2026-06-23 17:38:14` | `cowrie.log.closed` |
| `2026-06-23 17:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0209a9f92f84

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:38 |
| **Last Seen** | 2026-06-23 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:38:21` | `cowrie.session.connect` |
| `2026-06-23 17:38:21` | `cowrie.client.version` |
| `2026-06-23 17:38:21` | `cowrie.client.kex` |
| `2026-06-23 17:38:21` | `cowrie.login.success` |
| `2026-06-23 17:38:22` | `cowrie.session.params` |
| `2026-06-23 17:38:22` | `cowrie.command.input` |
| `2026-06-23 17:38:22` | `cowrie.log.closed` |
| `2026-06-23 17:38:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ce6737e917c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:39 |
| **Last Seen** | 2026-06-23 17:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'pass123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:39:07` | `cowrie.session.connect` |
| `2026-06-23 17:39:07` | `cowrie.client.version` |
| `2026-06-23 17:39:07` | `cowrie.client.kex` |
| `2026-06-23 17:39:08` | `cowrie.login.success` |
| `2026-06-23 17:39:09` | `cowrie.session.params` |
| `2026-06-23 17:39:09` | `cowrie.command.input` |
| `2026-06-23 17:39:09` | `cowrie.command.input` |
| `2026-06-23 17:39:09` | `cowrie.command.input` |
| `2026-06-23 17:39:09` | `cowrie.command.input` |
| `2026-06-23 17:39:10` | `cowrie.log.closed` |
| `2026-06-23 17:39:11` | `cowrie.session.params` |
| `2026-06-23 17:39:11` | `cowrie.command.input` |
| `2026-06-23 17:39:11` | `cowrie.command.input` |
| `2026-06-23 17:39:11` | `cowrie.command.failed` |
| `2026-06-23 17:39:11` | `cowrie.command.failed` |
| `2026-06-23 17:39:11` | `cowrie.command.failed` |
| `2026-06-23 17:39:11` | `cowrie.command.failed` |
| `2026-06-23 17:39:11` | `cowrie.log.closed` |
| `2026-06-23 17:39:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6537174fce27

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:39 |
| **Last Seen** | 2026-06-23 17:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:39:13` | `cowrie.session.connect` |
| `2026-06-23 17:39:13` | `cowrie.client.version` |
| `2026-06-23 17:39:13` | `cowrie.client.kex` |
| `2026-06-23 17:39:13` | `cowrie.login.success` |
| `2026-06-23 17:39:14` | `cowrie.session.params` |
| `2026-06-23 17:39:14` | `cowrie.command.input` |
| `2026-06-23 17:39:14` | `cowrie.log.closed` |
| `2026-06-23 17:39:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80e06b0663ab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:40 |
| **Last Seen** | 2026-06-23 17:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password1' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:40:03` | `cowrie.session.connect` |
| `2026-06-23 17:40:03` | `cowrie.client.version` |
| `2026-06-23 17:40:03` | `cowrie.client.kex` |
| `2026-06-23 17:40:04` | `cowrie.login.success` |
| `2026-06-23 17:40:05` | `cowrie.session.params` |
| `2026-06-23 17:40:05` | `cowrie.command.input` |
| `2026-06-23 17:40:05` | `cowrie.command.input` |
| `2026-06-23 17:40:05` | `cowrie.command.input` |
| `2026-06-23 17:40:05` | `cowrie.command.input` |
| `2026-06-23 17:40:05` | `cowrie.log.closed` |
| `2026-06-23 17:40:07` | `cowrie.session.params` |
| `2026-06-23 17:40:07` | `cowrie.command.input` |
| `2026-06-23 17:40:07` | `cowrie.command.input` |
| `2026-06-23 17:40:07` | `cowrie.command.failed` |
| `2026-06-23 17:40:07` | `cowrie.command.failed` |
| `2026-06-23 17:40:07` | `cowrie.command.failed` |
| `2026-06-23 17:40:07` | `cowrie.command.failed` |
| `2026-06-23 17:40:07` | `cowrie.log.closed` |
| `2026-06-23 17:40:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74247faf9763

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:40 |
| **Last Seen** | 2026-06-23 17:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:40:08` | `cowrie.session.connect` |
| `2026-06-23 17:40:08` | `cowrie.client.version` |
| `2026-06-23 17:40:08` | `cowrie.client.kex` |
| `2026-06-23 17:40:08` | `cowrie.login.success` |
| `2026-06-23 17:40:09` | `cowrie.session.params` |
| `2026-06-23 17:40:09` | `cowrie.command.input` |
| `2026-06-23 17:40:09` | `cowrie.log.closed` |
| `2026-06-23 17:40:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-518c9afc3876

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:40 |
| **Last Seen** | 2026-06-23 17:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'qwerty123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:40:59` | `cowrie.session.connect` |
| `2026-06-23 17:40:59` | `cowrie.client.version` |
| `2026-06-23 17:40:59` | `cowrie.client.kex` |
| `2026-06-23 17:41:01` | `cowrie.login.success` |
| `2026-06-23 17:41:02` | `cowrie.session.params` |
| `2026-06-23 17:41:02` | `cowrie.command.input` |
| `2026-06-23 17:41:02` | `cowrie.command.input` |
| `2026-06-23 17:41:02` | `cowrie.command.input` |
| `2026-06-23 17:41:02` | `cowrie.command.input` |
| `2026-06-23 17:41:02` | `cowrie.log.closed` |
| `2026-06-23 17:41:03` | `cowrie.session.params` |
| `2026-06-23 17:41:03` | `cowrie.command.input` |
| `2026-06-23 17:41:03` | `cowrie.command.input` |
| `2026-06-23 17:41:03` | `cowrie.command.failed` |
| `2026-06-23 17:41:03` | `cowrie.command.failed` |
| `2026-06-23 17:41:03` | `cowrie.command.failed` |
| `2026-06-23 17:41:03` | `cowrie.command.failed` |
| `2026-06-23 17:41:03` | `cowrie.log.closed` |
| `2026-06-23 17:41:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49e180dcd245

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:41 |
| **Last Seen** | 2026-06-23 17:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:41:03` | `cowrie.session.connect` |
| `2026-06-23 17:41:03` | `cowrie.client.version` |
| `2026-06-23 17:41:03` | `cowrie.client.kex` |
| `2026-06-23 17:41:04` | `cowrie.login.success` |
| `2026-06-23 17:41:05` | `cowrie.session.params` |
| `2026-06-23 17:41:05` | `cowrie.command.input` |
| `2026-06-23 17:41:05` | `cowrie.log.closed` |
| `2026-06-23 17:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72670ec8f192

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:41 |
| **Last Seen** | 2026-06-23 17:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:41:56` | `cowrie.session.connect` |
| `2026-06-23 17:41:56` | `cowrie.client.version` |
| `2026-06-23 17:41:56` | `cowrie.client.kex` |
| `2026-06-23 17:41:57` | `cowrie.login.success` |
| `2026-06-23 17:41:58` | `cowrie.session.params` |
| `2026-06-23 17:41:58` | `cowrie.command.input` |
| `2026-06-23 17:41:58` | `cowrie.command.input` |
| `2026-06-23 17:41:58` | `cowrie.command.input` |
| `2026-06-23 17:41:58` | `cowrie.command.input` |
| `2026-06-23 17:41:58` | `cowrie.log.closed` |
| `2026-06-23 17:42:00` | `cowrie.session.params` |
| `2026-06-23 17:42:00` | `cowrie.command.input` |
| `2026-06-23 17:42:00` | `cowrie.command.input` |
| `2026-06-23 17:42:00` | `cowrie.command.failed` |
| `2026-06-23 17:42:00` | `cowrie.command.failed` |
| `2026-06-23 17:42:00` | `cowrie.command.failed` |
| `2026-06-23 17:42:00` | `cowrie.command.failed` |
| `2026-06-23 17:42:00` | `cowrie.log.closed` |
| `2026-06-23 17:42:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c094bd362fc7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:41 |
| **Last Seen** | 2026-06-23 17:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:41:59` | `cowrie.session.connect` |
| `2026-06-23 17:41:59` | `cowrie.client.version` |
| `2026-06-23 17:41:59` | `cowrie.client.kex` |
| `2026-06-23 17:42:00` | `cowrie.login.success` |
| `2026-06-23 17:42:01` | `cowrie.session.params` |
| `2026-06-23 17:42:01` | `cowrie.command.input` |
| `2026-06-23 17:42:01` | `cowrie.log.closed` |
| `2026-06-23 17:42:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc12a848be4d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:42 |
| **Last Seen** | 2026-06-23 17:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123456' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:42:51` | `cowrie.session.connect` |
| `2026-06-23 17:42:51` | `cowrie.client.version` |
| `2026-06-23 17:42:51` | `cowrie.client.kex` |
| `2026-06-23 17:42:53` | `cowrie.login.success` |
| `2026-06-23 17:42:54` | `cowrie.session.params` |
| `2026-06-23 17:42:54` | `cowrie.command.input` |
| `2026-06-23 17:42:54` | `cowrie.command.input` |
| `2026-06-23 17:42:54` | `cowrie.command.input` |
| `2026-06-23 17:42:54` | `cowrie.command.input` |
| `2026-06-23 17:42:55` | `cowrie.log.closed` |
| `2026-06-23 17:42:56` | `cowrie.session.params` |
| `2026-06-23 17:42:56` | `cowrie.command.input` |
| `2026-06-23 17:42:56` | `cowrie.command.input` |
| `2026-06-23 17:42:56` | `cowrie.command.failed` |
| `2026-06-23 17:42:56` | `cowrie.command.failed` |
| `2026-06-23 17:42:56` | `cowrie.command.failed` |
| `2026-06-23 17:42:56` | `cowrie.command.failed` |
| `2026-06-23 17:42:56` | `cowrie.log.closed` |
| `2026-06-23 17:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1a55c8ac37e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:42 |
| **Last Seen** | 2026-06-23 17:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:42:53` | `cowrie.session.connect` |
| `2026-06-23 17:42:53` | `cowrie.client.version` |
| `2026-06-23 17:42:53` | `cowrie.client.kex` |
| `2026-06-23 17:42:53` | `cowrie.login.success` |
| `2026-06-23 17:42:55` | `cowrie.session.params` |
| `2026-06-23 17:42:55` | `cowrie.command.input` |
| `2026-06-23 17:42:55` | `cowrie.log.closed` |
| `2026-06-23 17:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45406474e341

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:43 |
| **Last Seen** | 2026-06-23 17:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:43:46` | `cowrie.session.connect` |
| `2026-06-23 17:43:46` | `cowrie.client.version` |
| `2026-06-23 17:43:46` | `cowrie.client.kex` |
| `2026-06-23 17:43:46` | `cowrie.login.success` |
| `2026-06-23 17:43:47` | `cowrie.session.params` |
| `2026-06-23 17:43:47` | `cowrie.command.input` |
| `2026-06-23 17:43:47` | `cowrie.log.closed` |
| `2026-06-23 17:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-148227858fb4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:43 |
| **Last Seen** | 2026-06-23 17:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234567' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:43:47` | `cowrie.session.connect` |
| `2026-06-23 17:43:47` | `cowrie.client.version` |
| `2026-06-23 17:43:47` | `cowrie.client.kex` |
| `2026-06-23 17:43:48` | `cowrie.login.success` |
| `2026-06-23 17:43:50` | `cowrie.session.params` |
| `2026-06-23 17:43:50` | `cowrie.command.input` |
| `2026-06-23 17:43:50` | `cowrie.command.input` |
| `2026-06-23 17:43:50` | `cowrie.command.input` |
| `2026-06-23 17:43:50` | `cowrie.command.input` |
| `2026-06-23 17:43:50` | `cowrie.log.closed` |
| `2026-06-23 17:43:51` | `cowrie.session.params` |
| `2026-06-23 17:43:51` | `cowrie.command.input` |
| `2026-06-23 17:43:51` | `cowrie.command.input` |
| `2026-06-23 17:43:51` | `cowrie.command.failed` |
| `2026-06-23 17:43:51` | `cowrie.command.failed` |
| `2026-06-23 17:43:51` | `cowrie.command.failed` |
| `2026-06-23 17:43:51` | `cowrie.command.failed` |
| `2026-06-23 17:43:51` | `cowrie.log.closed` |
| `2026-06-23 17:43:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-731d2a57ba1b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:44 |
| **Last Seen** | 2026-06-23 17:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:44:38` | `cowrie.session.connect` |
| `2026-06-23 17:44:38` | `cowrie.client.version` |
| `2026-06-23 17:44:38` | `cowrie.client.kex` |
| `2026-06-23 17:44:38` | `cowrie.login.success` |
| `2026-06-23 17:44:39` | `cowrie.session.params` |
| `2026-06-23 17:44:39` | `cowrie.command.input` |
| `2026-06-23 17:44:39` | `cowrie.log.closed` |
| `2026-06-23 17:44:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f73707b683fc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:44 |
| **Last Seen** | 2026-06-23 17:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345678' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:44:44` | `cowrie.session.connect` |
| `2026-06-23 17:44:44` | `cowrie.client.version` |
| `2026-06-23 17:44:44` | `cowrie.client.kex` |
| `2026-06-23 17:44:45` | `cowrie.login.success` |
| `2026-06-23 17:44:47` | `cowrie.session.params` |
| `2026-06-23 17:44:47` | `cowrie.command.input` |
| `2026-06-23 17:44:47` | `cowrie.command.input` |
| `2026-06-23 17:44:47` | `cowrie.command.input` |
| `2026-06-23 17:44:47` | `cowrie.command.input` |
| `2026-06-23 17:44:47` | `cowrie.log.closed` |
| `2026-06-23 17:44:48` | `cowrie.session.params` |
| `2026-06-23 17:44:48` | `cowrie.command.input` |
| `2026-06-23 17:44:48` | `cowrie.command.input` |
| `2026-06-23 17:44:48` | `cowrie.command.failed` |
| `2026-06-23 17:44:48` | `cowrie.command.failed` |
| `2026-06-23 17:44:48` | `cowrie.command.failed` |
| `2026-06-23 17:44:48` | `cowrie.command.failed` |
| `2026-06-23 17:44:48` | `cowrie.log.closed` |
| `2026-06-23 17:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3e70e8d96a8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:45 |
| **Last Seen** | 2026-06-23 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:45:32` | `cowrie.session.connect` |
| `2026-06-23 17:45:32` | `cowrie.client.version` |
| `2026-06-23 17:45:33` | `cowrie.client.kex` |
| `2026-06-23 17:45:33` | `cowrie.login.success` |
| `2026-06-23 17:45:34` | `cowrie.session.params` |
| `2026-06-23 17:45:34` | `cowrie.command.input` |
| `2026-06-23 17:45:34` | `cowrie.log.closed` |
| `2026-06-23 17:45:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c771e7d4de1d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:45 |
| **Last Seen** | 2026-06-23 17:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123456789' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:45:42` | `cowrie.session.connect` |
| `2026-06-23 17:45:42` | `cowrie.client.version` |
| `2026-06-23 17:45:42` | `cowrie.client.kex` |
| `2026-06-23 17:45:44` | `cowrie.login.success` |
| `2026-06-23 17:45:45` | `cowrie.session.params` |
| `2026-06-23 17:45:45` | `cowrie.command.input` |
| `2026-06-23 17:45:45` | `cowrie.command.input` |
| `2026-06-23 17:45:45` | `cowrie.command.input` |
| `2026-06-23 17:45:45` | `cowrie.command.input` |
| `2026-06-23 17:45:45` | `cowrie.log.closed` |
| `2026-06-23 17:45:47` | `cowrie.session.params` |
| `2026-06-23 17:45:47` | `cowrie.command.input` |
| `2026-06-23 17:45:47` | `cowrie.command.input` |
| `2026-06-23 17:45:47` | `cowrie.command.failed` |
| `2026-06-23 17:45:47` | `cowrie.command.failed` |
| `2026-06-23 17:45:47` | `cowrie.command.failed` |
| `2026-06-23 17:45:47` | `cowrie.command.failed` |
| `2026-06-23 17:45:47` | `cowrie.log.closed` |
| `2026-06-23 17:45:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc3687dc6c72

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:46 |
| **Last Seen** | 2026-06-23 17:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:46:28` | `cowrie.session.connect` |
| `2026-06-23 17:46:28` | `cowrie.client.version` |
| `2026-06-23 17:46:28` | `cowrie.client.kex` |
| `2026-06-23 17:46:29` | `cowrie.login.success` |
| `2026-06-23 17:46:29` | `cowrie.session.params` |
| `2026-06-23 17:46:29` | `cowrie.command.input` |
| `2026-06-23 17:46:30` | `cowrie.log.closed` |
| `2026-06-23 17:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9e509d2c5bf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:46 |
| **Last Seen** | 2026-06-23 17:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'abc123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:46:39` | `cowrie.session.connect` |
| `2026-06-23 17:46:39` | `cowrie.client.version` |
| `2026-06-23 17:46:39` | `cowrie.client.kex` |
| `2026-06-23 17:46:41` | `cowrie.login.success` |
| `2026-06-23 17:46:42` | `cowrie.session.params` |
| `2026-06-23 17:46:42` | `cowrie.command.input` |
| `2026-06-23 17:46:42` | `cowrie.command.input` |
| `2026-06-23 17:46:42` | `cowrie.command.input` |
| `2026-06-23 17:46:42` | `cowrie.command.input` |
| `2026-06-23 17:46:42` | `cowrie.log.closed` |
| `2026-06-23 17:46:43` | `cowrie.session.params` |
| `2026-06-23 17:46:43` | `cowrie.command.input` |
| `2026-06-23 17:46:43` | `cowrie.command.input` |
| `2026-06-23 17:46:43` | `cowrie.command.failed` |
| `2026-06-23 17:46:43` | `cowrie.command.failed` |
| `2026-06-23 17:46:43` | `cowrie.command.failed` |
| `2026-06-23 17:46:43` | `cowrie.command.failed` |
| `2026-06-23 17:46:44` | `cowrie.log.closed` |
| `2026-06-23 17:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2dd2fc07d72

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:47 |
| **Last Seen** | 2026-06-23 17:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:47:23` | `cowrie.session.connect` |
| `2026-06-23 17:47:23` | `cowrie.client.version` |
| `2026-06-23 17:47:23` | `cowrie.client.kex` |
| `2026-06-23 17:47:24` | `cowrie.login.success` |
| `2026-06-23 17:47:24` | `cowrie.session.params` |
| `2026-06-23 17:47:24` | `cowrie.command.input` |
| `2026-06-23 17:47:24` | `cowrie.log.closed` |
| `2026-06-23 17:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01866faea7bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:47 |
| **Last Seen** | 2026-06-23 17:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'admin123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:47:37` | `cowrie.session.connect` |
| `2026-06-23 17:47:37` | `cowrie.client.version` |
| `2026-06-23 17:47:37` | `cowrie.client.kex` |
| `2026-06-23 17:47:38` | `cowrie.login.success` |
| `2026-06-23 17:47:39` | `cowrie.session.params` |
| `2026-06-23 17:47:39` | `cowrie.command.input` |
| `2026-06-23 17:47:39` | `cowrie.command.input` |
| `2026-06-23 17:47:39` | `cowrie.command.input` |
| `2026-06-23 17:47:39` | `cowrie.command.input` |
| `2026-06-23 17:47:40` | `cowrie.log.closed` |
| `2026-06-23 17:47:41` | `cowrie.session.params` |
| `2026-06-23 17:47:41` | `cowrie.command.input` |
| `2026-06-23 17:47:41` | `cowrie.command.input` |
| `2026-06-23 17:47:41` | `cowrie.command.failed` |
| `2026-06-23 17:47:41` | `cowrie.command.failed` |
| `2026-06-23 17:47:41` | `cowrie.command.failed` |
| `2026-06-23 17:47:41` | `cowrie.command.failed` |
| `2026-06-23 17:47:41` | `cowrie.log.closed` |
| `2026-06-23 17:47:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d8f55408ab2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:48 |
| **Last Seen** | 2026-06-23 17:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:48:17` | `cowrie.session.connect` |
| `2026-06-23 17:48:17` | `cowrie.client.version` |
| `2026-06-23 17:48:17` | `cowrie.client.kex` |
| `2026-06-23 17:48:18` | `cowrie.login.success` |
| `2026-06-23 17:48:18` | `cowrie.session.params` |
| `2026-06-23 17:48:18` | `cowrie.command.input` |
| `2026-06-23 17:48:18` | `cowrie.log.closed` |
| `2026-06-23 17:48:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e94d8de050d

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]100` |
| **First Seen** | 2026-06-23 17:48 |
| **Last Seen** | 2026-06-23 17:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:48:27` | `cowrie.session.connect` |
| `2026-06-23 17:48:27` | `cowrie.login.success` |
| `2026-06-23 17:48:28` | `cowrie.session.params` |
| `2026-06-23 17:48:28` | `cowrie.command.input` |
| `2026-06-23 17:48:29` | `cowrie.command.input` |
| `2026-06-23 17:48:29` | `cowrie.command.input` |
| `2026-06-23 17:48:30` | `cowrie.command.input` |
| `2026-06-23 17:48:30` | `cowrie.command.failed` |
| `2026-06-23 17:48:30` | `cowrie.log.closed` |
| `2026-06-23 17:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]100` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7081c25d8519

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:48 |
| **Last Seen** | 2026-06-23 17:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:48:33` | `cowrie.session.connect` |
| `2026-06-23 17:48:33` | `cowrie.client.version` |
| `2026-06-23 17:48:33` | `cowrie.client.kex` |
| `2026-06-23 17:48:34` | `cowrie.login.success` |
| `2026-06-23 17:48:35` | `cowrie.session.params` |
| `2026-06-23 17:48:35` | `cowrie.command.input` |
| `2026-06-23 17:48:35` | `cowrie.command.input` |
| `2026-06-23 17:48:35` | `cowrie.command.input` |
| `2026-06-23 17:48:35` | `cowrie.command.input` |
| `2026-06-23 17:48:35` | `cowrie.log.closed` |
| `2026-06-23 17:48:37` | `cowrie.session.params` |
| `2026-06-23 17:48:37` | `cowrie.command.input` |
| `2026-06-23 17:48:37` | `cowrie.command.input` |
| `2026-06-23 17:48:37` | `cowrie.command.failed` |
| `2026-06-23 17:48:37` | `cowrie.command.failed` |
| `2026-06-23 17:48:37` | `cowrie.command.failed` |
| `2026-06-23 17:48:37` | `cowrie.command.failed` |
| `2026-06-23 17:48:37` | `cowrie.log.closed` |
| `2026-06-23 17:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43026205e48a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:49 |
| **Last Seen** | 2026-06-23 17:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:49:11` | `cowrie.session.connect` |
| `2026-06-23 17:49:11` | `cowrie.client.version` |
| `2026-06-23 17:49:11` | `cowrie.client.kex` |
| `2026-06-23 17:49:11` | `cowrie.login.success` |
| `2026-06-23 17:49:12` | `cowrie.session.params` |
| `2026-06-23 17:49:12` | `cowrie.command.input` |
| `2026-06-23 17:49:12` | `cowrie.log.closed` |
| `2026-06-23 17:49:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83c8003fe10b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:49 |
| **Last Seen** | 2026-06-23 17:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:49:29` | `cowrie.session.connect` |
| `2026-06-23 17:49:29` | `cowrie.client.version` |
| `2026-06-23 17:49:29` | `cowrie.client.kex` |
| `2026-06-23 17:49:30` | `cowrie.login.success` |
| `2026-06-23 17:49:31` | `cowrie.session.params` |
| `2026-06-23 17:49:31` | `cowrie.command.input` |
| `2026-06-23 17:49:31` | `cowrie.command.input` |
| `2026-06-23 17:49:31` | `cowrie.command.input` |
| `2026-06-23 17:49:31` | `cowrie.command.input` |
| `2026-06-23 17:49:32` | `cowrie.log.closed` |
| `2026-06-23 17:49:33` | `cowrie.session.params` |
| `2026-06-23 17:49:33` | `cowrie.command.input` |
| `2026-06-23 17:49:33` | `cowrie.command.input` |
| `2026-06-23 17:49:33` | `cowrie.command.failed` |
| `2026-06-23 17:49:33` | `cowrie.command.failed` |
| `2026-06-23 17:49:33` | `cowrie.command.failed` |
| `2026-06-23 17:49:33` | `cowrie.command.failed` |
| `2026-06-23 17:49:33` | `cowrie.log.closed` |
| `2026-06-23 17:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ad66fc22ef2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:50 |
| **Last Seen** | 2026-06-23 17:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:50:03` | `cowrie.session.connect` |
| `2026-06-23 17:50:03` | `cowrie.client.version` |
| `2026-06-23 17:50:03` | `cowrie.client.kex` |
| `2026-06-23 17:50:04` | `cowrie.login.success` |
| `2026-06-23 17:50:04` | `cowrie.session.params` |
| `2026-06-23 17:50:04` | `cowrie.command.input` |
| `2026-06-23 17:50:04` | `cowrie.log.closed` |
| `2026-06-23 17:50:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eefd5c858ebf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:50 |
| **Last Seen** | 2026-06-23 17:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:50:26` | `cowrie.session.connect` |
| `2026-06-23 17:50:26` | `cowrie.client.version` |
| `2026-06-23 17:50:26` | `cowrie.client.kex` |
| `2026-06-23 17:50:27` | `cowrie.login.success` |
| `2026-06-23 17:50:29` | `cowrie.session.params` |
| `2026-06-23 17:50:29` | `cowrie.command.input` |
| `2026-06-23 17:50:29` | `cowrie.command.input` |
| `2026-06-23 17:50:29` | `cowrie.command.input` |
| `2026-06-23 17:50:29` | `cowrie.command.input` |
| `2026-06-23 17:50:29` | `cowrie.log.closed` |
| `2026-06-23 17:50:31` | `cowrie.session.params` |
| `2026-06-23 17:50:31` | `cowrie.command.input` |
| `2026-06-23 17:50:31` | `cowrie.command.input` |
| `2026-06-23 17:50:31` | `cowrie.command.failed` |
| `2026-06-23 17:50:31` | `cowrie.command.failed` |
| `2026-06-23 17:50:31` | `cowrie.command.failed` |
| `2026-06-23 17:50:31` | `cowrie.command.failed` |
| `2026-06-23 17:50:31` | `cowrie.log.closed` |
| `2026-06-23 17:50:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12f7f876a5ed

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 17:50 |
| **Last Seen** | 2026-06-23 17:50 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:50:27` | `cowrie.session.connect` |
| `2026-06-23 17:50:29` | `cowrie.client.version` |
| `2026-06-23 17:50:29` | `cowrie.client.kex` |
| `2026-06-23 17:50:35` | `cowrie.login.success` |
| `2026-06-23 17:50:39` | `cowrie.session.params` |
| `2026-06-23 17:50:39` | `cowrie.command.input` |
| `2026-06-23 17:50:41` | `cowrie.log.closed` |
| `2026-06-23 17:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba7ce2707486

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:50 |
| **Last Seen** | 2026-06-23 17:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:50:55` | `cowrie.session.connect` |
| `2026-06-23 17:50:55` | `cowrie.client.version` |
| `2026-06-23 17:50:55` | `cowrie.client.kex` |
| `2026-06-23 17:50:56` | `cowrie.login.success` |
| `2026-06-23 17:50:56` | `cowrie.session.params` |
| `2026-06-23 17:50:56` | `cowrie.command.input` |
| `2026-06-23 17:50:57` | `cowrie.log.closed` |
| `2026-06-23 17:50:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-391c0facb1bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:51 |
| **Last Seen** | 2026-06-23 17:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:51:24` | `cowrie.session.connect` |
| `2026-06-23 17:51:24` | `cowrie.client.version` |
| `2026-06-23 17:51:24` | `cowrie.client.kex` |
| `2026-06-23 17:51:26` | `cowrie.login.success` |
| `2026-06-23 17:51:27` | `cowrie.session.params` |
| `2026-06-23 17:51:27` | `cowrie.command.input` |
| `2026-06-23 17:51:27` | `cowrie.command.input` |
| `2026-06-23 17:51:27` | `cowrie.command.input` |
| `2026-06-23 17:51:27` | `cowrie.command.input` |
| `2026-06-23 17:51:27` | `cowrie.log.closed` |
| `2026-06-23 17:51:28` | `cowrie.session.params` |
| `2026-06-23 17:51:28` | `cowrie.command.input` |
| `2026-06-23 17:51:28` | `cowrie.command.input` |
| `2026-06-23 17:51:28` | `cowrie.command.failed` |
| `2026-06-23 17:51:28` | `cowrie.command.failed` |
| `2026-06-23 17:51:28` | `cowrie.command.failed` |
| `2026-06-23 17:51:28` | `cowrie.command.failed` |
| `2026-06-23 17:51:29` | `cowrie.log.closed` |
| `2026-06-23 17:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9fd562c2052

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:51 |
| **Last Seen** | 2026-06-23 17:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:51:49` | `cowrie.session.connect` |
| `2026-06-23 17:51:49` | `cowrie.client.version` |
| `2026-06-23 17:51:49` | `cowrie.client.kex` |
| `2026-06-23 17:51:49` | `cowrie.login.success` |
| `2026-06-23 17:51:50` | `cowrie.session.params` |
| `2026-06-23 17:51:50` | `cowrie.command.input` |
| `2026-06-23 17:51:50` | `cowrie.log.closed` |
| `2026-06-23 17:51:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3afc86be3718

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:52 |
| **Last Seen** | 2026-06-23 17:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123456' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:52:20` | `cowrie.session.connect` |
| `2026-06-23 17:52:20` | `cowrie.client.version` |
| `2026-06-23 17:52:20` | `cowrie.client.kex` |
| `2026-06-23 17:52:21` | `cowrie.login.success` |
| `2026-06-23 17:52:23` | `cowrie.session.params` |
| `2026-06-23 17:52:23` | `cowrie.command.input` |
| `2026-06-23 17:52:23` | `cowrie.command.input` |
| `2026-06-23 17:52:23` | `cowrie.command.input` |
| `2026-06-23 17:52:23` | `cowrie.command.input` |
| `2026-06-23 17:52:23` | `cowrie.log.closed` |
| `2026-06-23 17:52:24` | `cowrie.session.params` |
| `2026-06-23 17:52:24` | `cowrie.command.input` |
| `2026-06-23 17:52:24` | `cowrie.command.input` |
| `2026-06-23 17:52:24` | `cowrie.command.failed` |
| `2026-06-23 17:52:24` | `cowrie.command.failed` |
| `2026-06-23 17:52:24` | `cowrie.command.failed` |
| `2026-06-23 17:52:24` | `cowrie.command.failed` |
| `2026-06-23 17:52:24` | `cowrie.log.closed` |
| `2026-06-23 17:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aa7d49bb280

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:52 |
| **Last Seen** | 2026-06-23 17:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:52:45` | `cowrie.session.connect` |
| `2026-06-23 17:52:45` | `cowrie.client.version` |
| `2026-06-23 17:52:46` | `cowrie.client.kex` |
| `2026-06-23 17:52:46` | `cowrie.login.success` |
| `2026-06-23 17:52:47` | `cowrie.session.params` |
| `2026-06-23 17:52:47` | `cowrie.command.input` |
| `2026-06-23 17:52:47` | `cowrie.log.closed` |
| `2026-06-23 17:52:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccc41037e289

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:53 |
| **Last Seen** | 2026-06-23 17:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234567' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:53:18` | `cowrie.session.connect` |
| `2026-06-23 17:53:18` | `cowrie.client.version` |
| `2026-06-23 17:53:18` | `cowrie.client.kex` |
| `2026-06-23 17:53:19` | `cowrie.login.success` |
| `2026-06-23 17:53:20` | `cowrie.session.params` |
| `2026-06-23 17:53:20` | `cowrie.command.input` |
| `2026-06-23 17:53:20` | `cowrie.command.input` |
| `2026-06-23 17:53:20` | `cowrie.command.input` |
| `2026-06-23 17:53:20` | `cowrie.command.input` |
| `2026-06-23 17:53:21` | `cowrie.log.closed` |
| `2026-06-23 17:53:22` | `cowrie.session.params` |
| `2026-06-23 17:53:22` | `cowrie.command.input` |
| `2026-06-23 17:53:22` | `cowrie.command.input` |
| `2026-06-23 17:53:22` | `cowrie.command.failed` |
| `2026-06-23 17:53:22` | `cowrie.command.failed` |
| `2026-06-23 17:53:22` | `cowrie.command.failed` |
| `2026-06-23 17:53:22` | `cowrie.command.failed` |
| `2026-06-23 17:53:22` | `cowrie.log.closed` |
| `2026-06-23 17:53:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4d6fa0e5385

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:53 |
| **Last Seen** | 2026-06-23 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:53:45` | `cowrie.session.connect` |
| `2026-06-23 17:53:45` | `cowrie.client.version` |
| `2026-06-23 17:53:45` | `cowrie.client.kex` |
| `2026-06-23 17:53:46` | `cowrie.login.success` |
| `2026-06-23 17:53:47` | `cowrie.session.params` |
| `2026-06-23 17:53:47` | `cowrie.command.input` |
| `2026-06-23 17:53:47` | `cowrie.log.closed` |
| `2026-06-23 17:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-715711456f57

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:54 |
| **Last Seen** | 2026-06-23 17:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345678' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:54:16` | `cowrie.session.connect` |
| `2026-06-23 17:54:16` | `cowrie.client.version` |
| `2026-06-23 17:54:16` | `cowrie.client.kex` |
| `2026-06-23 17:54:18` | `cowrie.login.success` |
| `2026-06-23 17:54:19` | `cowrie.session.params` |
| `2026-06-23 17:54:19` | `cowrie.command.input` |
| `2026-06-23 17:54:19` | `cowrie.command.input` |
| `2026-06-23 17:54:19` | `cowrie.command.input` |
| `2026-06-23 17:54:19` | `cowrie.command.input` |
| `2026-06-23 17:54:19` | `cowrie.log.closed` |
| `2026-06-23 17:54:20` | `cowrie.session.params` |
| `2026-06-23 17:54:20` | `cowrie.command.input` |
| `2026-06-23 17:54:20` | `cowrie.command.input` |
| `2026-06-23 17:54:20` | `cowrie.command.failed` |
| `2026-06-23 17:54:20` | `cowrie.command.failed` |
| `2026-06-23 17:54:20` | `cowrie.command.failed` |
| `2026-06-23 17:54:20` | `cowrie.command.failed` |
| `2026-06-23 17:54:21` | `cowrie.log.closed` |
| `2026-06-23 17:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa7bb5adc308

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:54 |
| **Last Seen** | 2026-06-23 17:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:54:45` | `cowrie.session.connect` |
| `2026-06-23 17:54:45` | `cowrie.client.version` |
| `2026-06-23 17:54:45` | `cowrie.client.kex` |
| `2026-06-23 17:54:45` | `cowrie.login.success` |
| `2026-06-23 17:54:46` | `cowrie.session.params` |
| `2026-06-23 17:54:46` | `cowrie.command.input` |
| `2026-06-23 17:54:46` | `cowrie.log.closed` |
| `2026-06-23 17:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-548c8c432ecd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:55 |
| **Last Seen** | 2026-06-23 17:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123456789' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:55:13` | `cowrie.session.connect` |
| `2026-06-23 17:55:13` | `cowrie.client.version` |
| `2026-06-23 17:55:13` | `cowrie.client.kex` |
| `2026-06-23 17:55:15` | `cowrie.login.success` |
| `2026-06-23 17:55:16` | `cowrie.session.params` |
| `2026-06-23 17:55:16` | `cowrie.command.input` |
| `2026-06-23 17:55:16` | `cowrie.command.input` |
| `2026-06-23 17:55:16` | `cowrie.command.input` |
| `2026-06-23 17:55:16` | `cowrie.command.input` |
| `2026-06-23 17:55:16` | `cowrie.log.closed` |
| `2026-06-23 17:55:17` | `cowrie.session.params` |
| `2026-06-23 17:55:17` | `cowrie.command.input` |
| `2026-06-23 17:55:17` | `cowrie.command.input` |
| `2026-06-23 17:55:17` | `cowrie.command.failed` |
| `2026-06-23 17:55:17` | `cowrie.command.failed` |
| `2026-06-23 17:55:17` | `cowrie.command.failed` |
| `2026-06-23 17:55:17` | `cowrie.command.failed` |
| `2026-06-23 17:55:18` | `cowrie.log.closed` |
| `2026-06-23 17:55:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38455c148694

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:55 |
| **Last Seen** | 2026-06-23 17:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:55:43` | `cowrie.session.connect` |
| `2026-06-23 17:55:43` | `cowrie.client.version` |
| `2026-06-23 17:55:43` | `cowrie.client.kex` |
| `2026-06-23 17:55:43` | `cowrie.login.success` |
| `2026-06-23 17:55:44` | `cowrie.session.params` |
| `2026-06-23 17:55:44` | `cowrie.command.input` |
| `2026-06-23 17:55:44` | `cowrie.log.closed` |
| `2026-06-23 17:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22541736c11a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:56 |
| **Last Seen** | 2026-06-23 17:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234567890' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:56:09` | `cowrie.session.connect` |
| `2026-06-23 17:56:09` | `cowrie.client.version` |
| `2026-06-23 17:56:09` | `cowrie.client.kex` |
| `2026-06-23 17:56:10` | `cowrie.login.success` |
| `2026-06-23 17:56:11` | `cowrie.session.params` |
| `2026-06-23 17:56:11` | `cowrie.command.input` |
| `2026-06-23 17:56:11` | `cowrie.command.input` |
| `2026-06-23 17:56:11` | `cowrie.command.input` |
| `2026-06-23 17:56:11` | `cowrie.command.input` |
| `2026-06-23 17:56:11` | `cowrie.log.closed` |
| `2026-06-23 17:56:13` | `cowrie.session.params` |
| `2026-06-23 17:56:13` | `cowrie.command.input` |
| `2026-06-23 17:56:13` | `cowrie.command.input` |
| `2026-06-23 17:56:13` | `cowrie.command.failed` |
| `2026-06-23 17:56:13` | `cowrie.command.failed` |
| `2026-06-23 17:56:13` | `cowrie.command.failed` |
| `2026-06-23 17:56:13` | `cowrie.command.failed` |
| `2026-06-23 17:56:13` | `cowrie.log.closed` |
| `2026-06-23 17:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b11b29abf1ce

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:56 |
| **Last Seen** | 2026-06-23 17:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:56:39` | `cowrie.session.connect` |
| `2026-06-23 17:56:39` | `cowrie.client.version` |
| `2026-06-23 17:56:39` | `cowrie.client.kex` |
| `2026-06-23 17:56:40` | `cowrie.login.success` |
| `2026-06-23 17:56:40` | `cowrie.session.params` |
| `2026-06-23 17:56:40` | `cowrie.command.input` |
| `2026-06-23 17:56:41` | `cowrie.log.closed` |
| `2026-06-23 17:56:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c42102df2a4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:57 |
| **Last Seen** | 2026-06-23 17:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1q2w3e4r' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:57:04` | `cowrie.session.connect` |
| `2026-06-23 17:57:04` | `cowrie.client.version` |
| `2026-06-23 17:57:04` | `cowrie.client.kex` |
| `2026-06-23 17:57:06` | `cowrie.login.success` |
| `2026-06-23 17:57:07` | `cowrie.session.params` |
| `2026-06-23 17:57:07` | `cowrie.command.input` |
| `2026-06-23 17:57:07` | `cowrie.command.input` |
| `2026-06-23 17:57:07` | `cowrie.command.input` |
| `2026-06-23 17:57:07` | `cowrie.command.input` |
| `2026-06-23 17:57:07` | `cowrie.log.closed` |
| `2026-06-23 17:57:09` | `cowrie.session.params` |
| `2026-06-23 17:57:09` | `cowrie.command.input` |
| `2026-06-23 17:57:09` | `cowrie.command.input` |
| `2026-06-23 17:57:09` | `cowrie.command.failed` |
| `2026-06-23 17:57:09` | `cowrie.command.failed` |
| `2026-06-23 17:57:09` | `cowrie.command.failed` |
| `2026-06-23 17:57:09` | `cowrie.command.failed` |
| `2026-06-23 17:57:09` | `cowrie.log.closed` |
| `2026-06-23 17:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c53d4a3d016e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:57 |
| **Last Seen** | 2026-06-23 17:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:57:36` | `cowrie.session.connect` |
| `2026-06-23 17:57:36` | `cowrie.client.version` |
| `2026-06-23 17:57:36` | `cowrie.client.kex` |
| `2026-06-23 17:57:36` | `cowrie.login.success` |
| `2026-06-23 17:57:37` | `cowrie.session.params` |
| `2026-06-23 17:57:37` | `cowrie.command.input` |
| `2026-06-23 17:57:37` | `cowrie.log.closed` |
| `2026-06-23 17:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f1747ec44d1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:58 |
| **Last Seen** | 2026-06-23 17:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'abc123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:58:00` | `cowrie.session.connect` |
| `2026-06-23 17:58:00` | `cowrie.client.version` |
| `2026-06-23 17:58:00` | `cowrie.client.kex` |
| `2026-06-23 17:58:01` | `cowrie.login.success` |
| `2026-06-23 17:58:03` | `cowrie.session.params` |
| `2026-06-23 17:58:03` | `cowrie.command.input` |
| `2026-06-23 17:58:03` | `cowrie.command.input` |
| `2026-06-23 17:58:03` | `cowrie.command.input` |
| `2026-06-23 17:58:03` | `cowrie.command.input` |
| `2026-06-23 17:58:03` | `cowrie.log.closed` |
| `2026-06-23 17:58:04` | `cowrie.session.params` |
| `2026-06-23 17:58:04` | `cowrie.command.input` |
| `2026-06-23 17:58:04` | `cowrie.command.input` |
| `2026-06-23 17:58:04` | `cowrie.command.failed` |
| `2026-06-23 17:58:04` | `cowrie.command.failed` |
| `2026-06-23 17:58:04` | `cowrie.command.failed` |
| `2026-06-23 17:58:04` | `cowrie.command.failed` |
| `2026-06-23 17:58:05` | `cowrie.log.closed` |
| `2026-06-23 17:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb71ff0ab82c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:58 |
| **Last Seen** | 2026-06-23 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:58:41` | `cowrie.session.connect` |
| `2026-06-23 17:58:41` | `cowrie.client.version` |
| `2026-06-23 17:58:41` | `cowrie.client.kex` |
| `2026-06-23 17:58:41` | `cowrie.login.success` |
| `2026-06-23 17:58:42` | `cowrie.session.params` |
| `2026-06-23 17:58:42` | `cowrie.command.input` |
| `2026-06-23 17:58:42` | `cowrie.log.closed` |
| `2026-06-23 17:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7eebb4fbbdf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:58 |
| **Last Seen** | 2026-06-23 17:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'admin123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:58:56` | `cowrie.session.connect` |
| `2026-06-23 17:58:56` | `cowrie.client.version` |
| `2026-06-23 17:58:56` | `cowrie.client.kex` |
| `2026-06-23 17:58:57` | `cowrie.login.success` |
| `2026-06-23 17:58:59` | `cowrie.session.params` |
| `2026-06-23 17:58:59` | `cowrie.command.input` |
| `2026-06-23 17:58:59` | `cowrie.command.input` |
| `2026-06-23 17:58:59` | `cowrie.command.input` |
| `2026-06-23 17:58:59` | `cowrie.command.input` |
| `2026-06-23 17:58:59` | `cowrie.log.closed` |
| `2026-06-23 17:59:00` | `cowrie.session.params` |
| `2026-06-23 17:59:00` | `cowrie.command.input` |
| `2026-06-23 17:59:00` | `cowrie.command.input` |
| `2026-06-23 17:59:00` | `cowrie.command.failed` |
| `2026-06-23 17:59:00` | `cowrie.command.failed` |
| `2026-06-23 17:59:00` | `cowrie.command.failed` |
| `2026-06-23 17:59:00` | `cowrie.command.failed` |
| `2026-06-23 17:59:01` | `cowrie.log.closed` |
| `2026-06-23 17:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58692be17ef0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 17:59 |
| **Last Seen** | 2026-06-23 17:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:59:40` | `cowrie.session.connect` |
| `2026-06-23 17:59:40` | `cowrie.client.version` |
| `2026-06-23 17:59:40` | `cowrie.client.kex` |
| `2026-06-23 17:59:41` | `cowrie.login.success` |
| `2026-06-23 17:59:41` | `cowrie.session.params` |
| `2026-06-23 17:59:41` | `cowrie.command.input` |
| `2026-06-23 17:59:41` | `cowrie.log.closed` |
| `2026-06-23 17:59:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8bd50568499

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 17:59 |
| **Last Seen** | 2026-06-23 17:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 17:59:53` | `cowrie.session.connect` |
| `2026-06-23 17:59:53` | `cowrie.client.version` |
| `2026-06-23 17:59:53` | `cowrie.client.kex` |
| `2026-06-23 17:59:54` | `cowrie.login.success` |
| `2026-06-23 17:59:56` | `cowrie.session.params` |
| `2026-06-23 17:59:56` | `cowrie.command.input` |
| `2026-06-23 17:59:56` | `cowrie.command.input` |
| `2026-06-23 17:59:56` | `cowrie.command.input` |
| `2026-06-23 17:59:56` | `cowrie.command.input` |
| `2026-06-23 17:59:56` | `cowrie.log.closed` |
| `2026-06-23 17:59:57` | `cowrie.session.params` |
| `2026-06-23 17:59:57` | `cowrie.command.input` |
| `2026-06-23 17:59:57` | `cowrie.command.input` |
| `2026-06-23 17:59:57` | `cowrie.command.failed` |
| `2026-06-23 17:59:57` | `cowrie.command.failed` |
| `2026-06-23 17:59:57` | `cowrie.command.failed` |
| `2026-06-23 17:59:57` | `cowrie.command.failed` |
| `2026-06-23 17:59:57` | `cowrie.log.closed` |
| `2026-06-23 17:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4d2c1a173be

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:00 |
| **Last Seen** | 2026-06-23 18:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:00:34` | `cowrie.session.connect` |
| `2026-06-23 18:00:34` | `cowrie.client.version` |
| `2026-06-23 18:00:34` | `cowrie.client.kex` |
| `2026-06-23 18:00:34` | `cowrie.login.success` |
| `2026-06-23 18:00:35` | `cowrie.session.params` |
| `2026-06-23 18:00:35` | `cowrie.command.input` |
| `2026-06-23 18:00:35` | `cowrie.log.closed` |
| `2026-06-23 18:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fc8a3327fa0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-06-23 18:00 |
| **Last Seen** | 2026-06-23 18:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password1' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:00:48` | `cowrie.session.connect` |
| `2026-06-23 18:00:48` | `cowrie.client.version` |
| `2026-06-23 18:00:48` | `cowrie.client.kex` |
| `2026-06-23 18:00:49` | `cowrie.login.success` |
| `2026-06-23 18:00:50` | `cowrie.session.params` |
| `2026-06-23 18:00:50` | `cowrie.command.input` |
| `2026-06-23 18:00:50` | `cowrie.command.input` |
| `2026-06-23 18:00:50` | `cowrie.command.input` |
| `2026-06-23 18:00:50` | `cowrie.command.input` |
| `2026-06-23 18:00:51` | `cowrie.log.closed` |
| `2026-06-23 18:00:52` | `cowrie.session.params` |
| `2026-06-23 18:00:52` | `cowrie.command.input` |
| `2026-06-23 18:00:52` | `cowrie.command.input` |
| `2026-06-23 18:00:52` | `cowrie.command.failed` |
| `2026-06-23 18:00:52` | `cowrie.command.failed` |
| `2026-06-23 18:00:52` | `cowrie.command.failed` |
| `2026-06-23 18:00:52` | `cowrie.command.failed` |
| `2026-06-23 18:00:52` | `cowrie.log.closed` |
| `2026-06-23 18:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05a17ba3fb5e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:01 |
| **Last Seen** | 2026-06-23 18:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:01:17` | `cowrie.session.connect` |
| `2026-06-23 18:01:17` | `cowrie.client.version` |
| `2026-06-23 18:01:17` | `cowrie.client.kex` |
| `2026-06-23 18:01:17` | `cowrie.login.success` |
| `2026-06-23 18:01:18` | `cowrie.session.params` |
| `2026-06-23 18:01:18` | `cowrie.command.input` |
| `2026-06-23 18:01:18` | `cowrie.log.closed` |
| `2026-06-23 18:01:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02269714ea29

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:01 |
| **Last Seen** | 2026-06-23 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:01:59` | `cowrie.session.connect` |
| `2026-06-23 18:01:59` | `cowrie.client.version` |
| `2026-06-23 18:01:59` | `cowrie.client.kex` |
| `2026-06-23 18:02:00` | `cowrie.login.success` |
| `2026-06-23 18:02:00` | `cowrie.session.params` |
| `2026-06-23 18:02:00` | `cowrie.command.input` |
| `2026-06-23 18:02:01` | `cowrie.log.closed` |
| `2026-06-23 18:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95050feb59fe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:02 |
| **Last Seen** | 2026-06-23 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:02:42` | `cowrie.session.connect` |
| `2026-06-23 18:02:42` | `cowrie.client.version` |
| `2026-06-23 18:02:42` | `cowrie.client.kex` |
| `2026-06-23 18:02:43` | `cowrie.login.success` |
| `2026-06-23 18:02:43` | `cowrie.session.params` |
| `2026-06-23 18:02:43` | `cowrie.command.input` |
| `2026-06-23 18:02:43` | `cowrie.log.closed` |
| `2026-06-23 18:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3c2659ed909

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:03 |
| **Last Seen** | 2026-06-23 18:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:03:25` | `cowrie.session.connect` |
| `2026-06-23 18:03:25` | `cowrie.client.version` |
| `2026-06-23 18:03:25` | `cowrie.client.kex` |
| `2026-06-23 18:03:25` | `cowrie.login.success` |
| `2026-06-23 18:03:26` | `cowrie.session.params` |
| `2026-06-23 18:03:26` | `cowrie.command.input` |
| `2026-06-23 18:03:26` | `cowrie.log.closed` |
| `2026-06-23 18:03:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea1fce0556d0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:04 |
| **Last Seen** | 2026-06-23 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:04:07` | `cowrie.session.connect` |
| `2026-06-23 18:04:07` | `cowrie.client.version` |
| `2026-06-23 18:04:07` | `cowrie.client.kex` |
| `2026-06-23 18:04:08` | `cowrie.login.success` |
| `2026-06-23 18:04:08` | `cowrie.session.params` |
| `2026-06-23 18:04:08` | `cowrie.command.input` |
| `2026-06-23 18:04:09` | `cowrie.log.closed` |
| `2026-06-23 18:04:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5e5ea9c664f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 18:04 |
| **Last Seen** | 2026-06-23 18:04 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:04:41` | `cowrie.session.connect` |
| `2026-06-23 18:04:42` | `cowrie.client.version` |
| `2026-06-23 18:04:42` | `cowrie.client.kex` |
| `2026-06-23 18:04:49` | `cowrie.login.success` |
| `2026-06-23 18:04:52` | `cowrie.session.params` |
| `2026-06-23 18:04:52` | `cowrie.command.input` |
| `2026-06-23 18:04:54` | `cowrie.log.closed` |
| `2026-06-23 18:04:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e33f6a5964e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:04 |
| **Last Seen** | 2026-06-23 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:04:53` | `cowrie.session.connect` |
| `2026-06-23 18:04:53` | `cowrie.client.version` |
| `2026-06-23 18:04:53` | `cowrie.client.kex` |
| `2026-06-23 18:04:53` | `cowrie.login.success` |
| `2026-06-23 18:04:54` | `cowrie.session.params` |
| `2026-06-23 18:04:54` | `cowrie.command.input` |
| `2026-06-23 18:04:54` | `cowrie.log.closed` |
| `2026-06-23 18:04:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31cd9e2138b8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:05 |
| **Last Seen** | 2026-06-23 18:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:05:40` | `cowrie.session.connect` |
| `2026-06-23 18:05:40` | `cowrie.client.version` |
| `2026-06-23 18:05:40` | `cowrie.client.kex` |
| `2026-06-23 18:05:40` | `cowrie.login.success` |
| `2026-06-23 18:05:41` | `cowrie.session.params` |
| `2026-06-23 18:05:41` | `cowrie.command.input` |
| `2026-06-23 18:05:41` | `cowrie.log.closed` |
| `2026-06-23 18:05:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a4172aa5bef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:06 |
| **Last Seen** | 2026-06-23 18:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:06:26` | `cowrie.session.connect` |
| `2026-06-23 18:06:26` | `cowrie.client.version` |
| `2026-06-23 18:06:26` | `cowrie.client.kex` |
| `2026-06-23 18:06:26` | `cowrie.login.success` |
| `2026-06-23 18:06:27` | `cowrie.session.params` |
| `2026-06-23 18:06:27` | `cowrie.command.input` |
| `2026-06-23 18:06:27` | `cowrie.log.closed` |
| `2026-06-23 18:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2ff95f90eea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:07 |
| **Last Seen** | 2026-06-23 18:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:07:12` | `cowrie.session.connect` |
| `2026-06-23 18:07:12` | `cowrie.client.version` |
| `2026-06-23 18:07:12` | `cowrie.client.kex` |
| `2026-06-23 18:07:12` | `cowrie.login.success` |
| `2026-06-23 18:07:13` | `cowrie.session.params` |
| `2026-06-23 18:07:13` | `cowrie.command.input` |
| `2026-06-23 18:07:13` | `cowrie.log.closed` |
| `2026-06-23 18:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67680b558ba6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:07 |
| **Last Seen** | 2026-06-23 18:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:07:57` | `cowrie.session.connect` |
| `2026-06-23 18:07:57` | `cowrie.client.version` |
| `2026-06-23 18:07:57` | `cowrie.client.kex` |
| `2026-06-23 18:07:57` | `cowrie.login.success` |
| `2026-06-23 18:07:58` | `cowrie.session.params` |
| `2026-06-23 18:07:58` | `cowrie.command.input` |
| `2026-06-23 18:07:58` | `cowrie.log.closed` |
| `2026-06-23 18:07:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00ccb4625abb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:08 |
| **Last Seen** | 2026-06-23 18:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:08:40` | `cowrie.session.connect` |
| `2026-06-23 18:08:40` | `cowrie.client.version` |
| `2026-06-23 18:08:41` | `cowrie.client.kex` |
| `2026-06-23 18:08:41` | `cowrie.login.success` |
| `2026-06-23 18:08:42` | `cowrie.session.params` |
| `2026-06-23 18:08:42` | `cowrie.command.input` |
| `2026-06-23 18:08:42` | `cowrie.log.closed` |
| `2026-06-23 18:08:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dbab81bd597

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:09 |
| **Last Seen** | 2026-06-23 18:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:09:24` | `cowrie.session.connect` |
| `2026-06-23 18:09:24` | `cowrie.client.version` |
| `2026-06-23 18:09:24` | `cowrie.client.kex` |
| `2026-06-23 18:09:25` | `cowrie.login.success` |
| `2026-06-23 18:09:26` | `cowrie.session.params` |
| `2026-06-23 18:09:26` | `cowrie.command.input` |
| `2026-06-23 18:09:26` | `cowrie.log.closed` |
| `2026-06-23 18:09:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d48d1796945f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:10 |
| **Last Seen** | 2026-06-23 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:10:08` | `cowrie.session.connect` |
| `2026-06-23 18:10:08` | `cowrie.client.version` |
| `2026-06-23 18:10:08` | `cowrie.client.kex` |
| `2026-06-23 18:10:08` | `cowrie.login.success` |
| `2026-06-23 18:10:09` | `cowrie.session.params` |
| `2026-06-23 18:10:09` | `cowrie.command.input` |
| `2026-06-23 18:10:09` | `cowrie.log.closed` |
| `2026-06-23 18:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e7b7d8fe45a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:10 |
| **Last Seen** | 2026-06-23 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:10:54` | `cowrie.session.connect` |
| `2026-06-23 18:10:54` | `cowrie.client.version` |
| `2026-06-23 18:10:54` | `cowrie.client.kex` |
| `2026-06-23 18:10:54` | `cowrie.login.success` |
| `2026-06-23 18:10:55` | `cowrie.session.params` |
| `2026-06-23 18:10:55` | `cowrie.command.input` |
| `2026-06-23 18:10:55` | `cowrie.log.closed` |
| `2026-06-23 18:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebbd09492378

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:11 |
| **Last Seen** | 2026-06-23 18:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:11:39` | `cowrie.session.connect` |
| `2026-06-23 18:11:39` | `cowrie.client.version` |
| `2026-06-23 18:11:39` | `cowrie.client.kex` |
| `2026-06-23 18:11:39` | `cowrie.login.success` |
| `2026-06-23 18:11:40` | `cowrie.session.params` |
| `2026-06-23 18:11:40` | `cowrie.command.input` |
| `2026-06-23 18:11:40` | `cowrie.log.closed` |
| `2026-06-23 18:11:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e63c426f698a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:12 |
| **Last Seen** | 2026-06-23 18:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:12:23` | `cowrie.session.connect` |
| `2026-06-23 18:12:23` | `cowrie.client.version` |
| `2026-06-23 18:12:23` | `cowrie.client.kex` |
| `2026-06-23 18:12:24` | `cowrie.login.success` |
| `2026-06-23 18:12:24` | `cowrie.session.params` |
| `2026-06-23 18:12:24` | `cowrie.command.input` |
| `2026-06-23 18:12:24` | `cowrie.log.closed` |
| `2026-06-23 18:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b85e4a870838

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:13 |
| **Last Seen** | 2026-06-23 18:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:13:09` | `cowrie.session.connect` |
| `2026-06-23 18:13:09` | `cowrie.client.version` |
| `2026-06-23 18:13:09` | `cowrie.client.kex` |
| `2026-06-23 18:13:10` | `cowrie.login.success` |
| `2026-06-23 18:13:11` | `cowrie.session.params` |
| `2026-06-23 18:13:11` | `cowrie.command.input` |
| `2026-06-23 18:13:11` | `cowrie.log.closed` |
| `2026-06-23 18:13:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e980f39b13e5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:13 |
| **Last Seen** | 2026-06-23 18:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:13:52` | `cowrie.session.connect` |
| `2026-06-23 18:13:52` | `cowrie.client.version` |
| `2026-06-23 18:13:53` | `cowrie.client.kex` |
| `2026-06-23 18:13:53` | `cowrie.login.success` |
| `2026-06-23 18:13:54` | `cowrie.session.params` |
| `2026-06-23 18:13:54` | `cowrie.command.input` |
| `2026-06-23 18:13:54` | `cowrie.log.closed` |
| `2026-06-23 18:13:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63c1d2435547

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:14 |
| **Last Seen** | 2026-06-23 18:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:14:36` | `cowrie.session.connect` |
| `2026-06-23 18:14:36` | `cowrie.client.version` |
| `2026-06-23 18:14:36` | `cowrie.client.kex` |
| `2026-06-23 18:14:36` | `cowrie.login.success` |
| `2026-06-23 18:14:37` | `cowrie.session.params` |
| `2026-06-23 18:14:37` | `cowrie.command.input` |
| `2026-06-23 18:14:37` | `cowrie.log.closed` |
| `2026-06-23 18:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41741fe32842

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:15 |
| **Last Seen** | 2026-06-23 18:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:15:18` | `cowrie.session.connect` |
| `2026-06-23 18:15:18` | `cowrie.client.version` |
| `2026-06-23 18:15:18` | `cowrie.client.kex` |
| `2026-06-23 18:15:19` | `cowrie.login.success` |
| `2026-06-23 18:15:20` | `cowrie.session.params` |
| `2026-06-23 18:15:20` | `cowrie.command.input` |
| `2026-06-23 18:15:20` | `cowrie.log.closed` |
| `2026-06-23 18:15:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95e238141e98

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:16 |
| **Last Seen** | 2026-06-23 18:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:16:01` | `cowrie.session.connect` |
| `2026-06-23 18:16:01` | `cowrie.client.version` |
| `2026-06-23 18:16:01` | `cowrie.client.kex` |
| `2026-06-23 18:16:02` | `cowrie.login.success` |
| `2026-06-23 18:16:02` | `cowrie.session.params` |
| `2026-06-23 18:16:02` | `cowrie.command.input` |
| `2026-06-23 18:16:02` | `cowrie.log.closed` |
| `2026-06-23 18:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e42f032461e3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:16 |
| **Last Seen** | 2026-06-23 18:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:16:44` | `cowrie.session.connect` |
| `2026-06-23 18:16:44` | `cowrie.client.version` |
| `2026-06-23 18:16:45` | `cowrie.client.kex` |
| `2026-06-23 18:16:45` | `cowrie.login.success` |
| `2026-06-23 18:16:46` | `cowrie.session.params` |
| `2026-06-23 18:16:46` | `cowrie.command.input` |
| `2026-06-23 18:16:46` | `cowrie.log.closed` |
| `2026-06-23 18:16:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f7ff3aa3941

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:17 |
| **Last Seen** | 2026-06-23 18:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:17:30` | `cowrie.session.connect` |
| `2026-06-23 18:17:30` | `cowrie.client.version` |
| `2026-06-23 18:17:30` | `cowrie.client.kex` |
| `2026-06-23 18:17:30` | `cowrie.login.success` |
| `2026-06-23 18:17:31` | `cowrie.session.params` |
| `2026-06-23 18:17:31` | `cowrie.command.input` |
| `2026-06-23 18:17:31` | `cowrie.log.closed` |
| `2026-06-23 18:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02c8383137be

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:18 |
| **Last Seen** | 2026-06-23 18:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:18:16` | `cowrie.session.connect` |
| `2026-06-23 18:18:16` | `cowrie.client.version` |
| `2026-06-23 18:18:16` | `cowrie.client.kex` |
| `2026-06-23 18:18:17` | `cowrie.login.success` |
| `2026-06-23 18:18:18` | `cowrie.session.params` |
| `2026-06-23 18:18:18` | `cowrie.command.input` |
| `2026-06-23 18:18:18` | `cowrie.log.closed` |
| `2026-06-23 18:18:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d667aa40e26c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:19 |
| **Last Seen** | 2026-06-23 18:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:19:02` | `cowrie.session.connect` |
| `2026-06-23 18:19:02` | `cowrie.client.version` |
| `2026-06-23 18:19:02` | `cowrie.client.kex` |
| `2026-06-23 18:19:03` | `cowrie.login.success` |
| `2026-06-23 18:19:03` | `cowrie.session.params` |
| `2026-06-23 18:19:03` | `cowrie.command.input` |
| `2026-06-23 18:19:04` | `cowrie.log.closed` |
| `2026-06-23 18:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7910db762d6

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 18:19 |
| **Last Seen** | 2026-06-23 18:19 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:19:03` | `cowrie.session.connect` |
| `2026-06-23 18:19:05` | `cowrie.client.version` |
| `2026-06-23 18:19:05` | `cowrie.client.kex` |
| `2026-06-23 18:19:10` | `cowrie.login.success` |
| `2026-06-23 18:19:15` | `cowrie.session.params` |
| `2026-06-23 18:19:15` | `cowrie.command.input` |
| `2026-06-23 18:19:16` | `cowrie.log.closed` |
| `2026-06-23 18:19:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4df34076bfcb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:19 |
| **Last Seen** | 2026-06-23 18:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:19:51` | `cowrie.session.connect` |
| `2026-06-23 18:19:51` | `cowrie.client.version` |
| `2026-06-23 18:19:51` | `cowrie.client.kex` |
| `2026-06-23 18:19:51` | `cowrie.login.success` |
| `2026-06-23 18:19:52` | `cowrie.session.params` |
| `2026-06-23 18:19:52` | `cowrie.command.input` |
| `2026-06-23 18:19:52` | `cowrie.log.closed` |
| `2026-06-23 18:19:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0af8b2a67ff1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:20 |
| **Last Seen** | 2026-06-23 18:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:20:37` | `cowrie.session.connect` |
| `2026-06-23 18:20:37` | `cowrie.client.version` |
| `2026-06-23 18:20:37` | `cowrie.client.kex` |
| `2026-06-23 18:20:37` | `cowrie.login.success` |
| `2026-06-23 18:20:38` | `cowrie.session.params` |
| `2026-06-23 18:20:38` | `cowrie.command.input` |
| `2026-06-23 18:20:38` | `cowrie.log.closed` |
| `2026-06-23 18:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-244da7178eaa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:21 |
| **Last Seen** | 2026-06-23 18:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:21:22` | `cowrie.session.connect` |
| `2026-06-23 18:21:22` | `cowrie.client.version` |
| `2026-06-23 18:21:22` | `cowrie.client.kex` |
| `2026-06-23 18:21:22` | `cowrie.login.success` |
| `2026-06-23 18:21:23` | `cowrie.session.params` |
| `2026-06-23 18:21:23` | `cowrie.command.input` |
| `2026-06-23 18:21:23` | `cowrie.log.closed` |
| `2026-06-23 18:21:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4256ced8c5f6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:22 |
| **Last Seen** | 2026-06-23 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:22:07` | `cowrie.session.connect` |
| `2026-06-23 18:22:07` | `cowrie.client.version` |
| `2026-06-23 18:22:07` | `cowrie.client.kex` |
| `2026-06-23 18:22:07` | `cowrie.login.success` |
| `2026-06-23 18:22:08` | `cowrie.session.params` |
| `2026-06-23 18:22:08` | `cowrie.command.input` |
| `2026-06-23 18:22:08` | `cowrie.log.closed` |
| `2026-06-23 18:22:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9518320a3951

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:22 |
| **Last Seen** | 2026-06-23 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:22:51` | `cowrie.session.connect` |
| `2026-06-23 18:22:51` | `cowrie.client.version` |
| `2026-06-23 18:22:51` | `cowrie.client.kex` |
| `2026-06-23 18:22:51` | `cowrie.login.success` |
| `2026-06-23 18:22:52` | `cowrie.session.params` |
| `2026-06-23 18:22:52` | `cowrie.command.input` |
| `2026-06-23 18:22:52` | `cowrie.log.closed` |
| `2026-06-23 18:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-531d8b87c274

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:23 |
| **Last Seen** | 2026-06-23 18:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:23:34` | `cowrie.session.connect` |
| `2026-06-23 18:23:34` | `cowrie.client.version` |
| `2026-06-23 18:23:35` | `cowrie.client.kex` |
| `2026-06-23 18:23:35` | `cowrie.login.success` |
| `2026-06-23 18:23:36` | `cowrie.session.params` |
| `2026-06-23 18:23:36` | `cowrie.command.input` |
| `2026-06-23 18:23:36` | `cowrie.log.closed` |
| `2026-06-23 18:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37c2c04f85ed

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:24 |
| **Last Seen** | 2026-06-23 18:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:24:19` | `cowrie.session.connect` |
| `2026-06-23 18:24:19` | `cowrie.client.version` |
| `2026-06-23 18:24:19` | `cowrie.client.kex` |
| `2026-06-23 18:24:20` | `cowrie.login.success` |
| `2026-06-23 18:24:20` | `cowrie.session.params` |
| `2026-06-23 18:24:20` | `cowrie.command.input` |
| `2026-06-23 18:24:21` | `cowrie.log.closed` |
| `2026-06-23 18:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b90c276bb1e8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:25 |
| **Last Seen** | 2026-06-23 18:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:25:06` | `cowrie.session.connect` |
| `2026-06-23 18:25:06` | `cowrie.client.version` |
| `2026-06-23 18:25:06` | `cowrie.client.kex` |
| `2026-06-23 18:25:07` | `cowrie.login.success` |
| `2026-06-23 18:25:07` | `cowrie.session.params` |
| `2026-06-23 18:25:07` | `cowrie.command.input` |
| `2026-06-23 18:25:07` | `cowrie.log.closed` |
| `2026-06-23 18:25:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c8ce2a8e7cc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:25 |
| **Last Seen** | 2026-06-23 18:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:25:51` | `cowrie.session.connect` |
| `2026-06-23 18:25:51` | `cowrie.client.version` |
| `2026-06-23 18:25:51` | `cowrie.client.kex` |
| `2026-06-23 18:25:52` | `cowrie.login.success` |
| `2026-06-23 18:25:52` | `cowrie.session.params` |
| `2026-06-23 18:25:52` | `cowrie.command.input` |
| `2026-06-23 18:25:53` | `cowrie.log.closed` |
| `2026-06-23 18:25:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85f171201ba9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:26 |
| **Last Seen** | 2026-06-23 18:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:26:35` | `cowrie.session.connect` |
| `2026-06-23 18:26:35` | `cowrie.client.version` |
| `2026-06-23 18:26:35` | `cowrie.client.kex` |
| `2026-06-23 18:26:36` | `cowrie.login.success` |
| `2026-06-23 18:26:37` | `cowrie.session.params` |
| `2026-06-23 18:26:37` | `cowrie.command.input` |
| `2026-06-23 18:26:37` | `cowrie.log.closed` |
| `2026-06-23 18:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ca6b71dcda8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:27 |
| **Last Seen** | 2026-06-23 18:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:27:19` | `cowrie.session.connect` |
| `2026-06-23 18:27:19` | `cowrie.client.version` |
| `2026-06-23 18:27:19` | `cowrie.client.kex` |
| `2026-06-23 18:27:20` | `cowrie.login.success` |
| `2026-06-23 18:27:20` | `cowrie.session.params` |
| `2026-06-23 18:27:20` | `cowrie.command.input` |
| `2026-06-23 18:27:20` | `cowrie.log.closed` |
| `2026-06-23 18:27:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee3cb8d8ae7a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:28 |
| **Last Seen** | 2026-06-23 18:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:28:04` | `cowrie.session.connect` |
| `2026-06-23 18:28:04` | `cowrie.client.version` |
| `2026-06-23 18:28:04` | `cowrie.client.kex` |
| `2026-06-23 18:28:04` | `cowrie.login.success` |
| `2026-06-23 18:28:05` | `cowrie.session.params` |
| `2026-06-23 18:28:05` | `cowrie.command.input` |
| `2026-06-23 18:28:05` | `cowrie.log.closed` |
| `2026-06-23 18:28:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-576bca70d865

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:28 |
| **Last Seen** | 2026-06-23 18:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:28:49` | `cowrie.session.connect` |
| `2026-06-23 18:28:49` | `cowrie.client.version` |
| `2026-06-23 18:28:50` | `cowrie.client.kex` |
| `2026-06-23 18:28:50` | `cowrie.login.success` |
| `2026-06-23 18:28:51` | `cowrie.session.params` |
| `2026-06-23 18:28:51` | `cowrie.command.input` |
| `2026-06-23 18:28:51` | `cowrie.log.closed` |
| `2026-06-23 18:28:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bf995fa1a34

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:29 |
| **Last Seen** | 2026-06-23 18:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:29:33` | `cowrie.session.connect` |
| `2026-06-23 18:29:33` | `cowrie.client.version` |
| `2026-06-23 18:29:33` | `cowrie.client.kex` |
| `2026-06-23 18:29:34` | `cowrie.login.success` |
| `2026-06-23 18:29:34` | `cowrie.session.params` |
| `2026-06-23 18:29:34` | `cowrie.command.input` |
| `2026-06-23 18:29:35` | `cowrie.log.closed` |
| `2026-06-23 18:29:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ee40f0c8ea5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:30 |
| **Last Seen** | 2026-06-23 18:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:30:18` | `cowrie.session.connect` |
| `2026-06-23 18:30:18` | `cowrie.client.version` |
| `2026-06-23 18:30:18` | `cowrie.client.kex` |
| `2026-06-23 18:30:19` | `cowrie.login.success` |
| `2026-06-23 18:30:20` | `cowrie.session.params` |
| `2026-06-23 18:30:20` | `cowrie.command.input` |
| `2026-06-23 18:30:20` | `cowrie.log.closed` |
| `2026-06-23 18:30:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19ea55ac99d3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:31 |
| **Last Seen** | 2026-06-23 18:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:31:05` | `cowrie.session.connect` |
| `2026-06-23 18:31:05` | `cowrie.client.version` |
| `2026-06-23 18:31:05` | `cowrie.client.kex` |
| `2026-06-23 18:31:05` | `cowrie.login.success` |
| `2026-06-23 18:31:06` | `cowrie.session.params` |
| `2026-06-23 18:31:06` | `cowrie.command.input` |
| `2026-06-23 18:31:06` | `cowrie.log.closed` |
| `2026-06-23 18:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a7a30e28a5e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:31 |
| **Last Seen** | 2026-06-23 18:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:31:51` | `cowrie.session.connect` |
| `2026-06-23 18:31:51` | `cowrie.client.version` |
| `2026-06-23 18:31:51` | `cowrie.client.kex` |
| `2026-06-23 18:31:52` | `cowrie.login.success` |
| `2026-06-23 18:31:53` | `cowrie.session.params` |
| `2026-06-23 18:31:53` | `cowrie.command.input` |
| `2026-06-23 18:31:53` | `cowrie.log.closed` |
| `2026-06-23 18:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f3ecf52868b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:32 |
| **Last Seen** | 2026-06-23 18:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:32:39` | `cowrie.session.connect` |
| `2026-06-23 18:32:39` | `cowrie.client.version` |
| `2026-06-23 18:32:39` | `cowrie.client.kex` |
| `2026-06-23 18:32:39` | `cowrie.login.success` |
| `2026-06-23 18:32:40` | `cowrie.session.params` |
| `2026-06-23 18:32:40` | `cowrie.command.input` |
| `2026-06-23 18:32:40` | `cowrie.log.closed` |
| `2026-06-23 18:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09b111f5b704

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 18:33 |
| **Last Seen** | 2026-06-23 18:33 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:33:24` | `cowrie.session.connect` |
| `2026-06-23 18:33:25` | `cowrie.client.version` |
| `2026-06-23 18:33:25` | `cowrie.client.kex` |
| `2026-06-23 18:33:32` | `cowrie.login.success` |
| `2026-06-23 18:33:35` | `cowrie.session.params` |
| `2026-06-23 18:33:35` | `cowrie.command.input` |
| `2026-06-23 18:33:37` | `cowrie.log.closed` |
| `2026-06-23 18:33:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-515813c2fad1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:33 |
| **Last Seen** | 2026-06-23 18:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:33:26` | `cowrie.session.connect` |
| `2026-06-23 18:33:26` | `cowrie.client.version` |
| `2026-06-23 18:33:26` | `cowrie.client.kex` |
| `2026-06-23 18:33:26` | `cowrie.login.success` |
| `2026-06-23 18:33:27` | `cowrie.session.params` |
| `2026-06-23 18:33:27` | `cowrie.command.input` |
| `2026-06-23 18:33:27` | `cowrie.log.closed` |
| `2026-06-23 18:33:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bed3c7893769

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:34 |
| **Last Seen** | 2026-06-23 18:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:34:12` | `cowrie.session.connect` |
| `2026-06-23 18:34:12` | `cowrie.client.version` |
| `2026-06-23 18:34:12` | `cowrie.client.kex` |
| `2026-06-23 18:34:13` | `cowrie.login.success` |
| `2026-06-23 18:34:14` | `cowrie.session.params` |
| `2026-06-23 18:34:14` | `cowrie.command.input` |
| `2026-06-23 18:34:14` | `cowrie.log.closed` |
| `2026-06-23 18:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa035ebd2e46

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:34 |
| **Last Seen** | 2026-06-23 18:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:34:59` | `cowrie.session.connect` |
| `2026-06-23 18:34:59` | `cowrie.client.version` |
| `2026-06-23 18:34:59` | `cowrie.client.kex` |
| `2026-06-23 18:34:59` | `cowrie.login.success` |
| `2026-06-23 18:35:00` | `cowrie.session.params` |
| `2026-06-23 18:35:00` | `cowrie.command.input` |
| `2026-06-23 18:35:00` | `cowrie.log.closed` |
| `2026-06-23 18:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f786db80be70

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:35 |
| **Last Seen** | 2026-06-23 18:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:35:46` | `cowrie.session.connect` |
| `2026-06-23 18:35:46` | `cowrie.client.version` |
| `2026-06-23 18:35:46` | `cowrie.client.kex` |
| `2026-06-23 18:35:47` | `cowrie.login.success` |
| `2026-06-23 18:35:48` | `cowrie.session.params` |
| `2026-06-23 18:35:48` | `cowrie.command.input` |
| `2026-06-23 18:35:48` | `cowrie.log.closed` |
| `2026-06-23 18:35:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4bd7f03f4ea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:36 |
| **Last Seen** | 2026-06-23 18:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:36:35` | `cowrie.session.connect` |
| `2026-06-23 18:36:35` | `cowrie.client.version` |
| `2026-06-23 18:36:35` | `cowrie.client.kex` |
| `2026-06-23 18:36:36` | `cowrie.login.success` |
| `2026-06-23 18:36:36` | `cowrie.session.params` |
| `2026-06-23 18:36:36` | `cowrie.command.input` |
| `2026-06-23 18:36:36` | `cowrie.log.closed` |
| `2026-06-23 18:36:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-344394a70606

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:37 |
| **Last Seen** | 2026-06-23 18:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:37:24` | `cowrie.session.connect` |
| `2026-06-23 18:37:24` | `cowrie.client.version` |
| `2026-06-23 18:37:24` | `cowrie.client.kex` |
| `2026-06-23 18:37:25` | `cowrie.login.success` |
| `2026-06-23 18:37:26` | `cowrie.session.params` |
| `2026-06-23 18:37:26` | `cowrie.command.input` |
| `2026-06-23 18:37:26` | `cowrie.log.closed` |
| `2026-06-23 18:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ee30a2644ca

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:38 |
| **Last Seen** | 2026-06-23 18:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:38:13` | `cowrie.session.connect` |
| `2026-06-23 18:38:13` | `cowrie.client.version` |
| `2026-06-23 18:38:13` | `cowrie.client.kex` |
| `2026-06-23 18:38:14` | `cowrie.login.success` |
| `2026-06-23 18:38:15` | `cowrie.session.params` |
| `2026-06-23 18:38:15` | `cowrie.command.input` |
| `2026-06-23 18:38:15` | `cowrie.log.closed` |
| `2026-06-23 18:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37d00fbc3b1f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:39 |
| **Last Seen** | 2026-06-23 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:39:02` | `cowrie.session.connect` |
| `2026-06-23 18:39:02` | `cowrie.client.version` |
| `2026-06-23 18:39:02` | `cowrie.client.kex` |
| `2026-06-23 18:39:02` | `cowrie.login.success` |
| `2026-06-23 18:39:03` | `cowrie.session.params` |
| `2026-06-23 18:39:03` | `cowrie.command.input` |
| `2026-06-23 18:39:03` | `cowrie.log.closed` |
| `2026-06-23 18:39:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-046cd1aa8378

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:39 |
| **Last Seen** | 2026-06-23 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:39:50` | `cowrie.session.connect` |
| `2026-06-23 18:39:50` | `cowrie.client.version` |
| `2026-06-23 18:39:50` | `cowrie.client.kex` |
| `2026-06-23 18:39:50` | `cowrie.login.success` |
| `2026-06-23 18:39:51` | `cowrie.session.params` |
| `2026-06-23 18:39:51` | `cowrie.command.input` |
| `2026-06-23 18:39:51` | `cowrie.log.closed` |
| `2026-06-23 18:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64dd2fb5587d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:40 |
| **Last Seen** | 2026-06-23 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:40:37` | `cowrie.session.connect` |
| `2026-06-23 18:40:37` | `cowrie.client.version` |
| `2026-06-23 18:40:37` | `cowrie.client.kex` |
| `2026-06-23 18:40:38` | `cowrie.login.success` |
| `2026-06-23 18:40:39` | `cowrie.session.params` |
| `2026-06-23 18:40:39` | `cowrie.command.input` |
| `2026-06-23 18:40:39` | `cowrie.log.closed` |
| `2026-06-23 18:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cb03c721191

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:41 |
| **Last Seen** | 2026-06-23 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:41:24` | `cowrie.session.connect` |
| `2026-06-23 18:41:24` | `cowrie.client.version` |
| `2026-06-23 18:41:24` | `cowrie.client.kex` |
| `2026-06-23 18:41:25` | `cowrie.login.success` |
| `2026-06-23 18:41:25` | `cowrie.session.params` |
| `2026-06-23 18:41:25` | `cowrie.command.input` |
| `2026-06-23 18:41:25` | `cowrie.log.closed` |
| `2026-06-23 18:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9239fc9728bb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:42 |
| **Last Seen** | 2026-06-23 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:42:11` | `cowrie.session.connect` |
| `2026-06-23 18:42:11` | `cowrie.client.version` |
| `2026-06-23 18:42:11` | `cowrie.client.kex` |
| `2026-06-23 18:42:12` | `cowrie.login.success` |
| `2026-06-23 18:42:12` | `cowrie.session.params` |
| `2026-06-23 18:42:12` | `cowrie.command.input` |
| `2026-06-23 18:42:13` | `cowrie.log.closed` |
| `2026-06-23 18:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adb3b85fd708

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:43 |
| **Last Seen** | 2026-06-23 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:43:00` | `cowrie.session.connect` |
| `2026-06-23 18:43:00` | `cowrie.client.version` |
| `2026-06-23 18:43:00` | `cowrie.client.kex` |
| `2026-06-23 18:43:00` | `cowrie.login.success` |
| `2026-06-23 18:43:01` | `cowrie.session.params` |
| `2026-06-23 18:43:01` | `cowrie.command.input` |
| `2026-06-23 18:43:01` | `cowrie.log.closed` |
| `2026-06-23 18:43:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f950c0d105a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:43 |
| **Last Seen** | 2026-06-23 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:43:49` | `cowrie.session.connect` |
| `2026-06-23 18:43:49` | `cowrie.client.version` |
| `2026-06-23 18:43:49` | `cowrie.client.kex` |
| `2026-06-23 18:43:49` | `cowrie.login.success` |
| `2026-06-23 18:43:50` | `cowrie.session.params` |
| `2026-06-23 18:43:50` | `cowrie.command.input` |
| `2026-06-23 18:43:50` | `cowrie.log.closed` |
| `2026-06-23 18:43:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5b2ca185e13

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:44 |
| **Last Seen** | 2026-06-23 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:44:38` | `cowrie.session.connect` |
| `2026-06-23 18:44:38` | `cowrie.client.version` |
| `2026-06-23 18:44:39` | `cowrie.client.kex` |
| `2026-06-23 18:44:39` | `cowrie.login.success` |
| `2026-06-23 18:44:40` | `cowrie.session.params` |
| `2026-06-23 18:44:40` | `cowrie.command.input` |
| `2026-06-23 18:44:40` | `cowrie.log.closed` |
| `2026-06-23 18:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc28ae46c37f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:45 |
| **Last Seen** | 2026-06-23 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:45:29` | `cowrie.session.connect` |
| `2026-06-23 18:45:29` | `cowrie.client.version` |
| `2026-06-23 18:45:29` | `cowrie.client.kex` |
| `2026-06-23 18:45:30` | `cowrie.login.success` |
| `2026-06-23 18:45:30` | `cowrie.session.params` |
| `2026-06-23 18:45:30` | `cowrie.command.input` |
| `2026-06-23 18:45:30` | `cowrie.log.closed` |
| `2026-06-23 18:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aabb6c901f31

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:46 |
| **Last Seen** | 2026-06-23 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:46:20` | `cowrie.session.connect` |
| `2026-06-23 18:46:20` | `cowrie.client.version` |
| `2026-06-23 18:46:20` | `cowrie.client.kex` |
| `2026-06-23 18:46:20` | `cowrie.login.success` |
| `2026-06-23 18:46:21` | `cowrie.session.params` |
| `2026-06-23 18:46:21` | `cowrie.command.input` |
| `2026-06-23 18:46:21` | `cowrie.log.closed` |
| `2026-06-23 18:46:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e16886cbb53d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:47 |
| **Last Seen** | 2026-06-23 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:47:09` | `cowrie.session.connect` |
| `2026-06-23 18:47:09` | `cowrie.client.version` |
| `2026-06-23 18:47:10` | `cowrie.client.kex` |
| `2026-06-23 18:47:10` | `cowrie.login.success` |
| `2026-06-23 18:47:11` | `cowrie.session.params` |
| `2026-06-23 18:47:11` | `cowrie.command.input` |
| `2026-06-23 18:47:11` | `cowrie.log.closed` |
| `2026-06-23 18:47:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b1662abfd66

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 18:47 |
| **Last Seen** | 2026-06-23 18:47 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:47:39` | `cowrie.session.connect` |
| `2026-06-23 18:47:41` | `cowrie.client.version` |
| `2026-06-23 18:47:41` | `cowrie.client.kex` |
| `2026-06-23 18:47:46` | `cowrie.login.success` |
| `2026-06-23 18:47:50` | `cowrie.session.params` |
| `2026-06-23 18:47:50` | `cowrie.command.input` |
| `2026-06-23 18:47:52` | `cowrie.log.closed` |
| `2026-06-23 18:47:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b8ada2c007a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:47 |
| **Last Seen** | 2026-06-23 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:47:58` | `cowrie.session.connect` |
| `2026-06-23 18:47:58` | `cowrie.client.version` |
| `2026-06-23 18:47:58` | `cowrie.client.kex` |
| `2026-06-23 18:47:59` | `cowrie.login.success` |
| `2026-06-23 18:48:00` | `cowrie.session.params` |
| `2026-06-23 18:48:00` | `cowrie.command.input` |
| `2026-06-23 18:48:00` | `cowrie.log.closed` |
| `2026-06-23 18:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4118728cfe28

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:48 |
| **Last Seen** | 2026-06-23 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:48:47` | `cowrie.session.connect` |
| `2026-06-23 18:48:47` | `cowrie.client.version` |
| `2026-06-23 18:48:47` | `cowrie.client.kex` |
| `2026-06-23 18:48:48` | `cowrie.login.success` |
| `2026-06-23 18:48:48` | `cowrie.session.params` |
| `2026-06-23 18:48:48` | `cowrie.command.input` |
| `2026-06-23 18:48:49` | `cowrie.log.closed` |
| `2026-06-23 18:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c7e28d74e75

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:49 |
| **Last Seen** | 2026-06-23 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:49:37` | `cowrie.session.connect` |
| `2026-06-23 18:49:37` | `cowrie.client.version` |
| `2026-06-23 18:49:38` | `cowrie.client.kex` |
| `2026-06-23 18:49:38` | `cowrie.login.success` |
| `2026-06-23 18:49:38` | `cowrie.session.params` |
| `2026-06-23 18:49:38` | `cowrie.command.input` |
| `2026-06-23 18:49:39` | `cowrie.log.closed` |
| `2026-06-23 18:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4120807878fa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:50 |
| **Last Seen** | 2026-06-23 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:50:29` | `cowrie.session.connect` |
| `2026-06-23 18:50:29` | `cowrie.client.version` |
| `2026-06-23 18:50:29` | `cowrie.client.kex` |
| `2026-06-23 18:50:30` | `cowrie.login.success` |
| `2026-06-23 18:50:30` | `cowrie.session.params` |
| `2026-06-23 18:50:30` | `cowrie.command.input` |
| `2026-06-23 18:50:31` | `cowrie.log.closed` |
| `2026-06-23 18:50:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c94c595dac0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:51 |
| **Last Seen** | 2026-06-23 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:51:21` | `cowrie.session.connect` |
| `2026-06-23 18:51:21` | `cowrie.client.version` |
| `2026-06-23 18:51:21` | `cowrie.client.kex` |
| `2026-06-23 18:51:21` | `cowrie.login.success` |
| `2026-06-23 18:51:22` | `cowrie.session.params` |
| `2026-06-23 18:51:22` | `cowrie.command.input` |
| `2026-06-23 18:51:22` | `cowrie.log.closed` |
| `2026-06-23 18:51:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3838703946ec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:52 |
| **Last Seen** | 2026-06-23 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:52:13` | `cowrie.session.connect` |
| `2026-06-23 18:52:13` | `cowrie.client.version` |
| `2026-06-23 18:52:13` | `cowrie.client.kex` |
| `2026-06-23 18:52:13` | `cowrie.login.success` |
| `2026-06-23 18:52:14` | `cowrie.session.params` |
| `2026-06-23 18:52:14` | `cowrie.command.input` |
| `2026-06-23 18:52:14` | `cowrie.log.closed` |
| `2026-06-23 18:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5482c0c51968

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:53 |
| **Last Seen** | 2026-06-23 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:53:02` | `cowrie.session.connect` |
| `2026-06-23 18:53:02` | `cowrie.client.version` |
| `2026-06-23 18:53:02` | `cowrie.client.kex` |
| `2026-06-23 18:53:03` | `cowrie.login.success` |
| `2026-06-23 18:53:03` | `cowrie.session.params` |
| `2026-06-23 18:53:03` | `cowrie.command.input` |
| `2026-06-23 18:53:03` | `cowrie.log.closed` |
| `2026-06-23 18:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1c23d45a43d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:53 |
| **Last Seen** | 2026-06-23 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:53:53` | `cowrie.session.connect` |
| `2026-06-23 18:53:53` | `cowrie.client.version` |
| `2026-06-23 18:53:53` | `cowrie.client.kex` |
| `2026-06-23 18:53:53` | `cowrie.login.success` |
| `2026-06-23 18:53:54` | `cowrie.session.params` |
| `2026-06-23 18:53:54` | `cowrie.command.input` |
| `2026-06-23 18:53:54` | `cowrie.log.closed` |
| `2026-06-23 18:53:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a60fc19cac6e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:54 |
| **Last Seen** | 2026-06-23 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:54:44` | `cowrie.session.connect` |
| `2026-06-23 18:54:44` | `cowrie.client.version` |
| `2026-06-23 18:54:44` | `cowrie.client.kex` |
| `2026-06-23 18:54:44` | `cowrie.login.success` |
| `2026-06-23 18:54:45` | `cowrie.session.params` |
| `2026-06-23 18:54:45` | `cowrie.command.input` |
| `2026-06-23 18:54:45` | `cowrie.log.closed` |
| `2026-06-23 18:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7a31e50c6a4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:55 |
| **Last Seen** | 2026-06-23 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:55:40` | `cowrie.session.connect` |
| `2026-06-23 18:55:40` | `cowrie.client.version` |
| `2026-06-23 18:55:40` | `cowrie.client.kex` |
| `2026-06-23 18:55:40` | `cowrie.login.success` |
| `2026-06-23 18:55:41` | `cowrie.session.params` |
| `2026-06-23 18:55:41` | `cowrie.command.input` |
| `2026-06-23 18:55:41` | `cowrie.log.closed` |
| `2026-06-23 18:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b85929f054c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:56 |
| **Last Seen** | 2026-06-23 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:56:41` | `cowrie.session.connect` |
| `2026-06-23 18:56:41` | `cowrie.client.version` |
| `2026-06-23 18:56:41` | `cowrie.client.kex` |
| `2026-06-23 18:56:42` | `cowrie.login.success` |
| `2026-06-23 18:56:42` | `cowrie.session.params` |
| `2026-06-23 18:56:42` | `cowrie.command.input` |
| `2026-06-23 18:56:42` | `cowrie.log.closed` |
| `2026-06-23 18:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eae5422f5fb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:57 |
| **Last Seen** | 2026-06-23 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:57:37` | `cowrie.session.connect` |
| `2026-06-23 18:57:37` | `cowrie.client.version` |
| `2026-06-23 18:57:38` | `cowrie.client.kex` |
| `2026-06-23 18:57:38` | `cowrie.login.success` |
| `2026-06-23 18:57:39` | `cowrie.session.params` |
| `2026-06-23 18:57:39` | `cowrie.command.input` |
| `2026-06-23 18:57:39` | `cowrie.log.closed` |
| `2026-06-23 18:57:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73e8ffeb3a4f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:58 |
| **Last Seen** | 2026-06-23 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:58:29` | `cowrie.session.connect` |
| `2026-06-23 18:58:29` | `cowrie.client.version` |
| `2026-06-23 18:58:29` | `cowrie.client.kex` |
| `2026-06-23 18:58:30` | `cowrie.login.success` |
| `2026-06-23 18:58:31` | `cowrie.session.params` |
| `2026-06-23 18:58:31` | `cowrie.command.input` |
| `2026-06-23 18:58:31` | `cowrie.log.closed` |
| `2026-06-23 18:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-564c7a86c6a2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 18:59 |
| **Last Seen** | 2026-06-23 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:59:21` | `cowrie.session.connect` |
| `2026-06-23 18:59:21` | `cowrie.client.version` |
| `2026-06-23 18:59:21` | `cowrie.client.kex` |
| `2026-06-23 18:59:22` | `cowrie.login.success` |
| `2026-06-23 18:59:22` | `cowrie.session.params` |
| `2026-06-23 18:59:22` | `cowrie.command.input` |
| `2026-06-23 18:59:23` | `cowrie.log.closed` |
| `2026-06-23 18:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-579110f4711c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:00 |
| **Last Seen** | 2026-06-23 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:00:13` | `cowrie.session.connect` |
| `2026-06-23 19:00:13` | `cowrie.client.version` |
| `2026-06-23 19:00:13` | `cowrie.client.kex` |
| `2026-06-23 19:00:13` | `cowrie.login.success` |
| `2026-06-23 19:00:14` | `cowrie.session.params` |
| `2026-06-23 19:00:14` | `cowrie.command.input` |
| `2026-06-23 19:00:14` | `cowrie.log.closed` |
| `2026-06-23 19:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f34bf298b30

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:01 |
| **Last Seen** | 2026-06-23 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:01:03` | `cowrie.session.connect` |
| `2026-06-23 19:01:03` | `cowrie.client.version` |
| `2026-06-23 19:01:04` | `cowrie.client.kex` |
| `2026-06-23 19:01:04` | `cowrie.login.success` |
| `2026-06-23 19:01:05` | `cowrie.session.params` |
| `2026-06-23 19:01:05` | `cowrie.command.input` |
| `2026-06-23 19:01:05` | `cowrie.log.closed` |
| `2026-06-23 19:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b22bdfd4799

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 19:01 |
| **Last Seen** | 2026-06-23 19:02 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:01:54` | `cowrie.session.connect` |
| `2026-06-23 19:01:55` | `cowrie.client.version` |
| `2026-06-23 19:01:55` | `cowrie.client.kex` |
| `2026-06-23 19:02:01` | `cowrie.login.success` |
| `2026-06-23 19:02:06` | `cowrie.session.params` |
| `2026-06-23 19:02:06` | `cowrie.command.input` |
| `2026-06-23 19:02:07` | `cowrie.log.closed` |
| `2026-06-23 19:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b720cba65cf1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:01 |
| **Last Seen** | 2026-06-23 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:01:55` | `cowrie.session.connect` |
| `2026-06-23 19:01:55` | `cowrie.client.version` |
| `2026-06-23 19:01:56` | `cowrie.client.kex` |
| `2026-06-23 19:01:56` | `cowrie.login.success` |
| `2026-06-23 19:01:57` | `cowrie.session.params` |
| `2026-06-23 19:01:57` | `cowrie.command.input` |
| `2026-06-23 19:01:57` | `cowrie.log.closed` |
| `2026-06-23 19:01:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63d5afc7f2f9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:02 |
| **Last Seen** | 2026-06-23 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:02:48` | `cowrie.session.connect` |
| `2026-06-23 19:02:48` | `cowrie.client.version` |
| `2026-06-23 19:02:48` | `cowrie.client.kex` |
| `2026-06-23 19:02:49` | `cowrie.login.success` |
| `2026-06-23 19:02:49` | `cowrie.session.params` |
| `2026-06-23 19:02:49` | `cowrie.command.input` |
| `2026-06-23 19:02:49` | `cowrie.log.closed` |
| `2026-06-23 19:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4647c05feb1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:03 |
| **Last Seen** | 2026-06-23 19:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:03:42` | `cowrie.session.connect` |
| `2026-06-23 19:03:42` | `cowrie.client.version` |
| `2026-06-23 19:03:42` | `cowrie.client.kex` |
| `2026-06-23 19:03:42` | `cowrie.login.success` |
| `2026-06-23 19:03:43` | `cowrie.session.params` |
| `2026-06-23 19:03:43` | `cowrie.command.input` |
| `2026-06-23 19:03:43` | `cowrie.log.closed` |
| `2026-06-23 19:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6568084ec9cd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:04 |
| **Last Seen** | 2026-06-23 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:04:35` | `cowrie.session.connect` |
| `2026-06-23 19:04:35` | `cowrie.client.version` |
| `2026-06-23 19:04:35` | `cowrie.client.kex` |
| `2026-06-23 19:04:35` | `cowrie.login.success` |
| `2026-06-23 19:04:36` | `cowrie.session.params` |
| `2026-06-23 19:04:36` | `cowrie.command.input` |
| `2026-06-23 19:04:36` | `cowrie.log.closed` |
| `2026-06-23 19:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37aca062702a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:05 |
| **Last Seen** | 2026-06-23 19:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:05:27` | `cowrie.session.connect` |
| `2026-06-23 19:05:27` | `cowrie.client.version` |
| `2026-06-23 19:05:27` | `cowrie.client.kex` |
| `2026-06-23 19:05:27` | `cowrie.login.success` |
| `2026-06-23 19:05:28` | `cowrie.session.params` |
| `2026-06-23 19:05:28` | `cowrie.command.input` |
| `2026-06-23 19:05:28` | `cowrie.log.closed` |
| `2026-06-23 19:05:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abe45aa7037d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:06 |
| **Last Seen** | 2026-06-23 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:06:18` | `cowrie.session.connect` |
| `2026-06-23 19:06:18` | `cowrie.client.version` |
| `2026-06-23 19:06:18` | `cowrie.client.kex` |
| `2026-06-23 19:06:19` | `cowrie.login.success` |
| `2026-06-23 19:06:20` | `cowrie.session.params` |
| `2026-06-23 19:06:20` | `cowrie.command.input` |
| `2026-06-23 19:06:20` | `cowrie.log.closed` |
| `2026-06-23 19:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6ee852580ef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:07 |
| **Last Seen** | 2026-06-23 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:07:10` | `cowrie.session.connect` |
| `2026-06-23 19:07:10` | `cowrie.client.version` |
| `2026-06-23 19:07:10` | `cowrie.client.kex` |
| `2026-06-23 19:07:11` | `cowrie.login.success` |
| `2026-06-23 19:07:11` | `cowrie.session.params` |
| `2026-06-23 19:07:11` | `cowrie.command.input` |
| `2026-06-23 19:07:11` | `cowrie.log.closed` |
| `2026-06-23 19:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d548cb2ec58

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:08 |
| **Last Seen** | 2026-06-23 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:08:02` | `cowrie.session.connect` |
| `2026-06-23 19:08:02` | `cowrie.client.version` |
| `2026-06-23 19:08:02` | `cowrie.client.kex` |
| `2026-06-23 19:08:03` | `cowrie.login.success` |
| `2026-06-23 19:08:03` | `cowrie.session.params` |
| `2026-06-23 19:08:03` | `cowrie.command.input` |
| `2026-06-23 19:08:04` | `cowrie.log.closed` |
| `2026-06-23 19:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1c8e7b0ad21

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:08 |
| **Last Seen** | 2026-06-23 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:08:54` | `cowrie.session.connect` |
| `2026-06-23 19:08:54` | `cowrie.client.version` |
| `2026-06-23 19:08:55` | `cowrie.client.kex` |
| `2026-06-23 19:08:55` | `cowrie.login.success` |
| `2026-06-23 19:08:56` | `cowrie.session.params` |
| `2026-06-23 19:08:56` | `cowrie.command.input` |
| `2026-06-23 19:08:56` | `cowrie.log.closed` |
| `2026-06-23 19:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52b75c6762a7

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-23 19:09 |
| **Last Seen** | 2026-06-23 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:09:23` | `cowrie.session.connect` |
| `2026-06-23 19:09:23` | `cowrie.client.version` |
| `2026-06-23 19:09:23` | `cowrie.client.kex` |
| `2026-06-23 19:09:24` | `cowrie.login.success` |
| `2026-06-23 19:09:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c58df13cfe3

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-23 19:09 |
| **Last Seen** | 2026-06-23 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:09:23` | `cowrie.session.connect` |
| `2026-06-23 19:09:23` | `cowrie.client.version` |
| `2026-06-23 19:09:23` | `cowrie.client.kex` |
| `2026-06-23 19:09:24` | `cowrie.login.success` |
| `2026-06-23 19:09:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d96ff035167

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:09 |
| **Last Seen** | 2026-06-23 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:09:48` | `cowrie.session.connect` |
| `2026-06-23 19:09:48` | `cowrie.client.version` |
| `2026-06-23 19:09:48` | `cowrie.client.kex` |
| `2026-06-23 19:09:48` | `cowrie.login.success` |
| `2026-06-23 19:09:49` | `cowrie.session.params` |
| `2026-06-23 19:09:49` | `cowrie.command.input` |
| `2026-06-23 19:09:49` | `cowrie.log.closed` |
| `2026-06-23 19:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92852498ec19

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:10 |
| **Last Seen** | 2026-06-23 19:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:10:41` | `cowrie.session.connect` |
| `2026-06-23 19:10:41` | `cowrie.client.version` |
| `2026-06-23 19:10:41` | `cowrie.client.kex` |
| `2026-06-23 19:10:42` | `cowrie.login.success` |
| `2026-06-23 19:10:43` | `cowrie.session.params` |
| `2026-06-23 19:10:43` | `cowrie.command.input` |
| `2026-06-23 19:10:43` | `cowrie.log.closed` |
| `2026-06-23 19:10:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a5b181392a1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:11 |
| **Last Seen** | 2026-06-23 19:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:11:35` | `cowrie.session.connect` |
| `2026-06-23 19:11:35` | `cowrie.client.version` |
| `2026-06-23 19:11:35` | `cowrie.client.kex` |
| `2026-06-23 19:11:35` | `cowrie.login.success` |
| `2026-06-23 19:11:36` | `cowrie.session.params` |
| `2026-06-23 19:11:36` | `cowrie.command.input` |
| `2026-06-23 19:11:36` | `cowrie.log.closed` |
| `2026-06-23 19:11:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-745c01c82ebd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:12 |
| **Last Seen** | 2026-06-23 19:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:12:28` | `cowrie.session.connect` |
| `2026-06-23 19:12:28` | `cowrie.client.version` |
| `2026-06-23 19:12:28` | `cowrie.client.kex` |
| `2026-06-23 19:12:28` | `cowrie.login.success` |
| `2026-06-23 19:12:29` | `cowrie.session.params` |
| `2026-06-23 19:12:29` | `cowrie.command.input` |
| `2026-06-23 19:12:29` | `cowrie.log.closed` |
| `2026-06-23 19:12:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2339105edec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:13 |
| **Last Seen** | 2026-06-23 19:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:13:21` | `cowrie.session.connect` |
| `2026-06-23 19:13:21` | `cowrie.client.version` |
| `2026-06-23 19:13:21` | `cowrie.client.kex` |
| `2026-06-23 19:13:21` | `cowrie.login.success` |
| `2026-06-23 19:13:22` | `cowrie.session.params` |
| `2026-06-23 19:13:22` | `cowrie.command.input` |
| `2026-06-23 19:13:22` | `cowrie.log.closed` |
| `2026-06-23 19:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-585fa7218f40

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:14 |
| **Last Seen** | 2026-06-23 19:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:14:15` | `cowrie.session.connect` |
| `2026-06-23 19:14:15` | `cowrie.client.version` |
| `2026-06-23 19:14:15` | `cowrie.client.kex` |
| `2026-06-23 19:14:15` | `cowrie.login.success` |
| `2026-06-23 19:14:16` | `cowrie.session.params` |
| `2026-06-23 19:14:16` | `cowrie.command.input` |
| `2026-06-23 19:14:16` | `cowrie.log.closed` |
| `2026-06-23 19:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf08a9928a09

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:15 |
| **Last Seen** | 2026-06-23 19:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:15:09` | `cowrie.session.connect` |
| `2026-06-23 19:15:09` | `cowrie.client.version` |
| `2026-06-23 19:15:09` | `cowrie.client.kex` |
| `2026-06-23 19:15:09` | `cowrie.login.success` |
| `2026-06-23 19:15:10` | `cowrie.session.params` |
| `2026-06-23 19:15:10` | `cowrie.command.input` |
| `2026-06-23 19:15:10` | `cowrie.log.closed` |
| `2026-06-23 19:15:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6650b0c2f404

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:16 |
| **Last Seen** | 2026-06-23 19:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:16:02` | `cowrie.session.connect` |
| `2026-06-23 19:16:02` | `cowrie.client.version` |
| `2026-06-23 19:16:03` | `cowrie.client.kex` |
| `2026-06-23 19:16:03` | `cowrie.login.success` |
| `2026-06-23 19:16:04` | `cowrie.session.params` |
| `2026-06-23 19:16:04` | `cowrie.command.input` |
| `2026-06-23 19:16:04` | `cowrie.log.closed` |
| `2026-06-23 19:16:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caf9d31f6596

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 19:16 |
| **Last Seen** | 2026-06-23 19:16 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:16:12` | `cowrie.session.connect` |
| `2026-06-23 19:16:14` | `cowrie.client.version` |
| `2026-06-23 19:16:14` | `cowrie.client.kex` |
| `2026-06-23 19:16:21` | `cowrie.login.success` |
| `2026-06-23 19:16:24` | `cowrie.session.params` |
| `2026-06-23 19:16:24` | `cowrie.command.input` |
| `2026-06-23 19:16:26` | `cowrie.log.closed` |
| `2026-06-23 19:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a705f388b73

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:16 |
| **Last Seen** | 2026-06-23 19:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:16:57` | `cowrie.session.connect` |
| `2026-06-23 19:16:57` | `cowrie.client.version` |
| `2026-06-23 19:16:57` | `cowrie.client.kex` |
| `2026-06-23 19:16:57` | `cowrie.login.success` |
| `2026-06-23 19:16:58` | `cowrie.session.params` |
| `2026-06-23 19:16:58` | `cowrie.command.input` |
| `2026-06-23 19:16:58` | `cowrie.log.closed` |
| `2026-06-23 19:16:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01e73157bf2a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:17 |
| **Last Seen** | 2026-06-23 19:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:17:49` | `cowrie.session.connect` |
| `2026-06-23 19:17:49` | `cowrie.client.version` |
| `2026-06-23 19:17:49` | `cowrie.client.kex` |
| `2026-06-23 19:17:50` | `cowrie.login.success` |
| `2026-06-23 19:17:50` | `cowrie.session.params` |
| `2026-06-23 19:17:50` | `cowrie.command.input` |
| `2026-06-23 19:17:51` | `cowrie.log.closed` |
| `2026-06-23 19:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-002d36697c7b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:18 |
| **Last Seen** | 2026-06-23 19:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:18:42` | `cowrie.session.connect` |
| `2026-06-23 19:18:42` | `cowrie.client.version` |
| `2026-06-23 19:18:42` | `cowrie.client.kex` |
| `2026-06-23 19:18:42` | `cowrie.login.success` |
| `2026-06-23 19:18:43` | `cowrie.session.params` |
| `2026-06-23 19:18:43` | `cowrie.command.input` |
| `2026-06-23 19:18:43` | `cowrie.log.closed` |
| `2026-06-23 19:18:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76f0f9067b75

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:19 |
| **Last Seen** | 2026-06-23 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:19:33` | `cowrie.session.connect` |
| `2026-06-23 19:19:33` | `cowrie.client.version` |
| `2026-06-23 19:19:33` | `cowrie.client.kex` |
| `2026-06-23 19:19:34` | `cowrie.login.success` |
| `2026-06-23 19:19:35` | `cowrie.session.params` |
| `2026-06-23 19:19:35` | `cowrie.command.input` |
| `2026-06-23 19:19:35` | `cowrie.log.closed` |
| `2026-06-23 19:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-180f3c7fc2ba

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:20 |
| **Last Seen** | 2026-06-23 19:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:20:26` | `cowrie.session.connect` |
| `2026-06-23 19:20:26` | `cowrie.client.version` |
| `2026-06-23 19:20:26` | `cowrie.client.kex` |
| `2026-06-23 19:20:27` | `cowrie.login.success` |
| `2026-06-23 19:20:27` | `cowrie.session.params` |
| `2026-06-23 19:20:27` | `cowrie.command.input` |
| `2026-06-23 19:20:28` | `cowrie.log.closed` |
| `2026-06-23 19:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bf04fcbd527

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:21 |
| **Last Seen** | 2026-06-23 19:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:21:19` | `cowrie.session.connect` |
| `2026-06-23 19:21:19` | `cowrie.client.version` |
| `2026-06-23 19:21:20` | `cowrie.client.kex` |
| `2026-06-23 19:21:20` | `cowrie.login.success` |
| `2026-06-23 19:21:21` | `cowrie.session.params` |
| `2026-06-23 19:21:21` | `cowrie.command.input` |
| `2026-06-23 19:21:21` | `cowrie.log.closed` |
| `2026-06-23 19:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53682d35c705

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:22 |
| **Last Seen** | 2026-06-23 19:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:22:14` | `cowrie.session.connect` |
| `2026-06-23 19:22:14` | `cowrie.client.version` |
| `2026-06-23 19:22:14` | `cowrie.client.kex` |
| `2026-06-23 19:22:15` | `cowrie.login.success` |
| `2026-06-23 19:22:16` | `cowrie.session.params` |
| `2026-06-23 19:22:16` | `cowrie.command.input` |
| `2026-06-23 19:22:16` | `cowrie.log.closed` |
| `2026-06-23 19:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e65eaf436592

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:23 |
| **Last Seen** | 2026-06-23 19:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:23:09` | `cowrie.session.connect` |
| `2026-06-23 19:23:09` | `cowrie.client.version` |
| `2026-06-23 19:23:10` | `cowrie.client.kex` |
| `2026-06-23 19:23:10` | `cowrie.login.success` |
| `2026-06-23 19:23:11` | `cowrie.session.params` |
| `2026-06-23 19:23:11` | `cowrie.command.input` |
| `2026-06-23 19:23:11` | `cowrie.log.closed` |
| `2026-06-23 19:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-772fecf42cad

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:24 |
| **Last Seen** | 2026-06-23 19:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:24:04` | `cowrie.session.connect` |
| `2026-06-23 19:24:04` | `cowrie.client.version` |
| `2026-06-23 19:24:04` | `cowrie.client.kex` |
| `2026-06-23 19:24:05` | `cowrie.login.success` |
| `2026-06-23 19:24:05` | `cowrie.session.params` |
| `2026-06-23 19:24:05` | `cowrie.command.input` |
| `2026-06-23 19:24:06` | `cowrie.log.closed` |
| `2026-06-23 19:24:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e6211fa17d3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:24 |
| **Last Seen** | 2026-06-23 19:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:24:59` | `cowrie.session.connect` |
| `2026-06-23 19:24:59` | `cowrie.client.version` |
| `2026-06-23 19:24:59` | `cowrie.client.kex` |
| `2026-06-23 19:24:59` | `cowrie.login.success` |
| `2026-06-23 19:25:00` | `cowrie.session.params` |
| `2026-06-23 19:25:00` | `cowrie.command.input` |
| `2026-06-23 19:25:00` | `cowrie.log.closed` |
| `2026-06-23 19:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92fac46c1ff1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:25 |
| **Last Seen** | 2026-06-23 19:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:25:53` | `cowrie.session.connect` |
| `2026-06-23 19:25:53` | `cowrie.client.version` |
| `2026-06-23 19:25:53` | `cowrie.client.kex` |
| `2026-06-23 19:25:54` | `cowrie.login.success` |
| `2026-06-23 19:25:54` | `cowrie.session.params` |
| `2026-06-23 19:25:54` | `cowrie.command.input` |
| `2026-06-23 19:25:55` | `cowrie.log.closed` |
| `2026-06-23 19:25:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fac19bfdb48

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:26 |
| **Last Seen** | 2026-06-23 19:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:26:47` | `cowrie.session.connect` |
| `2026-06-23 19:26:47` | `cowrie.client.version` |
| `2026-06-23 19:26:47` | `cowrie.client.kex` |
| `2026-06-23 19:26:47` | `cowrie.login.success` |
| `2026-06-23 19:26:48` | `cowrie.session.params` |
| `2026-06-23 19:26:48` | `cowrie.command.input` |
| `2026-06-23 19:26:48` | `cowrie.log.closed` |
| `2026-06-23 19:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0d4db58c46c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:27 |
| **Last Seen** | 2026-06-23 19:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:27:41` | `cowrie.session.connect` |
| `2026-06-23 19:27:41` | `cowrie.client.version` |
| `2026-06-23 19:27:41` | `cowrie.client.kex` |
| `2026-06-23 19:27:42` | `cowrie.login.success` |
| `2026-06-23 19:27:43` | `cowrie.session.params` |
| `2026-06-23 19:27:43` | `cowrie.command.input` |
| `2026-06-23 19:27:43` | `cowrie.log.closed` |
| `2026-06-23 19:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9283dc60445f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:28 |
| **Last Seen** | 2026-06-23 19:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:28:37` | `cowrie.session.connect` |
| `2026-06-23 19:28:37` | `cowrie.client.version` |
| `2026-06-23 19:28:37` | `cowrie.client.kex` |
| `2026-06-23 19:28:37` | `cowrie.login.success` |
| `2026-06-23 19:28:38` | `cowrie.session.params` |
| `2026-06-23 19:28:38` | `cowrie.command.input` |
| `2026-06-23 19:28:38` | `cowrie.log.closed` |
| `2026-06-23 19:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d572f16a63b1

| Field | Detail |
|---|---|
| **Source IP** | `121.29.5[.]231` |
| **First Seen** | 2026-06-23 19:28 |
| **Last Seen** | 2026-06-23 19:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:28:47` | `cowrie.session.connect` |
| `2026-06-23 19:28:47` | `cowrie.client.version` |
| `2026-06-23 19:28:47` | `cowrie.client.kex` |
| `2026-06-23 19:28:48` | `cowrie.login.success` |
| `2026-06-23 19:28:49` | `cowrie.session.params` |
| `2026-06-23 19:28:49` | `cowrie.command.input` |
| `2026-06-23 19:28:50` | `cowrie.log.closed` |
| `2026-06-23 19:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.29.5[.]231` to AbuseIPDB if not already reported
- [ ] Block `121.29.5[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a70978b9aa5e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:29 |
| **Last Seen** | 2026-06-23 19:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:29:33` | `cowrie.session.connect` |
| `2026-06-23 19:29:33` | `cowrie.client.version` |
| `2026-06-23 19:29:33` | `cowrie.client.kex` |
| `2026-06-23 19:29:33` | `cowrie.login.success` |
| `2026-06-23 19:29:34` | `cowrie.session.params` |
| `2026-06-23 19:29:34` | `cowrie.command.input` |
| `2026-06-23 19:29:34` | `cowrie.log.closed` |
| `2026-06-23 19:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d17c8bc2de4f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:30 |
| **Last Seen** | 2026-06-23 19:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:30:28` | `cowrie.session.connect` |
| `2026-06-23 19:30:28` | `cowrie.client.version` |
| `2026-06-23 19:30:28` | `cowrie.client.kex` |
| `2026-06-23 19:30:28` | `cowrie.login.success` |
| `2026-06-23 19:30:29` | `cowrie.session.params` |
| `2026-06-23 19:30:29` | `cowrie.command.input` |
| `2026-06-23 19:30:29` | `cowrie.log.closed` |
| `2026-06-23 19:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ebf0f6ce745

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 19:30 |
| **Last Seen** | 2026-06-23 19:30 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:30:35` | `cowrie.session.connect` |
| `2026-06-23 19:30:37` | `cowrie.client.version` |
| `2026-06-23 19:30:37` | `cowrie.client.kex` |
| `2026-06-23 19:30:43` | `cowrie.login.success` |
| `2026-06-23 19:30:47` | `cowrie.session.params` |
| `2026-06-23 19:30:47` | `cowrie.command.input` |
| `2026-06-23 19:30:48` | `cowrie.log.closed` |
| `2026-06-23 19:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51ae9e8d1ee0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:31 |
| **Last Seen** | 2026-06-23 19:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:31:23` | `cowrie.session.connect` |
| `2026-06-23 19:31:23` | `cowrie.client.version` |
| `2026-06-23 19:31:23` | `cowrie.client.kex` |
| `2026-06-23 19:31:24` | `cowrie.login.success` |
| `2026-06-23 19:31:24` | `cowrie.session.params` |
| `2026-06-23 19:31:24` | `cowrie.command.input` |
| `2026-06-23 19:31:25` | `cowrie.log.closed` |
| `2026-06-23 19:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3ebf76781c7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:32 |
| **Last Seen** | 2026-06-23 19:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:32:19` | `cowrie.session.connect` |
| `2026-06-23 19:32:19` | `cowrie.client.version` |
| `2026-06-23 19:32:19` | `cowrie.client.kex` |
| `2026-06-23 19:32:19` | `cowrie.login.success` |
| `2026-06-23 19:32:20` | `cowrie.session.params` |
| `2026-06-23 19:32:20` | `cowrie.command.input` |
| `2026-06-23 19:32:20` | `cowrie.log.closed` |
| `2026-06-23 19:32:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f5c0e748657

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:33 |
| **Last Seen** | 2026-06-23 19:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:33:13` | `cowrie.session.connect` |
| `2026-06-23 19:33:13` | `cowrie.client.version` |
| `2026-06-23 19:33:13` | `cowrie.client.kex` |
| `2026-06-23 19:33:14` | `cowrie.login.success` |
| `2026-06-23 19:33:15` | `cowrie.session.params` |
| `2026-06-23 19:33:15` | `cowrie.command.input` |
| `2026-06-23 19:33:15` | `cowrie.log.closed` |
| `2026-06-23 19:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-473588914232

| Field | Detail |
|---|---|
| **Source IP** | `118.194.235[.]105` |
| **First Seen** | 2026-06-23 19:33 |
| **Last Seen** | 2026-06-23 19:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:33:56` | `cowrie.session.connect` |
| `2026-06-23 19:33:57` | `cowrie.telnet.option` |
| `2026-06-23 19:33:57` | `cowrie.telnet.option` |
| `2026-06-23 19:34:57` | `cowrie.login.success` |
| `2026-06-23 19:34:58` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `118.194.235[.]105` to AbuseIPDB if not already reported
- [ ] Block `118.194.235[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfa7f7927823

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:34 |
| **Last Seen** | 2026-06-23 19:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:34:09` | `cowrie.session.connect` |
| `2026-06-23 19:34:09` | `cowrie.client.version` |
| `2026-06-23 19:34:09` | `cowrie.client.kex` |
| `2026-06-23 19:34:09` | `cowrie.login.success` |
| `2026-06-23 19:34:10` | `cowrie.session.params` |
| `2026-06-23 19:34:10` | `cowrie.command.input` |
| `2026-06-23 19:34:10` | `cowrie.log.closed` |
| `2026-06-23 19:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddbd3b570ae2

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-23 19:34 |
| **Last Seen** | 2026-06-23 19:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:34:41` | `cowrie.session.connect` |
| `2026-06-23 19:34:41` | `cowrie.client.version` |
| `2026-06-23 19:34:41` | `cowrie.client.kex` |
| `2026-06-23 19:34:41` | `cowrie.login.success` |
| `2026-06-23 19:34:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8da8cb26a9b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-23 19:34 |
| **Last Seen** | 2026-06-23 19:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:34:42` | `cowrie.session.connect` |
| `2026-06-23 19:34:42` | `cowrie.client.version` |
| `2026-06-23 19:34:42` | `cowrie.client.kex` |
| `2026-06-23 19:34:42` | `cowrie.login.success` |
| `2026-06-23 19:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4efd6d82c2d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-23 19:35 |
| **Last Seen** | 2026-06-23 19:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:35:01` | `cowrie.session.connect` |
| `2026-06-23 19:35:01` | `cowrie.client.version` |
| `2026-06-23 19:35:01` | `cowrie.client.kex` |
| `2026-06-23 19:35:01` | `cowrie.login.success` |
| `2026-06-23 19:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-622d0c753148

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:35 |
| **Last Seen** | 2026-06-23 19:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:35:06` | `cowrie.session.connect` |
| `2026-06-23 19:35:06` | `cowrie.client.version` |
| `2026-06-23 19:35:07` | `cowrie.client.kex` |
| `2026-06-23 19:35:07` | `cowrie.login.success` |
| `2026-06-23 19:35:08` | `cowrie.session.params` |
| `2026-06-23 19:35:08` | `cowrie.command.input` |
| `2026-06-23 19:35:08` | `cowrie.log.closed` |
| `2026-06-23 19:35:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-986c9e64a0cc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:36 |
| **Last Seen** | 2026-06-23 19:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:36:04` | `cowrie.session.connect` |
| `2026-06-23 19:36:04` | `cowrie.client.version` |
| `2026-06-23 19:36:04` | `cowrie.client.kex` |
| `2026-06-23 19:36:04` | `cowrie.login.success` |
| `2026-06-23 19:36:05` | `cowrie.session.params` |
| `2026-06-23 19:36:05` | `cowrie.command.input` |
| `2026-06-23 19:36:05` | `cowrie.log.closed` |
| `2026-06-23 19:36:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deae0167add9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:37 |
| **Last Seen** | 2026-06-23 19:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:37:01` | `cowrie.session.connect` |
| `2026-06-23 19:37:01` | `cowrie.client.version` |
| `2026-06-23 19:37:01` | `cowrie.client.kex` |
| `2026-06-23 19:37:02` | `cowrie.login.success` |
| `2026-06-23 19:37:02` | `cowrie.session.params` |
| `2026-06-23 19:37:02` | `cowrie.command.input` |
| `2026-06-23 19:37:03` | `cowrie.log.closed` |
| `2026-06-23 19:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acd6daf3afc2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:37 |
| **Last Seen** | 2026-06-23 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:37:59` | `cowrie.session.connect` |
| `2026-06-23 19:37:59` | `cowrie.client.version` |
| `2026-06-23 19:37:59` | `cowrie.client.kex` |
| `2026-06-23 19:37:59` | `cowrie.login.success` |
| `2026-06-23 19:38:00` | `cowrie.session.params` |
| `2026-06-23 19:38:00` | `cowrie.command.input` |
| `2026-06-23 19:38:00` | `cowrie.log.closed` |
| `2026-06-23 19:38:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77d9541760c2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:38 |
| **Last Seen** | 2026-06-23 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:38:56` | `cowrie.session.connect` |
| `2026-06-23 19:38:56` | `cowrie.client.version` |
| `2026-06-23 19:38:56` | `cowrie.client.kex` |
| `2026-06-23 19:38:56` | `cowrie.login.success` |
| `2026-06-23 19:38:57` | `cowrie.session.params` |
| `2026-06-23 19:38:57` | `cowrie.command.input` |
| `2026-06-23 19:38:57` | `cowrie.log.closed` |
| `2026-06-23 19:38:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-494bf263664e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:39 |
| **Last Seen** | 2026-06-23 19:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:39:53` | `cowrie.session.connect` |
| `2026-06-23 19:39:53` | `cowrie.client.version` |
| `2026-06-23 19:39:53` | `cowrie.client.kex` |
| `2026-06-23 19:39:53` | `cowrie.login.success` |
| `2026-06-23 19:39:54` | `cowrie.session.params` |
| `2026-06-23 19:39:54` | `cowrie.command.input` |
| `2026-06-23 19:39:54` | `cowrie.log.closed` |
| `2026-06-23 19:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f3cbce054f2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:40 |
| **Last Seen** | 2026-06-23 19:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:40:50` | `cowrie.session.connect` |
| `2026-06-23 19:40:50` | `cowrie.client.version` |
| `2026-06-23 19:40:50` | `cowrie.client.kex` |
| `2026-06-23 19:40:51` | `cowrie.login.success` |
| `2026-06-23 19:40:51` | `cowrie.session.params` |
| `2026-06-23 19:40:51` | `cowrie.command.input` |
| `2026-06-23 19:40:52` | `cowrie.log.closed` |
| `2026-06-23 19:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d69c5c34445a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:41 |
| **Last Seen** | 2026-06-23 19:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:41:49` | `cowrie.session.connect` |
| `2026-06-23 19:41:49` | `cowrie.client.version` |
| `2026-06-23 19:41:49` | `cowrie.client.kex` |
| `2026-06-23 19:41:49` | `cowrie.login.success` |
| `2026-06-23 19:41:50` | `cowrie.session.params` |
| `2026-06-23 19:41:50` | `cowrie.command.input` |
| `2026-06-23 19:41:50` | `cowrie.log.closed` |
| `2026-06-23 19:41:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6776e888aadb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:42 |
| **Last Seen** | 2026-06-23 19:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:42:47` | `cowrie.session.connect` |
| `2026-06-23 19:42:47` | `cowrie.client.version` |
| `2026-06-23 19:42:47` | `cowrie.client.kex` |
| `2026-06-23 19:42:47` | `cowrie.login.success` |
| `2026-06-23 19:42:48` | `cowrie.session.params` |
| `2026-06-23 19:42:48` | `cowrie.command.input` |
| `2026-06-23 19:42:48` | `cowrie.log.closed` |
| `2026-06-23 19:42:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a83d50efd01

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:43 |
| **Last Seen** | 2026-06-23 19:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:43:43` | `cowrie.session.connect` |
| `2026-06-23 19:43:43` | `cowrie.client.version` |
| `2026-06-23 19:43:44` | `cowrie.client.kex` |
| `2026-06-23 19:43:44` | `cowrie.login.success` |
| `2026-06-23 19:43:45` | `cowrie.session.params` |
| `2026-06-23 19:43:45` | `cowrie.command.input` |
| `2026-06-23 19:43:45` | `cowrie.log.closed` |
| `2026-06-23 19:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a114997aa72

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:44 |
| **Last Seen** | 2026-06-23 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:44:40` | `cowrie.session.connect` |
| `2026-06-23 19:44:40` | `cowrie.client.version` |
| `2026-06-23 19:44:41` | `cowrie.client.kex` |
| `2026-06-23 19:44:41` | `cowrie.login.success` |
| `2026-06-23 19:44:42` | `cowrie.session.params` |
| `2026-06-23 19:44:42` | `cowrie.command.input` |
| `2026-06-23 19:44:42` | `cowrie.log.closed` |
| `2026-06-23 19:44:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ef68ebfb41f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 19:44 |
| **Last Seen** | 2026-06-23 19:45 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:44:59` | `cowrie.session.connect` |
| `2026-06-23 19:45:00` | `cowrie.client.version` |
| `2026-06-23 19:45:00` | `cowrie.client.kex` |
| `2026-06-23 19:45:06` | `cowrie.login.success` |
| `2026-06-23 19:45:11` | `cowrie.session.params` |
| `2026-06-23 19:45:11` | `cowrie.command.input` |
| `2026-06-23 19:45:12` | `cowrie.log.closed` |
| `2026-06-23 19:45:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5495158ceff2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:45 |
| **Last Seen** | 2026-06-23 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:45:36` | `cowrie.session.connect` |
| `2026-06-23 19:45:36` | `cowrie.client.version` |
| `2026-06-23 19:45:37` | `cowrie.client.kex` |
| `2026-06-23 19:45:37` | `cowrie.login.success` |
| `2026-06-23 19:45:38` | `cowrie.session.params` |
| `2026-06-23 19:45:38` | `cowrie.command.input` |
| `2026-06-23 19:45:38` | `cowrie.log.closed` |
| `2026-06-23 19:45:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-569a4a4be099

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:46 |
| **Last Seen** | 2026-06-23 19:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:46:34` | `cowrie.session.connect` |
| `2026-06-23 19:46:34` | `cowrie.client.version` |
| `2026-06-23 19:46:34` | `cowrie.client.kex` |
| `2026-06-23 19:46:35` | `cowrie.login.success` |
| `2026-06-23 19:46:36` | `cowrie.session.params` |
| `2026-06-23 19:46:36` | `cowrie.command.input` |
| `2026-06-23 19:46:36` | `cowrie.log.closed` |
| `2026-06-23 19:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca4120b8e052

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:47 |
| **Last Seen** | 2026-06-23 19:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:47:32` | `cowrie.session.connect` |
| `2026-06-23 19:47:32` | `cowrie.client.version` |
| `2026-06-23 19:47:32` | `cowrie.client.kex` |
| `2026-06-23 19:47:33` | `cowrie.login.success` |
| `2026-06-23 19:47:33` | `cowrie.session.params` |
| `2026-06-23 19:47:33` | `cowrie.command.input` |
| `2026-06-23 19:47:33` | `cowrie.log.closed` |
| `2026-06-23 19:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-921e8c836b2e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:48 |
| **Last Seen** | 2026-06-23 19:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:48:32` | `cowrie.session.connect` |
| `2026-06-23 19:48:32` | `cowrie.client.version` |
| `2026-06-23 19:48:32` | `cowrie.client.kex` |
| `2026-06-23 19:48:32` | `cowrie.login.success` |
| `2026-06-23 19:48:33` | `cowrie.session.params` |
| `2026-06-23 19:48:33` | `cowrie.command.input` |
| `2026-06-23 19:48:33` | `cowrie.log.closed` |
| `2026-06-23 19:48:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-123839bef307

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:49 |
| **Last Seen** | 2026-06-23 19:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:49:29` | `cowrie.session.connect` |
| `2026-06-23 19:49:29` | `cowrie.client.version` |
| `2026-06-23 19:49:30` | `cowrie.client.kex` |
| `2026-06-23 19:49:30` | `cowrie.login.success` |
| `2026-06-23 19:49:31` | `cowrie.session.params` |
| `2026-06-23 19:49:31` | `cowrie.command.input` |
| `2026-06-23 19:49:31` | `cowrie.log.closed` |
| `2026-06-23 19:49:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dfb3ce3203f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:50 |
| **Last Seen** | 2026-06-23 19:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:50:27` | `cowrie.session.connect` |
| `2026-06-23 19:50:27` | `cowrie.client.version` |
| `2026-06-23 19:50:27` | `cowrie.client.kex` |
| `2026-06-23 19:50:27` | `cowrie.login.success` |
| `2026-06-23 19:50:28` | `cowrie.session.params` |
| `2026-06-23 19:50:28` | `cowrie.command.input` |
| `2026-06-23 19:50:28` | `cowrie.log.closed` |
| `2026-06-23 19:50:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec04c019eab1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:51 |
| **Last Seen** | 2026-06-23 19:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:51:23` | `cowrie.session.connect` |
| `2026-06-23 19:51:23` | `cowrie.client.version` |
| `2026-06-23 19:51:23` | `cowrie.client.kex` |
| `2026-06-23 19:51:23` | `cowrie.login.success` |
| `2026-06-23 19:51:24` | `cowrie.session.params` |
| `2026-06-23 19:51:24` | `cowrie.command.input` |
| `2026-06-23 19:51:24` | `cowrie.log.closed` |
| `2026-06-23 19:51:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51cfd7a82672

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:52 |
| **Last Seen** | 2026-06-23 19:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:52:21` | `cowrie.session.connect` |
| `2026-06-23 19:52:21` | `cowrie.client.version` |
| `2026-06-23 19:52:21` | `cowrie.client.kex` |
| `2026-06-23 19:52:21` | `cowrie.login.success` |
| `2026-06-23 19:52:22` | `cowrie.session.params` |
| `2026-06-23 19:52:22` | `cowrie.command.input` |
| `2026-06-23 19:52:22` | `cowrie.log.closed` |
| `2026-06-23 19:52:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dc3f7f20e05

| Field | Detail |
|---|---|
| **Source IP** | `61.240.17[.]66` |
| **First Seen** | 2026-06-23 19:52 |
| **Last Seen** | 2026-06-23 19:57 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:52:22` | `cowrie.session.connect` |
| `2026-06-23 19:52:22` | `cowrie.client.version` |
| `2026-06-23 19:52:22` | `cowrie.client.kex` |
| `2026-06-23 19:52:23` | `cowrie.login.success` |
| `2026-06-23 19:57:23` | `cowrie.session.file_upload` |
| `2026-06-23 19:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.240.17[.]66` to AbuseIPDB if not already reported
- [ ] Block `61.240.17[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f7ac1678ee0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:53 |
| **Last Seen** | 2026-06-23 19:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:53:18` | `cowrie.session.connect` |
| `2026-06-23 19:53:18` | `cowrie.client.version` |
| `2026-06-23 19:53:18` | `cowrie.client.kex` |
| `2026-06-23 19:53:19` | `cowrie.login.success` |
| `2026-06-23 19:53:19` | `cowrie.session.params` |
| `2026-06-23 19:53:19` | `cowrie.command.input` |
| `2026-06-23 19:53:20` | `cowrie.log.closed` |
| `2026-06-23 19:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28e60517cae6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:54 |
| **Last Seen** | 2026-06-23 19:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:54:17` | `cowrie.session.connect` |
| `2026-06-23 19:54:17` | `cowrie.client.version` |
| `2026-06-23 19:54:17` | `cowrie.client.kex` |
| `2026-06-23 19:54:17` | `cowrie.login.success` |
| `2026-06-23 19:54:18` | `cowrie.session.params` |
| `2026-06-23 19:54:18` | `cowrie.command.input` |
| `2026-06-23 19:54:18` | `cowrie.log.closed` |
| `2026-06-23 19:54:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f22b60e5067b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:55 |
| **Last Seen** | 2026-06-23 19:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:55:15` | `cowrie.session.connect` |
| `2026-06-23 19:55:15` | `cowrie.client.version` |
| `2026-06-23 19:55:15` | `cowrie.client.kex` |
| `2026-06-23 19:55:16` | `cowrie.login.success` |
| `2026-06-23 19:55:16` | `cowrie.session.params` |
| `2026-06-23 19:55:16` | `cowrie.command.input` |
| `2026-06-23 19:55:17` | `cowrie.log.closed` |
| `2026-06-23 19:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a616494b752a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:56 |
| **Last Seen** | 2026-06-23 19:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:56:13` | `cowrie.session.connect` |
| `2026-06-23 19:56:13` | `cowrie.client.version` |
| `2026-06-23 19:56:14` | `cowrie.client.kex` |
| `2026-06-23 19:56:14` | `cowrie.login.success` |
| `2026-06-23 19:56:15` | `cowrie.session.params` |
| `2026-06-23 19:56:15` | `cowrie.command.input` |
| `2026-06-23 19:56:15` | `cowrie.log.closed` |
| `2026-06-23 19:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4506ecfce515

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:57 |
| **Last Seen** | 2026-06-23 19:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:57:11` | `cowrie.session.connect` |
| `2026-06-23 19:57:11` | `cowrie.client.version` |
| `2026-06-23 19:57:11` | `cowrie.client.kex` |
| `2026-06-23 19:57:11` | `cowrie.login.success` |
| `2026-06-23 19:57:12` | `cowrie.session.params` |
| `2026-06-23 19:57:12` | `cowrie.command.input` |
| `2026-06-23 19:57:12` | `cowrie.log.closed` |
| `2026-06-23 19:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0abd6600767

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:58 |
| **Last Seen** | 2026-06-23 19:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:58:07` | `cowrie.session.connect` |
| `2026-06-23 19:58:07` | `cowrie.client.version` |
| `2026-06-23 19:58:07` | `cowrie.client.kex` |
| `2026-06-23 19:58:07` | `cowrie.login.success` |
| `2026-06-23 19:58:08` | `cowrie.session.params` |
| `2026-06-23 19:58:08` | `cowrie.command.input` |
| `2026-06-23 19:58:08` | `cowrie.log.closed` |
| `2026-06-23 19:58:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff0608728d9a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 19:59 |
| **Last Seen** | 2026-06-23 19:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:59:04` | `cowrie.session.connect` |
| `2026-06-23 19:59:04` | `cowrie.client.version` |
| `2026-06-23 19:59:04` | `cowrie.client.kex` |
| `2026-06-23 19:59:05` | `cowrie.login.success` |
| `2026-06-23 19:59:06` | `cowrie.session.params` |
| `2026-06-23 19:59:06` | `cowrie.command.input` |
| `2026-06-23 19:59:06` | `cowrie.log.closed` |
| `2026-06-23 19:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2ad5a33d3de

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 19:59 |
| **Last Seen** | 2026-06-23 19:59 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:59:06` | `cowrie.session.connect` |
| `2026-06-23 19:59:06` | `cowrie.client.version` |
| `2026-06-23 19:59:06` | `cowrie.client.kex` |
| `2026-06-23 19:59:13` | `cowrie.login.success` |
| `2026-06-23 19:59:17` | `cowrie.session.params` |
| `2026-06-23 19:59:17` | `cowrie.command.input` |
| `2026-06-23 19:59:18` | `cowrie.log.closed` |
| `2026-06-23 19:59:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c69fe2cd54e9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:00 |
| **Last Seen** | 2026-06-23 20:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:00:04` | `cowrie.session.connect` |
| `2026-06-23 20:00:04` | `cowrie.client.version` |
| `2026-06-23 20:00:04` | `cowrie.client.kex` |
| `2026-06-23 20:00:04` | `cowrie.login.success` |
| `2026-06-23 20:00:05` | `cowrie.session.params` |
| `2026-06-23 20:00:05` | `cowrie.command.input` |
| `2026-06-23 20:00:05` | `cowrie.log.closed` |
| `2026-06-23 20:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a9da9b21b44

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:00 |
| **Last Seen** | 2026-06-23 20:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:00:52` | `cowrie.session.connect` |
| `2026-06-23 20:00:52` | `cowrie.client.version` |
| `2026-06-23 20:00:52` | `cowrie.client.kex` |
| `2026-06-23 20:00:53` | `cowrie.login.success` |
| `2026-06-23 20:00:53` | `cowrie.session.params` |
| `2026-06-23 20:00:53` | `cowrie.command.input` |
| `2026-06-23 20:00:53` | `cowrie.log.closed` |
| `2026-06-23 20:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5cc8f8ddda2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:01 |
| **Last Seen** | 2026-06-23 20:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:01:38` | `cowrie.session.connect` |
| `2026-06-23 20:01:38` | `cowrie.client.version` |
| `2026-06-23 20:01:38` | `cowrie.client.kex` |
| `2026-06-23 20:01:39` | `cowrie.login.success` |
| `2026-06-23 20:01:40` | `cowrie.session.params` |
| `2026-06-23 20:01:40` | `cowrie.command.input` |
| `2026-06-23 20:01:40` | `cowrie.log.closed` |
| `2026-06-23 20:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b064a3113a1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:02 |
| **Last Seen** | 2026-06-23 20:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:02:23` | `cowrie.session.connect` |
| `2026-06-23 20:02:23` | `cowrie.client.version` |
| `2026-06-23 20:02:23` | `cowrie.client.kex` |
| `2026-06-23 20:02:23` | `cowrie.login.success` |
| `2026-06-23 20:02:24` | `cowrie.session.params` |
| `2026-06-23 20:02:24` | `cowrie.command.input` |
| `2026-06-23 20:02:24` | `cowrie.log.closed` |
| `2026-06-23 20:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8897a30f8995

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:03 |
| **Last Seen** | 2026-06-23 20:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:03:07` | `cowrie.session.connect` |
| `2026-06-23 20:03:07` | `cowrie.client.version` |
| `2026-06-23 20:03:08` | `cowrie.client.kex` |
| `2026-06-23 20:03:08` | `cowrie.login.success` |
| `2026-06-23 20:03:09` | `cowrie.session.params` |
| `2026-06-23 20:03:09` | `cowrie.command.input` |
| `2026-06-23 20:03:09` | `cowrie.log.closed` |
| `2026-06-23 20:03:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26a084415568

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:03 |
| **Last Seen** | 2026-06-23 20:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:03:52` | `cowrie.session.connect` |
| `2026-06-23 20:03:52` | `cowrie.client.version` |
| `2026-06-23 20:03:52` | `cowrie.client.kex` |
| `2026-06-23 20:03:52` | `cowrie.login.success` |
| `2026-06-23 20:03:53` | `cowrie.session.params` |
| `2026-06-23 20:03:53` | `cowrie.command.input` |
| `2026-06-23 20:03:53` | `cowrie.log.closed` |
| `2026-06-23 20:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3540620d6996

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:04 |
| **Last Seen** | 2026-06-23 20:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:04:37` | `cowrie.session.connect` |
| `2026-06-23 20:04:37` | `cowrie.client.version` |
| `2026-06-23 20:04:37` | `cowrie.client.kex` |
| `2026-06-23 20:04:38` | `cowrie.login.success` |
| `2026-06-23 20:04:38` | `cowrie.session.params` |
| `2026-06-23 20:04:38` | `cowrie.command.input` |
| `2026-06-23 20:04:39` | `cowrie.log.closed` |
| `2026-06-23 20:04:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0de740423b27

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:05 |
| **Last Seen** | 2026-06-23 20:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:05:24` | `cowrie.session.connect` |
| `2026-06-23 20:05:24` | `cowrie.client.version` |
| `2026-06-23 20:05:24` | `cowrie.client.kex` |
| `2026-06-23 20:05:24` | `cowrie.login.success` |
| `2026-06-23 20:05:25` | `cowrie.session.params` |
| `2026-06-23 20:05:25` | `cowrie.command.input` |
| `2026-06-23 20:05:25` | `cowrie.log.closed` |
| `2026-06-23 20:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1288f85e9c92

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:06 |
| **Last Seen** | 2026-06-23 20:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:06:12` | `cowrie.session.connect` |
| `2026-06-23 20:06:12` | `cowrie.client.version` |
| `2026-06-23 20:06:12` | `cowrie.client.kex` |
| `2026-06-23 20:06:12` | `cowrie.login.success` |
| `2026-06-23 20:06:13` | `cowrie.session.params` |
| `2026-06-23 20:06:13` | `cowrie.command.input` |
| `2026-06-23 20:06:13` | `cowrie.log.closed` |
| `2026-06-23 20:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c34ab55a481

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:07 |
| **Last Seen** | 2026-06-23 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:07:00` | `cowrie.session.connect` |
| `2026-06-23 20:07:00` | `cowrie.client.version` |
| `2026-06-23 20:07:00` | `cowrie.client.kex` |
| `2026-06-23 20:07:01` | `cowrie.login.success` |
| `2026-06-23 20:07:01` | `cowrie.session.params` |
| `2026-06-23 20:07:01` | `cowrie.command.input` |
| `2026-06-23 20:07:02` | `cowrie.log.closed` |
| `2026-06-23 20:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92405d4e1057

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:07 |
| **Last Seen** | 2026-06-23 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:07:49` | `cowrie.session.connect` |
| `2026-06-23 20:07:49` | `cowrie.client.version` |
| `2026-06-23 20:07:49` | `cowrie.client.kex` |
| `2026-06-23 20:07:50` | `cowrie.login.success` |
| `2026-06-23 20:07:50` | `cowrie.session.params` |
| `2026-06-23 20:07:50` | `cowrie.command.input` |
| `2026-06-23 20:07:51` | `cowrie.log.closed` |
| `2026-06-23 20:07:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7006f7222ee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:08 |
| **Last Seen** | 2026-06-23 20:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:08:37` | `cowrie.session.connect` |
| `2026-06-23 20:08:37` | `cowrie.client.version` |
| `2026-06-23 20:08:38` | `cowrie.client.kex` |
| `2026-06-23 20:08:38` | `cowrie.login.success` |
| `2026-06-23 20:08:39` | `cowrie.session.params` |
| `2026-06-23 20:08:39` | `cowrie.command.input` |
| `2026-06-23 20:08:39` | `cowrie.log.closed` |
| `2026-06-23 20:08:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b9c1941cceb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:09 |
| **Last Seen** | 2026-06-23 20:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:09:27` | `cowrie.session.connect` |
| `2026-06-23 20:09:27` | `cowrie.client.version` |
| `2026-06-23 20:09:27` | `cowrie.client.kex` |
| `2026-06-23 20:09:27` | `cowrie.login.success` |
| `2026-06-23 20:09:28` | `cowrie.session.params` |
| `2026-06-23 20:09:28` | `cowrie.command.input` |
| `2026-06-23 20:09:28` | `cowrie.log.closed` |
| `2026-06-23 20:09:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f418cc86699

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:10 |
| **Last Seen** | 2026-06-23 20:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:10:12` | `cowrie.session.connect` |
| `2026-06-23 20:10:12` | `cowrie.client.version` |
| `2026-06-23 20:10:12` | `cowrie.client.kex` |
| `2026-06-23 20:10:12` | `cowrie.login.success` |
| `2026-06-23 20:10:13` | `cowrie.session.params` |
| `2026-06-23 20:10:13` | `cowrie.command.input` |
| `2026-06-23 20:10:13` | `cowrie.log.closed` |
| `2026-06-23 20:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8210f354e73

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:10 |
| **Last Seen** | 2026-06-23 20:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:10:57` | `cowrie.session.connect` |
| `2026-06-23 20:10:57` | `cowrie.client.version` |
| `2026-06-23 20:10:57` | `cowrie.client.kex` |
| `2026-06-23 20:10:57` | `cowrie.login.success` |
| `2026-06-23 20:10:58` | `cowrie.session.params` |
| `2026-06-23 20:10:58` | `cowrie.command.input` |
| `2026-06-23 20:10:58` | `cowrie.log.closed` |
| `2026-06-23 20:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a583264be1ee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:11 |
| **Last Seen** | 2026-06-23 20:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:11:44` | `cowrie.session.connect` |
| `2026-06-23 20:11:44` | `cowrie.client.version` |
| `2026-06-23 20:11:44` | `cowrie.client.kex` |
| `2026-06-23 20:11:44` | `cowrie.login.success` |
| `2026-06-23 20:11:45` | `cowrie.session.params` |
| `2026-06-23 20:11:45` | `cowrie.command.input` |
| `2026-06-23 20:11:45` | `cowrie.log.closed` |
| `2026-06-23 20:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e693d95bdad

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:12 |
| **Last Seen** | 2026-06-23 20:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:12:33` | `cowrie.session.connect` |
| `2026-06-23 20:12:33` | `cowrie.client.version` |
| `2026-06-23 20:12:33` | `cowrie.client.kex` |
| `2026-06-23 20:12:33` | `cowrie.login.success` |
| `2026-06-23 20:12:34` | `cowrie.session.params` |
| `2026-06-23 20:12:34` | `cowrie.command.input` |
| `2026-06-23 20:12:34` | `cowrie.log.closed` |
| `2026-06-23 20:12:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7a5a5f4d053

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:13 |
| **Last Seen** | 2026-06-23 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:13:22` | `cowrie.session.connect` |
| `2026-06-23 20:13:22` | `cowrie.client.version` |
| `2026-06-23 20:13:22` | `cowrie.client.kex` |
| `2026-06-23 20:13:22` | `cowrie.login.success` |
| `2026-06-23 20:13:23` | `cowrie.session.params` |
| `2026-06-23 20:13:23` | `cowrie.command.input` |
| `2026-06-23 20:13:23` | `cowrie.log.closed` |
| `2026-06-23 20:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6d9ff93cb0e

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 20:13 |
| **Last Seen** | 2026-06-23 20:13 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:13:36` | `cowrie.session.connect` |
| `2026-06-23 20:13:38` | `cowrie.client.version` |
| `2026-06-23 20:13:38` | `cowrie.client.kex` |
| `2026-06-23 20:13:45` | `cowrie.login.success` |
| `2026-06-23 20:13:48` | `cowrie.session.params` |
| `2026-06-23 20:13:48` | `cowrie.command.input` |
| `2026-06-23 20:13:50` | `cowrie.log.closed` |
| `2026-06-23 20:13:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f15815cea701

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:14 |
| **Last Seen** | 2026-06-23 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:14:11` | `cowrie.session.connect` |
| `2026-06-23 20:14:11` | `cowrie.client.version` |
| `2026-06-23 20:14:11` | `cowrie.client.kex` |
| `2026-06-23 20:14:11` | `cowrie.login.success` |
| `2026-06-23 20:14:12` | `cowrie.session.params` |
| `2026-06-23 20:14:12` | `cowrie.command.input` |
| `2026-06-23 20:14:12` | `cowrie.log.closed` |
| `2026-06-23 20:14:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71678508a344

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:14 |
| **Last Seen** | 2026-06-23 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:14:59` | `cowrie.session.connect` |
| `2026-06-23 20:14:59` | `cowrie.client.version` |
| `2026-06-23 20:14:59` | `cowrie.client.kex` |
| `2026-06-23 20:15:00` | `cowrie.login.success` |
| `2026-06-23 20:15:00` | `cowrie.session.params` |
| `2026-06-23 20:15:00` | `cowrie.command.input` |
| `2026-06-23 20:15:00` | `cowrie.log.closed` |
| `2026-06-23 20:15:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a5a2a77de6e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:15 |
| **Last Seen** | 2026-06-23 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:15:47` | `cowrie.session.connect` |
| `2026-06-23 20:15:47` | `cowrie.client.version` |
| `2026-06-23 20:15:47` | `cowrie.client.kex` |
| `2026-06-23 20:15:47` | `cowrie.login.success` |
| `2026-06-23 20:15:48` | `cowrie.session.params` |
| `2026-06-23 20:15:48` | `cowrie.command.input` |
| `2026-06-23 20:15:48` | `cowrie.log.closed` |
| `2026-06-23 20:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f26b38b7027d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:16 |
| **Last Seen** | 2026-06-23 20:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:16:35` | `cowrie.session.connect` |
| `2026-06-23 20:16:35` | `cowrie.client.version` |
| `2026-06-23 20:16:35` | `cowrie.client.kex` |
| `2026-06-23 20:16:35` | `cowrie.login.success` |
| `2026-06-23 20:16:36` | `cowrie.session.params` |
| `2026-06-23 20:16:36` | `cowrie.command.input` |
| `2026-06-23 20:16:36` | `cowrie.log.closed` |
| `2026-06-23 20:16:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee0687009f7a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:17 |
| **Last Seen** | 2026-06-23 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:17:24` | `cowrie.session.connect` |
| `2026-06-23 20:17:24` | `cowrie.client.version` |
| `2026-06-23 20:17:24` | `cowrie.client.kex` |
| `2026-06-23 20:17:24` | `cowrie.login.success` |
| `2026-06-23 20:17:25` | `cowrie.session.params` |
| `2026-06-23 20:17:25` | `cowrie.command.input` |
| `2026-06-23 20:17:25` | `cowrie.log.closed` |
| `2026-06-23 20:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdb6169a695d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:18 |
| **Last Seen** | 2026-06-23 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:18:14` | `cowrie.session.connect` |
| `2026-06-23 20:18:14` | `cowrie.client.version` |
| `2026-06-23 20:18:14` | `cowrie.client.kex` |
| `2026-06-23 20:18:15` | `cowrie.login.success` |
| `2026-06-23 20:18:16` | `cowrie.session.params` |
| `2026-06-23 20:18:16` | `cowrie.command.input` |
| `2026-06-23 20:18:16` | `cowrie.log.closed` |
| `2026-06-23 20:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4886507a94b0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:19 |
| **Last Seen** | 2026-06-23 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:19:04` | `cowrie.session.connect` |
| `2026-06-23 20:19:04` | `cowrie.client.version` |
| `2026-06-23 20:19:04` | `cowrie.client.kex` |
| `2026-06-23 20:19:05` | `cowrie.login.success` |
| `2026-06-23 20:19:06` | `cowrie.session.params` |
| `2026-06-23 20:19:06` | `cowrie.command.input` |
| `2026-06-23 20:19:06` | `cowrie.log.closed` |
| `2026-06-23 20:19:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00a3c53e4c13

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:19 |
| **Last Seen** | 2026-06-23 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:19:54` | `cowrie.session.connect` |
| `2026-06-23 20:19:54` | `cowrie.client.version` |
| `2026-06-23 20:19:55` | `cowrie.client.kex` |
| `2026-06-23 20:19:55` | `cowrie.login.success` |
| `2026-06-23 20:19:56` | `cowrie.session.params` |
| `2026-06-23 20:19:56` | `cowrie.command.input` |
| `2026-06-23 20:19:56` | `cowrie.log.closed` |
| `2026-06-23 20:19:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fef9d72ae23

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:20 |
| **Last Seen** | 2026-06-23 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:20:43` | `cowrie.session.connect` |
| `2026-06-23 20:20:43` | `cowrie.client.version` |
| `2026-06-23 20:20:44` | `cowrie.client.kex` |
| `2026-06-23 20:20:44` | `cowrie.login.success` |
| `2026-06-23 20:20:45` | `cowrie.session.params` |
| `2026-06-23 20:20:45` | `cowrie.command.input` |
| `2026-06-23 20:20:45` | `cowrie.log.closed` |
| `2026-06-23 20:20:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56526c21de1e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:21 |
| **Last Seen** | 2026-06-23 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:21:33` | `cowrie.session.connect` |
| `2026-06-23 20:21:33` | `cowrie.client.version` |
| `2026-06-23 20:21:33` | `cowrie.client.kex` |
| `2026-06-23 20:21:33` | `cowrie.login.success` |
| `2026-06-23 20:21:34` | `cowrie.session.params` |
| `2026-06-23 20:21:34` | `cowrie.command.input` |
| `2026-06-23 20:21:34` | `cowrie.log.closed` |
| `2026-06-23 20:21:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2e161f08022

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:22 |
| **Last Seen** | 2026-06-23 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:22:22` | `cowrie.session.connect` |
| `2026-06-23 20:22:22` | `cowrie.client.version` |
| `2026-06-23 20:22:22` | `cowrie.client.kex` |
| `2026-06-23 20:22:22` | `cowrie.login.success` |
| `2026-06-23 20:22:23` | `cowrie.session.params` |
| `2026-06-23 20:22:23` | `cowrie.command.input` |
| `2026-06-23 20:22:23` | `cowrie.log.closed` |
| `2026-06-23 20:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64f7d92ff3a8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:23 |
| **Last Seen** | 2026-06-23 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:23:10` | `cowrie.session.connect` |
| `2026-06-23 20:23:10` | `cowrie.client.version` |
| `2026-06-23 20:23:10` | `cowrie.client.kex` |
| `2026-06-23 20:23:11` | `cowrie.login.success` |
| `2026-06-23 20:23:12` | `cowrie.session.params` |
| `2026-06-23 20:23:12` | `cowrie.command.input` |
| `2026-06-23 20:23:12` | `cowrie.log.closed` |
| `2026-06-23 20:23:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca6d0a167f5f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:23 |
| **Last Seen** | 2026-06-23 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:23:58` | `cowrie.session.connect` |
| `2026-06-23 20:23:58` | `cowrie.client.version` |
| `2026-06-23 20:23:58` | `cowrie.client.kex` |
| `2026-06-23 20:23:59` | `cowrie.login.success` |
| `2026-06-23 20:23:59` | `cowrie.session.params` |
| `2026-06-23 20:23:59` | `cowrie.command.input` |
| `2026-06-23 20:24:00` | `cowrie.log.closed` |
| `2026-06-23 20:24:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-add2f94287c4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:24 |
| **Last Seen** | 2026-06-23 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:24:47` | `cowrie.session.connect` |
| `2026-06-23 20:24:47` | `cowrie.client.version` |
| `2026-06-23 20:24:47` | `cowrie.client.kex` |
| `2026-06-23 20:24:48` | `cowrie.login.success` |
| `2026-06-23 20:24:49` | `cowrie.session.params` |
| `2026-06-23 20:24:49` | `cowrie.command.input` |
| `2026-06-23 20:24:49` | `cowrie.log.closed` |
| `2026-06-23 20:24:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-828300ca6ca8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:25 |
| **Last Seen** | 2026-06-23 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:25:37` | `cowrie.session.connect` |
| `2026-06-23 20:25:37` | `cowrie.client.version` |
| `2026-06-23 20:25:37` | `cowrie.client.kex` |
| `2026-06-23 20:25:37` | `cowrie.login.success` |
| `2026-06-23 20:25:38` | `cowrie.session.params` |
| `2026-06-23 20:25:38` | `cowrie.command.input` |
| `2026-06-23 20:25:38` | `cowrie.log.closed` |
| `2026-06-23 20:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bae88b7d7f3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:26 |
| **Last Seen** | 2026-06-23 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:26:26` | `cowrie.session.connect` |
| `2026-06-23 20:26:26` | `cowrie.client.version` |
| `2026-06-23 20:26:26` | `cowrie.client.kex` |
| `2026-06-23 20:26:27` | `cowrie.login.success` |
| `2026-06-23 20:26:27` | `cowrie.session.params` |
| `2026-06-23 20:26:27` | `cowrie.command.input` |
| `2026-06-23 20:26:27` | `cowrie.log.closed` |
| `2026-06-23 20:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25ca21af0a00

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:27 |
| **Last Seen** | 2026-06-23 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:27:15` | `cowrie.session.connect` |
| `2026-06-23 20:27:15` | `cowrie.client.version` |
| `2026-06-23 20:27:15` | `cowrie.client.kex` |
| `2026-06-23 20:27:15` | `cowrie.login.success` |
| `2026-06-23 20:27:16` | `cowrie.session.params` |
| `2026-06-23 20:27:16` | `cowrie.command.input` |
| `2026-06-23 20:27:16` | `cowrie.log.closed` |
| `2026-06-23 20:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-199df93c23c3

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 20:27 |
| **Last Seen** | 2026-06-23 20:28 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:27:58` | `cowrie.session.connect` |
| `2026-06-23 20:27:59` | `cowrie.client.version` |
| `2026-06-23 20:27:59` | `cowrie.client.kex` |
| `2026-06-23 20:28:06` | `cowrie.login.success` |
| `2026-06-23 20:28:09` | `cowrie.session.params` |
| `2026-06-23 20:28:09` | `cowrie.command.input` |
| `2026-06-23 20:28:12` | `cowrie.log.closed` |
| `2026-06-23 20:28:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a6c4558f1a2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:28 |
| **Last Seen** | 2026-06-23 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:28:03` | `cowrie.session.connect` |
| `2026-06-23 20:28:03` | `cowrie.client.version` |
| `2026-06-23 20:28:03` | `cowrie.client.kex` |
| `2026-06-23 20:28:03` | `cowrie.login.success` |
| `2026-06-23 20:28:04` | `cowrie.session.params` |
| `2026-06-23 20:28:04` | `cowrie.command.input` |
| `2026-06-23 20:28:04` | `cowrie.log.closed` |
| `2026-06-23 20:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2ec5859a8a0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:28 |
| **Last Seen** | 2026-06-23 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:28:51` | `cowrie.session.connect` |
| `2026-06-23 20:28:51` | `cowrie.client.version` |
| `2026-06-23 20:28:51` | `cowrie.client.kex` |
| `2026-06-23 20:28:52` | `cowrie.login.success` |
| `2026-06-23 20:28:53` | `cowrie.session.params` |
| `2026-06-23 20:28:53` | `cowrie.command.input` |
| `2026-06-23 20:28:53` | `cowrie.log.closed` |
| `2026-06-23 20:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dd94b81e0fd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:29 |
| **Last Seen** | 2026-06-23 20:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:29:39` | `cowrie.session.connect` |
| `2026-06-23 20:29:39` | `cowrie.client.version` |
| `2026-06-23 20:29:39` | `cowrie.client.kex` |
| `2026-06-23 20:29:40` | `cowrie.login.success` |
| `2026-06-23 20:29:40` | `cowrie.session.params` |
| `2026-06-23 20:29:40` | `cowrie.command.input` |
| `2026-06-23 20:29:40` | `cowrie.log.closed` |
| `2026-06-23 20:29:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61a3d9002aef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:30 |
| **Last Seen** | 2026-06-23 20:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:30:27` | `cowrie.session.connect` |
| `2026-06-23 20:30:27` | `cowrie.client.version` |
| `2026-06-23 20:30:27` | `cowrie.client.kex` |
| `2026-06-23 20:30:28` | `cowrie.login.success` |
| `2026-06-23 20:30:29` | `cowrie.session.params` |
| `2026-06-23 20:30:29` | `cowrie.command.input` |
| `2026-06-23 20:30:29` | `cowrie.log.closed` |
| `2026-06-23 20:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b85c0f816a9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:31 |
| **Last Seen** | 2026-06-23 20:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:31:16` | `cowrie.session.connect` |
| `2026-06-23 20:31:16` | `cowrie.client.version` |
| `2026-06-23 20:31:16` | `cowrie.client.kex` |
| `2026-06-23 20:31:16` | `cowrie.login.success` |
| `2026-06-23 20:31:17` | `cowrie.session.params` |
| `2026-06-23 20:31:17` | `cowrie.command.input` |
| `2026-06-23 20:31:17` | `cowrie.log.closed` |
| `2026-06-23 20:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e45de4c0e7a6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:32 |
| **Last Seen** | 2026-06-23 20:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:32:05` | `cowrie.session.connect` |
| `2026-06-23 20:32:05` | `cowrie.client.version` |
| `2026-06-23 20:32:05` | `cowrie.client.kex` |
| `2026-06-23 20:32:05` | `cowrie.login.success` |
| `2026-06-23 20:32:06` | `cowrie.session.params` |
| `2026-06-23 20:32:06` | `cowrie.command.input` |
| `2026-06-23 20:32:06` | `cowrie.log.closed` |
| `2026-06-23 20:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e2dd92aaea6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:32 |
| **Last Seen** | 2026-06-23 20:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:32:54` | `cowrie.session.connect` |
| `2026-06-23 20:32:54` | `cowrie.client.version` |
| `2026-06-23 20:32:54` | `cowrie.client.kex` |
| `2026-06-23 20:32:54` | `cowrie.login.success` |
| `2026-06-23 20:32:55` | `cowrie.session.params` |
| `2026-06-23 20:32:55` | `cowrie.command.input` |
| `2026-06-23 20:32:55` | `cowrie.log.closed` |
| `2026-06-23 20:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a7e2d81b2d2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:33 |
| **Last Seen** | 2026-06-23 20:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:33:42` | `cowrie.session.connect` |
| `2026-06-23 20:33:42` | `cowrie.client.version` |
| `2026-06-23 20:33:42` | `cowrie.client.kex` |
| `2026-06-23 20:33:43` | `cowrie.login.success` |
| `2026-06-23 20:33:44` | `cowrie.session.params` |
| `2026-06-23 20:33:44` | `cowrie.command.input` |
| `2026-06-23 20:33:44` | `cowrie.log.closed` |
| `2026-06-23 20:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed542a81b6f4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:34 |
| **Last Seen** | 2026-06-23 20:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:34:30` | `cowrie.session.connect` |
| `2026-06-23 20:34:30` | `cowrie.client.version` |
| `2026-06-23 20:34:30` | `cowrie.client.kex` |
| `2026-06-23 20:34:31` | `cowrie.login.success` |
| `2026-06-23 20:34:31` | `cowrie.session.params` |
| `2026-06-23 20:34:31` | `cowrie.command.input` |
| `2026-06-23 20:34:31` | `cowrie.log.closed` |
| `2026-06-23 20:34:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a76defe796e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:35 |
| **Last Seen** | 2026-06-23 20:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:35:17` | `cowrie.session.connect` |
| `2026-06-23 20:35:17` | `cowrie.client.version` |
| `2026-06-23 20:35:17` | `cowrie.client.kex` |
| `2026-06-23 20:35:18` | `cowrie.login.success` |
| `2026-06-23 20:35:19` | `cowrie.session.params` |
| `2026-06-23 20:35:19` | `cowrie.command.input` |
| `2026-06-23 20:35:19` | `cowrie.log.closed` |
| `2026-06-23 20:35:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff3927e8a0c8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:36 |
| **Last Seen** | 2026-06-23 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:36:03` | `cowrie.session.connect` |
| `2026-06-23 20:36:03` | `cowrie.client.version` |
| `2026-06-23 20:36:04` | `cowrie.client.kex` |
| `2026-06-23 20:36:04` | `cowrie.login.success` |
| `2026-06-23 20:36:05` | `cowrie.session.params` |
| `2026-06-23 20:36:05` | `cowrie.command.input` |
| `2026-06-23 20:36:05` | `cowrie.log.closed` |
| `2026-06-23 20:36:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44651624ea36

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:36 |
| **Last Seen** | 2026-06-23 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:36:50` | `cowrie.session.connect` |
| `2026-06-23 20:36:50` | `cowrie.client.version` |
| `2026-06-23 20:36:50` | `cowrie.client.kex` |
| `2026-06-23 20:36:50` | `cowrie.login.success` |
| `2026-06-23 20:36:51` | `cowrie.session.params` |
| `2026-06-23 20:36:51` | `cowrie.command.input` |
| `2026-06-23 20:36:51` | `cowrie.log.closed` |
| `2026-06-23 20:36:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4109dc5124e

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]101` |
| **First Seen** | 2026-06-23 20:37 |
| **Last Seen** | 2026-06-23 20:37 |
| **Session Duration** | 21s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:37:31` | `cowrie.session.connect` |
| `2026-06-23 20:37:31` | `cowrie.client.version` |
| `2026-06-23 20:37:31` | `cowrie.client.kex` |
| `2026-06-23 20:37:32` | `cowrie.client.fingerprint` |
| `2026-06-23 20:37:32` | `cowrie.login.failed` |
| `2026-06-23 20:37:32` | `cowrie.login.success` |
| `2026-06-23 20:37:51` | `cowrie.direct-tcpip.request` |
| `2026-06-23 20:37:51` | `cowrie.direct-tcpip.ja4` |
| `2026-06-23 20:37:51` | `cowrie.direct-tcpip.data` |
| `2026-06-23 20:37:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]101` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa3e7f22451e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:37 |
| **Last Seen** | 2026-06-23 20:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:37:38` | `cowrie.session.connect` |
| `2026-06-23 20:37:38` | `cowrie.client.version` |
| `2026-06-23 20:37:38` | `cowrie.client.kex` |
| `2026-06-23 20:37:38` | `cowrie.login.success` |
| `2026-06-23 20:37:39` | `cowrie.session.params` |
| `2026-06-23 20:37:39` | `cowrie.command.input` |
| `2026-06-23 20:37:39` | `cowrie.log.closed` |
| `2026-06-23 20:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa59bf5b3293

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-23 20:37 |
| **Last Seen** | 2026-06-23 20:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:37:54` | `cowrie.session.connect` |
| `2026-06-23 20:37:54` | `cowrie.client.version` |
| `2026-06-23 20:37:54` | `cowrie.client.kex` |
| `2026-06-23 20:37:55` | `cowrie.login.success` |
| `2026-06-23 20:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21ce1ea3ebf7

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-23 20:37 |
| **Last Seen** | 2026-06-23 20:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:37:54` | `cowrie.session.connect` |
| `2026-06-23 20:37:54` | `cowrie.client.version` |
| `2026-06-23 20:37:54` | `cowrie.client.kex` |
| `2026-06-23 20:37:55` | `cowrie.login.success` |
| `2026-06-23 20:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e469972c645c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:38 |
| **Last Seen** | 2026-06-23 20:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:38:27` | `cowrie.session.connect` |
| `2026-06-23 20:38:27` | `cowrie.client.version` |
| `2026-06-23 20:38:27` | `cowrie.client.kex` |
| `2026-06-23 20:38:27` | `cowrie.login.success` |
| `2026-06-23 20:38:28` | `cowrie.session.params` |
| `2026-06-23 20:38:28` | `cowrie.command.input` |
| `2026-06-23 20:38:28` | `cowrie.log.closed` |
| `2026-06-23 20:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e73ca80404d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:39 |
| **Last Seen** | 2026-06-23 20:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:39:17` | `cowrie.session.connect` |
| `2026-06-23 20:39:17` | `cowrie.client.version` |
| `2026-06-23 20:39:17` | `cowrie.client.kex` |
| `2026-06-23 20:39:17` | `cowrie.login.success` |
| `2026-06-23 20:39:18` | `cowrie.session.params` |
| `2026-06-23 20:39:18` | `cowrie.command.input` |
| `2026-06-23 20:39:18` | `cowrie.log.closed` |
| `2026-06-23 20:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-021e54e0cfcf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:40 |
| **Last Seen** | 2026-06-23 20:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:40:06` | `cowrie.session.connect` |
| `2026-06-23 20:40:06` | `cowrie.client.version` |
| `2026-06-23 20:40:06` | `cowrie.client.kex` |
| `2026-06-23 20:40:07` | `cowrie.login.success` |
| `2026-06-23 20:40:08` | `cowrie.session.params` |
| `2026-06-23 20:40:08` | `cowrie.command.input` |
| `2026-06-23 20:40:08` | `cowrie.log.closed` |
| `2026-06-23 20:40:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb9af9e6cf2c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:40 |
| **Last Seen** | 2026-06-23 20:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:40:55` | `cowrie.session.connect` |
| `2026-06-23 20:40:55` | `cowrie.client.version` |
| `2026-06-23 20:40:55` | `cowrie.client.kex` |
| `2026-06-23 20:40:55` | `cowrie.login.success` |
| `2026-06-23 20:40:56` | `cowrie.session.params` |
| `2026-06-23 20:40:56` | `cowrie.command.input` |
| `2026-06-23 20:40:56` | `cowrie.log.closed` |
| `2026-06-23 20:40:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6737a5d3e9e1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:41 |
| **Last Seen** | 2026-06-23 20:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:41:43` | `cowrie.session.connect` |
| `2026-06-23 20:41:43` | `cowrie.client.version` |
| `2026-06-23 20:41:43` | `cowrie.client.kex` |
| `2026-06-23 20:41:43` | `cowrie.login.success` |
| `2026-06-23 20:41:44` | `cowrie.session.params` |
| `2026-06-23 20:41:44` | `cowrie.command.input` |
| `2026-06-23 20:41:44` | `cowrie.log.closed` |
| `2026-06-23 20:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75e51675d3c7

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 20:42 |
| **Last Seen** | 2026-06-23 20:42 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:42:24` | `cowrie.session.connect` |
| `2026-06-23 20:42:25` | `cowrie.client.version` |
| `2026-06-23 20:42:25` | `cowrie.client.kex` |
| `2026-06-23 20:42:32` | `cowrie.login.success` |
| `2026-06-23 20:42:36` | `cowrie.session.params` |
| `2026-06-23 20:42:36` | `cowrie.command.input` |
| `2026-06-23 20:42:37` | `cowrie.log.closed` |
| `2026-06-23 20:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9636823ea7a5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:42 |
| **Last Seen** | 2026-06-23 20:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:42:30` | `cowrie.session.connect` |
| `2026-06-23 20:42:30` | `cowrie.client.version` |
| `2026-06-23 20:42:30` | `cowrie.client.kex` |
| `2026-06-23 20:42:30` | `cowrie.login.success` |
| `2026-06-23 20:42:31` | `cowrie.session.params` |
| `2026-06-23 20:42:31` | `cowrie.command.input` |
| `2026-06-23 20:42:31` | `cowrie.log.closed` |
| `2026-06-23 20:42:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f8d9100eddd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:43 |
| **Last Seen** | 2026-06-23 20:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:43:18` | `cowrie.session.connect` |
| `2026-06-23 20:43:18` | `cowrie.client.version` |
| `2026-06-23 20:43:18` | `cowrie.client.kex` |
| `2026-06-23 20:43:19` | `cowrie.login.success` |
| `2026-06-23 20:43:20` | `cowrie.session.params` |
| `2026-06-23 20:43:20` | `cowrie.command.input` |
| `2026-06-23 20:43:20` | `cowrie.log.closed` |
| `2026-06-23 20:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4ac4217cba3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:44 |
| **Last Seen** | 2026-06-23 20:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:44:07` | `cowrie.session.connect` |
| `2026-06-23 20:44:07` | `cowrie.client.version` |
| `2026-06-23 20:44:07` | `cowrie.client.kex` |
| `2026-06-23 20:44:08` | `cowrie.login.success` |
| `2026-06-23 20:44:08` | `cowrie.session.params` |
| `2026-06-23 20:44:08` | `cowrie.command.input` |
| `2026-06-23 20:44:09` | `cowrie.log.closed` |
| `2026-06-23 20:44:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b14b0772030a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:44 |
| **Last Seen** | 2026-06-23 20:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:44:57` | `cowrie.session.connect` |
| `2026-06-23 20:44:57` | `cowrie.client.version` |
| `2026-06-23 20:44:57` | `cowrie.client.kex` |
| `2026-06-23 20:44:57` | `cowrie.login.success` |
| `2026-06-23 20:44:58` | `cowrie.session.params` |
| `2026-06-23 20:44:58` | `cowrie.command.input` |
| `2026-06-23 20:44:58` | `cowrie.log.closed` |
| `2026-06-23 20:44:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5924b0cb58e0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:45 |
| **Last Seen** | 2026-06-23 20:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:45:47` | `cowrie.session.connect` |
| `2026-06-23 20:45:47` | `cowrie.client.version` |
| `2026-06-23 20:45:47` | `cowrie.client.kex` |
| `2026-06-23 20:45:48` | `cowrie.login.success` |
| `2026-06-23 20:45:48` | `cowrie.session.params` |
| `2026-06-23 20:45:48` | `cowrie.command.input` |
| `2026-06-23 20:45:48` | `cowrie.log.closed` |
| `2026-06-23 20:45:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-305715c69f66

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:46 |
| **Last Seen** | 2026-06-23 20:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:46:36` | `cowrie.session.connect` |
| `2026-06-23 20:46:36` | `cowrie.client.version` |
| `2026-06-23 20:46:36` | `cowrie.client.kex` |
| `2026-06-23 20:46:37` | `cowrie.login.success` |
| `2026-06-23 20:46:37` | `cowrie.session.params` |
| `2026-06-23 20:46:37` | `cowrie.command.input` |
| `2026-06-23 20:46:37` | `cowrie.log.closed` |
| `2026-06-23 20:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-401f2f0fbaa5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:47 |
| **Last Seen** | 2026-06-23 20:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:47:25` | `cowrie.session.connect` |
| `2026-06-23 20:47:25` | `cowrie.client.version` |
| `2026-06-23 20:47:25` | `cowrie.client.kex` |
| `2026-06-23 20:47:26` | `cowrie.login.success` |
| `2026-06-23 20:47:27` | `cowrie.session.params` |
| `2026-06-23 20:47:27` | `cowrie.command.input` |
| `2026-06-23 20:47:27` | `cowrie.log.closed` |
| `2026-06-23 20:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2700ff0a4907

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:48 |
| **Last Seen** | 2026-06-23 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:48:13` | `cowrie.session.connect` |
| `2026-06-23 20:48:13` | `cowrie.client.version` |
| `2026-06-23 20:48:13` | `cowrie.client.kex` |
| `2026-06-23 20:48:13` | `cowrie.login.success` |
| `2026-06-23 20:48:14` | `cowrie.session.params` |
| `2026-06-23 20:48:14` | `cowrie.command.input` |
| `2026-06-23 20:48:14` | `cowrie.log.closed` |
| `2026-06-23 20:48:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3720b9aecafa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:49 |
| **Last Seen** | 2026-06-23 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:49:00` | `cowrie.session.connect` |
| `2026-06-23 20:49:00` | `cowrie.client.version` |
| `2026-06-23 20:49:00` | `cowrie.client.kex` |
| `2026-06-23 20:49:00` | `cowrie.login.success` |
| `2026-06-23 20:49:01` | `cowrie.session.params` |
| `2026-06-23 20:49:01` | `cowrie.command.input` |
| `2026-06-23 20:49:01` | `cowrie.log.closed` |
| `2026-06-23 20:49:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20388aa1f937

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:49 |
| **Last Seen** | 2026-06-23 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:49:48` | `cowrie.session.connect` |
| `2026-06-23 20:49:48` | `cowrie.client.version` |
| `2026-06-23 20:49:48` | `cowrie.client.kex` |
| `2026-06-23 20:49:48` | `cowrie.login.success` |
| `2026-06-23 20:49:49` | `cowrie.session.params` |
| `2026-06-23 20:49:49` | `cowrie.command.input` |
| `2026-06-23 20:49:49` | `cowrie.log.closed` |
| `2026-06-23 20:49:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23370e61c242

| Field | Detail |
|---|---|
| **Source IP** | `47.85.8[.]171` |
| **First Seen** | 2026-06-23 20:50 |
| **Last Seen** | 2026-06-23 20:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:50:20` | `cowrie.session.connect` |
| `2026-06-23 20:50:20` | `cowrie.telnet.option` |
| `2026-06-23 20:50:20` | `cowrie.telnet.option` |
| `2026-06-23 20:51:20` | `cowrie.login.success` |
| `2026-06-23 20:51:20` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.85.8[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.8[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d80e31d98111

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:50 |
| **Last Seen** | 2026-06-23 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:50:41` | `cowrie.session.connect` |
| `2026-06-23 20:50:41` | `cowrie.client.version` |
| `2026-06-23 20:50:41` | `cowrie.client.kex` |
| `2026-06-23 20:50:41` | `cowrie.login.success` |
| `2026-06-23 20:50:42` | `cowrie.session.params` |
| `2026-06-23 20:50:42` | `cowrie.command.input` |
| `2026-06-23 20:50:42` | `cowrie.log.closed` |
| `2026-06-23 20:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c103c8c3e0c5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:51 |
| **Last Seen** | 2026-06-23 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:51:32` | `cowrie.session.connect` |
| `2026-06-23 20:51:32` | `cowrie.client.version` |
| `2026-06-23 20:51:32` | `cowrie.client.kex` |
| `2026-06-23 20:51:32` | `cowrie.login.success` |
| `2026-06-23 20:51:33` | `cowrie.session.params` |
| `2026-06-23 20:51:33` | `cowrie.command.input` |
| `2026-06-23 20:51:33` | `cowrie.log.closed` |
| `2026-06-23 20:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1d732d82cab

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:52 |
| **Last Seen** | 2026-06-23 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:52:24` | `cowrie.session.connect` |
| `2026-06-23 20:52:24` | `cowrie.client.version` |
| `2026-06-23 20:52:24` | `cowrie.client.kex` |
| `2026-06-23 20:52:24` | `cowrie.login.success` |
| `2026-06-23 20:52:25` | `cowrie.session.params` |
| `2026-06-23 20:52:25` | `cowrie.command.input` |
| `2026-06-23 20:52:25` | `cowrie.log.closed` |
| `2026-06-23 20:52:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2d0ddc7d428

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:53 |
| **Last Seen** | 2026-06-23 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:53:13` | `cowrie.session.connect` |
| `2026-06-23 20:53:13` | `cowrie.client.version` |
| `2026-06-23 20:53:13` | `cowrie.client.kex` |
| `2026-06-23 20:53:14` | `cowrie.login.success` |
| `2026-06-23 20:53:14` | `cowrie.session.params` |
| `2026-06-23 20:53:14` | `cowrie.command.input` |
| `2026-06-23 20:53:15` | `cowrie.log.closed` |
| `2026-06-23 20:53:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e786d77d740d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:54 |
| **Last Seen** | 2026-06-23 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:54:03` | `cowrie.session.connect` |
| `2026-06-23 20:54:03` | `cowrie.client.version` |
| `2026-06-23 20:54:03` | `cowrie.client.kex` |
| `2026-06-23 20:54:04` | `cowrie.login.success` |
| `2026-06-23 20:54:04` | `cowrie.session.params` |
| `2026-06-23 20:54:04` | `cowrie.command.input` |
| `2026-06-23 20:54:05` | `cowrie.log.closed` |
| `2026-06-23 20:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54e80c12b83a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:54 |
| **Last Seen** | 2026-06-23 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:54:51` | `cowrie.session.connect` |
| `2026-06-23 20:54:51` | `cowrie.client.version` |
| `2026-06-23 20:54:51` | `cowrie.client.kex` |
| `2026-06-23 20:54:52` | `cowrie.login.success` |
| `2026-06-23 20:54:52` | `cowrie.session.params` |
| `2026-06-23 20:54:52` | `cowrie.command.input` |
| `2026-06-23 20:54:52` | `cowrie.log.closed` |
| `2026-06-23 20:54:52` | `cowrie.session.closed` |

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
| `209.99.185[.]59` | **283** | 2026-06-23 16:55 | 2026-06-23 20:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `35.241.128[.]90` | **10** | 2026-06-23 17:19 | 2026-06-23 17:19 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `159.65.233[.]253` | **7** | 2026-06-23 17:11 | 2026-06-23 20:33 | 6m | 0 | `T1592` | 🟢 LOW |
| `185.192.125[.]141` | **3** | 2026-06-23 18:16 | 2026-06-23 20:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `135.119.96[.]127` | **2** | 2026-06-23 20:12 | 2026-06-23 20:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `36.133.27[.]243` | **2** | 2026-06-23 20:27 | 2026-06-23 20:29 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.126.120[.]53` | **2** | 2026-06-23 18:50 | 2026-06-23 18:52 | 2m | 0 | `T1592` | 🟢 LOW |
| `58.209.82[.]167` | **2** | 2026-06-23 18:23 | 2026-06-23 18:25 | 2m | 0 | `T1592` | 🟢 LOW |
| `106.75.163[.]108` | 1 | 2026-06-23 19:03 | 2026-06-23 19:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.29.5[.]231` | 1 | 2026-06-23 19:28 | 2026-06-23 19:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `122.117.121[.]225` | 1 | 2026-06-23 20:03 | 2026-06-23 20:04 | 30s | 0 | `T1592` | 🟢 LOW |
| `141.11.88[.]100` | 1 | 2026-06-23 17:48 | 2026-06-23 17:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `217.60.195[.]138` | 1 | 2026-06-23 17:36 | 2026-06-23 17:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.118.160[.]173` | 1 | 2026-06-23 17:16 | 2026-06-23 17:16 | 12s | 0 | `T1592` | 🟢 LOW |
| `34.38.222[.]164` | 1 | 2026-06-23 17:18 | 2026-06-23 17:18 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-06-23 20:04 | 2026-06-23 20:05 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-06-23 19:40 | 2026-06-23 19:40 | 1s | 0 | `T1592` | 🟢 LOW |
| `49.231.149[.]154` | 1 | 2026-06-23 19:24 | 2026-06-23 19:25 | 30s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-06-23 18:09 | 2026-06-23 18:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.240.17[.]66` | 1 | 2026-06-23 19:50 | 2026-06-23 19:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]110` | 1 | 2026-06-23 19:38 | 2026-06-23 19:39 | 15s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]68` | 1 | 2026-06-23 17:37 | 2026-06-23 17:37 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `35.241.128[.]90` | BE | Google LLC | **100** ⚠️ | 0 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 7 |
| `45.33.12[.]214` | US | Linode | **100** ⚠️ | 50 |
| `141.11.88[.]100` | US | Vantiva SA | **100** ⚠️ | 12 |
| `122.117.121[.]225` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 7 |
| `121.29.5[.]231` | CN | China Unicom Hebei province network | **100** ⚠️ | 10 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `135.119.96[.]127` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `45.79.207[.]111` | US | Linode | **100** ⚠️ | 50 |
| `34.38.222[.]164` | BE | Google LLC | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 432 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 389 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 72 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 70 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (43 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 30 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 756 cases |
| Tool 34  | Credential Extractor        | ✅ 390 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 37 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 43 filtered (5.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 29 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 388 priority case(s) shown individually · 22 recon entry/entries in table (8 group(s) consolidating 311 session(s)).

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
_Report time: 2026-06-23T21:45:23Z_

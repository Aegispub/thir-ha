# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-26 |
| **Generated At** | 2026-06-26T16:20:59Z |
| **Shift Time** | 16:20 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **617** |
| Confirmed Threats | **602** |
| False Positives Filtered | **15** (2.4%) |
| Unique Attacker IPs | **42** |
| Countries of Origin | **13** |
| High Severity Cases | **328** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **289** |
| Malware Samples Analyzed | **5** HIGH · **42** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **345** |
| Unique Credential Pairs | **302** |
| Unique Usernames | **159** |
| Unique Passwords | **249** |
| Successful Auth Pairs | **330** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 132 |
| `ubuntu` | 18 |
| `admin` | 16 |
| `oracle` | 5 |
| `test` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 26 |
| `1234` | 12 |
| `admin` | 10 |
| `` | 8 |
| `123` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `` | 8 |
| `admin` | `admin` | 7 |
| `root` | `smo@@kkklss` | 4 |
| `root` | `123@@@` | 3 |
| `root` | `LeitboGi0ro` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `guojinyang` | `jguo,5471` | `209.99.185.59` | 2026-06-26T10:55:37 |
| `test` | `ahsj2121!` | `209.99.185.59` | 2026-06-26T10:56:36 |
| `steam` | `admin` | `209.99.185.59` | 2026-06-26T10:57:32 |
| `yuanw` | `123` | `209.99.185.59` | 2026-06-26T10:58:29 |
| `user` | `sugontest` | `209.99.185.59` | 2026-06-26T10:59:28 |
| `pul` | `qwe123` | `209.99.185.59` | 2026-06-26T11:00:32 |
| `douyl` | `slst!!` | `209.99.185.59` | 2026-06-26T11:01:39 |
| `ubuntu` | `P@55w0rd!` | `209.99.185.59` | 2026-06-26T11:02:39 |
| `root` | `QWERTYasdfgh` | `45.198.224.120` | 2026-06-26T11:03:01 |
| `root` | `77777` | `209.99.185.59` | 2026-06-26T11:03:36 |
| `root` | `QWEzxc123` | `45.198.224.92` | 2026-06-26T11:04:28 |
| `git` | `gitgitgit` | `209.99.185.59` | 2026-06-26T11:04:34 |
| `solor` | `solor` | `45.205.1.42` | 2026-06-26T11:04:51 |
| `root` | `PaSsW0Rd` | `209.99.185.59` | 2026-06-26T11:05:33 |
| `avis` | `1234` | `209.99.185.59` | 2026-06-26T11:06:32 |
| `server` | `qwerty` | `209.99.185.59` | 2026-06-26T11:07:34 |
| `root` | `p@$$w0rd` | `209.99.185.59` | 2026-06-26T11:08:36 |
| `yoojin` | `1234` | `209.99.185.59` | 2026-06-26T11:09:39 |
| `mota` | `mota:` | `209.99.185.59` | 2026-06-26T11:10:44 |
| `root` | `@!` | `209.99.185.59` | 2026-06-26T11:11:55 |
| `pulse` | `1234` | `209.99.185.59` | 2026-06-26T11:13:02 |
| `weihuang` | `weihuang` | `45.198.224.120` | 2026-06-26T11:13:25 |
| `cajass` | `cajass` | `209.99.185.59` | 2026-06-26T11:14:13 |
| `liuyang` | `liuyang` | `209.99.185.59` | 2026-06-26T11:15:18 |
| `jinchao` | `ljc990109` | `209.99.185.59` | 2026-06-26T11:16:23 |
| `mysql` | `msql123456` | `209.99.185.59` | 2026-06-26T11:17:28 |
| `mysql` | `root` | `209.99.185.59` | 2026-06-26T11:18:31 |
| `root` | `morgan` | `45.205.1.42` | 2026-06-26T11:19:09 |
| `root` | `mike` | `209.99.185.59` | 2026-06-26T11:19:36 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-26T11:20:31 |
| `root` | `Mm123456` | `209.99.185.59` | 2026-06-26T11:20:45 |
| `charlie` | `charlie` | `209.99.185.59` | 2026-06-26T11:21:51 |
| `root` | `P@SVVORD` | `209.99.185.59` | 2026-06-26T11:22:59 |
| `hadoop` | `123456` | `45.198.224.120` | 2026-06-26T11:23:23 |
| `yangliusha13` | `yangliusha13` | `209.99.185.59` | 2026-06-26T11:24:07 |
| `chendi` | `cd3172869` | `209.99.185.59` | 2026-06-26T11:25:13 |
| `chenhao` | `123456` | `209.99.185.59` | 2026-06-26T11:26:22 |
| `sophie` | `sophie` | `209.99.185.59` | 2026-06-26T11:27:30 |
| `ngs` | `ngs` | `209.99.185.59` | 2026-06-26T11:28:38 |
| `root` | `p1a2s3s4w5o6r7d8` | `209.99.185.59` | 2026-06-26T11:29:43 |
| `wxh` | `123456` | `209.99.185.59` | 2026-06-26T11:30:49 |
| `junior` | `junior` | `209.99.185.59` | 2026-06-26T11:31:57 |
| `root` | `Password!123` | `209.99.185.59` | 2026-06-26T11:33:11 |
| `root` | `P@ssword123$` | `45.205.1.42` | 2026-06-26T11:33:38 |
| `events` | `events` | `45.198.224.120` | 2026-06-26T11:33:42 |
| `ubuntu` | `demo1234` | `209.99.185.59` | 2026-06-26T11:34:20 |
| `oracle` | `123qwerty` | `209.99.185.59` | 2026-06-26T11:35:32 |
| `nieliming` | `nieliming` | `209.99.185.59` | 2026-06-26T11:36:43 |
| `jwhu` | `jwhu0616` | `209.99.185.59` | 2026-06-26T11:37:52 |
| `root` | `QAZ123456` | `209.99.185.59` | 2026-06-26T11:39:02 |
| `chenwei` | `chenwei` | `209.99.185.59` | 2026-06-26T11:40:12 |
| `root` | `QWEzxc123` | `10.0.0.73` | 2026-06-26T11:41:04 |
| `zlatoust` | `zlatoust` | `209.99.185.59` | 2026-06-26T11:41:20 |
| `admin` | `admin` | `47.77.182.54` | 2026-06-26T11:42:04 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-26T11:42:05 |
| `www` | `www1234` | `209.99.185.59` | 2026-06-26T11:42:29 |
| `admin` | `admin` | `68.183.234.194` | 2026-06-26T11:42:45 |
| `root` | `12345qwert` | `10.0.0.73` | 2026-06-26T11:43:14 |
| `zhouxy` | `zxy1233` | `209.99.185.59` | 2026-06-26T11:43:43 |
| `jiahaoyang` | `jiahaoyang` | `45.198.224.120` | 2026-06-26T11:44:30 |
| `hg` | `hg` | `209.99.185.59` | 2026-06-26T11:44:54 |
| `ubuntu` | `abc12345` | `209.99.185.59` | 2026-06-26T11:46:11 |
| `fengyingchao` | `fengyingchao1234` | `209.99.185.59` | 2026-06-26T11:47:25 |
| `root` | `Root123456` | `45.205.1.42` | 2026-06-26T11:48:05 |
| `ubnt` | `123456` | `209.99.185.59` | 2026-06-26T11:48:36 |
| `web` | `777777` | `209.99.185.59` | 2026-06-26T11:49:52 |
| `root` | `Test@123` | `209.99.185.59` | 2026-06-26T11:51:10 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-26T11:51:14 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-26T11:51:14 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-26T11:51:19 |
| `fengyang` | `fy` | `209.99.185.59` | 2026-06-26T11:52:25 |
| `ubuntu` | `qwerqaz` | `209.99.185.59` | 2026-06-26T11:53:42 |
| `root` | `Zhuhui` | `209.99.185.59` | 2026-06-26T11:54:56 |
| `nagios` | `nagiosnagios` | `45.198.224.120` | 2026-06-26T11:55:46 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `64.62.156.24` | 2026-06-26T11:55:52 |
| `zhoumengmeng` | `zhoumengmeng` | `209.99.185.59` | 2026-06-26T11:56:06 |
| `root` | `root@2023` | `209.99.185.59` | 2026-06-26T11:57:26 |
| `local` | `1234` | `209.99.185.59` | 2026-06-26T11:58:42 |
| `ubuntu` | `999999` | `209.99.185.59` | 2026-06-26T11:59:58 |
| `zhangcy` | `zhangcy` | `209.99.185.59` | 2026-06-26T12:00:51 |
| `root` | `123` | `188.166.183.133` | 2026-06-26T12:01:23 |
| `guyuqing` | `guyuqing` | `209.99.185.59` | 2026-06-26T12:01:37 |
| `root` | `redhat123` | `209.99.185.59` | 2026-06-26T12:02:25 |
| `user` | `1234` | `45.205.1.42` | 2026-06-26T12:02:34 |
| `git` | `Git` | `209.99.185.59` | 2026-06-26T12:03:19 |
| `root` | `000000` | `91.92.40.176` | 2026-06-26T12:03:26 |
| `ubuntu` | `zaq1@WSX` | `209.99.185.59` | 2026-06-26T12:04:09 |
| `root` | `123123` | `209.99.185.59` | 2026-06-26T12:04:58 |
| `root` | `111111` | `91.92.40.176` | 2026-06-26T12:05:28 |
| `ll` | `ll123456` | `209.99.185.59` | 2026-06-26T12:05:51 |
| `lp` | `123456` | `209.99.185.59` | 2026-06-26T12:06:41 |
| `root` | `qJACJu6v` | `45.198.224.120` | 2026-06-26T12:07:15 |
| `root` | `123` | `91.92.40.176` | 2026-06-26T12:07:29 |
| `oracle` | `123456` | `209.99.185.59` | 2026-06-26T12:07:32 |
| `root` | `Pf2019@$` | `209.99.185.59` | 2026-06-26T12:08:20 |
| `root` | `Abcd@1234` | `209.99.185.59` | 2026-06-26T12:09:09 |
| `root` | `123123` | `91.92.40.176` | 2026-06-26T12:09:31 |
| `convert` | `123456` | `209.99.185.59` | 2026-06-26T12:10:01 |
| `root` | `zaq123` | `209.99.185.59` | 2026-06-26T12:10:55 |
| `root` | `1234` | `91.92.40.176` | 2026-06-26T12:11:35 |
| `developer` | `developer` | `209.99.185.59` | 2026-06-26T12:11:46 |
| `liuwei` | `liuwei` | `209.99.185.59` | 2026-06-26T12:12:40 |
| `yxb` | `Dxcqs@1234` | `209.99.185.59` | 2026-06-26T12:13:31 |
| `root` | `12345` | `91.92.40.176` | 2026-06-26T12:13:38 |
| `sheepdog` | `333333` | `209.99.185.59` | 2026-06-26T12:14:21 |
| `testing` | `testing` | `209.99.185.59` | 2026-06-26T12:15:15 |
| `Vty` | `connection` | `209.99.185.59` | 2026-06-26T12:16:07 |
| `root` | `qazwsxedcrfvtgb` | `45.205.1.42` | 2026-06-26T12:17:01 |
| `testuser` | `passpass` | `209.99.185.59` | 2026-06-26T12:17:04 |
| `root` | `12345678` | `91.92.40.176` | 2026-06-26T12:17:29 |
| `ubnt` | `1234` | `209.99.185.59` | 2026-06-26T12:17:58 |
| `student` | `student1` | `45.198.224.120` | 2026-06-26T12:18:31 |
| `root` | `Pass@word789` | `209.99.185.59` | 2026-06-26T12:18:49 |
| `root` | `123456789` | `91.92.40.176` | 2026-06-26T12:19:20 |
| `apache` | `q1w2e3` | `209.99.185.59` | 2026-06-26T12:19:40 |
| `yuanwd` | `wasd` | `209.99.185.59` | 2026-06-26T12:20:34 |
| `root` | `1q2w3e4r` | `91.92.40.176` | 2026-06-26T12:21:11 |
| `root` | `jennifer` | `209.99.185.59` | 2026-06-26T12:21:27 |
| `huangsiyan` | `huangsiyan` | `209.99.185.59` | 2026-06-26T12:22:29 |
| `root` | `654321` | `91.92.40.176` | 2026-06-26T12:22:59 |
| `jiankun` | `jiankun` | `209.99.185.59` | 2026-06-26T12:24:00 |
| `root` | `P@ssw0rd` | `91.92.40.176` | 2026-06-26T12:24:50 |
| `hat` | `hat123` | `209.99.185.59` | 2026-06-26T12:24:55 |
| `root` | `77777777` | `209.99.185.59` | 2026-06-26T12:25:51 |
| `root` | `admin` | `91.92.40.176` | 2026-06-26T12:26:40 |
| `vyr_odoo` | `psLRTSZAFyHToXlA7yXV` | `209.99.185.59` | 2026-06-26T12:26:44 |
| `jinxinzhu` | `jinxinzhu` | `209.99.185.59` | 2026-06-26T12:27:34 |
| `testuser` | `321` | `209.99.185.59` | 2026-06-26T12:28:28 |
| `root` | `admin123` | `91.92.40.176` | 2026-06-26T12:28:30 |
| `root` | `Ciomex18@;` | `209.99.185.59` | 2026-06-26T12:29:22 |
| `root` | `logon` | `45.198.224.120` | 2026-06-26T12:29:25 |
| `nx` | `123456` | `209.99.185.59` | 2026-06-26T12:30:17 |
| `root` | `passw0rd` | `91.92.40.176` | 2026-06-26T12:30:20 |
| `zy` | `zy123456` | `209.99.185.59` | 2026-06-26T12:31:11 |
| `ubuntu` | `dev1234` | `45.205.1.42` | 2026-06-26T12:31:35 |
| `chen2023` | `chen2023` | `209.99.185.59` | 2026-06-26T12:32:04 |
| `root` | `password` | `91.92.40.176` | 2026-06-26T12:32:14 |
| `root` | `8D;C&#039;rJLD/%?h[WF_c@mysql` | `209.99.185.59` | 2026-06-26T12:32:57 |
| `zjc` | `zjc` | `209.99.185.59` | 2026-06-26T12:33:50 |
| `root` | `password1` | `91.92.40.176` | 2026-06-26T12:34:02 |
| `zg` | `123456` | `209.99.185.59` | 2026-06-26T12:34:47 |
| `root` | `P@ssw0rd123$%^` | `209.99.185.59` | 2026-06-26T12:35:42 |
| `root` | `qwerty` | `91.92.40.176` | 2026-06-26T12:35:46 |
| `contact` | `hostmaster` | `209.99.185.59` | 2026-06-26T12:36:37 |
| `scsc` | `qaz,lp104@2022` | `209.99.185.59` | 2026-06-26T12:37:34 |
| `do` | `123456` | `209.99.185.59` | 2026-06-26T12:38:31 |
| `root` | `Asdf@1234` | `209.99.185.59` | 2026-06-26T12:39:29 |
| `root` | `P455W0RD` | `45.198.224.92` | 2026-06-26T12:40:00 |
| `taotao` | `asdfghjkl` | `209.99.185.59` | 2026-06-26T12:40:27 |
| `ubuntu` | `hadoop12345678` | `45.198.224.120` | 2026-06-26T12:40:46 |
| `root` | `huang1233210` | `209.99.185.59` | 2026-06-26T12:41:24 |
| `sunzheng` | `sunbaoli2021` | `209.99.185.59` | 2026-06-26T12:42:21 |
| `sg` | `1234` | `209.99.185.59` | 2026-06-26T12:43:25 |
| `test` | `qwerty123` | `209.99.185.59` | 2026-06-26T12:44:28 |
| `yangliusha15` | `yangliusha15` | `209.99.185.59` | 2026-06-26T12:45:26 |
| `root` | `Pa55w0rd05` | `45.205.1.42` | 2026-06-26T12:46:14 |
| `dell` | `Admin@4444` | `209.99.185.59` | 2026-06-26T12:46:22 |
| `portal` | `portal` | `209.99.185.59` | 2026-06-26T12:47:19 |
| `fengyingchao` | `0` | `209.99.185.59` | 2026-06-26T12:48:18 |
| `yuanwd` | `654321` | `209.99.185.59` | 2026-06-26T12:49:23 |
| `ceshi` | `ceshi` | `209.99.185.59` | 2026-06-26T12:50:31 |
| `liyou` | `liyou` | `209.99.185.59` | 2026-06-26T12:51:46 |
| `root` | `1qaz@WSX` | `45.198.224.120` | 2026-06-26T12:52:10 |
| `ubuntu` | `QWERTY` | `209.99.185.59` | 2026-06-26T12:52:47 |
| `lhy16` | `lhy65##` | `209.99.185.59` | 2026-06-26T12:53:44 |
| `root` | `fai` | `209.99.185.59` | 2026-06-26T12:54:42 |
| `lyl` | `111111` | `209.99.185.59` | 2026-06-26T12:55:43 |
| `zhongkai` | `keyanzhongkai` | `209.99.185.59` | 2026-06-26T12:56:43 |
| `sy` | `sy` | `209.99.185.59` | 2026-06-26T12:57:42 |
| `postgres` | `q1w2e3` | `209.99.185.59` | 2026-06-26T12:58:38 |
| `ltsp112` | `ltsp112` | `209.99.185.59` | 2026-06-26T12:59:35 |
| `ventase` | `ventase` | `209.99.185.59` | 2026-06-26T13:00:33 |
| `root` | `Pass123$%^` | `45.205.1.42` | 2026-06-26T13:00:43 |
| `apache` | `1234qwer` | `209.99.185.59` | 2026-06-26T13:01:34 |
| `root` | `2cv5BSb6qBg74oUfkhtlMjc7JFGsH7Nr54xL` | `209.99.185.59` | 2026-06-26T13:02:37 |
| `wsn` | `5338eba4` | `209.99.185.59` | 2026-06-26T13:03:42 |
| `root` | `anhyeuem` | `45.198.224.120` | 2026-06-26T13:03:52 |
| `mojia` | `mojia123456` | `209.99.185.59` | 2026-06-26T13:04:45 |
| `pcm` | `pcm` | `209.99.185.59` | 2026-06-26T13:05:48 |
| `ubuntu` | `12345s` | `209.99.185.59` | 2026-06-26T13:06:53 |
| `zqj` | `zqj` | `209.99.185.59` | 2026-06-26T13:07:55 |
| `ricci` | `ricci` | `209.99.185.59` | 2026-06-26T13:08:57 |
| `ubuntu` | `qazxswedc123` | `209.99.185.59` | 2026-06-26T13:09:58 |
| `airchem` | `korea2012` | `209.99.185.59` | 2026-06-26T13:11:00 |
| `bhuang` | `bhuang` | `209.99.185.59` | 2026-06-26T13:11:59 |
| `deploy` | `123qwe` | `209.99.185.59` | 2026-06-26T13:12:59 |
| `zabbix` | `changeme` | `209.99.185.59` | 2026-06-26T13:14:07 |
| `root` | `Qwsx333999Qwsx1111#` | `209.99.185.59` | 2026-06-26T13:15:10 |
| `www` | `adrian140489` | `45.205.1.42` | 2026-06-26T13:15:16 |
| `ec2-user` | `123456` | `45.198.224.120` | 2026-06-26T13:16:05 |
| `root` | `JuanseyAlfo2017` | `209.99.185.59` | 2026-06-26T13:16:15 |
| `root` | `123123123456` | `209.99.185.59` | 2026-06-26T13:17:20 |
| `root` | `P455W0RD` | `10.0.0.73` | 2026-06-26T13:17:25 |
| `root` | `xman` | `209.99.185.59` | 2026-06-26T13:18:24 |
| `hadoop` | `test` | `209.99.185.59` | 2026-06-26T13:19:30 |
| `root` | `zaq1xsw2cde3` | `209.99.185.59` | 2026-06-26T13:20:40 |
| `wangxin3` | `wangxin3` | `209.99.185.59` | 2026-06-26T13:21:47 |
| `root` | `root@999` | `209.99.185.59` | 2026-06-26T13:22:52 |
| `root` | `Jay56` | `209.99.185.59` | 2026-06-26T13:24:01 |
| `root` | `3edc#EDC` | `209.99.185.59` | 2026-06-26T13:25:14 |
| `q` | `123456` | `209.99.185.59` | 2026-06-26T13:26:19 |
| `xuhaozhe` | `111111` | `209.99.185.59` | 2026-06-26T13:27:24 |
| `ubuntu` | `123321` | `45.198.224.120` | 2026-06-26T13:27:24 |
| `root` | `qwe!@#` | `209.99.185.59` | 2026-06-26T13:28:26 |
| `root` | `P@ss123!@#` | `45.205.1.42` | 2026-06-26T13:29:28 |
| `student5` | `student5` | `209.99.185.59` | 2026-06-26T13:29:31 |
| `comptag` | `comptag` | `209.99.185.59` | 2026-06-26T13:30:34 |
| `root` | `123ABC` | `209.99.185.59` | 2026-06-26T13:31:37 |
| `oracle` | `333333` | `209.99.185.59` | 2026-06-26T13:32:43 |
| `nagios` | `654321` | `209.99.185.59` | 2026-06-26T13:33:53 |
| `root` | `Baidu123` | `209.99.185.59` | 2026-06-26T13:35:01 |
| `systemd` | `systemd` | `209.99.185.59` | 2026-06-26T13:36:13 |
| `hall` | `hall` | `209.99.185.59` | 2026-06-26T13:37:20 |
| `root` | `fitness` | `45.198.224.120` | 2026-06-26T13:37:58 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-06-26T13:38:12 |
| `www` | `qwer1234` | `209.99.185.59` | 2026-06-26T13:38:25 |
| `ec2-user` | `password` | `209.99.185.59` | 2026-06-26T13:39:33 |
| `work` | `111111` | `209.99.185.59` | 2026-06-26T13:40:44 |
| `root` | `a123b` | `209.99.185.59` | 2026-06-26T13:41:54 |
| `laizeyu` | `zjusocial123` | `209.99.185.59` | 2026-06-26T13:43:02 |
| `oracle` | `123!@#` | `45.205.1.42` | 2026-06-26T13:43:47 |
| `placement` | `placement` | `209.99.185.59` | 2026-06-26T13:44:12 |
| `demo` | `123456` | `209.99.185.59` | 2026-06-26T13:45:23 |
| `root` | `Painter` | `209.99.185.59` | 2026-06-26T13:46:32 |
| `hhbai` | `123456` | `209.99.185.59` | 2026-06-26T13:47:40 |
| `cookie` | `cookie` | `45.198.224.120` | 2026-06-26T13:48:24 |
| `sclipicibosu` | `saieilamuie` | `209.99.185.59` | 2026-06-26T13:48:50 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-26T13:49:56 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-26T13:49:56 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-26T13:49:58 |
| `zzq` | `zzq` | `209.99.185.59` | 2026-06-26T13:50:02 |
| `root` | `theworldinyourhand` | `209.99.185.59` | 2026-06-26T13:51:16 |
| `vmadmin` | `osbc1002` | `209.99.185.59` | 2026-06-26T13:52:28 |
| `root` | `qd8899xyz` | `209.99.185.59` | 2026-06-26T13:53:41 |
| `bnorth` | `bnorth1` | `209.99.185.59` | 2026-06-26T13:54:53 |
| `jiang` | `jiang` | `209.99.185.59` | 2026-06-26T13:56:02 |
| `root` | `lkjh` | `209.99.185.59` | 2026-06-26T13:57:14 |
| `root` | `postbox5050$` | `45.205.1.42` | 2026-06-26T13:58:12 |
| `root` | `rootpassword` | `209.99.185.59` | 2026-06-26T13:58:30 |
| `rongjiepeng` | `rongjiepeng` | `45.198.224.120` | 2026-06-26T13:58:48 |
| `ubuntu` | `Admin123` | `209.99.185.59` | 2026-06-26T13:59:48 |
| `ubuntu` | `asdlkj12` | `209.99.185.59` | 2026-06-26T14:00:49 |
| `elasticsearch` | `111111` | `209.99.185.59` | 2026-06-26T14:01:41 |
| `root` | `Pass123!@#` | `209.99.185.59` | 2026-06-26T14:02:30 |
| `tengyl` | `tengyl` | `209.99.185.59` | 2026-06-26T14:03:22 |
| `root` | `mobile` | `209.99.185.59` | 2026-06-26T14:04:13 |
| `root` | `Password!1234` | `209.99.185.59` | 2026-06-26T14:05:07 |
| `doctor` | `doctor` | `209.99.185.59` | 2026-06-26T14:06:03 |
| `root` | `R%access321@` | `209.99.185.59` | 2026-06-26T14:06:54 |
| `ubuntu` | `hduser12345678` | `209.99.185.59` | 2026-06-26T14:07:43 |
| `server` | `pass` | `209.99.185.59` | 2026-06-26T14:08:32 |
| `angel` | `666666` | `209.99.185.59` | 2026-06-26T14:09:21 |
| `user` | `123456789` | `45.198.224.120` | 2026-06-26T14:09:26 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-26T14:09:33 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-26T14:09:33 |
| `root` | `1234` | `188.166.183.133` | 2026-06-26T14:09:55 |
| `aa` | `123456` | `209.99.185.59` | 2026-06-26T14:10:13 |
| `ssd` | `123456` | `209.99.185.59` | 2026-06-26T14:11:05 |
| `nvidia` | `12345678` | `209.99.185.59` | 2026-06-26T14:12:00 |
| `root` | `11111111` | `45.205.1.42` | 2026-06-26T14:12:42 |
| `ump` | `123456` | `209.99.185.59` | 2026-06-26T14:12:53 |
| `root` | `Root@2018` | `209.99.185.59` | 2026-06-26T14:13:48 |
| `peiduanqing` | `123` | `209.99.185.59` | 2026-06-26T14:14:40 |
| `root` | `admin@3333` | `209.99.185.59` | 2026-06-26T14:15:36 |
| `root` | `1!2@3#` | `209.99.185.59` | 2026-06-26T14:16:29 |
| `student02` | `123456` | `45.198.224.92` | 2026-06-26T14:17:12 |
| `openbravo` | `openbravo123` | `209.99.185.59` | 2026-06-26T14:17:21 |
| `ansible` | `1234` | `209.99.185.59` | 2026-06-26T14:18:17 |
| `claire` | `claire123` | `209.99.185.59` | 2026-06-26T14:19:15 |
| `bandalg97` | `123456` | `209.99.185.59` | 2026-06-26T14:20:10 |
| `root` | `qwertasdfg` | `45.198.224.120` | 2026-06-26T14:20:13 |
| `root` | `7777777` | `209.99.185.59` | 2026-06-26T14:21:03 |
| `hadoop` | `hadoop123456` | `209.99.185.59` | 2026-06-26T14:21:55 |
| `lfy` | `123456` | `209.99.185.59` | 2026-06-26T14:22:48 |
| `rnd` | `rnd` | `209.99.185.59` | 2026-06-26T14:23:41 |
| `test` | `test2021` | `209.99.185.59` | 2026-06-26T14:24:39 |
| `root` | `RECOVERY` | `209.99.185.59` | 2026-06-26T14:25:34 |
| `root` | `000000` | `91.92.40.7` | 2026-06-26T14:26:25 |
| `admin` | `sugontest` | `209.99.185.59` | 2026-06-26T14:26:30 |
| `root` | `queenVALLEY@123` | `45.205.1.42` | 2026-06-26T14:27:22 |
| `root` | `Root@1111` | `209.99.185.59` | 2026-06-26T14:27:25 |
| `root` | `111111` | `91.92.40.7` | 2026-06-26T14:27:32 |
| `ceshi1` | `ceshi1` | `209.99.185.59` | 2026-06-26T14:28:18 |
| `root` | `123` | `91.92.40.7` | 2026-06-26T14:28:39 |
| `root` | `!!!ingodwetrust!!!` | `209.99.185.59` | 2026-06-26T14:29:14 |
| `root` | `123123` | `91.92.40.7` | 2026-06-26T14:29:43 |
| `ubuntu` | `myubuntu123` | `209.99.185.59` | 2026-06-26T14:30:13 |
| `root` | `1234` | `91.92.40.7` | 2026-06-26T14:30:49 |
| `ubuntu` | `admin12345678` | `45.198.224.120` | 2026-06-26T14:31:01 |
| `lgh` | `lgh123` | `209.99.185.59` | 2026-06-26T14:31:09 |
| `root` | `12345` | `91.92.40.7` | 2026-06-26T14:31:59 |
| `siml` | `siml:` | `209.99.185.59` | 2026-06-26T14:32:04 |
| `yybai` | `byy923923` | `209.99.185.59` | 2026-06-26T14:32:59 |
| `root` | `PAIPAILA` | `209.99.185.59` | 2026-06-26T14:33:55 |
| `root` | `12345678` | `91.92.40.7` | 2026-06-26T14:34:35 |
| `candols` | `antonio` | `209.99.185.59` | 2026-06-26T14:34:49 |
| `taylor` | `taylor` | `209.99.185.59` | 2026-06-26T14:35:43 |
| `root` | `123456789` | `91.92.40.7` | 2026-06-26T14:35:48 |
| `ssli` | `123456` | `209.99.185.59` | 2026-06-26T14:36:39 |
| `root` | `1q2w3e4r` | `91.92.40.7` | 2026-06-26T14:37:04 |
| `zhangjun` | `zhangjun123` | `209.99.185.59` | 2026-06-26T14:37:38 |
| `root` | `654321` | `91.92.40.7` | 2026-06-26T14:38:19 |
| `root` | `bnghty56mju7` | `209.99.185.59` | 2026-06-26T14:38:35 |
| `root` | `Zxcvbnm123` | `209.99.185.59` | 2026-06-26T14:39:33 |
| `root` | `P@ssw0rd` | `91.92.40.7` | 2026-06-26T14:39:37 |
| `richard` | `richard` | `209.99.185.59` | 2026-06-26T14:40:30 |
| `root` | `admin` | `91.92.40.7` | 2026-06-26T14:40:55 |
| `test4` | `123456` | `209.99.185.59` | 2026-06-26T14:41:30 |
| `root` | `QAZWSX123!` | `45.205.1.42` | 2026-06-26T14:42:02 |
| `root` | `admin123` | `91.92.40.7` | 2026-06-26T14:42:13 |
| `teamspeak3` | `teamspeak3` | `45.198.224.120` | 2026-06-26T14:42:22 |
| `tomcat` | `tomcat@2020` | `209.99.185.59` | 2026-06-26T14:42:29 |
| `app` | `app4321` | `209.99.185.59` | 2026-06-26T14:43:25 |
| `root` | `passw0rd` | `91.92.40.7` | 2026-06-26T14:43:31 |
| `oracle` | `password` | `209.99.185.59` | 2026-06-26T14:44:23 |
| `root` | `password` | `91.92.40.7` | 2026-06-26T14:44:44 |
| `shiyu` | `shiyu990601` | `209.99.185.59` | 2026-06-26T14:45:21 |
| `root` | `password1` | `91.92.40.7` | 2026-06-26T14:46:00 |
| `guest` | `passpass` | `209.99.185.59` | 2026-06-26T14:46:17 |
| `online` | `online` | `209.99.185.59` | 2026-06-26T14:47:11 |
| `test1` | `123456` | `209.99.185.59` | 2026-06-26T14:48:06 |
| `stu1` | `123456` | `209.99.185.59` | 2026-06-26T14:49:05 |
| `yuanwd` | `pass1234` | `209.99.185.59` | 2026-06-26T14:50:07 |
| `admin` | `admin` | `185.182.186.243` | 2026-06-26T14:50:29 |
| `arnold` | `arnold` | `209.99.185.59` | 2026-06-26T14:51:07 |
| `jen` | `jen123` | `209.99.185.59` | 2026-06-26T14:52:09 |
| `gpu` | `123` | `209.99.185.59` | 2026-06-26T14:53:07 |
| `root` | `qwe123rty` | `45.148.10.239` | 2026-06-26T14:53:33 |
| `ubuntu` | `deploy12` | `45.198.224.120` | 2026-06-26T14:53:50 |
| `flow-tools` | `1234` | `209.99.185.59` | 2026-06-26T14:54:04 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **617** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 328 |
| libssh | 18 |
| Paramiko (Python) | 10 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 279 | 6 |
| `2ec37a7cc8da...` | Mirai/variant | 35 | 2 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |
| `f1e5e9d24e5e...` | Mirai/variant | 4 | 1 |
| `bc3aee897af7...` | Mirai/variant | 4 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 279 | 6 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 35 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 14 | 5 | — |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 4 | 1 | Mirai/variant |
| `bc3aee897af7...` | Go SSH scanner | 4 | 2 | Mirai/variant |
| `19532158b559...` | libssh | 2 | 2 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 2 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 33 | 2 | `T1082, T1592, T1078, T1083` |

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
echo '000000' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'
```
Source IPs: `91.92.40.7`, `91.92.40.176`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **42** |
| Unique ASNs | **27** |
| High-Risk ASNs | **24** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 5 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |
| `AS208137` | Feo Prest SRL | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS197170` | TechTies Inc. | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (328)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f1b7b5611777

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:55 |
| **Last Seen** | 2026-06-26 10:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:55:36` | `cowrie.session.connect` |
| `2026-06-26 10:55:36` | `cowrie.client.version` |
| `2026-06-26 10:55:36` | `cowrie.client.kex` |
| `2026-06-26 10:55:37` | `cowrie.login.success` |
| `2026-06-26 10:55:38` | `cowrie.session.params` |
| `2026-06-26 10:55:38` | `cowrie.command.input` |
| `2026-06-26 10:55:38` | `cowrie.log.closed` |
| `2026-06-26 10:55:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-865e565c0074

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:56 |
| **Last Seen** | 2026-06-26 10:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:56:35` | `cowrie.session.connect` |
| `2026-06-26 10:56:35` | `cowrie.client.version` |
| `2026-06-26 10:56:35` | `cowrie.client.kex` |
| `2026-06-26 10:56:36` | `cowrie.login.success` |
| `2026-06-26 10:56:36` | `cowrie.session.params` |
| `2026-06-26 10:56:36` | `cowrie.command.input` |
| `2026-06-26 10:56:36` | `cowrie.log.closed` |
| `2026-06-26 10:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae13e2cc29f1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:57 |
| **Last Seen** | 2026-06-26 10:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:57:32` | `cowrie.session.connect` |
| `2026-06-26 10:57:32` | `cowrie.client.version` |
| `2026-06-26 10:57:32` | `cowrie.client.kex` |
| `2026-06-26 10:57:32` | `cowrie.login.success` |
| `2026-06-26 10:57:33` | `cowrie.session.params` |
| `2026-06-26 10:57:33` | `cowrie.command.input` |
| `2026-06-26 10:57:33` | `cowrie.log.closed` |
| `2026-06-26 10:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7226e169761a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:58 |
| **Last Seen** | 2026-06-26 10:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:58:29` | `cowrie.session.connect` |
| `2026-06-26 10:58:29` | `cowrie.client.version` |
| `2026-06-26 10:58:29` | `cowrie.client.kex` |
| `2026-06-26 10:58:29` | `cowrie.login.success` |
| `2026-06-26 10:58:30` | `cowrie.session.params` |
| `2026-06-26 10:58:30` | `cowrie.command.input` |
| `2026-06-26 10:58:30` | `cowrie.log.closed` |
| `2026-06-26 10:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccadf3e087b9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:59 |
| **Last Seen** | 2026-06-26 10:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:59:28` | `cowrie.session.connect` |
| `2026-06-26 10:59:28` | `cowrie.client.version` |
| `2026-06-26 10:59:28` | `cowrie.client.kex` |
| `2026-06-26 10:59:28` | `cowrie.login.success` |
| `2026-06-26 10:59:29` | `cowrie.session.params` |
| `2026-06-26 10:59:29` | `cowrie.command.input` |
| `2026-06-26 10:59:29` | `cowrie.log.closed` |
| `2026-06-26 10:59:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8af6ecd1b1fa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:00 |
| **Last Seen** | 2026-06-26 11:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:00:32` | `cowrie.session.connect` |
| `2026-06-26 11:00:32` | `cowrie.client.version` |
| `2026-06-26 11:00:32` | `cowrie.client.kex` |
| `2026-06-26 11:00:32` | `cowrie.login.success` |
| `2026-06-26 11:00:33` | `cowrie.session.params` |
| `2026-06-26 11:00:33` | `cowrie.command.input` |
| `2026-06-26 11:00:33` | `cowrie.log.closed` |
| `2026-06-26 11:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cf7f5f07511

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:01 |
| **Last Seen** | 2026-06-26 11:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:01:39` | `cowrie.session.connect` |
| `2026-06-26 11:01:39` | `cowrie.client.version` |
| `2026-06-26 11:01:39` | `cowrie.client.kex` |
| `2026-06-26 11:01:39` | `cowrie.login.success` |
| `2026-06-26 11:01:40` | `cowrie.session.params` |
| `2026-06-26 11:01:40` | `cowrie.command.input` |
| `2026-06-26 11:01:40` | `cowrie.log.closed` |
| `2026-06-26 11:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbbb38f83023

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:02 |
| **Last Seen** | 2026-06-26 11:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:02:38` | `cowrie.session.connect` |
| `2026-06-26 11:02:38` | `cowrie.client.version` |
| `2026-06-26 11:02:38` | `cowrie.client.kex` |
| `2026-06-26 11:02:39` | `cowrie.login.success` |
| `2026-06-26 11:02:39` | `cowrie.session.params` |
| `2026-06-26 11:02:39` | `cowrie.command.input` |
| `2026-06-26 11:02:39` | `cowrie.log.closed` |
| `2026-06-26 11:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a33f25ca8671

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 11:02 |
| **Last Seen** | 2026-06-26 11:03 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:02:54` | `cowrie.session.connect` |
| `2026-06-26 11:02:55` | `cowrie.client.version` |
| `2026-06-26 11:02:55` | `cowrie.client.kex` |
| `2026-06-26 11:03:01` | `cowrie.login.success` |
| `2026-06-26 11:03:06` | `cowrie.session.params` |
| `2026-06-26 11:03:06` | `cowrie.command.input` |
| `2026-06-26 11:03:07` | `cowrie.log.closed` |
| `2026-06-26 11:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa3f2e00975b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:03 |
| **Last Seen** | 2026-06-26 11:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:03:35` | `cowrie.session.connect` |
| `2026-06-26 11:03:35` | `cowrie.client.version` |
| `2026-06-26 11:03:35` | `cowrie.client.kex` |
| `2026-06-26 11:03:36` | `cowrie.login.success` |
| `2026-06-26 11:03:36` | `cowrie.session.params` |
| `2026-06-26 11:03:36` | `cowrie.command.input` |
| `2026-06-26 11:03:36` | `cowrie.log.closed` |
| `2026-06-26 11:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e24d2e3ad6cf

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-06-26 11:04 |
| **Last Seen** | 2026-06-26 11:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:04:28` | `cowrie.session.connect` |
| `2026-06-26 11:04:28` | `cowrie.client.version` |
| `2026-06-26 11:04:28` | `cowrie.client.kex` |
| `2026-06-26 11:04:28` | `cowrie.login.success` |
| `2026-06-26 11:04:29` | `cowrie.session.params` |
| `2026-06-26 11:04:29` | `cowrie.command.input` |
| `2026-06-26 11:04:29` | `cowrie.log.closed` |
| `2026-06-26 11:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c8de943f005

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:04 |
| **Last Seen** | 2026-06-26 11:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:04:34` | `cowrie.session.connect` |
| `2026-06-26 11:04:34` | `cowrie.client.version` |
| `2026-06-26 11:04:34` | `cowrie.client.kex` |
| `2026-06-26 11:04:34` | `cowrie.login.success` |
| `2026-06-26 11:04:35` | `cowrie.session.params` |
| `2026-06-26 11:04:35` | `cowrie.command.input` |
| `2026-06-26 11:04:35` | `cowrie.log.closed` |
| `2026-06-26 11:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de059cd34396

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 11:04 |
| **Last Seen** | 2026-06-26 11:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:04:49` | `cowrie.session.connect` |
| `2026-06-26 11:04:49` | `cowrie.client.version` |
| `2026-06-26 11:04:49` | `cowrie.client.kex` |
| `2026-06-26 11:04:51` | `cowrie.login.success` |
| `2026-06-26 11:04:52` | `cowrie.session.params` |
| `2026-06-26 11:04:52` | `cowrie.command.input` |
| `2026-06-26 11:04:52` | `cowrie.log.closed` |
| `2026-06-26 11:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61db112043a8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:05 |
| **Last Seen** | 2026-06-26 11:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:05:32` | `cowrie.session.connect` |
| `2026-06-26 11:05:32` | `cowrie.client.version` |
| `2026-06-26 11:05:32` | `cowrie.client.kex` |
| `2026-06-26 11:05:33` | `cowrie.login.success` |
| `2026-06-26 11:05:34` | `cowrie.session.params` |
| `2026-06-26 11:05:34` | `cowrie.command.input` |
| `2026-06-26 11:05:34` | `cowrie.log.closed` |
| `2026-06-26 11:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2a44fc60523

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:06 |
| **Last Seen** | 2026-06-26 11:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:06:31` | `cowrie.session.connect` |
| `2026-06-26 11:06:31` | `cowrie.client.version` |
| `2026-06-26 11:06:32` | `cowrie.client.kex` |
| `2026-06-26 11:06:32` | `cowrie.login.success` |
| `2026-06-26 11:06:33` | `cowrie.session.params` |
| `2026-06-26 11:06:33` | `cowrie.command.input` |
| `2026-06-26 11:06:33` | `cowrie.log.closed` |
| `2026-06-26 11:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1207f1a1fda

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:07 |
| **Last Seen** | 2026-06-26 11:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:07:33` | `cowrie.session.connect` |
| `2026-06-26 11:07:33` | `cowrie.client.version` |
| `2026-06-26 11:07:34` | `cowrie.client.kex` |
| `2026-06-26 11:07:34` | `cowrie.login.success` |
| `2026-06-26 11:07:35` | `cowrie.session.params` |
| `2026-06-26 11:07:35` | `cowrie.command.input` |
| `2026-06-26 11:07:35` | `cowrie.log.closed` |
| `2026-06-26 11:07:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d08505b4ed3e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:08 |
| **Last Seen** | 2026-06-26 11:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:08:35` | `cowrie.session.connect` |
| `2026-06-26 11:08:35` | `cowrie.client.version` |
| `2026-06-26 11:08:35` | `cowrie.client.kex` |
| `2026-06-26 11:08:36` | `cowrie.login.success` |
| `2026-06-26 11:08:37` | `cowrie.session.params` |
| `2026-06-26 11:08:37` | `cowrie.command.input` |
| `2026-06-26 11:08:37` | `cowrie.log.closed` |
| `2026-06-26 11:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d3810ee2c17

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:09 |
| **Last Seen** | 2026-06-26 11:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:09:39` | `cowrie.session.connect` |
| `2026-06-26 11:09:39` | `cowrie.client.version` |
| `2026-06-26 11:09:39` | `cowrie.client.kex` |
| `2026-06-26 11:09:39` | `cowrie.login.success` |
| `2026-06-26 11:09:40` | `cowrie.session.params` |
| `2026-06-26 11:09:40` | `cowrie.command.input` |
| `2026-06-26 11:09:40` | `cowrie.log.closed` |
| `2026-06-26 11:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fea53b541f8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:10 |
| **Last Seen** | 2026-06-26 11:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:10:44` | `cowrie.session.connect` |
| `2026-06-26 11:10:44` | `cowrie.client.version` |
| `2026-06-26 11:10:44` | `cowrie.client.kex` |
| `2026-06-26 11:10:44` | `cowrie.login.success` |
| `2026-06-26 11:10:45` | `cowrie.session.params` |
| `2026-06-26 11:10:45` | `cowrie.command.input` |
| `2026-06-26 11:10:45` | `cowrie.log.closed` |
| `2026-06-26 11:10:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb41f9716aa6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:11 |
| **Last Seen** | 2026-06-26 11:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:11:55` | `cowrie.session.connect` |
| `2026-06-26 11:11:55` | `cowrie.client.version` |
| `2026-06-26 11:11:55` | `cowrie.client.kex` |
| `2026-06-26 11:11:55` | `cowrie.login.success` |
| `2026-06-26 11:11:56` | `cowrie.session.params` |
| `2026-06-26 11:11:56` | `cowrie.command.input` |
| `2026-06-26 11:11:56` | `cowrie.log.closed` |
| `2026-06-26 11:11:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-891ba378d0ce

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:13 |
| **Last Seen** | 2026-06-26 11:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:13:02` | `cowrie.session.connect` |
| `2026-06-26 11:13:02` | `cowrie.client.version` |
| `2026-06-26 11:13:02` | `cowrie.client.kex` |
| `2026-06-26 11:13:02` | `cowrie.login.success` |
| `2026-06-26 11:13:03` | `cowrie.session.params` |
| `2026-06-26 11:13:03` | `cowrie.command.input` |
| `2026-06-26 11:13:03` | `cowrie.log.closed` |
| `2026-06-26 11:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11bc17a5bdbe

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 11:13 |
| **Last Seen** | 2026-06-26 11:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:13:19` | `cowrie.session.connect` |
| `2026-06-26 11:13:21` | `cowrie.client.version` |
| `2026-06-26 11:13:21` | `cowrie.client.kex` |
| `2026-06-26 11:13:25` | `cowrie.login.success` |
| `2026-06-26 11:13:29` | `cowrie.session.params` |
| `2026-06-26 11:13:29` | `cowrie.command.input` |
| `2026-06-26 11:13:30` | `cowrie.log.closed` |
| `2026-06-26 11:13:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c8d85789f9f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:14 |
| **Last Seen** | 2026-06-26 11:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:14:13` | `cowrie.session.connect` |
| `2026-06-26 11:14:13` | `cowrie.client.version` |
| `2026-06-26 11:14:13` | `cowrie.client.kex` |
| `2026-06-26 11:14:13` | `cowrie.login.success` |
| `2026-06-26 11:14:14` | `cowrie.session.params` |
| `2026-06-26 11:14:14` | `cowrie.command.input` |
| `2026-06-26 11:14:14` | `cowrie.log.closed` |
| `2026-06-26 11:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35baf86a8361

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:15 |
| **Last Seen** | 2026-06-26 11:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:15:17` | `cowrie.session.connect` |
| `2026-06-26 11:15:17` | `cowrie.client.version` |
| `2026-06-26 11:15:17` | `cowrie.client.kex` |
| `2026-06-26 11:15:18` | `cowrie.login.success` |
| `2026-06-26 11:15:18` | `cowrie.session.params` |
| `2026-06-26 11:15:18` | `cowrie.command.input` |
| `2026-06-26 11:15:18` | `cowrie.log.closed` |
| `2026-06-26 11:15:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4ec4496f893

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:16 |
| **Last Seen** | 2026-06-26 11:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:16:23` | `cowrie.session.connect` |
| `2026-06-26 11:16:23` | `cowrie.client.version` |
| `2026-06-26 11:16:23` | `cowrie.client.kex` |
| `2026-06-26 11:16:23` | `cowrie.login.success` |
| `2026-06-26 11:16:24` | `cowrie.session.params` |
| `2026-06-26 11:16:24` | `cowrie.command.input` |
| `2026-06-26 11:16:24` | `cowrie.log.closed` |
| `2026-06-26 11:16:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-652946a54dab

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:17 |
| **Last Seen** | 2026-06-26 11:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:17:27` | `cowrie.session.connect` |
| `2026-06-26 11:17:27` | `cowrie.client.version` |
| `2026-06-26 11:17:27` | `cowrie.client.kex` |
| `2026-06-26 11:17:28` | `cowrie.login.success` |
| `2026-06-26 11:17:28` | `cowrie.session.params` |
| `2026-06-26 11:17:28` | `cowrie.command.input` |
| `2026-06-26 11:17:28` | `cowrie.log.closed` |
| `2026-06-26 11:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-166aa3a5e3bb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:18 |
| **Last Seen** | 2026-06-26 11:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:18:31` | `cowrie.session.connect` |
| `2026-06-26 11:18:31` | `cowrie.client.version` |
| `2026-06-26 11:18:31` | `cowrie.client.kex` |
| `2026-06-26 11:18:31` | `cowrie.login.success` |
| `2026-06-26 11:18:32` | `cowrie.session.params` |
| `2026-06-26 11:18:32` | `cowrie.command.input` |
| `2026-06-26 11:18:32` | `cowrie.log.closed` |
| `2026-06-26 11:18:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b525b31147ad

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 11:19 |
| **Last Seen** | 2026-06-26 11:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:19:07` | `cowrie.session.connect` |
| `2026-06-26 11:19:08` | `cowrie.client.version` |
| `2026-06-26 11:19:08` | `cowrie.client.kex` |
| `2026-06-26 11:19:09` | `cowrie.login.success` |
| `2026-06-26 11:19:11` | `cowrie.session.params` |
| `2026-06-26 11:19:11` | `cowrie.command.input` |
| `2026-06-26 11:19:11` | `cowrie.log.closed` |
| `2026-06-26 11:19:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-643ad7adba2b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:19 |
| **Last Seen** | 2026-06-26 11:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:19:36` | `cowrie.session.connect` |
| `2026-06-26 11:19:36` | `cowrie.client.version` |
| `2026-06-26 11:19:36` | `cowrie.client.kex` |
| `2026-06-26 11:19:36` | `cowrie.login.success` |
| `2026-06-26 11:19:37` | `cowrie.session.params` |
| `2026-06-26 11:19:37` | `cowrie.command.input` |
| `2026-06-26 11:19:37` | `cowrie.log.closed` |
| `2026-06-26 11:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4799efc5d0a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:20 |
| **Last Seen** | 2026-06-26 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:20:45` | `cowrie.session.connect` |
| `2026-06-26 11:20:45` | `cowrie.client.version` |
| `2026-06-26 11:20:45` | `cowrie.client.kex` |
| `2026-06-26 11:20:45` | `cowrie.login.success` |
| `2026-06-26 11:20:46` | `cowrie.session.params` |
| `2026-06-26 11:20:46` | `cowrie.command.input` |
| `2026-06-26 11:20:46` | `cowrie.log.closed` |
| `2026-06-26 11:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b895a4602cf0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:21 |
| **Last Seen** | 2026-06-26 11:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:21:50` | `cowrie.session.connect` |
| `2026-06-26 11:21:50` | `cowrie.client.version` |
| `2026-06-26 11:21:50` | `cowrie.client.kex` |
| `2026-06-26 11:21:51` | `cowrie.login.success` |
| `2026-06-26 11:21:51` | `cowrie.session.params` |
| `2026-06-26 11:21:51` | `cowrie.command.input` |
| `2026-06-26 11:21:51` | `cowrie.log.closed` |
| `2026-06-26 11:21:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f62ae24b826

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:22 |
| **Last Seen** | 2026-06-26 11:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:22:58` | `cowrie.session.connect` |
| `2026-06-26 11:22:58` | `cowrie.client.version` |
| `2026-06-26 11:22:58` | `cowrie.client.kex` |
| `2026-06-26 11:22:59` | `cowrie.login.success` |
| `2026-06-26 11:22:59` | `cowrie.session.params` |
| `2026-06-26 11:22:59` | `cowrie.command.input` |
| `2026-06-26 11:23:00` | `cowrie.log.closed` |
| `2026-06-26 11:23:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a48d078fe94

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 11:23 |
| **Last Seen** | 2026-06-26 11:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:23:17` | `cowrie.session.connect` |
| `2026-06-26 11:23:18` | `cowrie.client.version` |
| `2026-06-26 11:23:18` | `cowrie.client.kex` |
| `2026-06-26 11:23:23` | `cowrie.login.success` |
| `2026-06-26 11:23:24` | `cowrie.session.params` |
| `2026-06-26 11:23:24` | `cowrie.command.input` |
| `2026-06-26 11:23:26` | `cowrie.log.closed` |
| `2026-06-26 11:23:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-080e0f969d23

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:24 |
| **Last Seen** | 2026-06-26 11:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:24:07` | `cowrie.session.connect` |
| `2026-06-26 11:24:07` | `cowrie.client.version` |
| `2026-06-26 11:24:07` | `cowrie.client.kex` |
| `2026-06-26 11:24:07` | `cowrie.login.success` |
| `2026-06-26 11:24:08` | `cowrie.session.params` |
| `2026-06-26 11:24:08` | `cowrie.command.input` |
| `2026-06-26 11:24:08` | `cowrie.log.closed` |
| `2026-06-26 11:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-947ba3b5b70f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:25 |
| **Last Seen** | 2026-06-26 11:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:25:13` | `cowrie.session.connect` |
| `2026-06-26 11:25:13` | `cowrie.client.version` |
| `2026-06-26 11:25:13` | `cowrie.client.kex` |
| `2026-06-26 11:25:13` | `cowrie.login.success` |
| `2026-06-26 11:25:14` | `cowrie.session.params` |
| `2026-06-26 11:25:14` | `cowrie.command.input` |
| `2026-06-26 11:25:14` | `cowrie.log.closed` |
| `2026-06-26 11:25:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b636d385a92

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:26 |
| **Last Seen** | 2026-06-26 11:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:26:22` | `cowrie.session.connect` |
| `2026-06-26 11:26:22` | `cowrie.client.version` |
| `2026-06-26 11:26:22` | `cowrie.client.kex` |
| `2026-06-26 11:26:22` | `cowrie.login.success` |
| `2026-06-26 11:26:23` | `cowrie.session.params` |
| `2026-06-26 11:26:23` | `cowrie.command.input` |
| `2026-06-26 11:26:23` | `cowrie.log.closed` |
| `2026-06-26 11:26:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8e28b3cb97c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:27 |
| **Last Seen** | 2026-06-26 11:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:27:30` | `cowrie.session.connect` |
| `2026-06-26 11:27:30` | `cowrie.client.version` |
| `2026-06-26 11:27:30` | `cowrie.client.kex` |
| `2026-06-26 11:27:30` | `cowrie.login.success` |
| `2026-06-26 11:27:31` | `cowrie.session.params` |
| `2026-06-26 11:27:31` | `cowrie.command.input` |
| `2026-06-26 11:27:31` | `cowrie.log.closed` |
| `2026-06-26 11:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf6438f11ac7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:28 |
| **Last Seen** | 2026-06-26 11:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:28:37` | `cowrie.session.connect` |
| `2026-06-26 11:28:37` | `cowrie.client.version` |
| `2026-06-26 11:28:37` | `cowrie.client.kex` |
| `2026-06-26 11:28:38` | `cowrie.login.success` |
| `2026-06-26 11:28:38` | `cowrie.session.params` |
| `2026-06-26 11:28:38` | `cowrie.command.input` |
| `2026-06-26 11:28:39` | `cowrie.log.closed` |
| `2026-06-26 11:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65ed5afaf551

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:29 |
| **Last Seen** | 2026-06-26 11:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:29:43` | `cowrie.session.connect` |
| `2026-06-26 11:29:43` | `cowrie.client.version` |
| `2026-06-26 11:29:43` | `cowrie.client.kex` |
| `2026-06-26 11:29:43` | `cowrie.login.success` |
| `2026-06-26 11:29:44` | `cowrie.session.params` |
| `2026-06-26 11:29:44` | `cowrie.command.input` |
| `2026-06-26 11:29:44` | `cowrie.log.closed` |
| `2026-06-26 11:29:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb62e47e4b82

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:30 |
| **Last Seen** | 2026-06-26 11:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:30:49` | `cowrie.session.connect` |
| `2026-06-26 11:30:49` | `cowrie.client.version` |
| `2026-06-26 11:30:49` | `cowrie.client.kex` |
| `2026-06-26 11:30:49` | `cowrie.login.success` |
| `2026-06-26 11:30:50` | `cowrie.session.params` |
| `2026-06-26 11:30:50` | `cowrie.command.input` |
| `2026-06-26 11:30:50` | `cowrie.log.closed` |
| `2026-06-26 11:30:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52efe9324967

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:31 |
| **Last Seen** | 2026-06-26 11:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:31:57` | `cowrie.session.connect` |
| `2026-06-26 11:31:57` | `cowrie.client.version` |
| `2026-06-26 11:31:57` | `cowrie.client.kex` |
| `2026-06-26 11:31:57` | `cowrie.login.success` |
| `2026-06-26 11:31:58` | `cowrie.session.params` |
| `2026-06-26 11:31:58` | `cowrie.command.input` |
| `2026-06-26 11:31:58` | `cowrie.log.closed` |
| `2026-06-26 11:31:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef047495110a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:33 |
| **Last Seen** | 2026-06-26 11:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:33:11` | `cowrie.session.connect` |
| `2026-06-26 11:33:11` | `cowrie.client.version` |
| `2026-06-26 11:33:11` | `cowrie.client.kex` |
| `2026-06-26 11:33:11` | `cowrie.login.success` |
| `2026-06-26 11:33:12` | `cowrie.session.params` |
| `2026-06-26 11:33:12` | `cowrie.command.input` |
| `2026-06-26 11:33:12` | `cowrie.log.closed` |
| `2026-06-26 11:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea8f18b409b7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 11:33 |
| **Last Seen** | 2026-06-26 11:33 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:33:34` | `cowrie.session.connect` |
| `2026-06-26 11:33:36` | `cowrie.client.version` |
| `2026-06-26 11:33:36` | `cowrie.client.kex` |
| `2026-06-26 11:33:42` | `cowrie.login.success` |
| `2026-06-26 11:33:45` | `cowrie.session.params` |
| `2026-06-26 11:33:45` | `cowrie.command.input` |
| `2026-06-26 11:33:47` | `cowrie.log.closed` |
| `2026-06-26 11:33:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fe4ea5c94d7

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 11:33 |
| **Last Seen** | 2026-06-26 11:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:33:36` | `cowrie.session.connect` |
| `2026-06-26 11:33:36` | `cowrie.client.version` |
| `2026-06-26 11:33:36` | `cowrie.client.kex` |
| `2026-06-26 11:33:38` | `cowrie.login.success` |
| `2026-06-26 11:33:40` | `cowrie.session.params` |
| `2026-06-26 11:33:40` | `cowrie.command.input` |
| `2026-06-26 11:33:40` | `cowrie.log.closed` |
| `2026-06-26 11:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-677b64a9a6e5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:34 |
| **Last Seen** | 2026-06-26 11:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:34:20` | `cowrie.session.connect` |
| `2026-06-26 11:34:20` | `cowrie.client.version` |
| `2026-06-26 11:34:20` | `cowrie.client.kex` |
| `2026-06-26 11:34:20` | `cowrie.login.success` |
| `2026-06-26 11:34:21` | `cowrie.session.params` |
| `2026-06-26 11:34:21` | `cowrie.command.input` |
| `2026-06-26 11:34:21` | `cowrie.log.closed` |
| `2026-06-26 11:34:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53daf3962e50

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:35 |
| **Last Seen** | 2026-06-26 11:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:35:31` | `cowrie.session.connect` |
| `2026-06-26 11:35:31` | `cowrie.client.version` |
| `2026-06-26 11:35:31` | `cowrie.client.kex` |
| `2026-06-26 11:35:32` | `cowrie.login.success` |
| `2026-06-26 11:35:33` | `cowrie.session.params` |
| `2026-06-26 11:35:33` | `cowrie.command.input` |
| `2026-06-26 11:35:33` | `cowrie.log.closed` |
| `2026-06-26 11:35:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d00cb14069f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:36 |
| **Last Seen** | 2026-06-26 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:36:43` | `cowrie.session.connect` |
| `2026-06-26 11:36:43` | `cowrie.client.version` |
| `2026-06-26 11:36:43` | `cowrie.client.kex` |
| `2026-06-26 11:36:43` | `cowrie.login.success` |
| `2026-06-26 11:36:44` | `cowrie.session.params` |
| `2026-06-26 11:36:44` | `cowrie.command.input` |
| `2026-06-26 11:36:44` | `cowrie.log.closed` |
| `2026-06-26 11:36:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3891fed4d294

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:37 |
| **Last Seen** | 2026-06-26 11:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:37:52` | `cowrie.session.connect` |
| `2026-06-26 11:37:52` | `cowrie.client.version` |
| `2026-06-26 11:37:52` | `cowrie.client.kex` |
| `2026-06-26 11:37:52` | `cowrie.login.success` |
| `2026-06-26 11:37:53` | `cowrie.session.params` |
| `2026-06-26 11:37:53` | `cowrie.command.input` |
| `2026-06-26 11:37:53` | `cowrie.log.closed` |
| `2026-06-26 11:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-125cf69e406a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:39 |
| **Last Seen** | 2026-06-26 11:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:39:02` | `cowrie.session.connect` |
| `2026-06-26 11:39:02` | `cowrie.client.version` |
| `2026-06-26 11:39:02` | `cowrie.client.kex` |
| `2026-06-26 11:39:02` | `cowrie.login.success` |
| `2026-06-26 11:39:03` | `cowrie.session.params` |
| `2026-06-26 11:39:03` | `cowrie.command.input` |
| `2026-06-26 11:39:03` | `cowrie.log.closed` |
| `2026-06-26 11:39:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92679fe9b739

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:40 |
| **Last Seen** | 2026-06-26 11:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:40:12` | `cowrie.session.connect` |
| `2026-06-26 11:40:12` | `cowrie.client.version` |
| `2026-06-26 11:40:12` | `cowrie.client.kex` |
| `2026-06-26 11:40:12` | `cowrie.login.success` |
| `2026-06-26 11:40:13` | `cowrie.session.params` |
| `2026-06-26 11:40:13` | `cowrie.command.input` |
| `2026-06-26 11:40:13` | `cowrie.log.closed` |
| `2026-06-26 11:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ab6ef1d0431

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:41 |
| **Last Seen** | 2026-06-26 11:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:41:20` | `cowrie.session.connect` |
| `2026-06-26 11:41:20` | `cowrie.client.version` |
| `2026-06-26 11:41:20` | `cowrie.client.kex` |
| `2026-06-26 11:41:20` | `cowrie.login.success` |
| `2026-06-26 11:41:21` | `cowrie.session.params` |
| `2026-06-26 11:41:21` | `cowrie.command.input` |
| `2026-06-26 11:41:21` | `cowrie.log.closed` |
| `2026-06-26 11:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f98be93c3940

| Field | Detail |
|---|---|
| **Source IP** | `68.183.234[.]194` |
| **First Seen** | 2026-06-26 11:41 |
| **Last Seen** | 2026-06-26 11:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:41:44` | `cowrie.session.connect` |
| `2026-06-26 11:41:45` | `cowrie.telnet.option` |
| `2026-06-26 11:41:45` | `cowrie.telnet.option` |
| `2026-06-26 11:42:45` | `cowrie.login.success` |
| `2026-06-26 11:42:45` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `68.183.234[.]194` to AbuseIPDB if not already reported
- [ ] Block `68.183.234[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6746eb1c6292

| Field | Detail |
|---|---|
| **Source IP** | `47.77.182[.]54` |
| **First Seen** | 2026-06-26 11:42 |
| **Last Seen** | 2026-06-26 11:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:42:04` | `cowrie.session.connect` |
| `2026-06-26 11:42:04` | `cowrie.client.version` |
| `2026-06-26 11:42:04` | `cowrie.client.kex` |
| `2026-06-26 11:42:04` | `cowrie.login.success` |
| `2026-06-26 11:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.77.182[.]54` to AbuseIPDB if not already reported
- [ ] Block `47.77.182[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbd3ccae6562

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-26 11:42 |
| **Last Seen** | 2026-06-26 11:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:42:04` | `cowrie.session.connect` |
| `2026-06-26 11:42:04` | `cowrie.client.version` |
| `2026-06-26 11:42:04` | `cowrie.client.kex` |
| `2026-06-26 11:42:05` | `cowrie.login.success` |
| `2026-06-26 11:42:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81803d8d0a74

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:42 |
| **Last Seen** | 2026-06-26 11:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:42:29` | `cowrie.session.connect` |
| `2026-06-26 11:42:29` | `cowrie.client.version` |
| `2026-06-26 11:42:29` | `cowrie.client.kex` |
| `2026-06-26 11:42:29` | `cowrie.login.success` |
| `2026-06-26 11:42:30` | `cowrie.session.params` |
| `2026-06-26 11:42:30` | `cowrie.command.input` |
| `2026-06-26 11:42:30` | `cowrie.log.closed` |
| `2026-06-26 11:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86d00cd82970

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:43 |
| **Last Seen** | 2026-06-26 11:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:43:42` | `cowrie.session.connect` |
| `2026-06-26 11:43:42` | `cowrie.client.version` |
| `2026-06-26 11:43:43` | `cowrie.client.kex` |
| `2026-06-26 11:43:43` | `cowrie.login.success` |
| `2026-06-26 11:43:44` | `cowrie.session.params` |
| `2026-06-26 11:43:44` | `cowrie.command.input` |
| `2026-06-26 11:43:44` | `cowrie.log.closed` |
| `2026-06-26 11:43:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-552d1cbfda9f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 11:44 |
| **Last Seen** | 2026-06-26 11:44 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:44:22` | `cowrie.session.connect` |
| `2026-06-26 11:44:23` | `cowrie.client.version` |
| `2026-06-26 11:44:23` | `cowrie.client.kex` |
| `2026-06-26 11:44:30` | `cowrie.login.success` |
| `2026-06-26 11:44:33` | `cowrie.session.params` |
| `2026-06-26 11:44:33` | `cowrie.command.input` |
| `2026-06-26 11:44:35` | `cowrie.log.closed` |
| `2026-06-26 11:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-993e6761c85f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:44 |
| **Last Seen** | 2026-06-26 11:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:44:54` | `cowrie.session.connect` |
| `2026-06-26 11:44:54` | `cowrie.client.version` |
| `2026-06-26 11:44:54` | `cowrie.client.kex` |
| `2026-06-26 11:44:54` | `cowrie.login.success` |
| `2026-06-26 11:44:55` | `cowrie.session.params` |
| `2026-06-26 11:44:55` | `cowrie.command.input` |
| `2026-06-26 11:44:55` | `cowrie.log.closed` |
| `2026-06-26 11:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38c49bc2496f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:46 |
| **Last Seen** | 2026-06-26 11:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:46:10` | `cowrie.session.connect` |
| `2026-06-26 11:46:10` | `cowrie.client.version` |
| `2026-06-26 11:46:10` | `cowrie.client.kex` |
| `2026-06-26 11:46:11` | `cowrie.login.success` |
| `2026-06-26 11:46:11` | `cowrie.session.params` |
| `2026-06-26 11:46:11` | `cowrie.command.input` |
| `2026-06-26 11:46:11` | `cowrie.log.closed` |
| `2026-06-26 11:46:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dedc4d941daf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:47 |
| **Last Seen** | 2026-06-26 11:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:47:25` | `cowrie.session.connect` |
| `2026-06-26 11:47:25` | `cowrie.client.version` |
| `2026-06-26 11:47:25` | `cowrie.client.kex` |
| `2026-06-26 11:47:25` | `cowrie.login.success` |
| `2026-06-26 11:47:26` | `cowrie.session.params` |
| `2026-06-26 11:47:26` | `cowrie.command.input` |
| `2026-06-26 11:47:26` | `cowrie.log.closed` |
| `2026-06-26 11:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91e37b8c573f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 11:48 |
| **Last Seen** | 2026-06-26 11:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:48:02` | `cowrie.session.connect` |
| `2026-06-26 11:48:02` | `cowrie.client.version` |
| `2026-06-26 11:48:02` | `cowrie.client.kex` |
| `2026-06-26 11:48:05` | `cowrie.login.success` |
| `2026-06-26 11:48:07` | `cowrie.session.params` |
| `2026-06-26 11:48:07` | `cowrie.command.input` |
| `2026-06-26 11:48:07` | `cowrie.log.closed` |
| `2026-06-26 11:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca37ee12139d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:48 |
| **Last Seen** | 2026-06-26 11:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:48:36` | `cowrie.session.connect` |
| `2026-06-26 11:48:36` | `cowrie.client.version` |
| `2026-06-26 11:48:36` | `cowrie.client.kex` |
| `2026-06-26 11:48:36` | `cowrie.login.success` |
| `2026-06-26 11:48:37` | `cowrie.session.params` |
| `2026-06-26 11:48:37` | `cowrie.command.input` |
| `2026-06-26 11:48:37` | `cowrie.log.closed` |
| `2026-06-26 11:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5eb1b37d94b9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:49 |
| **Last Seen** | 2026-06-26 11:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:49:51` | `cowrie.session.connect` |
| `2026-06-26 11:49:51` | `cowrie.client.version` |
| `2026-06-26 11:49:51` | `cowrie.client.kex` |
| `2026-06-26 11:49:52` | `cowrie.login.success` |
| `2026-06-26 11:49:53` | `cowrie.session.params` |
| `2026-06-26 11:49:53` | `cowrie.command.input` |
| `2026-06-26 11:49:53` | `cowrie.log.closed` |
| `2026-06-26 11:49:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e39692777903

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:51 |
| **Last Seen** | 2026-06-26 11:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:51:10` | `cowrie.session.connect` |
| `2026-06-26 11:51:10` | `cowrie.client.version` |
| `2026-06-26 11:51:10` | `cowrie.client.kex` |
| `2026-06-26 11:51:10` | `cowrie.login.success` |
| `2026-06-26 11:51:11` | `cowrie.session.params` |
| `2026-06-26 11:51:11` | `cowrie.command.input` |
| `2026-06-26 11:51:11` | `cowrie.log.closed` |
| `2026-06-26 11:51:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-437dec0d0c16

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-26 11:51 |
| **Last Seen** | 2026-06-26 11:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:51:14` | `cowrie.session.connect` |
| `2026-06-26 11:51:14` | `cowrie.client.version` |
| `2026-06-26 11:51:14` | `cowrie.client.kex` |
| `2026-06-26 11:51:14` | `cowrie.login.success` |
| `2026-06-26 11:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e6448874a3e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-26 11:51 |
| **Last Seen** | 2026-06-26 11:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:51:14` | `cowrie.session.connect` |
| `2026-06-26 11:51:14` | `cowrie.client.version` |
| `2026-06-26 11:51:14` | `cowrie.client.kex` |
| `2026-06-26 11:51:14` | `cowrie.login.success` |
| `2026-06-26 11:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e6c80e9cf09

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-26 11:51 |
| **Last Seen** | 2026-06-26 11:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:51:19` | `cowrie.session.connect` |
| `2026-06-26 11:51:19` | `cowrie.client.version` |
| `2026-06-26 11:51:19` | `cowrie.client.kex` |
| `2026-06-26 11:51:19` | `cowrie.login.success` |
| `2026-06-26 11:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9394486261f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-26 11:51 |
| **Last Seen** | 2026-06-26 11:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:51:19` | `cowrie.session.connect` |
| `2026-06-26 11:51:19` | `cowrie.client.version` |
| `2026-06-26 11:51:19` | `cowrie.client.kex` |
| `2026-06-26 11:51:19` | `cowrie.login.success` |
| `2026-06-26 11:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f25e6f85e2b4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:52 |
| **Last Seen** | 2026-06-26 11:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:52:24` | `cowrie.session.connect` |
| `2026-06-26 11:52:24` | `cowrie.client.version` |
| `2026-06-26 11:52:24` | `cowrie.client.kex` |
| `2026-06-26 11:52:25` | `cowrie.login.success` |
| `2026-06-26 11:52:26` | `cowrie.session.params` |
| `2026-06-26 11:52:26` | `cowrie.command.input` |
| `2026-06-26 11:52:26` | `cowrie.log.closed` |
| `2026-06-26 11:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0777f0ea090e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:53 |
| **Last Seen** | 2026-06-26 11:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:53:41` | `cowrie.session.connect` |
| `2026-06-26 11:53:41` | `cowrie.client.version` |
| `2026-06-26 11:53:41` | `cowrie.client.kex` |
| `2026-06-26 11:53:42` | `cowrie.login.success` |
| `2026-06-26 11:53:43` | `cowrie.session.params` |
| `2026-06-26 11:53:43` | `cowrie.command.input` |
| `2026-06-26 11:53:43` | `cowrie.log.closed` |
| `2026-06-26 11:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f8ef604b068

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:54 |
| **Last Seen** | 2026-06-26 11:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:54:56` | `cowrie.session.connect` |
| `2026-06-26 11:54:56` | `cowrie.client.version` |
| `2026-06-26 11:54:56` | `cowrie.client.kex` |
| `2026-06-26 11:54:56` | `cowrie.login.success` |
| `2026-06-26 11:54:57` | `cowrie.session.params` |
| `2026-06-26 11:54:57` | `cowrie.command.input` |
| `2026-06-26 11:54:57` | `cowrie.log.closed` |
| `2026-06-26 11:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60b512dfa784

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 11:55 |
| **Last Seen** | 2026-06-26 11:55 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:55:39` | `cowrie.session.connect` |
| `2026-06-26 11:55:41` | `cowrie.client.version` |
| `2026-06-26 11:55:41` | `cowrie.client.kex` |
| `2026-06-26 11:55:46` | `cowrie.login.success` |
| `2026-06-26 11:55:50` | `cowrie.session.params` |
| `2026-06-26 11:55:50` | `cowrie.command.input` |
| `2026-06-26 11:55:51` | `cowrie.log.closed` |
| `2026-06-26 11:55:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d1639ac9b0f

| Field | Detail |
|---|---|
| **Source IP** | `64.62.156[.]24` |
| **First Seen** | 2026-06-26 11:55 |
| **Last Seen** | 2026-06-26 11:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:140.0) Gecko/20100101 Firefox/140.0, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:55:52` | `cowrie.session.connect` |
| `2026-06-26 11:55:52` | `cowrie.login.success` |
| `2026-06-26 11:55:53` | `cowrie.session.params` |
| `2026-06-26 11:55:53` | `cowrie.command.input` |
| `2026-06-26 11:55:53` | `cowrie.command.input` |
| `2026-06-26 11:55:53` | `cowrie.command.failed` |
| `2026-06-26 11:55:53` | `cowrie.command.input` |
| `2026-06-26 11:55:53` | `cowrie.command.failed` |
| `2026-06-26 11:55:53` | `cowrie.command.input` |
| `2026-06-26 11:55:53` | `cowrie.log.closed` |
| `2026-06-26 11:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.62.156[.]24` to AbuseIPDB if not already reported
- [ ] Block `64.62.156[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60d9e255ba2b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:56 |
| **Last Seen** | 2026-06-26 11:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:56:06` | `cowrie.session.connect` |
| `2026-06-26 11:56:06` | `cowrie.client.version` |
| `2026-06-26 11:56:06` | `cowrie.client.kex` |
| `2026-06-26 11:56:06` | `cowrie.login.success` |
| `2026-06-26 11:56:07` | `cowrie.session.params` |
| `2026-06-26 11:56:07` | `cowrie.command.input` |
| `2026-06-26 11:56:07` | `cowrie.log.closed` |
| `2026-06-26 11:56:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d4eb74b8896

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:57 |
| **Last Seen** | 2026-06-26 11:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:57:25` | `cowrie.session.connect` |
| `2026-06-26 11:57:25` | `cowrie.client.version` |
| `2026-06-26 11:57:25` | `cowrie.client.kex` |
| `2026-06-26 11:57:26` | `cowrie.login.success` |
| `2026-06-26 11:57:27` | `cowrie.session.params` |
| `2026-06-26 11:57:27` | `cowrie.command.input` |
| `2026-06-26 11:57:27` | `cowrie.log.closed` |
| `2026-06-26 11:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-039f6e794d39

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:58 |
| **Last Seen** | 2026-06-26 11:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:58:41` | `cowrie.session.connect` |
| `2026-06-26 11:58:41` | `cowrie.client.version` |
| `2026-06-26 11:58:41` | `cowrie.client.kex` |
| `2026-06-26 11:58:42` | `cowrie.login.success` |
| `2026-06-26 11:58:42` | `cowrie.session.params` |
| `2026-06-26 11:58:42` | `cowrie.command.input` |
| `2026-06-26 11:58:42` | `cowrie.log.closed` |
| `2026-06-26 11:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcf0fc83c0a6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 11:59 |
| **Last Seen** | 2026-06-26 11:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 11:59:58` | `cowrie.session.connect` |
| `2026-06-26 11:59:58` | `cowrie.client.version` |
| `2026-06-26 11:59:58` | `cowrie.client.kex` |
| `2026-06-26 11:59:58` | `cowrie.login.success` |
| `2026-06-26 11:59:59` | `cowrie.session.params` |
| `2026-06-26 11:59:59` | `cowrie.command.input` |
| `2026-06-26 11:59:59` | `cowrie.log.closed` |
| `2026-06-26 11:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bb5271a0520

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:00 |
| **Last Seen** | 2026-06-26 12:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:00:50` | `cowrie.session.connect` |
| `2026-06-26 12:00:50` | `cowrie.client.version` |
| `2026-06-26 12:00:50` | `cowrie.client.kex` |
| `2026-06-26 12:00:51` | `cowrie.login.success` |
| `2026-06-26 12:00:51` | `cowrie.session.params` |
| `2026-06-26 12:00:51` | `cowrie.command.input` |
| `2026-06-26 12:00:51` | `cowrie.log.closed` |
| `2026-06-26 12:00:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05815af4aa13

| Field | Detail |
|---|---|
| **Source IP** | `188.166.183[.]133` |
| **First Seen** | 2026-06-26 12:01 |
| **Last Seen** | 2026-06-26 12:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:01:22` | `cowrie.session.connect` |
| `2026-06-26 12:01:22` | `cowrie.client.version` |
| `2026-06-26 12:01:22` | `cowrie.client.kex` |
| `2026-06-26 12:01:23` | `cowrie.login.success` |
| `2026-06-26 12:01:24` | `cowrie.session.params` |
| `2026-06-26 12:01:24` | `cowrie.command.input` |
| `2026-06-26 12:01:24` | `cowrie.log.closed` |
| `2026-06-26 12:01:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.166.183[.]133` to AbuseIPDB if not already reported
- [ ] Block `188.166.183[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec4da0292d86

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:01 |
| **Last Seen** | 2026-06-26 12:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:01:37` | `cowrie.session.connect` |
| `2026-06-26 12:01:37` | `cowrie.client.version` |
| `2026-06-26 12:01:37` | `cowrie.client.kex` |
| `2026-06-26 12:01:37` | `cowrie.login.success` |
| `2026-06-26 12:01:38` | `cowrie.session.params` |
| `2026-06-26 12:01:38` | `cowrie.command.input` |
| `2026-06-26 12:01:38` | `cowrie.log.closed` |
| `2026-06-26 12:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c45e2984a54

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:02 |
| **Last Seen** | 2026-06-26 12:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:02:25` | `cowrie.session.connect` |
| `2026-06-26 12:02:25` | `cowrie.client.version` |
| `2026-06-26 12:02:25` | `cowrie.client.kex` |
| `2026-06-26 12:02:25` | `cowrie.login.success` |
| `2026-06-26 12:02:26` | `cowrie.session.params` |
| `2026-06-26 12:02:26` | `cowrie.command.input` |
| `2026-06-26 12:02:26` | `cowrie.log.closed` |
| `2026-06-26 12:02:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4af115a63a10

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 12:02 |
| **Last Seen** | 2026-06-26 12:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:02:32` | `cowrie.session.connect` |
| `2026-06-26 12:02:33` | `cowrie.client.version` |
| `2026-06-26 12:02:33` | `cowrie.client.kex` |
| `2026-06-26 12:02:34` | `cowrie.login.success` |
| `2026-06-26 12:02:36` | `cowrie.session.params` |
| `2026-06-26 12:02:36` | `cowrie.command.input` |
| `2026-06-26 12:02:36` | `cowrie.log.closed` |
| `2026-06-26 12:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3725a5c0a6e4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:03 |
| **Last Seen** | 2026-06-26 12:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:03:19` | `cowrie.session.connect` |
| `2026-06-26 12:03:19` | `cowrie.client.version` |
| `2026-06-26 12:03:19` | `cowrie.client.kex` |
| `2026-06-26 12:03:19` | `cowrie.login.success` |
| `2026-06-26 12:03:20` | `cowrie.session.params` |
| `2026-06-26 12:03:20` | `cowrie.command.input` |
| `2026-06-26 12:03:20` | `cowrie.log.closed` |
| `2026-06-26 12:03:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0d00101159a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-06-26 12:03 |
| **Last Seen** | 2026-06-26 12:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '000000' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:03:24` | `cowrie.session.connect` |
| `2026-06-26 12:03:24` | `cowrie.client.version` |
| `2026-06-26 12:03:24` | `cowrie.client.kex` |
| `2026-06-26 12:03:26` | `cowrie.login.success` |
| `2026-06-26 12:03:28` | `cowrie.session.params` |
| `2026-06-26 12:03:28` | `cowrie.command.input` |
| `2026-06-26 12:03:28` | `cowrie.command.input` |
| `2026-06-26 12:03:28` | `cowrie.command.input` |
| `2026-06-26 12:03:28` | `cowrie.command.input` |
| `2026-06-26 12:03:29` | `cowrie.log.closed` |
| `2026-06-26 12:03:30` | `cowrie.session.params` |
| `2026-06-26 12:03:30` | `cowrie.command.input` |
| `2026-06-26 12:03:30` | `cowrie.command.input` |
| `2026-06-26 12:03:30` | `cowrie.command.failed` |
| `2026-06-26 12:03:30` | `cowrie.command.failed` |
| `2026-06-26 12:03:30` | `cowrie.command.failed` |
| `2026-06-26 12:03:30` | `cowrie.command.failed` |
| `2026-06-26 12:03:31` | `cowrie.log.closed` |
| `2026-06-26 12:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98bc5690fa77

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:04 |
| **Last Seen** | 2026-06-26 12:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:04:08` | `cowrie.session.connect` |
| `2026-06-26 12:04:08` | `cowrie.client.version` |
| `2026-06-26 12:04:08` | `cowrie.client.kex` |
| `2026-06-26 12:04:09` | `cowrie.login.success` |
| `2026-06-26 12:04:09` | `cowrie.session.params` |
| `2026-06-26 12:04:09` | `cowrie.command.input` |
| `2026-06-26 12:04:10` | `cowrie.log.closed` |
| `2026-06-26 12:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c7a4f43b9c6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:04 |
| **Last Seen** | 2026-06-26 12:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:04:58` | `cowrie.session.connect` |
| `2026-06-26 12:04:58` | `cowrie.client.version` |
| `2026-06-26 12:04:58` | `cowrie.client.kex` |
| `2026-06-26 12:04:58` | `cowrie.login.success` |
| `2026-06-26 12:04:59` | `cowrie.session.params` |
| `2026-06-26 12:04:59` | `cowrie.command.input` |
| `2026-06-26 12:04:59` | `cowrie.log.closed` |
| `2026-06-26 12:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbc049549bb0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-06-26 12:05 |
| **Last Seen** | 2026-06-26 12:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '111111' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:05:25` | `cowrie.session.connect` |
| `2026-06-26 12:05:26` | `cowrie.client.version` |
| `2026-06-26 12:05:26` | `cowrie.client.kex` |
| `2026-06-26 12:05:28` | `cowrie.login.success` |
| `2026-06-26 12:05:29` | `cowrie.session.params` |
| `2026-06-26 12:05:29` | `cowrie.command.input` |
| `2026-06-26 12:05:29` | `cowrie.command.input` |
| `2026-06-26 12:05:29` | `cowrie.command.input` |
| `2026-06-26 12:05:29` | `cowrie.command.input` |
| `2026-06-26 12:05:30` | `cowrie.log.closed` |
| `2026-06-26 12:05:31` | `cowrie.session.params` |
| `2026-06-26 12:05:31` | `cowrie.command.input` |
| `2026-06-26 12:05:31` | `cowrie.command.input` |
| `2026-06-26 12:05:31` | `cowrie.command.failed` |
| `2026-06-26 12:05:31` | `cowrie.command.failed` |
| `2026-06-26 12:05:31` | `cowrie.command.failed` |
| `2026-06-26 12:05:31` | `cowrie.command.failed` |
| `2026-06-26 12:05:32` | `cowrie.log.closed` |
| `2026-06-26 12:05:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d43afe9755a2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:05 |
| **Last Seen** | 2026-06-26 12:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:05:50` | `cowrie.session.connect` |
| `2026-06-26 12:05:50` | `cowrie.client.version` |
| `2026-06-26 12:05:51` | `cowrie.client.kex` |
| `2026-06-26 12:05:51` | `cowrie.login.success` |
| `2026-06-26 12:05:52` | `cowrie.session.params` |
| `2026-06-26 12:05:52` | `cowrie.command.input` |
| `2026-06-26 12:05:52` | `cowrie.log.closed` |
| `2026-06-26 12:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72f82c342089

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:06 |
| **Last Seen** | 2026-06-26 12:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:06:41` | `cowrie.session.connect` |
| `2026-06-26 12:06:41` | `cowrie.client.version` |
| `2026-06-26 12:06:41` | `cowrie.client.kex` |
| `2026-06-26 12:06:41` | `cowrie.login.success` |
| `2026-06-26 12:06:42` | `cowrie.session.params` |
| `2026-06-26 12:06:42` | `cowrie.command.input` |
| `2026-06-26 12:06:42` | `cowrie.log.closed` |
| `2026-06-26 12:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0aa4d9d3182

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 12:07 |
| **Last Seen** | 2026-06-26 12:07 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:07:08` | `cowrie.session.connect` |
| `2026-06-26 12:07:10` | `cowrie.client.version` |
| `2026-06-26 12:07:10` | `cowrie.client.kex` |
| `2026-06-26 12:07:15` | `cowrie.login.success` |
| `2026-06-26 12:07:18` | `cowrie.session.params` |
| `2026-06-26 12:07:18` | `cowrie.command.input` |
| `2026-06-26 12:07:19` | `cowrie.log.closed` |
| `2026-06-26 12:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19fe7d7cce27

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-06-26 12:07 |
| **Last Seen** | 2026-06-26 12:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:07:25` | `cowrie.session.connect` |
| `2026-06-26 12:07:26` | `cowrie.client.version` |
| `2026-06-26 12:07:26` | `cowrie.client.kex` |
| `2026-06-26 12:07:29` | `cowrie.login.success` |
| `2026-06-26 12:07:30` | `cowrie.session.params` |
| `2026-06-26 12:07:30` | `cowrie.command.input` |
| `2026-06-26 12:07:30` | `cowrie.command.input` |
| `2026-06-26 12:07:30` | `cowrie.command.input` |
| `2026-06-26 12:07:30` | `cowrie.command.input` |
| `2026-06-26 12:07:31` | `cowrie.log.closed` |
| `2026-06-26 12:07:32` | `cowrie.session.params` |
| `2026-06-26 12:07:32` | `cowrie.command.input` |
| `2026-06-26 12:07:32` | `cowrie.command.input` |
| `2026-06-26 12:07:32` | `cowrie.command.failed` |
| `2026-06-26 12:07:32` | `cowrie.command.failed` |
| `2026-06-26 12:07:32` | `cowrie.command.failed` |
| `2026-06-26 12:07:32` | `cowrie.command.failed` |
| `2026-06-26 12:07:33` | `cowrie.log.closed` |
| `2026-06-26 12:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fa4c9a9a4c9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:07 |
| **Last Seen** | 2026-06-26 12:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:07:31` | `cowrie.session.connect` |
| `2026-06-26 12:07:31` | `cowrie.client.version` |
| `2026-06-26 12:07:32` | `cowrie.client.kex` |
| `2026-06-26 12:07:32` | `cowrie.login.success` |
| `2026-06-26 12:07:33` | `cowrie.session.params` |
| `2026-06-26 12:07:33` | `cowrie.command.input` |
| `2026-06-26 12:07:33` | `cowrie.log.closed` |
| `2026-06-26 12:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44000cd0f5d9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:08 |
| **Last Seen** | 2026-06-26 12:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:08:20` | `cowrie.session.connect` |
| `2026-06-26 12:08:20` | `cowrie.client.version` |
| `2026-06-26 12:08:20` | `cowrie.client.kex` |
| `2026-06-26 12:08:20` | `cowrie.login.success` |
| `2026-06-26 12:08:21` | `cowrie.session.params` |
| `2026-06-26 12:08:21` | `cowrie.command.input` |
| `2026-06-26 12:08:21` | `cowrie.log.closed` |
| `2026-06-26 12:08:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c01442bf5e91

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:09 |
| **Last Seen** | 2026-06-26 12:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:09:08` | `cowrie.session.connect` |
| `2026-06-26 12:09:08` | `cowrie.client.version` |
| `2026-06-26 12:09:08` | `cowrie.client.kex` |
| `2026-06-26 12:09:09` | `cowrie.login.success` |
| `2026-06-26 12:09:09` | `cowrie.session.params` |
| `2026-06-26 12:09:09` | `cowrie.command.input` |
| `2026-06-26 12:09:09` | `cowrie.log.closed` |
| `2026-06-26 12:09:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ade604a36266

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-06-26 12:09 |
| **Last Seen** | 2026-06-26 12:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:09:27` | `cowrie.session.connect` |
| `2026-06-26 12:09:28` | `cowrie.client.version` |
| `2026-06-26 12:09:28` | `cowrie.client.kex` |
| `2026-06-26 12:09:31` | `cowrie.login.success` |
| `2026-06-26 12:09:32` | `cowrie.session.params` |
| `2026-06-26 12:09:32` | `cowrie.command.input` |
| `2026-06-26 12:09:32` | `cowrie.command.input` |
| `2026-06-26 12:09:32` | `cowrie.command.input` |
| `2026-06-26 12:09:32` | `cowrie.command.input` |
| `2026-06-26 12:09:33` | `cowrie.log.closed` |
| `2026-06-26 12:09:34` | `cowrie.session.params` |
| `2026-06-26 12:09:34` | `cowrie.command.input` |
| `2026-06-26 12:09:34` | `cowrie.command.input` |
| `2026-06-26 12:09:34` | `cowrie.command.failed` |
| `2026-06-26 12:09:34` | `cowrie.command.failed` |
| `2026-06-26 12:09:34` | `cowrie.command.failed` |
| `2026-06-26 12:09:34` | `cowrie.command.failed` |
| `2026-06-26 12:09:35` | `cowrie.log.closed` |
| `2026-06-26 12:09:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6091767b0ba

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:10 |
| **Last Seen** | 2026-06-26 12:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:10:00` | `cowrie.session.connect` |
| `2026-06-26 12:10:00` | `cowrie.client.version` |
| `2026-06-26 12:10:01` | `cowrie.client.kex` |
| `2026-06-26 12:10:01` | `cowrie.login.success` |
| `2026-06-26 12:10:02` | `cowrie.session.params` |
| `2026-06-26 12:10:02` | `cowrie.command.input` |
| `2026-06-26 12:10:02` | `cowrie.log.closed` |
| `2026-06-26 12:10:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba8a1daf4f9e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:10 |
| **Last Seen** | 2026-06-26 12:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:10:55` | `cowrie.session.connect` |
| `2026-06-26 12:10:55` | `cowrie.client.version` |
| `2026-06-26 12:10:55` | `cowrie.client.kex` |
| `2026-06-26 12:10:55` | `cowrie.login.success` |
| `2026-06-26 12:10:56` | `cowrie.session.params` |
| `2026-06-26 12:10:56` | `cowrie.command.input` |
| `2026-06-26 12:10:56` | `cowrie.log.closed` |
| `2026-06-26 12:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d5024ce7a37

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-06-26 12:11 |
| **Last Seen** | 2026-06-26 12:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:11:32` | `cowrie.session.connect` |
| `2026-06-26 12:11:32` | `cowrie.client.version` |
| `2026-06-26 12:11:32` | `cowrie.client.kex` |
| `2026-06-26 12:11:35` | `cowrie.login.success` |
| `2026-06-26 12:11:36` | `cowrie.session.params` |
| `2026-06-26 12:11:36` | `cowrie.command.input` |
| `2026-06-26 12:11:36` | `cowrie.command.input` |
| `2026-06-26 12:11:36` | `cowrie.command.input` |
| `2026-06-26 12:11:36` | `cowrie.command.input` |
| `2026-06-26 12:11:37` | `cowrie.log.closed` |
| `2026-06-26 12:11:38` | `cowrie.session.params` |
| `2026-06-26 12:11:38` | `cowrie.command.input` |
| `2026-06-26 12:11:38` | `cowrie.command.input` |
| `2026-06-26 12:11:38` | `cowrie.command.failed` |
| `2026-06-26 12:11:38` | `cowrie.command.failed` |
| `2026-06-26 12:11:38` | `cowrie.command.failed` |
| `2026-06-26 12:11:38` | `cowrie.command.failed` |
| `2026-06-26 12:11:39` | `cowrie.log.closed` |
| `2026-06-26 12:11:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db5e0531a766

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:11 |
| **Last Seen** | 2026-06-26 12:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:11:46` | `cowrie.session.connect` |
| `2026-06-26 12:11:46` | `cowrie.client.version` |
| `2026-06-26 12:11:46` | `cowrie.client.kex` |
| `2026-06-26 12:11:46` | `cowrie.login.success` |
| `2026-06-26 12:11:47` | `cowrie.session.params` |
| `2026-06-26 12:11:47` | `cowrie.command.input` |
| `2026-06-26 12:11:47` | `cowrie.log.closed` |
| `2026-06-26 12:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a658f02b26c6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:12 |
| **Last Seen** | 2026-06-26 12:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:12:40` | `cowrie.session.connect` |
| `2026-06-26 12:12:40` | `cowrie.client.version` |
| `2026-06-26 12:12:40` | `cowrie.client.kex` |
| `2026-06-26 12:12:40` | `cowrie.login.success` |
| `2026-06-26 12:12:41` | `cowrie.session.params` |
| `2026-06-26 12:12:41` | `cowrie.command.input` |
| `2026-06-26 12:12:41` | `cowrie.log.closed` |
| `2026-06-26 12:12:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21ac6226d6a8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:13 |
| **Last Seen** | 2026-06-26 12:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:13:31` | `cowrie.session.connect` |
| `2026-06-26 12:13:31` | `cowrie.client.version` |
| `2026-06-26 12:13:31` | `cowrie.client.kex` |
| `2026-06-26 12:13:31` | `cowrie.login.success` |
| `2026-06-26 12:13:32` | `cowrie.session.params` |
| `2026-06-26 12:13:32` | `cowrie.command.input` |
| `2026-06-26 12:13:32` | `cowrie.log.closed` |
| `2026-06-26 12:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a95d31d903d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-06-26 12:13 |
| **Last Seen** | 2026-06-26 12:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:13:35` | `cowrie.session.connect` |
| `2026-06-26 12:13:35` | `cowrie.client.version` |
| `2026-06-26 12:13:35` | `cowrie.client.kex` |
| `2026-06-26 12:13:38` | `cowrie.login.success` |
| `2026-06-26 12:13:39` | `cowrie.session.params` |
| `2026-06-26 12:13:39` | `cowrie.command.input` |
| `2026-06-26 12:13:39` | `cowrie.command.input` |
| `2026-06-26 12:13:39` | `cowrie.command.input` |
| `2026-06-26 12:13:39` | `cowrie.command.input` |
| `2026-06-26 12:13:40` | `cowrie.log.closed` |
| `2026-06-26 12:13:42` | `cowrie.session.params` |
| `2026-06-26 12:13:42` | `cowrie.command.input` |
| `2026-06-26 12:13:42` | `cowrie.command.input` |
| `2026-06-26 12:13:42` | `cowrie.command.failed` |
| `2026-06-26 12:13:42` | `cowrie.command.failed` |
| `2026-06-26 12:13:42` | `cowrie.command.failed` |
| `2026-06-26 12:13:42` | `cowrie.command.failed` |
| `2026-06-26 12:13:42` | `cowrie.log.closed` |
| `2026-06-26 12:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-881c91c5a2a5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:14 |
| **Last Seen** | 2026-06-26 12:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:14:20` | `cowrie.session.connect` |
| `2026-06-26 12:14:20` | `cowrie.client.version` |
| `2026-06-26 12:14:21` | `cowrie.client.kex` |
| `2026-06-26 12:14:21` | `cowrie.login.success` |
| `2026-06-26 12:14:22` | `cowrie.session.params` |
| `2026-06-26 12:14:22` | `cowrie.command.input` |
| `2026-06-26 12:14:22` | `cowrie.log.closed` |
| `2026-06-26 12:14:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4dde32e86e8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:15 |
| **Last Seen** | 2026-06-26 12:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:15:15` | `cowrie.session.connect` |
| `2026-06-26 12:15:15` | `cowrie.client.version` |
| `2026-06-26 12:15:15` | `cowrie.client.kex` |
| `2026-06-26 12:15:15` | `cowrie.login.success` |
| `2026-06-26 12:15:16` | `cowrie.session.params` |
| `2026-06-26 12:15:16` | `cowrie.command.input` |
| `2026-06-26 12:15:16` | `cowrie.log.closed` |
| `2026-06-26 12:15:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39436cffd09c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:16 |
| **Last Seen** | 2026-06-26 12:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:16:06` | `cowrie.session.connect` |
| `2026-06-26 12:16:06` | `cowrie.client.version` |
| `2026-06-26 12:16:07` | `cowrie.client.kex` |
| `2026-06-26 12:16:07` | `cowrie.login.success` |
| `2026-06-26 12:16:08` | `cowrie.session.params` |
| `2026-06-26 12:16:08` | `cowrie.command.input` |
| `2026-06-26 12:16:08` | `cowrie.log.closed` |
| `2026-06-26 12:16:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e2faa1c29ee

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 12:16 |
| **Last Seen** | 2026-06-26 12:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:16:59` | `cowrie.session.connect` |
| `2026-06-26 12:16:59` | `cowrie.client.version` |
| `2026-06-26 12:16:59` | `cowrie.client.kex` |
| `2026-06-26 12:17:01` | `cowrie.login.success` |
| `2026-06-26 12:17:03` | `cowrie.session.params` |
| `2026-06-26 12:17:03` | `cowrie.command.input` |
| `2026-06-26 12:17:03` | `cowrie.log.closed` |
| `2026-06-26 12:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d293bd3db249

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:17 |
| **Last Seen** | 2026-06-26 12:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:17:04` | `cowrie.session.connect` |
| `2026-06-26 12:17:04` | `cowrie.client.version` |
| `2026-06-26 12:17:04` | `cowrie.client.kex` |
| `2026-06-26 12:17:04` | `cowrie.login.success` |
| `2026-06-26 12:17:05` | `cowrie.session.params` |
| `2026-06-26 12:17:05` | `cowrie.command.input` |
| `2026-06-26 12:17:05` | `cowrie.log.closed` |
| `2026-06-26 12:17:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0794d2f0246

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-06-26 12:17 |
| **Last Seen** | 2026-06-26 12:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345678' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:17:26` | `cowrie.session.connect` |
| `2026-06-26 12:17:27` | `cowrie.client.version` |
| `2026-06-26 12:17:27` | `cowrie.client.kex` |
| `2026-06-26 12:17:29` | `cowrie.login.success` |
| `2026-06-26 12:17:31` | `cowrie.session.params` |
| `2026-06-26 12:17:31` | `cowrie.command.input` |
| `2026-06-26 12:17:31` | `cowrie.command.input` |
| `2026-06-26 12:17:31` | `cowrie.command.input` |
| `2026-06-26 12:17:31` | `cowrie.command.input` |
| `2026-06-26 12:17:31` | `cowrie.log.closed` |
| `2026-06-26 12:17:33` | `cowrie.session.params` |
| `2026-06-26 12:17:33` | `cowrie.command.input` |
| `2026-06-26 12:17:33` | `cowrie.command.input` |
| `2026-06-26 12:17:33` | `cowrie.command.failed` |
| `2026-06-26 12:17:33` | `cowrie.command.failed` |
| `2026-06-26 12:17:33` | `cowrie.command.failed` |
| `2026-06-26 12:17:33` | `cowrie.command.failed` |
| `2026-06-26 12:17:33` | `cowrie.log.closed` |
| `2026-06-26 12:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-928de19bf055

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:17 |
| **Last Seen** | 2026-06-26 12:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:17:58` | `cowrie.session.connect` |
| `2026-06-26 12:17:58` | `cowrie.client.version` |
| `2026-06-26 12:17:58` | `cowrie.client.kex` |
| `2026-06-26 12:17:58` | `cowrie.login.success` |
| `2026-06-26 12:17:59` | `cowrie.session.params` |
| `2026-06-26 12:17:59` | `cowrie.command.input` |
| `2026-06-26 12:17:59` | `cowrie.log.closed` |
| `2026-06-26 12:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-526c9e2f9f45

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 12:18 |
| **Last Seen** | 2026-06-26 12:18 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:18:24` | `cowrie.session.connect` |
| `2026-06-26 12:18:26` | `cowrie.client.version` |
| `2026-06-26 12:18:26` | `cowrie.client.kex` |
| `2026-06-26 12:18:31` | `cowrie.login.success` |
| `2026-06-26 12:18:35` | `cowrie.session.params` |
| `2026-06-26 12:18:35` | `cowrie.command.input` |
| `2026-06-26 12:18:36` | `cowrie.log.closed` |
| `2026-06-26 12:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e0c1209253a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:18 |
| **Last Seen** | 2026-06-26 12:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:18:49` | `cowrie.session.connect` |
| `2026-06-26 12:18:49` | `cowrie.client.version` |
| `2026-06-26 12:18:49` | `cowrie.client.kex` |
| `2026-06-26 12:18:49` | `cowrie.login.success` |
| `2026-06-26 12:18:50` | `cowrie.session.params` |
| `2026-06-26 12:18:50` | `cowrie.command.input` |
| `2026-06-26 12:18:50` | `cowrie.log.closed` |
| `2026-06-26 12:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-785544f4c513

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-06-26 12:19 |
| **Last Seen** | 2026-06-26 12:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123456789' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:19:19` | `cowrie.session.connect` |
| `2026-06-26 12:19:19` | `cowrie.client.version` |
| `2026-06-26 12:19:19` | `cowrie.client.kex` |
| `2026-06-26 12:19:20` | `cowrie.login.success` |
| `2026-06-26 12:19:22` | `cowrie.session.params` |
| `2026-06-26 12:19:22` | `cowrie.command.input` |
| `2026-06-26 12:19:22` | `cowrie.command.input` |
| `2026-06-26 12:19:22` | `cowrie.command.input` |
| `2026-06-26 12:19:22` | `cowrie.command.input` |
| `2026-06-26 12:19:22` | `cowrie.log.closed` |
| `2026-06-26 12:19:23` | `cowrie.session.params` |
| `2026-06-26 12:19:23` | `cowrie.command.input` |
| `2026-06-26 12:19:23` | `cowrie.command.input` |
| `2026-06-26 12:19:23` | `cowrie.command.failed` |
| `2026-06-26 12:19:23` | `cowrie.command.failed` |
| `2026-06-26 12:19:23` | `cowrie.command.failed` |
| `2026-06-26 12:19:23` | `cowrie.command.failed` |
| `2026-06-26 12:19:24` | `cowrie.log.closed` |
| `2026-06-26 12:19:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26c5e3da95b0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:19 |
| **Last Seen** | 2026-06-26 12:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:19:40` | `cowrie.session.connect` |
| `2026-06-26 12:19:40` | `cowrie.client.version` |
| `2026-06-26 12:19:40` | `cowrie.client.kex` |
| `2026-06-26 12:19:40` | `cowrie.login.success` |
| `2026-06-26 12:19:41` | `cowrie.session.params` |
| `2026-06-26 12:19:41` | `cowrie.command.input` |
| `2026-06-26 12:19:41` | `cowrie.log.closed` |
| `2026-06-26 12:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2d1e1b4a2c1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:20 |
| **Last Seen** | 2026-06-26 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:20:34` | `cowrie.session.connect` |
| `2026-06-26 12:20:34` | `cowrie.client.version` |
| `2026-06-26 12:20:34` | `cowrie.client.kex` |
| `2026-06-26 12:20:34` | `cowrie.login.success` |
| `2026-06-26 12:20:35` | `cowrie.session.params` |
| `2026-06-26 12:20:35` | `cowrie.command.input` |
| `2026-06-26 12:20:35` | `cowrie.log.closed` |
| `2026-06-26 12:20:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3d2d9b491a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-06-26 12:21 |
| **Last Seen** | 2026-06-26 12:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1q2w3e4r' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:21:10` | `cowrie.session.connect` |
| `2026-06-26 12:21:10` | `cowrie.client.version` |
| `2026-06-26 12:21:10` | `cowrie.client.kex` |
| `2026-06-26 12:21:11` | `cowrie.login.success` |
| `2026-06-26 12:21:12` | `cowrie.session.params` |
| `2026-06-26 12:21:12` | `cowrie.command.input` |
| `2026-06-26 12:21:12` | `cowrie.command.input` |
| `2026-06-26 12:21:12` | `cowrie.command.input` |
| `2026-06-26 12:21:12` | `cowrie.command.input` |
| `2026-06-26 12:21:13` | `cowrie.log.closed` |
| `2026-06-26 12:21:14` | `cowrie.session.params` |
| `2026-06-26 12:21:14` | `cowrie.command.input` |
| `2026-06-26 12:21:14` | `cowrie.command.input` |
| `2026-06-26 12:21:14` | `cowrie.command.failed` |
| `2026-06-26 12:21:14` | `cowrie.command.failed` |
| `2026-06-26 12:21:14` | `cowrie.command.failed` |
| `2026-06-26 12:21:14` | `cowrie.command.failed` |
| `2026-06-26 12:21:14` | `cowrie.log.closed` |
| `2026-06-26 12:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbb845fd3124

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:21 |
| **Last Seen** | 2026-06-26 12:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:21:26` | `cowrie.session.connect` |
| `2026-06-26 12:21:26` | `cowrie.client.version` |
| `2026-06-26 12:21:26` | `cowrie.client.kex` |
| `2026-06-26 12:21:27` | `cowrie.login.success` |
| `2026-06-26 12:21:27` | `cowrie.session.params` |
| `2026-06-26 12:21:27` | `cowrie.command.input` |
| `2026-06-26 12:21:27` | `cowrie.log.closed` |
| `2026-06-26 12:21:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e1e56e6edad

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:22 |
| **Last Seen** | 2026-06-26 12:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:22:28` | `cowrie.session.connect` |
| `2026-06-26 12:22:28` | `cowrie.client.version` |
| `2026-06-26 12:22:28` | `cowrie.client.kex` |
| `2026-06-26 12:22:29` | `cowrie.login.success` |
| `2026-06-26 12:22:30` | `cowrie.session.params` |
| `2026-06-26 12:22:30` | `cowrie.command.input` |
| `2026-06-26 12:22:30` | `cowrie.log.closed` |
| `2026-06-26 12:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1eb7791b7c6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-06-26 12:22 |
| **Last Seen** | 2026-06-26 12:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '654321' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:22:57` | `cowrie.session.connect` |
| `2026-06-26 12:22:57` | `cowrie.client.version` |
| `2026-06-26 12:22:57` | `cowrie.client.kex` |
| `2026-06-26 12:22:59` | `cowrie.login.success` |
| `2026-06-26 12:23:00` | `cowrie.session.params` |
| `2026-06-26 12:23:00` | `cowrie.command.input` |
| `2026-06-26 12:23:00` | `cowrie.command.input` |
| `2026-06-26 12:23:00` | `cowrie.command.input` |
| `2026-06-26 12:23:00` | `cowrie.command.input` |
| `2026-06-26 12:23:00` | `cowrie.log.closed` |
| `2026-06-26 12:23:02` | `cowrie.session.params` |
| `2026-06-26 12:23:02` | `cowrie.command.input` |
| `2026-06-26 12:23:02` | `cowrie.command.input` |
| `2026-06-26 12:23:02` | `cowrie.command.failed` |
| `2026-06-26 12:23:02` | `cowrie.command.failed` |
| `2026-06-26 12:23:02` | `cowrie.command.failed` |
| `2026-06-26 12:23:02` | `cowrie.command.failed` |
| `2026-06-26 12:23:02` | `cowrie.log.closed` |
| `2026-06-26 12:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f9ff49a57b9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:24 |
| **Last Seen** | 2026-06-26 12:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:24:00` | `cowrie.session.connect` |
| `2026-06-26 12:24:00` | `cowrie.client.version` |
| `2026-06-26 12:24:00` | `cowrie.client.kex` |
| `2026-06-26 12:24:00` | `cowrie.login.success` |
| `2026-06-26 12:24:01` | `cowrie.session.params` |
| `2026-06-26 12:24:01` | `cowrie.command.input` |
| `2026-06-26 12:24:01` | `cowrie.log.closed` |
| `2026-06-26 12:24:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32d610489d03

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-06-26 12:24 |
| **Last Seen** | 2026-06-26 12:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'P@ssw0rd' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:24:48` | `cowrie.session.connect` |
| `2026-06-26 12:24:48` | `cowrie.client.version` |
| `2026-06-26 12:24:48` | `cowrie.client.kex` |
| `2026-06-26 12:24:50` | `cowrie.login.success` |
| `2026-06-26 12:24:51` | `cowrie.session.params` |
| `2026-06-26 12:24:51` | `cowrie.command.input` |
| `2026-06-26 12:24:51` | `cowrie.command.input` |
| `2026-06-26 12:24:51` | `cowrie.command.input` |
| `2026-06-26 12:24:51` | `cowrie.command.input` |
| `2026-06-26 12:24:52` | `cowrie.log.closed` |
| `2026-06-26 12:24:53` | `cowrie.session.params` |
| `2026-06-26 12:24:53` | `cowrie.command.input` |
| `2026-06-26 12:24:53` | `cowrie.command.input` |
| `2026-06-26 12:24:53` | `cowrie.command.failed` |
| `2026-06-26 12:24:53` | `cowrie.command.failed` |
| `2026-06-26 12:24:53` | `cowrie.command.failed` |
| `2026-06-26 12:24:53` | `cowrie.command.failed` |
| `2026-06-26 12:24:53` | `cowrie.log.closed` |
| `2026-06-26 12:24:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecce45050a65

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:24 |
| **Last Seen** | 2026-06-26 12:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:24:55` | `cowrie.session.connect` |
| `2026-06-26 12:24:55` | `cowrie.client.version` |
| `2026-06-26 12:24:55` | `cowrie.client.kex` |
| `2026-06-26 12:24:55` | `cowrie.login.success` |
| `2026-06-26 12:24:56` | `cowrie.session.params` |
| `2026-06-26 12:24:56` | `cowrie.command.input` |
| `2026-06-26 12:24:56` | `cowrie.log.closed` |
| `2026-06-26 12:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68231eb2459c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:25 |
| **Last Seen** | 2026-06-26 12:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:25:50` | `cowrie.session.connect` |
| `2026-06-26 12:25:50` | `cowrie.client.version` |
| `2026-06-26 12:25:50` | `cowrie.client.kex` |
| `2026-06-26 12:25:51` | `cowrie.login.success` |
| `2026-06-26 12:25:51` | `cowrie.session.params` |
| `2026-06-26 12:25:51` | `cowrie.command.input` |
| `2026-06-26 12:25:52` | `cowrie.log.closed` |
| `2026-06-26 12:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5769a7bd9a1b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-06-26 12:26 |
| **Last Seen** | 2026-06-26 12:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'admin' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:26:38` | `cowrie.session.connect` |
| `2026-06-26 12:26:39` | `cowrie.client.version` |
| `2026-06-26 12:26:39` | `cowrie.client.kex` |
| `2026-06-26 12:26:40` | `cowrie.login.success` |
| `2026-06-26 12:26:42` | `cowrie.session.params` |
| `2026-06-26 12:26:42` | `cowrie.command.input` |
| `2026-06-26 12:26:42` | `cowrie.command.input` |
| `2026-06-26 12:26:42` | `cowrie.command.input` |
| `2026-06-26 12:26:42` | `cowrie.command.input` |
| `2026-06-26 12:26:42` | `cowrie.log.closed` |
| `2026-06-26 12:26:44` | `cowrie.session.params` |
| `2026-06-26 12:26:44` | `cowrie.command.input` |
| `2026-06-26 12:26:44` | `cowrie.command.input` |
| `2026-06-26 12:26:44` | `cowrie.command.failed` |
| `2026-06-26 12:26:44` | `cowrie.command.failed` |
| `2026-06-26 12:26:44` | `cowrie.command.failed` |
| `2026-06-26 12:26:44` | `cowrie.command.failed` |
| `2026-06-26 12:26:44` | `cowrie.log.closed` |
| `2026-06-26 12:26:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eed5ea840398

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:26 |
| **Last Seen** | 2026-06-26 12:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:26:44` | `cowrie.session.connect` |
| `2026-06-26 12:26:44` | `cowrie.client.version` |
| `2026-06-26 12:26:44` | `cowrie.client.kex` |
| `2026-06-26 12:26:44` | `cowrie.login.success` |
| `2026-06-26 12:26:45` | `cowrie.session.params` |
| `2026-06-26 12:26:45` | `cowrie.command.input` |
| `2026-06-26 12:26:45` | `cowrie.log.closed` |
| `2026-06-26 12:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfd42467387c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:27 |
| **Last Seen** | 2026-06-26 12:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:27:34` | `cowrie.session.connect` |
| `2026-06-26 12:27:34` | `cowrie.client.version` |
| `2026-06-26 12:27:34` | `cowrie.client.kex` |
| `2026-06-26 12:27:34` | `cowrie.login.success` |
| `2026-06-26 12:27:35` | `cowrie.session.params` |
| `2026-06-26 12:27:35` | `cowrie.command.input` |
| `2026-06-26 12:27:35` | `cowrie.log.closed` |
| `2026-06-26 12:27:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a30c47e68d0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:28 |
| **Last Seen** | 2026-06-26 12:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:28:27` | `cowrie.session.connect` |
| `2026-06-26 12:28:27` | `cowrie.client.version` |
| `2026-06-26 12:28:27` | `cowrie.client.kex` |
| `2026-06-26 12:28:28` | `cowrie.login.success` |
| `2026-06-26 12:28:28` | `cowrie.session.params` |
| `2026-06-26 12:28:28` | `cowrie.command.input` |
| `2026-06-26 12:28:29` | `cowrie.log.closed` |
| `2026-06-26 12:28:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a5e29879b6a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-06-26 12:28 |
| **Last Seen** | 2026-06-26 12:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'admin123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:28:29` | `cowrie.session.connect` |
| `2026-06-26 12:28:29` | `cowrie.client.version` |
| `2026-06-26 12:28:29` | `cowrie.client.kex` |
| `2026-06-26 12:28:30` | `cowrie.login.success` |
| `2026-06-26 12:28:32` | `cowrie.session.params` |
| `2026-06-26 12:28:32` | `cowrie.command.input` |
| `2026-06-26 12:28:32` | `cowrie.command.input` |
| `2026-06-26 12:28:32` | `cowrie.command.input` |
| `2026-06-26 12:28:32` | `cowrie.command.input` |
| `2026-06-26 12:28:32` | `cowrie.log.closed` |
| `2026-06-26 12:28:33` | `cowrie.session.params` |
| `2026-06-26 12:28:33` | `cowrie.command.input` |
| `2026-06-26 12:28:33` | `cowrie.command.input` |
| `2026-06-26 12:28:33` | `cowrie.command.failed` |
| `2026-06-26 12:28:33` | `cowrie.command.failed` |
| `2026-06-26 12:28:33` | `cowrie.command.failed` |
| `2026-06-26 12:28:33` | `cowrie.command.failed` |
| `2026-06-26 12:28:33` | `cowrie.log.closed` |
| `2026-06-26 12:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf59692ce38a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 12:29 |
| **Last Seen** | 2026-06-26 12:29 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:29:17` | `cowrie.session.connect` |
| `2026-06-26 12:29:19` | `cowrie.client.version` |
| `2026-06-26 12:29:19` | `cowrie.client.kex` |
| `2026-06-26 12:29:25` | `cowrie.login.success` |
| `2026-06-26 12:29:28` | `cowrie.session.params` |
| `2026-06-26 12:29:28` | `cowrie.command.input` |
| `2026-06-26 12:29:30` | `cowrie.log.closed` |
| `2026-06-26 12:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82dd0b3524b6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:29 |
| **Last Seen** | 2026-06-26 12:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:29:22` | `cowrie.session.connect` |
| `2026-06-26 12:29:22` | `cowrie.client.version` |
| `2026-06-26 12:29:22` | `cowrie.client.kex` |
| `2026-06-26 12:29:22` | `cowrie.login.success` |
| `2026-06-26 12:29:23` | `cowrie.session.params` |
| `2026-06-26 12:29:23` | `cowrie.command.input` |
| `2026-06-26 12:29:23` | `cowrie.log.closed` |
| `2026-06-26 12:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74763b8ad727

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:30 |
| **Last Seen** | 2026-06-26 12:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:30:17` | `cowrie.session.connect` |
| `2026-06-26 12:30:17` | `cowrie.client.version` |
| `2026-06-26 12:30:17` | `cowrie.client.kex` |
| `2026-06-26 12:30:17` | `cowrie.login.success` |
| `2026-06-26 12:30:18` | `cowrie.session.params` |
| `2026-06-26 12:30:18` | `cowrie.command.input` |
| `2026-06-26 12:30:18` | `cowrie.log.closed` |
| `2026-06-26 12:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-729a5f341f28

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-06-26 12:30 |
| **Last Seen** | 2026-06-26 12:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'passw0rd' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:30:18` | `cowrie.session.connect` |
| `2026-06-26 12:30:19` | `cowrie.client.version` |
| `2026-06-26 12:30:19` | `cowrie.client.kex` |
| `2026-06-26 12:30:20` | `cowrie.login.success` |
| `2026-06-26 12:30:22` | `cowrie.session.params` |
| `2026-06-26 12:30:22` | `cowrie.command.input` |
| `2026-06-26 12:30:22` | `cowrie.command.input` |
| `2026-06-26 12:30:22` | `cowrie.command.input` |
| `2026-06-26 12:30:22` | `cowrie.command.input` |
| `2026-06-26 12:30:22` | `cowrie.log.closed` |
| `2026-06-26 12:30:23` | `cowrie.session.params` |
| `2026-06-26 12:30:23` | `cowrie.command.input` |
| `2026-06-26 12:30:23` | `cowrie.command.input` |
| `2026-06-26 12:30:23` | `cowrie.command.failed` |
| `2026-06-26 12:30:23` | `cowrie.command.failed` |
| `2026-06-26 12:30:23` | `cowrie.command.failed` |
| `2026-06-26 12:30:23` | `cowrie.command.failed` |
| `2026-06-26 12:30:23` | `cowrie.log.closed` |
| `2026-06-26 12:30:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28fc49a3cffc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:31 |
| **Last Seen** | 2026-06-26 12:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:31:11` | `cowrie.session.connect` |
| `2026-06-26 12:31:11` | `cowrie.client.version` |
| `2026-06-26 12:31:11` | `cowrie.client.kex` |
| `2026-06-26 12:31:11` | `cowrie.login.success` |
| `2026-06-26 12:31:12` | `cowrie.session.params` |
| `2026-06-26 12:31:12` | `cowrie.command.input` |
| `2026-06-26 12:31:12` | `cowrie.log.closed` |
| `2026-06-26 12:31:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a83253b59752

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 12:31 |
| **Last Seen** | 2026-06-26 12:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:31:33` | `cowrie.session.connect` |
| `2026-06-26 12:31:33` | `cowrie.client.version` |
| `2026-06-26 12:31:33` | `cowrie.client.kex` |
| `2026-06-26 12:31:35` | `cowrie.login.success` |
| `2026-06-26 12:31:37` | `cowrie.session.params` |
| `2026-06-26 12:31:37` | `cowrie.command.input` |
| `2026-06-26 12:31:38` | `cowrie.log.closed` |
| `2026-06-26 12:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df6a4387870b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:32 |
| **Last Seen** | 2026-06-26 12:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:32:04` | `cowrie.session.connect` |
| `2026-06-26 12:32:04` | `cowrie.client.version` |
| `2026-06-26 12:32:04` | `cowrie.client.kex` |
| `2026-06-26 12:32:04` | `cowrie.login.success` |
| `2026-06-26 12:32:05` | `cowrie.session.params` |
| `2026-06-26 12:32:05` | `cowrie.command.input` |
| `2026-06-26 12:32:05` | `cowrie.log.closed` |
| `2026-06-26 12:32:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b15686b347bd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-06-26 12:32 |
| **Last Seen** | 2026-06-26 12:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:32:12` | `cowrie.session.connect` |
| `2026-06-26 12:32:12` | `cowrie.client.version` |
| `2026-06-26 12:32:12` | `cowrie.client.kex` |
| `2026-06-26 12:32:14` | `cowrie.login.success` |
| `2026-06-26 12:32:15` | `cowrie.session.params` |
| `2026-06-26 12:32:15` | `cowrie.command.input` |
| `2026-06-26 12:32:15` | `cowrie.command.input` |
| `2026-06-26 12:32:15` | `cowrie.command.input` |
| `2026-06-26 12:32:15` | `cowrie.command.input` |
| `2026-06-26 12:32:15` | `cowrie.log.closed` |
| `2026-06-26 12:32:17` | `cowrie.session.params` |
| `2026-06-26 12:32:17` | `cowrie.command.input` |
| `2026-06-26 12:32:17` | `cowrie.command.input` |
| `2026-06-26 12:32:17` | `cowrie.command.failed` |
| `2026-06-26 12:32:17` | `cowrie.command.failed` |
| `2026-06-26 12:32:17` | `cowrie.command.failed` |
| `2026-06-26 12:32:17` | `cowrie.command.failed` |
| `2026-06-26 12:32:17` | `cowrie.log.closed` |
| `2026-06-26 12:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4df8abd5887

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:32 |
| **Last Seen** | 2026-06-26 12:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:32:56` | `cowrie.session.connect` |
| `2026-06-26 12:32:56` | `cowrie.client.version` |
| `2026-06-26 12:32:56` | `cowrie.client.kex` |
| `2026-06-26 12:32:57` | `cowrie.login.success` |
| `2026-06-26 12:32:58` | `cowrie.session.params` |
| `2026-06-26 12:32:58` | `cowrie.command.input` |
| `2026-06-26 12:32:58` | `cowrie.log.closed` |
| `2026-06-26 12:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a580cc6f7c1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:33 |
| **Last Seen** | 2026-06-26 12:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:33:50` | `cowrie.session.connect` |
| `2026-06-26 12:33:50` | `cowrie.client.version` |
| `2026-06-26 12:33:50` | `cowrie.client.kex` |
| `2026-06-26 12:33:50` | `cowrie.login.success` |
| `2026-06-26 12:33:51` | `cowrie.session.params` |
| `2026-06-26 12:33:51` | `cowrie.command.input` |
| `2026-06-26 12:33:51` | `cowrie.log.closed` |
| `2026-06-26 12:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceb0dde485d3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-06-26 12:34 |
| **Last Seen** | 2026-06-26 12:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password1' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:34:00` | `cowrie.session.connect` |
| `2026-06-26 12:34:01` | `cowrie.client.version` |
| `2026-06-26 12:34:01` | `cowrie.client.kex` |
| `2026-06-26 12:34:02` | `cowrie.login.success` |
| `2026-06-26 12:34:04` | `cowrie.session.params` |
| `2026-06-26 12:34:04` | `cowrie.command.input` |
| `2026-06-26 12:34:04` | `cowrie.command.input` |
| `2026-06-26 12:34:04` | `cowrie.command.input` |
| `2026-06-26 12:34:04` | `cowrie.command.input` |
| `2026-06-26 12:34:04` | `cowrie.log.closed` |
| `2026-06-26 12:34:05` | `cowrie.session.params` |
| `2026-06-26 12:34:05` | `cowrie.command.input` |
| `2026-06-26 12:34:05` | `cowrie.command.input` |
| `2026-06-26 12:34:05` | `cowrie.command.failed` |
| `2026-06-26 12:34:05` | `cowrie.command.failed` |
| `2026-06-26 12:34:05` | `cowrie.command.failed` |
| `2026-06-26 12:34:05` | `cowrie.command.failed` |
| `2026-06-26 12:34:06` | `cowrie.log.closed` |
| `2026-06-26 12:34:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddcfa9afe03b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:34 |
| **Last Seen** | 2026-06-26 12:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:34:47` | `cowrie.session.connect` |
| `2026-06-26 12:34:47` | `cowrie.client.version` |
| `2026-06-26 12:34:47` | `cowrie.client.kex` |
| `2026-06-26 12:34:47` | `cowrie.login.success` |
| `2026-06-26 12:34:48` | `cowrie.session.params` |
| `2026-06-26 12:34:48` | `cowrie.command.input` |
| `2026-06-26 12:34:48` | `cowrie.log.closed` |
| `2026-06-26 12:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31418c42683e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:35 |
| **Last Seen** | 2026-06-26 12:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:35:41` | `cowrie.session.connect` |
| `2026-06-26 12:35:41` | `cowrie.client.version` |
| `2026-06-26 12:35:42` | `cowrie.client.kex` |
| `2026-06-26 12:35:42` | `cowrie.login.success` |
| `2026-06-26 12:35:43` | `cowrie.session.params` |
| `2026-06-26 12:35:43` | `cowrie.command.input` |
| `2026-06-26 12:35:43` | `cowrie.log.closed` |
| `2026-06-26 12:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-552652e08578

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-06-26 12:35 |
| **Last Seen** | 2026-06-26 12:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'qwerty' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:35:45` | `cowrie.session.connect` |
| `2026-06-26 12:35:45` | `cowrie.client.version` |
| `2026-06-26 12:35:45` | `cowrie.client.kex` |
| `2026-06-26 12:35:46` | `cowrie.login.success` |
| `2026-06-26 12:35:48` | `cowrie.session.params` |
| `2026-06-26 12:35:48` | `cowrie.command.input` |
| `2026-06-26 12:35:48` | `cowrie.command.input` |
| `2026-06-26 12:35:48` | `cowrie.command.input` |
| `2026-06-26 12:35:48` | `cowrie.command.input` |
| `2026-06-26 12:35:48` | `cowrie.log.closed` |
| `2026-06-26 12:35:49` | `cowrie.session.params` |
| `2026-06-26 12:35:49` | `cowrie.command.input` |
| `2026-06-26 12:35:49` | `cowrie.command.input` |
| `2026-06-26 12:35:49` | `cowrie.command.failed` |
| `2026-06-26 12:35:49` | `cowrie.command.failed` |
| `2026-06-26 12:35:49` | `cowrie.command.failed` |
| `2026-06-26 12:35:49` | `cowrie.command.failed` |
| `2026-06-26 12:35:49` | `cowrie.log.closed` |
| `2026-06-26 12:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a26ad9fd99b7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:36 |
| **Last Seen** | 2026-06-26 12:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:36:36` | `cowrie.session.connect` |
| `2026-06-26 12:36:36` | `cowrie.client.version` |
| `2026-06-26 12:36:36` | `cowrie.client.kex` |
| `2026-06-26 12:36:37` | `cowrie.login.success` |
| `2026-06-26 12:36:38` | `cowrie.session.params` |
| `2026-06-26 12:36:38` | `cowrie.command.input` |
| `2026-06-26 12:36:38` | `cowrie.log.closed` |
| `2026-06-26 12:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf1d8b66bcb9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:37 |
| **Last Seen** | 2026-06-26 12:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:37:33` | `cowrie.session.connect` |
| `2026-06-26 12:37:33` | `cowrie.client.version` |
| `2026-06-26 12:37:33` | `cowrie.client.kex` |
| `2026-06-26 12:37:34` | `cowrie.login.success` |
| `2026-06-26 12:37:34` | `cowrie.session.params` |
| `2026-06-26 12:37:34` | `cowrie.command.input` |
| `2026-06-26 12:37:34` | `cowrie.log.closed` |
| `2026-06-26 12:37:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1299146cb00

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:38 |
| **Last Seen** | 2026-06-26 12:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:38:30` | `cowrie.session.connect` |
| `2026-06-26 12:38:30` | `cowrie.client.version` |
| `2026-06-26 12:38:30` | `cowrie.client.kex` |
| `2026-06-26 12:38:31` | `cowrie.login.success` |
| `2026-06-26 12:38:32` | `cowrie.session.params` |
| `2026-06-26 12:38:32` | `cowrie.command.input` |
| `2026-06-26 12:38:32` | `cowrie.log.closed` |
| `2026-06-26 12:38:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7d8cae4cecb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:39 |
| **Last Seen** | 2026-06-26 12:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:39:28` | `cowrie.session.connect` |
| `2026-06-26 12:39:28` | `cowrie.client.version` |
| `2026-06-26 12:39:28` | `cowrie.client.kex` |
| `2026-06-26 12:39:29` | `cowrie.login.success` |
| `2026-06-26 12:39:30` | `cowrie.session.params` |
| `2026-06-26 12:39:30` | `cowrie.command.input` |
| `2026-06-26 12:39:30` | `cowrie.log.closed` |
| `2026-06-26 12:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65782c7c7fd0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-06-26 12:40 |
| **Last Seen** | 2026-06-26 12:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:40:00` | `cowrie.session.connect` |
| `2026-06-26 12:40:00` | `cowrie.client.version` |
| `2026-06-26 12:40:00` | `cowrie.client.kex` |
| `2026-06-26 12:40:00` | `cowrie.login.success` |
| `2026-06-26 12:40:01` | `cowrie.session.params` |
| `2026-06-26 12:40:01` | `cowrie.command.input` |
| `2026-06-26 12:40:01` | `cowrie.log.closed` |
| `2026-06-26 12:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d667b4fb8dd7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:40 |
| **Last Seen** | 2026-06-26 12:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:40:27` | `cowrie.session.connect` |
| `2026-06-26 12:40:27` | `cowrie.client.version` |
| `2026-06-26 12:40:27` | `cowrie.client.kex` |
| `2026-06-26 12:40:27` | `cowrie.login.success` |
| `2026-06-26 12:40:28` | `cowrie.session.params` |
| `2026-06-26 12:40:28` | `cowrie.command.input` |
| `2026-06-26 12:40:28` | `cowrie.log.closed` |
| `2026-06-26 12:40:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee9394010fa1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 12:40 |
| **Last Seen** | 2026-06-26 12:40 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:40:38` | `cowrie.session.connect` |
| `2026-06-26 12:40:40` | `cowrie.client.version` |
| `2026-06-26 12:40:40` | `cowrie.client.kex` |
| `2026-06-26 12:40:46` | `cowrie.login.success` |
| `2026-06-26 12:40:49` | `cowrie.session.params` |
| `2026-06-26 12:40:49` | `cowrie.command.input` |
| `2026-06-26 12:40:50` | `cowrie.log.closed` |
| `2026-06-26 12:40:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c56be47ad01c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:41 |
| **Last Seen** | 2026-06-26 12:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:41:23` | `cowrie.session.connect` |
| `2026-06-26 12:41:23` | `cowrie.client.version` |
| `2026-06-26 12:41:23` | `cowrie.client.kex` |
| `2026-06-26 12:41:24` | `cowrie.login.success` |
| `2026-06-26 12:41:25` | `cowrie.session.params` |
| `2026-06-26 12:41:25` | `cowrie.command.input` |
| `2026-06-26 12:41:25` | `cowrie.log.closed` |
| `2026-06-26 12:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f495a6f2ef4c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:42 |
| **Last Seen** | 2026-06-26 12:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:42:21` | `cowrie.session.connect` |
| `2026-06-26 12:42:21` | `cowrie.client.version` |
| `2026-06-26 12:42:21` | `cowrie.client.kex` |
| `2026-06-26 12:42:21` | `cowrie.login.success` |
| `2026-06-26 12:42:22` | `cowrie.session.params` |
| `2026-06-26 12:42:22` | `cowrie.command.input` |
| `2026-06-26 12:42:22` | `cowrie.log.closed` |
| `2026-06-26 12:42:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5d89553c56c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:43 |
| **Last Seen** | 2026-06-26 12:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:43:24` | `cowrie.session.connect` |
| `2026-06-26 12:43:24` | `cowrie.client.version` |
| `2026-06-26 12:43:24` | `cowrie.client.kex` |
| `2026-06-26 12:43:25` | `cowrie.login.success` |
| `2026-06-26 12:43:25` | `cowrie.session.params` |
| `2026-06-26 12:43:25` | `cowrie.command.input` |
| `2026-06-26 12:43:26` | `cowrie.log.closed` |
| `2026-06-26 12:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dccac61f6ce6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:44 |
| **Last Seen** | 2026-06-26 12:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:44:27` | `cowrie.session.connect` |
| `2026-06-26 12:44:27` | `cowrie.client.version` |
| `2026-06-26 12:44:28` | `cowrie.client.kex` |
| `2026-06-26 12:44:28` | `cowrie.login.success` |
| `2026-06-26 12:44:29` | `cowrie.session.params` |
| `2026-06-26 12:44:29` | `cowrie.command.input` |
| `2026-06-26 12:44:29` | `cowrie.log.closed` |
| `2026-06-26 12:44:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c3902d94719

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:45 |
| **Last Seen** | 2026-06-26 12:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:45:25` | `cowrie.session.connect` |
| `2026-06-26 12:45:25` | `cowrie.client.version` |
| `2026-06-26 12:45:26` | `cowrie.client.kex` |
| `2026-06-26 12:45:26` | `cowrie.login.success` |
| `2026-06-26 12:45:27` | `cowrie.session.params` |
| `2026-06-26 12:45:27` | `cowrie.command.input` |
| `2026-06-26 12:45:27` | `cowrie.log.closed` |
| `2026-06-26 12:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c63c1e34d962

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 12:46 |
| **Last Seen** | 2026-06-26 12:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:46:11` | `cowrie.session.connect` |
| `2026-06-26 12:46:11` | `cowrie.client.version` |
| `2026-06-26 12:46:11` | `cowrie.client.kex` |
| `2026-06-26 12:46:14` | `cowrie.login.success` |
| `2026-06-26 12:46:15` | `cowrie.session.params` |
| `2026-06-26 12:46:15` | `cowrie.command.input` |
| `2026-06-26 12:46:16` | `cowrie.log.closed` |
| `2026-06-26 12:46:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a28673be5d8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:46 |
| **Last Seen** | 2026-06-26 12:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:46:22` | `cowrie.session.connect` |
| `2026-06-26 12:46:22` | `cowrie.client.version` |
| `2026-06-26 12:46:22` | `cowrie.client.kex` |
| `2026-06-26 12:46:22` | `cowrie.login.success` |
| `2026-06-26 12:46:23` | `cowrie.session.params` |
| `2026-06-26 12:46:23` | `cowrie.command.input` |
| `2026-06-26 12:46:23` | `cowrie.log.closed` |
| `2026-06-26 12:46:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7041fc7bf467

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:47 |
| **Last Seen** | 2026-06-26 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:47:19` | `cowrie.session.connect` |
| `2026-06-26 12:47:19` | `cowrie.client.version` |
| `2026-06-26 12:47:19` | `cowrie.client.kex` |
| `2026-06-26 12:47:19` | `cowrie.login.success` |
| `2026-06-26 12:47:20` | `cowrie.session.params` |
| `2026-06-26 12:47:20` | `cowrie.command.input` |
| `2026-06-26 12:47:20` | `cowrie.log.closed` |
| `2026-06-26 12:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfbdc4b13385

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:48 |
| **Last Seen** | 2026-06-26 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:48:17` | `cowrie.session.connect` |
| `2026-06-26 12:48:17` | `cowrie.client.version` |
| `2026-06-26 12:48:17` | `cowrie.client.kex` |
| `2026-06-26 12:48:18` | `cowrie.login.success` |
| `2026-06-26 12:48:19` | `cowrie.session.params` |
| `2026-06-26 12:48:19` | `cowrie.command.input` |
| `2026-06-26 12:48:19` | `cowrie.log.closed` |
| `2026-06-26 12:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7701e987b0c0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:49 |
| **Last Seen** | 2026-06-26 12:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:49:22` | `cowrie.session.connect` |
| `2026-06-26 12:49:22` | `cowrie.client.version` |
| `2026-06-26 12:49:22` | `cowrie.client.kex` |
| `2026-06-26 12:49:23` | `cowrie.login.success` |
| `2026-06-26 12:49:24` | `cowrie.session.params` |
| `2026-06-26 12:49:24` | `cowrie.command.input` |
| `2026-06-26 12:49:24` | `cowrie.log.closed` |
| `2026-06-26 12:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab9c17c1470c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:50 |
| **Last Seen** | 2026-06-26 12:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:50:30` | `cowrie.session.connect` |
| `2026-06-26 12:50:30` | `cowrie.client.version` |
| `2026-06-26 12:50:31` | `cowrie.client.kex` |
| `2026-06-26 12:50:31` | `cowrie.login.success` |
| `2026-06-26 12:50:32` | `cowrie.session.params` |
| `2026-06-26 12:50:32` | `cowrie.command.input` |
| `2026-06-26 12:50:32` | `cowrie.log.closed` |
| `2026-06-26 12:50:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07a33b4c4a16

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:51 |
| **Last Seen** | 2026-06-26 12:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:51:44` | `cowrie.session.connect` |
| `2026-06-26 12:51:44` | `cowrie.client.version` |
| `2026-06-26 12:51:44` | `cowrie.client.kex` |
| `2026-06-26 12:51:46` | `cowrie.login.success` |
| `2026-06-26 12:51:48` | `cowrie.session.params` |
| `2026-06-26 12:51:48` | `cowrie.command.input` |
| `2026-06-26 12:51:48` | `cowrie.log.closed` |
| `2026-06-26 12:51:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b40c1ea96fcb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 12:52 |
| **Last Seen** | 2026-06-26 12:52 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:52:02` | `cowrie.session.connect` |
| `2026-06-26 12:52:04` | `cowrie.client.version` |
| `2026-06-26 12:52:04` | `cowrie.client.kex` |
| `2026-06-26 12:52:10` | `cowrie.login.success` |
| `2026-06-26 12:52:13` | `cowrie.session.params` |
| `2026-06-26 12:52:13` | `cowrie.command.input` |
| `2026-06-26 12:52:16` | `cowrie.log.closed` |
| `2026-06-26 12:52:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0c6aa6e03a4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:52 |
| **Last Seen** | 2026-06-26 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:52:47` | `cowrie.session.connect` |
| `2026-06-26 12:52:47` | `cowrie.client.version` |
| `2026-06-26 12:52:47` | `cowrie.client.kex` |
| `2026-06-26 12:52:47` | `cowrie.login.success` |
| `2026-06-26 12:52:48` | `cowrie.session.params` |
| `2026-06-26 12:52:48` | `cowrie.command.input` |
| `2026-06-26 12:52:48` | `cowrie.log.closed` |
| `2026-06-26 12:52:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6edf0b83d094

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:53 |
| **Last Seen** | 2026-06-26 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:53:44` | `cowrie.session.connect` |
| `2026-06-26 12:53:44` | `cowrie.client.version` |
| `2026-06-26 12:53:44` | `cowrie.client.kex` |
| `2026-06-26 12:53:44` | `cowrie.login.success` |
| `2026-06-26 12:53:45` | `cowrie.session.params` |
| `2026-06-26 12:53:45` | `cowrie.command.input` |
| `2026-06-26 12:53:45` | `cowrie.log.closed` |
| `2026-06-26 12:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aae870baf7e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:54 |
| **Last Seen** | 2026-06-26 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:54:42` | `cowrie.session.connect` |
| `2026-06-26 12:54:42` | `cowrie.client.version` |
| `2026-06-26 12:54:42` | `cowrie.client.kex` |
| `2026-06-26 12:54:42` | `cowrie.login.success` |
| `2026-06-26 12:54:43` | `cowrie.session.params` |
| `2026-06-26 12:54:43` | `cowrie.command.input` |
| `2026-06-26 12:54:43` | `cowrie.log.closed` |
| `2026-06-26 12:54:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50e69dd3b64d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:55 |
| **Last Seen** | 2026-06-26 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:55:43` | `cowrie.session.connect` |
| `2026-06-26 12:55:43` | `cowrie.client.version` |
| `2026-06-26 12:55:43` | `cowrie.client.kex` |
| `2026-06-26 12:55:43` | `cowrie.login.success` |
| `2026-06-26 12:55:44` | `cowrie.session.params` |
| `2026-06-26 12:55:44` | `cowrie.command.input` |
| `2026-06-26 12:55:44` | `cowrie.log.closed` |
| `2026-06-26 12:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a690a4bfa9ad

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:56 |
| **Last Seen** | 2026-06-26 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:56:43` | `cowrie.session.connect` |
| `2026-06-26 12:56:43` | `cowrie.client.version` |
| `2026-06-26 12:56:43` | `cowrie.client.kex` |
| `2026-06-26 12:56:43` | `cowrie.login.success` |
| `2026-06-26 12:56:44` | `cowrie.session.params` |
| `2026-06-26 12:56:44` | `cowrie.command.input` |
| `2026-06-26 12:56:44` | `cowrie.log.closed` |
| `2026-06-26 12:56:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a2016dc3451

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:57 |
| **Last Seen** | 2026-06-26 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:57:42` | `cowrie.session.connect` |
| `2026-06-26 12:57:42` | `cowrie.client.version` |
| `2026-06-26 12:57:42` | `cowrie.client.kex` |
| `2026-06-26 12:57:42` | `cowrie.login.success` |
| `2026-06-26 12:57:43` | `cowrie.session.params` |
| `2026-06-26 12:57:43` | `cowrie.command.input` |
| `2026-06-26 12:57:43` | `cowrie.log.closed` |
| `2026-06-26 12:57:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d7ff3cb69f5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:58 |
| **Last Seen** | 2026-06-26 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:58:37` | `cowrie.session.connect` |
| `2026-06-26 12:58:37` | `cowrie.client.version` |
| `2026-06-26 12:58:37` | `cowrie.client.kex` |
| `2026-06-26 12:58:38` | `cowrie.login.success` |
| `2026-06-26 12:58:39` | `cowrie.session.params` |
| `2026-06-26 12:58:39` | `cowrie.command.input` |
| `2026-06-26 12:58:39` | `cowrie.log.closed` |
| `2026-06-26 12:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b54e3766846

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 12:59 |
| **Last Seen** | 2026-06-26 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 12:59:34` | `cowrie.session.connect` |
| `2026-06-26 12:59:34` | `cowrie.client.version` |
| `2026-06-26 12:59:34` | `cowrie.client.kex` |
| `2026-06-26 12:59:35` | `cowrie.login.success` |
| `2026-06-26 12:59:35` | `cowrie.session.params` |
| `2026-06-26 12:59:35` | `cowrie.command.input` |
| `2026-06-26 12:59:35` | `cowrie.log.closed` |
| `2026-06-26 12:59:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86ec6800b8d4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:00 |
| **Last Seen** | 2026-06-26 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:00:32` | `cowrie.session.connect` |
| `2026-06-26 13:00:32` | `cowrie.client.version` |
| `2026-06-26 13:00:32` | `cowrie.client.kex` |
| `2026-06-26 13:00:33` | `cowrie.login.success` |
| `2026-06-26 13:00:33` | `cowrie.session.params` |
| `2026-06-26 13:00:33` | `cowrie.command.input` |
| `2026-06-26 13:00:34` | `cowrie.log.closed` |
| `2026-06-26 13:00:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df4bb6574930

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 13:00 |
| **Last Seen** | 2026-06-26 13:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:00:41` | `cowrie.session.connect` |
| `2026-06-26 13:00:41` | `cowrie.client.version` |
| `2026-06-26 13:00:41` | `cowrie.client.kex` |
| `2026-06-26 13:00:43` | `cowrie.login.success` |
| `2026-06-26 13:00:45` | `cowrie.session.params` |
| `2026-06-26 13:00:45` | `cowrie.command.input` |
| `2026-06-26 13:00:45` | `cowrie.log.closed` |
| `2026-06-26 13:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53b6cf02dcc4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:01 |
| **Last Seen** | 2026-06-26 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:01:34` | `cowrie.session.connect` |
| `2026-06-26 13:01:34` | `cowrie.client.version` |
| `2026-06-26 13:01:34` | `cowrie.client.kex` |
| `2026-06-26 13:01:34` | `cowrie.login.success` |
| `2026-06-26 13:01:35` | `cowrie.session.params` |
| `2026-06-26 13:01:35` | `cowrie.command.input` |
| `2026-06-26 13:01:35` | `cowrie.log.closed` |
| `2026-06-26 13:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e43b76274a3b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:02 |
| **Last Seen** | 2026-06-26 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:02:36` | `cowrie.session.connect` |
| `2026-06-26 13:02:36` | `cowrie.client.version` |
| `2026-06-26 13:02:37` | `cowrie.client.kex` |
| `2026-06-26 13:02:37` | `cowrie.login.success` |
| `2026-06-26 13:02:38` | `cowrie.session.params` |
| `2026-06-26 13:02:38` | `cowrie.command.input` |
| `2026-06-26 13:02:38` | `cowrie.log.closed` |
| `2026-06-26 13:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c97c8ba42e9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:03 |
| **Last Seen** | 2026-06-26 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:03:41` | `cowrie.session.connect` |
| `2026-06-26 13:03:41` | `cowrie.client.version` |
| `2026-06-26 13:03:42` | `cowrie.client.kex` |
| `2026-06-26 13:03:42` | `cowrie.login.success` |
| `2026-06-26 13:03:43` | `cowrie.session.params` |
| `2026-06-26 13:03:43` | `cowrie.command.input` |
| `2026-06-26 13:03:43` | `cowrie.log.closed` |
| `2026-06-26 13:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17796fe98da9

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 13:03 |
| **Last Seen** | 2026-06-26 13:03 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:03:44` | `cowrie.session.connect` |
| `2026-06-26 13:03:45` | `cowrie.client.version` |
| `2026-06-26 13:03:45` | `cowrie.client.kex` |
| `2026-06-26 13:03:52` | `cowrie.login.success` |
| `2026-06-26 13:03:56` | `cowrie.session.params` |
| `2026-06-26 13:03:56` | `cowrie.command.input` |
| `2026-06-26 13:03:58` | `cowrie.log.closed` |
| `2026-06-26 13:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38458f2adbe2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:04 |
| **Last Seen** | 2026-06-26 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:04:45` | `cowrie.session.connect` |
| `2026-06-26 13:04:45` | `cowrie.client.version` |
| `2026-06-26 13:04:45` | `cowrie.client.kex` |
| `2026-06-26 13:04:45` | `cowrie.login.success` |
| `2026-06-26 13:04:46` | `cowrie.session.params` |
| `2026-06-26 13:04:46` | `cowrie.command.input` |
| `2026-06-26 13:04:46` | `cowrie.log.closed` |
| `2026-06-26 13:04:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2d75783f4e5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:05 |
| **Last Seen** | 2026-06-26 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:05:47` | `cowrie.session.connect` |
| `2026-06-26 13:05:47` | `cowrie.client.version` |
| `2026-06-26 13:05:48` | `cowrie.client.kex` |
| `2026-06-26 13:05:48` | `cowrie.login.success` |
| `2026-06-26 13:05:49` | `cowrie.session.params` |
| `2026-06-26 13:05:49` | `cowrie.command.input` |
| `2026-06-26 13:05:49` | `cowrie.log.closed` |
| `2026-06-26 13:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af7c4a80e407

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:06 |
| **Last Seen** | 2026-06-26 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:06:53` | `cowrie.session.connect` |
| `2026-06-26 13:06:53` | `cowrie.client.version` |
| `2026-06-26 13:06:53` | `cowrie.client.kex` |
| `2026-06-26 13:06:53` | `cowrie.login.success` |
| `2026-06-26 13:06:54` | `cowrie.session.params` |
| `2026-06-26 13:06:54` | `cowrie.command.input` |
| `2026-06-26 13:06:54` | `cowrie.log.closed` |
| `2026-06-26 13:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f737ccd9b5c5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:07 |
| **Last Seen** | 2026-06-26 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:07:55` | `cowrie.session.connect` |
| `2026-06-26 13:07:55` | `cowrie.client.version` |
| `2026-06-26 13:07:55` | `cowrie.client.kex` |
| `2026-06-26 13:07:55` | `cowrie.login.success` |
| `2026-06-26 13:07:56` | `cowrie.session.params` |
| `2026-06-26 13:07:56` | `cowrie.command.input` |
| `2026-06-26 13:07:56` | `cowrie.log.closed` |
| `2026-06-26 13:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a09d4c6141a3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:08 |
| **Last Seen** | 2026-06-26 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:08:56` | `cowrie.session.connect` |
| `2026-06-26 13:08:56` | `cowrie.client.version` |
| `2026-06-26 13:08:56` | `cowrie.client.kex` |
| `2026-06-26 13:08:57` | `cowrie.login.success` |
| `2026-06-26 13:08:57` | `cowrie.session.params` |
| `2026-06-26 13:08:57` | `cowrie.command.input` |
| `2026-06-26 13:08:57` | `cowrie.log.closed` |
| `2026-06-26 13:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce719daa3285

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:09 |
| **Last Seen** | 2026-06-26 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:09:57` | `cowrie.session.connect` |
| `2026-06-26 13:09:57` | `cowrie.client.version` |
| `2026-06-26 13:09:57` | `cowrie.client.kex` |
| `2026-06-26 13:09:58` | `cowrie.login.success` |
| `2026-06-26 13:09:58` | `cowrie.session.params` |
| `2026-06-26 13:09:58` | `cowrie.command.input` |
| `2026-06-26 13:09:58` | `cowrie.log.closed` |
| `2026-06-26 13:09:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d929450c797

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:11 |
| **Last Seen** | 2026-06-26 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:11:00` | `cowrie.session.connect` |
| `2026-06-26 13:11:00` | `cowrie.client.version` |
| `2026-06-26 13:11:00` | `cowrie.client.kex` |
| `2026-06-26 13:11:00` | `cowrie.login.success` |
| `2026-06-26 13:11:01` | `cowrie.session.params` |
| `2026-06-26 13:11:01` | `cowrie.command.input` |
| `2026-06-26 13:11:01` | `cowrie.log.closed` |
| `2026-06-26 13:11:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ab11941e082

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:11 |
| **Last Seen** | 2026-06-26 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:11:59` | `cowrie.session.connect` |
| `2026-06-26 13:11:59` | `cowrie.client.version` |
| `2026-06-26 13:11:59` | `cowrie.client.kex` |
| `2026-06-26 13:11:59` | `cowrie.login.success` |
| `2026-06-26 13:12:00` | `cowrie.session.params` |
| `2026-06-26 13:12:00` | `cowrie.command.input` |
| `2026-06-26 13:12:00` | `cowrie.log.closed` |
| `2026-06-26 13:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19d61cc15f58

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:12 |
| **Last Seen** | 2026-06-26 13:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:12:58` | `cowrie.session.connect` |
| `2026-06-26 13:12:58` | `cowrie.client.version` |
| `2026-06-26 13:12:59` | `cowrie.client.kex` |
| `2026-06-26 13:12:59` | `cowrie.login.success` |
| `2026-06-26 13:13:00` | `cowrie.session.params` |
| `2026-06-26 13:13:00` | `cowrie.command.input` |
| `2026-06-26 13:13:00` | `cowrie.log.closed` |
| `2026-06-26 13:13:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81f30076019c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:14 |
| **Last Seen** | 2026-06-26 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:14:07` | `cowrie.session.connect` |
| `2026-06-26 13:14:07` | `cowrie.client.version` |
| `2026-06-26 13:14:07` | `cowrie.client.kex` |
| `2026-06-26 13:14:07` | `cowrie.login.success` |
| `2026-06-26 13:14:08` | `cowrie.session.params` |
| `2026-06-26 13:14:08` | `cowrie.command.input` |
| `2026-06-26 13:14:08` | `cowrie.log.closed` |
| `2026-06-26 13:14:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40c19e5ee34c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:15 |
| **Last Seen** | 2026-06-26 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:15:09` | `cowrie.session.connect` |
| `2026-06-26 13:15:09` | `cowrie.client.version` |
| `2026-06-26 13:15:09` | `cowrie.client.kex` |
| `2026-06-26 13:15:10` | `cowrie.login.success` |
| `2026-06-26 13:15:10` | `cowrie.session.params` |
| `2026-06-26 13:15:10` | `cowrie.command.input` |
| `2026-06-26 13:15:11` | `cowrie.log.closed` |
| `2026-06-26 13:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cdae0589bc0

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 13:15 |
| **Last Seen** | 2026-06-26 13:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:15:14` | `cowrie.session.connect` |
| `2026-06-26 13:15:14` | `cowrie.client.version` |
| `2026-06-26 13:15:14` | `cowrie.client.kex` |
| `2026-06-26 13:15:16` | `cowrie.login.success` |
| `2026-06-26 13:15:17` | `cowrie.session.params` |
| `2026-06-26 13:15:17` | `cowrie.command.input` |
| `2026-06-26 13:15:18` | `cowrie.log.closed` |
| `2026-06-26 13:15:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4c88aeb932a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 13:15 |
| **Last Seen** | 2026-06-26 13:16 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:15:57` | `cowrie.session.connect` |
| `2026-06-26 13:15:59` | `cowrie.client.version` |
| `2026-06-26 13:15:59` | `cowrie.client.kex` |
| `2026-06-26 13:16:05` | `cowrie.login.success` |
| `2026-06-26 13:16:08` | `cowrie.session.params` |
| `2026-06-26 13:16:08` | `cowrie.command.input` |
| `2026-06-26 13:16:10` | `cowrie.log.closed` |
| `2026-06-26 13:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43061c2399a4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:16 |
| **Last Seen** | 2026-06-26 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:16:14` | `cowrie.session.connect` |
| `2026-06-26 13:16:14` | `cowrie.client.version` |
| `2026-06-26 13:16:15` | `cowrie.client.kex` |
| `2026-06-26 13:16:15` | `cowrie.login.success` |
| `2026-06-26 13:16:16` | `cowrie.session.params` |
| `2026-06-26 13:16:16` | `cowrie.command.input` |
| `2026-06-26 13:16:16` | `cowrie.log.closed` |
| `2026-06-26 13:16:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef530b107bc1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:17 |
| **Last Seen** | 2026-06-26 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:17:20` | `cowrie.session.connect` |
| `2026-06-26 13:17:20` | `cowrie.client.version` |
| `2026-06-26 13:17:20` | `cowrie.client.kex` |
| `2026-06-26 13:17:20` | `cowrie.login.success` |
| `2026-06-26 13:17:21` | `cowrie.session.params` |
| `2026-06-26 13:17:21` | `cowrie.command.input` |
| `2026-06-26 13:17:21` | `cowrie.log.closed` |
| `2026-06-26 13:17:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8a125cd0bb9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:18 |
| **Last Seen** | 2026-06-26 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:18:24` | `cowrie.session.connect` |
| `2026-06-26 13:18:24` | `cowrie.client.version` |
| `2026-06-26 13:18:24` | `cowrie.client.kex` |
| `2026-06-26 13:18:24` | `cowrie.login.success` |
| `2026-06-26 13:18:25` | `cowrie.session.params` |
| `2026-06-26 13:18:25` | `cowrie.command.input` |
| `2026-06-26 13:18:25` | `cowrie.log.closed` |
| `2026-06-26 13:18:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f4084169f87

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:19 |
| **Last Seen** | 2026-06-26 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:19:29` | `cowrie.session.connect` |
| `2026-06-26 13:19:29` | `cowrie.client.version` |
| `2026-06-26 13:19:29` | `cowrie.client.kex` |
| `2026-06-26 13:19:30` | `cowrie.login.success` |
| `2026-06-26 13:19:31` | `cowrie.session.params` |
| `2026-06-26 13:19:31` | `cowrie.command.input` |
| `2026-06-26 13:19:31` | `cowrie.log.closed` |
| `2026-06-26 13:19:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d2e7d8ebfe8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:20 |
| **Last Seen** | 2026-06-26 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:20:40` | `cowrie.session.connect` |
| `2026-06-26 13:20:40` | `cowrie.client.version` |
| `2026-06-26 13:20:40` | `cowrie.client.kex` |
| `2026-06-26 13:20:40` | `cowrie.login.success` |
| `2026-06-26 13:20:41` | `cowrie.session.params` |
| `2026-06-26 13:20:41` | `cowrie.command.input` |
| `2026-06-26 13:20:41` | `cowrie.log.closed` |
| `2026-06-26 13:20:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b004b5d48c07

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:21 |
| **Last Seen** | 2026-06-26 13:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:21:47` | `cowrie.session.connect` |
| `2026-06-26 13:21:47` | `cowrie.client.version` |
| `2026-06-26 13:21:47` | `cowrie.client.kex` |
| `2026-06-26 13:21:47` | `cowrie.login.success` |
| `2026-06-26 13:21:48` | `cowrie.session.params` |
| `2026-06-26 13:21:48` | `cowrie.command.input` |
| `2026-06-26 13:21:48` | `cowrie.log.closed` |
| `2026-06-26 13:21:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-373b5788c2a1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:22 |
| **Last Seen** | 2026-06-26 13:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:22:52` | `cowrie.session.connect` |
| `2026-06-26 13:22:52` | `cowrie.client.version` |
| `2026-06-26 13:22:52` | `cowrie.client.kex` |
| `2026-06-26 13:22:52` | `cowrie.login.success` |
| `2026-06-26 13:22:53` | `cowrie.session.params` |
| `2026-06-26 13:22:53` | `cowrie.command.input` |
| `2026-06-26 13:22:53` | `cowrie.log.closed` |
| `2026-06-26 13:22:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb3ca6aca1b8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:24 |
| **Last Seen** | 2026-06-26 13:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:24:01` | `cowrie.session.connect` |
| `2026-06-26 13:24:01` | `cowrie.client.version` |
| `2026-06-26 13:24:01` | `cowrie.client.kex` |
| `2026-06-26 13:24:01` | `cowrie.login.success` |
| `2026-06-26 13:24:02` | `cowrie.session.params` |
| `2026-06-26 13:24:02` | `cowrie.command.input` |
| `2026-06-26 13:24:02` | `cowrie.log.closed` |
| `2026-06-26 13:24:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41adcd5f175b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:25 |
| **Last Seen** | 2026-06-26 13:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:25:14` | `cowrie.session.connect` |
| `2026-06-26 13:25:14` | `cowrie.client.version` |
| `2026-06-26 13:25:14` | `cowrie.client.kex` |
| `2026-06-26 13:25:14` | `cowrie.login.success` |
| `2026-06-26 13:25:15` | `cowrie.session.params` |
| `2026-06-26 13:25:15` | `cowrie.command.input` |
| `2026-06-26 13:25:15` | `cowrie.log.closed` |
| `2026-06-26 13:25:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bb9c22b4a93

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:26 |
| **Last Seen** | 2026-06-26 13:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:26:19` | `cowrie.session.connect` |
| `2026-06-26 13:26:19` | `cowrie.client.version` |
| `2026-06-26 13:26:19` | `cowrie.client.kex` |
| `2026-06-26 13:26:19` | `cowrie.login.success` |
| `2026-06-26 13:26:20` | `cowrie.session.params` |
| `2026-06-26 13:26:20` | `cowrie.command.input` |
| `2026-06-26 13:26:20` | `cowrie.log.closed` |
| `2026-06-26 13:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b70a6fe11de

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 13:27 |
| **Last Seen** | 2026-06-26 13:27 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:27:18` | `cowrie.session.connect` |
| `2026-06-26 13:27:19` | `cowrie.client.version` |
| `2026-06-26 13:27:19` | `cowrie.client.kex` |
| `2026-06-26 13:27:24` | `cowrie.login.success` |
| `2026-06-26 13:27:27` | `cowrie.session.params` |
| `2026-06-26 13:27:27` | `cowrie.command.input` |
| `2026-06-26 13:27:29` | `cowrie.log.closed` |
| `2026-06-26 13:27:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43662052c414

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:27 |
| **Last Seen** | 2026-06-26 13:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:27:23` | `cowrie.session.connect` |
| `2026-06-26 13:27:23` | `cowrie.client.version` |
| `2026-06-26 13:27:23` | `cowrie.client.kex` |
| `2026-06-26 13:27:24` | `cowrie.login.success` |
| `2026-06-26 13:27:24` | `cowrie.session.params` |
| `2026-06-26 13:27:24` | `cowrie.command.input` |
| `2026-06-26 13:27:25` | `cowrie.log.closed` |
| `2026-06-26 13:27:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00fade5b470c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:28 |
| **Last Seen** | 2026-06-26 13:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:28:26` | `cowrie.session.connect` |
| `2026-06-26 13:28:26` | `cowrie.client.version` |
| `2026-06-26 13:28:26` | `cowrie.client.kex` |
| `2026-06-26 13:28:26` | `cowrie.login.success` |
| `2026-06-26 13:28:27` | `cowrie.session.params` |
| `2026-06-26 13:28:27` | `cowrie.command.input` |
| `2026-06-26 13:28:27` | `cowrie.log.closed` |
| `2026-06-26 13:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ce8f1e90aae

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 13:29 |
| **Last Seen** | 2026-06-26 13:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:29:26` | `cowrie.session.connect` |
| `2026-06-26 13:29:26` | `cowrie.client.version` |
| `2026-06-26 13:29:26` | `cowrie.client.kex` |
| `2026-06-26 13:29:28` | `cowrie.login.success` |
| `2026-06-26 13:29:29` | `cowrie.session.params` |
| `2026-06-26 13:29:29` | `cowrie.command.input` |
| `2026-06-26 13:29:30` | `cowrie.log.closed` |
| `2026-06-26 13:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b88dada2f8a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:29 |
| **Last Seen** | 2026-06-26 13:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:29:30` | `cowrie.session.connect` |
| `2026-06-26 13:29:30` | `cowrie.client.version` |
| `2026-06-26 13:29:30` | `cowrie.client.kex` |
| `2026-06-26 13:29:31` | `cowrie.login.success` |
| `2026-06-26 13:29:31` | `cowrie.session.params` |
| `2026-06-26 13:29:31` | `cowrie.command.input` |
| `2026-06-26 13:29:32` | `cowrie.log.closed` |
| `2026-06-26 13:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6179fdff20f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:30 |
| **Last Seen** | 2026-06-26 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:30:33` | `cowrie.session.connect` |
| `2026-06-26 13:30:33` | `cowrie.client.version` |
| `2026-06-26 13:30:33` | `cowrie.client.kex` |
| `2026-06-26 13:30:34` | `cowrie.login.success` |
| `2026-06-26 13:30:34` | `cowrie.session.params` |
| `2026-06-26 13:30:34` | `cowrie.command.input` |
| `2026-06-26 13:30:35` | `cowrie.log.closed` |
| `2026-06-26 13:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a460ab5ce44

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:31 |
| **Last Seen** | 2026-06-26 13:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:31:37` | `cowrie.session.connect` |
| `2026-06-26 13:31:37` | `cowrie.client.version` |
| `2026-06-26 13:31:37` | `cowrie.client.kex` |
| `2026-06-26 13:31:37` | `cowrie.login.success` |
| `2026-06-26 13:31:38` | `cowrie.session.params` |
| `2026-06-26 13:31:38` | `cowrie.command.input` |
| `2026-06-26 13:31:38` | `cowrie.log.closed` |
| `2026-06-26 13:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02ea32f5d7c7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:32 |
| **Last Seen** | 2026-06-26 13:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:32:42` | `cowrie.session.connect` |
| `2026-06-26 13:32:42` | `cowrie.client.version` |
| `2026-06-26 13:32:43` | `cowrie.client.kex` |
| `2026-06-26 13:32:43` | `cowrie.login.success` |
| `2026-06-26 13:32:44` | `cowrie.session.params` |
| `2026-06-26 13:32:44` | `cowrie.command.input` |
| `2026-06-26 13:32:44` | `cowrie.log.closed` |
| `2026-06-26 13:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0675dd64103a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:33 |
| **Last Seen** | 2026-06-26 13:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:33:52` | `cowrie.session.connect` |
| `2026-06-26 13:33:52` | `cowrie.client.version` |
| `2026-06-26 13:33:52` | `cowrie.client.kex` |
| `2026-06-26 13:33:53` | `cowrie.login.success` |
| `2026-06-26 13:33:53` | `cowrie.session.params` |
| `2026-06-26 13:33:53` | `cowrie.command.input` |
| `2026-06-26 13:33:53` | `cowrie.log.closed` |
| `2026-06-26 13:33:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31e42186a8c6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:35 |
| **Last Seen** | 2026-06-26 13:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:35:01` | `cowrie.session.connect` |
| `2026-06-26 13:35:01` | `cowrie.client.version` |
| `2026-06-26 13:35:01` | `cowrie.client.kex` |
| `2026-06-26 13:35:01` | `cowrie.login.success` |
| `2026-06-26 13:35:02` | `cowrie.session.params` |
| `2026-06-26 13:35:02` | `cowrie.command.input` |
| `2026-06-26 13:35:02` | `cowrie.log.closed` |
| `2026-06-26 13:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29cfea0cf1f8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:36 |
| **Last Seen** | 2026-06-26 13:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:36:13` | `cowrie.session.connect` |
| `2026-06-26 13:36:13` | `cowrie.client.version` |
| `2026-06-26 13:36:13` | `cowrie.client.kex` |
| `2026-06-26 13:36:13` | `cowrie.login.success` |
| `2026-06-26 13:36:14` | `cowrie.session.params` |
| `2026-06-26 13:36:14` | `cowrie.command.input` |
| `2026-06-26 13:36:14` | `cowrie.log.closed` |
| `2026-06-26 13:36:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-138ffa11b653

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:37 |
| **Last Seen** | 2026-06-26 13:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:37:19` | `cowrie.session.connect` |
| `2026-06-26 13:37:19` | `cowrie.client.version` |
| `2026-06-26 13:37:19` | `cowrie.client.kex` |
| `2026-06-26 13:37:20` | `cowrie.login.success` |
| `2026-06-26 13:37:20` | `cowrie.session.params` |
| `2026-06-26 13:37:20` | `cowrie.command.input` |
| `2026-06-26 13:37:21` | `cowrie.log.closed` |
| `2026-06-26 13:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1587b24dfd92

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 13:37 |
| **Last Seen** | 2026-06-26 13:38 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:37:51` | `cowrie.session.connect` |
| `2026-06-26 13:37:52` | `cowrie.client.version` |
| `2026-06-26 13:37:52` | `cowrie.client.kex` |
| `2026-06-26 13:37:58` | `cowrie.login.success` |
| `2026-06-26 13:38:01` | `cowrie.session.params` |
| `2026-06-26 13:38:01` | `cowrie.command.input` |
| `2026-06-26 13:38:02` | `cowrie.log.closed` |
| `2026-06-26 13:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-307acd891171

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:38 |
| **Last Seen** | 2026-06-26 13:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:38:25` | `cowrie.session.connect` |
| `2026-06-26 13:38:25` | `cowrie.client.version` |
| `2026-06-26 13:38:25` | `cowrie.client.kex` |
| `2026-06-26 13:38:25` | `cowrie.login.success` |
| `2026-06-26 13:38:26` | `cowrie.session.params` |
| `2026-06-26 13:38:26` | `cowrie.command.input` |
| `2026-06-26 13:38:26` | `cowrie.log.closed` |
| `2026-06-26 13:38:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa4fc7c3321c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:39 |
| **Last Seen** | 2026-06-26 13:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:39:33` | `cowrie.session.connect` |
| `2026-06-26 13:39:33` | `cowrie.client.version` |
| `2026-06-26 13:39:33` | `cowrie.client.kex` |
| `2026-06-26 13:39:33` | `cowrie.login.success` |
| `2026-06-26 13:39:34` | `cowrie.session.params` |
| `2026-06-26 13:39:34` | `cowrie.command.input` |
| `2026-06-26 13:39:34` | `cowrie.log.closed` |
| `2026-06-26 13:39:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-864222e22e7e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:40 |
| **Last Seen** | 2026-06-26 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:40:44` | `cowrie.session.connect` |
| `2026-06-26 13:40:44` | `cowrie.client.version` |
| `2026-06-26 13:40:44` | `cowrie.client.kex` |
| `2026-06-26 13:40:44` | `cowrie.login.success` |
| `2026-06-26 13:40:45` | `cowrie.session.params` |
| `2026-06-26 13:40:45` | `cowrie.command.input` |
| `2026-06-26 13:40:45` | `cowrie.log.closed` |
| `2026-06-26 13:40:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd9f188853b6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:41 |
| **Last Seen** | 2026-06-26 13:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:41:54` | `cowrie.session.connect` |
| `2026-06-26 13:41:54` | `cowrie.client.version` |
| `2026-06-26 13:41:54` | `cowrie.client.kex` |
| `2026-06-26 13:41:54` | `cowrie.login.success` |
| `2026-06-26 13:41:55` | `cowrie.session.params` |
| `2026-06-26 13:41:55` | `cowrie.command.input` |
| `2026-06-26 13:41:55` | `cowrie.log.closed` |
| `2026-06-26 13:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-426b9c653a44

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:43 |
| **Last Seen** | 2026-06-26 13:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:43:01` | `cowrie.session.connect` |
| `2026-06-26 13:43:01` | `cowrie.client.version` |
| `2026-06-26 13:43:01` | `cowrie.client.kex` |
| `2026-06-26 13:43:02` | `cowrie.login.success` |
| `2026-06-26 13:43:02` | `cowrie.session.params` |
| `2026-06-26 13:43:02` | `cowrie.command.input` |
| `2026-06-26 13:43:02` | `cowrie.log.closed` |
| `2026-06-26 13:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-948c740ed6e6

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 13:43 |
| **Last Seen** | 2026-06-26 13:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:43:45` | `cowrie.session.connect` |
| `2026-06-26 13:43:45` | `cowrie.client.version` |
| `2026-06-26 13:43:45` | `cowrie.client.kex` |
| `2026-06-26 13:43:47` | `cowrie.login.success` |
| `2026-06-26 13:43:48` | `cowrie.session.params` |
| `2026-06-26 13:43:48` | `cowrie.command.input` |
| `2026-06-26 13:43:48` | `cowrie.log.closed` |
| `2026-06-26 13:43:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1c63b2a5374

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:44 |
| **Last Seen** | 2026-06-26 13:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:44:12` | `cowrie.session.connect` |
| `2026-06-26 13:44:12` | `cowrie.client.version` |
| `2026-06-26 13:44:12` | `cowrie.client.kex` |
| `2026-06-26 13:44:12` | `cowrie.login.success` |
| `2026-06-26 13:44:13` | `cowrie.session.params` |
| `2026-06-26 13:44:13` | `cowrie.command.input` |
| `2026-06-26 13:44:13` | `cowrie.log.closed` |
| `2026-06-26 13:44:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cc8c725518f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:45 |
| **Last Seen** | 2026-06-26 13:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:45:23` | `cowrie.session.connect` |
| `2026-06-26 13:45:23` | `cowrie.client.version` |
| `2026-06-26 13:45:23` | `cowrie.client.kex` |
| `2026-06-26 13:45:23` | `cowrie.login.success` |
| `2026-06-26 13:45:24` | `cowrie.session.params` |
| `2026-06-26 13:45:24` | `cowrie.command.input` |
| `2026-06-26 13:45:24` | `cowrie.log.closed` |
| `2026-06-26 13:45:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b44eb0001dda

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:46 |
| **Last Seen** | 2026-06-26 13:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:46:31` | `cowrie.session.connect` |
| `2026-06-26 13:46:31` | `cowrie.client.version` |
| `2026-06-26 13:46:31` | `cowrie.client.kex` |
| `2026-06-26 13:46:32` | `cowrie.login.success` |
| `2026-06-26 13:46:33` | `cowrie.session.params` |
| `2026-06-26 13:46:33` | `cowrie.command.input` |
| `2026-06-26 13:46:33` | `cowrie.log.closed` |
| `2026-06-26 13:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4db6549d7234

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:47 |
| **Last Seen** | 2026-06-26 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:47:40` | `cowrie.session.connect` |
| `2026-06-26 13:47:40` | `cowrie.client.version` |
| `2026-06-26 13:47:40` | `cowrie.client.kex` |
| `2026-06-26 13:47:40` | `cowrie.login.success` |
| `2026-06-26 13:47:41` | `cowrie.session.params` |
| `2026-06-26 13:47:41` | `cowrie.command.input` |
| `2026-06-26 13:47:41` | `cowrie.log.closed` |
| `2026-06-26 13:47:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c4f25cfec05

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 13:48 |
| **Last Seen** | 2026-06-26 13:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:48:17` | `cowrie.session.connect` |
| `2026-06-26 13:48:18` | `cowrie.client.version` |
| `2026-06-26 13:48:18` | `cowrie.client.kex` |
| `2026-06-26 13:48:24` | `cowrie.login.success` |
| `2026-06-26 13:48:26` | `cowrie.session.params` |
| `2026-06-26 13:48:26` | `cowrie.command.input` |
| `2026-06-26 13:48:28` | `cowrie.log.closed` |
| `2026-06-26 13:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68a500567214

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:48 |
| **Last Seen** | 2026-06-26 13:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:48:50` | `cowrie.session.connect` |
| `2026-06-26 13:48:50` | `cowrie.client.version` |
| `2026-06-26 13:48:50` | `cowrie.client.kex` |
| `2026-06-26 13:48:50` | `cowrie.login.success` |
| `2026-06-26 13:48:51` | `cowrie.session.params` |
| `2026-06-26 13:48:51` | `cowrie.command.input` |
| `2026-06-26 13:48:51` | `cowrie.log.closed` |
| `2026-06-26 13:48:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb0aea99d56a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-26 13:49 |
| **Last Seen** | 2026-06-26 13:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:49:55` | `cowrie.session.connect` |
| `2026-06-26 13:49:55` | `cowrie.client.version` |
| `2026-06-26 13:49:55` | `cowrie.client.kex` |
| `2026-06-26 13:49:56` | `cowrie.login.success` |
| `2026-06-26 13:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9c69f69d21f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-26 13:49 |
| **Last Seen** | 2026-06-26 13:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:49:55` | `cowrie.session.connect` |
| `2026-06-26 13:49:55` | `cowrie.client.version` |
| `2026-06-26 13:49:55` | `cowrie.client.kex` |
| `2026-06-26 13:49:56` | `cowrie.login.success` |
| `2026-06-26 13:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c92f2a877505

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-26 13:49 |
| **Last Seen** | 2026-06-26 13:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:49:57` | `cowrie.session.connect` |
| `2026-06-26 13:49:57` | `cowrie.client.version` |
| `2026-06-26 13:49:57` | `cowrie.client.kex` |
| `2026-06-26 13:49:58` | `cowrie.login.success` |
| `2026-06-26 13:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86924216ad47

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-26 13:49 |
| **Last Seen** | 2026-06-26 13:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:49:58` | `cowrie.session.connect` |
| `2026-06-26 13:49:58` | `cowrie.client.version` |
| `2026-06-26 13:49:58` | `cowrie.client.kex` |
| `2026-06-26 13:49:59` | `cowrie.login.success` |
| `2026-06-26 13:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e28e25756ad

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:50 |
| **Last Seen** | 2026-06-26 13:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:50:02` | `cowrie.session.connect` |
| `2026-06-26 13:50:02` | `cowrie.client.version` |
| `2026-06-26 13:50:02` | `cowrie.client.kex` |
| `2026-06-26 13:50:02` | `cowrie.login.success` |
| `2026-06-26 13:50:03` | `cowrie.session.params` |
| `2026-06-26 13:50:03` | `cowrie.command.input` |
| `2026-06-26 13:50:03` | `cowrie.log.closed` |
| `2026-06-26 13:50:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa6a1f1905ba

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:51 |
| **Last Seen** | 2026-06-26 13:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:51:16` | `cowrie.session.connect` |
| `2026-06-26 13:51:16` | `cowrie.client.version` |
| `2026-06-26 13:51:16` | `cowrie.client.kex` |
| `2026-06-26 13:51:16` | `cowrie.login.success` |
| `2026-06-26 13:51:17` | `cowrie.session.params` |
| `2026-06-26 13:51:17` | `cowrie.command.input` |
| `2026-06-26 13:51:17` | `cowrie.log.closed` |
| `2026-06-26 13:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a19e783f55f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:52 |
| **Last Seen** | 2026-06-26 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:52:28` | `cowrie.session.connect` |
| `2026-06-26 13:52:28` | `cowrie.client.version` |
| `2026-06-26 13:52:28` | `cowrie.client.kex` |
| `2026-06-26 13:52:28` | `cowrie.login.success` |
| `2026-06-26 13:52:29` | `cowrie.session.params` |
| `2026-06-26 13:52:29` | `cowrie.command.input` |
| `2026-06-26 13:52:29` | `cowrie.log.closed` |
| `2026-06-26 13:52:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bde888ee15d0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:53 |
| **Last Seen** | 2026-06-26 13:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:53:40` | `cowrie.session.connect` |
| `2026-06-26 13:53:40` | `cowrie.client.version` |
| `2026-06-26 13:53:40` | `cowrie.client.kex` |
| `2026-06-26 13:53:41` | `cowrie.login.success` |
| `2026-06-26 13:53:41` | `cowrie.session.params` |
| `2026-06-26 13:53:41` | `cowrie.command.input` |
| `2026-06-26 13:53:41` | `cowrie.log.closed` |
| `2026-06-26 13:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-700f6867ab7a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:54 |
| **Last Seen** | 2026-06-26 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:54:52` | `cowrie.session.connect` |
| `2026-06-26 13:54:52` | `cowrie.client.version` |
| `2026-06-26 13:54:52` | `cowrie.client.kex` |
| `2026-06-26 13:54:53` | `cowrie.login.success` |
| `2026-06-26 13:54:54` | `cowrie.session.params` |
| `2026-06-26 13:54:54` | `cowrie.command.input` |
| `2026-06-26 13:54:54` | `cowrie.log.closed` |
| `2026-06-26 13:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ce374d36a4c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:56 |
| **Last Seen** | 2026-06-26 13:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:56:02` | `cowrie.session.connect` |
| `2026-06-26 13:56:02` | `cowrie.client.version` |
| `2026-06-26 13:56:02` | `cowrie.client.kex` |
| `2026-06-26 13:56:02` | `cowrie.login.success` |
| `2026-06-26 13:56:03` | `cowrie.session.params` |
| `2026-06-26 13:56:03` | `cowrie.command.input` |
| `2026-06-26 13:56:03` | `cowrie.log.closed` |
| `2026-06-26 13:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-614b7ebef380

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:57 |
| **Last Seen** | 2026-06-26 13:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:57:14` | `cowrie.session.connect` |
| `2026-06-26 13:57:14` | `cowrie.client.version` |
| `2026-06-26 13:57:14` | `cowrie.client.kex` |
| `2026-06-26 13:57:14` | `cowrie.login.success` |
| `2026-06-26 13:57:15` | `cowrie.session.params` |
| `2026-06-26 13:57:15` | `cowrie.command.input` |
| `2026-06-26 13:57:15` | `cowrie.log.closed` |
| `2026-06-26 13:57:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee14e37ba9e9

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 13:58 |
| **Last Seen** | 2026-06-26 13:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:58:10` | `cowrie.session.connect` |
| `2026-06-26 13:58:10` | `cowrie.client.version` |
| `2026-06-26 13:58:10` | `cowrie.client.kex` |
| `2026-06-26 13:58:12` | `cowrie.login.success` |
| `2026-06-26 13:58:14` | `cowrie.session.params` |
| `2026-06-26 13:58:14` | `cowrie.command.input` |
| `2026-06-26 13:58:14` | `cowrie.log.closed` |
| `2026-06-26 13:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aa2275cf66e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:58 |
| **Last Seen** | 2026-06-26 13:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:58:30` | `cowrie.session.connect` |
| `2026-06-26 13:58:30` | `cowrie.client.version` |
| `2026-06-26 13:58:30` | `cowrie.client.kex` |
| `2026-06-26 13:58:30` | `cowrie.login.success` |
| `2026-06-26 13:58:31` | `cowrie.session.params` |
| `2026-06-26 13:58:31` | `cowrie.command.input` |
| `2026-06-26 13:58:31` | `cowrie.log.closed` |
| `2026-06-26 13:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bfa26a60c03

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 13:58 |
| **Last Seen** | 2026-06-26 13:58 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:58:41` | `cowrie.session.connect` |
| `2026-06-26 13:58:42` | `cowrie.client.version` |
| `2026-06-26 13:58:42` | `cowrie.client.kex` |
| `2026-06-26 13:58:48` | `cowrie.login.success` |
| `2026-06-26 13:58:51` | `cowrie.session.params` |
| `2026-06-26 13:58:51` | `cowrie.command.input` |
| `2026-06-26 13:58:52` | `cowrie.log.closed` |
| `2026-06-26 13:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc6218e42123

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 13:59 |
| **Last Seen** | 2026-06-26 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 13:59:47` | `cowrie.session.connect` |
| `2026-06-26 13:59:47` | `cowrie.client.version` |
| `2026-06-26 13:59:47` | `cowrie.client.kex` |
| `2026-06-26 13:59:48` | `cowrie.login.success` |
| `2026-06-26 13:59:49` | `cowrie.session.params` |
| `2026-06-26 13:59:49` | `cowrie.command.input` |
| `2026-06-26 13:59:49` | `cowrie.log.closed` |
| `2026-06-26 13:59:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c58bad053671

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:00 |
| **Last Seen** | 2026-06-26 14:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:00:48` | `cowrie.session.connect` |
| `2026-06-26 14:00:48` | `cowrie.client.version` |
| `2026-06-26 14:00:48` | `cowrie.client.kex` |
| `2026-06-26 14:00:49` | `cowrie.login.success` |
| `2026-06-26 14:00:49` | `cowrie.session.params` |
| `2026-06-26 14:00:49` | `cowrie.command.input` |
| `2026-06-26 14:00:50` | `cowrie.log.closed` |
| `2026-06-26 14:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-494279ce6d13

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:01 |
| **Last Seen** | 2026-06-26 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:01:41` | `cowrie.session.connect` |
| `2026-06-26 14:01:41` | `cowrie.client.version` |
| `2026-06-26 14:01:41` | `cowrie.client.kex` |
| `2026-06-26 14:01:41` | `cowrie.login.success` |
| `2026-06-26 14:01:42` | `cowrie.session.params` |
| `2026-06-26 14:01:42` | `cowrie.command.input` |
| `2026-06-26 14:01:42` | `cowrie.log.closed` |
| `2026-06-26 14:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dc7759cefa3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:02 |
| **Last Seen** | 2026-06-26 14:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:02:30` | `cowrie.session.connect` |
| `2026-06-26 14:02:30` | `cowrie.client.version` |
| `2026-06-26 14:02:30` | `cowrie.client.kex` |
| `2026-06-26 14:02:30` | `cowrie.login.success` |
| `2026-06-26 14:02:31` | `cowrie.session.params` |
| `2026-06-26 14:02:31` | `cowrie.command.input` |
| `2026-06-26 14:02:31` | `cowrie.log.closed` |
| `2026-06-26 14:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28d2fd816dd2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:03 |
| **Last Seen** | 2026-06-26 14:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:03:21` | `cowrie.session.connect` |
| `2026-06-26 14:03:21` | `cowrie.client.version` |
| `2026-06-26 14:03:21` | `cowrie.client.kex` |
| `2026-06-26 14:03:22` | `cowrie.login.success` |
| `2026-06-26 14:03:22` | `cowrie.session.params` |
| `2026-06-26 14:03:22` | `cowrie.command.input` |
| `2026-06-26 14:03:22` | `cowrie.log.closed` |
| `2026-06-26 14:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-021f42e8b506

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:04 |
| **Last Seen** | 2026-06-26 14:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:04:13` | `cowrie.session.connect` |
| `2026-06-26 14:04:13` | `cowrie.client.version` |
| `2026-06-26 14:04:13` | `cowrie.client.kex` |
| `2026-06-26 14:04:13` | `cowrie.login.success` |
| `2026-06-26 14:04:14` | `cowrie.session.params` |
| `2026-06-26 14:04:14` | `cowrie.command.input` |
| `2026-06-26 14:04:14` | `cowrie.log.closed` |
| `2026-06-26 14:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e2b126446ff

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:05 |
| **Last Seen** | 2026-06-26 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:05:07` | `cowrie.session.connect` |
| `2026-06-26 14:05:07` | `cowrie.client.version` |
| `2026-06-26 14:05:07` | `cowrie.client.kex` |
| `2026-06-26 14:05:07` | `cowrie.login.success` |
| `2026-06-26 14:05:08` | `cowrie.session.params` |
| `2026-06-26 14:05:08` | `cowrie.command.input` |
| `2026-06-26 14:05:08` | `cowrie.log.closed` |
| `2026-06-26 14:05:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2facd269a435

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:06 |
| **Last Seen** | 2026-06-26 14:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:06:02` | `cowrie.session.connect` |
| `2026-06-26 14:06:02` | `cowrie.client.version` |
| `2026-06-26 14:06:02` | `cowrie.client.kex` |
| `2026-06-26 14:06:03` | `cowrie.login.success` |
| `2026-06-26 14:06:03` | `cowrie.session.params` |
| `2026-06-26 14:06:03` | `cowrie.command.input` |
| `2026-06-26 14:06:03` | `cowrie.log.closed` |
| `2026-06-26 14:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-464955bba976

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:06 |
| **Last Seen** | 2026-06-26 14:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:06:54` | `cowrie.session.connect` |
| `2026-06-26 14:06:54` | `cowrie.client.version` |
| `2026-06-26 14:06:54` | `cowrie.client.kex` |
| `2026-06-26 14:06:54` | `cowrie.login.success` |
| `2026-06-26 14:06:55` | `cowrie.session.params` |
| `2026-06-26 14:06:55` | `cowrie.command.input` |
| `2026-06-26 14:06:55` | `cowrie.log.closed` |
| `2026-06-26 14:06:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c74ac89081ed

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:07 |
| **Last Seen** | 2026-06-26 14:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:07:43` | `cowrie.session.connect` |
| `2026-06-26 14:07:43` | `cowrie.client.version` |
| `2026-06-26 14:07:43` | `cowrie.client.kex` |
| `2026-06-26 14:07:43` | `cowrie.login.success` |
| `2026-06-26 14:07:44` | `cowrie.session.params` |
| `2026-06-26 14:07:44` | `cowrie.command.input` |
| `2026-06-26 14:07:44` | `cowrie.log.closed` |
| `2026-06-26 14:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a6204a9478b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:08 |
| **Last Seen** | 2026-06-26 14:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:08:32` | `cowrie.session.connect` |
| `2026-06-26 14:08:32` | `cowrie.client.version` |
| `2026-06-26 14:08:32` | `cowrie.client.kex` |
| `2026-06-26 14:08:32` | `cowrie.login.success` |
| `2026-06-26 14:08:33` | `cowrie.session.params` |
| `2026-06-26 14:08:33` | `cowrie.command.input` |
| `2026-06-26 14:08:33` | `cowrie.log.closed` |
| `2026-06-26 14:08:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aec00200a10

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 14:09 |
| **Last Seen** | 2026-06-26 14:09 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:09:18` | `cowrie.session.connect` |
| `2026-06-26 14:09:19` | `cowrie.client.version` |
| `2026-06-26 14:09:19` | `cowrie.client.kex` |
| `2026-06-26 14:09:26` | `cowrie.login.success` |
| `2026-06-26 14:09:28` | `cowrie.session.params` |
| `2026-06-26 14:09:28` | `cowrie.command.input` |
| `2026-06-26 14:09:30` | `cowrie.log.closed` |
| `2026-06-26 14:09:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa20eab73022

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:09 |
| **Last Seen** | 2026-06-26 14:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:09:21` | `cowrie.session.connect` |
| `2026-06-26 14:09:21` | `cowrie.client.version` |
| `2026-06-26 14:09:21` | `cowrie.client.kex` |
| `2026-06-26 14:09:21` | `cowrie.login.success` |
| `2026-06-26 14:09:22` | `cowrie.session.params` |
| `2026-06-26 14:09:22` | `cowrie.command.input` |
| `2026-06-26 14:09:22` | `cowrie.log.closed` |
| `2026-06-26 14:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d88e878290be

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-26 14:09 |
| **Last Seen** | 2026-06-26 14:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:09:32` | `cowrie.session.connect` |
| `2026-06-26 14:09:32` | `cowrie.client.version` |
| `2026-06-26 14:09:32` | `cowrie.client.kex` |
| `2026-06-26 14:09:33` | `cowrie.login.success` |
| `2026-06-26 14:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa4f56e1820a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-26 14:09 |
| **Last Seen** | 2026-06-26 14:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:09:32` | `cowrie.session.connect` |
| `2026-06-26 14:09:32` | `cowrie.client.version` |
| `2026-06-26 14:09:32` | `cowrie.client.kex` |
| `2026-06-26 14:09:33` | `cowrie.login.success` |
| `2026-06-26 14:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4948c7c4b86

| Field | Detail |
|---|---|
| **Source IP** | `188.166.183[.]133` |
| **First Seen** | 2026-06-26 14:09 |
| **Last Seen** | 2026-06-26 14:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:09:54` | `cowrie.session.connect` |
| `2026-06-26 14:09:54` | `cowrie.client.version` |
| `2026-06-26 14:09:54` | `cowrie.client.kex` |
| `2026-06-26 14:09:55` | `cowrie.login.success` |
| `2026-06-26 14:09:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.166.183[.]133` to AbuseIPDB if not already reported
- [ ] Block `188.166.183[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebe5e46e5bf6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:10 |
| **Last Seen** | 2026-06-26 14:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:10:12` | `cowrie.session.connect` |
| `2026-06-26 14:10:12` | `cowrie.client.version` |
| `2026-06-26 14:10:12` | `cowrie.client.kex` |
| `2026-06-26 14:10:13` | `cowrie.login.success` |
| `2026-06-26 14:10:13` | `cowrie.session.params` |
| `2026-06-26 14:10:13` | `cowrie.command.input` |
| `2026-06-26 14:10:14` | `cowrie.log.closed` |
| `2026-06-26 14:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-707a810e5376

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:11 |
| **Last Seen** | 2026-06-26 14:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:11:05` | `cowrie.session.connect` |
| `2026-06-26 14:11:05` | `cowrie.client.version` |
| `2026-06-26 14:11:05` | `cowrie.client.kex` |
| `2026-06-26 14:11:05` | `cowrie.login.success` |
| `2026-06-26 14:11:06` | `cowrie.session.params` |
| `2026-06-26 14:11:06` | `cowrie.command.input` |
| `2026-06-26 14:11:06` | `cowrie.log.closed` |
| `2026-06-26 14:11:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40b2eebfc34d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:11 |
| **Last Seen** | 2026-06-26 14:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:11:59` | `cowrie.session.connect` |
| `2026-06-26 14:11:59` | `cowrie.client.version` |
| `2026-06-26 14:11:59` | `cowrie.client.kex` |
| `2026-06-26 14:12:00` | `cowrie.login.success` |
| `2026-06-26 14:12:00` | `cowrie.session.params` |
| `2026-06-26 14:12:00` | `cowrie.command.input` |
| `2026-06-26 14:12:00` | `cowrie.log.closed` |
| `2026-06-26 14:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e79f7b2305a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 14:12 |
| **Last Seen** | 2026-06-26 14:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:12:39` | `cowrie.session.connect` |
| `2026-06-26 14:12:39` | `cowrie.client.version` |
| `2026-06-26 14:12:39` | `cowrie.client.kex` |
| `2026-06-26 14:12:42` | `cowrie.login.success` |
| `2026-06-26 14:12:44` | `cowrie.session.params` |
| `2026-06-26 14:12:44` | `cowrie.command.input` |
| `2026-06-26 14:12:44` | `cowrie.log.closed` |
| `2026-06-26 14:12:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7477034983df

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:12 |
| **Last Seen** | 2026-06-26 14:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:12:53` | `cowrie.session.connect` |
| `2026-06-26 14:12:53` | `cowrie.client.version` |
| `2026-06-26 14:12:53` | `cowrie.client.kex` |
| `2026-06-26 14:12:53` | `cowrie.login.success` |
| `2026-06-26 14:12:54` | `cowrie.session.params` |
| `2026-06-26 14:12:54` | `cowrie.command.input` |
| `2026-06-26 14:12:54` | `cowrie.log.closed` |
| `2026-06-26 14:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc81c90342e4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:13 |
| **Last Seen** | 2026-06-26 14:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:13:48` | `cowrie.session.connect` |
| `2026-06-26 14:13:48` | `cowrie.client.version` |
| `2026-06-26 14:13:48` | `cowrie.client.kex` |
| `2026-06-26 14:13:48` | `cowrie.login.success` |
| `2026-06-26 14:13:49` | `cowrie.session.params` |
| `2026-06-26 14:13:49` | `cowrie.command.input` |
| `2026-06-26 14:13:49` | `cowrie.log.closed` |
| `2026-06-26 14:13:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3bdc3d4c8ff

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:14 |
| **Last Seen** | 2026-06-26 14:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:14:40` | `cowrie.session.connect` |
| `2026-06-26 14:14:40` | `cowrie.client.version` |
| `2026-06-26 14:14:40` | `cowrie.client.kex` |
| `2026-06-26 14:14:40` | `cowrie.login.success` |
| `2026-06-26 14:14:41` | `cowrie.session.params` |
| `2026-06-26 14:14:41` | `cowrie.command.input` |
| `2026-06-26 14:14:41` | `cowrie.log.closed` |
| `2026-06-26 14:14:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a970846cffd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:15 |
| **Last Seen** | 2026-06-26 14:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:15:35` | `cowrie.session.connect` |
| `2026-06-26 14:15:35` | `cowrie.client.version` |
| `2026-06-26 14:15:36` | `cowrie.client.kex` |
| `2026-06-26 14:15:36` | `cowrie.login.success` |
| `2026-06-26 14:15:37` | `cowrie.session.params` |
| `2026-06-26 14:15:37` | `cowrie.command.input` |
| `2026-06-26 14:15:37` | `cowrie.log.closed` |
| `2026-06-26 14:15:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38db69a0c3d5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:16 |
| **Last Seen** | 2026-06-26 14:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:16:29` | `cowrie.session.connect` |
| `2026-06-26 14:16:29` | `cowrie.client.version` |
| `2026-06-26 14:16:29` | `cowrie.client.kex` |
| `2026-06-26 14:16:29` | `cowrie.login.success` |
| `2026-06-26 14:16:30` | `cowrie.session.params` |
| `2026-06-26 14:16:30` | `cowrie.command.input` |
| `2026-06-26 14:16:30` | `cowrie.log.closed` |
| `2026-06-26 14:16:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5ebc8375b3a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-06-26 14:17 |
| **Last Seen** | 2026-06-26 14:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:17:12` | `cowrie.session.connect` |
| `2026-06-26 14:17:12` | `cowrie.client.version` |
| `2026-06-26 14:17:12` | `cowrie.client.kex` |
| `2026-06-26 14:17:12` | `cowrie.login.success` |
| `2026-06-26 14:17:13` | `cowrie.session.params` |
| `2026-06-26 14:17:13` | `cowrie.command.input` |
| `2026-06-26 14:17:13` | `cowrie.log.closed` |
| `2026-06-26 14:17:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff8f9c00f67a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:17 |
| **Last Seen** | 2026-06-26 14:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:17:21` | `cowrie.session.connect` |
| `2026-06-26 14:17:21` | `cowrie.client.version` |
| `2026-06-26 14:17:21` | `cowrie.client.kex` |
| `2026-06-26 14:17:21` | `cowrie.login.success` |
| `2026-06-26 14:17:22` | `cowrie.session.params` |
| `2026-06-26 14:17:22` | `cowrie.command.input` |
| `2026-06-26 14:17:22` | `cowrie.log.closed` |
| `2026-06-26 14:17:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dabd87d234c8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:18 |
| **Last Seen** | 2026-06-26 14:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:18:16` | `cowrie.session.connect` |
| `2026-06-26 14:18:16` | `cowrie.client.version` |
| `2026-06-26 14:18:16` | `cowrie.client.kex` |
| `2026-06-26 14:18:17` | `cowrie.login.success` |
| `2026-06-26 14:18:18` | `cowrie.session.params` |
| `2026-06-26 14:18:18` | `cowrie.command.input` |
| `2026-06-26 14:18:18` | `cowrie.log.closed` |
| `2026-06-26 14:18:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0719861d2a4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:19 |
| **Last Seen** | 2026-06-26 14:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:19:15` | `cowrie.session.connect` |
| `2026-06-26 14:19:15` | `cowrie.client.version` |
| `2026-06-26 14:19:15` | `cowrie.client.kex` |
| `2026-06-26 14:19:15` | `cowrie.login.success` |
| `2026-06-26 14:19:16` | `cowrie.session.params` |
| `2026-06-26 14:19:16` | `cowrie.command.input` |
| `2026-06-26 14:19:16` | `cowrie.log.closed` |
| `2026-06-26 14:19:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f1c17d149a7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 14:20 |
| **Last Seen** | 2026-06-26 14:20 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:20:05` | `cowrie.session.connect` |
| `2026-06-26 14:20:07` | `cowrie.client.version` |
| `2026-06-26 14:20:07` | `cowrie.client.kex` |
| `2026-06-26 14:20:13` | `cowrie.login.success` |
| `2026-06-26 14:20:16` | `cowrie.session.params` |
| `2026-06-26 14:20:16` | `cowrie.command.input` |
| `2026-06-26 14:20:17` | `cowrie.log.closed` |
| `2026-06-26 14:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c03d1bd5a69

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:20 |
| **Last Seen** | 2026-06-26 14:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:20:10` | `cowrie.session.connect` |
| `2026-06-26 14:20:10` | `cowrie.client.version` |
| `2026-06-26 14:20:10` | `cowrie.client.kex` |
| `2026-06-26 14:20:10` | `cowrie.login.success` |
| `2026-06-26 14:20:11` | `cowrie.session.params` |
| `2026-06-26 14:20:11` | `cowrie.command.input` |
| `2026-06-26 14:20:11` | `cowrie.log.closed` |
| `2026-06-26 14:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49a6b5ee7acb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:21 |
| **Last Seen** | 2026-06-26 14:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:21:03` | `cowrie.session.connect` |
| `2026-06-26 14:21:03` | `cowrie.client.version` |
| `2026-06-26 14:21:03` | `cowrie.client.kex` |
| `2026-06-26 14:21:03` | `cowrie.login.success` |
| `2026-06-26 14:21:04` | `cowrie.session.params` |
| `2026-06-26 14:21:04` | `cowrie.command.input` |
| `2026-06-26 14:21:04` | `cowrie.log.closed` |
| `2026-06-26 14:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d28dc5d89623

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:21 |
| **Last Seen** | 2026-06-26 14:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:21:55` | `cowrie.session.connect` |
| `2026-06-26 14:21:55` | `cowrie.client.version` |
| `2026-06-26 14:21:55` | `cowrie.client.kex` |
| `2026-06-26 14:21:55` | `cowrie.login.success` |
| `2026-06-26 14:21:56` | `cowrie.session.params` |
| `2026-06-26 14:21:56` | `cowrie.command.input` |
| `2026-06-26 14:21:56` | `cowrie.log.closed` |
| `2026-06-26 14:21:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51f6f254dd4d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:22 |
| **Last Seen** | 2026-06-26 14:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:22:47` | `cowrie.session.connect` |
| `2026-06-26 14:22:47` | `cowrie.client.version` |
| `2026-06-26 14:22:47` | `cowrie.client.kex` |
| `2026-06-26 14:22:48` | `cowrie.login.success` |
| `2026-06-26 14:22:49` | `cowrie.session.params` |
| `2026-06-26 14:22:49` | `cowrie.command.input` |
| `2026-06-26 14:22:49` | `cowrie.log.closed` |
| `2026-06-26 14:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dd9d9f82689

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:23 |
| **Last Seen** | 2026-06-26 14:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:23:41` | `cowrie.session.connect` |
| `2026-06-26 14:23:41` | `cowrie.client.version` |
| `2026-06-26 14:23:41` | `cowrie.client.kex` |
| `2026-06-26 14:23:41` | `cowrie.login.success` |
| `2026-06-26 14:23:42` | `cowrie.session.params` |
| `2026-06-26 14:23:42` | `cowrie.command.input` |
| `2026-06-26 14:23:42` | `cowrie.log.closed` |
| `2026-06-26 14:23:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62eec377bc67

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:24 |
| **Last Seen** | 2026-06-26 14:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:24:38` | `cowrie.session.connect` |
| `2026-06-26 14:24:38` | `cowrie.client.version` |
| `2026-06-26 14:24:38` | `cowrie.client.kex` |
| `2026-06-26 14:24:39` | `cowrie.login.success` |
| `2026-06-26 14:24:40` | `cowrie.session.params` |
| `2026-06-26 14:24:40` | `cowrie.command.input` |
| `2026-06-26 14:24:40` | `cowrie.log.closed` |
| `2026-06-26 14:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e894cc9d11db

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:25 |
| **Last Seen** | 2026-06-26 14:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:25:33` | `cowrie.session.connect` |
| `2026-06-26 14:25:33` | `cowrie.client.version` |
| `2026-06-26 14:25:33` | `cowrie.client.kex` |
| `2026-06-26 14:25:34` | `cowrie.login.success` |
| `2026-06-26 14:25:35` | `cowrie.session.params` |
| `2026-06-26 14:25:35` | `cowrie.command.input` |
| `2026-06-26 14:25:35` | `cowrie.log.closed` |
| `2026-06-26 14:25:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71dc66d955b7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-06-26 14:26 |
| **Last Seen** | 2026-06-26 14:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '000000' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:26:24` | `cowrie.session.connect` |
| `2026-06-26 14:26:24` | `cowrie.client.version` |
| `2026-06-26 14:26:24` | `cowrie.client.kex` |
| `2026-06-26 14:26:25` | `cowrie.login.success` |
| `2026-06-26 14:26:27` | `cowrie.session.params` |
| `2026-06-26 14:26:27` | `cowrie.command.input` |
| `2026-06-26 14:26:27` | `cowrie.command.input` |
| `2026-06-26 14:26:27` | `cowrie.command.input` |
| `2026-06-26 14:26:27` | `cowrie.command.input` |
| `2026-06-26 14:26:27` | `cowrie.log.closed` |
| `2026-06-26 14:26:28` | `cowrie.session.params` |
| `2026-06-26 14:26:28` | `cowrie.command.input` |
| `2026-06-26 14:26:28` | `cowrie.command.input` |
| `2026-06-26 14:26:28` | `cowrie.command.failed` |
| `2026-06-26 14:26:28` | `cowrie.command.failed` |
| `2026-06-26 14:26:28` | `cowrie.command.failed` |
| `2026-06-26 14:26:28` | `cowrie.command.failed` |
| `2026-06-26 14:26:29` | `cowrie.log.closed` |
| `2026-06-26 14:26:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a32fb86bc059

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:26 |
| **Last Seen** | 2026-06-26 14:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:26:30` | `cowrie.session.connect` |
| `2026-06-26 14:26:30` | `cowrie.client.version` |
| `2026-06-26 14:26:30` | `cowrie.client.kex` |
| `2026-06-26 14:26:30` | `cowrie.login.success` |
| `2026-06-26 14:26:31` | `cowrie.session.params` |
| `2026-06-26 14:26:31` | `cowrie.command.input` |
| `2026-06-26 14:26:31` | `cowrie.log.closed` |
| `2026-06-26 14:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec9667199c15

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 14:27 |
| **Last Seen** | 2026-06-26 14:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:27:20` | `cowrie.session.connect` |
| `2026-06-26 14:27:20` | `cowrie.client.version` |
| `2026-06-26 14:27:20` | `cowrie.client.kex` |
| `2026-06-26 14:27:22` | `cowrie.login.success` |
| `2026-06-26 14:27:24` | `cowrie.session.params` |
| `2026-06-26 14:27:24` | `cowrie.command.input` |
| `2026-06-26 14:27:25` | `cowrie.log.closed` |
| `2026-06-26 14:27:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-423a4ceb2e01

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:27 |
| **Last Seen** | 2026-06-26 14:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:27:25` | `cowrie.session.connect` |
| `2026-06-26 14:27:25` | `cowrie.client.version` |
| `2026-06-26 14:27:25` | `cowrie.client.kex` |
| `2026-06-26 14:27:25` | `cowrie.login.success` |
| `2026-06-26 14:27:26` | `cowrie.session.params` |
| `2026-06-26 14:27:26` | `cowrie.command.input` |
| `2026-06-26 14:27:26` | `cowrie.log.closed` |
| `2026-06-26 14:27:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92d18ce9da98

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-06-26 14:27 |
| **Last Seen** | 2026-06-26 14:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '111111' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:27:31` | `cowrie.session.connect` |
| `2026-06-26 14:27:31` | `cowrie.client.version` |
| `2026-06-26 14:27:31` | `cowrie.client.kex` |
| `2026-06-26 14:27:32` | `cowrie.login.success` |
| `2026-06-26 14:27:33` | `cowrie.session.params` |
| `2026-06-26 14:27:33` | `cowrie.command.input` |
| `2026-06-26 14:27:33` | `cowrie.command.input` |
| `2026-06-26 14:27:33` | `cowrie.command.input` |
| `2026-06-26 14:27:33` | `cowrie.command.input` |
| `2026-06-26 14:27:34` | `cowrie.log.closed` |
| `2026-06-26 14:27:35` | `cowrie.session.params` |
| `2026-06-26 14:27:35` | `cowrie.command.input` |
| `2026-06-26 14:27:35` | `cowrie.command.input` |
| `2026-06-26 14:27:35` | `cowrie.command.failed` |
| `2026-06-26 14:27:35` | `cowrie.command.failed` |
| `2026-06-26 14:27:35` | `cowrie.command.failed` |
| `2026-06-26 14:27:35` | `cowrie.command.failed` |
| `2026-06-26 14:27:35` | `cowrie.log.closed` |
| `2026-06-26 14:27:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f817e7229789

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:28 |
| **Last Seen** | 2026-06-26 14:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:28:18` | `cowrie.session.connect` |
| `2026-06-26 14:28:18` | `cowrie.client.version` |
| `2026-06-26 14:28:18` | `cowrie.client.kex` |
| `2026-06-26 14:28:18` | `cowrie.login.success` |
| `2026-06-26 14:28:19` | `cowrie.session.params` |
| `2026-06-26 14:28:19` | `cowrie.command.input` |
| `2026-06-26 14:28:19` | `cowrie.log.closed` |
| `2026-06-26 14:28:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2cdaea4b93f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-06-26 14:28 |
| **Last Seen** | 2026-06-26 14:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:28:38` | `cowrie.session.connect` |
| `2026-06-26 14:28:38` | `cowrie.client.version` |
| `2026-06-26 14:28:38` | `cowrie.client.kex` |
| `2026-06-26 14:28:39` | `cowrie.login.success` |
| `2026-06-26 14:28:40` | `cowrie.session.params` |
| `2026-06-26 14:28:40` | `cowrie.command.input` |
| `2026-06-26 14:28:40` | `cowrie.command.input` |
| `2026-06-26 14:28:40` | `cowrie.command.input` |
| `2026-06-26 14:28:40` | `cowrie.command.input` |
| `2026-06-26 14:28:41` | `cowrie.log.closed` |
| `2026-06-26 14:28:42` | `cowrie.session.params` |
| `2026-06-26 14:28:42` | `cowrie.command.input` |
| `2026-06-26 14:28:42` | `cowrie.command.input` |
| `2026-06-26 14:28:42` | `cowrie.command.failed` |
| `2026-06-26 14:28:42` | `cowrie.command.failed` |
| `2026-06-26 14:28:42` | `cowrie.command.failed` |
| `2026-06-26 14:28:42` | `cowrie.command.failed` |
| `2026-06-26 14:28:42` | `cowrie.log.closed` |
| `2026-06-26 14:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a35983d7d1fa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:29 |
| **Last Seen** | 2026-06-26 14:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:29:13` | `cowrie.session.connect` |
| `2026-06-26 14:29:13` | `cowrie.client.version` |
| `2026-06-26 14:29:13` | `cowrie.client.kex` |
| `2026-06-26 14:29:14` | `cowrie.login.success` |
| `2026-06-26 14:29:14` | `cowrie.session.params` |
| `2026-06-26 14:29:14` | `cowrie.command.input` |
| `2026-06-26 14:29:15` | `cowrie.log.closed` |
| `2026-06-26 14:29:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9d27be953a7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-06-26 14:29 |
| **Last Seen** | 2026-06-26 14:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:29:42` | `cowrie.session.connect` |
| `2026-06-26 14:29:42` | `cowrie.client.version` |
| `2026-06-26 14:29:42` | `cowrie.client.kex` |
| `2026-06-26 14:29:43` | `cowrie.login.success` |
| `2026-06-26 14:29:45` | `cowrie.session.params` |
| `2026-06-26 14:29:45` | `cowrie.command.input` |
| `2026-06-26 14:29:45` | `cowrie.command.input` |
| `2026-06-26 14:29:45` | `cowrie.command.input` |
| `2026-06-26 14:29:45` | `cowrie.command.input` |
| `2026-06-26 14:29:45` | `cowrie.log.closed` |
| `2026-06-26 14:29:46` | `cowrie.session.params` |
| `2026-06-26 14:29:46` | `cowrie.command.input` |
| `2026-06-26 14:29:46` | `cowrie.command.input` |
| `2026-06-26 14:29:46` | `cowrie.command.failed` |
| `2026-06-26 14:29:46` | `cowrie.command.failed` |
| `2026-06-26 14:29:46` | `cowrie.command.failed` |
| `2026-06-26 14:29:46` | `cowrie.command.failed` |
| `2026-06-26 14:29:46` | `cowrie.log.closed` |
| `2026-06-26 14:29:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-687d7bb6c65e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:30 |
| **Last Seen** | 2026-06-26 14:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:30:13` | `cowrie.session.connect` |
| `2026-06-26 14:30:13` | `cowrie.client.version` |
| `2026-06-26 14:30:13` | `cowrie.client.kex` |
| `2026-06-26 14:30:13` | `cowrie.login.success` |
| `2026-06-26 14:30:14` | `cowrie.session.params` |
| `2026-06-26 14:30:14` | `cowrie.command.input` |
| `2026-06-26 14:30:14` | `cowrie.log.closed` |
| `2026-06-26 14:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f6bf10e1dba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-06-26 14:30 |
| **Last Seen** | 2026-06-26 14:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:30:48` | `cowrie.session.connect` |
| `2026-06-26 14:30:48` | `cowrie.client.version` |
| `2026-06-26 14:30:48` | `cowrie.client.kex` |
| `2026-06-26 14:30:49` | `cowrie.login.success` |
| `2026-06-26 14:30:51` | `cowrie.session.params` |
| `2026-06-26 14:30:51` | `cowrie.command.input` |
| `2026-06-26 14:30:51` | `cowrie.command.input` |
| `2026-06-26 14:30:51` | `cowrie.command.input` |
| `2026-06-26 14:30:51` | `cowrie.command.input` |
| `2026-06-26 14:30:51` | `cowrie.log.closed` |
| `2026-06-26 14:30:52` | `cowrie.session.params` |
| `2026-06-26 14:30:52` | `cowrie.command.input` |
| `2026-06-26 14:30:52` | `cowrie.command.input` |
| `2026-06-26 14:30:52` | `cowrie.command.failed` |
| `2026-06-26 14:30:52` | `cowrie.command.failed` |
| `2026-06-26 14:30:52` | `cowrie.command.failed` |
| `2026-06-26 14:30:52` | `cowrie.command.failed` |
| `2026-06-26 14:30:53` | `cowrie.log.closed` |
| `2026-06-26 14:30:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db840660db32

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 14:30 |
| **Last Seen** | 2026-06-26 14:31 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:30:54` | `cowrie.session.connect` |
| `2026-06-26 14:30:56` | `cowrie.client.version` |
| `2026-06-26 14:30:56` | `cowrie.client.kex` |
| `2026-06-26 14:31:01` | `cowrie.login.success` |
| `2026-06-26 14:31:05` | `cowrie.session.params` |
| `2026-06-26 14:31:05` | `cowrie.command.input` |
| `2026-06-26 14:31:06` | `cowrie.log.closed` |
| `2026-06-26 14:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e6d29598190

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:31 |
| **Last Seen** | 2026-06-26 14:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:31:09` | `cowrie.session.connect` |
| `2026-06-26 14:31:09` | `cowrie.client.version` |
| `2026-06-26 14:31:09` | `cowrie.client.kex` |
| `2026-06-26 14:31:09` | `cowrie.login.success` |
| `2026-06-26 14:31:10` | `cowrie.session.params` |
| `2026-06-26 14:31:10` | `cowrie.command.input` |
| `2026-06-26 14:31:10` | `cowrie.log.closed` |
| `2026-06-26 14:31:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-977c967bf969

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-06-26 14:31 |
| **Last Seen** | 2026-06-26 14:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:31:57` | `cowrie.session.connect` |
| `2026-06-26 14:31:57` | `cowrie.client.version` |
| `2026-06-26 14:31:57` | `cowrie.client.kex` |
| `2026-06-26 14:31:59` | `cowrie.login.success` |
| `2026-06-26 14:32:00` | `cowrie.session.params` |
| `2026-06-26 14:32:00` | `cowrie.command.input` |
| `2026-06-26 14:32:00` | `cowrie.command.input` |
| `2026-06-26 14:32:00` | `cowrie.command.input` |
| `2026-06-26 14:32:00` | `cowrie.command.input` |
| `2026-06-26 14:32:01` | `cowrie.log.closed` |
| `2026-06-26 14:32:03` | `cowrie.session.params` |
| `2026-06-26 14:32:03` | `cowrie.command.input` |
| `2026-06-26 14:32:03` | `cowrie.command.input` |
| `2026-06-26 14:32:03` | `cowrie.command.failed` |
| `2026-06-26 14:32:03` | `cowrie.command.failed` |
| `2026-06-26 14:32:03` | `cowrie.command.failed` |
| `2026-06-26 14:32:03` | `cowrie.command.failed` |
| `2026-06-26 14:32:03` | `cowrie.log.closed` |
| `2026-06-26 14:32:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02830d27f6e5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:32 |
| **Last Seen** | 2026-06-26 14:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:32:04` | `cowrie.session.connect` |
| `2026-06-26 14:32:04` | `cowrie.client.version` |
| `2026-06-26 14:32:04` | `cowrie.client.kex` |
| `2026-06-26 14:32:04` | `cowrie.login.success` |
| `2026-06-26 14:32:05` | `cowrie.session.params` |
| `2026-06-26 14:32:05` | `cowrie.command.input` |
| `2026-06-26 14:32:05` | `cowrie.log.closed` |
| `2026-06-26 14:32:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c040dcc4a8a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:32 |
| **Last Seen** | 2026-06-26 14:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:32:59` | `cowrie.session.connect` |
| `2026-06-26 14:32:59` | `cowrie.client.version` |
| `2026-06-26 14:32:59` | `cowrie.client.kex` |
| `2026-06-26 14:32:59` | `cowrie.login.success` |
| `2026-06-26 14:33:00` | `cowrie.session.params` |
| `2026-06-26 14:33:00` | `cowrie.command.input` |
| `2026-06-26 14:33:00` | `cowrie.log.closed` |
| `2026-06-26 14:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b22932c8be4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:33 |
| **Last Seen** | 2026-06-26 14:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:33:55` | `cowrie.session.connect` |
| `2026-06-26 14:33:55` | `cowrie.client.version` |
| `2026-06-26 14:33:55` | `cowrie.client.kex` |
| `2026-06-26 14:33:55` | `cowrie.login.success` |
| `2026-06-26 14:33:56` | `cowrie.session.params` |
| `2026-06-26 14:33:56` | `cowrie.command.input` |
| `2026-06-26 14:33:56` | `cowrie.log.closed` |
| `2026-06-26 14:33:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d59233816b23

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-06-26 14:34 |
| **Last Seen** | 2026-06-26 14:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345678' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:34:33` | `cowrie.session.connect` |
| `2026-06-26 14:34:33` | `cowrie.client.version` |
| `2026-06-26 14:34:34` | `cowrie.client.kex` |
| `2026-06-26 14:34:35` | `cowrie.login.success` |
| `2026-06-26 14:34:37` | `cowrie.session.params` |
| `2026-06-26 14:34:37` | `cowrie.command.input` |
| `2026-06-26 14:34:37` | `cowrie.command.input` |
| `2026-06-26 14:34:37` | `cowrie.command.input` |
| `2026-06-26 14:34:37` | `cowrie.command.input` |
| `2026-06-26 14:34:37` | `cowrie.log.closed` |
| `2026-06-26 14:34:39` | `cowrie.session.params` |
| `2026-06-26 14:34:39` | `cowrie.command.input` |
| `2026-06-26 14:34:39` | `cowrie.command.input` |
| `2026-06-26 14:34:39` | `cowrie.command.failed` |
| `2026-06-26 14:34:39` | `cowrie.command.failed` |
| `2026-06-26 14:34:39` | `cowrie.command.failed` |
| `2026-06-26 14:34:39` | `cowrie.command.failed` |
| `2026-06-26 14:34:39` | `cowrie.log.closed` |
| `2026-06-26 14:34:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb6db76be6ea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:34 |
| **Last Seen** | 2026-06-26 14:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:34:49` | `cowrie.session.connect` |
| `2026-06-26 14:34:49` | `cowrie.client.version` |
| `2026-06-26 14:34:49` | `cowrie.client.kex` |
| `2026-06-26 14:34:49` | `cowrie.login.success` |
| `2026-06-26 14:34:50` | `cowrie.session.params` |
| `2026-06-26 14:34:50` | `cowrie.command.input` |
| `2026-06-26 14:34:50` | `cowrie.log.closed` |
| `2026-06-26 14:34:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36d33fdb1d1d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:35 |
| **Last Seen** | 2026-06-26 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:35:42` | `cowrie.session.connect` |
| `2026-06-26 14:35:42` | `cowrie.client.version` |
| `2026-06-26 14:35:43` | `cowrie.client.kex` |
| `2026-06-26 14:35:43` | `cowrie.login.success` |
| `2026-06-26 14:35:44` | `cowrie.session.params` |
| `2026-06-26 14:35:44` | `cowrie.command.input` |
| `2026-06-26 14:35:44` | `cowrie.log.closed` |
| `2026-06-26 14:35:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c774ec2f613d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-06-26 14:35 |
| **Last Seen** | 2026-06-26 14:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123456789' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:35:47` | `cowrie.session.connect` |
| `2026-06-26 14:35:47` | `cowrie.client.version` |
| `2026-06-26 14:35:47` | `cowrie.client.kex` |
| `2026-06-26 14:35:48` | `cowrie.login.success` |
| `2026-06-26 14:35:50` | `cowrie.session.params` |
| `2026-06-26 14:35:50` | `cowrie.command.input` |
| `2026-06-26 14:35:50` | `cowrie.command.input` |
| `2026-06-26 14:35:50` | `cowrie.command.input` |
| `2026-06-26 14:35:50` | `cowrie.command.input` |
| `2026-06-26 14:35:50` | `cowrie.log.closed` |
| `2026-06-26 14:35:52` | `cowrie.session.params` |
| `2026-06-26 14:35:52` | `cowrie.command.input` |
| `2026-06-26 14:35:52` | `cowrie.command.input` |
| `2026-06-26 14:35:52` | `cowrie.command.failed` |
| `2026-06-26 14:35:52` | `cowrie.command.failed` |
| `2026-06-26 14:35:52` | `cowrie.command.failed` |
| `2026-06-26 14:35:52` | `cowrie.command.failed` |
| `2026-06-26 14:35:52` | `cowrie.log.closed` |
| `2026-06-26 14:35:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ed9fa34ac66

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:36 |
| **Last Seen** | 2026-06-26 14:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:36:38` | `cowrie.session.connect` |
| `2026-06-26 14:36:38` | `cowrie.client.version` |
| `2026-06-26 14:36:38` | `cowrie.client.kex` |
| `2026-06-26 14:36:39` | `cowrie.login.success` |
| `2026-06-26 14:36:40` | `cowrie.session.params` |
| `2026-06-26 14:36:40` | `cowrie.command.input` |
| `2026-06-26 14:36:40` | `cowrie.log.closed` |
| `2026-06-26 14:36:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90c31f3ad2c1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-06-26 14:37 |
| **Last Seen** | 2026-06-26 14:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1q2w3e4r' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:37:02` | `cowrie.session.connect` |
| `2026-06-26 14:37:02` | `cowrie.client.version` |
| `2026-06-26 14:37:02` | `cowrie.client.kex` |
| `2026-06-26 14:37:04` | `cowrie.login.success` |
| `2026-06-26 14:37:05` | `cowrie.session.params` |
| `2026-06-26 14:37:05` | `cowrie.command.input` |
| `2026-06-26 14:37:05` | `cowrie.command.input` |
| `2026-06-26 14:37:05` | `cowrie.command.input` |
| `2026-06-26 14:37:05` | `cowrie.command.input` |
| `2026-06-26 14:37:06` | `cowrie.log.closed` |
| `2026-06-26 14:37:08` | `cowrie.session.params` |
| `2026-06-26 14:37:08` | `cowrie.command.input` |
| `2026-06-26 14:37:08` | `cowrie.command.input` |
| `2026-06-26 14:37:08` | `cowrie.command.failed` |
| `2026-06-26 14:37:08` | `cowrie.command.failed` |
| `2026-06-26 14:37:08` | `cowrie.command.failed` |
| `2026-06-26 14:37:08` | `cowrie.command.failed` |
| `2026-06-26 14:37:08` | `cowrie.log.closed` |
| `2026-06-26 14:37:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7829c5da0ff0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:37 |
| **Last Seen** | 2026-06-26 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:37:37` | `cowrie.session.connect` |
| `2026-06-26 14:37:37` | `cowrie.client.version` |
| `2026-06-26 14:37:37` | `cowrie.client.kex` |
| `2026-06-26 14:37:38` | `cowrie.login.success` |
| `2026-06-26 14:37:38` | `cowrie.session.params` |
| `2026-06-26 14:37:38` | `cowrie.command.input` |
| `2026-06-26 14:37:39` | `cowrie.log.closed` |
| `2026-06-26 14:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e686b5e89735

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-06-26 14:38 |
| **Last Seen** | 2026-06-26 14:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '654321' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:38:17` | `cowrie.session.connect` |
| `2026-06-26 14:38:18` | `cowrie.client.version` |
| `2026-06-26 14:38:18` | `cowrie.client.kex` |
| `2026-06-26 14:38:19` | `cowrie.login.success` |
| `2026-06-26 14:38:20` | `cowrie.session.params` |
| `2026-06-26 14:38:20` | `cowrie.command.input` |
| `2026-06-26 14:38:20` | `cowrie.command.input` |
| `2026-06-26 14:38:20` | `cowrie.command.input` |
| `2026-06-26 14:38:20` | `cowrie.command.input` |
| `2026-06-26 14:38:21` | `cowrie.log.closed` |
| `2026-06-26 14:38:22` | `cowrie.session.params` |
| `2026-06-26 14:38:22` | `cowrie.command.input` |
| `2026-06-26 14:38:22` | `cowrie.command.input` |
| `2026-06-26 14:38:22` | `cowrie.command.failed` |
| `2026-06-26 14:38:22` | `cowrie.command.failed` |
| `2026-06-26 14:38:22` | `cowrie.command.failed` |
| `2026-06-26 14:38:22` | `cowrie.command.failed` |
| `2026-06-26 14:38:23` | `cowrie.log.closed` |
| `2026-06-26 14:38:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73e0d117d1c4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:38 |
| **Last Seen** | 2026-06-26 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:38:34` | `cowrie.session.connect` |
| `2026-06-26 14:38:34` | `cowrie.client.version` |
| `2026-06-26 14:38:35` | `cowrie.client.kex` |
| `2026-06-26 14:38:35` | `cowrie.login.success` |
| `2026-06-26 14:38:36` | `cowrie.session.params` |
| `2026-06-26 14:38:36` | `cowrie.command.input` |
| `2026-06-26 14:38:36` | `cowrie.log.closed` |
| `2026-06-26 14:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2af213f30492

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:39 |
| **Last Seen** | 2026-06-26 14:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:39:33` | `cowrie.session.connect` |
| `2026-06-26 14:39:33` | `cowrie.client.version` |
| `2026-06-26 14:39:33` | `cowrie.client.kex` |
| `2026-06-26 14:39:33` | `cowrie.login.success` |
| `2026-06-26 14:39:34` | `cowrie.session.params` |
| `2026-06-26 14:39:34` | `cowrie.command.input` |
| `2026-06-26 14:39:34` | `cowrie.log.closed` |
| `2026-06-26 14:39:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f064f2efbf8c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-06-26 14:39 |
| **Last Seen** | 2026-06-26 14:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'P@ssw0rd' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:39:35` | `cowrie.session.connect` |
| `2026-06-26 14:39:35` | `cowrie.client.version` |
| `2026-06-26 14:39:35` | `cowrie.client.kex` |
| `2026-06-26 14:39:37` | `cowrie.login.success` |
| `2026-06-26 14:39:39` | `cowrie.session.params` |
| `2026-06-26 14:39:39` | `cowrie.command.input` |
| `2026-06-26 14:39:39` | `cowrie.command.input` |
| `2026-06-26 14:39:39` | `cowrie.command.input` |
| `2026-06-26 14:39:39` | `cowrie.command.input` |
| `2026-06-26 14:39:39` | `cowrie.log.closed` |
| `2026-06-26 14:39:40` | `cowrie.session.params` |
| `2026-06-26 14:39:40` | `cowrie.command.input` |
| `2026-06-26 14:39:40` | `cowrie.command.input` |
| `2026-06-26 14:39:40` | `cowrie.command.failed` |
| `2026-06-26 14:39:40` | `cowrie.command.failed` |
| `2026-06-26 14:39:40` | `cowrie.command.failed` |
| `2026-06-26 14:39:40` | `cowrie.command.failed` |
| `2026-06-26 14:39:41` | `cowrie.log.closed` |
| `2026-06-26 14:39:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bc2e046a838

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:40 |
| **Last Seen** | 2026-06-26 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:40:30` | `cowrie.session.connect` |
| `2026-06-26 14:40:30` | `cowrie.client.version` |
| `2026-06-26 14:40:30` | `cowrie.client.kex` |
| `2026-06-26 14:40:30` | `cowrie.login.success` |
| `2026-06-26 14:40:31` | `cowrie.session.params` |
| `2026-06-26 14:40:31` | `cowrie.command.input` |
| `2026-06-26 14:40:31` | `cowrie.log.closed` |
| `2026-06-26 14:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e0bc6c598ad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-06-26 14:40 |
| **Last Seen** | 2026-06-26 14:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'admin' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:40:53` | `cowrie.session.connect` |
| `2026-06-26 14:40:53` | `cowrie.client.version` |
| `2026-06-26 14:40:53` | `cowrie.client.kex` |
| `2026-06-26 14:40:55` | `cowrie.login.success` |
| `2026-06-26 14:40:56` | `cowrie.session.params` |
| `2026-06-26 14:40:56` | `cowrie.command.input` |
| `2026-06-26 14:40:56` | `cowrie.command.input` |
| `2026-06-26 14:40:56` | `cowrie.command.input` |
| `2026-06-26 14:40:56` | `cowrie.command.input` |
| `2026-06-26 14:40:58` | `cowrie.log.closed` |
| `2026-06-26 14:41:00` | `cowrie.session.params` |
| `2026-06-26 14:41:00` | `cowrie.command.input` |
| `2026-06-26 14:41:00` | `cowrie.command.input` |
| `2026-06-26 14:41:00` | `cowrie.command.failed` |
| `2026-06-26 14:41:00` | `cowrie.command.failed` |
| `2026-06-26 14:41:00` | `cowrie.command.failed` |
| `2026-06-26 14:41:00` | `cowrie.command.failed` |
| `2026-06-26 14:41:00` | `cowrie.log.closed` |
| `2026-06-26 14:41:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42750ea12e36

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:41 |
| **Last Seen** | 2026-06-26 14:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:41:30` | `cowrie.session.connect` |
| `2026-06-26 14:41:30` | `cowrie.client.version` |
| `2026-06-26 14:41:30` | `cowrie.client.kex` |
| `2026-06-26 14:41:30` | `cowrie.login.success` |
| `2026-06-26 14:41:31` | `cowrie.session.params` |
| `2026-06-26 14:41:31` | `cowrie.command.input` |
| `2026-06-26 14:41:31` | `cowrie.log.closed` |
| `2026-06-26 14:41:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b164d8daedf

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 14:42 |
| **Last Seen** | 2026-06-26 14:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:42:00` | `cowrie.session.connect` |
| `2026-06-26 14:42:00` | `cowrie.client.version` |
| `2026-06-26 14:42:00` | `cowrie.client.kex` |
| `2026-06-26 14:42:02` | `cowrie.login.success` |
| `2026-06-26 14:42:04` | `cowrie.session.params` |
| `2026-06-26 14:42:04` | `cowrie.command.input` |
| `2026-06-26 14:42:04` | `cowrie.log.closed` |
| `2026-06-26 14:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bf26013e238

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-06-26 14:42 |
| **Last Seen** | 2026-06-26 14:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'admin123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:42:11` | `cowrie.session.connect` |
| `2026-06-26 14:42:12` | `cowrie.client.version` |
| `2026-06-26 14:42:12` | `cowrie.client.kex` |
| `2026-06-26 14:42:13` | `cowrie.login.success` |
| `2026-06-26 14:42:15` | `cowrie.session.params` |
| `2026-06-26 14:42:15` | `cowrie.command.input` |
| `2026-06-26 14:42:15` | `cowrie.command.input` |
| `2026-06-26 14:42:15` | `cowrie.command.input` |
| `2026-06-26 14:42:15` | `cowrie.command.input` |
| `2026-06-26 14:42:16` | `cowrie.log.closed` |
| `2026-06-26 14:42:17` | `cowrie.session.params` |
| `2026-06-26 14:42:17` | `cowrie.command.input` |
| `2026-06-26 14:42:17` | `cowrie.command.input` |
| `2026-06-26 14:42:17` | `cowrie.command.failed` |
| `2026-06-26 14:42:17` | `cowrie.command.failed` |
| `2026-06-26 14:42:17` | `cowrie.command.failed` |
| `2026-06-26 14:42:17` | `cowrie.command.failed` |
| `2026-06-26 14:42:18` | `cowrie.log.closed` |
| `2026-06-26 14:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd6f69b8a3a1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 14:42 |
| **Last Seen** | 2026-06-26 14:42 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:42:12` | `cowrie.session.connect` |
| `2026-06-26 14:42:15` | `cowrie.client.version` |
| `2026-06-26 14:42:15` | `cowrie.client.kex` |
| `2026-06-26 14:42:22` | `cowrie.login.success` |
| `2026-06-26 14:42:25` | `cowrie.session.params` |
| `2026-06-26 14:42:25` | `cowrie.command.input` |
| `2026-06-26 14:42:26` | `cowrie.log.closed` |
| `2026-06-26 14:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-576b9dd89927

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:42 |
| **Last Seen** | 2026-06-26 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:42:28` | `cowrie.session.connect` |
| `2026-06-26 14:42:28` | `cowrie.client.version` |
| `2026-06-26 14:42:28` | `cowrie.client.kex` |
| `2026-06-26 14:42:29` | `cowrie.login.success` |
| `2026-06-26 14:42:30` | `cowrie.session.params` |
| `2026-06-26 14:42:30` | `cowrie.command.input` |
| `2026-06-26 14:42:30` | `cowrie.log.closed` |
| `2026-06-26 14:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-849844d9bce5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:43 |
| **Last Seen** | 2026-06-26 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:43:25` | `cowrie.session.connect` |
| `2026-06-26 14:43:25` | `cowrie.client.version` |
| `2026-06-26 14:43:25` | `cowrie.client.kex` |
| `2026-06-26 14:43:25` | `cowrie.login.success` |
| `2026-06-26 14:43:26` | `cowrie.session.params` |
| `2026-06-26 14:43:26` | `cowrie.command.input` |
| `2026-06-26 14:43:26` | `cowrie.log.closed` |
| `2026-06-26 14:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb5866da89c5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-06-26 14:43 |
| **Last Seen** | 2026-06-26 14:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'passw0rd' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:43:29` | `cowrie.session.connect` |
| `2026-06-26 14:43:29` | `cowrie.client.version` |
| `2026-06-26 14:43:29` | `cowrie.client.kex` |
| `2026-06-26 14:43:31` | `cowrie.login.success` |
| `2026-06-26 14:43:32` | `cowrie.session.params` |
| `2026-06-26 14:43:32` | `cowrie.command.input` |
| `2026-06-26 14:43:32` | `cowrie.command.input` |
| `2026-06-26 14:43:32` | `cowrie.command.input` |
| `2026-06-26 14:43:32` | `cowrie.command.input` |
| `2026-06-26 14:43:33` | `cowrie.log.closed` |
| `2026-06-26 14:43:34` | `cowrie.session.params` |
| `2026-06-26 14:43:34` | `cowrie.command.input` |
| `2026-06-26 14:43:34` | `cowrie.command.input` |
| `2026-06-26 14:43:34` | `cowrie.command.failed` |
| `2026-06-26 14:43:34` | `cowrie.command.failed` |
| `2026-06-26 14:43:34` | `cowrie.command.failed` |
| `2026-06-26 14:43:34` | `cowrie.command.failed` |
| `2026-06-26 14:43:35` | `cowrie.log.closed` |
| `2026-06-26 14:43:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0fb3fa5a4a8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:44 |
| **Last Seen** | 2026-06-26 14:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:44:22` | `cowrie.session.connect` |
| `2026-06-26 14:44:22` | `cowrie.client.version` |
| `2026-06-26 14:44:23` | `cowrie.client.kex` |
| `2026-06-26 14:44:23` | `cowrie.login.success` |
| `2026-06-26 14:44:24` | `cowrie.session.params` |
| `2026-06-26 14:44:24` | `cowrie.command.input` |
| `2026-06-26 14:44:24` | `cowrie.log.closed` |
| `2026-06-26 14:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-668d41199280

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-06-26 14:44 |
| **Last Seen** | 2026-06-26 14:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:44:42` | `cowrie.session.connect` |
| `2026-06-26 14:44:42` | `cowrie.client.version` |
| `2026-06-26 14:44:42` | `cowrie.client.kex` |
| `2026-06-26 14:44:44` | `cowrie.login.success` |
| `2026-06-26 14:44:45` | `cowrie.session.params` |
| `2026-06-26 14:44:45` | `cowrie.command.input` |
| `2026-06-26 14:44:45` | `cowrie.command.input` |
| `2026-06-26 14:44:45` | `cowrie.command.input` |
| `2026-06-26 14:44:45` | `cowrie.command.input` |
| `2026-06-26 14:44:45` | `cowrie.log.closed` |
| `2026-06-26 14:44:47` | `cowrie.session.params` |
| `2026-06-26 14:44:47` | `cowrie.command.input` |
| `2026-06-26 14:44:47` | `cowrie.command.input` |
| `2026-06-26 14:44:47` | `cowrie.command.failed` |
| `2026-06-26 14:44:47` | `cowrie.command.failed` |
| `2026-06-26 14:44:47` | `cowrie.command.failed` |
| `2026-06-26 14:44:47` | `cowrie.command.failed` |
| `2026-06-26 14:44:47` | `cowrie.log.closed` |
| `2026-06-26 14:44:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb5c24dd41d3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:45 |
| **Last Seen** | 2026-06-26 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:45:21` | `cowrie.session.connect` |
| `2026-06-26 14:45:21` | `cowrie.client.version` |
| `2026-06-26 14:45:21` | `cowrie.client.kex` |
| `2026-06-26 14:45:21` | `cowrie.login.success` |
| `2026-06-26 14:45:22` | `cowrie.session.params` |
| `2026-06-26 14:45:22` | `cowrie.command.input` |
| `2026-06-26 14:45:22` | `cowrie.log.closed` |
| `2026-06-26 14:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-265910eb353b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-06-26 14:45 |
| **Last Seen** | 2026-06-26 14:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password1' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:45:58` | `cowrie.session.connect` |
| `2026-06-26 14:45:59` | `cowrie.client.version` |
| `2026-06-26 14:45:59` | `cowrie.client.kex` |
| `2026-06-26 14:46:00` | `cowrie.login.success` |
| `2026-06-26 14:46:02` | `cowrie.session.params` |
| `2026-06-26 14:46:02` | `cowrie.command.input` |
| `2026-06-26 14:46:02` | `cowrie.command.input` |
| `2026-06-26 14:46:02` | `cowrie.command.input` |
| `2026-06-26 14:46:02` | `cowrie.command.input` |
| `2026-06-26 14:46:02` | `cowrie.log.closed` |
| `2026-06-26 14:46:04` | `cowrie.session.params` |
| `2026-06-26 14:46:04` | `cowrie.command.input` |
| `2026-06-26 14:46:04` | `cowrie.command.input` |
| `2026-06-26 14:46:04` | `cowrie.command.failed` |
| `2026-06-26 14:46:04` | `cowrie.command.failed` |
| `2026-06-26 14:46:04` | `cowrie.command.failed` |
| `2026-06-26 14:46:04` | `cowrie.command.failed` |
| `2026-06-26 14:46:04` | `cowrie.log.closed` |
| `2026-06-26 14:46:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9699b52a9b0b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:46 |
| **Last Seen** | 2026-06-26 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:46:16` | `cowrie.session.connect` |
| `2026-06-26 14:46:16` | `cowrie.client.version` |
| `2026-06-26 14:46:17` | `cowrie.client.kex` |
| `2026-06-26 14:46:17` | `cowrie.login.success` |
| `2026-06-26 14:46:18` | `cowrie.session.params` |
| `2026-06-26 14:46:18` | `cowrie.command.input` |
| `2026-06-26 14:46:18` | `cowrie.log.closed` |
| `2026-06-26 14:46:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0cc6d953d53

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:47 |
| **Last Seen** | 2026-06-26 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:47:11` | `cowrie.session.connect` |
| `2026-06-26 14:47:11` | `cowrie.client.version` |
| `2026-06-26 14:47:11` | `cowrie.client.kex` |
| `2026-06-26 14:47:11` | `cowrie.login.success` |
| `2026-06-26 14:47:12` | `cowrie.session.params` |
| `2026-06-26 14:47:12` | `cowrie.command.input` |
| `2026-06-26 14:47:12` | `cowrie.log.closed` |
| `2026-06-26 14:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6253d9e8506

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:48 |
| **Last Seen** | 2026-06-26 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:48:06` | `cowrie.session.connect` |
| `2026-06-26 14:48:06` | `cowrie.client.version` |
| `2026-06-26 14:48:06` | `cowrie.client.kex` |
| `2026-06-26 14:48:06` | `cowrie.login.success` |
| `2026-06-26 14:48:07` | `cowrie.session.params` |
| `2026-06-26 14:48:07` | `cowrie.command.input` |
| `2026-06-26 14:48:07` | `cowrie.log.closed` |
| `2026-06-26 14:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-963fed899399

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:49 |
| **Last Seen** | 2026-06-26 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:49:05` | `cowrie.session.connect` |
| `2026-06-26 14:49:05` | `cowrie.client.version` |
| `2026-06-26 14:49:05` | `cowrie.client.kex` |
| `2026-06-26 14:49:05` | `cowrie.login.success` |
| `2026-06-26 14:49:06` | `cowrie.session.params` |
| `2026-06-26 14:49:06` | `cowrie.command.input` |
| `2026-06-26 14:49:06` | `cowrie.log.closed` |
| `2026-06-26 14:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-132b9eeab1dd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:50 |
| **Last Seen** | 2026-06-26 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:50:06` | `cowrie.session.connect` |
| `2026-06-26 14:50:06` | `cowrie.client.version` |
| `2026-06-26 14:50:06` | `cowrie.client.kex` |
| `2026-06-26 14:50:07` | `cowrie.login.success` |
| `2026-06-26 14:50:08` | `cowrie.session.params` |
| `2026-06-26 14:50:08` | `cowrie.command.input` |
| `2026-06-26 14:50:08` | `cowrie.log.closed` |
| `2026-06-26 14:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-640f0a123cdd

| Field | Detail |
|---|---|
| **Source IP** | `185.182.186[.]243` |
| **First Seen** | 2026-06-26 14:50 |
| **Last Seen** | 2026-06-26 14:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:50:29` | `cowrie.session.connect` |
| `2026-06-26 14:50:29` | `cowrie.client.version` |
| `2026-06-26 14:50:29` | `cowrie.client.kex` |
| `2026-06-26 14:50:29` | `cowrie.login.success` |
| `2026-06-26 14:50:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.182.186[.]243` to AbuseIPDB if not already reported
- [ ] Block `185.182.186[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-661730051667

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-26 14:50 |
| **Last Seen** | 2026-06-26 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:50:30` | `cowrie.session.connect` |
| `2026-06-26 14:50:30` | `cowrie.client.version` |
| `2026-06-26 14:50:30` | `cowrie.client.kex` |
| `2026-06-26 14:50:30` | `cowrie.login.success` |
| `2026-06-26 14:50:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d54cba396b6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:51 |
| **Last Seen** | 2026-06-26 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:51:07` | `cowrie.session.connect` |
| `2026-06-26 14:51:07` | `cowrie.client.version` |
| `2026-06-26 14:51:07` | `cowrie.client.kex` |
| `2026-06-26 14:51:07` | `cowrie.login.success` |
| `2026-06-26 14:51:08` | `cowrie.session.params` |
| `2026-06-26 14:51:08` | `cowrie.command.input` |
| `2026-06-26 14:51:08` | `cowrie.log.closed` |
| `2026-06-26 14:51:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d87c88f568a9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:52 |
| **Last Seen** | 2026-06-26 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:52:09` | `cowrie.session.connect` |
| `2026-06-26 14:52:09` | `cowrie.client.version` |
| `2026-06-26 14:52:09` | `cowrie.client.kex` |
| `2026-06-26 14:52:09` | `cowrie.login.success` |
| `2026-06-26 14:52:10` | `cowrie.session.params` |
| `2026-06-26 14:52:10` | `cowrie.command.input` |
| `2026-06-26 14:52:10` | `cowrie.log.closed` |
| `2026-06-26 14:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d5c6856bd53

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:53 |
| **Last Seen** | 2026-06-26 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:53:07` | `cowrie.session.connect` |
| `2026-06-26 14:53:07` | `cowrie.client.version` |
| `2026-06-26 14:53:07` | `cowrie.client.kex` |
| `2026-06-26 14:53:07` | `cowrie.login.success` |
| `2026-06-26 14:53:08` | `cowrie.session.params` |
| `2026-06-26 14:53:08` | `cowrie.command.input` |
| `2026-06-26 14:53:08` | `cowrie.log.closed` |
| `2026-06-26 14:53:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9860dd50686a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]239` |
| **First Seen** | 2026-06-26 14:53 |
| **Last Seen** | 2026-06-26 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:53:33` | `cowrie.session.connect` |
| `2026-06-26 14:53:33` | `cowrie.client.version` |
| `2026-06-26 14:53:33` | `cowrie.client.kex` |
| `2026-06-26 14:53:33` | `cowrie.login.success` |
| `2026-06-26 14:53:34` | `cowrie.session.params` |
| `2026-06-26 14:53:34` | `cowrie.command.input` |
| `2026-06-26 14:53:34` | `cowrie.log.closed` |
| `2026-06-26 14:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]239` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e020b1bf3929

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 14:53 |
| **Last Seen** | 2026-06-26 14:53 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:53:43` | `cowrie.session.connect` |
| `2026-06-26 14:53:44` | `cowrie.client.version` |
| `2026-06-26 14:53:44` | `cowrie.client.kex` |
| `2026-06-26 14:53:50` | `cowrie.login.success` |
| `2026-06-26 14:53:53` | `cowrie.session.params` |
| `2026-06-26 14:53:53` | `cowrie.command.input` |
| `2026-06-26 14:53:54` | `cowrie.log.closed` |
| `2026-06-26 14:53:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f89c84f08af

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 14:54 |
| **Last Seen** | 2026-06-26 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 14:54:04` | `cowrie.session.connect` |
| `2026-06-26 14:54:04` | `cowrie.client.version` |
| `2026-06-26 14:54:04` | `cowrie.client.kex` |
| `2026-06-26 14:54:04` | `cowrie.login.success` |
| `2026-06-26 14:54:05` | `cowrie.session.params` |
| `2026-06-26 14:54:05` | `cowrie.command.input` |
| `2026-06-26 14:54:05` | `cowrie.log.closed` |
| `2026-06-26 14:54:05` | `cowrie.session.closed` |

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
| `209.99.185[.]59` | **235** | 2026-06-26 10:55 | 2026-06-26 14:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `159.65.233[.]253` | **5** | 2026-06-26 11:25 | 2026-06-26 13:14 | 4m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **4** | 2026-06-26 11:46 | 2026-06-26 14:46 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `58.42.204[.]29` | **3** | 2026-06-26 12:43 | 2026-06-26 12:45 | 4m | 0 | `T1592` | 🟢 LOW |
| `101.96.234[.]229` | **2** | 2026-06-26 12:10 | 2026-06-26 12:12 | 2m | 0 | `T1592` | 🟢 LOW |
| `64.89.162[.]15` | **2** | 2026-06-26 11:45 | 2026-06-26 11:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]57` | **2** | 2026-06-26 14:17 | 2026-06-26 14:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]71` | **2** | 2026-06-26 14:33 | 2026-06-26 14:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]176` | **2** | 2026-06-26 11:59 | 2026-06-26 12:15 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.92.40[.]7` | **2** | 2026-06-26 14:22 | 2026-06-26 14:33 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `152.42.196[.]93` | 1 | 2026-06-26 13:20 | 2026-06-26 13:20 | 2s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]79` | 1 | 2026-06-26 10:56 | 2026-06-26 10:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]80` | 1 | 2026-06-26 12:32 | 2026-06-26 12:32 | 12s | 0 | `T1592` | 🟢 LOW |
| `216.70.97[.]74` | 1 | 2026-06-26 10:58 | 2026-06-26 10:58 | 30s | 0 | `T1592` | 🟢 LOW |
| `220.197.14[.]60` | 1 | 2026-06-26 14:09 | 2026-06-26 14:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `223.84.195[.]56` | 1 | 2026-06-26 14:14 | 2026-06-26 14:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.173.18[.]65` | 1 | 2026-06-26 11:18 | 2026-06-26 11:18 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-06-26 13:02 | 2026-06-26 13:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-06-26 14:52 | 2026-06-26 14:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.126.16[.]66` | 1 | 2026-06-26 14:38 | 2026-06-26 14:39 | 30s | 0 | `T1592` | 🟢 LOW |
| `60.188.249[.]64` | 1 | 2026-06-26 14:55 | 2026-06-26 14:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]202` | 1 | 2026-06-26 11:10 | 2026-06-26 11:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]38` | 1 | 2026-06-26 12:23 | 2026-06-26 12:24 | 15s | 0 | `T1592` | 🟢 LOW |
| `68.183.30[.]24` | 1 | 2026-06-26 13:39 | 2026-06-26 13:39 | 1s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-06-26 14:45 | 2026-06-26 14:46 | 7s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 61/100 | 🟡 MEDIUM | **3/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 47/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 40/100 | 🟡 MEDIUM | 0/75 ✅ |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 44/100 | 🟡 MEDIUM | **11/75** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 48/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 48/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 45/100 | 🟡 MEDIUM | **14/75** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
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
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8` | ELF Binary (Linux executable) (MIPS 32-bit) | `cc653189103bd14e...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d0f5cafd9fb6a363a8b97c84a3546f601a4ba10d49cdd7dae418288caec6940b` | ELF Binary (Linux executable) (x86 32-bit) | `d0f5cafd9fb6a363...` | 46/100 | 🟡 MEDIUM | **17/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318` | Unknown binary | `ea73a088909b5311...` | 55/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `eaf9adb4bb80316a3aafceabc0f2ed2aed7c76cf134b9b7c66226fc4f003aa97` | ELF Binary (Linux executable) (x86-64 64-bit) | `eaf9adb4bb80316a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `f11dd1e4a3d27eef85d44154d662ce94234ee71b54468aeb2c23edb30b74a5c5` | ELF Binary (Linux executable) (x86-64 64-bit) | `f11dd1e4a3d27eef...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |

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
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `39.173.18[.]65` | CN | China Mobile Communications Corporation | **100** ⚠️ | 16 |
| `188.166.183[.]133` | SG | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `185.182.186[.]243` | FR | Contabo GmbH | **100** ⚠️ | 9 |
| `216.70.97[.]74` | US | GoDaddy.com, LLC | **100** ⚠️ | 6 |
| `47.77.182[.]54` | US | Alibaba Cloud LLC | **100** ⚠️ | 50 |
| `58.42.204[.]29` | CN | CHINANET Guizhou province network | **100** ⚠️ | 50 |
| `101.96.234[.]229` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 12 |
| `85.217.149[.]71` | CA | NL MODAT | **100** ⚠️ | 50 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 357 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 328 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 33 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 33 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 6 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 16 below threshold 25 | 4 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 617 cases |
| Tool 34  | Credential Extractor        | ✅ 345 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 42 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (2.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 42 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 328 priority case(s) shown individually · 25 recon entry/entries in table (10 group(s) consolidating 259 session(s)).

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
_Report time: 2026-06-26T16:20:59Z_

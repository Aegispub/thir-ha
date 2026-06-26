# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-26 |
| **Generated At** | 2026-06-26T12:14:09Z |
| **Shift Time** | 12:14 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **526** |
| Confirmed Threats | **519** |
| False Positives Filtered | **7** (1.3%) |
| Unique Attacker IPs | **33** |
| Countries of Origin | **10** |
| High Severity Cases | **361** |
| Medium Severity Cases | **1** |
| Low Severity Cases | **164** |
| Malware Samples Analyzed | **5** HIGH · **42** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **366** |
| Unique Credential Pairs | **346** |
| Unique Usernames | **173** |
| Unique Passwords | **259** |
| Successful Auth Pairs | **359** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 118 |
| `admin` | 15 |
| `ubuntu` | 7 |
| `user` | 5 |
| `deploy` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 19 |
| `1234` | 12 |
| `123` | 9 |
| `password` | 8 |
| `root` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 6 |
| `root` | `123@@@` | 4 |
| `root` | `smo@@kkklss` | 4 |
| `admin` | `admin` | 4 |
| `daniel` | `daniel` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `changeme` | `91.92.40.171` | 2026-06-26T08:55:08 |
| `root` | `root@1234` | `91.92.40.171` | 2026-06-26T08:55:14 |
| `root` | `password` | `91.92.40.171` | 2026-06-26T08:55:20 |
| `lighthouse` | `lighthouse` | `91.92.40.171` | 2026-06-26T08:55:25 |
| `minecraft` | `123` | `91.92.40.171` | 2026-06-26T08:55:30 |
| `systemd` | `1q2w3e4r` | `91.92.40.171` | 2026-06-26T08:55:36 |
| `vpn` | `vpn` | `91.92.40.171` | 2026-06-26T08:55:41 |
| `sofyan` | `sofyan123` | `209.99.185.59` | 2026-06-26T08:55:43 |
| `vncuser` | `password` | `91.92.40.171` | 2026-06-26T08:55:47 |
| `root` | `1q2w3e4r5t6y` | `91.92.40.171` | 2026-06-26T08:55:52 |
| `root` | `111` | `91.92.40.171` | 2026-06-26T08:55:58 |
| `deployer` | `dev` | `91.92.40.171` | 2026-06-26T08:56:03 |
| `root` | `123321` | `91.92.40.171` | 2026-06-26T08:56:08 |
| `main` | `1234` | `91.92.40.171` | 2026-06-26T08:56:14 |
| `gd` | `gd` | `91.92.40.171` | 2026-06-26T08:56:20 |
| `dev` | `dev` | `91.92.40.171` | 2026-06-26T08:56:25 |
| `odoo17` | `12345` | `91.92.40.171` | 2026-06-26T08:56:31 |
| `ftp` | `changeme` | `209.99.185.59` | 2026-06-26T08:56:36 |
| `odoo14` | `odoo` | `91.92.40.171` | 2026-06-26T08:56:37 |
| `btc` | `btc` | `91.92.40.171` | 2026-06-26T08:56:42 |
| `admin` | `abc123` | `91.92.40.171` | 2026-06-26T08:56:47 |
| `fivem` | `12345` | `91.92.40.171` | 2026-06-26T08:56:53 |
| `root` | `1qazXSW@` | `91.92.40.171` | 2026-06-26T08:56:59 |
| `alex` | `alex` | `91.92.40.171` | 2026-06-26T08:57:04 |
| `centreon` | `centreon` | `91.92.40.171` | 2026-06-26T08:57:09 |
| `root` | `Huawei123` | `91.92.40.171` | 2026-06-26T08:57:15 |
| `calvin` | `calvin` | `91.92.40.171` | 2026-06-26T08:57:21 |
| `user` | `user1234` | `91.92.40.171` | 2026-06-26T08:57:26 |
| `root` | `p@ssw0rd` | `91.92.40.171` | 2026-06-26T08:57:32 |
| `root` | `t` | `209.99.185.59` | 2026-06-26T08:57:34 |
| `admin` | `1qaz@WSX` | `91.92.40.171` | 2026-06-26T08:57:37 |
| `potok` | `potok` | `91.92.40.171` | 2026-06-26T08:57:43 |
| `root` | `admin123` | `91.92.40.171` | 2026-06-26T08:57:49 |
| `student` | `password` | `91.92.40.171` | 2026-06-26T08:57:55 |
| `root` | `123123` | `91.92.40.171` | 2026-06-26T08:58:00 |
| `chris` | `123456` | `91.92.40.171` | 2026-06-26T08:58:05 |
| `root` | `asdfasdf-space` | `91.92.40.171` | 2026-06-26T08:58:11 |
| `prem` | `12345` | `91.92.40.171` | 2026-06-26T08:58:17 |
| `user3` | `1` | `91.92.40.171` | 2026-06-26T08:58:22 |
| `downloader` | `222222` | `209.99.185.59` | 2026-06-26T08:58:27 |
| `niaoyun` | `123456` | `91.92.40.171` | 2026-06-26T08:58:28 |
| `teste` | `teste` | `91.92.40.171` | 2026-06-26T08:58:32 |
| `hduser` | `hduser` | `91.92.40.171` | 2026-06-26T08:58:38 |
| `adminuser` | `123456` | `91.92.40.171` | 2026-06-26T08:58:43 |
| `appuser` | `appuser` | `91.92.40.171` | 2026-06-26T08:58:48 |
| `admin` | `root` | `91.92.40.171` | 2026-06-26T08:58:54 |
| `sftpuser` | `123` | `91.92.40.171` | 2026-06-26T08:58:59 |
| `support` | `123` | `91.92.40.171` | 2026-06-26T08:59:04 |
| `ubuntu` | `A123456a` | `91.92.40.171` | 2026-06-26T08:59:10 |
| `newuser` | `123` | `91.92.40.171` | 2026-06-26T08:59:15 |
| `home` | `home` | `91.92.40.171` | 2026-06-26T08:59:20 |
| `dmdba` | `dmdba` | `209.99.185.59` | 2026-06-26T08:59:21 |
| `root` | `hello123` | `91.92.40.171` | 2026-06-26T08:59:26 |
| `master` | `123` | `91.92.40.171` | 2026-06-26T08:59:31 |
| `alex` | `1234` | `91.92.40.171` | 2026-06-26T08:59:37 |
| `gateway` | `gateway` | `91.92.40.171` | 2026-06-26T08:59:43 |
| `david` | `david` | `91.92.40.171` | 2026-06-26T08:59:48 |
| `fa` | `fa` | `91.92.40.171` | 2026-06-26T08:59:53 |
| `root` | `P@ssword1` | `91.92.40.171` | 2026-06-26T08:59:59 |
| `ftpuser` | `123456789` | `91.92.40.171` | 2026-06-26T09:00:04 |
| `daniel` | `daniel` | `45.198.224.120` | 2026-06-26T09:00:10 |
| `avax` | `avax` | `91.92.40.171` | 2026-06-26T09:00:10 |
| `dev` | `123321` | `91.92.40.171` | 2026-06-26T09:00:15 |
| `zcc` | `zcczcc` | `209.99.185.59` | 2026-06-26T09:00:16 |
| `root` | `Admin@123` | `91.92.40.171` | 2026-06-26T09:00:21 |
| `rocky` | `1234` | `91.92.40.171` | 2026-06-26T09:00:27 |
| `username` | `passwd` | `91.92.40.171` | 2026-06-26T09:00:32 |
| `admin123` | `1234` | `91.92.40.171` | 2026-06-26T09:00:37 |
| `dev` | `123` | `91.92.40.171` | 2026-06-26T09:00:43 |
| `media` | `media` | `91.92.40.171` | 2026-06-26T09:00:48 |
| `web` | `web123` | `91.92.40.171` | 2026-06-26T09:00:54 |
| `oscar` | `1234` | `91.92.40.171` | 2026-06-26T09:00:59 |
| `root` | `Admin@123456` | `91.92.40.171` | 2026-06-26T09:01:05 |
| `admin1` | `redhat` | `91.92.40.171` | 2026-06-26T09:01:10 |
| `root` | `1qazxsw2` | `209.99.185.59` | 2026-06-26T09:01:12 |
| `root` | `qwe123!@` | `91.92.40.171` | 2026-06-26T09:01:16 |
| `support` | `support` | `91.92.40.171` | 2026-06-26T09:01:21 |
| `root` | `zaq12wsx` | `91.92.40.171` | 2026-06-26T09:01:27 |
| `guest` | `pi` | `91.92.40.171` | 2026-06-26T09:01:32 |
| `guest` | `guest` | `91.92.40.171` | 2026-06-26T09:01:38 |
| `ec2-user` | `12345678` | `91.92.40.171` | 2026-06-26T09:01:43 |
| `fivem` | `password` | `91.92.40.171` | 2026-06-26T09:01:48 |
| `fred` | `fred` | `91.92.40.171` | 2026-06-26T09:01:54 |
| `admin` | `E4IuG88G` | `91.92.40.171` | 2026-06-26T09:02:00 |
| `root` | `pass` | `91.92.40.171` | 2026-06-26T09:02:05 |
| `root` | `9ijn` | `209.99.185.59` | 2026-06-26T09:02:06 |
| `chenxi` | `123456` | `91.92.40.171` | 2026-06-26T09:02:10 |
| `server` | `123456` | `91.92.40.171` | 2026-06-26T09:02:16 |
| `manoj` | `manoj123` | `91.92.40.171` | 2026-06-26T09:02:21 |
| `root` | `qazwsxedc` | `91.92.40.171` | 2026-06-26T09:02:27 |
| `admin` | `admin123` | `91.92.40.171` | 2026-06-26T09:02:33 |
| `root` | `1qaz2wsx` | `91.92.40.171` | 2026-06-26T09:02:39 |
| `root` | `123abc456` | `91.92.40.171` | 2026-06-26T09:02:44 |
| `root` | `P@55w0rd` | `91.92.40.171` | 2026-06-26T09:02:49 |
| `kali` | `kali` | `91.92.40.171` | 2026-06-26T09:02:55 |
| `rg` | `123456` | `209.99.185.59` | 2026-06-26T09:03:00 |
| `odoo16` | `odoo16` | `91.92.40.171` | 2026-06-26T09:03:01 |
| `deploy` | `1234` | `91.92.40.171` | 2026-06-26T09:03:06 |
| `es` | `123456` | `91.92.40.171` | 2026-06-26T09:03:12 |
| `pi` | `root` | `91.92.40.171` | 2026-06-26T09:03:17 |
| `debian` | `qwerty` | `91.92.40.171` | 2026-06-26T09:03:23 |
| `jenkins` | `jenkins` | `91.92.40.171` | 2026-06-26T09:03:28 |
| `admin1` | `admin1` | `91.92.40.171` | 2026-06-26T09:03:34 |
| `root` | `ubuntu` | `91.92.40.171` | 2026-06-26T09:03:39 |
| `daniel` | `daniel` | `91.92.40.171` | 2026-06-26T09:03:45 |
| `deploy` | `123123` | `91.92.40.171` | 2026-06-26T09:03:51 |
| `zhangsan` | `zhangsan123` | `209.99.185.59` | 2026-06-26T09:03:54 |
| `root` | `Aa@123456` | `91.92.40.171` | 2026-06-26T09:03:57 |
| `runner` | `1234` | `91.92.40.171` | 2026-06-26T09:04:02 |
| `root` | `12345qwert` | `91.92.40.171` | 2026-06-26T09:04:08 |
| `root` | `aa123456` | `91.92.40.171` | 2026-06-26T09:04:14 |
| `openclaw` | `123456` | `91.92.40.171` | 2026-06-26T09:04:20 |
| `milad` | `milad` | `91.92.40.171` | 2026-06-26T09:04:25 |
| `pi` | `1` | `91.92.40.171` | 2026-06-26T09:04:31 |
| `git` | `123456` | `91.92.40.171` | 2026-06-26T09:04:37 |
| `bob` | `root` | `91.92.40.171` | 2026-06-26T09:04:42 |
| `cw` | `cw` | `91.92.40.171` | 2026-06-26T09:04:48 |
| `root` | `qmailr` | `209.99.185.59` | 2026-06-26T09:04:49 |
| `test` | `1234qwer` | `91.92.40.171` | 2026-06-26T09:04:55 |
| `ansible` | `ansible` | `91.92.40.171` | 2026-06-26T09:05:00 |
| `user` | `12345` | `91.92.40.171` | 2026-06-26T09:05:05 |
| `username` | `123456` | `91.92.40.171` | 2026-06-26T09:05:11 |
| `azureuser` | `root` | `91.92.40.171` | 2026-06-26T09:05:17 |
| `airflow` | `airflow` | `91.92.40.171` | 2026-06-26T09:05:22 |
| `ossuser` | `Changeme_123` | `91.92.40.171` | 2026-06-26T09:05:28 |
| `user2` | `user2` | `91.92.40.171` | 2026-06-26T09:05:33 |
| `user` | `rootroot` | `91.92.40.171` | 2026-06-26T09:05:38 |
| `nagios` | `p@ssw0rd` | `209.99.185.59` | 2026-06-26T09:05:44 |
| `adminuser` | `adminuser` | `91.92.40.171` | 2026-06-26T09:05:44 |
| `bot` | `123456` | `91.92.40.171` | 2026-06-26T09:05:50 |
| `user` | `root` | `91.92.40.171` | 2026-06-26T09:05:55 |
| `steam` | `1` | `91.92.40.171` | 2026-06-26T09:06:01 |
| `root` | `Ac123456` | `91.92.40.171` | 2026-06-26T09:06:07 |
| `docker` | `docker123` | `91.92.40.171` | 2026-06-26T09:06:12 |
| `root` | `P@ssw0rd2026` | `91.92.40.171` | 2026-06-26T09:06:18 |
| `root` | `linux` | `91.92.40.171` | 2026-06-26T09:06:24 |
| `crafty` | `crafty` | `91.92.40.171` | 2026-06-26T09:06:29 |
| `admin` | `P@ssw0rd` | `91.92.40.171` | 2026-06-26T09:06:35 |
| `dmzhang_01` | `dmzhang_01` | `209.99.185.59` | 2026-06-26T09:06:40 |
| `root` | `11111111` | `91.92.40.171` | 2026-06-26T09:06:41 |
| `root` | `CatCult2025!` | `91.92.40.171` | 2026-06-26T09:06:46 |
| `oracle` | `Aa123456` | `91.92.40.171` | 2026-06-26T09:06:52 |
| `ubuntu` | `123456789` | `91.92.40.171` | 2026-06-26T09:06:58 |
| `claude` | `abc123` | `91.92.40.171` | 2026-06-26T09:07:04 |
| `devops` | `123456789` | `91.92.40.171` | 2026-06-26T09:07:10 |
| `cloud` | `cloud123!` | `91.92.40.171` | 2026-06-26T09:07:15 |
| `ubuntu` | `qweewq123` | `45.205.1.42` | 2026-06-26T09:07:20 |
| `root` | `Yun@wocloud.szkj` | `91.92.40.171` | 2026-06-26T09:07:21 |
| `bob` | `1234` | `91.92.40.171` | 2026-06-26T09:07:27 |
| `support` | `Passw0rd` | `91.92.40.171` | 2026-06-26T09:07:32 |
| `dell` | `dell@444` | `209.99.185.59` | 2026-06-26T09:07:37 |
| `amin` | `amin` | `91.92.40.171` | 2026-06-26T09:07:38 |
| `odoo17` | `odoo` | `91.92.40.171` | 2026-06-26T09:07:44 |
| `system` | `system` | `91.92.40.171` | 2026-06-26T09:07:49 |
| `root` | `r00t` | `91.92.40.171` | 2026-06-26T09:07:55 |
| `cursor` | `cursor` | `91.92.40.171` | 2026-06-26T09:08:00 |
| `sonar` | `sonar` | `91.92.40.171` | 2026-06-26T09:08:06 |
| `test2` | `test2` | `91.92.40.171` | 2026-06-26T09:08:12 |
| `security` | `security` | `91.92.40.171` | 2026-06-26T09:08:18 |
| `root` | `null` | `91.92.40.171` | 2026-06-26T09:08:24 |
| `aiuser` | `aiuser` | `91.92.40.171` | 2026-06-26T09:08:29 |
| `fastuser` | `123456789` | `91.92.40.171` | 2026-06-26T09:08:34 |
| `ydkwon` | `1234` | `209.99.185.59` | 2026-06-26T09:08:35 |
| `frappe` | `frappe` | `91.92.40.171` | 2026-06-26T09:08:40 |
| `root` | `!Q@W3e4r` | `91.92.40.171` | 2026-06-26T09:08:46 |
| `user10` | `user10` | `91.92.40.171` | 2026-06-26T09:08:52 |
| `stack` | `stack` | `91.92.40.171` | 2026-06-26T09:08:58 |
| `username` | `user` | `91.92.40.171` | 2026-06-26T09:09:03 |
| `sam` | `sam` | `91.92.40.171` | 2026-06-26T09:09:09 |
| `deploy` | `user` | `91.92.40.171` | 2026-06-26T09:09:14 |
| `root1` | `root1` | `91.92.40.171` | 2026-06-26T09:09:20 |
| `runner` | `root` | `91.92.40.171` | 2026-06-26T09:09:26 |
| `root1` | `123456` | `91.92.40.171` | 2026-06-26T09:09:32 |
| `jianqiangtong` | `jianqiangtong` | `209.99.185.59` | 2026-06-26T09:09:32 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-26T09:09:33 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-26T09:09:33 |
| `coder` | `123456` | `91.92.40.171` | 2026-06-26T09:09:37 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-26T09:09:43 |
| `tester` | `tester` | `91.92.40.171` | 2026-06-26T09:09:43 |
| `mysql` | `mysql@1234` | `91.92.40.171` | 2026-06-26T09:09:49 |
| `postgres` | `password` | `91.92.40.171` | 2026-06-26T09:09:55 |
| `bot` | `bot` | `91.92.40.171` | 2026-06-26T09:10:00 |
| `minecraft` | `minecraft` | `91.92.40.171` | 2026-06-26T09:10:06 |
| `root` | `dxfUgwfiNcx8` | `91.92.40.171` | 2026-06-26T09:10:11 |
| `deployer` | `123456` | `91.92.40.171` | 2026-06-26T09:10:17 |
| `root` | `Abcd1234` | `91.92.40.171` | 2026-06-26T09:10:23 |
| `nlp` | `nlp` | `209.99.185.59` | 2026-06-26T09:10:27 |
| `admin` | `123123` | `91.92.40.171` | 2026-06-26T09:10:29 |
| `admin` | `111` | `91.92.40.171` | 2026-06-26T09:10:33 |
| `user3` | `user3` | `91.92.40.171` | 2026-06-26T09:10:39 |
| `odoo18` | `odoo` | `91.92.40.171` | 2026-06-26T09:10:45 |
| `localhost` | `localhost` | `91.92.40.171` | 2026-06-26T09:10:50 |
| `deploy` | `deploy123` | `91.92.40.171` | 2026-06-26T09:10:56 |
| `devops` | `1234` | `91.92.40.171` | 2026-06-26T09:11:01 |
| `xiao` | `xiao` | `91.92.40.171` | 2026-06-26T09:11:07 |
| `root` | `123qwe!@` | `91.92.40.171` | 2026-06-26T09:11:13 |
| `claude` | `1234` | `91.92.40.171` | 2026-06-26T09:11:18 |
| `chiye` | `chiye` | `45.198.224.120` | 2026-06-26T09:11:22 |
| `dolphinscheduler` | `dolphinscheduler` | `91.92.40.171` | 2026-06-26T09:11:24 |
| `root` | `idc@123` | `209.99.185.59` | 2026-06-26T09:11:26 |
| `root` | `1qazxsw2` | `91.92.40.171` | 2026-06-26T09:11:30 |
| `guest` | `111111` | `91.92.40.171` | 2026-06-26T09:11:35 |
| `ansible` | `qwerty` | `91.92.40.171` | 2026-06-26T09:11:41 |
| `user` | `user` | `91.92.40.171` | 2026-06-26T09:11:47 |
| `sysupdate` | `123456` | `91.92.40.171` | 2026-06-26T09:11:52 |
| `bot` | `abc123` | `91.92.40.171` | 2026-06-26T09:11:58 |
| `sdadmin` | `51nGleD` | `91.92.40.171` | 2026-06-26T09:12:03 |
| `odoo18` | `123` | `91.92.40.171` | 2026-06-26T09:12:09 |
| `root` | `741852963` | `91.92.40.171` | 2026-06-26T09:12:15 |
| `root` | `abc123` | `91.92.40.171` | 2026-06-26T09:12:20 |
| `root` | `Wcs123!@###` | `209.99.185.59` | 2026-06-26T09:12:23 |
| `ftpuser` | `ftpuser123` | `91.92.40.171` | 2026-06-26T09:12:26 |
| `git` | `123` | `91.92.40.171` | 2026-06-26T09:12:32 |
| `user1` | `123456789` | `91.92.40.171` | 2026-06-26T09:12:37 |
| `runner` | `test` | `91.92.40.171` | 2026-06-26T09:12:43 |
| `clawdbot` | `clawdbot` | `91.92.40.171` | 2026-06-26T09:12:49 |
| `user2` | `1` | `91.92.40.171` | 2026-06-26T09:12:54 |
| `admin` | `admin123!` | `91.92.40.171` | 2026-06-26T09:12:59 |
| `root` | `eve` | `91.92.40.171` | 2026-06-26T09:13:05 |
| `root` | `Abc12345` | `91.92.40.171` | 2026-06-26T09:13:11 |
| `webuser` | `webuser` | `91.92.40.171` | 2026-06-26T09:13:16 |
| `mysql` | `12345678` | `209.99.185.59` | 2026-06-26T09:13:22 |
| `root` | `z` | `209.99.185.59` | 2026-06-26T09:14:20 |
| `admin` | `admin` | `47.253.156.31` | 2026-06-26T09:14:32 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-26T09:14:33 |
| `root` | `Server123` | `209.99.185.59` | 2026-06-26T09:15:22 |
| `yaozhao` | `Fh3.1416` | `209.99.185.59` | 2026-06-26T09:16:20 |
| `ubuntu` | `upload123` | `209.99.185.59` | 2026-06-26T09:17:17 |
| `vps` | `pass123` | `209.99.185.59` | 2026-06-26T09:18:15 |
| `root` | `nasa` | `209.99.185.59` | 2026-06-26T09:19:13 |
| `centos` | `111111` | `209.99.185.59` | 2026-06-26T09:20:12 |
| `root` | `p@ss1234` | `209.99.185.59` | 2026-06-26T09:21:11 |
| `jhon` | `123456` | `209.99.185.59` | 2026-06-26T09:22:09 |
| `dingy` | `dingy@123` | `209.99.185.59` | 2026-06-26T09:23:07 |
| `device` | `qwerty123` | `209.99.185.59` | 2026-06-26T09:24:08 |
| `root` | `Pa$$w0rd444` | `45.205.1.42` | 2026-06-26T09:24:42 |
| `root` | `1000` | `209.99.185.59` | 2026-06-26T09:25:10 |
| `root` | `qwerT1234%` | `209.99.185.59` | 2026-06-26T09:26:11 |
| `root` | `qwe123,./` | `45.198.224.120` | 2026-06-26T09:26:25 |
| `buero3` | `buero3321` | `209.99.185.59` | 2026-06-26T09:27:12 |
| `peer` | `peer321` | `209.99.185.59` | 2026-06-26T09:28:11 |
| `root` | `P@ss1` | `209.99.185.59` | 2026-06-26T09:29:10 |
| `nagios` | `Pa55w0rd` | `209.99.185.59` | 2026-06-26T09:30:10 |
| `gitlab` | `12345678` | `209.99.185.59` | 2026-06-26T09:31:10 |
| `student1` | `password` | `209.99.185.59` | 2026-06-26T09:32:13 |
| `daiyx` | `NEWPASS123` | `209.99.185.59` | 2026-06-26T09:33:18 |
| `ubuntu` | `user123456789` | `209.99.185.59` | 2026-06-26T09:34:20 |
| `lqj` | `lqj` | `209.99.185.59` | 2026-06-26T09:35:25 |
| `zhaoq` | `zq123` | `209.99.185.59` | 2026-06-26T09:36:28 |
| `duyanjun` | `123456Dyj` | `209.99.185.59` | 2026-06-26T09:37:32 |
| `root` | `Password1234` | `45.198.224.120` | 2026-06-26T09:37:33 |
| `root` | `Surt!b@zarSql123` | `209.99.185.59` | 2026-06-26T09:38:35 |
| `liuyang` | `liuyang` | `45.205.1.42` | 2026-06-26T09:38:39 |
| `developer` | `password` | `209.99.185.59` | 2026-06-26T09:39:38 |
| `root` | `Aa123456789@` | `209.99.185.59` | 2026-06-26T09:40:40 |
| `root` | `Demo@123` | `209.99.185.59` | 2026-06-26T09:41:47 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-26T09:42:04 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-26T09:42:04 |
| `git` | `321` | `209.99.185.59` | 2026-06-26T09:42:51 |
| `plex` | `plex` | `209.99.185.59` | 2026-06-26T09:43:53 |
| `root` | `china@123` | `209.99.185.59` | 2026-06-26T09:44:59 |
| `jiadong` | `123456` | `209.99.185.59` | 2026-06-26T09:46:09 |
| `root` | `1mobile` | `209.99.185.59` | 2026-06-26T09:47:17 |
| `root` | `P@ssw0rd2012` | `45.198.224.120` | 2026-06-26T09:48:18 |
| `root` | `Root!@#2021` | `209.99.185.59` | 2026-06-26T09:48:22 |
| `root` | `Qwer1234!@#$` | `209.99.185.59` | 2026-06-26T09:49:27 |
| `admin` | `admin` | `141.11.88.108` | 2026-06-26T09:50:26 |
| `kai` | `kai` | `209.99.185.59` | 2026-06-26T09:50:35 |
| `admin` | `admin` | `45.225.135.21` | 2026-06-26T09:51:02 |
| `pul` | `P@ssw0rd` | `209.99.185.59` | 2026-06-26T09:51:41 |
| `postgres` | `Postgres@123` | `209.99.185.59` | 2026-06-26T09:52:46 |
| `postgres` | `qwer` | `45.205.1.42` | 2026-06-26T09:52:54 |
| `root` | `Huawei@5tgb` | `209.99.185.59` | 2026-06-26T09:53:54 |
| `root` | `k` | `209.99.185.59` | 2026-06-26T09:55:01 |
| `root` | `Admin12345` | `209.99.185.59` | 2026-06-26T09:56:09 |
| `ansible` | `ansible@123` | `209.99.185.59` | 2026-06-26T09:57:16 |
| `root` | `postgres0123` | `209.99.185.59` | 2026-06-26T09:58:26 |
| `root` | `admin1234` | `45.198.224.120` | 2026-06-26T09:58:56 |
| `root` | `Sugon@123` | `209.99.185.59` | 2026-06-26T09:59:37 |
| `datasave` | `ds123` | `209.99.185.59` | 2026-06-26T10:00:35 |
| `root` | `giuseppe` | `209.99.185.59` | 2026-06-26T10:01:18 |
| `root` | `Ducati916795513+` | `209.99.185.59` | 2026-06-26T10:02:04 |
| `netika` | `netika` | `209.99.185.59` | 2026-06-26T10:02:53 |
| `root` | `admin@#` | `209.99.185.59` | 2026-06-26T10:03:44 |
| `root` | `Qwer1` | `209.99.185.59` | 2026-06-26T10:05:15 |
| `students` | `students` | `209.99.185.59` | 2026-06-26T10:05:59 |
| `buero3` | `666666` | `209.99.185.59` | 2026-06-26T10:06:45 |
| `root` | `qw123456` | `45.205.1.42` | 2026-06-26T10:07:11 |
| `root` | `JaymzH` | `209.99.185.59` | 2026-06-26T10:07:29 |
| `chenhui` | `N2DbqkAeZx` | `209.99.185.59` | 2026-06-26T10:08:13 |
| `omnisky` | `iiau123` | `209.99.185.59` | 2026-06-26T10:09:01 |
| `pepper` | `pepper` | `45.198.224.120` | 2026-06-26T10:09:32 |
| `goodwe` | `Goodwe123` | `209.99.185.59` | 2026-06-26T10:09:55 |
| `root` | `a1` | `209.99.185.59` | 2026-06-26T10:10:44 |
| `root` | `123456abc` | `209.99.185.59` | 2026-06-26T10:11:34 |
| `root` | `alexa` | `209.99.185.59` | 2026-06-26T10:12:22 |
| `downloader` | `111111` | `209.99.185.59` | 2026-06-26T10:13:07 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-06-26T10:13:09 |
| `root` | `123@@@` | `165.1.75.106` | 2026-06-26T10:13:09 |
| `Phoenix` | `iRST2vXIA7` | `209.99.185.59` | 2026-06-26T10:13:52 |
| `bod_6` | `bod_6` | `209.99.185.59` | 2026-06-26T10:14:37 |
| `mysql` | `11111111` | `209.99.185.59` | 2026-06-26T10:15:24 |
| `news` | `1234` | `209.99.185.59` | 2026-06-26T10:16:14 |
| `dima` | `dima111111` | `209.99.185.59` | 2026-06-26T10:17:02 |
| `tomcat` | `tomcat123` | `209.99.185.59` | 2026-06-26T10:17:50 |
| `dmdba` | `1qaz2wsx` | `209.99.185.59` | 2026-06-26T10:18:38 |
| `b'\x16\x03\x03\x02c\x01\x00\x02_\x03\x03\x1d\xc9\xe7\x131\xd3a/\xb9\xc4-\x00a\x87\x01\x9b\xa2\x11\xbd\xe4\xe4'` | `b'B\x0b?=\xe1B\xf4\xd0\xaf$ \xde\xfd,\tc\x13\xfd\xbe\xe3\x17\xc3\x80\xaf6\xda\xad\x1cv\xc8\xde.+j\xaf/2\x91\xcf:7\x17"\x00\x8a\x00\x16\x003\x00g\xc0\x9e\xc0\xa2\x00\x9e\x009\x00k\xc0\x9f\xc0\xa3\x00\x9f\x00E\x00\xbe\x00\x88\x00\xc4\x00\x9a\xc0\x08\xc0\t\xc0#\xc0\xac\xc0\xae\xc0+\xc0'` | `195.184.76.236` | 2026-06-26T10:18:39 |
| `b"\xc0$\xc0\xad\xc0\xaf\xc0,\xc0r\xc0s\xcc\xa9\x13\x02\x13\x01\xcc\x14\xc0\x07\xc0\x12\xc0\x13\xc0'\xc0/\xc0\x14\xc0(\xc00\xc0`\xc0a\xc0v\xc0w\xcc\xa8\x13\x05\x13\x04\x13\x03\xcc\x13\xc0\x11\x00"` | `b'\x00/\x00<\xc0\x9c\xc0\xa0\x00\x9c\x005\x00=\xc0\x9d\xc0\xa1\x00\x9d\x00A\x00\xba\x00\x84\x00\xc0\x00\x07\x00\x04\x00\x05\x01\x00\x01\x8c\x00\x00\x00\x13\x00\x11\x00\x00\x0e129.80.119.236\x00\x0b\x00\x04\x03\x00\x01\x02\x00'` | `195.184.76.236` | 2026-06-26T10:18:39 |
| `  ` | `      #               0 .	` | `195.184.76.236` | 2026-06-26T10:18:39 |
| `root` | `corredoresJ1824` | `209.99.185.59` | 2026-06-26T10:19:25 |
| `ubuntu` | `admin123456` | `45.198.224.120` | 2026-06-26T10:20:07 |
| `root` | `a1b23c` | `209.99.185.59` | 2026-06-26T10:20:12 |
| `root` | `ProxyPass` | `209.99.185.59` | 2026-06-26T10:21:01 |
| `exploit` | `arbus8` | `45.205.1.42` | 2026-06-26T10:21:43 |
| `root` | `6655321` | `209.99.185.59` | 2026-06-26T10:21:53 |
| `jglee` | `jglee` | `209.99.185.59` | 2026-06-26T10:22:46 |
| `redmine` | `password` | `209.99.185.59` | 2026-06-26T10:23:38 |
| `oracle` | `123$%^` | `209.99.185.59` | 2026-06-26T10:24:28 |
| `ftp` | `ftp` | `209.99.185.59` | 2026-06-26T10:25:17 |
| `root` | `asd1234567890` | `209.99.185.59` | 2026-06-26T10:26:07 |
| `root` | `Lightning@123` | `209.99.185.59` | 2026-06-26T10:26:57 |
| `lilong` | `123456` | `209.99.185.59` | 2026-06-26T10:27:46 |
| `yunyang` | `31415926` | `209.99.185.59` | 2026-06-26T10:28:36 |
| `root` | `2wsx1qaz!` | `209.99.185.59` | 2026-06-26T10:29:27 |
| `root` | `PassWord` | `209.99.185.59` | 2026-06-26T10:30:18 |
| `root` | `qazxcv!@#` | `45.198.224.120` | 2026-06-26T10:30:42 |
| `mobile` | `mobile` | `209.99.185.59` | 2026-06-26T10:31:09 |
| `root` | `888` | `209.99.185.59` | 2026-06-26T10:32:04 |
| `caja25liberar` | `caja25liberar` | `209.99.185.59` | 2026-06-26T10:33:00 |
| `sfy` | `fengjia1314` | `209.99.185.59` | 2026-06-26T10:33:52 |
| `mobile` | `mobile@1234` | `209.99.185.59` | 2026-06-26T10:34:47 |
| `root` | `Password#12` | `209.99.185.59` | 2026-06-26T10:35:42 |
| `root` | `P@ssw0rd2012` | `45.205.1.42` | 2026-06-26T10:36:08 |
| `web` | `abc123` | `209.99.185.59` | 2026-06-26T10:36:36 |
| `student` | `student` | `209.99.185.59` | 2026-06-26T10:37:31 |
| `root` | `liverovast#adkz443` | `209.99.185.59` | 2026-06-26T10:38:29 |
| `root` | `qwe789` | `209.99.185.59` | 2026-06-26T10:39:23 |
| `vadim` | `vadim` | `209.99.185.59` | 2026-06-26T10:40:18 |
| `web` | `web123` | `45.198.224.120` | 2026-06-26T10:41:07 |
| `zabbix` | `abc123` | `209.99.185.59` | 2026-06-26T10:41:15 |
| `haowang` | `haowang` | `209.99.185.59` | 2026-06-26T10:42:14 |
| `tong` | `tong111111` | `209.99.185.59` | 2026-06-26T10:43:14 |
| `guo` | `guo` | `209.99.185.59` | 2026-06-26T10:44:09 |
| `test` | `1` | `209.99.185.59` | 2026-06-26T10:45:06 |
| `root` | `Admin@4444` | `209.99.185.59` | 2026-06-26T10:46:01 |
| `jenkins` | `jenkins` | `209.99.185.59` | 2026-06-26T10:47:00 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-26T10:47:10 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-26T10:47:10 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-26T10:47:14 |
| `root` | `m@ils3rv3r` | `209.99.185.59` | 2026-06-26T10:47:57 |
| `root` | `P@ssworD` | `209.99.185.59` | 2026-06-26T10:48:54 |
| `wallet` | `123456` | `209.99.185.59` | 2026-06-26T10:49:50 |
| `ubuntu` | `000` | `45.205.1.42` | 2026-06-26T10:50:30 |
| `huawei` | `Huawei123` | `209.99.185.59` | 2026-06-26T10:50:47 |
| `ex11` | `123` | `209.99.185.59` | 2026-06-26T10:51:42 |
| `root` | `qsQq#3Mx` | `45.198.224.120` | 2026-06-26T10:52:10 |
| `root` | `1QaZ2WsX` | `209.99.185.59` | 2026-06-26T10:52:39 |
| `confluence4` | `confluence4` | `209.99.185.59` | 2026-06-26T10:53:39 |
| `root` | `QAZ@12` | `209.99.185.59` | 2026-06-26T10:54:38 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **526** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 354 |
| Paramiko (Python) | 14 |
| libssh | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 196 | 1 |
| `16443846184e...` | Generic scanner | 146 | 3 |
| `a2de0f306611...` | Mirai/variant | 14 | 4 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |
| `19532158b559...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 196 | 1 | Generic scanner |
| `16443846184e...` | Go SSH scanner | 146 | 3 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 14 | 4 | Mirai/variant |
| `95420f9d932d...` | Go SSH scanner | 7 | 4 | — |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
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
| Total IPs Analysed | **33** |
| Unique ASNs | **24** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS213412` | ONYPHE SAS | 2 | HIGH |
| `AS58461` | CT HangZhou IDC | 1 | HIGH |
| `AS58224` | Iran Telecommunication Company PJS | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (362)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-23ca17c0eaee

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:55 |
| **Last Seen** | 2026-06-26 08:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:55:07` | `cowrie.session.connect` |
| `2026-06-26 08:55:07` | `cowrie.client.version` |
| `2026-06-26 08:55:07` | `cowrie.client.kex` |
| `2026-06-26 08:55:08` | `cowrie.login.success` |
| `2026-06-26 08:55:09` | `cowrie.session.params` |
| `2026-06-26 08:55:09` | `cowrie.command.input` |
| `2026-06-26 08:55:10` | `cowrie.log.closed` |
| `2026-06-26 08:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb5cb9387d07

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:55 |
| **Last Seen** | 2026-06-26 08:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:55:13` | `cowrie.session.connect` |
| `2026-06-26 08:55:13` | `cowrie.client.version` |
| `2026-06-26 08:55:13` | `cowrie.client.kex` |
| `2026-06-26 08:55:14` | `cowrie.login.success` |
| `2026-06-26 08:55:15` | `cowrie.session.params` |
| `2026-06-26 08:55:15` | `cowrie.command.input` |
| `2026-06-26 08:55:15` | `cowrie.log.closed` |
| `2026-06-26 08:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f81802e32c4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:55 |
| **Last Seen** | 2026-06-26 08:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:55:18` | `cowrie.session.connect` |
| `2026-06-26 08:55:19` | `cowrie.client.version` |
| `2026-06-26 08:55:19` | `cowrie.client.kex` |
| `2026-06-26 08:55:20` | `cowrie.login.success` |
| `2026-06-26 08:55:21` | `cowrie.session.params` |
| `2026-06-26 08:55:21` | `cowrie.command.input` |
| `2026-06-26 08:55:21` | `cowrie.log.closed` |
| `2026-06-26 08:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f7f552d66ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:55 |
| **Last Seen** | 2026-06-26 08:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:55:24` | `cowrie.session.connect` |
| `2026-06-26 08:55:24` | `cowrie.client.version` |
| `2026-06-26 08:55:24` | `cowrie.client.kex` |
| `2026-06-26 08:55:25` | `cowrie.login.success` |
| `2026-06-26 08:55:25` | `cowrie.session.params` |
| `2026-06-26 08:55:25` | `cowrie.command.input` |
| `2026-06-26 08:55:26` | `cowrie.log.closed` |
| `2026-06-26 08:55:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1918742dc4de

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:55 |
| **Last Seen** | 2026-06-26 08:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:55:30` | `cowrie.session.connect` |
| `2026-06-26 08:55:30` | `cowrie.client.version` |
| `2026-06-26 08:55:30` | `cowrie.client.kex` |
| `2026-06-26 08:55:30` | `cowrie.login.success` |
| `2026-06-26 08:55:31` | `cowrie.session.params` |
| `2026-06-26 08:55:31` | `cowrie.command.input` |
| `2026-06-26 08:55:32` | `cowrie.log.closed` |
| `2026-06-26 08:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-224a852ebaf7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:55 |
| **Last Seen** | 2026-06-26 08:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:55:35` | `cowrie.session.connect` |
| `2026-06-26 08:55:35` | `cowrie.client.version` |
| `2026-06-26 08:55:35` | `cowrie.client.kex` |
| `2026-06-26 08:55:36` | `cowrie.login.success` |
| `2026-06-26 08:55:37` | `cowrie.session.params` |
| `2026-06-26 08:55:37` | `cowrie.command.input` |
| `2026-06-26 08:55:37` | `cowrie.log.closed` |
| `2026-06-26 08:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c7c92318fa6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:55 |
| **Last Seen** | 2026-06-26 08:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:55:41` | `cowrie.session.connect` |
| `2026-06-26 08:55:41` | `cowrie.client.version` |
| `2026-06-26 08:55:41` | `cowrie.client.kex` |
| `2026-06-26 08:55:41` | `cowrie.login.success` |
| `2026-06-26 08:55:42` | `cowrie.session.params` |
| `2026-06-26 08:55:42` | `cowrie.command.input` |
| `2026-06-26 08:55:42` | `cowrie.log.closed` |
| `2026-06-26 08:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-012b6f65dd10

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 08:55 |
| **Last Seen** | 2026-06-26 08:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:55:42` | `cowrie.session.connect` |
| `2026-06-26 08:55:42` | `cowrie.client.version` |
| `2026-06-26 08:55:43` | `cowrie.client.kex` |
| `2026-06-26 08:55:43` | `cowrie.login.success` |
| `2026-06-26 08:55:44` | `cowrie.session.params` |
| `2026-06-26 08:55:44` | `cowrie.command.input` |
| `2026-06-26 08:55:44` | `cowrie.log.closed` |
| `2026-06-26 08:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbe660bb9927

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:55 |
| **Last Seen** | 2026-06-26 08:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:55:46` | `cowrie.session.connect` |
| `2026-06-26 08:55:46` | `cowrie.client.version` |
| `2026-06-26 08:55:46` | `cowrie.client.kex` |
| `2026-06-26 08:55:47` | `cowrie.login.success` |
| `2026-06-26 08:55:48` | `cowrie.session.params` |
| `2026-06-26 08:55:48` | `cowrie.command.input` |
| `2026-06-26 08:55:48` | `cowrie.log.closed` |
| `2026-06-26 08:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ab57f70c6fe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:55 |
| **Last Seen** | 2026-06-26 08:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:55:52` | `cowrie.session.connect` |
| `2026-06-26 08:55:52` | `cowrie.client.version` |
| `2026-06-26 08:55:52` | `cowrie.client.kex` |
| `2026-06-26 08:55:52` | `cowrie.login.success` |
| `2026-06-26 08:55:53` | `cowrie.session.params` |
| `2026-06-26 08:55:53` | `cowrie.command.input` |
| `2026-06-26 08:55:53` | `cowrie.log.closed` |
| `2026-06-26 08:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3e0b334cca0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:55 |
| **Last Seen** | 2026-06-26 08:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:55:57` | `cowrie.session.connect` |
| `2026-06-26 08:55:57` | `cowrie.client.version` |
| `2026-06-26 08:55:57` | `cowrie.client.kex` |
| `2026-06-26 08:55:58` | `cowrie.login.success` |
| `2026-06-26 08:55:59` | `cowrie.session.params` |
| `2026-06-26 08:55:59` | `cowrie.command.input` |
| `2026-06-26 08:55:59` | `cowrie.log.closed` |
| `2026-06-26 08:55:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1bd4901e34d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:56 |
| **Last Seen** | 2026-06-26 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:56:02` | `cowrie.session.connect` |
| `2026-06-26 08:56:02` | `cowrie.client.version` |
| `2026-06-26 08:56:03` | `cowrie.client.kex` |
| `2026-06-26 08:56:03` | `cowrie.login.success` |
| `2026-06-26 08:56:04` | `cowrie.session.params` |
| `2026-06-26 08:56:04` | `cowrie.command.input` |
| `2026-06-26 08:56:04` | `cowrie.log.closed` |
| `2026-06-26 08:56:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfa0b79355bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:56 |
| **Last Seen** | 2026-06-26 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:56:08` | `cowrie.session.connect` |
| `2026-06-26 08:56:08` | `cowrie.client.version` |
| `2026-06-26 08:56:08` | `cowrie.client.kex` |
| `2026-06-26 08:56:08` | `cowrie.login.success` |
| `2026-06-26 08:56:09` | `cowrie.session.params` |
| `2026-06-26 08:56:09` | `cowrie.command.input` |
| `2026-06-26 08:56:10` | `cowrie.log.closed` |
| `2026-06-26 08:56:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36980d288770

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:56 |
| **Last Seen** | 2026-06-26 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:56:14` | `cowrie.session.connect` |
| `2026-06-26 08:56:14` | `cowrie.client.version` |
| `2026-06-26 08:56:14` | `cowrie.client.kex` |
| `2026-06-26 08:56:14` | `cowrie.login.success` |
| `2026-06-26 08:56:15` | `cowrie.session.params` |
| `2026-06-26 08:56:15` | `cowrie.command.input` |
| `2026-06-26 08:56:15` | `cowrie.log.closed` |
| `2026-06-26 08:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39b27438a62c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:56 |
| **Last Seen** | 2026-06-26 08:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:56:19` | `cowrie.session.connect` |
| `2026-06-26 08:56:19` | `cowrie.client.version` |
| `2026-06-26 08:56:19` | `cowrie.client.kex` |
| `2026-06-26 08:56:20` | `cowrie.login.success` |
| `2026-06-26 08:56:21` | `cowrie.session.params` |
| `2026-06-26 08:56:21` | `cowrie.command.input` |
| `2026-06-26 08:56:21` | `cowrie.log.closed` |
| `2026-06-26 08:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaeb39ab1d44

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:56 |
| **Last Seen** | 2026-06-26 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:56:24` | `cowrie.session.connect` |
| `2026-06-26 08:56:25` | `cowrie.client.version` |
| `2026-06-26 08:56:25` | `cowrie.client.kex` |
| `2026-06-26 08:56:25` | `cowrie.login.success` |
| `2026-06-26 08:56:26` | `cowrie.session.params` |
| `2026-06-26 08:56:26` | `cowrie.command.input` |
| `2026-06-26 08:56:26` | `cowrie.log.closed` |
| `2026-06-26 08:56:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27bb06387780

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:56 |
| **Last Seen** | 2026-06-26 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:56:30` | `cowrie.session.connect` |
| `2026-06-26 08:56:30` | `cowrie.client.version` |
| `2026-06-26 08:56:30` | `cowrie.client.kex` |
| `2026-06-26 08:56:31` | `cowrie.login.success` |
| `2026-06-26 08:56:32` | `cowrie.session.params` |
| `2026-06-26 08:56:32` | `cowrie.command.input` |
| `2026-06-26 08:56:32` | `cowrie.log.closed` |
| `2026-06-26 08:56:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b704a7939326

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 08:56 |
| **Last Seen** | 2026-06-26 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:56:35` | `cowrie.session.connect` |
| `2026-06-26 08:56:35` | `cowrie.client.version` |
| `2026-06-26 08:56:35` | `cowrie.client.kex` |
| `2026-06-26 08:56:36` | `cowrie.login.success` |
| `2026-06-26 08:56:36` | `cowrie.session.params` |
| `2026-06-26 08:56:36` | `cowrie.command.input` |
| `2026-06-26 08:56:36` | `cowrie.log.closed` |
| `2026-06-26 08:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35144dcdc23d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:56 |
| **Last Seen** | 2026-06-26 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:56:36` | `cowrie.session.connect` |
| `2026-06-26 08:56:36` | `cowrie.client.version` |
| `2026-06-26 08:56:36` | `cowrie.client.kex` |
| `2026-06-26 08:56:37` | `cowrie.login.success` |
| `2026-06-26 08:56:38` | `cowrie.session.params` |
| `2026-06-26 08:56:38` | `cowrie.command.input` |
| `2026-06-26 08:56:38` | `cowrie.log.closed` |
| `2026-06-26 08:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a80742479d0f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:56 |
| **Last Seen** | 2026-06-26 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:56:42` | `cowrie.session.connect` |
| `2026-06-26 08:56:42` | `cowrie.client.version` |
| `2026-06-26 08:56:42` | `cowrie.client.kex` |
| `2026-06-26 08:56:42` | `cowrie.login.success` |
| `2026-06-26 08:56:43` | `cowrie.session.params` |
| `2026-06-26 08:56:43` | `cowrie.command.input` |
| `2026-06-26 08:56:43` | `cowrie.log.closed` |
| `2026-06-26 08:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5e90789a031

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:56 |
| **Last Seen** | 2026-06-26 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:56:47` | `cowrie.session.connect` |
| `2026-06-26 08:56:47` | `cowrie.client.version` |
| `2026-06-26 08:56:47` | `cowrie.client.kex` |
| `2026-06-26 08:56:47` | `cowrie.login.success` |
| `2026-06-26 08:56:49` | `cowrie.session.params` |
| `2026-06-26 08:56:49` | `cowrie.command.input` |
| `2026-06-26 08:56:49` | `cowrie.log.closed` |
| `2026-06-26 08:56:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaff62929729

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:56 |
| **Last Seen** | 2026-06-26 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:56:52` | `cowrie.session.connect` |
| `2026-06-26 08:56:52` | `cowrie.client.version` |
| `2026-06-26 08:56:53` | `cowrie.client.kex` |
| `2026-06-26 08:56:53` | `cowrie.login.success` |
| `2026-06-26 08:56:54` | `cowrie.session.params` |
| `2026-06-26 08:56:54` | `cowrie.command.input` |
| `2026-06-26 08:56:54` | `cowrie.log.closed` |
| `2026-06-26 08:56:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e779ec1256ef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:56 |
| **Last Seen** | 2026-06-26 08:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:56:58` | `cowrie.session.connect` |
| `2026-06-26 08:56:58` | `cowrie.client.version` |
| `2026-06-26 08:56:58` | `cowrie.client.kex` |
| `2026-06-26 08:56:59` | `cowrie.login.success` |
| `2026-06-26 08:57:00` | `cowrie.session.params` |
| `2026-06-26 08:57:00` | `cowrie.command.input` |
| `2026-06-26 08:57:00` | `cowrie.log.closed` |
| `2026-06-26 08:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e3e74aed700

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:57 |
| **Last Seen** | 2026-06-26 08:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:57:03` | `cowrie.session.connect` |
| `2026-06-26 08:57:03` | `cowrie.client.version` |
| `2026-06-26 08:57:03` | `cowrie.client.kex` |
| `2026-06-26 08:57:04` | `cowrie.login.success` |
| `2026-06-26 08:57:06` | `cowrie.session.params` |
| `2026-06-26 08:57:06` | `cowrie.command.input` |
| `2026-06-26 08:57:06` | `cowrie.log.closed` |
| `2026-06-26 08:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a9f2bc08975

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:57 |
| **Last Seen** | 2026-06-26 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:57:09` | `cowrie.session.connect` |
| `2026-06-26 08:57:09` | `cowrie.client.version` |
| `2026-06-26 08:57:09` | `cowrie.client.kex` |
| `2026-06-26 08:57:09` | `cowrie.login.success` |
| `2026-06-26 08:57:10` | `cowrie.session.params` |
| `2026-06-26 08:57:10` | `cowrie.command.input` |
| `2026-06-26 08:57:11` | `cowrie.log.closed` |
| `2026-06-26 08:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-428a16e8ea1c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:57 |
| **Last Seen** | 2026-06-26 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:57:15` | `cowrie.session.connect` |
| `2026-06-26 08:57:15` | `cowrie.client.version` |
| `2026-06-26 08:57:15` | `cowrie.client.kex` |
| `2026-06-26 08:57:15` | `cowrie.login.success` |
| `2026-06-26 08:57:16` | `cowrie.session.params` |
| `2026-06-26 08:57:16` | `cowrie.command.input` |
| `2026-06-26 08:57:16` | `cowrie.log.closed` |
| `2026-06-26 08:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99d9e7fd6af5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:57 |
| **Last Seen** | 2026-06-26 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:57:20` | `cowrie.session.connect` |
| `2026-06-26 08:57:20` | `cowrie.client.version` |
| `2026-06-26 08:57:20` | `cowrie.client.kex` |
| `2026-06-26 08:57:21` | `cowrie.login.success` |
| `2026-06-26 08:57:22` | `cowrie.session.params` |
| `2026-06-26 08:57:22` | `cowrie.command.input` |
| `2026-06-26 08:57:22` | `cowrie.log.closed` |
| `2026-06-26 08:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f436f69ea51b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:57 |
| **Last Seen** | 2026-06-26 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:57:25` | `cowrie.session.connect` |
| `2026-06-26 08:57:26` | `cowrie.client.version` |
| `2026-06-26 08:57:26` | `cowrie.client.kex` |
| `2026-06-26 08:57:26` | `cowrie.login.success` |
| `2026-06-26 08:57:27` | `cowrie.session.params` |
| `2026-06-26 08:57:27` | `cowrie.command.input` |
| `2026-06-26 08:57:27` | `cowrie.log.closed` |
| `2026-06-26 08:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3b0c13be331

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:57 |
| **Last Seen** | 2026-06-26 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:57:31` | `cowrie.session.connect` |
| `2026-06-26 08:57:31` | `cowrie.client.version` |
| `2026-06-26 08:57:31` | `cowrie.client.kex` |
| `2026-06-26 08:57:32` | `cowrie.login.success` |
| `2026-06-26 08:57:33` | `cowrie.session.params` |
| `2026-06-26 08:57:33` | `cowrie.command.input` |
| `2026-06-26 08:57:33` | `cowrie.log.closed` |
| `2026-06-26 08:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b31ca7e872b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 08:57 |
| **Last Seen** | 2026-06-26 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:57:33` | `cowrie.session.connect` |
| `2026-06-26 08:57:33` | `cowrie.client.version` |
| `2026-06-26 08:57:33` | `cowrie.client.kex` |
| `2026-06-26 08:57:34` | `cowrie.login.success` |
| `2026-06-26 08:57:34` | `cowrie.session.params` |
| `2026-06-26 08:57:34` | `cowrie.command.input` |
| `2026-06-26 08:57:35` | `cowrie.log.closed` |
| `2026-06-26 08:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5b9fa7e4fbe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:57 |
| **Last Seen** | 2026-06-26 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:57:37` | `cowrie.session.connect` |
| `2026-06-26 08:57:37` | `cowrie.client.version` |
| `2026-06-26 08:57:37` | `cowrie.client.kex` |
| `2026-06-26 08:57:37` | `cowrie.login.success` |
| `2026-06-26 08:57:38` | `cowrie.session.params` |
| `2026-06-26 08:57:38` | `cowrie.command.input` |
| `2026-06-26 08:57:38` | `cowrie.log.closed` |
| `2026-06-26 08:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0da8f6a3d065

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:57 |
| **Last Seen** | 2026-06-26 08:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:57:42` | `cowrie.session.connect` |
| `2026-06-26 08:57:43` | `cowrie.client.version` |
| `2026-06-26 08:57:43` | `cowrie.client.kex` |
| `2026-06-26 08:57:43` | `cowrie.login.success` |
| `2026-06-26 08:57:44` | `cowrie.session.params` |
| `2026-06-26 08:57:44` | `cowrie.command.input` |
| `2026-06-26 08:57:45` | `cowrie.log.closed` |
| `2026-06-26 08:57:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f24307874b3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:57 |
| **Last Seen** | 2026-06-26 08:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:57:48` | `cowrie.session.connect` |
| `2026-06-26 08:57:48` | `cowrie.client.version` |
| `2026-06-26 08:57:48` | `cowrie.client.kex` |
| `2026-06-26 08:57:49` | `cowrie.login.success` |
| `2026-06-26 08:57:50` | `cowrie.session.params` |
| `2026-06-26 08:57:50` | `cowrie.command.input` |
| `2026-06-26 08:57:50` | `cowrie.log.closed` |
| `2026-06-26 08:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe4fe2327c60

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:57 |
| **Last Seen** | 2026-06-26 08:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:57:53` | `cowrie.session.connect` |
| `2026-06-26 08:57:54` | `cowrie.client.version` |
| `2026-06-26 08:57:54` | `cowrie.client.kex` |
| `2026-06-26 08:57:55` | `cowrie.login.success` |
| `2026-06-26 08:57:57` | `cowrie.session.params` |
| `2026-06-26 08:57:57` | `cowrie.command.input` |
| `2026-06-26 08:57:57` | `cowrie.log.closed` |
| `2026-06-26 08:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f923a464d2d7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:57 |
| **Last Seen** | 2026-06-26 08:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:57:59` | `cowrie.session.connect` |
| `2026-06-26 08:57:59` | `cowrie.client.version` |
| `2026-06-26 08:57:59` | `cowrie.client.kex` |
| `2026-06-26 08:58:00` | `cowrie.login.success` |
| `2026-06-26 08:58:01` | `cowrie.session.params` |
| `2026-06-26 08:58:01` | `cowrie.command.input` |
| `2026-06-26 08:58:01` | `cowrie.log.closed` |
| `2026-06-26 08:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15c01b8f03d9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:58 |
| **Last Seen** | 2026-06-26 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:58:05` | `cowrie.session.connect` |
| `2026-06-26 08:58:05` | `cowrie.client.version` |
| `2026-06-26 08:58:05` | `cowrie.client.kex` |
| `2026-06-26 08:58:05` | `cowrie.login.success` |
| `2026-06-26 08:58:06` | `cowrie.session.params` |
| `2026-06-26 08:58:06` | `cowrie.command.input` |
| `2026-06-26 08:58:06` | `cowrie.log.closed` |
| `2026-06-26 08:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea8a47023e30

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:58 |
| **Last Seen** | 2026-06-26 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:58:11` | `cowrie.session.connect` |
| `2026-06-26 08:58:11` | `cowrie.client.version` |
| `2026-06-26 08:58:11` | `cowrie.client.kex` |
| `2026-06-26 08:58:11` | `cowrie.login.success` |
| `2026-06-26 08:58:12` | `cowrie.session.params` |
| `2026-06-26 08:58:12` | `cowrie.command.input` |
| `2026-06-26 08:58:12` | `cowrie.log.closed` |
| `2026-06-26 08:58:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19bddf74bed8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:58 |
| **Last Seen** | 2026-06-26 08:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:58:16` | `cowrie.session.connect` |
| `2026-06-26 08:58:16` | `cowrie.client.version` |
| `2026-06-26 08:58:16` | `cowrie.client.kex` |
| `2026-06-26 08:58:17` | `cowrie.login.success` |
| `2026-06-26 08:58:18` | `cowrie.session.params` |
| `2026-06-26 08:58:18` | `cowrie.command.input` |
| `2026-06-26 08:58:18` | `cowrie.log.closed` |
| `2026-06-26 08:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cf1925a05ae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:58 |
| **Last Seen** | 2026-06-26 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:58:21` | `cowrie.session.connect` |
| `2026-06-26 08:58:21` | `cowrie.client.version` |
| `2026-06-26 08:58:21` | `cowrie.client.kex` |
| `2026-06-26 08:58:22` | `cowrie.login.success` |
| `2026-06-26 08:58:23` | `cowrie.session.params` |
| `2026-06-26 08:58:23` | `cowrie.command.input` |
| `2026-06-26 08:58:23` | `cowrie.log.closed` |
| `2026-06-26 08:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b4e1b136883

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:58 |
| **Last Seen** | 2026-06-26 08:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:58:26` | `cowrie.session.connect` |
| `2026-06-26 08:58:27` | `cowrie.client.version` |
| `2026-06-26 08:58:27` | `cowrie.client.kex` |
| `2026-06-26 08:58:28` | `cowrie.login.success` |
| `2026-06-26 08:58:29` | `cowrie.session.params` |
| `2026-06-26 08:58:29` | `cowrie.command.input` |
| `2026-06-26 08:58:29` | `cowrie.log.closed` |
| `2026-06-26 08:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd9bcfbfc34e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 08:58 |
| **Last Seen** | 2026-06-26 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:58:27` | `cowrie.session.connect` |
| `2026-06-26 08:58:27` | `cowrie.client.version` |
| `2026-06-26 08:58:27` | `cowrie.client.kex` |
| `2026-06-26 08:58:27` | `cowrie.login.success` |
| `2026-06-26 08:58:28` | `cowrie.session.params` |
| `2026-06-26 08:58:28` | `cowrie.command.input` |
| `2026-06-26 08:58:28` | `cowrie.log.closed` |
| `2026-06-26 08:58:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f31932d5577b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:58 |
| **Last Seen** | 2026-06-26 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:58:32` | `cowrie.session.connect` |
| `2026-06-26 08:58:32` | `cowrie.client.version` |
| `2026-06-26 08:58:32` | `cowrie.client.kex` |
| `2026-06-26 08:58:32` | `cowrie.login.success` |
| `2026-06-26 08:58:33` | `cowrie.session.params` |
| `2026-06-26 08:58:33` | `cowrie.command.input` |
| `2026-06-26 08:58:33` | `cowrie.log.closed` |
| `2026-06-26 08:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7550c91f4d7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:58 |
| **Last Seen** | 2026-06-26 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:58:37` | `cowrie.session.connect` |
| `2026-06-26 08:58:37` | `cowrie.client.version` |
| `2026-06-26 08:58:37` | `cowrie.client.kex` |
| `2026-06-26 08:58:38` | `cowrie.login.success` |
| `2026-06-26 08:58:39` | `cowrie.session.params` |
| `2026-06-26 08:58:39` | `cowrie.command.input` |
| `2026-06-26 08:58:39` | `cowrie.log.closed` |
| `2026-06-26 08:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e8085ba0385

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:58 |
| **Last Seen** | 2026-06-26 08:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:58:42` | `cowrie.session.connect` |
| `2026-06-26 08:58:43` | `cowrie.client.version` |
| `2026-06-26 08:58:43` | `cowrie.client.kex` |
| `2026-06-26 08:58:43` | `cowrie.login.success` |
| `2026-06-26 08:58:44` | `cowrie.session.params` |
| `2026-06-26 08:58:44` | `cowrie.command.input` |
| `2026-06-26 08:58:44` | `cowrie.log.closed` |
| `2026-06-26 08:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-996e82597e40

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:58 |
| **Last Seen** | 2026-06-26 08:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:58:48` | `cowrie.session.connect` |
| `2026-06-26 08:58:48` | `cowrie.client.version` |
| `2026-06-26 08:58:48` | `cowrie.client.kex` |
| `2026-06-26 08:58:48` | `cowrie.login.success` |
| `2026-06-26 08:58:49` | `cowrie.session.params` |
| `2026-06-26 08:58:49` | `cowrie.command.input` |
| `2026-06-26 08:58:50` | `cowrie.log.closed` |
| `2026-06-26 08:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-195b712524cd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:58 |
| **Last Seen** | 2026-06-26 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:58:53` | `cowrie.session.connect` |
| `2026-06-26 08:58:53` | `cowrie.client.version` |
| `2026-06-26 08:58:53` | `cowrie.client.kex` |
| `2026-06-26 08:58:54` | `cowrie.login.success` |
| `2026-06-26 08:58:55` | `cowrie.session.params` |
| `2026-06-26 08:58:55` | `cowrie.command.input` |
| `2026-06-26 08:58:55` | `cowrie.log.closed` |
| `2026-06-26 08:58:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa5086e35546

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:58 |
| **Last Seen** | 2026-06-26 08:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:58:58` | `cowrie.session.connect` |
| `2026-06-26 08:58:58` | `cowrie.client.version` |
| `2026-06-26 08:58:58` | `cowrie.client.kex` |
| `2026-06-26 08:58:59` | `cowrie.login.success` |
| `2026-06-26 08:59:00` | `cowrie.session.params` |
| `2026-06-26 08:59:00` | `cowrie.command.input` |
| `2026-06-26 08:59:00` | `cowrie.log.closed` |
| `2026-06-26 08:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1042b0434bcd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:59 |
| **Last Seen** | 2026-06-26 08:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:59:04` | `cowrie.session.connect` |
| `2026-06-26 08:59:04` | `cowrie.client.version` |
| `2026-06-26 08:59:04` | `cowrie.client.kex` |
| `2026-06-26 08:59:04` | `cowrie.login.success` |
| `2026-06-26 08:59:05` | `cowrie.session.params` |
| `2026-06-26 08:59:05` | `cowrie.command.input` |
| `2026-06-26 08:59:06` | `cowrie.log.closed` |
| `2026-06-26 08:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cb072f3f24a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:59 |
| **Last Seen** | 2026-06-26 08:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:59:09` | `cowrie.session.connect` |
| `2026-06-26 08:59:09` | `cowrie.client.version` |
| `2026-06-26 08:59:09` | `cowrie.client.kex` |
| `2026-06-26 08:59:10` | `cowrie.login.success` |
| `2026-06-26 08:59:11` | `cowrie.session.params` |
| `2026-06-26 08:59:11` | `cowrie.command.input` |
| `2026-06-26 08:59:11` | `cowrie.log.closed` |
| `2026-06-26 08:59:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86dd4857ad45

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:59 |
| **Last Seen** | 2026-06-26 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:59:14` | `cowrie.session.connect` |
| `2026-06-26 08:59:14` | `cowrie.client.version` |
| `2026-06-26 08:59:15` | `cowrie.client.kex` |
| `2026-06-26 08:59:15` | `cowrie.login.success` |
| `2026-06-26 08:59:16` | `cowrie.session.params` |
| `2026-06-26 08:59:16` | `cowrie.command.input` |
| `2026-06-26 08:59:16` | `cowrie.log.closed` |
| `2026-06-26 08:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2e0b98998fc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:59 |
| **Last Seen** | 2026-06-26 08:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:59:20` | `cowrie.session.connect` |
| `2026-06-26 08:59:20` | `cowrie.client.version` |
| `2026-06-26 08:59:20` | `cowrie.client.kex` |
| `2026-06-26 08:59:20` | `cowrie.login.success` |
| `2026-06-26 08:59:21` | `cowrie.session.params` |
| `2026-06-26 08:59:21` | `cowrie.command.input` |
| `2026-06-26 08:59:22` | `cowrie.log.closed` |
| `2026-06-26 08:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16e84dcd1298

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 08:59 |
| **Last Seen** | 2026-06-26 08:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:59:20` | `cowrie.session.connect` |
| `2026-06-26 08:59:20` | `cowrie.client.version` |
| `2026-06-26 08:59:21` | `cowrie.client.kex` |
| `2026-06-26 08:59:21` | `cowrie.login.success` |
| `2026-06-26 08:59:22` | `cowrie.session.params` |
| `2026-06-26 08:59:22` | `cowrie.command.input` |
| `2026-06-26 08:59:22` | `cowrie.log.closed` |
| `2026-06-26 08:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f27ab4fb129

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:59 |
| **Last Seen** | 2026-06-26 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:59:25` | `cowrie.session.connect` |
| `2026-06-26 08:59:25` | `cowrie.client.version` |
| `2026-06-26 08:59:25` | `cowrie.client.kex` |
| `2026-06-26 08:59:26` | `cowrie.login.success` |
| `2026-06-26 08:59:27` | `cowrie.session.params` |
| `2026-06-26 08:59:27` | `cowrie.command.input` |
| `2026-06-26 08:59:27` | `cowrie.log.closed` |
| `2026-06-26 08:59:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0350818bec2d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:59 |
| **Last Seen** | 2026-06-26 08:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:59:31` | `cowrie.session.connect` |
| `2026-06-26 08:59:31` | `cowrie.client.version` |
| `2026-06-26 08:59:31` | `cowrie.client.kex` |
| `2026-06-26 08:59:31` | `cowrie.login.success` |
| `2026-06-26 08:59:33` | `cowrie.session.params` |
| `2026-06-26 08:59:33` | `cowrie.command.input` |
| `2026-06-26 08:59:33` | `cowrie.log.closed` |
| `2026-06-26 08:59:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2995a6aa36c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:59 |
| **Last Seen** | 2026-06-26 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:59:36` | `cowrie.session.connect` |
| `2026-06-26 08:59:36` | `cowrie.client.version` |
| `2026-06-26 08:59:36` | `cowrie.client.kex` |
| `2026-06-26 08:59:37` | `cowrie.login.success` |
| `2026-06-26 08:59:38` | `cowrie.session.params` |
| `2026-06-26 08:59:38` | `cowrie.command.input` |
| `2026-06-26 08:59:38` | `cowrie.log.closed` |
| `2026-06-26 08:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5268849e2a73

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:59 |
| **Last Seen** | 2026-06-26 08:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:59:41` | `cowrie.session.connect` |
| `2026-06-26 08:59:41` | `cowrie.client.version` |
| `2026-06-26 08:59:42` | `cowrie.client.kex` |
| `2026-06-26 08:59:43` | `cowrie.login.success` |
| `2026-06-26 08:59:44` | `cowrie.session.params` |
| `2026-06-26 08:59:44` | `cowrie.command.input` |
| `2026-06-26 08:59:44` | `cowrie.log.closed` |
| `2026-06-26 08:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9928a1b0777

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:59 |
| **Last Seen** | 2026-06-26 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:59:47` | `cowrie.session.connect` |
| `2026-06-26 08:59:47` | `cowrie.client.version` |
| `2026-06-26 08:59:47` | `cowrie.client.kex` |
| `2026-06-26 08:59:48` | `cowrie.login.success` |
| `2026-06-26 08:59:48` | `cowrie.session.params` |
| `2026-06-26 08:59:48` | `cowrie.command.input` |
| `2026-06-26 08:59:49` | `cowrie.log.closed` |
| `2026-06-26 08:59:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-283f131ae17a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:59 |
| **Last Seen** | 2026-06-26 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:59:52` | `cowrie.session.connect` |
| `2026-06-26 08:59:53` | `cowrie.client.version` |
| `2026-06-26 08:59:53` | `cowrie.client.kex` |
| `2026-06-26 08:59:53` | `cowrie.login.success` |
| `2026-06-26 08:59:54` | `cowrie.session.params` |
| `2026-06-26 08:59:54` | `cowrie.command.input` |
| `2026-06-26 08:59:54` | `cowrie.log.closed` |
| `2026-06-26 08:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-506523f2403c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:59 |
| **Last Seen** | 2026-06-26 09:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:59:58` | `cowrie.session.connect` |
| `2026-06-26 08:59:58` | `cowrie.client.version` |
| `2026-06-26 08:59:58` | `cowrie.client.kex` |
| `2026-06-26 08:59:59` | `cowrie.login.success` |
| `2026-06-26 09:00:00` | `cowrie.session.params` |
| `2026-06-26 09:00:00` | `cowrie.command.input` |
| `2026-06-26 09:00:00` | `cowrie.log.closed` |
| `2026-06-26 09:00:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa1d2b403335

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 09:00 |
| **Last Seen** | 2026-06-26 09:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:00:02` | `cowrie.session.connect` |
| `2026-06-26 09:00:03` | `cowrie.client.version` |
| `2026-06-26 09:00:03` | `cowrie.client.kex` |
| `2026-06-26 09:00:10` | `cowrie.login.success` |
| `2026-06-26 09:00:13` | `cowrie.session.params` |
| `2026-06-26 09:00:13` | `cowrie.command.input` |
| `2026-06-26 09:00:14` | `cowrie.log.closed` |
| `2026-06-26 09:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc3e96a2308c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:00 |
| **Last Seen** | 2026-06-26 09:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:00:04` | `cowrie.session.connect` |
| `2026-06-26 09:00:04` | `cowrie.client.version` |
| `2026-06-26 09:00:04` | `cowrie.client.kex` |
| `2026-06-26 09:00:04` | `cowrie.login.success` |
| `2026-06-26 09:00:05` | `cowrie.session.params` |
| `2026-06-26 09:00:05` | `cowrie.command.input` |
| `2026-06-26 09:00:05` | `cowrie.log.closed` |
| `2026-06-26 09:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33816cb36449

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:00 |
| **Last Seen** | 2026-06-26 09:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:00:09` | `cowrie.session.connect` |
| `2026-06-26 09:00:09` | `cowrie.client.version` |
| `2026-06-26 09:00:09` | `cowrie.client.kex` |
| `2026-06-26 09:00:10` | `cowrie.login.success` |
| `2026-06-26 09:00:10` | `cowrie.session.params` |
| `2026-06-26 09:00:10` | `cowrie.command.input` |
| `2026-06-26 09:00:10` | `cowrie.log.closed` |
| `2026-06-26 09:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14fff5d79202

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:00 |
| **Last Seen** | 2026-06-26 09:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:00:14` | `cowrie.session.connect` |
| `2026-06-26 09:00:15` | `cowrie.client.version` |
| `2026-06-26 09:00:15` | `cowrie.client.kex` |
| `2026-06-26 09:00:15` | `cowrie.login.success` |
| `2026-06-26 09:00:16` | `cowrie.session.params` |
| `2026-06-26 09:00:16` | `cowrie.command.input` |
| `2026-06-26 09:00:16` | `cowrie.log.closed` |
| `2026-06-26 09:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c75e123d968a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:00 |
| **Last Seen** | 2026-06-26 09:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:00:16` | `cowrie.session.connect` |
| `2026-06-26 09:00:16` | `cowrie.client.version` |
| `2026-06-26 09:00:16` | `cowrie.client.kex` |
| `2026-06-26 09:00:16` | `cowrie.login.success` |
| `2026-06-26 09:00:17` | `cowrie.session.params` |
| `2026-06-26 09:00:17` | `cowrie.command.input` |
| `2026-06-26 09:00:17` | `cowrie.log.closed` |
| `2026-06-26 09:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1491c0549eaa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:00 |
| **Last Seen** | 2026-06-26 09:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:00:20` | `cowrie.session.connect` |
| `2026-06-26 09:00:20` | `cowrie.client.version` |
| `2026-06-26 09:00:20` | `cowrie.client.kex` |
| `2026-06-26 09:00:21` | `cowrie.login.success` |
| `2026-06-26 09:00:21` | `cowrie.session.params` |
| `2026-06-26 09:00:21` | `cowrie.command.input` |
| `2026-06-26 09:00:22` | `cowrie.log.closed` |
| `2026-06-26 09:00:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69e2f001297c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:00 |
| **Last Seen** | 2026-06-26 09:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:00:26` | `cowrie.session.connect` |
| `2026-06-26 09:00:26` | `cowrie.client.version` |
| `2026-06-26 09:00:26` | `cowrie.client.kex` |
| `2026-06-26 09:00:27` | `cowrie.login.success` |
| `2026-06-26 09:00:28` | `cowrie.session.params` |
| `2026-06-26 09:00:28` | `cowrie.command.input` |
| `2026-06-26 09:00:28` | `cowrie.log.closed` |
| `2026-06-26 09:00:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80980b2be659

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:00 |
| **Last Seen** | 2026-06-26 09:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:00:31` | `cowrie.session.connect` |
| `2026-06-26 09:00:32` | `cowrie.client.version` |
| `2026-06-26 09:00:32` | `cowrie.client.kex` |
| `2026-06-26 09:00:32` | `cowrie.login.success` |
| `2026-06-26 09:00:33` | `cowrie.session.params` |
| `2026-06-26 09:00:33` | `cowrie.command.input` |
| `2026-06-26 09:00:33` | `cowrie.log.closed` |
| `2026-06-26 09:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8105da280271

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:00 |
| **Last Seen** | 2026-06-26 09:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:00:37` | `cowrie.session.connect` |
| `2026-06-26 09:00:37` | `cowrie.client.version` |
| `2026-06-26 09:00:37` | `cowrie.client.kex` |
| `2026-06-26 09:00:37` | `cowrie.login.success` |
| `2026-06-26 09:00:39` | `cowrie.session.params` |
| `2026-06-26 09:00:39` | `cowrie.command.input` |
| `2026-06-26 09:00:39` | `cowrie.log.closed` |
| `2026-06-26 09:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ad09f05d069

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:00 |
| **Last Seen** | 2026-06-26 09:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:00:42` | `cowrie.session.connect` |
| `2026-06-26 09:00:42` | `cowrie.client.version` |
| `2026-06-26 09:00:43` | `cowrie.client.kex` |
| `2026-06-26 09:00:43` | `cowrie.login.success` |
| `2026-06-26 09:00:44` | `cowrie.session.params` |
| `2026-06-26 09:00:44` | `cowrie.command.input` |
| `2026-06-26 09:00:44` | `cowrie.log.closed` |
| `2026-06-26 09:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c712db7f7d0f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:00 |
| **Last Seen** | 2026-06-26 09:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:00:48` | `cowrie.session.connect` |
| `2026-06-26 09:00:48` | `cowrie.client.version` |
| `2026-06-26 09:00:48` | `cowrie.client.kex` |
| `2026-06-26 09:00:48` | `cowrie.login.success` |
| `2026-06-26 09:00:49` | `cowrie.session.params` |
| `2026-06-26 09:00:49` | `cowrie.command.input` |
| `2026-06-26 09:00:49` | `cowrie.log.closed` |
| `2026-06-26 09:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea6b316ff166

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:00 |
| **Last Seen** | 2026-06-26 09:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:00:53` | `cowrie.session.connect` |
| `2026-06-26 09:00:53` | `cowrie.client.version` |
| `2026-06-26 09:00:53` | `cowrie.client.kex` |
| `2026-06-26 09:00:54` | `cowrie.login.success` |
| `2026-06-26 09:00:55` | `cowrie.session.params` |
| `2026-06-26 09:00:55` | `cowrie.command.input` |
| `2026-06-26 09:00:55` | `cowrie.log.closed` |
| `2026-06-26 09:00:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55e9d5ad422e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:00 |
| **Last Seen** | 2026-06-26 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:00:59` | `cowrie.session.connect` |
| `2026-06-26 09:00:59` | `cowrie.client.version` |
| `2026-06-26 09:00:59` | `cowrie.client.kex` |
| `2026-06-26 09:00:59` | `cowrie.login.success` |
| `2026-06-26 09:01:00` | `cowrie.session.params` |
| `2026-06-26 09:01:00` | `cowrie.command.input` |
| `2026-06-26 09:01:00` | `cowrie.log.closed` |
| `2026-06-26 09:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-332b1062579b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:01 |
| **Last Seen** | 2026-06-26 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:01:04` | `cowrie.session.connect` |
| `2026-06-26 09:01:04` | `cowrie.client.version` |
| `2026-06-26 09:01:04` | `cowrie.client.kex` |
| `2026-06-26 09:01:05` | `cowrie.login.success` |
| `2026-06-26 09:01:06` | `cowrie.session.params` |
| `2026-06-26 09:01:06` | `cowrie.command.input` |
| `2026-06-26 09:01:06` | `cowrie.log.closed` |
| `2026-06-26 09:01:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85cba7a3b4c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:01 |
| **Last Seen** | 2026-06-26 09:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:01:09` | `cowrie.session.connect` |
| `2026-06-26 09:01:09` | `cowrie.client.version` |
| `2026-06-26 09:01:10` | `cowrie.client.kex` |
| `2026-06-26 09:01:10` | `cowrie.login.success` |
| `2026-06-26 09:01:11` | `cowrie.session.params` |
| `2026-06-26 09:01:11` | `cowrie.command.input` |
| `2026-06-26 09:01:12` | `cowrie.log.closed` |
| `2026-06-26 09:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a895535b1ce

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:01 |
| **Last Seen** | 2026-06-26 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:01:11` | `cowrie.session.connect` |
| `2026-06-26 09:01:11` | `cowrie.client.version` |
| `2026-06-26 09:01:11` | `cowrie.client.kex` |
| `2026-06-26 09:01:12` | `cowrie.login.success` |
| `2026-06-26 09:01:13` | `cowrie.session.params` |
| `2026-06-26 09:01:13` | `cowrie.command.input` |
| `2026-06-26 09:01:13` | `cowrie.log.closed` |
| `2026-06-26 09:01:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec7b71d2feb3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:01 |
| **Last Seen** | 2026-06-26 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:01:15` | `cowrie.session.connect` |
| `2026-06-26 09:01:15` | `cowrie.client.version` |
| `2026-06-26 09:01:15` | `cowrie.client.kex` |
| `2026-06-26 09:01:16` | `cowrie.login.success` |
| `2026-06-26 09:01:17` | `cowrie.session.params` |
| `2026-06-26 09:01:17` | `cowrie.command.input` |
| `2026-06-26 09:01:17` | `cowrie.log.closed` |
| `2026-06-26 09:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c6d267ff728

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:01 |
| **Last Seen** | 2026-06-26 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:01:21` | `cowrie.session.connect` |
| `2026-06-26 09:01:21` | `cowrie.client.version` |
| `2026-06-26 09:01:21` | `cowrie.client.kex` |
| `2026-06-26 09:01:21` | `cowrie.login.success` |
| `2026-06-26 09:01:22` | `cowrie.session.params` |
| `2026-06-26 09:01:22` | `cowrie.command.input` |
| `2026-06-26 09:01:22` | `cowrie.log.closed` |
| `2026-06-26 09:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c77ab1d7ac9d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:01 |
| **Last Seen** | 2026-06-26 09:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:01:26` | `cowrie.session.connect` |
| `2026-06-26 09:01:26` | `cowrie.client.version` |
| `2026-06-26 09:01:26` | `cowrie.client.kex` |
| `2026-06-26 09:01:27` | `cowrie.login.success` |
| `2026-06-26 09:01:28` | `cowrie.session.params` |
| `2026-06-26 09:01:28` | `cowrie.command.input` |
| `2026-06-26 09:01:28` | `cowrie.log.closed` |
| `2026-06-26 09:01:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f917951b23a8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:01 |
| **Last Seen** | 2026-06-26 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:01:31` | `cowrie.session.connect` |
| `2026-06-26 09:01:32` | `cowrie.client.version` |
| `2026-06-26 09:01:32` | `cowrie.client.kex` |
| `2026-06-26 09:01:32` | `cowrie.login.success` |
| `2026-06-26 09:01:33` | `cowrie.session.params` |
| `2026-06-26 09:01:33` | `cowrie.command.input` |
| `2026-06-26 09:01:33` | `cowrie.log.closed` |
| `2026-06-26 09:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bfc9143029b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:01 |
| **Last Seen** | 2026-06-26 09:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:01:37` | `cowrie.session.connect` |
| `2026-06-26 09:01:37` | `cowrie.client.version` |
| `2026-06-26 09:01:37` | `cowrie.client.kex` |
| `2026-06-26 09:01:38` | `cowrie.login.success` |
| `2026-06-26 09:01:39` | `cowrie.session.params` |
| `2026-06-26 09:01:39` | `cowrie.command.input` |
| `2026-06-26 09:01:39` | `cowrie.log.closed` |
| `2026-06-26 09:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ae225d2199c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:01 |
| **Last Seen** | 2026-06-26 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:01:42` | `cowrie.session.connect` |
| `2026-06-26 09:01:43` | `cowrie.client.version` |
| `2026-06-26 09:01:43` | `cowrie.client.kex` |
| `2026-06-26 09:01:43` | `cowrie.login.success` |
| `2026-06-26 09:01:44` | `cowrie.session.params` |
| `2026-06-26 09:01:44` | `cowrie.command.input` |
| `2026-06-26 09:01:44` | `cowrie.log.closed` |
| `2026-06-26 09:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd40eef1db51

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:01 |
| **Last Seen** | 2026-06-26 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:01:48` | `cowrie.session.connect` |
| `2026-06-26 09:01:48` | `cowrie.client.version` |
| `2026-06-26 09:01:48` | `cowrie.client.kex` |
| `2026-06-26 09:01:48` | `cowrie.login.success` |
| `2026-06-26 09:01:49` | `cowrie.session.params` |
| `2026-06-26 09:01:49` | `cowrie.command.input` |
| `2026-06-26 09:01:49` | `cowrie.log.closed` |
| `2026-06-26 09:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61accf8b3467

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:01 |
| **Last Seen** | 2026-06-26 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:01:54` | `cowrie.session.connect` |
| `2026-06-26 09:01:54` | `cowrie.client.version` |
| `2026-06-26 09:01:54` | `cowrie.client.kex` |
| `2026-06-26 09:01:54` | `cowrie.login.success` |
| `2026-06-26 09:01:55` | `cowrie.session.params` |
| `2026-06-26 09:01:55` | `cowrie.command.input` |
| `2026-06-26 09:01:55` | `cowrie.log.closed` |
| `2026-06-26 09:01:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78e2aa7655ec

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:01 |
| **Last Seen** | 2026-06-26 09:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:01:59` | `cowrie.session.connect` |
| `2026-06-26 09:01:59` | `cowrie.client.version` |
| `2026-06-26 09:01:59` | `cowrie.client.kex` |
| `2026-06-26 09:02:00` | `cowrie.login.success` |
| `2026-06-26 09:02:01` | `cowrie.session.params` |
| `2026-06-26 09:02:01` | `cowrie.command.input` |
| `2026-06-26 09:02:01` | `cowrie.log.closed` |
| `2026-06-26 09:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f7222560d58

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:02 |
| **Last Seen** | 2026-06-26 09:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:02:04` | `cowrie.session.connect` |
| `2026-06-26 09:02:04` | `cowrie.client.version` |
| `2026-06-26 09:02:04` | `cowrie.client.kex` |
| `2026-06-26 09:02:05` | `cowrie.login.success` |
| `2026-06-26 09:02:06` | `cowrie.session.params` |
| `2026-06-26 09:02:06` | `cowrie.command.input` |
| `2026-06-26 09:02:06` | `cowrie.log.closed` |
| `2026-06-26 09:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27d23d4e48bd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:02 |
| **Last Seen** | 2026-06-26 09:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:02:06` | `cowrie.session.connect` |
| `2026-06-26 09:02:06` | `cowrie.client.version` |
| `2026-06-26 09:02:06` | `cowrie.client.kex` |
| `2026-06-26 09:02:06` | `cowrie.login.success` |
| `2026-06-26 09:02:07` | `cowrie.session.params` |
| `2026-06-26 09:02:07` | `cowrie.command.input` |
| `2026-06-26 09:02:07` | `cowrie.log.closed` |
| `2026-06-26 09:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ade18f0ee8cd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:02 |
| **Last Seen** | 2026-06-26 09:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:02:10` | `cowrie.session.connect` |
| `2026-06-26 09:02:10` | `cowrie.client.version` |
| `2026-06-26 09:02:10` | `cowrie.client.kex` |
| `2026-06-26 09:02:10` | `cowrie.login.success` |
| `2026-06-26 09:02:11` | `cowrie.session.params` |
| `2026-06-26 09:02:11` | `cowrie.command.input` |
| `2026-06-26 09:02:12` | `cowrie.log.closed` |
| `2026-06-26 09:02:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aca4b76d845

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:02 |
| **Last Seen** | 2026-06-26 09:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:02:15` | `cowrie.session.connect` |
| `2026-06-26 09:02:15` | `cowrie.client.version` |
| `2026-06-26 09:02:15` | `cowrie.client.kex` |
| `2026-06-26 09:02:16` | `cowrie.login.success` |
| `2026-06-26 09:02:17` | `cowrie.session.params` |
| `2026-06-26 09:02:17` | `cowrie.command.input` |
| `2026-06-26 09:02:17` | `cowrie.log.closed` |
| `2026-06-26 09:02:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66aa45780005

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:02 |
| **Last Seen** | 2026-06-26 09:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:02:21` | `cowrie.session.connect` |
| `2026-06-26 09:02:21` | `cowrie.client.version` |
| `2026-06-26 09:02:21` | `cowrie.client.kex` |
| `2026-06-26 09:02:21` | `cowrie.login.success` |
| `2026-06-26 09:02:22` | `cowrie.session.params` |
| `2026-06-26 09:02:22` | `cowrie.command.input` |
| `2026-06-26 09:02:23` | `cowrie.log.closed` |
| `2026-06-26 09:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c1d83cd1852

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:02 |
| **Last Seen** | 2026-06-26 09:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:02:27` | `cowrie.session.connect` |
| `2026-06-26 09:02:27` | `cowrie.client.version` |
| `2026-06-26 09:02:27` | `cowrie.client.kex` |
| `2026-06-26 09:02:27` | `cowrie.login.success` |
| `2026-06-26 09:02:28` | `cowrie.session.params` |
| `2026-06-26 09:02:28` | `cowrie.command.input` |
| `2026-06-26 09:02:28` | `cowrie.log.closed` |
| `2026-06-26 09:02:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbed3bf52efa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:02 |
| **Last Seen** | 2026-06-26 09:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:02:32` | `cowrie.session.connect` |
| `2026-06-26 09:02:32` | `cowrie.client.version` |
| `2026-06-26 09:02:32` | `cowrie.client.kex` |
| `2026-06-26 09:02:33` | `cowrie.login.success` |
| `2026-06-26 09:02:34` | `cowrie.session.params` |
| `2026-06-26 09:02:34` | `cowrie.command.input` |
| `2026-06-26 09:02:34` | `cowrie.log.closed` |
| `2026-06-26 09:02:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a07cc3c8f525

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:02 |
| **Last Seen** | 2026-06-26 09:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:02:38` | `cowrie.session.connect` |
| `2026-06-26 09:02:38` | `cowrie.client.version` |
| `2026-06-26 09:02:38` | `cowrie.client.kex` |
| `2026-06-26 09:02:39` | `cowrie.login.success` |
| `2026-06-26 09:02:40` | `cowrie.session.params` |
| `2026-06-26 09:02:40` | `cowrie.command.input` |
| `2026-06-26 09:02:40` | `cowrie.log.closed` |
| `2026-06-26 09:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce3c687dde20

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:02 |
| **Last Seen** | 2026-06-26 09:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:02:43` | `cowrie.session.connect` |
| `2026-06-26 09:02:43` | `cowrie.client.version` |
| `2026-06-26 09:02:43` | `cowrie.client.kex` |
| `2026-06-26 09:02:44` | `cowrie.login.success` |
| `2026-06-26 09:02:45` | `cowrie.session.params` |
| `2026-06-26 09:02:45` | `cowrie.command.input` |
| `2026-06-26 09:02:45` | `cowrie.log.closed` |
| `2026-06-26 09:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a508c6d5fc3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:02 |
| **Last Seen** | 2026-06-26 09:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:02:49` | `cowrie.session.connect` |
| `2026-06-26 09:02:49` | `cowrie.client.version` |
| `2026-06-26 09:02:49` | `cowrie.client.kex` |
| `2026-06-26 09:02:49` | `cowrie.login.success` |
| `2026-06-26 09:02:51` | `cowrie.session.params` |
| `2026-06-26 09:02:51` | `cowrie.command.input` |
| `2026-06-26 09:02:51` | `cowrie.log.closed` |
| `2026-06-26 09:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54e09cd9db74

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:02 |
| **Last Seen** | 2026-06-26 09:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:02:55` | `cowrie.session.connect` |
| `2026-06-26 09:02:55` | `cowrie.client.version` |
| `2026-06-26 09:02:55` | `cowrie.client.kex` |
| `2026-06-26 09:02:55` | `cowrie.login.success` |
| `2026-06-26 09:02:56` | `cowrie.session.params` |
| `2026-06-26 09:02:56` | `cowrie.command.input` |
| `2026-06-26 09:02:56` | `cowrie.log.closed` |
| `2026-06-26 09:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90919a681c80

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:02 |
| **Last Seen** | 2026-06-26 09:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:02:59` | `cowrie.session.connect` |
| `2026-06-26 09:02:59` | `cowrie.client.version` |
| `2026-06-26 09:03:00` | `cowrie.client.kex` |
| `2026-06-26 09:03:00` | `cowrie.login.success` |
| `2026-06-26 09:03:01` | `cowrie.session.params` |
| `2026-06-26 09:03:01` | `cowrie.command.input` |
| `2026-06-26 09:03:01` | `cowrie.log.closed` |
| `2026-06-26 09:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a27b505d2dad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:03 |
| **Last Seen** | 2026-06-26 09:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:03:01` | `cowrie.session.connect` |
| `2026-06-26 09:03:01` | `cowrie.client.version` |
| `2026-06-26 09:03:01` | `cowrie.client.kex` |
| `2026-06-26 09:03:01` | `cowrie.login.success` |
| `2026-06-26 09:03:02` | `cowrie.session.params` |
| `2026-06-26 09:03:02` | `cowrie.command.input` |
| `2026-06-26 09:03:03` | `cowrie.log.closed` |
| `2026-06-26 09:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e11eb98729a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:03 |
| **Last Seen** | 2026-06-26 09:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:03:05` | `cowrie.session.connect` |
| `2026-06-26 09:03:06` | `cowrie.client.version` |
| `2026-06-26 09:03:06` | `cowrie.client.kex` |
| `2026-06-26 09:03:06` | `cowrie.login.success` |
| `2026-06-26 09:03:07` | `cowrie.session.params` |
| `2026-06-26 09:03:07` | `cowrie.command.input` |
| `2026-06-26 09:03:07` | `cowrie.log.closed` |
| `2026-06-26 09:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67e0b2923204

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:03 |
| **Last Seen** | 2026-06-26 09:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:03:11` | `cowrie.session.connect` |
| `2026-06-26 09:03:11` | `cowrie.client.version` |
| `2026-06-26 09:03:11` | `cowrie.client.kex` |
| `2026-06-26 09:03:12` | `cowrie.login.success` |
| `2026-06-26 09:03:13` | `cowrie.session.params` |
| `2026-06-26 09:03:13` | `cowrie.command.input` |
| `2026-06-26 09:03:13` | `cowrie.log.closed` |
| `2026-06-26 09:03:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f06685ccad7c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:03 |
| **Last Seen** | 2026-06-26 09:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:03:17` | `cowrie.session.connect` |
| `2026-06-26 09:03:17` | `cowrie.client.version` |
| `2026-06-26 09:03:17` | `cowrie.client.kex` |
| `2026-06-26 09:03:17` | `cowrie.login.success` |
| `2026-06-26 09:03:18` | `cowrie.session.params` |
| `2026-06-26 09:03:18` | `cowrie.command.input` |
| `2026-06-26 09:03:18` | `cowrie.log.closed` |
| `2026-06-26 09:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7a922567d63

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:03 |
| **Last Seen** | 2026-06-26 09:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:03:22` | `cowrie.session.connect` |
| `2026-06-26 09:03:22` | `cowrie.client.version` |
| `2026-06-26 09:03:22` | `cowrie.client.kex` |
| `2026-06-26 09:03:23` | `cowrie.login.success` |
| `2026-06-26 09:03:24` | `cowrie.session.params` |
| `2026-06-26 09:03:24` | `cowrie.command.input` |
| `2026-06-26 09:03:25` | `cowrie.log.closed` |
| `2026-06-26 09:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f3c067e9bcc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:03 |
| **Last Seen** | 2026-06-26 09:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:03:28` | `cowrie.session.connect` |
| `2026-06-26 09:03:28` | `cowrie.client.version` |
| `2026-06-26 09:03:28` | `cowrie.client.kex` |
| `2026-06-26 09:03:28` | `cowrie.login.success` |
| `2026-06-26 09:03:29` | `cowrie.session.params` |
| `2026-06-26 09:03:29` | `cowrie.command.input` |
| `2026-06-26 09:03:29` | `cowrie.log.closed` |
| `2026-06-26 09:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84b884083122

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:03 |
| **Last Seen** | 2026-06-26 09:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:03:33` | `cowrie.session.connect` |
| `2026-06-26 09:03:33` | `cowrie.client.version` |
| `2026-06-26 09:03:33` | `cowrie.client.kex` |
| `2026-06-26 09:03:34` | `cowrie.login.success` |
| `2026-06-26 09:03:35` | `cowrie.session.params` |
| `2026-06-26 09:03:35` | `cowrie.command.input` |
| `2026-06-26 09:03:35` | `cowrie.log.closed` |
| `2026-06-26 09:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c69f46e32a54

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:03 |
| **Last Seen** | 2026-06-26 09:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:03:39` | `cowrie.session.connect` |
| `2026-06-26 09:03:39` | `cowrie.client.version` |
| `2026-06-26 09:03:39` | `cowrie.client.kex` |
| `2026-06-26 09:03:39` | `cowrie.login.success` |
| `2026-06-26 09:03:40` | `cowrie.session.params` |
| `2026-06-26 09:03:40` | `cowrie.command.input` |
| `2026-06-26 09:03:41` | `cowrie.log.closed` |
| `2026-06-26 09:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98713ef6996b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:03 |
| **Last Seen** | 2026-06-26 09:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:03:44` | `cowrie.session.connect` |
| `2026-06-26 09:03:44` | `cowrie.client.version` |
| `2026-06-26 09:03:44` | `cowrie.client.kex` |
| `2026-06-26 09:03:45` | `cowrie.login.success` |
| `2026-06-26 09:03:46` | `cowrie.session.params` |
| `2026-06-26 09:03:46` | `cowrie.command.input` |
| `2026-06-26 09:03:46` | `cowrie.log.closed` |
| `2026-06-26 09:03:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28fb46bda75c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:03 |
| **Last Seen** | 2026-06-26 09:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:03:50` | `cowrie.session.connect` |
| `2026-06-26 09:03:50` | `cowrie.client.version` |
| `2026-06-26 09:03:50` | `cowrie.client.kex` |
| `2026-06-26 09:03:51` | `cowrie.login.success` |
| `2026-06-26 09:03:51` | `cowrie.session.params` |
| `2026-06-26 09:03:51` | `cowrie.command.input` |
| `2026-06-26 09:03:51` | `cowrie.log.closed` |
| `2026-06-26 09:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8a9cbd880ec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:03 |
| **Last Seen** | 2026-06-26 09:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:03:54` | `cowrie.session.connect` |
| `2026-06-26 09:03:54` | `cowrie.client.version` |
| `2026-06-26 09:03:54` | `cowrie.client.kex` |
| `2026-06-26 09:03:54` | `cowrie.login.success` |
| `2026-06-26 09:03:55` | `cowrie.session.params` |
| `2026-06-26 09:03:55` | `cowrie.command.input` |
| `2026-06-26 09:03:55` | `cowrie.log.closed` |
| `2026-06-26 09:03:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fba00efbfa05

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:03 |
| **Last Seen** | 2026-06-26 09:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:03:56` | `cowrie.session.connect` |
| `2026-06-26 09:03:56` | `cowrie.client.version` |
| `2026-06-26 09:03:56` | `cowrie.client.kex` |
| `2026-06-26 09:03:57` | `cowrie.login.success` |
| `2026-06-26 09:03:58` | `cowrie.session.params` |
| `2026-06-26 09:03:58` | `cowrie.command.input` |
| `2026-06-26 09:03:58` | `cowrie.log.closed` |
| `2026-06-26 09:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1287802fda97

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:04 |
| **Last Seen** | 2026-06-26 09:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:04:02` | `cowrie.session.connect` |
| `2026-06-26 09:04:02` | `cowrie.client.version` |
| `2026-06-26 09:04:02` | `cowrie.client.kex` |
| `2026-06-26 09:04:02` | `cowrie.login.success` |
| `2026-06-26 09:04:03` | `cowrie.session.params` |
| `2026-06-26 09:04:03` | `cowrie.command.input` |
| `2026-06-26 09:04:04` | `cowrie.log.closed` |
| `2026-06-26 09:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93a362f481ab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:04 |
| **Last Seen** | 2026-06-26 09:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:04:07` | `cowrie.session.connect` |
| `2026-06-26 09:04:07` | `cowrie.client.version` |
| `2026-06-26 09:04:07` | `cowrie.client.kex` |
| `2026-06-26 09:04:08` | `cowrie.login.success` |
| `2026-06-26 09:04:09` | `cowrie.session.params` |
| `2026-06-26 09:04:09` | `cowrie.command.input` |
| `2026-06-26 09:04:09` | `cowrie.log.closed` |
| `2026-06-26 09:04:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e52bb87161f6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:04 |
| **Last Seen** | 2026-06-26 09:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:04:13` | `cowrie.session.connect` |
| `2026-06-26 09:04:13` | `cowrie.client.version` |
| `2026-06-26 09:04:13` | `cowrie.client.kex` |
| `2026-06-26 09:04:14` | `cowrie.login.success` |
| `2026-06-26 09:04:14` | `cowrie.session.params` |
| `2026-06-26 09:04:14` | `cowrie.command.input` |
| `2026-06-26 09:04:15` | `cowrie.log.closed` |
| `2026-06-26 09:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecc25989916a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:04 |
| **Last Seen** | 2026-06-26 09:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:04:18` | `cowrie.session.connect` |
| `2026-06-26 09:04:18` | `cowrie.client.version` |
| `2026-06-26 09:04:19` | `cowrie.client.kex` |
| `2026-06-26 09:04:20` | `cowrie.login.success` |
| `2026-06-26 09:04:20` | `cowrie.session.params` |
| `2026-06-26 09:04:20` | `cowrie.command.input` |
| `2026-06-26 09:04:21` | `cowrie.log.closed` |
| `2026-06-26 09:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cc1746ad913

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:04 |
| **Last Seen** | 2026-06-26 09:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:04:24` | `cowrie.session.connect` |
| `2026-06-26 09:04:24` | `cowrie.client.version` |
| `2026-06-26 09:04:24` | `cowrie.client.kex` |
| `2026-06-26 09:04:25` | `cowrie.login.success` |
| `2026-06-26 09:04:26` | `cowrie.session.params` |
| `2026-06-26 09:04:26` | `cowrie.command.input` |
| `2026-06-26 09:04:26` | `cowrie.log.closed` |
| `2026-06-26 09:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98456322bbb1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:04 |
| **Last Seen** | 2026-06-26 09:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:04:30` | `cowrie.session.connect` |
| `2026-06-26 09:04:30` | `cowrie.client.version` |
| `2026-06-26 09:04:30` | `cowrie.client.kex` |
| `2026-06-26 09:04:31` | `cowrie.login.success` |
| `2026-06-26 09:04:32` | `cowrie.session.params` |
| `2026-06-26 09:04:32` | `cowrie.command.input` |
| `2026-06-26 09:04:32` | `cowrie.log.closed` |
| `2026-06-26 09:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d737175ab29

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:04 |
| **Last Seen** | 2026-06-26 09:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:04:36` | `cowrie.session.connect` |
| `2026-06-26 09:04:36` | `cowrie.client.version` |
| `2026-06-26 09:04:36` | `cowrie.client.kex` |
| `2026-06-26 09:04:37` | `cowrie.login.success` |
| `2026-06-26 09:04:37` | `cowrie.session.params` |
| `2026-06-26 09:04:37` | `cowrie.command.input` |
| `2026-06-26 09:04:37` | `cowrie.log.closed` |
| `2026-06-26 09:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4e541c36b30

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:04 |
| **Last Seen** | 2026-06-26 09:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:04:41` | `cowrie.session.connect` |
| `2026-06-26 09:04:41` | `cowrie.client.version` |
| `2026-06-26 09:04:42` | `cowrie.client.kex` |
| `2026-06-26 09:04:42` | `cowrie.login.success` |
| `2026-06-26 09:04:43` | `cowrie.session.params` |
| `2026-06-26 09:04:43` | `cowrie.command.input` |
| `2026-06-26 09:04:44` | `cowrie.log.closed` |
| `2026-06-26 09:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85a1e0e626fb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:04 |
| **Last Seen** | 2026-06-26 09:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:04:47` | `cowrie.session.connect` |
| `2026-06-26 09:04:47` | `cowrie.client.version` |
| `2026-06-26 09:04:48` | `cowrie.client.kex` |
| `2026-06-26 09:04:48` | `cowrie.login.success` |
| `2026-06-26 09:04:49` | `cowrie.session.params` |
| `2026-06-26 09:04:49` | `cowrie.command.input` |
| `2026-06-26 09:04:50` | `cowrie.log.closed` |
| `2026-06-26 09:04:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64a9e8d94ea0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:04 |
| **Last Seen** | 2026-06-26 09:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:04:48` | `cowrie.session.connect` |
| `2026-06-26 09:04:48` | `cowrie.client.version` |
| `2026-06-26 09:04:48` | `cowrie.client.kex` |
| `2026-06-26 09:04:49` | `cowrie.login.success` |
| `2026-06-26 09:04:50` | `cowrie.session.params` |
| `2026-06-26 09:04:50` | `cowrie.command.input` |
| `2026-06-26 09:04:50` | `cowrie.log.closed` |
| `2026-06-26 09:04:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5df787b9a98

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:04 |
| **Last Seen** | 2026-06-26 09:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:04:53` | `cowrie.session.connect` |
| `2026-06-26 09:04:53` | `cowrie.client.version` |
| `2026-06-26 09:04:53` | `cowrie.client.kex` |
| `2026-06-26 09:04:55` | `cowrie.login.success` |
| `2026-06-26 09:04:56` | `cowrie.session.params` |
| `2026-06-26 09:04:56` | `cowrie.command.input` |
| `2026-06-26 09:04:56` | `cowrie.log.closed` |
| `2026-06-26 09:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d8c825d7e59

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:04 |
| **Last Seen** | 2026-06-26 09:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:04:59` | `cowrie.session.connect` |
| `2026-06-26 09:04:59` | `cowrie.client.version` |
| `2026-06-26 09:04:59` | `cowrie.client.kex` |
| `2026-06-26 09:05:00` | `cowrie.login.success` |
| `2026-06-26 09:05:01` | `cowrie.session.params` |
| `2026-06-26 09:05:01` | `cowrie.command.input` |
| `2026-06-26 09:05:01` | `cowrie.log.closed` |
| `2026-06-26 09:05:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2edc156e6c2d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:05 |
| **Last Seen** | 2026-06-26 09:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:05:04` | `cowrie.session.connect` |
| `2026-06-26 09:05:05` | `cowrie.client.version` |
| `2026-06-26 09:05:05` | `cowrie.client.kex` |
| `2026-06-26 09:05:05` | `cowrie.login.success` |
| `2026-06-26 09:05:07` | `cowrie.session.params` |
| `2026-06-26 09:05:07` | `cowrie.command.input` |
| `2026-06-26 09:05:07` | `cowrie.log.closed` |
| `2026-06-26 09:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d0554786bf3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:05 |
| **Last Seen** | 2026-06-26 09:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:05:10` | `cowrie.session.connect` |
| `2026-06-26 09:05:10` | `cowrie.client.version` |
| `2026-06-26 09:05:10` | `cowrie.client.kex` |
| `2026-06-26 09:05:11` | `cowrie.login.success` |
| `2026-06-26 09:05:12` | `cowrie.session.params` |
| `2026-06-26 09:05:12` | `cowrie.command.input` |
| `2026-06-26 09:05:13` | `cowrie.log.closed` |
| `2026-06-26 09:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5998b61b2a29

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:05 |
| **Last Seen** | 2026-06-26 09:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:05:16` | `cowrie.session.connect` |
| `2026-06-26 09:05:16` | `cowrie.client.version` |
| `2026-06-26 09:05:16` | `cowrie.client.kex` |
| `2026-06-26 09:05:17` | `cowrie.login.success` |
| `2026-06-26 09:05:17` | `cowrie.session.params` |
| `2026-06-26 09:05:17` | `cowrie.command.input` |
| `2026-06-26 09:05:18` | `cowrie.log.closed` |
| `2026-06-26 09:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b2808921daf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:05 |
| **Last Seen** | 2026-06-26 09:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:05:21` | `cowrie.session.connect` |
| `2026-06-26 09:05:21` | `cowrie.client.version` |
| `2026-06-26 09:05:21` | `cowrie.client.kex` |
| `2026-06-26 09:05:22` | `cowrie.login.success` |
| `2026-06-26 09:05:23` | `cowrie.session.params` |
| `2026-06-26 09:05:23` | `cowrie.command.input` |
| `2026-06-26 09:05:23` | `cowrie.log.closed` |
| `2026-06-26 09:05:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9582c536ac4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:05 |
| **Last Seen** | 2026-06-26 09:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:05:27` | `cowrie.session.connect` |
| `2026-06-26 09:05:27` | `cowrie.client.version` |
| `2026-06-26 09:05:27` | `cowrie.client.kex` |
| `2026-06-26 09:05:28` | `cowrie.login.success` |
| `2026-06-26 09:05:29` | `cowrie.session.params` |
| `2026-06-26 09:05:29` | `cowrie.command.input` |
| `2026-06-26 09:05:29` | `cowrie.log.closed` |
| `2026-06-26 09:05:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-097e76f87302

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:05 |
| **Last Seen** | 2026-06-26 09:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:05:32` | `cowrie.session.connect` |
| `2026-06-26 09:05:32` | `cowrie.client.version` |
| `2026-06-26 09:05:32` | `cowrie.client.kex` |
| `2026-06-26 09:05:33` | `cowrie.login.success` |
| `2026-06-26 09:05:34` | `cowrie.session.params` |
| `2026-06-26 09:05:34` | `cowrie.command.input` |
| `2026-06-26 09:05:34` | `cowrie.log.closed` |
| `2026-06-26 09:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56ff9f6c8e1f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:05 |
| **Last Seen** | 2026-06-26 09:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:05:38` | `cowrie.session.connect` |
| `2026-06-26 09:05:38` | `cowrie.client.version` |
| `2026-06-26 09:05:38` | `cowrie.client.kex` |
| `2026-06-26 09:05:38` | `cowrie.login.success` |
| `2026-06-26 09:05:39` | `cowrie.session.params` |
| `2026-06-26 09:05:39` | `cowrie.command.input` |
| `2026-06-26 09:05:40` | `cowrie.log.closed` |
| `2026-06-26 09:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3c737c7f442

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:05 |
| **Last Seen** | 2026-06-26 09:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:05:44` | `cowrie.session.connect` |
| `2026-06-26 09:05:44` | `cowrie.client.version` |
| `2026-06-26 09:05:44` | `cowrie.client.kex` |
| `2026-06-26 09:05:44` | `cowrie.login.success` |
| `2026-06-26 09:05:46` | `cowrie.session.params` |
| `2026-06-26 09:05:46` | `cowrie.command.input` |
| `2026-06-26 09:05:46` | `cowrie.log.closed` |
| `2026-06-26 09:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f22af77bfd6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:05 |
| **Last Seen** | 2026-06-26 09:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:05:44` | `cowrie.session.connect` |
| `2026-06-26 09:05:44` | `cowrie.client.version` |
| `2026-06-26 09:05:44` | `cowrie.client.kex` |
| `2026-06-26 09:05:44` | `cowrie.login.success` |
| `2026-06-26 09:05:45` | `cowrie.session.params` |
| `2026-06-26 09:05:45` | `cowrie.command.input` |
| `2026-06-26 09:05:45` | `cowrie.log.closed` |
| `2026-06-26 09:05:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70848614fdae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:05 |
| **Last Seen** | 2026-06-26 09:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:05:49` | `cowrie.session.connect` |
| `2026-06-26 09:05:49` | `cowrie.client.version` |
| `2026-06-26 09:05:49` | `cowrie.client.kex` |
| `2026-06-26 09:05:50` | `cowrie.login.success` |
| `2026-06-26 09:05:51` | `cowrie.session.params` |
| `2026-06-26 09:05:51` | `cowrie.command.input` |
| `2026-06-26 09:05:51` | `cowrie.log.closed` |
| `2026-06-26 09:05:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98cc8fcd848e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:05 |
| **Last Seen** | 2026-06-26 09:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:05:55` | `cowrie.session.connect` |
| `2026-06-26 09:05:55` | `cowrie.client.version` |
| `2026-06-26 09:05:55` | `cowrie.client.kex` |
| `2026-06-26 09:05:55` | `cowrie.login.success` |
| `2026-06-26 09:05:56` | `cowrie.session.params` |
| `2026-06-26 09:05:56` | `cowrie.command.input` |
| `2026-06-26 09:05:57` | `cowrie.log.closed` |
| `2026-06-26 09:05:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-046daa4d106c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:06 |
| **Last Seen** | 2026-06-26 09:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:06:01` | `cowrie.session.connect` |
| `2026-06-26 09:06:01` | `cowrie.client.version` |
| `2026-06-26 09:06:01` | `cowrie.client.kex` |
| `2026-06-26 09:06:01` | `cowrie.login.success` |
| `2026-06-26 09:06:02` | `cowrie.session.params` |
| `2026-06-26 09:06:02` | `cowrie.command.input` |
| `2026-06-26 09:06:02` | `cowrie.log.closed` |
| `2026-06-26 09:06:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b92c61b0524

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:06 |
| **Last Seen** | 2026-06-26 09:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:06:06` | `cowrie.session.connect` |
| `2026-06-26 09:06:06` | `cowrie.client.version` |
| `2026-06-26 09:06:06` | `cowrie.client.kex` |
| `2026-06-26 09:06:07` | `cowrie.login.success` |
| `2026-06-26 09:06:08` | `cowrie.session.params` |
| `2026-06-26 09:06:08` | `cowrie.command.input` |
| `2026-06-26 09:06:08` | `cowrie.log.closed` |
| `2026-06-26 09:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d3f7e0f1947

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:06 |
| **Last Seen** | 2026-06-26 09:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:06:12` | `cowrie.session.connect` |
| `2026-06-26 09:06:12` | `cowrie.client.version` |
| `2026-06-26 09:06:12` | `cowrie.client.kex` |
| `2026-06-26 09:06:12` | `cowrie.login.success` |
| `2026-06-26 09:06:13` | `cowrie.session.params` |
| `2026-06-26 09:06:13` | `cowrie.command.input` |
| `2026-06-26 09:06:13` | `cowrie.log.closed` |
| `2026-06-26 09:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e593e75a501e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:06 |
| **Last Seen** | 2026-06-26 09:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:06:17` | `cowrie.session.connect` |
| `2026-06-26 09:06:17` | `cowrie.client.version` |
| `2026-06-26 09:06:17` | `cowrie.client.kex` |
| `2026-06-26 09:06:18` | `cowrie.login.success` |
| `2026-06-26 09:06:19` | `cowrie.session.params` |
| `2026-06-26 09:06:19` | `cowrie.command.input` |
| `2026-06-26 09:06:19` | `cowrie.log.closed` |
| `2026-06-26 09:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be0e530b0f6d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:06 |
| **Last Seen** | 2026-06-26 09:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:06:23` | `cowrie.session.connect` |
| `2026-06-26 09:06:23` | `cowrie.client.version` |
| `2026-06-26 09:06:23` | `cowrie.client.kex` |
| `2026-06-26 09:06:24` | `cowrie.login.success` |
| `2026-06-26 09:06:24` | `cowrie.session.params` |
| `2026-06-26 09:06:24` | `cowrie.command.input` |
| `2026-06-26 09:06:24` | `cowrie.log.closed` |
| `2026-06-26 09:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5e7bd65678a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:06 |
| **Last Seen** | 2026-06-26 09:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:06:29` | `cowrie.session.connect` |
| `2026-06-26 09:06:29` | `cowrie.client.version` |
| `2026-06-26 09:06:29` | `cowrie.client.kex` |
| `2026-06-26 09:06:29` | `cowrie.login.success` |
| `2026-06-26 09:06:30` | `cowrie.session.params` |
| `2026-06-26 09:06:30` | `cowrie.command.input` |
| `2026-06-26 09:06:30` | `cowrie.log.closed` |
| `2026-06-26 09:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c865986da955

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:06 |
| **Last Seen** | 2026-06-26 09:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:06:34` | `cowrie.session.connect` |
| `2026-06-26 09:06:34` | `cowrie.client.version` |
| `2026-06-26 09:06:34` | `cowrie.client.kex` |
| `2026-06-26 09:06:35` | `cowrie.login.success` |
| `2026-06-26 09:06:36` | `cowrie.session.params` |
| `2026-06-26 09:06:36` | `cowrie.command.input` |
| `2026-06-26 09:06:36` | `cowrie.log.closed` |
| `2026-06-26 09:06:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37dffbe0cb3e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:06 |
| **Last Seen** | 2026-06-26 09:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:06:40` | `cowrie.session.connect` |
| `2026-06-26 09:06:40` | `cowrie.client.version` |
| `2026-06-26 09:06:40` | `cowrie.client.kex` |
| `2026-06-26 09:06:41` | `cowrie.login.success` |
| `2026-06-26 09:06:43` | `cowrie.session.params` |
| `2026-06-26 09:06:43` | `cowrie.command.input` |
| `2026-06-26 09:06:43` | `cowrie.log.closed` |
| `2026-06-26 09:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ab801dc5723

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:06 |
| **Last Seen** | 2026-06-26 09:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:06:40` | `cowrie.session.connect` |
| `2026-06-26 09:06:40` | `cowrie.client.version` |
| `2026-06-26 09:06:40` | `cowrie.client.kex` |
| `2026-06-26 09:06:40` | `cowrie.login.success` |
| `2026-06-26 09:06:41` | `cowrie.session.params` |
| `2026-06-26 09:06:41` | `cowrie.command.input` |
| `2026-06-26 09:06:41` | `cowrie.log.closed` |
| `2026-06-26 09:06:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e969652eafbd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:06 |
| **Last Seen** | 2026-06-26 09:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:06:45` | `cowrie.session.connect` |
| `2026-06-26 09:06:45` | `cowrie.client.version` |
| `2026-06-26 09:06:46` | `cowrie.client.kex` |
| `2026-06-26 09:06:46` | `cowrie.login.success` |
| `2026-06-26 09:06:48` | `cowrie.session.params` |
| `2026-06-26 09:06:48` | `cowrie.command.input` |
| `2026-06-26 09:06:48` | `cowrie.log.closed` |
| `2026-06-26 09:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89ed4cd4698d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:06 |
| **Last Seen** | 2026-06-26 09:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:06:51` | `cowrie.session.connect` |
| `2026-06-26 09:06:51` | `cowrie.client.version` |
| `2026-06-26 09:06:51` | `cowrie.client.kex` |
| `2026-06-26 09:06:52` | `cowrie.login.success` |
| `2026-06-26 09:06:52` | `cowrie.session.params` |
| `2026-06-26 09:06:52` | `cowrie.command.input` |
| `2026-06-26 09:06:53` | `cowrie.log.closed` |
| `2026-06-26 09:06:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6cff2875011

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:06 |
| **Last Seen** | 2026-06-26 09:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:06:57` | `cowrie.session.connect` |
| `2026-06-26 09:06:57` | `cowrie.client.version` |
| `2026-06-26 09:06:57` | `cowrie.client.kex` |
| `2026-06-26 09:06:58` | `cowrie.login.success` |
| `2026-06-26 09:06:59` | `cowrie.session.params` |
| `2026-06-26 09:06:59` | `cowrie.command.input` |
| `2026-06-26 09:06:59` | `cowrie.log.closed` |
| `2026-06-26 09:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7614fbeec029

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:07 |
| **Last Seen** | 2026-06-26 09:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:07:03` | `cowrie.session.connect` |
| `2026-06-26 09:07:03` | `cowrie.client.version` |
| `2026-06-26 09:07:03` | `cowrie.client.kex` |
| `2026-06-26 09:07:04` | `cowrie.login.success` |
| `2026-06-26 09:07:04` | `cowrie.session.params` |
| `2026-06-26 09:07:04` | `cowrie.command.input` |
| `2026-06-26 09:07:05` | `cowrie.log.closed` |
| `2026-06-26 09:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-949c77aeff1c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:07 |
| **Last Seen** | 2026-06-26 09:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:07:09` | `cowrie.session.connect` |
| `2026-06-26 09:07:09` | `cowrie.client.version` |
| `2026-06-26 09:07:09` | `cowrie.client.kex` |
| `2026-06-26 09:07:10` | `cowrie.login.success` |
| `2026-06-26 09:07:11` | `cowrie.session.params` |
| `2026-06-26 09:07:11` | `cowrie.command.input` |
| `2026-06-26 09:07:11` | `cowrie.log.closed` |
| `2026-06-26 09:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe9724fea186

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:07 |
| **Last Seen** | 2026-06-26 09:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:07:14` | `cowrie.session.connect` |
| `2026-06-26 09:07:14` | `cowrie.client.version` |
| `2026-06-26 09:07:14` | `cowrie.client.kex` |
| `2026-06-26 09:07:15` | `cowrie.login.success` |
| `2026-06-26 09:07:16` | `cowrie.session.params` |
| `2026-06-26 09:07:16` | `cowrie.command.input` |
| `2026-06-26 09:07:16` | `cowrie.log.closed` |
| `2026-06-26 09:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-246f0dd799de

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 09:07 |
| **Last Seen** | 2026-06-26 09:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:07:19` | `cowrie.session.connect` |
| `2026-06-26 09:07:19` | `cowrie.client.version` |
| `2026-06-26 09:07:19` | `cowrie.client.kex` |
| `2026-06-26 09:07:20` | `cowrie.login.success` |
| `2026-06-26 09:07:22` | `cowrie.session.params` |
| `2026-06-26 09:07:22` | `cowrie.command.input` |
| `2026-06-26 09:07:23` | `cowrie.log.closed` |
| `2026-06-26 09:07:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26796c4deae4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:07 |
| **Last Seen** | 2026-06-26 09:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:07:20` | `cowrie.session.connect` |
| `2026-06-26 09:07:20` | `cowrie.client.version` |
| `2026-06-26 09:07:20` | `cowrie.client.kex` |
| `2026-06-26 09:07:21` | `cowrie.login.success` |
| `2026-06-26 09:07:21` | `cowrie.session.params` |
| `2026-06-26 09:07:21` | `cowrie.command.input` |
| `2026-06-26 09:07:22` | `cowrie.log.closed` |
| `2026-06-26 09:07:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03e9bb7594cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:07 |
| **Last Seen** | 2026-06-26 09:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:07:26` | `cowrie.session.connect` |
| `2026-06-26 09:07:26` | `cowrie.client.version` |
| `2026-06-26 09:07:26` | `cowrie.client.kex` |
| `2026-06-26 09:07:27` | `cowrie.login.success` |
| `2026-06-26 09:07:28` | `cowrie.session.params` |
| `2026-06-26 09:07:28` | `cowrie.command.input` |
| `2026-06-26 09:07:28` | `cowrie.log.closed` |
| `2026-06-26 09:07:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f876aff7569

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:07 |
| **Last Seen** | 2026-06-26 09:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:07:31` | `cowrie.session.connect` |
| `2026-06-26 09:07:32` | `cowrie.client.version` |
| `2026-06-26 09:07:32` | `cowrie.client.kex` |
| `2026-06-26 09:07:32` | `cowrie.login.success` |
| `2026-06-26 09:07:33` | `cowrie.session.params` |
| `2026-06-26 09:07:33` | `cowrie.command.input` |
| `2026-06-26 09:07:33` | `cowrie.log.closed` |
| `2026-06-26 09:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b88a1975484c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:07 |
| **Last Seen** | 2026-06-26 09:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:07:36` | `cowrie.session.connect` |
| `2026-06-26 09:07:36` | `cowrie.client.version` |
| `2026-06-26 09:07:36` | `cowrie.client.kex` |
| `2026-06-26 09:07:37` | `cowrie.login.success` |
| `2026-06-26 09:07:38` | `cowrie.session.params` |
| `2026-06-26 09:07:38` | `cowrie.command.input` |
| `2026-06-26 09:07:38` | `cowrie.log.closed` |
| `2026-06-26 09:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ddff4d80c5c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:07 |
| **Last Seen** | 2026-06-26 09:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:07:38` | `cowrie.session.connect` |
| `2026-06-26 09:07:38` | `cowrie.client.version` |
| `2026-06-26 09:07:38` | `cowrie.client.kex` |
| `2026-06-26 09:07:38` | `cowrie.login.success` |
| `2026-06-26 09:07:39` | `cowrie.session.params` |
| `2026-06-26 09:07:39` | `cowrie.command.input` |
| `2026-06-26 09:07:39` | `cowrie.log.closed` |
| `2026-06-26 09:07:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ca2ca22d234

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:07 |
| **Last Seen** | 2026-06-26 09:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:07:43` | `cowrie.session.connect` |
| `2026-06-26 09:07:43` | `cowrie.client.version` |
| `2026-06-26 09:07:43` | `cowrie.client.kex` |
| `2026-06-26 09:07:44` | `cowrie.login.success` |
| `2026-06-26 09:07:45` | `cowrie.session.params` |
| `2026-06-26 09:07:45` | `cowrie.command.input` |
| `2026-06-26 09:07:45` | `cowrie.log.closed` |
| `2026-06-26 09:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-962935586b53

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:07 |
| **Last Seen** | 2026-06-26 09:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:07:49` | `cowrie.session.connect` |
| `2026-06-26 09:07:49` | `cowrie.client.version` |
| `2026-06-26 09:07:49` | `cowrie.client.kex` |
| `2026-06-26 09:07:49` | `cowrie.login.success` |
| `2026-06-26 09:07:50` | `cowrie.session.params` |
| `2026-06-26 09:07:50` | `cowrie.command.input` |
| `2026-06-26 09:07:50` | `cowrie.log.closed` |
| `2026-06-26 09:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-894b2d55277f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:07 |
| **Last Seen** | 2026-06-26 09:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:07:55` | `cowrie.session.connect` |
| `2026-06-26 09:07:55` | `cowrie.client.version` |
| `2026-06-26 09:07:55` | `cowrie.client.kex` |
| `2026-06-26 09:07:55` | `cowrie.login.success` |
| `2026-06-26 09:07:56` | `cowrie.session.params` |
| `2026-06-26 09:07:56` | `cowrie.command.input` |
| `2026-06-26 09:07:56` | `cowrie.log.closed` |
| `2026-06-26 09:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-527c4c0ab973

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:08 |
| **Last Seen** | 2026-06-26 09:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:08:00` | `cowrie.session.connect` |
| `2026-06-26 09:08:00` | `cowrie.client.version` |
| `2026-06-26 09:08:00` | `cowrie.client.kex` |
| `2026-06-26 09:08:00` | `cowrie.login.success` |
| `2026-06-26 09:08:02` | `cowrie.session.params` |
| `2026-06-26 09:08:02` | `cowrie.command.input` |
| `2026-06-26 09:08:02` | `cowrie.log.closed` |
| `2026-06-26 09:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83e6dd8c937e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:08 |
| **Last Seen** | 2026-06-26 09:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:08:06` | `cowrie.session.connect` |
| `2026-06-26 09:08:06` | `cowrie.client.version` |
| `2026-06-26 09:08:06` | `cowrie.client.kex` |
| `2026-06-26 09:08:06` | `cowrie.login.success` |
| `2026-06-26 09:08:07` | `cowrie.session.params` |
| `2026-06-26 09:08:07` | `cowrie.command.input` |
| `2026-06-26 09:08:07` | `cowrie.log.closed` |
| `2026-06-26 09:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cfba3829524

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:08 |
| **Last Seen** | 2026-06-26 09:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:08:11` | `cowrie.session.connect` |
| `2026-06-26 09:08:11` | `cowrie.client.version` |
| `2026-06-26 09:08:12` | `cowrie.client.kex` |
| `2026-06-26 09:08:12` | `cowrie.login.success` |
| `2026-06-26 09:08:13` | `cowrie.session.params` |
| `2026-06-26 09:08:13` | `cowrie.command.input` |
| `2026-06-26 09:08:13` | `cowrie.log.closed` |
| `2026-06-26 09:08:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85bbc2f2ff7d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:08 |
| **Last Seen** | 2026-06-26 09:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:08:17` | `cowrie.session.connect` |
| `2026-06-26 09:08:17` | `cowrie.client.version` |
| `2026-06-26 09:08:17` | `cowrie.client.kex` |
| `2026-06-26 09:08:18` | `cowrie.login.success` |
| `2026-06-26 09:08:19` | `cowrie.session.params` |
| `2026-06-26 09:08:19` | `cowrie.command.input` |
| `2026-06-26 09:08:19` | `cowrie.log.closed` |
| `2026-06-26 09:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1397b798a88b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:08 |
| **Last Seen** | 2026-06-26 09:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:08:23` | `cowrie.session.connect` |
| `2026-06-26 09:08:23` | `cowrie.client.version` |
| `2026-06-26 09:08:23` | `cowrie.client.kex` |
| `2026-06-26 09:08:24` | `cowrie.login.success` |
| `2026-06-26 09:08:25` | `cowrie.session.params` |
| `2026-06-26 09:08:25` | `cowrie.command.input` |
| `2026-06-26 09:08:25` | `cowrie.log.closed` |
| `2026-06-26 09:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76505963f832

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:08 |
| **Last Seen** | 2026-06-26 09:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:08:28` | `cowrie.session.connect` |
| `2026-06-26 09:08:28` | `cowrie.client.version` |
| `2026-06-26 09:08:28` | `cowrie.client.kex` |
| `2026-06-26 09:08:29` | `cowrie.login.success` |
| `2026-06-26 09:08:29` | `cowrie.session.params` |
| `2026-06-26 09:08:29` | `cowrie.command.input` |
| `2026-06-26 09:08:30` | `cowrie.log.closed` |
| `2026-06-26 09:08:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf1c9bf7617f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:08 |
| **Last Seen** | 2026-06-26 09:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:08:34` | `cowrie.session.connect` |
| `2026-06-26 09:08:34` | `cowrie.client.version` |
| `2026-06-26 09:08:34` | `cowrie.client.kex` |
| `2026-06-26 09:08:34` | `cowrie.login.success` |
| `2026-06-26 09:08:35` | `cowrie.session.params` |
| `2026-06-26 09:08:35` | `cowrie.command.input` |
| `2026-06-26 09:08:35` | `cowrie.log.closed` |
| `2026-06-26 09:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c005474f44c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:08 |
| **Last Seen** | 2026-06-26 09:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:08:35` | `cowrie.session.connect` |
| `2026-06-26 09:08:35` | `cowrie.client.version` |
| `2026-06-26 09:08:35` | `cowrie.client.kex` |
| `2026-06-26 09:08:35` | `cowrie.login.success` |
| `2026-06-26 09:08:36` | `cowrie.session.params` |
| `2026-06-26 09:08:36` | `cowrie.command.input` |
| `2026-06-26 09:08:36` | `cowrie.log.closed` |
| `2026-06-26 09:08:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ea6df1539a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:08 |
| **Last Seen** | 2026-06-26 09:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:08:39` | `cowrie.session.connect` |
| `2026-06-26 09:08:39` | `cowrie.client.version` |
| `2026-06-26 09:08:39` | `cowrie.client.kex` |
| `2026-06-26 09:08:40` | `cowrie.login.success` |
| `2026-06-26 09:08:41` | `cowrie.session.params` |
| `2026-06-26 09:08:41` | `cowrie.command.input` |
| `2026-06-26 09:08:41` | `cowrie.log.closed` |
| `2026-06-26 09:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23bf5f388bec

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:08 |
| **Last Seen** | 2026-06-26 09:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:08:46` | `cowrie.session.connect` |
| `2026-06-26 09:08:46` | `cowrie.client.version` |
| `2026-06-26 09:08:46` | `cowrie.client.kex` |
| `2026-06-26 09:08:46` | `cowrie.login.success` |
| `2026-06-26 09:08:47` | `cowrie.session.params` |
| `2026-06-26 09:08:47` | `cowrie.command.input` |
| `2026-06-26 09:08:47` | `cowrie.log.closed` |
| `2026-06-26 09:08:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d4c2cf27179

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:08 |
| **Last Seen** | 2026-06-26 09:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:08:51` | `cowrie.session.connect` |
| `2026-06-26 09:08:51` | `cowrie.client.version` |
| `2026-06-26 09:08:52` | `cowrie.client.kex` |
| `2026-06-26 09:08:52` | `cowrie.login.success` |
| `2026-06-26 09:08:53` | `cowrie.session.params` |
| `2026-06-26 09:08:53` | `cowrie.command.input` |
| `2026-06-26 09:08:53` | `cowrie.log.closed` |
| `2026-06-26 09:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-997d4eab1f77

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:08 |
| **Last Seen** | 2026-06-26 09:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:08:57` | `cowrie.session.connect` |
| `2026-06-26 09:08:57` | `cowrie.client.version` |
| `2026-06-26 09:08:57` | `cowrie.client.kex` |
| `2026-06-26 09:08:58` | `cowrie.login.success` |
| `2026-06-26 09:08:59` | `cowrie.session.params` |
| `2026-06-26 09:08:59` | `cowrie.command.input` |
| `2026-06-26 09:08:59` | `cowrie.log.closed` |
| `2026-06-26 09:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46139888f7c6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:09 |
| **Last Seen** | 2026-06-26 09:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:09:02` | `cowrie.session.connect` |
| `2026-06-26 09:09:03` | `cowrie.client.version` |
| `2026-06-26 09:09:03` | `cowrie.client.kex` |
| `2026-06-26 09:09:03` | `cowrie.login.success` |
| `2026-06-26 09:09:04` | `cowrie.session.params` |
| `2026-06-26 09:09:04` | `cowrie.command.input` |
| `2026-06-26 09:09:04` | `cowrie.log.closed` |
| `2026-06-26 09:09:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69bc56a3b546

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:09 |
| **Last Seen** | 2026-06-26 09:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:09:08` | `cowrie.session.connect` |
| `2026-06-26 09:09:08` | `cowrie.client.version` |
| `2026-06-26 09:09:08` | `cowrie.client.kex` |
| `2026-06-26 09:09:09` | `cowrie.login.success` |
| `2026-06-26 09:09:10` | `cowrie.session.params` |
| `2026-06-26 09:09:10` | `cowrie.command.input` |
| `2026-06-26 09:09:10` | `cowrie.log.closed` |
| `2026-06-26 09:09:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c9bf0b04f6d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:09 |
| **Last Seen** | 2026-06-26 09:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:09:14` | `cowrie.session.connect` |
| `2026-06-26 09:09:14` | `cowrie.client.version` |
| `2026-06-26 09:09:14` | `cowrie.client.kex` |
| `2026-06-26 09:09:14` | `cowrie.login.success` |
| `2026-06-26 09:09:16` | `cowrie.session.params` |
| `2026-06-26 09:09:16` | `cowrie.command.input` |
| `2026-06-26 09:09:16` | `cowrie.log.closed` |
| `2026-06-26 09:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d568c67dd74

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:09 |
| **Last Seen** | 2026-06-26 09:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:09:19` | `cowrie.session.connect` |
| `2026-06-26 09:09:19` | `cowrie.client.version` |
| `2026-06-26 09:09:19` | `cowrie.client.kex` |
| `2026-06-26 09:09:20` | `cowrie.login.success` |
| `2026-06-26 09:09:21` | `cowrie.session.params` |
| `2026-06-26 09:09:21` | `cowrie.command.input` |
| `2026-06-26 09:09:21` | `cowrie.log.closed` |
| `2026-06-26 09:09:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cec48d7bf7c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:09 |
| **Last Seen** | 2026-06-26 09:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:09:25` | `cowrie.session.connect` |
| `2026-06-26 09:09:25` | `cowrie.client.version` |
| `2026-06-26 09:09:25` | `cowrie.client.kex` |
| `2026-06-26 09:09:26` | `cowrie.login.success` |
| `2026-06-26 09:09:26` | `cowrie.session.params` |
| `2026-06-26 09:09:26` | `cowrie.command.input` |
| `2026-06-26 09:09:27` | `cowrie.log.closed` |
| `2026-06-26 09:09:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a31e224bb9c6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:09 |
| **Last Seen** | 2026-06-26 09:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:09:31` | `cowrie.session.connect` |
| `2026-06-26 09:09:31` | `cowrie.client.version` |
| `2026-06-26 09:09:31` | `cowrie.client.kex` |
| `2026-06-26 09:09:32` | `cowrie.login.success` |
| `2026-06-26 09:09:33` | `cowrie.session.params` |
| `2026-06-26 09:09:33` | `cowrie.command.input` |
| `2026-06-26 09:09:34` | `cowrie.log.closed` |
| `2026-06-26 09:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56f548645188

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:09 |
| **Last Seen** | 2026-06-26 09:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:09:31` | `cowrie.session.connect` |
| `2026-06-26 09:09:31` | `cowrie.client.version` |
| `2026-06-26 09:09:31` | `cowrie.client.kex` |
| `2026-06-26 09:09:32` | `cowrie.login.success` |
| `2026-06-26 09:09:33` | `cowrie.session.params` |
| `2026-06-26 09:09:33` | `cowrie.command.input` |
| `2026-06-26 09:09:33` | `cowrie.log.closed` |
| `2026-06-26 09:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebee7c5f1ca3

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-26 09:09 |
| **Last Seen** | 2026-06-26 09:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:09:33` | `cowrie.session.connect` |
| `2026-06-26 09:09:33` | `cowrie.client.version` |
| `2026-06-26 09:09:33` | `cowrie.client.kex` |
| `2026-06-26 09:09:33` | `cowrie.login.success` |
| `2026-06-26 09:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f159334a071

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-26 09:09 |
| **Last Seen** | 2026-06-26 09:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:09:33` | `cowrie.session.connect` |
| `2026-06-26 09:09:33` | `cowrie.client.version` |
| `2026-06-26 09:09:33` | `cowrie.client.kex` |
| `2026-06-26 09:09:33` | `cowrie.login.success` |
| `2026-06-26 09:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f35b6fb2e2e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:09 |
| **Last Seen** | 2026-06-26 09:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:09:36` | `cowrie.session.connect` |
| `2026-06-26 09:09:37` | `cowrie.client.version` |
| `2026-06-26 09:09:37` | `cowrie.client.kex` |
| `2026-06-26 09:09:37` | `cowrie.login.success` |
| `2026-06-26 09:09:38` | `cowrie.session.params` |
| `2026-06-26 09:09:38` | `cowrie.command.input` |
| `2026-06-26 09:09:39` | `cowrie.log.closed` |
| `2026-06-26 09:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f050b33a73f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:09 |
| **Last Seen** | 2026-06-26 09:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:09:42` | `cowrie.session.connect` |
| `2026-06-26 09:09:42` | `cowrie.client.version` |
| `2026-06-26 09:09:42` | `cowrie.client.kex` |
| `2026-06-26 09:09:43` | `cowrie.login.success` |
| `2026-06-26 09:09:44` | `cowrie.session.params` |
| `2026-06-26 09:09:44` | `cowrie.command.input` |
| `2026-06-26 09:09:45` | `cowrie.log.closed` |
| `2026-06-26 09:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e354b59256b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-26 09:09 |
| **Last Seen** | 2026-06-26 09:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:09:43` | `cowrie.session.connect` |
| `2026-06-26 09:09:43` | `cowrie.client.version` |
| `2026-06-26 09:09:43` | `cowrie.client.kex` |
| `2026-06-26 09:09:43` | `cowrie.login.success` |
| `2026-06-26 09:09:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d97d4df49963

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-26 09:09 |
| **Last Seen** | 2026-06-26 09:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:09:43` | `cowrie.session.connect` |
| `2026-06-26 09:09:43` | `cowrie.client.version` |
| `2026-06-26 09:09:43` | `cowrie.client.kex` |
| `2026-06-26 09:09:43` | `cowrie.login.success` |
| `2026-06-26 09:09:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de32c0c3048f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:09 |
| **Last Seen** | 2026-06-26 09:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:09:48` | `cowrie.session.connect` |
| `2026-06-26 09:09:48` | `cowrie.client.version` |
| `2026-06-26 09:09:48` | `cowrie.client.kex` |
| `2026-06-26 09:09:49` | `cowrie.login.success` |
| `2026-06-26 09:09:50` | `cowrie.session.params` |
| `2026-06-26 09:09:50` | `cowrie.command.input` |
| `2026-06-26 09:09:50` | `cowrie.log.closed` |
| `2026-06-26 09:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e50479fabb76

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:09 |
| **Last Seen** | 2026-06-26 09:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:09:54` | `cowrie.session.connect` |
| `2026-06-26 09:09:54` | `cowrie.client.version` |
| `2026-06-26 09:09:54` | `cowrie.client.kex` |
| `2026-06-26 09:09:55` | `cowrie.login.success` |
| `2026-06-26 09:09:56` | `cowrie.session.params` |
| `2026-06-26 09:09:56` | `cowrie.command.input` |
| `2026-06-26 09:09:56` | `cowrie.log.closed` |
| `2026-06-26 09:09:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e40df92c3cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:09 |
| **Last Seen** | 2026-06-26 09:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:09:59` | `cowrie.session.connect` |
| `2026-06-26 09:10:00` | `cowrie.client.version` |
| `2026-06-26 09:10:00` | `cowrie.client.kex` |
| `2026-06-26 09:10:00` | `cowrie.login.success` |
| `2026-06-26 09:10:01` | `cowrie.session.params` |
| `2026-06-26 09:10:01` | `cowrie.command.input` |
| `2026-06-26 09:10:01` | `cowrie.log.closed` |
| `2026-06-26 09:10:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f23c778dbed

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:10 |
| **Last Seen** | 2026-06-26 09:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:10:05` | `cowrie.session.connect` |
| `2026-06-26 09:10:05` | `cowrie.client.version` |
| `2026-06-26 09:10:05` | `cowrie.client.kex` |
| `2026-06-26 09:10:06` | `cowrie.login.success` |
| `2026-06-26 09:10:07` | `cowrie.session.params` |
| `2026-06-26 09:10:07` | `cowrie.command.input` |
| `2026-06-26 09:10:07` | `cowrie.log.closed` |
| `2026-06-26 09:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0e654865c64

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:10 |
| **Last Seen** | 2026-06-26 09:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:10:10` | `cowrie.session.connect` |
| `2026-06-26 09:10:11` | `cowrie.client.version` |
| `2026-06-26 09:10:11` | `cowrie.client.kex` |
| `2026-06-26 09:10:11` | `cowrie.login.success` |
| `2026-06-26 09:10:12` | `cowrie.session.params` |
| `2026-06-26 09:10:12` | `cowrie.command.input` |
| `2026-06-26 09:10:12` | `cowrie.log.closed` |
| `2026-06-26 09:10:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91c220245a97

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:10 |
| **Last Seen** | 2026-06-26 09:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:10:16` | `cowrie.session.connect` |
| `2026-06-26 09:10:16` | `cowrie.client.version` |
| `2026-06-26 09:10:16` | `cowrie.client.kex` |
| `2026-06-26 09:10:17` | `cowrie.login.success` |
| `2026-06-26 09:10:17` | `cowrie.session.params` |
| `2026-06-26 09:10:17` | `cowrie.command.input` |
| `2026-06-26 09:10:18` | `cowrie.log.closed` |
| `2026-06-26 09:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66de4c027eb3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:10 |
| **Last Seen** | 2026-06-26 09:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:10:22` | `cowrie.session.connect` |
| `2026-06-26 09:10:22` | `cowrie.client.version` |
| `2026-06-26 09:10:22` | `cowrie.client.kex` |
| `2026-06-26 09:10:23` | `cowrie.login.success` |
| `2026-06-26 09:10:24` | `cowrie.session.params` |
| `2026-06-26 09:10:24` | `cowrie.command.input` |
| `2026-06-26 09:10:24` | `cowrie.log.closed` |
| `2026-06-26 09:10:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d35a9f117ea6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:10 |
| **Last Seen** | 2026-06-26 09:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:10:27` | `cowrie.session.connect` |
| `2026-06-26 09:10:27` | `cowrie.client.version` |
| `2026-06-26 09:10:27` | `cowrie.client.kex` |
| `2026-06-26 09:10:29` | `cowrie.login.success` |
| `2026-06-26 09:10:30` | `cowrie.session.params` |
| `2026-06-26 09:10:30` | `cowrie.command.input` |
| `2026-06-26 09:10:30` | `cowrie.log.closed` |
| `2026-06-26 09:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e798c9af2518

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:10 |
| **Last Seen** | 2026-06-26 09:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:10:27` | `cowrie.session.connect` |
| `2026-06-26 09:10:27` | `cowrie.client.version` |
| `2026-06-26 09:10:27` | `cowrie.client.kex` |
| `2026-06-26 09:10:27` | `cowrie.login.success` |
| `2026-06-26 09:10:28` | `cowrie.session.params` |
| `2026-06-26 09:10:28` | `cowrie.command.input` |
| `2026-06-26 09:10:28` | `cowrie.log.closed` |
| `2026-06-26 09:10:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92c790a10e8e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:10 |
| **Last Seen** | 2026-06-26 09:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:10:32` | `cowrie.session.connect` |
| `2026-06-26 09:10:33` | `cowrie.client.version` |
| `2026-06-26 09:10:33` | `cowrie.client.kex` |
| `2026-06-26 09:10:33` | `cowrie.login.success` |
| `2026-06-26 09:10:35` | `cowrie.session.params` |
| `2026-06-26 09:10:35` | `cowrie.command.input` |
| `2026-06-26 09:10:35` | `cowrie.log.closed` |
| `2026-06-26 09:10:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2edc0252e98b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:10 |
| **Last Seen** | 2026-06-26 09:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:10:38` | `cowrie.session.connect` |
| `2026-06-26 09:10:38` | `cowrie.client.version` |
| `2026-06-26 09:10:39` | `cowrie.client.kex` |
| `2026-06-26 09:10:39` | `cowrie.login.success` |
| `2026-06-26 09:10:40` | `cowrie.session.params` |
| `2026-06-26 09:10:40` | `cowrie.command.input` |
| `2026-06-26 09:10:40` | `cowrie.log.closed` |
| `2026-06-26 09:10:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-105e11e5601f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:10 |
| **Last Seen** | 2026-06-26 09:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:10:44` | `cowrie.session.connect` |
| `2026-06-26 09:10:44` | `cowrie.client.version` |
| `2026-06-26 09:10:44` | `cowrie.client.kex` |
| `2026-06-26 09:10:45` | `cowrie.login.success` |
| `2026-06-26 09:10:46` | `cowrie.session.params` |
| `2026-06-26 09:10:46` | `cowrie.command.input` |
| `2026-06-26 09:10:46` | `cowrie.log.closed` |
| `2026-06-26 09:10:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e94eea3e081f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:10 |
| **Last Seen** | 2026-06-26 09:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:10:49` | `cowrie.session.connect` |
| `2026-06-26 09:10:49` | `cowrie.client.version` |
| `2026-06-26 09:10:50` | `cowrie.client.kex` |
| `2026-06-26 09:10:50` | `cowrie.login.success` |
| `2026-06-26 09:10:51` | `cowrie.session.params` |
| `2026-06-26 09:10:51` | `cowrie.command.input` |
| `2026-06-26 09:10:51` | `cowrie.log.closed` |
| `2026-06-26 09:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c1e1f433755

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:10 |
| **Last Seen** | 2026-06-26 09:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:10:55` | `cowrie.session.connect` |
| `2026-06-26 09:10:55` | `cowrie.client.version` |
| `2026-06-26 09:10:55` | `cowrie.client.kex` |
| `2026-06-26 09:10:56` | `cowrie.login.success` |
| `2026-06-26 09:10:56` | `cowrie.session.params` |
| `2026-06-26 09:10:56` | `cowrie.command.input` |
| `2026-06-26 09:10:57` | `cowrie.log.closed` |
| `2026-06-26 09:10:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0e7b8105c76

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:11 |
| **Last Seen** | 2026-06-26 09:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:11:01` | `cowrie.session.connect` |
| `2026-06-26 09:11:01` | `cowrie.client.version` |
| `2026-06-26 09:11:01` | `cowrie.client.kex` |
| `2026-06-26 09:11:01` | `cowrie.login.success` |
| `2026-06-26 09:11:02` | `cowrie.session.params` |
| `2026-06-26 09:11:02` | `cowrie.command.input` |
| `2026-06-26 09:11:02` | `cowrie.log.closed` |
| `2026-06-26 09:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-615a530bff9f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:11 |
| **Last Seen** | 2026-06-26 09:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:11:06` | `cowrie.session.connect` |
| `2026-06-26 09:11:06` | `cowrie.client.version` |
| `2026-06-26 09:11:06` | `cowrie.client.kex` |
| `2026-06-26 09:11:07` | `cowrie.login.success` |
| `2026-06-26 09:11:08` | `cowrie.session.params` |
| `2026-06-26 09:11:08` | `cowrie.command.input` |
| `2026-06-26 09:11:08` | `cowrie.log.closed` |
| `2026-06-26 09:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b9bdd64060a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:11 |
| **Last Seen** | 2026-06-26 09:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:11:12` | `cowrie.session.connect` |
| `2026-06-26 09:11:12` | `cowrie.client.version` |
| `2026-06-26 09:11:12` | `cowrie.client.kex` |
| `2026-06-26 09:11:13` | `cowrie.login.success` |
| `2026-06-26 09:11:14` | `cowrie.session.params` |
| `2026-06-26 09:11:14` | `cowrie.command.input` |
| `2026-06-26 09:11:14` | `cowrie.log.closed` |
| `2026-06-26 09:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2d9e3074e25

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 09:11 |
| **Last Seen** | 2026-06-26 09:12 |
| **Session Duration** | 73s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:11:15` | `cowrie.session.connect` |
| `2026-06-26 09:11:16` | `cowrie.client.version` |
| `2026-06-26 09:11:16` | `cowrie.client.kex` |
| `2026-06-26 09:11:22` | `cowrie.login.success` |
| `2026-06-26 09:11:25` | `cowrie.session.params` |
| `2026-06-26 09:11:25` | `cowrie.command.input` |
| `2026-06-26 09:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d30171c5e2e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:11 |
| **Last Seen** | 2026-06-26 09:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:11:18` | `cowrie.session.connect` |
| `2026-06-26 09:11:18` | `cowrie.client.version` |
| `2026-06-26 09:11:18` | `cowrie.client.kex` |
| `2026-06-26 09:11:18` | `cowrie.login.success` |
| `2026-06-26 09:11:19` | `cowrie.session.params` |
| `2026-06-26 09:11:19` | `cowrie.command.input` |
| `2026-06-26 09:11:19` | `cowrie.log.closed` |
| `2026-06-26 09:11:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5941695a4296

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:11 |
| **Last Seen** | 2026-06-26 09:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:11:23` | `cowrie.session.connect` |
| `2026-06-26 09:11:23` | `cowrie.client.version` |
| `2026-06-26 09:11:23` | `cowrie.client.kex` |
| `2026-06-26 09:11:24` | `cowrie.login.success` |
| `2026-06-26 09:11:25` | `cowrie.session.params` |
| `2026-06-26 09:11:25` | `cowrie.command.input` |
| `2026-06-26 09:11:25` | `cowrie.log.closed` |
| `2026-06-26 09:11:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e58d3fa7e5bb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:11 |
| **Last Seen** | 2026-06-26 09:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:11:25` | `cowrie.session.connect` |
| `2026-06-26 09:11:25` | `cowrie.client.version` |
| `2026-06-26 09:11:25` | `cowrie.client.kex` |
| `2026-06-26 09:11:26` | `cowrie.login.success` |
| `2026-06-26 09:11:27` | `cowrie.session.params` |
| `2026-06-26 09:11:27` | `cowrie.command.input` |
| `2026-06-26 09:11:27` | `cowrie.log.closed` |
| `2026-06-26 09:11:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-514d5c2d8b0d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:11 |
| **Last Seen** | 2026-06-26 09:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:11:29` | `cowrie.session.connect` |
| `2026-06-26 09:11:29` | `cowrie.client.version` |
| `2026-06-26 09:11:29` | `cowrie.client.kex` |
| `2026-06-26 09:11:30` | `cowrie.login.success` |
| `2026-06-26 09:11:30` | `cowrie.session.params` |
| `2026-06-26 09:11:30` | `cowrie.command.input` |
| `2026-06-26 09:11:31` | `cowrie.log.closed` |
| `2026-06-26 09:11:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-632d725bb437

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:11 |
| **Last Seen** | 2026-06-26 09:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:11:34` | `cowrie.session.connect` |
| `2026-06-26 09:11:35` | `cowrie.client.version` |
| `2026-06-26 09:11:35` | `cowrie.client.kex` |
| `2026-06-26 09:11:35` | `cowrie.login.success` |
| `2026-06-26 09:11:36` | `cowrie.session.params` |
| `2026-06-26 09:11:36` | `cowrie.command.input` |
| `2026-06-26 09:11:36` | `cowrie.log.closed` |
| `2026-06-26 09:11:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78ca8a34f233

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:11 |
| **Last Seen** | 2026-06-26 09:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:11:40` | `cowrie.session.connect` |
| `2026-06-26 09:11:40` | `cowrie.client.version` |
| `2026-06-26 09:11:40` | `cowrie.client.kex` |
| `2026-06-26 09:11:41` | `cowrie.login.success` |
| `2026-06-26 09:11:42` | `cowrie.session.params` |
| `2026-06-26 09:11:42` | `cowrie.command.input` |
| `2026-06-26 09:11:42` | `cowrie.log.closed` |
| `2026-06-26 09:11:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aab50f5bdfd5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:11 |
| **Last Seen** | 2026-06-26 09:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:11:46` | `cowrie.session.connect` |
| `2026-06-26 09:11:46` | `cowrie.client.version` |
| `2026-06-26 09:11:46` | `cowrie.client.kex` |
| `2026-06-26 09:11:47` | `cowrie.login.success` |
| `2026-06-26 09:11:48` | `cowrie.session.params` |
| `2026-06-26 09:11:48` | `cowrie.command.input` |
| `2026-06-26 09:11:48` | `cowrie.log.closed` |
| `2026-06-26 09:11:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43df9555c077

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:11 |
| **Last Seen** | 2026-06-26 09:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:11:51` | `cowrie.session.connect` |
| `2026-06-26 09:11:52` | `cowrie.client.version` |
| `2026-06-26 09:11:52` | `cowrie.client.kex` |
| `2026-06-26 09:11:52` | `cowrie.login.success` |
| `2026-06-26 09:11:53` | `cowrie.session.params` |
| `2026-06-26 09:11:53` | `cowrie.command.input` |
| `2026-06-26 09:11:53` | `cowrie.log.closed` |
| `2026-06-26 09:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dc53b491185

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:11 |
| **Last Seen** | 2026-06-26 09:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:11:57` | `cowrie.session.connect` |
| `2026-06-26 09:11:57` | `cowrie.client.version` |
| `2026-06-26 09:11:57` | `cowrie.client.kex` |
| `2026-06-26 09:11:58` | `cowrie.login.success` |
| `2026-06-26 09:11:59` | `cowrie.session.params` |
| `2026-06-26 09:11:59` | `cowrie.command.input` |
| `2026-06-26 09:11:59` | `cowrie.log.closed` |
| `2026-06-26 09:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb684c3dd767

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:12 |
| **Last Seen** | 2026-06-26 09:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:12:03` | `cowrie.session.connect` |
| `2026-06-26 09:12:03` | `cowrie.client.version` |
| `2026-06-26 09:12:03` | `cowrie.client.kex` |
| `2026-06-26 09:12:03` | `cowrie.login.success` |
| `2026-06-26 09:12:04` | `cowrie.session.params` |
| `2026-06-26 09:12:04` | `cowrie.command.input` |
| `2026-06-26 09:12:04` | `cowrie.log.closed` |
| `2026-06-26 09:12:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f94d78e587d2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:12 |
| **Last Seen** | 2026-06-26 09:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:12:09` | `cowrie.session.connect` |
| `2026-06-26 09:12:09` | `cowrie.client.version` |
| `2026-06-26 09:12:09` | `cowrie.client.kex` |
| `2026-06-26 09:12:09` | `cowrie.login.success` |
| `2026-06-26 09:12:10` | `cowrie.session.params` |
| `2026-06-26 09:12:10` | `cowrie.command.input` |
| `2026-06-26 09:12:10` | `cowrie.log.closed` |
| `2026-06-26 09:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-727dddccc11d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:12 |
| **Last Seen** | 2026-06-26 09:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:12:14` | `cowrie.session.connect` |
| `2026-06-26 09:12:14` | `cowrie.client.version` |
| `2026-06-26 09:12:14` | `cowrie.client.kex` |
| `2026-06-26 09:12:15` | `cowrie.login.success` |
| `2026-06-26 09:12:16` | `cowrie.session.params` |
| `2026-06-26 09:12:16` | `cowrie.command.input` |
| `2026-06-26 09:12:16` | `cowrie.log.closed` |
| `2026-06-26 09:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26be789c67ce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:12 |
| **Last Seen** | 2026-06-26 09:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:12:20` | `cowrie.session.connect` |
| `2026-06-26 09:12:20` | `cowrie.client.version` |
| `2026-06-26 09:12:20` | `cowrie.client.kex` |
| `2026-06-26 09:12:20` | `cowrie.login.success` |
| `2026-06-26 09:12:21` | `cowrie.session.params` |
| `2026-06-26 09:12:21` | `cowrie.command.input` |
| `2026-06-26 09:12:21` | `cowrie.log.closed` |
| `2026-06-26 09:12:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-849a83193768

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:12 |
| **Last Seen** | 2026-06-26 09:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:12:23` | `cowrie.session.connect` |
| `2026-06-26 09:12:23` | `cowrie.client.version` |
| `2026-06-26 09:12:23` | `cowrie.client.kex` |
| `2026-06-26 09:12:23` | `cowrie.login.success` |
| `2026-06-26 09:12:24` | `cowrie.session.params` |
| `2026-06-26 09:12:24` | `cowrie.command.input` |
| `2026-06-26 09:12:24` | `cowrie.log.closed` |
| `2026-06-26 09:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76d8d880236d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:12 |
| **Last Seen** | 2026-06-26 09:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:12:25` | `cowrie.session.connect` |
| `2026-06-26 09:12:25` | `cowrie.client.version` |
| `2026-06-26 09:12:25` | `cowrie.client.kex` |
| `2026-06-26 09:12:26` | `cowrie.login.success` |
| `2026-06-26 09:12:26` | `cowrie.session.params` |
| `2026-06-26 09:12:26` | `cowrie.command.input` |
| `2026-06-26 09:12:27` | `cowrie.log.closed` |
| `2026-06-26 09:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c6fc0269f11

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:12 |
| **Last Seen** | 2026-06-26 09:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:12:31` | `cowrie.session.connect` |
| `2026-06-26 09:12:31` | `cowrie.client.version` |
| `2026-06-26 09:12:31` | `cowrie.client.kex` |
| `2026-06-26 09:12:32` | `cowrie.login.success` |
| `2026-06-26 09:12:33` | `cowrie.session.params` |
| `2026-06-26 09:12:33` | `cowrie.command.input` |
| `2026-06-26 09:12:33` | `cowrie.log.closed` |
| `2026-06-26 09:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-088d029ad6d2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:12 |
| **Last Seen** | 2026-06-26 09:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:12:37` | `cowrie.session.connect` |
| `2026-06-26 09:12:37` | `cowrie.client.version` |
| `2026-06-26 09:12:37` | `cowrie.client.kex` |
| `2026-06-26 09:12:37` | `cowrie.login.success` |
| `2026-06-26 09:12:39` | `cowrie.session.params` |
| `2026-06-26 09:12:39` | `cowrie.command.input` |
| `2026-06-26 09:12:39` | `cowrie.log.closed` |
| `2026-06-26 09:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c22930ae228a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:12 |
| **Last Seen** | 2026-06-26 09:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:12:42` | `cowrie.session.connect` |
| `2026-06-26 09:12:42` | `cowrie.client.version` |
| `2026-06-26 09:12:42` | `cowrie.client.kex` |
| `2026-06-26 09:12:43` | `cowrie.login.success` |
| `2026-06-26 09:12:43` | `cowrie.session.params` |
| `2026-06-26 09:12:43` | `cowrie.command.input` |
| `2026-06-26 09:12:44` | `cowrie.log.closed` |
| `2026-06-26 09:12:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a76f34e6c72

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:12 |
| **Last Seen** | 2026-06-26 09:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:12:48` | `cowrie.session.connect` |
| `2026-06-26 09:12:48` | `cowrie.client.version` |
| `2026-06-26 09:12:48` | `cowrie.client.kex` |
| `2026-06-26 09:12:49` | `cowrie.login.success` |
| `2026-06-26 09:12:50` | `cowrie.session.params` |
| `2026-06-26 09:12:50` | `cowrie.command.input` |
| `2026-06-26 09:12:50` | `cowrie.log.closed` |
| `2026-06-26 09:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d17a4aeddac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:12 |
| **Last Seen** | 2026-06-26 09:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:12:53` | `cowrie.session.connect` |
| `2026-06-26 09:12:53` | `cowrie.client.version` |
| `2026-06-26 09:12:53` | `cowrie.client.kex` |
| `2026-06-26 09:12:54` | `cowrie.login.success` |
| `2026-06-26 09:12:55` | `cowrie.session.params` |
| `2026-06-26 09:12:55` | `cowrie.command.input` |
| `2026-06-26 09:12:55` | `cowrie.log.closed` |
| `2026-06-26 09:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6392688cee6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:12 |
| **Last Seen** | 2026-06-26 09:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:12:59` | `cowrie.session.connect` |
| `2026-06-26 09:12:59` | `cowrie.client.version` |
| `2026-06-26 09:12:59` | `cowrie.client.kex` |
| `2026-06-26 09:12:59` | `cowrie.login.success` |
| `2026-06-26 09:13:00` | `cowrie.session.params` |
| `2026-06-26 09:13:00` | `cowrie.command.input` |
| `2026-06-26 09:13:01` | `cowrie.log.closed` |
| `2026-06-26 09:13:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-221e097bf8e4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:13 |
| **Last Seen** | 2026-06-26 09:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:13:04` | `cowrie.session.connect` |
| `2026-06-26 09:13:04` | `cowrie.client.version` |
| `2026-06-26 09:13:04` | `cowrie.client.kex` |
| `2026-06-26 09:13:05` | `cowrie.login.success` |
| `2026-06-26 09:13:06` | `cowrie.session.params` |
| `2026-06-26 09:13:06` | `cowrie.command.input` |
| `2026-06-26 09:13:06` | `cowrie.log.closed` |
| `2026-06-26 09:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-582848f5ec97

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:13 |
| **Last Seen** | 2026-06-26 09:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:13:10` | `cowrie.session.connect` |
| `2026-06-26 09:13:10` | `cowrie.client.version` |
| `2026-06-26 09:13:10` | `cowrie.client.kex` |
| `2026-06-26 09:13:11` | `cowrie.login.success` |
| `2026-06-26 09:13:12` | `cowrie.session.params` |
| `2026-06-26 09:13:12` | `cowrie.command.input` |
| `2026-06-26 09:13:12` | `cowrie.log.closed` |
| `2026-06-26 09:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0e059436888

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 09:13 |
| **Last Seen** | 2026-06-26 09:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:13:16` | `cowrie.session.connect` |
| `2026-06-26 09:13:16` | `cowrie.client.version` |
| `2026-06-26 09:13:16` | `cowrie.client.kex` |
| `2026-06-26 09:13:16` | `cowrie.login.success` |
| `2026-06-26 09:13:17` | `cowrie.session.params` |
| `2026-06-26 09:13:17` | `cowrie.command.input` |
| `2026-06-26 09:13:18` | `cowrie.log.closed` |
| `2026-06-26 09:13:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70d7a458dd10

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:13 |
| **Last Seen** | 2026-06-26 09:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:13:21` | `cowrie.session.connect` |
| `2026-06-26 09:13:21` | `cowrie.client.version` |
| `2026-06-26 09:13:21` | `cowrie.client.kex` |
| `2026-06-26 09:13:22` | `cowrie.login.success` |
| `2026-06-26 09:13:22` | `cowrie.session.params` |
| `2026-06-26 09:13:22` | `cowrie.command.input` |
| `2026-06-26 09:13:23` | `cowrie.log.closed` |
| `2026-06-26 09:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-553cc72a39f9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:14 |
| **Last Seen** | 2026-06-26 09:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:14:20` | `cowrie.session.connect` |
| `2026-06-26 09:14:20` | `cowrie.client.version` |
| `2026-06-26 09:14:20` | `cowrie.client.kex` |
| `2026-06-26 09:14:20` | `cowrie.login.success` |
| `2026-06-26 09:14:21` | `cowrie.session.params` |
| `2026-06-26 09:14:21` | `cowrie.command.input` |
| `2026-06-26 09:14:21` | `cowrie.log.closed` |
| `2026-06-26 09:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31fbaee84530

| Field | Detail |
|---|---|
| **Source IP** | `47.253.156[.]31` |
| **First Seen** | 2026-06-26 09:14 |
| **Last Seen** | 2026-06-26 09:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:14:27` | `cowrie.session.connect` |
| `2026-06-26 09:14:27` | `cowrie.client.version` |
| `2026-06-26 09:14:32` | `cowrie.client.kex` |
| `2026-06-26 09:14:32` | `cowrie.login.success` |
| `2026-06-26 09:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.253.156[.]31` to AbuseIPDB if not already reported
- [ ] Block `47.253.156[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e0cd7297a4f

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-26 09:14 |
| **Last Seen** | 2026-06-26 09:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:14:33` | `cowrie.session.connect` |
| `2026-06-26 09:14:33` | `cowrie.client.version` |
| `2026-06-26 09:14:33` | `cowrie.client.kex` |
| `2026-06-26 09:14:33` | `cowrie.login.success` |
| `2026-06-26 09:14:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e852acbbecbe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:15 |
| **Last Seen** | 2026-06-26 09:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:15:22` | `cowrie.session.connect` |
| `2026-06-26 09:15:22` | `cowrie.client.version` |
| `2026-06-26 09:15:22` | `cowrie.client.kex` |
| `2026-06-26 09:15:22` | `cowrie.login.success` |
| `2026-06-26 09:15:23` | `cowrie.session.params` |
| `2026-06-26 09:15:23` | `cowrie.command.input` |
| `2026-06-26 09:15:23` | `cowrie.log.closed` |
| `2026-06-26 09:15:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc42c784e31e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:16 |
| **Last Seen** | 2026-06-26 09:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:16:20` | `cowrie.session.connect` |
| `2026-06-26 09:16:20` | `cowrie.client.version` |
| `2026-06-26 09:16:20` | `cowrie.client.kex` |
| `2026-06-26 09:16:20` | `cowrie.login.success` |
| `2026-06-26 09:16:21` | `cowrie.session.params` |
| `2026-06-26 09:16:21` | `cowrie.command.input` |
| `2026-06-26 09:16:21` | `cowrie.log.closed` |
| `2026-06-26 09:16:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e7e9633c452

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:17 |
| **Last Seen** | 2026-06-26 09:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:17:17` | `cowrie.session.connect` |
| `2026-06-26 09:17:17` | `cowrie.client.version` |
| `2026-06-26 09:17:17` | `cowrie.client.kex` |
| `2026-06-26 09:17:17` | `cowrie.login.success` |
| `2026-06-26 09:17:18` | `cowrie.session.params` |
| `2026-06-26 09:17:18` | `cowrie.command.input` |
| `2026-06-26 09:17:18` | `cowrie.log.closed` |
| `2026-06-26 09:17:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a194611b31ab

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:18 |
| **Last Seen** | 2026-06-26 09:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:18:14` | `cowrie.session.connect` |
| `2026-06-26 09:18:14` | `cowrie.client.version` |
| `2026-06-26 09:18:14` | `cowrie.client.kex` |
| `2026-06-26 09:18:15` | `cowrie.login.success` |
| `2026-06-26 09:18:15` | `cowrie.session.params` |
| `2026-06-26 09:18:15` | `cowrie.command.input` |
| `2026-06-26 09:18:15` | `cowrie.log.closed` |
| `2026-06-26 09:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b612e463fe0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:19 |
| **Last Seen** | 2026-06-26 09:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:19:13` | `cowrie.session.connect` |
| `2026-06-26 09:19:13` | `cowrie.client.version` |
| `2026-06-26 09:19:13` | `cowrie.client.kex` |
| `2026-06-26 09:19:13` | `cowrie.login.success` |
| `2026-06-26 09:19:14` | `cowrie.session.params` |
| `2026-06-26 09:19:14` | `cowrie.command.input` |
| `2026-06-26 09:19:14` | `cowrie.log.closed` |
| `2026-06-26 09:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb98d5de6ecc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:20 |
| **Last Seen** | 2026-06-26 09:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:20:11` | `cowrie.session.connect` |
| `2026-06-26 09:20:11` | `cowrie.client.version` |
| `2026-06-26 09:20:12` | `cowrie.client.kex` |
| `2026-06-26 09:20:12` | `cowrie.login.success` |
| `2026-06-26 09:20:13` | `cowrie.session.params` |
| `2026-06-26 09:20:13` | `cowrie.command.input` |
| `2026-06-26 09:20:13` | `cowrie.log.closed` |
| `2026-06-26 09:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72909d1cdf28

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:21 |
| **Last Seen** | 2026-06-26 09:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:21:11` | `cowrie.session.connect` |
| `2026-06-26 09:21:11` | `cowrie.client.version` |
| `2026-06-26 09:21:11` | `cowrie.client.kex` |
| `2026-06-26 09:21:11` | `cowrie.login.success` |
| `2026-06-26 09:21:12` | `cowrie.session.params` |
| `2026-06-26 09:21:12` | `cowrie.command.input` |
| `2026-06-26 09:21:12` | `cowrie.log.closed` |
| `2026-06-26 09:21:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1acfa6b6fe8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:22 |
| **Last Seen** | 2026-06-26 09:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:22:08` | `cowrie.session.connect` |
| `2026-06-26 09:22:08` | `cowrie.client.version` |
| `2026-06-26 09:22:08` | `cowrie.client.kex` |
| `2026-06-26 09:22:09` | `cowrie.login.success` |
| `2026-06-26 09:22:10` | `cowrie.session.params` |
| `2026-06-26 09:22:10` | `cowrie.command.input` |
| `2026-06-26 09:22:10` | `cowrie.log.closed` |
| `2026-06-26 09:22:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d86c7b31643b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:23 |
| **Last Seen** | 2026-06-26 09:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:23:07` | `cowrie.session.connect` |
| `2026-06-26 09:23:07` | `cowrie.client.version` |
| `2026-06-26 09:23:07` | `cowrie.client.kex` |
| `2026-06-26 09:23:07` | `cowrie.login.success` |
| `2026-06-26 09:23:08` | `cowrie.session.params` |
| `2026-06-26 09:23:08` | `cowrie.command.input` |
| `2026-06-26 09:23:08` | `cowrie.log.closed` |
| `2026-06-26 09:23:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffc285549c5d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:24 |
| **Last Seen** | 2026-06-26 09:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:24:07` | `cowrie.session.connect` |
| `2026-06-26 09:24:07` | `cowrie.client.version` |
| `2026-06-26 09:24:07` | `cowrie.client.kex` |
| `2026-06-26 09:24:08` | `cowrie.login.success` |
| `2026-06-26 09:24:08` | `cowrie.session.params` |
| `2026-06-26 09:24:08` | `cowrie.command.input` |
| `2026-06-26 09:24:09` | `cowrie.log.closed` |
| `2026-06-26 09:24:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efb311a545f3

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 09:24 |
| **Last Seen** | 2026-06-26 09:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:24:40` | `cowrie.session.connect` |
| `2026-06-26 09:24:40` | `cowrie.client.version` |
| `2026-06-26 09:24:40` | `cowrie.client.kex` |
| `2026-06-26 09:24:42` | `cowrie.login.success` |
| `2026-06-26 09:24:44` | `cowrie.session.params` |
| `2026-06-26 09:24:44` | `cowrie.command.input` |
| `2026-06-26 09:24:44` | `cowrie.log.closed` |
| `2026-06-26 09:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64a6e488b452

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:25 |
| **Last Seen** | 2026-06-26 09:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:25:09` | `cowrie.session.connect` |
| `2026-06-26 09:25:09` | `cowrie.client.version` |
| `2026-06-26 09:25:09` | `cowrie.client.kex` |
| `2026-06-26 09:25:10` | `cowrie.login.success` |
| `2026-06-26 09:25:10` | `cowrie.session.params` |
| `2026-06-26 09:25:10` | `cowrie.command.input` |
| `2026-06-26 09:25:10` | `cowrie.log.closed` |
| `2026-06-26 09:25:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38aace80219d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:26 |
| **Last Seen** | 2026-06-26 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:26:11` | `cowrie.session.connect` |
| `2026-06-26 09:26:11` | `cowrie.client.version` |
| `2026-06-26 09:26:11` | `cowrie.client.kex` |
| `2026-06-26 09:26:11` | `cowrie.login.success` |
| `2026-06-26 09:26:12` | `cowrie.session.params` |
| `2026-06-26 09:26:12` | `cowrie.command.input` |
| `2026-06-26 09:26:12` | `cowrie.log.closed` |
| `2026-06-26 09:26:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3ef787966c9

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 09:26 |
| **Last Seen** | 2026-06-26 09:26 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:26:18` | `cowrie.session.connect` |
| `2026-06-26 09:26:19` | `cowrie.client.version` |
| `2026-06-26 09:26:19` | `cowrie.client.kex` |
| `2026-06-26 09:26:25` | `cowrie.login.success` |
| `2026-06-26 09:26:28` | `cowrie.session.params` |
| `2026-06-26 09:26:28` | `cowrie.command.input` |
| `2026-06-26 09:26:29` | `cowrie.log.closed` |
| `2026-06-26 09:26:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a981a716bf37

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:27 |
| **Last Seen** | 2026-06-26 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:27:12` | `cowrie.session.connect` |
| `2026-06-26 09:27:12` | `cowrie.client.version` |
| `2026-06-26 09:27:12` | `cowrie.client.kex` |
| `2026-06-26 09:27:12` | `cowrie.login.success` |
| `2026-06-26 09:27:13` | `cowrie.session.params` |
| `2026-06-26 09:27:13` | `cowrie.command.input` |
| `2026-06-26 09:27:13` | `cowrie.log.closed` |
| `2026-06-26 09:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57e0e620121c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:28 |
| **Last Seen** | 2026-06-26 09:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:28:11` | `cowrie.session.connect` |
| `2026-06-26 09:28:11` | `cowrie.client.version` |
| `2026-06-26 09:28:11` | `cowrie.client.kex` |
| `2026-06-26 09:28:11` | `cowrie.login.success` |
| `2026-06-26 09:28:12` | `cowrie.session.params` |
| `2026-06-26 09:28:12` | `cowrie.command.input` |
| `2026-06-26 09:28:12` | `cowrie.log.closed` |
| `2026-06-26 09:28:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f84821721f22

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:29 |
| **Last Seen** | 2026-06-26 09:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:29:10` | `cowrie.session.connect` |
| `2026-06-26 09:29:10` | `cowrie.client.version` |
| `2026-06-26 09:29:10` | `cowrie.client.kex` |
| `2026-06-26 09:29:10` | `cowrie.login.success` |
| `2026-06-26 09:29:11` | `cowrie.session.params` |
| `2026-06-26 09:29:11` | `cowrie.command.input` |
| `2026-06-26 09:29:11` | `cowrie.log.closed` |
| `2026-06-26 09:29:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f766b45be680

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:30 |
| **Last Seen** | 2026-06-26 09:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:30:09` | `cowrie.session.connect` |
| `2026-06-26 09:30:09` | `cowrie.client.version` |
| `2026-06-26 09:30:09` | `cowrie.client.kex` |
| `2026-06-26 09:30:10` | `cowrie.login.success` |
| `2026-06-26 09:30:10` | `cowrie.session.params` |
| `2026-06-26 09:30:10` | `cowrie.command.input` |
| `2026-06-26 09:30:11` | `cowrie.log.closed` |
| `2026-06-26 09:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04f802f4de9d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:31 |
| **Last Seen** | 2026-06-26 09:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:31:10` | `cowrie.session.connect` |
| `2026-06-26 09:31:10` | `cowrie.client.version` |
| `2026-06-26 09:31:10` | `cowrie.client.kex` |
| `2026-06-26 09:31:10` | `cowrie.login.success` |
| `2026-06-26 09:31:11` | `cowrie.session.params` |
| `2026-06-26 09:31:11` | `cowrie.command.input` |
| `2026-06-26 09:31:11` | `cowrie.log.closed` |
| `2026-06-26 09:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78d734db0606

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:32 |
| **Last Seen** | 2026-06-26 09:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:32:13` | `cowrie.session.connect` |
| `2026-06-26 09:32:13` | `cowrie.client.version` |
| `2026-06-26 09:32:13` | `cowrie.client.kex` |
| `2026-06-26 09:32:13` | `cowrie.login.success` |
| `2026-06-26 09:32:14` | `cowrie.session.params` |
| `2026-06-26 09:32:14` | `cowrie.command.input` |
| `2026-06-26 09:32:14` | `cowrie.log.closed` |
| `2026-06-26 09:32:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0058baa4bccb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:33 |
| **Last Seen** | 2026-06-26 09:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:33:17` | `cowrie.session.connect` |
| `2026-06-26 09:33:17` | `cowrie.client.version` |
| `2026-06-26 09:33:17` | `cowrie.client.kex` |
| `2026-06-26 09:33:18` | `cowrie.login.success` |
| `2026-06-26 09:33:18` | `cowrie.session.params` |
| `2026-06-26 09:33:18` | `cowrie.command.input` |
| `2026-06-26 09:33:18` | `cowrie.log.closed` |
| `2026-06-26 09:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffdceaf56149

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:34 |
| **Last Seen** | 2026-06-26 09:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:34:20` | `cowrie.session.connect` |
| `2026-06-26 09:34:20` | `cowrie.client.version` |
| `2026-06-26 09:34:20` | `cowrie.client.kex` |
| `2026-06-26 09:34:20` | `cowrie.login.success` |
| `2026-06-26 09:34:21` | `cowrie.session.params` |
| `2026-06-26 09:34:21` | `cowrie.command.input` |
| `2026-06-26 09:34:21` | `cowrie.log.closed` |
| `2026-06-26 09:34:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ebf6a678872

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:35 |
| **Last Seen** | 2026-06-26 09:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:35:24` | `cowrie.session.connect` |
| `2026-06-26 09:35:24` | `cowrie.client.version` |
| `2026-06-26 09:35:24` | `cowrie.client.kex` |
| `2026-06-26 09:35:25` | `cowrie.login.success` |
| `2026-06-26 09:35:25` | `cowrie.session.params` |
| `2026-06-26 09:35:25` | `cowrie.command.input` |
| `2026-06-26 09:35:25` | `cowrie.log.closed` |
| `2026-06-26 09:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ecde939c64d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:36 |
| **Last Seen** | 2026-06-26 09:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:36:28` | `cowrie.session.connect` |
| `2026-06-26 09:36:28` | `cowrie.client.version` |
| `2026-06-26 09:36:28` | `cowrie.client.kex` |
| `2026-06-26 09:36:28` | `cowrie.login.success` |
| `2026-06-26 09:36:29` | `cowrie.session.params` |
| `2026-06-26 09:36:29` | `cowrie.command.input` |
| `2026-06-26 09:36:29` | `cowrie.log.closed` |
| `2026-06-26 09:36:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34ab72ecf67b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 09:37 |
| **Last Seen** | 2026-06-26 09:37 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:37:27` | `cowrie.session.connect` |
| `2026-06-26 09:37:28` | `cowrie.client.version` |
| `2026-06-26 09:37:28` | `cowrie.client.kex` |
| `2026-06-26 09:37:33` | `cowrie.login.success` |
| `2026-06-26 09:37:36` | `cowrie.session.params` |
| `2026-06-26 09:37:36` | `cowrie.command.input` |
| `2026-06-26 09:37:37` | `cowrie.log.closed` |
| `2026-06-26 09:37:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd9ae256f668

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:37 |
| **Last Seen** | 2026-06-26 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:37:32` | `cowrie.session.connect` |
| `2026-06-26 09:37:32` | `cowrie.client.version` |
| `2026-06-26 09:37:32` | `cowrie.client.kex` |
| `2026-06-26 09:37:32` | `cowrie.login.success` |
| `2026-06-26 09:37:33` | `cowrie.session.params` |
| `2026-06-26 09:37:33` | `cowrie.command.input` |
| `2026-06-26 09:37:33` | `cowrie.log.closed` |
| `2026-06-26 09:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab074264997b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:38 |
| **Last Seen** | 2026-06-26 09:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:38:35` | `cowrie.session.connect` |
| `2026-06-26 09:38:35` | `cowrie.client.version` |
| `2026-06-26 09:38:35` | `cowrie.client.kex` |
| `2026-06-26 09:38:35` | `cowrie.login.success` |
| `2026-06-26 09:38:36` | `cowrie.session.params` |
| `2026-06-26 09:38:36` | `cowrie.command.input` |
| `2026-06-26 09:38:36` | `cowrie.log.closed` |
| `2026-06-26 09:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9abd0950933a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 09:38 |
| **Last Seen** | 2026-06-26 09:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:38:37` | `cowrie.session.connect` |
| `2026-06-26 09:38:37` | `cowrie.client.version` |
| `2026-06-26 09:38:37` | `cowrie.client.kex` |
| `2026-06-26 09:38:39` | `cowrie.login.success` |
| `2026-06-26 09:38:41` | `cowrie.session.params` |
| `2026-06-26 09:38:41` | `cowrie.command.input` |
| `2026-06-26 09:38:41` | `cowrie.log.closed` |
| `2026-06-26 09:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a650fe204d0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:39 |
| **Last Seen** | 2026-06-26 09:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:39:38` | `cowrie.session.connect` |
| `2026-06-26 09:39:38` | `cowrie.client.version` |
| `2026-06-26 09:39:38` | `cowrie.client.kex` |
| `2026-06-26 09:39:38` | `cowrie.login.success` |
| `2026-06-26 09:39:39` | `cowrie.session.params` |
| `2026-06-26 09:39:39` | `cowrie.command.input` |
| `2026-06-26 09:39:39` | `cowrie.log.closed` |
| `2026-06-26 09:39:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-470668134b05

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:40 |
| **Last Seen** | 2026-06-26 09:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:40:40` | `cowrie.session.connect` |
| `2026-06-26 09:40:40` | `cowrie.client.version` |
| `2026-06-26 09:40:40` | `cowrie.client.kex` |
| `2026-06-26 09:40:40` | `cowrie.login.success` |
| `2026-06-26 09:40:41` | `cowrie.session.params` |
| `2026-06-26 09:40:41` | `cowrie.command.input` |
| `2026-06-26 09:40:41` | `cowrie.log.closed` |
| `2026-06-26 09:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4051126808df

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:41 |
| **Last Seen** | 2026-06-26 09:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:41:46` | `cowrie.session.connect` |
| `2026-06-26 09:41:46` | `cowrie.client.version` |
| `2026-06-26 09:41:46` | `cowrie.client.kex` |
| `2026-06-26 09:41:47` | `cowrie.login.success` |
| `2026-06-26 09:41:47` | `cowrie.session.params` |
| `2026-06-26 09:41:47` | `cowrie.command.input` |
| `2026-06-26 09:41:47` | `cowrie.log.closed` |
| `2026-06-26 09:41:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bea572b43072

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-26 09:42 |
| **Last Seen** | 2026-06-26 09:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:42:02` | `cowrie.session.connect` |
| `2026-06-26 09:42:02` | `cowrie.client.version` |
| `2026-06-26 09:42:03` | `cowrie.client.kex` |
| `2026-06-26 09:42:04` | `cowrie.login.success` |
| `2026-06-26 09:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e459dcc89a6f

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-26 09:42 |
| **Last Seen** | 2026-06-26 09:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:42:03` | `cowrie.session.connect` |
| `2026-06-26 09:42:03` | `cowrie.client.version` |
| `2026-06-26 09:42:03` | `cowrie.client.kex` |
| `2026-06-26 09:42:04` | `cowrie.login.success` |
| `2026-06-26 09:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d87021281a8a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:42 |
| **Last Seen** | 2026-06-26 09:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:42:50` | `cowrie.session.connect` |
| `2026-06-26 09:42:50` | `cowrie.client.version` |
| `2026-06-26 09:42:50` | `cowrie.client.kex` |
| `2026-06-26 09:42:51` | `cowrie.login.success` |
| `2026-06-26 09:42:51` | `cowrie.session.params` |
| `2026-06-26 09:42:51` | `cowrie.command.input` |
| `2026-06-26 09:42:52` | `cowrie.log.closed` |
| `2026-06-26 09:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc05bd80a893

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:43 |
| **Last Seen** | 2026-06-26 09:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:43:52` | `cowrie.session.connect` |
| `2026-06-26 09:43:52` | `cowrie.client.version` |
| `2026-06-26 09:43:52` | `cowrie.client.kex` |
| `2026-06-26 09:43:53` | `cowrie.login.success` |
| `2026-06-26 09:43:54` | `cowrie.session.params` |
| `2026-06-26 09:43:54` | `cowrie.command.input` |
| `2026-06-26 09:43:54` | `cowrie.log.closed` |
| `2026-06-26 09:43:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1baf078c0268

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:44 |
| **Last Seen** | 2026-06-26 09:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:44:58` | `cowrie.session.connect` |
| `2026-06-26 09:44:58` | `cowrie.client.version` |
| `2026-06-26 09:44:59` | `cowrie.client.kex` |
| `2026-06-26 09:44:59` | `cowrie.login.success` |
| `2026-06-26 09:44:59` | `cowrie.session.params` |
| `2026-06-26 09:44:59` | `cowrie.command.input` |
| `2026-06-26 09:45:00` | `cowrie.log.closed` |
| `2026-06-26 09:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb33881e97c1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:46 |
| **Last Seen** | 2026-06-26 09:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:46:09` | `cowrie.session.connect` |
| `2026-06-26 09:46:09` | `cowrie.client.version` |
| `2026-06-26 09:46:09` | `cowrie.client.kex` |
| `2026-06-26 09:46:09` | `cowrie.login.success` |
| `2026-06-26 09:46:10` | `cowrie.session.params` |
| `2026-06-26 09:46:10` | `cowrie.command.input` |
| `2026-06-26 09:46:10` | `cowrie.log.closed` |
| `2026-06-26 09:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c419bf5c00f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:47 |
| **Last Seen** | 2026-06-26 09:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:47:17` | `cowrie.session.connect` |
| `2026-06-26 09:47:17` | `cowrie.client.version` |
| `2026-06-26 09:47:17` | `cowrie.client.kex` |
| `2026-06-26 09:47:17` | `cowrie.login.success` |
| `2026-06-26 09:47:18` | `cowrie.session.params` |
| `2026-06-26 09:47:18` | `cowrie.command.input` |
| `2026-06-26 09:47:18` | `cowrie.log.closed` |
| `2026-06-26 09:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09d05836d847

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 09:48 |
| **Last Seen** | 2026-06-26 09:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:48:12` | `cowrie.session.connect` |
| `2026-06-26 09:48:13` | `cowrie.client.version` |
| `2026-06-26 09:48:13` | `cowrie.client.kex` |
| `2026-06-26 09:48:18` | `cowrie.login.success` |
| `2026-06-26 09:48:21` | `cowrie.session.params` |
| `2026-06-26 09:48:21` | `cowrie.command.input` |
| `2026-06-26 09:48:22` | `cowrie.log.closed` |
| `2026-06-26 09:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da144a7b3a7b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:48 |
| **Last Seen** | 2026-06-26 09:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:48:22` | `cowrie.session.connect` |
| `2026-06-26 09:48:22` | `cowrie.client.version` |
| `2026-06-26 09:48:22` | `cowrie.client.kex` |
| `2026-06-26 09:48:22` | `cowrie.login.success` |
| `2026-06-26 09:48:23` | `cowrie.session.params` |
| `2026-06-26 09:48:23` | `cowrie.command.input` |
| `2026-06-26 09:48:23` | `cowrie.log.closed` |
| `2026-06-26 09:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-578b00a410c1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:49 |
| **Last Seen** | 2026-06-26 09:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:49:27` | `cowrie.session.connect` |
| `2026-06-26 09:49:27` | `cowrie.client.version` |
| `2026-06-26 09:49:27` | `cowrie.client.kex` |
| `2026-06-26 09:49:27` | `cowrie.login.success` |
| `2026-06-26 09:49:28` | `cowrie.session.params` |
| `2026-06-26 09:49:28` | `cowrie.command.input` |
| `2026-06-26 09:49:28` | `cowrie.log.closed` |
| `2026-06-26 09:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59b644ccd800

| Field | Detail |
|---|---|
| **Source IP** | `45.225.135[.]21` |
| **First Seen** | 2026-06-26 09:49 |
| **Last Seen** | 2026-06-26 09:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:49:56` | `cowrie.session.connect` |
| `2026-06-26 09:49:57` | `cowrie.telnet.option` |
| `2026-06-26 09:49:57` | `cowrie.telnet.option` |
| `2026-06-26 09:51:02` | `cowrie.login.success` |
| `2026-06-26 09:51:03` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `45.225.135[.]21` to AbuseIPDB if not already reported
- [ ] Block `45.225.135[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-476e0482d84f

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]108` |
| **First Seen** | 2026-06-26 09:50 |
| **Last Seen** | 2026-06-26 09:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, busybox TEST, cat /proc, /` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:50:25` | `cowrie.session.connect` |
| `2026-06-26 09:50:26` | `cowrie.login.success` |
| `2026-06-26 09:50:27` | `cowrie.session.params` |
| `2026-06-26 09:50:28` | `cowrie.command.input` |
| `2026-06-26 09:50:28` | `cowrie.command.input` |
| `2026-06-26 09:50:29` | `cowrie.command.input` |
| `2026-06-26 09:50:30` | `cowrie.command.input` |
| `2026-06-26 09:50:30` | `cowrie.log.closed` |
| `2026-06-26 09:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]108` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e7c045a2a53

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:50 |
| **Last Seen** | 2026-06-26 09:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:50:35` | `cowrie.session.connect` |
| `2026-06-26 09:50:35` | `cowrie.client.version` |
| `2026-06-26 09:50:35` | `cowrie.client.kex` |
| `2026-06-26 09:50:35` | `cowrie.login.success` |
| `2026-06-26 09:50:36` | `cowrie.session.params` |
| `2026-06-26 09:50:36` | `cowrie.command.input` |
| `2026-06-26 09:50:36` | `cowrie.log.closed` |
| `2026-06-26 09:50:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4d4c9f8cf42

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:51 |
| **Last Seen** | 2026-06-26 09:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:51:41` | `cowrie.session.connect` |
| `2026-06-26 09:51:41` | `cowrie.client.version` |
| `2026-06-26 09:51:41` | `cowrie.client.kex` |
| `2026-06-26 09:51:41` | `cowrie.login.success` |
| `2026-06-26 09:51:42` | `cowrie.session.params` |
| `2026-06-26 09:51:42` | `cowrie.command.input` |
| `2026-06-26 09:51:42` | `cowrie.log.closed` |
| `2026-06-26 09:51:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e9f2b8c22b1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:52 |
| **Last Seen** | 2026-06-26 09:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:52:45` | `cowrie.session.connect` |
| `2026-06-26 09:52:45` | `cowrie.client.version` |
| `2026-06-26 09:52:45` | `cowrie.client.kex` |
| `2026-06-26 09:52:46` | `cowrie.login.success` |
| `2026-06-26 09:52:47` | `cowrie.session.params` |
| `2026-06-26 09:52:47` | `cowrie.command.input` |
| `2026-06-26 09:52:47` | `cowrie.log.closed` |
| `2026-06-26 09:52:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bb52eb6ea3e

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 09:52 |
| **Last Seen** | 2026-06-26 09:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:52:52` | `cowrie.session.connect` |
| `2026-06-26 09:52:52` | `cowrie.client.version` |
| `2026-06-26 09:52:52` | `cowrie.client.kex` |
| `2026-06-26 09:52:54` | `cowrie.login.success` |
| `2026-06-26 09:52:55` | `cowrie.session.params` |
| `2026-06-26 09:52:55` | `cowrie.command.input` |
| `2026-06-26 09:52:55` | `cowrie.log.closed` |
| `2026-06-26 09:52:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df959a9b7f02

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:53 |
| **Last Seen** | 2026-06-26 09:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:53:54` | `cowrie.session.connect` |
| `2026-06-26 09:53:54` | `cowrie.client.version` |
| `2026-06-26 09:53:54` | `cowrie.client.kex` |
| `2026-06-26 09:53:54` | `cowrie.login.success` |
| `2026-06-26 09:53:55` | `cowrie.session.params` |
| `2026-06-26 09:53:55` | `cowrie.command.input` |
| `2026-06-26 09:53:55` | `cowrie.log.closed` |
| `2026-06-26 09:53:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abfd9eeea69b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:55 |
| **Last Seen** | 2026-06-26 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:55:01` | `cowrie.session.connect` |
| `2026-06-26 09:55:01` | `cowrie.client.version` |
| `2026-06-26 09:55:01` | `cowrie.client.kex` |
| `2026-06-26 09:55:01` | `cowrie.login.success` |
| `2026-06-26 09:55:02` | `cowrie.session.params` |
| `2026-06-26 09:55:02` | `cowrie.command.input` |
| `2026-06-26 09:55:02` | `cowrie.log.closed` |
| `2026-06-26 09:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57de42391ee4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:56 |
| **Last Seen** | 2026-06-26 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:56:09` | `cowrie.session.connect` |
| `2026-06-26 09:56:09` | `cowrie.client.version` |
| `2026-06-26 09:56:09` | `cowrie.client.kex` |
| `2026-06-26 09:56:09` | `cowrie.login.success` |
| `2026-06-26 09:56:10` | `cowrie.session.params` |
| `2026-06-26 09:56:10` | `cowrie.command.input` |
| `2026-06-26 09:56:10` | `cowrie.log.closed` |
| `2026-06-26 09:56:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-359ce7021c32

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:57 |
| **Last Seen** | 2026-06-26 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:57:15` | `cowrie.session.connect` |
| `2026-06-26 09:57:15` | `cowrie.client.version` |
| `2026-06-26 09:57:16` | `cowrie.client.kex` |
| `2026-06-26 09:57:16` | `cowrie.login.success` |
| `2026-06-26 09:57:17` | `cowrie.session.params` |
| `2026-06-26 09:57:17` | `cowrie.command.input` |
| `2026-06-26 09:57:17` | `cowrie.log.closed` |
| `2026-06-26 09:57:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd19ece1ffe4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:58 |
| **Last Seen** | 2026-06-26 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:58:26` | `cowrie.session.connect` |
| `2026-06-26 09:58:26` | `cowrie.client.version` |
| `2026-06-26 09:58:26` | `cowrie.client.kex` |
| `2026-06-26 09:58:26` | `cowrie.login.success` |
| `2026-06-26 09:58:27` | `cowrie.session.params` |
| `2026-06-26 09:58:27` | `cowrie.command.input` |
| `2026-06-26 09:58:27` | `cowrie.log.closed` |
| `2026-06-26 09:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fbff75d4177

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 09:58 |
| **Last Seen** | 2026-06-26 09:59 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:58:49` | `cowrie.session.connect` |
| `2026-06-26 09:58:50` | `cowrie.client.version` |
| `2026-06-26 09:58:50` | `cowrie.client.kex` |
| `2026-06-26 09:58:56` | `cowrie.login.success` |
| `2026-06-26 09:58:59` | `cowrie.session.params` |
| `2026-06-26 09:58:59` | `cowrie.command.input` |
| `2026-06-26 09:59:01` | `cowrie.log.closed` |
| `2026-06-26 09:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c610a7897584

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 09:59 |
| **Last Seen** | 2026-06-26 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 09:59:37` | `cowrie.session.connect` |
| `2026-06-26 09:59:37` | `cowrie.client.version` |
| `2026-06-26 09:59:37` | `cowrie.client.kex` |
| `2026-06-26 09:59:37` | `cowrie.login.success` |
| `2026-06-26 09:59:38` | `cowrie.session.params` |
| `2026-06-26 09:59:38` | `cowrie.command.input` |
| `2026-06-26 09:59:38` | `cowrie.log.closed` |
| `2026-06-26 09:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-740b266049ca

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:00 |
| **Last Seen** | 2026-06-26 10:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:00:35` | `cowrie.session.connect` |
| `2026-06-26 10:00:35` | `cowrie.client.version` |
| `2026-06-26 10:00:35` | `cowrie.client.kex` |
| `2026-06-26 10:00:35` | `cowrie.login.success` |
| `2026-06-26 10:00:36` | `cowrie.session.params` |
| `2026-06-26 10:00:36` | `cowrie.command.input` |
| `2026-06-26 10:00:36` | `cowrie.log.closed` |
| `2026-06-26 10:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8acc16bef8d2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:01 |
| **Last Seen** | 2026-06-26 10:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:01:18` | `cowrie.session.connect` |
| `2026-06-26 10:01:18` | `cowrie.client.version` |
| `2026-06-26 10:01:18` | `cowrie.client.kex` |
| `2026-06-26 10:01:18` | `cowrie.login.success` |
| `2026-06-26 10:01:19` | `cowrie.session.params` |
| `2026-06-26 10:01:19` | `cowrie.command.input` |
| `2026-06-26 10:01:19` | `cowrie.log.closed` |
| `2026-06-26 10:01:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-913ed8c05ca7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:02 |
| **Last Seen** | 2026-06-26 10:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:02:04` | `cowrie.session.connect` |
| `2026-06-26 10:02:04` | `cowrie.client.version` |
| `2026-06-26 10:02:04` | `cowrie.client.kex` |
| `2026-06-26 10:02:04` | `cowrie.login.success` |
| `2026-06-26 10:02:05` | `cowrie.session.params` |
| `2026-06-26 10:02:05` | `cowrie.command.input` |
| `2026-06-26 10:02:05` | `cowrie.log.closed` |
| `2026-06-26 10:02:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04159a408217

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:02 |
| **Last Seen** | 2026-06-26 10:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:02:53` | `cowrie.session.connect` |
| `2026-06-26 10:02:53` | `cowrie.client.version` |
| `2026-06-26 10:02:53` | `cowrie.client.kex` |
| `2026-06-26 10:02:53` | `cowrie.login.success` |
| `2026-06-26 10:02:54` | `cowrie.session.params` |
| `2026-06-26 10:02:54` | `cowrie.command.input` |
| `2026-06-26 10:02:54` | `cowrie.log.closed` |
| `2026-06-26 10:02:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56a409cb2540

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:03 |
| **Last Seen** | 2026-06-26 10:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:03:44` | `cowrie.session.connect` |
| `2026-06-26 10:03:44` | `cowrie.client.version` |
| `2026-06-26 10:03:44` | `cowrie.client.kex` |
| `2026-06-26 10:03:44` | `cowrie.login.success` |
| `2026-06-26 10:03:45` | `cowrie.session.params` |
| `2026-06-26 10:03:45` | `cowrie.command.input` |
| `2026-06-26 10:03:45` | `cowrie.log.closed` |
| `2026-06-26 10:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-684af63896e7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:05 |
| **Last Seen** | 2026-06-26 10:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:05:14` | `cowrie.session.connect` |
| `2026-06-26 10:05:14` | `cowrie.client.version` |
| `2026-06-26 10:05:15` | `cowrie.client.kex` |
| `2026-06-26 10:05:15` | `cowrie.login.success` |
| `2026-06-26 10:05:16` | `cowrie.session.params` |
| `2026-06-26 10:05:16` | `cowrie.command.input` |
| `2026-06-26 10:05:16` | `cowrie.log.closed` |
| `2026-06-26 10:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-900b00e7e990

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:05 |
| **Last Seen** | 2026-06-26 10:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:05:59` | `cowrie.session.connect` |
| `2026-06-26 10:05:59` | `cowrie.client.version` |
| `2026-06-26 10:05:59` | `cowrie.client.kex` |
| `2026-06-26 10:05:59` | `cowrie.login.success` |
| `2026-06-26 10:06:00` | `cowrie.session.params` |
| `2026-06-26 10:06:00` | `cowrie.command.input` |
| `2026-06-26 10:06:00` | `cowrie.log.closed` |
| `2026-06-26 10:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7833e1b4fc5a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:06 |
| **Last Seen** | 2026-06-26 10:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:06:44` | `cowrie.session.connect` |
| `2026-06-26 10:06:44` | `cowrie.client.version` |
| `2026-06-26 10:06:44` | `cowrie.client.kex` |
| `2026-06-26 10:06:45` | `cowrie.login.success` |
| `2026-06-26 10:06:45` | `cowrie.session.params` |
| `2026-06-26 10:06:45` | `cowrie.command.input` |
| `2026-06-26 10:06:46` | `cowrie.log.closed` |
| `2026-06-26 10:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d59a18df93e

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 10:07 |
| **Last Seen** | 2026-06-26 10:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:07:09` | `cowrie.session.connect` |
| `2026-06-26 10:07:09` | `cowrie.client.version` |
| `2026-06-26 10:07:09` | `cowrie.client.kex` |
| `2026-06-26 10:07:11` | `cowrie.login.success` |
| `2026-06-26 10:07:13` | `cowrie.session.params` |
| `2026-06-26 10:07:13` | `cowrie.command.input` |
| `2026-06-26 10:07:14` | `cowrie.log.closed` |
| `2026-06-26 10:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bcf6c2dad6c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:07 |
| **Last Seen** | 2026-06-26 10:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:07:29` | `cowrie.session.connect` |
| `2026-06-26 10:07:29` | `cowrie.client.version` |
| `2026-06-26 10:07:29` | `cowrie.client.kex` |
| `2026-06-26 10:07:29` | `cowrie.login.success` |
| `2026-06-26 10:07:30` | `cowrie.session.params` |
| `2026-06-26 10:07:30` | `cowrie.command.input` |
| `2026-06-26 10:07:30` | `cowrie.log.closed` |
| `2026-06-26 10:07:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31d68b077c62

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:08 |
| **Last Seen** | 2026-06-26 10:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:08:13` | `cowrie.session.connect` |
| `2026-06-26 10:08:13` | `cowrie.client.version` |
| `2026-06-26 10:08:13` | `cowrie.client.kex` |
| `2026-06-26 10:08:13` | `cowrie.login.success` |
| `2026-06-26 10:08:14` | `cowrie.session.params` |
| `2026-06-26 10:08:14` | `cowrie.command.input` |
| `2026-06-26 10:08:14` | `cowrie.log.closed` |
| `2026-06-26 10:08:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cf99b73418e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:09 |
| **Last Seen** | 2026-06-26 10:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:09:00` | `cowrie.session.connect` |
| `2026-06-26 10:09:00` | `cowrie.client.version` |
| `2026-06-26 10:09:00` | `cowrie.client.kex` |
| `2026-06-26 10:09:01` | `cowrie.login.success` |
| `2026-06-26 10:09:01` | `cowrie.session.params` |
| `2026-06-26 10:09:01` | `cowrie.command.input` |
| `2026-06-26 10:09:02` | `cowrie.log.closed` |
| `2026-06-26 10:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-033fc986d704

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 10:09 |
| **Last Seen** | 2026-06-26 10:09 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:09:27` | `cowrie.session.connect` |
| `2026-06-26 10:09:28` | `cowrie.client.version` |
| `2026-06-26 10:09:28` | `cowrie.client.kex` |
| `2026-06-26 10:09:32` | `cowrie.login.success` |
| `2026-06-26 10:09:36` | `cowrie.session.params` |
| `2026-06-26 10:09:36` | `cowrie.command.input` |
| `2026-06-26 10:09:37` | `cowrie.log.closed` |
| `2026-06-26 10:09:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a6e97c8a730

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:09 |
| **Last Seen** | 2026-06-26 10:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:09:54` | `cowrie.session.connect` |
| `2026-06-26 10:09:54` | `cowrie.client.version` |
| `2026-06-26 10:09:54` | `cowrie.client.kex` |
| `2026-06-26 10:09:55` | `cowrie.login.success` |
| `2026-06-26 10:09:55` | `cowrie.session.params` |
| `2026-06-26 10:09:55` | `cowrie.command.input` |
| `2026-06-26 10:09:55` | `cowrie.log.closed` |
| `2026-06-26 10:09:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1db87cb9749e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:10 |
| **Last Seen** | 2026-06-26 10:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:10:44` | `cowrie.session.connect` |
| `2026-06-26 10:10:44` | `cowrie.client.version` |
| `2026-06-26 10:10:44` | `cowrie.client.kex` |
| `2026-06-26 10:10:44` | `cowrie.login.success` |
| `2026-06-26 10:10:45` | `cowrie.session.params` |
| `2026-06-26 10:10:45` | `cowrie.command.input` |
| `2026-06-26 10:10:45` | `cowrie.log.closed` |
| `2026-06-26 10:10:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-483a2aa2d91f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:11 |
| **Last Seen** | 2026-06-26 10:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:11:33` | `cowrie.session.connect` |
| `2026-06-26 10:11:33` | `cowrie.client.version` |
| `2026-06-26 10:11:33` | `cowrie.client.kex` |
| `2026-06-26 10:11:34` | `cowrie.login.success` |
| `2026-06-26 10:11:35` | `cowrie.session.params` |
| `2026-06-26 10:11:35` | `cowrie.command.input` |
| `2026-06-26 10:11:35` | `cowrie.log.closed` |
| `2026-06-26 10:11:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d56b60dbb24b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:12 |
| **Last Seen** | 2026-06-26 10:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:12:22` | `cowrie.session.connect` |
| `2026-06-26 10:12:22` | `cowrie.client.version` |
| `2026-06-26 10:12:22` | `cowrie.client.kex` |
| `2026-06-26 10:12:22` | `cowrie.login.success` |
| `2026-06-26 10:12:23` | `cowrie.session.params` |
| `2026-06-26 10:12:23` | `cowrie.command.input` |
| `2026-06-26 10:12:23` | `cowrie.log.closed` |
| `2026-06-26 10:12:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fea7fbf8e7b4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:13 |
| **Last Seen** | 2026-06-26 10:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:13:07` | `cowrie.session.connect` |
| `2026-06-26 10:13:07` | `cowrie.client.version` |
| `2026-06-26 10:13:07` | `cowrie.client.kex` |
| `2026-06-26 10:13:07` | `cowrie.login.success` |
| `2026-06-26 10:13:08` | `cowrie.session.params` |
| `2026-06-26 10:13:08` | `cowrie.command.input` |
| `2026-06-26 10:13:08` | `cowrie.log.closed` |
| `2026-06-26 10:13:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bde8c5c3e7db

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-26 10:13 |
| **Last Seen** | 2026-06-26 10:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:13:09` | `cowrie.session.connect` |
| `2026-06-26 10:13:09` | `cowrie.client.version` |
| `2026-06-26 10:13:09` | `cowrie.client.kex` |
| `2026-06-26 10:13:09` | `cowrie.login.success` |
| `2026-06-26 10:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec1765e77342

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-26 10:13 |
| **Last Seen** | 2026-06-26 10:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:13:09` | `cowrie.session.connect` |
| `2026-06-26 10:13:09` | `cowrie.client.version` |
| `2026-06-26 10:13:09` | `cowrie.client.kex` |
| `2026-06-26 10:13:09` | `cowrie.login.success` |
| `2026-06-26 10:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c92600a498b4

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-26 10:13 |
| **Last Seen** | 2026-06-26 10:15 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:13:29` | `cowrie.session.connect` |
| `2026-06-26 10:13:29` | `cowrie.client.version` |
| `2026-06-26 10:13:29` | `cowrie.client.kex` |
| `2026-06-26 10:13:30` | `cowrie.login.success` |
| `2026-06-26 10:13:31` | `cowrie.session.file_upload` |
| `2026-06-26 10:13:31` | `cowrie.session.params` |
| `2026-06-26 10:13:31` | `cowrie.command.input` |
| `2026-06-26 10:13:31` | `cowrie.command.input` |
| `2026-06-26 10:13:31` | `cowrie.command.input` |
| `2026-06-26 10:13:31` | `cowrie.command.failed` |
| `2026-06-26 10:13:31` | `cowrie.log.closed` |
| `2026-06-26 10:13:32` | `cowrie.session.params` |
| `2026-06-26 10:13:32` | `cowrie.command.input` |
| `2026-06-26 10:13:32` | `cowrie.log.closed` |
| `2026-06-26 10:13:33` | `cowrie.session.params` |
| `2026-06-26 10:13:33` | `cowrie.command.input` |
| `2026-06-26 10:13:33` | `cowrie.log.closed` |
| `2026-06-26 10:13:34` | `cowrie.session.params` |
| `2026-06-26 10:13:34` | `cowrie.command.input` |
| `2026-06-26 10:13:34` | `cowrie.command.failed` |
| `2026-06-26 10:13:34` | `cowrie.command.failed` |
| `2026-06-26 10:14:34` | `cowrie.session.params` |
| `2026-06-26 10:14:34` | `cowrie.command.input` |
| `2026-06-26 10:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0c80d2edd16

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:13 |
| **Last Seen** | 2026-06-26 10:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:13:51` | `cowrie.session.connect` |
| `2026-06-26 10:13:51` | `cowrie.client.version` |
| `2026-06-26 10:13:51` | `cowrie.client.kex` |
| `2026-06-26 10:13:52` | `cowrie.login.success` |
| `2026-06-26 10:13:53` | `cowrie.session.params` |
| `2026-06-26 10:13:53` | `cowrie.command.input` |
| `2026-06-26 10:13:53` | `cowrie.log.closed` |
| `2026-06-26 10:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c3305b77902

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:14 |
| **Last Seen** | 2026-06-26 10:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:14:37` | `cowrie.session.connect` |
| `2026-06-26 10:14:37` | `cowrie.client.version` |
| `2026-06-26 10:14:37` | `cowrie.client.kex` |
| `2026-06-26 10:14:37` | `cowrie.login.success` |
| `2026-06-26 10:14:38` | `cowrie.session.params` |
| `2026-06-26 10:14:38` | `cowrie.command.input` |
| `2026-06-26 10:14:38` | `cowrie.log.closed` |
| `2026-06-26 10:14:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac25942838ea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:15 |
| **Last Seen** | 2026-06-26 10:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:15:24` | `cowrie.session.connect` |
| `2026-06-26 10:15:24` | `cowrie.client.version` |
| `2026-06-26 10:15:24` | `cowrie.client.kex` |
| `2026-06-26 10:15:24` | `cowrie.login.success` |
| `2026-06-26 10:15:25` | `cowrie.session.params` |
| `2026-06-26 10:15:25` | `cowrie.command.input` |
| `2026-06-26 10:15:25` | `cowrie.log.closed` |
| `2026-06-26 10:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60f1a520c885

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-26 10:15 |
| **Last Seen** | 2026-06-26 10:17 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:15:50` | `cowrie.session.connect` |
| `2026-06-26 10:15:50` | `cowrie.client.version` |
| `2026-06-26 10:15:50` | `cowrie.client.kex` |
| `2026-06-26 10:15:51` | `cowrie.login.success` |
| `2026-06-26 10:15:51` | `cowrie.session.file_upload` |
| `2026-06-26 10:15:52` | `cowrie.session.params` |
| `2026-06-26 10:15:52` | `cowrie.command.input` |
| `2026-06-26 10:15:52` | `cowrie.command.input` |
| `2026-06-26 10:15:52` | `cowrie.command.input` |
| `2026-06-26 10:15:52` | `cowrie.command.failed` |
| `2026-06-26 10:15:52` | `cowrie.log.closed` |
| `2026-06-26 10:15:53` | `cowrie.session.params` |
| `2026-06-26 10:15:53` | `cowrie.command.input` |
| `2026-06-26 10:15:53` | `cowrie.log.closed` |
| `2026-06-26 10:15:54` | `cowrie.session.params` |
| `2026-06-26 10:15:54` | `cowrie.command.input` |
| `2026-06-26 10:15:54` | `cowrie.log.closed` |
| `2026-06-26 10:15:55` | `cowrie.session.params` |
| `2026-06-26 10:15:55` | `cowrie.command.input` |
| `2026-06-26 10:15:55` | `cowrie.command.failed` |
| `2026-06-26 10:15:55` | `cowrie.command.failed` |
| `2026-06-26 10:16:56` | `cowrie.session.params` |
| `2026-06-26 10:16:56` | `cowrie.command.input` |
| `2026-06-26 10:17:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07c51e26e897

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:16 |
| **Last Seen** | 2026-06-26 10:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:16:13` | `cowrie.session.connect` |
| `2026-06-26 10:16:13` | `cowrie.client.version` |
| `2026-06-26 10:16:14` | `cowrie.client.kex` |
| `2026-06-26 10:16:14` | `cowrie.login.success` |
| `2026-06-26 10:16:15` | `cowrie.session.params` |
| `2026-06-26 10:16:15` | `cowrie.command.input` |
| `2026-06-26 10:16:15` | `cowrie.log.closed` |
| `2026-06-26 10:16:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fee54de2a22

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:17 |
| **Last Seen** | 2026-06-26 10:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:17:02` | `cowrie.session.connect` |
| `2026-06-26 10:17:02` | `cowrie.client.version` |
| `2026-06-26 10:17:02` | `cowrie.client.kex` |
| `2026-06-26 10:17:02` | `cowrie.login.success` |
| `2026-06-26 10:17:03` | `cowrie.session.params` |
| `2026-06-26 10:17:03` | `cowrie.command.input` |
| `2026-06-26 10:17:03` | `cowrie.log.closed` |
| `2026-06-26 10:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b48999d6df09

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:17 |
| **Last Seen** | 2026-06-26 10:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:17:50` | `cowrie.session.connect` |
| `2026-06-26 10:17:50` | `cowrie.client.version` |
| `2026-06-26 10:17:50` | `cowrie.client.kex` |
| `2026-06-26 10:17:50` | `cowrie.login.success` |
| `2026-06-26 10:17:51` | `cowrie.session.params` |
| `2026-06-26 10:17:51` | `cowrie.command.input` |
| `2026-06-26 10:17:51` | `cowrie.log.closed` |
| `2026-06-26 10:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba4cca5d551b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:18 |
| **Last Seen** | 2026-06-26 10:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:18:37` | `cowrie.session.connect` |
| `2026-06-26 10:18:37` | `cowrie.client.version` |
| `2026-06-26 10:18:37` | `cowrie.client.kex` |
| `2026-06-26 10:18:38` | `cowrie.login.success` |
| `2026-06-26 10:18:39` | `cowrie.session.params` |
| `2026-06-26 10:18:39` | `cowrie.command.input` |
| `2026-06-26 10:18:39` | `cowrie.log.closed` |
| `2026-06-26 10:18:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-734b52aab7cf

| Field | Detail |
|---|---|
| **Source IP** | `195.184.76[.]236` |
| **First Seen** | 2026-06-26 10:18 |
| **Last Seen** | 2026-06-26 10:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 3 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:18:39` | `cowrie.session.connect` |
| `2026-06-26 10:18:39` | `cowrie.login.success` |
| `2026-06-26 10:18:39` | `cowrie.login.success` |
| `2026-06-26 10:18:39` | `cowrie.login.success` |
| `2026-06-26 10:18:40` | `cowrie.session.params` |
| `2026-06-26 10:18:40` | `cowrie.log.closed` |
| `2026-06-26 10:18:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.184.76[.]236` to AbuseIPDB if not already reported
- [ ] Block `195.184.76[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f777fd2d3b9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:19 |
| **Last Seen** | 2026-06-26 10:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:19:24` | `cowrie.session.connect` |
| `2026-06-26 10:19:24` | `cowrie.client.version` |
| `2026-06-26 10:19:24` | `cowrie.client.kex` |
| `2026-06-26 10:19:25` | `cowrie.login.success` |
| `2026-06-26 10:19:25` | `cowrie.session.params` |
| `2026-06-26 10:19:25` | `cowrie.command.input` |
| `2026-06-26 10:19:26` | `cowrie.log.closed` |
| `2026-06-26 10:19:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ff902b6786c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 10:20 |
| **Last Seen** | 2026-06-26 10:20 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:20:00` | `cowrie.session.connect` |
| `2026-06-26 10:20:02` | `cowrie.client.version` |
| `2026-06-26 10:20:02` | `cowrie.client.kex` |
| `2026-06-26 10:20:07` | `cowrie.login.success` |
| `2026-06-26 10:20:11` | `cowrie.session.params` |
| `2026-06-26 10:20:11` | `cowrie.command.input` |
| `2026-06-26 10:20:13` | `cowrie.log.closed` |
| `2026-06-26 10:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74da584bac5f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:20 |
| **Last Seen** | 2026-06-26 10:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:20:12` | `cowrie.session.connect` |
| `2026-06-26 10:20:12` | `cowrie.client.version` |
| `2026-06-26 10:20:12` | `cowrie.client.kex` |
| `2026-06-26 10:20:12` | `cowrie.login.success` |
| `2026-06-26 10:20:13` | `cowrie.session.params` |
| `2026-06-26 10:20:13` | `cowrie.command.input` |
| `2026-06-26 10:20:13` | `cowrie.log.closed` |
| `2026-06-26 10:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6910ad46317

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:21 |
| **Last Seen** | 2026-06-26 10:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:21:01` | `cowrie.session.connect` |
| `2026-06-26 10:21:01` | `cowrie.client.version` |
| `2026-06-26 10:21:01` | `cowrie.client.kex` |
| `2026-06-26 10:21:01` | `cowrie.login.success` |
| `2026-06-26 10:21:02` | `cowrie.session.params` |
| `2026-06-26 10:21:02` | `cowrie.command.input` |
| `2026-06-26 10:21:02` | `cowrie.log.closed` |
| `2026-06-26 10:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc438a73f39f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 10:21 |
| **Last Seen** | 2026-06-26 10:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:21:40` | `cowrie.session.connect` |
| `2026-06-26 10:21:40` | `cowrie.client.version` |
| `2026-06-26 10:21:40` | `cowrie.client.kex` |
| `2026-06-26 10:21:43` | `cowrie.login.success` |
| `2026-06-26 10:21:45` | `cowrie.session.params` |
| `2026-06-26 10:21:45` | `cowrie.command.input` |
| `2026-06-26 10:21:45` | `cowrie.log.closed` |
| `2026-06-26 10:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c848d6a05cc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:21 |
| **Last Seen** | 2026-06-26 10:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:21:52` | `cowrie.session.connect` |
| `2026-06-26 10:21:52` | `cowrie.client.version` |
| `2026-06-26 10:21:52` | `cowrie.client.kex` |
| `2026-06-26 10:21:53` | `cowrie.login.success` |
| `2026-06-26 10:21:53` | `cowrie.session.params` |
| `2026-06-26 10:21:53` | `cowrie.command.input` |
| `2026-06-26 10:21:53` | `cowrie.log.closed` |
| `2026-06-26 10:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b7d9ba5a6e7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:22 |
| **Last Seen** | 2026-06-26 10:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:22:46` | `cowrie.session.connect` |
| `2026-06-26 10:22:46` | `cowrie.client.version` |
| `2026-06-26 10:22:46` | `cowrie.client.kex` |
| `2026-06-26 10:22:46` | `cowrie.login.success` |
| `2026-06-26 10:22:47` | `cowrie.session.params` |
| `2026-06-26 10:22:47` | `cowrie.command.input` |
| `2026-06-26 10:22:47` | `cowrie.log.closed` |
| `2026-06-26 10:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a0872356fa6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:23 |
| **Last Seen** | 2026-06-26 10:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:23:37` | `cowrie.session.connect` |
| `2026-06-26 10:23:37` | `cowrie.client.version` |
| `2026-06-26 10:23:37` | `cowrie.client.kex` |
| `2026-06-26 10:23:38` | `cowrie.login.success` |
| `2026-06-26 10:23:38` | `cowrie.session.params` |
| `2026-06-26 10:23:38` | `cowrie.command.input` |
| `2026-06-26 10:23:39` | `cowrie.log.closed` |
| `2026-06-26 10:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e264d3b4642

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:24 |
| **Last Seen** | 2026-06-26 10:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:24:28` | `cowrie.session.connect` |
| `2026-06-26 10:24:28` | `cowrie.client.version` |
| `2026-06-26 10:24:28` | `cowrie.client.kex` |
| `2026-06-26 10:24:28` | `cowrie.login.success` |
| `2026-06-26 10:24:29` | `cowrie.session.params` |
| `2026-06-26 10:24:29` | `cowrie.command.input` |
| `2026-06-26 10:24:29` | `cowrie.log.closed` |
| `2026-06-26 10:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e6096e1fa34

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:25 |
| **Last Seen** | 2026-06-26 10:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:25:17` | `cowrie.session.connect` |
| `2026-06-26 10:25:17` | `cowrie.client.version` |
| `2026-06-26 10:25:17` | `cowrie.client.kex` |
| `2026-06-26 10:25:17` | `cowrie.login.success` |
| `2026-06-26 10:25:18` | `cowrie.session.params` |
| `2026-06-26 10:25:18` | `cowrie.command.input` |
| `2026-06-26 10:25:18` | `cowrie.log.closed` |
| `2026-06-26 10:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e9b3b7592b8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:26 |
| **Last Seen** | 2026-06-26 10:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:26:07` | `cowrie.session.connect` |
| `2026-06-26 10:26:07` | `cowrie.client.version` |
| `2026-06-26 10:26:07` | `cowrie.client.kex` |
| `2026-06-26 10:26:07` | `cowrie.login.success` |
| `2026-06-26 10:26:08` | `cowrie.session.params` |
| `2026-06-26 10:26:08` | `cowrie.command.input` |
| `2026-06-26 10:26:08` | `cowrie.log.closed` |
| `2026-06-26 10:26:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e47f8ccd2b47

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:26 |
| **Last Seen** | 2026-06-26 10:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:26:56` | `cowrie.session.connect` |
| `2026-06-26 10:26:56` | `cowrie.client.version` |
| `2026-06-26 10:26:56` | `cowrie.client.kex` |
| `2026-06-26 10:26:57` | `cowrie.login.success` |
| `2026-06-26 10:26:58` | `cowrie.session.params` |
| `2026-06-26 10:26:58` | `cowrie.command.input` |
| `2026-06-26 10:26:58` | `cowrie.log.closed` |
| `2026-06-26 10:26:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af3f73621fa0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:27 |
| **Last Seen** | 2026-06-26 10:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:27:45` | `cowrie.session.connect` |
| `2026-06-26 10:27:45` | `cowrie.client.version` |
| `2026-06-26 10:27:45` | `cowrie.client.kex` |
| `2026-06-26 10:27:46` | `cowrie.login.success` |
| `2026-06-26 10:27:47` | `cowrie.session.params` |
| `2026-06-26 10:27:47` | `cowrie.command.input` |
| `2026-06-26 10:27:47` | `cowrie.log.closed` |
| `2026-06-26 10:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f66f443d920

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:28 |
| **Last Seen** | 2026-06-26 10:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:28:35` | `cowrie.session.connect` |
| `2026-06-26 10:28:35` | `cowrie.client.version` |
| `2026-06-26 10:28:35` | `cowrie.client.kex` |
| `2026-06-26 10:28:36` | `cowrie.login.success` |
| `2026-06-26 10:28:36` | `cowrie.session.params` |
| `2026-06-26 10:28:36` | `cowrie.command.input` |
| `2026-06-26 10:28:37` | `cowrie.log.closed` |
| `2026-06-26 10:28:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c78f607ba238

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:29 |
| **Last Seen** | 2026-06-26 10:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:29:26` | `cowrie.session.connect` |
| `2026-06-26 10:29:26` | `cowrie.client.version` |
| `2026-06-26 10:29:26` | `cowrie.client.kex` |
| `2026-06-26 10:29:27` | `cowrie.login.success` |
| `2026-06-26 10:29:28` | `cowrie.session.params` |
| `2026-06-26 10:29:28` | `cowrie.command.input` |
| `2026-06-26 10:29:28` | `cowrie.log.closed` |
| `2026-06-26 10:29:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b96ddb4c9d27

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:30 |
| **Last Seen** | 2026-06-26 10:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:30:17` | `cowrie.session.connect` |
| `2026-06-26 10:30:17` | `cowrie.client.version` |
| `2026-06-26 10:30:18` | `cowrie.client.kex` |
| `2026-06-26 10:30:18` | `cowrie.login.success` |
| `2026-06-26 10:30:19` | `cowrie.session.params` |
| `2026-06-26 10:30:19` | `cowrie.command.input` |
| `2026-06-26 10:30:19` | `cowrie.log.closed` |
| `2026-06-26 10:30:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7049af26965

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 10:30 |
| **Last Seen** | 2026-06-26 10:30 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:30:35` | `cowrie.session.connect` |
| `2026-06-26 10:30:37` | `cowrie.client.version` |
| `2026-06-26 10:30:37` | `cowrie.client.kex` |
| `2026-06-26 10:30:42` | `cowrie.login.success` |
| `2026-06-26 10:30:45` | `cowrie.session.params` |
| `2026-06-26 10:30:45` | `cowrie.command.input` |
| `2026-06-26 10:30:46` | `cowrie.log.closed` |
| `2026-06-26 10:30:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f32a3df08bf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:31 |
| **Last Seen** | 2026-06-26 10:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:31:08` | `cowrie.session.connect` |
| `2026-06-26 10:31:08` | `cowrie.client.version` |
| `2026-06-26 10:31:08` | `cowrie.client.kex` |
| `2026-06-26 10:31:09` | `cowrie.login.success` |
| `2026-06-26 10:31:10` | `cowrie.session.params` |
| `2026-06-26 10:31:10` | `cowrie.command.input` |
| `2026-06-26 10:31:10` | `cowrie.log.closed` |
| `2026-06-26 10:31:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c6182cfc8c7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:32 |
| **Last Seen** | 2026-06-26 10:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:32:03` | `cowrie.session.connect` |
| `2026-06-26 10:32:03` | `cowrie.client.version` |
| `2026-06-26 10:32:03` | `cowrie.client.kex` |
| `2026-06-26 10:32:04` | `cowrie.login.success` |
| `2026-06-26 10:32:05` | `cowrie.session.params` |
| `2026-06-26 10:32:05` | `cowrie.command.input` |
| `2026-06-26 10:32:05` | `cowrie.log.closed` |
| `2026-06-26 10:32:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95620c6c67e0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:32 |
| **Last Seen** | 2026-06-26 10:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:32:59` | `cowrie.session.connect` |
| `2026-06-26 10:32:59` | `cowrie.client.version` |
| `2026-06-26 10:32:59` | `cowrie.client.kex` |
| `2026-06-26 10:33:00` | `cowrie.login.success` |
| `2026-06-26 10:33:00` | `cowrie.session.params` |
| `2026-06-26 10:33:00` | `cowrie.command.input` |
| `2026-06-26 10:33:00` | `cowrie.log.closed` |
| `2026-06-26 10:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd31ad7fe7dc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:33 |
| **Last Seen** | 2026-06-26 10:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:33:51` | `cowrie.session.connect` |
| `2026-06-26 10:33:51` | `cowrie.client.version` |
| `2026-06-26 10:33:51` | `cowrie.client.kex` |
| `2026-06-26 10:33:52` | `cowrie.login.success` |
| `2026-06-26 10:33:52` | `cowrie.session.params` |
| `2026-06-26 10:33:52` | `cowrie.command.input` |
| `2026-06-26 10:33:53` | `cowrie.log.closed` |
| `2026-06-26 10:33:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e81031d07b9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:34 |
| **Last Seen** | 2026-06-26 10:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:34:47` | `cowrie.session.connect` |
| `2026-06-26 10:34:47` | `cowrie.client.version` |
| `2026-06-26 10:34:47` | `cowrie.client.kex` |
| `2026-06-26 10:34:47` | `cowrie.login.success` |
| `2026-06-26 10:34:48` | `cowrie.session.params` |
| `2026-06-26 10:34:48` | `cowrie.command.input` |
| `2026-06-26 10:34:48` | `cowrie.log.closed` |
| `2026-06-26 10:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf84b821065b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:35 |
| **Last Seen** | 2026-06-26 10:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:35:42` | `cowrie.session.connect` |
| `2026-06-26 10:35:42` | `cowrie.client.version` |
| `2026-06-26 10:35:42` | `cowrie.client.kex` |
| `2026-06-26 10:35:42` | `cowrie.login.success` |
| `2026-06-26 10:35:43` | `cowrie.session.params` |
| `2026-06-26 10:35:43` | `cowrie.command.input` |
| `2026-06-26 10:35:43` | `cowrie.log.closed` |
| `2026-06-26 10:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-773851f03aa0

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 10:36 |
| **Last Seen** | 2026-06-26 10:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:36:06` | `cowrie.session.connect` |
| `2026-06-26 10:36:06` | `cowrie.client.version` |
| `2026-06-26 10:36:06` | `cowrie.client.kex` |
| `2026-06-26 10:36:08` | `cowrie.login.success` |
| `2026-06-26 10:36:10` | `cowrie.session.params` |
| `2026-06-26 10:36:10` | `cowrie.command.input` |
| `2026-06-26 10:36:10` | `cowrie.log.closed` |
| `2026-06-26 10:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-306c726cc878

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:36 |
| **Last Seen** | 2026-06-26 10:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:36:35` | `cowrie.session.connect` |
| `2026-06-26 10:36:35` | `cowrie.client.version` |
| `2026-06-26 10:36:36` | `cowrie.client.kex` |
| `2026-06-26 10:36:36` | `cowrie.login.success` |
| `2026-06-26 10:36:37` | `cowrie.session.params` |
| `2026-06-26 10:36:37` | `cowrie.command.input` |
| `2026-06-26 10:36:37` | `cowrie.log.closed` |
| `2026-06-26 10:36:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ae218214397

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:37 |
| **Last Seen** | 2026-06-26 10:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:37:30` | `cowrie.session.connect` |
| `2026-06-26 10:37:30` | `cowrie.client.version` |
| `2026-06-26 10:37:30` | `cowrie.client.kex` |
| `2026-06-26 10:37:31` | `cowrie.login.success` |
| `2026-06-26 10:37:31` | `cowrie.session.params` |
| `2026-06-26 10:37:31` | `cowrie.command.input` |
| `2026-06-26 10:37:32` | `cowrie.log.closed` |
| `2026-06-26 10:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8837914fdba4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:38 |
| **Last Seen** | 2026-06-26 10:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:38:29` | `cowrie.session.connect` |
| `2026-06-26 10:38:29` | `cowrie.client.version` |
| `2026-06-26 10:38:29` | `cowrie.client.kex` |
| `2026-06-26 10:38:29` | `cowrie.login.success` |
| `2026-06-26 10:38:30` | `cowrie.session.params` |
| `2026-06-26 10:38:30` | `cowrie.command.input` |
| `2026-06-26 10:38:30` | `cowrie.log.closed` |
| `2026-06-26 10:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee698e15ac5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:39 |
| **Last Seen** | 2026-06-26 10:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:39:22` | `cowrie.session.connect` |
| `2026-06-26 10:39:22` | `cowrie.client.version` |
| `2026-06-26 10:39:22` | `cowrie.client.kex` |
| `2026-06-26 10:39:23` | `cowrie.login.success` |
| `2026-06-26 10:39:23` | `cowrie.session.params` |
| `2026-06-26 10:39:23` | `cowrie.command.input` |
| `2026-06-26 10:39:23` | `cowrie.log.closed` |
| `2026-06-26 10:39:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29445c17ce9b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:40 |
| **Last Seen** | 2026-06-26 10:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:40:18` | `cowrie.session.connect` |
| `2026-06-26 10:40:18` | `cowrie.client.version` |
| `2026-06-26 10:40:18` | `cowrie.client.kex` |
| `2026-06-26 10:40:18` | `cowrie.login.success` |
| `2026-06-26 10:40:19` | `cowrie.session.params` |
| `2026-06-26 10:40:19` | `cowrie.command.input` |
| `2026-06-26 10:40:19` | `cowrie.log.closed` |
| `2026-06-26 10:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f554d0aa534e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 10:41 |
| **Last Seen** | 2026-06-26 10:41 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:41:00` | `cowrie.session.connect` |
| `2026-06-26 10:41:01` | `cowrie.client.version` |
| `2026-06-26 10:41:01` | `cowrie.client.kex` |
| `2026-06-26 10:41:07` | `cowrie.login.success` |
| `2026-06-26 10:41:11` | `cowrie.session.params` |
| `2026-06-26 10:41:11` | `cowrie.command.input` |
| `2026-06-26 10:41:12` | `cowrie.log.closed` |
| `2026-06-26 10:41:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a228c821487

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:41 |
| **Last Seen** | 2026-06-26 10:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:41:15` | `cowrie.session.connect` |
| `2026-06-26 10:41:15` | `cowrie.client.version` |
| `2026-06-26 10:41:15` | `cowrie.client.kex` |
| `2026-06-26 10:41:15` | `cowrie.login.success` |
| `2026-06-26 10:41:16` | `cowrie.session.params` |
| `2026-06-26 10:41:16` | `cowrie.command.input` |
| `2026-06-26 10:41:16` | `cowrie.log.closed` |
| `2026-06-26 10:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49b6bab3b6c7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:42 |
| **Last Seen** | 2026-06-26 10:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:42:14` | `cowrie.session.connect` |
| `2026-06-26 10:42:14` | `cowrie.client.version` |
| `2026-06-26 10:42:14` | `cowrie.client.kex` |
| `2026-06-26 10:42:14` | `cowrie.login.success` |
| `2026-06-26 10:42:15` | `cowrie.session.params` |
| `2026-06-26 10:42:15` | `cowrie.command.input` |
| `2026-06-26 10:42:15` | `cowrie.log.closed` |
| `2026-06-26 10:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50c6e6b66967

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:43 |
| **Last Seen** | 2026-06-26 10:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:43:14` | `cowrie.session.connect` |
| `2026-06-26 10:43:14` | `cowrie.client.version` |
| `2026-06-26 10:43:14` | `cowrie.client.kex` |
| `2026-06-26 10:43:14` | `cowrie.login.success` |
| `2026-06-26 10:43:15` | `cowrie.session.params` |
| `2026-06-26 10:43:15` | `cowrie.command.input` |
| `2026-06-26 10:43:15` | `cowrie.log.closed` |
| `2026-06-26 10:43:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2deba7b07e78

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:44 |
| **Last Seen** | 2026-06-26 10:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:44:09` | `cowrie.session.connect` |
| `2026-06-26 10:44:09` | `cowrie.client.version` |
| `2026-06-26 10:44:09` | `cowrie.client.kex` |
| `2026-06-26 10:44:09` | `cowrie.login.success` |
| `2026-06-26 10:44:10` | `cowrie.session.params` |
| `2026-06-26 10:44:10` | `cowrie.command.input` |
| `2026-06-26 10:44:10` | `cowrie.log.closed` |
| `2026-06-26 10:44:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07aed20d51ee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:45 |
| **Last Seen** | 2026-06-26 10:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:45:06` | `cowrie.session.connect` |
| `2026-06-26 10:45:06` | `cowrie.client.version` |
| `2026-06-26 10:45:06` | `cowrie.client.kex` |
| `2026-06-26 10:45:06` | `cowrie.login.success` |
| `2026-06-26 10:45:07` | `cowrie.session.params` |
| `2026-06-26 10:45:07` | `cowrie.command.input` |
| `2026-06-26 10:45:07` | `cowrie.log.closed` |
| `2026-06-26 10:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92e43afc3cfb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:46 |
| **Last Seen** | 2026-06-26 10:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:46:01` | `cowrie.session.connect` |
| `2026-06-26 10:46:01` | `cowrie.client.version` |
| `2026-06-26 10:46:01` | `cowrie.client.kex` |
| `2026-06-26 10:46:01` | `cowrie.login.success` |
| `2026-06-26 10:46:02` | `cowrie.session.params` |
| `2026-06-26 10:46:02` | `cowrie.command.input` |
| `2026-06-26 10:46:02` | `cowrie.log.closed` |
| `2026-06-26 10:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddbef50e789f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:47 |
| **Last Seen** | 2026-06-26 10:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:47:00` | `cowrie.session.connect` |
| `2026-06-26 10:47:00` | `cowrie.client.version` |
| `2026-06-26 10:47:00` | `cowrie.client.kex` |
| `2026-06-26 10:47:00` | `cowrie.login.success` |
| `2026-06-26 10:47:01` | `cowrie.session.params` |
| `2026-06-26 10:47:01` | `cowrie.command.input` |
| `2026-06-26 10:47:01` | `cowrie.log.closed` |
| `2026-06-26 10:47:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-451b0af56fcd

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-26 10:47 |
| **Last Seen** | 2026-06-26 10:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:47:10` | `cowrie.session.connect` |
| `2026-06-26 10:47:10` | `cowrie.client.version` |
| `2026-06-26 10:47:10` | `cowrie.client.kex` |
| `2026-06-26 10:47:10` | `cowrie.login.success` |
| `2026-06-26 10:47:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a628901c6cb

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-26 10:47 |
| **Last Seen** | 2026-06-26 10:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:47:10` | `cowrie.session.connect` |
| `2026-06-26 10:47:10` | `cowrie.client.version` |
| `2026-06-26 10:47:10` | `cowrie.client.kex` |
| `2026-06-26 10:47:10` | `cowrie.login.success` |
| `2026-06-26 10:47:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2678184a119e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-26 10:47 |
| **Last Seen** | 2026-06-26 10:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:47:14` | `cowrie.session.connect` |
| `2026-06-26 10:47:14` | `cowrie.client.version` |
| `2026-06-26 10:47:14` | `cowrie.client.kex` |
| `2026-06-26 10:47:14` | `cowrie.login.success` |
| `2026-06-26 10:47:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d76eb2ac6e86

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-26 10:47 |
| **Last Seen** | 2026-06-26 10:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:47:15` | `cowrie.session.connect` |
| `2026-06-26 10:47:15` | `cowrie.client.version` |
| `2026-06-26 10:47:15` | `cowrie.client.kex` |
| `2026-06-26 10:47:15` | `cowrie.login.success` |
| `2026-06-26 10:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08c98ababc88

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:47 |
| **Last Seen** | 2026-06-26 10:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:47:57` | `cowrie.session.connect` |
| `2026-06-26 10:47:57` | `cowrie.client.version` |
| `2026-06-26 10:47:57` | `cowrie.client.kex` |
| `2026-06-26 10:47:57` | `cowrie.login.success` |
| `2026-06-26 10:47:58` | `cowrie.session.params` |
| `2026-06-26 10:47:58` | `cowrie.command.input` |
| `2026-06-26 10:47:58` | `cowrie.log.closed` |
| `2026-06-26 10:47:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2373a3647d06

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:48 |
| **Last Seen** | 2026-06-26 10:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:48:54` | `cowrie.session.connect` |
| `2026-06-26 10:48:54` | `cowrie.client.version` |
| `2026-06-26 10:48:54` | `cowrie.client.kex` |
| `2026-06-26 10:48:54` | `cowrie.login.success` |
| `2026-06-26 10:48:55` | `cowrie.session.params` |
| `2026-06-26 10:48:55` | `cowrie.command.input` |
| `2026-06-26 10:48:55` | `cowrie.log.closed` |
| `2026-06-26 10:48:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c31710a19f96

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:49 |
| **Last Seen** | 2026-06-26 10:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:49:50` | `cowrie.session.connect` |
| `2026-06-26 10:49:50` | `cowrie.client.version` |
| `2026-06-26 10:49:50` | `cowrie.client.kex` |
| `2026-06-26 10:49:50` | `cowrie.login.success` |
| `2026-06-26 10:49:51` | `cowrie.session.params` |
| `2026-06-26 10:49:51` | `cowrie.command.input` |
| `2026-06-26 10:49:51` | `cowrie.log.closed` |
| `2026-06-26 10:49:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fba0dd312dfe

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 10:50 |
| **Last Seen** | 2026-06-26 10:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:50:28` | `cowrie.session.connect` |
| `2026-06-26 10:50:28` | `cowrie.client.version` |
| `2026-06-26 10:50:28` | `cowrie.client.kex` |
| `2026-06-26 10:50:30` | `cowrie.login.success` |
| `2026-06-26 10:50:31` | `cowrie.session.params` |
| `2026-06-26 10:50:31` | `cowrie.command.input` |
| `2026-06-26 10:50:32` | `cowrie.log.closed` |
| `2026-06-26 10:50:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23aef0641aee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:50 |
| **Last Seen** | 2026-06-26 10:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:50:46` | `cowrie.session.connect` |
| `2026-06-26 10:50:46` | `cowrie.client.version` |
| `2026-06-26 10:50:46` | `cowrie.client.kex` |
| `2026-06-26 10:50:47` | `cowrie.login.success` |
| `2026-06-26 10:50:48` | `cowrie.session.params` |
| `2026-06-26 10:50:48` | `cowrie.command.input` |
| `2026-06-26 10:50:48` | `cowrie.log.closed` |
| `2026-06-26 10:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41492274f0ec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:51 |
| **Last Seen** | 2026-06-26 10:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:51:42` | `cowrie.session.connect` |
| `2026-06-26 10:51:42` | `cowrie.client.version` |
| `2026-06-26 10:51:42` | `cowrie.client.kex` |
| `2026-06-26 10:51:42` | `cowrie.login.success` |
| `2026-06-26 10:51:43` | `cowrie.session.params` |
| `2026-06-26 10:51:43` | `cowrie.command.input` |
| `2026-06-26 10:51:43` | `cowrie.log.closed` |
| `2026-06-26 10:51:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3b62b046c8a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 10:52 |
| **Last Seen** | 2026-06-26 10:52 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:52:02` | `cowrie.session.connect` |
| `2026-06-26 10:52:03` | `cowrie.client.version` |
| `2026-06-26 10:52:03` | `cowrie.client.kex` |
| `2026-06-26 10:52:10` | `cowrie.login.success` |
| `2026-06-26 10:52:14` | `cowrie.session.params` |
| `2026-06-26 10:52:14` | `cowrie.command.input` |
| `2026-06-26 10:52:15` | `cowrie.log.closed` |
| `2026-06-26 10:52:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b457e9bd9250

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:52 |
| **Last Seen** | 2026-06-26 10:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:52:39` | `cowrie.session.connect` |
| `2026-06-26 10:52:39` | `cowrie.client.version` |
| `2026-06-26 10:52:39` | `cowrie.client.kex` |
| `2026-06-26 10:52:39` | `cowrie.login.success` |
| `2026-06-26 10:52:40` | `cowrie.session.params` |
| `2026-06-26 10:52:40` | `cowrie.command.input` |
| `2026-06-26 10:52:40` | `cowrie.log.closed` |
| `2026-06-26 10:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-053ffdc8d8b2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:53 |
| **Last Seen** | 2026-06-26 10:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:53:38` | `cowrie.session.connect` |
| `2026-06-26 10:53:38` | `cowrie.client.version` |
| `2026-06-26 10:53:38` | `cowrie.client.kex` |
| `2026-06-26 10:53:39` | `cowrie.login.success` |
| `2026-06-26 10:53:40` | `cowrie.session.params` |
| `2026-06-26 10:53:40` | `cowrie.command.input` |
| `2026-06-26 10:53:40` | `cowrie.log.closed` |
| `2026-06-26 10:53:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cb98ab8960d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 10:54 |
| **Last Seen** | 2026-06-26 10:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 10:54:37` | `cowrie.session.connect` |
| `2026-06-26 10:54:37` | `cowrie.client.version` |
| `2026-06-26 10:54:37` | `cowrie.client.kex` |
| `2026-06-26 10:54:38` | `cowrie.login.success` |
| `2026-06-26 10:54:38` | `cowrie.session.params` |
| `2026-06-26 10:54:38` | `cowrie.command.input` |
| `2026-06-26 10:54:39` | `cowrie.log.closed` |
| `2026-06-26 10:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🟡 MEDIUM · IR-3325f41d3ff0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-06-26 08:55 |
| **Last Seen** | 2026-06-26 08:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **Commands Executed** | `uname -s -v -n -r -m` |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 08:55:04` | `cowrie.session.params` |
| `2026-06-26 08:55:04` | `cowrie.command.input` |
| `2026-06-26 08:55:04` | `cowrie.log.closed` |
| `2026-06-26 08:55:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `91.92.40[.]171`
- [ ] No immediate escalation required

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `209.99.185[.]59` | **128** | 2026-06-26 08:55 | 2026-06-26 10:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `216.70.97[.]74` | **5** | 2026-06-26 09:00 | 2026-06-26 09:59 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.42.141[.]232` | **3** | 2026-06-26 09:20 | 2026-06-26 09:26 | 4m | 0 | `T1592` | 🟢 LOW |
| `141.11.88[.]108` | **2** | 2026-06-26 09:50 | 2026-06-26 09:50 | 0m | 1 | `T1110.001` | 🟢 LOW |
| `159.65.233[.]253` | **2** | 2026-06-26 09:01 | 2026-06-26 09:18 | 1m | 0 | `T1592` | 🟢 LOW |
| `20.65.194[.]48` | **2** | 2026-06-26 10:54 | 2026-06-26 10:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `219.138.78[.]67` | **2** | 2026-06-26 10:21 | 2026-06-26 10:23 | 2m | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | **2** | 2026-06-26 10:46 | 2026-06-26 10:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `61.178.209[.]47` | **2** | 2026-06-26 10:32 | 2026-06-26 10:34 | 2m | 0 | `T1592` | 🟢 LOW |
| `1.220.119[.]115` | 1 | 2026-06-26 10:09 | 2026-06-26 10:09 | 30s | 0 | `T1592` | 🟢 LOW |
| `115.220.2[.]156` | 1 | 2026-06-26 10:03 | 2026-06-26 10:03 | 1s | 0 | `T1592` | 🟢 LOW |
| `118.194.235[.]105` | 1 | 2026-06-26 10:47 | 2026-06-26 10:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-06-26 10:48 | 2026-06-26 10:48 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `195.184.76[.]10` | 1 | 2026-06-26 10:18 | 2026-06-26 10:18 | 2s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-06-26 10:23 | 2026-06-26 10:23 | 35s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]79` | 1 | 2026-06-26 10:54 | 2026-06-26 10:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]92` | 1 | 2026-06-26 09:49 | 2026-06-26 09:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-06-26 09:37 | 2026-06-26 09:37 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `47.253.156[.]31` | US | Alibaba Cloud - US | **100** ⚠️ | 9 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `118.194.235[.]105` | SG | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `101.42.141[.]232` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **100** ⚠️ | 2 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `213.177.179[.]79` | NL | wcd | **100** ⚠️ | 50 |
| `91.92.40[.]171` | NL | TechTies Inc. | **100** ⚠️ | 16 |
| `219.138.78[.]67` | CN | CHINANET hubei province network | **100** ⚠️ | 7 |
| `212.8.242[.]38` | NL | WorldStream B.V. | **100** ⚠️ | 10 |
| `209.99.185[.]59` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 22 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 371 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 361 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 526 cases |
| Tool 34  | Credential Extractor        | ✅ 366 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 33 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (1.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 42 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 362 priority case(s) shown individually · 18 recon entry/entries in table (9 group(s) consolidating 148 session(s)).

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
_Report time: 2026-06-26T12:14:09Z_

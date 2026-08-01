# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-01 |
| **Generated At** | 2026-08-01T06:34:35Z |
| **Shift Time** | 06:34 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **274** |
| Confirmed Threats | **255** |
| False Positives Filtered | **19** (6.9%) |
| Unique Attacker IPs | **82** |
| Countries of Origin | **26** |
| High Severity Cases | **195** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **79** |
| Malware Samples Analyzed | **4** HIGH · **28** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **220** |
| Unique Credential Pairs | **173** |
| Unique Usernames | **82** |
| Unique Passwords | **112** |
| Successful Auth Pairs | **204** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 58 |
| `admin` | 18 |
| `user` | 15 |
| `support` | 11 |
| `test` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 14 |
| `` | 7 |
| `admin` | 6 |
| `12345678` | 6 |
| `password` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `user` | `user13` | 6 |
| `admin` | `admin` | 5 |
| `support` | `support` | 5 |
| `root` | `` | 5 |
| `345gs5662d34` | `345gs5662d34` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `1qaz@WSX` | `91.92.42.36` | 2026-08-01T02:55:05 |
| `git` | `123456` | `91.92.42.36` | 2026-08-01T02:55:12 |
| `testuser` | `test` | `91.92.42.36` | 2026-08-01T02:55:19 |
| `root` | `Aa@123456` | `91.92.42.36` | 2026-08-01T02:55:24 |
| `sysupdate` | `Password1` | `91.92.42.36` | 2026-08-01T02:55:32 |
| `root` | `Root@123` | `91.92.42.36` | 2026-08-01T02:55:38 |
| `supervisor` | `0000` | `10.0.0.73` | 2026-08-01T02:55:44 |
| `root` | `11111111` | `91.92.42.36` | 2026-08-01T02:55:45 |
| `root` | `test1234` | `91.92.42.36` | 2026-08-01T02:55:52 |
| `main` | `12345` | `91.92.42.36` | 2026-08-01T02:55:59 |
| `ansible` | `qwerty` | `91.92.42.36` | 2026-08-01T02:56:06 |
| `guest` | `111111` | `91.92.42.36` | 2026-08-01T02:56:13 |
| `root` | `qwe@123` | `91.92.42.36` | 2026-08-01T02:56:20 |
| `root` | `abc12345` | `91.92.42.36` | 2026-08-01T02:56:24 |
| `sam` | `abc123` | `91.92.42.36` | 2026-08-01T02:56:32 |
| `root` | `Passw0rd` | `91.92.42.36` | 2026-08-01T02:56:39 |
| `ts3` | `ts3` | `91.92.42.36` | 2026-08-01T02:56:45 |
| `nutanix` | `nutanix/4u` | `91.92.42.36` | 2026-08-01T02:56:52 |
| `test1` | `test1` | `91.92.42.36` | 2026-08-01T02:56:59 |
| `root` | `111111` | `91.92.42.36` | 2026-08-01T02:57:04 |
| `admin` | `admin` | `91.92.42.36` | 2026-08-01T02:57:12 |
| `support` | `Passw0rd` | `91.92.42.36` | 2026-08-01T02:57:19 |
| `master` | `123` | `91.92.42.36` | 2026-08-01T02:57:25 |
| `cursor` | `cursor` | `91.92.42.36` | 2026-08-01T02:57:32 |
| `gitlab-runner` | `passwd` | `91.92.42.36` | 2026-08-01T02:57:37 |
| `deploy` | `1` | `91.92.42.36` | 2026-08-01T02:57:45 |
| `jellyfin` | `root` | `91.92.42.36` | 2026-08-01T02:57:50 |
| `rajvir` | `rajvir123` | `91.92.42.36` | 2026-08-01T02:57:57 |
| `user` | `1234` | `91.92.42.36` | 2026-08-01T02:58:03 |
| `webuser` | `123456` | `91.92.42.36` | 2026-08-01T02:58:11 |
| `root` | `aa123456` | `91.92.42.36` | 2026-08-01T02:58:17 |
| `vncuser` | `123456` | `91.92.42.36` | 2026-08-01T02:58:23 |
| `deploy` | `rootroot` | `91.92.42.36` | 2026-08-01T02:58:30 |
| `DSL` | `DSL` | `222.190.110.210` | 2026-08-01T02:58:36 |
| `root` | `abcd@1234` | `91.92.42.36` | 2026-08-01T02:58:37 |
| `pi` | `123456` | `91.92.42.36` | 2026-08-01T02:58:43 |
| `DSL` | `DSL` | `176.172.239.193` | 2026-08-01T02:58:48 |
| `root` | `1qazXSW@` | `91.92.42.36` | 2026-08-01T02:58:49 |
| `vagrant` | `vagrant` | `91.92.42.36` | 2026-08-01T02:58:55 |
| `user` | `111111` | `91.92.42.36` | 2026-08-01T02:59:01 |
| `test` | `passwd` | `91.92.42.36` | 2026-08-01T02:59:07 |
| `root` | `qwe123456` | `91.92.42.36` | 2026-08-01T02:59:14 |
| `myuser` | `123456` | `91.92.42.36` | 2026-08-01T02:59:21 |
| `root` | `Test1234` | `91.92.42.36` | 2026-08-01T02:59:27 |
| `david` | `david` | `91.92.42.36` | 2026-08-01T02:59:33 |
| `www` | `12345678` | `91.92.42.36` | 2026-08-01T02:59:42 |
| `admin` | `!QAZ2wsx` | `91.92.42.36` | 2026-08-01T02:59:47 |
| `sam` | `1234567890` | `91.92.42.36` | 2026-08-01T02:59:54 |
| `user1` | `123456` | `91.92.42.36` | 2026-08-01T03:00:01 |
| `term2` | `term2` | `91.92.42.36` | 2026-08-01T03:00:07 |
| `frappe` | `123` | `91.92.42.36` | 2026-08-01T03:00:12 |
| `user` | `user1234` | `91.92.42.36` | 2026-08-01T03:00:19 |
| `sam` | `1qaz@WSX` | `91.92.42.36` | 2026-08-01T03:00:26 |
| `vpn` | `vpn` | `91.92.42.36` | 2026-08-01T03:00:32 |
| `sonar` | `sonar` | `91.92.42.36` | 2026-08-01T03:00:38 |
| `root` | `1qaz@WSX` | `91.92.42.36` | 2026-08-01T03:00:44 |
| `debian` | `toor` | `91.92.42.36` | 2026-08-01T03:00:49 |
| `vncuser` | `password` | `91.92.42.36` | 2026-08-01T03:00:56 |
| `tester` | `password` | `91.92.42.36` | 2026-08-01T03:01:01 |
| `sftpuser` | `123` | `91.92.42.36` | 2026-08-01T03:01:08 |
| `root` | `!QAZ2wsx3edc` | `91.92.42.36` | 2026-08-01T03:01:15 |
| `devops` | `devops` | `91.92.42.36` | 2026-08-01T03:01:23 |
| `ftp` | `ftp` | `91.92.42.36` | 2026-08-01T03:01:28 |
| `root` | `P@ssword1` | `91.92.42.36` | 2026-08-01T03:01:34 |
| `es` | `123456` | `91.92.42.36` | 2026-08-01T03:01:40 |
| `wizard` | `wizard` | `91.92.42.36` | 2026-08-01T03:01:46 |
| `mysql` | `mysql@1234` | `91.92.42.36` | 2026-08-01T03:01:53 |
| `root1` | `123456` | `91.92.42.36` | 2026-08-01T03:02:00 |
| `test` | `12345678` | `91.92.42.36` | 2026-08-01T03:02:05 |
| `claude` | `12345678` | `91.92.42.36` | 2026-08-01T03:02:11 |
| `debian` | `qwerty` | `91.92.42.36` | 2026-08-01T03:02:18 |
| `root` | `Yun@wocloud.szkj` | `91.92.42.36` | 2026-08-01T03:02:25 |
| `user4` | `user4` | `91.92.42.36` | 2026-08-01T03:02:33 |
| `root` | `qwe123!@` | `91.92.42.36` | 2026-08-01T03:02:39 |
| `support` | `support` | `176.53.159.196` | 2026-08-01T03:02:45 |
| `root` | `hello123` | `91.92.42.36` | 2026-08-01T03:02:46 |
| `steam` | `steam` | `91.92.42.36` | 2026-08-01T03:02:51 |
| `ansible` | `ansible` | `91.92.42.36` | 2026-08-01T03:02:58 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-01T03:03:01 |
| `john` | `john` | `91.92.42.36` | 2026-08-01T03:03:05 |
| `ftp` | `ftp123` | `91.92.42.36` | 2026-08-01T03:03:13 |
| `username` | `123456` | `91.92.42.36` | 2026-08-01T03:03:20 |
| `root` | `123321` | `91.92.42.36` | 2026-08-01T03:03:25 |
| `cloud-user` | `password` | `91.92.42.36` | 2026-08-01T03:03:28 |
| `prem` | `12345` | `91.92.42.36` | 2026-08-01T03:03:34 |
| `nagios` | `nagios` | `91.92.42.36` | 2026-08-01T03:03:41 |
| `support` | `123` | `91.92.42.36` | 2026-08-01T03:03:48 |
| `devops` | `1234` | `91.92.42.36` | 2026-08-01T03:03:55 |
| `fastuser` | `fastuser` | `91.92.42.36` | 2026-08-01T03:04:01 |
| `root` | `redhat` | `91.92.42.36` | 2026-08-01T03:04:08 |
| `fa` | `fa` | `91.92.42.36` | 2026-08-01T03:04:15 |
| `root` | `aA123456` | `91.92.42.36` | 2026-08-01T03:04:21 |
| `admin1` | `12345678` | `91.92.42.36` | 2026-08-01T03:04:28 |
| `user` | `rootroot` | `91.92.42.36` | 2026-08-01T03:04:33 |
| `username` | `user` | `91.92.42.36` | 2026-08-01T03:04:41 |
| `uploader` | `uploader` | `91.92.42.36` | 2026-08-01T03:04:48 |
| `tactical` | `tactical` | `91.92.42.36` | 2026-08-01T03:04:56 |
| `support` | `support` | `91.92.42.36` | 2026-08-01T03:05:01 |
| `admin1` | `redhat` | `91.92.42.36` | 2026-08-01T03:05:07 |
| `karel` | `karel` | `91.92.42.36` | 2026-08-01T03:05:13 |
| `user2` | `123` | `91.92.42.36` | 2026-08-01T03:05:18 |
| `mohammad` | `mohammad` | `91.92.42.36` | 2026-08-01T03:05:24 |
| `kingbase` | `123456` | `91.92.42.36` | 2026-08-01T03:05:30 |
| `admin` | `1qaz@WSX` | `91.92.42.36` | 2026-08-01T03:05:38 |
| `kali` | `kali` | `91.92.42.36` | 2026-08-01T03:05:43 |
| `testuser` | `123321` | `91.92.42.36` | 2026-08-01T03:05:49 |
| `zahra` | `12345678` | `91.92.42.36` | 2026-08-01T03:05:56 |
| `root` | `12345` | `35.187.231.181` | 2026-08-01T03:06:00 |
| `odoo` | `odoo` | `91.92.42.36` | 2026-08-01T03:06:02 |
| `root` | `default` | `35.187.231.181` | 2026-08-01T03:06:02 |
| `root` | `password` | `35.187.231.181` | 2026-08-01T03:06:06 |
| `root` | `Qq123456` | `91.92.42.36` | 2026-08-01T03:06:09 |
| `root` | `` | `35.187.231.181` | 2026-08-01T03:06:09 |
| `admin` | `admin` | `35.187.231.181` | 2026-08-01T03:06:12 |
| `admin` | `password` | `35.187.231.181` | 2026-08-01T03:06:15 |
| `admin` | `abc123` | `91.92.42.36` | 2026-08-01T03:06:17 |
| `admin` | `12345` | `35.187.231.181` | 2026-08-01T03:06:18 |
| `DSL` | `DSL` | `111.70.14.135` | 2026-08-01T03:06:20 |
| `admin` | `` | `35.187.231.181` | 2026-08-01T03:06:22 |
| `operator` | `operator2026` | `91.92.42.36` | 2026-08-01T03:06:23 |
| `user` | `user` | `35.187.231.181` | 2026-08-01T03:06:25 |
| `user` | `password` | `35.187.231.181` | 2026-08-01T03:06:29 |
| `admin` | `0000` | `91.92.42.36` | 2026-08-01T03:06:30 |
| `user` | `` | `35.187.231.181` | 2026-08-01T03:06:31 |
| `support` | `support` | `35.187.231.181` | 2026-08-01T03:06:35 |
| `root` | `12345qwert` | `91.92.42.36` | 2026-08-01T03:06:37 |
| `guest` | `guest` | `35.187.231.181` | 2026-08-01T03:06:38 |
| `test` | `test` | `35.187.231.181` | 2026-08-01T03:06:41 |
| `root` | `Aaaa1111` | `91.92.42.36` | 2026-08-01T03:06:45 |
| `root` | `toor` | `35.187.231.181` | 2026-08-01T03:06:46 |
| `cloud` | `1` | `91.92.42.36` | 2026-08-01T03:06:49 |
| `admin` | `123456` | `35.187.231.181` | 2026-08-01T03:06:53 |
| `root` | `admin` | `35.187.231.181` | 2026-08-01T03:06:55 |
| `bot` | `root` | `91.92.42.36` | 2026-08-01T03:06:56 |
| `student` | `123456` | `91.92.42.36` | 2026-08-01T03:07:00 |
| `amine` | `amine` | `91.92.42.36` | 2026-08-01T03:07:07 |
| `root` | `Ac123456` | `91.92.42.36` | 2026-08-01T03:07:14 |
| `root` | `1029384756` | `91.92.42.36` | 2026-08-01T03:07:21 |
| `user` | `user` | `91.92.42.36` | 2026-08-01T03:07:27 |
| `root` | `Password1` | `91.92.42.36` | 2026-08-01T03:07:40 |
| `appuser` | `test` | `91.92.42.36` | 2026-08-01T03:07:47 |
| `deploy` | `root` | `91.92.42.36` | 2026-08-01T03:07:55 |
| `master` | `qwerty` | `91.92.42.36` | 2026-08-01T03:08:00 |
| `root` | `QWEqwe123` | `91.92.42.36` | 2026-08-01T03:08:05 |
| `user` | `git` | `91.92.42.36` | 2026-08-01T03:08:11 |
| `gpadmin` | `gpadmin` | `91.92.42.36` | 2026-08-01T03:08:18 |
| `ec2-user` | `12345678` | `91.92.42.36` | 2026-08-01T03:08:25 |
| `minecraft` | `minecraft` | `91.92.42.36` | 2026-08-01T03:08:30 |
| `test` | `Password123` | `187.212.37.143` | 2026-08-01T03:12:52 |
| `345gs5662d34` | `345gs5662d34` | `187.212.37.143` | 2026-08-01T03:12:54 |
| `test` | `3245gs5662d34` | `187.212.37.143` | 2026-08-01T03:12:55 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-01T03:12:55 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-01T03:12:55 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-01T03:12:57 |
| `ubuntu` | `123@.com` | `60.54.18.211` | 2026-08-01T03:13:07 |
| `345gs5662d34` | `345gs5662d34` | `60.54.18.211` | 2026-08-01T03:13:11 |
| `ubuntu` | `3245gs5662d34` | `60.54.18.211` | 2026-08-01T03:13:13 |
| `root` | `HaCoi01@azzxxx` | `27.50.29.181` | 2026-08-01T03:18:52 |
| `admin` | `admin123!@#` | `220.80.223.144` | 2026-08-01T03:20:39 |
| `admin` | `admin` | `196.245.52.130` | 2026-08-01T03:25:14 |
| `nobody` | `nobody5` | `10.0.0.73` | 2026-08-01T03:26:06 |
| `support` | `support` | `10.0.0.73` | 2026-08-01T03:28:01 |
| `root` | `root000` | `14.54.22.11` | 2026-08-01T03:29:25 |
| `admin` | `Abcd1234` | `10.0.0.73` | 2026-08-01T03:30:27 |
| `nobody` | `nobody5` | `65.20.251.170` | 2026-08-01T03:31:20 |
| `nobody` | `nobody5` | `124.133.10.66` | 2026-08-01T03:31:29 |
| `root` | `987987` | `10.0.0.73` | 2026-08-01T03:36:03 |
| `nobody` | `nobody5` | `103.190.91.116` | 2026-08-01T03:39:00 |
| `root` | `root000` | `118.163.145.175` | 2026-08-01T03:45:43 |
| `admin` | `Abcd1234` | `196.188.93.169` | 2026-08-01T03:47:55 |
| `admin` | `Abcd1234` | `46.77.69.201` | 2026-08-01T03:48:07 |
| `support` | `abcdefgh` | `101.13.4.119` | 2026-08-01T03:53:04 |
| `root` | `IsfHh00h4f` | `8.152.171.185` | 2026-08-01T03:53:54 |
| `root` | `987987` | `220.161.52.149` | 2026-08-01T03:54:53 |
| `root` | `987987` | `220.178.39.106` | 2026-08-01T03:55:06 |
| `root` | `987987` | `196.188.93.169` | 2026-08-01T03:55:13 |
| `vignesh` | `vignesh` | `163.7.6.41` | 2026-08-01T03:55:48 |
| `345gs5662d34` | `345gs5662d34` | `163.7.6.41` | 2026-08-01T03:55:52 |
| `vignesh` | `3245gs5662d34` | `163.7.6.41` | 2026-08-01T03:55:54 |
| `testuser` | `111111` | `51.254.113.225` | 2026-08-01T03:57:57 |
| `345gs5662d34` | `345gs5662d34` | `51.254.113.225` | 2026-08-01T03:57:59 |
| `testuser` | `3245gs5662d34` | `51.254.113.225` | 2026-08-01T03:58:00 |
| `NOLOGIN` | `NOLOGIN` | `10.0.0.73` | 2026-08-01T03:58:46 |
| `centos` | `centos77` | `10.0.0.73` | 2026-08-01T04:02:01 |
| `admin` | `admin` | `118.194.235.105` | 2026-08-01T04:04:16 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-01T04:04:16 |
| `support` | `abcdefgh` | `10.0.0.73` | 2026-08-01T04:04:53 |
| `user` | `user13` | `10.0.0.73` | 2026-08-01T04:10:50 |
| `dict` | `dict@123` | `162.243.147.237` | 2026-08-01T04:18:06 |
| `345gs5662d34` | `345gs5662d34` | `162.243.147.237` | 2026-08-01T04:18:08 |
| `dict` | `3245gs5662d34` | `162.243.147.237` | 2026-08-01T04:18:08 |
| `centos` | `centos77` | `115.245.122.146` | 2026-08-01T04:20:19 |
| `centos` | `centos77` | `90.230.168.26` | 2026-08-01T04:20:26 |
| `root` | ` ` | `43.226.39.177` | 2026-08-01T04:21:15 |
| `support` | `abcdefgh` | `122.170.99.195` | 2026-08-01T04:22:29 |
| `user` | `user13` | `93.241.232.14` | 2026-08-01T04:29:43 |
| `user` | `user13` | `220.246.43.172` | 2026-08-01T04:29:53 |
| `user` | `user13` | `211.247.127.250` | 2026-08-01T04:30:01 |
| `user` | `user13` | `103.174.145.35` | 2026-08-01T04:30:09 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2223` | `8.211.21.181` | 2026-08-01T04:35:05 |
| `default` | `letmein` | `10.0.0.73` | 2026-08-01T04:36:44 |
| `supervisor` | `qwer1234` | `10.0.0.73` | 2026-08-01T04:39:49 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-01T04:41:01 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-01T04:41:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **274** |
| Sessions with Fingerprint | **18** |
| Unique HASSH Fingerprints | **18** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 156 |
| OpenSSH | 26 |
| libssh | 21 |
| Paramiko (Python) | 6 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 126 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 26 | 25 |
| `16443846184e...` | Generic scanner | 21 | 2 |
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 126 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 26 | 25 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 21 | 2 | Generic scanner |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `51.254.113.225`, `187.212.37.143`, `60.54.18.211`, `162.243.147.237`, `163.7.6.41`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **82** |
| Unique ASNs | **59** |
| High-Risk ASNs | **51** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 7 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS3301` | Telia Company AB | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS48721` | Flyservers S.A. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (195)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a75476e6ba36

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:55 |
| **Last Seen** | 2026-08-01 02:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:55:03` | `cowrie.session.connect` |
| `2026-08-01 02:55:04` | `cowrie.client.version` |
| `2026-08-01 02:55:04` | `cowrie.client.kex` |
| `2026-08-01 02:55:05` | `cowrie.login.success` |
| `2026-08-01 02:55:07` | `cowrie.session.params` |
| `2026-08-01 02:55:07` | `cowrie.command.input` |
| `2026-08-01 02:55:08` | `cowrie.log.closed` |
| `2026-08-01 02:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46f7af839335

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:55 |
| **Last Seen** | 2026-08-01 02:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:55:09` | `cowrie.session.connect` |
| `2026-08-01 02:55:10` | `cowrie.client.version` |
| `2026-08-01 02:55:10` | `cowrie.client.kex` |
| `2026-08-01 02:55:12` | `cowrie.login.success` |
| `2026-08-01 02:55:14` | `cowrie.session.params` |
| `2026-08-01 02:55:14` | `cowrie.command.input` |
| `2026-08-01 02:55:15` | `cowrie.log.closed` |
| `2026-08-01 02:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45d86d118d78

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:55 |
| **Last Seen** | 2026-08-01 02:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:55:15` | `cowrie.session.connect` |
| `2026-08-01 02:55:16` | `cowrie.client.version` |
| `2026-08-01 02:55:16` | `cowrie.client.kex` |
| `2026-08-01 02:55:19` | `cowrie.login.success` |
| `2026-08-01 02:55:21` | `cowrie.session.params` |
| `2026-08-01 02:55:21` | `cowrie.command.input` |
| `2026-08-01 02:55:22` | `cowrie.log.closed` |
| `2026-08-01 02:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bd6c41de9a6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:55 |
| **Last Seen** | 2026-08-01 02:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:55:22` | `cowrie.session.connect` |
| `2026-08-01 02:55:22` | `cowrie.client.version` |
| `2026-08-01 02:55:22` | `cowrie.client.kex` |
| `2026-08-01 02:55:24` | `cowrie.login.success` |
| `2026-08-01 02:55:26` | `cowrie.session.params` |
| `2026-08-01 02:55:26` | `cowrie.command.input` |
| `2026-08-01 02:55:27` | `cowrie.log.closed` |
| `2026-08-01 02:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f99b83751b8f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:55 |
| **Last Seen** | 2026-08-01 02:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:55:27` | `cowrie.session.connect` |
| `2026-08-01 02:55:28` | `cowrie.client.version` |
| `2026-08-01 02:55:28` | `cowrie.client.kex` |
| `2026-08-01 02:55:32` | `cowrie.login.success` |
| `2026-08-01 02:55:34` | `cowrie.session.params` |
| `2026-08-01 02:55:34` | `cowrie.command.input` |
| `2026-08-01 02:55:36` | `cowrie.log.closed` |
| `2026-08-01 02:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01d94e4c3314

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:55 |
| **Last Seen** | 2026-08-01 02:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:55:32` | `cowrie.session.connect` |
| `2026-08-01 02:55:33` | `cowrie.client.version` |
| `2026-08-01 02:55:33` | `cowrie.client.kex` |
| `2026-08-01 02:55:38` | `cowrie.login.success` |
| `2026-08-01 02:55:41` | `cowrie.session.params` |
| `2026-08-01 02:55:41` | `cowrie.command.input` |
| `2026-08-01 02:55:42` | `cowrie.log.closed` |
| `2026-08-01 02:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d4db8e33a61

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:55 |
| **Last Seen** | 2026-08-01 02:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:55:38` | `cowrie.session.connect` |
| `2026-08-01 02:55:39` | `cowrie.client.version` |
| `2026-08-01 02:55:39` | `cowrie.client.kex` |
| `2026-08-01 02:55:45` | `cowrie.login.success` |
| `2026-08-01 02:55:50` | `cowrie.session.params` |
| `2026-08-01 02:55:50` | `cowrie.command.input` |
| `2026-08-01 02:55:51` | `cowrie.log.closed` |
| `2026-08-01 02:55:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed3f53d057e7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:55 |
| **Last Seen** | 2026-08-01 02:55 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:55:44` | `cowrie.session.connect` |
| `2026-08-01 02:55:45` | `cowrie.client.version` |
| `2026-08-01 02:55:45` | `cowrie.client.kex` |
| `2026-08-01 02:55:52` | `cowrie.login.success` |
| `2026-08-01 02:55:57` | `cowrie.session.params` |
| `2026-08-01 02:55:57` | `cowrie.command.input` |
| `2026-08-01 02:55:59` | `cowrie.log.closed` |
| `2026-08-01 02:55:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cb98fad4d0a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:55 |
| **Last Seen** | 2026-08-01 02:56 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:55:50` | `cowrie.session.connect` |
| `2026-08-01 02:55:52` | `cowrie.client.version` |
| `2026-08-01 02:55:52` | `cowrie.client.kex` |
| `2026-08-01 02:55:59` | `cowrie.login.success` |
| `2026-08-01 02:56:03` | `cowrie.session.params` |
| `2026-08-01 02:56:03` | `cowrie.command.input` |
| `2026-08-01 02:56:06` | `cowrie.log.closed` |
| `2026-08-01 02:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc8f849ae0f8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:55 |
| **Last Seen** | 2026-08-01 02:56 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:55:56` | `cowrie.session.connect` |
| `2026-08-01 02:55:58` | `cowrie.client.version` |
| `2026-08-01 02:55:58` | `cowrie.client.kex` |
| `2026-08-01 02:56:06` | `cowrie.login.success` |
| `2026-08-01 02:56:11` | `cowrie.session.params` |
| `2026-08-01 02:56:11` | `cowrie.command.input` |
| `2026-08-01 02:56:13` | `cowrie.log.closed` |
| `2026-08-01 02:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-982c99e4bf53

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:56 |
| **Last Seen** | 2026-08-01 02:56 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:56:02` | `cowrie.session.connect` |
| `2026-08-01 02:56:03` | `cowrie.client.version` |
| `2026-08-01 02:56:03` | `cowrie.client.kex` |
| `2026-08-01 02:56:13` | `cowrie.login.success` |
| `2026-08-01 02:56:19` | `cowrie.session.params` |
| `2026-08-01 02:56:19` | `cowrie.command.input` |
| `2026-08-01 02:56:21` | `cowrie.log.closed` |
| `2026-08-01 02:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5333bf73339

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:56 |
| **Last Seen** | 2026-08-01 02:56 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:56:08` | `cowrie.session.connect` |
| `2026-08-01 02:56:10` | `cowrie.client.version` |
| `2026-08-01 02:56:10` | `cowrie.client.kex` |
| `2026-08-01 02:56:20` | `cowrie.login.success` |
| `2026-08-01 02:56:23` | `cowrie.session.params` |
| `2026-08-01 02:56:23` | `cowrie.command.input` |
| `2026-08-01 02:56:25` | `cowrie.log.closed` |
| `2026-08-01 02:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b4d4db61236

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:56 |
| **Last Seen** | 2026-08-01 02:56 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:56:13` | `cowrie.session.connect` |
| `2026-08-01 02:56:17` | `cowrie.client.version` |
| `2026-08-01 02:56:17` | `cowrie.client.kex` |
| `2026-08-01 02:56:24` | `cowrie.login.success` |
| `2026-08-01 02:56:28` | `cowrie.session.params` |
| `2026-08-01 02:56:28` | `cowrie.command.input` |
| `2026-08-01 02:56:30` | `cowrie.log.closed` |
| `2026-08-01 02:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49c18c0450d8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:56 |
| **Last Seen** | 2026-08-01 02:56 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:56:23` | `cowrie.session.connect` |
| `2026-08-01 02:56:24` | `cowrie.client.version` |
| `2026-08-01 02:56:24` | `cowrie.client.kex` |
| `2026-08-01 02:56:32` | `cowrie.login.success` |
| `2026-08-01 02:56:37` | `cowrie.session.params` |
| `2026-08-01 02:56:37` | `cowrie.command.input` |
| `2026-08-01 02:56:39` | `cowrie.log.closed` |
| `2026-08-01 02:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7d949c25c39

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:56 |
| **Last Seen** | 2026-08-01 02:56 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:56:29` | `cowrie.session.connect` |
| `2026-08-01 02:56:30` | `cowrie.client.version` |
| `2026-08-01 02:56:30` | `cowrie.client.kex` |
| `2026-08-01 02:56:39` | `cowrie.login.success` |
| `2026-08-01 02:56:43` | `cowrie.session.params` |
| `2026-08-01 02:56:43` | `cowrie.command.input` |
| `2026-08-01 02:56:45` | `cowrie.log.closed` |
| `2026-08-01 02:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be3a6d71ddbd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:56 |
| **Last Seen** | 2026-08-01 02:56 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:56:36` | `cowrie.session.connect` |
| `2026-08-01 02:56:38` | `cowrie.client.version` |
| `2026-08-01 02:56:38` | `cowrie.client.kex` |
| `2026-08-01 02:56:45` | `cowrie.login.success` |
| `2026-08-01 02:56:50` | `cowrie.session.params` |
| `2026-08-01 02:56:50` | `cowrie.command.input` |
| `2026-08-01 02:56:52` | `cowrie.log.closed` |
| `2026-08-01 02:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56159ac8a396

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:56 |
| **Last Seen** | 2026-08-01 02:56 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:56:43` | `cowrie.session.connect` |
| `2026-08-01 02:56:45` | `cowrie.client.version` |
| `2026-08-01 02:56:45` | `cowrie.client.kex` |
| `2026-08-01 02:56:52` | `cowrie.login.success` |
| `2026-08-01 02:56:58` | `cowrie.session.params` |
| `2026-08-01 02:56:58` | `cowrie.command.input` |
| `2026-08-01 02:56:59` | `cowrie.log.closed` |
| `2026-08-01 02:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2994389d2607

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:56 |
| **Last Seen** | 2026-08-01 02:57 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:56:49` | `cowrie.session.connect` |
| `2026-08-01 02:56:50` | `cowrie.client.version` |
| `2026-08-01 02:56:50` | `cowrie.client.kex` |
| `2026-08-01 02:56:59` | `cowrie.login.success` |
| `2026-08-01 02:57:02` | `cowrie.session.params` |
| `2026-08-01 02:57:02` | `cowrie.command.input` |
| `2026-08-01 02:57:03` | `cowrie.log.closed` |
| `2026-08-01 02:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19973841c354

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:56 |
| **Last Seen** | 2026-08-01 02:57 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:56:56` | `cowrie.session.connect` |
| `2026-08-01 02:56:58` | `cowrie.client.version` |
| `2026-08-01 02:56:58` | `cowrie.client.kex` |
| `2026-08-01 02:57:04` | `cowrie.login.success` |
| `2026-08-01 02:57:07` | `cowrie.session.params` |
| `2026-08-01 02:57:07` | `cowrie.command.input` |
| `2026-08-01 02:57:08` | `cowrie.log.closed` |
| `2026-08-01 02:57:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f089a864dc2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:57 |
| **Last Seen** | 2026-08-01 02:57 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:57:04` | `cowrie.session.connect` |
| `2026-08-01 02:57:05` | `cowrie.client.version` |
| `2026-08-01 02:57:05` | `cowrie.client.kex` |
| `2026-08-01 02:57:12` | `cowrie.login.success` |
| `2026-08-01 02:57:16` | `cowrie.session.params` |
| `2026-08-01 02:57:16` | `cowrie.command.input` |
| `2026-08-01 02:57:18` | `cowrie.log.closed` |
| `2026-08-01 02:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-022858e0346c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:57 |
| **Last Seen** | 2026-08-01 02:57 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:57:09` | `cowrie.session.connect` |
| `2026-08-01 02:57:11` | `cowrie.client.version` |
| `2026-08-01 02:57:11` | `cowrie.client.kex` |
| `2026-08-01 02:57:19` | `cowrie.login.success` |
| `2026-08-01 02:57:23` | `cowrie.session.params` |
| `2026-08-01 02:57:23` | `cowrie.command.input` |
| `2026-08-01 02:57:25` | `cowrie.log.closed` |
| `2026-08-01 02:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd4db1aa6551

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:57 |
| **Last Seen** | 2026-08-01 02:57 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:57:16` | `cowrie.session.connect` |
| `2026-08-01 02:57:17` | `cowrie.client.version` |
| `2026-08-01 02:57:17` | `cowrie.client.kex` |
| `2026-08-01 02:57:25` | `cowrie.login.success` |
| `2026-08-01 02:57:29` | `cowrie.session.params` |
| `2026-08-01 02:57:29` | `cowrie.command.input` |
| `2026-08-01 02:57:31` | `cowrie.log.closed` |
| `2026-08-01 02:57:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44464fc3fa48

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:57 |
| **Last Seen** | 2026-08-01 02:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:57:23` | `cowrie.session.connect` |
| `2026-08-01 02:57:25` | `cowrie.client.version` |
| `2026-08-01 02:57:25` | `cowrie.client.kex` |
| `2026-08-01 02:57:32` | `cowrie.login.success` |
| `2026-08-01 02:57:34` | `cowrie.session.params` |
| `2026-08-01 02:57:34` | `cowrie.command.input` |
| `2026-08-01 02:57:35` | `cowrie.log.closed` |
| `2026-08-01 02:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb0a2291eacc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:57 |
| **Last Seen** | 2026-08-01 02:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:57:31` | `cowrie.session.connect` |
| `2026-08-01 02:57:32` | `cowrie.client.version` |
| `2026-08-01 02:57:32` | `cowrie.client.kex` |
| `2026-08-01 02:57:37` | `cowrie.login.success` |
| `2026-08-01 02:57:40` | `cowrie.session.params` |
| `2026-08-01 02:57:40` | `cowrie.command.input` |
| `2026-08-01 02:57:41` | `cowrie.log.closed` |
| `2026-08-01 02:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b276efdc85a9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:57 |
| **Last Seen** | 2026-08-01 02:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:57:38` | `cowrie.session.connect` |
| `2026-08-01 02:57:40` | `cowrie.client.version` |
| `2026-08-01 02:57:40` | `cowrie.client.kex` |
| `2026-08-01 02:57:45` | `cowrie.login.success` |
| `2026-08-01 02:57:47` | `cowrie.session.params` |
| `2026-08-01 02:57:47` | `cowrie.command.input` |
| `2026-08-01 02:57:49` | `cowrie.log.closed` |
| `2026-08-01 02:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2069191aedf8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:57 |
| **Last Seen** | 2026-08-01 02:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:57:44` | `cowrie.session.connect` |
| `2026-08-01 02:57:45` | `cowrie.client.version` |
| `2026-08-01 02:57:45` | `cowrie.client.kex` |
| `2026-08-01 02:57:50` | `cowrie.login.success` |
| `2026-08-01 02:57:53` | `cowrie.session.params` |
| `2026-08-01 02:57:53` | `cowrie.command.input` |
| `2026-08-01 02:57:55` | `cowrie.log.closed` |
| `2026-08-01 02:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-497fc41ab71f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:57 |
| **Last Seen** | 2026-08-01 02:58 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:57:50` | `cowrie.session.connect` |
| `2026-08-01 02:57:52` | `cowrie.client.version` |
| `2026-08-01 02:57:52` | `cowrie.client.kex` |
| `2026-08-01 02:57:57` | `cowrie.login.success` |
| `2026-08-01 02:58:01` | `cowrie.session.params` |
| `2026-08-01 02:58:01` | `cowrie.command.input` |
| `2026-08-01 02:58:02` | `cowrie.log.closed` |
| `2026-08-01 02:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a4741a97493

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:57 |
| **Last Seen** | 2026-08-01 02:58 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:57:56` | `cowrie.session.connect` |
| `2026-08-01 02:57:58` | `cowrie.client.version` |
| `2026-08-01 02:57:58` | `cowrie.client.kex` |
| `2026-08-01 02:58:03` | `cowrie.login.success` |
| `2026-08-01 02:58:07` | `cowrie.session.params` |
| `2026-08-01 02:58:07` | `cowrie.command.input` |
| `2026-08-01 02:58:08` | `cowrie.log.closed` |
| `2026-08-01 02:58:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afcf9eddc5e8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:58 |
| **Last Seen** | 2026-08-01 02:58 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:58:03` | `cowrie.session.connect` |
| `2026-08-01 02:58:04` | `cowrie.client.version` |
| `2026-08-01 02:58:04` | `cowrie.client.kex` |
| `2026-08-01 02:58:11` | `cowrie.login.success` |
| `2026-08-01 02:58:15` | `cowrie.session.params` |
| `2026-08-01 02:58:15` | `cowrie.command.input` |
| `2026-08-01 02:58:16` | `cowrie.log.closed` |
| `2026-08-01 02:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4a9059073da

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:58 |
| **Last Seen** | 2026-08-01 02:58 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:58:09` | `cowrie.session.connect` |
| `2026-08-01 02:58:11` | `cowrie.client.version` |
| `2026-08-01 02:58:11` | `cowrie.client.kex` |
| `2026-08-01 02:58:17` | `cowrie.login.success` |
| `2026-08-01 02:58:19` | `cowrie.session.params` |
| `2026-08-01 02:58:19` | `cowrie.command.input` |
| `2026-08-01 02:58:20` | `cowrie.log.closed` |
| `2026-08-01 02:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dcbee8450bd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:58 |
| **Last Seen** | 2026-08-01 02:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:58:17` | `cowrie.session.connect` |
| `2026-08-01 02:58:18` | `cowrie.client.version` |
| `2026-08-01 02:58:18` | `cowrie.client.kex` |
| `2026-08-01 02:58:23` | `cowrie.login.success` |
| `2026-08-01 02:58:26` | `cowrie.session.params` |
| `2026-08-01 02:58:26` | `cowrie.command.input` |
| `2026-08-01 02:58:27` | `cowrie.log.closed` |
| `2026-08-01 02:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57141f9d8539

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:58 |
| **Last Seen** | 2026-08-01 02:58 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:58:24` | `cowrie.session.connect` |
| `2026-08-01 02:58:25` | `cowrie.client.version` |
| `2026-08-01 02:58:25` | `cowrie.client.kex` |
| `2026-08-01 02:58:30` | `cowrie.login.success` |
| `2026-08-01 02:58:34` | `cowrie.session.params` |
| `2026-08-01 02:58:34` | `cowrie.command.input` |
| `2026-08-01 02:58:36` | `cowrie.log.closed` |
| `2026-08-01 02:58:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a461fb28ed5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:58 |
| **Last Seen** | 2026-08-01 02:58 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:58:30` | `cowrie.session.connect` |
| `2026-08-01 02:58:31` | `cowrie.client.version` |
| `2026-08-01 02:58:31` | `cowrie.client.kex` |
| `2026-08-01 02:58:37` | `cowrie.login.success` |
| `2026-08-01 02:58:41` | `cowrie.session.params` |
| `2026-08-01 02:58:41` | `cowrie.command.input` |
| `2026-08-01 02:58:43` | `cowrie.log.closed` |
| `2026-08-01 02:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ef1b7bcbcc8

| Field | Detail |
|---|---|
| **Source IP** | `222.190.110[.]210` |
| **First Seen** | 2026-08-01 02:58 |
| **Last Seen** | 2026-08-01 02:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:58:31` | `cowrie.session.connect` |
| `2026-08-01 02:58:32` | `cowrie.client.version` |
| `2026-08-01 02:58:32` | `cowrie.client.kex` |
| `2026-08-01 02:58:36` | `cowrie.login.success` |
| `2026-08-01 02:58:36` | `cowrie.direct-tcpip.request` |
| `2026-08-01 02:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.190.110[.]210` to AbuseIPDB if not already reported
- [ ] Block `222.190.110[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3e477481892

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:58 |
| **Last Seen** | 2026-08-01 02:58 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:58:35` | `cowrie.session.connect` |
| `2026-08-01 02:58:37` | `cowrie.client.version` |
| `2026-08-01 02:58:37` | `cowrie.client.kex` |
| `2026-08-01 02:58:43` | `cowrie.login.success` |
| `2026-08-01 02:58:46` | `cowrie.session.params` |
| `2026-08-01 02:58:47` | `cowrie.command.input` |
| `2026-08-01 02:58:48` | `cowrie.log.closed` |
| `2026-08-01 02:58:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3c6416cd0aa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:58 |
| **Last Seen** | 2026-08-01 02:58 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:58:41` | `cowrie.session.connect` |
| `2026-08-01 02:58:43` | `cowrie.client.version` |
| `2026-08-01 02:58:43` | `cowrie.client.kex` |
| `2026-08-01 02:58:49` | `cowrie.login.success` |
| `2026-08-01 02:58:54` | `cowrie.session.params` |
| `2026-08-01 02:58:54` | `cowrie.command.input` |
| `2026-08-01 02:58:55` | `cowrie.log.closed` |
| `2026-08-01 02:58:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2286de62c4da

| Field | Detail |
|---|---|
| **Source IP** | `176.172.239[.]193` |
| **First Seen** | 2026-08-01 02:58 |
| **Last Seen** | 2026-08-01 02:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:58:47` | `cowrie.session.connect` |
| `2026-08-01 02:58:47` | `cowrie.client.version` |
| `2026-08-01 02:58:47` | `cowrie.client.kex` |
| `2026-08-01 02:58:48` | `cowrie.login.success` |
| `2026-08-01 02:58:48` | `cowrie.direct-tcpip.request` |
| `2026-08-01 02:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.172.239[.]193` to AbuseIPDB if not already reported
- [ ] Block `176.172.239[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8b3784e54e3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:58 |
| **Last Seen** | 2026-08-01 02:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:58:48` | `cowrie.session.connect` |
| `2026-08-01 02:58:49` | `cowrie.client.version` |
| `2026-08-01 02:58:49` | `cowrie.client.kex` |
| `2026-08-01 02:58:55` | `cowrie.login.success` |
| `2026-08-01 02:58:57` | `cowrie.session.params` |
| `2026-08-01 02:58:57` | `cowrie.command.input` |
| `2026-08-01 02:58:58` | `cowrie.log.closed` |
| `2026-08-01 02:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b83311ca375a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:58 |
| **Last Seen** | 2026-08-01 02:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:58:56` | `cowrie.session.connect` |
| `2026-08-01 02:58:57` | `cowrie.client.version` |
| `2026-08-01 02:58:57` | `cowrie.client.kex` |
| `2026-08-01 02:59:01` | `cowrie.login.success` |
| `2026-08-01 02:59:03` | `cowrie.session.params` |
| `2026-08-01 02:59:03` | `cowrie.command.input` |
| `2026-08-01 02:59:03` | `cowrie.log.closed` |
| `2026-08-01 02:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8384032598e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:59 |
| **Last Seen** | 2026-08-01 02:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:59:03` | `cowrie.session.connect` |
| `2026-08-01 02:59:04` | `cowrie.client.version` |
| `2026-08-01 02:59:04` | `cowrie.client.kex` |
| `2026-08-01 02:59:07` | `cowrie.login.success` |
| `2026-08-01 02:59:09` | `cowrie.session.params` |
| `2026-08-01 02:59:09` | `cowrie.command.input` |
| `2026-08-01 02:59:10` | `cowrie.log.closed` |
| `2026-08-01 02:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c2ad36d8ec6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:59 |
| **Last Seen** | 2026-08-01 02:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:59:09` | `cowrie.session.connect` |
| `2026-08-01 02:59:10` | `cowrie.client.version` |
| `2026-08-01 02:59:10` | `cowrie.client.kex` |
| `2026-08-01 02:59:14` | `cowrie.login.success` |
| `2026-08-01 02:59:17` | `cowrie.session.params` |
| `2026-08-01 02:59:17` | `cowrie.command.input` |
| `2026-08-01 02:59:18` | `cowrie.log.closed` |
| `2026-08-01 02:59:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a07f0b26f86

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:59 |
| **Last Seen** | 2026-08-01 02:59 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:59:15` | `cowrie.session.connect` |
| `2026-08-01 02:59:16` | `cowrie.client.version` |
| `2026-08-01 02:59:16` | `cowrie.client.kex` |
| `2026-08-01 02:59:21` | `cowrie.login.success` |
| `2026-08-01 02:59:24` | `cowrie.session.params` |
| `2026-08-01 02:59:24` | `cowrie.command.input` |
| `2026-08-01 02:59:26` | `cowrie.log.closed` |
| `2026-08-01 02:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d6324a8b272

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:59 |
| **Last Seen** | 2026-08-01 02:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:59:20` | `cowrie.session.connect` |
| `2026-08-01 02:59:22` | `cowrie.client.version` |
| `2026-08-01 02:59:22` | `cowrie.client.kex` |
| `2026-08-01 02:59:27` | `cowrie.login.success` |
| `2026-08-01 02:59:29` | `cowrie.session.params` |
| `2026-08-01 02:59:29` | `cowrie.command.input` |
| `2026-08-01 02:59:30` | `cowrie.log.closed` |
| `2026-08-01 02:59:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-984e5729695c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:59 |
| **Last Seen** | 2026-08-01 02:59 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:59:28` | `cowrie.session.connect` |
| `2026-08-01 02:59:29` | `cowrie.client.version` |
| `2026-08-01 02:59:29` | `cowrie.client.kex` |
| `2026-08-01 02:59:33` | `cowrie.login.success` |
| `2026-08-01 02:59:37` | `cowrie.session.params` |
| `2026-08-01 02:59:37` | `cowrie.command.input` |
| `2026-08-01 02:59:39` | `cowrie.log.closed` |
| `2026-08-01 02:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9dad16aabea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:59 |
| **Last Seen** | 2026-08-01 02:59 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:59:33` | `cowrie.session.connect` |
| `2026-08-01 02:59:34` | `cowrie.client.version` |
| `2026-08-01 02:59:34` | `cowrie.client.kex` |
| `2026-08-01 02:59:42` | `cowrie.login.success` |
| `2026-08-01 02:59:45` | `cowrie.session.params` |
| `2026-08-01 02:59:45` | `cowrie.command.input` |
| `2026-08-01 02:59:47` | `cowrie.log.closed` |
| `2026-08-01 02:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39322985e5a8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:59 |
| **Last Seen** | 2026-08-01 02:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:59:38` | `cowrie.session.connect` |
| `2026-08-01 02:59:41` | `cowrie.client.version` |
| `2026-08-01 02:59:41` | `cowrie.client.kex` |
| `2026-08-01 02:59:47` | `cowrie.login.success` |
| `2026-08-01 02:59:50` | `cowrie.session.params` |
| `2026-08-01 02:59:50` | `cowrie.command.input` |
| `2026-08-01 02:59:52` | `cowrie.log.closed` |
| `2026-08-01 02:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e6034bcd8fd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:59 |
| **Last Seen** | 2026-08-01 02:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:59:46` | `cowrie.session.connect` |
| `2026-08-01 02:59:48` | `cowrie.client.version` |
| `2026-08-01 02:59:48` | `cowrie.client.kex` |
| `2026-08-01 02:59:54` | `cowrie.login.success` |
| `2026-08-01 02:59:58` | `cowrie.session.params` |
| `2026-08-01 02:59:58` | `cowrie.command.input` |
| `2026-08-01 02:59:59` | `cowrie.log.closed` |
| `2026-08-01 02:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c64d1a1c636

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 02:59 |
| **Last Seen** | 2026-08-01 03:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 02:59:53` | `cowrie.session.connect` |
| `2026-08-01 02:59:55` | `cowrie.client.version` |
| `2026-08-01 02:59:55` | `cowrie.client.kex` |
| `2026-08-01 03:00:01` | `cowrie.login.success` |
| `2026-08-01 03:00:05` | `cowrie.session.params` |
| `2026-08-01 03:00:05` | `cowrie.command.input` |
| `2026-08-01 03:00:06` | `cowrie.log.closed` |
| `2026-08-01 03:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-478c81e6f968

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:00 |
| **Last Seen** | 2026-08-01 03:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:00:00` | `cowrie.session.connect` |
| `2026-08-01 03:00:02` | `cowrie.client.version` |
| `2026-08-01 03:00:02` | `cowrie.client.kex` |
| `2026-08-01 03:00:07` | `cowrie.login.success` |
| `2026-08-01 03:00:11` | `cowrie.session.params` |
| `2026-08-01 03:00:11` | `cowrie.command.input` |
| `2026-08-01 03:00:12` | `cowrie.log.closed` |
| `2026-08-01 03:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41cca1e9634f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:00 |
| **Last Seen** | 2026-08-01 03:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:00:06` | `cowrie.session.connect` |
| `2026-08-01 03:00:07` | `cowrie.client.version` |
| `2026-08-01 03:00:07` | `cowrie.client.kex` |
| `2026-08-01 03:00:12` | `cowrie.login.success` |
| `2026-08-01 03:00:15` | `cowrie.session.params` |
| `2026-08-01 03:00:15` | `cowrie.command.input` |
| `2026-08-01 03:00:16` | `cowrie.log.closed` |
| `2026-08-01 03:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afa084956111

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:00 |
| **Last Seen** | 2026-08-01 03:00 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:00:14` | `cowrie.session.connect` |
| `2026-08-01 03:00:15` | `cowrie.client.version` |
| `2026-08-01 03:00:15` | `cowrie.client.kex` |
| `2026-08-01 03:00:19` | `cowrie.login.success` |
| `2026-08-01 03:00:22` | `cowrie.session.params` |
| `2026-08-01 03:00:22` | `cowrie.command.input` |
| `2026-08-01 03:00:24` | `cowrie.log.closed` |
| `2026-08-01 03:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fe4931ba2a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:00 |
| **Last Seen** | 2026-08-01 03:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:00:20` | `cowrie.session.connect` |
| `2026-08-01 03:00:21` | `cowrie.client.version` |
| `2026-08-01 03:00:21` | `cowrie.client.kex` |
| `2026-08-01 03:00:26` | `cowrie.login.success` |
| `2026-08-01 03:00:27` | `cowrie.session.params` |
| `2026-08-01 03:00:27` | `cowrie.command.input` |
| `2026-08-01 03:00:28` | `cowrie.log.closed` |
| `2026-08-01 03:00:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdedadbebc49

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:00 |
| **Last Seen** | 2026-08-01 03:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:00:27` | `cowrie.session.connect` |
| `2026-08-01 03:00:28` | `cowrie.client.version` |
| `2026-08-01 03:00:28` | `cowrie.client.kex` |
| `2026-08-01 03:00:32` | `cowrie.login.success` |
| `2026-08-01 03:00:34` | `cowrie.session.params` |
| `2026-08-01 03:00:34` | `cowrie.command.input` |
| `2026-08-01 03:00:34` | `cowrie.log.closed` |
| `2026-08-01 03:00:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3acde0d81ca7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:00 |
| **Last Seen** | 2026-08-01 03:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:00:34` | `cowrie.session.connect` |
| `2026-08-01 03:00:35` | `cowrie.client.version` |
| `2026-08-01 03:00:35` | `cowrie.client.kex` |
| `2026-08-01 03:00:38` | `cowrie.login.success` |
| `2026-08-01 03:00:40` | `cowrie.session.params` |
| `2026-08-01 03:00:40` | `cowrie.command.input` |
| `2026-08-01 03:00:41` | `cowrie.log.closed` |
| `2026-08-01 03:00:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bea1114d66ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:00 |
| **Last Seen** | 2026-08-01 03:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:00:40` | `cowrie.session.connect` |
| `2026-08-01 03:00:40` | `cowrie.client.version` |
| `2026-08-01 03:00:40` | `cowrie.client.kex` |
| `2026-08-01 03:00:44` | `cowrie.login.success` |
| `2026-08-01 03:00:45` | `cowrie.session.params` |
| `2026-08-01 03:00:45` | `cowrie.command.input` |
| `2026-08-01 03:00:46` | `cowrie.log.closed` |
| `2026-08-01 03:00:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e069c7b4ef79

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:00 |
| **Last Seen** | 2026-08-01 03:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:00:48` | `cowrie.session.connect` |
| `2026-08-01 03:00:48` | `cowrie.client.version` |
| `2026-08-01 03:00:48` | `cowrie.client.kex` |
| `2026-08-01 03:00:49` | `cowrie.login.success` |
| `2026-08-01 03:00:51` | `cowrie.session.params` |
| `2026-08-01 03:00:51` | `cowrie.command.input` |
| `2026-08-01 03:00:51` | `cowrie.log.closed` |
| `2026-08-01 03:00:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5525d70f0d37

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:00 |
| **Last Seen** | 2026-08-01 03:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:00:53` | `cowrie.session.connect` |
| `2026-08-01 03:00:54` | `cowrie.client.version` |
| `2026-08-01 03:00:54` | `cowrie.client.kex` |
| `2026-08-01 03:00:56` | `cowrie.login.success` |
| `2026-08-01 03:00:58` | `cowrie.session.params` |
| `2026-08-01 03:00:58` | `cowrie.command.input` |
| `2026-08-01 03:00:58` | `cowrie.log.closed` |
| `2026-08-01 03:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-add8e6ecfa17

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:01 |
| **Last Seen** | 2026-08-01 03:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:01:00` | `cowrie.session.connect` |
| `2026-08-01 03:01:00` | `cowrie.client.version` |
| `2026-08-01 03:01:00` | `cowrie.client.kex` |
| `2026-08-01 03:01:01` | `cowrie.login.success` |
| `2026-08-01 03:01:03` | `cowrie.session.params` |
| `2026-08-01 03:01:03` | `cowrie.command.input` |
| `2026-08-01 03:01:03` | `cowrie.log.closed` |
| `2026-08-01 03:01:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad388bf6fb7e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:01 |
| **Last Seen** | 2026-08-01 03:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:01:06` | `cowrie.session.connect` |
| `2026-08-01 03:01:06` | `cowrie.client.version` |
| `2026-08-01 03:01:06` | `cowrie.client.kex` |
| `2026-08-01 03:01:08` | `cowrie.login.success` |
| `2026-08-01 03:01:10` | `cowrie.session.params` |
| `2026-08-01 03:01:10` | `cowrie.command.input` |
| `2026-08-01 03:01:11` | `cowrie.log.closed` |
| `2026-08-01 03:01:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3e1d274bab8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:01 |
| **Last Seen** | 2026-08-01 03:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:01:12` | `cowrie.session.connect` |
| `2026-08-01 03:01:13` | `cowrie.client.version` |
| `2026-08-01 03:01:13` | `cowrie.client.kex` |
| `2026-08-01 03:01:15` | `cowrie.login.success` |
| `2026-08-01 03:01:16` | `cowrie.session.params` |
| `2026-08-01 03:01:16` | `cowrie.command.input` |
| `2026-08-01 03:01:17` | `cowrie.log.closed` |
| `2026-08-01 03:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdfe39c47a94

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:01 |
| **Last Seen** | 2026-08-01 03:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:01:18` | `cowrie.session.connect` |
| `2026-08-01 03:01:19` | `cowrie.client.version` |
| `2026-08-01 03:01:19` | `cowrie.client.kex` |
| `2026-08-01 03:01:23` | `cowrie.login.success` |
| `2026-08-01 03:01:24` | `cowrie.session.params` |
| `2026-08-01 03:01:24` | `cowrie.command.input` |
| `2026-08-01 03:01:25` | `cowrie.log.closed` |
| `2026-08-01 03:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f916bcc5696e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:01 |
| **Last Seen** | 2026-08-01 03:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:01:25` | `cowrie.session.connect` |
| `2026-08-01 03:01:26` | `cowrie.client.version` |
| `2026-08-01 03:01:26` | `cowrie.client.kex` |
| `2026-08-01 03:01:28` | `cowrie.login.success` |
| `2026-08-01 03:01:30` | `cowrie.session.params` |
| `2026-08-01 03:01:30` | `cowrie.command.input` |
| `2026-08-01 03:01:31` | `cowrie.log.closed` |
| `2026-08-01 03:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f68a16a8fae4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:01 |
| **Last Seen** | 2026-08-01 03:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:01:32` | `cowrie.session.connect` |
| `2026-08-01 03:01:32` | `cowrie.client.version` |
| `2026-08-01 03:01:32` | `cowrie.client.kex` |
| `2026-08-01 03:01:34` | `cowrie.login.success` |
| `2026-08-01 03:01:36` | `cowrie.session.params` |
| `2026-08-01 03:01:36` | `cowrie.command.input` |
| `2026-08-01 03:01:36` | `cowrie.log.closed` |
| `2026-08-01 03:01:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f95c160330a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:01 |
| **Last Seen** | 2026-08-01 03:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:01:38` | `cowrie.session.connect` |
| `2026-08-01 03:01:38` | `cowrie.client.version` |
| `2026-08-01 03:01:38` | `cowrie.client.kex` |
| `2026-08-01 03:01:40` | `cowrie.login.success` |
| `2026-08-01 03:01:41` | `cowrie.session.params` |
| `2026-08-01 03:01:41` | `cowrie.command.input` |
| `2026-08-01 03:01:41` | `cowrie.log.closed` |
| `2026-08-01 03:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e97521d0c166

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:01 |
| **Last Seen** | 2026-08-01 03:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:01:45` | `cowrie.session.connect` |
| `2026-08-01 03:01:45` | `cowrie.client.version` |
| `2026-08-01 03:01:45` | `cowrie.client.kex` |
| `2026-08-01 03:01:46` | `cowrie.login.success` |
| `2026-08-01 03:01:48` | `cowrie.session.params` |
| `2026-08-01 03:01:48` | `cowrie.command.input` |
| `2026-08-01 03:01:48` | `cowrie.log.closed` |
| `2026-08-01 03:01:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dd01652274a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:01 |
| **Last Seen** | 2026-08-01 03:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:01:50` | `cowrie.session.connect` |
| `2026-08-01 03:01:51` | `cowrie.client.version` |
| `2026-08-01 03:01:51` | `cowrie.client.kex` |
| `2026-08-01 03:01:53` | `cowrie.login.success` |
| `2026-08-01 03:01:56` | `cowrie.session.params` |
| `2026-08-01 03:01:56` | `cowrie.command.input` |
| `2026-08-01 03:01:57` | `cowrie.log.closed` |
| `2026-08-01 03:01:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f33b503561e9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:01 |
| **Last Seen** | 2026-08-01 03:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:01:56` | `cowrie.session.connect` |
| `2026-08-01 03:01:57` | `cowrie.client.version` |
| `2026-08-01 03:01:57` | `cowrie.client.kex` |
| `2026-08-01 03:02:00` | `cowrie.login.success` |
| `2026-08-01 03:02:01` | `cowrie.session.params` |
| `2026-08-01 03:02:01` | `cowrie.command.input` |
| `2026-08-01 03:02:02` | `cowrie.log.closed` |
| `2026-08-01 03:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d55265b70440

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:02 |
| **Last Seen** | 2026-08-01 03:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:02:02` | `cowrie.session.connect` |
| `2026-08-01 03:02:03` | `cowrie.client.version` |
| `2026-08-01 03:02:03` | `cowrie.client.kex` |
| `2026-08-01 03:02:05` | `cowrie.login.success` |
| `2026-08-01 03:02:07` | `cowrie.session.params` |
| `2026-08-01 03:02:07` | `cowrie.command.input` |
| `2026-08-01 03:02:07` | `cowrie.log.closed` |
| `2026-08-01 03:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ccdd8e0be6f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:02 |
| **Last Seen** | 2026-08-01 03:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:02:08` | `cowrie.session.connect` |
| `2026-08-01 03:02:09` | `cowrie.client.version` |
| `2026-08-01 03:02:09` | `cowrie.client.kex` |
| `2026-08-01 03:02:11` | `cowrie.login.success` |
| `2026-08-01 03:02:13` | `cowrie.session.params` |
| `2026-08-01 03:02:13` | `cowrie.command.input` |
| `2026-08-01 03:02:14` | `cowrie.log.closed` |
| `2026-08-01 03:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46218b980c47

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:02 |
| **Last Seen** | 2026-08-01 03:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:02:13` | `cowrie.session.connect` |
| `2026-08-01 03:02:14` | `cowrie.client.version` |
| `2026-08-01 03:02:14` | `cowrie.client.kex` |
| `2026-08-01 03:02:18` | `cowrie.login.success` |
| `2026-08-01 03:02:22` | `cowrie.session.params` |
| `2026-08-01 03:02:22` | `cowrie.command.input` |
| `2026-08-01 03:02:23` | `cowrie.log.closed` |
| `2026-08-01 03:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54d55cbcd084

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:02 |
| **Last Seen** | 2026-08-01 03:02 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:02:19` | `cowrie.session.connect` |
| `2026-08-01 03:02:20` | `cowrie.client.version` |
| `2026-08-01 03:02:20` | `cowrie.client.kex` |
| `2026-08-01 03:02:25` | `cowrie.login.success` |
| `2026-08-01 03:02:29` | `cowrie.session.params` |
| `2026-08-01 03:02:29` | `cowrie.command.input` |
| `2026-08-01 03:02:31` | `cowrie.log.closed` |
| `2026-08-01 03:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40877f57e808

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:02 |
| **Last Seen** | 2026-08-01 03:02 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:02:25` | `cowrie.session.connect` |
| `2026-08-01 03:02:26` | `cowrie.client.version` |
| `2026-08-01 03:02:26` | `cowrie.client.kex` |
| `2026-08-01 03:02:33` | `cowrie.login.success` |
| `2026-08-01 03:02:37` | `cowrie.session.params` |
| `2026-08-01 03:02:37` | `cowrie.command.input` |
| `2026-08-01 03:02:39` | `cowrie.log.closed` |
| `2026-08-01 03:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-024d2624cc1b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:02 |
| **Last Seen** | 2026-08-01 03:02 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:02:31` | `cowrie.session.connect` |
| `2026-08-01 03:02:33` | `cowrie.client.version` |
| `2026-08-01 03:02:33` | `cowrie.client.kex` |
| `2026-08-01 03:02:39` | `cowrie.login.success` |
| `2026-08-01 03:02:43` | `cowrie.session.params` |
| `2026-08-01 03:02:43` | `cowrie.command.input` |
| `2026-08-01 03:02:45` | `cowrie.log.closed` |
| `2026-08-01 03:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d317d81a16f9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:02 |
| **Last Seen** | 2026-08-01 03:02 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:02:38` | `cowrie.session.connect` |
| `2026-08-01 03:02:39` | `cowrie.client.version` |
| `2026-08-01 03:02:39` | `cowrie.client.kex` |
| `2026-08-01 03:02:46` | `cowrie.login.success` |
| `2026-08-01 03:02:49` | `cowrie.session.params` |
| `2026-08-01 03:02:49` | `cowrie.command.input` |
| `2026-08-01 03:02:51` | `cowrie.log.closed` |
| `2026-08-01 03:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7bea0d47819

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:02 |
| **Last Seen** | 2026-08-01 03:02 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:02:43` | `cowrie.session.connect` |
| `2026-08-01 03:02:45` | `cowrie.client.version` |
| `2026-08-01 03:02:45` | `cowrie.client.kex` |
| `2026-08-01 03:02:51` | `cowrie.login.success` |
| `2026-08-01 03:02:56` | `cowrie.session.params` |
| `2026-08-01 03:02:56` | `cowrie.command.input` |
| `2026-08-01 03:02:57` | `cowrie.log.closed` |
| `2026-08-01 03:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-625bedc624bd

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-01 03:02 |
| **Last Seen** | 2026-08-01 03:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:02:44` | `cowrie.session.connect` |
| `2026-08-01 03:02:44` | `cowrie.client.version` |
| `2026-08-01 03:02:44` | `cowrie.client.kex` |
| `2026-08-01 03:02:45` | `cowrie.login.success` |
| `2026-08-01 03:02:45` | `cowrie.direct-tcpip.request` |
| `2026-08-01 03:02:45` | `cowrie.direct-tcpip.data` |
| `2026-08-01 03:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b3957096d4c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:02 |
| **Last Seen** | 2026-08-01 03:03 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:02:50` | `cowrie.session.connect` |
| `2026-08-01 03:02:51` | `cowrie.client.version` |
| `2026-08-01 03:02:51` | `cowrie.client.kex` |
| `2026-08-01 03:02:58` | `cowrie.login.success` |
| `2026-08-01 03:03:03` | `cowrie.session.params` |
| `2026-08-01 03:03:03` | `cowrie.command.input` |
| `2026-08-01 03:03:04` | `cowrie.log.closed` |
| `2026-08-01 03:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17eb66204b7d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:02 |
| **Last Seen** | 2026-08-01 03:03 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:02:57` | `cowrie.session.connect` |
| `2026-08-01 03:02:58` | `cowrie.client.version` |
| `2026-08-01 03:02:58` | `cowrie.client.kex` |
| `2026-08-01 03:03:05` | `cowrie.login.success` |
| `2026-08-01 03:03:11` | `cowrie.session.params` |
| `2026-08-01 03:03:11` | `cowrie.command.input` |
| `2026-08-01 03:03:13` | `cowrie.log.closed` |
| `2026-08-01 03:03:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9ef8b9661da

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:03 |
| **Last Seen** | 2026-08-01 03:03 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:03:03` | `cowrie.session.connect` |
| `2026-08-01 03:03:04` | `cowrie.client.version` |
| `2026-08-01 03:03:04` | `cowrie.client.kex` |
| `2026-08-01 03:03:13` | `cowrie.login.success` |
| `2026-08-01 03:03:17` | `cowrie.session.params` |
| `2026-08-01 03:03:17` | `cowrie.command.input` |
| `2026-08-01 03:03:20` | `cowrie.log.closed` |
| `2026-08-01 03:03:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8ca84859584

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:03 |
| **Last Seen** | 2026-08-01 03:03 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:03:07` | `cowrie.session.connect` |
| `2026-08-01 03:03:11` | `cowrie.client.version` |
| `2026-08-01 03:03:11` | `cowrie.client.kex` |
| `2026-08-01 03:03:20` | `cowrie.login.success` |
| `2026-08-01 03:03:24` | `cowrie.session.params` |
| `2026-08-01 03:03:24` | `cowrie.command.input` |
| `2026-08-01 03:03:25` | `cowrie.log.closed` |
| `2026-08-01 03:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ae3f60dc2b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:03 |
| **Last Seen** | 2026-08-01 03:03 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:03:16` | `cowrie.session.connect` |
| `2026-08-01 03:03:17` | `cowrie.client.version` |
| `2026-08-01 03:03:17` | `cowrie.client.kex` |
| `2026-08-01 03:03:25` | `cowrie.login.success` |
| `2026-08-01 03:03:27` | `cowrie.session.params` |
| `2026-08-01 03:03:27` | `cowrie.command.input` |
| `2026-08-01 03:03:27` | `cowrie.log.closed` |
| `2026-08-01 03:03:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ba528b2a34f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:03 |
| **Last Seen** | 2026-08-01 03:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:03:24` | `cowrie.session.connect` |
| `2026-08-01 03:03:25` | `cowrie.client.version` |
| `2026-08-01 03:03:25` | `cowrie.client.kex` |
| `2026-08-01 03:03:28` | `cowrie.login.success` |
| `2026-08-01 03:03:29` | `cowrie.session.params` |
| `2026-08-01 03:03:29` | `cowrie.command.input` |
| `2026-08-01 03:03:30` | `cowrie.log.closed` |
| `2026-08-01 03:03:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e8d7e73bdda

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:03 |
| **Last Seen** | 2026-08-01 03:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:03:32` | `cowrie.session.connect` |
| `2026-08-01 03:03:32` | `cowrie.client.version` |
| `2026-08-01 03:03:32` | `cowrie.client.kex` |
| `2026-08-01 03:03:34` | `cowrie.login.success` |
| `2026-08-01 03:03:35` | `cowrie.session.params` |
| `2026-08-01 03:03:35` | `cowrie.command.input` |
| `2026-08-01 03:03:35` | `cowrie.log.closed` |
| `2026-08-01 03:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b89d12fcfac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:03 |
| **Last Seen** | 2026-08-01 03:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:03:39` | `cowrie.session.connect` |
| `2026-08-01 03:03:39` | `cowrie.client.version` |
| `2026-08-01 03:03:39` | `cowrie.client.kex` |
| `2026-08-01 03:03:41` | `cowrie.login.success` |
| `2026-08-01 03:03:43` | `cowrie.session.params` |
| `2026-08-01 03:03:43` | `cowrie.command.input` |
| `2026-08-01 03:03:43` | `cowrie.log.closed` |
| `2026-08-01 03:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecd279bc6663

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:03 |
| **Last Seen** | 2026-08-01 03:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:03:44` | `cowrie.session.connect` |
| `2026-08-01 03:03:45` | `cowrie.client.version` |
| `2026-08-01 03:03:45` | `cowrie.client.kex` |
| `2026-08-01 03:03:48` | `cowrie.login.success` |
| `2026-08-01 03:03:50` | `cowrie.session.params` |
| `2026-08-01 03:03:50` | `cowrie.command.input` |
| `2026-08-01 03:03:51` | `cowrie.log.closed` |
| `2026-08-01 03:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-494d94297240

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:03 |
| **Last Seen** | 2026-08-01 03:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:03:52` | `cowrie.session.connect` |
| `2026-08-01 03:03:53` | `cowrie.client.version` |
| `2026-08-01 03:03:53` | `cowrie.client.kex` |
| `2026-08-01 03:03:55` | `cowrie.login.success` |
| `2026-08-01 03:03:56` | `cowrie.session.params` |
| `2026-08-01 03:03:56` | `cowrie.command.input` |
| `2026-08-01 03:03:56` | `cowrie.log.closed` |
| `2026-08-01 03:03:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f63788cf1b2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:03 |
| **Last Seen** | 2026-08-01 03:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:03:58` | `cowrie.session.connect` |
| `2026-08-01 03:03:59` | `cowrie.client.version` |
| `2026-08-01 03:03:59` | `cowrie.client.kex` |
| `2026-08-01 03:04:01` | `cowrie.login.success` |
| `2026-08-01 03:04:03` | `cowrie.session.params` |
| `2026-08-01 03:04:03` | `cowrie.command.input` |
| `2026-08-01 03:04:03` | `cowrie.log.closed` |
| `2026-08-01 03:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2272f31b8de6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:04 |
| **Last Seen** | 2026-08-01 03:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:04:04` | `cowrie.session.connect` |
| `2026-08-01 03:04:05` | `cowrie.client.version` |
| `2026-08-01 03:04:05` | `cowrie.client.kex` |
| `2026-08-01 03:04:08` | `cowrie.login.success` |
| `2026-08-01 03:04:10` | `cowrie.session.params` |
| `2026-08-01 03:04:10` | `cowrie.command.input` |
| `2026-08-01 03:04:10` | `cowrie.log.closed` |
| `2026-08-01 03:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afc00bc014ea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:04 |
| **Last Seen** | 2026-08-01 03:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:04:11` | `cowrie.session.connect` |
| `2026-08-01 03:04:12` | `cowrie.client.version` |
| `2026-08-01 03:04:12` | `cowrie.client.kex` |
| `2026-08-01 03:04:15` | `cowrie.login.success` |
| `2026-08-01 03:04:17` | `cowrie.session.params` |
| `2026-08-01 03:04:17` | `cowrie.command.input` |
| `2026-08-01 03:04:18` | `cowrie.log.closed` |
| `2026-08-01 03:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b66244bfb1c6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:04 |
| **Last Seen** | 2026-08-01 03:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:04:17` | `cowrie.session.connect` |
| `2026-08-01 03:04:18` | `cowrie.client.version` |
| `2026-08-01 03:04:18` | `cowrie.client.kex` |
| `2026-08-01 03:04:21` | `cowrie.login.success` |
| `2026-08-01 03:04:23` | `cowrie.session.params` |
| `2026-08-01 03:04:23` | `cowrie.command.input` |
| `2026-08-01 03:04:23` | `cowrie.log.closed` |
| `2026-08-01 03:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd61ea8f2dc3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:04 |
| **Last Seen** | 2026-08-01 03:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:04:23` | `cowrie.session.connect` |
| `2026-08-01 03:04:23` | `cowrie.client.version` |
| `2026-08-01 03:04:23` | `cowrie.client.kex` |
| `2026-08-01 03:04:28` | `cowrie.login.success` |
| `2026-08-01 03:04:30` | `cowrie.session.params` |
| `2026-08-01 03:04:30` | `cowrie.command.input` |
| `2026-08-01 03:04:30` | `cowrie.log.closed` |
| `2026-08-01 03:04:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d74ed0790b7d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:04 |
| **Last Seen** | 2026-08-01 03:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:04:30` | `cowrie.session.connect` |
| `2026-08-01 03:04:30` | `cowrie.client.version` |
| `2026-08-01 03:04:30` | `cowrie.client.kex` |
| `2026-08-01 03:04:33` | `cowrie.login.success` |
| `2026-08-01 03:04:35` | `cowrie.session.params` |
| `2026-08-01 03:04:35` | `cowrie.command.input` |
| `2026-08-01 03:04:36` | `cowrie.log.closed` |
| `2026-08-01 03:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0df1e472b08b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:04 |
| **Last Seen** | 2026-08-01 03:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:04:36` | `cowrie.session.connect` |
| `2026-08-01 03:04:36` | `cowrie.client.version` |
| `2026-08-01 03:04:36` | `cowrie.client.kex` |
| `2026-08-01 03:04:41` | `cowrie.login.success` |
| `2026-08-01 03:04:44` | `cowrie.session.params` |
| `2026-08-01 03:04:44` | `cowrie.command.input` |
| `2026-08-01 03:04:45` | `cowrie.log.closed` |
| `2026-08-01 03:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96a1373de41d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:04 |
| **Last Seen** | 2026-08-01 03:04 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:04:41` | `cowrie.session.connect` |
| `2026-08-01 03:04:42` | `cowrie.client.version` |
| `2026-08-01 03:04:42` | `cowrie.client.kex` |
| `2026-08-01 03:04:48` | `cowrie.login.success` |
| `2026-08-01 03:04:52` | `cowrie.session.params` |
| `2026-08-01 03:04:52` | `cowrie.command.input` |
| `2026-08-01 03:04:54` | `cowrie.log.closed` |
| `2026-08-01 03:04:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7523f464c5cb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:04 |
| **Last Seen** | 2026-08-01 03:05 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:04:46` | `cowrie.session.connect` |
| `2026-08-01 03:04:48` | `cowrie.client.version` |
| `2026-08-01 03:04:48` | `cowrie.client.kex` |
| `2026-08-01 03:04:56` | `cowrie.login.success` |
| `2026-08-01 03:05:00` | `cowrie.session.params` |
| `2026-08-01 03:05:00` | `cowrie.command.input` |
| `2026-08-01 03:05:02` | `cowrie.log.closed` |
| `2026-08-01 03:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b574c3df253

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:04 |
| **Last Seen** | 2026-08-01 03:05 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:04:52` | `cowrie.session.connect` |
| `2026-08-01 03:04:53` | `cowrie.client.version` |
| `2026-08-01 03:04:54` | `cowrie.client.kex` |
| `2026-08-01 03:05:01` | `cowrie.login.success` |
| `2026-08-01 03:05:06` | `cowrie.session.params` |
| `2026-08-01 03:05:06` | `cowrie.command.input` |
| `2026-08-01 03:05:07` | `cowrie.log.closed` |
| `2026-08-01 03:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99f438c97ca0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:04 |
| **Last Seen** | 2026-08-01 03:05 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:04:58` | `cowrie.session.connect` |
| `2026-08-01 03:05:00` | `cowrie.client.version` |
| `2026-08-01 03:05:00` | `cowrie.client.kex` |
| `2026-08-01 03:05:07` | `cowrie.login.success` |
| `2026-08-01 03:05:11` | `cowrie.session.params` |
| `2026-08-01 03:05:11` | `cowrie.command.input` |
| `2026-08-01 03:05:13` | `cowrie.log.closed` |
| `2026-08-01 03:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a410439ce96a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:05 |
| **Last Seen** | 2026-08-01 03:05 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:05:06` | `cowrie.session.connect` |
| `2026-08-01 03:05:06` | `cowrie.client.version` |
| `2026-08-01 03:05:06` | `cowrie.client.kex` |
| `2026-08-01 03:05:13` | `cowrie.login.success` |
| `2026-08-01 03:05:16` | `cowrie.session.params` |
| `2026-08-01 03:05:16` | `cowrie.command.input` |
| `2026-08-01 03:05:17` | `cowrie.log.closed` |
| `2026-08-01 03:05:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-728a4cee624b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:05 |
| **Last Seen** | 2026-08-01 03:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:05:12` | `cowrie.session.connect` |
| `2026-08-01 03:05:13` | `cowrie.client.version` |
| `2026-08-01 03:05:13` | `cowrie.client.kex` |
| `2026-08-01 03:05:18` | `cowrie.login.success` |
| `2026-08-01 03:05:20` | `cowrie.session.params` |
| `2026-08-01 03:05:20` | `cowrie.command.input` |
| `2026-08-01 03:05:21` | `cowrie.log.closed` |
| `2026-08-01 03:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-894ccbe83b8f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:05 |
| **Last Seen** | 2026-08-01 03:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:05:19` | `cowrie.session.connect` |
| `2026-08-01 03:05:20` | `cowrie.client.version` |
| `2026-08-01 03:05:20` | `cowrie.client.kex` |
| `2026-08-01 03:05:24` | `cowrie.login.success` |
| `2026-08-01 03:05:27` | `cowrie.session.params` |
| `2026-08-01 03:05:27` | `cowrie.command.input` |
| `2026-08-01 03:05:28` | `cowrie.log.closed` |
| `2026-08-01 03:05:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7c5b6bf4adc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:05 |
| **Last Seen** | 2026-08-01 03:05 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:05:24` | `cowrie.session.connect` |
| `2026-08-01 03:05:26` | `cowrie.client.version` |
| `2026-08-01 03:05:26` | `cowrie.client.kex` |
| `2026-08-01 03:05:30` | `cowrie.login.success` |
| `2026-08-01 03:05:33` | `cowrie.session.params` |
| `2026-08-01 03:05:33` | `cowrie.command.input` |
| `2026-08-01 03:05:34` | `cowrie.log.closed` |
| `2026-08-01 03:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1b87eb8e531

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:05 |
| **Last Seen** | 2026-08-01 03:05 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:05:31` | `cowrie.session.connect` |
| `2026-08-01 03:05:33` | `cowrie.client.version` |
| `2026-08-01 03:05:33` | `cowrie.client.kex` |
| `2026-08-01 03:05:38` | `cowrie.login.success` |
| `2026-08-01 03:05:41` | `cowrie.session.params` |
| `2026-08-01 03:05:41` | `cowrie.command.input` |
| `2026-08-01 03:05:42` | `cowrie.log.closed` |
| `2026-08-01 03:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b950fd1a8bf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:05 |
| **Last Seen** | 2026-08-01 03:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:05:37` | `cowrie.session.connect` |
| `2026-08-01 03:05:38` | `cowrie.client.version` |
| `2026-08-01 03:05:38` | `cowrie.client.kex` |
| `2026-08-01 03:05:43` | `cowrie.login.success` |
| `2026-08-01 03:05:44` | `cowrie.session.params` |
| `2026-08-01 03:05:44` | `cowrie.command.input` |
| `2026-08-01 03:05:46` | `cowrie.log.closed` |
| `2026-08-01 03:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a71be7d5d369

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:05 |
| **Last Seen** | 2026-08-01 03:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:05:44` | `cowrie.session.connect` |
| `2026-08-01 03:05:46` | `cowrie.client.version` |
| `2026-08-01 03:05:46` | `cowrie.client.kex` |
| `2026-08-01 03:05:49` | `cowrie.login.success` |
| `2026-08-01 03:05:52` | `cowrie.session.params` |
| `2026-08-01 03:05:52` | `cowrie.command.input` |
| `2026-08-01 03:05:52` | `cowrie.log.closed` |
| `2026-08-01 03:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a2a96278bfb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:05 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:05:52` | `cowrie.session.connect` |
| `2026-08-01 03:05:52` | `cowrie.client.version` |
| `2026-08-01 03:05:52` | `cowrie.client.kex` |
| `2026-08-01 03:05:56` | `cowrie.login.success` |
| `2026-08-01 03:05:59` | `cowrie.session.params` |
| `2026-08-01 03:05:59` | `cowrie.command.input` |
| `2026-08-01 03:06:00` | `cowrie.log.closed` |
| `2026-08-01 03:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d08bec12051

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:05 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:05:57` | `cowrie.session.connect` |
| `2026-08-01 03:05:58` | `cowrie.client.version` |
| `2026-08-01 03:05:58` | `cowrie.client.kex` |
| `2026-08-01 03:06:02` | `cowrie.login.success` |
| `2026-08-01 03:06:05` | `cowrie.session.params` |
| `2026-08-01 03:06:05` | `cowrie.command.input` |
| `2026-08-01 03:06:06` | `cowrie.log.closed` |
| `2026-08-01 03:06:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f90dfca08e1b

| Field | Detail |
|---|---|
| **Source IP** | `35.187.231[.]181` |
| **First Seen** | 2026-08-01 03:05 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:05:59` | `cowrie.session.connect` |
| `2026-08-01 03:05:59` | `cowrie.client.version` |
| `2026-08-01 03:05:59` | `cowrie.client.kex` |
| `2026-08-01 03:06:00` | `cowrie.login.success` |
| `2026-08-01 03:06:01` | `cowrie.session.params` |
| `2026-08-01 03:06:01` | `cowrie.command.input` |
| `2026-08-01 03:06:01` | `cowrie.log.closed` |
| `2026-08-01 03:06:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.231[.]181` to AbuseIPDB if not already reported
- [ ] Block `35.187.231[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73b6ef717c30

| Field | Detail |
|---|---|
| **Source IP** | `35.187.231[.]181` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:01` | `cowrie.session.connect` |
| `2026-08-01 03:06:01` | `cowrie.client.version` |
| `2026-08-01 03:06:01` | `cowrie.client.kex` |
| `2026-08-01 03:06:02` | `cowrie.login.success` |
| `2026-08-01 03:06:04` | `cowrie.session.params` |
| `2026-08-01 03:06:04` | `cowrie.command.input` |
| `2026-08-01 03:06:04` | `cowrie.log.closed` |
| `2026-08-01 03:06:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.231[.]181` to AbuseIPDB if not already reported
- [ ] Block `35.187.231[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f55a571bcd71

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:04` | `cowrie.session.connect` |
| `2026-08-01 03:06:04` | `cowrie.client.version` |
| `2026-08-01 03:06:04` | `cowrie.client.kex` |
| `2026-08-01 03:06:09` | `cowrie.login.success` |
| `2026-08-01 03:06:12` | `cowrie.session.params` |
| `2026-08-01 03:06:12` | `cowrie.command.input` |
| `2026-08-01 03:06:14` | `cowrie.log.closed` |
| `2026-08-01 03:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5af28f1e445f

| Field | Detail |
|---|---|
| **Source IP** | `35.187.231[.]181` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:04` | `cowrie.session.connect` |
| `2026-08-01 03:06:04` | `cowrie.client.version` |
| `2026-08-01 03:06:04` | `cowrie.client.kex` |
| `2026-08-01 03:06:06` | `cowrie.login.success` |
| `2026-08-01 03:06:07` | `cowrie.session.params` |
| `2026-08-01 03:06:07` | `cowrie.command.input` |
| `2026-08-01 03:06:07` | `cowrie.log.closed` |
| `2026-08-01 03:06:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.231[.]181` to AbuseIPDB if not already reported
- [ ] Block `35.187.231[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa412398ed52

| Field | Detail |
|---|---|
| **Source IP** | `35.187.231[.]181` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:08` | `cowrie.session.connect` |
| `2026-08-01 03:06:08` | `cowrie.client.version` |
| `2026-08-01 03:06:08` | `cowrie.client.kex` |
| `2026-08-01 03:06:09` | `cowrie.login.success` |
| `2026-08-01 03:06:10` | `cowrie.session.params` |
| `2026-08-01 03:06:10` | `cowrie.command.input` |
| `2026-08-01 03:06:10` | `cowrie.log.closed` |
| `2026-08-01 03:06:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.231[.]181` to AbuseIPDB if not already reported
- [ ] Block `35.187.231[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-909fbcae5341

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:09` | `cowrie.session.connect` |
| `2026-08-01 03:06:10` | `cowrie.client.version` |
| `2026-08-01 03:06:10` | `cowrie.client.kex` |
| `2026-08-01 03:06:17` | `cowrie.login.success` |
| `2026-08-01 03:06:21` | `cowrie.session.params` |
| `2026-08-01 03:06:21` | `cowrie.command.input` |
| `2026-08-01 03:06:23` | `cowrie.log.closed` |
| `2026-08-01 03:06:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-986349a09782

| Field | Detail |
|---|---|
| **Source IP** | `35.187.231[.]181` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:11` | `cowrie.session.connect` |
| `2026-08-01 03:06:11` | `cowrie.client.version` |
| `2026-08-01 03:06:11` | `cowrie.client.kex` |
| `2026-08-01 03:06:12` | `cowrie.login.success` |
| `2026-08-01 03:06:14` | `cowrie.session.params` |
| `2026-08-01 03:06:14` | `cowrie.command.input` |
| `2026-08-01 03:06:14` | `cowrie.log.closed` |
| `2026-08-01 03:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.231[.]181` to AbuseIPDB if not already reported
- [ ] Block `35.187.231[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b38a25970cb0

| Field | Detail |
|---|---|
| **Source IP** | `35.187.231[.]181` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:14` | `cowrie.session.connect` |
| `2026-08-01 03:06:14` | `cowrie.client.version` |
| `2026-08-01 03:06:14` | `cowrie.client.kex` |
| `2026-08-01 03:06:15` | `cowrie.login.success` |
| `2026-08-01 03:06:17` | `cowrie.session.params` |
| `2026-08-01 03:06:17` | `cowrie.command.input` |
| `2026-08-01 03:06:17` | `cowrie.log.closed` |
| `2026-08-01 03:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.231[.]181` to AbuseIPDB if not already reported
- [ ] Block `35.187.231[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29edc1e40ac5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:15` | `cowrie.session.connect` |
| `2026-08-01 03:06:16` | `cowrie.client.version` |
| `2026-08-01 03:06:16` | `cowrie.client.kex` |
| `2026-08-01 03:06:23` | `cowrie.login.success` |
| `2026-08-01 03:06:28` | `cowrie.session.params` |
| `2026-08-01 03:06:28` | `cowrie.command.input` |
| `2026-08-01 03:06:30` | `cowrie.log.closed` |
| `2026-08-01 03:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbd7459775c8

| Field | Detail |
|---|---|
| **Source IP** | `35.187.231[.]181` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:17` | `cowrie.session.connect` |
| `2026-08-01 03:06:17` | `cowrie.client.version` |
| `2026-08-01 03:06:17` | `cowrie.client.kex` |
| `2026-08-01 03:06:18` | `cowrie.login.success` |
| `2026-08-01 03:06:19` | `cowrie.session.params` |
| `2026-08-01 03:06:19` | `cowrie.command.input` |
| `2026-08-01 03:06:20` | `cowrie.log.closed` |
| `2026-08-01 03:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.231[.]181` to AbuseIPDB if not already reported
- [ ] Block `35.187.231[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cc07babe2f2

| Field | Detail |
|---|---|
| **Source IP** | `111.70.14[.]135` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:17` | `cowrie.session.connect` |
| `2026-08-01 03:06:18` | `cowrie.client.version` |
| `2026-08-01 03:06:18` | `cowrie.client.kex` |
| `2026-08-01 03:06:20` | `cowrie.login.success` |
| `2026-08-01 03:06:21` | `cowrie.direct-tcpip.request` |
| `2026-08-01 03:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.14[.]135` to AbuseIPDB if not already reported
- [ ] Block `111.70.14[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-230e779dbc72

| Field | Detail |
|---|---|
| **Source IP** | `35.187.231[.]181` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:20` | `cowrie.session.connect` |
| `2026-08-01 03:06:20` | `cowrie.client.version` |
| `2026-08-01 03:06:20` | `cowrie.client.kex` |
| `2026-08-01 03:06:22` | `cowrie.login.success` |
| `2026-08-01 03:06:23` | `cowrie.session.params` |
| `2026-08-01 03:06:23` | `cowrie.command.input` |
| `2026-08-01 03:06:23` | `cowrie.log.closed` |
| `2026-08-01 03:06:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.231[.]181` to AbuseIPDB if not already reported
- [ ] Block `35.187.231[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce421797a3b2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:21` | `cowrie.session.connect` |
| `2026-08-01 03:06:22` | `cowrie.client.version` |
| `2026-08-01 03:06:22` | `cowrie.client.kex` |
| `2026-08-01 03:06:30` | `cowrie.login.success` |
| `2026-08-01 03:06:35` | `cowrie.session.params` |
| `2026-08-01 03:06:35` | `cowrie.command.input` |
| `2026-08-01 03:06:37` | `cowrie.log.closed` |
| `2026-08-01 03:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f41a890eea6e

| Field | Detail |
|---|---|
| **Source IP** | `35.187.231[.]181` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:24` | `cowrie.session.connect` |
| `2026-08-01 03:06:24` | `cowrie.client.version` |
| `2026-08-01 03:06:24` | `cowrie.client.kex` |
| `2026-08-01 03:06:25` | `cowrie.login.success` |
| `2026-08-01 03:06:26` | `cowrie.session.params` |
| `2026-08-01 03:06:26` | `cowrie.command.input` |
| `2026-08-01 03:06:26` | `cowrie.log.closed` |
| `2026-08-01 03:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.231[.]181` to AbuseIPDB if not already reported
- [ ] Block `35.187.231[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87dfa790764e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:27` | `cowrie.session.connect` |
| `2026-08-01 03:06:28` | `cowrie.client.version` |
| `2026-08-01 03:06:28` | `cowrie.client.kex` |
| `2026-08-01 03:06:37` | `cowrie.login.success` |
| `2026-08-01 03:06:42` | `cowrie.session.params` |
| `2026-08-01 03:06:42` | `cowrie.command.input` |
| `2026-08-01 03:06:45` | `cowrie.log.closed` |
| `2026-08-01 03:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93a512680ed3

| Field | Detail |
|---|---|
| **Source IP** | `35.187.231[.]181` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:27` | `cowrie.session.connect` |
| `2026-08-01 03:06:27` | `cowrie.client.version` |
| `2026-08-01 03:06:27` | `cowrie.client.kex` |
| `2026-08-01 03:06:29` | `cowrie.login.success` |
| `2026-08-01 03:06:30` | `cowrie.session.params` |
| `2026-08-01 03:06:30` | `cowrie.command.input` |
| `2026-08-01 03:06:30` | `cowrie.log.closed` |
| `2026-08-01 03:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.231[.]181` to AbuseIPDB if not already reported
- [ ] Block `35.187.231[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a11b3a215e9f

| Field | Detail |
|---|---|
| **Source IP** | `35.187.231[.]181` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:30` | `cowrie.session.connect` |
| `2026-08-01 03:06:30` | `cowrie.client.version` |
| `2026-08-01 03:06:30` | `cowrie.client.kex` |
| `2026-08-01 03:06:31` | `cowrie.login.success` |
| `2026-08-01 03:06:32` | `cowrie.session.params` |
| `2026-08-01 03:06:32` | `cowrie.command.input` |
| `2026-08-01 03:06:33` | `cowrie.log.closed` |
| `2026-08-01 03:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.231[.]181` to AbuseIPDB if not already reported
- [ ] Block `35.187.231[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95f7c7421071

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:32` | `cowrie.session.connect` |
| `2026-08-01 03:06:35` | `cowrie.client.version` |
| `2026-08-01 03:06:35` | `cowrie.client.kex` |
| `2026-08-01 03:06:45` | `cowrie.login.success` |
| `2026-08-01 03:06:49` | `cowrie.session.params` |
| `2026-08-01 03:06:49` | `cowrie.command.input` |
| `2026-08-01 03:06:52` | `cowrie.log.closed` |
| `2026-08-01 03:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30109246b8b1

| Field | Detail |
|---|---|
| **Source IP** | `35.187.231[.]181` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:33` | `cowrie.session.connect` |
| `2026-08-01 03:06:33` | `cowrie.client.version` |
| `2026-08-01 03:06:33` | `cowrie.client.kex` |
| `2026-08-01 03:06:35` | `cowrie.login.success` |
| `2026-08-01 03:06:36` | `cowrie.session.params` |
| `2026-08-01 03:06:36` | `cowrie.command.input` |
| `2026-08-01 03:06:36` | `cowrie.log.closed` |
| `2026-08-01 03:06:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.231[.]181` to AbuseIPDB if not already reported
- [ ] Block `35.187.231[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e34013a4194c

| Field | Detail |
|---|---|
| **Source IP** | `35.187.231[.]181` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:36` | `cowrie.session.connect` |
| `2026-08-01 03:06:36` | `cowrie.client.version` |
| `2026-08-01 03:06:37` | `cowrie.client.kex` |
| `2026-08-01 03:06:38` | `cowrie.login.success` |
| `2026-08-01 03:06:39` | `cowrie.session.params` |
| `2026-08-01 03:06:39` | `cowrie.command.input` |
| `2026-08-01 03:06:39` | `cowrie.log.closed` |
| `2026-08-01 03:06:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.231[.]181` to AbuseIPDB if not already reported
- [ ] Block `35.187.231[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1a7dd118075

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:38` | `cowrie.session.connect` |
| `2026-08-01 03:06:41` | `cowrie.client.version` |
| `2026-08-01 03:06:41` | `cowrie.client.kex` |
| `2026-08-01 03:06:49` | `cowrie.login.success` |
| `2026-08-01 03:06:54` | `cowrie.session.params` |
| `2026-08-01 03:06:54` | `cowrie.command.input` |
| `2026-08-01 03:06:56` | `cowrie.log.closed` |
| `2026-08-01 03:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1412d8a544e5

| Field | Detail |
|---|---|
| **Source IP** | `35.187.231[.]181` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:39` | `cowrie.session.connect` |
| `2026-08-01 03:06:39` | `cowrie.client.version` |
| `2026-08-01 03:06:40` | `cowrie.client.kex` |
| `2026-08-01 03:06:41` | `cowrie.login.success` |
| `2026-08-01 03:06:42` | `cowrie.session.params` |
| `2026-08-01 03:06:42` | `cowrie.command.input` |
| `2026-08-01 03:06:42` | `cowrie.log.closed` |
| `2026-08-01 03:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.231[.]181` to AbuseIPDB if not already reported
- [ ] Block `35.187.231[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0242995069c

| Field | Detail |
|---|---|
| **Source IP** | `35.187.231[.]181` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:42` | `cowrie.session.connect` |
| `2026-08-01 03:06:42` | `cowrie.client.version` |
| `2026-08-01 03:06:43` | `cowrie.client.kex` |
| `2026-08-01 03:06:43` | `cowrie.login.success` |
| `2026-08-01 03:06:45` | `cowrie.session.params` |
| `2026-08-01 03:06:45` | `cowrie.command.input` |
| `2026-08-01 03:06:45` | `cowrie.log.closed` |
| `2026-08-01 03:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.231[.]181` to AbuseIPDB if not already reported
- [ ] Block `35.187.231[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ac0d7a341d7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:07 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:45` | `cowrie.session.connect` |
| `2026-08-01 03:06:47` | `cowrie.client.version` |
| `2026-08-01 03:06:47` | `cowrie.client.kex` |
| `2026-08-01 03:06:56` | `cowrie.login.success` |
| `2026-08-01 03:06:59` | `cowrie.session.params` |
| `2026-08-01 03:06:59` | `cowrie.command.input` |
| `2026-08-01 03:07:00` | `cowrie.log.closed` |
| `2026-08-01 03:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f6dad57ad8a

| Field | Detail |
|---|---|
| **Source IP** | `35.187.231[.]181` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:45` | `cowrie.session.connect` |
| `2026-08-01 03:06:45` | `cowrie.client.version` |
| `2026-08-01 03:06:45` | `cowrie.client.kex` |
| `2026-08-01 03:06:46` | `cowrie.login.success` |
| `2026-08-01 03:06:47` | `cowrie.session.params` |
| `2026-08-01 03:06:47` | `cowrie.command.input` |
| `2026-08-01 03:06:48` | `cowrie.log.closed` |
| `2026-08-01 03:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.231[.]181` to AbuseIPDB if not already reported
- [ ] Block `35.187.231[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-143107064548

| Field | Detail |
|---|---|
| **Source IP** | `35.187.231[.]181` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:51` | `cowrie.session.connect` |
| `2026-08-01 03:06:51` | `cowrie.client.version` |
| `2026-08-01 03:06:52` | `cowrie.client.kex` |
| `2026-08-01 03:06:53` | `cowrie.login.success` |
| `2026-08-01 03:06:54` | `cowrie.session.params` |
| `2026-08-01 03:06:54` | `cowrie.command.input` |
| `2026-08-01 03:06:54` | `cowrie.log.closed` |
| `2026-08-01 03:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.231[.]181` to AbuseIPDB if not already reported
- [ ] Block `35.187.231[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6356993dd043

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:07 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:52` | `cowrie.session.connect` |
| `2026-08-01 03:06:54` | `cowrie.client.version` |
| `2026-08-01 03:06:54` | `cowrie.client.kex` |
| `2026-08-01 03:07:00` | `cowrie.login.success` |
| `2026-08-01 03:07:02` | `cowrie.session.params` |
| `2026-08-01 03:07:02` | `cowrie.command.input` |
| `2026-08-01 03:07:04` | `cowrie.log.closed` |
| `2026-08-01 03:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6054d30ab79f

| Field | Detail |
|---|---|
| **Source IP** | `35.187.231[.]181` |
| **First Seen** | 2026-08-01 03:06 |
| **Last Seen** | 2026-08-01 03:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:06:54` | `cowrie.session.connect` |
| `2026-08-01 03:06:54` | `cowrie.client.version` |
| `2026-08-01 03:06:55` | `cowrie.client.kex` |
| `2026-08-01 03:06:55` | `cowrie.login.success` |
| `2026-08-01 03:06:57` | `cowrie.session.params` |
| `2026-08-01 03:06:57` | `cowrie.command.input` |
| `2026-08-01 03:06:57` | `cowrie.log.closed` |
| `2026-08-01 03:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.231[.]181` to AbuseIPDB if not already reported
- [ ] Block `35.187.231[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acde326f46e5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:07 |
| **Last Seen** | 2026-08-01 03:07 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:07:00` | `cowrie.session.connect` |
| `2026-08-01 03:07:01` | `cowrie.client.version` |
| `2026-08-01 03:07:01` | `cowrie.client.kex` |
| `2026-08-01 03:07:07` | `cowrie.login.success` |
| `2026-08-01 03:07:10` | `cowrie.session.params` |
| `2026-08-01 03:07:10` | `cowrie.command.input` |
| `2026-08-01 03:07:12` | `cowrie.log.closed` |
| `2026-08-01 03:07:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-effb3fb78e48

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:07 |
| **Last Seen** | 2026-08-01 03:07 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:07:06` | `cowrie.session.connect` |
| `2026-08-01 03:07:08` | `cowrie.client.version` |
| `2026-08-01 03:07:08` | `cowrie.client.kex` |
| `2026-08-01 03:07:14` | `cowrie.login.success` |
| `2026-08-01 03:07:17` | `cowrie.session.params` |
| `2026-08-01 03:07:17` | `cowrie.command.input` |
| `2026-08-01 03:07:19` | `cowrie.log.closed` |
| `2026-08-01 03:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fc8db57aae3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:07 |
| **Last Seen** | 2026-08-01 03:07 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:07:12` | `cowrie.session.connect` |
| `2026-08-01 03:07:14` | `cowrie.client.version` |
| `2026-08-01 03:07:14` | `cowrie.client.kex` |
| `2026-08-01 03:07:21` | `cowrie.login.success` |
| `2026-08-01 03:07:25` | `cowrie.session.params` |
| `2026-08-01 03:07:25` | `cowrie.command.input` |
| `2026-08-01 03:07:27` | `cowrie.log.closed` |
| `2026-08-01 03:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09b30750f7ce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:07 |
| **Last Seen** | 2026-08-01 03:07 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:07:18` | `cowrie.session.connect` |
| `2026-08-01 03:07:20` | `cowrie.client.version` |
| `2026-08-01 03:07:20` | `cowrie.client.kex` |
| `2026-08-01 03:07:27` | `cowrie.login.success` |
| `2026-08-01 03:07:31` | `cowrie.session.params` |
| `2026-08-01 03:07:31` | `cowrie.command.input` |
| `2026-08-01 03:07:33` | `cowrie.log.closed` |
| `2026-08-01 03:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b16d28b1c3ab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:07 |
| **Last Seen** | 2026-08-01 03:07 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:07:31` | `cowrie.session.connect` |
| `2026-08-01 03:07:33` | `cowrie.client.version` |
| `2026-08-01 03:07:33` | `cowrie.client.kex` |
| `2026-08-01 03:07:40` | `cowrie.login.success` |
| `2026-08-01 03:07:46` | `cowrie.session.params` |
| `2026-08-01 03:07:46` | `cowrie.command.input` |
| `2026-08-01 03:07:47` | `cowrie.log.closed` |
| `2026-08-01 03:07:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-745460ed6e87

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:07 |
| **Last Seen** | 2026-08-01 03:07 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:07:37` | `cowrie.session.connect` |
| `2026-08-01 03:07:39` | `cowrie.client.version` |
| `2026-08-01 03:07:39` | `cowrie.client.kex` |
| `2026-08-01 03:07:47` | `cowrie.login.success` |
| `2026-08-01 03:07:52` | `cowrie.session.params` |
| `2026-08-01 03:07:52` | `cowrie.command.input` |
| `2026-08-01 03:07:55` | `cowrie.log.closed` |
| `2026-08-01 03:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b6df7ec33b3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:07 |
| **Last Seen** | 2026-08-01 03:08 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:07:43` | `cowrie.session.connect` |
| `2026-08-01 03:07:46` | `cowrie.client.version` |
| `2026-08-01 03:07:46` | `cowrie.client.kex` |
| `2026-08-01 03:07:55` | `cowrie.login.success` |
| `2026-08-01 03:07:59` | `cowrie.session.params` |
| `2026-08-01 03:07:59` | `cowrie.command.input` |
| `2026-08-01 03:08:00` | `cowrie.log.closed` |
| `2026-08-01 03:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7d97f42d189

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:07 |
| **Last Seen** | 2026-08-01 03:08 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:07:50` | `cowrie.session.connect` |
| `2026-08-01 03:07:52` | `cowrie.client.version` |
| `2026-08-01 03:07:52` | `cowrie.client.kex` |
| `2026-08-01 03:08:00` | `cowrie.login.success` |
| `2026-08-01 03:08:04` | `cowrie.session.params` |
| `2026-08-01 03:08:04` | `cowrie.command.input` |
| `2026-08-01 03:08:05` | `cowrie.log.closed` |
| `2026-08-01 03:08:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dff94c9fa8bc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:07 |
| **Last Seen** | 2026-08-01 03:08 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:07:57` | `cowrie.session.connect` |
| `2026-08-01 03:07:59` | `cowrie.client.version` |
| `2026-08-01 03:07:59` | `cowrie.client.kex` |
| `2026-08-01 03:08:05` | `cowrie.login.success` |
| `2026-08-01 03:08:07` | `cowrie.session.params` |
| `2026-08-01 03:08:07` | `cowrie.command.input` |
| `2026-08-01 03:08:08` | `cowrie.log.closed` |
| `2026-08-01 03:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64c1f1cdabf8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:08 |
| **Last Seen** | 2026-08-01 03:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:08:06` | `cowrie.session.connect` |
| `2026-08-01 03:08:06` | `cowrie.client.version` |
| `2026-08-01 03:08:06` | `cowrie.client.kex` |
| `2026-08-01 03:08:11` | `cowrie.login.success` |
| `2026-08-01 03:08:14` | `cowrie.session.params` |
| `2026-08-01 03:08:14` | `cowrie.command.input` |
| `2026-08-01 03:08:15` | `cowrie.log.closed` |
| `2026-08-01 03:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa9505103e4a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:08 |
| **Last Seen** | 2026-08-01 03:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:08:13` | `cowrie.session.connect` |
| `2026-08-01 03:08:14` | `cowrie.client.version` |
| `2026-08-01 03:08:14` | `cowrie.client.kex` |
| `2026-08-01 03:08:18` | `cowrie.login.success` |
| `2026-08-01 03:08:21` | `cowrie.session.params` |
| `2026-08-01 03:08:21` | `cowrie.command.input` |
| `2026-08-01 03:08:22` | `cowrie.log.closed` |
| `2026-08-01 03:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d13461d15a1f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:08 |
| **Last Seen** | 2026-08-01 03:08 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:08:20` | `cowrie.session.connect` |
| `2026-08-01 03:08:21` | `cowrie.client.version` |
| `2026-08-01 03:08:21` | `cowrie.client.kex` |
| `2026-08-01 03:08:25` | `cowrie.login.success` |
| `2026-08-01 03:08:29` | `cowrie.session.params` |
| `2026-08-01 03:08:29` | `cowrie.command.input` |
| `2026-08-01 03:08:30` | `cowrie.log.closed` |
| `2026-08-01 03:08:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61e84aea8b13

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-08-01 03:08 |
| **Last Seen** | 2026-08-01 03:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:08:25` | `cowrie.session.connect` |
| `2026-08-01 03:08:26` | `cowrie.client.version` |
| `2026-08-01 03:08:26` | `cowrie.client.kex` |
| `2026-08-01 03:08:30` | `cowrie.login.success` |
| `2026-08-01 03:08:31` | `cowrie.session.params` |
| `2026-08-01 03:08:31` | `cowrie.command.input` |
| `2026-08-01 03:08:31` | `cowrie.log.closed` |
| `2026-08-01 03:08:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-943720f1bb9d

| Field | Detail |
|---|---|
| **Source IP** | `187.212.37[.]143` |
| **First Seen** | 2026-08-01 03:12 |
| **Last Seen** | 2026-08-01 03:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:12:52` | `cowrie.session.connect` |
| `2026-08-01 03:12:52` | `cowrie.client.version` |
| `2026-08-01 03:12:52` | `cowrie.client.kex` |
| `2026-08-01 03:12:52` | `cowrie.login.success` |
| `2026-08-01 03:12:53` | `cowrie.session.params` |
| `2026-08-01 03:12:53` | `cowrie.command.input` |
| `2026-08-01 03:12:53` | `cowrie.command.failed` |
| `2026-08-01 03:12:53` | `cowrie.log.closed` |
| `2026-08-01 03:12:54` | `cowrie.session.params` |
| `2026-08-01 03:12:54` | `cowrie.command.input` |
| `2026-08-01 03:12:54` | `cowrie.session.file_download` |
| `2026-08-01 03:12:54` | `cowrie.log.closed` |
| `2026-08-01 03:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.37[.]143` to AbuseIPDB if not already reported
- [ ] Block `187.212.37[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f0701f3636c

| Field | Detail |
|---|---|
| **Source IP** | `187.212.37[.]143` |
| **First Seen** | 2026-08-01 03:12 |
| **Last Seen** | 2026-08-01 03:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:12:54` | `cowrie.session.connect` |
| `2026-08-01 03:12:54` | `cowrie.client.version` |
| `2026-08-01 03:12:54` | `cowrie.client.kex` |
| `2026-08-01 03:12:54` | `cowrie.login.success` |
| `2026-08-01 03:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.37[.]143` to AbuseIPDB if not already reported
- [ ] Block `187.212.37[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0bc502cddd2

| Field | Detail |
|---|---|
| **Source IP** | `187.212.37[.]143` |
| **First Seen** | 2026-08-01 03:12 |
| **Last Seen** | 2026-08-01 03:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:12:55` | `cowrie.session.connect` |
| `2026-08-01 03:12:55` | `cowrie.client.version` |
| `2026-08-01 03:12:55` | `cowrie.client.kex` |
| `2026-08-01 03:12:55` | `cowrie.login.success` |
| `2026-08-01 03:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.37[.]143` to AbuseIPDB if not already reported
- [ ] Block `187.212.37[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f2048f2f302

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 03:12 |
| **Last Seen** | 2026-08-01 03:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:12:55` | `cowrie.session.connect` |
| `2026-08-01 03:12:55` | `cowrie.client.version` |
| `2026-08-01 03:12:55` | `cowrie.client.kex` |
| `2026-08-01 03:12:55` | `cowrie.login.success` |
| `2026-08-01 03:12:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0613f7a37dbb

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 03:12 |
| **Last Seen** | 2026-08-01 03:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:12:55` | `cowrie.session.connect` |
| `2026-08-01 03:12:55` | `cowrie.client.version` |
| `2026-08-01 03:12:55` | `cowrie.client.kex` |
| `2026-08-01 03:12:55` | `cowrie.login.success` |
| `2026-08-01 03:12:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a656bfda539

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 03:12 |
| **Last Seen** | 2026-08-01 03:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:12:57` | `cowrie.session.connect` |
| `2026-08-01 03:12:57` | `cowrie.client.version` |
| `2026-08-01 03:12:57` | `cowrie.client.kex` |
| `2026-08-01 03:12:57` | `cowrie.login.success` |
| `2026-08-01 03:12:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d19b0d5a3b2b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 03:12 |
| **Last Seen** | 2026-08-01 03:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:12:57` | `cowrie.session.connect` |
| `2026-08-01 03:12:57` | `cowrie.client.version` |
| `2026-08-01 03:12:57` | `cowrie.client.kex` |
| `2026-08-01 03:12:57` | `cowrie.login.success` |
| `2026-08-01 03:12:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7693c0e71277

| Field | Detail |
|---|---|
| **Source IP** | `60.54.18[.]211` |
| **First Seen** | 2026-08-01 03:13 |
| **Last Seen** | 2026-08-01 03:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:13:06` | `cowrie.session.connect` |
| `2026-08-01 03:13:06` | `cowrie.client.version` |
| `2026-08-01 03:13:06` | `cowrie.client.kex` |
| `2026-08-01 03:13:07` | `cowrie.login.success` |
| `2026-08-01 03:13:08` | `cowrie.session.params` |
| `2026-08-01 03:13:08` | `cowrie.command.input` |
| `2026-08-01 03:13:08` | `cowrie.command.failed` |
| `2026-08-01 03:13:09` | `cowrie.log.closed` |
| `2026-08-01 03:13:09` | `cowrie.session.params` |
| `2026-08-01 03:13:09` | `cowrie.command.input` |
| `2026-08-01 03:13:10` | `cowrie.session.file_download` |
| `2026-08-01 03:13:10` | `cowrie.log.closed` |
| `2026-08-01 03:13:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.54.18[.]211` to AbuseIPDB if not already reported
- [ ] Block `60.54.18[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca9597b824a6

| Field | Detail |
|---|---|
| **Source IP** | `60.54.18[.]211` |
| **First Seen** | 2026-08-01 03:13 |
| **Last Seen** | 2026-08-01 03:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:13:10` | `cowrie.session.connect` |
| `2026-08-01 03:13:10` | `cowrie.client.version` |
| `2026-08-01 03:13:10` | `cowrie.client.kex` |
| `2026-08-01 03:13:11` | `cowrie.login.success` |
| `2026-08-01 03:13:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.54.18[.]211` to AbuseIPDB if not already reported
- [ ] Block `60.54.18[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd265303ad5d

| Field | Detail |
|---|---|
| **Source IP** | `60.54.18[.]211` |
| **First Seen** | 2026-08-01 03:13 |
| **Last Seen** | 2026-08-01 03:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:13:12` | `cowrie.session.connect` |
| `2026-08-01 03:13:12` | `cowrie.client.version` |
| `2026-08-01 03:13:12` | `cowrie.client.kex` |
| `2026-08-01 03:13:13` | `cowrie.login.success` |
| `2026-08-01 03:13:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.54.18[.]211` to AbuseIPDB if not already reported
- [ ] Block `60.54.18[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73e7452b5486

| Field | Detail |
|---|---|
| **Source IP** | `27.50.29[.]181` |
| **First Seen** | 2026-08-01 03:18 |
| **Last Seen** | 2026-08-01 03:19 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:18:43` | `cowrie.session.connect` |
| `2026-08-01 03:18:44` | `cowrie.client.version` |
| `2026-08-01 03:18:44` | `cowrie.client.kex` |
| `2026-08-01 03:18:52` | `cowrie.login.success` |
| `2026-08-01 03:18:58` | `cowrie.session.params` |
| `2026-08-01 03:18:58` | `cowrie.command.input` |
| `2026-08-01 03:19:00` | `cowrie.log.closed` |
| `2026-08-01 03:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.50.29[.]181` to AbuseIPDB if not already reported
- [ ] Block `27.50.29[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eb8daaf9601

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-08-01 03:20 |
| **Last Seen** | 2026-08-01 03:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:20:36` | `cowrie.session.connect` |
| `2026-08-01 03:20:37` | `cowrie.client.version` |
| `2026-08-01 03:20:37` | `cowrie.client.kex` |
| `2026-08-01 03:20:39` | `cowrie.login.success` |
| `2026-08-01 03:20:40` | `cowrie.direct-tcpip.request` |
| `2026-08-01 03:20:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7c66cb02e32

| Field | Detail |
|---|---|
| **Source IP** | `196.245.52[.]130` |
| **First Seen** | 2026-08-01 03:24 |
| **Last Seen** | 2026-08-01 03:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:24:07` | `cowrie.session.connect` |
| `2026-08-01 03:24:11` | `cowrie.telnet.option` |
| `2026-08-01 03:24:13` | `cowrie.telnet.option` |
| `2026-08-01 03:25:14` | `cowrie.login.success` |
| `2026-08-01 03:25:15` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `196.245.52[.]130` to AbuseIPDB if not already reported
- [ ] Block `196.245.52[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2003692a6af1

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-08-01 03:29 |
| **Last Seen** | 2026-08-01 03:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:29:22` | `cowrie.session.connect` |
| `2026-08-01 03:29:22` | `cowrie.client.version` |
| `2026-08-01 03:29:22` | `cowrie.client.kex` |
| `2026-08-01 03:29:25` | `cowrie.login.success` |
| `2026-08-01 03:29:25` | `cowrie.direct-tcpip.request` |
| `2026-08-01 03:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77bbf2e05340

| Field | Detail |
|---|---|
| **Source IP** | `65.20.251[.]170` |
| **First Seen** | 2026-08-01 03:31 |
| **Last Seen** | 2026-08-01 03:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:31:19` | `cowrie.session.connect` |
| `2026-08-01 03:31:19` | `cowrie.client.version` |
| `2026-08-01 03:31:19` | `cowrie.client.kex` |
| `2026-08-01 03:31:20` | `cowrie.login.success` |
| `2026-08-01 03:31:21` | `cowrie.direct-tcpip.request` |
| `2026-08-01 03:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.251[.]170` to AbuseIPDB if not already reported
- [ ] Block `65.20.251[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45e57f7150f5

| Field | Detail |
|---|---|
| **Source IP** | `124.133.10[.]66` |
| **First Seen** | 2026-08-01 03:31 |
| **Last Seen** | 2026-08-01 03:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:31:26` | `cowrie.session.connect` |
| `2026-08-01 03:31:27` | `cowrie.client.version` |
| `2026-08-01 03:31:27` | `cowrie.client.kex` |
| `2026-08-01 03:31:29` | `cowrie.login.success` |
| `2026-08-01 03:31:30` | `cowrie.direct-tcpip.request` |
| `2026-08-01 03:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.133.10[.]66` to AbuseIPDB if not already reported
- [ ] Block `124.133.10[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20c5d59df851

| Field | Detail |
|---|---|
| **Source IP** | `103.190.91[.]116` |
| **First Seen** | 2026-08-01 03:38 |
| **Last Seen** | 2026-08-01 03:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:38:58` | `cowrie.session.connect` |
| `2026-08-01 03:38:59` | `cowrie.client.version` |
| `2026-08-01 03:38:59` | `cowrie.client.kex` |
| `2026-08-01 03:39:00` | `cowrie.login.success` |
| `2026-08-01 03:39:01` | `cowrie.direct-tcpip.request` |
| `2026-08-01 03:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.91[.]116` to AbuseIPDB if not already reported
- [ ] Block `103.190.91[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a49d97bbfb6

| Field | Detail |
|---|---|
| **Source IP** | `118.163.145[.]175` |
| **First Seen** | 2026-08-01 03:45 |
| **Last Seen** | 2026-08-01 03:45 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:45:40` | `cowrie.session.connect` |
| `2026-08-01 03:45:40` | `cowrie.client.version` |
| `2026-08-01 03:45:40` | `cowrie.client.kex` |
| `2026-08-01 03:45:43` | `cowrie.login.success` |
| `2026-08-01 03:45:44` | `cowrie.direct-tcpip.request` |
| `2026-08-01 03:45:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.145[.]175` to AbuseIPDB if not already reported
- [ ] Block `118.163.145[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0d8f3699163

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-01 03:47 |
| **Last Seen** | 2026-08-01 03:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:47:53` | `cowrie.session.connect` |
| `2026-08-01 03:47:53` | `cowrie.client.version` |
| `2026-08-01 03:47:53` | `cowrie.client.kex` |
| `2026-08-01 03:47:55` | `cowrie.login.success` |
| `2026-08-01 03:47:55` | `cowrie.direct-tcpip.request` |
| `2026-08-01 03:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44457fb500f2

| Field | Detail |
|---|---|
| **Source IP** | `46.77.69[.]201` |
| **First Seen** | 2026-08-01 03:48 |
| **Last Seen** | 2026-08-01 03:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:48:04` | `cowrie.session.connect` |
| `2026-08-01 03:48:05` | `cowrie.client.version` |
| `2026-08-01 03:48:05` | `cowrie.client.kex` |
| `2026-08-01 03:48:07` | `cowrie.login.success` |
| `2026-08-01 03:48:08` | `cowrie.direct-tcpip.request` |
| `2026-08-01 03:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.77.69[.]201` to AbuseIPDB if not already reported
- [ ] Block `46.77.69[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c262466e020

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]119` |
| **First Seen** | 2026-08-01 03:53 |
| **Last Seen** | 2026-08-01 03:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:53:01` | `cowrie.session.connect` |
| `2026-08-01 03:53:02` | `cowrie.client.version` |
| `2026-08-01 03:53:02` | `cowrie.client.kex` |
| `2026-08-01 03:53:04` | `cowrie.login.success` |
| `2026-08-01 03:53:05` | `cowrie.direct-tcpip.request` |
| `2026-08-01 03:53:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1120d8435eb2

| Field | Detail |
|---|---|
| **Source IP** | `8.152.171[.]185` |
| **First Seen** | 2026-08-01 03:53 |
| **Last Seen** | 2026-08-01 03:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:53:52` | `cowrie.session.connect` |
| `2026-08-01 03:53:52` | `cowrie.client.version` |
| `2026-08-01 03:53:53` | `cowrie.client.kex` |
| `2026-08-01 03:53:54` | `cowrie.login.success` |
| `2026-08-01 03:53:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.152.171[.]185` to AbuseIPDB if not already reported
- [ ] Block `8.152.171[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05aed5b1addd

| Field | Detail |
|---|---|
| **Source IP** | `220.161.52[.]149` |
| **First Seen** | 2026-08-01 03:54 |
| **Last Seen** | 2026-08-01 03:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:54:50` | `cowrie.session.connect` |
| `2026-08-01 03:54:51` | `cowrie.client.version` |
| `2026-08-01 03:54:51` | `cowrie.client.kex` |
| `2026-08-01 03:54:53` | `cowrie.login.success` |
| `2026-08-01 03:54:54` | `cowrie.direct-tcpip.request` |
| `2026-08-01 03:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.161.52[.]149` to AbuseIPDB if not already reported
- [ ] Block `220.161.52[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eabd9365a000

| Field | Detail |
|---|---|
| **Source IP** | `220.178.39[.]106` |
| **First Seen** | 2026-08-01 03:55 |
| **Last Seen** | 2026-08-01 03:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:55:03` | `cowrie.session.connect` |
| `2026-08-01 03:55:04` | `cowrie.client.version` |
| `2026-08-01 03:55:04` | `cowrie.client.kex` |
| `2026-08-01 03:55:06` | `cowrie.login.success` |
| `2026-08-01 03:55:07` | `cowrie.direct-tcpip.request` |
| `2026-08-01 03:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.39[.]106` to AbuseIPDB if not already reported
- [ ] Block `220.178.39[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca6667b846b4

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-01 03:55 |
| **Last Seen** | 2026-08-01 03:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:55:12` | `cowrie.session.connect` |
| `2026-08-01 03:55:12` | `cowrie.client.version` |
| `2026-08-01 03:55:12` | `cowrie.client.kex` |
| `2026-08-01 03:55:13` | `cowrie.login.success` |
| `2026-08-01 03:55:14` | `cowrie.direct-tcpip.request` |
| `2026-08-01 03:55:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37540c76f123

| Field | Detail |
|---|---|
| **Source IP** | `163.7.6[.]41` |
| **First Seen** | 2026-08-01 03:55 |
| **Last Seen** | 2026-08-01 03:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:55:47` | `cowrie.session.connect` |
| `2026-08-01 03:55:47` | `cowrie.client.version` |
| `2026-08-01 03:55:47` | `cowrie.client.kex` |
| `2026-08-01 03:55:48` | `cowrie.login.success` |
| `2026-08-01 03:55:49` | `cowrie.session.params` |
| `2026-08-01 03:55:49` | `cowrie.command.input` |
| `2026-08-01 03:55:49` | `cowrie.command.failed` |
| `2026-08-01 03:55:50` | `cowrie.log.closed` |
| `2026-08-01 03:55:50` | `cowrie.session.params` |
| `2026-08-01 03:55:50` | `cowrie.command.input` |
| `2026-08-01 03:55:51` | `cowrie.session.file_download` |
| `2026-08-01 03:55:51` | `cowrie.log.closed` |
| `2026-08-01 03:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.6[.]41` to AbuseIPDB if not already reported
- [ ] Block `163.7.6[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4dc888b0bdf

| Field | Detail |
|---|---|
| **Source IP** | `163.7.6[.]41` |
| **First Seen** | 2026-08-01 03:55 |
| **Last Seen** | 2026-08-01 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:55:51` | `cowrie.session.connect` |
| `2026-08-01 03:55:51` | `cowrie.client.version` |
| `2026-08-01 03:55:51` | `cowrie.client.kex` |
| `2026-08-01 03:55:52` | `cowrie.login.success` |
| `2026-08-01 03:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.6[.]41` to AbuseIPDB if not already reported
- [ ] Block `163.7.6[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-182fa14a0137

| Field | Detail |
|---|---|
| **Source IP** | `163.7.6[.]41` |
| **First Seen** | 2026-08-01 03:55 |
| **Last Seen** | 2026-08-01 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:55:53` | `cowrie.session.connect` |
| `2026-08-01 03:55:53` | `cowrie.client.version` |
| `2026-08-01 03:55:53` | `cowrie.client.kex` |
| `2026-08-01 03:55:54` | `cowrie.login.success` |
| `2026-08-01 03:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.6[.]41` to AbuseIPDB if not already reported
- [ ] Block `163.7.6[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa3f32c7e52d

| Field | Detail |
|---|---|
| **Source IP** | `51.254.113[.]225` |
| **First Seen** | 2026-08-01 03:57 |
| **Last Seen** | 2026-08-01 03:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:57:56` | `cowrie.session.connect` |
| `2026-08-01 03:57:56` | `cowrie.client.version` |
| `2026-08-01 03:57:56` | `cowrie.client.kex` |
| `2026-08-01 03:57:57` | `cowrie.login.success` |
| `2026-08-01 03:57:57` | `cowrie.session.params` |
| `2026-08-01 03:57:57` | `cowrie.command.input` |
| `2026-08-01 03:57:57` | `cowrie.command.failed` |
| `2026-08-01 03:57:57` | `cowrie.log.closed` |
| `2026-08-01 03:57:58` | `cowrie.session.params` |
| `2026-08-01 03:57:58` | `cowrie.command.input` |
| `2026-08-01 03:57:58` | `cowrie.session.file_download` |
| `2026-08-01 03:57:58` | `cowrie.log.closed` |
| `2026-08-01 03:58:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.254.113[.]225` to AbuseIPDB if not already reported
- [ ] Block `51.254.113[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ef1852570e5

| Field | Detail |
|---|---|
| **Source IP** | `51.254.113[.]225` |
| **First Seen** | 2026-08-01 03:57 |
| **Last Seen** | 2026-08-01 03:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:57:58` | `cowrie.session.connect` |
| `2026-08-01 03:57:58` | `cowrie.client.version` |
| `2026-08-01 03:57:59` | `cowrie.client.kex` |
| `2026-08-01 03:57:59` | `cowrie.login.success` |
| `2026-08-01 03:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.254.113[.]225` to AbuseIPDB if not already reported
- [ ] Block `51.254.113[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fed120f2ccfe

| Field | Detail |
|---|---|
| **Source IP** | `51.254.113[.]225` |
| **First Seen** | 2026-08-01 03:57 |
| **Last Seen** | 2026-08-01 03:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 03:57:59` | `cowrie.session.connect` |
| `2026-08-01 03:57:59` | `cowrie.client.version` |
| `2026-08-01 03:57:59` | `cowrie.client.kex` |
| `2026-08-01 03:58:00` | `cowrie.login.success` |
| `2026-08-01 03:58:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.254.113[.]225` to AbuseIPDB if not already reported
- [ ] Block `51.254.113[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b1c9fc8b92b

| Field | Detail |
|---|---|
| **Source IP** | `118.194.235[.]105` |
| **First Seen** | 2026-08-01 04:04 |
| **Last Seen** | 2026-08-01 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 04:04:15` | `cowrie.session.connect` |
| `2026-08-01 04:04:15` | `cowrie.client.version` |
| `2026-08-01 04:04:15` | `cowrie.client.kex` |
| `2026-08-01 04:04:16` | `cowrie.login.success` |
| `2026-08-01 04:04:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.235[.]105` to AbuseIPDB if not already reported
- [ ] Block `118.194.235[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01b5c357c07d

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-01 04:04 |
| **Last Seen** | 2026-08-01 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 04:04:16` | `cowrie.session.connect` |
| `2026-08-01 04:04:16` | `cowrie.client.version` |
| `2026-08-01 04:04:16` | `cowrie.client.kex` |
| `2026-08-01 04:04:16` | `cowrie.login.success` |
| `2026-08-01 04:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e24ea3561a4

| Field | Detail |
|---|---|
| **Source IP** | `162.243.147[.]237` |
| **First Seen** | 2026-08-01 04:18 |
| **Last Seen** | 2026-08-01 04:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 04:18:05` | `cowrie.session.connect` |
| `2026-08-01 04:18:05` | `cowrie.client.version` |
| `2026-08-01 04:18:05` | `cowrie.client.kex` |
| `2026-08-01 04:18:06` | `cowrie.login.success` |
| `2026-08-01 04:18:06` | `cowrie.session.params` |
| `2026-08-01 04:18:06` | `cowrie.command.input` |
| `2026-08-01 04:18:06` | `cowrie.command.failed` |
| `2026-08-01 04:18:07` | `cowrie.log.closed` |
| `2026-08-01 04:18:07` | `cowrie.session.params` |
| `2026-08-01 04:18:07` | `cowrie.command.input` |
| `2026-08-01 04:18:07` | `cowrie.session.file_download` |
| `2026-08-01 04:18:07` | `cowrie.log.closed` |
| `2026-08-01 04:18:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `162.243.147[.]237` to AbuseIPDB if not already reported
- [ ] Block `162.243.147[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f181c3e6cf47

| Field | Detail |
|---|---|
| **Source IP** | `162.243.147[.]237` |
| **First Seen** | 2026-08-01 04:18 |
| **Last Seen** | 2026-08-01 04:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 04:18:07` | `cowrie.session.connect` |
| `2026-08-01 04:18:07` | `cowrie.client.version` |
| `2026-08-01 04:18:07` | `cowrie.client.kex` |
| `2026-08-01 04:18:08` | `cowrie.login.success` |
| `2026-08-01 04:18:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `162.243.147[.]237` to AbuseIPDB if not already reported
- [ ] Block `162.243.147[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5a52b74199a

| Field | Detail |
|---|---|
| **Source IP** | `162.243.147[.]237` |
| **First Seen** | 2026-08-01 04:18 |
| **Last Seen** | 2026-08-01 04:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 04:18:08` | `cowrie.session.connect` |
| `2026-08-01 04:18:08` | `cowrie.client.version` |
| `2026-08-01 04:18:08` | `cowrie.client.kex` |
| `2026-08-01 04:18:08` | `cowrie.login.success` |
| `2026-08-01 04:18:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `162.243.147[.]237` to AbuseIPDB if not already reported
- [ ] Block `162.243.147[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d879effb8ca

| Field | Detail |
|---|---|
| **Source IP** | `43.226.39[.]177` |
| **First Seen** | 2026-08-01 04:19 |
| **Last Seen** | 2026-08-01 04:21 |
| **Session Duration** | 106s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 04:19:29` | `cowrie.session.connect` |
| `2026-08-01 04:21:00` | `cowrie.client.version` |
| `2026-08-01 04:21:00` | `cowrie.client.kex` |
| `2026-08-01 04:21:15` | `cowrie.login.success` |
| `2026-08-01 04:21:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.226.39[.]177` to AbuseIPDB if not already reported
- [ ] Block `43.226.39[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3842a0abfcb5

| Field | Detail |
|---|---|
| **Source IP** | `115.245.122[.]146` |
| **First Seen** | 2026-08-01 04:20 |
| **Last Seen** | 2026-08-01 04:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 04:20:16` | `cowrie.session.connect` |
| `2026-08-01 04:20:17` | `cowrie.client.version` |
| `2026-08-01 04:20:17` | `cowrie.client.kex` |
| `2026-08-01 04:20:19` | `cowrie.login.success` |
| `2026-08-01 04:20:19` | `cowrie.direct-tcpip.request` |
| `2026-08-01 04:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.245.122[.]146` to AbuseIPDB if not already reported
- [ ] Block `115.245.122[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-975506938e54

| Field | Detail |
|---|---|
| **Source IP** | `90.230.168[.]26` |
| **First Seen** | 2026-08-01 04:20 |
| **Last Seen** | 2026-08-01 04:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 04:20:24` | `cowrie.session.connect` |
| `2026-08-01 04:20:25` | `cowrie.client.version` |
| `2026-08-01 04:20:25` | `cowrie.client.kex` |
| `2026-08-01 04:20:26` | `cowrie.login.success` |
| `2026-08-01 04:20:26` | `cowrie.direct-tcpip.request` |
| `2026-08-01 04:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.230.168[.]26` to AbuseIPDB if not already reported
- [ ] Block `90.230.168[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc21525b05e6

| Field | Detail |
|---|---|
| **Source IP** | `122.170.99[.]195` |
| **First Seen** | 2026-08-01 04:22 |
| **Last Seen** | 2026-08-01 04:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 04:22:26` | `cowrie.session.connect` |
| `2026-08-01 04:22:27` | `cowrie.client.version` |
| `2026-08-01 04:22:27` | `cowrie.client.kex` |
| `2026-08-01 04:22:29` | `cowrie.login.success` |
| `2026-08-01 04:22:29` | `cowrie.direct-tcpip.request` |
| `2026-08-01 04:22:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.99[.]195` to AbuseIPDB if not already reported
- [ ] Block `122.170.99[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47ec72cf730d

| Field | Detail |
|---|---|
| **Source IP** | `93.241.232[.]14` |
| **First Seen** | 2026-08-01 04:29 |
| **Last Seen** | 2026-08-01 04:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 04:29:41` | `cowrie.session.connect` |
| `2026-08-01 04:29:42` | `cowrie.client.version` |
| `2026-08-01 04:29:42` | `cowrie.client.kex` |
| `2026-08-01 04:29:43` | `cowrie.login.success` |
| `2026-08-01 04:29:43` | `cowrie.direct-tcpip.request` |
| `2026-08-01 04:29:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.241.232[.]14` to AbuseIPDB if not already reported
- [ ] Block `93.241.232[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21457e10c8a4

| Field | Detail |
|---|---|
| **Source IP** | `220.246.43[.]172` |
| **First Seen** | 2026-08-01 04:29 |
| **Last Seen** | 2026-08-01 04:29 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 04:29:48` | `cowrie.session.connect` |
| `2026-08-01 04:29:49` | `cowrie.client.version` |
| `2026-08-01 04:29:49` | `cowrie.client.kex` |
| `2026-08-01 04:29:53` | `cowrie.login.success` |
| `2026-08-01 04:29:54` | `cowrie.direct-tcpip.request` |
| `2026-08-01 04:29:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.43[.]172` to AbuseIPDB if not already reported
- [ ] Block `220.246.43[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa1b1d9c7983

| Field | Detail |
|---|---|
| **Source IP** | `211.247.127[.]250` |
| **First Seen** | 2026-08-01 04:29 |
| **Last Seen** | 2026-08-01 04:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 04:29:58` | `cowrie.session.connect` |
| `2026-08-01 04:29:59` | `cowrie.client.version` |
| `2026-08-01 04:29:59` | `cowrie.client.kex` |
| `2026-08-01 04:30:01` | `cowrie.login.success` |
| `2026-08-01 04:30:02` | `cowrie.direct-tcpip.request` |
| `2026-08-01 04:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.247.127[.]250` to AbuseIPDB if not already reported
- [ ] Block `211.247.127[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-703cf3a31e28

| Field | Detail |
|---|---|
| **Source IP** | `103.174.145[.]35` |
| **First Seen** | 2026-08-01 04:30 |
| **Last Seen** | 2026-08-01 04:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 04:30:07` | `cowrie.session.connect` |
| `2026-08-01 04:30:08` | `cowrie.client.version` |
| `2026-08-01 04:30:08` | `cowrie.client.kex` |
| `2026-08-01 04:30:09` | `cowrie.login.success` |
| `2026-08-01 04:30:10` | `cowrie.direct-tcpip.request` |
| `2026-08-01 04:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.145[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.174.145[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd38e3d78478

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-01 04:33 |
| **Last Seen** | 2026-08-01 04:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 04:33:04` | `cowrie.session.connect` |
| `2026-08-01 04:33:04` | `cowrie.client.version` |
| `2026-08-01 04:33:04` | `cowrie.client.kex` |
| `2026-08-01 04:33:05` | `cowrie.login.success` |
| `2026-08-01 04:33:05` | `cowrie.direct-tcpip.request` |
| `2026-08-01 04:33:05` | `cowrie.direct-tcpip.data` |
| `2026-08-01 04:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e66066550c0

| Field | Detail |
|---|---|
| **Source IP** | `8.211.21[.]181` |
| **First Seen** | 2026-08-01 04:35 |
| **Last Seen** | 2026-08-01 04:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: curl/7.64.1, Accept: */*` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 04:35:05` | `cowrie.session.connect` |
| `2026-08-01 04:35:05` | `cowrie.login.success` |
| `2026-08-01 04:35:06` | `cowrie.session.params` |
| `2026-08-01 04:35:06` | `cowrie.command.input` |
| `2026-08-01 04:35:06` | `cowrie.command.failed` |
| `2026-08-01 04:35:06` | `cowrie.command.input` |
| `2026-08-01 04:35:06` | `cowrie.command.failed` |
| `2026-08-01 04:35:06` | `cowrie.command.input` |
| `2026-08-01 04:35:08` | `cowrie.log.closed` |
| `2026-08-01 04:35:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.211.21[.]181` to AbuseIPDB if not already reported
- [ ] Block `8.211.21[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c92c01ac8d27

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-01 04:41 |
| **Last Seen** | 2026-08-01 04:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 04:41:00` | `cowrie.session.connect` |
| `2026-08-01 04:41:00` | `cowrie.client.version` |
| `2026-08-01 04:41:01` | `cowrie.client.kex` |
| `2026-08-01 04:41:01` | `cowrie.login.success` |
| `2026-08-01 04:41:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1db2e3e908e4

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-01 04:41 |
| **Last Seen** | 2026-08-01 04:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 04:41:01` | `cowrie.session.connect` |
| `2026-08-01 04:41:01` | `cowrie.client.version` |
| `2026-08-01 04:41:01` | `cowrie.client.kex` |
| `2026-08-01 04:41:02` | `cowrie.login.success` |
| `2026-08-01 04:41:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **14** | 2026-08-01 03:04 | 2026-08-01 04:47 | 10m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-01 02:55 | 2026-08-01 04:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **3** | 2026-08-01 03:08 | 2026-08-01 04:31 | 2m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-08-01 03:09 | 2026-08-01 03:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | **3** | 2026-08-01 04:27 | 2026-08-01 04:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `35.187.231[.]181` | **3** | 2026-08-01 03:05 | 2026-08-01 03:06 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-08-01 04:06 | 2026-08-01 04:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-01 03:22 | 2026-08-01 04:21 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `222.88.163[.]204` | **2** | 2026-08-01 04:38 | 2026-08-01 04:40 | 2m | 0 | `T1592` | 🟢 LOW |
| `34.122.244[.]225` | **2** | 2026-08-01 04:09 | 2026-08-01 04:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **2** | 2026-08-01 03:32 | 2026-08-01 04:09 | 1m | 0 | `T1592` | 🟢 LOW |
| `8.211.21[.]181` | **2** | 2026-08-01 04:34 | 2026-08-01 04:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `182.252.140[.]114` | 1 | 2026-08-01 03:18 | 2026-08-01 03:18 | 5s | 0 | `T1592` | 🟢 LOW |
| `183.171.236[.]23` | 1 | 2026-08-01 03:39 | 2026-08-01 03:39 | 8s | 0 | `T1592` | 🟢 LOW |
| `210.182.73[.]132` | 1 | 2026-08-01 03:55 | 2026-08-01 03:55 | 10s | 0 | `T1592` | 🟢 LOW |
| `210.61.64[.]135` | 1 | 2026-08-01 04:43 | 2026-08-01 04:43 | 31s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-08-01 03:09 | 2026-08-01 03:10 | 39s | 0 | `T1592` | 🟢 LOW |
| `220.180.171[.]157` | 1 | 2026-08-01 03:53 | 2026-08-01 03:53 | 10s | 0 | `T1592` | 🟢 LOW |
| `222.99.52[.]202` | 1 | 2026-08-01 04:04 | 2026-08-01 04:04 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-08-01 04:09 | 2026-08-01 04:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-08-01 04:34 | 2026-08-01 04:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-08-01 03:46 | 2026-08-01 03:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.16.103[.]46` | 1 | 2026-08-01 03:33 | 2026-08-01 03:34 | 48s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-08-01 04:02 | 2026-08-01 04:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]196` | 1 | 2026-08-01 04:03 | 2026-08-01 04:03 | 17s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-08-01 03:38 | 2026-08-01 03:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.230.212[.]29` | 1 | 2026-08-01 04:38 | 2026-08-01 04:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.92.42[.]36` | 1 | 2026-08-01 03:07 | 2026-08-01 03:07 | 11s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `3f3bf218089d1488617d37f8a5116bb2791eb39ce06a1b5bc9a4cdfe5e94dd39` | ELF Binary (Linux executable) (RISC-V 64-bit) | `3f3bf218089d1488...` | 33/100 | 🟢 LOW | **9/75** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |

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

_`197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` (197c74408e15bd1168105f56...)_
- `Execution from /tmp` — `/tmp/clean_file`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
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
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `210.182.73[.]132` | KR | LG DACOM Corporation | **100** ⚠️ | 44 |
| `122.170.99[.]195` | IN | ABTS-MUMBAI | **100** ⚠️ | 50 |
| `65.20.251[.]170` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `194.165.16[.]162` | PA | Flyservers S.A. | **100** ⚠️ | 50 |
| `60.54.18[.]211` | MY | TM TECHNOLOGY SERVICES SDN. BHD. | **100** ⚠️ | 3 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 5 |
| `88.214.25[.]125` | DE | VDS&VPN services | **100** ⚠️ | 50 |
| `103.174.145[.]35` | IN | VAIDIK NETSOL OPC PVT LTD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 212 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 195 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |

---

## 🔕 False Positive Summary (19 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 3 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 274 cases |
| Tool 34  | Credential Extractor        | ✅ 220 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 18 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 82 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 19 filtered (6.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 59 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 26 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 195 priority case(s) shown individually · 28 recon entry/entries in table (12 group(s) consolidating 44 session(s)).

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
_Report time: 2026-08-01T06:34:35Z_

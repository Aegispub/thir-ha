# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-29 |
| **Generated At** | 2026-07-29T06:36:43Z |
| **Shift Time** | 06:36 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **590** |
| Confirmed Threats | **554** |
| False Positives Filtered | **36** (6.1%) |
| Unique Attacker IPs | **161** |
| Countries of Origin | **36** |
| High Severity Cases | **318** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **272** |
| Malware Samples Analyzed | **3** HIGH · **30** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **349** |
| Unique Credential Pairs | **232** |
| Unique Usernames | **37** |
| Unique Passwords | **126** |
| Successful Auth Pairs | **322** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 78 |
| `admin` | 22 |
| `support` | 21 |
| `oracle` | 13 |
| `administrator` | 11 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 25 |
| `123456` | 20 |
| `password` | 18 |
| `qwerty` | 18 |
| `server` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 8 |
| `root` | `LeitboGi0ro` | 7 |
| `root` | `smo@@kkklss` | 6 |
| `ubnt` | `44` | 6 |
| `oracle` | `123123123` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ts3` | `ts3@123` | `193.32.162.15` | 2026-07-29T00:55:59 |
| `centos` | `5555555` | `210.0.90.82` | 2026-07-29T00:56:58 |
| `ts3` | `Ts3123` | `193.32.162.15` | 2026-07-29T00:57:18 |
| `centos` | `5555555` | `10.0.0.73` | 2026-07-29T00:57:24 |
| `ts3` | `server` | `193.32.162.15` | 2026-07-29T00:58:40 |
| `minecraft` | `minecraft` | `193.32.162.15` | 2026-07-29T01:00:03 |
| `minecraft` | `password` | `193.32.162.15` | 2026-07-29T01:01:27 |
| `operator` | `operator` | `171.231.196.169` | 2026-07-29T01:01:52 |
| `minecraft` | `123456` | `193.32.162.15` | 2026-07-29T01:02:50 |
| `administrator` | `987654321` | `200.89.159.59` | 2026-07-29T01:03:30 |
| `administrator` | `987654321` | `45.178.227.0` | 2026-07-29T01:03:42 |
| `minecraft` | `qwerty` | `193.32.162.15` | 2026-07-29T01:04:13 |
| `minecraft` | `admin` | `193.32.162.15` | 2026-07-29T01:05:36 |
| `root` | `ipscan` | `171.231.177.152` | 2026-07-29T01:05:48 |
| `support` | `admin` | `171.231.177.152` | 2026-07-29T01:05:58 |
| `minecraft` | `minecraft123` | `193.32.162.15` | 2026-07-29T01:07:01 |
| `root` | `` | `94.154.43.144` | 2026-07-29T01:07:18 |
| `minecraft` | `server` | `193.32.162.15` | 2026-07-29T01:08:25 |
| `minecraft` | `craft` | `193.32.162.15` | 2026-07-29T01:09:49 |
| `minecraft` | `notch` | `193.32.162.15` | 2026-07-29T01:11:09 |
| `git` | `git` | `193.32.162.15` | 2026-07-29T01:12:31 |
| `git` | `password` | `193.32.162.15` | 2026-07-29T01:13:54 |
| `support` | `777` | `187.115.144.103` | 2026-07-29T01:15:02 |
| `support` | `777` | `220.122.115.9` | 2026-07-29T01:15:11 |
| `git` | `123456` | `193.32.162.15` | 2026-07-29T01:15:19 |
| `mike` | `mike2024` | `103.193.179.139` | 2026-07-29T01:15:27 |
| `345gs5662d34` | `345gs5662d34` | `103.193.179.139` | 2026-07-29T01:15:32 |
| `mike` | `3245gs5662d34` | `103.193.179.139` | 2026-07-29T01:15:34 |
| `git` | `git123` | `193.32.162.15` | 2026-07-29T01:16:42 |
| `root` | `111111` | `80.94.92.55` | 2026-07-29T01:17:05 |
| `git` | `github` | `193.32.162.15` | 2026-07-29T01:18:05 |
| `root` | `kedacom` | `85.198.19.242` | 2026-07-29T01:18:21 |
| `support` | `777` | `196.188.187.85` | 2026-07-29T01:18:24 |
| `345gs5662d34` | `345gs5662d34` | `85.198.19.242` | 2026-07-29T01:18:25 |
| `root` | `3245gs5662d34` | `85.198.19.242` | 2026-07-29T01:18:27 |
| `support` | `777` | `103.174.80.40` | 2026-07-29T01:18:31 |
| `git` | `qwerty` | `193.32.162.15` | 2026-07-29T01:19:30 |
| `root` | `123123Aa` | `14.103.117.81` | 2026-07-29T01:19:31 |
| `345gs5662d34` | `345gs5662d34` | `14.103.117.81` | 2026-07-29T01:19:36 |
| `root` | `123123` | `80.94.92.55` | 2026-07-29T01:19:36 |
| `root` | `3245gs5662d34` | `14.103.117.81` | 2026-07-29T01:19:39 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-29T01:20:15 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-29T01:20:15 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-29T01:20:24 |
| `git` | `git@123` | `193.32.162.15` | 2026-07-29T01:20:56 |
| `centos` | `5555` | `120.234.232.184` | 2026-07-29T01:21:20 |
| `root` | `1234` | `80.94.92.55` | 2026-07-29T01:22:03 |
| `git` | `Git123` | `193.32.162.15` | 2026-07-29T01:22:24 |
| `git` | `admin` | `193.32.162.15` | 2026-07-29T01:23:49 |
| `root` | `12345` | `80.94.92.55` | 2026-07-29T01:24:17 |
| `jenkins` | `jenkins` | `193.32.162.15` | 2026-07-29T01:25:17 |
| `jenkins` | `password` | `193.32.162.15` | 2026-07-29T01:26:48 |
| `root` | `12345678` | `80.94.92.55` | 2026-07-29T01:27:05 |
| `user` | `5` | `223.107.146.186` | 2026-07-29T01:27:52 |
| `user` | `5` | `112.120.115.152` | 2026-07-29T01:28:01 |
| `jenkins` | `123456` | `193.32.162.15` | 2026-07-29T01:28:21 |
| `root` | `123456789` | `80.94.92.55` | 2026-07-29T01:28:38 |
| `jenkins` | `admin` | `193.32.162.15` | 2026-07-29T01:29:50 |
| `root` | `Password1` | `80.94.92.55` | 2026-07-29T01:30:26 |
| `user` | `5` | `116.114.84.246` | 2026-07-29T01:31:02 |
| `user` | `5` | `182.135.63.175` | 2026-07-29T01:31:12 |
| `jenkins` | `qwerty` | `193.32.162.15` | 2026-07-29T01:31:16 |
| `user` | `5` | `10.0.0.73` | 2026-07-29T01:31:30 |
| `root` | `admin` | `80.94.92.55` | 2026-07-29T01:32:19 |
| `jenkins` | `jenkins123` | `193.32.162.15` | 2026-07-29T01:32:40 |
| `jenkins` | `jenkins@123` | `193.32.162.15` | 2026-07-29T01:34:01 |
| `root` | `admin123` | `80.94.92.55` | 2026-07-29T01:34:04 |
| `jenkins` | `Jenkins123` | `193.32.162.15` | 2026-07-29T01:35:23 |
| `root` | `default` | `80.94.92.55` | 2026-07-29T01:35:43 |
| `jenkins` | `deploy` | `193.32.162.15` | 2026-07-29T01:36:44 |
| `root` | `letmein` | `80.94.92.55` | 2026-07-29T01:37:40 |
| `vagrant` | `vagrant` | `193.32.162.15` | 2026-07-29T01:38:06 |
| `vagrant` | `password` | `193.32.162.15` | 2026-07-29T01:39:28 |
| `root` | `passw0rd` | `80.94.92.55` | 2026-07-29T01:40:14 |
| `vagrant` | `123456` | `193.32.162.15` | 2026-07-29T01:40:51 |
| `vagrant` | `qwerty` | `193.32.162.15` | 2026-07-29T01:42:15 |
| `ubuntu` | `admin` | `94.200.95.18` | 2026-07-29T01:42:24 |
| `root` | `password` | `80.94.92.55` | 2026-07-29T01:42:28 |
| `ubuntu` | `admin` | `61.12.84.172` | 2026-07-29T01:42:31 |
| `user` | `55` | `10.0.0.73` | 2026-07-29T01:43:02 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-29T01:43:24 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-29T01:43:24 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-29T01:43:30 |
| `vagrant` | `vagrant123` | `193.32.162.15` | 2026-07-29T01:43:40 |
| `root` | `qwerty` | `80.94.92.55` | 2026-07-29T01:44:20 |
| `vagrant` | `vm` | `193.32.162.15` | 2026-07-29T01:45:04 |
| `root` | `` | `94.154.43.92` | 2026-07-29T01:45:07 |
| `ubuntu` | `admin` | `10.0.0.73` | 2026-07-29T01:46:09 |
| `vagrant` | `box` | `193.32.162.15` | 2026-07-29T01:46:28 |
| `root` | `system` | `80.94.92.55` | 2026-07-29T01:46:37 |
| `root` | `toor` | `80.94.92.55` | 2026-07-29T01:47:37 |
| `vagrant` | `deploy` | `193.32.162.15` | 2026-07-29T01:47:51 |
| `support` | `support` | `10.0.0.73` | 2026-07-29T01:48:39 |
| `admin` | `111111` | `80.94.92.55` | 2026-07-29T01:48:42 |
| `vagrant` | `admin` | `193.32.162.15` | 2026-07-29T01:49:12 |
| `admin` | `123123` | `80.94.92.55` | 2026-07-29T01:50:13 |
| `docker` | `docker` | `193.32.162.15` | 2026-07-29T01:50:33 |
| `admin` | `1234` | `80.94.92.55` | 2026-07-29T01:51:18 |
| `docker` | `password` | `193.32.162.15` | 2026-07-29T01:51:57 |
| `centos` | `111` | `220.178.39.106` | 2026-07-29T01:52:14 |
| `admin` | `12345` | `80.94.92.55` | 2026-07-29T01:52:16 |
| `admin` | `123456` | `80.94.92.55` | 2026-07-29T01:53:07 |
| `docker` | `123456` | `193.32.162.15` | 2026-07-29T01:53:22 |
| `admin` | `12345678` | `80.94.92.55` | 2026-07-29T01:53:56 |
| `docker` | `qwerty` | `193.32.162.15` | 2026-07-29T01:54:43 |
| `admin` | `123456789` | `80.94.92.55` | 2026-07-29T01:54:47 |
| `centos` | `111` | `218.202.143.68` | 2026-07-29T01:55:40 |
| `admin` | `Administrator` | `80.94.92.55` | 2026-07-29T01:55:45 |
| `docker` | `docker123` | `193.32.162.15` | 2026-07-29T01:56:06 |
| `admin` | `access` | `80.94.92.55` | 2026-07-29T01:56:43 |
| `admin` | `admin` | `80.94.92.55` | 2026-07-29T01:57:26 |
| `docker` | `admin` | `193.32.162.15` | 2026-07-29T01:57:31 |
| `admin` | `admin123` | `80.94.92.55` | 2026-07-29T01:58:19 |
| `docker` | `container` | `193.32.162.15` | 2026-07-29T01:58:54 |
| `docker` | `deploy` | `193.32.162.15` | 2026-07-29T02:00:15 |
| `docker` | `root` | `193.32.162.15` | 2026-07-29T02:01:37 |
| `www` | `www` | `193.32.162.15` | 2026-07-29T02:02:59 |
| `www` | `password` | `193.32.162.15` | 2026-07-29T02:04:22 |
| `www` | `123456` | `193.32.162.15` | 2026-07-29T02:05:45 |
| `guest` | `22222` | `27.223.98.117` | 2026-07-29T02:06:35 |
| `guest` | `22222` | `182.76.71.82` | 2026-07-29T02:06:48 |
| `www` | `qwerty` | `193.32.162.15` | 2026-07-29T02:07:12 |
| `guest` | `9999` | `10.0.0.73` | 2026-07-29T02:07:23 |
| `support` | `support` | `176.53.159.196` | 2026-07-29T02:08:33 |
| `www` | `admin` | `193.32.162.15` | 2026-07-29T02:08:36 |
| `guest` | `22222` | `117.247.77.115` | 2026-07-29T02:09:56 |
| `www` | `www123` | `193.32.162.15` | 2026-07-29T02:10:02 |
| `guest` | `22222` | `190.57.233.133` | 2026-07-29T02:10:05 |
| `www` | `web` | `193.32.162.15` | 2026-07-29T02:11:30 |
| `www` | `host` | `193.32.162.15` | 2026-07-29T02:12:56 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-29T02:13:47 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-29T02:13:48 |
| `www` | `server` | `193.32.162.15` | 2026-07-29T02:14:19 |
| `www-data` | `www-data` | `193.32.162.15` | 2026-07-29T02:15:43 |
| `www-data` | `password` | `193.32.162.15` | 2026-07-29T02:17:08 |
| `www-data` | `123456` | `193.32.162.15` | 2026-07-29T02:18:32 |
| `www-data` | `qwerty` | `193.32.162.15` | 2026-07-29T02:19:55 |
| `www-data` | `admin` | `193.32.162.15` | 2026-07-29T02:21:20 |
| `www-data` | `web` | `193.32.162.15` | 2026-07-29T02:22:48 |
| `www-data` | `server` | `193.32.162.15` | 2026-07-29T02:24:13 |
| `www-data` | `apache` | `193.32.162.15` | 2026-07-29T02:25:38 |
| `www-data` | `nginx` | `193.32.162.15` | 2026-07-29T02:27:02 |
| `backup` | `backup` | `193.32.162.15` | 2026-07-29T02:28:24 |
| `backup` | `password` | `193.32.162.15` | 2026-07-29T02:29:48 |
| `backup` | `123456` | `193.32.162.15` | 2026-07-29T02:31:11 |
| `oracle` | `123abc` | `176.170.1.244` | 2026-07-29T02:31:11 |
| `oracle` | `123abc` | `103.120.116.162` | 2026-07-29T02:31:20 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.195.127.65` | 2026-07-29T02:32:35 |
| `backup` | `qwerty` | `193.32.162.15` | 2026-07-29T02:32:36 |
| `*1` | `$4` | `35.195.127.65` | 2026-07-29T02:32:43 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 9070` | `35.195.127.65` | 2026-07-29T02:32:45 |
| `backup` | `backup123` | `193.32.162.15` | 2026-07-29T02:33:55 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `65.49.20.69` | 2026-07-29T02:34:17 |
| `backup` | `admin` | `193.32.162.15` | 2026-07-29T02:35:17 |
| `backup` | `restore` | `193.32.162.15` | 2026-07-29T02:36:40 |
| `backup` | `data` | `193.32.162.15` | 2026-07-29T02:38:04 |
| `backup` | `server` | `193.32.162.15` | 2026-07-29T02:39:30 |
| `ubnt` | `44` | `75.80.65.214` | 2026-07-29T02:40:51 |
| `support` | `support` | `193.32.162.15` | 2026-07-29T02:40:58 |
| `ubnt` | `44` | `125.19.244.62` | 2026-07-29T02:40:59 |
| `support` | `password` | `193.32.162.15` | 2026-07-29T02:42:27 |
| `support` | `123456` | `193.32.162.15` | 2026-07-29T02:43:54 |
| `ubnt` | `44` | `60.173.105.206` | 2026-07-29T02:44:18 |
| `ubnt` | `44` | `24.97.253.246` | 2026-07-29T02:44:25 |
| `ubnt` | `44` | `10.0.0.73` | 2026-07-29T02:44:36 |
| `support` | `qwerty` | `193.32.162.15` | 2026-07-29T02:45:19 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.195.144.153` | 2026-07-29T02:46:39 |
| `support` | `help` | `193.32.162.15` | 2026-07-29T02:46:44 |
| `*1` | `$4` | `35.195.144.153` | 2026-07-29T02:46:52 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 3630` | `35.195.144.153` | 2026-07-29T02:46:54 |
| `support` | `admin` | `193.32.162.15` | 2026-07-29T02:48:09 |
| `support` | `tech` | `193.32.162.15` | 2026-07-29T02:49:34 |
| `support` | `user` | `193.32.162.15` | 2026-07-29T02:50:58 |
| `support` | `pass` | `193.32.162.15` | 2026-07-29T02:52:23 |
| `user` | `88888` | `187.126.105.42` | 2026-07-29T02:52:26 |
| `user` | `88888` | `182.73.164.228` | 2026-07-29T02:52:34 |
| `developer` | `developer` | `193.32.162.15` | 2026-07-29T02:53:49 |
| `developer` | `password` | `193.32.162.15` | 2026-07-29T02:55:13 |
| `nobody` | `4444` | `65.20.233.110` | 2026-07-29T02:55:28 |
| `nobody` | `4444` | `138.118.213.68` | 2026-07-29T02:55:36 |
| `user` | `88888` | `10.0.0.73` | 2026-07-29T02:56:05 |
| `developer` | `123456` | `193.32.162.15` | 2026-07-29T02:56:37 |
| `developer` | `qwerty` | `193.32.162.15` | 2026-07-29T02:58:01 |
| `nobody` | `4444` | `223.107.72.234` | 2026-07-29T02:58:37 |
| `nobody` | `4444` | `10.0.0.73` | 2026-07-29T02:59:07 |
| `developer` | `dev` | `193.32.162.15` | 2026-07-29T02:59:23 |
| `developer` | `admin` | `193.32.162.15` | 2026-07-29T03:00:44 |
| `root` | `` | `91.92.40.18` | 2026-07-29T03:01:36 |
| `developer` | `code` | `193.32.162.15` | 2026-07-29T03:02:07 |
| `developer` | `deploy` | `193.32.162.15` | 2026-07-29T03:03:28 |
| `developer` | `git` | `193.32.162.15` | 2026-07-29T03:04:49 |
| `root` | `5555555` | `210.13.99.66` | 2026-07-29T03:05:19 |
| `root` | `5555555` | `103.93.37.178` | 2026-07-29T03:05:28 |
| `webadmin` | `webadmin` | `193.32.162.15` | 2026-07-29T03:06:08 |
| `webadmin` | `password` | `193.32.162.15` | 2026-07-29T03:07:29 |
| `root` | `5555555` | `111.70.32.179` | 2026-07-29T03:08:46 |
| `webadmin` | `123456` | `193.32.162.15` | 2026-07-29T03:08:52 |
| `root` | `5555555` | `65.20.237.119` | 2026-07-29T03:08:55 |
| `root` | `5555555` | `10.0.0.73` | 2026-07-29T03:09:10 |
| `root` | `000000` | `92.118.39.71` | 2026-07-29T03:09:42 |
| `webadmin` | `qwerty` | `193.32.162.15` | 2026-07-29T03:10:15 |
| `root` | `LeitboGi0ro` | `158.178.141.210` | 2026-07-29T03:11:19 |
| `root` | `123@@@` | `158.178.141.210` | 2026-07-29T03:11:19 |
| `webadmin` | `admin` | `193.32.162.15` | 2026-07-29T03:11:36 |
| `root` | `111111` | `92.118.39.71` | 2026-07-29T03:12:10 |
| `webadmin` | `web` | `193.32.162.15` | 2026-07-29T03:12:52 |
| `admin` | `admin` | `47.252.16.44` | 2026-07-29T03:13:21 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-29T03:13:21 |
| `webadmin` | `server` | `193.32.162.15` | 2026-07-29T03:14:09 |
| `root` | `123` | `92.118.39.71` | 2026-07-29T03:14:33 |
| `webadmin` | `root` | `193.32.162.15` | 2026-07-29T03:15:27 |
| `webadmin` | `P@ssw0rd` | `193.32.162.15` | 2026-07-29T03:16:44 |
| `root` | `123123` | `92.118.39.71` | 2026-07-29T03:16:47 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.156.227.119` | 2026-07-29T03:17:41 |
| `*1` | `$4` | `34.156.227.119` | 2026-07-29T03:17:54 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 1594` | `34.156.227.119` | 2026-07-29T03:17:56 |
| `newuser` | `newuser` | `193.32.162.15` | 2026-07-29T03:18:03 |
| `root` | `1234` | `92.118.39.71` | 2026-07-29T03:18:47 |
| `newuser` | `password` | `193.32.162.15` | 2026-07-29T03:19:23 |
| `root` | `7777` | `93.177.157.179` | 2026-07-29T03:20:03 |
| `root` | `7777` | `111.70.23.236` | 2026-07-29T03:20:12 |
| `root` | `7777` | `10.0.0.73` | 2026-07-29T03:20:29 |
| `newuser` | `123456` | `193.32.162.15` | 2026-07-29T03:20:44 |
| `root` | `12345` | `92.118.39.71` | 2026-07-29T03:20:45 |
| `newuser` | `qwerty` | `193.32.162.15` | 2026-07-29T03:22:07 |
| `root` | `qwedsa` | `112.197.2.116` | 2026-07-29T03:22:22 |
| `newuser` | `welcome` | `193.32.162.15` | 2026-07-29T03:23:32 |
| `root` | `12345678` | `92.118.39.71` | 2026-07-29T03:24:37 |
| `newuser` | `user` | `193.32.162.15` | 2026-07-29T03:24:56 |
| `root` | `123456789` | `92.118.39.71` | 2026-07-29T03:26:20 |
| `newuser` | `pass` | `193.32.162.15` | 2026-07-29T03:26:21 |
| `newuser` | `temp` | `193.32.162.15` | 2026-07-29T03:27:48 |
| `root` | `1q2w3e4r` | `92.118.39.71` | 2026-07-29T03:28:08 |
| `newuser` | `changeme` | `193.32.162.15` | 2026-07-29T03:29:13 |
| `debian` | `7777777` | `121.159.71.249` | 2026-07-29T03:29:52 |
| `root` | `654321` | `92.118.39.71` | 2026-07-29T03:29:59 |
| `administrator` | `administrator` | `193.32.162.15` | 2026-07-29T03:30:38 |
| `root` | `P@ssw0rd` | `92.118.39.71` | 2026-07-29T03:31:52 |
| `administrator` | `password` | `193.32.162.15` | 2026-07-29T03:32:00 |
| `debian` | `7777777` | `103.174.80.40` | 2026-07-29T03:33:09 |
| `debian` | `7777777` | `82.65.140.218` | 2026-07-29T03:33:16 |
| `administrator` | `123456` | `193.32.162.15` | 2026-07-29T03:33:20 |
| `root` | `admin` | `92.118.39.71` | 2026-07-29T03:33:38 |
| `administrator` | `qwerty` | `193.32.162.15` | 2026-07-29T03:34:42 |
| `root` | `admin123` | `92.118.39.71` | 2026-07-29T03:35:27 |
| `administrator` | `admin` | `193.32.162.15` | 2026-07-29T03:36:05 |
| `root` | `passw0rd` | `92.118.39.71` | 2026-07-29T03:37:18 |
| `administrator` | `P@ssw0rd` | `193.32.162.15` | 2026-07-29T03:37:28 |
| `administrator` | `welcome` | `193.32.162.15` | 2026-07-29T03:38:50 |
| `root` | `password` | `92.118.39.71` | 2026-07-29T03:39:08 |
| `administrator` | `pass` | `193.32.162.15` | 2026-07-29T03:40:13 |
| `root` | `password1` | `92.118.39.71` | 2026-07-29T03:40:56 |
| `debian` | `debian999` | `111.70.32.51` | 2026-07-29T03:41:11 |
| `administrator` | `root` | `193.32.162.15` | 2026-07-29T03:41:35 |
| `root` | `qwerty` | `92.118.39.71` | 2026-07-29T03:42:52 |
| `ssh` | `ssh` | `193.32.162.15` | 2026-07-29T03:42:59 |
| `ssh` | `password` | `193.32.162.15` | 2026-07-29T03:44:19 |
| `root` | `root123` | `92.118.39.71` | 2026-07-29T03:44:32 |
| `debian` | `debian999` | `10.0.0.73` | 2026-07-29T03:44:40 |
| `ssh` | `123456` | `193.32.162.15` | 2026-07-29T03:45:43 |
| `root` | `toor` | `92.118.39.71` | 2026-07-29T03:46:29 |
| `ssh` | `qwerty` | `193.32.162.15` | 2026-07-29T03:47:10 |
| `default` | `1111` | `106.201.230.195` | 2026-07-29T03:47:24 |
| `default` | `1111` | `10.0.0.73` | 2026-07-29T03:47:50 |
| `ssh` | `secure` | `193.32.162.15` | 2026-07-29T03:48:36 |
| `ssh` | `admin` | `193.32.162.15` | 2026-07-29T03:50:03 |
| `admin` | `000000` | `92.118.39.71` | 2026-07-29T03:50:15 |
| `ssh` | `server` | `193.32.162.15` | 2026-07-29T03:51:33 |
| `ssh` | `connect` | `193.32.162.15` | 2026-07-29T03:53:02 |
| `oracle` | `123123123` | `201.28.237.90` | 2026-07-29T03:54:12 |
| `oracle` | `123123123` | `85.19.195.12` | 2026-07-29T03:54:18 |
| `ssh` | `login` | `193.32.162.15` | 2026-07-29T03:54:31 |
| `admin` | `111111` | `92.118.39.71` | 2026-07-29T03:54:34 |
| `sysadmin` | `sysadmin` | `193.32.162.15` | 2026-07-29T03:55:57 |
| `admin` | `123` | `92.118.39.71` | 2026-07-29T03:57:10 |
| `sysadmin` | `password` | `193.32.162.15` | 2026-07-29T03:57:26 |
| `oracle` | `123123123` | `220.74.119.84` | 2026-07-29T03:57:40 |
| `oracle` | `123123123` | `60.174.35.18` | 2026-07-29T03:57:50 |
| `oracle` | `123123123` | `10.0.0.73` | 2026-07-29T03:57:59 |
| `sysadmin` | `123456` | `193.32.162.15` | 2026-07-29T03:58:50 |
| `admin` | `123123` | `92.118.39.71` | 2026-07-29T03:59:53 |
| `sysadmin` | `qwerty` | `193.32.162.15` | 2026-07-29T04:00:10 |
| `sysadmin` | `admin` | `193.32.162.15` | 2026-07-29T04:01:31 |
| `admin` | `1234` | `92.118.39.71` | 2026-07-29T04:02:03 |
| `sysadmin` | `root` | `193.32.162.15` | 2026-07-29T04:02:51 |
| `sysadmin` | `P@ssw0rd` | `193.32.162.15` | 2026-07-29T04:04:10 |
| `sysadmin` | `server` | `193.32.162.15` | 2026-07-29T04:05:33 |
| `sysadmin` | `deploy` | `193.32.162.15` | 2026-07-29T04:06:56 |
| `admin` | `12345` | `92.118.39.71` | 2026-07-29T04:07:34 |
| `info` | `info` | `193.32.162.15` | 2026-07-29T04:08:17 |
| `oracle` | `Passw0rd` | `178.178.222.59` | 2026-07-29T04:08:31 |
| `Default` | `123456789` | `1.212.225.99` | 2026-07-29T04:08:48 |
| `Default` | `123456789` | `182.73.164.228` | 2026-07-29T04:08:57 |
| `info` | `password` | `193.32.162.15` | 2026-07-29T04:09:38 |
| `info` | `123456` | `193.32.162.15` | 2026-07-29T04:10:56 |
| `oracle` | `Passw0rd` | `58.17.128.7` | 2026-07-29T04:11:58 |
| `oracle` | `Passw0rd` | `125.20.207.154` | 2026-07-29T04:12:13 |
| `info` | `qwerty` | `193.32.162.15` | 2026-07-29T04:12:15 |
| `oracle` | `Passw0rd` | `10.0.0.73` | 2026-07-29T04:12:26 |
| `info` | `admin` | `193.32.162.15` | 2026-07-29T04:13:35 |
| `info` | `welcome` | `193.32.162.15` | 2026-07-29T04:14:55 |
| `info` | `data` | `193.32.162.15` | 2026-07-29T04:16:16 |
| `info` | `contact` | `193.32.162.15` | 2026-07-29T04:17:38 |
| `admin` | `123456` | `92.118.39.71` | 2026-07-29T04:18:11 |
| `guest` | `guest555` | `177.174.89.99` | 2026-07-29T04:18:44 |
| `guest` | `guest555` | `117.211.15.106` | 2026-07-29T04:18:57 |
| `info` | `pass` | `193.32.162.15` | 2026-07-29T04:19:01 |
| `guest` | `guest555` | `10.0.0.73` | 2026-07-29T04:22:20 |
| `admin` | `1234567` | `92.118.39.71` | 2026-07-29T04:22:36 |
| `postgres` | `maintenance` | `195.222.57.190` | 2026-07-29T04:29:52 |
| `root` | `syncmaster` | `103.84.236.222` | 2026-07-29T04:29:53 |
| `345gs5662d34` | `345gs5662d34` | `103.84.236.222` | 2026-07-29T04:29:58 |
| `root` | `3245gs5662d34` | `103.84.236.222` | 2026-07-29T04:30:00 |
| `postgres` | `maintenance` | `65.20.131.63` | 2026-07-29T04:30:03 |
| `postgres` | `p@ssword` | `88.84.209.146` | 2026-07-29T04:33:06 |
| `postgres` | `maintenance` | `117.34.210.196` | 2026-07-29T04:33:12 |
| `postgres` | `p@ssword` | `49.124.152.235` | 2026-07-29T04:33:15 |
| `postgres` | `maintenance` | `93.241.232.14` | 2026-07-29T04:33:19 |
| `pi` | `112233` | `10.0.0.73` | 2026-07-29T04:46:55 |
| `admin` | `admin` | `120.48.144.5` | 2026-07-29T04:50:01 |
| `guest` | `44444` | `111.70.32.179` | 2026-07-29T04:54:12 |
| `guest` | `44444` | `175.198.18.3` | 2026-07-29T04:54:21 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **590** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 214 |
| OpenSSH | 63 |
| libssh | 26 |
| Paramiko (Python) | 18 |
| AsyncSSH (Python) | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 205 | 3 |
| `acaa53e0a7d7...` | Mirai/variant | 61 | 58 |
| `a2de0f306611...` | Mirai/variant | 14 | 3 |
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `fda360b1b4f4...` | Mirai/variant | 4 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 205 | 3 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 61 | 58 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 14 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 13 | 5 | — |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 4 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **10** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1059.004, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 201 | 3 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 2 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo WRITABLE >/tmp/.testfile 2>&1
```
```
ls -l /tmp/.testfile 2>&1
```
```
rm -f /tmp/.testfile
```
```
cd /tmp
```
```
for pid in /proc/[0-9]*; do pid_num="${pid##*/}"; if [ -r "$pid/maps" ]; then suspicious=true; while IFS= read -r line; do case "$line" in *"/lib/"*|*"/lib64/"*|*".so"*) suspicious=false; break;; esac; done < "$pid/maps"; if [ "$suspicious" = true ]; then kill -9 "$pid_num" 2>/dev/null; fi; fi; done;
```
Source IPs: `91.92.40.18`

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
Source IPs: `92.118.39.71`, `193.32.162.15`, `80.94.92.55`

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
Source IPs: `94.154.43.144`, `94.154.43.92`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **161** |
| Unique ASNs | **95** |
| High-Risk ASNs | **83** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 9 | HIGH |
| `AS22773` | Cox Communications Inc. | 8 | MEDIUM |
| `AS46562` | Performive LLC | 8 | LOW |
| `AS25369` | Hydra Communications Ltd | 6 | HIGH |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 4 | HIGH |
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (318)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8925332a3430

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 00:55 |
| **Last Seen** | 2026-07-29 00:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 00:55:56` | `cowrie.session.connect` |
| `2026-07-29 00:55:57` | `cowrie.client.version` |
| `2026-07-29 00:55:57` | `cowrie.client.kex` |
| `2026-07-29 00:55:59` | `cowrie.login.success` |
| `2026-07-29 00:56:00` | `cowrie.session.params` |
| `2026-07-29 00:56:00` | `cowrie.command.input` |
| `2026-07-29 00:56:00` | `cowrie.command.input` |
| `2026-07-29 00:56:00` | `cowrie.command.input` |
| `2026-07-29 00:56:00` | `cowrie.command.input` |
| `2026-07-29 00:56:00` | `cowrie.command.input` |
| `2026-07-29 00:56:00` | `cowrie.command.success` |
| `2026-07-29 00:56:00` | `cowrie.command.input` |
| `2026-07-29 00:56:00` | `cowrie.command.input` |
| `2026-07-29 00:56:00` | `cowrie.command.input` |
| `2026-07-29 00:56:00` | `cowrie.command.input` |
| `2026-07-29 00:56:01` | `cowrie.log.closed` |
| `2026-07-29 00:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a12c1f3f321f

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]82` |
| **First Seen** | 2026-07-29 00:56 |
| **Last Seen** | 2026-07-29 00:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 00:56:55` | `cowrie.session.connect` |
| `2026-07-29 00:56:55` | `cowrie.client.version` |
| `2026-07-29 00:56:55` | `cowrie.client.kex` |
| `2026-07-29 00:56:58` | `cowrie.login.success` |
| `2026-07-29 00:56:59` | `cowrie.direct-tcpip.request` |
| `2026-07-29 00:57:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]82` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c87b7cd25b28

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 00:57 |
| **Last Seen** | 2026-07-29 00:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 00:57:16` | `cowrie.session.connect` |
| `2026-07-29 00:57:17` | `cowrie.client.version` |
| `2026-07-29 00:57:17` | `cowrie.client.kex` |
| `2026-07-29 00:57:18` | `cowrie.login.success` |
| `2026-07-29 00:57:20` | `cowrie.session.params` |
| `2026-07-29 00:57:20` | `cowrie.command.input` |
| `2026-07-29 00:57:20` | `cowrie.command.input` |
| `2026-07-29 00:57:20` | `cowrie.command.input` |
| `2026-07-29 00:57:20` | `cowrie.command.input` |
| `2026-07-29 00:57:20` | `cowrie.command.input` |
| `2026-07-29 00:57:20` | `cowrie.command.success` |
| `2026-07-29 00:57:20` | `cowrie.command.input` |
| `2026-07-29 00:57:20` | `cowrie.command.input` |
| `2026-07-29 00:57:20` | `cowrie.command.input` |
| `2026-07-29 00:57:20` | `cowrie.command.input` |
| `2026-07-29 00:57:20` | `cowrie.log.closed` |
| `2026-07-29 00:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bfcf9b026f8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 00:58 |
| **Last Seen** | 2026-07-29 00:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 00:58:38` | `cowrie.session.connect` |
| `2026-07-29 00:58:38` | `cowrie.client.version` |
| `2026-07-29 00:58:38` | `cowrie.client.kex` |
| `2026-07-29 00:58:40` | `cowrie.login.success` |
| `2026-07-29 00:58:41` | `cowrie.session.params` |
| `2026-07-29 00:58:41` | `cowrie.command.input` |
| `2026-07-29 00:58:41` | `cowrie.command.input` |
| `2026-07-29 00:58:41` | `cowrie.command.input` |
| `2026-07-29 00:58:41` | `cowrie.command.input` |
| `2026-07-29 00:58:41` | `cowrie.command.input` |
| `2026-07-29 00:58:41` | `cowrie.command.success` |
| `2026-07-29 00:58:41` | `cowrie.command.input` |
| `2026-07-29 00:58:41` | `cowrie.command.input` |
| `2026-07-29 00:58:41` | `cowrie.command.input` |
| `2026-07-29 00:58:41` | `cowrie.command.input` |
| `2026-07-29 00:58:41` | `cowrie.log.closed` |
| `2026-07-29 00:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fabab8f4afa0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:00 |
| **Last Seen** | 2026-07-29 01:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:00:00` | `cowrie.session.connect` |
| `2026-07-29 01:00:01` | `cowrie.client.version` |
| `2026-07-29 01:00:01` | `cowrie.client.kex` |
| `2026-07-29 01:00:03` | `cowrie.login.success` |
| `2026-07-29 01:00:04` | `cowrie.session.params` |
| `2026-07-29 01:00:04` | `cowrie.command.input` |
| `2026-07-29 01:00:04` | `cowrie.command.input` |
| `2026-07-29 01:00:04` | `cowrie.command.input` |
| `2026-07-29 01:00:04` | `cowrie.command.input` |
| `2026-07-29 01:00:04` | `cowrie.command.input` |
| `2026-07-29 01:00:04` | `cowrie.command.success` |
| `2026-07-29 01:00:04` | `cowrie.command.input` |
| `2026-07-29 01:00:04` | `cowrie.command.input` |
| `2026-07-29 01:00:04` | `cowrie.command.input` |
| `2026-07-29 01:00:04` | `cowrie.command.input` |
| `2026-07-29 01:00:05` | `cowrie.log.closed` |
| `2026-07-29 01:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adeaced0a0a0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:01 |
| **Last Seen** | 2026-07-29 01:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:01:25` | `cowrie.session.connect` |
| `2026-07-29 01:01:25` | `cowrie.client.version` |
| `2026-07-29 01:01:25` | `cowrie.client.kex` |
| `2026-07-29 01:01:27` | `cowrie.login.success` |
| `2026-07-29 01:01:29` | `cowrie.session.params` |
| `2026-07-29 01:01:29` | `cowrie.command.input` |
| `2026-07-29 01:01:29` | `cowrie.command.input` |
| `2026-07-29 01:01:29` | `cowrie.command.input` |
| `2026-07-29 01:01:29` | `cowrie.command.input` |
| `2026-07-29 01:01:29` | `cowrie.command.input` |
| `2026-07-29 01:01:29` | `cowrie.command.success` |
| `2026-07-29 01:01:29` | `cowrie.command.input` |
| `2026-07-29 01:01:29` | `cowrie.command.input` |
| `2026-07-29 01:01:29` | `cowrie.command.input` |
| `2026-07-29 01:01:29` | `cowrie.command.input` |
| `2026-07-29 01:01:30` | `cowrie.log.closed` |
| `2026-07-29 01:01:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-921a9e4a78aa

| Field | Detail |
|---|---|
| **Source IP** | `171.231.196[.]169` |
| **First Seen** | 2026-07-29 01:01 |
| **Last Seen** | 2026-07-29 01:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:01:46` | `cowrie.session.connect` |
| `2026-07-29 01:01:47` | `cowrie.client.version` |
| `2026-07-29 01:01:47` | `cowrie.client.kex` |
| `2026-07-29 01:01:52` | `cowrie.login.success` |
| `2026-07-29 01:01:52` | `cowrie.direct-tcpip.request` |
| `2026-07-29 01:01:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 01:01:53` | `cowrie.direct-tcpip.data` |
| `2026-07-29 01:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.196[.]169` to AbuseIPDB if not already reported
- [ ] Block `171.231.196[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de297b359a8a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:02 |
| **Last Seen** | 2026-07-29 01:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:02:48` | `cowrie.session.connect` |
| `2026-07-29 01:02:49` | `cowrie.client.version` |
| `2026-07-29 01:02:49` | `cowrie.client.kex` |
| `2026-07-29 01:02:50` | `cowrie.login.success` |
| `2026-07-29 01:02:52` | `cowrie.session.params` |
| `2026-07-29 01:02:52` | `cowrie.command.input` |
| `2026-07-29 01:02:52` | `cowrie.command.input` |
| `2026-07-29 01:02:52` | `cowrie.command.input` |
| `2026-07-29 01:02:52` | `cowrie.command.input` |
| `2026-07-29 01:02:52` | `cowrie.command.input` |
| `2026-07-29 01:02:52` | `cowrie.command.success` |
| `2026-07-29 01:02:52` | `cowrie.command.input` |
| `2026-07-29 01:02:52` | `cowrie.command.input` |
| `2026-07-29 01:02:52` | `cowrie.command.input` |
| `2026-07-29 01:02:52` | `cowrie.command.input` |
| `2026-07-29 01:02:52` | `cowrie.log.closed` |
| `2026-07-29 01:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22a51bc4ab42

| Field | Detail |
|---|---|
| **Source IP** | `200.89.159[.]59` |
| **First Seen** | 2026-07-29 01:03 |
| **Last Seen** | 2026-07-29 01:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:03:28` | `cowrie.session.connect` |
| `2026-07-29 01:03:29` | `cowrie.client.version` |
| `2026-07-29 01:03:29` | `cowrie.client.kex` |
| `2026-07-29 01:03:30` | `cowrie.login.success` |
| `2026-07-29 01:03:31` | `cowrie.direct-tcpip.request` |
| `2026-07-29 01:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.89.159[.]59` to AbuseIPDB if not already reported
- [ ] Block `200.89.159[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db764031d6f9

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-07-29 01:03 |
| **Last Seen** | 2026-07-29 01:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:03:40` | `cowrie.session.connect` |
| `2026-07-29 01:03:40` | `cowrie.client.version` |
| `2026-07-29 01:03:40` | `cowrie.client.kex` |
| `2026-07-29 01:03:42` | `cowrie.login.success` |
| `2026-07-29 01:03:42` | `cowrie.direct-tcpip.request` |
| `2026-07-29 01:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2add6ba26c2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:04 |
| **Last Seen** | 2026-07-29 01:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:04:11` | `cowrie.session.connect` |
| `2026-07-29 01:04:11` | `cowrie.client.version` |
| `2026-07-29 01:04:11` | `cowrie.client.kex` |
| `2026-07-29 01:04:13` | `cowrie.login.success` |
| `2026-07-29 01:04:14` | `cowrie.session.params` |
| `2026-07-29 01:04:14` | `cowrie.command.input` |
| `2026-07-29 01:04:14` | `cowrie.command.input` |
| `2026-07-29 01:04:14` | `cowrie.command.input` |
| `2026-07-29 01:04:14` | `cowrie.command.input` |
| `2026-07-29 01:04:14` | `cowrie.command.input` |
| `2026-07-29 01:04:14` | `cowrie.command.success` |
| `2026-07-29 01:04:14` | `cowrie.command.input` |
| `2026-07-29 01:04:14` | `cowrie.command.input` |
| `2026-07-29 01:04:14` | `cowrie.command.input` |
| `2026-07-29 01:04:14` | `cowrie.command.input` |
| `2026-07-29 01:04:15` | `cowrie.log.closed` |
| `2026-07-29 01:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cf2deadbe20

| Field | Detail |
|---|---|
| **Source IP** | `171.231.177[.]152` |
| **First Seen** | 2026-07-29 01:05 |
| **Last Seen** | 2026-07-29 01:06 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:05:31` | `cowrie.session.connect` |
| `2026-07-29 01:05:31` | `cowrie.client.version` |
| `2026-07-29 01:05:33` | `cowrie.client.kex` |
| `2026-07-29 01:05:58` | `cowrie.login.success` |
| `2026-07-29 01:06:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.177[.]152` to AbuseIPDB if not already reported
- [ ] Block `171.231.177[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e201b1a061a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:05 |
| **Last Seen** | 2026-07-29 01:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:05:34` | `cowrie.session.connect` |
| `2026-07-29 01:05:35` | `cowrie.client.version` |
| `2026-07-29 01:05:35` | `cowrie.client.kex` |
| `2026-07-29 01:05:36` | `cowrie.login.success` |
| `2026-07-29 01:05:38` | `cowrie.session.params` |
| `2026-07-29 01:05:38` | `cowrie.command.input` |
| `2026-07-29 01:05:38` | `cowrie.command.input` |
| `2026-07-29 01:05:38` | `cowrie.command.input` |
| `2026-07-29 01:05:38` | `cowrie.command.input` |
| `2026-07-29 01:05:38` | `cowrie.command.input` |
| `2026-07-29 01:05:38` | `cowrie.command.success` |
| `2026-07-29 01:05:38` | `cowrie.command.input` |
| `2026-07-29 01:05:38` | `cowrie.command.input` |
| `2026-07-29 01:05:38` | `cowrie.command.input` |
| `2026-07-29 01:05:38` | `cowrie.command.input` |
| `2026-07-29 01:05:39` | `cowrie.log.closed` |
| `2026-07-29 01:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1a34c15800b

| Field | Detail |
|---|---|
| **Source IP** | `171.231.177[.]152` |
| **First Seen** | 2026-07-29 01:05 |
| **Last Seen** | 2026-07-29 01:05 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:05:36` | `cowrie.session.connect` |
| `2026-07-29 01:05:36` | `cowrie.client.version` |
| `2026-07-29 01:05:46` | `cowrie.client.kex` |
| `2026-07-29 01:05:48` | `cowrie.login.success` |
| `2026-07-29 01:05:49` | `cowrie.direct-tcpip.request` |
| `2026-07-29 01:05:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 01:05:49` | `cowrie.direct-tcpip.data` |
| `2026-07-29 01:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.177[.]152` to AbuseIPDB if not already reported
- [ ] Block `171.231.177[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b039e50dac7a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:06 |
| **Last Seen** | 2026-07-29 01:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:06:59` | `cowrie.session.connect` |
| `2026-07-29 01:06:59` | `cowrie.client.version` |
| `2026-07-29 01:06:59` | `cowrie.client.kex` |
| `2026-07-29 01:07:01` | `cowrie.login.success` |
| `2026-07-29 01:07:02` | `cowrie.session.params` |
| `2026-07-29 01:07:02` | `cowrie.command.input` |
| `2026-07-29 01:07:02` | `cowrie.command.input` |
| `2026-07-29 01:07:02` | `cowrie.command.input` |
| `2026-07-29 01:07:02` | `cowrie.command.input` |
| `2026-07-29 01:07:02` | `cowrie.command.input` |
| `2026-07-29 01:07:02` | `cowrie.command.success` |
| `2026-07-29 01:07:02` | `cowrie.command.input` |
| `2026-07-29 01:07:02` | `cowrie.command.input` |
| `2026-07-29 01:07:02` | `cowrie.command.input` |
| `2026-07-29 01:07:02` | `cowrie.command.input` |
| `2026-07-29 01:07:02` | `cowrie.log.closed` |
| `2026-07-29 01:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1fe34c2e64e

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]144` |
| **First Seen** | 2026-07-29 01:07 |
| **Last Seen** | 2026-07-29 01:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:07:18` | `cowrie.session.connect` |
| `2026-07-29 01:07:18` | `cowrie.login.success` |
| `2026-07-29 01:07:19` | `cowrie.session.params` |
| `2026-07-29 01:07:19` | `cowrie.command.input` |
| `2026-07-29 01:07:20` | `cowrie.command.input` |
| `2026-07-29 01:07:20` | `cowrie.command.input` |
| `2026-07-29 01:07:21` | `cowrie.command.input` |
| `2026-07-29 01:07:21` | `cowrie.command.failed` |
| `2026-07-29 01:07:22` | `cowrie.log.closed` |
| `2026-07-29 01:07:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]144` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6214bb3eaf3b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:08 |
| **Last Seen** | 2026-07-29 01:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:08:23` | `cowrie.session.connect` |
| `2026-07-29 01:08:24` | `cowrie.client.version` |
| `2026-07-29 01:08:24` | `cowrie.client.kex` |
| `2026-07-29 01:08:25` | `cowrie.login.success` |
| `2026-07-29 01:08:27` | `cowrie.session.params` |
| `2026-07-29 01:08:27` | `cowrie.command.input` |
| `2026-07-29 01:08:27` | `cowrie.command.input` |
| `2026-07-29 01:08:27` | `cowrie.command.input` |
| `2026-07-29 01:08:27` | `cowrie.command.input` |
| `2026-07-29 01:08:27` | `cowrie.command.input` |
| `2026-07-29 01:08:27` | `cowrie.command.success` |
| `2026-07-29 01:08:27` | `cowrie.command.input` |
| `2026-07-29 01:08:27` | `cowrie.command.input` |
| `2026-07-29 01:08:27` | `cowrie.command.input` |
| `2026-07-29 01:08:27` | `cowrie.command.input` |
| `2026-07-29 01:08:27` | `cowrie.log.closed` |
| `2026-07-29 01:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54b65b375dfc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:09 |
| **Last Seen** | 2026-07-29 01:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:09:46` | `cowrie.session.connect` |
| `2026-07-29 01:09:47` | `cowrie.client.version` |
| `2026-07-29 01:09:47` | `cowrie.client.kex` |
| `2026-07-29 01:09:49` | `cowrie.login.success` |
| `2026-07-29 01:09:50` | `cowrie.session.params` |
| `2026-07-29 01:09:50` | `cowrie.command.input` |
| `2026-07-29 01:09:50` | `cowrie.command.input` |
| `2026-07-29 01:09:50` | `cowrie.command.input` |
| `2026-07-29 01:09:50` | `cowrie.command.input` |
| `2026-07-29 01:09:50` | `cowrie.command.input` |
| `2026-07-29 01:09:50` | `cowrie.command.success` |
| `2026-07-29 01:09:50` | `cowrie.command.input` |
| `2026-07-29 01:09:50` | `cowrie.command.input` |
| `2026-07-29 01:09:50` | `cowrie.command.input` |
| `2026-07-29 01:09:50` | `cowrie.command.input` |
| `2026-07-29 01:09:50` | `cowrie.log.closed` |
| `2026-07-29 01:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa8f4d7a594e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:11 |
| **Last Seen** | 2026-07-29 01:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:11:07` | `cowrie.session.connect` |
| `2026-07-29 01:11:07` | `cowrie.client.version` |
| `2026-07-29 01:11:07` | `cowrie.client.kex` |
| `2026-07-29 01:11:09` | `cowrie.login.success` |
| `2026-07-29 01:11:10` | `cowrie.session.params` |
| `2026-07-29 01:11:10` | `cowrie.command.input` |
| `2026-07-29 01:11:10` | `cowrie.command.input` |
| `2026-07-29 01:11:10` | `cowrie.command.input` |
| `2026-07-29 01:11:10` | `cowrie.command.input` |
| `2026-07-29 01:11:10` | `cowrie.command.input` |
| `2026-07-29 01:11:10` | `cowrie.command.success` |
| `2026-07-29 01:11:10` | `cowrie.command.input` |
| `2026-07-29 01:11:10` | `cowrie.command.input` |
| `2026-07-29 01:11:10` | `cowrie.command.input` |
| `2026-07-29 01:11:10` | `cowrie.command.input` |
| `2026-07-29 01:11:11` | `cowrie.log.closed` |
| `2026-07-29 01:11:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0427d3c467a0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:12 |
| **Last Seen** | 2026-07-29 01:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:12:29` | `cowrie.session.connect` |
| `2026-07-29 01:12:30` | `cowrie.client.version` |
| `2026-07-29 01:12:30` | `cowrie.client.kex` |
| `2026-07-29 01:12:31` | `cowrie.login.success` |
| `2026-07-29 01:12:33` | `cowrie.session.params` |
| `2026-07-29 01:12:33` | `cowrie.command.input` |
| `2026-07-29 01:12:33` | `cowrie.command.input` |
| `2026-07-29 01:12:33` | `cowrie.command.input` |
| `2026-07-29 01:12:33` | `cowrie.command.input` |
| `2026-07-29 01:12:33` | `cowrie.command.input` |
| `2026-07-29 01:12:33` | `cowrie.command.success` |
| `2026-07-29 01:12:33` | `cowrie.command.input` |
| `2026-07-29 01:12:33` | `cowrie.command.input` |
| `2026-07-29 01:12:33` | `cowrie.command.input` |
| `2026-07-29 01:12:33` | `cowrie.command.input` |
| `2026-07-29 01:12:33` | `cowrie.log.closed` |
| `2026-07-29 01:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4612a8dedf0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:13 |
| **Last Seen** | 2026-07-29 01:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:13:52` | `cowrie.session.connect` |
| `2026-07-29 01:13:53` | `cowrie.client.version` |
| `2026-07-29 01:13:53` | `cowrie.client.kex` |
| `2026-07-29 01:13:54` | `cowrie.login.success` |
| `2026-07-29 01:13:56` | `cowrie.session.params` |
| `2026-07-29 01:13:56` | `cowrie.command.input` |
| `2026-07-29 01:13:56` | `cowrie.command.input` |
| `2026-07-29 01:13:56` | `cowrie.command.input` |
| `2026-07-29 01:13:56` | `cowrie.command.input` |
| `2026-07-29 01:13:56` | `cowrie.command.input` |
| `2026-07-29 01:13:56` | `cowrie.command.success` |
| `2026-07-29 01:13:56` | `cowrie.command.input` |
| `2026-07-29 01:13:56` | `cowrie.command.input` |
| `2026-07-29 01:13:56` | `cowrie.command.input` |
| `2026-07-29 01:13:56` | `cowrie.command.input` |
| `2026-07-29 01:13:56` | `cowrie.log.closed` |
| `2026-07-29 01:13:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30c781e676b1

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-07-29 01:14 |
| **Last Seen** | 2026-07-29 01:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:14:59` | `cowrie.session.connect` |
| `2026-07-29 01:15:00` | `cowrie.client.version` |
| `2026-07-29 01:15:00` | `cowrie.client.kex` |
| `2026-07-29 01:15:02` | `cowrie.login.success` |
| `2026-07-29 01:15:03` | `cowrie.direct-tcpip.request` |
| `2026-07-29 01:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d138b488591c

| Field | Detail |
|---|---|
| **Source IP** | `220.122.115[.]9` |
| **First Seen** | 2026-07-29 01:15 |
| **Last Seen** | 2026-07-29 01:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:15:08` | `cowrie.session.connect` |
| `2026-07-29 01:15:09` | `cowrie.client.version` |
| `2026-07-29 01:15:09` | `cowrie.client.kex` |
| `2026-07-29 01:15:11` | `cowrie.login.success` |
| `2026-07-29 01:15:11` | `cowrie.direct-tcpip.request` |
| `2026-07-29 01:15:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.122.115[.]9` to AbuseIPDB if not already reported
- [ ] Block `220.122.115[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f1955223f44

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:15 |
| **Last Seen** | 2026-07-29 01:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:15:17` | `cowrie.session.connect` |
| `2026-07-29 01:15:18` | `cowrie.client.version` |
| `2026-07-29 01:15:18` | `cowrie.client.kex` |
| `2026-07-29 01:15:19` | `cowrie.login.success` |
| `2026-07-29 01:15:21` | `cowrie.session.params` |
| `2026-07-29 01:15:21` | `cowrie.command.input` |
| `2026-07-29 01:15:21` | `cowrie.command.input` |
| `2026-07-29 01:15:21` | `cowrie.command.input` |
| `2026-07-29 01:15:21` | `cowrie.command.input` |
| `2026-07-29 01:15:21` | `cowrie.command.input` |
| `2026-07-29 01:15:21` | `cowrie.command.success` |
| `2026-07-29 01:15:21` | `cowrie.command.input` |
| `2026-07-29 01:15:21` | `cowrie.command.input` |
| `2026-07-29 01:15:21` | `cowrie.command.input` |
| `2026-07-29 01:15:21` | `cowrie.command.input` |
| `2026-07-29 01:15:21` | `cowrie.log.closed` |
| `2026-07-29 01:15:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f039713da89

| Field | Detail |
|---|---|
| **Source IP** | `103.193.179[.]139` |
| **First Seen** | 2026-07-29 01:15 |
| **Last Seen** | 2026-07-29 01:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:15:26` | `cowrie.session.connect` |
| `2026-07-29 01:15:26` | `cowrie.client.version` |
| `2026-07-29 01:15:26` | `cowrie.client.kex` |
| `2026-07-29 01:15:27` | `cowrie.login.success` |
| `2026-07-29 01:15:28` | `cowrie.session.params` |
| `2026-07-29 01:15:28` | `cowrie.command.input` |
| `2026-07-29 01:15:28` | `cowrie.command.failed` |
| `2026-07-29 01:15:29` | `cowrie.log.closed` |
| `2026-07-29 01:15:30` | `cowrie.session.params` |
| `2026-07-29 01:15:30` | `cowrie.command.input` |
| `2026-07-29 01:15:30` | `cowrie.session.file_download` |
| `2026-07-29 01:15:30` | `cowrie.log.closed` |
| `2026-07-29 01:15:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.193.179[.]139` to AbuseIPDB if not already reported
- [ ] Block `103.193.179[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48159e75c32d

| Field | Detail |
|---|---|
| **Source IP** | `103.193.179[.]139` |
| **First Seen** | 2026-07-29 01:15 |
| **Last Seen** | 2026-07-29 01:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:15:31` | `cowrie.session.connect` |
| `2026-07-29 01:15:31` | `cowrie.client.version` |
| `2026-07-29 01:15:31` | `cowrie.client.kex` |
| `2026-07-29 01:15:32` | `cowrie.login.success` |
| `2026-07-29 01:15:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.193.179[.]139` to AbuseIPDB if not already reported
- [ ] Block `103.193.179[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-064bcebf2926

| Field | Detail |
|---|---|
| **Source IP** | `103.193.179[.]139` |
| **First Seen** | 2026-07-29 01:15 |
| **Last Seen** | 2026-07-29 01:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:15:32` | `cowrie.session.connect` |
| `2026-07-29 01:15:32` | `cowrie.client.version` |
| `2026-07-29 01:15:33` | `cowrie.client.kex` |
| `2026-07-29 01:15:34` | `cowrie.login.success` |
| `2026-07-29 01:15:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.193.179[.]139` to AbuseIPDB if not already reported
- [ ] Block `103.193.179[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-954d087cbe58

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:16 |
| **Last Seen** | 2026-07-29 01:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:16:41` | `cowrie.session.connect` |
| `2026-07-29 01:16:41` | `cowrie.client.version` |
| `2026-07-29 01:16:41` | `cowrie.client.kex` |
| `2026-07-29 01:16:42` | `cowrie.login.success` |
| `2026-07-29 01:16:43` | `cowrie.session.params` |
| `2026-07-29 01:16:43` | `cowrie.command.input` |
| `2026-07-29 01:16:43` | `cowrie.command.input` |
| `2026-07-29 01:16:43` | `cowrie.command.input` |
| `2026-07-29 01:16:43` | `cowrie.command.input` |
| `2026-07-29 01:16:43` | `cowrie.command.input` |
| `2026-07-29 01:16:43` | `cowrie.command.success` |
| `2026-07-29 01:16:43` | `cowrie.command.input` |
| `2026-07-29 01:16:43` | `cowrie.command.input` |
| `2026-07-29 01:16:43` | `cowrie.command.input` |
| `2026-07-29 01:16:43` | `cowrie.command.input` |
| `2026-07-29 01:16:44` | `cowrie.log.closed` |
| `2026-07-29 01:16:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a42e42b5a8b3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:17 |
| **Last Seen** | 2026-07-29 01:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:17:01` | `cowrie.session.connect` |
| `2026-07-29 01:17:02` | `cowrie.client.version` |
| `2026-07-29 01:17:02` | `cowrie.client.kex` |
| `2026-07-29 01:17:05` | `cowrie.login.success` |
| `2026-07-29 01:17:08` | `cowrie.session.params` |
| `2026-07-29 01:17:08` | `cowrie.command.input` |
| `2026-07-29 01:17:08` | `cowrie.command.input` |
| `2026-07-29 01:17:08` | `cowrie.command.input` |
| `2026-07-29 01:17:08` | `cowrie.command.input` |
| `2026-07-29 01:17:08` | `cowrie.command.input` |
| `2026-07-29 01:17:08` | `cowrie.command.success` |
| `2026-07-29 01:17:08` | `cowrie.command.input` |
| `2026-07-29 01:17:08` | `cowrie.command.input` |
| `2026-07-29 01:17:08` | `cowrie.command.input` |
| `2026-07-29 01:17:08` | `cowrie.command.input` |
| `2026-07-29 01:17:10` | `cowrie.log.closed` |
| `2026-07-29 01:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f39b4bf4b0e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:18 |
| **Last Seen** | 2026-07-29 01:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:18:03` | `cowrie.session.connect` |
| `2026-07-29 01:18:03` | `cowrie.client.version` |
| `2026-07-29 01:18:03` | `cowrie.client.kex` |
| `2026-07-29 01:18:05` | `cowrie.login.success` |
| `2026-07-29 01:18:06` | `cowrie.session.params` |
| `2026-07-29 01:18:06` | `cowrie.command.input` |
| `2026-07-29 01:18:06` | `cowrie.command.input` |
| `2026-07-29 01:18:06` | `cowrie.command.input` |
| `2026-07-29 01:18:06` | `cowrie.command.input` |
| `2026-07-29 01:18:06` | `cowrie.command.input` |
| `2026-07-29 01:18:06` | `cowrie.command.success` |
| `2026-07-29 01:18:06` | `cowrie.command.input` |
| `2026-07-29 01:18:06` | `cowrie.command.input` |
| `2026-07-29 01:18:06` | `cowrie.command.input` |
| `2026-07-29 01:18:06` | `cowrie.command.input` |
| `2026-07-29 01:18:06` | `cowrie.log.closed` |
| `2026-07-29 01:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e54739cc5bbe

| Field | Detail |
|---|---|
| **Source IP** | `85.198.19[.]242` |
| **First Seen** | 2026-07-29 01:18 |
| **Last Seen** | 2026-07-29 01:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:18:19` | `cowrie.session.connect` |
| `2026-07-29 01:18:19` | `cowrie.client.version` |
| `2026-07-29 01:18:20` | `cowrie.client.kex` |
| `2026-07-29 01:18:21` | `cowrie.login.success` |
| `2026-07-29 01:18:22` | `cowrie.session.params` |
| `2026-07-29 01:18:22` | `cowrie.command.input` |
| `2026-07-29 01:18:22` | `cowrie.command.failed` |
| `2026-07-29 01:18:22` | `cowrie.log.closed` |
| `2026-07-29 01:18:23` | `cowrie.session.params` |
| `2026-07-29 01:18:23` | `cowrie.command.input` |
| `2026-07-29 01:18:24` | `cowrie.session.file_download` |
| `2026-07-29 01:18:24` | `cowrie.log.closed` |
| `2026-07-29 01:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.198.19[.]242` to AbuseIPDB if not already reported
- [ ] Block `85.198.19[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd783e34fc65

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]85` |
| **First Seen** | 2026-07-29 01:18 |
| **Last Seen** | 2026-07-29 01:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:18:21` | `cowrie.session.connect` |
| `2026-07-29 01:18:22` | `cowrie.client.version` |
| `2026-07-29 01:18:22` | `cowrie.client.kex` |
| `2026-07-29 01:18:24` | `cowrie.login.success` |
| `2026-07-29 01:18:24` | `cowrie.direct-tcpip.request` |
| `2026-07-29 01:18:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]85` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]85` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d84338ce53a9

| Field | Detail |
|---|---|
| **Source IP** | `85.198.19[.]242` |
| **First Seen** | 2026-07-29 01:18 |
| **Last Seen** | 2026-07-29 01:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:18:24` | `cowrie.session.connect` |
| `2026-07-29 01:18:24` | `cowrie.client.version` |
| `2026-07-29 01:18:24` | `cowrie.client.kex` |
| `2026-07-29 01:18:25` | `cowrie.login.success` |
| `2026-07-29 01:18:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.198.19[.]242` to AbuseIPDB if not already reported
- [ ] Block `85.198.19[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fae22b8d2f8e

| Field | Detail |
|---|---|
| **Source IP** | `85.198.19[.]242` |
| **First Seen** | 2026-07-29 01:18 |
| **Last Seen** | 2026-07-29 01:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:18:26` | `cowrie.session.connect` |
| `2026-07-29 01:18:26` | `cowrie.client.version` |
| `2026-07-29 01:18:26` | `cowrie.client.kex` |
| `2026-07-29 01:18:27` | `cowrie.login.success` |
| `2026-07-29 01:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.198.19[.]242` to AbuseIPDB if not already reported
- [ ] Block `85.198.19[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cf28fbedccd

| Field | Detail |
|---|---|
| **Source IP** | `103.174.80[.]40` |
| **First Seen** | 2026-07-29 01:18 |
| **Last Seen** | 2026-07-29 01:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:18:29` | `cowrie.session.connect` |
| `2026-07-29 01:18:30` | `cowrie.client.version` |
| `2026-07-29 01:18:30` | `cowrie.client.kex` |
| `2026-07-29 01:18:31` | `cowrie.login.success` |
| `2026-07-29 01:18:32` | `cowrie.direct-tcpip.request` |
| `2026-07-29 01:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.80[.]40` to AbuseIPDB if not already reported
- [ ] Block `103.174.80[.]40` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-816d2cf11ec9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:19 |
| **Last Seen** | 2026-07-29 01:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:19:28` | `cowrie.session.connect` |
| `2026-07-29 01:19:29` | `cowrie.client.version` |
| `2026-07-29 01:19:29` | `cowrie.client.kex` |
| `2026-07-29 01:19:30` | `cowrie.login.success` |
| `2026-07-29 01:19:31` | `cowrie.session.params` |
| `2026-07-29 01:19:31` | `cowrie.command.input` |
| `2026-07-29 01:19:31` | `cowrie.command.input` |
| `2026-07-29 01:19:31` | `cowrie.command.input` |
| `2026-07-29 01:19:31` | `cowrie.command.input` |
| `2026-07-29 01:19:31` | `cowrie.command.input` |
| `2026-07-29 01:19:31` | `cowrie.command.success` |
| `2026-07-29 01:19:31` | `cowrie.command.input` |
| `2026-07-29 01:19:31` | `cowrie.command.input` |
| `2026-07-29 01:19:31` | `cowrie.command.input` |
| `2026-07-29 01:19:31` | `cowrie.command.input` |
| `2026-07-29 01:19:31` | `cowrie.log.closed` |
| `2026-07-29 01:19:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aad1f960b071

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]81` |
| **First Seen** | 2026-07-29 01:19 |
| **Last Seen** | 2026-07-29 01:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:19:29` | `cowrie.session.connect` |
| `2026-07-29 01:19:29` | `cowrie.client.version` |
| `2026-07-29 01:19:30` | `cowrie.client.kex` |
| `2026-07-29 01:19:31` | `cowrie.login.success` |
| `2026-07-29 01:19:32` | `cowrie.session.params` |
| `2026-07-29 01:19:32` | `cowrie.command.input` |
| `2026-07-29 01:19:32` | `cowrie.command.failed` |
| `2026-07-29 01:19:33` | `cowrie.log.closed` |
| `2026-07-29 01:19:34` | `cowrie.session.params` |
| `2026-07-29 01:19:34` | `cowrie.command.input` |
| `2026-07-29 01:19:34` | `cowrie.session.file_download` |
| `2026-07-29 01:19:34` | `cowrie.log.closed` |
| `2026-07-29 01:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]81` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-021ab30006cd

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:19 |
| **Last Seen** | 2026-07-29 01:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:19:31` | `cowrie.session.connect` |
| `2026-07-29 01:19:32` | `cowrie.client.version` |
| `2026-07-29 01:19:32` | `cowrie.client.kex` |
| `2026-07-29 01:19:36` | `cowrie.login.success` |
| `2026-07-29 01:19:38` | `cowrie.session.params` |
| `2026-07-29 01:19:38` | `cowrie.command.input` |
| `2026-07-29 01:19:38` | `cowrie.command.input` |
| `2026-07-29 01:19:38` | `cowrie.command.input` |
| `2026-07-29 01:19:38` | `cowrie.command.input` |
| `2026-07-29 01:19:38` | `cowrie.command.input` |
| `2026-07-29 01:19:38` | `cowrie.command.success` |
| `2026-07-29 01:19:38` | `cowrie.command.input` |
| `2026-07-29 01:19:38` | `cowrie.command.input` |
| `2026-07-29 01:19:38` | `cowrie.command.input` |
| `2026-07-29 01:19:38` | `cowrie.command.input` |
| `2026-07-29 01:19:40` | `cowrie.log.closed` |
| `2026-07-29 01:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c20183721cb

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]81` |
| **First Seen** | 2026-07-29 01:19 |
| **Last Seen** | 2026-07-29 01:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:19:34` | `cowrie.session.connect` |
| `2026-07-29 01:19:34` | `cowrie.client.version` |
| `2026-07-29 01:19:34` | `cowrie.client.kex` |
| `2026-07-29 01:19:36` | `cowrie.login.success` |
| `2026-07-29 01:19:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]81` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee9983437d1b

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]81` |
| **First Seen** | 2026-07-29 01:19 |
| **Last Seen** | 2026-07-29 01:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:19:36` | `cowrie.session.connect` |
| `2026-07-29 01:19:36` | `cowrie.client.version` |
| `2026-07-29 01:19:36` | `cowrie.client.kex` |
| `2026-07-29 01:19:39` | `cowrie.login.success` |
| `2026-07-29 01:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]81` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eda9ef610810

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 01:20 |
| **Last Seen** | 2026-07-29 01:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:20:15` | `cowrie.session.connect` |
| `2026-07-29 01:20:15` | `cowrie.client.version` |
| `2026-07-29 01:20:15` | `cowrie.client.kex` |
| `2026-07-29 01:20:15` | `cowrie.login.success` |
| `2026-07-29 01:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eb42cdfcbce

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 01:20 |
| **Last Seen** | 2026-07-29 01:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:20:15` | `cowrie.session.connect` |
| `2026-07-29 01:20:15` | `cowrie.client.version` |
| `2026-07-29 01:20:15` | `cowrie.client.kex` |
| `2026-07-29 01:20:15` | `cowrie.login.success` |
| `2026-07-29 01:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e62739dc977

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 01:20 |
| **Last Seen** | 2026-07-29 01:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:20:24` | `cowrie.session.connect` |
| `2026-07-29 01:20:24` | `cowrie.client.version` |
| `2026-07-29 01:20:24` | `cowrie.client.kex` |
| `2026-07-29 01:20:24` | `cowrie.login.success` |
| `2026-07-29 01:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47e24f9d63af

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 01:20 |
| **Last Seen** | 2026-07-29 01:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:20:24` | `cowrie.session.connect` |
| `2026-07-29 01:20:24` | `cowrie.client.version` |
| `2026-07-29 01:20:24` | `cowrie.client.kex` |
| `2026-07-29 01:20:24` | `cowrie.login.success` |
| `2026-07-29 01:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eff5fae160b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:20 |
| **Last Seen** | 2026-07-29 01:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:20:55` | `cowrie.session.connect` |
| `2026-07-29 01:20:55` | `cowrie.client.version` |
| `2026-07-29 01:20:55` | `cowrie.client.kex` |
| `2026-07-29 01:20:56` | `cowrie.login.success` |
| `2026-07-29 01:20:57` | `cowrie.session.params` |
| `2026-07-29 01:20:57` | `cowrie.command.input` |
| `2026-07-29 01:20:57` | `cowrie.command.input` |
| `2026-07-29 01:20:57` | `cowrie.command.input` |
| `2026-07-29 01:20:57` | `cowrie.command.input` |
| `2026-07-29 01:20:57` | `cowrie.command.input` |
| `2026-07-29 01:20:57` | `cowrie.command.success` |
| `2026-07-29 01:20:57` | `cowrie.command.input` |
| `2026-07-29 01:20:57` | `cowrie.command.input` |
| `2026-07-29 01:20:57` | `cowrie.command.input` |
| `2026-07-29 01:20:57` | `cowrie.command.input` |
| `2026-07-29 01:20:57` | `cowrie.log.closed` |
| `2026-07-29 01:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c5b117f186b

| Field | Detail |
|---|---|
| **Source IP** | `120.234.232[.]184` |
| **First Seen** | 2026-07-29 01:21 |
| **Last Seen** | 2026-07-29 01:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:21:18` | `cowrie.session.connect` |
| `2026-07-29 01:21:18` | `cowrie.client.version` |
| `2026-07-29 01:21:18` | `cowrie.client.kex` |
| `2026-07-29 01:21:20` | `cowrie.login.success` |
| `2026-07-29 01:21:21` | `cowrie.direct-tcpip.request` |
| `2026-07-29 01:21:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.234.232[.]184` to AbuseIPDB if not already reported
- [ ] Block `120.234.232[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-125f028d1de7

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:22 |
| **Last Seen** | 2026-07-29 01:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:22:01` | `cowrie.session.connect` |
| `2026-07-29 01:22:02` | `cowrie.client.version` |
| `2026-07-29 01:22:02` | `cowrie.client.kex` |
| `2026-07-29 01:22:03` | `cowrie.login.success` |
| `2026-07-29 01:22:04` | `cowrie.session.params` |
| `2026-07-29 01:22:04` | `cowrie.command.input` |
| `2026-07-29 01:22:04` | `cowrie.command.input` |
| `2026-07-29 01:22:04` | `cowrie.command.input` |
| `2026-07-29 01:22:04` | `cowrie.command.input` |
| `2026-07-29 01:22:04` | `cowrie.command.input` |
| `2026-07-29 01:22:04` | `cowrie.command.success` |
| `2026-07-29 01:22:04` | `cowrie.command.input` |
| `2026-07-29 01:22:04` | `cowrie.command.input` |
| `2026-07-29 01:22:04` | `cowrie.command.input` |
| `2026-07-29 01:22:04` | `cowrie.command.input` |
| `2026-07-29 01:22:05` | `cowrie.log.closed` |
| `2026-07-29 01:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65b10e3f652f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:22 |
| **Last Seen** | 2026-07-29 01:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:22:22` | `cowrie.session.connect` |
| `2026-07-29 01:22:22` | `cowrie.client.version` |
| `2026-07-29 01:22:22` | `cowrie.client.kex` |
| `2026-07-29 01:22:24` | `cowrie.login.success` |
| `2026-07-29 01:22:25` | `cowrie.session.params` |
| `2026-07-29 01:22:25` | `cowrie.command.input` |
| `2026-07-29 01:22:25` | `cowrie.command.input` |
| `2026-07-29 01:22:25` | `cowrie.command.input` |
| `2026-07-29 01:22:25` | `cowrie.command.input` |
| `2026-07-29 01:22:25` | `cowrie.command.input` |
| `2026-07-29 01:22:25` | `cowrie.command.success` |
| `2026-07-29 01:22:25` | `cowrie.command.input` |
| `2026-07-29 01:22:25` | `cowrie.command.input` |
| `2026-07-29 01:22:25` | `cowrie.command.input` |
| `2026-07-29 01:22:25` | `cowrie.command.input` |
| `2026-07-29 01:22:25` | `cowrie.log.closed` |
| `2026-07-29 01:22:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daf867e856e8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:23 |
| **Last Seen** | 2026-07-29 01:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:23:47` | `cowrie.session.connect` |
| `2026-07-29 01:23:48` | `cowrie.client.version` |
| `2026-07-29 01:23:48` | `cowrie.client.kex` |
| `2026-07-29 01:23:49` | `cowrie.login.success` |
| `2026-07-29 01:23:50` | `cowrie.session.params` |
| `2026-07-29 01:23:50` | `cowrie.command.input` |
| `2026-07-29 01:23:50` | `cowrie.command.input` |
| `2026-07-29 01:23:50` | `cowrie.command.input` |
| `2026-07-29 01:23:50` | `cowrie.command.input` |
| `2026-07-29 01:23:50` | `cowrie.command.input` |
| `2026-07-29 01:23:50` | `cowrie.command.success` |
| `2026-07-29 01:23:50` | `cowrie.command.input` |
| `2026-07-29 01:23:50` | `cowrie.command.input` |
| `2026-07-29 01:23:50` | `cowrie.command.input` |
| `2026-07-29 01:23:50` | `cowrie.command.input` |
| `2026-07-29 01:23:50` | `cowrie.log.closed` |
| `2026-07-29 01:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aece64f55fc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:24 |
| **Last Seen** | 2026-07-29 01:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:24:12` | `cowrie.session.connect` |
| `2026-07-29 01:24:12` | `cowrie.client.version` |
| `2026-07-29 01:24:12` | `cowrie.client.kex` |
| `2026-07-29 01:24:17` | `cowrie.login.success` |
| `2026-07-29 01:24:19` | `cowrie.session.params` |
| `2026-07-29 01:24:19` | `cowrie.command.input` |
| `2026-07-29 01:24:19` | `cowrie.command.input` |
| `2026-07-29 01:24:19` | `cowrie.command.input` |
| `2026-07-29 01:24:19` | `cowrie.command.input` |
| `2026-07-29 01:24:19` | `cowrie.command.input` |
| `2026-07-29 01:24:19` | `cowrie.command.success` |
| `2026-07-29 01:24:19` | `cowrie.command.input` |
| `2026-07-29 01:24:19` | `cowrie.command.input` |
| `2026-07-29 01:24:19` | `cowrie.command.input` |
| `2026-07-29 01:24:19` | `cowrie.command.input` |
| `2026-07-29 01:24:20` | `cowrie.log.closed` |
| `2026-07-29 01:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d49667453cf

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:25 |
| **Last Seen** | 2026-07-29 01:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:25:15` | `cowrie.session.connect` |
| `2026-07-29 01:25:15` | `cowrie.client.version` |
| `2026-07-29 01:25:16` | `cowrie.client.kex` |
| `2026-07-29 01:25:17` | `cowrie.login.success` |
| `2026-07-29 01:25:18` | `cowrie.session.params` |
| `2026-07-29 01:25:18` | `cowrie.command.input` |
| `2026-07-29 01:25:18` | `cowrie.command.input` |
| `2026-07-29 01:25:18` | `cowrie.command.input` |
| `2026-07-29 01:25:18` | `cowrie.command.input` |
| `2026-07-29 01:25:18` | `cowrie.command.input` |
| `2026-07-29 01:25:18` | `cowrie.command.success` |
| `2026-07-29 01:25:18` | `cowrie.command.input` |
| `2026-07-29 01:25:18` | `cowrie.command.input` |
| `2026-07-29 01:25:18` | `cowrie.command.input` |
| `2026-07-29 01:25:18` | `cowrie.command.input` |
| `2026-07-29 01:25:18` | `cowrie.log.closed` |
| `2026-07-29 01:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-682058ce74b5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:26 |
| **Last Seen** | 2026-07-29 01:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:26:47` | `cowrie.session.connect` |
| `2026-07-29 01:26:47` | `cowrie.client.version` |
| `2026-07-29 01:26:47` | `cowrie.client.kex` |
| `2026-07-29 01:26:48` | `cowrie.login.success` |
| `2026-07-29 01:26:50` | `cowrie.session.params` |
| `2026-07-29 01:26:50` | `cowrie.command.input` |
| `2026-07-29 01:26:50` | `cowrie.command.input` |
| `2026-07-29 01:26:50` | `cowrie.command.input` |
| `2026-07-29 01:26:50` | `cowrie.command.input` |
| `2026-07-29 01:26:50` | `cowrie.command.input` |
| `2026-07-29 01:26:50` | `cowrie.command.success` |
| `2026-07-29 01:26:50` | `cowrie.command.input` |
| `2026-07-29 01:26:50` | `cowrie.command.input` |
| `2026-07-29 01:26:50` | `cowrie.command.input` |
| `2026-07-29 01:26:50` | `cowrie.command.input` |
| `2026-07-29 01:26:50` | `cowrie.log.closed` |
| `2026-07-29 01:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95f20195388d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:27 |
| **Last Seen** | 2026-07-29 01:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:27:03` | `cowrie.session.connect` |
| `2026-07-29 01:27:03` | `cowrie.client.version` |
| `2026-07-29 01:27:03` | `cowrie.client.kex` |
| `2026-07-29 01:27:05` | `cowrie.login.success` |
| `2026-07-29 01:27:07` | `cowrie.session.params` |
| `2026-07-29 01:27:07` | `cowrie.command.input` |
| `2026-07-29 01:27:07` | `cowrie.command.input` |
| `2026-07-29 01:27:07` | `cowrie.command.input` |
| `2026-07-29 01:27:07` | `cowrie.command.input` |
| `2026-07-29 01:27:07` | `cowrie.command.input` |
| `2026-07-29 01:27:07` | `cowrie.command.success` |
| `2026-07-29 01:27:07` | `cowrie.command.input` |
| `2026-07-29 01:27:07` | `cowrie.command.input` |
| `2026-07-29 01:27:07` | `cowrie.command.input` |
| `2026-07-29 01:27:07` | `cowrie.command.input` |
| `2026-07-29 01:27:08` | `cowrie.log.closed` |
| `2026-07-29 01:27:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f33dc1ffc40

| Field | Detail |
|---|---|
| **Source IP** | `223.107.146[.]186` |
| **First Seen** | 2026-07-29 01:27 |
| **Last Seen** | 2026-07-29 01:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:27:49` | `cowrie.session.connect` |
| `2026-07-29 01:27:50` | `cowrie.client.version` |
| `2026-07-29 01:27:50` | `cowrie.client.kex` |
| `2026-07-29 01:27:52` | `cowrie.login.success` |
| `2026-07-29 01:27:53` | `cowrie.direct-tcpip.request` |
| `2026-07-29 01:27:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.107.146[.]186` to AbuseIPDB if not already reported
- [ ] Block `223.107.146[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9445e263eda5

| Field | Detail |
|---|---|
| **Source IP** | `112.120.115[.]152` |
| **First Seen** | 2026-07-29 01:27 |
| **Last Seen** | 2026-07-29 01:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:27:58` | `cowrie.session.connect` |
| `2026-07-29 01:27:59` | `cowrie.client.version` |
| `2026-07-29 01:27:59` | `cowrie.client.kex` |
| `2026-07-29 01:28:01` | `cowrie.login.success` |
| `2026-07-29 01:28:02` | `cowrie.direct-tcpip.request` |
| `2026-07-29 01:28:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.115[.]152` to AbuseIPDB if not already reported
- [ ] Block `112.120.115[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fef99a3dff5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:28 |
| **Last Seen** | 2026-07-29 01:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:28:20` | `cowrie.session.connect` |
| `2026-07-29 01:28:20` | `cowrie.client.version` |
| `2026-07-29 01:28:20` | `cowrie.client.kex` |
| `2026-07-29 01:28:21` | `cowrie.login.success` |
| `2026-07-29 01:28:22` | `cowrie.session.params` |
| `2026-07-29 01:28:22` | `cowrie.command.input` |
| `2026-07-29 01:28:22` | `cowrie.command.input` |
| `2026-07-29 01:28:22` | `cowrie.command.input` |
| `2026-07-29 01:28:22` | `cowrie.command.input` |
| `2026-07-29 01:28:22` | `cowrie.command.input` |
| `2026-07-29 01:28:22` | `cowrie.command.success` |
| `2026-07-29 01:28:22` | `cowrie.command.input` |
| `2026-07-29 01:28:22` | `cowrie.command.input` |
| `2026-07-29 01:28:22` | `cowrie.command.input` |
| `2026-07-29 01:28:22` | `cowrie.command.input` |
| `2026-07-29 01:28:22` | `cowrie.log.closed` |
| `2026-07-29 01:28:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-603e48fc1050

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:28 |
| **Last Seen** | 2026-07-29 01:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:28:36` | `cowrie.session.connect` |
| `2026-07-29 01:28:37` | `cowrie.client.version` |
| `2026-07-29 01:28:37` | `cowrie.client.kex` |
| `2026-07-29 01:28:38` | `cowrie.login.success` |
| `2026-07-29 01:28:40` | `cowrie.session.params` |
| `2026-07-29 01:28:40` | `cowrie.command.input` |
| `2026-07-29 01:28:40` | `cowrie.command.input` |
| `2026-07-29 01:28:40` | `cowrie.command.input` |
| `2026-07-29 01:28:40` | `cowrie.command.input` |
| `2026-07-29 01:28:40` | `cowrie.command.input` |
| `2026-07-29 01:28:40` | `cowrie.command.success` |
| `2026-07-29 01:28:40` | `cowrie.command.input` |
| `2026-07-29 01:28:40` | `cowrie.command.input` |
| `2026-07-29 01:28:40` | `cowrie.command.input` |
| `2026-07-29 01:28:40` | `cowrie.command.input` |
| `2026-07-29 01:28:40` | `cowrie.log.closed` |
| `2026-07-29 01:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ffb1bf98854

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:29 |
| **Last Seen** | 2026-07-29 01:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:29:49` | `cowrie.session.connect` |
| `2026-07-29 01:29:49` | `cowrie.client.version` |
| `2026-07-29 01:29:49` | `cowrie.client.kex` |
| `2026-07-29 01:29:50` | `cowrie.login.success` |
| `2026-07-29 01:29:51` | `cowrie.session.params` |
| `2026-07-29 01:29:51` | `cowrie.command.input` |
| `2026-07-29 01:29:51` | `cowrie.command.input` |
| `2026-07-29 01:29:51` | `cowrie.command.input` |
| `2026-07-29 01:29:51` | `cowrie.command.input` |
| `2026-07-29 01:29:51` | `cowrie.command.input` |
| `2026-07-29 01:29:51` | `cowrie.command.success` |
| `2026-07-29 01:29:51` | `cowrie.command.input` |
| `2026-07-29 01:29:51` | `cowrie.command.input` |
| `2026-07-29 01:29:51` | `cowrie.command.input` |
| `2026-07-29 01:29:51` | `cowrie.command.input` |
| `2026-07-29 01:29:52` | `cowrie.log.closed` |
| `2026-07-29 01:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17882b40449a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:30 |
| **Last Seen** | 2026-07-29 01:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:30:25` | `cowrie.session.connect` |
| `2026-07-29 01:30:25` | `cowrie.client.version` |
| `2026-07-29 01:30:25` | `cowrie.client.kex` |
| `2026-07-29 01:30:26` | `cowrie.login.success` |
| `2026-07-29 01:30:27` | `cowrie.session.params` |
| `2026-07-29 01:30:27` | `cowrie.command.input` |
| `2026-07-29 01:30:27` | `cowrie.command.input` |
| `2026-07-29 01:30:27` | `cowrie.command.input` |
| `2026-07-29 01:30:27` | `cowrie.command.input` |
| `2026-07-29 01:30:27` | `cowrie.command.input` |
| `2026-07-29 01:30:27` | `cowrie.command.success` |
| `2026-07-29 01:30:27` | `cowrie.command.input` |
| `2026-07-29 01:30:27` | `cowrie.command.input` |
| `2026-07-29 01:30:27` | `cowrie.command.input` |
| `2026-07-29 01:30:27` | `cowrie.command.input` |
| `2026-07-29 01:30:27` | `cowrie.log.closed` |
| `2026-07-29 01:30:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78078f1a7fe8

| Field | Detail |
|---|---|
| **Source IP** | `116.114.84[.]246` |
| **First Seen** | 2026-07-29 01:30 |
| **Last Seen** | 2026-07-29 01:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:30:59` | `cowrie.session.connect` |
| `2026-07-29 01:31:00` | `cowrie.client.version` |
| `2026-07-29 01:31:00` | `cowrie.client.kex` |
| `2026-07-29 01:31:02` | `cowrie.login.success` |
| `2026-07-29 01:31:03` | `cowrie.direct-tcpip.request` |
| `2026-07-29 01:31:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.84[.]246` to AbuseIPDB if not already reported
- [ ] Block `116.114.84[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40fbf646742f

| Field | Detail |
|---|---|
| **Source IP** | `182.135.63[.]175` |
| **First Seen** | 2026-07-29 01:31 |
| **Last Seen** | 2026-07-29 01:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:31:08` | `cowrie.session.connect` |
| `2026-07-29 01:31:09` | `cowrie.client.version` |
| `2026-07-29 01:31:09` | `cowrie.client.kex` |
| `2026-07-29 01:31:12` | `cowrie.login.success` |
| `2026-07-29 01:31:13` | `cowrie.direct-tcpip.request` |
| `2026-07-29 01:31:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.135.63[.]175` to AbuseIPDB if not already reported
- [ ] Block `182.135.63[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ead5bd210a8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:31 |
| **Last Seen** | 2026-07-29 01:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:31:15` | `cowrie.session.connect` |
| `2026-07-29 01:31:15` | `cowrie.client.version` |
| `2026-07-29 01:31:15` | `cowrie.client.kex` |
| `2026-07-29 01:31:16` | `cowrie.login.success` |
| `2026-07-29 01:31:18` | `cowrie.session.params` |
| `2026-07-29 01:31:18` | `cowrie.command.input` |
| `2026-07-29 01:31:18` | `cowrie.command.input` |
| `2026-07-29 01:31:18` | `cowrie.command.input` |
| `2026-07-29 01:31:18` | `cowrie.command.input` |
| `2026-07-29 01:31:18` | `cowrie.command.input` |
| `2026-07-29 01:31:18` | `cowrie.command.success` |
| `2026-07-29 01:31:18` | `cowrie.command.input` |
| `2026-07-29 01:31:18` | `cowrie.command.input` |
| `2026-07-29 01:31:18` | `cowrie.command.input` |
| `2026-07-29 01:31:18` | `cowrie.command.input` |
| `2026-07-29 01:31:18` | `cowrie.log.closed` |
| `2026-07-29 01:31:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6d757530c30

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:32 |
| **Last Seen** | 2026-07-29 01:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:32:18` | `cowrie.session.connect` |
| `2026-07-29 01:32:18` | `cowrie.client.version` |
| `2026-07-29 01:32:18` | `cowrie.client.kex` |
| `2026-07-29 01:32:19` | `cowrie.login.success` |
| `2026-07-29 01:32:20` | `cowrie.session.params` |
| `2026-07-29 01:32:20` | `cowrie.command.input` |
| `2026-07-29 01:32:20` | `cowrie.command.input` |
| `2026-07-29 01:32:20` | `cowrie.command.input` |
| `2026-07-29 01:32:20` | `cowrie.command.input` |
| `2026-07-29 01:32:20` | `cowrie.command.input` |
| `2026-07-29 01:32:20` | `cowrie.command.success` |
| `2026-07-29 01:32:20` | `cowrie.command.input` |
| `2026-07-29 01:32:20` | `cowrie.command.input` |
| `2026-07-29 01:32:20` | `cowrie.command.input` |
| `2026-07-29 01:32:20` | `cowrie.command.input` |
| `2026-07-29 01:32:21` | `cowrie.log.closed` |
| `2026-07-29 01:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c459ee048cd0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:32 |
| **Last Seen** | 2026-07-29 01:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:32:38` | `cowrie.session.connect` |
| `2026-07-29 01:32:38` | `cowrie.client.version` |
| `2026-07-29 01:32:38` | `cowrie.client.kex` |
| `2026-07-29 01:32:40` | `cowrie.login.success` |
| `2026-07-29 01:32:42` | `cowrie.session.params` |
| `2026-07-29 01:32:42` | `cowrie.command.input` |
| `2026-07-29 01:32:42` | `cowrie.command.input` |
| `2026-07-29 01:32:42` | `cowrie.command.input` |
| `2026-07-29 01:32:42` | `cowrie.command.input` |
| `2026-07-29 01:32:42` | `cowrie.command.input` |
| `2026-07-29 01:32:42` | `cowrie.command.success` |
| `2026-07-29 01:32:42` | `cowrie.command.input` |
| `2026-07-29 01:32:42` | `cowrie.command.input` |
| `2026-07-29 01:32:42` | `cowrie.command.input` |
| `2026-07-29 01:32:42` | `cowrie.command.input` |
| `2026-07-29 01:32:42` | `cowrie.log.closed` |
| `2026-07-29 01:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12e9fa9df864

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:33 |
| **Last Seen** | 2026-07-29 01:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:33:59` | `cowrie.session.connect` |
| `2026-07-29 01:34:00` | `cowrie.client.version` |
| `2026-07-29 01:34:00` | `cowrie.client.kex` |
| `2026-07-29 01:34:01` | `cowrie.login.success` |
| `2026-07-29 01:34:03` | `cowrie.session.params` |
| `2026-07-29 01:34:03` | `cowrie.command.input` |
| `2026-07-29 01:34:03` | `cowrie.command.input` |
| `2026-07-29 01:34:03` | `cowrie.command.input` |
| `2026-07-29 01:34:03` | `cowrie.command.input` |
| `2026-07-29 01:34:03` | `cowrie.command.input` |
| `2026-07-29 01:34:03` | `cowrie.command.success` |
| `2026-07-29 01:34:03` | `cowrie.command.input` |
| `2026-07-29 01:34:03` | `cowrie.command.input` |
| `2026-07-29 01:34:03` | `cowrie.command.input` |
| `2026-07-29 01:34:03` | `cowrie.command.input` |
| `2026-07-29 01:34:03` | `cowrie.log.closed` |
| `2026-07-29 01:34:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-422c96eacb93

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:34 |
| **Last Seen** | 2026-07-29 01:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:34:03` | `cowrie.session.connect` |
| `2026-07-29 01:34:03` | `cowrie.client.version` |
| `2026-07-29 01:34:03` | `cowrie.client.kex` |
| `2026-07-29 01:34:04` | `cowrie.login.success` |
| `2026-07-29 01:34:05` | `cowrie.session.params` |
| `2026-07-29 01:34:05` | `cowrie.command.input` |
| `2026-07-29 01:34:05` | `cowrie.command.input` |
| `2026-07-29 01:34:05` | `cowrie.command.input` |
| `2026-07-29 01:34:05` | `cowrie.command.input` |
| `2026-07-29 01:34:05` | `cowrie.command.input` |
| `2026-07-29 01:34:05` | `cowrie.command.success` |
| `2026-07-29 01:34:05` | `cowrie.command.input` |
| `2026-07-29 01:34:05` | `cowrie.command.input` |
| `2026-07-29 01:34:05` | `cowrie.command.input` |
| `2026-07-29 01:34:05` | `cowrie.command.input` |
| `2026-07-29 01:34:06` | `cowrie.log.closed` |
| `2026-07-29 01:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bddac64c0597

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:35 |
| **Last Seen** | 2026-07-29 01:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:35:20` | `cowrie.session.connect` |
| `2026-07-29 01:35:21` | `cowrie.client.version` |
| `2026-07-29 01:35:21` | `cowrie.client.kex` |
| `2026-07-29 01:35:23` | `cowrie.login.success` |
| `2026-07-29 01:35:24` | `cowrie.session.params` |
| `2026-07-29 01:35:24` | `cowrie.command.input` |
| `2026-07-29 01:35:24` | `cowrie.command.input` |
| `2026-07-29 01:35:24` | `cowrie.command.input` |
| `2026-07-29 01:35:24` | `cowrie.command.input` |
| `2026-07-29 01:35:24` | `cowrie.command.input` |
| `2026-07-29 01:35:24` | `cowrie.command.success` |
| `2026-07-29 01:35:24` | `cowrie.command.input` |
| `2026-07-29 01:35:24` | `cowrie.command.input` |
| `2026-07-29 01:35:24` | `cowrie.command.input` |
| `2026-07-29 01:35:24` | `cowrie.command.input` |
| `2026-07-29 01:35:25` | `cowrie.log.closed` |
| `2026-07-29 01:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbaf48543ada

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:35 |
| **Last Seen** | 2026-07-29 01:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:35:41` | `cowrie.session.connect` |
| `2026-07-29 01:35:42` | `cowrie.client.version` |
| `2026-07-29 01:35:42` | `cowrie.client.kex` |
| `2026-07-29 01:35:43` | `cowrie.login.success` |
| `2026-07-29 01:35:44` | `cowrie.session.params` |
| `2026-07-29 01:35:44` | `cowrie.command.input` |
| `2026-07-29 01:35:44` | `cowrie.command.input` |
| `2026-07-29 01:35:44` | `cowrie.command.input` |
| `2026-07-29 01:35:44` | `cowrie.command.input` |
| `2026-07-29 01:35:44` | `cowrie.command.input` |
| `2026-07-29 01:35:44` | `cowrie.command.success` |
| `2026-07-29 01:35:44` | `cowrie.command.input` |
| `2026-07-29 01:35:44` | `cowrie.command.input` |
| `2026-07-29 01:35:44` | `cowrie.command.input` |
| `2026-07-29 01:35:44` | `cowrie.command.input` |
| `2026-07-29 01:35:45` | `cowrie.log.closed` |
| `2026-07-29 01:35:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25e0436cf22c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:36 |
| **Last Seen** | 2026-07-29 01:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:36:42` | `cowrie.session.connect` |
| `2026-07-29 01:36:42` | `cowrie.client.version` |
| `2026-07-29 01:36:42` | `cowrie.client.kex` |
| `2026-07-29 01:36:44` | `cowrie.login.success` |
| `2026-07-29 01:36:45` | `cowrie.session.params` |
| `2026-07-29 01:36:45` | `cowrie.command.input` |
| `2026-07-29 01:36:45` | `cowrie.command.input` |
| `2026-07-29 01:36:45` | `cowrie.command.input` |
| `2026-07-29 01:36:45` | `cowrie.command.input` |
| `2026-07-29 01:36:45` | `cowrie.command.input` |
| `2026-07-29 01:36:45` | `cowrie.command.success` |
| `2026-07-29 01:36:45` | `cowrie.command.input` |
| `2026-07-29 01:36:45` | `cowrie.command.input` |
| `2026-07-29 01:36:45` | `cowrie.command.input` |
| `2026-07-29 01:36:45` | `cowrie.command.input` |
| `2026-07-29 01:36:45` | `cowrie.log.closed` |
| `2026-07-29 01:36:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b589fcd8473

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:37 |
| **Last Seen** | 2026-07-29 01:37 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:37:34` | `cowrie.session.connect` |
| `2026-07-29 01:37:35` | `cowrie.client.version` |
| `2026-07-29 01:37:35` | `cowrie.client.kex` |
| `2026-07-29 01:37:40` | `cowrie.login.success` |
| `2026-07-29 01:37:45` | `cowrie.session.params` |
| `2026-07-29 01:37:45` | `cowrie.command.input` |
| `2026-07-29 01:37:45` | `cowrie.command.input` |
| `2026-07-29 01:37:45` | `cowrie.command.input` |
| `2026-07-29 01:37:45` | `cowrie.command.input` |
| `2026-07-29 01:37:45` | `cowrie.command.input` |
| `2026-07-29 01:37:45` | `cowrie.command.success` |
| `2026-07-29 01:37:45` | `cowrie.command.input` |
| `2026-07-29 01:37:45` | `cowrie.command.input` |
| `2026-07-29 01:37:45` | `cowrie.command.input` |
| `2026-07-29 01:37:45` | `cowrie.command.input` |
| `2026-07-29 01:37:49` | `cowrie.log.closed` |
| `2026-07-29 01:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f285eb5b71d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:38 |
| **Last Seen** | 2026-07-29 01:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:38:04` | `cowrie.session.connect` |
| `2026-07-29 01:38:04` | `cowrie.client.version` |
| `2026-07-29 01:38:04` | `cowrie.client.kex` |
| `2026-07-29 01:38:06` | `cowrie.login.success` |
| `2026-07-29 01:38:07` | `cowrie.session.params` |
| `2026-07-29 01:38:07` | `cowrie.command.input` |
| `2026-07-29 01:38:07` | `cowrie.command.input` |
| `2026-07-29 01:38:07` | `cowrie.command.input` |
| `2026-07-29 01:38:07` | `cowrie.command.input` |
| `2026-07-29 01:38:07` | `cowrie.command.input` |
| `2026-07-29 01:38:07` | `cowrie.command.success` |
| `2026-07-29 01:38:07` | `cowrie.command.input` |
| `2026-07-29 01:38:07` | `cowrie.command.input` |
| `2026-07-29 01:38:07` | `cowrie.command.input` |
| `2026-07-29 01:38:07` | `cowrie.command.input` |
| `2026-07-29 01:38:08` | `cowrie.log.closed` |
| `2026-07-29 01:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caef830dfccb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:39 |
| **Last Seen** | 2026-07-29 01:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:39:26` | `cowrie.session.connect` |
| `2026-07-29 01:39:27` | `cowrie.client.version` |
| `2026-07-29 01:39:27` | `cowrie.client.kex` |
| `2026-07-29 01:39:28` | `cowrie.login.success` |
| `2026-07-29 01:39:30` | `cowrie.session.params` |
| `2026-07-29 01:39:30` | `cowrie.command.input` |
| `2026-07-29 01:39:30` | `cowrie.command.input` |
| `2026-07-29 01:39:30` | `cowrie.command.input` |
| `2026-07-29 01:39:30` | `cowrie.command.input` |
| `2026-07-29 01:39:30` | `cowrie.command.input` |
| `2026-07-29 01:39:30` | `cowrie.command.success` |
| `2026-07-29 01:39:30` | `cowrie.command.input` |
| `2026-07-29 01:39:30` | `cowrie.command.input` |
| `2026-07-29 01:39:30` | `cowrie.command.input` |
| `2026-07-29 01:39:30` | `cowrie.command.input` |
| `2026-07-29 01:39:30` | `cowrie.log.closed` |
| `2026-07-29 01:39:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e019cc249ae3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:40 |
| **Last Seen** | 2026-07-29 01:40 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:40:00` | `cowrie.session.connect` |
| `2026-07-29 01:40:02` | `cowrie.client.version` |
| `2026-07-29 01:40:02` | `cowrie.client.kex` |
| `2026-07-29 01:40:14` | `cowrie.login.success` |
| `2026-07-29 01:40:31` | `cowrie.session.params` |
| `2026-07-29 01:40:31` | `cowrie.command.input` |
| `2026-07-29 01:40:31` | `cowrie.command.input` |
| `2026-07-29 01:40:31` | `cowrie.command.input` |
| `2026-07-29 01:40:31` | `cowrie.command.input` |
| `2026-07-29 01:40:31` | `cowrie.command.input` |
| `2026-07-29 01:40:31` | `cowrie.command.success` |
| `2026-07-29 01:40:31` | `cowrie.command.input` |
| `2026-07-29 01:40:31` | `cowrie.command.input` |
| `2026-07-29 01:40:31` | `cowrie.command.input` |
| `2026-07-29 01:40:31` | `cowrie.command.input` |
| `2026-07-29 01:40:35` | `cowrie.log.closed` |
| `2026-07-29 01:40:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bba51359bdea

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:40 |
| **Last Seen** | 2026-07-29 01:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:40:50` | `cowrie.session.connect` |
| `2026-07-29 01:40:50` | `cowrie.client.version` |
| `2026-07-29 01:40:50` | `cowrie.client.kex` |
| `2026-07-29 01:40:51` | `cowrie.login.success` |
| `2026-07-29 01:40:53` | `cowrie.session.params` |
| `2026-07-29 01:40:53` | `cowrie.command.input` |
| `2026-07-29 01:40:53` | `cowrie.command.input` |
| `2026-07-29 01:40:53` | `cowrie.command.input` |
| `2026-07-29 01:40:53` | `cowrie.command.input` |
| `2026-07-29 01:40:53` | `cowrie.command.input` |
| `2026-07-29 01:40:53` | `cowrie.command.success` |
| `2026-07-29 01:40:53` | `cowrie.command.input` |
| `2026-07-29 01:40:53` | `cowrie.command.input` |
| `2026-07-29 01:40:53` | `cowrie.command.input` |
| `2026-07-29 01:40:53` | `cowrie.command.input` |
| `2026-07-29 01:40:53` | `cowrie.log.closed` |
| `2026-07-29 01:40:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc728730ae5f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:42 |
| **Last Seen** | 2026-07-29 01:42 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:42:13` | `cowrie.session.connect` |
| `2026-07-29 01:42:15` | `cowrie.client.version` |
| `2026-07-29 01:42:15` | `cowrie.client.kex` |
| `2026-07-29 01:42:28` | `cowrie.login.success` |
| `2026-07-29 01:42:39` | `cowrie.session.params` |
| `2026-07-29 01:42:39` | `cowrie.command.input` |
| `2026-07-29 01:42:39` | `cowrie.command.input` |
| `2026-07-29 01:42:39` | `cowrie.command.input` |
| `2026-07-29 01:42:39` | `cowrie.command.input` |
| `2026-07-29 01:42:39` | `cowrie.command.input` |
| `2026-07-29 01:42:39` | `cowrie.command.success` |
| `2026-07-29 01:42:39` | `cowrie.command.input` |
| `2026-07-29 01:42:39` | `cowrie.command.input` |
| `2026-07-29 01:42:39` | `cowrie.command.input` |
| `2026-07-29 01:42:39` | `cowrie.command.input` |
| `2026-07-29 01:42:39` | `cowrie.log.closed` |
| `2026-07-29 01:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5da2c8a48f41

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:42 |
| **Last Seen** | 2026-07-29 01:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:42:13` | `cowrie.session.connect` |
| `2026-07-29 01:42:13` | `cowrie.client.version` |
| `2026-07-29 01:42:14` | `cowrie.client.kex` |
| `2026-07-29 01:42:15` | `cowrie.login.success` |
| `2026-07-29 01:42:17` | `cowrie.session.params` |
| `2026-07-29 01:42:17` | `cowrie.command.input` |
| `2026-07-29 01:42:17` | `cowrie.command.input` |
| `2026-07-29 01:42:17` | `cowrie.command.input` |
| `2026-07-29 01:42:17` | `cowrie.command.input` |
| `2026-07-29 01:42:17` | `cowrie.command.input` |
| `2026-07-29 01:42:17` | `cowrie.command.success` |
| `2026-07-29 01:42:17` | `cowrie.command.input` |
| `2026-07-29 01:42:17` | `cowrie.command.input` |
| `2026-07-29 01:42:17` | `cowrie.command.input` |
| `2026-07-29 01:42:17` | `cowrie.command.input` |
| `2026-07-29 01:42:17` | `cowrie.log.closed` |
| `2026-07-29 01:42:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06cfcdce774e

| Field | Detail |
|---|---|
| **Source IP** | `94.200.95[.]18` |
| **First Seen** | 2026-07-29 01:42 |
| **Last Seen** | 2026-07-29 01:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:42:22` | `cowrie.session.connect` |
| `2026-07-29 01:42:22` | `cowrie.client.version` |
| `2026-07-29 01:42:22` | `cowrie.client.kex` |
| `2026-07-29 01:42:24` | `cowrie.login.success` |
| `2026-07-29 01:42:24` | `cowrie.direct-tcpip.request` |
| `2026-07-29 01:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.200.95[.]18` to AbuseIPDB if not already reported
- [ ] Block `94.200.95[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e134b99c178

| Field | Detail |
|---|---|
| **Source IP** | `61.12.84[.]172` |
| **First Seen** | 2026-07-29 01:42 |
| **Last Seen** | 2026-07-29 01:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:42:29` | `cowrie.session.connect` |
| `2026-07-29 01:42:30` | `cowrie.client.version` |
| `2026-07-29 01:42:30` | `cowrie.client.kex` |
| `2026-07-29 01:42:31` | `cowrie.login.success` |
| `2026-07-29 01:42:32` | `cowrie.direct-tcpip.request` |
| `2026-07-29 01:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.84[.]172` to AbuseIPDB if not already reported
- [ ] Block `61.12.84[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe107cac9966

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 01:43 |
| **Last Seen** | 2026-07-29 01:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:43:23` | `cowrie.session.connect` |
| `2026-07-29 01:43:23` | `cowrie.client.version` |
| `2026-07-29 01:43:23` | `cowrie.client.kex` |
| `2026-07-29 01:43:24` | `cowrie.login.success` |
| `2026-07-29 01:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b2ec362fcdb

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 01:43 |
| **Last Seen** | 2026-07-29 01:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:43:23` | `cowrie.session.connect` |
| `2026-07-29 01:43:23` | `cowrie.client.version` |
| `2026-07-29 01:43:23` | `cowrie.client.kex` |
| `2026-07-29 01:43:24` | `cowrie.login.success` |
| `2026-07-29 01:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-825390df8b58

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 01:43 |
| **Last Seen** | 2026-07-29 01:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:43:29` | `cowrie.session.connect` |
| `2026-07-29 01:43:29` | `cowrie.client.version` |
| `2026-07-29 01:43:30` | `cowrie.client.kex` |
| `2026-07-29 01:43:30` | `cowrie.login.success` |
| `2026-07-29 01:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d2f945a78b9

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 01:43 |
| **Last Seen** | 2026-07-29 01:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:43:31` | `cowrie.session.connect` |
| `2026-07-29 01:43:31` | `cowrie.client.version` |
| `2026-07-29 01:43:31` | `cowrie.client.kex` |
| `2026-07-29 01:43:31` | `cowrie.login.success` |
| `2026-07-29 01:43:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-139e6eed773a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:43 |
| **Last Seen** | 2026-07-29 01:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:43:38` | `cowrie.session.connect` |
| `2026-07-29 01:43:38` | `cowrie.client.version` |
| `2026-07-29 01:43:38` | `cowrie.client.kex` |
| `2026-07-29 01:43:40` | `cowrie.login.success` |
| `2026-07-29 01:43:41` | `cowrie.session.params` |
| `2026-07-29 01:43:41` | `cowrie.command.input` |
| `2026-07-29 01:43:41` | `cowrie.command.input` |
| `2026-07-29 01:43:41` | `cowrie.command.input` |
| `2026-07-29 01:43:41` | `cowrie.command.input` |
| `2026-07-29 01:43:41` | `cowrie.command.input` |
| `2026-07-29 01:43:41` | `cowrie.command.success` |
| `2026-07-29 01:43:41` | `cowrie.command.input` |
| `2026-07-29 01:43:41` | `cowrie.command.input` |
| `2026-07-29 01:43:41` | `cowrie.command.input` |
| `2026-07-29 01:43:41` | `cowrie.command.input` |
| `2026-07-29 01:43:41` | `cowrie.log.closed` |
| `2026-07-29 01:43:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e188cfdfa15

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:44 |
| **Last Seen** | 2026-07-29 01:44 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:44:10` | `cowrie.session.connect` |
| `2026-07-29 01:44:12` | `cowrie.client.version` |
| `2026-07-29 01:44:12` | `cowrie.client.kex` |
| `2026-07-29 01:44:20` | `cowrie.login.success` |
| `2026-07-29 01:44:26` | `cowrie.session.params` |
| `2026-07-29 01:44:26` | `cowrie.command.input` |
| `2026-07-29 01:44:26` | `cowrie.command.input` |
| `2026-07-29 01:44:26` | `cowrie.command.input` |
| `2026-07-29 01:44:26` | `cowrie.command.input` |
| `2026-07-29 01:44:26` | `cowrie.command.input` |
| `2026-07-29 01:44:26` | `cowrie.command.success` |
| `2026-07-29 01:44:26` | `cowrie.command.input` |
| `2026-07-29 01:44:26` | `cowrie.command.input` |
| `2026-07-29 01:44:26` | `cowrie.command.input` |
| `2026-07-29 01:44:26` | `cowrie.command.input` |
| `2026-07-29 01:44:27` | `cowrie.log.closed` |
| `2026-07-29 01:44:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d9328540234

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:45 |
| **Last Seen** | 2026-07-29 01:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:45:02` | `cowrie.session.connect` |
| `2026-07-29 01:45:02` | `cowrie.client.version` |
| `2026-07-29 01:45:02` | `cowrie.client.kex` |
| `2026-07-29 01:45:04` | `cowrie.login.success` |
| `2026-07-29 01:45:05` | `cowrie.session.params` |
| `2026-07-29 01:45:05` | `cowrie.command.input` |
| `2026-07-29 01:45:05` | `cowrie.command.input` |
| `2026-07-29 01:45:05` | `cowrie.command.input` |
| `2026-07-29 01:45:05` | `cowrie.command.input` |
| `2026-07-29 01:45:05` | `cowrie.command.input` |
| `2026-07-29 01:45:05` | `cowrie.command.success` |
| `2026-07-29 01:45:05` | `cowrie.command.input` |
| `2026-07-29 01:45:05` | `cowrie.command.input` |
| `2026-07-29 01:45:05` | `cowrie.command.input` |
| `2026-07-29 01:45:05` | `cowrie.command.input` |
| `2026-07-29 01:45:06` | `cowrie.log.closed` |
| `2026-07-29 01:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4888e1458dcf

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]92` |
| **First Seen** | 2026-07-29 01:45 |
| **Last Seen** | 2026-07-29 01:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:45:06` | `cowrie.session.connect` |
| `2026-07-29 01:45:07` | `cowrie.login.success` |
| `2026-07-29 01:45:07` | `cowrie.session.params` |
| `2026-07-29 01:45:08` | `cowrie.command.input` |
| `2026-07-29 01:45:08` | `cowrie.command.input` |
| `2026-07-29 01:45:09` | `cowrie.command.input` |
| `2026-07-29 01:45:10` | `cowrie.command.input` |
| `2026-07-29 01:45:10` | `cowrie.command.failed` |
| `2026-07-29 01:45:10` | `cowrie.log.closed` |
| `2026-07-29 01:45:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]92` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2575b53a723e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:46 |
| **Last Seen** | 2026-07-29 01:46 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:46:22` | `cowrie.session.connect` |
| `2026-07-29 01:46:24` | `cowrie.client.version` |
| `2026-07-29 01:46:24` | `cowrie.client.kex` |
| `2026-07-29 01:46:37` | `cowrie.login.success` |
| `2026-07-29 01:46:41` | `cowrie.session.params` |
| `2026-07-29 01:46:41` | `cowrie.command.input` |
| `2026-07-29 01:46:41` | `cowrie.command.input` |
| `2026-07-29 01:46:41` | `cowrie.command.input` |
| `2026-07-29 01:46:41` | `cowrie.command.input` |
| `2026-07-29 01:46:41` | `cowrie.command.input` |
| `2026-07-29 01:46:41` | `cowrie.command.success` |
| `2026-07-29 01:46:41` | `cowrie.command.input` |
| `2026-07-29 01:46:41` | `cowrie.command.input` |
| `2026-07-29 01:46:41` | `cowrie.command.input` |
| `2026-07-29 01:46:41` | `cowrie.command.input` |
| `2026-07-29 01:46:43` | `cowrie.log.closed` |
| `2026-07-29 01:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e216e70c60eb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:46 |
| **Last Seen** | 2026-07-29 01:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:46:26` | `cowrie.session.connect` |
| `2026-07-29 01:46:26` | `cowrie.client.version` |
| `2026-07-29 01:46:26` | `cowrie.client.kex` |
| `2026-07-29 01:46:28` | `cowrie.login.success` |
| `2026-07-29 01:46:29` | `cowrie.session.params` |
| `2026-07-29 01:46:29` | `cowrie.command.input` |
| `2026-07-29 01:46:29` | `cowrie.command.input` |
| `2026-07-29 01:46:29` | `cowrie.command.input` |
| `2026-07-29 01:46:29` | `cowrie.command.input` |
| `2026-07-29 01:46:29` | `cowrie.command.input` |
| `2026-07-29 01:46:29` | `cowrie.command.success` |
| `2026-07-29 01:46:29` | `cowrie.command.input` |
| `2026-07-29 01:46:29` | `cowrie.command.input` |
| `2026-07-29 01:46:29` | `cowrie.command.input` |
| `2026-07-29 01:46:29` | `cowrie.command.input` |
| `2026-07-29 01:46:30` | `cowrie.log.closed` |
| `2026-07-29 01:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0a94917002f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:47 |
| **Last Seen** | 2026-07-29 01:47 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:47:22` | `cowrie.session.connect` |
| `2026-07-29 01:47:24` | `cowrie.client.version` |
| `2026-07-29 01:47:24` | `cowrie.client.kex` |
| `2026-07-29 01:47:37` | `cowrie.login.success` |
| `2026-07-29 01:47:45` | `cowrie.session.params` |
| `2026-07-29 01:47:45` | `cowrie.command.input` |
| `2026-07-29 01:47:45` | `cowrie.command.input` |
| `2026-07-29 01:47:45` | `cowrie.command.input` |
| `2026-07-29 01:47:45` | `cowrie.command.input` |
| `2026-07-29 01:47:45` | `cowrie.command.input` |
| `2026-07-29 01:47:45` | `cowrie.command.success` |
| `2026-07-29 01:47:45` | `cowrie.command.input` |
| `2026-07-29 01:47:45` | `cowrie.command.input` |
| `2026-07-29 01:47:45` | `cowrie.command.input` |
| `2026-07-29 01:47:45` | `cowrie.command.input` |
| `2026-07-29 01:47:45` | `cowrie.log.closed` |
| `2026-07-29 01:47:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e83b44dd094

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:47 |
| **Last Seen** | 2026-07-29 01:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:47:49` | `cowrie.session.connect` |
| `2026-07-29 01:47:49` | `cowrie.client.version` |
| `2026-07-29 01:47:49` | `cowrie.client.kex` |
| `2026-07-29 01:47:51` | `cowrie.login.success` |
| `2026-07-29 01:47:52` | `cowrie.session.params` |
| `2026-07-29 01:47:52` | `cowrie.command.input` |
| `2026-07-29 01:47:52` | `cowrie.command.input` |
| `2026-07-29 01:47:52` | `cowrie.command.input` |
| `2026-07-29 01:47:52` | `cowrie.command.input` |
| `2026-07-29 01:47:52` | `cowrie.command.input` |
| `2026-07-29 01:47:52` | `cowrie.command.success` |
| `2026-07-29 01:47:52` | `cowrie.command.input` |
| `2026-07-29 01:47:52` | `cowrie.command.input` |
| `2026-07-29 01:47:52` | `cowrie.command.input` |
| `2026-07-29 01:47:52` | `cowrie.command.input` |
| `2026-07-29 01:47:53` | `cowrie.log.closed` |
| `2026-07-29 01:47:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cd2cfadcd5b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:48 |
| **Last Seen** | 2026-07-29 01:48 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:48:33` | `cowrie.session.connect` |
| `2026-07-29 01:48:35` | `cowrie.client.version` |
| `2026-07-29 01:48:35` | `cowrie.client.kex` |
| `2026-07-29 01:48:42` | `cowrie.login.success` |
| `2026-07-29 01:48:47` | `cowrie.session.params` |
| `2026-07-29 01:48:47` | `cowrie.command.input` |
| `2026-07-29 01:48:47` | `cowrie.command.input` |
| `2026-07-29 01:48:47` | `cowrie.command.input` |
| `2026-07-29 01:48:47` | `cowrie.command.input` |
| `2026-07-29 01:48:47` | `cowrie.command.input` |
| `2026-07-29 01:48:47` | `cowrie.command.success` |
| `2026-07-29 01:48:47` | `cowrie.command.input` |
| `2026-07-29 01:48:47` | `cowrie.command.input` |
| `2026-07-29 01:48:47` | `cowrie.command.input` |
| `2026-07-29 01:48:47` | `cowrie.command.input` |
| `2026-07-29 01:48:48` | `cowrie.log.closed` |
| `2026-07-29 01:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f814440c1148

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:49 |
| **Last Seen** | 2026-07-29 01:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:49:10` | `cowrie.session.connect` |
| `2026-07-29 01:49:11` | `cowrie.client.version` |
| `2026-07-29 01:49:11` | `cowrie.client.kex` |
| `2026-07-29 01:49:12` | `cowrie.login.success` |
| `2026-07-29 01:49:14` | `cowrie.session.params` |
| `2026-07-29 01:49:14` | `cowrie.command.input` |
| `2026-07-29 01:49:14` | `cowrie.command.input` |
| `2026-07-29 01:49:14` | `cowrie.command.input` |
| `2026-07-29 01:49:14` | `cowrie.command.input` |
| `2026-07-29 01:49:14` | `cowrie.command.input` |
| `2026-07-29 01:49:14` | `cowrie.command.success` |
| `2026-07-29 01:49:14` | `cowrie.command.input` |
| `2026-07-29 01:49:14` | `cowrie.command.input` |
| `2026-07-29 01:49:14` | `cowrie.command.input` |
| `2026-07-29 01:49:14` | `cowrie.command.input` |
| `2026-07-29 01:49:14` | `cowrie.log.closed` |
| `2026-07-29 01:49:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85c0bdb554bc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:49 |
| **Last Seen** | 2026-07-29 01:50 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:49:59` | `cowrie.session.connect` |
| `2026-07-29 01:50:01` | `cowrie.client.version` |
| `2026-07-29 01:50:09` | `cowrie.client.kex` |
| `2026-07-29 01:50:13` | `cowrie.login.success` |
| `2026-07-29 01:50:16` | `cowrie.session.params` |
| `2026-07-29 01:50:16` | `cowrie.command.input` |
| `2026-07-29 01:50:16` | `cowrie.command.input` |
| `2026-07-29 01:50:16` | `cowrie.command.input` |
| `2026-07-29 01:50:16` | `cowrie.command.input` |
| `2026-07-29 01:50:16` | `cowrie.command.input` |
| `2026-07-29 01:50:16` | `cowrie.command.success` |
| `2026-07-29 01:50:16` | `cowrie.command.input` |
| `2026-07-29 01:50:16` | `cowrie.command.input` |
| `2026-07-29 01:50:16` | `cowrie.command.input` |
| `2026-07-29 01:50:16` | `cowrie.command.input` |
| `2026-07-29 01:50:17` | `cowrie.log.closed` |
| `2026-07-29 01:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a5a8ae6631f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:50 |
| **Last Seen** | 2026-07-29 01:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:50:32` | `cowrie.session.connect` |
| `2026-07-29 01:50:32` | `cowrie.client.version` |
| `2026-07-29 01:50:32` | `cowrie.client.kex` |
| `2026-07-29 01:50:33` | `cowrie.login.success` |
| `2026-07-29 01:50:35` | `cowrie.session.params` |
| `2026-07-29 01:50:35` | `cowrie.command.input` |
| `2026-07-29 01:50:35` | `cowrie.command.input` |
| `2026-07-29 01:50:35` | `cowrie.command.input` |
| `2026-07-29 01:50:35` | `cowrie.command.input` |
| `2026-07-29 01:50:35` | `cowrie.command.input` |
| `2026-07-29 01:50:35` | `cowrie.command.success` |
| `2026-07-29 01:50:35` | `cowrie.command.input` |
| `2026-07-29 01:50:35` | `cowrie.command.input` |
| `2026-07-29 01:50:35` | `cowrie.command.input` |
| `2026-07-29 01:50:35` | `cowrie.command.input` |
| `2026-07-29 01:50:35` | `cowrie.log.closed` |
| `2026-07-29 01:50:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9756a92af5e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:51 |
| **Last Seen** | 2026-07-29 01:51 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:51:11` | `cowrie.session.connect` |
| `2026-07-29 01:51:12` | `cowrie.client.version` |
| `2026-07-29 01:51:12` | `cowrie.client.kex` |
| `2026-07-29 01:51:18` | `cowrie.login.success` |
| `2026-07-29 01:51:21` | `cowrie.session.params` |
| `2026-07-29 01:51:21` | `cowrie.command.input` |
| `2026-07-29 01:51:21` | `cowrie.command.input` |
| `2026-07-29 01:51:21` | `cowrie.command.input` |
| `2026-07-29 01:51:21` | `cowrie.command.input` |
| `2026-07-29 01:51:21` | `cowrie.command.input` |
| `2026-07-29 01:51:21` | `cowrie.command.success` |
| `2026-07-29 01:51:21` | `cowrie.command.input` |
| `2026-07-29 01:51:21` | `cowrie.command.input` |
| `2026-07-29 01:51:21` | `cowrie.command.input` |
| `2026-07-29 01:51:21` | `cowrie.command.input` |
| `2026-07-29 01:51:22` | `cowrie.log.closed` |
| `2026-07-29 01:51:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66c41d4f18be

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:51 |
| **Last Seen** | 2026-07-29 01:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:51:55` | `cowrie.session.connect` |
| `2026-07-29 01:51:56` | `cowrie.client.version` |
| `2026-07-29 01:51:56` | `cowrie.client.kex` |
| `2026-07-29 01:51:57` | `cowrie.login.success` |
| `2026-07-29 01:51:59` | `cowrie.session.params` |
| `2026-07-29 01:51:59` | `cowrie.command.input` |
| `2026-07-29 01:51:59` | `cowrie.command.input` |
| `2026-07-29 01:51:59` | `cowrie.command.input` |
| `2026-07-29 01:51:59` | `cowrie.command.input` |
| `2026-07-29 01:51:59` | `cowrie.command.input` |
| `2026-07-29 01:51:59` | `cowrie.command.success` |
| `2026-07-29 01:51:59` | `cowrie.command.input` |
| `2026-07-29 01:51:59` | `cowrie.command.input` |
| `2026-07-29 01:51:59` | `cowrie.command.input` |
| `2026-07-29 01:51:59` | `cowrie.command.input` |
| `2026-07-29 01:52:00` | `cowrie.log.closed` |
| `2026-07-29 01:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9c780d26d8c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:52 |
| **Last Seen** | 2026-07-29 01:52 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:52:03` | `cowrie.session.connect` |
| `2026-07-29 01:52:05` | `cowrie.client.version` |
| `2026-07-29 01:52:05` | `cowrie.client.kex` |
| `2026-07-29 01:52:16` | `cowrie.login.success` |
| `2026-07-29 01:52:22` | `cowrie.session.params` |
| `2026-07-29 01:52:22` | `cowrie.command.input` |
| `2026-07-29 01:52:22` | `cowrie.command.input` |
| `2026-07-29 01:52:22` | `cowrie.command.input` |
| `2026-07-29 01:52:22` | `cowrie.command.input` |
| `2026-07-29 01:52:22` | `cowrie.command.input` |
| `2026-07-29 01:52:22` | `cowrie.command.success` |
| `2026-07-29 01:52:22` | `cowrie.command.input` |
| `2026-07-29 01:52:22` | `cowrie.command.input` |
| `2026-07-29 01:52:22` | `cowrie.command.input` |
| `2026-07-29 01:52:22` | `cowrie.command.input` |
| `2026-07-29 01:52:24` | `cowrie.log.closed` |
| `2026-07-29 01:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8247400e584

| Field | Detail |
|---|---|
| **Source IP** | `220.178.39[.]106` |
| **First Seen** | 2026-07-29 01:52 |
| **Last Seen** | 2026-07-29 01:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:52:10` | `cowrie.session.connect` |
| `2026-07-29 01:52:11` | `cowrie.client.version` |
| `2026-07-29 01:52:11` | `cowrie.client.kex` |
| `2026-07-29 01:52:14` | `cowrie.login.success` |
| `2026-07-29 01:52:14` | `cowrie.direct-tcpip.request` |
| `2026-07-29 01:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.39[.]106` to AbuseIPDB if not already reported
- [ ] Block `220.178.39[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-778b5c4ad14d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:52 |
| **Last Seen** | 2026-07-29 01:53 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:52:53` | `cowrie.session.connect` |
| `2026-07-29 01:52:55` | `cowrie.client.version` |
| `2026-07-29 01:52:55` | `cowrie.client.kex` |
| `2026-07-29 01:53:07` | `cowrie.login.success` |
| `2026-07-29 01:53:13` | `cowrie.session.params` |
| `2026-07-29 01:53:13` | `cowrie.command.input` |
| `2026-07-29 01:53:13` | `cowrie.command.input` |
| `2026-07-29 01:53:13` | `cowrie.command.input` |
| `2026-07-29 01:53:13` | `cowrie.command.input` |
| `2026-07-29 01:53:13` | `cowrie.command.input` |
| `2026-07-29 01:53:13` | `cowrie.command.success` |
| `2026-07-29 01:53:13` | `cowrie.command.input` |
| `2026-07-29 01:53:13` | `cowrie.command.input` |
| `2026-07-29 01:53:13` | `cowrie.command.input` |
| `2026-07-29 01:53:13` | `cowrie.command.input` |
| `2026-07-29 01:53:17` | `cowrie.log.closed` |
| `2026-07-29 01:53:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80fbfd196575

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:53 |
| **Last Seen** | 2026-07-29 01:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:53:20` | `cowrie.session.connect` |
| `2026-07-29 01:53:21` | `cowrie.client.version` |
| `2026-07-29 01:53:21` | `cowrie.client.kex` |
| `2026-07-29 01:53:22` | `cowrie.login.success` |
| `2026-07-29 01:53:24` | `cowrie.session.params` |
| `2026-07-29 01:53:24` | `cowrie.command.input` |
| `2026-07-29 01:53:24` | `cowrie.command.input` |
| `2026-07-29 01:53:24` | `cowrie.command.input` |
| `2026-07-29 01:53:24` | `cowrie.command.input` |
| `2026-07-29 01:53:24` | `cowrie.command.input` |
| `2026-07-29 01:53:24` | `cowrie.command.success` |
| `2026-07-29 01:53:24` | `cowrie.command.input` |
| `2026-07-29 01:53:24` | `cowrie.command.input` |
| `2026-07-29 01:53:24` | `cowrie.command.input` |
| `2026-07-29 01:53:24` | `cowrie.command.input` |
| `2026-07-29 01:53:24` | `cowrie.log.closed` |
| `2026-07-29 01:53:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f7f1e054de6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:53 |
| **Last Seen** | 2026-07-29 01:54 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:53:43` | `cowrie.session.connect` |
| `2026-07-29 01:53:45` | `cowrie.client.version` |
| `2026-07-29 01:53:45` | `cowrie.client.kex` |
| `2026-07-29 01:53:56` | `cowrie.login.success` |
| `2026-07-29 01:53:59` | `cowrie.session.params` |
| `2026-07-29 01:53:59` | `cowrie.command.input` |
| `2026-07-29 01:53:59` | `cowrie.command.input` |
| `2026-07-29 01:53:59` | `cowrie.command.input` |
| `2026-07-29 01:53:59` | `cowrie.command.input` |
| `2026-07-29 01:53:59` | `cowrie.command.input` |
| `2026-07-29 01:53:59` | `cowrie.command.success` |
| `2026-07-29 01:53:59` | `cowrie.command.input` |
| `2026-07-29 01:53:59` | `cowrie.command.input` |
| `2026-07-29 01:53:59` | `cowrie.command.input` |
| `2026-07-29 01:53:59` | `cowrie.command.input` |
| `2026-07-29 01:54:00` | `cowrie.log.closed` |
| `2026-07-29 01:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5a3026f28a5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:54 |
| **Last Seen** | 2026-07-29 01:55 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:54:33` | `cowrie.session.connect` |
| `2026-07-29 01:54:34` | `cowrie.client.version` |
| `2026-07-29 01:54:34` | `cowrie.client.kex` |
| `2026-07-29 01:54:47` | `cowrie.login.success` |
| `2026-07-29 01:54:54` | `cowrie.session.params` |
| `2026-07-29 01:54:54` | `cowrie.command.input` |
| `2026-07-29 01:54:54` | `cowrie.command.input` |
| `2026-07-29 01:54:54` | `cowrie.command.input` |
| `2026-07-29 01:54:54` | `cowrie.command.input` |
| `2026-07-29 01:54:54` | `cowrie.command.input` |
| `2026-07-29 01:54:54` | `cowrie.command.success` |
| `2026-07-29 01:54:54` | `cowrie.command.input` |
| `2026-07-29 01:54:54` | `cowrie.command.input` |
| `2026-07-29 01:54:54` | `cowrie.command.input` |
| `2026-07-29 01:54:54` | `cowrie.command.input` |
| `2026-07-29 01:54:58` | `cowrie.log.closed` |
| `2026-07-29 01:55:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bf1896fbe9b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:54 |
| **Last Seen** | 2026-07-29 01:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:54:42` | `cowrie.session.connect` |
| `2026-07-29 01:54:42` | `cowrie.client.version` |
| `2026-07-29 01:54:42` | `cowrie.client.kex` |
| `2026-07-29 01:54:43` | `cowrie.login.success` |
| `2026-07-29 01:54:45` | `cowrie.session.params` |
| `2026-07-29 01:54:45` | `cowrie.command.input` |
| `2026-07-29 01:54:45` | `cowrie.command.input` |
| `2026-07-29 01:54:45` | `cowrie.command.input` |
| `2026-07-29 01:54:45` | `cowrie.command.input` |
| `2026-07-29 01:54:45` | `cowrie.command.input` |
| `2026-07-29 01:54:45` | `cowrie.command.success` |
| `2026-07-29 01:54:45` | `cowrie.command.input` |
| `2026-07-29 01:54:45` | `cowrie.command.input` |
| `2026-07-29 01:54:45` | `cowrie.command.input` |
| `2026-07-29 01:54:45` | `cowrie.command.input` |
| `2026-07-29 01:54:45` | `cowrie.log.closed` |
| `2026-07-29 01:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bce8f8a487af

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:55 |
| **Last Seen** | 2026-07-29 01:55 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:55:36` | `cowrie.session.connect` |
| `2026-07-29 01:55:36` | `cowrie.client.version` |
| `2026-07-29 01:55:39` | `cowrie.client.kex` |
| `2026-07-29 01:55:45` | `cowrie.login.success` |
| `2026-07-29 01:55:51` | `cowrie.session.params` |
| `2026-07-29 01:55:51` | `cowrie.command.input` |
| `2026-07-29 01:55:51` | `cowrie.command.input` |
| `2026-07-29 01:55:51` | `cowrie.command.input` |
| `2026-07-29 01:55:51` | `cowrie.command.input` |
| `2026-07-29 01:55:51` | `cowrie.command.input` |
| `2026-07-29 01:55:51` | `cowrie.command.success` |
| `2026-07-29 01:55:51` | `cowrie.command.input` |
| `2026-07-29 01:55:51` | `cowrie.command.input` |
| `2026-07-29 01:55:51` | `cowrie.command.input` |
| `2026-07-29 01:55:51` | `cowrie.command.input` |
| `2026-07-29 01:55:53` | `cowrie.log.closed` |
| `2026-07-29 01:55:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4fdc51c1b76

| Field | Detail |
|---|---|
| **Source IP** | `218.202.143[.]68` |
| **First Seen** | 2026-07-29 01:55 |
| **Last Seen** | 2026-07-29 01:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:55:37` | `cowrie.session.connect` |
| `2026-07-29 01:55:38` | `cowrie.client.version` |
| `2026-07-29 01:55:38` | `cowrie.client.kex` |
| `2026-07-29 01:55:40` | `cowrie.login.success` |
| `2026-07-29 01:55:41` | `cowrie.direct-tcpip.request` |
| `2026-07-29 01:55:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.202.143[.]68` to AbuseIPDB if not already reported
- [ ] Block `218.202.143[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-724e9318179d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:56 |
| **Last Seen** | 2026-07-29 01:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:56:05` | `cowrie.session.connect` |
| `2026-07-29 01:56:06` | `cowrie.client.version` |
| `2026-07-29 01:56:06` | `cowrie.client.kex` |
| `2026-07-29 01:56:06` | `cowrie.login.success` |
| `2026-07-29 01:56:07` | `cowrie.session.params` |
| `2026-07-29 01:56:07` | `cowrie.command.input` |
| `2026-07-29 01:56:07` | `cowrie.command.input` |
| `2026-07-29 01:56:07` | `cowrie.command.input` |
| `2026-07-29 01:56:07` | `cowrie.command.input` |
| `2026-07-29 01:56:07` | `cowrie.command.input` |
| `2026-07-29 01:56:07` | `cowrie.command.success` |
| `2026-07-29 01:56:07` | `cowrie.command.input` |
| `2026-07-29 01:56:07` | `cowrie.command.input` |
| `2026-07-29 01:56:07` | `cowrie.command.input` |
| `2026-07-29 01:56:07` | `cowrie.command.input` |
| `2026-07-29 01:56:08` | `cowrie.log.closed` |
| `2026-07-29 01:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06af9f450d92

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:56 |
| **Last Seen** | 2026-07-29 01:56 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:56:31` | `cowrie.session.connect` |
| `2026-07-29 01:56:32` | `cowrie.client.version` |
| `2026-07-29 01:56:32` | `cowrie.client.kex` |
| `2026-07-29 01:56:43` | `cowrie.login.success` |
| `2026-07-29 01:56:48` | `cowrie.session.params` |
| `2026-07-29 01:56:48` | `cowrie.command.input` |
| `2026-07-29 01:56:48` | `cowrie.command.input` |
| `2026-07-29 01:56:48` | `cowrie.command.input` |
| `2026-07-29 01:56:48` | `cowrie.command.input` |
| `2026-07-29 01:56:48` | `cowrie.command.input` |
| `2026-07-29 01:56:48` | `cowrie.command.success` |
| `2026-07-29 01:56:48` | `cowrie.command.input` |
| `2026-07-29 01:56:48` | `cowrie.command.input` |
| `2026-07-29 01:56:48` | `cowrie.command.input` |
| `2026-07-29 01:56:48` | `cowrie.command.input` |
| `2026-07-29 01:56:49` | `cowrie.log.closed` |
| `2026-07-29 01:56:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fea601a7fcfa

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:57 |
| **Last Seen** | 2026-07-29 01:57 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:57:15` | `cowrie.session.connect` |
| `2026-07-29 01:57:18` | `cowrie.client.version` |
| `2026-07-29 01:57:18` | `cowrie.client.kex` |
| `2026-07-29 01:57:26` | `cowrie.login.success` |
| `2026-07-29 01:57:30` | `cowrie.session.params` |
| `2026-07-29 01:57:30` | `cowrie.command.input` |
| `2026-07-29 01:57:30` | `cowrie.command.input` |
| `2026-07-29 01:57:30` | `cowrie.command.input` |
| `2026-07-29 01:57:30` | `cowrie.command.input` |
| `2026-07-29 01:57:30` | `cowrie.command.input` |
| `2026-07-29 01:57:30` | `cowrie.command.success` |
| `2026-07-29 01:57:30` | `cowrie.command.input` |
| `2026-07-29 01:57:30` | `cowrie.command.input` |
| `2026-07-29 01:57:30` | `cowrie.command.input` |
| `2026-07-29 01:57:30` | `cowrie.command.input` |
| `2026-07-29 01:57:32` | `cowrie.log.closed` |
| `2026-07-29 01:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6fa7d229395

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:57 |
| **Last Seen** | 2026-07-29 01:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:57:29` | `cowrie.session.connect` |
| `2026-07-29 01:57:29` | `cowrie.client.version` |
| `2026-07-29 01:57:29` | `cowrie.client.kex` |
| `2026-07-29 01:57:31` | `cowrie.login.success` |
| `2026-07-29 01:57:33` | `cowrie.session.params` |
| `2026-07-29 01:57:33` | `cowrie.command.input` |
| `2026-07-29 01:57:33` | `cowrie.command.input` |
| `2026-07-29 01:57:33` | `cowrie.command.input` |
| `2026-07-29 01:57:33` | `cowrie.command.input` |
| `2026-07-29 01:57:33` | `cowrie.command.input` |
| `2026-07-29 01:57:33` | `cowrie.command.success` |
| `2026-07-29 01:57:33` | `cowrie.command.input` |
| `2026-07-29 01:57:33` | `cowrie.command.input` |
| `2026-07-29 01:57:33` | `cowrie.command.input` |
| `2026-07-29 01:57:33` | `cowrie.command.input` |
| `2026-07-29 01:57:33` | `cowrie.log.closed` |
| `2026-07-29 01:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7f45cbe6e88

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-29 01:58 |
| **Last Seen** | 2026-07-29 01:58 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:58:06` | `cowrie.session.connect` |
| `2026-07-29 01:58:08` | `cowrie.client.version` |
| `2026-07-29 01:58:08` | `cowrie.client.kex` |
| `2026-07-29 01:58:19` | `cowrie.login.success` |
| `2026-07-29 01:58:27` | `cowrie.session.params` |
| `2026-07-29 01:58:27` | `cowrie.command.input` |
| `2026-07-29 01:58:27` | `cowrie.command.input` |
| `2026-07-29 01:58:27` | `cowrie.command.input` |
| `2026-07-29 01:58:27` | `cowrie.command.input` |
| `2026-07-29 01:58:27` | `cowrie.command.input` |
| `2026-07-29 01:58:27` | `cowrie.command.success` |
| `2026-07-29 01:58:27` | `cowrie.command.input` |
| `2026-07-29 01:58:27` | `cowrie.command.input` |
| `2026-07-29 01:58:27` | `cowrie.command.input` |
| `2026-07-29 01:58:27` | `cowrie.command.input` |
| `2026-07-29 01:58:31` | `cowrie.log.closed` |
| `2026-07-29 01:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54193cfab187

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 01:58 |
| **Last Seen** | 2026-07-29 01:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 01:58:52` | `cowrie.session.connect` |
| `2026-07-29 01:58:52` | `cowrie.client.version` |
| `2026-07-29 01:58:52` | `cowrie.client.kex` |
| `2026-07-29 01:58:54` | `cowrie.login.success` |
| `2026-07-29 01:58:55` | `cowrie.session.params` |
| `2026-07-29 01:58:55` | `cowrie.command.input` |
| `2026-07-29 01:58:55` | `cowrie.command.input` |
| `2026-07-29 01:58:55` | `cowrie.command.input` |
| `2026-07-29 01:58:55` | `cowrie.command.input` |
| `2026-07-29 01:58:55` | `cowrie.command.input` |
| `2026-07-29 01:58:55` | `cowrie.command.success` |
| `2026-07-29 01:58:55` | `cowrie.command.input` |
| `2026-07-29 01:58:55` | `cowrie.command.input` |
| `2026-07-29 01:58:55` | `cowrie.command.input` |
| `2026-07-29 01:58:55` | `cowrie.command.input` |
| `2026-07-29 01:58:56` | `cowrie.log.closed` |
| `2026-07-29 01:58:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91c2d86373d8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:00 |
| **Last Seen** | 2026-07-29 02:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:00:13` | `cowrie.session.connect` |
| `2026-07-29 02:00:13` | `cowrie.client.version` |
| `2026-07-29 02:00:13` | `cowrie.client.kex` |
| `2026-07-29 02:00:15` | `cowrie.login.success` |
| `2026-07-29 02:00:16` | `cowrie.session.params` |
| `2026-07-29 02:00:16` | `cowrie.command.input` |
| `2026-07-29 02:00:16` | `cowrie.command.input` |
| `2026-07-29 02:00:16` | `cowrie.command.input` |
| `2026-07-29 02:00:16` | `cowrie.command.input` |
| `2026-07-29 02:00:16` | `cowrie.command.input` |
| `2026-07-29 02:00:16` | `cowrie.command.success` |
| `2026-07-29 02:00:16` | `cowrie.command.input` |
| `2026-07-29 02:00:16` | `cowrie.command.input` |
| `2026-07-29 02:00:16` | `cowrie.command.input` |
| `2026-07-29 02:00:16` | `cowrie.command.input` |
| `2026-07-29 02:00:17` | `cowrie.log.closed` |
| `2026-07-29 02:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d0da2ab5c06

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:01 |
| **Last Seen** | 2026-07-29 02:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:01:35` | `cowrie.session.connect` |
| `2026-07-29 02:01:35` | `cowrie.client.version` |
| `2026-07-29 02:01:35` | `cowrie.client.kex` |
| `2026-07-29 02:01:37` | `cowrie.login.success` |
| `2026-07-29 02:01:39` | `cowrie.session.params` |
| `2026-07-29 02:01:39` | `cowrie.command.input` |
| `2026-07-29 02:01:39` | `cowrie.command.input` |
| `2026-07-29 02:01:39` | `cowrie.command.input` |
| `2026-07-29 02:01:39` | `cowrie.command.input` |
| `2026-07-29 02:01:39` | `cowrie.command.input` |
| `2026-07-29 02:01:39` | `cowrie.command.success` |
| `2026-07-29 02:01:39` | `cowrie.command.input` |
| `2026-07-29 02:01:39` | `cowrie.command.input` |
| `2026-07-29 02:01:39` | `cowrie.command.input` |
| `2026-07-29 02:01:39` | `cowrie.command.input` |
| `2026-07-29 02:01:40` | `cowrie.log.closed` |
| `2026-07-29 02:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4a6cd0e5ab9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:02 |
| **Last Seen** | 2026-07-29 02:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:02:57` | `cowrie.session.connect` |
| `2026-07-29 02:02:57` | `cowrie.client.version` |
| `2026-07-29 02:02:57` | `cowrie.client.kex` |
| `2026-07-29 02:02:59` | `cowrie.login.success` |
| `2026-07-29 02:03:00` | `cowrie.session.params` |
| `2026-07-29 02:03:00` | `cowrie.command.input` |
| `2026-07-29 02:03:00` | `cowrie.command.input` |
| `2026-07-29 02:03:00` | `cowrie.command.input` |
| `2026-07-29 02:03:00` | `cowrie.command.input` |
| `2026-07-29 02:03:00` | `cowrie.command.input` |
| `2026-07-29 02:03:00` | `cowrie.command.success` |
| `2026-07-29 02:03:00` | `cowrie.command.input` |
| `2026-07-29 02:03:00` | `cowrie.command.input` |
| `2026-07-29 02:03:00` | `cowrie.command.input` |
| `2026-07-29 02:03:00` | `cowrie.command.input` |
| `2026-07-29 02:03:00` | `cowrie.log.closed` |
| `2026-07-29 02:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b48921b07485

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:04 |
| **Last Seen** | 2026-07-29 02:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:04:21` | `cowrie.session.connect` |
| `2026-07-29 02:04:21` | `cowrie.client.version` |
| `2026-07-29 02:04:21` | `cowrie.client.kex` |
| `2026-07-29 02:04:22` | `cowrie.login.success` |
| `2026-07-29 02:04:24` | `cowrie.session.params` |
| `2026-07-29 02:04:24` | `cowrie.command.input` |
| `2026-07-29 02:04:24` | `cowrie.command.input` |
| `2026-07-29 02:04:24` | `cowrie.command.input` |
| `2026-07-29 02:04:24` | `cowrie.command.input` |
| `2026-07-29 02:04:24` | `cowrie.command.input` |
| `2026-07-29 02:04:24` | `cowrie.command.success` |
| `2026-07-29 02:04:24` | `cowrie.command.input` |
| `2026-07-29 02:04:24` | `cowrie.command.input` |
| `2026-07-29 02:04:24` | `cowrie.command.input` |
| `2026-07-29 02:04:24` | `cowrie.command.input` |
| `2026-07-29 02:04:24` | `cowrie.log.closed` |
| `2026-07-29 02:04:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-189890d9ec9a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:05 |
| **Last Seen** | 2026-07-29 02:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:05:44` | `cowrie.session.connect` |
| `2026-07-29 02:05:44` | `cowrie.client.version` |
| `2026-07-29 02:05:44` | `cowrie.client.kex` |
| `2026-07-29 02:05:45` | `cowrie.login.success` |
| `2026-07-29 02:05:47` | `cowrie.session.params` |
| `2026-07-29 02:05:47` | `cowrie.command.input` |
| `2026-07-29 02:05:47` | `cowrie.command.input` |
| `2026-07-29 02:05:47` | `cowrie.command.input` |
| `2026-07-29 02:05:47` | `cowrie.command.input` |
| `2026-07-29 02:05:47` | `cowrie.command.input` |
| `2026-07-29 02:05:47` | `cowrie.command.success` |
| `2026-07-29 02:05:47` | `cowrie.command.input` |
| `2026-07-29 02:05:47` | `cowrie.command.input` |
| `2026-07-29 02:05:47` | `cowrie.command.input` |
| `2026-07-29 02:05:47` | `cowrie.command.input` |
| `2026-07-29 02:05:47` | `cowrie.log.closed` |
| `2026-07-29 02:05:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fee36083b386

| Field | Detail |
|---|---|
| **Source IP** | `27.223.98[.]117` |
| **First Seen** | 2026-07-29 02:06 |
| **Last Seen** | 2026-07-29 02:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:06:33` | `cowrie.session.connect` |
| `2026-07-29 02:06:34` | `cowrie.client.version` |
| `2026-07-29 02:06:34` | `cowrie.client.kex` |
| `2026-07-29 02:06:35` | `cowrie.login.success` |
| `2026-07-29 02:06:36` | `cowrie.direct-tcpip.request` |
| `2026-07-29 02:06:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.223.98[.]117` to AbuseIPDB if not already reported
- [ ] Block `27.223.98[.]117` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-743af82c6ee0

| Field | Detail |
|---|---|
| **Source IP** | `182.76.71[.]82` |
| **First Seen** | 2026-07-29 02:06 |
| **Last Seen** | 2026-07-29 02:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:06:45` | `cowrie.session.connect` |
| `2026-07-29 02:06:46` | `cowrie.client.version` |
| `2026-07-29 02:06:46` | `cowrie.client.kex` |
| `2026-07-29 02:06:48` | `cowrie.login.success` |
| `2026-07-29 02:06:48` | `cowrie.direct-tcpip.request` |
| `2026-07-29 02:06:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.71[.]82` to AbuseIPDB if not already reported
- [ ] Block `182.76.71[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a52bc3f27579

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:07 |
| **Last Seen** | 2026-07-29 02:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:07:10` | `cowrie.session.connect` |
| `2026-07-29 02:07:10` | `cowrie.client.version` |
| `2026-07-29 02:07:10` | `cowrie.client.kex` |
| `2026-07-29 02:07:12` | `cowrie.login.success` |
| `2026-07-29 02:07:13` | `cowrie.session.params` |
| `2026-07-29 02:07:13` | `cowrie.command.input` |
| `2026-07-29 02:07:13` | `cowrie.command.input` |
| `2026-07-29 02:07:13` | `cowrie.command.input` |
| `2026-07-29 02:07:13` | `cowrie.command.input` |
| `2026-07-29 02:07:13` | `cowrie.command.input` |
| `2026-07-29 02:07:13` | `cowrie.command.success` |
| `2026-07-29 02:07:13` | `cowrie.command.input` |
| `2026-07-29 02:07:13` | `cowrie.command.input` |
| `2026-07-29 02:07:13` | `cowrie.command.input` |
| `2026-07-29 02:07:13` | `cowrie.command.input` |
| `2026-07-29 02:07:13` | `cowrie.log.closed` |
| `2026-07-29 02:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21dcdf749a42

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-29 02:08 |
| **Last Seen** | 2026-07-29 02:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:08:32` | `cowrie.session.connect` |
| `2026-07-29 02:08:32` | `cowrie.client.version` |
| `2026-07-29 02:08:32` | `cowrie.client.kex` |
| `2026-07-29 02:08:33` | `cowrie.login.success` |
| `2026-07-29 02:08:33` | `cowrie.direct-tcpip.request` |
| `2026-07-29 02:08:33` | `cowrie.direct-tcpip.data` |
| `2026-07-29 02:08:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08b9cf7256a6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:08 |
| **Last Seen** | 2026-07-29 02:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:08:34` | `cowrie.session.connect` |
| `2026-07-29 02:08:35` | `cowrie.client.version` |
| `2026-07-29 02:08:35` | `cowrie.client.kex` |
| `2026-07-29 02:08:36` | `cowrie.login.success` |
| `2026-07-29 02:08:37` | `cowrie.session.params` |
| `2026-07-29 02:08:37` | `cowrie.command.input` |
| `2026-07-29 02:08:37` | `cowrie.command.input` |
| `2026-07-29 02:08:37` | `cowrie.command.input` |
| `2026-07-29 02:08:37` | `cowrie.command.input` |
| `2026-07-29 02:08:37` | `cowrie.command.input` |
| `2026-07-29 02:08:37` | `cowrie.command.success` |
| `2026-07-29 02:08:37` | `cowrie.command.input` |
| `2026-07-29 02:08:37` | `cowrie.command.input` |
| `2026-07-29 02:08:37` | `cowrie.command.input` |
| `2026-07-29 02:08:37` | `cowrie.command.input` |
| `2026-07-29 02:08:37` | `cowrie.log.closed` |
| `2026-07-29 02:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10f718fcfec0

| Field | Detail |
|---|---|
| **Source IP** | `117.247.77[.]115` |
| **First Seen** | 2026-07-29 02:09 |
| **Last Seen** | 2026-07-29 02:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:09:54` | `cowrie.session.connect` |
| `2026-07-29 02:09:54` | `cowrie.client.version` |
| `2026-07-29 02:09:54` | `cowrie.client.kex` |
| `2026-07-29 02:09:56` | `cowrie.login.success` |
| `2026-07-29 02:09:57` | `cowrie.direct-tcpip.request` |
| `2026-07-29 02:10:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.77[.]115` to AbuseIPDB if not already reported
- [ ] Block `117.247.77[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd158cdfc339

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:10 |
| **Last Seen** | 2026-07-29 02:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:10:00` | `cowrie.session.connect` |
| `2026-07-29 02:10:01` | `cowrie.client.version` |
| `2026-07-29 02:10:01` | `cowrie.client.kex` |
| `2026-07-29 02:10:02` | `cowrie.login.success` |
| `2026-07-29 02:10:03` | `cowrie.session.params` |
| `2026-07-29 02:10:03` | `cowrie.command.input` |
| `2026-07-29 02:10:03` | `cowrie.command.input` |
| `2026-07-29 02:10:03` | `cowrie.command.input` |
| `2026-07-29 02:10:03` | `cowrie.command.input` |
| `2026-07-29 02:10:03` | `cowrie.command.input` |
| `2026-07-29 02:10:03` | `cowrie.command.success` |
| `2026-07-29 02:10:03` | `cowrie.command.input` |
| `2026-07-29 02:10:03` | `cowrie.command.input` |
| `2026-07-29 02:10:03` | `cowrie.command.input` |
| `2026-07-29 02:10:03` | `cowrie.command.input` |
| `2026-07-29 02:10:03` | `cowrie.log.closed` |
| `2026-07-29 02:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4acee730576a

| Field | Detail |
|---|---|
| **Source IP** | `190.57.233[.]133` |
| **First Seen** | 2026-07-29 02:10 |
| **Last Seen** | 2026-07-29 02:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:10:03` | `cowrie.session.connect` |
| `2026-07-29 02:10:03` | `cowrie.client.version` |
| `2026-07-29 02:10:03` | `cowrie.client.kex` |
| `2026-07-29 02:10:05` | `cowrie.login.success` |
| `2026-07-29 02:10:06` | `cowrie.direct-tcpip.request` |
| `2026-07-29 02:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.57.233[.]133` to AbuseIPDB if not already reported
- [ ] Block `190.57.233[.]133` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75c5b22dbe50

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:11 |
| **Last Seen** | 2026-07-29 02:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:11:28` | `cowrie.session.connect` |
| `2026-07-29 02:11:29` | `cowrie.client.version` |
| `2026-07-29 02:11:29` | `cowrie.client.kex` |
| `2026-07-29 02:11:30` | `cowrie.login.success` |
| `2026-07-29 02:11:31` | `cowrie.session.params` |
| `2026-07-29 02:11:31` | `cowrie.command.input` |
| `2026-07-29 02:11:31` | `cowrie.command.input` |
| `2026-07-29 02:11:31` | `cowrie.command.input` |
| `2026-07-29 02:11:31` | `cowrie.command.input` |
| `2026-07-29 02:11:31` | `cowrie.command.input` |
| `2026-07-29 02:11:31` | `cowrie.command.success` |
| `2026-07-29 02:11:31` | `cowrie.command.input` |
| `2026-07-29 02:11:31` | `cowrie.command.input` |
| `2026-07-29 02:11:31` | `cowrie.command.input` |
| `2026-07-29 02:11:31` | `cowrie.command.input` |
| `2026-07-29 02:11:32` | `cowrie.log.closed` |
| `2026-07-29 02:11:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50e1a9026386

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:12 |
| **Last Seen** | 2026-07-29 02:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:12:55` | `cowrie.session.connect` |
| `2026-07-29 02:12:55` | `cowrie.client.version` |
| `2026-07-29 02:12:55` | `cowrie.client.kex` |
| `2026-07-29 02:12:56` | `cowrie.login.success` |
| `2026-07-29 02:12:58` | `cowrie.session.params` |
| `2026-07-29 02:12:58` | `cowrie.command.input` |
| `2026-07-29 02:12:58` | `cowrie.command.input` |
| `2026-07-29 02:12:58` | `cowrie.command.input` |
| `2026-07-29 02:12:58` | `cowrie.command.input` |
| `2026-07-29 02:12:58` | `cowrie.command.input` |
| `2026-07-29 02:12:58` | `cowrie.command.success` |
| `2026-07-29 02:12:58` | `cowrie.command.input` |
| `2026-07-29 02:12:58` | `cowrie.command.input` |
| `2026-07-29 02:12:58` | `cowrie.command.input` |
| `2026-07-29 02:12:58` | `cowrie.command.input` |
| `2026-07-29 02:12:58` | `cowrie.log.closed` |
| `2026-07-29 02:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02b66f67b574

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-29 02:13 |
| **Last Seen** | 2026-07-29 02:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:13:46` | `cowrie.session.connect` |
| `2026-07-29 02:13:46` | `cowrie.client.version` |
| `2026-07-29 02:13:47` | `cowrie.client.kex` |
| `2026-07-29 02:13:47` | `cowrie.login.success` |
| `2026-07-29 02:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-495f1abe2d28

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-29 02:13 |
| **Last Seen** | 2026-07-29 02:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:13:47` | `cowrie.session.connect` |
| `2026-07-29 02:13:47` | `cowrie.client.version` |
| `2026-07-29 02:13:47` | `cowrie.client.kex` |
| `2026-07-29 02:13:48` | `cowrie.login.success` |
| `2026-07-29 02:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5357ebfec1cb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:14 |
| **Last Seen** | 2026-07-29 02:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:14:17` | `cowrie.session.connect` |
| `2026-07-29 02:14:18` | `cowrie.client.version` |
| `2026-07-29 02:14:18` | `cowrie.client.kex` |
| `2026-07-29 02:14:19` | `cowrie.login.success` |
| `2026-07-29 02:14:20` | `cowrie.session.params` |
| `2026-07-29 02:14:20` | `cowrie.command.input` |
| `2026-07-29 02:14:20` | `cowrie.command.input` |
| `2026-07-29 02:14:20` | `cowrie.command.input` |
| `2026-07-29 02:14:20` | `cowrie.command.input` |
| `2026-07-29 02:14:20` | `cowrie.command.input` |
| `2026-07-29 02:14:20` | `cowrie.command.success` |
| `2026-07-29 02:14:20` | `cowrie.command.input` |
| `2026-07-29 02:14:20` | `cowrie.command.input` |
| `2026-07-29 02:14:20` | `cowrie.command.input` |
| `2026-07-29 02:14:20` | `cowrie.command.input` |
| `2026-07-29 02:14:21` | `cowrie.log.closed` |
| `2026-07-29 02:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-986e6b91db53

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:15 |
| **Last Seen** | 2026-07-29 02:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:15:42` | `cowrie.session.connect` |
| `2026-07-29 02:15:42` | `cowrie.client.version` |
| `2026-07-29 02:15:42` | `cowrie.client.kex` |
| `2026-07-29 02:15:43` | `cowrie.login.success` |
| `2026-07-29 02:15:44` | `cowrie.session.params` |
| `2026-07-29 02:15:44` | `cowrie.command.input` |
| `2026-07-29 02:15:44` | `cowrie.command.input` |
| `2026-07-29 02:15:44` | `cowrie.command.input` |
| `2026-07-29 02:15:44` | `cowrie.command.input` |
| `2026-07-29 02:15:44` | `cowrie.command.input` |
| `2026-07-29 02:15:44` | `cowrie.command.success` |
| `2026-07-29 02:15:44` | `cowrie.command.input` |
| `2026-07-29 02:15:44` | `cowrie.command.input` |
| `2026-07-29 02:15:44` | `cowrie.command.input` |
| `2026-07-29 02:15:44` | `cowrie.command.input` |
| `2026-07-29 02:15:45` | `cowrie.log.closed` |
| `2026-07-29 02:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1966cd2fce30

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:17 |
| **Last Seen** | 2026-07-29 02:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:17:07` | `cowrie.session.connect` |
| `2026-07-29 02:17:07` | `cowrie.client.version` |
| `2026-07-29 02:17:07` | `cowrie.client.kex` |
| `2026-07-29 02:17:08` | `cowrie.login.success` |
| `2026-07-29 02:17:10` | `cowrie.session.params` |
| `2026-07-29 02:17:10` | `cowrie.command.input` |
| `2026-07-29 02:17:10` | `cowrie.command.input` |
| `2026-07-29 02:17:10` | `cowrie.command.input` |
| `2026-07-29 02:17:10` | `cowrie.command.input` |
| `2026-07-29 02:17:10` | `cowrie.command.input` |
| `2026-07-29 02:17:10` | `cowrie.command.success` |
| `2026-07-29 02:17:10` | `cowrie.command.input` |
| `2026-07-29 02:17:10` | `cowrie.command.input` |
| `2026-07-29 02:17:10` | `cowrie.command.input` |
| `2026-07-29 02:17:10` | `cowrie.command.input` |
| `2026-07-29 02:17:10` | `cowrie.log.closed` |
| `2026-07-29 02:17:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3473bcd6e31b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:18 |
| **Last Seen** | 2026-07-29 02:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:18:30` | `cowrie.session.connect` |
| `2026-07-29 02:18:31` | `cowrie.client.version` |
| `2026-07-29 02:18:31` | `cowrie.client.kex` |
| `2026-07-29 02:18:32` | `cowrie.login.success` |
| `2026-07-29 02:18:34` | `cowrie.session.params` |
| `2026-07-29 02:18:34` | `cowrie.command.input` |
| `2026-07-29 02:18:34` | `cowrie.command.input` |
| `2026-07-29 02:18:34` | `cowrie.command.input` |
| `2026-07-29 02:18:34` | `cowrie.command.input` |
| `2026-07-29 02:18:34` | `cowrie.command.input` |
| `2026-07-29 02:18:34` | `cowrie.command.success` |
| `2026-07-29 02:18:34` | `cowrie.command.input` |
| `2026-07-29 02:18:34` | `cowrie.command.input` |
| `2026-07-29 02:18:34` | `cowrie.command.input` |
| `2026-07-29 02:18:34` | `cowrie.command.input` |
| `2026-07-29 02:18:34` | `cowrie.log.closed` |
| `2026-07-29 02:18:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6623354104a4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:19 |
| **Last Seen** | 2026-07-29 02:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:19:54` | `cowrie.session.connect` |
| `2026-07-29 02:19:54` | `cowrie.client.version` |
| `2026-07-29 02:19:54` | `cowrie.client.kex` |
| `2026-07-29 02:19:55` | `cowrie.login.success` |
| `2026-07-29 02:19:57` | `cowrie.session.params` |
| `2026-07-29 02:19:57` | `cowrie.command.input` |
| `2026-07-29 02:19:57` | `cowrie.command.input` |
| `2026-07-29 02:19:57` | `cowrie.command.input` |
| `2026-07-29 02:19:57` | `cowrie.command.input` |
| `2026-07-29 02:19:57` | `cowrie.command.input` |
| `2026-07-29 02:19:57` | `cowrie.command.success` |
| `2026-07-29 02:19:57` | `cowrie.command.input` |
| `2026-07-29 02:19:57` | `cowrie.command.input` |
| `2026-07-29 02:19:57` | `cowrie.command.input` |
| `2026-07-29 02:19:57` | `cowrie.command.input` |
| `2026-07-29 02:19:57` | `cowrie.log.closed` |
| `2026-07-29 02:19:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-912a52c84c60

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:21 |
| **Last Seen** | 2026-07-29 02:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:21:19` | `cowrie.session.connect` |
| `2026-07-29 02:21:19` | `cowrie.client.version` |
| `2026-07-29 02:21:19` | `cowrie.client.kex` |
| `2026-07-29 02:21:20` | `cowrie.login.success` |
| `2026-07-29 02:21:21` | `cowrie.session.params` |
| `2026-07-29 02:21:21` | `cowrie.command.input` |
| `2026-07-29 02:21:21` | `cowrie.command.input` |
| `2026-07-29 02:21:21` | `cowrie.command.input` |
| `2026-07-29 02:21:21` | `cowrie.command.input` |
| `2026-07-29 02:21:21` | `cowrie.command.input` |
| `2026-07-29 02:21:21` | `cowrie.command.success` |
| `2026-07-29 02:21:21` | `cowrie.command.input` |
| `2026-07-29 02:21:21` | `cowrie.command.input` |
| `2026-07-29 02:21:21` | `cowrie.command.input` |
| `2026-07-29 02:21:21` | `cowrie.command.input` |
| `2026-07-29 02:21:22` | `cowrie.log.closed` |
| `2026-07-29 02:21:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6968f64134d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:22 |
| **Last Seen** | 2026-07-29 02:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:22:46` | `cowrie.session.connect` |
| `2026-07-29 02:22:46` | `cowrie.client.version` |
| `2026-07-29 02:22:46` | `cowrie.client.kex` |
| `2026-07-29 02:22:48` | `cowrie.login.success` |
| `2026-07-29 02:22:49` | `cowrie.session.params` |
| `2026-07-29 02:22:49` | `cowrie.command.input` |
| `2026-07-29 02:22:49` | `cowrie.command.input` |
| `2026-07-29 02:22:49` | `cowrie.command.input` |
| `2026-07-29 02:22:49` | `cowrie.command.input` |
| `2026-07-29 02:22:49` | `cowrie.command.input` |
| `2026-07-29 02:22:49` | `cowrie.command.success` |
| `2026-07-29 02:22:49` | `cowrie.command.input` |
| `2026-07-29 02:22:49` | `cowrie.command.input` |
| `2026-07-29 02:22:49` | `cowrie.command.input` |
| `2026-07-29 02:22:49` | `cowrie.command.input` |
| `2026-07-29 02:22:49` | `cowrie.log.closed` |
| `2026-07-29 02:22:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2be0fb76b698

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:24 |
| **Last Seen** | 2026-07-29 02:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:24:11` | `cowrie.session.connect` |
| `2026-07-29 02:24:11` | `cowrie.client.version` |
| `2026-07-29 02:24:11` | `cowrie.client.kex` |
| `2026-07-29 02:24:13` | `cowrie.login.success` |
| `2026-07-29 02:24:15` | `cowrie.session.params` |
| `2026-07-29 02:24:15` | `cowrie.command.input` |
| `2026-07-29 02:24:15` | `cowrie.command.input` |
| `2026-07-29 02:24:15` | `cowrie.command.input` |
| `2026-07-29 02:24:15` | `cowrie.command.input` |
| `2026-07-29 02:24:15` | `cowrie.command.input` |
| `2026-07-29 02:24:15` | `cowrie.command.success` |
| `2026-07-29 02:24:15` | `cowrie.command.input` |
| `2026-07-29 02:24:15` | `cowrie.command.input` |
| `2026-07-29 02:24:15` | `cowrie.command.input` |
| `2026-07-29 02:24:15` | `cowrie.command.input` |
| `2026-07-29 02:24:15` | `cowrie.log.closed` |
| `2026-07-29 02:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e243a413379d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:25 |
| **Last Seen** | 2026-07-29 02:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:25:36` | `cowrie.session.connect` |
| `2026-07-29 02:25:36` | `cowrie.client.version` |
| `2026-07-29 02:25:36` | `cowrie.client.kex` |
| `2026-07-29 02:25:38` | `cowrie.login.success` |
| `2026-07-29 02:25:40` | `cowrie.session.params` |
| `2026-07-29 02:25:40` | `cowrie.command.input` |
| `2026-07-29 02:25:40` | `cowrie.command.input` |
| `2026-07-29 02:25:40` | `cowrie.command.input` |
| `2026-07-29 02:25:40` | `cowrie.command.input` |
| `2026-07-29 02:25:40` | `cowrie.command.input` |
| `2026-07-29 02:25:40` | `cowrie.command.success` |
| `2026-07-29 02:25:40` | `cowrie.command.input` |
| `2026-07-29 02:25:40` | `cowrie.command.input` |
| `2026-07-29 02:25:40` | `cowrie.command.input` |
| `2026-07-29 02:25:40` | `cowrie.command.input` |
| `2026-07-29 02:25:40` | `cowrie.log.closed` |
| `2026-07-29 02:25:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2be8cd929fc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:27 |
| **Last Seen** | 2026-07-29 02:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:27:00` | `cowrie.session.connect` |
| `2026-07-29 02:27:00` | `cowrie.client.version` |
| `2026-07-29 02:27:00` | `cowrie.client.kex` |
| `2026-07-29 02:27:02` | `cowrie.login.success` |
| `2026-07-29 02:27:03` | `cowrie.session.params` |
| `2026-07-29 02:27:03` | `cowrie.command.input` |
| `2026-07-29 02:27:03` | `cowrie.command.input` |
| `2026-07-29 02:27:03` | `cowrie.command.input` |
| `2026-07-29 02:27:03` | `cowrie.command.input` |
| `2026-07-29 02:27:03` | `cowrie.command.input` |
| `2026-07-29 02:27:03` | `cowrie.command.success` |
| `2026-07-29 02:27:03` | `cowrie.command.input` |
| `2026-07-29 02:27:03` | `cowrie.command.input` |
| `2026-07-29 02:27:03` | `cowrie.command.input` |
| `2026-07-29 02:27:03` | `cowrie.command.input` |
| `2026-07-29 02:27:04` | `cowrie.log.closed` |
| `2026-07-29 02:27:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f05ae0ad28a1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:28 |
| **Last Seen** | 2026-07-29 02:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:28:23` | `cowrie.session.connect` |
| `2026-07-29 02:28:23` | `cowrie.client.version` |
| `2026-07-29 02:28:23` | `cowrie.client.kex` |
| `2026-07-29 02:28:24` | `cowrie.login.success` |
| `2026-07-29 02:28:26` | `cowrie.session.params` |
| `2026-07-29 02:28:26` | `cowrie.command.input` |
| `2026-07-29 02:28:26` | `cowrie.command.input` |
| `2026-07-29 02:28:26` | `cowrie.command.input` |
| `2026-07-29 02:28:26` | `cowrie.command.input` |
| `2026-07-29 02:28:26` | `cowrie.command.input` |
| `2026-07-29 02:28:26` | `cowrie.command.success` |
| `2026-07-29 02:28:26` | `cowrie.command.input` |
| `2026-07-29 02:28:26` | `cowrie.command.input` |
| `2026-07-29 02:28:26` | `cowrie.command.input` |
| `2026-07-29 02:28:26` | `cowrie.command.input` |
| `2026-07-29 02:28:27` | `cowrie.log.closed` |
| `2026-07-29 02:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1a4ad837649

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:29 |
| **Last Seen** | 2026-07-29 02:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:29:46` | `cowrie.session.connect` |
| `2026-07-29 02:29:47` | `cowrie.client.version` |
| `2026-07-29 02:29:47` | `cowrie.client.kex` |
| `2026-07-29 02:29:48` | `cowrie.login.success` |
| `2026-07-29 02:29:50` | `cowrie.session.params` |
| `2026-07-29 02:29:50` | `cowrie.command.input` |
| `2026-07-29 02:29:50` | `cowrie.command.input` |
| `2026-07-29 02:29:50` | `cowrie.command.input` |
| `2026-07-29 02:29:50` | `cowrie.command.input` |
| `2026-07-29 02:29:50` | `cowrie.command.input` |
| `2026-07-29 02:29:50` | `cowrie.command.success` |
| `2026-07-29 02:29:50` | `cowrie.command.input` |
| `2026-07-29 02:29:50` | `cowrie.command.input` |
| `2026-07-29 02:29:50` | `cowrie.command.input` |
| `2026-07-29 02:29:50` | `cowrie.command.input` |
| `2026-07-29 02:29:50` | `cowrie.log.closed` |
| `2026-07-29 02:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c7764f888a4

| Field | Detail |
|---|---|
| **Source IP** | `176.170.1[.]244` |
| **First Seen** | 2026-07-29 02:30 |
| **Last Seen** | 2026-07-29 02:31 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:30:58` | `cowrie.session.connect` |
| `2026-07-29 02:31:01` | `cowrie.client.version` |
| `2026-07-29 02:31:01` | `cowrie.client.kex` |
| `2026-07-29 02:31:11` | `cowrie.login.success` |
| `2026-07-29 02:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.170.1[.]244` to AbuseIPDB if not already reported
- [ ] Block `176.170.1[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7da5a2f1e95

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:31 |
| **Last Seen** | 2026-07-29 02:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:31:10` | `cowrie.session.connect` |
| `2026-07-29 02:31:10` | `cowrie.client.version` |
| `2026-07-29 02:31:10` | `cowrie.client.kex` |
| `2026-07-29 02:31:11` | `cowrie.login.success` |
| `2026-07-29 02:31:13` | `cowrie.session.params` |
| `2026-07-29 02:31:13` | `cowrie.command.input` |
| `2026-07-29 02:31:13` | `cowrie.command.input` |
| `2026-07-29 02:31:13` | `cowrie.command.input` |
| `2026-07-29 02:31:13` | `cowrie.command.input` |
| `2026-07-29 02:31:13` | `cowrie.command.input` |
| `2026-07-29 02:31:13` | `cowrie.command.success` |
| `2026-07-29 02:31:13` | `cowrie.command.input` |
| `2026-07-29 02:31:13` | `cowrie.command.input` |
| `2026-07-29 02:31:13` | `cowrie.command.input` |
| `2026-07-29 02:31:13` | `cowrie.command.input` |
| `2026-07-29 02:31:13` | `cowrie.log.closed` |
| `2026-07-29 02:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9ce16fe4a7d

| Field | Detail |
|---|---|
| **Source IP** | `103.120.116[.]162` |
| **First Seen** | 2026-07-29 02:31 |
| **Last Seen** | 2026-07-29 02:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:31:18` | `cowrie.session.connect` |
| `2026-07-29 02:31:19` | `cowrie.client.version` |
| `2026-07-29 02:31:19` | `cowrie.client.kex` |
| `2026-07-29 02:31:20` | `cowrie.login.success` |
| `2026-07-29 02:31:20` | `cowrie.direct-tcpip.request` |
| `2026-07-29 02:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.116[.]162` to AbuseIPDB if not already reported
- [ ] Block `103.120.116[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89336d0fa338

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:32 |
| **Last Seen** | 2026-07-29 02:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:32:33` | `cowrie.session.connect` |
| `2026-07-29 02:32:34` | `cowrie.client.version` |
| `2026-07-29 02:32:34` | `cowrie.client.kex` |
| `2026-07-29 02:32:36` | `cowrie.login.success` |
| `2026-07-29 02:32:37` | `cowrie.session.params` |
| `2026-07-29 02:32:37` | `cowrie.command.input` |
| `2026-07-29 02:32:37` | `cowrie.command.input` |
| `2026-07-29 02:32:37` | `cowrie.command.input` |
| `2026-07-29 02:32:37` | `cowrie.command.input` |
| `2026-07-29 02:32:37` | `cowrie.command.input` |
| `2026-07-29 02:32:37` | `cowrie.command.success` |
| `2026-07-29 02:32:37` | `cowrie.command.input` |
| `2026-07-29 02:32:37` | `cowrie.command.input` |
| `2026-07-29 02:32:37` | `cowrie.command.input` |
| `2026-07-29 02:32:37` | `cowrie.command.input` |
| `2026-07-29 02:32:38` | `cowrie.log.closed` |
| `2026-07-29 02:32:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5233fc367f2

| Field | Detail |
|---|---|
| **Source IP** | `35.195.127[.]65` |
| **First Seen** | 2026-07-29 02:32 |
| **Last Seen** | 2026-07-29 02:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:32:35` | `cowrie.session.connect` |
| `2026-07-29 02:32:35` | `cowrie.login.success` |
| `2026-07-29 02:32:35` | `cowrie.session.params` |
| `2026-07-29 02:32:35` | `cowrie.command.input` |
| `2026-07-29 02:32:35` | `cowrie.command.input` |
| `2026-07-29 02:32:35` | `cowrie.command.failed` |
| `2026-07-29 02:32:36` | `cowrie.command.input` |
| `2026-07-29 02:32:36` | `cowrie.log.closed` |
| `2026-07-29 02:32:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.127[.]65` to AbuseIPDB if not already reported
- [ ] Block `35.195.127[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e511daefd27

| Field | Detail |
|---|---|
| **Source IP** | `35.195.127[.]65` |
| **First Seen** | 2026-07-29 02:32 |
| **Last Seen** | 2026-07-29 02:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:32:43` | `cowrie.session.connect` |
| `2026-07-29 02:32:43` | `cowrie.login.success` |
| `2026-07-29 02:32:44` | `cowrie.session.params` |
| `2026-07-29 02:32:44` | `cowrie.command.input` |
| `2026-07-29 02:32:44` | `cowrie.command.failed` |
| `2026-07-29 02:32:51` | `cowrie.log.closed` |
| `2026-07-29 02:32:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.127[.]65` to AbuseIPDB if not already reported
- [ ] Block `35.195.127[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e9ef34e1465

| Field | Detail |
|---|---|
| **Source IP** | `35.195.127[.]65` |
| **First Seen** | 2026-07-29 02:32 |
| **Last Seen** | 2026-07-29 02:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:32:45` | `cowrie.session.connect` |
| `2026-07-29 02:32:45` | `cowrie.login.success` |
| `2026-07-29 02:32:46` | `cowrie.session.params` |
| `2026-07-29 02:32:46` | `cowrie.command.input` |
| `2026-07-29 02:32:51` | `cowrie.log.closed` |
| `2026-07-29 02:32:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.127[.]65` to AbuseIPDB if not already reported
- [ ] Block `35.195.127[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bc5af9b5aaf

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:33 |
| **Last Seen** | 2026-07-29 02:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:33:54` | `cowrie.session.connect` |
| `2026-07-29 02:33:54` | `cowrie.client.version` |
| `2026-07-29 02:33:54` | `cowrie.client.kex` |
| `2026-07-29 02:33:55` | `cowrie.login.success` |
| `2026-07-29 02:33:56` | `cowrie.session.params` |
| `2026-07-29 02:33:56` | `cowrie.command.input` |
| `2026-07-29 02:33:57` | `cowrie.command.input` |
| `2026-07-29 02:33:57` | `cowrie.command.input` |
| `2026-07-29 02:33:57` | `cowrie.command.input` |
| `2026-07-29 02:33:57` | `cowrie.command.input` |
| `2026-07-29 02:33:57` | `cowrie.command.success` |
| `2026-07-29 02:33:57` | `cowrie.command.input` |
| `2026-07-29 02:33:57` | `cowrie.command.input` |
| `2026-07-29 02:33:57` | `cowrie.command.input` |
| `2026-07-29 02:33:57` | `cowrie.command.input` |
| `2026-07-29 02:33:57` | `cowrie.log.closed` |
| `2026-07-29 02:33:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57fdec6949fe

| Field | Detail |
|---|---|
| **Source IP** | `65.49.20[.]69` |
| **First Seen** | 2026-07-29 02:34 |
| **Last Seen** | 2026-07-29 02:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:34:17` | `cowrie.session.connect` |
| `2026-07-29 02:34:17` | `cowrie.login.success` |
| `2026-07-29 02:34:18` | `cowrie.session.params` |
| `2026-07-29 02:34:18` | `cowrie.command.input` |
| `2026-07-29 02:34:18` | `cowrie.command.input` |
| `2026-07-29 02:34:18` | `cowrie.command.failed` |
| `2026-07-29 02:34:18` | `cowrie.command.input` |
| `2026-07-29 02:34:18` | `cowrie.command.failed` |
| `2026-07-29 02:34:18` | `cowrie.command.input` |
| `2026-07-29 02:34:18` | `cowrie.log.closed` |
| `2026-07-29 02:34:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.49.20[.]69` to AbuseIPDB if not already reported
- [ ] Block `65.49.20[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4f8470607b1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:35 |
| **Last Seen** | 2026-07-29 02:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:35:16` | `cowrie.session.connect` |
| `2026-07-29 02:35:16` | `cowrie.client.version` |
| `2026-07-29 02:35:16` | `cowrie.client.kex` |
| `2026-07-29 02:35:17` | `cowrie.login.success` |
| `2026-07-29 02:35:19` | `cowrie.session.params` |
| `2026-07-29 02:35:19` | `cowrie.command.input` |
| `2026-07-29 02:35:19` | `cowrie.command.input` |
| `2026-07-29 02:35:19` | `cowrie.command.input` |
| `2026-07-29 02:35:19` | `cowrie.command.input` |
| `2026-07-29 02:35:19` | `cowrie.command.input` |
| `2026-07-29 02:35:19` | `cowrie.command.success` |
| `2026-07-29 02:35:19` | `cowrie.command.input` |
| `2026-07-29 02:35:19` | `cowrie.command.input` |
| `2026-07-29 02:35:19` | `cowrie.command.input` |
| `2026-07-29 02:35:19` | `cowrie.command.input` |
| `2026-07-29 02:35:19` | `cowrie.log.closed` |
| `2026-07-29 02:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8814af1e0cc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:36 |
| **Last Seen** | 2026-07-29 02:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:36:38` | `cowrie.session.connect` |
| `2026-07-29 02:36:39` | `cowrie.client.version` |
| `2026-07-29 02:36:39` | `cowrie.client.kex` |
| `2026-07-29 02:36:40` | `cowrie.login.success` |
| `2026-07-29 02:36:42` | `cowrie.session.params` |
| `2026-07-29 02:36:42` | `cowrie.command.input` |
| `2026-07-29 02:36:42` | `cowrie.command.input` |
| `2026-07-29 02:36:42` | `cowrie.command.input` |
| `2026-07-29 02:36:42` | `cowrie.command.input` |
| `2026-07-29 02:36:42` | `cowrie.command.input` |
| `2026-07-29 02:36:42` | `cowrie.command.success` |
| `2026-07-29 02:36:42` | `cowrie.command.input` |
| `2026-07-29 02:36:42` | `cowrie.command.input` |
| `2026-07-29 02:36:42` | `cowrie.command.input` |
| `2026-07-29 02:36:42` | `cowrie.command.input` |
| `2026-07-29 02:36:42` | `cowrie.log.closed` |
| `2026-07-29 02:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3d20798cb34

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:38 |
| **Last Seen** | 2026-07-29 02:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:38:02` | `cowrie.session.connect` |
| `2026-07-29 02:38:03` | `cowrie.client.version` |
| `2026-07-29 02:38:03` | `cowrie.client.kex` |
| `2026-07-29 02:38:04` | `cowrie.login.success` |
| `2026-07-29 02:38:05` | `cowrie.session.params` |
| `2026-07-29 02:38:05` | `cowrie.command.input` |
| `2026-07-29 02:38:05` | `cowrie.command.input` |
| `2026-07-29 02:38:05` | `cowrie.command.input` |
| `2026-07-29 02:38:05` | `cowrie.command.input` |
| `2026-07-29 02:38:05` | `cowrie.command.input` |
| `2026-07-29 02:38:05` | `cowrie.command.success` |
| `2026-07-29 02:38:05` | `cowrie.command.input` |
| `2026-07-29 02:38:05` | `cowrie.command.input` |
| `2026-07-29 02:38:05` | `cowrie.command.input` |
| `2026-07-29 02:38:05` | `cowrie.command.input` |
| `2026-07-29 02:38:06` | `cowrie.log.closed` |
| `2026-07-29 02:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47286ff3a49f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:39 |
| **Last Seen** | 2026-07-29 02:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:39:28` | `cowrie.session.connect` |
| `2026-07-29 02:39:28` | `cowrie.client.version` |
| `2026-07-29 02:39:28` | `cowrie.client.kex` |
| `2026-07-29 02:39:30` | `cowrie.login.success` |
| `2026-07-29 02:39:31` | `cowrie.session.params` |
| `2026-07-29 02:39:31` | `cowrie.command.input` |
| `2026-07-29 02:39:31` | `cowrie.command.input` |
| `2026-07-29 02:39:31` | `cowrie.command.input` |
| `2026-07-29 02:39:31` | `cowrie.command.input` |
| `2026-07-29 02:39:31` | `cowrie.command.input` |
| `2026-07-29 02:39:31` | `cowrie.command.success` |
| `2026-07-29 02:39:31` | `cowrie.command.input` |
| `2026-07-29 02:39:31` | `cowrie.command.input` |
| `2026-07-29 02:39:31` | `cowrie.command.input` |
| `2026-07-29 02:39:31` | `cowrie.command.input` |
| `2026-07-29 02:39:31` | `cowrie.log.closed` |
| `2026-07-29 02:39:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e67af4813b0

| Field | Detail |
|---|---|
| **Source IP** | `75.80.65[.]214` |
| **First Seen** | 2026-07-29 02:40 |
| **Last Seen** | 2026-07-29 02:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:40:49` | `cowrie.session.connect` |
| `2026-07-29 02:40:49` | `cowrie.client.version` |
| `2026-07-29 02:40:49` | `cowrie.client.kex` |
| `2026-07-29 02:40:51` | `cowrie.login.success` |
| `2026-07-29 02:40:51` | `cowrie.direct-tcpip.request` |
| `2026-07-29 02:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `75.80.65[.]214` to AbuseIPDB if not already reported
- [ ] Block `75.80.65[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8eaa190b654

| Field | Detail |
|---|---|
| **Source IP** | `125.19.244[.]62` |
| **First Seen** | 2026-07-29 02:40 |
| **Last Seen** | 2026-07-29 02:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:40:56` | `cowrie.session.connect` |
| `2026-07-29 02:40:57` | `cowrie.client.version` |
| `2026-07-29 02:40:57` | `cowrie.client.kex` |
| `2026-07-29 02:40:59` | `cowrie.login.success` |
| `2026-07-29 02:40:59` | `cowrie.direct-tcpip.request` |
| `2026-07-29 02:41:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.19.244[.]62` to AbuseIPDB if not already reported
- [ ] Block `125.19.244[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a63d74daec9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:40 |
| **Last Seen** | 2026-07-29 02:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:40:56` | `cowrie.session.connect` |
| `2026-07-29 02:40:56` | `cowrie.client.version` |
| `2026-07-29 02:40:56` | `cowrie.client.kex` |
| `2026-07-29 02:40:58` | `cowrie.login.success` |
| `2026-07-29 02:40:59` | `cowrie.session.params` |
| `2026-07-29 02:40:59` | `cowrie.command.input` |
| `2026-07-29 02:40:59` | `cowrie.command.input` |
| `2026-07-29 02:40:59` | `cowrie.command.input` |
| `2026-07-29 02:40:59` | `cowrie.command.input` |
| `2026-07-29 02:40:59` | `cowrie.command.input` |
| `2026-07-29 02:40:59` | `cowrie.command.success` |
| `2026-07-29 02:40:59` | `cowrie.command.input` |
| `2026-07-29 02:40:59` | `cowrie.command.input` |
| `2026-07-29 02:40:59` | `cowrie.command.input` |
| `2026-07-29 02:40:59` | `cowrie.command.input` |
| `2026-07-29 02:40:59` | `cowrie.log.closed` |
| `2026-07-29 02:40:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04dcb4db1f2d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:42 |
| **Last Seen** | 2026-07-29 02:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:42:25` | `cowrie.session.connect` |
| `2026-07-29 02:42:25` | `cowrie.client.version` |
| `2026-07-29 02:42:25` | `cowrie.client.kex` |
| `2026-07-29 02:42:27` | `cowrie.login.success` |
| `2026-07-29 02:42:28` | `cowrie.session.params` |
| `2026-07-29 02:42:28` | `cowrie.command.input` |
| `2026-07-29 02:42:28` | `cowrie.command.input` |
| `2026-07-29 02:42:28` | `cowrie.command.input` |
| `2026-07-29 02:42:28` | `cowrie.command.input` |
| `2026-07-29 02:42:28` | `cowrie.command.input` |
| `2026-07-29 02:42:28` | `cowrie.command.success` |
| `2026-07-29 02:42:28` | `cowrie.command.input` |
| `2026-07-29 02:42:28` | `cowrie.command.input` |
| `2026-07-29 02:42:28` | `cowrie.command.input` |
| `2026-07-29 02:42:28` | `cowrie.command.input` |
| `2026-07-29 02:42:28` | `cowrie.log.closed` |
| `2026-07-29 02:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cba45fd435f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:43 |
| **Last Seen** | 2026-07-29 02:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:43:53` | `cowrie.session.connect` |
| `2026-07-29 02:43:53` | `cowrie.client.version` |
| `2026-07-29 02:43:53` | `cowrie.client.kex` |
| `2026-07-29 02:43:54` | `cowrie.login.success` |
| `2026-07-29 02:43:55` | `cowrie.session.params` |
| `2026-07-29 02:43:55` | `cowrie.command.input` |
| `2026-07-29 02:43:55` | `cowrie.command.input` |
| `2026-07-29 02:43:55` | `cowrie.command.input` |
| `2026-07-29 02:43:55` | `cowrie.command.input` |
| `2026-07-29 02:43:55` | `cowrie.command.input` |
| `2026-07-29 02:43:55` | `cowrie.command.success` |
| `2026-07-29 02:43:55` | `cowrie.command.input` |
| `2026-07-29 02:43:55` | `cowrie.command.input` |
| `2026-07-29 02:43:55` | `cowrie.command.input` |
| `2026-07-29 02:43:55` | `cowrie.command.input` |
| `2026-07-29 02:43:56` | `cowrie.log.closed` |
| `2026-07-29 02:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b895b17e278

| Field | Detail |
|---|---|
| **Source IP** | `60.173.105[.]206` |
| **First Seen** | 2026-07-29 02:44 |
| **Last Seen** | 2026-07-29 02:44 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:44:12` | `cowrie.session.connect` |
| `2026-07-29 02:44:15` | `cowrie.client.version` |
| `2026-07-29 02:44:15` | `cowrie.client.kex` |
| `2026-07-29 02:44:18` | `cowrie.login.success` |
| `2026-07-29 02:44:19` | `cowrie.direct-tcpip.request` |
| `2026-07-29 02:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.173.105[.]206` to AbuseIPDB if not already reported
- [ ] Block `60.173.105[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d6c17c19bd1

| Field | Detail |
|---|---|
| **Source IP** | `24.97.253[.]246` |
| **First Seen** | 2026-07-29 02:44 |
| **Last Seen** | 2026-07-29 02:49 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:44:24` | `cowrie.session.connect` |
| `2026-07-29 02:44:24` | `cowrie.client.version` |
| `2026-07-29 02:44:24` | `cowrie.client.kex` |
| `2026-07-29 02:44:25` | `cowrie.login.success` |
| `2026-07-29 02:44:25` | `cowrie.direct-tcpip.request` |
| `2026-07-29 02:49:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.97.253[.]246` to AbuseIPDB if not already reported
- [ ] Block `24.97.253[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a55ea87706c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:45 |
| **Last Seen** | 2026-07-29 02:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:45:18` | `cowrie.session.connect` |
| `2026-07-29 02:45:18` | `cowrie.client.version` |
| `2026-07-29 02:45:18` | `cowrie.client.kex` |
| `2026-07-29 02:45:19` | `cowrie.login.success` |
| `2026-07-29 02:45:20` | `cowrie.session.params` |
| `2026-07-29 02:45:20` | `cowrie.command.input` |
| `2026-07-29 02:45:20` | `cowrie.command.input` |
| `2026-07-29 02:45:20` | `cowrie.command.input` |
| `2026-07-29 02:45:20` | `cowrie.command.input` |
| `2026-07-29 02:45:20` | `cowrie.command.input` |
| `2026-07-29 02:45:20` | `cowrie.command.success` |
| `2026-07-29 02:45:20` | `cowrie.command.input` |
| `2026-07-29 02:45:20` | `cowrie.command.input` |
| `2026-07-29 02:45:20` | `cowrie.command.input` |
| `2026-07-29 02:45:20` | `cowrie.command.input` |
| `2026-07-29 02:45:21` | `cowrie.log.closed` |
| `2026-07-29 02:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6289672f0647

| Field | Detail |
|---|---|
| **Source IP** | `35.195.144[.]153` |
| **First Seen** | 2026-07-29 02:46 |
| **Last Seen** | 2026-07-29 02:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:46:39` | `cowrie.session.connect` |
| `2026-07-29 02:46:39` | `cowrie.login.success` |
| `2026-07-29 02:46:39` | `cowrie.session.params` |
| `2026-07-29 02:46:39` | `cowrie.command.input` |
| `2026-07-29 02:46:39` | `cowrie.command.input` |
| `2026-07-29 02:46:39` | `cowrie.command.failed` |
| `2026-07-29 02:46:39` | `cowrie.command.input` |
| `2026-07-29 02:46:39` | `cowrie.log.closed` |
| `2026-07-29 02:46:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.144[.]153` to AbuseIPDB if not already reported
- [ ] Block `35.195.144[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34d986df3307

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:46 |
| **Last Seen** | 2026-07-29 02:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:46:43` | `cowrie.session.connect` |
| `2026-07-29 02:46:43` | `cowrie.client.version` |
| `2026-07-29 02:46:43` | `cowrie.client.kex` |
| `2026-07-29 02:46:44` | `cowrie.login.success` |
| `2026-07-29 02:46:45` | `cowrie.session.params` |
| `2026-07-29 02:46:45` | `cowrie.command.input` |
| `2026-07-29 02:46:45` | `cowrie.command.input` |
| `2026-07-29 02:46:45` | `cowrie.command.input` |
| `2026-07-29 02:46:45` | `cowrie.command.input` |
| `2026-07-29 02:46:45` | `cowrie.command.input` |
| `2026-07-29 02:46:45` | `cowrie.command.success` |
| `2026-07-29 02:46:45` | `cowrie.command.input` |
| `2026-07-29 02:46:45` | `cowrie.command.input` |
| `2026-07-29 02:46:45` | `cowrie.command.input` |
| `2026-07-29 02:46:45` | `cowrie.command.input` |
| `2026-07-29 02:46:46` | `cowrie.log.closed` |
| `2026-07-29 02:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c11a9175255

| Field | Detail |
|---|---|
| **Source IP** | `35.195.144[.]153` |
| **First Seen** | 2026-07-29 02:46 |
| **Last Seen** | 2026-07-29 02:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:46:52` | `cowrie.session.connect` |
| `2026-07-29 02:46:52` | `cowrie.login.success` |
| `2026-07-29 02:46:53` | `cowrie.session.params` |
| `2026-07-29 02:46:53` | `cowrie.command.input` |
| `2026-07-29 02:46:53` | `cowrie.command.failed` |
| `2026-07-29 02:46:58` | `cowrie.log.closed` |
| `2026-07-29 02:46:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.144[.]153` to AbuseIPDB if not already reported
- [ ] Block `35.195.144[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaade5badb04

| Field | Detail |
|---|---|
| **Source IP** | `35.195.144[.]153` |
| **First Seen** | 2026-07-29 02:46 |
| **Last Seen** | 2026-07-29 02:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:46:54` | `cowrie.session.connect` |
| `2026-07-29 02:46:54` | `cowrie.login.success` |
| `2026-07-29 02:46:55` | `cowrie.session.params` |
| `2026-07-29 02:46:55` | `cowrie.command.input` |
| `2026-07-29 02:46:58` | `cowrie.log.closed` |
| `2026-07-29 02:46:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.144[.]153` to AbuseIPDB if not already reported
- [ ] Block `35.195.144[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4fe64ad2b1f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:48 |
| **Last Seen** | 2026-07-29 02:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:48:08` | `cowrie.session.connect` |
| `2026-07-29 02:48:08` | `cowrie.client.version` |
| `2026-07-29 02:48:08` | `cowrie.client.kex` |
| `2026-07-29 02:48:09` | `cowrie.login.success` |
| `2026-07-29 02:48:10` | `cowrie.session.params` |
| `2026-07-29 02:48:10` | `cowrie.command.input` |
| `2026-07-29 02:48:10` | `cowrie.command.input` |
| `2026-07-29 02:48:10` | `cowrie.command.input` |
| `2026-07-29 02:48:10` | `cowrie.command.input` |
| `2026-07-29 02:48:10` | `cowrie.command.input` |
| `2026-07-29 02:48:10` | `cowrie.command.success` |
| `2026-07-29 02:48:10` | `cowrie.command.input` |
| `2026-07-29 02:48:10` | `cowrie.command.input` |
| `2026-07-29 02:48:10` | `cowrie.command.input` |
| `2026-07-29 02:48:10` | `cowrie.command.input` |
| `2026-07-29 02:48:10` | `cowrie.log.closed` |
| `2026-07-29 02:48:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3533c1b44017

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:49 |
| **Last Seen** | 2026-07-29 02:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:49:33` | `cowrie.session.connect` |
| `2026-07-29 02:49:33` | `cowrie.client.version` |
| `2026-07-29 02:49:33` | `cowrie.client.kex` |
| `2026-07-29 02:49:34` | `cowrie.login.success` |
| `2026-07-29 02:49:35` | `cowrie.session.params` |
| `2026-07-29 02:49:35` | `cowrie.command.input` |
| `2026-07-29 02:49:35` | `cowrie.command.input` |
| `2026-07-29 02:49:35` | `cowrie.command.input` |
| `2026-07-29 02:49:35` | `cowrie.command.input` |
| `2026-07-29 02:49:35` | `cowrie.command.input` |
| `2026-07-29 02:49:35` | `cowrie.command.success` |
| `2026-07-29 02:49:35` | `cowrie.command.input` |
| `2026-07-29 02:49:35` | `cowrie.command.input` |
| `2026-07-29 02:49:35` | `cowrie.command.input` |
| `2026-07-29 02:49:35` | `cowrie.command.input` |
| `2026-07-29 02:49:36` | `cowrie.log.closed` |
| `2026-07-29 02:49:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0c8818a7ac8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:50 |
| **Last Seen** | 2026-07-29 02:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:50:57` | `cowrie.session.connect` |
| `2026-07-29 02:50:57` | `cowrie.client.version` |
| `2026-07-29 02:50:57` | `cowrie.client.kex` |
| `2026-07-29 02:50:58` | `cowrie.login.success` |
| `2026-07-29 02:50:59` | `cowrie.session.params` |
| `2026-07-29 02:50:59` | `cowrie.command.input` |
| `2026-07-29 02:50:59` | `cowrie.command.input` |
| `2026-07-29 02:50:59` | `cowrie.command.input` |
| `2026-07-29 02:50:59` | `cowrie.command.input` |
| `2026-07-29 02:50:59` | `cowrie.command.input` |
| `2026-07-29 02:50:59` | `cowrie.command.success` |
| `2026-07-29 02:50:59` | `cowrie.command.input` |
| `2026-07-29 02:50:59` | `cowrie.command.input` |
| `2026-07-29 02:50:59` | `cowrie.command.input` |
| `2026-07-29 02:50:59` | `cowrie.command.input` |
| `2026-07-29 02:50:59` | `cowrie.log.closed` |
| `2026-07-29 02:51:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a252070a4238

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:52 |
| **Last Seen** | 2026-07-29 02:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:52:22` | `cowrie.session.connect` |
| `2026-07-29 02:52:22` | `cowrie.client.version` |
| `2026-07-29 02:52:22` | `cowrie.client.kex` |
| `2026-07-29 02:52:23` | `cowrie.login.success` |
| `2026-07-29 02:52:24` | `cowrie.session.params` |
| `2026-07-29 02:52:24` | `cowrie.command.input` |
| `2026-07-29 02:52:24` | `cowrie.command.input` |
| `2026-07-29 02:52:24` | `cowrie.command.input` |
| `2026-07-29 02:52:24` | `cowrie.command.input` |
| `2026-07-29 02:52:24` | `cowrie.command.input` |
| `2026-07-29 02:52:24` | `cowrie.command.success` |
| `2026-07-29 02:52:24` | `cowrie.command.input` |
| `2026-07-29 02:52:24` | `cowrie.command.input` |
| `2026-07-29 02:52:24` | `cowrie.command.input` |
| `2026-07-29 02:52:24` | `cowrie.command.input` |
| `2026-07-29 02:52:24` | `cowrie.log.closed` |
| `2026-07-29 02:52:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-620cd175d9a0

| Field | Detail |
|---|---|
| **Source IP** | `187.126.105[.]42` |
| **First Seen** | 2026-07-29 02:52 |
| **Last Seen** | 2026-07-29 02:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:52:23` | `cowrie.session.connect` |
| `2026-07-29 02:52:24` | `cowrie.client.version` |
| `2026-07-29 02:52:24` | `cowrie.client.kex` |
| `2026-07-29 02:52:26` | `cowrie.login.success` |
| `2026-07-29 02:52:26` | `cowrie.direct-tcpip.request` |
| `2026-07-29 02:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.126.105[.]42` to AbuseIPDB if not already reported
- [ ] Block `187.126.105[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d77c59ba22d

| Field | Detail |
|---|---|
| **Source IP** | `182.73.164[.]228` |
| **First Seen** | 2026-07-29 02:52 |
| **Last Seen** | 2026-07-29 02:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:52:32` | `cowrie.session.connect` |
| `2026-07-29 02:52:32` | `cowrie.client.version` |
| `2026-07-29 02:52:32` | `cowrie.client.kex` |
| `2026-07-29 02:52:34` | `cowrie.login.success` |
| `2026-07-29 02:52:35` | `cowrie.direct-tcpip.request` |
| `2026-07-29 02:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.73.164[.]228` to AbuseIPDB if not already reported
- [ ] Block `182.73.164[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17c2e415d5a1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:53 |
| **Last Seen** | 2026-07-29 02:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:53:48` | `cowrie.session.connect` |
| `2026-07-29 02:53:48` | `cowrie.client.version` |
| `2026-07-29 02:53:48` | `cowrie.client.kex` |
| `2026-07-29 02:53:49` | `cowrie.login.success` |
| `2026-07-29 02:53:50` | `cowrie.session.params` |
| `2026-07-29 02:53:50` | `cowrie.command.input` |
| `2026-07-29 02:53:50` | `cowrie.command.input` |
| `2026-07-29 02:53:50` | `cowrie.command.input` |
| `2026-07-29 02:53:50` | `cowrie.command.input` |
| `2026-07-29 02:53:50` | `cowrie.command.input` |
| `2026-07-29 02:53:50` | `cowrie.command.success` |
| `2026-07-29 02:53:50` | `cowrie.command.input` |
| `2026-07-29 02:53:50` | `cowrie.command.input` |
| `2026-07-29 02:53:50` | `cowrie.command.input` |
| `2026-07-29 02:53:50` | `cowrie.command.input` |
| `2026-07-29 02:53:51` | `cowrie.log.closed` |
| `2026-07-29 02:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78844e4619ea

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:55 |
| **Last Seen** | 2026-07-29 02:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:55:11` | `cowrie.session.connect` |
| `2026-07-29 02:55:12` | `cowrie.client.version` |
| `2026-07-29 02:55:12` | `cowrie.client.kex` |
| `2026-07-29 02:55:13` | `cowrie.login.success` |
| `2026-07-29 02:55:15` | `cowrie.session.params` |
| `2026-07-29 02:55:15` | `cowrie.command.input` |
| `2026-07-29 02:55:15` | `cowrie.command.input` |
| `2026-07-29 02:55:15` | `cowrie.command.input` |
| `2026-07-29 02:55:15` | `cowrie.command.input` |
| `2026-07-29 02:55:15` | `cowrie.command.input` |
| `2026-07-29 02:55:15` | `cowrie.command.success` |
| `2026-07-29 02:55:15` | `cowrie.command.input` |
| `2026-07-29 02:55:15` | `cowrie.command.input` |
| `2026-07-29 02:55:15` | `cowrie.command.input` |
| `2026-07-29 02:55:15` | `cowrie.command.input` |
| `2026-07-29 02:55:15` | `cowrie.log.closed` |
| `2026-07-29 02:55:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-415781f9bc85

| Field | Detail |
|---|---|
| **Source IP** | `65.20.233[.]110` |
| **First Seen** | 2026-07-29 02:55 |
| **Last Seen** | 2026-07-29 02:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:55:26` | `cowrie.session.connect` |
| `2026-07-29 02:55:26` | `cowrie.client.version` |
| `2026-07-29 02:55:26` | `cowrie.client.kex` |
| `2026-07-29 02:55:28` | `cowrie.login.success` |
| `2026-07-29 02:55:28` | `cowrie.direct-tcpip.request` |
| `2026-07-29 02:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.233[.]110` to AbuseIPDB if not already reported
- [ ] Block `65.20.233[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9032f8d51479

| Field | Detail |
|---|---|
| **Source IP** | `138.118.213[.]68` |
| **First Seen** | 2026-07-29 02:55 |
| **Last Seen** | 2026-07-29 02:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:55:33` | `cowrie.session.connect` |
| `2026-07-29 02:55:34` | `cowrie.client.version` |
| `2026-07-29 02:55:34` | `cowrie.client.kex` |
| `2026-07-29 02:55:36` | `cowrie.login.success` |
| `2026-07-29 02:55:37` | `cowrie.direct-tcpip.request` |
| `2026-07-29 02:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.118.213[.]68` to AbuseIPDB if not already reported
- [ ] Block `138.118.213[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c2e52ccd5d8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:56 |
| **Last Seen** | 2026-07-29 02:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:56:35` | `cowrie.session.connect` |
| `2026-07-29 02:56:35` | `cowrie.client.version` |
| `2026-07-29 02:56:35` | `cowrie.client.kex` |
| `2026-07-29 02:56:37` | `cowrie.login.success` |
| `2026-07-29 02:56:38` | `cowrie.session.params` |
| `2026-07-29 02:56:38` | `cowrie.command.input` |
| `2026-07-29 02:56:38` | `cowrie.command.input` |
| `2026-07-29 02:56:38` | `cowrie.command.input` |
| `2026-07-29 02:56:38` | `cowrie.command.input` |
| `2026-07-29 02:56:38` | `cowrie.command.input` |
| `2026-07-29 02:56:38` | `cowrie.command.success` |
| `2026-07-29 02:56:38` | `cowrie.command.input` |
| `2026-07-29 02:56:38` | `cowrie.command.input` |
| `2026-07-29 02:56:38` | `cowrie.command.input` |
| `2026-07-29 02:56:38` | `cowrie.command.input` |
| `2026-07-29 02:56:38` | `cowrie.log.closed` |
| `2026-07-29 02:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42d485ec7ff1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:57 |
| **Last Seen** | 2026-07-29 02:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:57:59` | `cowrie.session.connect` |
| `2026-07-29 02:57:59` | `cowrie.client.version` |
| `2026-07-29 02:57:59` | `cowrie.client.kex` |
| `2026-07-29 02:58:01` | `cowrie.login.success` |
| `2026-07-29 02:58:02` | `cowrie.session.params` |
| `2026-07-29 02:58:02` | `cowrie.command.input` |
| `2026-07-29 02:58:02` | `cowrie.command.input` |
| `2026-07-29 02:58:02` | `cowrie.command.input` |
| `2026-07-29 02:58:02` | `cowrie.command.input` |
| `2026-07-29 02:58:02` | `cowrie.command.input` |
| `2026-07-29 02:58:02` | `cowrie.command.success` |
| `2026-07-29 02:58:02` | `cowrie.command.input` |
| `2026-07-29 02:58:02` | `cowrie.command.input` |
| `2026-07-29 02:58:02` | `cowrie.command.input` |
| `2026-07-29 02:58:02` | `cowrie.command.input` |
| `2026-07-29 02:58:03` | `cowrie.log.closed` |
| `2026-07-29 02:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6638db58f85a

| Field | Detail |
|---|---|
| **Source IP** | `223.107.72[.]234` |
| **First Seen** | 2026-07-29 02:58 |
| **Last Seen** | 2026-07-29 02:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:58:34` | `cowrie.session.connect` |
| `2026-07-29 02:58:35` | `cowrie.client.version` |
| `2026-07-29 02:58:35` | `cowrie.client.kex` |
| `2026-07-29 02:58:37` | `cowrie.login.success` |
| `2026-07-29 02:58:38` | `cowrie.direct-tcpip.request` |
| `2026-07-29 02:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.107.72[.]234` to AbuseIPDB if not already reported
- [ ] Block `223.107.72[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc79f995075b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 02:59 |
| **Last Seen** | 2026-07-29 02:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 02:59:21` | `cowrie.session.connect` |
| `2026-07-29 02:59:21` | `cowrie.client.version` |
| `2026-07-29 02:59:21` | `cowrie.client.kex` |
| `2026-07-29 02:59:23` | `cowrie.login.success` |
| `2026-07-29 02:59:25` | `cowrie.session.params` |
| `2026-07-29 02:59:25` | `cowrie.command.input` |
| `2026-07-29 02:59:25` | `cowrie.command.input` |
| `2026-07-29 02:59:25` | `cowrie.command.input` |
| `2026-07-29 02:59:25` | `cowrie.command.input` |
| `2026-07-29 02:59:25` | `cowrie.command.input` |
| `2026-07-29 02:59:25` | `cowrie.command.success` |
| `2026-07-29 02:59:25` | `cowrie.command.input` |
| `2026-07-29 02:59:25` | `cowrie.command.input` |
| `2026-07-29 02:59:25` | `cowrie.command.input` |
| `2026-07-29 02:59:25` | `cowrie.command.input` |
| `2026-07-29 02:59:25` | `cowrie.log.closed` |
| `2026-07-29 02:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de98d4da4bae

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:00 |
| **Last Seen** | 2026-07-29 03:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:00:42` | `cowrie.session.connect` |
| `2026-07-29 03:00:42` | `cowrie.client.version` |
| `2026-07-29 03:00:42` | `cowrie.client.kex` |
| `2026-07-29 03:00:44` | `cowrie.login.success` |
| `2026-07-29 03:00:45` | `cowrie.session.params` |
| `2026-07-29 03:00:45` | `cowrie.command.input` |
| `2026-07-29 03:00:45` | `cowrie.command.input` |
| `2026-07-29 03:00:45` | `cowrie.command.input` |
| `2026-07-29 03:00:45` | `cowrie.command.input` |
| `2026-07-29 03:00:45` | `cowrie.command.input` |
| `2026-07-29 03:00:45` | `cowrie.command.success` |
| `2026-07-29 03:00:45` | `cowrie.command.input` |
| `2026-07-29 03:00:45` | `cowrie.command.input` |
| `2026-07-29 03:00:45` | `cowrie.command.input` |
| `2026-07-29 03:00:45` | `cowrie.command.input` |
| `2026-07-29 03:00:46` | `cowrie.log.closed` |
| `2026-07-29 03:00:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f444c3d17c7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-29 03:01 |
| **Last Seen** | 2026-07-29 03:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:01:20` | `cowrie.session.connect` |
| `2026-07-29 03:01:20` | `cowrie.client.version` |
| `2026-07-29 03:01:20` | `cowrie.client.kex` |
| `2026-07-29 03:01:20` | `cowrie.login.success` |
| `2026-07-29 03:01:21` | `cowrie.direct-tcpip.request` |
| `2026-07-29 03:01:21` | `cowrie.direct-tcpip.data` |
| `2026-07-29 03:01:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8fff6e16d82

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]18` |
| **First Seen** | 2026-07-29 03:01 |
| **Last Seen** | 2026-07-29 03:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_OK` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:01:35` | `cowrie.session.connect` |
| `2026-07-29 03:01:36` | `cowrie.login.success` |
| `2026-07-29 03:01:36` | `cowrie.session.params` |
| `2026-07-29 03:01:37` | `cowrie.command.input` |
| `2026-07-29 03:01:37` | `cowrie.log.closed` |
| `2026-07-29 03:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]18` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3052026c128d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]18` |
| **First Seen** | 2026-07-29 03:01 |
| **Last Seen** | 2026-07-29 03:02 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo WRITABLE >/tmp/.testfile 2>&1, ls -l /tmp/.testfile 2>&1, rm -f /tmp/.testfile, cd /tmp, for pid in /proc/[0-9]*; do pid_num="${pid##*/}"; if [ -r "$pid/maps" ]; then suspicious=true; while IFS= read -r line; do case "$line" in *"/lib/"*|*"/lib64/"*|*".so"*) suspicious=false; break;; esac; done < "$pid/maps"; if [ "$suspicious" = true ]; then kill -9 "$pid_num" 2>/dev/null; fi; fi; done;` |
| **Download Attempts** | hxxp://91.199.133[.]133:8080/deploy.sh, hxxp://91.199.133[.]133:8080/deploy.sh, 0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7 |
| **Malware Analysis** | 0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7 (LOW) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1489 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:01:37` | `cowrie.session.connect` |
| `2026-07-29 03:01:39` | `cowrie.login.success` |
| `2026-07-29 03:01:39` | `cowrie.session.params` |
| `2026-07-29 03:01:40` | `cowrie.command.input` |
| `2026-07-29 03:01:41` | `cowrie.command.input` |
| `2026-07-29 03:01:41` | `cowrie.command.input` |
| `2026-07-29 03:01:42` | `cowrie.command.input` |
| `2026-07-29 03:01:42` | `cowrie.command.input` |
| `2026-07-29 03:01:42` | `cowrie.command.input` |
| `2026-07-29 03:01:43` | `cowrie.command.input` |
| `2026-07-29 03:01:43` | `cowrie.command.failed` |
| `2026-07-29 03:01:43` | `cowrie.command.failed` |
| `2026-07-29 03:01:43` | `cowrie.command.failed` |
| `2026-07-29 03:01:43` | `cowrie.command.failed` |
| `2026-07-29 03:01:43` | `cowrie.command.failed` |
| `2026-07-29 03:01:43` | `cowrie.command.failed` |
| `2026-07-29 03:01:43` | `cowrie.command.failed` |
| `2026-07-29 03:01:43` | `cowrie.command.failed` |
| `2026-07-29 03:01:43` | `cowrie.command.failed` |
| `2026-07-29 03:01:43` | `cowrie.command.failed` |
| `2026-07-29 03:01:43` | `cowrie.command.input` |
| `2026-07-29 03:01:43` | `cowrie.command.input` |
| `2026-07-29 03:01:43` | `cowrie.command.input` |
| `2026-07-29 03:01:43` | `cowrie.command.input` |
| `2026-07-29 03:01:43` | `cowrie.command.input` |
| `2026-07-29 03:01:43` | `cowrie.command.input` |
| `2026-07-29 03:01:43` | `cowrie.command.input` |
| `2026-07-29 03:01:43` | `cowrie.command.input` |
| `2026-07-29 03:01:43` | `cowrie.session.file_download` |
| `2026-07-29 03:01:43` | `cowrie.session.file_download` |
| `2026-07-29 03:01:43` | `cowrie.session.file_download.failed` |
| `2026-07-29 03:02:03` | `cowrie.command.input` |
| `2026-07-29 03:02:05` | `cowrie.command.input` |
| `2026-07-29 03:02:06` | `cowrie.command.input` |
| `2026-07-29 03:02:06` | `cowrie.command.input` |
| `2026-07-29 03:02:06` | `cowrie.command.input` |
| `2026-07-29 03:02:06` | `cowrie.command.input` |
| `2026-07-29 03:02:07` | `cowrie.command.input` |
| `2026-07-29 03:02:07` | `cowrie.command.input` |
| `2026-07-29 03:02:07` | `cowrie.command.input` |
| `2026-07-29 03:02:07` | `cowrie.command.input` |
| `2026-07-29 03:02:07` | `cowrie.command.input` |
| `2026-07-29 03:02:07` | `cowrie.command.failed` |
| `2026-07-29 03:02:07` | `cowrie.command.failed` |
| `2026-07-29 03:02:07` | `cowrie.command.failed` |
| `2026-07-29 03:02:07` | `cowrie.command.failed` |
| `2026-07-29 03:02:32` | `cowrie.session.input` |
| `2026-07-29 03:02:34` | `cowrie.session.file_download` |
| `2026-07-29 03:02:34` | `cowrie.session.file_download` |
| `2026-07-29 03:02:34` | `cowrie.log.closed` |
| `2026-07-29 03:02:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]18` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1e6918eea9c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:02 |
| **Last Seen** | 2026-07-29 03:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:02:05` | `cowrie.session.connect` |
| `2026-07-29 03:02:05` | `cowrie.client.version` |
| `2026-07-29 03:02:05` | `cowrie.client.kex` |
| `2026-07-29 03:02:07` | `cowrie.login.success` |
| `2026-07-29 03:02:09` | `cowrie.session.params` |
| `2026-07-29 03:02:09` | `cowrie.command.input` |
| `2026-07-29 03:02:09` | `cowrie.command.input` |
| `2026-07-29 03:02:09` | `cowrie.command.input` |
| `2026-07-29 03:02:09` | `cowrie.command.input` |
| `2026-07-29 03:02:09` | `cowrie.command.input` |
| `2026-07-29 03:02:09` | `cowrie.command.success` |
| `2026-07-29 03:02:09` | `cowrie.command.input` |
| `2026-07-29 03:02:09` | `cowrie.command.input` |
| `2026-07-29 03:02:09` | `cowrie.command.input` |
| `2026-07-29 03:02:09` | `cowrie.command.input` |
| `2026-07-29 03:02:09` | `cowrie.log.closed` |
| `2026-07-29 03:02:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97ec171ea76d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:03 |
| **Last Seen** | 2026-07-29 03:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:03:26` | `cowrie.session.connect` |
| `2026-07-29 03:03:26` | `cowrie.client.version` |
| `2026-07-29 03:03:26` | `cowrie.client.kex` |
| `2026-07-29 03:03:28` | `cowrie.login.success` |
| `2026-07-29 03:03:30` | `cowrie.session.params` |
| `2026-07-29 03:03:30` | `cowrie.command.input` |
| `2026-07-29 03:03:30` | `cowrie.command.input` |
| `2026-07-29 03:03:30` | `cowrie.command.input` |
| `2026-07-29 03:03:30` | `cowrie.command.input` |
| `2026-07-29 03:03:30` | `cowrie.command.input` |
| `2026-07-29 03:03:30` | `cowrie.command.success` |
| `2026-07-29 03:03:30` | `cowrie.command.input` |
| `2026-07-29 03:03:30` | `cowrie.command.input` |
| `2026-07-29 03:03:30` | `cowrie.command.input` |
| `2026-07-29 03:03:30` | `cowrie.command.input` |
| `2026-07-29 03:03:31` | `cowrie.log.closed` |
| `2026-07-29 03:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb3da0f98ffe

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:04 |
| **Last Seen** | 2026-07-29 03:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:04:47` | `cowrie.session.connect` |
| `2026-07-29 03:04:47` | `cowrie.client.version` |
| `2026-07-29 03:04:47` | `cowrie.client.kex` |
| `2026-07-29 03:04:49` | `cowrie.login.success` |
| `2026-07-29 03:04:51` | `cowrie.session.params` |
| `2026-07-29 03:04:51` | `cowrie.command.input` |
| `2026-07-29 03:04:51` | `cowrie.command.input` |
| `2026-07-29 03:04:51` | `cowrie.command.input` |
| `2026-07-29 03:04:51` | `cowrie.command.input` |
| `2026-07-29 03:04:51` | `cowrie.command.input` |
| `2026-07-29 03:04:51` | `cowrie.command.success` |
| `2026-07-29 03:04:51` | `cowrie.command.input` |
| `2026-07-29 03:04:51` | `cowrie.command.input` |
| `2026-07-29 03:04:51` | `cowrie.command.input` |
| `2026-07-29 03:04:51` | `cowrie.command.input` |
| `2026-07-29 03:04:52` | `cowrie.log.closed` |
| `2026-07-29 03:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-964addd4fd84

| Field | Detail |
|---|---|
| **Source IP** | `210.13.99[.]66` |
| **First Seen** | 2026-07-29 03:05 |
| **Last Seen** | 2026-07-29 03:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:05:16` | `cowrie.session.connect` |
| `2026-07-29 03:05:17` | `cowrie.client.version` |
| `2026-07-29 03:05:17` | `cowrie.client.kex` |
| `2026-07-29 03:05:19` | `cowrie.login.success` |
| `2026-07-29 03:05:20` | `cowrie.direct-tcpip.request` |
| `2026-07-29 03:05:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.13.99[.]66` to AbuseIPDB if not already reported
- [ ] Block `210.13.99[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f8f31ecf6ec

| Field | Detail |
|---|---|
| **Source IP** | `103.93.37[.]178` |
| **First Seen** | 2026-07-29 03:05 |
| **Last Seen** | 2026-07-29 03:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:05:25` | `cowrie.session.connect` |
| `2026-07-29 03:05:26` | `cowrie.client.version` |
| `2026-07-29 03:05:26` | `cowrie.client.kex` |
| `2026-07-29 03:05:28` | `cowrie.login.success` |
| `2026-07-29 03:05:29` | `cowrie.direct-tcpip.request` |
| `2026-07-29 03:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.93.37[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.93.37[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-014180259119

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:06 |
| **Last Seen** | 2026-07-29 03:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:06:06` | `cowrie.session.connect` |
| `2026-07-29 03:06:06` | `cowrie.client.version` |
| `2026-07-29 03:06:06` | `cowrie.client.kex` |
| `2026-07-29 03:06:08` | `cowrie.login.success` |
| `2026-07-29 03:06:09` | `cowrie.session.params` |
| `2026-07-29 03:06:09` | `cowrie.command.input` |
| `2026-07-29 03:06:09` | `cowrie.command.input` |
| `2026-07-29 03:06:09` | `cowrie.command.input` |
| `2026-07-29 03:06:09` | `cowrie.command.input` |
| `2026-07-29 03:06:09` | `cowrie.command.input` |
| `2026-07-29 03:06:09` | `cowrie.command.success` |
| `2026-07-29 03:06:09` | `cowrie.command.input` |
| `2026-07-29 03:06:09` | `cowrie.command.input` |
| `2026-07-29 03:06:09` | `cowrie.command.input` |
| `2026-07-29 03:06:09` | `cowrie.command.input` |
| `2026-07-29 03:06:11` | `cowrie.log.closed` |
| `2026-07-29 03:06:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaf2a16e0e2e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:07 |
| **Last Seen** | 2026-07-29 03:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:07:27` | `cowrie.session.connect` |
| `2026-07-29 03:07:28` | `cowrie.client.version` |
| `2026-07-29 03:07:28` | `cowrie.client.kex` |
| `2026-07-29 03:07:29` | `cowrie.login.success` |
| `2026-07-29 03:07:30` | `cowrie.session.params` |
| `2026-07-29 03:07:30` | `cowrie.command.input` |
| `2026-07-29 03:07:30` | `cowrie.command.input` |
| `2026-07-29 03:07:30` | `cowrie.command.input` |
| `2026-07-29 03:07:30` | `cowrie.command.input` |
| `2026-07-29 03:07:30` | `cowrie.command.input` |
| `2026-07-29 03:07:30` | `cowrie.command.success` |
| `2026-07-29 03:07:30` | `cowrie.command.input` |
| `2026-07-29 03:07:30` | `cowrie.command.input` |
| `2026-07-29 03:07:30` | `cowrie.command.input` |
| `2026-07-29 03:07:30` | `cowrie.command.input` |
| `2026-07-29 03:07:31` | `cowrie.log.closed` |
| `2026-07-29 03:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc07f3139097

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]179` |
| **First Seen** | 2026-07-29 03:08 |
| **Last Seen** | 2026-07-29 03:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:08:43` | `cowrie.session.connect` |
| `2026-07-29 03:08:44` | `cowrie.client.version` |
| `2026-07-29 03:08:44` | `cowrie.client.kex` |
| `2026-07-29 03:08:46` | `cowrie.login.success` |
| `2026-07-29 03:08:47` | `cowrie.direct-tcpip.request` |
| `2026-07-29 03:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]179` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0303de63a91

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:08 |
| **Last Seen** | 2026-07-29 03:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:08:50` | `cowrie.session.connect` |
| `2026-07-29 03:08:50` | `cowrie.client.version` |
| `2026-07-29 03:08:50` | `cowrie.client.kex` |
| `2026-07-29 03:08:52` | `cowrie.login.success` |
| `2026-07-29 03:08:53` | `cowrie.session.params` |
| `2026-07-29 03:08:53` | `cowrie.command.input` |
| `2026-07-29 03:08:53` | `cowrie.command.input` |
| `2026-07-29 03:08:53` | `cowrie.command.input` |
| `2026-07-29 03:08:53` | `cowrie.command.input` |
| `2026-07-29 03:08:53` | `cowrie.command.input` |
| `2026-07-29 03:08:53` | `cowrie.command.success` |
| `2026-07-29 03:08:53` | `cowrie.command.input` |
| `2026-07-29 03:08:53` | `cowrie.command.input` |
| `2026-07-29 03:08:53` | `cowrie.command.input` |
| `2026-07-29 03:08:53` | `cowrie.command.input` |
| `2026-07-29 03:08:54` | `cowrie.log.closed` |
| `2026-07-29 03:08:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81550ee7af28

| Field | Detail |
|---|---|
| **Source IP** | `65.20.237[.]119` |
| **First Seen** | 2026-07-29 03:08 |
| **Last Seen** | 2026-07-29 03:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:08:52` | `cowrie.session.connect` |
| `2026-07-29 03:08:53` | `cowrie.client.version` |
| `2026-07-29 03:08:53` | `cowrie.client.kex` |
| `2026-07-29 03:08:55` | `cowrie.login.success` |
| `2026-07-29 03:08:55` | `cowrie.direct-tcpip.request` |
| `2026-07-29 03:09:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.237[.]119` to AbuseIPDB if not already reported
- [ ] Block `65.20.237[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-309e1b172582

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:09 |
| **Last Seen** | 2026-07-29 03:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:09:40` | `cowrie.session.connect` |
| `2026-07-29 03:09:40` | `cowrie.client.version` |
| `2026-07-29 03:09:40` | `cowrie.client.kex` |
| `2026-07-29 03:09:42` | `cowrie.login.success` |
| `2026-07-29 03:09:43` | `cowrie.session.params` |
| `2026-07-29 03:09:43` | `cowrie.command.input` |
| `2026-07-29 03:09:43` | `cowrie.command.input` |
| `2026-07-29 03:09:43` | `cowrie.command.input` |
| `2026-07-29 03:09:43` | `cowrie.command.input` |
| `2026-07-29 03:09:43` | `cowrie.command.input` |
| `2026-07-29 03:09:43` | `cowrie.command.success` |
| `2026-07-29 03:09:43` | `cowrie.command.input` |
| `2026-07-29 03:09:43` | `cowrie.command.input` |
| `2026-07-29 03:09:43` | `cowrie.command.input` |
| `2026-07-29 03:09:43` | `cowrie.command.input` |
| `2026-07-29 03:09:44` | `cowrie.log.closed` |
| `2026-07-29 03:09:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e859b560a27

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:10 |
| **Last Seen** | 2026-07-29 03:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:10:13` | `cowrie.session.connect` |
| `2026-07-29 03:10:13` | `cowrie.client.version` |
| `2026-07-29 03:10:13` | `cowrie.client.kex` |
| `2026-07-29 03:10:15` | `cowrie.login.success` |
| `2026-07-29 03:10:16` | `cowrie.session.params` |
| `2026-07-29 03:10:16` | `cowrie.command.input` |
| `2026-07-29 03:10:16` | `cowrie.command.input` |
| `2026-07-29 03:10:16` | `cowrie.command.input` |
| `2026-07-29 03:10:16` | `cowrie.command.input` |
| `2026-07-29 03:10:16` | `cowrie.command.input` |
| `2026-07-29 03:10:16` | `cowrie.command.success` |
| `2026-07-29 03:10:16` | `cowrie.command.input` |
| `2026-07-29 03:10:16` | `cowrie.command.input` |
| `2026-07-29 03:10:16` | `cowrie.command.input` |
| `2026-07-29 03:10:16` | `cowrie.command.input` |
| `2026-07-29 03:10:16` | `cowrie.log.closed` |
| `2026-07-29 03:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-033e13b84fc5

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-29 03:11 |
| **Last Seen** | 2026-07-29 03:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:11:18` | `cowrie.session.connect` |
| `2026-07-29 03:11:18` | `cowrie.client.version` |
| `2026-07-29 03:11:18` | `cowrie.client.kex` |
| `2026-07-29 03:11:19` | `cowrie.login.success` |
| `2026-07-29 03:11:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90386b824cb7

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-29 03:11 |
| **Last Seen** | 2026-07-29 03:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:11:18` | `cowrie.session.connect` |
| `2026-07-29 03:11:18` | `cowrie.client.version` |
| `2026-07-29 03:11:18` | `cowrie.client.kex` |
| `2026-07-29 03:11:19` | `cowrie.login.success` |
| `2026-07-29 03:11:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-089a5f1811e3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:11 |
| **Last Seen** | 2026-07-29 03:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:11:34` | `cowrie.session.connect` |
| `2026-07-29 03:11:35` | `cowrie.client.version` |
| `2026-07-29 03:11:35` | `cowrie.client.kex` |
| `2026-07-29 03:11:36` | `cowrie.login.success` |
| `2026-07-29 03:11:37` | `cowrie.session.params` |
| `2026-07-29 03:11:38` | `cowrie.command.input` |
| `2026-07-29 03:11:38` | `cowrie.command.input` |
| `2026-07-29 03:11:38` | `cowrie.command.input` |
| `2026-07-29 03:11:38` | `cowrie.command.input` |
| `2026-07-29 03:11:38` | `cowrie.command.input` |
| `2026-07-29 03:11:38` | `cowrie.command.success` |
| `2026-07-29 03:11:38` | `cowrie.command.input` |
| `2026-07-29 03:11:38` | `cowrie.command.input` |
| `2026-07-29 03:11:38` | `cowrie.command.input` |
| `2026-07-29 03:11:38` | `cowrie.command.input` |
| `2026-07-29 03:11:38` | `cowrie.log.closed` |
| `2026-07-29 03:11:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc7d3bb42ffe

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-29 03:11 |
| **Last Seen** | 2026-07-29 03:13 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:11:37` | `cowrie.session.connect` |
| `2026-07-29 03:11:37` | `cowrie.client.version` |
| `2026-07-29 03:11:38` | `cowrie.client.kex` |
| `2026-07-29 03:11:38` | `cowrie.login.success` |
| `2026-07-29 03:11:40` | `cowrie.session.file_upload` |
| `2026-07-29 03:11:41` | `cowrie.session.params` |
| `2026-07-29 03:11:41` | `cowrie.command.input` |
| `2026-07-29 03:11:41` | `cowrie.command.input` |
| `2026-07-29 03:11:41` | `cowrie.command.input` |
| `2026-07-29 03:11:41` | `cowrie.command.failed` |
| `2026-07-29 03:11:42` | `cowrie.log.closed` |
| `2026-07-29 03:11:43` | `cowrie.session.params` |
| `2026-07-29 03:11:43` | `cowrie.command.input` |
| `2026-07-29 03:11:43` | `cowrie.log.closed` |
| `2026-07-29 03:11:44` | `cowrie.session.params` |
| `2026-07-29 03:11:44` | `cowrie.command.input` |
| `2026-07-29 03:11:44` | `cowrie.log.closed` |
| `2026-07-29 03:11:45` | `cowrie.session.params` |
| `2026-07-29 03:11:45` | `cowrie.command.input` |
| `2026-07-29 03:11:45` | `cowrie.command.failed` |
| `2026-07-29 03:11:45` | `cowrie.command.failed` |
| `2026-07-29 03:12:46` | `cowrie.session.params` |
| `2026-07-29 03:12:46` | `cowrie.command.input` |
| `2026-07-29 03:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94bad19d2a36

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:12 |
| **Last Seen** | 2026-07-29 03:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:12:08` | `cowrie.session.connect` |
| `2026-07-29 03:12:08` | `cowrie.client.version` |
| `2026-07-29 03:12:08` | `cowrie.client.kex` |
| `2026-07-29 03:12:10` | `cowrie.login.success` |
| `2026-07-29 03:12:12` | `cowrie.session.params` |
| `2026-07-29 03:12:12` | `cowrie.command.input` |
| `2026-07-29 03:12:12` | `cowrie.command.input` |
| `2026-07-29 03:12:12` | `cowrie.command.input` |
| `2026-07-29 03:12:12` | `cowrie.command.input` |
| `2026-07-29 03:12:12` | `cowrie.command.input` |
| `2026-07-29 03:12:12` | `cowrie.command.success` |
| `2026-07-29 03:12:12` | `cowrie.command.input` |
| `2026-07-29 03:12:12` | `cowrie.command.input` |
| `2026-07-29 03:12:12` | `cowrie.command.input` |
| `2026-07-29 03:12:12` | `cowrie.command.input` |
| `2026-07-29 03:12:12` | `cowrie.log.closed` |
| `2026-07-29 03:12:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-730e225b3598

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:12 |
| **Last Seen** | 2026-07-29 03:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:12:50` | `cowrie.session.connect` |
| `2026-07-29 03:12:50` | `cowrie.client.version` |
| `2026-07-29 03:12:50` | `cowrie.client.kex` |
| `2026-07-29 03:12:52` | `cowrie.login.success` |
| `2026-07-29 03:12:53` | `cowrie.session.params` |
| `2026-07-29 03:12:53` | `cowrie.command.input` |
| `2026-07-29 03:12:53` | `cowrie.command.input` |
| `2026-07-29 03:12:53` | `cowrie.command.input` |
| `2026-07-29 03:12:53` | `cowrie.command.input` |
| `2026-07-29 03:12:53` | `cowrie.command.input` |
| `2026-07-29 03:12:53` | `cowrie.command.success` |
| `2026-07-29 03:12:53` | `cowrie.command.input` |
| `2026-07-29 03:12:53` | `cowrie.command.input` |
| `2026-07-29 03:12:53` | `cowrie.command.input` |
| `2026-07-29 03:12:53` | `cowrie.command.input` |
| `2026-07-29 03:12:54` | `cowrie.log.closed` |
| `2026-07-29 03:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d2f453fc64c

| Field | Detail |
|---|---|
| **Source IP** | `47.252.16[.]44` |
| **First Seen** | 2026-07-29 03:13 |
| **Last Seen** | 2026-07-29 03:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:13:20` | `cowrie.session.connect` |
| `2026-07-29 03:13:20` | `cowrie.client.version` |
| `2026-07-29 03:13:20` | `cowrie.client.kex` |
| `2026-07-29 03:13:21` | `cowrie.login.success` |
| `2026-07-29 03:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.252.16[.]44` to AbuseIPDB if not already reported
- [ ] Block `47.252.16[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37b7ade91baf

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-29 03:13 |
| **Last Seen** | 2026-07-29 03:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:13:21` | `cowrie.session.connect` |
| `2026-07-29 03:13:21` | `cowrie.client.version` |
| `2026-07-29 03:13:21` | `cowrie.client.kex` |
| `2026-07-29 03:13:21` | `cowrie.login.success` |
| `2026-07-29 03:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-151b9942a7ad

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-29 03:14 |
| **Last Seen** | 2026-07-29 03:16 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:14:03` | `cowrie.session.connect` |
| `2026-07-29 03:14:03` | `cowrie.client.version` |
| `2026-07-29 03:14:03` | `cowrie.client.kex` |
| `2026-07-29 03:14:04` | `cowrie.login.success` |
| `2026-07-29 03:14:06` | `cowrie.session.file_upload` |
| `2026-07-29 03:14:07` | `cowrie.session.params` |
| `2026-07-29 03:14:07` | `cowrie.command.input` |
| `2026-07-29 03:14:07` | `cowrie.command.input` |
| `2026-07-29 03:14:07` | `cowrie.command.input` |
| `2026-07-29 03:14:07` | `cowrie.command.failed` |
| `2026-07-29 03:14:07` | `cowrie.log.closed` |
| `2026-07-29 03:14:08` | `cowrie.session.params` |
| `2026-07-29 03:14:08` | `cowrie.command.input` |
| `2026-07-29 03:14:08` | `cowrie.log.closed` |
| `2026-07-29 03:14:09` | `cowrie.session.params` |
| `2026-07-29 03:14:09` | `cowrie.command.input` |
| `2026-07-29 03:14:10` | `cowrie.log.closed` |
| `2026-07-29 03:14:11` | `cowrie.session.params` |
| `2026-07-29 03:14:11` | `cowrie.command.input` |
| `2026-07-29 03:14:11` | `cowrie.command.failed` |
| `2026-07-29 03:14:11` | `cowrie.command.failed` |
| `2026-07-29 03:15:12` | `cowrie.session.params` |
| `2026-07-29 03:15:12` | `cowrie.command.input` |
| `2026-07-29 03:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57b95db43b4c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:14 |
| **Last Seen** | 2026-07-29 03:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:14:07` | `cowrie.session.connect` |
| `2026-07-29 03:14:07` | `cowrie.client.version` |
| `2026-07-29 03:14:07` | `cowrie.client.kex` |
| `2026-07-29 03:14:09` | `cowrie.login.success` |
| `2026-07-29 03:14:11` | `cowrie.session.params` |
| `2026-07-29 03:14:11` | `cowrie.command.input` |
| `2026-07-29 03:14:11` | `cowrie.command.input` |
| `2026-07-29 03:14:11` | `cowrie.command.input` |
| `2026-07-29 03:14:11` | `cowrie.command.input` |
| `2026-07-29 03:14:11` | `cowrie.command.input` |
| `2026-07-29 03:14:11` | `cowrie.command.success` |
| `2026-07-29 03:14:11` | `cowrie.command.input` |
| `2026-07-29 03:14:11` | `cowrie.command.input` |
| `2026-07-29 03:14:11` | `cowrie.command.input` |
| `2026-07-29 03:14:11` | `cowrie.command.input` |
| `2026-07-29 03:14:12` | `cowrie.log.closed` |
| `2026-07-29 03:14:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98f78716b0aa

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:14 |
| **Last Seen** | 2026-07-29 03:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:14:31` | `cowrie.session.connect` |
| `2026-07-29 03:14:31` | `cowrie.client.version` |
| `2026-07-29 03:14:31` | `cowrie.client.kex` |
| `2026-07-29 03:14:33` | `cowrie.login.success` |
| `2026-07-29 03:14:34` | `cowrie.session.params` |
| `2026-07-29 03:14:34` | `cowrie.command.input` |
| `2026-07-29 03:14:34` | `cowrie.command.input` |
| `2026-07-29 03:14:34` | `cowrie.command.input` |
| `2026-07-29 03:14:34` | `cowrie.command.input` |
| `2026-07-29 03:14:34` | `cowrie.command.input` |
| `2026-07-29 03:14:34` | `cowrie.command.success` |
| `2026-07-29 03:14:34` | `cowrie.command.input` |
| `2026-07-29 03:14:34` | `cowrie.command.input` |
| `2026-07-29 03:14:34` | `cowrie.command.input` |
| `2026-07-29 03:14:34` | `cowrie.command.input` |
| `2026-07-29 03:14:34` | `cowrie.log.closed` |
| `2026-07-29 03:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-216bc362a21b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:15 |
| **Last Seen** | 2026-07-29 03:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:15:25` | `cowrie.session.connect` |
| `2026-07-29 03:15:25` | `cowrie.client.version` |
| `2026-07-29 03:15:25` | `cowrie.client.kex` |
| `2026-07-29 03:15:27` | `cowrie.login.success` |
| `2026-07-29 03:15:28` | `cowrie.session.params` |
| `2026-07-29 03:15:28` | `cowrie.command.input` |
| `2026-07-29 03:15:28` | `cowrie.command.input` |
| `2026-07-29 03:15:28` | `cowrie.command.input` |
| `2026-07-29 03:15:28` | `cowrie.command.input` |
| `2026-07-29 03:15:28` | `cowrie.command.input` |
| `2026-07-29 03:15:28` | `cowrie.command.success` |
| `2026-07-29 03:15:28` | `cowrie.command.input` |
| `2026-07-29 03:15:28` | `cowrie.command.input` |
| `2026-07-29 03:15:28` | `cowrie.command.input` |
| `2026-07-29 03:15:28` | `cowrie.command.input` |
| `2026-07-29 03:15:28` | `cowrie.log.closed` |
| `2026-07-29 03:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed6b66db94c5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:16 |
| **Last Seen** | 2026-07-29 03:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:16:43` | `cowrie.session.connect` |
| `2026-07-29 03:16:43` | `cowrie.client.version` |
| `2026-07-29 03:16:43` | `cowrie.client.kex` |
| `2026-07-29 03:16:44` | `cowrie.login.success` |
| `2026-07-29 03:16:45` | `cowrie.session.params` |
| `2026-07-29 03:16:45` | `cowrie.command.input` |
| `2026-07-29 03:16:45` | `cowrie.command.input` |
| `2026-07-29 03:16:45` | `cowrie.command.input` |
| `2026-07-29 03:16:45` | `cowrie.command.input` |
| `2026-07-29 03:16:45` | `cowrie.command.input` |
| `2026-07-29 03:16:45` | `cowrie.command.success` |
| `2026-07-29 03:16:45` | `cowrie.command.input` |
| `2026-07-29 03:16:45` | `cowrie.command.input` |
| `2026-07-29 03:16:45` | `cowrie.command.input` |
| `2026-07-29 03:16:45` | `cowrie.command.input` |
| `2026-07-29 03:16:46` | `cowrie.log.closed` |
| `2026-07-29 03:16:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5ba37004c70

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:16 |
| **Last Seen** | 2026-07-29 03:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:16:45` | `cowrie.session.connect` |
| `2026-07-29 03:16:45` | `cowrie.client.version` |
| `2026-07-29 03:16:46` | `cowrie.client.kex` |
| `2026-07-29 03:16:47` | `cowrie.login.success` |
| `2026-07-29 03:16:49` | `cowrie.session.params` |
| `2026-07-29 03:16:49` | `cowrie.command.input` |
| `2026-07-29 03:16:49` | `cowrie.command.input` |
| `2026-07-29 03:16:49` | `cowrie.command.input` |
| `2026-07-29 03:16:49` | `cowrie.command.input` |
| `2026-07-29 03:16:49` | `cowrie.command.input` |
| `2026-07-29 03:16:49` | `cowrie.command.success` |
| `2026-07-29 03:16:49` | `cowrie.command.input` |
| `2026-07-29 03:16:49` | `cowrie.command.input` |
| `2026-07-29 03:16:49` | `cowrie.command.input` |
| `2026-07-29 03:16:49` | `cowrie.command.input` |
| `2026-07-29 03:16:49` | `cowrie.log.closed` |
| `2026-07-29 03:16:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faf48d741aa3

| Field | Detail |
|---|---|
| **Source IP** | `34.156.227[.]119` |
| **First Seen** | 2026-07-29 03:17 |
| **Last Seen** | 2026-07-29 03:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:17:41` | `cowrie.session.connect` |
| `2026-07-29 03:17:41` | `cowrie.login.success` |
| `2026-07-29 03:17:41` | `cowrie.session.params` |
| `2026-07-29 03:17:41` | `cowrie.command.input` |
| `2026-07-29 03:17:41` | `cowrie.command.input` |
| `2026-07-29 03:17:41` | `cowrie.command.failed` |
| `2026-07-29 03:17:41` | `cowrie.command.input` |
| `2026-07-29 03:17:41` | `cowrie.log.closed` |
| `2026-07-29 03:17:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.227[.]119` to AbuseIPDB if not already reported
- [ ] Block `34.156.227[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dae59a1560fd

| Field | Detail |
|---|---|
| **Source IP** | `34.156.227[.]119` |
| **First Seen** | 2026-07-29 03:17 |
| **Last Seen** | 2026-07-29 03:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:17:54` | `cowrie.session.connect` |
| `2026-07-29 03:17:54` | `cowrie.login.success` |
| `2026-07-29 03:17:55` | `cowrie.session.params` |
| `2026-07-29 03:17:55` | `cowrie.command.input` |
| `2026-07-29 03:17:55` | `cowrie.command.failed` |
| `2026-07-29 03:17:57` | `cowrie.log.closed` |
| `2026-07-29 03:17:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.227[.]119` to AbuseIPDB if not already reported
- [ ] Block `34.156.227[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-378547844599

| Field | Detail |
|---|---|
| **Source IP** | `34.156.227[.]119` |
| **First Seen** | 2026-07-29 03:17 |
| **Last Seen** | 2026-07-29 03:18 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:17:56` | `cowrie.session.connect` |
| `2026-07-29 03:17:56` | `cowrie.login.success` |
| `2026-07-29 03:17:57` | `cowrie.session.params` |
| `2026-07-29 03:17:57` | `cowrie.command.input` |
| `2026-07-29 03:18:12` | `cowrie.log.closed` |
| `2026-07-29 03:18:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.227[.]119` to AbuseIPDB if not already reported
- [ ] Block `34.156.227[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6fee013caf1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:18 |
| **Last Seen** | 2026-07-29 03:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:18:02` | `cowrie.session.connect` |
| `2026-07-29 03:18:02` | `cowrie.client.version` |
| `2026-07-29 03:18:02` | `cowrie.client.kex` |
| `2026-07-29 03:18:03` | `cowrie.login.success` |
| `2026-07-29 03:18:04` | `cowrie.session.params` |
| `2026-07-29 03:18:04` | `cowrie.command.input` |
| `2026-07-29 03:18:04` | `cowrie.command.input` |
| `2026-07-29 03:18:04` | `cowrie.command.input` |
| `2026-07-29 03:18:04` | `cowrie.command.input` |
| `2026-07-29 03:18:04` | `cowrie.command.input` |
| `2026-07-29 03:18:04` | `cowrie.command.success` |
| `2026-07-29 03:18:04` | `cowrie.command.input` |
| `2026-07-29 03:18:04` | `cowrie.command.input` |
| `2026-07-29 03:18:04` | `cowrie.command.input` |
| `2026-07-29 03:18:04` | `cowrie.command.input` |
| `2026-07-29 03:18:05` | `cowrie.log.closed` |
| `2026-07-29 03:18:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18f91bb46247

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:18 |
| **Last Seen** | 2026-07-29 03:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:18:46` | `cowrie.session.connect` |
| `2026-07-29 03:18:46` | `cowrie.client.version` |
| `2026-07-29 03:18:46` | `cowrie.client.kex` |
| `2026-07-29 03:18:47` | `cowrie.login.success` |
| `2026-07-29 03:18:49` | `cowrie.session.params` |
| `2026-07-29 03:18:49` | `cowrie.command.input` |
| `2026-07-29 03:18:49` | `cowrie.command.input` |
| `2026-07-29 03:18:49` | `cowrie.command.input` |
| `2026-07-29 03:18:49` | `cowrie.command.input` |
| `2026-07-29 03:18:49` | `cowrie.command.input` |
| `2026-07-29 03:18:49` | `cowrie.command.success` |
| `2026-07-29 03:18:49` | `cowrie.command.input` |
| `2026-07-29 03:18:49` | `cowrie.command.input` |
| `2026-07-29 03:18:49` | `cowrie.command.input` |
| `2026-07-29 03:18:49` | `cowrie.command.input` |
| `2026-07-29 03:18:49` | `cowrie.log.closed` |
| `2026-07-29 03:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4415eab188a2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:19 |
| **Last Seen** | 2026-07-29 03:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:19:22` | `cowrie.session.connect` |
| `2026-07-29 03:19:22` | `cowrie.client.version` |
| `2026-07-29 03:19:22` | `cowrie.client.kex` |
| `2026-07-29 03:19:23` | `cowrie.login.success` |
| `2026-07-29 03:19:24` | `cowrie.session.params` |
| `2026-07-29 03:19:24` | `cowrie.command.input` |
| `2026-07-29 03:19:24` | `cowrie.command.input` |
| `2026-07-29 03:19:24` | `cowrie.command.input` |
| `2026-07-29 03:19:24` | `cowrie.command.input` |
| `2026-07-29 03:19:24` | `cowrie.command.input` |
| `2026-07-29 03:19:24` | `cowrie.command.success` |
| `2026-07-29 03:19:24` | `cowrie.command.input` |
| `2026-07-29 03:19:24` | `cowrie.command.input` |
| `2026-07-29 03:19:24` | `cowrie.command.input` |
| `2026-07-29 03:19:24` | `cowrie.command.input` |
| `2026-07-29 03:19:25` | `cowrie.log.closed` |
| `2026-07-29 03:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8b5982a36fa

| Field | Detail |
|---|---|
| **Source IP** | `93.177.157[.]179` |
| **First Seen** | 2026-07-29 03:20 |
| **Last Seen** | 2026-07-29 03:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:20:02` | `cowrie.session.connect` |
| `2026-07-29 03:20:02` | `cowrie.client.version` |
| `2026-07-29 03:20:02` | `cowrie.client.kex` |
| `2026-07-29 03:20:03` | `cowrie.login.success` |
| `2026-07-29 03:20:04` | `cowrie.direct-tcpip.request` |
| `2026-07-29 03:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.177.157[.]179` to AbuseIPDB if not already reported
- [ ] Block `93.177.157[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8bcbbf22e23

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]236` |
| **First Seen** | 2026-07-29 03:20 |
| **Last Seen** | 2026-07-29 03:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:20:09` | `cowrie.session.connect` |
| `2026-07-29 03:20:10` | `cowrie.client.version` |
| `2026-07-29 03:20:10` | `cowrie.client.kex` |
| `2026-07-29 03:20:12` | `cowrie.login.success` |
| `2026-07-29 03:20:13` | `cowrie.direct-tcpip.request` |
| `2026-07-29 03:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]236` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b71a5f82fe5b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:20 |
| **Last Seen** | 2026-07-29 03:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:20:43` | `cowrie.session.connect` |
| `2026-07-29 03:20:43` | `cowrie.client.version` |
| `2026-07-29 03:20:43` | `cowrie.client.kex` |
| `2026-07-29 03:20:44` | `cowrie.login.success` |
| `2026-07-29 03:20:46` | `cowrie.session.params` |
| `2026-07-29 03:20:46` | `cowrie.command.input` |
| `2026-07-29 03:20:46` | `cowrie.command.input` |
| `2026-07-29 03:20:46` | `cowrie.command.input` |
| `2026-07-29 03:20:46` | `cowrie.command.input` |
| `2026-07-29 03:20:46` | `cowrie.command.input` |
| `2026-07-29 03:20:46` | `cowrie.command.success` |
| `2026-07-29 03:20:46` | `cowrie.command.input` |
| `2026-07-29 03:20:46` | `cowrie.command.input` |
| `2026-07-29 03:20:46` | `cowrie.command.input` |
| `2026-07-29 03:20:46` | `cowrie.command.input` |
| `2026-07-29 03:20:46` | `cowrie.log.closed` |
| `2026-07-29 03:20:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75433358a329

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:20 |
| **Last Seen** | 2026-07-29 03:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:20:43` | `cowrie.session.connect` |
| `2026-07-29 03:20:43` | `cowrie.client.version` |
| `2026-07-29 03:20:43` | `cowrie.client.kex` |
| `2026-07-29 03:20:45` | `cowrie.login.success` |
| `2026-07-29 03:20:47` | `cowrie.session.params` |
| `2026-07-29 03:20:47` | `cowrie.command.input` |
| `2026-07-29 03:20:47` | `cowrie.command.input` |
| `2026-07-29 03:20:47` | `cowrie.command.input` |
| `2026-07-29 03:20:47` | `cowrie.command.input` |
| `2026-07-29 03:20:47` | `cowrie.command.input` |
| `2026-07-29 03:20:47` | `cowrie.command.success` |
| `2026-07-29 03:20:47` | `cowrie.command.input` |
| `2026-07-29 03:20:47` | `cowrie.command.input` |
| `2026-07-29 03:20:47` | `cowrie.command.input` |
| `2026-07-29 03:20:47` | `cowrie.command.input` |
| `2026-07-29 03:20:48` | `cowrie.log.closed` |
| `2026-07-29 03:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-febf9870b13b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:22 |
| **Last Seen** | 2026-07-29 03:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:22:06` | `cowrie.session.connect` |
| `2026-07-29 03:22:06` | `cowrie.client.version` |
| `2026-07-29 03:22:06` | `cowrie.client.kex` |
| `2026-07-29 03:22:07` | `cowrie.login.success` |
| `2026-07-29 03:22:08` | `cowrie.session.params` |
| `2026-07-29 03:22:08` | `cowrie.command.input` |
| `2026-07-29 03:22:08` | `cowrie.command.input` |
| `2026-07-29 03:22:08` | `cowrie.command.input` |
| `2026-07-29 03:22:08` | `cowrie.command.input` |
| `2026-07-29 03:22:08` | `cowrie.command.input` |
| `2026-07-29 03:22:08` | `cowrie.command.success` |
| `2026-07-29 03:22:08` | `cowrie.command.input` |
| `2026-07-29 03:22:08` | `cowrie.command.input` |
| `2026-07-29 03:22:08` | `cowrie.command.input` |
| `2026-07-29 03:22:08` | `cowrie.command.input` |
| `2026-07-29 03:22:09` | `cowrie.log.closed` |
| `2026-07-29 03:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5246712b7036

| Field | Detail |
|---|---|
| **Source IP** | `112.197.2[.]116` |
| **First Seen** | 2026-07-29 03:22 |
| **Last Seen** | 2026-07-29 03:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:22:21` | `cowrie.session.connect` |
| `2026-07-29 03:22:21` | `cowrie.client.version` |
| `2026-07-29 03:22:21` | `cowrie.client.kex` |
| `2026-07-29 03:22:22` | `cowrie.login.success` |
| `2026-07-29 03:22:23` | `cowrie.session.params` |
| `2026-07-29 03:22:23` | `cowrie.command.input` |
| `2026-07-29 03:22:24` | `cowrie.log.closed` |
| `2026-07-29 03:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.197.2[.]116` to AbuseIPDB if not already reported
- [ ] Block `112.197.2[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ada4800745b3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:23 |
| **Last Seen** | 2026-07-29 03:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:23:31` | `cowrie.session.connect` |
| `2026-07-29 03:23:31` | `cowrie.client.version` |
| `2026-07-29 03:23:31` | `cowrie.client.kex` |
| `2026-07-29 03:23:32` | `cowrie.login.success` |
| `2026-07-29 03:23:35` | `cowrie.session.params` |
| `2026-07-29 03:23:35` | `cowrie.command.input` |
| `2026-07-29 03:23:35` | `cowrie.command.input` |
| `2026-07-29 03:23:35` | `cowrie.command.input` |
| `2026-07-29 03:23:35` | `cowrie.command.input` |
| `2026-07-29 03:23:35` | `cowrie.command.input` |
| `2026-07-29 03:23:35` | `cowrie.command.success` |
| `2026-07-29 03:23:35` | `cowrie.command.input` |
| `2026-07-29 03:23:35` | `cowrie.command.input` |
| `2026-07-29 03:23:35` | `cowrie.command.input` |
| `2026-07-29 03:23:35` | `cowrie.command.input` |
| `2026-07-29 03:23:35` | `cowrie.log.closed` |
| `2026-07-29 03:23:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfd43bf1ede1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:24 |
| **Last Seen** | 2026-07-29 03:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:24:35` | `cowrie.session.connect` |
| `2026-07-29 03:24:35` | `cowrie.client.version` |
| `2026-07-29 03:24:35` | `cowrie.client.kex` |
| `2026-07-29 03:24:37` | `cowrie.login.success` |
| `2026-07-29 03:24:38` | `cowrie.session.params` |
| `2026-07-29 03:24:38` | `cowrie.command.input` |
| `2026-07-29 03:24:38` | `cowrie.command.input` |
| `2026-07-29 03:24:38` | `cowrie.command.input` |
| `2026-07-29 03:24:38` | `cowrie.command.input` |
| `2026-07-29 03:24:38` | `cowrie.command.input` |
| `2026-07-29 03:24:38` | `cowrie.command.success` |
| `2026-07-29 03:24:38` | `cowrie.command.input` |
| `2026-07-29 03:24:38` | `cowrie.command.input` |
| `2026-07-29 03:24:38` | `cowrie.command.input` |
| `2026-07-29 03:24:38` | `cowrie.command.input` |
| `2026-07-29 03:24:39` | `cowrie.log.closed` |
| `2026-07-29 03:24:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afac4697c73f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:24 |
| **Last Seen** | 2026-07-29 03:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:24:55` | `cowrie.session.connect` |
| `2026-07-29 03:24:55` | `cowrie.client.version` |
| `2026-07-29 03:24:56` | `cowrie.client.kex` |
| `2026-07-29 03:24:56` | `cowrie.login.success` |
| `2026-07-29 03:24:57` | `cowrie.session.params` |
| `2026-07-29 03:24:57` | `cowrie.command.input` |
| `2026-07-29 03:24:57` | `cowrie.command.input` |
| `2026-07-29 03:24:57` | `cowrie.command.input` |
| `2026-07-29 03:24:57` | `cowrie.command.input` |
| `2026-07-29 03:24:57` | `cowrie.command.input` |
| `2026-07-29 03:24:57` | `cowrie.command.success` |
| `2026-07-29 03:24:57` | `cowrie.command.input` |
| `2026-07-29 03:24:57` | `cowrie.command.input` |
| `2026-07-29 03:24:57` | `cowrie.command.input` |
| `2026-07-29 03:24:57` | `cowrie.command.input` |
| `2026-07-29 03:24:57` | `cowrie.log.closed` |
| `2026-07-29 03:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84e09e4aff14

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:26 |
| **Last Seen** | 2026-07-29 03:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:26:17` | `cowrie.session.connect` |
| `2026-07-29 03:26:18` | `cowrie.client.version` |
| `2026-07-29 03:26:18` | `cowrie.client.kex` |
| `2026-07-29 03:26:20` | `cowrie.login.success` |
| `2026-07-29 03:26:23` | `cowrie.session.params` |
| `2026-07-29 03:26:23` | `cowrie.command.input` |
| `2026-07-29 03:26:23` | `cowrie.command.input` |
| `2026-07-29 03:26:23` | `cowrie.command.input` |
| `2026-07-29 03:26:23` | `cowrie.command.input` |
| `2026-07-29 03:26:23` | `cowrie.command.input` |
| `2026-07-29 03:26:23` | `cowrie.command.success` |
| `2026-07-29 03:26:23` | `cowrie.command.input` |
| `2026-07-29 03:26:23` | `cowrie.command.input` |
| `2026-07-29 03:26:23` | `cowrie.command.input` |
| `2026-07-29 03:26:23` | `cowrie.command.input` |
| `2026-07-29 03:26:24` | `cowrie.log.closed` |
| `2026-07-29 03:26:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6c6ed788040

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:26 |
| **Last Seen** | 2026-07-29 03:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:26:20` | `cowrie.session.connect` |
| `2026-07-29 03:26:20` | `cowrie.client.version` |
| `2026-07-29 03:26:20` | `cowrie.client.kex` |
| `2026-07-29 03:26:21` | `cowrie.login.success` |
| `2026-07-29 03:26:22` | `cowrie.session.params` |
| `2026-07-29 03:26:22` | `cowrie.command.input` |
| `2026-07-29 03:26:22` | `cowrie.command.input` |
| `2026-07-29 03:26:22` | `cowrie.command.input` |
| `2026-07-29 03:26:22` | `cowrie.command.input` |
| `2026-07-29 03:26:22` | `cowrie.command.input` |
| `2026-07-29 03:26:22` | `cowrie.command.success` |
| `2026-07-29 03:26:22` | `cowrie.command.input` |
| `2026-07-29 03:26:22` | `cowrie.command.input` |
| `2026-07-29 03:26:22` | `cowrie.command.input` |
| `2026-07-29 03:26:22` | `cowrie.command.input` |
| `2026-07-29 03:26:22` | `cowrie.log.closed` |
| `2026-07-29 03:26:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-966cd2daa6c8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:27 |
| **Last Seen** | 2026-07-29 03:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:27:46` | `cowrie.session.connect` |
| `2026-07-29 03:27:46` | `cowrie.client.version` |
| `2026-07-29 03:27:47` | `cowrie.client.kex` |
| `2026-07-29 03:27:48` | `cowrie.login.success` |
| `2026-07-29 03:27:49` | `cowrie.session.params` |
| `2026-07-29 03:27:49` | `cowrie.command.input` |
| `2026-07-29 03:27:49` | `cowrie.command.input` |
| `2026-07-29 03:27:49` | `cowrie.command.input` |
| `2026-07-29 03:27:49` | `cowrie.command.input` |
| `2026-07-29 03:27:49` | `cowrie.command.input` |
| `2026-07-29 03:27:49` | `cowrie.command.success` |
| `2026-07-29 03:27:49` | `cowrie.command.input` |
| `2026-07-29 03:27:49` | `cowrie.command.input` |
| `2026-07-29 03:27:49` | `cowrie.command.input` |
| `2026-07-29 03:27:49` | `cowrie.command.input` |
| `2026-07-29 03:27:49` | `cowrie.log.closed` |
| `2026-07-29 03:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aec5e2f6b9b3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:28 |
| **Last Seen** | 2026-07-29 03:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:28:06` | `cowrie.session.connect` |
| `2026-07-29 03:28:06` | `cowrie.client.version` |
| `2026-07-29 03:28:06` | `cowrie.client.kex` |
| `2026-07-29 03:28:08` | `cowrie.login.success` |
| `2026-07-29 03:28:09` | `cowrie.session.params` |
| `2026-07-29 03:28:09` | `cowrie.command.input` |
| `2026-07-29 03:28:09` | `cowrie.command.input` |
| `2026-07-29 03:28:10` | `cowrie.command.input` |
| `2026-07-29 03:28:10` | `cowrie.command.input` |
| `2026-07-29 03:28:10` | `cowrie.command.input` |
| `2026-07-29 03:28:10` | `cowrie.command.success` |
| `2026-07-29 03:28:10` | `cowrie.command.input` |
| `2026-07-29 03:28:10` | `cowrie.command.input` |
| `2026-07-29 03:28:10` | `cowrie.command.input` |
| `2026-07-29 03:28:10` | `cowrie.command.input` |
| `2026-07-29 03:28:11` | `cowrie.log.closed` |
| `2026-07-29 03:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05cb9f39adf8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:29 |
| **Last Seen** | 2026-07-29 03:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:29:12` | `cowrie.session.connect` |
| `2026-07-29 03:29:12` | `cowrie.client.version` |
| `2026-07-29 03:29:12` | `cowrie.client.kex` |
| `2026-07-29 03:29:13` | `cowrie.login.success` |
| `2026-07-29 03:29:14` | `cowrie.session.params` |
| `2026-07-29 03:29:14` | `cowrie.command.input` |
| `2026-07-29 03:29:14` | `cowrie.command.input` |
| `2026-07-29 03:29:14` | `cowrie.command.input` |
| `2026-07-29 03:29:14` | `cowrie.command.input` |
| `2026-07-29 03:29:14` | `cowrie.command.input` |
| `2026-07-29 03:29:14` | `cowrie.command.success` |
| `2026-07-29 03:29:14` | `cowrie.command.input` |
| `2026-07-29 03:29:14` | `cowrie.command.input` |
| `2026-07-29 03:29:14` | `cowrie.command.input` |
| `2026-07-29 03:29:14` | `cowrie.command.input` |
| `2026-07-29 03:29:15` | `cowrie.log.closed` |
| `2026-07-29 03:29:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79a060e6e749

| Field | Detail |
|---|---|
| **Source IP** | `121.159.71[.]249` |
| **First Seen** | 2026-07-29 03:29 |
| **Last Seen** | 2026-07-29 03:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:29:49` | `cowrie.session.connect` |
| `2026-07-29 03:29:50` | `cowrie.client.version` |
| `2026-07-29 03:29:50` | `cowrie.client.kex` |
| `2026-07-29 03:29:52` | `cowrie.login.success` |
| `2026-07-29 03:29:53` | `cowrie.direct-tcpip.request` |
| `2026-07-29 03:29:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.159.71[.]249` to AbuseIPDB if not already reported
- [ ] Block `121.159.71[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06c2559611db

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:29 |
| **Last Seen** | 2026-07-29 03:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:29:57` | `cowrie.session.connect` |
| `2026-07-29 03:29:57` | `cowrie.client.version` |
| `2026-07-29 03:29:58` | `cowrie.client.kex` |
| `2026-07-29 03:29:59` | `cowrie.login.success` |
| `2026-07-29 03:30:01` | `cowrie.session.params` |
| `2026-07-29 03:30:01` | `cowrie.command.input` |
| `2026-07-29 03:30:01` | `cowrie.command.input` |
| `2026-07-29 03:30:01` | `cowrie.command.input` |
| `2026-07-29 03:30:01` | `cowrie.command.input` |
| `2026-07-29 03:30:01` | `cowrie.command.input` |
| `2026-07-29 03:30:01` | `cowrie.command.success` |
| `2026-07-29 03:30:01` | `cowrie.command.input` |
| `2026-07-29 03:30:01` | `cowrie.command.input` |
| `2026-07-29 03:30:01` | `cowrie.command.input` |
| `2026-07-29 03:30:01` | `cowrie.command.input` |
| `2026-07-29 03:30:02` | `cowrie.log.closed` |
| `2026-07-29 03:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2be35245809f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:30 |
| **Last Seen** | 2026-07-29 03:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:30:36` | `cowrie.session.connect` |
| `2026-07-29 03:30:36` | `cowrie.client.version` |
| `2026-07-29 03:30:36` | `cowrie.client.kex` |
| `2026-07-29 03:30:38` | `cowrie.login.success` |
| `2026-07-29 03:30:39` | `cowrie.session.params` |
| `2026-07-29 03:30:39` | `cowrie.command.input` |
| `2026-07-29 03:30:39` | `cowrie.command.input` |
| `2026-07-29 03:30:39` | `cowrie.command.input` |
| `2026-07-29 03:30:39` | `cowrie.command.input` |
| `2026-07-29 03:30:39` | `cowrie.command.input` |
| `2026-07-29 03:30:39` | `cowrie.command.success` |
| `2026-07-29 03:30:39` | `cowrie.command.input` |
| `2026-07-29 03:30:39` | `cowrie.command.input` |
| `2026-07-29 03:30:39` | `cowrie.command.input` |
| `2026-07-29 03:30:39` | `cowrie.command.input` |
| `2026-07-29 03:30:40` | `cowrie.log.closed` |
| `2026-07-29 03:30:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd232ecb3475

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:31 |
| **Last Seen** | 2026-07-29 03:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:31:51` | `cowrie.session.connect` |
| `2026-07-29 03:31:51` | `cowrie.client.version` |
| `2026-07-29 03:31:51` | `cowrie.client.kex` |
| `2026-07-29 03:31:52` | `cowrie.login.success` |
| `2026-07-29 03:31:54` | `cowrie.session.params` |
| `2026-07-29 03:31:54` | `cowrie.command.input` |
| `2026-07-29 03:31:54` | `cowrie.command.input` |
| `2026-07-29 03:31:54` | `cowrie.command.input` |
| `2026-07-29 03:31:54` | `cowrie.command.input` |
| `2026-07-29 03:31:54` | `cowrie.command.input` |
| `2026-07-29 03:31:54` | `cowrie.command.success` |
| `2026-07-29 03:31:54` | `cowrie.command.input` |
| `2026-07-29 03:31:54` | `cowrie.command.input` |
| `2026-07-29 03:31:54` | `cowrie.command.input` |
| `2026-07-29 03:31:54` | `cowrie.command.input` |
| `2026-07-29 03:31:54` | `cowrie.log.closed` |
| `2026-07-29 03:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a26b7088443c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:31 |
| **Last Seen** | 2026-07-29 03:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:31:57` | `cowrie.session.connect` |
| `2026-07-29 03:31:58` | `cowrie.client.version` |
| `2026-07-29 03:31:58` | `cowrie.client.kex` |
| `2026-07-29 03:32:00` | `cowrie.login.success` |
| `2026-07-29 03:32:01` | `cowrie.session.params` |
| `2026-07-29 03:32:01` | `cowrie.command.input` |
| `2026-07-29 03:32:01` | `cowrie.command.input` |
| `2026-07-29 03:32:01` | `cowrie.command.input` |
| `2026-07-29 03:32:01` | `cowrie.command.input` |
| `2026-07-29 03:32:01` | `cowrie.command.input` |
| `2026-07-29 03:32:01` | `cowrie.command.success` |
| `2026-07-29 03:32:01` | `cowrie.command.input` |
| `2026-07-29 03:32:01` | `cowrie.command.input` |
| `2026-07-29 03:32:01` | `cowrie.command.input` |
| `2026-07-29 03:32:01` | `cowrie.command.input` |
| `2026-07-29 03:32:02` | `cowrie.log.closed` |
| `2026-07-29 03:32:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-993a2791046c

| Field | Detail |
|---|---|
| **Source IP** | `103.174.80[.]40` |
| **First Seen** | 2026-07-29 03:33 |
| **Last Seen** | 2026-07-29 03:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:33:07` | `cowrie.session.connect` |
| `2026-07-29 03:33:08` | `cowrie.client.version` |
| `2026-07-29 03:33:08` | `cowrie.client.kex` |
| `2026-07-29 03:33:09` | `cowrie.login.success` |
| `2026-07-29 03:33:10` | `cowrie.direct-tcpip.request` |
| `2026-07-29 03:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.80[.]40` to AbuseIPDB if not already reported
- [ ] Block `103.174.80[.]40` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-374ad8a41c21

| Field | Detail |
|---|---|
| **Source IP** | `82.65.140[.]218` |
| **First Seen** | 2026-07-29 03:33 |
| **Last Seen** | 2026-07-29 03:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:33:15` | `cowrie.session.connect` |
| `2026-07-29 03:33:15` | `cowrie.client.version` |
| `2026-07-29 03:33:15` | `cowrie.client.kex` |
| `2026-07-29 03:33:16` | `cowrie.login.success` |
| `2026-07-29 03:33:16` | `cowrie.direct-tcpip.request` |
| `2026-07-29 03:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.65.140[.]218` to AbuseIPDB if not already reported
- [ ] Block `82.65.140[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9612b11a5aaf

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:33 |
| **Last Seen** | 2026-07-29 03:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:33:18` | `cowrie.session.connect` |
| `2026-07-29 03:33:18` | `cowrie.client.version` |
| `2026-07-29 03:33:18` | `cowrie.client.kex` |
| `2026-07-29 03:33:20` | `cowrie.login.success` |
| `2026-07-29 03:33:21` | `cowrie.session.params` |
| `2026-07-29 03:33:21` | `cowrie.command.input` |
| `2026-07-29 03:33:21` | `cowrie.command.input` |
| `2026-07-29 03:33:21` | `cowrie.command.input` |
| `2026-07-29 03:33:21` | `cowrie.command.input` |
| `2026-07-29 03:33:21` | `cowrie.command.input` |
| `2026-07-29 03:33:21` | `cowrie.command.success` |
| `2026-07-29 03:33:21` | `cowrie.command.input` |
| `2026-07-29 03:33:21` | `cowrie.command.input` |
| `2026-07-29 03:33:21` | `cowrie.command.input` |
| `2026-07-29 03:33:21` | `cowrie.command.input` |
| `2026-07-29 03:33:22` | `cowrie.log.closed` |
| `2026-07-29 03:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be391cf3d25c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:33 |
| **Last Seen** | 2026-07-29 03:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:33:36` | `cowrie.session.connect` |
| `2026-07-29 03:33:36` | `cowrie.client.version` |
| `2026-07-29 03:33:36` | `cowrie.client.kex` |
| `2026-07-29 03:33:38` | `cowrie.login.success` |
| `2026-07-29 03:33:40` | `cowrie.session.params` |
| `2026-07-29 03:33:40` | `cowrie.command.input` |
| `2026-07-29 03:33:40` | `cowrie.command.input` |
| `2026-07-29 03:33:40` | `cowrie.command.input` |
| `2026-07-29 03:33:40` | `cowrie.command.input` |
| `2026-07-29 03:33:40` | `cowrie.command.input` |
| `2026-07-29 03:33:40` | `cowrie.command.success` |
| `2026-07-29 03:33:40` | `cowrie.command.input` |
| `2026-07-29 03:33:40` | `cowrie.command.input` |
| `2026-07-29 03:33:40` | `cowrie.command.input` |
| `2026-07-29 03:33:40` | `cowrie.command.input` |
| `2026-07-29 03:33:41` | `cowrie.log.closed` |
| `2026-07-29 03:33:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e250df9c41c5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:34 |
| **Last Seen** | 2026-07-29 03:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:34:40` | `cowrie.session.connect` |
| `2026-07-29 03:34:40` | `cowrie.client.version` |
| `2026-07-29 03:34:40` | `cowrie.client.kex` |
| `2026-07-29 03:34:42` | `cowrie.login.success` |
| `2026-07-29 03:34:43` | `cowrie.session.params` |
| `2026-07-29 03:34:43` | `cowrie.command.input` |
| `2026-07-29 03:34:43` | `cowrie.command.input` |
| `2026-07-29 03:34:43` | `cowrie.command.input` |
| `2026-07-29 03:34:43` | `cowrie.command.input` |
| `2026-07-29 03:34:43` | `cowrie.command.input` |
| `2026-07-29 03:34:43` | `cowrie.command.success` |
| `2026-07-29 03:34:43` | `cowrie.command.input` |
| `2026-07-29 03:34:43` | `cowrie.command.input` |
| `2026-07-29 03:34:43` | `cowrie.command.input` |
| `2026-07-29 03:34:43` | `cowrie.command.input` |
| `2026-07-29 03:34:44` | `cowrie.log.closed` |
| `2026-07-29 03:34:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de2c55e621bf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:35 |
| **Last Seen** | 2026-07-29 03:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:35:24` | `cowrie.session.connect` |
| `2026-07-29 03:35:25` | `cowrie.client.version` |
| `2026-07-29 03:35:25` | `cowrie.client.kex` |
| `2026-07-29 03:35:27` | `cowrie.login.success` |
| `2026-07-29 03:35:29` | `cowrie.session.params` |
| `2026-07-29 03:35:29` | `cowrie.command.input` |
| `2026-07-29 03:35:29` | `cowrie.command.input` |
| `2026-07-29 03:35:29` | `cowrie.command.input` |
| `2026-07-29 03:35:29` | `cowrie.command.input` |
| `2026-07-29 03:35:29` | `cowrie.command.input` |
| `2026-07-29 03:35:29` | `cowrie.command.success` |
| `2026-07-29 03:35:29` | `cowrie.command.input` |
| `2026-07-29 03:35:29` | `cowrie.command.input` |
| `2026-07-29 03:35:29` | `cowrie.command.input` |
| `2026-07-29 03:35:29` | `cowrie.command.input` |
| `2026-07-29 03:35:30` | `cowrie.log.closed` |
| `2026-07-29 03:35:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b89294c25db

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:36 |
| **Last Seen** | 2026-07-29 03:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:36:03` | `cowrie.session.connect` |
| `2026-07-29 03:36:04` | `cowrie.client.version` |
| `2026-07-29 03:36:04` | `cowrie.client.kex` |
| `2026-07-29 03:36:05` | `cowrie.login.success` |
| `2026-07-29 03:36:07` | `cowrie.session.params` |
| `2026-07-29 03:36:07` | `cowrie.command.input` |
| `2026-07-29 03:36:07` | `cowrie.command.input` |
| `2026-07-29 03:36:07` | `cowrie.command.input` |
| `2026-07-29 03:36:07` | `cowrie.command.input` |
| `2026-07-29 03:36:07` | `cowrie.command.input` |
| `2026-07-29 03:36:07` | `cowrie.command.success` |
| `2026-07-29 03:36:07` | `cowrie.command.input` |
| `2026-07-29 03:36:07` | `cowrie.command.input` |
| `2026-07-29 03:36:07` | `cowrie.command.input` |
| `2026-07-29 03:36:07` | `cowrie.command.input` |
| `2026-07-29 03:36:07` | `cowrie.log.closed` |
| `2026-07-29 03:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d9f4733f7de

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:37 |
| **Last Seen** | 2026-07-29 03:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:37:17` | `cowrie.session.connect` |
| `2026-07-29 03:37:17` | `cowrie.client.version` |
| `2026-07-29 03:37:17` | `cowrie.client.kex` |
| `2026-07-29 03:37:18` | `cowrie.login.success` |
| `2026-07-29 03:37:19` | `cowrie.session.params` |
| `2026-07-29 03:37:19` | `cowrie.command.input` |
| `2026-07-29 03:37:19` | `cowrie.command.input` |
| `2026-07-29 03:37:19` | `cowrie.command.input` |
| `2026-07-29 03:37:19` | `cowrie.command.input` |
| `2026-07-29 03:37:19` | `cowrie.command.input` |
| `2026-07-29 03:37:19` | `cowrie.command.success` |
| `2026-07-29 03:37:19` | `cowrie.command.input` |
| `2026-07-29 03:37:19` | `cowrie.command.input` |
| `2026-07-29 03:37:19` | `cowrie.command.input` |
| `2026-07-29 03:37:19` | `cowrie.command.input` |
| `2026-07-29 03:37:20` | `cowrie.log.closed` |
| `2026-07-29 03:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8df885d8206e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:37 |
| **Last Seen** | 2026-07-29 03:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:37:26` | `cowrie.session.connect` |
| `2026-07-29 03:37:26` | `cowrie.client.version` |
| `2026-07-29 03:37:26` | `cowrie.client.kex` |
| `2026-07-29 03:37:28` | `cowrie.login.success` |
| `2026-07-29 03:37:29` | `cowrie.session.params` |
| `2026-07-29 03:37:29` | `cowrie.command.input` |
| `2026-07-29 03:37:29` | `cowrie.command.input` |
| `2026-07-29 03:37:29` | `cowrie.command.input` |
| `2026-07-29 03:37:29` | `cowrie.command.input` |
| `2026-07-29 03:37:29` | `cowrie.command.input` |
| `2026-07-29 03:37:29` | `cowrie.command.success` |
| `2026-07-29 03:37:29` | `cowrie.command.input` |
| `2026-07-29 03:37:29` | `cowrie.command.input` |
| `2026-07-29 03:37:29` | `cowrie.command.input` |
| `2026-07-29 03:37:29` | `cowrie.command.input` |
| `2026-07-29 03:37:29` | `cowrie.log.closed` |
| `2026-07-29 03:37:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2aa7de993c6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:38 |
| **Last Seen** | 2026-07-29 03:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:38:48` | `cowrie.session.connect` |
| `2026-07-29 03:38:49` | `cowrie.client.version` |
| `2026-07-29 03:38:49` | `cowrie.client.kex` |
| `2026-07-29 03:38:50` | `cowrie.login.success` |
| `2026-07-29 03:38:51` | `cowrie.session.params` |
| `2026-07-29 03:38:51` | `cowrie.command.input` |
| `2026-07-29 03:38:51` | `cowrie.command.input` |
| `2026-07-29 03:38:51` | `cowrie.command.input` |
| `2026-07-29 03:38:51` | `cowrie.command.input` |
| `2026-07-29 03:38:51` | `cowrie.command.input` |
| `2026-07-29 03:38:51` | `cowrie.command.success` |
| `2026-07-29 03:38:51` | `cowrie.command.input` |
| `2026-07-29 03:38:51` | `cowrie.command.input` |
| `2026-07-29 03:38:51` | `cowrie.command.input` |
| `2026-07-29 03:38:51` | `cowrie.command.input` |
| `2026-07-29 03:38:51` | `cowrie.log.closed` |
| `2026-07-29 03:38:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef193005af09

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:39 |
| **Last Seen** | 2026-07-29 03:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:39:06` | `cowrie.session.connect` |
| `2026-07-29 03:39:06` | `cowrie.client.version` |
| `2026-07-29 03:39:06` | `cowrie.client.kex` |
| `2026-07-29 03:39:08` | `cowrie.login.success` |
| `2026-07-29 03:39:09` | `cowrie.session.params` |
| `2026-07-29 03:39:09` | `cowrie.command.input` |
| `2026-07-29 03:39:09` | `cowrie.command.input` |
| `2026-07-29 03:39:09` | `cowrie.command.input` |
| `2026-07-29 03:39:09` | `cowrie.command.input` |
| `2026-07-29 03:39:09` | `cowrie.command.input` |
| `2026-07-29 03:39:09` | `cowrie.command.success` |
| `2026-07-29 03:39:09` | `cowrie.command.input` |
| `2026-07-29 03:39:09` | `cowrie.command.input` |
| `2026-07-29 03:39:09` | `cowrie.command.input` |
| `2026-07-29 03:39:09` | `cowrie.command.input` |
| `2026-07-29 03:39:10` | `cowrie.log.closed` |
| `2026-07-29 03:39:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cdac144f795

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:40 |
| **Last Seen** | 2026-07-29 03:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:40:11` | `cowrie.session.connect` |
| `2026-07-29 03:40:11` | `cowrie.client.version` |
| `2026-07-29 03:40:11` | `cowrie.client.kex` |
| `2026-07-29 03:40:13` | `cowrie.login.success` |
| `2026-07-29 03:40:14` | `cowrie.session.params` |
| `2026-07-29 03:40:14` | `cowrie.command.input` |
| `2026-07-29 03:40:14` | `cowrie.command.input` |
| `2026-07-29 03:40:14` | `cowrie.command.input` |
| `2026-07-29 03:40:14` | `cowrie.command.input` |
| `2026-07-29 03:40:14` | `cowrie.command.input` |
| `2026-07-29 03:40:14` | `cowrie.command.success` |
| `2026-07-29 03:40:14` | `cowrie.command.input` |
| `2026-07-29 03:40:14` | `cowrie.command.input` |
| `2026-07-29 03:40:14` | `cowrie.command.input` |
| `2026-07-29 03:40:14` | `cowrie.command.input` |
| `2026-07-29 03:40:15` | `cowrie.log.closed` |
| `2026-07-29 03:40:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-042833581d6c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:40 |
| **Last Seen** | 2026-07-29 03:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:40:55` | `cowrie.session.connect` |
| `2026-07-29 03:40:55` | `cowrie.client.version` |
| `2026-07-29 03:40:55` | `cowrie.client.kex` |
| `2026-07-29 03:40:56` | `cowrie.login.success` |
| `2026-07-29 03:40:57` | `cowrie.session.params` |
| `2026-07-29 03:40:57` | `cowrie.command.input` |
| `2026-07-29 03:40:57` | `cowrie.command.input` |
| `2026-07-29 03:40:57` | `cowrie.command.input` |
| `2026-07-29 03:40:57` | `cowrie.command.input` |
| `2026-07-29 03:40:57` | `cowrie.command.input` |
| `2026-07-29 03:40:57` | `cowrie.command.success` |
| `2026-07-29 03:40:57` | `cowrie.command.input` |
| `2026-07-29 03:40:57` | `cowrie.command.input` |
| `2026-07-29 03:40:57` | `cowrie.command.input` |
| `2026-07-29 03:40:57` | `cowrie.command.input` |
| `2026-07-29 03:40:57` | `cowrie.log.closed` |
| `2026-07-29 03:40:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1af690a8a187

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]51` |
| **First Seen** | 2026-07-29 03:41 |
| **Last Seen** | 2026-07-29 03:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:41:08` | `cowrie.session.connect` |
| `2026-07-29 03:41:09` | `cowrie.client.version` |
| `2026-07-29 03:41:09` | `cowrie.client.kex` |
| `2026-07-29 03:41:11` | `cowrie.login.success` |
| `2026-07-29 03:41:12` | `cowrie.direct-tcpip.request` |
| `2026-07-29 03:41:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]51` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe5b495461cd

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:41 |
| **Last Seen** | 2026-07-29 03:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:41:33` | `cowrie.session.connect` |
| `2026-07-29 03:41:33` | `cowrie.client.version` |
| `2026-07-29 03:41:33` | `cowrie.client.kex` |
| `2026-07-29 03:41:35` | `cowrie.login.success` |
| `2026-07-29 03:41:36` | `cowrie.session.params` |
| `2026-07-29 03:41:36` | `cowrie.command.input` |
| `2026-07-29 03:41:36` | `cowrie.command.input` |
| `2026-07-29 03:41:36` | `cowrie.command.input` |
| `2026-07-29 03:41:36` | `cowrie.command.input` |
| `2026-07-29 03:41:36` | `cowrie.command.input` |
| `2026-07-29 03:41:36` | `cowrie.command.success` |
| `2026-07-29 03:41:36` | `cowrie.command.input` |
| `2026-07-29 03:41:36` | `cowrie.command.input` |
| `2026-07-29 03:41:36` | `cowrie.command.input` |
| `2026-07-29 03:41:36` | `cowrie.command.input` |
| `2026-07-29 03:41:37` | `cowrie.log.closed` |
| `2026-07-29 03:41:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecb884217144

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:42 |
| **Last Seen** | 2026-07-29 03:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:42:49` | `cowrie.session.connect` |
| `2026-07-29 03:42:50` | `cowrie.client.version` |
| `2026-07-29 03:42:50` | `cowrie.client.kex` |
| `2026-07-29 03:42:52` | `cowrie.login.success` |
| `2026-07-29 03:42:54` | `cowrie.session.params` |
| `2026-07-29 03:42:54` | `cowrie.command.input` |
| `2026-07-29 03:42:54` | `cowrie.command.input` |
| `2026-07-29 03:42:54` | `cowrie.command.input` |
| `2026-07-29 03:42:54` | `cowrie.command.input` |
| `2026-07-29 03:42:54` | `cowrie.command.input` |
| `2026-07-29 03:42:54` | `cowrie.command.success` |
| `2026-07-29 03:42:54` | `cowrie.command.input` |
| `2026-07-29 03:42:54` | `cowrie.command.input` |
| `2026-07-29 03:42:54` | `cowrie.command.input` |
| `2026-07-29 03:42:54` | `cowrie.command.input` |
| `2026-07-29 03:42:55` | `cowrie.log.closed` |
| `2026-07-29 03:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd6f5cfdd7a5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:42 |
| **Last Seen** | 2026-07-29 03:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:42:57` | `cowrie.session.connect` |
| `2026-07-29 03:42:57` | `cowrie.client.version` |
| `2026-07-29 03:42:57` | `cowrie.client.kex` |
| `2026-07-29 03:42:59` | `cowrie.login.success` |
| `2026-07-29 03:43:00` | `cowrie.session.params` |
| `2026-07-29 03:43:00` | `cowrie.command.input` |
| `2026-07-29 03:43:00` | `cowrie.command.input` |
| `2026-07-29 03:43:00` | `cowrie.command.input` |
| `2026-07-29 03:43:00` | `cowrie.command.input` |
| `2026-07-29 03:43:00` | `cowrie.command.input` |
| `2026-07-29 03:43:00` | `cowrie.command.success` |
| `2026-07-29 03:43:00` | `cowrie.command.input` |
| `2026-07-29 03:43:00` | `cowrie.command.input` |
| `2026-07-29 03:43:00` | `cowrie.command.input` |
| `2026-07-29 03:43:00` | `cowrie.command.input` |
| `2026-07-29 03:43:00` | `cowrie.log.closed` |
| `2026-07-29 03:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b42dcead88a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:44 |
| **Last Seen** | 2026-07-29 03:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:44:18` | `cowrie.session.connect` |
| `2026-07-29 03:44:18` | `cowrie.client.version` |
| `2026-07-29 03:44:18` | `cowrie.client.kex` |
| `2026-07-29 03:44:19` | `cowrie.login.success` |
| `2026-07-29 03:44:21` | `cowrie.session.params` |
| `2026-07-29 03:44:21` | `cowrie.command.input` |
| `2026-07-29 03:44:21` | `cowrie.command.input` |
| `2026-07-29 03:44:21` | `cowrie.command.input` |
| `2026-07-29 03:44:21` | `cowrie.command.input` |
| `2026-07-29 03:44:21` | `cowrie.command.input` |
| `2026-07-29 03:44:21` | `cowrie.command.success` |
| `2026-07-29 03:44:21` | `cowrie.command.input` |
| `2026-07-29 03:44:21` | `cowrie.command.input` |
| `2026-07-29 03:44:21` | `cowrie.command.input` |
| `2026-07-29 03:44:21` | `cowrie.command.input` |
| `2026-07-29 03:44:21` | `cowrie.log.closed` |
| `2026-07-29 03:44:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ccd30dbe2bc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:44 |
| **Last Seen** | 2026-07-29 03:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:44:30` | `cowrie.session.connect` |
| `2026-07-29 03:44:30` | `cowrie.client.version` |
| `2026-07-29 03:44:30` | `cowrie.client.kex` |
| `2026-07-29 03:44:32` | `cowrie.login.success` |
| `2026-07-29 03:44:33` | `cowrie.session.params` |
| `2026-07-29 03:44:33` | `cowrie.command.input` |
| `2026-07-29 03:44:33` | `cowrie.command.input` |
| `2026-07-29 03:44:33` | `cowrie.command.input` |
| `2026-07-29 03:44:33` | `cowrie.command.input` |
| `2026-07-29 03:44:33` | `cowrie.command.input` |
| `2026-07-29 03:44:33` | `cowrie.command.success` |
| `2026-07-29 03:44:33` | `cowrie.command.input` |
| `2026-07-29 03:44:33` | `cowrie.command.input` |
| `2026-07-29 03:44:33` | `cowrie.command.input` |
| `2026-07-29 03:44:33` | `cowrie.command.input` |
| `2026-07-29 03:44:34` | `cowrie.log.closed` |
| `2026-07-29 03:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d2cf3cd77db

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-29 03:45 |
| **Last Seen** | 2026-07-29 03:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:45:04` | `cowrie.session.connect` |
| `2026-07-29 03:45:04` | `cowrie.client.version` |
| `2026-07-29 03:45:04` | `cowrie.client.kex` |
| `2026-07-29 03:45:05` | `cowrie.login.success` |
| `2026-07-29 03:45:05` | `cowrie.direct-tcpip.request` |
| `2026-07-29 03:45:05` | `cowrie.direct-tcpip.data` |
| `2026-07-29 03:45:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bfc27da0758

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:45 |
| **Last Seen** | 2026-07-29 03:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:45:42` | `cowrie.session.connect` |
| `2026-07-29 03:45:42` | `cowrie.client.version` |
| `2026-07-29 03:45:42` | `cowrie.client.kex` |
| `2026-07-29 03:45:43` | `cowrie.login.success` |
| `2026-07-29 03:45:44` | `cowrie.session.params` |
| `2026-07-29 03:45:44` | `cowrie.command.input` |
| `2026-07-29 03:45:44` | `cowrie.command.input` |
| `2026-07-29 03:45:44` | `cowrie.command.input` |
| `2026-07-29 03:45:44` | `cowrie.command.input` |
| `2026-07-29 03:45:44` | `cowrie.command.input` |
| `2026-07-29 03:45:44` | `cowrie.command.success` |
| `2026-07-29 03:45:44` | `cowrie.command.input` |
| `2026-07-29 03:45:44` | `cowrie.command.input` |
| `2026-07-29 03:45:44` | `cowrie.command.input` |
| `2026-07-29 03:45:44` | `cowrie.command.input` |
| `2026-07-29 03:45:44` | `cowrie.log.closed` |
| `2026-07-29 03:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c070f10ea33f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:46 |
| **Last Seen** | 2026-07-29 03:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:46:28` | `cowrie.session.connect` |
| `2026-07-29 03:46:28` | `cowrie.client.version` |
| `2026-07-29 03:46:28` | `cowrie.client.kex` |
| `2026-07-29 03:46:29` | `cowrie.login.success` |
| `2026-07-29 03:46:30` | `cowrie.session.params` |
| `2026-07-29 03:46:30` | `cowrie.command.input` |
| `2026-07-29 03:46:30` | `cowrie.command.input` |
| `2026-07-29 03:46:30` | `cowrie.command.input` |
| `2026-07-29 03:46:30` | `cowrie.command.input` |
| `2026-07-29 03:46:30` | `cowrie.command.input` |
| `2026-07-29 03:46:30` | `cowrie.command.success` |
| `2026-07-29 03:46:30` | `cowrie.command.input` |
| `2026-07-29 03:46:30` | `cowrie.command.input` |
| `2026-07-29 03:46:30` | `cowrie.command.input` |
| `2026-07-29 03:46:30` | `cowrie.command.input` |
| `2026-07-29 03:46:31` | `cowrie.log.closed` |
| `2026-07-29 03:46:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f46898f7647f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:47 |
| **Last Seen** | 2026-07-29 03:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:47:08` | `cowrie.session.connect` |
| `2026-07-29 03:47:08` | `cowrie.client.version` |
| `2026-07-29 03:47:08` | `cowrie.client.kex` |
| `2026-07-29 03:47:10` | `cowrie.login.success` |
| `2026-07-29 03:47:11` | `cowrie.session.params` |
| `2026-07-29 03:47:11` | `cowrie.command.input` |
| `2026-07-29 03:47:11` | `cowrie.command.input` |
| `2026-07-29 03:47:11` | `cowrie.command.input` |
| `2026-07-29 03:47:11` | `cowrie.command.input` |
| `2026-07-29 03:47:11` | `cowrie.command.input` |
| `2026-07-29 03:47:11` | `cowrie.command.success` |
| `2026-07-29 03:47:11` | `cowrie.command.input` |
| `2026-07-29 03:47:11` | `cowrie.command.input` |
| `2026-07-29 03:47:11` | `cowrie.command.input` |
| `2026-07-29 03:47:11` | `cowrie.command.input` |
| `2026-07-29 03:47:11` | `cowrie.log.closed` |
| `2026-07-29 03:47:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64164c4b9c9e

| Field | Detail |
|---|---|
| **Source IP** | `106.201.230[.]195` |
| **First Seen** | 2026-07-29 03:47 |
| **Last Seen** | 2026-07-29 03:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:47:22` | `cowrie.session.connect` |
| `2026-07-29 03:47:23` | `cowrie.client.version` |
| `2026-07-29 03:47:23` | `cowrie.client.kex` |
| `2026-07-29 03:47:24` | `cowrie.login.success` |
| `2026-07-29 03:47:24` | `cowrie.direct-tcpip.request` |
| `2026-07-29 03:47:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.201.230[.]195` to AbuseIPDB if not already reported
- [ ] Block `106.201.230[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38f3584fdc43

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:48 |
| **Last Seen** | 2026-07-29 03:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:48:35` | `cowrie.session.connect` |
| `2026-07-29 03:48:35` | `cowrie.client.version` |
| `2026-07-29 03:48:35` | `cowrie.client.kex` |
| `2026-07-29 03:48:36` | `cowrie.login.success` |
| `2026-07-29 03:48:37` | `cowrie.session.params` |
| `2026-07-29 03:48:37` | `cowrie.command.input` |
| `2026-07-29 03:48:37` | `cowrie.command.input` |
| `2026-07-29 03:48:37` | `cowrie.command.input` |
| `2026-07-29 03:48:37` | `cowrie.command.input` |
| `2026-07-29 03:48:37` | `cowrie.command.input` |
| `2026-07-29 03:48:37` | `cowrie.command.success` |
| `2026-07-29 03:48:37` | `cowrie.command.input` |
| `2026-07-29 03:48:37` | `cowrie.command.input` |
| `2026-07-29 03:48:37` | `cowrie.command.input` |
| `2026-07-29 03:48:37` | `cowrie.command.input` |
| `2026-07-29 03:48:38` | `cowrie.log.closed` |
| `2026-07-29 03:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-922a317fd5d2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:50 |
| **Last Seen** | 2026-07-29 03:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:50:01` | `cowrie.session.connect` |
| `2026-07-29 03:50:02` | `cowrie.client.version` |
| `2026-07-29 03:50:02` | `cowrie.client.kex` |
| `2026-07-29 03:50:03` | `cowrie.login.success` |
| `2026-07-29 03:50:04` | `cowrie.session.params` |
| `2026-07-29 03:50:04` | `cowrie.command.input` |
| `2026-07-29 03:50:04` | `cowrie.command.input` |
| `2026-07-29 03:50:04` | `cowrie.command.input` |
| `2026-07-29 03:50:04` | `cowrie.command.input` |
| `2026-07-29 03:50:04` | `cowrie.command.input` |
| `2026-07-29 03:50:04` | `cowrie.command.success` |
| `2026-07-29 03:50:04` | `cowrie.command.input` |
| `2026-07-29 03:50:04` | `cowrie.command.input` |
| `2026-07-29 03:50:04` | `cowrie.command.input` |
| `2026-07-29 03:50:04` | `cowrie.command.input` |
| `2026-07-29 03:50:04` | `cowrie.log.closed` |
| `2026-07-29 03:50:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fe93e4ef1d7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:50 |
| **Last Seen** | 2026-07-29 03:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:50:14` | `cowrie.session.connect` |
| `2026-07-29 03:50:14` | `cowrie.client.version` |
| `2026-07-29 03:50:14` | `cowrie.client.kex` |
| `2026-07-29 03:50:15` | `cowrie.login.success` |
| `2026-07-29 03:50:16` | `cowrie.session.params` |
| `2026-07-29 03:50:16` | `cowrie.command.input` |
| `2026-07-29 03:50:16` | `cowrie.command.input` |
| `2026-07-29 03:50:16` | `cowrie.command.input` |
| `2026-07-29 03:50:16` | `cowrie.command.input` |
| `2026-07-29 03:50:16` | `cowrie.command.input` |
| `2026-07-29 03:50:16` | `cowrie.command.success` |
| `2026-07-29 03:50:16` | `cowrie.command.input` |
| `2026-07-29 03:50:16` | `cowrie.command.input` |
| `2026-07-29 03:50:16` | `cowrie.command.input` |
| `2026-07-29 03:50:16` | `cowrie.command.input` |
| `2026-07-29 03:50:16` | `cowrie.log.closed` |
| `2026-07-29 03:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-244e0bf1601f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:51 |
| **Last Seen** | 2026-07-29 03:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:51:32` | `cowrie.session.connect` |
| `2026-07-29 03:51:32` | `cowrie.client.version` |
| `2026-07-29 03:51:32` | `cowrie.client.kex` |
| `2026-07-29 03:51:33` | `cowrie.login.success` |
| `2026-07-29 03:51:34` | `cowrie.session.params` |
| `2026-07-29 03:51:34` | `cowrie.command.input` |
| `2026-07-29 03:51:34` | `cowrie.command.input` |
| `2026-07-29 03:51:34` | `cowrie.command.input` |
| `2026-07-29 03:51:34` | `cowrie.command.input` |
| `2026-07-29 03:51:34` | `cowrie.command.input` |
| `2026-07-29 03:51:34` | `cowrie.command.success` |
| `2026-07-29 03:51:34` | `cowrie.command.input` |
| `2026-07-29 03:51:34` | `cowrie.command.input` |
| `2026-07-29 03:51:34` | `cowrie.command.input` |
| `2026-07-29 03:51:34` | `cowrie.command.input` |
| `2026-07-29 03:51:34` | `cowrie.log.closed` |
| `2026-07-29 03:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91bd6d789dd9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:53 |
| **Last Seen** | 2026-07-29 03:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:53:01` | `cowrie.session.connect` |
| `2026-07-29 03:53:02` | `cowrie.client.version` |
| `2026-07-29 03:53:02` | `cowrie.client.kex` |
| `2026-07-29 03:53:02` | `cowrie.login.success` |
| `2026-07-29 03:53:04` | `cowrie.session.params` |
| `2026-07-29 03:53:04` | `cowrie.command.input` |
| `2026-07-29 03:53:04` | `cowrie.command.input` |
| `2026-07-29 03:53:04` | `cowrie.command.input` |
| `2026-07-29 03:53:04` | `cowrie.command.input` |
| `2026-07-29 03:53:04` | `cowrie.command.input` |
| `2026-07-29 03:53:04` | `cowrie.command.success` |
| `2026-07-29 03:53:04` | `cowrie.command.input` |
| `2026-07-29 03:53:04` | `cowrie.command.input` |
| `2026-07-29 03:53:04` | `cowrie.command.input` |
| `2026-07-29 03:53:04` | `cowrie.command.input` |
| `2026-07-29 03:53:04` | `cowrie.log.closed` |
| `2026-07-29 03:53:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45f5bf527597

| Field | Detail |
|---|---|
| **Source IP** | `201.28.237[.]90` |
| **First Seen** | 2026-07-29 03:54 |
| **Last Seen** | 2026-07-29 03:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:54:10` | `cowrie.session.connect` |
| `2026-07-29 03:54:10` | `cowrie.client.version` |
| `2026-07-29 03:54:10` | `cowrie.client.kex` |
| `2026-07-29 03:54:12` | `cowrie.login.success` |
| `2026-07-29 03:54:13` | `cowrie.direct-tcpip.request` |
| `2026-07-29 03:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.237[.]90` to AbuseIPDB if not already reported
- [ ] Block `201.28.237[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8a5c9ba2fda

| Field | Detail |
|---|---|
| **Source IP** | `85.19.195[.]12` |
| **First Seen** | 2026-07-29 03:54 |
| **Last Seen** | 2026-07-29 03:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:54:17` | `cowrie.session.connect` |
| `2026-07-29 03:54:18` | `cowrie.client.version` |
| `2026-07-29 03:54:18` | `cowrie.client.kex` |
| `2026-07-29 03:54:18` | `cowrie.login.success` |
| `2026-07-29 03:54:19` | `cowrie.direct-tcpip.request` |
| `2026-07-29 03:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.19.195[.]12` to AbuseIPDB if not already reported
- [ ] Block `85.19.195[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c1548fe8b76

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:54 |
| **Last Seen** | 2026-07-29 03:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:54:30` | `cowrie.session.connect` |
| `2026-07-29 03:54:30` | `cowrie.client.version` |
| `2026-07-29 03:54:30` | `cowrie.client.kex` |
| `2026-07-29 03:54:31` | `cowrie.login.success` |
| `2026-07-29 03:54:32` | `cowrie.session.params` |
| `2026-07-29 03:54:32` | `cowrie.command.input` |
| `2026-07-29 03:54:32` | `cowrie.command.input` |
| `2026-07-29 03:54:32` | `cowrie.command.input` |
| `2026-07-29 03:54:32` | `cowrie.command.input` |
| `2026-07-29 03:54:32` | `cowrie.command.input` |
| `2026-07-29 03:54:32` | `cowrie.command.success` |
| `2026-07-29 03:54:32` | `cowrie.command.input` |
| `2026-07-29 03:54:32` | `cowrie.command.input` |
| `2026-07-29 03:54:32` | `cowrie.command.input` |
| `2026-07-29 03:54:32` | `cowrie.command.input` |
| `2026-07-29 03:54:32` | `cowrie.log.closed` |
| `2026-07-29 03:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e2d827dbc60

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:54 |
| **Last Seen** | 2026-07-29 03:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:54:33` | `cowrie.session.connect` |
| `2026-07-29 03:54:33` | `cowrie.client.version` |
| `2026-07-29 03:54:33` | `cowrie.client.kex` |
| `2026-07-29 03:54:34` | `cowrie.login.success` |
| `2026-07-29 03:54:35` | `cowrie.session.params` |
| `2026-07-29 03:54:35` | `cowrie.command.input` |
| `2026-07-29 03:54:35` | `cowrie.command.input` |
| `2026-07-29 03:54:35` | `cowrie.command.input` |
| `2026-07-29 03:54:35` | `cowrie.command.input` |
| `2026-07-29 03:54:35` | `cowrie.command.input` |
| `2026-07-29 03:54:35` | `cowrie.command.success` |
| `2026-07-29 03:54:35` | `cowrie.command.input` |
| `2026-07-29 03:54:35` | `cowrie.command.input` |
| `2026-07-29 03:54:35` | `cowrie.command.input` |
| `2026-07-29 03:54:35` | `cowrie.command.input` |
| `2026-07-29 03:54:35` | `cowrie.log.closed` |
| `2026-07-29 03:54:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1aee766d9ae

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:55 |
| **Last Seen** | 2026-07-29 03:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:55:56` | `cowrie.session.connect` |
| `2026-07-29 03:55:56` | `cowrie.client.version` |
| `2026-07-29 03:55:57` | `cowrie.client.kex` |
| `2026-07-29 03:55:57` | `cowrie.login.success` |
| `2026-07-29 03:55:59` | `cowrie.session.params` |
| `2026-07-29 03:55:59` | `cowrie.command.input` |
| `2026-07-29 03:55:59` | `cowrie.command.input` |
| `2026-07-29 03:55:59` | `cowrie.command.input` |
| `2026-07-29 03:55:59` | `cowrie.command.input` |
| `2026-07-29 03:55:59` | `cowrie.command.input` |
| `2026-07-29 03:55:59` | `cowrie.command.success` |
| `2026-07-29 03:55:59` | `cowrie.command.input` |
| `2026-07-29 03:55:59` | `cowrie.command.input` |
| `2026-07-29 03:55:59` | `cowrie.command.input` |
| `2026-07-29 03:55:59` | `cowrie.command.input` |
| `2026-07-29 03:55:59` | `cowrie.log.closed` |
| `2026-07-29 03:55:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c80a33793f5b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 03:56 |
| **Last Seen** | 2026-07-29 03:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:56:13` | `cowrie.session.connect` |
| `2026-07-29 03:56:13` | `cowrie.client.version` |
| `2026-07-29 03:56:13` | `cowrie.client.kex` |
| `2026-07-29 03:56:13` | `cowrie.login.success` |
| `2026-07-29 03:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98eac4bd0376

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 03:56 |
| **Last Seen** | 2026-07-29 03:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:56:13` | `cowrie.session.connect` |
| `2026-07-29 03:56:13` | `cowrie.client.version` |
| `2026-07-29 03:56:13` | `cowrie.client.kex` |
| `2026-07-29 03:56:13` | `cowrie.login.success` |
| `2026-07-29 03:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a246000de55

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 03:56 |
| **Last Seen** | 2026-07-29 03:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:56:17` | `cowrie.session.connect` |
| `2026-07-29 03:56:17` | `cowrie.client.version` |
| `2026-07-29 03:56:17` | `cowrie.client.kex` |
| `2026-07-29 03:56:17` | `cowrie.login.success` |
| `2026-07-29 03:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fa60b1fc73a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 03:56 |
| **Last Seen** | 2026-07-29 03:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:56:17` | `cowrie.session.connect` |
| `2026-07-29 03:56:17` | `cowrie.client.version` |
| `2026-07-29 03:56:17` | `cowrie.client.kex` |
| `2026-07-29 03:56:17` | `cowrie.login.success` |
| `2026-07-29 03:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b316de5bd62b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:57 |
| **Last Seen** | 2026-07-29 03:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:57:09` | `cowrie.session.connect` |
| `2026-07-29 03:57:09` | `cowrie.client.version` |
| `2026-07-29 03:57:09` | `cowrie.client.kex` |
| `2026-07-29 03:57:10` | `cowrie.login.success` |
| `2026-07-29 03:57:11` | `cowrie.session.params` |
| `2026-07-29 03:57:11` | `cowrie.command.input` |
| `2026-07-29 03:57:11` | `cowrie.command.input` |
| `2026-07-29 03:57:11` | `cowrie.command.input` |
| `2026-07-29 03:57:11` | `cowrie.command.input` |
| `2026-07-29 03:57:11` | `cowrie.command.input` |
| `2026-07-29 03:57:11` | `cowrie.command.success` |
| `2026-07-29 03:57:11` | `cowrie.command.input` |
| `2026-07-29 03:57:11` | `cowrie.command.input` |
| `2026-07-29 03:57:11` | `cowrie.command.input` |
| `2026-07-29 03:57:11` | `cowrie.command.input` |
| `2026-07-29 03:57:11` | `cowrie.log.closed` |
| `2026-07-29 03:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d6c98520233

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:57 |
| **Last Seen** | 2026-07-29 03:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:57:25` | `cowrie.session.connect` |
| `2026-07-29 03:57:25` | `cowrie.client.version` |
| `2026-07-29 03:57:25` | `cowrie.client.kex` |
| `2026-07-29 03:57:26` | `cowrie.login.success` |
| `2026-07-29 03:57:27` | `cowrie.session.params` |
| `2026-07-29 03:57:27` | `cowrie.command.input` |
| `2026-07-29 03:57:27` | `cowrie.command.input` |
| `2026-07-29 03:57:27` | `cowrie.command.input` |
| `2026-07-29 03:57:27` | `cowrie.command.input` |
| `2026-07-29 03:57:27` | `cowrie.command.input` |
| `2026-07-29 03:57:27` | `cowrie.command.success` |
| `2026-07-29 03:57:27` | `cowrie.command.input` |
| `2026-07-29 03:57:27` | `cowrie.command.input` |
| `2026-07-29 03:57:27` | `cowrie.command.input` |
| `2026-07-29 03:57:27` | `cowrie.command.input` |
| `2026-07-29 03:57:28` | `cowrie.log.closed` |
| `2026-07-29 03:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b26ec46c826

| Field | Detail |
|---|---|
| **Source IP** | `220.74.119[.]84` |
| **First Seen** | 2026-07-29 03:57 |
| **Last Seen** | 2026-07-29 03:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:57:37` | `cowrie.session.connect` |
| `2026-07-29 03:57:38` | `cowrie.client.version` |
| `2026-07-29 03:57:38` | `cowrie.client.kex` |
| `2026-07-29 03:57:40` | `cowrie.login.success` |
| `2026-07-29 03:57:41` | `cowrie.direct-tcpip.request` |
| `2026-07-29 03:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.74.119[.]84` to AbuseIPDB if not already reported
- [ ] Block `220.74.119[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ab6eb1cf697

| Field | Detail |
|---|---|
| **Source IP** | `60.174.35[.]18` |
| **First Seen** | 2026-07-29 03:57 |
| **Last Seen** | 2026-07-29 03:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:57:47` | `cowrie.session.connect` |
| `2026-07-29 03:57:48` | `cowrie.client.version` |
| `2026-07-29 03:57:48` | `cowrie.client.kex` |
| `2026-07-29 03:57:50` | `cowrie.login.success` |
| `2026-07-29 03:57:51` | `cowrie.direct-tcpip.request` |
| `2026-07-29 03:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.35[.]18` to AbuseIPDB if not already reported
- [ ] Block `60.174.35[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-487d21461267

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 03:58 |
| **Last Seen** | 2026-07-29 03:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:58:49` | `cowrie.session.connect` |
| `2026-07-29 03:58:49` | `cowrie.client.version` |
| `2026-07-29 03:58:49` | `cowrie.client.kex` |
| `2026-07-29 03:58:50` | `cowrie.login.success` |
| `2026-07-29 03:58:51` | `cowrie.session.params` |
| `2026-07-29 03:58:51` | `cowrie.command.input` |
| `2026-07-29 03:58:51` | `cowrie.command.input` |
| `2026-07-29 03:58:51` | `cowrie.command.input` |
| `2026-07-29 03:58:51` | `cowrie.command.input` |
| `2026-07-29 03:58:51` | `cowrie.command.input` |
| `2026-07-29 03:58:51` | `cowrie.command.success` |
| `2026-07-29 03:58:51` | `cowrie.command.input` |
| `2026-07-29 03:58:51` | `cowrie.command.input` |
| `2026-07-29 03:58:51` | `cowrie.command.input` |
| `2026-07-29 03:58:51` | `cowrie.command.input` |
| `2026-07-29 03:58:52` | `cowrie.log.closed` |
| `2026-07-29 03:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74a613c895ef

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 03:59 |
| **Last Seen** | 2026-07-29 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 03:59:53` | `cowrie.session.connect` |
| `2026-07-29 03:59:53` | `cowrie.client.version` |
| `2026-07-29 03:59:53` | `cowrie.client.kex` |
| `2026-07-29 03:59:53` | `cowrie.login.success` |
| `2026-07-29 03:59:54` | `cowrie.session.params` |
| `2026-07-29 03:59:54` | `cowrie.command.input` |
| `2026-07-29 03:59:54` | `cowrie.command.input` |
| `2026-07-29 03:59:54` | `cowrie.command.input` |
| `2026-07-29 03:59:54` | `cowrie.command.input` |
| `2026-07-29 03:59:54` | `cowrie.command.input` |
| `2026-07-29 03:59:54` | `cowrie.command.success` |
| `2026-07-29 03:59:54` | `cowrie.command.input` |
| `2026-07-29 03:59:54` | `cowrie.command.input` |
| `2026-07-29 03:59:54` | `cowrie.command.input` |
| `2026-07-29 03:59:54` | `cowrie.command.input` |
| `2026-07-29 03:59:55` | `cowrie.log.closed` |
| `2026-07-29 03:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05a51b543512

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 04:00 |
| **Last Seen** | 2026-07-29 04:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:00:09` | `cowrie.session.connect` |
| `2026-07-29 04:00:09` | `cowrie.client.version` |
| `2026-07-29 04:00:09` | `cowrie.client.kex` |
| `2026-07-29 04:00:10` | `cowrie.login.success` |
| `2026-07-29 04:00:11` | `cowrie.session.params` |
| `2026-07-29 04:00:11` | `cowrie.command.input` |
| `2026-07-29 04:00:11` | `cowrie.command.input` |
| `2026-07-29 04:00:11` | `cowrie.command.input` |
| `2026-07-29 04:00:11` | `cowrie.command.input` |
| `2026-07-29 04:00:11` | `cowrie.command.input` |
| `2026-07-29 04:00:11` | `cowrie.command.success` |
| `2026-07-29 04:00:11` | `cowrie.command.input` |
| `2026-07-29 04:00:11` | `cowrie.command.input` |
| `2026-07-29 04:00:12` | `cowrie.command.input` |
| `2026-07-29 04:00:12` | `cowrie.command.input` |
| `2026-07-29 04:00:12` | `cowrie.log.closed` |
| `2026-07-29 04:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-868a77d4bc41

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 04:01 |
| **Last Seen** | 2026-07-29 04:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:01:29` | `cowrie.session.connect` |
| `2026-07-29 04:01:29` | `cowrie.client.version` |
| `2026-07-29 04:01:29` | `cowrie.client.kex` |
| `2026-07-29 04:01:31` | `cowrie.login.success` |
| `2026-07-29 04:01:33` | `cowrie.session.params` |
| `2026-07-29 04:01:33` | `cowrie.command.input` |
| `2026-07-29 04:01:33` | `cowrie.command.input` |
| `2026-07-29 04:01:33` | `cowrie.command.input` |
| `2026-07-29 04:01:33` | `cowrie.command.input` |
| `2026-07-29 04:01:33` | `cowrie.command.input` |
| `2026-07-29 04:01:33` | `cowrie.command.success` |
| `2026-07-29 04:01:33` | `cowrie.command.input` |
| `2026-07-29 04:01:33` | `cowrie.command.input` |
| `2026-07-29 04:01:33` | `cowrie.command.input` |
| `2026-07-29 04:01:33` | `cowrie.command.input` |
| `2026-07-29 04:01:33` | `cowrie.log.closed` |
| `2026-07-29 04:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc64e09a6626

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 04:02 |
| **Last Seen** | 2026-07-29 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:02:02` | `cowrie.session.connect` |
| `2026-07-29 04:02:02` | `cowrie.client.version` |
| `2026-07-29 04:02:02` | `cowrie.client.kex` |
| `2026-07-29 04:02:03` | `cowrie.login.success` |
| `2026-07-29 04:02:04` | `cowrie.session.params` |
| `2026-07-29 04:02:04` | `cowrie.command.input` |
| `2026-07-29 04:02:04` | `cowrie.command.input` |
| `2026-07-29 04:02:04` | `cowrie.command.input` |
| `2026-07-29 04:02:04` | `cowrie.command.input` |
| `2026-07-29 04:02:04` | `cowrie.command.input` |
| `2026-07-29 04:02:04` | `cowrie.command.success` |
| `2026-07-29 04:02:04` | `cowrie.command.input` |
| `2026-07-29 04:02:04` | `cowrie.command.input` |
| `2026-07-29 04:02:04` | `cowrie.command.input` |
| `2026-07-29 04:02:04` | `cowrie.command.input` |
| `2026-07-29 04:02:04` | `cowrie.log.closed` |
| `2026-07-29 04:02:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c697603c284f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 04:02 |
| **Last Seen** | 2026-07-29 04:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:02:49` | `cowrie.session.connect` |
| `2026-07-29 04:02:49` | `cowrie.client.version` |
| `2026-07-29 04:02:49` | `cowrie.client.kex` |
| `2026-07-29 04:02:51` | `cowrie.login.success` |
| `2026-07-29 04:02:52` | `cowrie.session.params` |
| `2026-07-29 04:02:52` | `cowrie.command.input` |
| `2026-07-29 04:02:52` | `cowrie.command.input` |
| `2026-07-29 04:02:52` | `cowrie.command.input` |
| `2026-07-29 04:02:52` | `cowrie.command.input` |
| `2026-07-29 04:02:52` | `cowrie.command.input` |
| `2026-07-29 04:02:52` | `cowrie.command.success` |
| `2026-07-29 04:02:52` | `cowrie.command.input` |
| `2026-07-29 04:02:52` | `cowrie.command.input` |
| `2026-07-29 04:02:52` | `cowrie.command.input` |
| `2026-07-29 04:02:52` | `cowrie.command.input` |
| `2026-07-29 04:02:53` | `cowrie.log.closed` |
| `2026-07-29 04:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b88abfc56e8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 04:04 |
| **Last Seen** | 2026-07-29 04:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:04:08` | `cowrie.session.connect` |
| `2026-07-29 04:04:08` | `cowrie.client.version` |
| `2026-07-29 04:04:08` | `cowrie.client.kex` |
| `2026-07-29 04:04:10` | `cowrie.login.success` |
| `2026-07-29 04:04:12` | `cowrie.session.params` |
| `2026-07-29 04:04:12` | `cowrie.command.input` |
| `2026-07-29 04:04:12` | `cowrie.command.input` |
| `2026-07-29 04:04:12` | `cowrie.command.input` |
| `2026-07-29 04:04:12` | `cowrie.command.input` |
| `2026-07-29 04:04:12` | `cowrie.command.input` |
| `2026-07-29 04:04:12` | `cowrie.command.success` |
| `2026-07-29 04:04:12` | `cowrie.command.input` |
| `2026-07-29 04:04:12` | `cowrie.command.input` |
| `2026-07-29 04:04:12` | `cowrie.command.input` |
| `2026-07-29 04:04:12` | `cowrie.command.input` |
| `2026-07-29 04:04:12` | `cowrie.log.closed` |
| `2026-07-29 04:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f579dc02c8ab

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 04:05 |
| **Last Seen** | 2026-07-29 04:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:05:31` | `cowrie.session.connect` |
| `2026-07-29 04:05:32` | `cowrie.client.version` |
| `2026-07-29 04:05:32` | `cowrie.client.kex` |
| `2026-07-29 04:05:33` | `cowrie.login.success` |
| `2026-07-29 04:05:34` | `cowrie.session.params` |
| `2026-07-29 04:05:34` | `cowrie.command.input` |
| `2026-07-29 04:05:34` | `cowrie.command.input` |
| `2026-07-29 04:05:34` | `cowrie.command.input` |
| `2026-07-29 04:05:34` | `cowrie.command.input` |
| `2026-07-29 04:05:34` | `cowrie.command.input` |
| `2026-07-29 04:05:34` | `cowrie.command.success` |
| `2026-07-29 04:05:34` | `cowrie.command.input` |
| `2026-07-29 04:05:34` | `cowrie.command.input` |
| `2026-07-29 04:05:34` | `cowrie.command.input` |
| `2026-07-29 04:05:34` | `cowrie.command.input` |
| `2026-07-29 04:05:35` | `cowrie.log.closed` |
| `2026-07-29 04:05:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2d4ba5499f1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 04:06 |
| **Last Seen** | 2026-07-29 04:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:06:55` | `cowrie.session.connect` |
| `2026-07-29 04:06:55` | `cowrie.client.version` |
| `2026-07-29 04:06:55` | `cowrie.client.kex` |
| `2026-07-29 04:06:56` | `cowrie.login.success` |
| `2026-07-29 04:06:57` | `cowrie.session.params` |
| `2026-07-29 04:06:57` | `cowrie.command.input` |
| `2026-07-29 04:06:57` | `cowrie.command.input` |
| `2026-07-29 04:06:57` | `cowrie.command.input` |
| `2026-07-29 04:06:57` | `cowrie.command.input` |
| `2026-07-29 04:06:58` | `cowrie.command.input` |
| `2026-07-29 04:06:58` | `cowrie.command.success` |
| `2026-07-29 04:06:58` | `cowrie.command.input` |
| `2026-07-29 04:06:58` | `cowrie.command.input` |
| `2026-07-29 04:06:58` | `cowrie.command.input` |
| `2026-07-29 04:06:58` | `cowrie.command.input` |
| `2026-07-29 04:06:58` | `cowrie.log.closed` |
| `2026-07-29 04:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa1fab733dea

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 04:07 |
| **Last Seen** | 2026-07-29 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:07:33` | `cowrie.session.connect` |
| `2026-07-29 04:07:33` | `cowrie.client.version` |
| `2026-07-29 04:07:33` | `cowrie.client.kex` |
| `2026-07-29 04:07:34` | `cowrie.login.success` |
| `2026-07-29 04:07:34` | `cowrie.session.params` |
| `2026-07-29 04:07:34` | `cowrie.command.input` |
| `2026-07-29 04:07:34` | `cowrie.command.input` |
| `2026-07-29 04:07:34` | `cowrie.command.input` |
| `2026-07-29 04:07:34` | `cowrie.command.input` |
| `2026-07-29 04:07:34` | `cowrie.command.input` |
| `2026-07-29 04:07:34` | `cowrie.command.success` |
| `2026-07-29 04:07:34` | `cowrie.command.input` |
| `2026-07-29 04:07:34` | `cowrie.command.input` |
| `2026-07-29 04:07:34` | `cowrie.command.input` |
| `2026-07-29 04:07:34` | `cowrie.command.input` |
| `2026-07-29 04:07:35` | `cowrie.log.closed` |
| `2026-07-29 04:07:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee1f50cd249c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 04:08 |
| **Last Seen** | 2026-07-29 04:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:08:15` | `cowrie.session.connect` |
| `2026-07-29 04:08:16` | `cowrie.client.version` |
| `2026-07-29 04:08:16` | `cowrie.client.kex` |
| `2026-07-29 04:08:17` | `cowrie.login.success` |
| `2026-07-29 04:08:19` | `cowrie.session.params` |
| `2026-07-29 04:08:19` | `cowrie.command.input` |
| `2026-07-29 04:08:19` | `cowrie.command.input` |
| `2026-07-29 04:08:19` | `cowrie.command.input` |
| `2026-07-29 04:08:19` | `cowrie.command.input` |
| `2026-07-29 04:08:19` | `cowrie.command.input` |
| `2026-07-29 04:08:19` | `cowrie.command.success` |
| `2026-07-29 04:08:19` | `cowrie.command.input` |
| `2026-07-29 04:08:19` | `cowrie.command.input` |
| `2026-07-29 04:08:19` | `cowrie.command.input` |
| `2026-07-29 04:08:19` | `cowrie.command.input` |
| `2026-07-29 04:08:19` | `cowrie.log.closed` |
| `2026-07-29 04:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7998adce429

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]59` |
| **First Seen** | 2026-07-29 04:08 |
| **Last Seen** | 2026-07-29 04:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:08:29` | `cowrie.session.connect` |
| `2026-07-29 04:08:30` | `cowrie.client.version` |
| `2026-07-29 04:08:30` | `cowrie.client.kex` |
| `2026-07-29 04:08:31` | `cowrie.login.success` |
| `2026-07-29 04:08:31` | `cowrie.direct-tcpip.request` |
| `2026-07-29 04:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]59` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-781d47ba94e1

| Field | Detail |
|---|---|
| **Source IP** | `1.212.225[.]99` |
| **First Seen** | 2026-07-29 04:08 |
| **Last Seen** | 2026-07-29 04:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:08:45` | `cowrie.session.connect` |
| `2026-07-29 04:08:46` | `cowrie.client.version` |
| `2026-07-29 04:08:46` | `cowrie.client.kex` |
| `2026-07-29 04:08:48` | `cowrie.login.success` |
| `2026-07-29 04:08:49` | `cowrie.direct-tcpip.request` |
| `2026-07-29 04:08:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.212.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `1.212.225[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-824560e97f45

| Field | Detail |
|---|---|
| **Source IP** | `182.73.164[.]228` |
| **First Seen** | 2026-07-29 04:08 |
| **Last Seen** | 2026-07-29 04:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:08:54` | `cowrie.session.connect` |
| `2026-07-29 04:08:55` | `cowrie.client.version` |
| `2026-07-29 04:08:55` | `cowrie.client.kex` |
| `2026-07-29 04:08:57` | `cowrie.login.success` |
| `2026-07-29 04:08:58` | `cowrie.direct-tcpip.request` |
| `2026-07-29 04:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.73.164[.]228` to AbuseIPDB if not already reported
- [ ] Block `182.73.164[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f1bf84202c1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 04:09 |
| **Last Seen** | 2026-07-29 04:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:09:36` | `cowrie.session.connect` |
| `2026-07-29 04:09:36` | `cowrie.client.version` |
| `2026-07-29 04:09:36` | `cowrie.client.kex` |
| `2026-07-29 04:09:38` | `cowrie.login.success` |
| `2026-07-29 04:09:39` | `cowrie.session.params` |
| `2026-07-29 04:09:39` | `cowrie.command.input` |
| `2026-07-29 04:09:39` | `cowrie.command.input` |
| `2026-07-29 04:09:39` | `cowrie.command.input` |
| `2026-07-29 04:09:39` | `cowrie.command.input` |
| `2026-07-29 04:09:39` | `cowrie.command.input` |
| `2026-07-29 04:09:39` | `cowrie.command.success` |
| `2026-07-29 04:09:39` | `cowrie.command.input` |
| `2026-07-29 04:09:39` | `cowrie.command.input` |
| `2026-07-29 04:09:39` | `cowrie.command.input` |
| `2026-07-29 04:09:39` | `cowrie.command.input` |
| `2026-07-29 04:09:40` | `cowrie.log.closed` |
| `2026-07-29 04:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00cb93ea784e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 04:10 |
| **Last Seen** | 2026-07-29 04:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:10:54` | `cowrie.session.connect` |
| `2026-07-29 04:10:54` | `cowrie.client.version` |
| `2026-07-29 04:10:54` | `cowrie.client.kex` |
| `2026-07-29 04:10:56` | `cowrie.login.success` |
| `2026-07-29 04:10:57` | `cowrie.session.params` |
| `2026-07-29 04:10:57` | `cowrie.command.input` |
| `2026-07-29 04:10:57` | `cowrie.command.input` |
| `2026-07-29 04:10:57` | `cowrie.command.input` |
| `2026-07-29 04:10:57` | `cowrie.command.input` |
| `2026-07-29 04:10:57` | `cowrie.command.input` |
| `2026-07-29 04:10:57` | `cowrie.command.success` |
| `2026-07-29 04:10:57` | `cowrie.command.input` |
| `2026-07-29 04:10:57` | `cowrie.command.input` |
| `2026-07-29 04:10:57` | `cowrie.command.input` |
| `2026-07-29 04:10:57` | `cowrie.command.input` |
| `2026-07-29 04:10:58` | `cowrie.log.closed` |
| `2026-07-29 04:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e05032a18c6

| Field | Detail |
|---|---|
| **Source IP** | `58.17.128[.]7` |
| **First Seen** | 2026-07-29 04:11 |
| **Last Seen** | 2026-07-29 04:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:11:55` | `cowrie.session.connect` |
| `2026-07-29 04:11:55` | `cowrie.client.version` |
| `2026-07-29 04:11:55` | `cowrie.client.kex` |
| `2026-07-29 04:11:58` | `cowrie.login.success` |
| `2026-07-29 04:11:59` | `cowrie.direct-tcpip.request` |
| `2026-07-29 04:12:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.17.128[.]7` to AbuseIPDB if not already reported
- [ ] Block `58.17.128[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4681b667bbc

| Field | Detail |
|---|---|
| **Source IP** | `125.20.207[.]154` |
| **First Seen** | 2026-07-29 04:12 |
| **Last Seen** | 2026-07-29 04:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:12:08` | `cowrie.session.connect` |
| `2026-07-29 04:12:09` | `cowrie.client.version` |
| `2026-07-29 04:12:09` | `cowrie.client.kex` |
| `2026-07-29 04:12:13` | `cowrie.login.success` |
| `2026-07-29 04:12:13` | `cowrie.direct-tcpip.request` |
| `2026-07-29 04:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.20.207[.]154` to AbuseIPDB if not already reported
- [ ] Block `125.20.207[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f392d2681c44

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 04:12 |
| **Last Seen** | 2026-07-29 04:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:12:13` | `cowrie.session.connect` |
| `2026-07-29 04:12:13` | `cowrie.client.version` |
| `2026-07-29 04:12:13` | `cowrie.client.kex` |
| `2026-07-29 04:12:15` | `cowrie.login.success` |
| `2026-07-29 04:12:16` | `cowrie.session.params` |
| `2026-07-29 04:12:16` | `cowrie.command.input` |
| `2026-07-29 04:12:16` | `cowrie.command.input` |
| `2026-07-29 04:12:16` | `cowrie.command.input` |
| `2026-07-29 04:12:16` | `cowrie.command.input` |
| `2026-07-29 04:12:16` | `cowrie.command.input` |
| `2026-07-29 04:12:16` | `cowrie.command.success` |
| `2026-07-29 04:12:16` | `cowrie.command.input` |
| `2026-07-29 04:12:16` | `cowrie.command.input` |
| `2026-07-29 04:12:16` | `cowrie.command.input` |
| `2026-07-29 04:12:16` | `cowrie.command.input` |
| `2026-07-29 04:12:17` | `cowrie.log.closed` |
| `2026-07-29 04:12:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e652708f9e37

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 04:13 |
| **Last Seen** | 2026-07-29 04:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:13:34` | `cowrie.session.connect` |
| `2026-07-29 04:13:34` | `cowrie.client.version` |
| `2026-07-29 04:13:34` | `cowrie.client.kex` |
| `2026-07-29 04:13:35` | `cowrie.login.success` |
| `2026-07-29 04:13:37` | `cowrie.session.params` |
| `2026-07-29 04:13:37` | `cowrie.command.input` |
| `2026-07-29 04:13:37` | `cowrie.command.input` |
| `2026-07-29 04:13:37` | `cowrie.command.input` |
| `2026-07-29 04:13:37` | `cowrie.command.input` |
| `2026-07-29 04:13:37` | `cowrie.command.input` |
| `2026-07-29 04:13:37` | `cowrie.command.success` |
| `2026-07-29 04:13:37` | `cowrie.command.input` |
| `2026-07-29 04:13:37` | `cowrie.command.input` |
| `2026-07-29 04:13:37` | `cowrie.command.input` |
| `2026-07-29 04:13:37` | `cowrie.command.input` |
| `2026-07-29 04:13:37` | `cowrie.log.closed` |
| `2026-07-29 04:13:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d35762bc0dfe

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 04:14 |
| **Last Seen** | 2026-07-29 04:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:14:54` | `cowrie.session.connect` |
| `2026-07-29 04:14:54` | `cowrie.client.version` |
| `2026-07-29 04:14:54` | `cowrie.client.kex` |
| `2026-07-29 04:14:55` | `cowrie.login.success` |
| `2026-07-29 04:14:56` | `cowrie.session.params` |
| `2026-07-29 04:14:56` | `cowrie.command.input` |
| `2026-07-29 04:14:56` | `cowrie.command.input` |
| `2026-07-29 04:14:56` | `cowrie.command.input` |
| `2026-07-29 04:14:56` | `cowrie.command.input` |
| `2026-07-29 04:14:56` | `cowrie.command.input` |
| `2026-07-29 04:14:56` | `cowrie.command.success` |
| `2026-07-29 04:14:56` | `cowrie.command.input` |
| `2026-07-29 04:14:56` | `cowrie.command.input` |
| `2026-07-29 04:14:56` | `cowrie.command.input` |
| `2026-07-29 04:14:56` | `cowrie.command.input` |
| `2026-07-29 04:14:57` | `cowrie.log.closed` |
| `2026-07-29 04:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80fcc7093762

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 04:16 |
| **Last Seen** | 2026-07-29 04:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:16:15` | `cowrie.session.connect` |
| `2026-07-29 04:16:15` | `cowrie.client.version` |
| `2026-07-29 04:16:15` | `cowrie.client.kex` |
| `2026-07-29 04:16:16` | `cowrie.login.success` |
| `2026-07-29 04:16:17` | `cowrie.session.params` |
| `2026-07-29 04:16:17` | `cowrie.command.input` |
| `2026-07-29 04:16:17` | `cowrie.command.input` |
| `2026-07-29 04:16:17` | `cowrie.command.input` |
| `2026-07-29 04:16:17` | `cowrie.command.input` |
| `2026-07-29 04:16:17` | `cowrie.command.input` |
| `2026-07-29 04:16:17` | `cowrie.command.success` |
| `2026-07-29 04:16:17` | `cowrie.command.input` |
| `2026-07-29 04:16:17` | `cowrie.command.input` |
| `2026-07-29 04:16:17` | `cowrie.command.input` |
| `2026-07-29 04:16:17` | `cowrie.command.input` |
| `2026-07-29 04:16:17` | `cowrie.log.closed` |
| `2026-07-29 04:16:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf68dab7a245

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 04:17 |
| **Last Seen** | 2026-07-29 04:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:17:37` | `cowrie.session.connect` |
| `2026-07-29 04:17:37` | `cowrie.client.version` |
| `2026-07-29 04:17:37` | `cowrie.client.kex` |
| `2026-07-29 04:17:38` | `cowrie.login.success` |
| `2026-07-29 04:17:39` | `cowrie.session.params` |
| `2026-07-29 04:17:39` | `cowrie.command.input` |
| `2026-07-29 04:17:39` | `cowrie.command.input` |
| `2026-07-29 04:17:39` | `cowrie.command.input` |
| `2026-07-29 04:17:39` | `cowrie.command.input` |
| `2026-07-29 04:17:39` | `cowrie.command.input` |
| `2026-07-29 04:17:39` | `cowrie.command.success` |
| `2026-07-29 04:17:39` | `cowrie.command.input` |
| `2026-07-29 04:17:39` | `cowrie.command.input` |
| `2026-07-29 04:17:39` | `cowrie.command.input` |
| `2026-07-29 04:17:39` | `cowrie.command.input` |
| `2026-07-29 04:17:40` | `cowrie.log.closed` |
| `2026-07-29 04:17:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbdb83da5326

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 04:18 |
| **Last Seen** | 2026-07-29 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:18:10` | `cowrie.session.connect` |
| `2026-07-29 04:18:10` | `cowrie.client.version` |
| `2026-07-29 04:18:11` | `cowrie.client.kex` |
| `2026-07-29 04:18:11` | `cowrie.login.success` |
| `2026-07-29 04:18:12` | `cowrie.session.params` |
| `2026-07-29 04:18:12` | `cowrie.command.input` |
| `2026-07-29 04:18:12` | `cowrie.command.input` |
| `2026-07-29 04:18:12` | `cowrie.command.input` |
| `2026-07-29 04:18:12` | `cowrie.command.input` |
| `2026-07-29 04:18:12` | `cowrie.command.input` |
| `2026-07-29 04:18:12` | `cowrie.command.success` |
| `2026-07-29 04:18:12` | `cowrie.command.input` |
| `2026-07-29 04:18:12` | `cowrie.command.input` |
| `2026-07-29 04:18:12` | `cowrie.command.input` |
| `2026-07-29 04:18:12` | `cowrie.command.input` |
| `2026-07-29 04:18:12` | `cowrie.log.closed` |
| `2026-07-29 04:18:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe63c34eff49

| Field | Detail |
|---|---|
| **Source IP** | `177.174.89[.]99` |
| **First Seen** | 2026-07-29 04:18 |
| **Last Seen** | 2026-07-29 04:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:18:42` | `cowrie.session.connect` |
| `2026-07-29 04:18:42` | `cowrie.client.version` |
| `2026-07-29 04:18:42` | `cowrie.client.kex` |
| `2026-07-29 04:18:44` | `cowrie.login.success` |
| `2026-07-29 04:18:45` | `cowrie.direct-tcpip.request` |
| `2026-07-29 04:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.89[.]99` to AbuseIPDB if not already reported
- [ ] Block `177.174.89[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0fc126be3eb

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-07-29 04:18 |
| **Last Seen** | 2026-07-29 04:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:18:54` | `cowrie.session.connect` |
| `2026-07-29 04:18:55` | `cowrie.client.version` |
| `2026-07-29 04:18:55` | `cowrie.client.kex` |
| `2026-07-29 04:18:57` | `cowrie.login.success` |
| `2026-07-29 04:18:58` | `cowrie.direct-tcpip.request` |
| `2026-07-29 04:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a5a539578f3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-29 04:19 |
| **Last Seen** | 2026-07-29 04:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:19:00` | `cowrie.session.connect` |
| `2026-07-29 04:19:00` | `cowrie.client.version` |
| `2026-07-29 04:19:00` | `cowrie.client.kex` |
| `2026-07-29 04:19:01` | `cowrie.login.success` |
| `2026-07-29 04:19:03` | `cowrie.session.params` |
| `2026-07-29 04:19:03` | `cowrie.command.input` |
| `2026-07-29 04:19:03` | `cowrie.command.input` |
| `2026-07-29 04:19:03` | `cowrie.command.input` |
| `2026-07-29 04:19:03` | `cowrie.command.input` |
| `2026-07-29 04:19:03` | `cowrie.command.input` |
| `2026-07-29 04:19:03` | `cowrie.command.success` |
| `2026-07-29 04:19:03` | `cowrie.command.input` |
| `2026-07-29 04:19:03` | `cowrie.command.input` |
| `2026-07-29 04:19:03` | `cowrie.command.input` |
| `2026-07-29 04:19:03` | `cowrie.command.input` |
| `2026-07-29 04:19:03` | `cowrie.log.closed` |
| `2026-07-29 04:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f13773720a1e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-29 04:22 |
| **Last Seen** | 2026-07-29 04:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:22:36` | `cowrie.session.connect` |
| `2026-07-29 04:22:36` | `cowrie.client.version` |
| `2026-07-29 04:22:36` | `cowrie.client.kex` |
| `2026-07-29 04:22:36` | `cowrie.login.success` |
| `2026-07-29 04:22:37` | `cowrie.session.params` |
| `2026-07-29 04:22:37` | `cowrie.command.input` |
| `2026-07-29 04:22:37` | `cowrie.command.input` |
| `2026-07-29 04:22:37` | `cowrie.command.input` |
| `2026-07-29 04:22:37` | `cowrie.command.input` |
| `2026-07-29 04:22:37` | `cowrie.command.input` |
| `2026-07-29 04:22:37` | `cowrie.command.success` |
| `2026-07-29 04:22:37` | `cowrie.command.input` |
| `2026-07-29 04:22:37` | `cowrie.command.input` |
| `2026-07-29 04:22:37` | `cowrie.command.input` |
| `2026-07-29 04:22:37` | `cowrie.command.input` |
| `2026-07-29 04:22:37` | `cowrie.log.closed` |
| `2026-07-29 04:22:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be9b2b1bc406

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-07-29 04:29 |
| **Last Seen** | 2026-07-29 04:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:29:51` | `cowrie.session.connect` |
| `2026-07-29 04:29:51` | `cowrie.client.version` |
| `2026-07-29 04:29:51` | `cowrie.client.kex` |
| `2026-07-29 04:29:52` | `cowrie.login.success` |
| `2026-07-29 04:29:52` | `cowrie.direct-tcpip.request` |
| `2026-07-29 04:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c8baf670cb9

| Field | Detail |
|---|---|
| **Source IP** | `103.84.236[.]222` |
| **First Seen** | 2026-07-29 04:29 |
| **Last Seen** | 2026-07-29 04:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:29:52` | `cowrie.session.connect` |
| `2026-07-29 04:29:52` | `cowrie.client.version` |
| `2026-07-29 04:29:52` | `cowrie.client.kex` |
| `2026-07-29 04:29:53` | `cowrie.login.success` |
| `2026-07-29 04:29:54` | `cowrie.session.params` |
| `2026-07-29 04:29:54` | `cowrie.command.input` |
| `2026-07-29 04:29:54` | `cowrie.command.failed` |
| `2026-07-29 04:29:55` | `cowrie.log.closed` |
| `2026-07-29 04:29:56` | `cowrie.session.params` |
| `2026-07-29 04:29:56` | `cowrie.command.input` |
| `2026-07-29 04:29:56` | `cowrie.session.file_download` |
| `2026-07-29 04:29:56` | `cowrie.log.closed` |
| `2026-07-29 04:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.84.236[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.84.236[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffd57b17838c

| Field | Detail |
|---|---|
| **Source IP** | `103.84.236[.]222` |
| **First Seen** | 2026-07-29 04:29 |
| **Last Seen** | 2026-07-29 04:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:29:56` | `cowrie.session.connect` |
| `2026-07-29 04:29:56` | `cowrie.client.version` |
| `2026-07-29 04:29:57` | `cowrie.client.kex` |
| `2026-07-29 04:29:58` | `cowrie.login.success` |
| `2026-07-29 04:29:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.84.236[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.84.236[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60fe54f629d2

| Field | Detail |
|---|---|
| **Source IP** | `103.84.236[.]222` |
| **First Seen** | 2026-07-29 04:29 |
| **Last Seen** | 2026-07-29 04:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:29:58` | `cowrie.session.connect` |
| `2026-07-29 04:29:58` | `cowrie.client.version` |
| `2026-07-29 04:29:59` | `cowrie.client.kex` |
| `2026-07-29 04:30:00` | `cowrie.login.success` |
| `2026-07-29 04:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.84.236[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.84.236[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c9d6e0b4aa8

| Field | Detail |
|---|---|
| **Source IP** | `65.20.131[.]63` |
| **First Seen** | 2026-07-29 04:30 |
| **Last Seen** | 2026-07-29 04:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:30:01` | `cowrie.session.connect` |
| `2026-07-29 04:30:02` | `cowrie.client.version` |
| `2026-07-29 04:30:02` | `cowrie.client.kex` |
| `2026-07-29 04:30:03` | `cowrie.login.success` |
| `2026-07-29 04:30:04` | `cowrie.direct-tcpip.request` |
| `2026-07-29 04:30:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.131[.]63` to AbuseIPDB if not already reported
- [ ] Block `65.20.131[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13ccb0804bb3

| Field | Detail |
|---|---|
| **Source IP** | `88.84.209[.]146` |
| **First Seen** | 2026-07-29 04:33 |
| **Last Seen** | 2026-07-29 04:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:33:04` | `cowrie.session.connect` |
| `2026-07-29 04:33:05` | `cowrie.client.version` |
| `2026-07-29 04:33:05` | `cowrie.client.kex` |
| `2026-07-29 04:33:06` | `cowrie.login.success` |
| `2026-07-29 04:33:06` | `cowrie.direct-tcpip.request` |
| `2026-07-29 04:33:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.84.209[.]146` to AbuseIPDB if not already reported
- [ ] Block `88.84.209[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bb2198b1435

| Field | Detail |
|---|---|
| **Source IP** | `117.34.210[.]196` |
| **First Seen** | 2026-07-29 04:33 |
| **Last Seen** | 2026-07-29 04:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:33:08` | `cowrie.session.connect` |
| `2026-07-29 04:33:11` | `cowrie.client.version` |
| `2026-07-29 04:33:11` | `cowrie.client.kex` |
| `2026-07-29 04:33:12` | `cowrie.login.success` |
| `2026-07-29 04:33:13` | `cowrie.direct-tcpip.request` |
| `2026-07-29 04:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.34.210[.]196` to AbuseIPDB if not already reported
- [ ] Block `117.34.210[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9680333b5c17

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]235` |
| **First Seen** | 2026-07-29 04:33 |
| **Last Seen** | 2026-07-29 04:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:33:12` | `cowrie.session.connect` |
| `2026-07-29 04:33:13` | `cowrie.client.version` |
| `2026-07-29 04:33:13` | `cowrie.client.kex` |
| `2026-07-29 04:33:15` | `cowrie.login.success` |
| `2026-07-29 04:33:16` | `cowrie.direct-tcpip.request` |
| `2026-07-29 04:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]235` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]235` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c87bdf4a0a0

| Field | Detail |
|---|---|
| **Source IP** | `93.241.232[.]14` |
| **First Seen** | 2026-07-29 04:33 |
| **Last Seen** | 2026-07-29 04:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:33:18` | `cowrie.session.connect` |
| `2026-07-29 04:33:19` | `cowrie.client.version` |
| `2026-07-29 04:33:19` | `cowrie.client.kex` |
| `2026-07-29 04:33:19` | `cowrie.login.success` |
| `2026-07-29 04:33:19` | `cowrie.direct-tcpip.request` |
| `2026-07-29 04:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.241.232[.]14` to AbuseIPDB if not already reported
- [ ] Block `93.241.232[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64ad4de95a0d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-29 04:35 |
| **Last Seen** | 2026-07-29 04:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:35:58` | `cowrie.session.connect` |
| `2026-07-29 04:35:58` | `cowrie.client.version` |
| `2026-07-29 04:35:58` | `cowrie.client.kex` |
| `2026-07-29 04:35:58` | `cowrie.login.success` |
| `2026-07-29 04:35:59` | `cowrie.direct-tcpip.request` |
| `2026-07-29 04:35:59` | `cowrie.direct-tcpip.data` |
| `2026-07-29 04:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9f4e5e9aee9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]18` |
| **First Seen** | 2026-07-29 04:48 |
| **Last Seen** | 2026-07-29 04:49 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo WRITABLE >/tmp/.testfile 2>&1, ls -l /tmp/.testfile 2>&1, rm -f /tmp/.testfile, cd /tmp, for pid in /proc/[0-9]*; do pid_num="${pid##*/}"; if [ -r "$pid/maps" ]; then suspicious=true; while IFS= read -r line; do case "$line" in *"/lib/"*|*"/lib64/"*|*".so"*) suspicious=false; break;; esac; done < "$pid/maps"; if [ "$suspicious" = true ]; then kill -9 "$pid_num" 2>/dev/null; fi; fi; done;` |
| **Download Attempts** | hxxp://91.199.133[.]133:8080/deploy.sh, hxxp://91.199.133[.]133:8080/deploy.sh, b5147693ed4a8744cd3c32e2a2b8c6ec77acc6c8f0494b994398161a0ba009c5 |
| **Malware Analysis** | 0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7 (LOW) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1489 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:48:10` | `cowrie.session.connect` |
| `2026-07-29 04:48:12` | `cowrie.login.success` |
| `2026-07-29 04:48:12` | `cowrie.session.params` |
| `2026-07-29 04:48:13` | `cowrie.command.input` |
| `2026-07-29 04:48:14` | `cowrie.command.input` |
| `2026-07-29 04:48:14` | `cowrie.command.input` |
| `2026-07-29 04:48:14` | `cowrie.command.input` |
| `2026-07-29 04:48:15` | `cowrie.command.input` |
| `2026-07-29 04:48:15` | `cowrie.command.input` |
| `2026-07-29 04:48:16` | `cowrie.command.input` |
| `2026-07-29 04:48:16` | `cowrie.command.failed` |
| `2026-07-29 04:48:16` | `cowrie.command.failed` |
| `2026-07-29 04:48:16` | `cowrie.command.failed` |
| `2026-07-29 04:48:16` | `cowrie.command.failed` |
| `2026-07-29 04:48:16` | `cowrie.command.failed` |
| `2026-07-29 04:48:16` | `cowrie.command.failed` |
| `2026-07-29 04:48:16` | `cowrie.command.failed` |
| `2026-07-29 04:48:16` | `cowrie.command.failed` |
| `2026-07-29 04:48:16` | `cowrie.command.failed` |
| `2026-07-29 04:48:16` | `cowrie.command.failed` |
| `2026-07-29 04:48:16` | `cowrie.command.input` |
| `2026-07-29 04:48:16` | `cowrie.command.input` |
| `2026-07-29 04:48:16` | `cowrie.command.input` |
| `2026-07-29 04:48:16` | `cowrie.command.input` |
| `2026-07-29 04:48:16` | `cowrie.command.input` |
| `2026-07-29 04:48:16` | `cowrie.command.input` |
| `2026-07-29 04:48:16` | `cowrie.command.input` |
| `2026-07-29 04:48:16` | `cowrie.command.input` |
| `2026-07-29 04:48:16` | `cowrie.session.file_download` |
| `2026-07-29 04:48:16` | `cowrie.session.file_download` |
| `2026-07-29 04:48:16` | `cowrie.session.file_download.failed` |
| `2026-07-29 04:48:36` | `cowrie.command.input` |
| `2026-07-29 04:48:38` | `cowrie.command.input` |
| `2026-07-29 04:48:39` | `cowrie.command.input` |
| `2026-07-29 04:48:39` | `cowrie.command.input` |
| `2026-07-29 04:48:39` | `cowrie.command.input` |
| `2026-07-29 04:48:39` | `cowrie.command.input` |
| `2026-07-29 04:48:39` | `cowrie.command.input` |
| `2026-07-29 04:48:39` | `cowrie.command.input` |
| `2026-07-29 04:48:39` | `cowrie.command.input` |
| `2026-07-29 04:48:39` | `cowrie.command.input` |
| `2026-07-29 04:48:39` | `cowrie.command.input` |
| `2026-07-29 04:48:39` | `cowrie.command.failed` |
| `2026-07-29 04:48:39` | `cowrie.command.failed` |
| `2026-07-29 04:48:39` | `cowrie.command.failed` |
| `2026-07-29 04:48:39` | `cowrie.command.failed` |
| `2026-07-29 04:49:04` | `cowrie.session.input` |
| `2026-07-29 04:49:06` | `cowrie.session.file_download` |
| `2026-07-29 04:49:06` | `cowrie.session.file_download` |
| `2026-07-29 04:49:06` | `cowrie.log.closed` |
| `2026-07-29 04:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]18` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f7b6f2f220e

| Field | Detail |
|---|---|
| **Source IP** | `120.48.144[.]5` |
| **First Seen** | 2026-07-29 04:48 |
| **Last Seen** | 2026-07-29 04:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:48:25` | `cowrie.session.connect` |
| `2026-07-29 04:48:26` | `cowrie.telnet.option` |
| `2026-07-29 04:50:01` | `cowrie.telnet.option` |
| `2026-07-29 04:50:01` | `cowrie.login.success` |
| `2026-07-29 04:50:01` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `120.48.144[.]5` to AbuseIPDB if not already reported
- [ ] Block `120.48.144[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-404ace505f56

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]179` |
| **First Seen** | 2026-07-29 04:54 |
| **Last Seen** | 2026-07-29 04:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:54:09` | `cowrie.session.connect` |
| `2026-07-29 04:54:09` | `cowrie.client.version` |
| `2026-07-29 04:54:09` | `cowrie.client.kex` |
| `2026-07-29 04:54:12` | `cowrie.login.success` |
| `2026-07-29 04:54:12` | `cowrie.direct-tcpip.request` |
| `2026-07-29 04:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]179` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-198e84a5e90c

| Field | Detail |
|---|---|
| **Source IP** | `175.198.18[.]3` |
| **First Seen** | 2026-07-29 04:54 |
| **Last Seen** | 2026-07-29 04:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 04:54:18` | `cowrie.session.connect` |
| `2026-07-29 04:54:18` | `cowrie.client.version` |
| `2026-07-29 04:54:18` | `cowrie.client.kex` |
| `2026-07-29 04:54:21` | `cowrie.login.success` |
| `2026-07-29 04:54:22` | `cowrie.direct-tcpip.request` |
| `2026-07-29 04:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.198.18[.]3` to AbuseIPDB if not already reported
- [ ] Block `175.198.18[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **57** | 2026-07-29 01:05 | 2026-07-29 04:53 | 49m | 0 | `T1592` | 🟠 MEDIUM |
| `34.156.227[.]119` | **30** | 2026-07-29 03:17 | 2026-07-29 03:17 | 1m | 0 | `T1592` | 🟠 MEDIUM |
| `35.195.127[.]65` | **30** | 2026-07-29 02:32 | 2026-07-29 02:32 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `35.195.144[.]153` | **30** | 2026-07-29 02:46 | 2026-07-29 02:46 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-29 01:18 | 2026-07-29 04:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]165` | **6** | 2026-07-29 00:59 | 2026-07-29 01:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **6** | 2026-07-29 03:13 | 2026-07-29 03:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]106` | **5** | 2026-07-29 03:52 | 2026-07-29 03:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | **5** | 2026-07-29 01:13 | 2026-07-29 01:59 | 1m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `132.148.30[.]167` | **3** | 2026-07-29 02:10 | 2026-07-29 04:18 | 1m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-07-29 04:42 | 2026-07-29 04:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]209` | **3** | 2026-07-29 03:52 | 2026-07-29 03:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]164` | **3** | 2026-07-29 03:53 | 2026-07-29 03:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]121` | **3** | 2026-07-29 02:24 | 2026-07-29 02:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.48.96[.]161` | **2** | 2026-07-29 04:46 | 2026-07-29 04:48 | 2m | 0 | `T1592` | 🟢 LOW |
| `20.127.195[.]188` | **2** | 2026-07-29 02:54 | 2026-07-29 02:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | **2** | 2026-07-29 03:03 | 2026-07-29 03:22 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.81[.]213` | 1 | 2026-07-29 03:46 | 2026-07-29 03:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.21.105[.]250` | 1 | 2026-07-29 03:47 | 2026-07-29 03:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.20.223[.]26` | 1 | 2026-07-29 04:40 | 2026-07-29 04:40 | 13s | 0 | `T1592` | 🟢 LOW |
| `118.123.116[.]93` | 1 | 2026-07-29 00:57 | 2026-07-29 00:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.148.49[.]82` | 1 | 2026-07-29 01:37 | 2026-07-29 01:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.66.124[.]149` | 1 | 2026-07-29 01:46 | 2026-07-29 01:46 | 2s | 0 | `T1592` | 🟢 LOW |
| `125.227.91[.]167` | 1 | 2026-07-29 00:56 | 2026-07-29 00:56 | 30s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]235` | 1 | 2026-07-29 03:11 | 2026-07-29 03:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `166.62.102[.]109` | 1 | 2026-07-29 02:24 | 2026-07-29 02:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `166.62.102[.]109` | 1 | 2026-07-29 04:32 | 2026-07-29 04:33 | 57s | 0 | `T1592` | 🟢 LOW |
| `168.228.151[.]76` | 1 | 2026-07-29 04:33 | 2026-07-29 04:34 | 14s | 0 | `T1592` | 🟢 LOW |
| `171.231.177[.]152` | 1 | 2026-07-29 00:56 | 2026-07-29 00:57 | 67s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-07-29 03:50 | 2026-07-29 03:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]211` | 1 | 2026-07-29 02:48 | 2026-07-29 02:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]225` | 1 | 2026-07-29 04:17 | 2026-07-29 04:17 | 10s | 0 | `T1592` | 🟢 LOW |
| `194.50.235[.]140` | 1 | 2026-07-29 04:17 | 2026-07-29 04:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.73.75[.]82` | 1 | 2026-07-29 01:42 | 2026-07-29 01:42 | 5s | 0 | `T1592` | 🟢 LOW |
| `213.5.196[.]164` | 1 | 2026-07-29 01:15 | 2026-07-29 01:16 | 13s | 0 | `T1592` | 🟢 LOW |
| `31.76.20[.]19` | 1 | 2026-07-29 03:11 | 2026-07-29 03:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-07-29 04:03 | 2026-07-29 04:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.194.67[.]29` | 1 | 2026-07-29 04:07 | 2026-07-29 04:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.194.89[.]44` | 1 | 2026-07-29 02:40 | 2026-07-29 02:40 | 6s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-07-29 01:41 | 2026-07-29 01:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.175.134[.]187` | 1 | 2026-07-29 03:44 | 2026-07-29 03:44 | 14s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]40` | 1 | 2026-07-29 03:19 | 2026-07-29 03:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `54.90.159[.]174` | 1 | 2026-07-29 01:13 | 2026-07-29 01:13 | 1s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]48` | 1 | 2026-07-29 03:56 | 2026-07-29 03:56 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]205` | 1 | 2026-07-29 01:47 | 2026-07-29 01:48 | 16s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-29 03:14 | 2026-07-29 03:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.48.30[.]162` | 1 | 2026-07-29 02:54 | 2026-07-29 02:54 | 31s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]179` | 1 | 2026-07-29 02:09 | 2026-07-29 02:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.37.172[.]132` | 1 | 2026-07-29 02:09 | 2026-07-29 02:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.37.172[.]137` | 1 | 2026-07-29 02:47 | 2026-07-29 02:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]18` | 1 | 2026-07-29 03:01 | 2026-07-29 03:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.253.236[.]73` | 1 | 2026-07-29 04:01 | 2026-07-29 04:02 | 12s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]144` | 1 | 2026-07-29 01:07 | 2026-07-29 01:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]92` | 1 | 2026-07-29 01:45 | 2026-07-29 01:45 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
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
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |

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
| `151.243.11[.]235` | DE | LLC VASH KREDIT BANK | **100** ⚠️ | 24 |
| `112.197.2[.]116` | VN | Asia Pacific Network Information Centre | **100** ⚠️ | 45 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `171.231.177[.]152` | VN | Viettel Group | **100** ⚠️ | 1 |
| `120.48.96[.]161` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 6 |
| `168.228.151[.]76` | BR | INTEGRATO TELECOMUNICAÇÕES LTDA - ME | **100** ⚠️ | 4 |
| `193.32.162[.]15` | RO | UNMANAGED LTD | **100** ⚠️ | 19 |
| `86.48.30[.]162` | US | Contabo GmbH | **100** ⚠️ | 1 |
| `34.156.227[.]119` | BE | Google LLC | **100** ⚠️ | 1 |
| `46.175.134[.]187` | GE | LTD NETSERVICE | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 327 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 318 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 205 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 205 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 203 |

---

## 🔕 False Positive Summary (36 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 23 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 590 cases |
| Tool 34  | Credential Extractor        | ✅ 349 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 10 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 161 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 36 filtered (6.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 95 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 318 priority case(s) shown individually · 54 recon entry/entries in table (17 group(s) consolidating 199 session(s)).

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
_Report time: 2026-07-29T06:36:43Z_

